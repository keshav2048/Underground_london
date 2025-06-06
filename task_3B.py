from adjacency_list_graph import *
from dijkstra import *
import matplotlib.pyplot as plt

"""The imported data is stored in these two lists."""
vertices = ['Edgware Road', 'Queensbury', "St. Paul's", 'Stepney Green', 'Green Park', 'Arsenal', 'Gloucester Road',
            "King's Cross St. Pancras", 'Woodside Park', 'Barking', 'Arnos Grove', 'Ruislip Manor', 'Victoria',
            'Upminster Bridge', 'East Acton', 'Fulham Broadway', "Regent's Park", 'Stratford', 'Preston Road',
            'Bermondsey', 'Paddington', 'Piccadilly Circus', 'West Harrow', 'Wembley Central', 'Belsize Park', 'Temple',
            'Putney Bridge', 'Grange Hill', 'Park Royal', 'Cannon Street', 'North Harrow', 'South Ruislip',
            'Dagenham East', 'Manor House', 'Croxley', 'Moor Park', 'West Ruislip', 'South Kensington', 'Goldhawk Road',
            'Eastcote', 'Borough', 'Monument', 'Heathrow Terminals 1, 2, 3', 'Tottenham', 'Latimer Road', 'Euston',
            'Theydon Bois', 'Covent Garden', 'Chiswick Park', 'Kilburn Park', 'Becontree', 'Stonebridge Park',
            'Acton Town', 'Wembley Park', 'Angel', 'Walthamstow Central', 'Gunnersbury', 'Euston Square', 'West Ham',
            'Pinner', 'Southfields', 'Canada Water', "St. James's Park", 'Loughton', 'Tower Hill', 'Kentish Town',
            'Buckhurst Hill', 'Kensal Green', 'Swiss Cottage', 'Ealing Broadway', 'Barkingside', 'Dagenham Heathway',
            'Redbridge', 'Kilburn', 'Hendon Central', 'Kingsbury', 'Turnham Green', 'Roding Valley', 'Harlesden',
            'East Finchley', 'Finchley Road', 'Elephant & Castle', 'Amersham', 'Burnt Oak', 'Northolt',
            'West Kensington', 'Farringdon', 'Oval', 'Finsbury Park Victoria', 'Caledonian Road', 'Stamford Brook',
            'Plaistow', 'Gants Hill', 'Blackfriars', 'Mansion House', 'Alperton', "Queen's Park", 'East Ham',
            'Warren Street', 'Harrow & Wealdstone', 'Rickmansworth', 'Camden Town', 'Holloway Road', 'Aldgate East',
            'Holland Park', 'Sloane Square', 'Whitechapel', 'Willesden Green', 'North Greenwich', 'Hounslow West',
            'Tufnell Park', 'Highbury & Islington', 'Pimlico', 'Russell Square', 'Charing Cross', 'Chesham',
            'Stockwell', 'Bow Road', 'Hounslow Central', 'North Ealing', 'Stanmore', 'Woodford', 'Southwark',
            'Hainault', 'Chalfont & Latimer', 'South Harrow', 'Westbourne Park', 'Wood Green', 'Bank', 'Wood Lane',
            'Hatton Cross', 'South Woodford', "Shepherd's Bush Market", 'Ravenscourt Park', 'Chorleywood', 'Edgware',
            'Heathrow Terminal 5', 'Newbury Park', 'Leyton', 'Watford', 'Rayners Lane', 'Northfields', 'Bayswater',
            'Hillingdon', 'North Wembley', 'West Finchley', "Shepherd's Bush", 'East Putney', 'Vauxhall',
            'Tottenham Court Road', 'Kew Gardens', 'Seven Sisters', 'Finsbury Park', 'Ealing Common', 'West Brompton',
            'Wimbledon', 'Colindale', 'Royal Oak', 'Moorgate', 'Barons Court', 'Ruislip', 'Canning Town',
            'Ruislip Gardens', 'Ickenham', 'Oakwood', 'Baker Street', 'Northwood', 'Old Street', 'Archway',
            'West Hampstead', 'Warwick Avenue', 'Marylebone', 'Wanstead', 'Epping', 'Greenford', 'Queensway',
            'Bethnal Green', 'Holborn Central', 'Waterloo', 'Debden', 'Southgate', 'Golders Green', 'Marble Arch',
            'Turnpike Lane', 'Hyde Park Corner', "Earl's Court", 'Lancaster Gate', 'Perivale', 'Snaresbrook',
            'Mornington Crescent', 'Richmond', 'Bond Street', "St. John's Wood", 'Northwood Hills', 'Mile End',
            'Harrow-on-the-Hill', 'Notting Hill Gate', 'Chalk Farm', 'Colliers Wood', 'Tooting Broadway',
            'Hounslow East', 'Osterley', 'Fairlop', 'Brent Cross', 'Blackhorse Road', 'Aldgate', 'Lambeth North',
            'Great Portland Street', 'Hornchurch', 'Finchley Central', 'Uxbridge', 'Highgate', 'North Acton',
            'Westminster', 'Upton Park', 'Neasden', 'Hampstead', 'Boston Manor', 'Elm Park', 'Bromley-by-Bow', 'Balham',
            'Goodge Street', 'Cockfosters', 'Heathrow Terminal 4', 'London Bridge', 'Morden', 'Mill Hill East',
            'Parsons Green', 'Kensington (Olympia)', 'Embankment', 'Leytonstone', 'Chigwell', 'Wimbledon Park',
            'High Barnet', 'Leicester Square', 'Totteridge & Whetstone', 'Willesden Junction', 'Clapham Common',
            'White City', 'Canary Wharf', 'South Ealing', 'Liverpool Street', 'Upney', 'South Kenton', 'Clapham North',
            'Hanger Lane', 'Canons Park', 'Holborn', 'Kenton', 'Chancery Lane', 'Oxford Circus', 'Hammersmith',
            'Kennington', 'Bounds Green', 'Tottenham Hale', 'Brixton', 'Barbican', 'Upminster', 'Dollis Hill',
            'West Acton', 'Sudbury Town', 'Tooting Bec', 'High Street Kensington', 'Maida Vale', 'Northwick Park',
            'South Wimbledon', 'Ladbroke Grove', 'Sudbury Hill', 'Clapham South', 'Knightsbridge']
