from django.contrib.auth.base_user import BaseUserManager


class BlogUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, name, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        if not name:
            raise ValueError('The given name must be set')
        email = self.normalize_email(email)

        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, name, password, **extra_fields):
        return self._create_user(email, name, password, **extra_fields)

    def create_superuser(self, email, name, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_admin', True)
        extra_fields.setdefault('is_staff', True)
        return self._create_user(email, name, password, **extra_fields)
