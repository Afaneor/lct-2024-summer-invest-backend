import rules
from rules.predicates import is_authenticated

rules.set_perm('personal_cabinet.view_business', is_authenticated)
rules.set_perm('personal_cabinet.add_business', is_authenticated)
rules.set_perm('personal_cabinet.change_business', is_authenticated)
rules.set_perm('personal_cabinet.delete_business', is_authenticated)
rules.set_perm('personal_cabinet.list_business', is_authenticated)
