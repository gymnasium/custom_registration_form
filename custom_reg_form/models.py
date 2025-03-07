from django.conf import settings
from django.db import models

# Backwards compatible settings.AUTH_USER_MODEL
USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class ExtraInfo(models.Model):
    """
    This model contains two extra fields that will be saved when a user registers.
    The form that wraps this model is in the forms.py file.
    """

    user = models.OneToOneField(USER_MODEL, null=True, on_delete=models.CASCADE)

    REGION0 = 'Other'
    REGION1 = 'Australia'
    REGION2 = 'Canada'
    REGION3 = 'Europe'
    REGION4 = 'Japan'
    REGION5 = 'United States'

    MARKETS = (
        (REGION0, (
            ("NA", "Not Applicable"),
        )),
        (REGION1, (
            ("36", "Australia - Melbourne"),
            ("39", "Australia - Sydney"),
        )),
        (REGION2, (
            ("40", "Canada - Toronto"),
            ("47", "Canada - Vancouver"),
        )),
        (REGION3, (
            ("35", "France - Paris"),
            ("43", "Netherlands - Amsterdam"),
            ("29", "UK - London"),
            ("115", "Germany"),
        )),
        (REGION4, (
            ("92", "Japan - Fukuoka"),
            ("64", "Japan - Osaka"),
            ("79", "Japan - Nagoya"),
            ("44", "Japan - Tokyo"),
        )),
        (REGION5, (
            ("120", "Alabama"),
            ("122", "Arkansas"),
            ("23", "Atlanta"),
            ("60", "Austin"),
            ("46", "Baltimore"),
            ("102", "Boise"),
            ("10", "Boston"),
            ("61", "Charlotte"),
            ("14", "Chicago"),
            ("34", "Connecticut"),
            ("22", "Dallas"),
            ("27", "Denver"),
            ("24", "Detroit"),
            ("826", "Houston"),
            ("58", "Indianapolis"),
            ("116", "Kentucky"),
            ("13", "Los Angeles"),
            ("117", "Louisiana"),
            ("33", "Miami"),
            ("20", "Minneapolis"),
            ("118", "Mississippi"),
            ("807", "Moline"),
            ("30", "New Jersey"),
            ("11", "New York City"),
            ("51", "Northern Virginia"),
            ("32", "Ohio"),
            ("119", "Oklahoma"),
            ("19", "Orange County"),
            ("72", "Orlando"),
            ("121", "Pensacola, FL"),
            ("18", "Philadelphia"),
            ("31", "Phoenix"),
            ("41", "Portland, OR"),
            ("73", "Providence"),
            ("803", "Raleigh/Durham"),
            ("78", "Richmond"),
            ("16", "San Diego"),
            ("12", "San Francisco"),
            ("17", "Seattle"),
            ("15", "Silicon Valley"),
            ("37", "St. Louis"),
            ("68", "Tampa"),
            ("63", "Tennessee"),
            ("25", "Washington, DC"),
            ("881", "Wisconsin"),
        )),
    )
    market = models.CharField(
        blank=True,
        choices=MARKETS,
        max_length=5,
        verbose_name="Select Nearest Aquent Office",
    )

    subscribe_jobs = models.BooleanField(
        blank=True,
        default=False,
        editable=True,
        verbose_name="Receive emails with job opportunities?",
    ),

    def __str__(self):
        return f"{self.user.username} | Market: {self.market} | Job Offers: {self.subscribe_jobs}"
    
    class Meta:
        app_label = "custom_reg_form"
        db_table = "custom_reg_form"
        db_table_comment = "Additional account & registration data for Open EdX students"
        verbose_name = "Custom Data"
        verbose_name_plural = "Custom Data"
