#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule

class Ansible:

    def __init__(self):
        # Me traigo todo lo que esta "debajo" de "weblogic:"
        module_args = dict(
            hola=dict(type='str', required=False),
            adios=dict(type='str', required=False)
        )

        # Me creo el modulo
        module = AnsibleModule(
            argument_spec=module_args
        )

        self.module = module

        # Me creo un dict vacio para ir metiendo los resultados
        self.result = dict()

class Weblogic(Ansible):

    def __init__(self):
        # Invoca al constructor de clase Ansible
        Ansible.__init__(self)

    def hola(self):
        self.send_message('hola')

    def adios(self):
        self.send_message('adios')

    def send_message(self, action):
        message = ("action {0} <<< | soy el pinche {0} | >>> variable {1}")
        self.result[action] = message.format(action, self.module.params[action])

def main():

    # Me creo la instancia
    weblogic = Weblogic()

    # Para todos los "parametros" que me llegaron estilo "hola, adios"
    for key, value in weblogic.module.params.items():
        # Si son None ni los miro
        if value:
            # Si estan bien veo de llamar                    
            getattr(weblogic, key)()

    weblogic.module.exit_json(**weblogic.result)

if __name__ == '__main__':
    main()