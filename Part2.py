
def to_grade_point(grade):

   if grade>100 or 0>grade:
      raise Exception("Grade must be an integer from 0 to 100 inclusive")
   elif grade >= 85: 
      return ("A",4.0)
   elif 84>= grade >= 80: 
      return ("A-",3.7)  
   elif 79>= grade >= 75: 
      return ("B+",3.3)  
   elif 74>= grade >= 70: 
      return ("B",3.0)  
   elif 69>= grade >= 65: 
      return ("B-",2.7)
   elif 64>= grade >= 60: 
      return ("C+",2.3)
   else :         
      return("F",0.0)
   
#for grade in [0, 99, 80, 85, 84, 60, 59, 74]:
#print("{} -> {}".format(grade, to_grade_point(grade)))

class GradeRecords:

   
 def __init__(self,term):

    self.term=term
    self.grades=[]
    self.num_courses=0

 def add_course(self,coursecode,grade,credits):

    self.grades.append((coursecode,grade,credits))
    self.num_courses+=1
 
 def get_best_courses(self):

    biglist=[]
    scores=[]
    counter=0
    codes=[]

    sortedlist=sorted(self.grades,key=lambda i: i[1],reverse=True) 

    for x in sortedlist:

        grade=x[1]
    
        biglist.append(grade)

    biglist2=[to_grade_point(i) for i in biglist]

    for x in biglist2:

        grade=x[1]
        scores.append(grade)
        
        if x[1]==biglist2[0][1]:

            counter+=1
    for x in sortedlist[:counter]:

        coursecode=x[0]
        codes.append(coursecode)

    return codes

 def get_GPA(self):

      count=0
      grader=0
      biglist=[]
      biglist2=[]

      for x in self.grades:

        grade=x[1]
    
        biglist.append(grade)

      biglist2=[to_grade_point(i) for i in biglist]

      for i in biglist2:

         grader+=i[1]
         count+=1

      return round(grader/count,1)

 def to_dict(self):

      dictionnary=dict()
      biglist=[]
      biglist2=[]
      codes=[]
      grades=[]

      for x in self.grades:

        grade=x[1]
    
        biglist.append(grade)

      biglist2=[to_grade_point(i) for i in biglist]

      for y in biglist2:

         grade=y[1]
         grades.append(grade)

      for z in self.grades:

         code=z[0]
         codes.append(code)
      
      for key in codes:

         for value in grades:

            dictionnary[key]=value
            grades.remove(value)
            break

      return dictionnary

gr = GradeRecords("Fall 2019")
print("First batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 202", 83, 3)
gr.add_course("CLAS 203", 75, 3)
gr.add_course("LING 360", 81, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))

print() 

print("Second batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 551", 67, 4)
gr.add_course("HIST 318", 88, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))





           







        