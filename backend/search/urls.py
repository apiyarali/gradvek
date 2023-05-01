from .views import (
    CountAllView,
    GetActions,
    Datasets,
    GetAdverseEventTargetPath,
    GetGwas,
    GetHGene,
    GetHProtein,
    GetIntact,
    GetPathway,
    GetReactome,
    GetSignor,
    GetTargetAdverseEventPath,
    RoutesListAPIView,
    CountView,
    GetAdverseEventByTargetView,
    GetPheno,
    SuggestHintView,

)
from django.urls import path

from . import views


app_name = "search"


urlpatterns = [

    path('api/pheno/<str:target>/', GetPheno.as_view(), name='pheno'),
    path('api/gwas/<str:target>/', GetGwas.as_view(), name='gwas'),
    path('api/hgene/<str:target>/', GetHGene.as_view(), name='hgene'),
    path('api/hprotein/<str:target>/', GetHProtein.as_view(), name='hprotein'),
    path('api/intact/<str:target>/', GetIntact.as_view(), name='intact'),
    path('api/pathway/<str:target>/', GetPathway.as_view(), name='pathway'),
    path('api/reactome/<str:target>/', GetReactome.as_view(), name='reactome'),
    path('api/signor/<str:target>/', GetSignor.as_view(), name='signor'),

    # Return the list of routes in the Django site
    path('api/routes/', RoutesListAPIView.as_view(), name='api-routes-list'),
    
    # Return an array of actions for the specified target
    path("api/actions/", GetActions.as_view(), name='get_actions'),
    path('api/actions/<str:target>/', GetActions.as_view(), name='get_actions_target'),


    path("api/descriptors", views.DescriptorListView.as_view(), name="descriptors"),

    # Trying to copy paths from gradvek 1.0

    # Upload one or more entities in a comma-separated file
    path('api/csv/', views.upload_csv, name='upload_csv'),

    # Return the content of a previously uploaded comma-separated file
    path('api/csv/<str:file_id>/', views.get_csv, name='get_csv'),

    # Clear out the database
    path('api/clear/', views.clear, name='clear'),

    # Initialize entities (all or of the specified type) from the OpenTargets store
    path('api/init/', views.init_type, name='init_all'),
    path('api/init/<str:type_string>/', views.init_type, name='init_type'),

    # Add a single gene entity to the database
    path('api/gene/<str:id>/', views.gene, name='gene'),

    # GET: Return an array of all known datasets (both active and inactive)
    # POST: Modify the active status of one or more datasets
    path('api/datasets/', Datasets.as_view(), name='datasets'),

    # This route returns an array of adverse events associated with a specific target, optionally filtered by action types. It requires the drug target symbol as a path parameter
    # target: Drug Symbol
    path('api/weight/<str:target>/', GetAdverseEventByTargetView.as_view(), name='get_adverse_event'),

    # This route returns an array of weights (log likelihood ratios) of adverse events associated with a specific target, optionally filtered by action types. It requires the drug target symbol and adverse event ID (meddraId) as path parameters.
    # target: Drug Symbol, ae: meddraId
    path('api/weight/<str:target>/<str:ae>/', GetAdverseEventByTargetView.as_view(), name='get_weights_target_ae'),

    # These paths define API routes for querying paths from a target to one or all adverse events
    # associated with it, optionally filtered by drug and action.
    # target: Symbol, ae: meddraId, drug_id: chemblId
    path('api/ae/path/<str:target>/', GetAdverseEventTargetPath.as_view(), name='get_paths_target'),
    path('api/ae/path/<str:target>/<str:ae>/', GetAdverseEventTargetPath.as_view(), name='get_paths_target_ae'),
    path('api/ae/path/<str:target>/<str:ae>/<str:drug_id>/', GetAdverseEventTargetPath.as_view(), name='get_paths_target_ae_drug'),

    # These paths define API routes for querying paths from a adverse event to one or all targets
    # associated with it, optionally filtered by drug and action.
    # ae: meddraId, target: Symbol  drug_id: chemblId
    path('api/target/path/<str:ae>/', GetTargetAdverseEventPath.as_view(), name='get_paths_ae'),
    path('api/target/path/<str:ae>/<str:target>/', GetTargetAdverseEventPath.as_view(), name='get_paths_ae_target'),
    path('api/target/path/<str:ae>/<str:target>/<str:drug_id>/', GetTargetAdverseEventPath.as_view(), name='get_paths_ae_target_drug'),

    # Return an array of Cytoscape entities representing paths from a target to one or all adverse events associated with it, optionally filtered by drug and action
    path('api/count/', CountAllView.as_view(), name='count_all'),
#     path('api/count/', CountView.as_view(), name='count_all'),
    path('api/count/<str:type_string>/', CountView.as_view(), name='count_entity'),

    # Health check
    path('api/info/', views.info, name='info'),

    # Return an array of suggested entities in response to a hint (beginning of the name)
    path('api/suggest/<str:entity_type>/<str:hint>/', SuggestHintView.as_view(), name='suggest_hint'),


    # Return an array of actions for the specified target
    path('api/actions/<str:target>/', views.actions, name='actions_target'),

    # TODO Add some paths for retrieving similarity information?

    # # Trying to copy paths from gradvek 1.0

    # # Upload one or more entities in a comma-separated file
    # path('api/csv/', views.upload_csv, name='upload_csv'),

    # # Return the content of a previously uploaded comma-separated file
    # path('api/csv/<str:file_id>/', views.get_csv, name='get_csv'),

    # # Clear out the database
    path('api/clear/', views.clear, name='clear'),

    # # Initialize entities (all or of the specified type) from the OpenTargets store
    # path('api/init/', views.init_type, name='init_all'),
    # path('api/init/<str:type_string>/', views.init_type, name='init_type'),

    # # Add a single gene entity to the database
    # path('api/gene/<str:id>/', views.gene, name='gene'),

    # # Return an array of all known datasets (both active and inactive)
    # path('api/datasets/', views.datasets, name='datasets'),

    # # Modify the active status of one or more datasets
    # path('api/enable_datasets/', views.enable_datasets, name='enable_datasets'),

    # # Return an array of adverse events associated with a specific target, optionally filtered by action
    # path('api/weight/<str:target>/', views.get_adverse_event, name='get_adverse_event'),

    # # Return an array of weights of adverse events associated with a specific target, optionally filtered by action
    # path('api/weight/<str:target>/<str:ae>/', views.get_weights_target_ae, name='get_weights_target_ae'),

    # # Return an array of Cytoscape entities representing paths from a target to one or all adverse events associated with it, optionally filtered by drug and action
    # path('api/ae/path/<str:target>/', views.get_paths_target_ae_drug_view, name='get_paths_target_ae'),
    # path('api/ae/path/<str:target>/<str:ae>/', views.get_paths_target_ae_drug_view, name='get_paths_target_ae_ae'),
    # path('api/ae/path/<str:target>/<str:ae>/<str:drug_id>/', views.get_paths_target_ae_drug_view, name='get_paths_target_ae_drug'),

    # # Return an array of Cytoscape entities representing paths from a target to one or all adverse events associated with it, optionally filtered by drug and action
    # path('api/count/<str:type_string>/', views.count, name='count'),

    # # Health check
    # path('api/info/', views.info, name='info'),

    # # Return an array of suggested entities in response to a hint (beginning of the name)
    # path('api/suggest/<str:hint>/', views.suggest_hint, name='suggest_hint'),

    # # Return an array of all actions in the database
    # path('api/actions/', views.actions, name='actions'),

    # # Return an array of actions for the specified target
    # path('api/actions/<str:target>/', views.actions, name='actions_target')

    # # TODO Add some paths for retrieving similarity information?

]
