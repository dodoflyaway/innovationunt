from django.contrib import admin
from .models import invuser
from .models import product
from .models import sub
from .models import comment
from .models import sitetrans
from .models import invtokenacc
from .models import todo
from .models import admin_my
from .models import encash_request
from usern.models import orduser


# Register your models here.

admin.site.register(invuser)
admin.site.register(product)
admin.site.register(sub)
admin.site.register(comment)
admin.site.register(sitetrans)
admin.site.register(invtokenacc)
admin.site.register(todo)
admin.site.register(admin_my)
admin.site.register(encash_request)




