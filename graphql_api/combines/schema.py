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
# Tenant Resources
from graphql_api.resources.tenant.schema import type_schema \
    as tenant_type_schema
from graphql_api.resources.tenant.schema import input_schema \
    as tenant_input_schema
from graphql_api.resources.tenant.resolvers import tenant
# TenantSetting Resources
from graphql_api.resources.tenant_setting.schema import type_schema \
    as tenant_setting_type_schema
from graphql_api.resources.tenant_setting.schema import input_schema \
    as tenant_setting_input_schema
from graphql_api.resources.tenant_setting.resolvers import tenant_setting
# TenantPlan Resources
from graphql_api.resources.tenant_plan.schema import type_schema \
    as tenant_plan_type_schema
from graphql_api.resources.tenant_plan.schema import input_schema \
    as tenant_plan_input_schema
from graphql_api.resources.tenant_plan.resolvers import tenant_plan
# UserSetting Resources
from graphql_api.resources.user_setting.schema import type_schema \
    as user_setting_type_schema
from graphql_api.resources.user_setting.schema import input_schema \
    as user_setting_input_schema
from graphql_api.resources.user_setting.resolvers import user_setting
# Commons
from graphql_api.resources.core.schema import scalar_schema
from graphql_api.resources.core.scalars import datetime_scalar


# Make schema executable
schema = make_executable_schema([query_type_schema, mutation_type_schema,
                                 plan_type_schema, plan_input_schema,
                                 group_type_schema, group_input_schema,
                                 user_type_schema, user_input_schema,
                                 user_setting_type_schema,
                                 user_setting_input_schema,
                                 tenant_type_schema, tenant_input_schema,
                                 tenant_setting_type_schema,
                                 tenant_setting_input_schema,
                                 tenant_plan_type_schema,
                                 tenant_plan_input_schema, scalar_schema],
                                [query, mutation, plan, group, user,
                                 user_setting, tenant, tenant_setting,
                                 tenant_plan],
                                datetime_scalar)
