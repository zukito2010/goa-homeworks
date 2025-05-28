def project_workers(*workers,**equiqments):
    for worker in workers:
        print(worker, end=' ')
    print()
    for key,value in equiqments.items():
        print(f'{key} is {value}')

project_workers('gia', 'lia', 'genadi', gloves=True, boots=True,toolbox=True)