edges = [('Cannon Street', 'Monument', 1), ('Colliers Wood', 'South Wimbledon', 2),
         ('Ealing Common', 'North Ealing', 2), ('Northfields', 'Boston Manor', 2), ('Baker Street', 'Bond Street', 2),
         ('Turnham Green', 'Gunnersbury', 3), ('London Bridge', 'Bermondsey', 2),
         ('South Kensington', 'Sloane Square', 2), ('Roding Valley', 'Woodford', 4), ('Chigwell', 'Grange Hill', 2),
         ('Stratford', 'Mile End', 4), ('Southgate', 'Arnos Grove', 4), ('Canons Park', 'Queensbury', 3),
         ('Finchley Central', 'East Finchley', 4), ('Osterley', 'Hounslow East', 2), ('Fairlop', 'Barkingside', 2),
         ('Southfields', 'Wimbledon Park', 2), ('Borough', 'Elephant & Castle', 2), ('Gunnersbury', 'Kew Gardens', 2),
         ('Paddington', 'Edgware Road', 2), ('Finchley Road', 'Baker Street', 5), ('Baker Street', "Regent's Park", 2),
         ('Watford', 'Croxley', 4), ('Oxford Circus', 'Bond Street', 2), ('Harlesden', 'Willesden Junction', 2),
         ('Turnham Green', 'Chiswick Park', 2), ('Baker Street', 'Great Portland Street', 2),
         ('East Putney', 'Southfields', 2), ('Angel', 'Old Street', 3), ('Buckhurst Hill', 'Woodford', 2),
         ('East Finchley', 'Highgate', 3), ('Barking', 'East Ham', 4), ('Stonebridge Park', 'Harlesden', 2),
         ('Canning Town', 'West Ham', 3), ('Barons Court', 'Hammersmith', 3), ('Northwood Hills', 'Northwood', 3),
         ('Greenford', 'Northolt', 2), ('Parsons Green', 'Putney Bridge', 3), ('Tower Hill', 'Aldgate', 2),
         ('High Barnet', 'Totteridge & Whetstone', 4), ('Chorleywood', 'Rickmansworth', 4),
         ('Rayners Lane', 'Eastcote', 2), ('Willesden Junction', 'Kensal Green', 3),
         ('Green Park', 'Hyde Park Corner', 2), ('Victoria', 'Sloane Square', 2), ('Lancaster Gate', 'Queensway', 2),
         ('Southwark', 'London Bridge', 2), ('Knightsbridge', 'South Kensington', 2), ('Kenton', 'South Kenton', 2),
         ('Harrow-on-the-Hill', 'Wembley Park', 9), ("Earl's Court", 'West Brompton', 2), ('Oakwood', 'Southgate', 3),
         ('Redbridge', 'Wanstead', 2), ('Holborn Central', 'Covent Garden', 2), ('Ealing Common', 'Ealing Broadway', 5),
         ("Earl's Court", 'Kensington (Olympia)', 3), ('Perivale', 'Greenford', 2), ('Monument', 'Tower Hill', 2),
         ('Kentish Town', 'Camden Town', 2), ('Warren Street', 'Oxford Circus', 2), ('Farringdon', 'Barbican', 4),
         ('Clapham South', 'Balham', 2), ('Hyde Park Corner', 'Knightsbridge', 2), ('Upminster', 'Upminster Bridge', 2),
         ('Arnos Grove', 'Bounds Green', 2), ('Leicester Square', 'Charing Cross', 1),
         ('Covent Garden', 'Leicester Square', 1), ('Grange Hill', 'Hainault', 5),
         ('Northwick Park', 'Preston Road', 3), ("Shepherd's Bush Market", 'Goldhawk Road', 1),
         ('Great Portland Street', 'Baker Street', 2), ('White City', 'East Acton', 3),
         ('Caledonian Road', "King's Cross St. Pancras", 4), ('South Ruislip', 'Ruislip Gardens', 2),
         ('Bond Street', 'Marble Arch', 2), ('Liverpool Street', 'Aldgate', 3),
         ('Hatton Cross', 'Heathrow Terminal 4', 3), ('Goldhawk Road', 'Hammersmith', 2), ('Plaistow', 'West Ham', 2),
         ('Bond Street', 'Green Park', 2), ('Woodside Park', 'West Finchley', 2), ('Northolt', 'South Ruislip', 3),
         ('North Acton', 'West Acton', 2), ('Chalk Farm', 'Camden Town', 1),
         ('Goodge Street', 'Tottenham Court Road', 1), ('Paddington', 'Royal Oak', 2), ('Embankment', 'Temple', 2),
         ('North Harrow', 'Pinner', 2), ("King's Cross St. Pancras", 'Russell Square', 2),
         ('Eastcote', 'Ruislip Manor', 2), ('Oxford Circus', 'Piccadilly Circus', 2), ('Mile End', 'Bethnal Green', 2),
         ('Arsenal', 'Holloway Road', 2), ("Queen's Park", 'Kilburn Park', 2), ('Edgware Road', 'Marylebone', 1),
         ('Bow Road', 'Mile End', 2), ('Mile End', 'Stepney Green', 2), ('Ickenham', 'Hillingdon', 2),
         ("Earl's Court", 'High Street Kensington', 5), ("King's Cross St. Pancras", 'Farringdon', 2),
         ('Acton Town', 'Ealing Common', 2), ('Waterloo', 'Southwark', 2), ('Boston Manor', 'Osterley', 3),
         ('Sudbury Town', 'Sudbury Hill', 2), ('Holloway Road', 'Caledonian Road', 2),
         ('Wimbledon Park', 'Wimbledon', 4), ('Newbury Park', 'Gants Hill', 3), ('Tooting Bec', 'Tooting Broadway', 2),
         ('Stamford Brook', 'Turnham Green', 1), ('Royal Oak', 'Westbourne Park', 2),
         ('Upminster Bridge', 'Hornchurch', 2), ('Harrow-on-the-Hill', 'Northwick Park', 3),
         ('South Woodford', 'Snaresbrook', 2), ('South Kenton', 'North Wembley', 2),
         ('Wembley Central', 'Stonebridge Park', 2), ('Russell Square', 'Holborn Central', 2),
         ('Hounslow West', 'Hatton Cross', 4), ('East Acton', 'North Acton', 2), ('Latimer Road', 'Wood Lane', 2),
         ('Bank', 'London Bridge', 2), ('Preston Road', 'Wembley Park', 3), ('Uxbridge', 'Hillingdon', 4),
         ('Archway', 'Tufnell Park', 2), ("Earl's Court", 'Barons Court', 3),
         ('Farringdon', "King's Cross St. Pancras", 4), ('Blackhorse Road', 'Tottenham Hale', 3),
         ('Liverpool Street', 'Bank', 2), ('Barkingside', 'Newbury Park', 2), ('Hornchurch', 'Elm Park', 2),
         ('Gloucester Road', "Earl's Court", 2), ('Monument', 'Cannon Street', 1), ('Oval', 'Stockwell', 2),
         ("St. Paul's", 'Chancery Lane', 2), ('Notting Hill Gate', 'Bayswater', 2),
         ('Queensway', 'Notting Hill Gate', 2), ('South Kensington', 'Gloucester Road', 2),
         ("King's Cross St. Pancras", 'Euston Square', 2), ('Ravenscourt Park', 'Stamford Brook', 2),
         ('South Ealing', 'Northfields', 1), ('Westminster', 'Embankment', 1), ('Bethnal Green', 'Liverpool Street', 3),
         ('Victoria', "St. James's Park", 2), ('Clapham Common', 'Clapham South', 2), ('Northwood', 'Moor Park', 3),
         ('Snaresbrook', 'Leytonstone', 2), ('West Acton', 'Ealing Broadway', 3), ('Kingsbury', 'Wembley Park', 3),
         ('Swiss Cottage', "St. John's Wood", 2), ('Canada Water', 'Canary Wharf', 3), ('Embankment', 'Waterloo', 2),
         ('Harrow-on-the-Hill', 'Finchley Road', 16), ('Leicester Square', 'Piccadilly Circus', 1),
         ('Kew Gardens', 'Richmond', 4), ("Regent's Park", 'Oxford Circus', 2), ("St. John's Wood", 'Baker Street', 3),
         ('Hammersmith', 'Acton Town', 8), ('Kennington', 'Oval', 3), ('Moorgate', 'Bank', 2),
         ('Hammersmith', 'Turnham Green', 4), ('North Wembley', 'Wembley Central', 2),
         ('Euston Square', "King's Cross St. Pancras", 2), ('High Street Kensington', 'Notting Hill Gate', 2),
         ('Oxford Circus', 'Green Park', 2), ('Piccadilly Circus', 'Green Park', 2), ('Neasden', 'Dollis Hill', 2),
         ('Aldgate', 'Liverpool Street', 3), ('London Bridge', 'Borough', 2), ('Warwick Avenue', 'Paddington', 2),
         ("King's Cross St. Pancras", 'Euston', 2), ('Hammersmith', 'Ravenscourt Park', 2),
         ('Pinner', 'Northwood Hills', 3), ('Whitechapel', 'Aldgate East', 2), ('Becontree', 'Upney', 2),
         ('Mill Hill East', 'Finchley Central', 4), ('Chesham', 'Chalfont & Latimer', 9), ('Victoria', 'Pimlico', 2),
         ('Bounds Green', 'Wood Green', 3), ('Dagenham Heathway', 'Becontree', 3), ('Kilburn Park', 'Maida Vale', 2),
         ('West Ham', 'Bromley-by-Bow', 2), ('North Greenwich', 'Canning Town', 3), ('Ruislip', 'Ruislip Manor', 2),
         ('Notting Hill Gate', 'Holland Park', 1), ('Manor House', 'Finsbury Park Victoria', 2),
         ('Dagenham East', 'Dagenham Heathway', 2), ('Sudbury Hill', 'South Harrow', 3),
         ('Aldgate East', 'Tower Hill', 3), ('Walthamstow Central', 'Blackhorse Road', 3),
         ('East Ham', 'Upton Park', 2), ('Hanger Lane', 'Perivale', 3), ('Mansion House', 'Blackfriars', 2),
         ('Loughton', 'Buckhurst Hill', 3), ('Blackfriars', 'Temple', 1), ('Euston Square', 'Great Portland Street', 2),
         ('Hatton Cross', 'Heathrow Terminals 1, 2, 3', 4), ('Gloucester Road', 'South Kensington', 3),
         ('Wembley Park', 'Neasden', 4), ('Warren Street', 'Goodge Street', 2), ('West Hampstead', 'Finchley Road', 1),
         ('Blackfriars', 'Mansion House', 2), ('Brent Cross', 'Golders Green', 3), ('Putney Bridge', 'East Putney', 3),
         ('Lambeth North', 'Elephant & Castle', 3), ('Kilburn', 'West Hampstead', 2), ('Holborn', 'Tottenham', 2),
         ('Stockwell', 'Brixton', 2), ('Warren Street', 'Euston', 1), ('Maida Vale', 'Warwick Avenue', 1),
         ('Park Royal', 'Alperton', 2), ('Clapham North', 'Clapham Common', 2), ('Baker Street', 'Edgware Road', 3),
         ('West Brompton', 'Fulham Broadway', 2), ('Bayswater', 'Notting Hill Gate', 2),
         ('Embankment', 'Westminster', 1), ('Moorgate', 'Barbican', 2), ('Barbican', 'Moorgate', 2),
         ('Tufnell Park', 'Kentish Town', 1), ('Temple', 'Blackfriars', 1), ('Marble Arch', 'Lancaster Gate', 3),
         ('West Kensington', 'Barons Court', 2), ('Golders Green', 'Hampstead', 4),
         ('Harrow & Wealdstone', 'Kenton', 2), ('Harrow-on-the-Hill', 'North Harrow', 3),
         ('Eastcote', 'Rayners Lane', 2), ('Wood Lane', "Shepherd's Bush Market", 2), ('Balham', 'Tooting Bec', 2),
         ('Queensbury', 'Kingsbury', 2), ('Amersham', 'Chalfont & Latimer', 4), ('Liverpool Street', 'Moorgate', 2),
         ('Westminster', "St. James's Park", 2), ('Finchley Road', 'Swiss Cottage', 2),
         ('Hounslow East', 'Hounslow Central', 1), ('Bromley-by-Bow', 'Bow Road', 2), ('Ruislip', 'Ickenham', 4),
         ('Aldgate East', 'Liverpool Street', 3), ("St. James's Park", 'Victoria', 2), ('South Wimbledon', 'Morden', 3),
         ("Shepherd's Bush", 'White City', 3), ('Turnpike Lane', 'Manor House', 4), ('Waterloo', 'Lambeth North', 2),
         ('Chiswick Park', 'Acton Town', 2), ('North Ealing', 'Park Royal', 2), ('Turnham Green', 'Acton Town', 4),
         ('Cannon Street', 'Mansion House', 2), ('Rayners Lane', 'West Harrow', 3), ('Bayswater', 'Paddington', 2),
         ('Stepney Green', 'Whitechapel', 3), ('Sloane Square', 'Victoria', 2), ('Paddington', 'Bayswater', 2),
         ('Stockwell', 'Clapham North', 2), ('Bank', "St. Paul's", 2), ('Cockfosters', 'Oakwood', 2),
         ('Upton Park', 'Plaistow', 2), ('Leytonstone', 'Leyton', 2), ('Hampstead', 'Belsize Park', 3),
         ('West Finchley', 'Finchley Central', 2), ('Charing Cross', 'Embankment', 1),
         ('Notting Hill Gate', 'High Street Kensington', 2), ('Westminster', 'Waterloo', 2),
         ("King's Cross St. Pancras", 'Angel', 3), ('Tottenham', 'Oxford Circus', 1), ('Marylebone', 'Baker Street', 2),
         ('Camden Town', 'Mornington Crescent', 2), ('Sloane Square', 'South Kensington', 2),
         ('Waterloo', 'Kennington', 3), ('Heathrow Terminals 1, 2, 3', 'Heathrow Terminal 5', 4),
         ('Fulham Broadway', 'Parsons Green', 2), ('Acton Town', 'South Ealing', 3),
         ('Piccadilly Circus', 'Charing Cross', 2), ('West Ham', 'Stratford', 2), ('Gants Hill', 'Redbridge', 2),
         ('Great Portland Street', 'Euston Square', 2), ('Hainault', 'Fairlop', 2), ('Epping', 'Theydon Bois', 3),
         ('Tooting Broadway', 'Colliers Wood', 2), ('Moor Park', 'Harrow-on-the-Hill', 14),
         ('Green Park', 'Victoria', 2), ('North Acton', 'Hanger Lane', 3), ('Croxley', 'Moor Park', 4),
         ("St. James's Park", 'Westminster', 2), ('Green Park', 'Westminster', 2), ('Debden', 'Loughton', 2),
         ('Wanstead', 'Leytonstone', 2), ('Upney', 'Barking', 3), ('Ruislip Manor', 'Eastcote', 2),
         ('Edgware', 'Burnt Oak', 4), ('Canary Wharf', 'North Greenwich', 3), ('Moorgate', 'Liverpool Street', 2),
         ('Belsize Park', 'Chalk Farm', 2), ('Westbourne Park', 'Ladbroke Grove', 2), ('Euston', 'Camden Town', 4),
         ('Ruislip Manor', 'Ruislip', 2), ('Colindale', 'Hendon Central', 3), ('Temple', 'Embankment', 2),
         ('Willesden Green', 'Kilburn', 2), ('Hillingdon', 'Ickenham', 2), ('Woodford', 'South Woodford', 3),
         ('Wood Green', 'Turnpike Lane', 2), ('Highbury & Islington', "King's Cross St. Pancras", 3),
         ('West Harrow', 'Harrow-on-the-Hill', 2), ('Ruislip Gardens', 'West Ruislip', 2),
         ('Hendon Central', 'Brent Cross', 2), ('Roding Valley', 'Chigwell', 3),
         ('Chalfont & Latimer', 'Chorleywood', 4), ('Highgate', 'Archway', 3), ('Bermondsey', 'Canada Water', 2),
         ('Tottenham Court Road', 'Leicester Square', 2), ('Alperton', 'Sudbury Town', 3),
         ('Theydon Bois', 'Debden', 3), ('Finsbury Park', 'Highbury & Islington', 2),
         ('Dollis Hill', 'Willesden Green', 2), ('Euston', 'Warren Street', 2), ('Rickmansworth', 'Moor Park', 5),
         ('Kensal Green', "Queen's Park", 2), ('Vauxhall', 'Stockwell', 3), ('Wembley Park', 'Finchley Road', 7),
         ('Tottenham Hale', 'Seven Sisters', 2), ('Hounslow Central', 'Hounslow West', 3),
         ('Old Street', 'Moorgate', 2), ('Stanmore', 'Canons Park', 4), ("Earl's Court", 'West Kensington', 2),
         ('Chancery Lane', 'Holborn', 1), ('Elephant & Castle', 'Kennington', 2),
         ('Finsbury Park Victoria', 'Arsenal', 1), ('Euston', "King's Cross St. Pancras", 2),
         ('Ickenham', 'Ruislip', 2), ('Burnt Oak', 'Colindale', 2), ('Seven Sisters', 'Finsbury Park', 5),
         ('Pimlico', 'Vauxhall', 2), ('Barbican', 'Farringdon', 1), ('Edgware Road', 'Paddington', 3),
         ('South Harrow', 'Rayners Lane', 5), ('Mansion House', 'Cannon Street', 2),
         ('Holland Park', "Shepherd's Bush", 2), ('Totteridge & Whetstone', 'Woodside Park', 2),
         ('Mornington Crescent', 'Euston', 2), ('Ladbroke Grove', 'Latimer Road', 2), ('Tower Hill', 'Monument', 2),
         ('Bank', 'Waterloo', 5), ('Elm Park', 'Dagenham East', 3), ('Leyton', 'Stratford', 3),
         ('High Street Kensington', 'Gloucester Road', 3), ('Hillingdon', 'Uxbridge', 4)]

