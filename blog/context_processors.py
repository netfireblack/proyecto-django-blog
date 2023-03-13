from blog.models import Category, Article

def get_categories(request):

    # Esta consulta permite obtener todos los id de las categorias que tienen articulos publicados. Es similar a una subconsulta
    ids_categories_in_use = Article.objects.filter(public=True).values_list('categories', flat=True)
    # Esta subconsulta permite obtener los datos de la tabla categoria pero solo de las categorias que cumplan los requisitos de categorias en uso
    categories = Category.objects.filter(id__in=ids_categories_in_use).values_list('id', 'name')

    return {
        'categories': categories,
        'ids': ids_categories_in_use
    }