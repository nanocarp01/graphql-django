from django.urls import path
from graphene_django.views import GraphQLView
from APIg.schema import schema
from . import views

app_name = 'APIg'

urlpatterns = [
    # Only a single URL to access GraphQL
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema), name='graphql'),

]