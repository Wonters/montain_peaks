# Mountain Peaks

Montain Peaks is api rest which plot peaks on a map

- one model store a peak location and attribute: lat, lon, altitude, name
- an api rest handle 
    * create/read/update/delete a peak
    * retrieve a list of peaks in a given geographical bounding box
    * ip filtering admin page protected 
    with user/password authentication should allow viewing rejected connections.
- a documentation for api rest accessible on api/docs url
- One view to show peak on a satelite layout

**Install**
- In the directory montain_peaks do : $ docker-compose up 
- Make the migrations : $ docker-compose run web python manage.py migrate
- Create a superuser : $ docker-compose run web python manage.py createsuperuser

** Go to the http://127.0.0.1:8000/api/ **

    


