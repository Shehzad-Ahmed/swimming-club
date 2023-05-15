list.of.packages <- c("dplyr", "tidyverse", "ggplot2", "corrplot", "caret", "arules", "arulesViz", "caTools", "neuralnet", "rpart", "xgboost", "rpart.plot")
new.packages <- list.of.packages[!(list.of.packages %in% installed.packages()[,"Package"])]
if(length(new.packages)) install.packages(new.packages) # Thanks to https://stackoverflow.com/questions/4090169/elegant-way-to-check-for-missing-packages-and-install-them

library(dplyr)
library(tidyverse)
library(ggplot2)
library(corrplot)
library(caret)
library(arules)
library(arulesViz)
library(caTools) # For splitting the dataset.
library(neuralnet)
library(rpart)
library(xgboost)

telco <- read.csv('telco-customers.csv')
head(telco)
m.data <- telco[!complete.cases(telco),]
summary(m.data)
summary(m.data$TotalCharges)
summary(m.data$tenure)

# --- Data Cleaning and Preparation ---

# Imputes the missing value with corresponding Monthly charges.
for(i in 1:nrow(m.data)){
  telco[telco$customerID==m.data$customerID[i],]$TotalCharges <- m.data$MonthlyCharges[i]
}

# Check if there are any rows with missing values.
sum(is.na(telco))

# Check for typos for all character types variables.
for(i in 1:ncol(telco)){
  if(is.character(telco[1, i])){
  print(unique(telco[i]))
    print('-------')
  }
}
# Since senior citizen is indicate by 0,1
unique(telco$SeniorCitizen)

# Errors

summary(telco$tenure)
summary(telco$MonthlyCharges)
summary(telco$TotalCharges)


# Check Duplicates
dup.data <- duplicated(telco)
telco[dup.data, ]

processed.data <- data.frame(telco)

# Remove irrelevant columns CustomerId.
processed.data <- subset(processed.data, select = -c(customerID))

# Encoding and Transformation.
processed.data <- processed.data %>%
  mutate_all(~ as.numeric(factor(.)) -1)

# Normalize numeric columns
processed.data$tenure <- scale(processed.data$tenure)
processed.data$MonthlyCharges <- scale(processed.data$MonthlyCharges)
processed.data$TotalCharges <- scale(processed.data$TotalCharges)

# Splitting the dataset into train and test data.
set.seed(1042)

split <- sample.split(processed.data$Churn, SplitRatio=0.75)
train <- processed.data[split, ]
test <- processed.data[!split, ]


# --- Exploratory Data Analysis (EDA) ---
# https://bookdown.org/sujatar/r_for_fundamental_data_analysis_in_market_research/visual.html

# - Univariate Analysis -

# Gender
ggplot(telco %>% count(gender) %>%
         mutate(
           percent=round((n/sum(n))*100, digits = 2)),
       mapping=aes(x=as.factor(gender),y=percent)) +
  geom_bar(stat="identity",fill=c("turquoise4","yellow"),width=0.45) +
  ggtitle("Proportion of Gender") +
  xlab("Gender") +
  ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Senior Citizen
sc.df <- telco %>%
  group_by(SeniorCitizen) %>% # Variable to be transformed
  count() %>%
  ungroup() %>%
  mutate(perc = `n` / sum(`n`)) %>%
  arrange(perc) %>%
  mutate(labels = scales::percent(perc))

ggplot(sc.df, aes(x = "", y = perc, fill = c("Yes", "No"))) +
  geom_col(color = "black") +
  geom_label(aes(label = labels), color = c(1, "white"),
             position = position_stack(vjust = 0.5),
             show.legend = FALSE) +
  guides(fill = guide_legend(title = "Is Senior Citizen?")) +
  scale_fill_viridis_d() +
  coord_polar(theta = "y") +
  theme_void() + ggtitle("Proportion of senior and non-senior customers")

# Partner
ggplot(telco %>% count(Partner) %>%
         mutate(
           percent=round((n/sum(n))*100, digits = 2)),
       mapping=aes(x=as.factor(Partner),y=percent)) +
  geom_bar(stat="identity",fill=c("red","green"),width=0.45) +
  ggtitle("Proportion of customers having partner") +
  xlab("Partner") + ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Dependents
ggplot(telco %>% count(Dependents) %>%
         mutate(percent=round((n/sum(n))*100, digits = 2)),
       mapping=aes(x=as.factor(Dependents),y=percent)) +
  geom_bar(stat="identity",fill=c("orange","blue"),width=0.45) +
  ggtitle("Proportion of customers having dependents") +
  xlab("Dependents") + ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Tenure
ggplot(telco, aes(x=tenure)) + geom_histogram(binwidth = 1, color="turquoise4", fill="turquoise") +
  ggtitle("Histogram of Tenure") +
  geom_vline(aes(xintercept=mean(tenure)), color="blue", linetype="dashed", linewidth=1)


