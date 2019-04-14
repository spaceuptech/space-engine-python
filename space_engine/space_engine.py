"""
SpaceUp API for Space Cloud FaaS Engines
"""
import pynats
import json
from typing import Callable


class Engine:
    """
    Class representing the Space Cloud FaaS Engine Interface
    ::
        from space_engine import Engine
        engine = Engine("my-engine")

        def my_func(params, auth, cb):
            print("Params:", params, "Auth:", auth)
            # Do something
            res = {"ack": True, "message": "Function as a Service is Awesome!"}
            cb("response", res)

        # Register function with engine
        engine.register_func("my-func", my_func)

    :param engine_name: (str) Name of the engine
    :param kwargs: Connection options for NATS
    """

    def __init__(self, engine_name: str, **kwargs):
        self.engine_name = engine_name
        self.nats = pynats.NATSClient(**kwargs)

    """
        Callback function to be called before returning from function.
        Callback
        :param kind: (str) Type of callback action to be performed
        :param res: Data to be sent to client
    """

    """
       Callback function for realtime updates to the subscribed data
       EngineFunction
       :param params: Params received by function.
       :param auth: Auth object of client. Will be undefined if request is unauthenticated
       :param cb: (Callback) Callback function to be called by the function
    """

    def register_func(self, func_name: str, func: Callable):
        """
        Register the function to FaaS Engine
        :param func_name: (str) Name of the function.
        :param func: (EngineFunction) Function to be registered
        """

        subject = f'faas:{self.engine_name}:{func_name}'

        def cb(req, reply_to: str):
            # Parse the request
            req = json.loads(req)

            def _cb(kind: str, res):
                if kind == "response":
                    self.nats.publish(subject=reply_to,
                                      payload=json.dumps(res, separators=(',', ':')).encode(encoding='utf-8'))

            func(req["params"], req["auth"], _cb)

        # Subscribe to nats subject
        self.nats.subscribe(subject, queue=self.engine_name, callback=cb)


__all__ = ['Engine']
