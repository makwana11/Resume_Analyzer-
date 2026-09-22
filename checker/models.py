from django.db import models


class Resume(models.Model):
    """
    Ek resume upload ane teni JD (Job Description) sathe match ni entry.
    """
    name = models.CharField(max_length=100)
    resume_file = models.FileField(upload_to='resumes/')
    job_description = models.TextField()

    # Analysis result - jyare user resume upload kare tyare calculate thay
    match_score = models.FloatField(default=0)
    matched_keywords = models.TextField(blank=True)
    missing_keywords = models.TextField(blank=True)

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.match_score}%"
