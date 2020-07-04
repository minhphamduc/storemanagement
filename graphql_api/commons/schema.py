import os
from ariadne import load_schema_from_path


# Load schema from graphql folder
dir_path = os.path.dirname(os.path.realpath(__file__))
scalar_schema = load_schema_from_path("%s/graphql/scalars.graphql" % dir_path)
