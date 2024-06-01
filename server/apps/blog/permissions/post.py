import rules
from rules.predicates import always_true

rules.set_perm('blog.view_post', always_true)
rules.set_perm('blog.list_post', always_true)
