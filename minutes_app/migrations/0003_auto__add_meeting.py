# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Meeting'
        db.create_table('minutes_app_meeting', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('items_discussed', self.gf('django.db.models.fields.TextField')()),
            ('decisions_made', self.gf('django.db.models.fields.TextField')()),
            ('action_items', self.gf('django.db.models.fields.TextField')()),
            ('occurred', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal('minutes_app', ['Meeting'])


    def backwards(self, orm):
        
        # Deleting model 'Meeting'
        db.delete_table('minutes_app_meeting')


    models = {
        'minutes_app.meeting': {
            'Meta': {'object_name': 'Meeting'},
            'action_items': ('django.db.models.fields.TextField', [], {}),
            'decisions_made': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items_discussed': ('django.db.models.fields.TextField', [], {}),
            'occurred': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['minutes_app']
