from django.urls import path
from graphene_django.views import GraphQLView
from APIg.schema import schema
from django.contrib.auth.decorators import login_required

from . import views

app_name = 'APIg'

urlpatterns = [
    # Only a single URL to access GraphQL
    path("graphql", login_required(GraphQLView.as_view(graphiql=True, schema=schema)), name='graphql'),
    path('', views.index, name='index'),
]