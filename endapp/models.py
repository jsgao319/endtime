# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

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
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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


class Qinxi(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    hunfou = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    guojia = models.CharField(max_length=200, blank=True, null=True)
    politics = models.CharField(max_length=200, blank=True, null=True)
    jobjiny = models.CharField(max_length=200, blank=True, null=True)
    current_address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    job_wanted = models.CharField(max_length=200, blank=True, null=True)
    jobsite = models.CharField(max_length=200, blank=True, null=True)
    expect_job = models.CharField(max_length=200, blank=True, null=True)
    job_nature = models.CharField(max_length=200, blank=True, null=True)
    expect_vocation = models.CharField(max_length=200, blank=True, null=True)
    salary = models.CharField(max_length=200, blank=True, null=True)
    education_experience = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    specialty = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qinxi'


class Qinxi2(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=50, blank=True, null=True)
    hunfou = models.CharField(max_length=50, blank=True, null=True)
    age = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.CharField(max_length=50, blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    guojia = models.CharField(max_length=200, blank=True, null=True)
    politics = models.CharField(max_length=200, blank=True, null=True)
    jobjiny = models.CharField(max_length=200, blank=True, null=True)
    current_address = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    job_wanted = models.CharField(max_length=200, blank=True, null=True)
    jobsite = models.CharField(max_length=200, blank=True, null=True)
    expect_job = models.CharField(max_length=200, blank=True, null=True)
    job_nature = models.CharField(max_length=200, blank=True, null=True)
    expect_vocation = models.CharField(max_length=200, blank=True, null=True)
    salary = models.CharField(max_length=200, blank=True, null=True)
    education_experience = models.CharField(max_length=200, blank=True, null=True)
    school = models.CharField(max_length=200, blank=True, null=True)
    specialty = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'qinxi2'


class TUser(models.Model):
    email = models.CharField(max_length=40, blank=True, null=True)
    nickname = models.CharField(max_length=40, blank=True, null=True)
    password = models.CharField(max_length=40, blank=True, null=True)
    aass = models.CharField(max_length=10, blank=True, null=True)
    column_8 = models.CharField(db_column='Column_8', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_user'


class Xinxibiao1(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    xueli = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    jobjiny = models.CharField(max_length=50, blank=True, null=True)
    homesite = models.CharField(max_length=50, blank=True, null=True)
    census = models.CharField(max_length=40, blank=True, null=True)
    jobstate = models.CharField(max_length=50, blank=True, null=True)
    jobsite = models.CharField(max_length=50, blank=True, null=True)
    jobzhiwei = models.CharField(max_length=400, blank=True, null=True)
    jobhanye = models.CharField(max_length=400, blank=True, null=True)
    jobmoney = models.CharField(max_length=400, blank=True, null=True)
    educaton = models.CharField(max_length=400, blank=True, null=True)
    yuliu1 = models.CharField(max_length=400, blank=True, null=True)
    yuliu2 = models.CharField(max_length=400, blank=True, null=True)
    yuliu3 = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinxibiao1'


class Xinxibiao2(models.Model):
    name = models.CharField(max_length=20, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    age = models.CharField(max_length=20, blank=True, null=True)
    xueli = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    jobjiny = models.CharField(max_length=50, blank=True, null=True)
    homesite = models.CharField(max_length=50, blank=True, null=True)
    census = models.CharField(max_length=40, blank=True, null=True)
    jobstate = models.CharField(max_length=50, blank=True, null=True)
    jobsite = models.CharField(max_length=50, blank=True, null=True)
    jobzhiwei = models.CharField(max_length=400, blank=True, null=True)
    jobhanye = models.CharField(max_length=400, blank=True, null=True)
    jobmoney = models.CharField(max_length=400, blank=True, null=True)
    educaton = models.CharField(max_length=400, blank=True, null=True)
    yuliu1 = models.CharField(max_length=400, blank=True, null=True)
    yuliu2 = models.CharField(max_length=400, blank=True, null=True)
    yuliu3 = models.CharField(max_length=400, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'xinxibiao2'
