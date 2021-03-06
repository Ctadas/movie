# Generated by Django 2.1.7 on 2019-02-22 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DoubanMovie',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False, verbose_name='主键ID')),
                ('douban_movie_id', models.CharField(default='', max_length=100, verbose_name='豆瓣电影ID')),
                ('title', models.CharField(default='', max_length=500, verbose_name='电影标题')),
                ('cover', models.CharField(blank=True, max_length=500, verbose_name='电影封面图片地址')),
                ('directors', models.CharField(blank=True, max_length=500, verbose_name='导演，多个导演之间用/分割')),
                ('writers', models.CharField(blank=True, max_length=500, verbose_name='编剧，多个编剧之间用/分割')),
                ('actors', models.CharField(blank=True, max_length=2000, verbose_name='主演，多个主演之间用/分割')),
                ('type', models.CharField(blank=True, max_length=500, verbose_name='类型，多个类型之间用/分割')),
                ('area', models.CharField(blank=True, max_length=500, verbose_name='制片国家/地区')),
                ('lang', models.CharField(blank=True, max_length=100, verbose_name='语言')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='上映日期。多个上映日期则选择最新的上映日期')),
                ('runtime', models.IntegerField(blank=True, null=True, verbose_name='片长（分钟）')),
                ('imdb', models.CharField(blank=True, max_length=100, verbose_name='imdb链接')),
                ('rate', models.FloatField(blank=True, null=True, verbose_name='电影评分')),
                ('votes', models.IntegerField(blank=True, null=True, verbose_name='电影评分投票人数')),
                ('summary', models.CharField(blank=True, max_length=2000, verbose_name='电影简介')),
            ],
            options={
                'db_table': 't_douban_movie',
            },
        ),
    ]
