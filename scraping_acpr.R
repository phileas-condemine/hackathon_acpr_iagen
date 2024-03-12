library(rvest)
library(dplyr)
library(xml2)
library(stringr)
library(data.table)
library(pbapply)
library(purrr)
# write R code using xml2 & rvest libraries to get all href attributes in the following url page : 
url = "https://acpr.banque-france.fr/site-map"


plan <- read_html(url)
plan %>% html_attr("href")

# Select all the anchor tags and extract the 'href' attribute  
hrefs <- plan %>%  
  html_nodes("a") %>%  
  html_attr("href")  

# Print out the hrefs  
print(hrefs)  

useful_links = grep("(^/)|(acpr.banque-france.fr)",hrefs,value=TRUE)
dt_links = data.table(path = useful_links)
dt_links[grepl("^/",path),path := paste0("https://acpr.banque-france.fr",path)]

dt_links = unique(dt_links)


dt_links[grepl("112-",path)]

acpr_html = pblapply(dt_links$path,read_html)





dt_links[,clean_path := str_replace_all(path,"[/.-:\\?]","_")]
dt_links[,clean_path := str_remove(clean_path,"https___acpr_banque-france_fr_")]
# dt_links[,clean_path := substr(clean_path,1,100)]
dt_links$clean_path[1]
# names(acpr_html) <- dt_links$clean_path
names(acpr_html) <- dt_links$path

acpr_html_sub = acpr_html %>% map(function(x){x %>% html_node("#content-region") %>% html_text()})


dt = data.table(text = unlist(acpr_html_sub),url = names(acpr_html_sub))

quantile(nchar(dt$text),0:100/100)


openxlsx::write.xlsx(list(data = dt),"acpr_website_to_text.xlsx")

# map(1:length(acpr_html), function(i){xml2::write_html(x = acpr_html[[i]],file = paste0("acpr_html/",names(acpr_html)[i],".html"))})

res <- map(1:length(acpr_html_sub), function(i){writeLines(text = acpr_html_sub[[i]],con = paste0("acpr_text/",names(acpr_html_sub)[i],".txt"))})


quantile(nchar(acpr_html_sub),0:100/100)



# files = list.files("acpr_text/",full.names = TRUE)
# 
# 
# sapply(files,function(path){
#   path = gsub(".txt$","",path)
#   if(nchar(path)>100){
#     file.rename(paste0(path,".txt"),paste0(substr(path,1,100),".txt"))
#   }
# })
# 