# Phone Service
ggplot(
  telco %>% count(PhoneService) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(PhoneService),y=percent)
  ) + geom_bar(stat="identity",fill=c("beige","brown"),width=0.45) +
  ggtitle("Proportion of customers subscribed to phone service") +
  xlab("Phone Service")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)


# Multiple Lines
ggplot(
  telco %>% count(MultipleLines) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(MultipleLines),y=percent)
) + geom_bar(stat="identity",fill=c("purple","blue", "turquoise"),width=0.45) +
  ggtitle("Proportion of customers subscribed to multiple lines service") +
  xlab("Multiple Lines")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)


# Internet Service
ggplot(
  telco %>% count(InternetService) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(InternetService),y=percent)
) + geom_bar(stat="identity",fill=c("turquoise","turquoise3", "red3"),width=0.45) +
  ggtitle("Proportion of customers subscribed to type of internet service") +
  xlab("Internet Service")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Online Security
ggplot(
  telco %>% count(OnlineSecurity) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(OnlineSecurity),y=percent)
) + geom_bar(stat="identity",fill=c("beige","brown", "black"),width=0.45) +
  ggtitle("Proportion of customers subscribed to online security service") +
  xlab("Online Security")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)


# Online Backup
ggplot(
  telco %>% count(OnlineBackup) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(OnlineBackup),y=percent)
) + geom_bar(stat="identity",fill=c("yellow","red", "green"), width=0.45) +
  ggtitle("Proportion of customers subscribed to online backup service") +
  xlab("Online Backup")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Device Protection
ggplot(
  telco %>% count(DeviceProtection) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(DeviceProtection),y=percent)
) + geom_bar(stat="identity",fill=c("white","grey", "pink"), width=0.45) +
  ggtitle("Proportion of customers subscribed to device protection service") +
  xlab("Device Protection")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Tech Support
ggplot(
  telco %>% count(TechSupport) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(TechSupport),y=percent)
) + geom_bar(stat="identity",fill=c("orange2","red3", "yellow4"), width=0.45) +
  ggtitle("Proportion of customers subscribed to tech support service") +
  xlab("Tech Support")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Streaming TV
ggplot(
  telco %>% count(StreamingTV) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(StreamingTV),y=percent)
) + geom_bar(stat="identity",fill=c("purple3","blue3", "turquoise3"), width=0.45) +
  ggtitle("Proportion of customers subscribed to streaming TV service") +
  xlab("Streaming TV")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Streaming Movies
ggplot(
  telco %>% count(StreamingMovies) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(StreamingMovies),y=percent)
) + geom_bar(stat="identity",fill=c("green", "pink", "turquoise2"), width=0.45) +
  ggtitle("Proportion of customers subscribed to streaming Movies service") +
  xlab("Streaming Movies")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Contract
ggplot(
  telco %>% count(Contract) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(Contract),y=percent)
) + geom_bar(stat="identity",fill=c("pink2", "red3", "orange3"), width=0.45) +
  ggtitle("Proportion of customers using contract type") +
  xlab("Contract Type")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Paperless Billing
ggplot(
  telco %>% count(PaperlessBilling) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(PaperlessBilling),y=percent)
) + geom_bar(stat="identity",fill=c("pink", "green4"), width=0.45) +
  ggtitle("Proportion of customers using paperless billing") +
  xlab("Paperless Billing")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Payment Method
ggplot(
  telco %>% count(PaymentMethod) %>%
    mutate(
      percent=round((n/sum(n))*100, digits = 2)),
  mapping=aes(x=as.factor(PaymentMethod),y=percent)
) + geom_bar(stat="identity",fill=c("purple1", "blue4","purple4","blue"), width=0.45) +
  ggtitle("Proportion of customers using mode of payment") +
  xlab("Paperless Billing")+ylab("Percentage") +
  geom_text(aes(label=percent),color="brown",size=5,vjust=-.25)

# Monthly Charges
ggplot(telco, aes(x=MonthlyCharges)) + geom_histogram(binwidth = 1, color="pink4", fill="pink") +
  ggtitle("Histogram of Tenure") +
  geom_vline(aes(xintercept=mean(MonthlyCharges)), color="blue", linetype="dashed", linewidth=1)


# Total Charges
ggplot(telco, aes(x=TotalCharges)) + geom_histogram(binwidth = 10, color="brown4", fill="brown") +
  ggtitle("Histogram of Tenure") +
  geom_vline(aes(xintercept=mean(TotalCharges)), color="blue", linetype="dashed", linewidth=1)

# Churn

churn.df <- telco %>%
  group_by(Churn) %>% # Variable to be transformed
  count() %>%
  ungroup() %>%
  mutate(perc = `n` / sum(`n`)) %>%
  arrange(perc) %>%
  mutate(labels = scales::percent(perc))

