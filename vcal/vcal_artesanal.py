from datetime import datetime
from pytz import timezone

# https://docs.python.org/3/library/datetime.html
# https://pypi.org/project/pytz/


def get_ical_text(event_name, description, begin_datetime, end_datetime):
    """Generate the text bodyof an iCal/vCal event 

    parameters:
    event_name      -- Title of the event
    description     -- Description of the event
    begin_datetime  -- Date/time in which the event starts (set with timezone)
    end_datetime    -- Date/time in which the event ends (set with timezone)
"""
    if not all([event_name, begin_datetime, end_datetime]):
        return -1  # Error: empty parameters
   
    if begin_datetime > end_datetime:
        return -1  # Error: Begin Date later than End Date
    now = datetime.now(tz=timezone('CET'))
    if end_datetime < now:
        return -1  # Error: Event in the past
    
    text = f"""BEGIN:VCALENDAR
VERSION:2.0
PRODID:-//My calendar product//mxm.dk//
BEGIN:VEVENT
SUMMARY:{event_name}
DTSTART;VALUE=DATE:{datetime.strftime(begin_datetime,'%Y%m%dT%H%M%S')}
DTEND;VALUE=DATE:{datetime.strftime(end_datetime,'%Y%m%dT%H%M%S')}
DTSTAMP:{now}
DESCRIPTION:{description}
END:VEVENT
END:VCALENDAR"""
    
    return text


if __name__ == "__main__":
    
    #test positive case
    beginevent = datetime.strptime("28/03/2023 09:00",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
    endevent = datetime.strptime("28/03/2023 13:50",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
    ical1 = get_ical_text("Example event", "John Doe is attending Example Event", beginevent, endevent)
    assert type(ical1) == str 
    
    #test failure cases
    #end date before start date
    ical2 = get_ical_text("Example event", "John Doe is attending Example Event", endevent, beginevent)
    assert ical2 == -1 
   
    #end date in the past
    beginevent = datetime.strptime("28/03/2020 09:00",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
    endevent = datetime.strptime("28/03/2020 13:50",  '%d/%m/%Y %H:%M').astimezone(tz=timezone('CET'))
    ical3 = get_ical_text("Example event", "John Doe is attending Example Event", endevent, beginevent)
    assert ical3 == -1 
    
    #parameter null, empty or None
    ical4 = get_ical_text("Example event", None, endevent, beginevent)
    assert ical4 == -1 
    
    
    
