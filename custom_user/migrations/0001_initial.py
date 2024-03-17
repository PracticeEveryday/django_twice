# Generated by Django 4.2.11 on 2024-03-17 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(help_text='Email Field', max_length=60, unique=True, verbose_name='Email')),
                ('is_superuser', models.BooleanField(default=False, help_text='superuser 여부입니다.')),
                ('is_active', models.BooleanField(default=True, help_text='활성화 상태 여부입니다.')),
                ('is_staff', models.BooleanField(default=False, help_text='Staff 여부입니다.')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='생성된 날짜입니다.')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='업데이트 된 날짜입니다.')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
