#%%


name='FRØY'
chars=["Å", "Ø", "Æ"]
new_chars=["AA","O","AE"]
new_name=name
for ch,nch in zip(chars,new_chars):
    new_name = new_name.replace(ch, nch)

#%%
def replace_chars(name):
    ''' replace Norwegian characters and space in names'''
    chars=[" ", "/","Å", "Ø", "Æ"]
    new_chars=["_","_","AA","O","AE"]
    new_name = name
    for ch,nch in zip(chars,new_chars):
        new_name = new_name.replace(ch, nch)
    return new_name
 
#%%

assert replace_chars('Å')=='Aq', "Should be Aq"
# %%

help(replace_chars)
# %%
def replace_chars(name,*,chars=[" ", "/","Å", "Ø", "Æ"],new_chars=["_","_","AA","O","AE"]):
    ''' replace Norwegian characters and space in names'''
    new_name = name
    for ch,nch in zip(chars,new_chars):
        new_name = new_name.replace(ch, nch)
    return new_name
# %%
name='16/1-12 Troldhaugen'
replace_chars(name,["_"],["/"])
# %%
name='16/1-12 Troldhaugen'
replace_chars(name,chars=["/"],new_chars=["_"])
# %%
def replace_chars(name,*,chars=[" ", "/","Å", "Ø", "Æ"],new_chars=["_","_","AA","O","AE"]):
    ''' replace Norwegian characters and space in names'''
    try:
        new_name = name
        for ch,nch in zip(chars,new_chars):
            new_name = new_name.replace(ch, nch)
        return new_name
    except:
        raise Exception('Something went wrong in replace_chars')
replace_chars(2)
# %%
def replace_chars(name,*,chars=[" ", "/"],new_chars=["","_"]):
    ''' replace Norwegian characters and space in names'''
    if type(name)!=str:
        raise ValueError('replace_chars: name must be a string')
    new_name = name
    for ch,nch in zip(chars,new_chars):
        new_name = new_name.replace(ch, nch)
    return new_name
replace_chars(2)
# %%
def replace_chars(name,*,chars=[" ", "/"],new_chars=["","_"]):
    ''' replace Norwegian characters and space in names'''
    if type(name)!=str:
        raise ValueError('replace_chars: name must be a string')
    if len(chars) != len(new_chars):
        raise ValueError('replace_chars: chars and new_chars must same size')
    new_name = name
    for ch,nch in zip(chars,new_chars):
        new_name = new_name.replace(ch, nch)
    return new_name

def test_replace_chars():
    assert replace_chars('  ') == ''
    assert replace_chars('//') == '__'
    assert replace_chars('G O//O D') =='GO__OD'
test_replace_chars()    
    
replace_chars('G O//O D')
# %%
