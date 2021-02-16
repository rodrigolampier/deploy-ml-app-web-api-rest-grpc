"""

from flask_restplus import Api
from log import log
from config import api_restplus_config as config

api = Api(version=config.VERSION,
          title=config.TITLE,
          description=config.DESCRIPTION,
          prefix=config.PREFIX,
          doc=config.DOC
          )


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)
    return {'message': message}, 500

    """
