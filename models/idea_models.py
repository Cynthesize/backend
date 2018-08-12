class Idea(models.Model):
    likes = models.IntegerField(default=0)
    comments = models.ListField()
    owner = models.CharField(max_length=250, default=None)
    summary = models.TextField()
