import configparser
import os
import subprocess

# Read host config
import config

for key, value in config.hosts.items():
    print(key, value)

#print('Hosts: 0: all hosts', hosts)
#print('Hosts: 0: all hosts', config.hosts)
print('0: all Hosts')
config.select_host = int(input('Please select a host: '))

while True:

    print('\nTask: \n1 Ping \n2 Clear caches \n3 Check open updates \n4 Append updates \n5 Reboot \n6 Check uptime \n0 Quit')
    select_task = int(input('\n\nPlease select a task: '))

    def check_ping():
        if config.select_host == 0:
            for value in config.hosts.values():
                print('Ping check all hosts')
                os.system("ping -c 1 " + value)
                print(value)
        else:
            print('Ping check host')
            os.system("ping -c 1 " + config.hosts[config.select_host])

    def check_uptime():
        if config.select_host == 0:
            print('Check uptime on all hosts')
            for value in config.hosts.values():
                print("\nCheck: ", value)
                login = config.remote_user + '@' + value
                subprocess.run(['ssh', login, 'uptime'])
        else:
            print('\nCheck host uptime')
            login = config.remote_user + '@' + config.hosts[config.select_host]
            subprocess.run(['ssh', login, 'uptime'])

    def clear_caches():
        if config.select_host == 0:
            print('Clear all caches')
            for value in config.hosts.values():
                print("Clean cache: ", value)
                login = config.remote_user + '@' + value
                subprocess.run(['ssh', login, 'dnf clean all'])
        else:
            print('Update check host')
            login = config.remote_user + '@' + config.hosts[config.select_host]
            subprocess.run(['ssh', login, 'dnf clean all'])            

    def check_updates():
        if config.select_host == 0:
            print('Update check all hosts')
            for value in config.hosts.values():
                print("\n*****************************")
                print("Check: ", value)
                login = config.remote_user + '@' + value
                subprocess.run(['ssh', login, 'dnf check-update'])
        else:
            print('Update check host')
            login = config.remote_user + '@' + config.hosts[config.select_host]
            subprocess.run(['ssh', login, 'dnf check-update'])

    def install_updates():
        if config.select_host == 0:
            print('Install updates on all hosts')
            for value in config.hosts.values():
                print("Check: ", value)
                login = config.remote_user + '@' + value
                subprocess.run(['ssh', login, 'sudo dnf update -y'])
        else:
            print('Install updates on host')
            login = config.remote_user + '@' + config.hosts[config.select_host]
            subprocess.run(['ssh', login, 'sudo dnf update -y'])

    def reboot_host():
        if config.select_host == 0:
            print('\n***\nJust single host usage!\n***\nChose another task.\n\n')
            pass
        else:
            print('Reboot host!')
            login = config.remote_user + '@' + config.hosts[config.select_host]
            subprocess.run(['ssh', login, 'sudo reboot'])

    match select_task:
        case 1:
            print('Task: Ping check')
            check_ping()

        case 2:
            print('Task: Clear caches')
            clear_caches()            

        case 3:
            print('Task: Update check')
            check_updates()

        case 4:
            print('Task: Install updates')
            install_updates()

        case 5:
            print('Task: Reboot host')
            reboot_host()

        case 6:
            print('Task: Check host uptime')
            check_uptime()            

        case 0:
            print("Bye!")
            quit()

        case _:
            print("Choose an option.")
