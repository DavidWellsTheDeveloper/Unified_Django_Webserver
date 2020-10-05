from django.db import models


class Faq(models.Model):
    faq_id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=300)
    question_short = models.CharField(max_length=100, null=True)
    answer = models.TextField()

    def __str__(self):
        return f"Q: {self.question} --- A: {self.answer}"
