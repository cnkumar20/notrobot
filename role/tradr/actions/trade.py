from typing import Any
# create a logger for this module

log = logger()

class Buy:
    def __init__(self,auth_conn:dict|Any) -> None:
        if auth_conn is None:
            raise ValueError("Authentication connection cannot be None.")
        if type(auth_conn) not in [dict]:
            raise TypeError("Authentication connection must be a dictionary or a valid type.")


    def execute(self,**kwargs) -> dict:
        auth = kwargs.get('auth', None)
        order_details: dict = kwargs.get('order_details', None)
        if auth is None or order_details is None:
            raise ValueError("Authentication and order details are required for buying.")
        # Simulate buy operation
        print(f"Executing buy order for {order_details} with auth {auth}")
        return {"status": "success", "details": order_details}


class Sell:
    def __init__(self,auth_conn:dict|Any) -> None:
        if auth_conn is None:
            raise ValueError("Authentication connection cannot be None.")
        if type(auth_conn) not in [dict]:
            raise TypeError("Authentication connection must be a dictionary or a valid type.")
    def execute(self,**kwargs) -> dict:
        auth = kwargs.get('auth', None)
        order_details: dict = kwargs.get('order_details', None)
        if auth is None or order_details is None:
            raise ValueError("Authentication and order details are required for selling.")
        # Simulate sell operation
        print(f"Executing sell order for {order_details} with auth {auth}")
        return {"status": "success", "details": order_details}  


