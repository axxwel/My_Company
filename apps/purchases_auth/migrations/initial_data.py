from django.db import migrations, models

def populate_names(apps, schema_editor):
    names = ["Suyoj", "Sanjay", "Sangeeta"]                               
    Author = apps.get_model('person', 'Author')
    for name in names:
        obj = Author(first_name=name)
        obj.save()
        
class Migration(migrations.Migration):
    initial = True    
    
    dependencies = []    
                   
    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True,serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Author',
            },
        ),
        migrations.RunPython(populate_names),
    ]