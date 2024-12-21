# Generated by Django 5.1.3 on 2024-12-06 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentorship', '0007_course_category_course_image_course_likes_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='trainers/')),
            ],
        ),
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='courses/'),
        ),
    ]