import os

from channels.auth import AuthMiddlewareStack
from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from django.conf.urls import url
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django_asgi_app = get_asgi_application()

from actionlog.consumers import ActionLogEntryConsumer # noqa: E402 (has to come after settings)
from adjallocation.consumers import AdjudicatorAllocationWorkerConsumer, PanelEditConsumer # noqa: E402 (has to come after settings)
from checkins.consumers import CheckInEventConsumer # noqa: E402 (has to come after settings)
from draw.consumers import DebateEditConsumer # noqa: E402 (has to come after settings)
from notifications.consumers import NotificationQueueConsumer # noqa: E402 (has to come after settings)
from results.consumers import BallotResultConsumer, BallotStatusConsumer # noqa: E402 (has to come after settings)
from venues.consumers import VenuesWorkerConsumer # noqa: E402 (has to come after settings)

application = ProtocolTypeRouter({

    # Django's ASGI application to handle traditional HTTP requests
    "http": get_asgi_application(),

    # WebSocket handlers
    "websocket": AuthMiddlewareStack(
        URLRouter([
            # TournamentOverviewContainer
            url(r'^ws/(?P<tournament_slug>[-\w_]+)/action_logs/$', ActionLogEntryConsumer.as_asgi()),
            url(r'^ws/(?P<tournament_slug>[-\w_]+)/ballot_results/$', BallotResultConsumer.as_asgi()),
            url(r'^ws/(?P<tournament_slug>[-\w_]+)/ballot_statuses/$', BallotStatusConsumer.as_asgi()),
            # CheckInStatusContainer
            url(r'^ws/(?P<tournament_slug>[-\w_]+)/checkins/$', CheckInEventConsumer.as_asgi()),
            # Draw and Preformed Panel Edits
            url(r'^ws/(?P<tournament_slug>[-\w_]+)/round/(?P<round_seq>[-\w_]+)/debates/$', DebateEditConsumer.as_asgi()),
            url(r'^ws/(?P<tournament_slug>[-\w_]+)/round/(?P<round_seq>[-\w_]+)/panels/$', PanelEditConsumer.as_asgi()),
        ]),
    ),

    # Worker handlers (which don't need a URL/protocol)
    "channel": ChannelNameRouter({
        # Name used in runworker cmd : SyncConsumer responsible
        "notifications":  NotificationQueueConsumer, # Email sending
        "adjallocation": AdjudicatorAllocationWorkerConsumer,
        "venues": VenuesWorkerConsumer,
    }),
})
