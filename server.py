"""
A tozti extension providing discussion threads.
"""
__license__ = 'AGPL'
__author__ = 'The tozti Project'
__email__ = 'tozti@ens-lyon.fr'


"""The schema for a discussion thread."""
THREAD_SCHEMA = {
    'body': {
        'name': {
            'type': 'string'
        },
        'messages': {
            'type': 'relationship',
            'arity': 'to-many',
            'targets': 'discussion/message'
        },
        'important': {
            'type': 'relationship',
            'arity': 'to-many',
            'targets': 'discussion/message'
        },
    }
}

"""The schema for a single message."""
MESSAGE_SCHEMA = {
    'body': {
        'content': {
            'type': 'string'
        },
        'author': {
            'type': 'relationship',
            'arity': 'to-one',
            'targets': 'core/user'
        },
        'parent': {
            'type': 'relationship',
            'arity': 'to-one',
            'targets': 'discussion/message'
        },
        'replies': {
            'type': 'relationship',
            'arity': 'auto',
            'pred-type': 'discussion/message',
            'pred-relationship': 'parent'
        }
    },

    'optional': ['parent']
}


MANIFEST = {
    'name': 'discussion',
    'includes': ['build.js', 'css/style.css'],
    'types': {
        'thread': THREAD_SCHEMA,
        'message': MESSAGE_SCHEMA
    }
}
