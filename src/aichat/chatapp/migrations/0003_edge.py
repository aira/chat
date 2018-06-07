# Generated by Django 2.0.5 on 2018-05-25 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatapp', '0002_node'),
    ]

    operations = [
        migrations.CreateModel(
            name='edge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trigger', models.CharField(max_length=200)),
                ('response', models.TextField()),
                ('is_globstar', models.NullBooleanField(choices=[(None, ''), (True, 'Yes'), (False, 'No')], default=None, max_length=3)),
                ('dest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chatapp.node')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='chatapp.node')),
            ],
        ),
    ]
