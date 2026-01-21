#Importing required modules
from fpdf import FPDF
import mysql.connector as my
import tkinter as tk
from tkinter import filedialog

# Function to get input text and display it
def show_text():
    global root
    # Get the input text from the entry widget
    a = int(entry.get())
    root.destroy()
    #Marks List Function Definition
    def marks(a):
        e,p,c,m,cs,pfl=['English'],['Physics'],['Chemistry'],['Maths'],['Computer'],['P.Ed/ FA/ Lib.Sci']
        cu.execute('SELECT * FROM STUDENTS NATURAL JOIN (SELECT * FROM wt1 UNION ALL SELECT * FROM wt2 UNION ALL SELECT * FROM hy) AS combined_table WHERE adm={}'.format(a))

        #Adding Marks of various Subjects in their respective lists retrieved from the database
        for i in cu:
            e.append(i[8])
            p.append(i[9])
            c.append(i[10])
            m.append(i[11])
            cs.append(i[12])
            pfl.append(i[13])

        #Putting all the subject marks list into a single list
        m=[e,p,c,m,cs,pfl]
        return m

    #Student Data retrieving Function Definition
    def stdata(a):
        cu.execute('SELECT * FROM STUDENTS WHERE adm={}'.format(a))
        #Getting the student information according to the Admission Number entered by user
        for i in cu:
            a=i
        return a

    #Grading Function Definition
    def grading_system(mo,tm):
        a=mo/tm*100  #Percentage in the exam

        #Grading system according to percentage obtained
        if a>=91:
            return 'A+'
        elif a>=81 and a<91 :
            return 'A'
        elif a>=71 and a<81 :
            return 'B+'
        elif a>=61 and a<71 :
            return 'B'
        elif a>=51 and a<61 :
            return 'C+'
        elif a>=41 and a<51 :
            return 'C'
        elif a>=31 and a<41 :
            return 'D'
        else:
            return 'F'

    #Remark Function Definition
    def remarking_system(mo,tm):
        a=mo/tm*100    #Percentage in the exam

        #Remarking system according to percentage obtained
        if a>=91:
            return 'Excellent'
        elif a>=81 and a<91 :
            return 'Very Good'
        elif a>=71 and a<81 :
            return 'Good'
        elif a>=61 and a<71 :
            return 'Satisfactory'
        elif a>=51 and a<61 :
            return 'Average'
        elif a>=41 and a<51 :
            return 'Below Average'
        elif a>=31 and a<41 :
            return 'Needs Improvement'
        else:
            return 'Fail'

    #Main Function Definition as a Class
    class PDF(FPDF):

        #Heading in the Report Card Function Definition
        def header(self):
            #School Details
            self.set_font("Times", "B", 22)
            self.cell(0, 15, "DAV MODEL SCHOOL, DURGAPUR", align="C")
            self.ln(9)

            self.set_font("Times", "", 16)
            self.cell(0, 15, "J.M. SENGUPTA ROAD, B-ZONE, DURGAPUR", align="C")
            self.ln(9)

            self.set_font("Times", "", 12)
            self.cell(0, 15, "DIST.- PASCHIM BARDHAMAN, WEST BENGAL- 713205", align="C")
            self.ln(9)

            self.set_font("Times", "", 15)
            self.cell(0, 15, 'E-mail- dav@davmodeldurgapur.com', align="C")

            self.set_line_width(0.6)
            self.line(10, 50, 200, 50)
            self.ln(15)

            self.set_font("Times", "BU", 30)
            self.cell(0, 15, "Student Report Card", align="C")
            self.ln(17)

        #Points of Student Information Function Definition
        def student_details(self, adm_no,stu_name, stu_class, roll_no,f_name,m_name,dob,att):
            self.set_font("Arial", "B", 14)

            #1st line
            self.cell(5, 10, " ")
            self.cell(100, 10, "Name: {}".format(stu_name), align="L")
            self.cell(0, 10, "Admission No: {}H".format(adm_no), ln=True, align="L")

            #2nd line
            self.cell(5, 10, " ")
            self.cell(100, 10, "Class: {}".format(stu_class), align="L")
            self.cell(0, 10, "Roll Number: {}".format(roll_no), ln=True, align="L")

            #3rd line
            self.cell(5, 10, " ")
            self.cell(100, 10, "Father's Name: {}".format(f_name), align="L")
            self.cell(0, 10, "Mother's Name: {}".format(m_name), ln=True, align="L")

            #4th line
            self.cell(5, 10, " ")
            self.cell(100, 10, "D.O.B.: {}".format(dob), align="L")
            self.cell(0, 10, "Attendance: {}/200".format(att), ln=True, align="L")        
            self.ln(10)
    
        #Heading of the columns of the marks table Function Definition
        def table_header(self):
            self.set_font("Arial", "B", 14)
            self.set_fill_color(255, 230, 204)
            self.cell(48, 8, "Subject", border=1, align="C",fill=True)
            self.set_fill_color(255, 243, 230)
            self.cell(48, 8, "Weekly Test 1", border=1, align="C",fill=True)
            self.cell(48, 8, "Weekly Test 2", border=1, align="C",fill=True)
            self.cell(48, 8, "Half Yearly", border=1, align="C",fill=True)
            self.ln()

        #Creating the rows for each Subject Function Definition
        def table_row(self, subject_name, wt1, wt2, hy):
            self.set_font("Arial", "B", 14)
            self.set_fill_color(255, 230, 204)
            self.cell(48, 8, subject_name, border=1, align="C",fill=True)
            self.set_font("Arial", "", 12)
            self.cell(48, 8, str(wt1), border=1, align="C")
            self.cell(48, 8, str(wt2), border=1, align="C")
            self.cell(48, 8, str(hy), border=1, align="C")
            self.ln()

        #Percentage displaying row Function Definition
        def percentage_row(self,wt1,wt2,hy):
            self.set_font("Arial", "B", 14)
            self.set_fill_color(255, 230, 204)
            self.cell(48, 8, 'Percentage', border=1, align="C",fill=True)
            self.set_fill_color(255, 243, 230)
            self.cell(48, 8, str(wt1)+'%', border=1, align="C",fill=True)
            self.cell(48, 8, str(wt2)+'%', border=1, align="C",fill=True)
            self.cell(48, 8, str(hy)+'%', border=1, align="C",fill=True)
            self.ln()   

        #Grade displaying row Function Definition
        def grading_row(self,wt1t,wt2t,hyt):
            self.set_font("Arial", "B", 14)
            self.set_fill_color(255, 230, 204)
            self.cell(48, 8, 'Grade', border=1, align="C",fill=True)
            self.set_fill_color(255, 243, 230)
            self.cell(48, 8, grading_system(wt1t,150), border=1, align="C",fill=True)
            self.cell(48, 8, grading_system(wt2t,150), border=1, align="C",fill=True)
            self.cell(48, 8, grading_system(hyt,600), border=1, align="C",fill=True)
            self.ln()

        #Remarks displaying row Function Definition
        def remarking_row(self,wt1t,wt2t,hyt):
            self.set_font("Arial", "B", 14)
            self.set_fill_color(255, 230, 204)
            self.cell(48, 8, 'Remarks', border=1, align="C",fill=True)
            self.set_fill_color(255, 243, 230)
            self.cell(48, 8, remarking_system(wt1t,150), border=1, align="C",fill=True)
            self.cell(48, 8, remarking_system(wt2t,150), border=1, align="C",fill=True)
            self.cell(48, 8, remarking_system(hyt,600), border=1, align="C",fill=True)
            self.ln()

        #Teacher's Remarks
        def teacher_remark(self,n):
            import random
            l=["{} consistently demonstrates enthusiasm for learning and active participation.",
               "{} displays a positive attitude and works well with classmates.",
               "{} shows steady improvement and puts in great effort daily.",
               "{} is a responsible student who completes assignments on time.",
               "{} has a curious mind and enjoys exploring new topics.",
               "{} is dependable and maintains focus during classroom activities.",
               "{} collaborates effectively and brings creative ideas to discussions.",
               "{} is attentive in class and shows good organizational skills.",
               "{} participates regularly and remains engaged throughout lessons.",
               "{} completes work diligently and approaches tasks thoughtfully."]
            r=random.randint(0,len(l)-1)
            self.cell(48, 10, '')
            self.ln(10)

            self.set_fill_color(255, 230, 204)
            self.set_font("Arial", "BU", 14)
            self.cell(192, 10, "Teacher's Remark", border=1, ln=True, align="C",fill=True)
            self.set_font("Arial", "", 12)
            self.cell(192, 10, l[r].format(n.split()[0].title()), border=1, ln=True, align="C")
            self.ln()

            #Watermark
            self.image(r"C:\Users\dipay\OneDrive\Documents\CS-Project\DAV-wm(1).png", 22, 70, 170, 170)

        #Signature Blocks
        def signature_block(self):
            self.set_font("Arial", "BU", 14)
            self.cell(45, 15, align="C")
            self.cell(51, 15, border=1, align="C")
            self.cell(51, 15, border=1, align="C")
            self.ln()

            self.set_fill_color(255, 230, 204)
            self.cell(45, 8, align="C")
            self.cell(51, 8, "Parent's Signature", border=1, align="C", fill=True)
            self.cell(51, 8, "Pricipal's Signature", border=1, align="C", fill=True)

            #Ending lines
            self.set_line_width(1)
            self.line(10, 280, 200, 280)
            self.line(10, 282, 200, 282)

    #Report Card Creation Function Definition
    def generate_report_card(student_data, marks_data,name, pdf_filename):
        global wt1t
        global wt2t
        global hyt
        wt1t=0
        wt2t=0
        hyt=0
        pdf = PDF()
        pdf.add_page()

        #CBSE and DAV Logos
        pdf.image(r"C:\Users\dipay\OneDrive\Documents\CS-Project\CBSE.png", x=5, y=10, w=30, h=35)
        pdf.image(r"C:\Users\dipay\OneDrive\Documents\CS-Project\DAV Top.jpg", x=175, y=10, w=32, h=35)

        #Pricipal Mam's Signature
        pdf.image(r"C:\Users\dipay\OneDrive\Documents\CS-Project\P Sign.jpg", x=110, y=246, w=40, h=15)

        # Add student details
        adm_no,stu_name, stu_class, roll_no,f_name,m_name,dob,att = student_data
        pdf.student_details(adm_no,stu_name, stu_class, roll_no,f_name,m_name,dob,att)

        # Add table header
        pdf.table_header()

        # Add marks data
        for subject_name, wt1, wt2, hy in marks_data:
            pdf.table_row(subject_name, wt1, wt2, hy)
            wt1t+=wt1
            wt2t+=wt2
            hyt+=hy

        #Calling the functions created for the marks evaluation 
        pdf.table_row('Total',wt1t,wt2t,hyt)
        pdf.percentage_row(round(wt1t*2/3,2),round(wt2t*2/3,2),round(hyt/6,2))
        pdf.grading_row(wt1t,wt2t,hyt)
        pdf.remarking_row(wt1t,wt2t,hyt)
        pdf.teacher_remark(name)
        pdf.signature_block()

        #Saving the PDF to a file along with error handling
        try:
            pdf.output(pdf_filename)
            print('Report Card ready at {}'.format(pdf_filename))
        except Exception as e:
            print(f"Error generating PDF: {e}")

    #Getting list of Admission numbers
    cu.execute("Select * from students")
    l=[]
    for i in cu:
        l.append(i[0])

    #Sending data to respective functions and finally saving the pdf
    if a in l:
        marks_data = marks(a)
        student_data = stdata(a)
        f = student_data[1] + '.pdf' 
        folder_selected = filedialog.askdirectory( title="Select Folder")
        if folder_selected:
            pdf_filename=str(folder_selected)+r"/{}".format(f)
            generate_report_card(student_data, marks_data,f, pdf_filename) 
        else:
            print('Saving Location not Selected')
    else:
        print('Admission number not found')

try:
    #Database Connection 
    con=my.connect(host='localhost', user='root', passwd='', database='dipayan')
    cu=con.cursor()

    # Create the main application window
    root = tk.Tk()
    root.title("Report Card Generator")
    root.geometry("300x200")

    # Create an entry widget for input
    entry_label = tk.Label(root, text="Enter Admission Number:")
    entry_label.pack(pady=5)
    entry = tk.Entry(root, width=30)
    entry.pack(pady=5)

    # Create a button to trigger the display of input text
    submit_button = tk.Button(root, text="Generate", command=show_text)
    root.bind('<Return>', lambda event: show_text())
    submit_button.pack(pady=10)

    # Create a label to display the output text
    output_label = tk.Label(root, text="")
    output_label.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()

    #Closing connections and cursors
    cu.close()
    con.close()

#Error Handling
except my.errors.DatabaseError:
    print("Connection to the database was unsuccessful")

except my.errors.InterfaceError:
    print("Connection to MySQL was unsuccessful")