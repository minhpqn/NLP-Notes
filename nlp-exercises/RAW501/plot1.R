df <- read.table("./ex1data1.txt", sep=",", header=FALSE)
plot(df[,1], df[,2], xlab="Profit in $10,000s", ylab="Population of City in 10,000s")
