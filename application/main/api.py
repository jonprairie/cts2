class api:
    def __init__(self, api_call_mapping):
        '''api interface, takes a dict of api calls mapped to
        modules/packages that expose the functionality to fulfill
        the call. The exposed method must be named particularly.
        api call: "get_player_list" ==> method name: GetPlayerList.'''
        self.api_call_mapping = api_call_mapping

    def call(self, api_call, *args, **kwargs):
        func_name = "".join(
            w.capitalize() for w in api_call.split("_")
        )
        try:
            module = self.api_call_mapping[
                api_call
            ]
            f = eval("module." + func_name)
            ret_value = f(*args, **kwargs)
        except Exception as e:
            raise e

        return ret_value