"""The weighted graph is created using the AdjacencyListGraph class from adjacency_list_graph."""
graph1 = AdjacencyListGraph(len(vertices), False, True)
for edge in edges:
    try:  # This stops the runtime error if an edge that already exist is inserted.
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), 1)
    # The weight above is 1 as this task requires us to count the number of stations.
    except RuntimeError:  # If an edge already exists we just ignore it because all the weights
        # are the same.
        pass

pred = []
outcomes = []
possible_outcome = []
final = []
route = []

"""The dijkstra algorithm is ran from all the vertices and outcomes are stored in 'outcomes'."""
for i in vertices:
    d, pi = dijkstra(graph1, vertices.index(i))
    for j in range(len(vertices)):
        pred.append({"vertices": vertices[j], "pred": None if pi[j] is None else vertices[pi[j]], "dist": str(d[j])})
        if str(d[j]) != "0":  # This stops the outcome from being appended when both stations are same.
            outcomes.append(int(str(d[j])))

d = 0
x = len(vertices)
"""This stores all the outcomes of the dijkstra algorithm"""
for i in range(len(vertices)):
    final.append(pred[d:x])
    d += len(vertices)
    x += len(vertices)

"""Generates all the possible outcome"""
# This is needed to get the longest route
for i in vertices:
    for j in vertices:
        if i != j:
            possible_outcome.append((i, j))


# This function is used to find the route. It uses preda which is the list of all stations distance and there
# predecessors from the starting point
def connector(prede, st, preda):
    # The "prede" is the destination and "st" is the starting point.
    for i in preda:
        if i["vertices"] == prede:
            if i["pred"] != None:
                route.append(i["pred"])
            if i["pred"] == st:
                break
            else:
                connector(i["pred"], st, preda)

"""Fetches the index of the longest route"""
s = 0
for i in outcomes:
    if s <= i:
        s = i
        index = outcomes.index(i)

"""Prints the longest route"""
longest_route = possible_outcome[index]
print(f"The number of stations are {s} from {longest_route[0]} to {longest_route[1]}")
connector(longest_route[1], longest_route[0], final[vertices.index(longest_route[0])])
route.insert(0, longest_route[1])
print(f"the route taken is {route[::-1]}")


"""Plots the histogram using hist from matplotlib.pyplot library"""
plt.hist(outcomes, bins=int((max(outcomes)) - 1), edgecolor='black')
plt.xlabel('Time Taken (in Minutes)')
plt.ylabel('Frequency')
plt.title('Histograms and Longest Path (in Minutes)')
plt.show()  # Prints the graph
