from flask import Flask, render_template, request, session


app = Flask("hello")


app.secret_key = "111"

@app.route("/", methods=['GET', 'POST'])
def index():
	try:
		balance = session["balance"]
	except KeyError:
		balance = session["balance"] = 8000


	if request.method == "GET":
		return render_template("atm.html", balance=balance, msg="")

	if request.method == "POST":

        
		if request.form["amount"] == "" :
			msg = "Amount is required"
			return render_template("atm.html", balance=balance, msg=msg)
			
		
		if int(request.form["amount"]) < 0 :
			return render_template("atm.html", balance=balance, msg="Cannot enter negative amount")

	
		if request.form["action"] == 'Withdraw':

			
			if int(request.form["amount"]) > session["balance"] :
				msg = "Cannot withdraw amount greater than balance"
				return render_template("atm.html", balance=balance, msg=msg)

			
			elif int(request.form["amount"]) > 5000 :
				msg = "Cannot withdraw amount greater than 5000"
				return render_template("atm.html", balance=balance, msg=msg)

			
			else:
				balance = balance - int(request.form["amount"])
				session["balance"] = balance
				msg = "Money Withdrawn"
				return render_template("atm.html", balance=balance, msg=msg)

		
		elif request.form["action"] == 'Deposit':

			
			balance = balance + int(request.form["amount"])
			session["balance"] = balance
			msg = "Money Deposited"
			return render_template("atm.html", balance=balance, msg=msg)


app.run()
