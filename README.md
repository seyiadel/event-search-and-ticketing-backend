# event-search-and-ticketing-backend
Want to host an event? This API allows you create events,tickets, accepts ticket payments, get the list of attendees and withdraw your ticket earnings as an organizer.

### Workflow for an organizer:

Sign Up -> Create an Organization -> Create Bank Details ->  Create an Event -> Create Tickets for Event -> Publish to Public.

### Workflow for the attendee:

List of Events -> Select an Event -> Click on Buy Tickets -> Redirect to make payments -> Payment Success [recieves Ticket Mail with detail].

To integrate the backend API to your frontend, here is the URL and the endpoints for each feature/operation.


### URL: https://event-ticketing-test-link-production.up.railway.app/
Swagger Documentation: `/swagger/` - To test API, know Required Data to be sent and Response to be received.
## Endpoints per Organizer Workflow:
* POST `/sign-up/` - Register / Sign Up User to the API.
            Input Parameters(request body) = ```{"first_name":"Oluwaloseyi", "last_name":"Adeleye", "email": "seyiadel03@gmail.com","password": "*********", "confirm_password":"*********"}```. 
      RESPONSE = ```{
  "first_name": "Oluwaloseyi",
  "last_name":"Adeleye",
  "email":"seyiadel03@gmail.com"}```
* POST`/login/` - Logs In a User ; creating the user instance. Parameters(request_body) = ```{"email":"seyiadel03@gmail.com", "password":"*********"}```. RESPONSE = ```{"expiry":"2022-04-26T087:6484:748",
  "token":"79qbq3y3y4h69202hrq2629hrqhwa9h2i7692aa7avjajve6"}```
  Note -> Prefix the <token> with "Token" before adding to the authorization header. i.e "Authorization": Token 79qbq3y3y4h69202hrq2629hrqhwa9h2i7692aa7avjajve6 .
* POST `/organization/create` - Create an Organization for User(organization is to group events created to a sector, a user can create an event for different organization) Parameters(request body) =  ```
 {
  "name": "string",
  "bio": "string",
}``` RESPONSE = ```{
  "id": 1,
  "creator": 1,
  "name": "Enterprise Events Organization",
  "bio": "hosting events with no stress",
  "tickets_sold": null,
  "created_at": "2023-06-29T21:58:34.136464Z"
  }``` .
* POST `/dashboard/organization/{organization_id}/add-bank-detail/` - To enable user withdraw ticket earnings per event in an organization. Note: To add the bank code, you send a GET request to `/list-bank/` which list the available banks, then you pull the bank "name" and bank "code" from the list - Associating the bank name  and bank code as an ENUM, the user selects the bank name and the bank code is sent to the API to verify the details given and get stored.  Request body = ```{
  "account_number":"0123456789"
  "bank_code": "50211",
}```. RESPONSE = ```{
  "id": 2,
  "account_number": 0123456789,
  "bank_name": "Central Bank",
  "bank_code": "50211",
  "account_name": "LAST_NAME, MIDDLE_NAME FIRST_NAME",
  "recipient_code": "string",
  "created_at": "2023-06-29T22:17:32.752488Z",
  "owner": 2
}```. 
* POST `/dashboard/organization/{organization_id}/event/create` - Create event by inputing its details such as Event[name, description, venue, location, country, type, start_time, start_date, end_time, end_date].
* PUT `/dashboard/organization/{organization_id}/event/{event_id}/` - Update/Make changes to the event detail.
* POST `/dashboard/events/{event_id}/tickets/create` - Create Tickets per event. Parameters: Ticket[status, price, available_tickets, start_time, start_date, end_time, end_date].
* GET `/dashboard/organization/{organization_id}/` - Get an organization by id.
* GET `/dashboard/organization/{organization_id}/events` - Get all events associated with organization
* GET `/events/{event_id}/` - Get an event by id
* GET `/events/{event_id}/tickets` - Get tickets created for an event
* POST `dashboard/organization/{organization_id}/events/{event_id}/withdraw-earnings/` - Withdraw earnings made from event tickets sales.

### Endpoints per Attendee Flow:
* GET `/events` - Get all Events
* GET `/events/{event_id}` - Get an event by id
* GET `/events/{event_id}/tickets` - Get tickets created for an event
* POST `/tickets/{ticket_id}/checkout` - Redirects to make payment for ticket
