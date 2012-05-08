# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Company'
        db.create_table('customers_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal('customers', ['Company'])

        # Adding model 'Customer'
        db.create_table('customers_customer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Company'], null=True, blank=True)),
            ('age', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
        ))
        db.send_create_signal('customers', ['Customer'])

        # Adding model 'Interaction'
        db.create_table('customers_interaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('kind', self.gf('django.db.models.fields.IntegerField')()),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['customers.Customer'])),
            ('what', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('customers', ['Interaction'])

    def backwards(self, orm):
        # Deleting model 'Company'
        db.delete_table('customers_company')

        # Deleting model 'Customer'
        db.delete_table('customers_customer')

        # Deleting model 'Interaction'
        db.delete_table('customers_interaction')

    models = {
        'customers.company': {
            'Meta': {'object_name': 'Company'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        'customers.customer': {
            'Meta': {'object_name': 'Customer'},
            'age': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Company']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'})
        },
        'customers.interaction': {
            'Meta': {'object_name': 'Interaction'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['customers.Customer']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'kind': ('django.db.models.fields.IntegerField', [], {}),
            'what': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['customers']