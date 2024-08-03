import smtplib as s

m = 1
while True:    
    ob = s.SMTP("smtp.gmail.com",587)
    ob.starttls()
    ob.login("musawir2024@gmail.com","tdfy iwuh ulcn nznq")
    subject = "musawir"
    body=f"iam your frend {m}"
    message = "subject:{}\n\n{}".format(subject,body)

    ob.sendmail("musawir2024@gmail.com","musawir8880@gmail.com",message)
    ob.quit()
    print("sending succesfull")
    m +=1
