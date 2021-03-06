# Generated by Django 2.0.7 on 2018-07-04 18:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_original_id', models.CharField(max_length=255)),
                ('project_crawl_url', models.CharField(max_length=255)),
                ('website_id', models.IntegerField()),
                ('crawl_status', models.IntegerField(default=1)),
                ('crawl_count', models.IntegerField(default=1)),
                ('crawl_time', models.DateTimeField(default='2018-07-04 12:00:00')),
                ('last_crawl_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TaoBaoProject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=255)),
                ('original_id', models.CharField(max_length=255, unique=True)),
                ('curr_money', models.DecimalField(decimal_places=2, max_digits=18)),
                ('target_money', models.DecimalField(decimal_places=2, max_digits=18)),
                ('status', models.CharField(max_length=255)),
                ('status_value', models.IntegerField()),
                ('project_url', models.CharField(max_length=255)),
                ('finish_per', models.IntegerField()),
                ('support_person', models.IntegerField()),
                ('focus_count', models.IntegerField()),
                ('video_url', models.CharField(max_length=255)),
                ('qrcode', models.CharField(max_length=255)),
                ('project_image', models.CharField(max_length=255)),
                ('remain_day', models.IntegerField()),
                ('person_name', models.CharField(max_length=255)),
                ('begin_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('update_time', models.DateTimeField(default='2018-07-04 12:00:00')),
            ],
        ),
        migrations.CreateModel(
            name='TaoBaoprojectItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('item_id', models.CharField(max_length=255)),
                ('image', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=18)),
                ('support_person', models.IntegerField()),
                ('total', models.IntegerField()),
                ('desc', models.CharField(max_length=255)),
                ('update_time', models.DateTimeField(default='2018-07-04 12:00:00')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spider.TaoBaoProject', to_field='original_id')),
            ],
        ),
    ]
