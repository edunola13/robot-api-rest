# Generated by Django 2.2.7 on 2019-11-26 19:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('devices', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('external_id', models.CharField(max_length=20)),
                ('component_type', models.CharField(choices=[('SENSOR', 'Sensor'), ('ACTUATOR', 'Actuador'), ('CONTROL', 'Controlador')], max_length=10)),
                ('status_data', models.TextField(max_length=500)),
                ('record_history', models.BooleanField(default=False)),
                ('record_interval', models.PositiveIntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('sensor_type', models.CharField(choices=[('DOOR', 'Sensor de Puerta'), ('IR', 'Sensor Infrarojo')], max_length=10)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('external_id', models.CharField(max_length=20)),
                ('component_type', models.CharField(choices=[('SENSOR', 'Sensor'), ('ACTUATOR', 'Actuador'), ('CONTROL', 'Controlador')], max_length=10)),
                ('status_data', models.TextField(max_length=500)),
                ('record_history', models.BooleanField(default=False)),
                ('record_interval', models.PositiveIntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('controller_type', models.CharField(choices=[('SIMPLE', 'Controlador Simple')], max_length=10)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Actuator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=100)),
                ('external_id', models.CharField(max_length=20)),
                ('component_type', models.CharField(choices=[('SENSOR', 'Sensor'), ('ACTUATOR', 'Actuador'), ('CONTROL', 'Controlador')], max_length=10)),
                ('status_data', models.TextField(max_length=500)),
                ('record_history', models.BooleanField(default=False)),
                ('record_interval', models.PositiveIntegerField(default=0)),
                ('enabled', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('actuator_type', models.CharField(choices=[('Bocina', 'Bocina')], max_length=10)),
                ('device', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='devices.Device')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
    ]
