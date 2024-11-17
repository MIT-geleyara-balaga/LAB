#Load the mtcars dataset
data(mtcars)

#Explore the dataset
head(mtcars)

#Fit a multivariate linear regression model
#we;ll predict 'mpg'(miles per gallon) based on 'hp' (horespower) and 'wt'(weight)
model<-lm(mpg~hp+wt,data=mtcars)
model
lm(formula=mpg~hp+wt,data=mtcars)

#print the model summary
summary(model)

#make predictions using the model
new_data<-data.frame(hp=c(150,200),wt=c(3.5,4.0))
preditions<-predict(model,newdata=new_data)
cat("Predicted MPG for new data:\n")
print(preditions)