ggplot(churn.df, aes(x = "", y = perc, fill = Churn)) +
  geom_col(color = "black") +
  geom_label(aes(label = labels), color = c(1, "white"),
             position = position_stack(vjust = 0.5),
             show.legend = FALSE) +
  guides(fill = guide_legend(title = "Churn?")) +
  scale_fill_viridis_d() +
  coord_polar(theta = "y") +
  theme_void() + ggtitle("Proportion of customers churn out")

# - Bivariate Analysis -

# Churn vs SeniorCitizen

ggplot(telco %>% count(Churn,SeniorCitizen) %>% mutate(percent=(n/sum(n))*100),
       mapping=aes(x=SeniorCitizen,y=n,fill=Churn))+
  geom_bar(stat="identity",position=position_dodge(0.75),width=0.75)+
  geom_text(aes(label=n),vjust=-0.5,position=position_dodge(0.75))


# Churn vs Gender

ggplot(telco %>% count(gender,Churn) %>% mutate(percent=(n/sum(n))*100),
       mapping=aes(x=Churn,y=n,fill=as.factor(gender)))+
  geom_bar(stat="identity",position=position_dodge(0.75),width=0.75)+
  geom_text(aes(label=n),vjust=-0.5,position=position_dodge(0.75))
# Not conclusive enough, not added in report.

# Churn vs Internet Service

ggplot(telco %>% count(Churn,InternetService) %>% mutate(percent=(n/sum(n))*100),
       mapping=aes(x=Churn,y=n,fill=as.factor(InternetService)))+
  geom_bar(stat="identity",position=position_dodge(0.75),width=0.75)+
  geom_text(aes(label=n),vjust=-0.5,position=position_dodge(0.75))

# Churn vs Tenure

ggplot(telco, aes(x = factor(Churn), y = tenure)) +
  geom_violin(fill = "lightblue", color = "black", alpha = 0.8) +
  labs(title = "Churn by tenure")

# Churn vs Contract type

ggplot(telco %>% count(Churn,Contract) %>% mutate(percent=(n/sum(n))*100),
       mapping=aes(x=Churn,y=n,fill=as.factor(Contract)))+
  geom_bar(stat="identity",position=position_dodge(0.75),width=0.75)+
  geom_text(aes(label=n),vjust=-0.5,position=position_dodge(0.75))

# Relationship between variables.
corrplot(cor(data.frame(
  MonthlyCharges = as.numeric(telco$MonthlyCharges),
  Tenure = as.numeric(telco$tenure),
  TotalCharges = as.numeric(telco$TotalCharges)
)))


# --- Model Applications ---

# - Logistic Regression -

# Train Model
glm.model <- glm(Churn ~., data=train, family=binomial(link=('logit')))

# Make predictions on the test set
glm.predictions <- predict(glm.model, test, type = "response")
glm.predicted.classes <- ifelse(glm.predictions > 0.5, 1, 0)

# Evaluate Performance
glm.conf.mat <- confusionMatrix(as.factor(glm.predicted.classes), as.factor(test$Churn))


# - Neural Network -

# Train Model
nn.model <- neuralnet(Churn ~ ., data=train, hidden = 2)

# Make predictions on the test set
nn.predictions <- predict(nn.model, test)

# Evaluate Performance
nn.predicted.classes <- ifelse(nn.predictions > 0.5, 1, 0)
nn.conf.mat <- confusionMatrix(as.factor(nn.predicted.classes), as.factor(test$Churn))


# - Decision Trees -

train.churn <- factor(train$Churn)
test.churn <- factor(test$Churn)

# Train Model.
tree.model <- rpart(Churn ~ ., data = train, method = "class")

# Make Predictions on test test.
tree.predictions <- predict(tree.model, test, type = "class")

# Evaluate Performance
tree.conf.mat <- confusionMatrix(tree.predictions, test.churn)


# - XGBoost -

train.churn <- factor(train$Churn)
test.churn <- factor(test$Churn)

xg.train <- xgb.DMatrix(data = data.matrix(train[ , -20]), label = train.churn)
xg.test <- xgb.DMatrix(data = data.matrix(test[ , -20]), label = test.churn)

# Train model
xg.model <- xgboost(data = xg.train, max_depth = 3, eta = 0.1, nrounds = 100)

# Make predictions on test set
xg.predictions <- predict(xg.model, xg.test)


# --- Perfomance Evaluations of all models ---
xg.predictions[(xg.predictions>3)] = 3
pred.churn = as.factor((levels(test.churn))[round(xg.predictions)])
xg.conf.mat <- confusionMatrix(test.churn, pred.churn)
xgb.importance(xg.model)


print(glm.conf.mat)
print(nn.conf.mat)
print(tree.conf.mat)
print(xg.conf.mat)


# --- Feature importance by CART model. ---

#identify best cp value to use
best <- tree.model$cptable[which.min(tree.model$cptable[,"xerror"]),"CP"]
#produce a pruned tree based on the best cp value
pruned.tree <- prune(tree.model, cp=best)
#plot the pruned tree
prp(pruned.tree)

# ~ The End ~
