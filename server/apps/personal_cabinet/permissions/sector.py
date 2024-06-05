import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_sector', always_true)
rules.set_perm('personal_cabinet.add_sector', always_true)
rules.set_perm('personal_cabinet.change_sector', always_true)
rules.set_perm('personal_cabinet.delete_sector', always_true)
rules.set_perm('personal_cabinet.list_sector', always_true)
