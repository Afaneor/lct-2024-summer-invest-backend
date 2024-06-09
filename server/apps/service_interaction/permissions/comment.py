import rules
from rules.predicates import is_authenticated

rules.set_perm('service_interaction.view_comment', is_authenticated)
rules.set_perm('service_interaction.add_comment', is_authenticated)
rules.set_perm('service_interaction.list_comment', is_authenticated)
