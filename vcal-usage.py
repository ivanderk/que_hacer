from datetime import datetime
from pytz import timezone
import vcal_artesanal

#import vcal_battery 

beginevent = datetime.strptime("28/03/2023 09:00",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
endevent = datetime.strptime("28/03/2023 13:50",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
ical1 = vcal_artesanal.get_ical_text("Example event", "John Doe is attending Example Event", beginevent, endevent)
print(ical1)

# beginevent = datetime.strptime("28/03/2023 09:00",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
# endevent = datetime.strptime("28/03/2023 13:50",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
# ical1 = vcal_battery.get_ical_text("Example event", "John Doe is attending Example Event", beginevent, endevent)
# print(ical1)