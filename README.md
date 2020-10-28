# ansible_demos

Test conn

ansible all -m ping

ubuntu_test | SUCCESS => {
    "changed": false,
    "ping": "pong"
}

Run commands

ansible all -a "df -h ."
ubuntu_test | CHANGED | rc=0 >>
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  5.9G  3.0G  2.6G  54% /

To run a play

ansible-playbook playbook.yml

To run demos

git clone https://github.com/rdnovell/ansible_demos 

cd ansible_demos

ansible-playbook include_demo/playbook.yml

ansible-playbook register_demo/playbook.yml

ansible-playbook fact_demo/playbook.yml

ansible-playbook list_demo/playbook.yml

ansible-playbook role_demo/roles.yml

ansible-playbook var_demo/main.yml

ansible-playbook custom_module_demo/main.yml

