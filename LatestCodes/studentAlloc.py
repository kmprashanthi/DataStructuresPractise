def allocateSchools(schoolSeatsArray, studentScoreArray, studentSchoolPreferencesArray):
    student = len(studentScoreArray)
    seats = sum(schoolSeatsArray)

    i =0
    d = {}
    for i in range(0,student):
        d[i] = studentScoreArray[i]
    print (d)
    for stud in sorted(d,key=d.get,reverse=True):
        print ("student :",stud)
        for pref in studentSchoolPreferencesArray[stud]:
            print ("preference array :",studentSchoolPreferencesArray[stud])
            if (schoolSeatsArray[pref]>0):
                schoolSeatsArray[pref] -=1
                seats -= 1
                student -=1
                print (schoolSeatsArray[pref],seats,student)
                break
    return [seats,student]

schoolSeatsArray = [1,0]
studentScoreArray = [990,780]
studentSchoolPreferencesArray=[[0],[0]]
print (allocateSchools(schoolSeatsArray, studentScoreArray, studentSchoolPreferencesArray))