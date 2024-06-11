from server.apps.personal_cabinet.models import SelectionRequest


def formation_context(selection_request: SelectionRequest) -> None:
    """Формирование предложений и мер поддержки."""
    report_context = report.context

    if report_context.get('context_for_file').get('offers_and_wishes'):
        return

    supports = ''
    offers = ''
    offers_and_wishes= ''

    for en_index, support in enumerate(Support.objects.filter(tags__in=report.tags.all(), is_actual=True)[0:2]):  # noqa: E501
        supports += (
            f'Мера поддержки № {en_index + 1}:\a' +
            f"Название: {support.title}\a" +
            f"Сумма субсидий: {support.amount}\a" +
            f"Подробнее: {support.site}\a\a"
        )

    for en_index, offer in enumerate(Offer.objects.filter(tags__in=report.tags.all())[0:2]):  # noqa: E501
        offers += (
            f'Партнерское предложение № {en_index + 1}:\a' +
            f"Название: {offer.title}\a" +
            f"Процентная ставка: {offer.interest_rate}\a" +
            f"Срок займа: {offer.loan_term}\a" +
            f"Сумма займа: {offer.amount}\a" +
            f"Подробнее: {offer.site}\a\a"
        )
    if supports:
        offers_and_wishes += (
            'Меры по поддержке промышленных предприятий:\a' +
            supports + '\a\a'
        )
    if offers:
        offers_and_wishes += (
            'Партнерские предложения по инвестированию:\a' +
            offers + '\a\a'
        )
    report_context.get('context_for_file').update(
        {'offers_and_wishes': offers_and_wishes},
    )

    report.context = report_context
    report.save()
