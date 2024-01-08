#%%
name='FRØY'
chars=["Å", "Ø", "Æ"]
new_chars=["AA","O","AE"]
new_name=name
for ch,nch in zip(chars,new_chars):
    new_name = new_name.replace(ch, nch)

# %%
