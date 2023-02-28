from flask import abort, render_template, request, redirect, url_for, session

def authenticate_handler(response):
    "Middleware to enforce redirect to login if not authenticated (not the 'static' route)"
    if not request.endpoint:
        #abort(404)
        return render_template('error.html', error_message="Page not found", error_description="This isn't the page you are looking for....")
  
   
    if request.endpoint in 'static':
        return response
    
    if request.endpoint not in ('login', 'logout') and 'user_name' not in session:
        return redirect(url_for('login', next=request.url))

    return response

   