# request baskets
Request Baskets is a web service to collect arbitrary HTTP requests and inspect them via RESTful API or simple web UI.

It is strongly inspired by ideas and application design of the RequestHub project and reproduces functionality offered by RequestBin service.


## Features
*   RESTful API to manage and configure baskets, see Request Baskets API documentation in interactive mode
*   All baskets are protected by unique tokens from unauthorized access; end-points to collect requests do not require authorization though
* Individually configurable capacity for every basket
* Pagination support to retrieve collections: basket names, collected requests
* Configurable responses for every HTTP method
* Alternative storage types for configured baskets and collected requests:
    * In-memory - ultra fast, but limited to available RAM and collected data is lost after service restart
    * Bolt DB - fast persistent storage for collected data based on embedded bbolt database (maintained fork of Bolt), service can be restarted without data loss and storage is not limited by available RAM
    * SQL database - classical data storage, multiple instances of service can run simultaneously and collect data in shared data storage, which makes the solution more robust and scaleable (PostgreSQL and MySQL are only supported at the moment)
    * Can be extended by custom implementations of storage interface

## Usage
Open http://localhost:55555 in your browser. The main page will display a list of baskets that may be accessed if the basket token is known. It is possible to create a new basket if the name is not in use.

If basket was successfully created the authorization token is displayed. It is important to remember the token because it authorizes the access to management features of created basket and allows to retrieve collected HTTP requests. The token is temporary stored in browser session to simplify UI integration and improve user experience. However, once browser tab is closed, the token will be lost.

To collect HTTP requests send them (GET, POST, PUT, DELETE, etc.) to http://localhost:55555/<basket_name>

To view collected requests and manage basket: Open basket web UI http://localhost:55555/web/<basket_name> Use RESTful API exposed at http://localhost:55555/api/baskets/<basket_name>/...

It is possible to forward all incoming HTTP requests to arbitrary URL by configuring basket via web UI or RESTful API.

## Database
Request baskets keeps configured baskets and collected HTTP requests in memory. This data is lost after service or server restart.