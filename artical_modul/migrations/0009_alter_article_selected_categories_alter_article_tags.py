# Generated by Django 4.2.7 on 2024-01-08 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artical_modul', '0008_alter_article_selected_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='selected_categories',
            field=models.ManyToManyField(to='artical_modul.articlecategory', verbose_name='دسته بندی ها'),
        ),
        migrations.AlterField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(related_name='articales', to='artical_modul.articaletag', verbose_name='تگ ها'),
        ),
    ]