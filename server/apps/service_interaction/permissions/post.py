import rules
from rules.predicates import is_authenticated

rules.set_perm('service_interaction.view_post', is_authenticated)
rules.set_perm('service_interaction.add_post', is_authenticated)
rules.set_perm('service_interaction.list_post', is_authenticated)
