# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-14 14:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('recomm_id', models.IntegerField(db_column='recommendation_id', null=True)),
                ('content_recommended', models.CharField(db_column='content_id', max_length=50, null=True)),
                ('confidence', models.FloatField(db_column='confidence', null=True)),
                ('support', models.FloatField(db_column='support', null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'banners',
            },
        ),
        migrations.CreateModel(
            name='BannerContent',
            fields=[
                ('content_id', models.CharField(db_column='CONTENT_ID', db_index=True, max_length=50, primary_key=True, serialize=False)),
                ('content_name', models.CharField(db_column='PARENT_NAME', max_length=200, null=True)),
                ('content_type', models.CharField(db_column='CONTENT_TYPE', db_index=True, max_length=200, null=True)),
                ('circle', models.CharField(db_column='CIRCLE', db_index=True, max_length=50)),
                ('language', models.CharField(db_column='LANGUAGE', max_length=200, null=True)),
                ('mou', models.DecimalField(db_column='mou', decimal_places=5, max_digits=15, null=True)),
                ('mou_user', models.DecimalField(db_column='mou_user', decimal_places=5, max_digits=15, null=True)),
                ('partner', models.CharField(db_column='PARTNER', max_length=200)),
                ('uu_played', models.IntegerField(db_column='UU_PLAYED', null=True)),
                ('session', models.IntegerField(db_column='SESSIONS', null=True)),
                ('id', models.AutoField(primary_key=True)),
            ],
            options={
                'db_table': 'banner_content',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.CharField(db_column='content_id', db_index=True, max_length=100, primary_key=True, serialize=False)),
                ('content_type', models.CharField(db_column='content_type', max_length=200, null=True)),
                ('content_name', models.CharField(db_column='content_name', max_length=200, null=True)),
                ('language', models.CharField(max_length=200, null=True)),
                ('duration', models.CharField(max_length=100, null=True)),
                ('partner', models.CharField(max_length=200, null=True)),
                ('genre', models.CharField(max_length=200, null=True)),
                ('actor', models.CharField(max_length=100, null=True)),
                ('parent_id', models.CharField(db_column='content_parent_id', max_length=200, null=True)),
                ('parent_name', models.CharField(db_column='partner_name', max_length=200, null=True)),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='ContentAll',
            fields=[
                ('content_id', models.CharField(db_column='CONTENT_ID', db_index=True, max_length=50, primary_key=True, serialize=False)),
                ('content_name', models.CharField(db_column='PARENT_NAME', max_length=200, null=True)),
                ('content_type', models.CharField(db_column='CONTENT_TYPE', db_index=True, max_length=200, null=True)),
                ('circle', models.CharField(db_column='CIRCLE', db_index=True, max_length=50)),
                ('language', models.CharField(db_column='LANGUAGE', max_length=200, null=True)),
                ('mou', models.DecimalField(db_column='mou', decimal_places=5, max_digits=15, null=True)),
                ('mou_user', models.DecimalField(db_column='mou_user', decimal_places=5, max_digits=15, null=True)),
                ('partner', models.CharField(db_column='PARTNER', max_length=200)),
                ('uu_played', models.IntegerField(db_column='UU_PLAYED', null=True)),
                ('session', models.IntegerField(db_column='SESSIONS', null=True)),
                ('id', models.AutoField(primary_key=True)),
            ],
            options={
                'db_table': 'content_data',
            },
        ),
        migrations.CreateModel(
            name='ContentSeen',
            fields=[
                ('user_id', models.BigIntegerField(db_index=True)),
                ('content_id', models.CharField(max_length=50)),
                ('content_name', models.CharField(max_length=100, null=True)),
                ('date', models.DateTimeField()),
                ('mou', models.DecimalField(db_index=True, decimal_places=3, max_digits=8)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_streaming_history',
            },
        ),
        migrations.CreateModel(
            name='Decider',
            fields=[
                ('recomm_bucket', models.CharField(db_column='recommendation_bucket', db_index=True, max_length=150, null=True)),
                ('recomm_id', models.IntegerField(db_column='recommendation_id', null=True)),
                ('gender', models.CharField(db_column='gender', db_index=True, max_length=10, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('language', models.CharField(db_column='language', db_index=True, max_length=50, null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'decider',
            },
        ),
        migrations.CreateModel(
            name='LastContentPlayed',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('uu_played', models.IntegerField(db_column='UU_PLAYED', null=True)),
                ('session', models.IntegerField(db_column='SESSIONS', null=True)),
                ('circle', models.CharField(db_column='CIRCLE', db_index=True, max_length=50)),
                ('mou', models.DecimalField(db_column='mou', decimal_places=5, max_digits=15, null=True)),
                ('last_date', models.DateField(db_column='last_played_date')),
                ('content_id', models.CharField(db_column='last_played_content_id', max_length=50)),
                ('content_type', models.CharField(db_column='last_played_content_type', max_length=20)),
            ],
            options={
                'db_table': 'user_played_data',
            },
        ),
        migrations.CreateModel(
            name='Override',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('action', models.CharField(max_length=30)),
                ('recomm_id', models.IntegerField(db_column='recommendation_id', null=True)),
                ('content_seen', models.IntegerField(db_column='content_seen', null=True)),
                ('content_recommended', models.IntegerField(db_column='content_recommended', null=True)),
                ('support_12', models.FloatField(db_column='support_12', null=True)),
                ('support_1', models.FloatField(db_column='support_1', null=True)),
                ('support_2', models.FloatField(db_column='support_2', null=True)),
                ('confidence', models.FloatField(null=True)),
                ('lift', models.FloatField(null=True)),
            ],
            options={
                'db_table': 'override',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('recomm_id', models.IntegerField(db_column='recommendation_id', db_index=True, null=True)),
                ('content_seen', models.CharField(db_column='content_seen', db_index=True, max_length=50, null=True)),
                ('content_recommended', models.CharField(db_column='content_recommended', max_length=50, null=True)),
                ('support_12', models.FloatField(null=True)),
                ('support_1', models.FloatField(null=True)),
                ('support_2', models.FloatField(null=True)),
                ('confidence', models.FloatField(null=True)),
                ('lift', models.FloatField(null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'recommendation_base',
            },
        ),
        migrations.CreateModel(
            name='Recommendation_Content',
            fields=[
                ('recomm_id', models.IntegerField(db_column='recommendation_id', db_index=True, null=True)),
                ('content_seen', models.CharField(db_column='content_seen', db_index=True, max_length=50, null=True)),
                ('content_recommended', models.CharField(db_column='content_recommended', max_length=50, null=True)),
                ('confidence', models.FloatField(null=True)),
                ('actor_score', models.FloatField(null=True)),
                ('genre_score', models.FloatField(null=True)),
                ('streams', models.FloatField(null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'recommendation_content',
            },
        ),
        migrations.CreateModel(
            name='RecommendationAll',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.BigIntegerField(db_column='user_id', db_index=True, null=True)),
                ('content_id', models.CharField(db_column='content_id', db_index=True, max_length=50, null=True)),
                ('recomm_score', models.DecimalField(db_column='rank', decimal_places=5, max_digits=15, null=True)),
                ('content_type', models.CharField(db_column='content_type', max_length=200, null=True)),
                ('actor', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'recommendations_all',
            },
        ),
        migrations.CreateModel(
            name='TVRecommendation',
            fields=[
                ('recomm_id', models.IntegerField(db_column='recommendation_id', db_index=True, null=True)),
                ('content_seen', models.CharField(db_column='content_seen', db_index=True, max_length=50, null=True)),
                ('content_recommended', models.CharField(db_column='content_recommended', max_length=50, null=True)),
                ('support_12', models.FloatField(null=True)),
                ('support_1', models.FloatField(null=True)),
                ('support_2', models.FloatField(null=True)),
                ('confidence', models.FloatField(null=True)),
                ('lift', models.FloatField(null=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'recommendation_base_tv',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('country', models.CharField(max_length=50, null=True)),
                ('state', models.CharField(max_length=50, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('age', models.CharField(max_length=15, null=True)),
                ('language', models.CharField(db_column='user_language', default=None, max_length=200, null=True)),
                ('user_preferences', models.CharField(db_column='content_language', default=None, max_length=200, null=True)),
            ],
            options={
                'db_table': 'user_data',
            },
        ),
        migrations.CreateModel(
            name='User_AB',
            fields=[
                ('user_id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('group', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'users_ab',
            },
        ),
        migrations.CreateModel(
            name='UserAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField(db_column='user_id', db_index=True)),
                ('content_id', models.CharField(max_length=100)),
                ('action_id', models.IntegerField(db_column='action_id', db_index=True)),
                ('value', models.CharField(max_length=100, null=True)),
            ],
            options={
                'db_table': 'user_action',
            },
        ),
        migrations.AlterUniqueTogether(
            name='decider',
            unique_together=set([('recomm_bucket', 'gender', 'language')]),
        ),
    ]
