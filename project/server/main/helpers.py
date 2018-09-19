import hashlib
import uuid
from flask import current_app
from datetime import datetime, timezone, timedelta


def generate_hash_from_filename(fname):
    fname = str(uuid.uuid4()) + str(fname)
    return hashlib.md5(fname.encode("utf-8")).hexdigest()


def get_path(fname):
    hashed = generate_hash_from_filename(fname)
    path_info = (fname, hashed[:2], hashed[2:4], hashed[4:6], hashed,)
    return path_info


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']


def get_date_br():
    now = datetime.now()
    diff = timedelta(hours=-3)
    tz = timezone(diff)
    sp_now = now.astimezone(tz)
    return sp_now.strftime('%Y-%m-%d')
