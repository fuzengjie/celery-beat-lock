import socket

from celery.beat import PersistentScheduler
from django.conf import settings
from django.core.cache import caches


class LockedPersistentScheduler(PersistentScheduler):

    max_interval = getattr(settings, 'CELERYBEAT_LOCK_TIMEOUT', 5)
    lock_key = getattr(settings, 'CELERYBEAT_LOCK_KEY', "celerybeat-lock")
    cache_name = getattr(settings, 'CELERYBEAT_LOCK_CACHE', "default")
    instance = getattr(settings, 'CELERYBEAT_LOCAK_INSTANCE',socket.gethostname() )

    def tick(self):

        cache = caches[self.cache_name]
        beathost = cache.get(self.lock_key)

        if beathost is None:
            if cache.add(self.lock_key, instance, self.max_interval):
                self.logger.debug("Acquired lock Running TICK")
                return super(LockedPersistentScheduler, self).tick()

        elif instance == beathost:
            self.logger.debug("%s Running TICK" % instance)
            return super(LockedPersistentScheduler, self).tick()

        self.logger.debug("%s No TICK" % instance)
        return self.max_interval
