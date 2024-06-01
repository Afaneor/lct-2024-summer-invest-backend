import rules
from rules.predicates import always_true

rules.set_perm('hincal.view_report', always_true)
rules.set_perm('hincal.add_report', always_true)
rules.set_perm('hincal.change_report', always_true)
rules.set_perm('hincal.delete_report', always_true)
rules.set_perm('hincal.list_report', always_true)
