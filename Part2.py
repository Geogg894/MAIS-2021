#simple method, returns letter and GPA equivalent of grade
def to_grade_point(grade):

   #if/else conditions for input grade

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

# to_grade_point test   
for grade in [0, 99, 80, 85, 84, 60, 59, 74]:
    print("{} -> {}".format(grade, to_grade_point(grade)))

class GradeRecords:

 #class attributes  
 def __init__(self,term):

    self.term=term
    self.grades=[]
    self.num_courses=0

 #update list and number of courses
 def add_course(self,coursecode,grade,credits):

    self.grades.append((coursecode,grade,credits))
    self.num_courses+=1
 
 def get_best_courses(self):

 #variable initializations
    biglist=[]
    counter=0
    codes=[]
 #sort list of tuples based on grade
    sortedlist=sorted(self.grades,key=lambda i: i[1],reverse=True) 
 #store highest grade in new list 
    for x in sortedlist:

        grade=x[1] 
        biglist.append(grade)
 #store list of tuples
    biglist2=[to_grade_point(i) for i in biglist]
 # iterate through stored list, compare each grade to highest grade
    for x in biglist2:

        grade=x[1]
        
        if grade==biglist2[0][1]:
 # if equal to top grade, update counter
            counter+=1
    for x in sortedlist[:counter]:
 # Append coursecode with top grade to list, return list
        coursecode=x[0]
        codes.append(coursecode)

    return codes

 def get_GPA(self):

      count=0
      grader=0
      biglist=[]
      biglist2=[]
#append all grades in list
      for x in self.grades:

        grade=x[1]
    
        biglist.append(grade)

      biglist2=[to_grade_point(i) for i in biglist]

      for i in biglist2:
# iterate through list, continuously add grades and update counter
         grader+=i[1]
         count+=1
# return 1 decimal GPA by dividing grade sum by count
      return round(grader/count,1)

 def to_dict(self):

# initializations
      dictionnary=dict()
      biglist=[]
      biglist2=[]
      codes=[]
      grades=[]

      for x in self.grades:

        grade=x[1]
    
        biglist.append(grade)

      biglist2=[to_grade_point(i) for i in biglist]
#store letter grades from list
      for y in biglist2:

         letter=y[0]
         grades.append(letter)
#store course codes from list
      for z in self.grades:

         code=z[0]
         codes.append(code)
#store letter grades to corresponding key codes, return dictionnary     
      for key in codes:

         for value in grades:

            dictionnary[key]=value
            grades.remove(value)
            break

      return dictionnary

#test print statements      

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


print("Second batch")
print("Term: {}".format(gr.term))

gr.add_course("COMP 551", 67, 4)
gr.add_course("HIST 318", 88, 3)

print("Number of courses: {}".format(gr.num_courses))
print("Best courses: {}".format(gr.get_best_courses()))
print("GPA: {}".format(gr.get_GPA()))
print("Dictionary: {}".format(gr.to_dict()))





           







        