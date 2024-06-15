import rules
from rules.predicates import always_true

rules.set_perm('personal_cabinet.view_subsector', always_true)
rules.set_perm('personal_cabinet.list_subsector', always_true)
