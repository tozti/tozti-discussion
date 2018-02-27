MANIFEST = {
    'includes': ['build.js', 'css/style.css'],
    'types': {
      'message': {
        'body': {
          'date': { 'type': 'date' },
          'content': { 'type': 'string' },
          'author': { 
            'type': 'relationship',
            'arity': 'to-one',
            'targets': 'core/user'
          },
          'answers': { 
            'type': 'relationship',
            'arity': 'to-many',
            'targets': 'tozti-discussion/answer'
          }
        }
      }
      'answer': {
        'body': {
          'date': { 'type': 'date' },
          'content': { 'type': 'string' },
          'author': { 
            'type': 'relationship',
            'arity': 'to-one',
            'targets': 'core/user'
          }
        }
      }
      'thread': {
        'body': {
          'title': { 'type': 'string' },
          'messages': {
            'type': 'relationship',
            'arity': 'to-many',
            'targets': 'tozti-discussion/message',
          }
        }
      }
    }
}
