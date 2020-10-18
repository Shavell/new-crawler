import os
from datetime import datetime

from peewee import *

# Set root directory of project
db = SqliteDatabase(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sqlite.db'))


class StoreId(Model):
    id        = PrimaryKeyField()
    storeUrl  = CharField(unique=True)
    comment   = CharField()
    created   = DateTimeField(default=datetime.now)
    done      = BooleanField(default=False)

    class Meta:
        database = db
        table_name = 'store_id'

class Store(Model):
    id                = PrimaryKeyField()
    storeId           = ForeignKeyField(StoreId, backref='storeid', field='id')
    storeName         = CharField(null=True, max_length=250)
    products          = CharField(null=True, max_length=250)
    following         = CharField(null=True, max_length=250)
    chatPerformance   = CharField(null=True, max_length=250)
    cancellationRate  = CharField(null=True, max_length=250)
    joined            = CharField(null=True, max_length=250)
    followers         = CharField(null=True, max_length=250)
    rating            = CharField(null=True, max_length=250)
    about             = CharField(null=True, max_length=2500)

    class Meta:
        database = db
        table_name = 'store'

class StoreItem(Model):
    id            = PrimaryKeyField()
    store         = ForeignKeyField(Store, backref='store', field='id')
    productName   = CharField(null=True)
    productPrice  = CharField(null=True)
    productUrl    = CharField(null=True)
    productSold   = CharField(null=True)

    class Meta:
        database = db
        table_name = 'store_item'


class StoreItemDetail(Model):
    pass



def generate_migrate():
    example = [
        {
            'comment': 'JYC Electronics Store',
            'storeUrl': 'https://shopee.ph/shop/165702374',
        }
    ]
    for i in example:
        StoreId.create(comment=i['comment'], storeUrl=i['storeUrl'])


if __name__ == "__main__":
    if StoreId.table_exists() is not True:
        db.create_tables([StoreId, Store, StoreItem])
        generate_migrate()
    elif StoreId.select().count() == 0:
        generate_migrate()
    else:
        print('Nothing to do. You can continue to next step.')
