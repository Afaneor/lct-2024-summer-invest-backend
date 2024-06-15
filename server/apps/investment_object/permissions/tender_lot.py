import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_tenderlot', always_true)
rules.set_perm('investment_object.list_tenderlot', always_true)
