import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_subscription', always_true)
rules.set_perm('personal_cabinet.add_subscription', always_true)
rules.set_perm('personal_cabinet.delete_subscription', always_true)
rules.set_perm('personal_cabinet.list_subscription', always_true)
