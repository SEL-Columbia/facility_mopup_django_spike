from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext

from nmis.mopup.models import SurveyedFacility, ListedFacility

from nmis.misc.models import LGA

def select_lga(request):
    context = RequestContext(request)
    context.lgas = LGA.objects.all()
    return render_to_response("select_lga.html", context_instance=context)

def lga(request, lga_id):
    context = RequestContext(request)
    context.lga = LGA.objects.get(id=lga_id)
    context.surveyed_facilities = context.lga.surveyed_facilities.all()
    context.listed_facilities = context.lga.listed_facilities.all()
    return render_to_response("lga.html", context_instance=context)

def pick_match(request, lga_id, fac_type, facility_id, match_to_id=None):
    context = RequestContext(request)
    context.lga = LGA.objects.get(id=lga_id)
    context.fac_type = fac_type
    context.fac_id = facility_id

    if fac_type == "surveyed":
        context.match_title = "Match Surveyed Facility"
        context.description = """
        This facility was collected in the baseline survey. Please select
        the matching facility from the list below which was provided by the LGA.
        """

        context.facility = context.lga.surveyed_facilities.get(id=facility_id)
        context.available_for_list = context.lga.listed_facilities.filter(lga=context.lga, matched_facility=None)
    else:
        context.match_title = "Match Listed Facility"
        context.descripton = """
        This facility was listed by the LGA. Please select the matching facility
        from the list below which was collected in the survey round.
        """

        context.facility = context.lga.listed_facilities.get(id=facility_id)
        _sfacs = context.lga.surveyed_facilities.filter(lga=context.lga)
        _avail = [fac for fac in _sfacs if fac.matched_facilities.count() == 0]
        context.available_for_list = _avail

    context.no_facilities_available_for_list = 0 == len(context.available_for_list)
    return render_to_response("match.html", context_instance=context)

def make_match(request, lga_id, fac_type, facility_id, match_to_id):
    _lga = LGA.objects.get(id=lga_id)
    if fac_type == "surveyed":
        facility = _lga.surveyed_facilities.get(id=facility_id)
        for _fac in facility.matched_facilities.all():
            _fac.matched_facility = None
            _fac.save()
        expected_match = _lga.listed_facilities.get(id=match_to_id)
        expected_match.matched_facility = facility
        expected_match.save()
    else:
        facility = _lga.listed_facilities.get(id=facility_id)
        expected_match = _lga.surveyed_facilities.get(id=match_to_id)
        facility.matched_facility = expected_match
        facility.save()
    return HttpResponseRedirect("/mopup/%s" % lga_id)

def clear_match(request, lga_id, fac_type, facility_id):
    _lga = LGA.objects.get(id=lga_id)
    if fac_type == "surveyed":
        facility = _lga.surveyed_facilities.get(id=facility_id)
        for _fac in facility.matched_facilities.all():
            _fac.matched_facility = None
            _fac.save()
    else:
        facility = _lga.listed_facilities.get(id=facility_id)
        facility.matched_facility = None
        facility.save()
    return HttpResponseRedirect("/mopup/%s" % lga_id)
