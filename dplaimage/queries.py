from config import dpla_api_key
import random
import requests

class Query(dict):

    def __init__(self):
        self.dict = {}
        subject_field = ''
        size = 30
        p = 1
        self.dict = {'page': p, 
                 'page_size':size, 
                 "sourceResource.date.after": "1945-01-01",
                 "sourceResource.date.before": "2010-01-01",
                 "sourceResource.subject.name":"", 
                 'sourceResource.type':'image', 
                 'api_key': dpla_api_key}
        
    def __getitem__(self):
        return self.dict[item]

    def set_date_range(self,after = None,before = None ):
        if after is None:
            # Is this bad?
            after = "0001-01-01"
        if before is None:
            before = ["2040-01-01"]
        self["sourceResource.date.after"]  = after
        self["sourceResource.date.before"] = before

    def set_subject(self):
        query["sourceResource.subject.name"] = subject        

    def __iter__(self):
        # Iteration is random by default.
        # Some other kind should be allowed.
        
        base_url = 'http://api.dp.la/v2/items?'
        query = self.dict
        p = 1
        r = requests.get(base_url, params=query)
        count = r.json()['count']
        print "There are {} results.".format(count)
        query["page_size"] = 1
        while True:
            query["page"] = random.randint(1,count)
            r = requests.get(base_url, params=query)
            data = r.json()
            #return data
            for doc in data["docs"]:
                yield doc

