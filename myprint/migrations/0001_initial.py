# Generated by Django 4.1.1 on 2022-10-27 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Biz Haqimizda',
            },
        ),
        migrations.CreateModel(
            name='AboutImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=60, null=True)),
                ('name_uz', models.CharField(blank=True, max_length=60, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=60, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/about')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('name_uz', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/category_image', verbose_name='image')),
                ('parent', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='myprint.category')),
            ],
            options={
                'verbose_name': 'Kategoriya',
                'verbose_name_plural': 'Kategoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Designe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/service')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='media/service')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='media/service')),
            ],
            options={
                'verbose_name': 'Dizayn',
            },
        ),
        migrations.CreateModel(
            name='DigitalPrint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('size', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=50)),
                ('on_site_print', models.CharField(max_length=50)),
                ('double_site_print', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/service')),
            ],
            options={
                'verbose_name': 'Raqamli chop etish',
            },
        ),
        migrations.CreateModel(
            name='InfoProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=65, verbose_name='size')),
                ('element', models.CharField(max_length=65, verbose_name='element')),
            ],
        ),
        migrations.CreateModel(
            name='LargeFormat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('product_name', models.CharField(max_length=50)),
                ('product_name_uz', models.CharField(max_length=50, null=True)),
                ('product_name_ru', models.CharField(max_length=50, null=True)),
                ('type', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('image1', models.ImageField(blank=True, null=True, upload_to='media/service')),
                ('image2', models.ImageField(blank=True, null=True, upload_to='media/service')),
                ('image3', models.ImageField(blank=True, null=True, upload_to='media/service')),
            ],
            options={
                'verbose_name': 'Katta formatda chop etish',
            },
        ),
        migrations.CreateModel(
            name='LaserPrint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=50, null=True, upload_to='media/service')),
            ],
            options={
                'verbose_name': 'Lazerni chop etish',
            },
        ),
        migrations.CreateModel(
            name='Product_Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('vendor_code', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=14)),
            ],
            options={
                'verbose_name': 'Maxsulot zakazi',
                'verbose_name_plural': 'Maxsulot zakazlari',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('key', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Sozlama',
                'verbose_name_plural': 'Sozlamalar',
            },
        ),
        migrations.CreateModel(
            name='Sponsors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/sponsor', verbose_name='image')),
            ],
        ),
        migrations.CreateModel(
            name='TextPrint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('description_uz', models.TextField(blank=True, null=True)),
                ('description_ru', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, max_length=50, null=True, upload_to='media/service')),
            ],
            options={
                'verbose_name': 'Tekstilni chop etish',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('name_uz', models.CharField(max_length=65, null=True)),
                ('name_ru', models.CharField(max_length=65, null=True)),
            ],
            options={
                'verbose_name': "Xizmat ko'rsatish turlari",
            },
        ),
        migrations.CreateModel(
            name='TypeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('name_uz', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/typeserveis')),
            ],
            options={
                'verbose_name': 'Xizmat turi',
            },
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name_order', models.CharField(max_length=300)),
                ('name_client', models.CharField(max_length=65)),
                ('client_phone_number', models.CharField(max_length=65)),
                ('manager_name', models.CharField(max_length=65)),
                ('date_order', models.DateTimeField(auto_now_add=True)),
                ('ready_product_date_order', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Foydalanuvchi zakazi',
                'verbose_name_plural': 'Foydalanuvchi zakazlari',
                'db_table': 'userorders',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('name_uz', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/product', verbose_name='image')),
                ('vendor_code', models.CharField(max_length=20)),
                ('description', models.TextField(verbose_name='description')),
                ('description_uz', models.TextField(null=True, verbose_name='description')),
                ('description_ru', models.TextField(null=True, verbose_name='description')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myprint.category')),
                ('info_product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myprint.infoproduct')),
            ],
            options={
                'verbose_name': 'Maxsulot',
                'verbose_name_plural': 'Maxsulotlar',
            },
        ),
        migrations.CreateModel(
            name='OrderService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=65, verbose_name='full_name')),
                ('phone_number', models.CharField(max_length=15, verbose_name='phone_number')),
                ('creat_add', models.DateTimeField(auto_now_add=True)),
                ('order_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myprint.type')),
            ],
            options={
                'verbose_name': "Xizmat ko'rsatish zakazlari",
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65)),
                ('status_order', models.CharField(blank=True, choices=[('шт', 'шт'), ('усл', 'усл')], default='шт', max_length=20, null=True)),
                ('amount', models.IntegerField(null=True)),
                ('price', models.IntegerField(null=True)),
                ('price_free_VAT', models.FloatField(null=True)),
                ('VAT', models.FloatField(null=True)),
                ('price_with_VAT', models.FloatField(null=True)),
                ('total', models.FloatField(null=True)),
                ('total_price_with_VAT', models.FloatField(null=True)),
                ('total_price_ALL', models.FloatField(null=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orderform', to='myprint.userorder', verbose_name='Zakazlar')),
            ],
            options={
                'verbose_name': 'Zakaz',
                'verbose_name_plural': 'Zakazlar',
                'db_table': 'orderform',
            },
        ),
        migrations.CreateModel(
            name='MenuService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=65, verbose_name='name')),
                ('name_uz', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=65, null=True, verbose_name='name')),
                ('image', models.ImageField(upload_to='media/menuservice', verbose_name='image')),
                ('type_service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myprint.typeservice')),
            ],
            options={
                'verbose_name': 'Menyu Xizmati',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/service')),
                ('type_sevice', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myprint.type')),
            ],
            options={
                'verbose_name': "Xizmat ko'rsatish rasmlari",
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=64, verbose_name='first_name')),
                ('full_name', models.CharField(blank=True, max_length=64, verbose_name='full_name')),
                ('phone_number', models.IntegerField(blank=True, unique=True, verbose_name='phone_number')),
                ('email', models.EmailField(max_length=25, null=True, verbose_name='email address')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superadmin', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Manager',
                'verbose_name_plural': 'Managers',
            },
        ),
    ]