from django.db import models

class LoveResult(models.Model):
    your_name = models.CharField(max_length=100)
    crush_name = models.CharField(max_length=100)
    score = models.IntegerField()  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.your_name} + {self.crush_name} = {self.score}%"