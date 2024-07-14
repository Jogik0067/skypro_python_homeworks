import pytest
from string_utils import StringUtils

stringutils = StringUtils()

#--------  ПРОВЕРКА capitilize
@pytest.mark.parametrize('tekst, itog', [
    ('testik','Testik'),('123','123'),('текст с пробелами','Текст с пробелами'),('кЕННИ','Кенни'),('кЕНнИ','Кенни'), #___POSITIVE
    ('',''),(' ',' '),('~@','~@') #___NEGATIVE
    ])
def test_big_letter(tekst,itog):
    res = stringutils.capitilize(tekst)
    assert res == itog

#-------- ПРОВЕРКА trim
@pytest.mark.parametrize('tekst, itog', [
    ('  testik','testik'), (' текст с пробелами','текст с пробелами'),('  ~@ ','~@ '),  #___POSITIVE
    ('',''), (' ',''), ('~@ ','~@ ') #___NEGATIVE
    ])
def test_del_space(tekst,itog):
    res = stringutils.trim(tekst)
    assert res == itog

#-------- ПРОВЕРКА to_list
@pytest.mark.parametrize('tekst, delit, itog', [
    ("a,b,c,d",None,["a","b","c","d"]),("253!bqw!90d",'!',["253","bqw","90d"]),("a1 b1 c1 d1",' ',['a1', 'b1', 'c1', 'd1']), #___POSITIVE
    ('',',',[]), (' ,',',',[' ','']), ("a,b+c,d",None,["a","b+c","d"]),("a1,b1,c1,d1",'1',['a', ',b', ',c', ',d', '']) #___NEGATIVE
    ])
def test_string_to_list(tekst,delit,itog):
    if delit is None:
        res = stringutils.to_list(tekst)
    else:
        res = stringutils.to_list(tekst,delit)
    assert res == itog

#-------- ПРОВЕРКА contains
@pytest.mark.parametrize('stroka, simbol, itog', [
    ('testik','t',True), ('текст с пробелами',' ',True),('1~@ ','~',True),  #___POSITIVE
    ('','G',False), ('    ','!',False), ('ТЕКСТ ПРОВЕРКИ','',False) #___NEGATIVE___!!
    ])
def test_contains(stroka,simbol,itog):
    res = stringutils.contains(stroka,simbol)
    assert res == itog

#-------- ПРОВЕРКА delete_symbol
@pytest.mark.parametrize('stroka, simbol, itog', [
    ('testik','t','esik'), ('текст с пробелами',' ','текстспробелами'),('1~@ ','~','1@ '),  #___POSITIVE
    ('','G',''), ('    ','!','    '), ('ТЕКСТ ПРОВЕРКИ','','ТЕКСТ ПРОВЕРКИ') #___NEGATIVE
    ])
def test_delete_symbol(stroka,simbol,itog):
    res = stringutils.delete_symbol(stroka,simbol)
    assert res == itog

#-------- ПРОВЕРКА starts_with
@pytest.mark.parametrize('stroka, simbol, itog', [
    ('testik','t',True), ('Текст с пробелами','Т',True),('~1@ ','~',True),  #___POSITIVE
    ('','G',False), ('    ','!',False), ('ТЕКСТ ПРОВЕРКИ','',False)   #___NEGATIVE____!!!
    ])
def test_starts_with(stroka,simbol,itog):
    res = stringutils.starts_with(stroka,simbol)
    assert res == itog

#-------- ПРОВЕРКА end_with
@pytest.mark.parametrize('stroka, simbol, itog', [
    ('testik','k',True), ('Текст с пробеламV','V',True),('~1@ ',' ',True),  #___POSITIVE
    ('','G',False), ('    ','!',False), ('ТЕКСТ ПРОВЕРКИ','',False)]) #___NEGATIVE____!!!

def test_end_with(stroka,simbol,itog):
    res = stringutils.end_with(stroka,simbol)
    assert res == itog

#-------- ПРОВЕРКА is_empty
@pytest.mark.parametrize('tekst, itog', [
    ('',True),(' ',True), #___POSITIVE
    ('Testik',False),('  123',False) #___NEGATIVE    
    ])
def test_is_empty(tekst,itog):
    res = stringutils.is_empty(tekst)
    assert res == itog

#-------- ПРОВЕРКА list_to_string
@pytest.mark.parametrize('spisok, delit, itog', [
    (["a","b","c","d"],None,'a, b, c, d'),(["253","bqw","90d"],'!',"253!bqw!90d"),(['a1', 'b1', 'c1', 'd1'],' ',"a1 b1 c1 d1"), #___POSITIVE
    ([],',',''), ([' ',''],',',' ,'), (["a","b+c","d"],None,'a, b+c, d'),(['a', ',b', ',c', ',d', ''],'1',"a1,b1,c1,d1")])#___NEGATIVE

def test_list_to_string(spisok,delit,itog):
    if delit is None:
        res = stringutils.list_to_string(spisok)
    else:
        res = stringutils.list_to_string(spisok,delit)
    assert res == itog

#-------- ПРОВЕРКА на пустой реквизит
def test_string_to_list_None_Empty():
    with pytest.raises(AttributeError):
        stringutils.capitilize(None) 
        stringutils.trim(None)
        stringutils.to_list(None)
        stringutils.contains(None,'G')
        stringutils.delete_symbol(None,'G')
        stringutils.starts_with(None,'G')
        stringutils.end_with(None,'G')
        stringutils.is_empty(None)