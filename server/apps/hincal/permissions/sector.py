import rules
from rules.predicates import always_true

rules.set_perm('hincal.view_sector', always_true)
rules.set_perm('hincal.add_sector', always_true)
rules.set_perm('hincal.change_sector', always_true)
rules.set_perm('hincal.delete_sector', always_true)
rules.set_perm('hincal.list_sector', always_true)
