import rules
from rules.predicates import always_true

rules.set_perm('service_interaction.view_topic', always_true)
rules.set_perm('service_interaction.list_topic', always_true)
