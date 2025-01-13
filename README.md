# Chicago Lobbyist Database Application

## CS 341, Fall 2024  

---

## Table of Contents
1. [Project Description](#project-description)  
2. [Database Details](#database-details)  
3. [Project Parts](#project-parts)  
   - [Part 1 – Data Access Tier](#part-1--data-access-tier)  
   - [Part 2 – Object Mapping Tier](#part-2--object-mapping-tier)  
   - [Part 3 – Presentation Tier](#part-3--presentation-tier)  

---

## Project Description

The goal of this project is to write a **console-based database application** in Python using an **N-tier design**. The data used for this project contains information pertaining to **registered lobbyists in Chicago**, their employers, their clients, and their compensation.

### Quick Facts
- The database has 8 tables:
  1. `LobbyistInfo`
  2. `LobbyistYears`
  3. `EmployerInfo`
  4. `EmployerYears`
  5. `ClientInfo`
  6. `ClientYears`
  7. `LobbyistAndEmployer`
  8. `Compensation`
- Data can be found on [Chicago’s Open Data Portal](https://data.cityofchicago.org/).

---

## Database Details

A **lobbyist** is a person who tries to influence legislation in a particular way. In Chicago, lobbyists must register with the Board of Ethics each year and file quarterly reports. The database (`Chicago_Lobbyists.db`) contains:

- **LobbyistInfo** – general information about lobbyists (ID, name, address, phone, fax, etc.).  
- **LobbyistYears** – the years in which each lobbyist is registered.  
- **EmployerInfo** and **EmployerYears** – employer details and their years of registration.  
- **ClientInfo** and **ClientYears** – client details and their years of registration.  
- **LobbyistAndEmployer** – relations tying lobbyists to employers.  
- **Compensation** – compensation amounts for lobbyists from clients.  

You can run `.schema` in SQLite to see design details.

---

## Project Parts

### Part 1 – Data Access Tier

- **File:** `datatier.py`  
- I've implemented three functions to execute SQL queries:
  1. `select_one_row()`
  2. `select_n_rows()`
  3. `perform_action()`

### Part 2 – Object Mapping Tier

- **File:** `objecttier.py`  
- I've created classes and functions that utilize the data tier (`datatier.py`) to build Python objects.  
  - Classes:
    1. `Lobbyist`
    2. `LobbyistDetails`
    3. `LobbyistClients`
  - Functions:
    - `num_lobbyists()`
    - `num_employers()`
    - `num_clients()`
    - `get_lobbyists()`
    - `get_lobbyist_details()`
    - `get_top_N_lobbyists()`
    - `add_lobbyist_year()`
    - `set_salutation()`

### Part 3 – Presentation Tier

- **File:** `main.py`  
- I've Implemented a **console-based user interface** with 5 commands:
  1. **Look up lobbyists** by name (supports `_` and `%` wildcards).  
  2. **Look up details** on a specific lobbyist by ID.  
  3. **Find the top N lobbyists** by total compensation for a given year.  
  4. **Insert** (register) a new year for a lobbyist.  
  5. **Set** or replace a lobbyist’s salutation.  



