"""
A tozti extension providing discussion threads.
"""
__license__ = 'AGPL'
__author__ = 'The tozti Project'
__email__ = 'tozti@ens-lyon.fr'


from tozti.utils import RouterDef, json_response, BadDataError
from tozti.auth.decorators import restrict_known_user
from aiohttp import web
from uuid import UUID
import logbook


"""The RPC routes."""
router = RouterDef()
reply_route = router.add_route('/reply')
logger = logbook.Logger('tozti.discussion')


@reply_route.post
@restrict_known_user
async def reply_post(req):
    store = req.app['tozti-store']
    json = await req.json()

    try:
        user_id = req['user']
        thread_id = UUID(json['thread_id'])
    except (KeyError, ValueError):
        return BadDataError()

    message = {
        'data': {
            'type': 'discussion/message',
            'body': {
                'content': json['content'],
                'author': {'data': {'id': str(user_id)}},
            }
        }
    }

    if json['parent_id'] is not None:
        message['data']['body']['parent'] = {
            'data': {'id': str(UUID(json['parent_id']))}
        }

    # Create the message in the store.
    message = await store.create(message)

    # Link the message to its parent thread.
    relationship = {'data': [{'id': str(message['id'])}]}
    await store.item_append(thread_id, 'messages', relationship)

    return json_response({})


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
    'router': router,
    'types': {
        'thread': THREAD_SCHEMA,
        'message': MESSAGE_SCHEMA
    },
}
