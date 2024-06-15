import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_privilege', always_true)
rules.set_perm('investment_object.list_privilege', always_true)
