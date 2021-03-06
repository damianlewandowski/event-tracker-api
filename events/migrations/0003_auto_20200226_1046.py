# Generated by Django 3.0.3 on 2020-02-26 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20200226_0926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='events.Event'),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upvotes', models.IntegerField(default=0)),
                ('downvotes', models.IntegerField(default=0)),
                ('comment', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='events.Comment')),
                ('event', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='events.Event')),
            ],
        ),
    ]
