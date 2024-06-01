import rules
from rules.predicates import always_true

rules.set_perm('support.view_support', always_true)
rules.set_perm('support.list_support', always_true)
