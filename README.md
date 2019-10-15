# Account_intelligence_Test
Account Intelligence test for RedHat

This project should be pretty straight forward, clone the repo into your own virtualenvironment, install the dependencies in the requirements.txt and change the DB in the config and you should be good to go.

The three methods you should use are:
 -/actor/<string:actor> where you replace what's after the second slash with what actor you'd like to search for, it returns all the movies the actor/actress was in along with what other actors were in it and budget and gross
-/topGenres which returns the top 10 genres by net profit. This is computed by subtracting the budget from the gross. This method takes into account movies with multiple genres, it searches through all the genres for a movie and if the movie has that genre it will be accounted for in the profitability of the genre. For example, if a movie has action, comedy and drama it will be counted in all three categories.
-/topActors which which returns the top 10 genres by net profit. This is computed by subtracting the budget from the gross. This method takes into account if an actor was actor 1, 2 or 3 in the movie.

I alsowant to say that I didn't structure the project in a typical mvc fashion. If I was going to expand on this project, I'd add directories for the model, the app, the tests and the business logic to give it more structure. I also forgot to add the csvs to the .gitignore I hope that's not a big deal. 
