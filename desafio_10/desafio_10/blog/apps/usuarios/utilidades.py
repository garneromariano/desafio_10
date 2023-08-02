def es_colaborador(user):
    return user.is_authenticated and user.perfil == 'colaborador'

def es_miembro(user):
    return user.is_authenticated and user.perfil == 'miembro'

def es_visitante(user):
    return user.is_authenticated and user.perfil == 'visitante'

def es_miembro_o_colaborador(user):
    return es_miembro(user) or es_colaborador(user)