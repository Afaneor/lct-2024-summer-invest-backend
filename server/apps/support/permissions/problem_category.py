import rules
from rules.predicates import always_true, is_authenticated

rules.set_perm('support.view_problemcategory', is_authenticated)
rules.set_perm('support.add_problemcategory', is_authenticated)
rules.set_perm('support.change_problemcategory', is_authenticated)
rules.set_perm('support.delete_problemcategory', is_authenticated)
rules.set_perm('support.list_problemcategory', is_authenticated)
