# Generated by Django 4.2.1 on 2023-07-23 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogpost', '0006_post_piedeposteo_alter_post_cuerpo2'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('fechaCreado', models.DateTimeField(auto_now_add=True)),
                ('contenido', models.TextField()),
                ('activo', models.BooleanField(default=False)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentario', to='blogpost.post')),
            ],
        ),
    ]
