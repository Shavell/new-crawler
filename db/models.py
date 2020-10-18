import os
from datetime import datetime

from peewee import *

# Set root directory of project
db = SqliteDatabase(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'sqlite.db'))


class StoreId(Model):
    id = PrimaryKeyField()
    storeUrl = CharField(unique=True)
    comment = CharField()
    created = DateTimeField(default=datetime.now)
    done = BooleanField(default=False)

    class Meta:
        database = db
        table_name = 'store_id'

class Store(Model):
    id = PrimaryKeyField()
    storeId = ForeignKeyField(StoreId, backref='stores', field='id', index=True)
    storeName = CharField(null=True)
    products = IntegerField(null=True)
    following = CharField(null=True)
    chatPerformance = CharField(null=True)
    cancellationRate = CharField(null=True)
    joined = CharField(null=True)
    followers = CharField(null=True)
    rating = CharField(null=True)
    about = CharField(null=True, max_length=2500)

    class Meta:
        database = db
        table_name = 'store'

class StoreItem(Model):
    id = PrimaryKeyField()
    store = ForeignKeyField(Store, backref='id', field='id', index=True)
    productName = CharField(null=True)
    productPrice = CharField(null=True)
    productUrl = CharField(null=True)
    productSold = CharField(null=True)

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
