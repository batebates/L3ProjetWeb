from channels.routing import route
from room.consumers import ws_add,ws_receive,ws_disconnect
from django.conf.urls import include

room_routing = [
    # route("websocket.connect", ws_add, path=r"^/(?P<room>[a-zA-Z0-9_]+)/$"),
    route("websocket.connect", ws_add),
    route("websocket.disconnect", ws_disconnect),
    route("websocket.receive", ws_receive),
]

routing = [
    # You can use a string import path as the first argument as well.
    #include(room_routing, path=r"^/room"),
    include(room_routing),
]
