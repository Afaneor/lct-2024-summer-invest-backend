import rules
from rules.predicates import always_true

rules.set_perm('hincal.view_archive', always_true)
rules.set_perm('hincal.add_archive', always_true)
rules.set_perm('hincal.change_archive', always_true)
rules.set_perm('hincal.delete_archive', always_true)
rules.set_perm('hincal.list_archive', always_true)
