from flask import Blueprint

user_bp = Blueprint("users", 
                    __name__, 
                    url_prefix="/users", 
                    template_folder="templates/users",
                    static_folder="static"
                    )

from . import views