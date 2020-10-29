# ansible_demos

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

