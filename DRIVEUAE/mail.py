# This module used to send mail:
# At
# 1. Time of user registration
# 2. Time of forget password/ re-activate account
# 3. Time of slotBooking

from DRIVEUAE import module as ml

class sendmail():
    #
    # Academy Registration Mail
    class academyregistermail():
        def __init__(self, email, name , pd, uid, temp_id):
            self.email = email
            self.name = name
            self.pd = pd
            self.uid = uid
            self.temp_id = temp_id
        #
        def registration_mail(self):
            configuration = ml.sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = ml.config.mail_key
            api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
            send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                    to=[{"email": self.email ,"name": self.name}],
                                    template_id=self.temp_id,
                                    params={"name": self.name, "email": self.email, "pwd": self.pd},
                                    headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
            try:
                # Send a transactional email
                api_response = api_instance.send_transac_email(send_smtp_email)
                bcrypt = ml.Bcrypt()  # password Hashing
                pass_decode = bcrypt.generate_password_hash(self.pd).decode('utf-8')
                ml.config.user.insert_one({"userID": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode })
                ml.config.profile.insert_one({"_id": self.uid,"Name": self.name, "Email":self.email,"ContactNumber":'',"Address":'', "City":'', "State":'', "Country":'', "zipCode":''})
                ml.pprint(api_response)
            except ml.ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    #
    #
    #

    class strategiesfunnelmail():
        def __init__(self, email, name , pd, uid, temp_id):
            self.email = email
            self.name = name
            self.pd = pd
            self.uid = uid
            self.temp_id = temp_id
        #
        def registration_mail(self):
            configuration = ml.sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = ml.config.mail_key
            api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
            send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                    to=[{"email": self.email ,"name": self.name}],
                                    template_id=self.temp_id,
                                    params={"name": self.name, "email": self.email, "pwd": self.pd},
                                    headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
            try:
                # Send a transactional email
                api_response = api_instance.send_transac_email(send_smtp_email)
                bcrypt = ml.Bcrypt()  # password Hashing
                pass_decode = bcrypt.generate_password_hash(self.pd).decode('utf-8')
                if self.email in [temp['Email'] for temp in ml.config.user.find({}, {"Email":1} )]: # check user email present or not in 'academy' database if "TRUE"
                    ml.config.strategies.insert_one({"userID": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode }) # insert data only 'strategies' database
                    ml.pprint(api_response)
                else: # if emailID not in 'academy' database then store database in 'strategies', 'academy' and 'profile' database
                    ml.config.user.insert_one({"userID": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode })
                    ml.config.strategies.insert_one({"userID": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode })
                    ml.config.profile.insert_one({"userID": self.uid,"Name": self.name, "Email":self.email,"ContactNumber":'',"Address":'', "City":'', "State":'', "Country":'', "zipCode":''})
                    ml.pprint(api_response)
            except ml.ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    #
    #
    #

    class studiofunnelmail():
        def __init__(self, email, name , pd, uid, temp_id):
            self.email = email
            self.name = name
            self.pd = pd
            self.uid = uid
            self.temp_id = temp_id
        #
        def registration_mail(self):
            configuration = ml.sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = ml.config.mail_key
            api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
            send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                    to=[{"email": self.email ,"name": self.name}],
                                    template_id=self.temp_id,
                                    params={"name": self.name, "email": self.email, "pwd": self.pd},
                                    headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
            try:
                # Send a transactional email
                api_response = api_instance.send_transac_email(send_smtp_email)
                bcrypt = ml.Bcrypt()  # password Hashing
                pass_decode = bcrypt.generate_password_hash(self.pd).decode('utf-8')
                if self.email in [temp['Email'] for temp in ml.config.user.find({}, {"Email":1} )]: # check user email present or not in 'academy' database if "TRUE"
                    ml.config.studio.insert_one({"userID": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode }) # insert data only 'studio' database
                    ml.pprint(api_response)
                else: # if emailID not in 'academy' database then store database in 'studio', 'academy' and 'profile' database
                    ml.config.user.insert_one({"userID": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode })
                    ml.config.studio.insert_one({"userID": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode })
                    ml.config.profile.insert_one({"userID": self.uid,"Name": self.name, "Email":self.email,"ContactNumber":'',"Address":'', "City":'', "State":'', "Country":'', "zipCode":''})
                    ml.pprint(api_response)
            except ml.ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)
    #
    #
    #

    # mail at forget/reactivation account with parameters
    class forgetReactivate():
        def __init__(self, email, name, pd, uid, temp_id):
            self.email = email
            self.name = name
            self.pd = pd
            self.uid = uid
            self.temp_id = temp_id
        #
        def reactivate_mail(self):
            configuration = ml.sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = ml.config.mail_key
            api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
            send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                    to=[{"email": self.email ,"name": self.name}],
                                    template_id=self.temp_id,
                                    params={"name": self.name, "email": self.email, "pwd": self.pd},
                                    headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
            try:
                # Send a transactional email
                api_response = api_instance.send_transac_email(send_smtp_email)
                bcrypt = ml.Bcrypt()  # password Hashing
                pass_decode = bcrypt.generate_password_hash(self.pd).decode('utf-8')
                # again Register into Database
                ml.config.user.insert_one({"_id": self.uid, "Name": self.name, "Email":self.email, "Password":pass_decode })
                # delete Data from delete Database
                ml.config.User_delete.remove({"Email":self.email},{"Name":1, "Email":1, "Password":1, "_id":1})
                # insert data into profile Database
                ml.config.profile.insert_one({"_id": self.uid,"Name": self.name, "Email":self.email,"ContactNumber":'',"Address":'', "City":'', "State":'', "Country":'', "zipCode":''})
                ml.pprint(api_response)
            except ml.ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)

    #
    # mail to user and admin for booking a slot
    class BookingSlot():
        def __init__(self, name, email, contact, skypeID, date, country, state, uid, li, t_id):
            self.name = name
            self.email = email
            self.contact = contact
            self.skypeID = skypeID
            self.date = date
            self.country = country
            self.state = state
            self.uid = uid
            self.li = li
            self.t_id = t_id
        #
        def slotbooking(self):
            configuration = ml.sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = ml.config.mail_key
            api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
            for i in range(0,len(self.t_id),1):
                send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                        to=[{"email": self.li[i] }],
                                        template_id= self.t_id[i],
                                        params={"name": self.name, "date":self.date, "country":self.country, "skypeID":self.skypeID, "state":self.state, "email":self.email, "contact":self.contact},
                                        headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
                try:
                    # Send a transactional email
                    api_response = api_instance.send_transac_email(send_smtp_email)
                    ml.pprint(api_response)
                    if self.li[i] == self.email:
                        ml.config.timeslotBooking.insert_one({"_id":self.uid,"Name":self.name, "Email":self.email, "Contact":self.contact, "SkypeID":self.skypeID,"Date":self.date, "Country":self.country, "State":self.state})
                except ml.ApiException as e:
                    print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)


    # payment Success
    # mail to the user for successful course purchase
    class userPayment():
        def __init__(self, orderID, paymentID, userName, userEmail, contact, courseName, courseAmount, purchaseTime, line1, city, state, country, template, tt):
            self.orderID = orderID
            self.paymentID = paymentID
            self.userName = userName
            self.userEmail = userEmail
            self.contact = contact
            self.courseName = courseName
            self.courseAmount = courseAmount
            self.purchaseTime = purchaseTime
            self.line1 = line1
            self.city = city
            self.state = state
            self.country = country
            self.template = template
            self.tt = tt
        #
        def paymentSuccess(self):
            configuration = ml.sib_api_v3_sdk.Configuration()
            configuration.api_key['api-key'] = ml.config.mail_key
            api_instance = ml.sib_api_v3_sdk.SMTPApi(ml.sib_api_v3_sdk.ApiClient(configuration))
            send_smtp_email = ml.sib_api_v3_sdk.SendSmtpEmail(
                                    to=[{"email": self.userEmail ,"name": self.userName}],
                                    template_id= self.template,
                                    params={"orderID": self.orderID,
                                            "paymentID" : self.paymentID,
                                            "userName": self.userName,
                                            "userEmail": self.userEmail,
                                            "contact": self.contact,
                                            "courseName": self.courseName,
                                            "courseAmount": self.courseAmount,
                                            "purchaseTime": self.purchaseTime,
                                            "line1": self.line1,
                                            "city": self.city,
                                            "state": self.state,
                                            "country": self.country,
                                            "time": self.tt},
                                    headers={"X-Mailin-custom": "custom_header_1:custom_value_1|custom_header_2:custom_value_2|custom_header_3:custom_value_3", "charset": "iso-8859-1"}) # SendSmtpEmail | Values to send a transactional email
            try:
                # Send a transactional email
                api_response = api_instance.send_transac_email(send_smtp_email)
                ml.pprint(api_response)
            except ml.ApiException as e:
                print("Exception when calling SMTPApi->send_transac_email: %s\n" % e)



