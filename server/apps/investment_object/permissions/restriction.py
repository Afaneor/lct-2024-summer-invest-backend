import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_restriction', always_true)
rules.set_perm('investment_object.list_restriction', always_true)
