def format_error(message, field=None, code=None):
    return [{
        'message': message,
        'field': field or '',
        'code': code or '',
    }]