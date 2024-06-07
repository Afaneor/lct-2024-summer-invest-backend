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
from server.apps.investment_object.api.views.real_estate import (
    RealEstateViewSet,
)
from server.apps.investment_object.api.views.restriction import (
    RestrictionViewSet,
)
from server.apps.investment_object.api.views.specialized_site import (
    SpecializedSiteViewSet,
)
from server.apps.investment_object.api.views.tender import TenderViewSet
from server.apps.investment_object.api.views.tender_lot import TenderLotViewSet

__all__ = [
    'EconomicActivityViewSet',
    'InfrastructureViewSet',
    'InvestmentObjectViewSet',
    'PrivilegeViewSet',
    'RealEstateViewSet',
    'RestrictionViewSet',
    'ReadyBusinessViewSet',
    'TenderViewSet',
    'SpecializedSiteViewSet',
    'TenderLotViewSet',
]
