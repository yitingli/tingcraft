from users.models import CraftCrew


class EmailOrUsernameModelBackend(object):
    def authenticate(self, username=None, password=None):
        if '@' in username:
            kwargs = {'email': username}
        else:
            kwargs = {'username': username}
        try:
            user = CraftCrew.objects.get(**kwargs)
            if user.check_password(password):
                return user
        except CraftCrew.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CraftCrew.objects.get(pk=user_id)
        except CraftCrew.DoesNotExist:
            return None
