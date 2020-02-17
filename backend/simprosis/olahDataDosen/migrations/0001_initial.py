# Generated by Django 2.2 on 2020-02-17 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('rps', '0002_auto_20200217_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='dosen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nidn', models.CharField(max_length=10)),
                ('jabatan', models.CharField(choices=[('Tenaga Pengajar', 'Tenaga Pengajar'), ('Asisten Ahli', 'Asisten Ahli'), ('Lektor', 'Lektor'), ('Lektor Kepala', 'Lektor Kepala'), ('Guru Besar', 'Guru Besar')], max_length=50)),
                ('golongan', models.CharField(choices=[('3a', 'III/a'), ('3b', 'III/b'), ('3c', 'III/c'), ('3d', 'III/d'), ('4a', 'IV/a'), ('4b', 'IV/b'), ('4c', 'IV/c'), ('4d', 'IV/d'), ('4e', 'IV/e')], max_length=5)),
                ('nik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rps.userProfiles')),
            ],
            options={
                'verbose_name': 'dosen',
                'verbose_name_plural': 'dosen',
            },
        ),
    ]
