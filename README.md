# Ansible and YAML for dummies

## Yaml examples

### Strings

```yaml
'A single-quoted string in YAML'
"A double-quoted string in YAML\n"
```

### Comments
```yaml
# Comment on a line
```

### Lists
```yaml
# A list of tasty fruits
items:
  - Apple
  - Orange
  - Strawberry
  - Mango

# Abbreviated form
items: ['Apple', 'Orange', 'Strawberry', 'Mango']
```

### Dicts
```yaml
# An employee record dict
martin:
  name: Martin D'vloper
  job: Developer
  skill: Elite
```
### Transforming dictionaries into lists
```yaml
{{ dict | dict2items }}
```

### Transforming lists into dictionaries
```yaml
{{ tags | items2dict }}
```

## Ansible 

## Installation

```yaml
sudo apt-add-repository ppa:ansible/ansible
sudo apt update
sudo apt install ansible

sudo vi /etc/ansible/hosts

Output /etc/ansible/hosts
[servers]
server1 ansible_host=192.168.1.2
server2 ansible_host=192.168.1.3
server3 ansible_host=192.168.1.4

[servers:vars]
ansible_python_interpreter=/usr/bin/python3

ansible-inventory --list -y

Output
all:
  children:
    servers:
      hosts:
        server1:
          ansible_host: 192.168.1.2
          ansible_python_interpreter: /usr/bin/python3
        server2:
          ansible_host: 192.168.1.3
          ansible_python_interpreter: /usr/bin/python3
        server3:
          ansible_host: 192.168.1.4
          ansible_python_interpreter: /usr/bin/python3
    ungrouped: {}

ssh-keygen -t rsa
ssh-copy-id -i ~/.ssh/id_rsa.pub 192.168.1.2
ssh-copy-id -i ~/.ssh/id_rsa.pub 192.168.1.3
ssh-copy-id -i ~/.ssh/id_rsa.pub 192.168.1.4
```

## Demos

### Test conn

ansible all -m ping

ubuntu_test | SUCCESS => {
    "changed": false,
    "ping": "pong"
}

### Run commands

```console
ansible all -a "df -h ."

ubuntu_test | CHANGED | rc=0 >>
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  5.9G  3.0G  2.6G  54% /
```

### To run a play

```console
ansible-playbook playbook.yml
```

### To run demos

```console
git clone https://github.com/rdnovell/ansible_demos 

cd ansible_demos

ansible-playbook include_demo/main.yml

ansible-playbook register_demo/main.yml

ansible-playbook fact_demo/main.yml

ansible-playbook list_demo/main.yml

ansible-playbook role_demo/main.yml

ansible-playbook var_demo/main.yml

ansible-playbook var_files_demo/main.yml

ansible-playbook custom_module_demo/main.yml

ansible-playbook collections_demo/main.yml
```

## Details

### Run tasks in parallel for each hosts, not host linear lock

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/free_strategy.html#free-strategy

```yaml
hosts: all
  strategy: free
```
