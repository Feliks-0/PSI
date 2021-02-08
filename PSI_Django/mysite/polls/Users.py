from django.contrib.auth.models import User

user = User.objects.create_user('mirek', 'mirek@thebeatles.com', 'mirek')