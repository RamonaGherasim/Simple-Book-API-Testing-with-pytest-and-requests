"""
API = Application Programming Interface
=> este o serie de servicii, functionalitati si elemente care asigura
comunicarea dintre un client si un server
=> API-ul asigura transferul de informatii prin intermediul unui protocol de
comunicare
=> Protocol de comunicare = o serie de reguli si metode de transmitere a
informatiei in retea
=> Cel mai cunoscut protocol este HTTP (Hyper Text Transfer Protocol) - din
motive de securitate a inceput sa functioneze cu un cerificat de securitate din
2010 si asa a rezultate protocolul HTTPS
=> Tranferul de informatii se face de regula prin intermediul unor metode HTTP

Cele mai cunoscute metode HTTP sunt:
- GET: Solicita citirea de informatii din baza de date
- POST: Face o solicitare de scriere a unei informatii COMPLET NOI in baza de date
- PUT: Solicita actualizarea COMPLETA/TOTALA a unei informatii deja existente
in baza de date
(ex: daca am clientul Ionel Popescu, cu CNP-ul 1650307312008 nascut in Zalau si
domiciliant in Cluj
Daca Ionel Popescu isi schimba domiciliul si vrem sa il actualizam cu PUT, atunci
acesta se va sterge complet din baza de date si se va recrea informatia corecta)
- PATCH: Solicita actualizarea PARTIALA a unei informatii deha existente in
baza de date
(Daca Ionel Popescu isi schimba domiciliul si vrem sa il actualizam cu PATCH,
atunci acesta se va actualiza doar pe campul care este de interes [aici adresa],
restul informatiilor ramanand la fel)
- DELETE: Se solicita stergerea informatiilor din baza de date

CODURI DE STATUS:
In ultima executarii unui request(unei cereri) prin oricare din metodele de mai
sus, se returneaza un status cod ca si raspuns. Acesta reflecta rezultatul
request-ului.
    Codurile de raspuns se grupeaza astfel:
    1. Coduri informationale (1XX) - sunt coduri care reflecta faptul ca o
    informatie a fost pur si simplu procesata
    2. Coduri de succes (2XX) - sunt coduri care reflecta faptul ca informatia
    a fost procesata cu succes.
        200 => informatia a fost citita cu succes
        201 => informatia a fost creata sau modificata cu succes (apare atunci
                cand scriem informatii de orice fel in baza de date)
        204 => informatia a fost stearsa cu succes
    3. Coduri de redirectionare (3XX) - pagina pe care am accesat-o a fost
    mutata la o alta adresa
    4. Coduri de eroare client (4XX) - inseamna ca utilizatorul/clientul a
    transmis o informatie gresita
        400 => informatia transmisa este invalida si nu poate fi procesata
        401 => unauthorised, adica utilizatorul nu este logat si sistemul nu
                poate decide daca acesta are acces sau nu la anumite informatii
        403 => forbidden, inseamna ca utilizatorul este logat dar nu este
                autorizat sa acceseze anumite informatii
        404 => pagina nu a fost gasita
    5. Coduri de eroare server (5XX)
        500 => Internal Server Error, adica informatia transmisa catre server
                cel mai probabil a fost corecta, dar serverul nu a putut sa o
                proceseze
        503 => Service Unavailable, adica serverul care ar rebui sa proceseze
                informatia nu functioneaza
        Se foloseste de multe ori atunci cand aplicatia este in mentenanta
    Pentru mai multe info: https://en.wikipedia.org/wiki/List_of_HTTP_status_codes


Postman = Tool de testare manuala de API
Postman are ca si componente asa numitele colectii - o serie de request-uri de
API pe care le putem folosi (pentru a primi respons-uri).

!!!! REQUEST: O solicitare de tranfer de date pentru sciere, citire, modificare
sau stergere
CRUD = CREATE, READ, UPDATE, DELETE
Componentele unui request:
1. HOST - link-ul de baza al oricarui request (e.g. www.google.com)
2. ENDPOINT - extensie a unui request, adica activitatea efectiva pe care vrem
sa o facem (e.g. www.google.com/maps@coordinates...) URI = endpoint
Pentru mai multe detalii: https://www.tutorialspoint.com/http/http_quick_guide.htm

!!!! RESPONSE: rezultatul unui REQUEST, returnat in JSON
JSON = JavaScript Object Notation
=> Un format simplu de transmitere de date mai ales de tip API
Pentru mai multe detalii: https://www.w3schools.com/js/js_json_intro.app

Link Introducere in API: https://www.youtube.com/watch?v=vCJVFnepECc&list=PLUDwpEzHYYLuW9XEvFEJk2kqsk6HqscI4&index=1


Postman - API used: https://github.com/vdespa/introduction-to-postman-course/blob/main/simple-books-api.md
"""

# Install-uri necesare: requests si pytest
