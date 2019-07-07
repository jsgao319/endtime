import redis
import time
host = '192.168.91.131'
port = 6379

r = redis.Redis(host=host, port=port)
print(r)
def fanpa(f):
    def  inner(*args,**kwargs):
        iptime=time.time()
        try:
            real_ip = args[0].META['HTTP_X_FORWARDED_FOR']
            regip = real_ip.split(",")[0]
        except:
            try:
                regip = args[0].META['REMOTE_ADDR']
            except:
                regip = ""
        if r.get('de'+regip):
            return
        try:
            if int(r.get(regip+'num'))>=60:
                timedif=int(iptime)-int(r.get(regip))
                if timedif>60:
                    r.set(regip + 'num', 0, ex=3600 * 3)
                    r.set(regip, iptime, ex=3600 * 3)
                elif timedif<60:
                    r.set('de'+regip,'',ex=3600 * 3)
                    return
            elif int(r.get(regip+'num'))<60:
                r.incrby(regip+'num',1)
        except:
            r.set(regip, iptime, ex=3600*24)
            r.set(regip+'num',1,ex=3600*24)
        a=f(args[0])
        return a
    return inner
