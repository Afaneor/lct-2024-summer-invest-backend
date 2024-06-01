import rules
from rules.predicates import always_true

rules.set_perm('hincal.view_subsector', always_true)
rules.set_perm('hincal.add_subsector', always_true)
rules.set_perm('hincal.change_subsector', always_true)
rules.set_perm('hincal.delete_subsector', always_true)
rules.set_perm('hincal.list_subsector', always_true)
