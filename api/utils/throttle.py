from rest_framework.throttling import SimpleRateThrottle
from rest_framework.exceptions import Throttled


def get_throttle_class(rate: str):
    class CustomThrottle(SimpleRateThrottle):
        scope = 'custom_scope'

        def get_cache_key(self, request, view):
            ident = request.user.id if request.user.is_authenticated else self.get_ident(
                request)
            return f"throttle_{ident}_{request.path}"

        def __init__(self):
            self.rate = rate
            super().__init__()

        def throttle_failure(self):
            # Optionally add logging or custom logic here
            raise Throttled(detail={
                "status": "FAILED",
                "message": "Limit reached. Try again later!"
            })

    return CustomThrottle
