import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_transactionform', always_true)
rules.set_perm('investment_object.list_transactionform', always_true)
