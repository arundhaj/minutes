# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Meeting.action_items'
        db.alter_column('minutes_app_meeting', 'action_items', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Meeting.decisions_made'
        db.alter_column('minutes_app_meeting', 'decisions_made', self.gf('django.db.models.fields.TextField')(null=True))

        # Changing field 'Meeting.items_discussed'
        db.alter_column('minutes_app_meeting', 'items_discussed', self.gf('django.db.models.fields.TextField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Meeting.action_items'
        db.alter_column('minutes_app_meeting', 'action_items', self.gf('django.db.models.fields.TextField')(default='arun'))

        # Changing field 'Meeting.decisions_made'
        db.alter_column('minutes_app_meeting', 'decisions_made', self.gf('django.db.models.fields.TextField')(default='arun'))

        # Changing field 'Meeting.items_discussed'
        db.alter_column('minutes_app_meeting', 'items_discussed', self.gf('django.db.models.fields.TextField')(default='arun'))


    models = {
        'minutes_app.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'action_items': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'decisions_made': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_discussed': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'occurred': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url_ref': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        }
    }

    complete_apps = ['minutes_app']
