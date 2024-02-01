from django.db import models
from django.contrib.auth.models import User


### School ###
class School(models.Model):
    name = models.CharField(max_length = 100)
    users = models.ManyToManyField(
        User,
        through = 'SchoolMember',
        related_name = 'schools'
    )
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']

### SchoolMember ###
class SchoolMember(models.Model):
    school = models.ForeignKey(
        School,
        on_delete = models.CASCADE,
        related_name = 'members'
    )
    user = models.ForeignKey(
        User,
        on_delete = models.CASCADE,
        related_name = 'school_memberships',
    )

    def __str__(self) -> str:
        return f'{self.school}'
    
    class Meta:
        ordering = ['id']
