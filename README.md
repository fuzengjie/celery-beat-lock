# django-celerybeat-lock
Locked celerybeat scheduler for running celerybeat on multiple nodes


## Usage
```
$ celery beat -A myapp -S django_celerybeat_lock:LockedPersistentScheduler
```

## Django Settings
```
# Number of seconds a node can hold the lock
CELERYBEAT_LOCK_TIMEOUT = <int> # Default: 5

# The name of the cache key of the lock
CELERYBEAT_LOCK_KEY = <str> # Default: celerybeat-lock

# The name of the cache in Django's CACHES setting
CELERYBEAT_LOCK_CACHE = <str> # Default: default
# The name of the celery beat Django's CACHES setting 
CELERYBEAT_LOCK_INSTANCE = <str> # Default:localhost 
```

## Example settings
```
...
import django_cache_url
...
CACHES {
    'default': django_cache_url.config(),
    'celery-broker': django_cache_url.parse("redis://localhost:6379/0")
}
CELERYBEAT_LOCK_TIMEOUT = 60
CELERYBEAT_LOCK_KEY = "celerybeat-lock"
CELERYBEAT_LOCK_CACHE = "celery-broker"
```
