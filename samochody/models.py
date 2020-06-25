from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    last_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Fuels(models.Model):
    index = models.IntegerField(blank=True, primary_key=True)
    fuel = models.CharField("Rodzaj paliwa", max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fuels'


class Makes(models.Model):
    index = models.IntegerField(blank=True, primary_key=True)
    make = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'makes'


class Models(models.Model):
    index = models.IntegerField(blank=True, primary_key=True)
    model = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'models'


class Cars(models.Model):
    index = models.PositiveIntegerField(blank=True, primary_key=True)
    price = models.IntegerField("cena", blank=True, null=True)
    id_model = models.IntegerField(blank=True, null=True)
    id_car = models.BigIntegerField("ID samochodu", blank=True, null=True)
    production_year = models.PositiveSmallIntegerField("rok produkcji", blank=True, null=True)
    mileage = models.IntegerField("przebieg", blank=True, null=True)
    capacity = models.IntegerField("pojemność", blank=True, null=True)
    id_fuel = models.IntegerField(blank=True, null=True)
    date_ad = models.CharField("data dodania", max_length=20, blank=True, null=True)
    id_make = models.IntegerField(blank=True, null=True)
    is_activ = models.BooleanField(blank=True, null=True)
    new_price = models.PositiveIntegerField("nowa cena", blank=True, null=True)
    currency = models.CharField("waluta", max_length=4, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cars'
