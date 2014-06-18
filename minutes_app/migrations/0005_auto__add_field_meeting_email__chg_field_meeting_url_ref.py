# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Meeting.email'
        db.add_column('minutes_app_meeting', 'email', self.gf('django.db.models.fields.EmailField')(default='arundhaj@gmail.com', max_length=75), keep_default=False)

        # Changing field 'Meeting.url_ref'
        db.alter_column('minutes_app_meeting', 'url_ref', self.gf('autoslug.fields.AutoSlugField')(unique=True, max_length=50, populate_from=None, unique_with=()))


    def backwards(self, orm):
        
        # Deleting field 'Meeting.email'
        db.delete_column('minutes_app_meeting', 'email')

        # Changing field 'Meeting.url_ref'
        db.alter_column('minutes_app_meeting', 'url_ref', self.gf('autoslug.fields.AutoSlugField')(max_length=50, unique_with=(), unique=True, populate_from='title'))


    models = {
        'minutes_app.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'action_items': ('django.db.models.fields.TextField', [], {}),
            'decisions_made': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_discussed': ('django.db.models.fields.TextField', [], {}),
            'occurred': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url_ref': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': 'None', 'unique_with': '()', 'db_index': 'True'})
        }
    }

    complete_apps = ['minutes_app']
