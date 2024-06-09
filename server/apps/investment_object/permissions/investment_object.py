import rules
from rules.predicates import always_true, is_superuser

rules.set_perm('investment_object.view_investmentobject', always_true)
rules.set_perm('investment_object.add_investmentobject', always_true)
rules.set_perm('investment_object.change_investmentobject', always_true)
rules.set_perm('investment_object.delete_investmentobject', always_true)
rules.set_perm('investment_object.list_investmentobject', always_true)
rules.set_perm(
    'investment_object.action_is_superuser_investmentobject',
    is_superuser,
)
