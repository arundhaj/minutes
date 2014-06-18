# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Meeting.url_ref'
        db.add_column('minutes_app_meeting', 'url_ref', self.gf('autoslug.fields.AutoSlugField')(default=datetime.date(2013, 2, 28), unique_with=(), populate_from='title', max_length=50, unique=True, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Meeting.url_ref'
        db.delete_column('minutes_app_meeting', 'url_ref')


    models = {
        'minutes_app.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'action_items': ('django.db.models.fields.TextField', [], {}),
            'decisions_made': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_discussed': ('django.db.models.fields.TextField', [], {}),
            'occurred': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'url_ref': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'title'", 'unique_with': '()', 'db_index': 'True'})
        }
    }

    complete_apps = ['minutes_app']
