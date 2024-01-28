import configparser
import os
import subprocess

# Read host config
import config

#print('Hosts: 0: all hosts', hosts)
print('Hosts: 0: all hosts', config.hosts)
config.select_host = int(input('Please select a host: '))

while True:

    print('\nTask: \n1 Ping \n2 Check open updates \n3 Append updates \n4 Reboot \n5 Quit')
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

    def check_updates():
        if config.select_host == 0:
            print('Update check all hosts')
            for value in config.hosts.values():
                print("Check: ", value)
                login = config.remote_user + '@' + value
                subprocess.run(['ssh', login, 'dnf check-update'])
                # subprocess.run(("ssh", "<REMOTE UNAME>@<REMOTE IP/HOSTNAME>", "free", "-m"))
        else:
            print('Update check host')
            login = config.remote_user + '@' + config.hosts[config.select_host]
            subprocess.run(['ssh', login, 'dnf check-update'])
            #os.system("ping -c 1 " + hosts[select_host])

    def install_updates():
        if config.select_host == 0:
            print('Install updates on all hosts')
            for value in hosts.values():
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
            print('Task: Update check')
            check_updates()

        case 3:
            print('Task: Install updates')
            install_updates()

        case 4:
            print('Task: Reboot host')
            reboot_host()

        case 5:
            print("Bye!")
            quit()

        case _:
            print("Choose an option.")