charcter_vector<-c("apple","bannana","cherry")
print(charcter_vector)

#creating matrix
numeric_matrix<-matrix(1:6,nrow=2,ncol=3)
print(numeric_matrix)

#creating list
my_list<-list(name=c("Ram","Daniel","Raj"),age=c(30,53,40),hobbies=c("singing","Reading","golf"))
print(my_list)

#creating an array
arr<-c(1:24,dim=c(4,3,2))
print(arr)

#creating 2 data frame
dataframe<-data.frame(name=c("Ramya","Ram","Raj"),age=c(25,30,22),gender=c("female","male","male"))
print(dataframe)

#creating factors
gender<-c("male","female","male","female","male")
factor_gender<-factor(gender,levels=c("male","female"))
print(factor_gender)