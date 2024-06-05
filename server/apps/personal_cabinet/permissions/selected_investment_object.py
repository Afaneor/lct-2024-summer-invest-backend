import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_selectedinvestmentobject', always_true)
rules.set_perm('personal_cabinet.add_selectedinvestmentobject', always_true)
rules.set_perm('personal_cabinet.change_selectedinvestmentobject', always_true)
rules.set_perm('personal_cabinet.delete_selectedinvestmentobject', always_true)
rules.set_perm('personal_cabinet.list_selectedinvestmentobject', always_true)
