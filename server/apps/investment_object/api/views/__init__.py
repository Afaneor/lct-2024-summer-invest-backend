from server.apps.investment_object.api.views.economic_activity import (
    EconomicActivityViewSet,
)
from server.apps.investment_object.api.views.infrastructure import (
    InfrastructureViewSet,
)
from server.apps.investment_object.api.views.investment_object import (
    InvestmentObjectViewSet,
)
from server.apps.investment_object.api.views.privilege import PrivilegeViewSet
from server.apps.investment_object.api.views.ready_business import (
    ReadyBusinessViewSet,
)
from server.apps.investment_object.api.views.tender import TenderViewSet
from server.apps.investment_object.api.views.tender_lot import TenderLotViewSet

__all__ = [
    'EconomicActivityViewSet',
    'InfrastructureViewSet',
    'InvestmentObjectViewSet',
    'PrivilegeViewSet',
    'ReadyBusinessViewSet',
    'TenderViewSet',
    'TenderLotViewSet',
]
