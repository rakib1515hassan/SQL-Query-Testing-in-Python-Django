# Install CK Text Editor in a project


1) Install 

        pip install django-ckeditor

2) setting.py

    (i) INSTALLED_APPS  

        INSTALLED_APPS = [
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',
            'your_app',

            ## For CKEditor Text Editor
            'ckeditor',
            'ckeditor_uploader',
        ]

    (ii) Set static and media files

            STATIC_URL = 'static/'
            STATICFILES_DIRS = os.path.join(BASE_DIR, 'static'),
            STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')


            MEDIA_URL = '/Ck_Items/'
            MEDIA_ROOT = os.path.join(BASE_DIR, 'media/Ck_Items')


    (iii) Set plugins

            CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
            CKEDITOR_UPLOAD_PATH = "uploads/"
            CKEDITOR_CONFIGS = {
                'default': {
                    'toolbar': 'full',
                    # 'height': 300,
                    # 'width': 300,

                    'removePlugins':'exportpdf',  # এই Proparty ব্যবহার করে, আপনি কিছু Plagin বন্ধ করতে পারেন যা সম্পাদনা সংক্রান্ত 
                                                # স্পেসিফিক ফিচার যোগ করে। "exportpdf" নামের Plagin বন্ধ করার ফলে, ব্যবহারকারীরা
                                                #  ক্রমান্বয়ে PDF ডকুমেন্ট তৈরি করতে পারবেন না এবং এই Plagin এর সম্পর্কিত কোনো বিশেষ
                                                #  সম্প্রদায়ের সমর্থন থাকবে না।

                    
                    'extraPlugins': ','.join(
                        [
                            'codesnippet',    ## For Code snippet added with your CkEditors
                            'widget',

                            'html5video',     ## For HTML5 video added with your CkEditors
                            'youtube',        ## For YouTube video added with your CkEditors     
                            
                        ]
                    ),       
                },
            }



3) url.py

        from django.contrib import admin
        from django.urls import path, include

        from django.conf import settings
        from django.conf.urls.static import static

        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', include('your_app.urls')),

            ## For Ck-editor, It is not a app.
            path('ckeditor/', include('ckeditor_uploader.urls')),  
        ]

        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



4) Make Model 

        from django.db import models
        from ckeditor.fields import RichTextField
        from ckeditor_uploader.fields import RichTextUploadingField

        class Blog(models.Model):
            name      = models.CharField( max_length=100 )

            # Image Add করার Option আসবে না।
            content_1 = RichTextField( null=True, blank=True, config_name="default", )  

            # Image Add করার Option আসবে।   
            content_2 = RichTextUploadingField( null=True, blank=True, config_name="default", )
            

            def __str__(self):
                return self.name



5) If Ck Text Editor set on any html file then make a forms.py fie

        from django.forms import ModelForm
        from .models import *

        class BlogForm(ModelForm):

            class Meta:
                model = Blog
                fields = '__all__'


    Now send it on Html by views.py

        from django.shortcuts import render
        from .models import *
        from .forms import *

        def home(request):
            data = Blog.objects.all()
            form = BlogForm
            if request.method == 'POST':
                form = BlogForm(request.POST)
                if form.is_valid:
                    form.save()
                    form = BlogForm
                  
            context ={
                "data": data, 
                "form": form
                }
            return render(request, "index.html", context)



6) If show code in html then net to set up 

    <!-- For CkEditor -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/styles/devibeans.min.css" />

    <!-- For CkEditor -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.6.0/highlight.min.js"></script>