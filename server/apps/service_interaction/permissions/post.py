import rules
from rules.predicates import always_true

rules.set_perm('service_interaction.view_post', always_true)
rules.set_perm('service_interaction.add_post', always_true)
rules.set_perm('service_interaction.change_post', always_true)
rules.set_perm('service_interaction.delete_post', always_true)
rules.set_perm('service_interaction.list_post', always_true)
