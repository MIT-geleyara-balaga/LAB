#create a sample data_frame
data_frame<- data.frame(Name=c("Alice","Bennett","Charlie","David","Emma"),
                        Age=c (25, 30, 22, 28, 35),
                             Gender =c("Female","Male","Male","Male","Female"),
                             Score=c (85, 92, 78, 88, 95))
print(data_frame)

#indexing and Subsetting
cat("\nSubset of Data Frame (Age > 25):\n")
subset_data <- data_frame[data_frame$Age > 25, ]
print(subset_data)

#calculate summary statistics
summary_stats<-summary(data_frame $ Score)
summary_stats

#add a new column
data_frame $ Grade<-ifelse(data_frame $ Score>=90,"A",ifelse(data_frame $ Score>=80,"B","C"))
print(data_frame)

#grouping and aggregation
gender_avg_score<-aggregate(data_frame$Score,by=list(data_frame$Gender),FUN=mean)
colnames(gender_avg_score)<-c("Gender","Avg_Score")
print(gender_avg_score)