from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
apikey="i8mDLqH-ZuZCNKBq2IhF7EcO1p-KbJAe2aNfn_7VDVMH"
url="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/6768c9e1-880a-4d3f-b968-bdace1208cf1"
authenticator=IAMAuthenticator(apikey)
def en2fr():
    mess=input("enter text: ")
    mess=[mess]
    lt=LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
    lt.set_service_url(url)
    translation=lt.translate(text=mess,model_id='en-fr').get_result()
    print(translation)
    return translation
def fr2en():
    mess = input("enter text: ")
    mess=[mess]
    Lt = LanguageTranslatorV3(version='2018-05-01', authenticator=authenticator)
    Lt.set_service_url(url)
    Translation = Lt.translate(text=mess, model_id='fr-en').get_result()
    print(Translation)
    return Translation
# text=input("enter text: ")
# C=en2fr(text)
# C=str(C)
# fr2en(C)