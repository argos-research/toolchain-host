from taskgen.event import AbstractEventHandler


class StdOutHandler(AbstractEventHandler):

    def __init__(self):
        pass

        
    def __taskset_event__(self, taskset, event):
        if event:
            print(event)
    
    def __taskset_start__(self, taskset):
        pass

    def __taskset_finish__(self, taskset):
        pass

    def __taskset_stop__(self, taskset):
        pass




