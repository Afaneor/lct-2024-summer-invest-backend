import rules
from rules.predicates import always_true

rules.set_perm('support.view_offer', always_true)
rules.set_perm('support.list_offer', always_true)
