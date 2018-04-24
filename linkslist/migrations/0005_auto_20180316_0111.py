# Generated by Django 2.0.2 on 2018-03-16 00:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('linkslist', '0004_auto_20180303_2056'),
    ]

    operations = [
        migrations.CreateModel(
            name='FolderAwe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('author', models.TextField()),
                ('createdate', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='idlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='linkslist.FolderAwe'),
        ),
        migrations.AddField(
            model_name='linkdata',
            name='idlist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='linkslist.FolderAwe'),
        ),
    ]