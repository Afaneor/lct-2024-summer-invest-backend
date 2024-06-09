import rules
from rules.predicates import always_true

rules.set_perm('service_support.view_problemcategory', always_true)
rules.set_perm('service_support.add_problemcategory', always_true)
rules.set_perm('service_support.change_problemcategory', always_true)
rules.set_perm('service_support.delete_problemcategory', always_true)
rules.set_perm('service_support.list_problemcategory', always_true)
