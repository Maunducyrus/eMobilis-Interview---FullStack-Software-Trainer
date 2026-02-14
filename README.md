"# eMobilis-Interview---FullStack-Software-Trainer" 
@api_view decorator - It turns a regular Django function into an API view. It ensures the function can handle specific HTTP methods (like GET or POST)

StudentSerializer - The Serializer acts as a translator.
In GET: It converts database objects into JSON.

In POST/PUT: It takes incoming JSON, validates it (checks if data is correct), and converts it back into a database object.

get_object_or_404 - It's a defensive coding practice. If a user tries to edit a student with an ID that doesn't exist, get() would crash the server with an error.

Response and others return render. Why?" - student_list (API): Returns raw JSON data. This is used for decoupled frontends or mobile apps.

student_ui_list (UI): Returns an HTML template (list.html). This is used for traditional server-side rendered websites

What happens if a user sends empty or bad data to the POST method? - The Answer: I use if serializer.is_valid():. If the data is bad (e.g., an invalid email format), the code skips the .save() and returns serializer.errors with a 400 Bad Request status.