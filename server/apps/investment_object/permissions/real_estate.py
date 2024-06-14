import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_realestate', always_true)
rules.set_perm('investment_object.list_realestate', always_true)
