import datetime

def time_now():
    return datetime.datetime.now()

def time_elap_now(time):
    return time-time_now()

def to_sec(time):
    return time.total_seconds()


class Parser(object):
    def __init__(self, text):
        self.args = text.split(" ")
        self.assumes = dict()
        self.types = dict()
        return 


    def setAssum(self, arg_type, key, assum):
        self.setType(arg_type, key)
        if type(assum) is not list:
            assum = [assum]
        for a in assum:
            if key not in self.assumes:
                self.assumes[key] = set()
            self.assumes[key].add(a)

    
    def setType(self, arg_type, key):
        self.types[key] = arg_type

    def _getArgs(self, key):
        args = list()

        if key not in self.assumes:
            self.assumes[key] = set()
        self.assumes[key].add(key)
        
        for k in self.assumes[key]:
            if k in self.args:
                try:
                    data = self.args[self.args.index(k)+1]
                    if key in self.types:
                        data = self.types[key](data)
                except:
                    data = None


                args.append(data)
        return args

    def __getitem__(self, key):
        if type(key) == int:
            data = self.args[key] 
            if key in self.types:
                data = self.types[key](data)
            return data
        return self._getArgs(key)

    def __len__(self):
        return len(self.args)
