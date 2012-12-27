# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'State'
        db.create_table('tx_locations_state', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('abbreviation', self.gf('django.db.models.fields.CharField')(max_length=10)),
        ))
        db.send_create_signal('tx_locations', ['State'])

        # Adding model 'City'
        db.create_table('tx_locations_city', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('state', self.gf('django.db.models.fields.related.ForeignKey')(related_name='cities', to=orm['tx_locations.State'])),
        ))
        db.send_create_signal('tx_locations', ['City'])


    def backwards(self, orm):
        # Deleting model 'State'
        db.delete_table('tx_locations_state')

        # Deleting model 'City'
        db.delete_table('tx_locations_city')


    models = {
        'tx_locations.city': {
            'Meta': {'object_name': 'City'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'state': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'cities'", 'to': "orm['tx_locations.State']"})
        },
        'tx_locations.state': {
            'Meta': {'object_name': 'State'},
            'abbreviation': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '250'})
        }
    }

    complete_apps = ['tx_locations']