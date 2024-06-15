import rules
from rules.predicates import is_authenticated

rules.set_perm('personal_cabinet.view_message', is_authenticated)
rules.set_perm('personal_cabinet.add_message', is_authenticated)
rules.set_perm('personal_cabinet.list_message', is_authenticated)
