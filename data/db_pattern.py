from firebase_admin import db
import data.model.data_db as model
import conf.conf_db as conf


def insert_pattern(data: model.DataPattern):
    ref = db.reference(conf.TABLE_PATTERN)
    ref.child(data.title).push({
        'qty': str(data.qty),
        'free': str(data.free),
        'last_update': data.last_update,
        'pattern': data.pattern
    })


def update_pattern(data: model.DataPattern):
    ref = db.reference(conf.TABLE_PATTERN)
    ref.child(data.title).set({
        'qty': str(data.qty),
        'free': str(data.free),
        'last_update': data.last_update,
        'pattern': data.pattern
    })


def drop_table(db_name):
    ref = db.reference(db_name)
    return ref.delete()
