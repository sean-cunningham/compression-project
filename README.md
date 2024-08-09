# READ ME

## Overview

I found the topic of compression to be very interesting during this course and wnated to dig deeper than were were able to cover in the section on Huffman encoding. For this reason I decided to research different compression algorithms, select a few, and build the algorithms into a application that allows users to upload a file and see how see an output comparing the compression data of the different algorithms.

The application can be accessed at:

## How to Use

This application is pretty bare bones and straight forward. Drag any file into the drop one (or click on the drop zone to navigate toa file). Once the file is chosen it will compress it using via multiple algorithms and show the results of the compression in cards below the drop zone.

Notes on use:

- **Use small files.** These are not great algorithms and large files will take some time to compress. there are to test files in the code base in the api test direectory that can be used. The first is test_file.txt which is a few chapters of Moby dick. The second (rle_test) is in the same directory and is just a txt file with the letter r repeated multiple times. There is solid reasoning for this which will be explained below.
- If you are not able to acess the live application you can do the following:
    - clone the repo
    - download and install docker desktop (https://www.docker.com/products/docker-desktop/)
    - cd into the main directory
    - In the terminal use `docker-compose build && docker-compose up` (this may take a moment)
    - One that loads open a browser and navigate to localhost:5173
    - You should be able to see that running applcation here
    - If you have issues try deleteing the node modules directory inside ghi and run `npm install` then repeat the docker compose comands

## Data Structures

I ended up selecting Run Length Encoding and Lempel Ziv Welch as my compression algorithms. I also created an algorithm for Burows Wheeler Transformation (which is used to reorganize data to make it more compressable)

### Run Length Encoding

This algorithm is probably he most basic algorithm for ending. All it does is scan a file for recurring adjacent bytes and groups them by appending the number of recurring instances to a single instance of that byte.

For example: aaaaaabbbbbbaaabbb would compresss to 6a6b3a3b. As you can see this results in a smaller file the original.

The key weak point of this algorithm is that it depends on large groups of recurring bytes to be efficient. As you can see with the first test file it actually makes the file larger than the original. Hence the reason for the other test file to show that it actually works for the right kind of data.

### Lemper Ziv Welch

This algorithm is a bit cooler and was also a bit harder to grasp. It is dictionary based. It first loads a dictionary with the first 256 bytes. it then scnas the file byte by byte to see if that byte is already in the dictionary. if it is it is replaced by that dictionary key. If it is not it is grouped with the next byte. if that grouped byte string is not in the dictionary it is added and thei dictionary key is incremented by one. As you continue down the list you get increasingly more grouped bytes added intoe the dictionary which can then be replaced by the correspoding key. This one was a bit challenging to inmplement (espsecially the decompression) but was also more fun.

### Burrows Wheeler Transformation

This is not a compression algorithm, but a method to arrange your data to be more compressable. It is confusing to me to be honest, but what it essentially does is create an array or every version of a byte string after having been rotated one spot for each byte in the string. for example. banana becomes abanan->nababa->anabab... this continues until you get all the way back around. sort these new byte strings alphabetically, and then create a new byte string from the last value in each. this new byte string 'should' be more compressible because it should have more grouped bytes. I'm not sure how well it worked for me and honestly I think I messed up the decompression because it did not work correctly for all tests.

### Key Challenges and lessons learned

1.  Enjoy the scope creep but don't over due it. Save yourself time to get the thing done. As of this writing (Thursday evening) I just broke my front end deployment and need to trouble shoot to even have a working application at this point. In all fairness this last minute rush to completion is pretty par for the course for the end of a sprint for me so I'm optomistic that be the time your reading this the code will work.
2.  I forgot how much I have forgotten about basically everything I did with this project. I work almost exclusively writing yaml files for kubernetes deployments at work. I havent touched React or Python in a while and had quite a steep re-learning curve. this is actually why I chose to do this though. It was a fun way to shake off the cobwebs.
3.  The AWS deployments have given me some challenges. I'm deployeing with elastic beanstalk and this is the fist time I have done this. Again, I did this for the learning experience but in retrospec maybe not the best idea with an approaching deadline. fingers crossed I fix this deployment issue.
4.  I wich I would have spent more time on the algorithms. If given more time I would have ejoyed tinkering with te algorithms more to make them more efficent. For example, the RLE actually makes my files larger in most cases. I believe with some tinkering I could have at least made this less of an issue. Maybe this is an exercise for a raininy saturday, right?

## Technology Implemented

Python, Javascript, React, FastAPI, Vite, Docker, AWS Elastic Beanstalk
