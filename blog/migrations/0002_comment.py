# Generated by Django 3.1.1 on 2020-09-21 11:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='blog.timestampedmodel')),
                ('message', models.CharField(max_length=1000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_comment_list', to=settings.AUTH_USER_MODEL)),
                ('comment_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_comment_list', to='blog.post')),
                ('like_user_set', models.ManyToManyField(blank=True, related_name='like_comment_list', to=settings.AUTH_USER_MODEL)),
            ],
            bases=('blog.timestampedmodel',),
        ),
    ]
