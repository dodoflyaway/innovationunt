from django.contrib import admin
from .models import invuser
from .models import product
from .models import sub
from .models import comment
from .models import sitetrans
from usern.models import orduser


# Register your models here.

admin.site.register(invuser)
admin.site.register(product)
admin.site.register(sub)
admin.site.register(comment)
admin.site.register(sitetrans)


