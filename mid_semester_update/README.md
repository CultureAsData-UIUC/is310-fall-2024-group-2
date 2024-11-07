# Mid-Semester Dataset and Documentation Update
Final dataset link: https://drive.google.com/file/d/1E9O77AfjznqOfkooEgtJZOqrapEKO7dC/view?usp=sharing

### Process and Choices:
*Data collection:*
Our plan for finding/creating a dataset was to search online for databases that would include banned books. This turned out to be more challenging than expected. We first looked at the American Library Association, but they didn’t have much organized information on banned books. They had one dataset linked from PEN America, but we did not have access to it (originally). Members of the group also went in person to the UIUC Library and archives to see if there was any information we could pull on banned books. We looked around online for other possible databases on banned books, like Penn Library, but they had a rather small collection of books that were at least 50 years old. We were looking for recently banned books, as this topic has become rather important in recent years, specifically in states like Florida. Eventually, we found two datasets from PEN America, one with data from 2021-2022, and one with data from 2022-2023. We also contacted them on using their most recent data, for which they gave us access, but we’re still waiting on a response for permission to upload it to GitHub as part of our final dataset. Some of our members also took a trip to the archives, where they received data from 1997-1998 and 1998-1999. These files were scanned and given to us, where we then manually entered each and every datapoint. We merged those datapoints into our set as well. Lastly, some members of our group emailed Professor Emily Knox asking if she knew of any datasets we could use, for which we received a new one, but it was by the same creator as the PEN America data, thus indicating potential overlap between the datasets so we didn’t use it. We renamed some of the PEN America datapoints that had entirely null values, and renamed the columns so the two years of data one another, as the column names slightly changed over time. Other than that, we’ve decided to keep all the datapoints for now, as each ban is useful to us. We also created a new variable in the final dataset that helped us estimate how long a book has been banned for. In the future, we need to “clean” this data more, so that the column names line up with one another more properly, and double-check for overlapping points.

*Challenges:*
The biggest challenges we faced with creating our dataset had to do with finding initial information as well as scraping. Finding organized datasets and databases on banned books took a long time. We originally planned to compare current data with past data, but it was nearly impossible to find data on books that were banned in the past. You can find early instances of book banning, but there are only a couple hundred instances of book bans (in the USA) prior to 1970 that were well documented. It is safe to say that book banning has become more and more popular in recent times. We also had trouble adding to our final dataset. We wanted to include additional information to the books in our dataset like ISBN, genre, etc. However, every website we looked to scrape prohibited it. We also looked on popular dataset websites, but nothing worked there either. We did find a couple large datasets on Kaggle, but there were very few matches between the books in our dataset and the books in the others. Overall, for our dataset to have included ISBN and genre it would’ve shrunk over 10 times in size. We decided that would be helpful to us, and we elected to move forward without those variables. 

*Criteria:*
There are many possibilities for what we can use in our final dataset, so we decided not to rule out any existing data points yet. We looked for any possible biases in our dataset so we could get rid of it, but we never really found any. We used the .unique() command in python to see each possible value from a variable. We also looked for any discrepancies in the data and if we could explain them. We used some techniques from earlier readings like “What Gets Counted Counts” by Catherine D’Ignazio and Lauren Klein to figure out if the way the data was collected could have presented any bias, but we didn’t find any there either. We did find out that Florida and Texas banned the most books. We first thought that the collectors of the data could’ve specifically focused on those two states to skew the data, but that seems rather unlikely. The more plausible explanation is that those two states’ governments have been obsessive over education and banning books from children in recent years (there are many articles that support this). In addition to eliminating bias, we looked for data points that presented no use to us so we could delete them, but we decided to keep everything in. However, we can acknowledge that there are a few variables in our dataset that provide little importance. For reference, the secondary author(s), illustrators(s) and translator(s) variables could provide insights, except they are all almost empty. The vast majority of entries for those variables are NaN, meaning they likely can’t be used for anything. However, there is a possibility that these variables could be used, so we aren’t going to rule them out yet. For example, the illustrator(s) variable could be useful, as if a book has an illustrator to it, it is likely a children’s story. Although we have conducted extensive research to find which data points could be left out of the final dataset, we have not deleted a single point as of yet.


### Content Description:
Our dataset contains 5,971 instances and 40 variables. For our instances that come from PEN America’s Index of School Book Bans July 1, 2021 - June 30, 2022, we combined them with their same index from July 1, 2022 - June 30, 2023. We only kept columns that appear in both of these datasets. We also added an “Estimated Ban Duration in Months” column to show how long it has been since that initial ban of that book in that place. Our other columns include: Title, Author, Secondary Author(s), Illustrator(s), Translator(s), State, District, Date of Challenge/Removal, Ban Status, and Origin of Challenge. These two dataframes were combined by first renaming the columns to match based on their data because the names were slighly tweaked between the years, and using the pandas concat command to merge the dataframes. We then directly combined our manually created archives data directly with this other combined dataframe. 


### Responsibility and Contributions:
This dataset was found by all members of our group, as we each looked into datasets and agreed these were the best ones. Avery and Ryan handled the coding for this dataset. Lhaye and Rebeca visited our archives, got the data scanned, and manually created datasets from it. Henry and Lhaye emailed the creator of the PEN America Index we’re using to see if we can access the in-progress version of the dataset, which is also a work in progress. Henry and Lhaye also emailed Professor Emily Knox who got back to us about using another dataset that we didn’t include for reasons mentioned above. 