
from django.conf.urls import url, include
from django.contrib import admin



urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog_posts/', include(('blog_posts.urls', 'blog_posts'), namespace='blog_posts')),
    url(r'^',include('blog_posts.urls'))

]
