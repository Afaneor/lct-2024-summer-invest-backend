import rules
from rules.predicates import always_true, is_authenticated

rules.set_perm('service_interaction.view_event', always_true)
rules.set_perm('service_interaction.add_event', is_authenticated)
rules.set_perm('service_interaction.list_event', always_true)
