import rules
from rules.predicates import always_true

rules.set_perm('service_interaction.view_feedback', always_true)
rules.set_perm('service_interaction.add_feedback', always_true)
rules.set_perm('service_interaction.change_feedback', always_true)
rules.set_perm('service_interaction.delete_feedback', always_true)
rules.set_perm('service_interaction.list_feedback', always_true)
