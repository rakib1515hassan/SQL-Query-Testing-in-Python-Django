# Install Django Tinymce Text Editor In Django Project.

Tinymce version = django-tinymce 3.6.1

1) Installation:
    
        pip install django-tinymce

2) Add tinymce to INSTALLED_APPS in settings.py for your project:

        INSTALLED_APPS = (
            'tinymce',
        )

3) Add tinymce.urls to urls.py for your project:

        urlpatterns = patterns('',
       
                path('tinymce/', include('tinymce.urls')),
       
        )


4) Add it on Modules

        from tinymce.models import HTMLField

        class Query_Code(models.Model):

                title       = models.CharField( max_length=200, null=True, blank=True)
                description = HTMLField()

                def __str__(self):
                        return self.title


                                       
# Add Tinymce Editor in Admin Panel

1) In Admin Panel add css and js files

Example:- Media class এর মধ্যমে CSS and Js file add করা যায় Admin pannel এর জন্যে।

        @admin.register(Query_Code)
        class Query_BlogsAdmin(admin.ModelAdmin):
            list_display = ('id', 'title')
            ordering = ['-id']

            class Media:        
                css = {
                     "all" : ("CSS/tiny.css",)
                }

                js = ("JS/tiny.js",)


2) Javascript code এ বলে দিতে হবে textfields এর id


        document.addEventListener("DOMContentLoaded", function(event){
                        let sc = document.createElement("script")
                sc.setAttribute('src', 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js');


                // উপরে যে script tag টি create করা হয়েছে তা Admin HTML এর head এর ভেতর include করা হয়েছে।
                document.head.appendChild(sc);


                sc.onload = ()=>{
                        // tinymce.init({
                        //     selector: '#id_SQL_query'
                        // });
        
        
                        // tinymce.init({
                        //     selector: '#id_ORM_query'
                        // });

                        var useDarkMode = window.matchMedia('(prefers-color-scheme: dark)').matches;

                        tinymce.init({
                        selector: 'textarea#full-featured',    //এখানে <textarea> এর id বলে দিতে হবে।
                        plugins: 'print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker imagetools textpattern noneditable help formatpainter permanentpen pageembed charmap tinycomments mentions quickbars linkchecker emoticons advtable export',
                        tinydrive_token_provider: 'URL_TO_YOUR_TOKEN_PROVIDER',
                        tinydrive_dropbox_app_key: 'YOUR_DROPBOX_APP_KEY',
                        tinydrive_google_drive_key: 'YOUR_GOOGLE_DRIVE_KEY',
                        tinydrive_google_drive_client_id: 'YOUR_GOOGLE_DRIVE_CLIENT_ID',
                        mobile: {
                        plugins: 'print preview powerpaste casechange importcss tinydrive searchreplace autolink autosave save directionality advcode visualblocks visualchars fullscreen image link media mediaembed template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists checklist wordcount tinymcespellchecker a11ychecker textpattern noneditable help formatpainter pageembed charmap mentions quickbars linkchecker emoticons advtable'
                        },
                        menu: {
                                tc: {
                                        title: 'Comments',
                                        items: 'addcomment showcomments deleteallconversations'
                                }
                        },
                        menubar: 'file edit view insert format tools table tc help',
                        toolbar: 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
                        autosave_ask_before_unload: true,
                        autosave_interval: '30s',
                        autosave_prefix: '{path}{query}-{id}-',
                        autosave_restore_when_empty: false,
                        autosave_retention: '2m',
                        image_advtab: true,
                        link_list: [
                                { title: 'My page 1', value: 'https://www.tiny.cloud' },
                                { title: 'My page 2', value: 'http://www.moxiecode.com' }
                        ],
                        image_list: [
                                { title: 'My page 1', value: 'https://www.tiny.cloud' },
                                { title: 'My page 2', value: 'http://www.moxiecode.com' }
                        ],
                        image_class_list: [
                                { title: 'None', value: '' },
                                { title: 'Some class', value: 'class-name' }
                        ],
                        importcss_append: true,
                        templates: [
                                { title: 'New Table', description: 'creates a new table', content: '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>' },
                                { title: 'Starting my story', description: 'A cure for writers block', content: 'Once upon a time...' },
                                { title: 'New list with dates', description: 'New List with dates', content: '<div class="mceTmpl"><span class="cdate">cdate</span><br /><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>' }
                        ],
                        template_cdate_format: '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
                        template_mdate_format: '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
                        height: 600,
                        image_caption: true,
                        quickbars_selection_toolbar: 'bold italic | quicklink h2 h3 blockquote quickimage quicktable',
                        noneditable_noneditable_class: 'mceNonEditable',
                        toolbar_mode: 'sliding',
                        spellchecker_ignore_list: ['Ephox', 'Moxiecode'],
                        tinycomments_mode: 'embedded',
                        content_style: '.mymention{ color: gray; }',
                        contextmenu: 'link image imagetools table configurepermanentpen',
                        a11y_advanced_options: true,
                        skin: useDarkMode ? 'oxide-dark' : 'oxide',
                        content_css: useDarkMode ? 'dark' : 'default',
                        /*
                        The following settings require more configuration than shown here.
                        For information on configuring the mentions plugin, see:
                        https://www.tiny.cloud/docs/plugins/premium/mentions/.
                        */
                        mentions_selector: '.mymention',
                        mentions_fetch: mentions_fetch,
                        mentions_menu_hover: mentions_menu_hover,
                        mentions_menu_complete: mentions_menu_complete,
                        mentions_select: mentions_select,
                        mentions_item_type: 'profile'
                        });


        
                };
        

        });