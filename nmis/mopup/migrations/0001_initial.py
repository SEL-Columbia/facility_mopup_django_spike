# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SurveyedFacility'
        db.create_table(u'mopup_surveyedfacility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('nmis_id', self.gf('django.db.models.fields.TextField')()),
            ('lga', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.LGA'], null=True, blank=True)),
        ))
        db.send_create_signal(u'mopup', ['SurveyedFacility'])

        # Adding model 'ListedFacility'
        db.create_table(u'mopup_listedfacility', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('lga', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['misc.LGA'], null=True, blank=True)),
            ('matched_facility', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='matched_facility', null=True, to=orm['mopup.SurveyedFacility'])),
        ))
        db.send_create_signal(u'mopup', ['ListedFacility'])


    def backwards(self, orm):
        # Deleting model 'SurveyedFacility'
        db.delete_table(u'mopup_surveyedfacility')

        # Deleting model 'ListedFacility'
        db.delete_table(u'mopup_listedfacility')


    models = {
        u'misc.lga': {
            'Meta': {'object_name': 'LGA'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'unique_slug': ('django.db.models.fields.TextField', [], {})
        },
        u'mopup.listedfacility': {
            'Meta': {'object_name': 'ListedFacility'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lga': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.LGA']", 'null': 'True', 'blank': 'True'}),
            'matched_facility': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'matched_facility'", 'null': 'True', 'to': u"orm['mopup.SurveyedFacility']"}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'mopup.surveyedfacility': {
            'Meta': {'object_name': 'SurveyedFacility'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lga': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['misc.LGA']", 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'nmis_id': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['mopup']