from flask import render_template, request, redirect, url_for

from objects.globals import app

@app.route("/profile/<int:user_id>", methods=["GET", "POST"])
async def profile(user_id):
    if request.cookies.get("login") == None:
        return redirect(url_for("index"))

    if request.method == "POST":
        if "logout" in request.form:
            resp_redirect = redirect(url_for("index"))
            resp_redirect.delete_cookie("login")
            return resp_redirect

    return render_template("profile.html", title="My Profile", user_id=user_id)