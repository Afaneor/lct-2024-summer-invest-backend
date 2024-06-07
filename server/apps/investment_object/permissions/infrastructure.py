import rules
from rules.predicates import always_true

rules.set_perm('investment_object.view_infrastructure', always_true)
rules.set_perm('investment_object.add_infrastructure', always_true)
rules.set_perm('investment_object.change_infrastructure', always_true)
rules.set_perm('investment_object.delete_infrastructure', always_true)
rules.set_perm('investment_object.list_infrastructure', always_true)
