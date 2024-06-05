from server.apps.personal_cabinet.api.views.business import BusinessViewSet
from server.apps.personal_cabinet.api.views.message import MessageViewSet
from server.apps.personal_cabinet.api.views.sector import SectorViewSet
from server.apps.personal_cabinet.api.views.selected_investment_object import (
    SelectedInvestmentObjectViewSet,
)
from server.apps.personal_cabinet.api.views.selection_request import (
    SelectionRequestViewSet,
)
from server.apps.personal_cabinet.api.views.sub_sector import SubSectorViewSet
from server.apps.personal_cabinet.api.views.territorial_location import (
    TerritorialLocationViewSet,
)

__all__ = [
    'BusinessViewSet',
    'MessageViewSet',
    'SectorViewSet',
    'SelectedInvestmentObjectViewSet',
    'SelectionRequestViewSet',
    'SubSectorViewSet',
    'TerritorialLocationViewSet',
]
