import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_business', always_true)
rules.set_perm('personal_cabinet.add_business', always_true)
rules.set_perm('personal_cabinet.change_business', always_true)
rules.set_perm('personal_cabinet.delete_business', always_true)
rules.set_perm('personal_cabinet.list_business', always_true)
