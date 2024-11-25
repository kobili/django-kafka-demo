# Generated by Django 4.2 on 2024-11-16 21:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KafkaConsumerLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_topic', models.CharField(db_index=True, max_length=100)),
                ('event_key', models.CharField(blank=True, max_length=100, null=True)),
                ('event_value', models.TextField()),
                ('consumer_group_id', models.CharField(blank=True, help_text='The consumer group that handled the event.', max_length=250, null=True)),
                ('is_success', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Kafka Consumer Log',
                'verbose_name_plural': 'Kafka Consumer Logs',
            },
        ),
        migrations.CreateModel(
            name='KafkaProducerLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(db_index=True, max_length=100)),
                ('key', models.CharField(blank=True, max_length=100, null=True)),
                ('value', models.TextField()),
                ('partition', models.CharField(blank=True, max_length=50, null=True)),
                ('offset', models.CharField(blank=True, max_length=50, null=True)),
                ('is_success', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('error_message', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Kafka Producer Log',
                'verbose_name_plural': 'Kafka Producer Logs',
            },
        ),
    ]
