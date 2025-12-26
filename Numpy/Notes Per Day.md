###    Day 1 of advance Python by Vikas sir  ---- 30 Oct 2025



**Q what is array**



Ans - Array is a collection of homogeneous element

    - array is user define datatype

    - Searching is fast if we use array



**Q Why we use array rather then variable**



Ans - Variable can store single data at a time

    - But array can store number of data at a time



**Q why we use array**



Ans - To access the data of list or tuple





**Q task -- How to find the size of any declared variable**



 Ans -  import sys

        sys.getsizeof(a)



      A single-digit number takes 28 bytes in Python not because the number itself needs that much, but because

      it’s stored inside a full Python object that contains metadata about the number.



-- Python defines integers as objects using a structure

-- The memory not only store the actual value it stores the

 



* Common info for all Python objects
* Reference count
* Pointers
* How many digits used
* Actual value data











###         Day 2 of advance Python  ---- 31 Oct 2025



* **Using for loop without indexing**

 

    -- it means we actually play the value

    -- when we do not use range in for loop that's mean we are picking the value

    -- if we make any change in value during the loop the actual value do not change



* **Using for loop with indexing**

 

    -- it means we actually play the index of value

    -- when we use range in for loop that's mean we are picking the index of value

    -- if we make any change in value during the



1 -- **Numeric Array** (Indexed Array)

 

     -- array is an array where each element is identified by a number(index)

     -- The index starts from 0 by default (in most language)

     -- Used when we just want to store a list of value



2 -- **Associative Array**



    -- An associative array is an array where each element is identified by a key(name) instead of number

    -- Also know as a dictionary or map(depending on language)

    -- Used when we want to store Key-value pairs



**Q task -- How to store null value in list or array**



 Ans -  For list use None

        For array use np.nan









###          Day 3 of advance Python  ---- 1 Nov 2025



-- Reshape(row, col) for 2D          it is a manipulation function of numpy array

-- Reshape(template,row,col) for 3D







###          Day 4 of advance Python  ---- 3 Nov 2025







-- If we want to print the element of this \[\[2,3,4,5,6,6]] in vertical line one by one

 

   -- 1. we can create for loop to iterate the element but will get more complex when applying for 3D,4D.....

   -- 2. To solve the above problem we use np.nditer():

   -- 3 if we want to see indexing along with the element soo we have to use np.ndenumerate():





-- np.zeros(row, col)              it will generate constant value of zero(0) and gives float as default datatype



-- np.ones(row, col)               it will generate constant value of ones(1) and gives float as default datatype



-- np.empty((row, col),dtype= int) it will generate constant value and gives float as default datatype



-- np.eye()                        it will generate identity metrics 1 in diagonal and fill 0 in remaining









###          Day 5 of advance Python  ---- 4 Nov 2025



-- arrange(start, stop-1, step size(1))



-- np.random.rand(3)   generate the 3 random number as a float datatype



-- np.random.randint(4) generate a single number between 1 to 4(exclusive) as integer datatype

   np.random.randint(1,6,6) generate  6 number between 1 to 6(exclusive) as integer datatype



-- np.linspace(start,stop(inclusive),range)  generate float values evenly separated we can also set endpoint as

                                             false and can find interval between the values

 

-- np.linspace(start,stop(inclusive),range,endpoint = False,retstep = True)







--------- now we study the manipulation functions



-- n.flatten()  used to convert 2D array in 1D however the original array do not change when we assign a new value

                to array



Ex :- n =np.array(\[\[2,3],\[4,6],\[5,6]])

      d = n.flatten()

      print(d)

      d\[1]=600

      print(d)

      print(n)     # see the original values do not get change even i assign a new value above





-- n.ravel()    used to convert 2D array in 1D however the original array getschanged when we assign a new value

                to array





Ex :- k = np.array(\[\[2,3],\[4,6],\[7,8]])

      k

      h = k.ravel()

      print(h)

      h\[1] = 390

      print(h)

      print(k)    # see the original values get changed when i assign a new value above







###         Day 6 of advance Python  ---- 5 Nov 2025





continued the manipulation function of numpy array



-- np.split(A,2)   it will divide the array in two equal list or tuple but if the array values goes out of bound

                   it will give an error



------------------------- To Remove The Above Error We Use array\_split Given Below -----------------------------





-- np.array\_split(A,2)   it will divide the array in two equal list or tuple but if the array values goes out of

                         bound it will fill by null value







-- sort(a) it rearrange the array values order in ascending or descending manner



-- np.concatenate(\[])  \*\* datatype and size should be same in concatenate







###       Day 7 of advance Python  ---- 6 Nov 2025





-- Transpose   used to reduce dimentions



   ex 1 :- w = A.T   in this first the original memory is save and the second transpose memory is also gets saved

                   meaning the source code memory(original data) also exixt and the generated code memory also

                   exist





   ex 2 :- B = np.transpose(\[\[],\[],\[]])  here only the transpose memory gets saved







----------------------- Conditional based  functions -----------------------





-- np.where(conditions)       --- \*\*\* it returns the indexing value

 



    ex :-  np.where(S<0,1,S)     ---- it acts like find and replace all function







---------------------- Mathematical and statistical given in notes to do --------------------------



    add vs sum









###      Day 8 of advance Python  ---- 7 Nov 2025



-- save

-- load















###      Day 9 of advance Python  ---- 8 Nov 2025





-----        solving questions given by sir











### Day 10 of advance Python  ---- 10 Nov 2025







---- slicing practice







### Day 11 of advance Python  ---- 11 Nov 2025







---- slicing practice







### Day 12 of advance Python  ---- 12 Nov 2025







-- copy behave as (normal view)



-- view behave as (algorithmic view)





\# pandas -----------------------------------

&nbsp; 

we can create series and data frame using panda



series ---  works only on single column



data frame --- works on both single and multiple columns



































