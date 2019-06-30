import os
from datetime import datetime

from peewee import *

db = SqliteDatabase(os.path.join(os.path.dirname(__file__), '../sqlite.db'))


class TrackingCode(Model):
    id = PrimaryKeyField()
    tracking_id = CharField(unique=True)
    definition = CharField()
    created = DateTimeField(default=datetime.now)
    active = BooleanField(default=True)

    class Meta:
        database = db
        table_name = 'tracking_code'


class LogTestTransaction(Model):
    id = PrimaryKeyField()
    start = DateTimeField(default=datetime.now())
    end = DateTimeField(null=True)

    class Meta:
        database = db
        table_name = 'log_test_transaction'


class LogAction(Model):
    id = PrimaryKeyField()
    tracking_code = ForeignKeyField(TrackingCode, backref='logaction', field='tracking_id')
    captcha_key = CharField()
    start = DateTimeField()
    end = DateTimeField(default=datetime.now())
    err = BooleanField(default=True)
    err_desc = CharField(null=True, default="")
    log_test_transaction = ForeignKeyField(LogTestTransaction, backref='logtesttransaction', field='id')

    class Meta:
        database = db
        table_name = 'log_action'


class LogResult(Model):
    id = PrimaryKeyField()
    last_process_comment = CharField(null=True)
    last_process_date = DateField(formats=['%d/%m/%Y'], null=True)
    delivery_comment = CharField(null=True)
    total_fees = CharField(null=True)
    all_actions_result = BlobField(null=True)
    all_fees = BlobField(null=True)
    log_action = ForeignKeyField(LogAction, backref='logresult', field='id')

    class Meta:
        database = db
        table_name = 'log_result'


def generate_migrate():
    example = [
        {
            'definition': 'silikon, sabitleyici',
            'tracking_id': 'RV940360077CN'
        },
        {
            'definition': 'vidalama',
            'tracking_id': 'RP614332548CN'
        },
        {
            'definition': 'silikon, vidalama',
            'tracking_id': 'LL440197678CN'
        }
    ]
    for i in example:
        TrackingCode.create(definition=i['definition'], tracking_id=i['tracking_id'])


if __name__ == "__main__":
    if db.table_exists(TrackingCode) is not True:
        db.create_tables([TrackingCode, LogAction, LogResult, LogTestTransaction])
        generate_migrate()
