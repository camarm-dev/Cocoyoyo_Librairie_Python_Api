from pprint import pprint
from cocoyoyo_librairie.api import CocoyoyoLibrairie, CocoyoyoLibrairie_Exception

""" If you want to disable the message on init: """
# module = CocoyoyoLibrairie(False)
""" else: """
module = CocoyoyoLibrairie()

search = module.search('Petit')
""" Uncomment below to view result """
# pprint(search)

search_id = module.search_id(search['resultat_livres'][0]['id'])
""" Uncomment below to view result """
# pprint(search_id)

search_isbn = module.search_isbn(9791035204396)
""" Uncomment below to view result """
# pprint(search_isbn)

search_user = module.search_user('No Token')
""" Uncomment below to view result """
# pprint(search_user)

"""
I want to have doc of library
Uncomment below to view result
"""
# print(module.__doc__)

"""
I want to have doc of search() method
Uncomment below to view result
"""
# print(module.search.__doc__)


""" You can catch exceptions of API: """
try:
    search_user = module.search_user('00')
except CocoyoyoLibrairie_Exception as e:
    print(f'An exception occurred !\n{e.__class__}: {"".join(e.args)} !')
