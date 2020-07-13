library(ggplot2)
set.seed(3891412)

for(i in 1:60){
  starsx = data.frame(sample(c(0:100),40, replace = TRUE))
  starsy = data.frame(sample(c(0:100),40, replace = TRUE))
  starry = cbind(starsx,starsy)
  colnames(starry) <- c("starsx","starsy")

  ggplot(data=starry, aes(x=starsx, y = starsy)) + geom_point(color = "blue",size=7) + labs(x="", y ="") +
    theme(axis.line=element_blank(),axis.text.x=element_blank(),
          axis.text.y=element_blank(),axis.ticks=element_blank(),
          axis.title.x=element_blank(),
          axis.title.y=element_blank(),legend.position="none",
          panel.background=element_blank(),panel.border=element_blank(),panel.grid.major=element_blank(),
          panel.grid.minor=element_blank(),plot.background = element_rect(fill = "azure2"))
  
  name <- paste0("star_", as.character(i),".png")
  ggsave(name)
}
