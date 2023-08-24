from flask import *  
import pandas as pd


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')


@app.route("/register_details", methods=['POST', 'GET'])
def log_in():
    return render_template('register.html')


@app.route("/sign_in_details", methods=['POST', 'GET'])
def sign_in():
    return render_template('sign.html')


@app.route("/register_parameters", methods=['POST', 'GET'])
def sign_in_parameters():
    
    output_dictionary={}
    
    if request.method == 'POST':
        
        first_name = request.form.get('first_name')
        print(first_name)
        last_name = request.form.get('last_name')
        print(last_name)
        mobile_number = request.form.get('mobile_number')
        print(mobile_number)
        email = request.form.get('email')
        print(email)
        password = request.form.get('password')
        print(password)
        password_confirmation = request.form.get('cnf_password')
        print(password_confirmation)
        
        output_dictionary['first_name']=first_name
        output_dictionary['last_name']=last_name
        output_dictionary['mobile_number']=mobile_number
        output_dictionary['email']=email
        output_dictionary['password']=password
        output_dictionary['cnf_password']=password_confirmation
        output_dictionary['balance']=1000


        df=pd.DataFrame(output_dictionary, index=[0])
        df.to_csv('sign_details.csv')

        return render_template('index.html')



@app.route("/signin_parameters", methods=['POST', 'GET'])
def log_in_parameters():
    if request.method == 'POST':
        email=request.form.get('email')
        print(email)
        password=request.form.get('password')
        print(password,'your type',type(password))

        df=pd.read_csv('sign_details.csv')
        sign_password=df['password'][0]

        print('sign_password',sign_password,'type',type(sign_password))

        if str(password)==str(sign_password):
            return render_template('services.html')
        else:
            print('wrong password')
            return redirect(url_for('log_in'))  



@app.route("/deposite")
def deposite():
    return render_template('display_amount_deposit.html')


@app.route("/deposite_parameters", methods=['POST', 'GET'])
def deposite_parameters():
    
    output_dictionary={}
    
    if request.method == 'POST':
        
        amount = int(request.form.get('amount'))

        df=pd.read_csv('sign_details.csv')
        balance=df['balance'][0]
        addition_operation=balance+amount
        df['balance']=addition_operation
        df.to_csv('sign_details.csv')
    

        return render_template('amount_deposit.html',amount=amount,balance=addition_operation)


@app.route("/withdraw")
def withdraw():
    return render_template('display_amount_withdraw.html')


@app.route("/withdraw_parameters", methods=['POST', 'GET'])
def withdraw_parameters():
    
    output_dictionary={}
    
    if request.method == 'POST':
        
        withdraw_amount = int(request.form.get('withdraw_amount'))

        df=pd.read_csv('sign_details.csv')
        balance=df['balance'][0]
        subration_operation=balance-withdraw_amount
        df['balance']=subration_operation
        df.to_csv('sign_details.csv')
    

        return render_template('amount_withdraw.html',withdraw_amount=withdraw_amount,balance=subration_operation)


@app.route("/balance")
def balance():
    df=pd.read_csv('sign_details.csv')
    balance=df['balance'][0]
    return render_template('display_balance.html',balance=balance)



@app.route("/profile", methods=['POST', 'GET'])
def profile():
    df=pd.read_csv('sign_details.csv')
    first_name=df['first_name'][0]  
    print(first_name)
    last_name=df['last_name'][0]
    print(last_name)
    full_name=first_name+''+last_name
    print(full_name)
    email=df['email'][0]
    print(email)
    mobile_number=df['mobile_number'][0]
    print(mobile_number)

    return render_template('profile.html',name=full_name,email=email,mobile_number=mobile_number)


@app.route("/services_parameters", methods=['POST', 'GET'])
def services_parameters():
    if request.method == 'POST':
        services=request.form.get('radio')
        print('your services',services)
        if services =='Deposit':
            return redirect(url_for('deposite'))  # dynamic #
        elif services=='Withdraw':
            return redirect(url_for('withdraw'))
        elif services=='Profile':
            return redirect(url_for('profile'))
        elif services=='Balance':
            return redirect(url_for('balance'))
        elif services=='Exit':
            return render_template('index.html') # static #



#  run the code without giving clear screen in terminal
        
if __name__ == "__main__":
    app.run(debug=True)   
