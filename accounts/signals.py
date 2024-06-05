from django.db.models.signals import post_save, pre_save  #---for import signal---
from django.dispatch import receiver  #--import receiver---
from .models import User, UserProfile  #---we are using this profile so we import---

#Signals are used to perform some action on the modification/creation of a particular entry in the Database. For example, One would want to create a profile instance, as soon as a new user instance is created in Database
#---we want that if user will create the user_profile will auto create
@receiver(post_save, sender=User)  #---use this decorator to received signal---
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        #print('user profile is created')
#---we use try except in else because if profile updated then save and if nit created then create---
    else:
        try:        
           profile = UserProfile.objects.get(user=instance)
           profile.save()
        except:
        
         # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            #print('profile was not exist but I created one')
        # print('user is updated')

# @receiver(pre_save,sender=User)
# def pre_save_profile_receiver(sender,instance,**kwargs):
#     print(instance.username, 'this user is being saved')
    
#post_save.connect(post_save_create_profile_receiver,sender=User)

@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
# post_save.connect(post_save_create_profile_receiver, sender=User)