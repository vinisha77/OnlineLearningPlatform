from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personalpath', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='level',
            table='personalpath_level',
        ),
    ]
