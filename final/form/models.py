from django.db import models

class auth(models.Model):
    ROLES = (
        ('Intern', 'Intern'),
        ('Developer' , 'Developer'),
        ('HR' , 'HR'),
        ('Enginerr','Engineer'),

    )

    Designation = (
        (
            ('Senior Assosicate', 'Senior Assosicate'),
            ('Intern','Intern'),
            ('Associate','Associate'),
            ('Software','Software'),

        )
    )

    name = models.CharField(max_length=50,null = True)
    role = models.CharField(max_length=50,null = True,choices = ROLES)
    designation = models.CharField(max_length=50,null = True,choices = Designation)

    def __str__(self):
        return self.name

