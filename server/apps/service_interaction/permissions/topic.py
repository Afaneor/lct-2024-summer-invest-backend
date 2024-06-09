import rules
from rules.predicates import is_authenticated

rules.set_perm('service_interaction.view_topic', is_authenticated)
rules.set_perm('service_interaction.list_topic', is_authenticated)
