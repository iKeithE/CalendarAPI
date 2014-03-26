CalendarAPI
===========

Submitter: Keith Eyre, Student No: D11124850

Heroku CalendarAPI URL: http://pure-tundra-8991.herokuapp.com/


Testing:

  • Part 1 - Create a new Calendar
    
      Plan
        • Create a calendar with unique ID '100'
        • Create another calendar with a unique ID '200'
        • Create a calendar with a non-unique ID '200'
        
      Results
        • New calendar with ID 100 created sucesfully
        • New calendar with ID 200 created sucesfully
        • New calendar with ID 200 created unsucesfully - ID already taken
        
        Outputs and curl commands can be found in CreateCalendar.txt
        
  • Part 2 - Create a new entry for a calendar with unique ID 
        
      Plan
        • Create new calendar with unique ID 500
        • Create new calendar with unique ID 501
        • Create new entry with unique entry ID 1
        • Attempt to create another entry with a non-unique entry ID 1
        • Create entry in different calendar with the same ID as in another calendar
        
      Results
        • New calendar created with ID 500
        • New calendar created with ID 501
        • New calendar entry created with ID 1 in calendar with ID 500
        • New calendar entry not created with ID 1 in calendar with ID 500 - Entry ID already exists
        • New calendar entry created with ID 1 in calendar with ID 501 - No conflicts
        
        Outputs and curl commands can be found in CreateCalendarEntry.txt
        
  • Part 3 - List Calendar entries
        
      Plan
        • Create 2 calendars with unique IDs
        • Retrieve individual calendars
        • Retrieve both/ all calendars
        • Attempt to retrieve non-existing calendar
        
      Results
        • Both calendars created with unique IDs 500, 501
        • Individual calendar retrieved
        • Both calendars retrieved
        • No calendar retrieved - No existing calendar 600
        
        Outputs and curl commands can be found in ListCalendars.txt
        
  • Part 4 - List individual calendar entries
  
    Plan
      • Create calendar with unique ID
      • Create 2 new entries in calendar with unique IDs
      • Retrieve individual entry using ID 1
      • Retrieve individual entry using ID 2
  
    Results
      • Created calendar with unique ID
      • Created 2 new entries in calendar with unique IDs
      • Retrieved individual entry using ID 1
      • Retrieved individual entry using ID 2
      
      Outputs and curl commands can be found in ListCalendarEntriesIndividually.txt
  
  
  • Part 5 - Delete Entry from Calendar
  
    Plan
      • Create calendar with unique ID
      • Create entry in calender with unique entry ID
      • Delete entry from calendar
      • Attempt to delete non-existing entry in calendar
      • Attempt to delete entry from non-existing calendar
        
    Results
      • Created calendar with unique ID
      • Created entry in calender with unique entry ID
      • Deleted entry from calendar
      • Attempted to delete non-existing entry in calendar - Entry does not exist
      • Attempted to delete entry from non-existing calendar - Calendar does not exist
      
      Outputs and curl commands can be found in DeleteEntryFromCalendar.txt
        
  • Part 6- Delete Calendar
  
    Plan
      • Create calendar with unique ID
      • Delete Calendar with unique ID 
      • Attempt to delete non-existing calendar with unique ID
      • Attempt to delete non-existing calendar with unique ID
        
    Results
      • Create calendar with unique ID
      • Create Entry in calendar with unique ID
      • Delete Calendar with unique ID 
      • Attempt to delete non-existing calendar with unique ID
      
      Outputs and curl commands can be found in DeleteCalendar.txt
      
      
      
        
        
        
        
        
        
