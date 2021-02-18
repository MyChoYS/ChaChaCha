from django.db import models
from searchApp.models import Academy,TestSite

class Academy_review(models.Model):
    title = models.CharField(max_length=45, default="제목없음")
    password = models.CharField(max_length=8)
    content = models.CharField(max_length=500)
    writedate = models.DateField(auto_now_add=True)
    academy_id = models.ForeignKey(Academy, on_delete=models.CASCADE)

class TestSite_review(models.Model):
    title = models.CharField(max_length=45, default="제목없음")
    password = models.CharField(max_length=8)
    content = models.CharField(max_length=500)
    writedate = models.DateField(auto_now_add=True)
    testsite_id = models.ForeignKey(TestSite, on_delete=models.CASCADE)