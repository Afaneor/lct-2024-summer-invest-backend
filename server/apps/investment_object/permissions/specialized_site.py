import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_specializedsite', always_true)
rules.set_perm('investment_object.list_specializedsite', always_true)
