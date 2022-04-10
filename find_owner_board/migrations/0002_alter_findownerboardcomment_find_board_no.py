
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('find_owner_board', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='findownerboardcomment',
            name='find_board_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='find_owner_board.findownerboard'),
        ),
    ]
