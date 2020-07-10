from ariadne import make_executable_schema
# Query Resources
from graphql_api.resources.query.schema import type_schema as query_type_schema
from graphql_api.resources.query.resolvers import query
# Mutation Resources
from graphql_api.resources.mutation.schema import type_schema \
    as mutation_type_schema
from graphql_api.resources.mutation.resolvers import mutation
# Plan Resources
from graphql_api.resources.plan.schema import type_schema as plan_type_schema
from graphql_api.resources.plan.schema import input_schema as plan_input_schema
from graphql_api.resources.plan.resolvers import plan
# Group Resources
from graphql_api.resources.group.schema import type_schema as group_type_schema
from graphql_api.resources.group.schema import input_schema \
    as group_input_schema
from graphql_api.resources.group.resolvers import group
# User Resources
from graphql_api.resources.user.schema import type_schema \
    as user_type_schema
from graphql_api.resources.user.schema import input_schema \
    as user_input_schema
from graphql_api.resources.user.resolvers import user
# UserPlan Resources
from graphql_api.resources.user_plan.schema import type_schema \
    as user_plan_type_schema
from graphql_api.resources.user_plan.schema import input_schema \
    as user_plan_input_schema
from graphql_api.resources.user_plan.resolvers import user_plan
# Setting Resources
from graphql_api.resources.setting.schema import type_schema \
    as setting_type_schema
from graphql_api.resources.setting.schema import input_schema \
    as setting_input_schema
from graphql_api.resources.setting.resolvers import setting
# Commons
from graphql_api.resources.core.schema import scalar_schema
from graphql_api.resources.core.scalars import datetime_scalar


# Make schema executable
schema = make_executable_schema([query_type_schema, mutation_type_schema,
                                 plan_type_schema, plan_input_schema,
                                 group_type_schema, group_input_schema,
                                 user_type_schema, user_input_schema,
                                 user_plan_type_schema, user_plan_input_schema,
                                 scalar_schema, setting_type_schema,
                                 setting_input_schema],
                                [query, mutation, plan, group, user, user_plan,
                                 setting],
                                datetime_scalar)