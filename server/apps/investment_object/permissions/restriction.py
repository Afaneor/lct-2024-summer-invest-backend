import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_restriction', always_true)
rules.set_perm('investment_object.add_restriction', always_true)
rules.set_perm('investment_object.change_restriction', always_true)
rules.set_perm('investment_object.delete_restriction', always_true)
rules.set_perm('investment_object.list_restriction', always_true)
