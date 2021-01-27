from starlette.applications import Starlette
from ariadne.asgi import GraphQL
# Import schema executable
from graphql_api.combines.schema import schema


app = Starlette(debug=True)
app.mount("/graphql", GraphQL(schema, debug=True))
