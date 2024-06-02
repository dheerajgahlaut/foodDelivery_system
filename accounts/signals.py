from django.db.models.signals import post_save,pre_save  #---for import signal---
from django.dispatch import receiver  #--import receiver---
from .models import User,UserProfile  #---we are using this profile so we import---

#Signals are used to perform some action on the modification/creation of a particular entry in the Database. For example, One would want to create a profile instance, as soon as a new user instance is created in Database
#---we want that if user wull create the user_profile will auto create
@receiver(post_save, sender=User)  #---use this decorator to received signal---
def post_save_create_profile_receiver(sender,instance,created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(User=instance)
        print('user profile is created')
#---we use try except in else because if profile updated then save and if nit created then create---
    else:
        try:        
           profile = UserProfile.objects.get(User=instance)
           profile.save()
        except:
            #create the userprofileif not exist
            UserProfile.objects.get(User=instance)
            print('profle was not exixt but I created one')
        print('user is updated')

@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance,**kwargs):
    print(instance.username, 'this user is being saved')
    
#post_save.connect(post_save_create_profile_receiver,sender=User)