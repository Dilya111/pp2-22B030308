{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {
    "collapsed": false
   },
   "outputs": [],
   "source": [
    "# Dictionary of movies\n",
    "\n",
    "movies = [\n",
    "{\n",
    "\"name\": \"Usual Suspects\", \n",
    "\"imdb\": 7.0,\n",
    "\"category\": \"Thriller\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Hitman\",\n",
    "\"imdb\": 6.3,\n",
    "\"category\": \"Action\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Dark Knight\",\n",
    "\"imdb\": 9.0,\n",
    "\"category\": \"Adventure\"\n",
    "},\n",
    "{\n",
    "\"name\": \"The Help\",\n",
    "\"imdb\": 8.0,\n",
    "\"category\": \"Drama\"\n",
    "},\n",
    "{\n",
    "\"name\": \"The Choice\",\n",
    "\"imdb\": 6.2,\n",
    "\"category\": \"Romance\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Colonia\",\n",
    "\"imdb\": 7.4,\n",
    "\"category\": \"Romance\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Love\",\n",
    "\"imdb\": 6.0,\n",
    "\"category\": \"Romance\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Bride Wars\",\n",
    "\"imdb\": 5.4,\n",
    "\"category\": \"Romance\"\n",
    "},\n",
    "{\n",
    "\"name\": \"AlphaJet\",\n",
    "\"imdb\": 3.2,\n",
    "\"category\": \"War\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Ringing Crime\",\n",
    "\"imdb\": 4.0,\n",
    "\"category\": \"Crime\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Joking muck\",\n",
    "\"imdb\": 7.2,\n",
    "\"category\": \"Comedy\"\n",
    "},\n",
    "{\n",
    "\"name\": \"What is the name\",\n",
    "\"imdb\": 9.2,\n",
    "\"category\": \"Suspense\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Detective\",\n",
    "\"imdb\": 7.0,\n",
    "\"category\": \"Suspense\"\n",
    "},\n",
    "{\n",
    "\"name\": \"Exam\",\n",
    "\"imdb\": 4.2,\n",
    "\"category\": \"Thriller\"\n",
    "},\n",
    "{\n",
    "\"name\": \"We Two\",\n",
    "\"imdb\": 7.2,\n",
    "\"category\": \"Romance\"\n",
    "}\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Checking if Dark Knight is greater than 5.5\n",
      "\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "# Write a function that takes a single movie and \n",
    "# returns True if its IMDB score is above 5.5\n",
    "\n",
    "def check_score_greater(movie): \n",
    "    if(movie['imdb']>5.5):\n",
    "        return True\n",
    "    else:\n",
    "        return False\n",
    "\n",
    "    \n",
    "# Could change movie title from Dark Knight to any other\n",
    "# and change to the corresponding element # from 2 to \n",
    "# whichever movie you want to see is above 5.5 or not\n",
    "print ''\n",
    "print 'Checking if Dark Knight is greater than 5.5'\n",
    "print ''\n",
    "is_greater=check_score_greater(movies[2])\n",
    "if(is_greater):\n",
    "    print 'True'\n",
    "else :\n",
    "    print 'False'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "List of movies with an IMDB score > 5.5: \n",
      "\n",
      "[{'category': 'Thriller', 'imdb': 7.0, 'name': 'Usual Suspects'}, {'category': 'Action', 'imdb': 6.3, 'name': 'Hitman'}, {'category': 'Adventure', 'imdb': 9.0, 'name': 'Dark Knight'}, {'category': 'Drama', 'imdb': 8.0, 'name': 'The Help'}, {'category': 'Romance', 'imdb': 6.2, 'name': 'The Choice'}, {'category': 'Romance', 'imdb': 7.4, 'name': 'Colonia'}, {'category': 'Romance', 'imdb': 6.0, 'name': 'Love'}, {'category': 'Comedy', 'imdb': 7.2, 'name': 'Joking muck'}, {'category': 'Suspense', 'imdb': 9.2, 'name': 'What is the name'}, {'category': 'Suspense', 'imdb': 7.0, 'name': 'Detective'}, {'category': 'Romance', 'imdb': 7.2, 'name': 'We Two'}]\n"
     ]
    }
   ],
   "source": [
    "# Write a function that returns a sublist of movies \n",
    "# with an IMDB score above 5.5. \n",
    "\n",
    "def sublist_movies_high_score(movies): \n",
    "    out_list=[];\n",
    "    for i in range(0,len(movies)):\n",
    "        curr_movie=movies[i];\n",
    "        if curr_movie['imdb']>5.5:\n",
    "            out_list.append(curr_movie)\n",
    "    return out_list\n",
    "\n",
    "print ''\n",
    "print 'List of movies with an IMDB score > 5.5: '\n",
    "print ''\n",
    "out_list=sublist_movies_high_score(movies)\n",
    "print out_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Movies in the Thriller are: \n",
      "\n",
      "[{'category': 'Thriller', 'imdb': 7.0, 'name': 'Usual Suspects'}, {'category': 'Thriller', 'imdb': 4.2, 'name': 'Exam'}]\n"
     ]
    }
   ],
   "source": [
    "# Write a function that takes a category name and returns \n",
    "# just those movies under that category.\n",
    "\n",
    "def return_movie_category(movies,cat_name): \n",
    "    out_list=[]\n",
    "    for i in movies:\n",
    "        curr_cat=i['category']\n",
    "        if cat_name.lower()==curr_cat.lower():\n",
    "            out_list.append(i)\n",
    "    return out_list\n",
    "\n",
    "# You could change to any category you'd like\n",
    "print ''\n",
    "print 'Movies in the Thriller are: '\n",
    "print ''\n",
    "out_list=return_movie_category(movies,'Thriller')\n",
    "print out_list"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Average IMDB score of all the movies is: \n",
      "6.48666666667\n"
     ]
    }
   ],
   "source": [
    "# Write a function that takes a list of movies and computes \n",
    "# the average IMDB score.\n",
    "\n",
    "def avg_imdb_score(movies): \n",
    "    avg_score=0\n",
    "    tot_movies=len(movies)\n",
    "    for i in movies:\n",
    "        avg_score=avg_score+i['imdb']\n",
    "    avg_score=avg_score/tot_movies\n",
    "    return avg_score\n",
    "\n",
    "print ''\n",
    "print 'Average IMDB score of all the movies is: '\n",
    "s1=avg_imdb_score(movies)\n",
    "print s1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "collapsed": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Average IMDB of movies in the Thriller category is: \n",
      "5.6\n"
     ]
    }
   ],
   "source": [
    "# Write a function that takes a category and computes \n",
    "# the average IMDB score (HINT: reuse the function \n",
    "# from question 2.)\n",
    "\n",
    "def avg_imdb_acc_to_cat(movies,cat_name): \n",
    "    cat_movies=return_movie_category(movies,cat_name)\n",
    "    avg_score=avg_imdb_score(cat_movies)\n",
    "    return avg_score\n",
    "\n",
    "print ''\n",
    "print 'Average IMDB of movies in the Thriller category is: '\n",
    "s2=avg_imdb_acc_to_cat(movies,'Thriller')\n",
    "print s2"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 2",
   "language": "python",
   "name": "python2"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 2
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython2",
   "version": "2.7.10"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}