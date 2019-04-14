# API for Space Cloud FaaS Engines

## Installation

**Coming soon!**
```bash
```

## Quick Start

### Create Engine Instance

```python
from space_engine import Engine
engine = Engine("my-engine")
```

**Note: All instances with same engine name are automatically load balanced.**

### Register the function 
```python
def my_func(params, auth, cb):
    print("Params:", params, "Auth:", auth)
    # Do something
    res = {"ack": True, "message": "Function as a Service is Awesome!"}
    cb("response", res)

# Register function with engine
engine.register_func("my-func", my_func)
```

**Note: Enable Functions module in Space Cloud, run space-exec and nats server to be able to use it.**

## Classes

<dl>
<dt><a href="#Engine">Engine</a></dt>
<dd><p>Class representing the Space Cloud FaaS Engine Interface</p>
</dd>
</dl>

## Functions

<dl>
<dt><a href="#Callback">Callback(kind, res)</a></dt>
<dd><p>Callback function to be called before returning from function</p>
</dd>
<dt><a href="#EngineFunction">EngineFunction(params, auth, cb)</a></dt>
<dd><p>Callback function for realtime updates to the subscribed data</p>
</dd>
</dl>

<a name="Engine"></a>

## Engine
Class representing the Space Cloud FaaS Engine Interface
  
* [Engine](#Engine)
    * [Engine(engine_name, **kwargs)](#new_Engine_new)
    * [.register_func(func_name, func)](#Engine+registerFunc)

<a name="new_Engine_new"></a>

### Engine(engine_name, **kwargs)
Create an instance of the Space Cloud FaaS Engine Interface

**Kind**: Global Class

| Param | Type | Description |
| --- | --- | --- |
| engine_name | <code>str</code> | Name of the engine. |
| opts | | Connection options for NATS |

**Example**  
```python
from space_engine import Engine
engine = Engine("my-engine")
def my_func(params, auth, cb):
    print("Params:", params, "Auth:", auth)
    # Do something
    res = {"ack": True, "message": "Function as a Service is Awesome!"}
    cb("response", res)

# Register function with engine
engine.register_func("my-func", my_func)
```
<a name="Engine+registerFunc"></a>

### engine.register_func(func_name, func)
Register the function to FaaS Engine

**Kind**: instance method of [<code>Engine</code>](#Engine)  

| Param | Type | Description |
| --- | --- | --- |
| func_name | <code>str</code> | Name of the function |
| func | [<code>EngineFunction</code>](#EngineFunction) | Function to be registered |

<a name="Callback"></a>

## Callback(kind, res)
Callback to be called before returning from function.

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| kind | <code>str</code> | Type of callback action to be performed |
| res | | Data to be sent to client |

<a name="EngineFunction"></a>

## EngineFunction(params, auth, cb)
Callback for realtime updates to the subscribed data

**Kind**: global function  

| Param | Type | Description |
| --- | --- | --- |
| params | | Params received by function |
| auth | | Auth object of client. Will be undefined if request is unauthenticated |
| cb | [<code>Callback</code>](#Callback) | The callback function to be called by the function |
