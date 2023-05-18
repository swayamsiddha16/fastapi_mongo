from scripts.db.mongo import add_student,view_students,update_student,delete_student,aggregated_student_data,Student
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

# "rahul.krishna@knowledgelens.com"

class Studenthandler:    
    def create_student(self,student: Student):
        return add_student(student)
        
    def get_student(self):
        data = view_students()
        if data:
            return{"status":"success","response":data,"message":"data fetched successfully"}
        else:
            return{"status":"error"}
            
       
        
    def student_update(self,student_id: int, updated_data: dict):
        data = update_student(student_id, updated_data)
        if data:
            return{"status":"success","response": data,"message":"data updated successfully"}
        else:
            return{"status":"error"}
            
       
        
    
    def del_student(self,student_id: int):
        data = delete_student(student_id)
        if data:
            return{"status":"success","response": data,"message":"data deleted successfully"}
        else:
            return{"status":"error"}
        
    
    def aggregated_data(self,email:str):
        print("from hander")
        total_aggregate = aggregated_student_data()
        print(total_aggregate)
        mailinfo = self.convert_mailbody(total_aggregate)
        self.sendmail_handler(mailinfo,email)
        return "mail sent"
    
    def sendmail_handler(self,email_body,recipient):#send,re,body,sub
        message = Mail(
            from_email='swayamsiddha2000@gmail.com',#const
            to_emails=recipient,
            subject="Aggregate data of a student",
            html_content=email_body
            )
        try:
            sg = SendGridAPIClient("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")#api key#const
            response = sg.send(message)
            print(response.status_code)
            print(response.body)
            print(response.headers)
        except Exception as e:
            print(e)
        
        

    def convert_mailbody(self,data):
        result = ""
        for student in data:
            result += f"<p><b> id: {student['id']} </b></p>"
            result += f"<p><b> name: {student['name']} </b></p>"
            result += f"<p><b> email: {student['email']} </b></p>"
            result += f"<p><b> course: {student['course']} </b></p>"
            result += f"<p><b> age: {student['age']} </b></p>"
            result += "<p><b> ______________________________________________ </b></p>"
        return result

    
 
   
   
   
