The program I have made is designed to convert celestial coordinates of stars (and other objects) into simple altitude and azimuth coordinates in degrees.
It was planned to make use of APIs to retrieve information regarding location of both the telescope and the stars, however, due to technical difficulties and lack of time, the information
has been predetermined in the separate files in the folder FinalProject17.

I have designed the program such that new catalogs of objects and stars can easily be added to the list of catalogs in the event I wish to add more.

I separated the values of the objects from the actual program in order to make it easier to modify the catalogs of objects (i.e. you can add stars to stars.py
without changing the main code)

The telescope must be aligned to 0 degrees altitude (level with ground) and 0 degrees azimuth (pointed north).

The program uses geographical coordinates and time to adjust the altitude and azimuth of the stars.

Calculations:
http://www.stargazing.net/kepler/altaz.html
-All calculations I found online used J2000 time in their calculations as opposed to Python's UNIX time which starts from the epoch in 1970. I have
attempted to solve this problem in the file date_time.py in which I convert UNIX time to J2000 time and from there I used the calculations from the linked
website to calculate the Local Sidereal Time. The accuracy of the time can be improved with the use of an API.

Star Catalog:
http://www.astronexus.com/hyg
-This website is where I got a database of stars. There are other celestial objects (like galaxies and supernovae) that are available online. The star
information is in comma delineated format so in the future, the code can be designed to parse the information and make the code that much more comprehensive.
There are only a few stars in star.py solely to show proof of concept. More stars and objects can be added at a later date.

Explanation of Celestial Coordinates and Altitude/Azimuth:
http://astro.unl.edu/naap/motion1/cec_units.html
-A valuable resource for explaining how the sky is observed and marked.

Presentation and flowchart:
https://docs.google.com/presentation/d/1QtWgBbMuUF6MRJJCI5WVTiNy5luRx_h3CJccLFVjhSg/edit?usp=sharing
