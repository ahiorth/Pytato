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
