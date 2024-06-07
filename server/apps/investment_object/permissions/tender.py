import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_tender', always_true)
rules.set_perm('investment_object.add_tender', always_true)
rules.set_perm('investment_object.change_tender', always_true)
rules.set_perm('investment_object.delete_tender', always_true)
rules.set_perm('investment_object.list_tender', always_true)
