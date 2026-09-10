from django.urls import path
from .views import (
    UtilisateurListAPI,
    UtilisateurDetailAPI,
    CultureListAPIView,
    CultureDetailAPIView,
    ExploitationListAPIView,
    ExploitationDetailAPIView,
    ParcelleListAPIView,
    ParcelleDetailAPIView,
    DiagnosticListAPIView,
    DiagnosticDetailAPIView,
    MaladieListAPIView,
    MaladieDetailAPIView,
    RecommandationListAPIView,
    ResultatDiagnosticDetailAPIView,
    ResultatDiagnosticListAPIView,
    RecommandationDetailAPIView,
)
from .tomato_views import (
    AgentCasAPIView,
    AnalyseDiagnosticAPIView,
    ConnexionAPIView,
    ConseilsAPIView,
    GalerieMaladiesAPIView,
    MarcheDetailAPIView,
    MarcheListAPIView,
    PrevisionMeteoDetailAPIView,
    PrevisionMeteoListAPIView,
    PrixDetailAPIView,
    PrixListAPIView,
    SanteAPIView,
    ZoneMeteoDetailAPIView,
    ZoneMeteoListAPIView,
)

urlpatterns = [
    path('sante/', SanteAPIView.as_view(), name='sante'),
    path('auth/connexion/', ConnexionAPIView.as_view(), name='connexion'),
    path(
        'diagnostics/analyse/',
        AnalyseDiagnosticAPIView.as_view(),
        name='diagnostic-analyse',
    ),
    path(
        'maladies/galerie/',
        GalerieMaladiesAPIView.as_view(),
        name='maladies-galerie',
    ),
    path('conseils/', ConseilsAPIView.as_view(), name='conseils'),
    path('agent/cas/', AgentCasAPIView.as_view(), name='agent-cas'),

    path('cultures/', CultureListAPIView.as_view(), name='cultures-list'),
    path('cultures/<int:pk>/', CultureDetailAPIView.as_view(), name='culture-detail'),

    path('exploitations/', ExploitationListAPIView.as_view(), name='exploitations-list'),
    path('exploitations/<int:pk>/', ExploitationDetailAPIView.as_view(), name='exploitation-detail'),

    path('parcelles/', ParcelleListAPIView.as_view(), name='parcelles-list'),
    path('parcelles/<int:pk>/', ParcelleDetailAPIView.as_view(), name='parcelle-detail'),

    path('diagnostics/', DiagnosticListAPIView.as_view(), name='diagnostics-list'),
    path('diagnostics/<int:pk>/', DiagnosticDetailAPIView.as_view(), name='diagnostic-detail'),

    path('maladies/', MaladieListAPIView.as_view(), name='maladies-list'),
    path('maladies/<int:pk>/', MaladieDetailAPIView.as_view(), name='maladie-detail'),

    path('resultatdiagnostics/', ResultatDiagnosticListAPIView.as_view(), name='resultatdiagnostics-list'),
    path('resultatdiagnostics/<int:pk>/', ResultatDiagnosticDetailAPIView.as_view(), name='resultatdiagnostic-detail'),

    path('recommandations/', RecommandationListAPIView.as_view(), name='recommandations-list'),
    path('recommandations/<int:pk>/', RecommandationDetailAPIView.as_view(), name='recommandation-detail'),

    path('utilisateurs/', UtilisateurListAPI.as_view(), name='utilisateurs-list'),
    path('utilisateurs/<int:pk>/', UtilisateurDetailAPI.as_view(), name='utilisateur-detail'),

    path('marches/', MarcheListAPIView.as_view(), name='marches-list'),
    path('marches/<int:pk>/', MarcheDetailAPIView.as_view(), name='marche-detail'),
    path('prix/', PrixListAPIView.as_view(), name='prix-list'),
    path('prix/<int:pk>/', PrixDetailAPIView.as_view(), name='prix-detail'),
    path('zones-meteo/', ZoneMeteoListAPIView.as_view(), name='zones-meteo-list'),
    path('zones-meteo/<int:pk>/', ZoneMeteoDetailAPIView.as_view(), name='zone-meteo-detail'),
    path('previsions-meteo/', PrevisionMeteoListAPIView.as_view(), name='previsions-meteo-list'),
    path('previsions-meteo/<int:pk>/', PrevisionMeteoDetailAPIView.as_view(), name='prevision-meteo-detail'),
]
