import yaml
import ansible_runner
import os

"""
this will ping all the hosts in the inventory file

"""
def pingHosts():
    invPath = os.path.join(os.path.dirname(__file__), 'hosts.yml')
    with open(invPath, 'r') as file:
        inventory = yaml.safe_load(file)

    groupNames = list(inventory.keys())
    groupIndex = 0

    while groupIndex < len(groupNames):
        groupName = groupNames[groupIndex]
        groupDetails = inventory[groupName]
        if 'hosts' in groupDetails:
            hostNames = list(groupDetails['hosts'].keys())
            hostIndex = 0
            while hostIndex < len(hostNames):
                hostName = hostNames[hostIndex]
                hostData = groupDetails['hosts'][hostName]
                ipAddress = hostData.get('ansible_host', 'N/A')
                print(f"Name: {hostName}, IP: {ipAddress}, Groups: {groupName}")
                pingResponse = ansible_runner.run(
                    inventory=invPath,
                    host_pattern=hostName,
                    module='ping'
                )
                if pingResponse.status == 'successful':
                    print(f"{hostName} ping: SUCCESS")
                else:
                    print(f"{hostName} ping: FAILED")
                hostIndex += 1
        groupIndex += 1

pingHosts()
