from django.utils.functional import SimpleLazyObject
from django.contrib.auth.models import AnonymousUser

def get_user_groups(request):
    user = SimpleLazyObject(lambda: getattr(request, 'user', None))
    if user is None or isinstance(user, AnonymousUser):
        return {}

    groups = {
        'is_admin': user.groups.filter(name='administrador').exists(),
        'is_auditor': user.groups.filter(name='auditor').exists(),
        'is_comprador': user.groups.filter(name='comprador').exists(),
        'is_logistica': user.groups.filter(name='encargado_logistica').exists(),
        'is_gestor': user.groups.filter(name='gestor_inventario').exists(),
    }

    return groups

def user_groups_context_processor(request):
    groups = get_user_groups(request)
    return groups