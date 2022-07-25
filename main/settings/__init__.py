from .base import * #ortak settingsleri import et

env_name = config('ENV_NAME')

#! env name e göre development settingsi yada production setingsii import et
if env_name == 'dev':
    from .dev import *
elif env_name == 'prod':
    from .prod import *