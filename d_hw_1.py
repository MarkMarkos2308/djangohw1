from django.db import models


# # problem 1

# class person(models.Model):
#     name = models.CharField(null=True)

# # problem 2
#
# class person(models.Model):
#     name = models.CharField(blank=True, default='default')


# # problem 3
#
# 'user.apps.UserConfig'
# 'car.apps.CarConfig'

# # problem 4
#
# 'set DJANGO_SETTINGS_MODULE=user.settings'
# 'set DJANGO_SETTINGS_MODULE=car.settings'

# # problem 5
#
#
# class st(models.Model):
#     name = models.CharField()
#     surname = models.CharField()
#     major = models.CharField()
#     o = (('F', 'Freshman'), ('S1', 'Sophomore'), ('J', 'Junior'), ('S2', 'Senior'))
#     student_year = models.CharField(max_length=2, choices=o)

# # problem 6
#
#
# class pers(models.Model):
#     firs_name = models.CharField(null=False)
#     last_name = models.CharField(null=False)
#
#
# class address(models.Model):
#     street = models.CharField(null=False)
#     house = models.ForeignKey(pers, null=False, on_delete=models.CASCADE)
#     city = models.CharField(null=False)
#     person = models.CharField(null=False)
