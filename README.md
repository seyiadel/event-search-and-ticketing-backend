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
* GET `/accounts/google/login` - User Registration through Google SignIn [Oauth2.0]
* POST `/organization/create` - Create an Organization for User(organization is to group events created to a sector, a user can create an event for different organization)
* POST `/dashboard/organization/{organization_id}/add-bank-detail/` - To enable user withdraw ticket earnings per event in an organization. Note: To add the bank code, you send a GET request to `/list-bank/` which list the available banks, then you pull the bank name and bank code from the list - Associating the bank name  and bank code as an ENUM, the user selects the bank name but the bank code is sent to the API to verify the details given and get stored.
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
