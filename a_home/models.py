from django.db import models

class EssayOrder(models.Model):
    ACADEMIC_LEVELS = [
        ("HS", "High School"),
        ("UG", "Undergraduate"),
        ("GR", "Graduate"),
    ]
    FORMATTING_STYLES = [
        ("APA", "APA"),
        ("MLA", "MLA"),
        ("Chicago", "Chicago"),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    topic = models.CharField(max_length=200)
    pages = models.PositiveIntegerField()
    deadline = models.DateField()
    academic_level = models.CharField(max_length=10, choices=ACADEMIC_LEVELS)
    formatting_style = models.CharField(max_length=20, choices=FORMATTING_STYLES)
    instructions = models.TextField(blank=True)

    # 💰 price will be calculated automatically
    price = models.DecimalField(max_digits=8, decimal_places=2, editable=False, default=0.00)

    submitted_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically calculate price = $10 per page
        self.price = self.pages * 10
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.topic} ({self.name}) - ${self.price}"

