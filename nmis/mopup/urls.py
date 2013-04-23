#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls.defaults import *
from django.core.urlresolvers import reverse
from . import views

urlpatterns = patterns('',
	url(r'^$', 'nmis.mopup.views.select_lga', name='mopup_select_lga'),
	url(r'^(?P<lga_id>\w+)/$', 'nmis.mopup.views.lga', name='mopup_lga'),
	url(r'^(?P<lga_id>\w+)/(?P<fac_type>surveyed|listed)/(?P<facility_id>\w+)/?$', 'nmis.mopup.views.pick_match', name='pick_match'),
	url(r'^(?P<lga_id>\w+)/(?P<fac_type>surveyed|listed)/(?P<facility_id>\w+)/match_to/(?P<match_to_id>\d+)$', 'nmis.mopup.views.make_match', name='make_match'),
	url(r'^(?P<lga_id>\w+)/(?P<fac_type>surveyed|listed)/(?P<facility_id>\w+)/clear_match$', 'nmis.mopup.views.clear_match', name='clear_match'),
)


