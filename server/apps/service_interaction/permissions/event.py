import rules
from rules.predicates import always_true, is_superuser

rules.set_perm('service_interaction.view_event', always_true)
rules.set_perm('service_interaction.add_event', is_superuser)
rules.set_perm('service_interaction.list_event', always_true)
