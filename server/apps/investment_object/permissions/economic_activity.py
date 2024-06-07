import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_economicactivity', always_true)
rules.set_perm('investment_object.add_economicactivity', always_true)
rules.set_perm('investment_object.change_economicactivity', always_true)
rules.set_perm('investment_object.delete_economicactivity', always_true)
rules.set_perm('investment_object.list_economicactivity', always_true)
