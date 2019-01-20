# Generated by Django 2.1.4 on 2019-01-19 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0024_auto_20190106_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_chunk',
            name='hash_blake2b',
            field=models.CharField(max_length=128, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='file_chunk',
            unique_together={('position', 'file')},
        ),
        migrations.AlterUniqueTogether(
            name='fileserver_cluster_member_shard_link',
            unique_together={('member', 'shard')},
        ),
        migrations.AlterUniqueTogether(
            name='fileserver_cluster_shard_link',
            unique_together={('cluster', 'shard')},
        ),
        migrations.AddField(
            model_name='file',
            name='delete_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='fileserver_cluster_member_shard_link',
            name='delete',
            field=models.BooleanField(default=True, help_text='Weather this shard accepts delete jobs', verbose_name='Delete'),
        ),
    ]
