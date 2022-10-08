# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from priceloop_api.paths.api_v1_0_hello_auth import Api

from priceloop_api.paths import PathValues

path = PathValues.API_V1_0_HELLOAUTH