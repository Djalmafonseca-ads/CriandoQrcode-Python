#!/usr/bin/env python
# coding: utf-8

# In[5]:


import qrcode
imagem_qrcode = qrcode.make("https://www.linkedin.com/in/djalma-neto-dev/")
imagem_qrcode.save("qrcode_perfil_linkedin.png")


# In[ ]:




