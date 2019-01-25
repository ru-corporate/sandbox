from boo.account.names import account_name
from boo.account.variables import DEFAULT_LOOKUP_DICT


for k,v in DEFAULT_LOOKUP_DICT.items():
    print("|"," | ".join([k,v,account_name(k)]), "|")
