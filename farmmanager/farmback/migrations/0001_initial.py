# Generated by Django 3.0.4 on 2020-03-18 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvanceForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('decription', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Consumable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('descript', models.CharField(max_length=100)),
                ('takenby', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Expenditure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('suppl', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=50)),
                ('typeofex', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('tax', models.IntegerField(blank=True)),
                ('descript', models.CharField(blank=True, max_length=500)),
                ('invno', models.IntegerField(blank=True)),
                ('paymod', models.CharField(max_length=50)),
                ('rcptno', models.IntegerField(blank=True)),
                ('baldue', models.IntegerField(blank=True)),
                ('baldate', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('source', models.CharField(max_length=100)),
                ('descript', models.CharField(max_length=100)),
                ('store', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.CharField(max_length=100)),
                ('product', models.CharField(max_length=50)),
                ('unit', models.CharField(max_length=50)),
                ('tax', models.IntegerField(blank=True)),
                ('descript', models.CharField(blank=True, max_length=500)),
                ('invnumber', models.IntegerField(blank=True)),
                ('paymode', models.CharField(max_length=50)),
                ('receiptnum', models.IntegerField(blank=True)),
                ('baldue', models.IntegerField(blank=True)),
                ('balduedate', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('paymod', models.CharField(max_length=50)),
                ('paye', models.IntegerField(blank=True)),
                ('nssf1', models.IntegerField(blank=True)),
                ('tax', models.IntegerField(blank=True)),
                ('lst', models.IntegerField(blank=True)),
                ('advance', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Personnel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('phone2', models.IntegerField(blank=True)),
                ('nin', models.CharField(blank=True, max_length=100, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('qualif', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Requisition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('costtype', models.CharField(max_length=100)),
                ('activity', models.CharField(max_length=100)),
                ('descript', models.CharField(max_length=50)),
                ('requestby', models.CharField(max_length=50)),
                ('approvby', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ToolBinCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('toolname', models.CharField(max_length=100)),
                ('descript', models.CharField(max_length=100)),
                ('storename', models.CharField(max_length=100)),
                ('takenby', models.CharField(max_length=100)),
                ('toolcond', models.CharField(max_length=100)),
                ('serialno', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]