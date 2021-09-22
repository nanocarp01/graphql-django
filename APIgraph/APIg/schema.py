import graphene
from graphene_django import DjangoObjectType
from .models import API

class ApisType(DjangoObjectType):
    class Meta:
        model = API
        fields = ("id","legajo", "secretaria", "agente")
    
class Query(graphene.ObjectType):
    all_apis = graphene.List(ApisType)

    def resolve_all_apis(root, info):
        return API.objects.all()
    
schema = graphene.Schema(query=Query)