from django.contrib import admin

from .models import Post, Comment, UserProfile

# Import the UserProfile model individually.
# Import the UserProfile model with Category and Page.
# If you choose this option, you'll want to modify the import statement you've already got to include UserProfile.
#from .models import Category, Page, UserProfile




admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
