from channels.auth import AuthMiddlewareStack
from channels.routing import URLRouter, ProtocolTypeRouter
import chat_with_people.routing


application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(chat_with_people.routing.websocket_urlpatterns)
    ),
})
# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': AllowedHostsOriginValidator(
#         AuthMiddlewareStack((
#             URLRouter(
#                 chat_with_people.routing.webscoket_urlpatterns
#             )
#         ))
#     )
# })