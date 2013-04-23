from django.db import models
from django.contrib.auth.models import User
from nmis.misc.models import LGA

class SurveyedFacility(models.Model):
    name = models.TextField()
    nmis_id = models.TextField()
    lga = models.ForeignKey(LGA, null=True, blank=True, related_name="surveyed_facilities")

    def matched_facility_name(self):
        _f = self.get_matched_facility()
        if _f:
            return _f.name

    def get_matched_facility(self):
        _matches = self.matched_facilities.all()
        if len(_matches) > 0:
            return _matches[0]

    def matched_id(self):
        if self.matched_facilities.count() > 0:
            return self.matched_facilities.all()[0].id
        else:
            return None

class ListedFacility(models.Model):
    name = models.TextField()
    lga = models.ForeignKey(LGA, null=True, blank=True, related_name="listed_facilities")
    matched_facility = models.ForeignKey(SurveyedFacility, related_name="matched_facilities", null=True, blank=True)

    def matched_facility_name(self):
        _f = self.get_matched_facility()
        if _f:
            return _f.name

    def get_matched_facility(self):
        if self.matched_facility_id is not None:
            return self.matched_facility

    def matched_id(self):
        return self.matched_facility_id