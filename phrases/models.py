from django.db import models

class Phrase(models.Model):
        phrase_text     = models.CharField(max_length=300)
        color         	= models.ForeignKey('Color')

        def __unicode__(self):
                return self.phrase_text

class Color(models.Model):
        name            = models.CharField(max_length=200)
        red            	= models.IntegerField(default=0)
        green     	= models.IntegerField(default=0)
        blue		= models.IntegerField(default=0)

        def __unicode__(self):
                return self.name
