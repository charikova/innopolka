from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documents/', include("Documents.urls")),
    path('user/', include("UserCards.urls")),
    path('', include("Documents.urls")),
    path('librarian/', include("librarian.urls")),
]
