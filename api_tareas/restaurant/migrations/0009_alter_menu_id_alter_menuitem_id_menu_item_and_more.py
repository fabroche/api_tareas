# Generated by Django 4.1.7 on 2023-11-19 17:48

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_alter_menuitem_id_menu_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='id',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='id_menu_item',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='menuitemcategory',
            name='id_menu_item_category',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]