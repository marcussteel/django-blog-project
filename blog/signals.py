import imp
from .utils import get_random_code

#oluşturtuğum postu kaydetmeden önce bana slug oluştursun isteyeceğim
from django.db.models.signals import pre_save

# postu save  et dediğim zaman benim yazdığım kodun gerçekleşmesni sağlıyor, önce bekle ben şu işlemi yapacağım sonra kaydetme işlemini tamamla
from django.dispatch import receiver

# slug fieldların arasına tire koyan fomksiyon boşluklara tire koyuyor 
from django.template.defaultfilters import slugify


from .models import Post

#decorator iki parametre alıyor. 


#instance posttan aldığımız veriyi düşünün, **kwargs ise sayısını bilmediğimiz argümanlar getirebilir python çaışırken
@receiver(pre_save, sender=Post)
def pre_save_create_slug(sender,instance, **kwargs):
    #slug yoksa oluşturacak ve boşluklara tire koyacak
    if not instance.slug:
        instance.slug = slugify(instance.title + " " + get_random_code())

a= "mjs ce e"
print(slugify(a))