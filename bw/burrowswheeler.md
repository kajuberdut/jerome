## Burrows Wheeler 
### Use
This transformation is useful because it 
* a. is reversible 
* b. tends to create long runs of the same character which increases the efficiency of runlength encoding.

### Forward Transformation
To execute a burrows wheeler transformation:
1. Create a matrix of all possible rotations of a string with $ appended.

    |N|Rotations |
    |-|--------- |
    |1|banana$   |
    |2|$banana   |
    |3|a$banan   |
    |4|na$bana   |
    |5|ana$ban   |
    |6|nana$ba   |
    |7|anana$b   |

2. Sort the matrix in lexicographic order:

    |N|Sorted|
    |-|------|
    |2|$banana|
    |3|a$banan|
    |5|ana$ban|
    |7|anana$b|
    |1|banana$|
    |4|na$bana|
    |6|nana$ba|


3. Take the last character of each row.
    ```
    -> annb$aa
    ```

### Reverse Transformation

The inverse Burrows Wheeler tranform walks backward through the first (f) and last (l) column of the matrix above.
The first column need not be provided or stored, it is the same as the transformed string sorted in lexicographic order.

1. Given (l) the last row (our "annb$aa" above,) with the index in l (l[i]) shown:

    | l | l[i] |
    | - | ---- |
    | a | 1    |
    | n | 2    |
    | n | 3    |
    | b | 4    |
    | $ | 5    |
    | a | 6    |
    | a | 7    |

 2. We can order those to get f. If we keep the indexes from above we have f + f's index in l (l[i]):

    |f|l[i]|
    |-|----|
    |$|4   |
    |a|0   |
    |a|5   |
    |a|6   |
    |b|3   |
    |n|1   |
    |n|2   |

3. Begining with the special mark appended to the original string, walk to the nth row (f[i]) of f where n is the index of f in l (l[i]).


    |f[i]  |  (f) | (l) |  l[i]|
    | ---- |  --- | --- | ---- |
    |  0   |   $  |  a  |    4 |
    |  1   |   a  |  n  |    0 |
    |  2   |   a  |  n  |    5 |
    |  3   |   a  |  b  |    6 |
    |  4   |   b  |  $  |    3 |
    |  5   |   n  |  a  |    1 |
    |  6   |   n  |  a  |    2 |
    
    1. Index of $ in l is 4
    2. f[4] = b that was [3] in l
    3. f[3] = a l[6]
    4. f[6] = n l[2]
    5. f[2] = a l[5]
    6. f[5] = n l[1]
    7. f[1] = $

The original string is seen above in the character to the right of the "="s.