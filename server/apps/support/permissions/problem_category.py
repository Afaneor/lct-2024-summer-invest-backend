import rules
from rules.predicates import always_true

rules.set_perm('support.view_problemcategory', always_true)
rules.set_perm('support.list_problemcategory', always_true)
