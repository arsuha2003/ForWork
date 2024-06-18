from django.core import validators
from django.db import models
import random
import string


class Tiny(models.Model):
    full_url = models.CharField('Полный Адрес', max_length=255, blank=False, null=False, unique=True)
    short_url = models.CharField('Короткий Адрес', max_length=50, blank=False, null=False, unique=True)

    def __str__(self):
        return self.long_u + ' : ' + self.short_u

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def id_generator(size=1):
        # chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
        chars = ['a', 'b', 'c']
        new_short = ''
        unique = True
        while unique == True:
            new_short = ''.join(random.choice(chars) for _ in range(size))
            if Tiny.objects.filter(short_u = new_short).exists():
                unique = False
            else:
                unique = True
        return new_short

    def save(self, *args, **kwargs):
        self.short_u = self.id_generator()
        super(Sites, self).save(*args, **kwargs)