import rules
from rules.predicates import always_true

rules.set_perm('service_support.view_servicesupport', always_true)
rules.set_perm('service_support.add_servicesupport', always_true)
rules.set_perm('service_support.change_servicesupport', always_true)
rules.set_perm('service_support.delete_servicesupport', always_true)
rules.set_perm('service_support.list_servicesupport', always_true)
