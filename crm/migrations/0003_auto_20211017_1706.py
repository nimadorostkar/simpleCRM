# Generated by Django 3.2.8 on 2021-10-17 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20210830_2252'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.AddField(
            model_name='customer',
            name='additional_information',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='اطلاعات تکمیلی'),
        ),
        migrations.AddField(
            model_name='order',
            name='additional_information',
            field=models.TextField(blank=True, max_length=1000, null=True, verbose_name='اطلاعات تکمیلی'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='media/Default.png', null=True, upload_to='media', verbose_name='تصویر'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(max_length=200, null=True, verbose_name='آدرس'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True, verbose_name='تلفن'),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.customer', verbose_name='مشتری'),
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='crm.product', verbose_name='محصول'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('CANCELED', 'CANCELED'), ('COMPLETED', 'COMPLETED'), ('PAID', 'PAID'), ('PENDING PAYMENT', 'PENDING PAYMENT')], max_length=200, null=True, verbose_name='وضعیت'),
        ),
    ]
