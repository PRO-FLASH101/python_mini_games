# to find the amount of triangles
amount_triangles_wanted = int(input("How many triangles do you want? \nEnter here: "))

#the base stuff
triangle = "        *    \n      * * *   \n    * * * * *  \n  * * * * * * * \n* * * * * * * * *\n"
the_arrow = "        *    \n      * * *   \n    * * * * *  \n  * * * * * * * \n* * * * * * * * *\n      * * *   \n      * * *   \n      * * *   \n      * * *   \n      * * *   "

#the christams tree
final_tree = amount_triangles_wanted * triangle + the_arrow

print(final_tree)
