from address import Address
from mailing import Mailing

KUDA = Address("214011","Смоленск","Ленина",18,12)
OTKUDA = Address("119019 ","Москва","Никитский бульвар",5,9)
mail = Mailing(KUDA,OTKUDA,999,"ML-0901")

print(f"Отправление {mail.track} из {mail.from_address.index}, {mail.from_address.town}, {mail.from_address.street}, {mail.from_address.house} - {mail.from_address.flat} в {mail.to_address.index}, {mail.to_address.town}, {mail.to_address.street}, {mail.to_address.house} - {mail.to_address.flat}. Стоимость {mail.cost} рублей.")