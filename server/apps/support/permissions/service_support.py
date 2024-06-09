import rules
from rules.predicates import always_true

rules.set_perm('support.view_servicesupport', always_true)
rules.set_perm('support.add_servicesupport', always_true)
rules.set_perm('support.change_servicesupport', always_true)
rules.set_perm('support.delete_servicesupport', always_true)
rules.set_perm('support.list_servicesupport', always_true)
