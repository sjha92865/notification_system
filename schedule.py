from crontab import CronTab



def schedule(arr):
    #print(type(arr[0]))
    d={'CHG': '11/02/2022, 23:04:00'}
    #print(d)
    dd=list(arr[0].items())
    dd=dd[:3]
    cron = CronTab(user='shubhamjha')
    cron.remove_all()
    for i in dd:
        key=i[0]
        value=i[1]
        
        # print("hh",type(cron))
        # for job in cron:
        #     if job.comment=="CHG-72":
        #         job.hour.every(10)
        #         cron.write()
        #         print("ch-72 modified")
            # else:

                
        command='/usr/bin/python3 /Users/shubhamjha/Desktop/example1.py'+'  '+key
        job = cron.new(command=command,comment=key)
    
        value=value.replace("/", "-")
        value=value.split(',')
        value=''.join(value)
        #print(value)
        datetimeobj=datetime.datetime.strptime(value, "%d-%m-%Y %H:%M:%S")
        print("hii",datetimeobj)
        job.minute.every(1)
        # iter = cron.find_command('bar')
        # print(iter)
        # iter = cron.find_command('CHG-72')
        # print(iter)
        # job.set_command(key+'.sh')
        job.setall(datetimeobj)
        # job.setall(datetime(2000, 4, 2, 10, 2))
        # job.minute.every(1)
        cron.write()


    return
