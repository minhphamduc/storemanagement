from ariadne import make_executable_schema
# Import sdl
from graphql_api.resources.query.schema import type_schema as query_type_schema
from graphql_api.resources.mutation.schema import type_schema \
    as mutation_type_schema
from graphql_api.resources.plan.schema import type_schema as plan_type_schema
from graphql_api.resources.plan.schema import input_schema as plan_input_schema
from graphql_api.resources.group.schema import type_schema as group_type_schema
from graphql_api.resources.group.schema import input_schema \
    as group_input_schema
from graphql_api.resources.user.schema import type_schema \
    as user_type_schema
from graphql_api.resources.user.schema import input_schema \
    as user_input_schema
from graphql_api.resources.user_plan.schema import type_schema \
    as user_plan_type_schema
from graphql_api.resources.user_plan.schema import input_schema \
    as user_plan_input_schema
from graphql_api.resources.user_plan.schema import scalar_schema \
    as user_plan_scalar_schema
from graphql_api.resources.setting.schema import type_schema \
    as setting_type_schema
from graphql_api.resources.setting.schema import input_schema \
    as setting_input_schema
# Import resolver
from graphql_api.resources.query.resolvers import query
from graphql_api.resources.mutation.resolvers import mutation
from graphql_api.resources.plan.resolvers import plan
from graphql_api.resources.group.resolvers import group
from graphql_api.resources.user.resolvers import user
from graphql_api.resources.user_plan.resolvers import user_plan
from graphql_api.resources.setting.resolvers import setting
# Import scalar
from graphql_api.resources.user_plan.scalars import datetime_scalar \
    as user_plan_datetime_scalar


# Make schema executable
schema = make_executable_schema([query_type_schema, mutation_type_schema,
                                 plan_type_schema, plan_input_schema,
                                 group_type_schema, group_input_schema,
                                 user_type_schema, user_input_schema,
                                 user_plan_type_schema, user_plan_input_schema,
                                 user_plan_scalar_schema, setting_type_schema,
                                 setting_input_schema],
                                [query, mutation, plan, group, user, user_plan,
                                 setting],
                                user_plan_datetime_scalar)
