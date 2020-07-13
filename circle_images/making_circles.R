plot(NA,xlim=c(0,10),ylim=c(0,10),
     
     axes=F,xlab="",ylab="", main="",cex.lab=1.5)



trace_circle <- function(x,y,r,deg,inc,color,nsteps=100,...){
  
  beg=inc*pi/180
  
  end=beg+deg*pi/180
  
  
  
  rs <- seq(beg,end,len=nsteps)
  
  xc <- x+r*cos(rs)
  
  yc <- y+r*sin(rs)
  
  polygon(xc,yc,col=color,border=NA)
  
  if(deg<=180){
    
    color2=color
    
  } else {
    
    color2="white"
    
    
    
  }
  
  polygon(c(x,x+r*cos(beg),x+r*cos(end)),c(y,y+r*sin(beg),y+r*sin(end)),col=color2,border=color2)
  
}



c_pos1=c(3,3)

c_pos2=c(7,3)

c_pos3=c(3,7)

c_pos4=c(7,7)



positions_main=cbind(c_pos1,c_pos2,c_pos3,c_pos4,c_pos1,c_pos2,c_pos3,c_pos4,c_pos1,c_pos2)

positions_second=cbind(c_pos4,c_pos3,c_pos2,c_pos1,c_pos4,c_pos3,c_pos2,c_pos1,c_pos4,c_pos3)



x=5

y=5

r=2

deg=290

color_main="blue"

color_sec="grey"



for(i in 1:10){
  
  
  
  plot(NA,xlim=c(0,10),ylim=c(0,10),
       
       axes=F,xlab="",ylab="", main="",cex.lab=1.5)
  
  deg_main=sample(200:340,1)
  
  deg_second=360-deg_main-1
  
  inc_main=sample(0:180,1)
  
  inc_second=sample(0:180,1)
  
  trace_circle(positions_main[1,i],positions_main[2,i],r,deg_main,inc=inc_main,color_main)
  
  trace_circle(positions_second[1,i],positions_second[2,i],r,deg_second,inc=inc_second,color_sec)
  
}