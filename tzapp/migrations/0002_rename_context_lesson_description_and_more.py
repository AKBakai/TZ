# Generated by Django 4.0.4 on 2022-05-05 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tzapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lesson',
            old_name='context',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='lessonmaterial',
            old_name='context',
            new_name='context1',
        ),
        migrations.RemoveField(
            model_name='course',
            name='context',
        ),
        migrations.RemoveField(
            model_name='direction',
            name='context',
        ),
        migrations.AddField(
            model_name='lesson',
            name='anons',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='upload_file',
            field=models.FileField(default=1, upload_to='uploads_file'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lesson',
            name='upload_video',
            field=models.FileField(default=1, upload_to='uploads_video'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonmaterial',
            name='context2',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonmaterial',
            name='image',
            field=models.ImageField(default=1, upload_to='uploads_image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lessonmaterial',
            name='upload_file_1',
            field=models.FileField(default=1, upload_to='uploads_file_1'),
            preserve_default=False,
        ),
    ]
