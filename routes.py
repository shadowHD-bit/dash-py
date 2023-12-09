import dash
import pages.dataset.dataset as dataset
import pages.main.main as main
import pages.products.products as products
import pages.geography.geography as geography
import pages.refunds.refunds as refunds
import pages.settings.settings as settings
import pages.index.index as index
import pages.not_found.not_found_404 as not_found_404


def register_pages():
    '''
    Функция регистрации страниц дэшборда
    '''
    # Страница датасета
    dash.register_page(dataset.__name__, 
                       title="Информационная панель | Датасет",
                       name="Датасет", 
                       path='/dataset', 
                       order=5, 
                       layout=dataset.layout)

    # Главная страница
    dash.register_page(main.__name__, 
                       name="Главная",
                       title="Информационная панель | Главная", 
                       path='/main', 
                       order=0, 
                       layout=main.layout)

    # Страница статистики по товару
    dash.register_page(products.__name__, 
                       name="Товары",
                       title="Информационная панель | Товары", 
                       path='/products', 
                       order=2, 
                       layout=products.layout)

    # Страница статистики по странам
    dash.register_page(geography.__name__, 
                       name="География",
                       title="Информационная панель | География", 
                       path='/geography', 
                       order=1, 
                       layout=geography.layout)

    # Страница статистики по возвратам
    dash.register_page(refunds.__name__, 
                       name="Возвраты",
                       title="Информационная панель | Возвраты", 
                       path='/refunds', 
                       order=3, 
                       layout=refunds.layout)

    # Страница настроек
    dash.register_page(settings.__name__, 
                       title="Информационная панель | Настройки",
                       name="Настройки", 
                       path='/settings', 
                       order=4, 
                       layout=settings.layout)

    # Страница запуска приложения
    dash.register_page(index.__name__, 
                       name="Index",
                       title="Информационная панель", 
                       path='/', 
                       layout=index.layout)

    # Страница 404
    dash.register_page(not_found_404.__name__, 
                       title="Информационная панель | Уппсс!",
                       name="Страница не найдена", 
                       layout=not_found_404.layout)
