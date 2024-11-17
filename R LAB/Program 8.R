#create a sample data set
data<-c(3,4,7,8,9,10,12,14,15,18,21)

#plot
plot(data)

#create a histogram
hist(data,breaks=5,main = "Histogram",xlab = "value",ylab = "frequency",col = "green")

#create a line chart
x<-1:length(data) # nolint
line_data<-cumsum(data)
plot(x, line_data, type="l", col="red", main="Line Chart", xlab="X-axis", ylab="Y-axis")

#create a pie chart
slices<-c(30,20,10,40)
lbls<-c("slice 1","slice 2","slice 3","slice 4")
pie(slices,labels=lbls,main="pie chart")

#create a boxplot
boxplot(data,main="Boxplot",xlab="Value",ylab="Distribution",col="purple")

#create a scatterplot
x2<-c(2,4,6,8,10)
y2<-c(5,7,3,9,2)
plot(x2,y2,type="p",pch=20,col="orange",main="scatterplot",xlab="X-axis",ylab="Y-axis")