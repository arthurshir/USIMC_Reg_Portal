from django.core.management.base import BaseCommand
# from registration_site.models import *

class Command(BaseCommand):
    args = '<foo bar ...>'
    help = 'our help string comes here'

    def _create_users(self):
    	print("Creating dat")
    	# for i in range(100):
	    # 	user = User.objects.create_user(username=email, password=password, firstName="", lastName="")
	    #     profile = Profile.objects.create(user = user)
	    #     performer = Performer.objects.create(owningProfile=profile)

    def handle(self, *args, **options):
        self._create_users()