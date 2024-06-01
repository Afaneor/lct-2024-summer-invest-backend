import rules
from rules.predicates import always_true

rules.set_perm('hincal.view_businessindicator', always_true)
rules.set_perm('hincal.add_businessindicator', always_true)
rules.set_perm('hincal.change_businessindicator', always_true)
rules.set_perm('hincal.delete_businessindicator', always_true)
rules.set_perm('hincal.list_businessindicator', always_true)
