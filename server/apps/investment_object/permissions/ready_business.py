import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_readybusiness', always_true)
rules.set_perm('investment_object.list_readybusiness', always_true)
