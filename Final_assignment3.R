myCourses <- c("Math 101", "Chemistry 101", "Biology 101", "Physics 101", "Litreture 101", "Algebra 101", "Computer sceince 101","Geography 101")
print(length(myCourses))
print(myCourses[c(1,2)])
print(myCourses[c(3,4)])
## Sorting based on the alphabet in decreasing order
myCoursesSorted <- sort(myCourses, decreasing = TRUE)
print (myCoursesSorted)

## Sorting based on the alphabet in increasing order
myCoursesSorted <- sort(myCourses, decreasing = FALSE)
print (myCoursesSorted)