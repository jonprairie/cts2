import inspect
import traceback


class api:
    def __init__(self):
        '''api interface, takes a dict of api calls mapped to
        modules/packages that expose the functionality to fulfill
        the call. The exposed method must be named particularly.
        api call: "get_player_list" ==> method name: GetPlayerList.'''
        self.api_call_mapping = dict()

    def Update(self, api_call_mapping):
        self.api_call_mapping.update(api_call_mapping)

    def GetPackages(self):
        return set(self.api_call_mapping.values())

    def Call(self, api_call, *args, **kwargs):
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
            print "API Error:"
            print "  api function:", func_name, api_call
            print "  args:", args
            print "  kwargs:", kwargs
            print "-"*60
            print "  api traceback:"
            traceback.print_exc()
            print "-"*60
            raise Exception('exit')

        return ret_value
