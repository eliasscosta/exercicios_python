import httplib
from httplib import HTTPException
try:
     host = 'www.uol.com.br'
     h = httplib.HTTPConnection(host, 80)
     h.request('GET', '/')
          
     conn = h.getresponse()
     #data = conn.read()
     if conn.status == 200:  #OK
          #f = h.getfile()
          print 'Acesso OK'
except HTTPException, e:
     print str(e)
