# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Meeting.email'
        db.delete_column('minutes_app_meeting', 'email')


        # Changing field 'Meeting.occurred'
        db.alter_column('minutes_app_meeting', 'occurred', self.gf('django.db.models.fields.DateTimeField')(null=True))

    def backwards(self, orm):
        # Adding field 'Meeting.email'
        db.add_column('minutes_app_meeting', 'email',
                      self.gf('django.db.models.fields.EmailField')(default='', max_length=75),
                      keep_default=False)


        # Changing field 'Meeting.occurred'
        db.alter_column('minutes_app_meeting', 'occurred', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 6, 16, 0, 0)))

    models = {
        'minutes_app.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'action_items': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'decisions_made': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_discussed': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'occurred': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url_ref': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()'})
        }
    }

    complete_apps = ['minutes_app']