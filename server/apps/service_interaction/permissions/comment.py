import rules
from rules.predicates import always_true

rules.set_perm('service_interaction.view_comment', always_true)
rules.set_perm('service_interaction.add_comment', always_true)
rules.set_perm('service_interaction.change_comment', always_true)
rules.set_perm('service_interaction.delete_comment', always_true)
rules.set_perm('service_interaction.list_comment', always_true)
