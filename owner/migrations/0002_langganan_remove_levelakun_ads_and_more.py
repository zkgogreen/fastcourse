# Generated by Django 4.2.6 on 2023-10-19 23:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Langganan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('durasi', models.IntegerField(default=1)),
                ('harga', models.IntegerField(default=50000)),
                ('diskon', models.IntegerField(default=40000)),
            ],
        ),
        migrations.RemoveField(
            model_name='levelakun',
            name='ads',
        ),
        migrations.RemoveField(
            model_name='levelakun',
            name='isPrivate',
        ),
        migrations.RemoveField(
            model_name='levelakun',
            name='premium',
        ),
        migrations.RemoveField(
            model_name='levelakun',
            name='vidio',
        ),
        migrations.AddField(
            model_name='artikel',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_artikel', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='earn',
            name='user_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pendapatan_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='levelakun',
            name='bonus',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='levelakun',
            name='foto',
            field=models.FileField(blank=True, null=True, upload_to='photo/level'),
        ),
        migrations.AddField(
            model_name='levelakun',
            name='ketentuan',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='levelakun',
            name='materi',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
        migrations.AddField(
            model_name='levelakun',
            name='people',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='levelakun',
            name='langganan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='langganan', to='owner.langganan'),
        ),
    ]
