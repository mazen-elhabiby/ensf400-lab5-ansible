import ansible_runner

"""
Script to run an Ansible playbook
"""


def run_playbook(playbook_path, inventory_path):
    # Run the Ansible playbook 
    result = ansible_runner.run(private_data_dir='.',
                                playbook=playbook_path,
                                inventory=inventory_path)

    # Check if the playbook run was successful
    if result.rc == 0:
        print("Playbook executed successfully.")
    else:
        print("Playbook execution failed.")

    print("Stats:", result.stats)

    for event in result.events:
        print(event['event'])

    print("STDOUT from playbook execution:")
    print(result.stdout.read())

if __name__ == "__main__":
    playbook_path = 'hello.yml'  
    inventory_path = 'hosts.yml' 

    run_playbook(playbook_path, inventory_path)
