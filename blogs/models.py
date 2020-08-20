from django.db import models

class Blog(models.Model):
    # title
    title = models.CharField(max_length=200)
    # text
    text = models.TextField()
    # date
    date = models.DateTimeField(auto_now_add=True)
    # owner
    owner = models.CharField(max_length=100)

    def __str__(self):
        if len(str(self.text)) > 30:    	
            return str(self.text)[:30]+"..."
        else:
            return str(self.text)


