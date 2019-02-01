from boo.account.variables import varnames_to_code
from boo.account.names import account_name
from boo.row import new_text_field_name

def _whatis(varname: str):
    """Return best guess of variable *name* text description.
    """
    if varname.endswith("_lag"):
        varname = varname[:-len("_lag")] 
    output = dict(description = "", result = "")
    desc = new_text_field_name(varname)
    if desc:
        output['result'] = "New text field"
        output['description'] = desc # ok1
        return output          
    code = varnames_to_code().get(varname)
    if not code:
        output['result'] = f"'{varname}' does not seem legal"
        return output # anything like 'zzz'
    desc = account_name(code)
    if desc:
        output['description'] = desc # 'of'
        output['result'] = f"'{varname}' found"
        return output 
    output['description'] = code
    output['result'] = f"Original text name" #inn
    return output 

def whatis(varname: str):
    return _whatis(varname)['description']