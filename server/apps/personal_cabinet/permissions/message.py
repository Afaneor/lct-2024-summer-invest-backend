import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_message', always_true)
rules.set_perm('personal_cabinet.add_message', always_true)
rules.set_perm('personal_cabinet.list_message', always_true)
