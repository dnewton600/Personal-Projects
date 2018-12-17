library(dplyr)
library(tidyr)
library(ggplot2)
library(haven)
library(grid)

ATP_W24 <- read_sav("Documents/Personal Projects/Datasets/USA_Trends_24_Jan17/ATP W24.sav")
pew_data <- ATP_W24

# dimension of data
dim(pew_data)

# Select columns of interest
rel_group <- select(pew_data, matches("REL3[ABCDEFGHI].*"))
names(rel_group) <- c("Evangelicals",
                      "Catholics",
                      "Mormons",
                      "Jews",
                      "Muslims",
                      "Athiests",
                      "Buddhists",
                      "Hindus",
                      "Protestants")

# Make 'Relgion' into variable
rel_group_tdy <- gather(rel_group,"Religion","Rating")
head(rel_group_tdy)

# Plot distribution with geom jitter
ggplot(data = rel_group_tdy, aes(x = Religion, y = Rating)) +
  geom_jitter(alpha = .05)

# Boxplot to show quartiles
ggplot(data = rel_group_tdy, aes(x = Religion, y = Rating)) +
  geom_boxplot()

# compute group medians and sort
sorted_medians <- rel_group_tdy %>%
  group_by(Religion) %>%
  summarise(MedianRating = median(Rating)) %>%
  arrange(desc(MedianRating))

grid.table(sorted_medians)
# How do people view offensive jokes?
