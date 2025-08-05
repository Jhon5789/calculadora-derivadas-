y <- function(x)
  2^x
}
x <- seq(-10.10, by= 0.2)
y1 <- round (y(x),2)
tabla <- data.frame(x,y1)
tabla
plot(tabla,type="l")

#Ejercicio 2. Compara Graficas
y1 <- function(x){
  3^x
}
y2 <- function(x){
  3^-x
}

x <- seq(-10,10, by=0.2)
y3 <- y1(x)
y4 <- y2(x)

win.graph()
par(mfrow=c(2,2))
plot(x, y3, main="y=3^x", col="green")
plot(x, y4, main="y=3^-x", col="blue")
plot(x, y3, type= "l", main="y=3^x")
plot(x, y4, type= "l", main="y=3^-x")
