from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('adopt_review/', include("adopt_review.urls")),
    path('adopt_assignment/', include("adopt_assignment.urls")),
    path('inquiry_board/', include("inquiry_board.urls")),
    path('notice/', include("notice.urls")),
    path('streetanimal/', include("streetanimal.urls")),
    path('find_owner_board/', include("find_owner_board.urls")),


    path('lost_pet_board/', include("lost_pet_board.urls")),

]


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

