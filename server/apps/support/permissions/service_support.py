import rules
from rules.predicates import always_true

rules.set_perm('support.view_servicesupport', always_true)
rules.set_perm('support.list_servicesupport', always_true)
