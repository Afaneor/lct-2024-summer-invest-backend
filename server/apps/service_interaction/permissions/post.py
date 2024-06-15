import rules
from rules.predicates import always_true, is_authenticated

rules.set_perm('service_interaction.view_post', always_true)
rules.set_perm('service_interaction.add_post', is_authenticated)
rules.set_perm('service_interaction.list_post', always_true)
