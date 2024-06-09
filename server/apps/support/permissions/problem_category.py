import rules
from rules.predicates import always_true

rules.set_perm('service_support.view_serviceproblem', always_true)
rules.set_perm('service_support.add_serviceproblem', always_true)
rules.set_perm('service_support.change_serviceproblem', always_true)
rules.set_perm('service_support.delete_serviceproblem', always_true)
rules.set_perm('service_support.list_serviceproblem', always_true)
