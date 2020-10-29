# ansible_demos

## Yaml examples

### Strings

```console
'A single-quoted string in YAML'
"A double-quoted string in YAML\n"
```

```console
# Comment on a line
```

```console
# A list of tasty fruits
items:
  - Apple
  - Orange
  - Strawberry
  - Mango

# Abbreviated form
items: ['Apple', 'Orange', 'Strawberry', 'Mango']
```

```console
# An employee record dict
martin:
  name: Martin D'vloper
  job: Developer
  skill: Elite
```

## Test conn

ansible all -m ping

ubuntu_test | SUCCESS => {
    "changed": false,
    "ping": "pong"
}

## Run commands

```console
ansible all -a "df -h ."

ubuntu_test | CHANGED | rc=0 >>
Filesystem                         Size  Used Avail Use% Mounted on
/dev/mapper/ubuntu--vg-ubuntu--lv  5.9G  3.0G  2.6G  54% /
```

## To run a play

```console
ansible-playbook playbook.yml
```

## To run demos

```console
git clone https://github.com/rdnovell/ansible_demos 

cd ansible_demos

ansible-playbook include_demo/playbook.yml

ansible-playbook register_demo/playbook.yml

ansible-playbook fact_demo/playbook.yml

ansible-playbook list_demo/playbook.yml

ansible-playbook role_demo/roles.yml

ansible-playbook var_demo/main.yml

ansible-playbook var_files_demo/main.yml

ansible-playbook custom_module_demo/main.yml

ansible-playbook collections_demo/main.yml
```

