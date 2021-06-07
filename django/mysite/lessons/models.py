from django.db import models

# Create your models here.
class booktest(models.Model):
    lessonNo = models.IntegerField()
    arabic = models.CharField(max_length =40)
    english = models.CharField(max_length =40)

#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

class Book1(models.Model):
    lesson = models.IntegerField(db_column='Lesson', blank=True, null=True)  # Field name made lowercase.
    english = models.TextField(db_column='English', blank=True, null=True)  # Field name made lowercase.
    arabic = models.TextField(db_column='Arabic', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BOOK1'
