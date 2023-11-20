import sqlite3
import openpyxl
import os

class Course:
    def __init__(self,id,name,compre_date,midsem_date):
        self.id=id
        self.name=name
        self.compre_date=compre_date
        self.midsem_date=midsem_date
    def get_all_sections(self):
        pass
    def __str__(self):
        return self.id+' '+self.name+' '
    def populate_section(self,section):
        conn = sqlite3.connect("courses.db")
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {section.course_id} VALUES({section.type},{section.day},{section.start},{section.end})")
        conn.close()

class Section:
    def __init__(self,id,course_id,type,day,start,end):
        self.course_id=course_id
        self.type=type
        self.day=day
        self.start=start
        self.end=end
        self.time_slot={day:[start,end]}
'''
class Lab_Section(Section):
    def __init__(self,id,course_id,day,start,end,instructor):
        super().__init__(course_id,day,start,end)
        self.instructor=instructor

class Tut_Section(Section):
    def __init__(self,id,course_id,day,start,end,instructor):
        super().__init__(course_id,day,start,end)
        self.instructor=instructor

class Lecture_Section(Section):
    def __init__(self,id,course_id,day,start,end,instructor):
        super().__init__(course_id,day,start,end)
        self.instructor=instructor
'''
class Timetable:
    def __init__(self):
        pass
    def enroll_subject(self):
        pass
    def check_clashes(self):
        pass
    def export_to_csv(self):
        pass

def populate_course():
    workbook = openpyxl.load_workbook("course.xlsx")
    conn = sqlite3.connect("courses.db")
    cur = conn.cursor()
    sheet = workbook.worksheets[0]
    for row_cells in sheet.iter_rows(min_row=2):
        cur.execute(f"CREATE TABLE IF NOT EXISTS '{row_cells[0].value}' (tut_id INTEGER PRIMARY KEY,type TEXT, day TEXT, start datetime, end datetime)")
    conn.close()
    
def delete_db():
    os.remove('courses.db')
populate_course()

