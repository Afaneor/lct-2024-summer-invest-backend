import rules
from rules.predicates import always_true

rules.set_perm('hincal.view_equipment', always_true)
rules.set_perm('hincal.add_equipment', always_true)
rules.set_perm('hincal.change_equipment', always_true)
rules.set_perm('hincal.delete_equipment', always_true)
rules.set_perm('hincal.list_equipment', always_true)
