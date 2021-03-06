from .views import mod_todo
from app import register_module


@register_module()
def setup_module(app, nav, nav_bar):
    # Register blueprint
    app.register_blueprint(mod_todo)
    # Setup main menu bar items
    nav_bar.items.append(nav.Item('ToDo', 'todo.index', constraints=[nav.Item.REQUIRELOGIN]))
