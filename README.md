# Cipher-_basics
<head>
<b>
<h1>Introduction</h1>
<h2>The meaning of encryption, decryption, and its history:</h2>
When we encrypt a text, we turn it from an understandable text with meaning (plaintext/original) into a meaningless set of letters and signs (cipher text).
On the other hand, decrypting is turning a set of letters and signs back from being meaningless (ciphered) into a meaningful message that the user can understand (deciphered), which is the complete copy of the original text.
General History
<h3>First appearance</h3>
To begin, the first evidence of the use of cryptography was discovered in an inscription carved around 1900 BC in the chamber of a nobleman's tomb in Egypt.The scribe used some unfamiliar hieroglyphic symbols in place of more ordinary ones. The purpose was not to hide the message, but to change its shape and meaning, making the script not understandable unless it returned to its true form. Even though the inscription was different, it was still based on the original text in some way.
Evidence of some use of encryption and decryption (cryptography) appeared in most major ancient civilizations. For example, Kautilya's "Arthshashtra," a classic work on government, talks about India's spy service and how assignments were given to spies in "secret writing."
<h3>In the world war,</h3>
During the first two years of World War I, code systems were used for high-command and diplomatic communications, just as they had been for centuries, and cipher systems were used almost exclusively for tactical communications. However, field cipher systems, such as the U.S. Signal Corps’s cipher disk mentioned above, lacked sophistication (and security), however. Nevertheless, by the end of the war, some complicated cipher systems were used for high-level communications, the most famous of which was the German ADFGVX fractionation cipher, described in the section "Cryptography: Product ciphers" (Simmons, 2016).
Modern use
<h3>In modern days,</h3> cryptography is widely used in banks and messaging apps such as WhatsApp, where text and messages are all end-to-end encrypted.

![image](https://user-images.githubusercontent.com/99323462/185692064-a55c2fa0-2346-4ddd-8e04-044257b3f2c7.png)

</b>

<b>

<h1>The code:</h1>
<h2>main:</h2>

The main code is used to call the other functions defined below according to the user input.

To further explain the main function, start with a large while loop that will keep the code running until the user decides to turn it off, either manually or by deciding to not continue in the last question. Furthermore, the main function is used to determine whether the user wants to

1-Use an old file or create a new one.

2-If he wants to decrypt, encrypt, or count

3-In case the user chooses to encrypt or decrypt, The user will be presented with the choice of the following cipher languages: Ceaser, Playfair, and Join.

A while loop is created after each needed input to assure that the input is valid and ask the user to reenter their choice if necessary.

According to each choice, the user will be presented with further questions to input. For instance, if he chooses to use an old file, he will be asked to insert its name. If he chooses to create a new one, the user will be asked to insert the new input "text" he wants to include in the file.

![image](https://user-images.githubusercontent.com/99323462/185693804-f5cdab3b-e211-40c0-adcb-10b6e6f4d28f.png)

<h2>Ceaser function:</h2>
Variables that must be inputted for the function
1) A filename to read from, 
2) a file to save the output to, and
3) an integer value to calculate the shift.
4) a statement of true or false to determine if the code used is a joint one.

The following code defines the first cipher language "Ceaser". The code starts with opening the allocated "filename" file as r "read" in a new variable named "f". Then a new variable is also introduced named "answer", in which the "wheresave" file is opened as "write" to save the new output. Finally, an empty string is introduced.

The major part of the function starts with a for loop where "I" moves across the lines in the file where the split function is used to cut the line into words under a variable named x and a new variable is introduced called "n" and it is used to count the number of words in each line to be able to jump a line in the right location. Then a nested loop is introduced to move across each word in a line under the variable "j". Furthermore, the variable "n" is increased by a value of 1, and a new variable "m" with a value of zero, then a space is inserted into the string to separate each word from the other. Moreover, another nested for loop is used to move across each letter in a word where the current letter is called by variable "z". In this instance, the letter is shifted based on an if statement regarding if it is an upper case or a lower case .

If the letter was an upper case, then the num (the shift, which was inputted by the user) is either added or subtracted from the value "65", which stands for the ordinal "ord" of the first letter "A". The shift is then divided by 26, which is the number of letters in the English alphabet. After all of that, the shift is determined and is added to the ordinal of the letter allocated by the nested loop/variable "z", which is then added to the ordinal of the first letter "A". Finally, the resulting number is transformed into a letter through the use of the "chr" function to be introduced as the new letter in the variable "Q".
*In the case of lowercase letters, the process is repeated. However, instead of using the value 65, it is replaced by 97, which is the ordinal of "a".
After this, the letter is added/inserted into the string (string+=Q) and the value of variable "m" is increased by 1 to count the number of letters in a word. Afterwards, another if statement is used which states that if the value of variable "n", which stands for the number of words in a line, equales the "len" function of variable "x" and if the value of variable "m", which stands for the number of letters in a word, equals the function "len" of variable "j", then the code will insert a line skip/space (n) into the string.

At this point, the changes in the function output have ended. However, what is left is how the function will present the output and that depends on the user input on what process was used (encryption or decryption) and if it is a single or joined use of cipher language.
Finally, the files are closed and the function returns the new file associated with the "answer" variable.

![image](https://user-images.githubusercontent.com/99323462/185694329-3a99923c-378a-4c3b-a257-8516e8317094.png)

<h2>Playfair function</h2>
<h3>Index finder:</h3>

The index finder is used to move around the matrix with ease by determining the column and row of each letter.

![image](https://user-images.githubusercontent.com/99323462/185694680-1eef69b5-2cbe-40b7-b6e5-db6169e12f50.png)


<h3>File reader with doubles and evens:</h3>

The letter j is replaced in the alphabet by the letter I.

And "X" is placed between all double letters. For example, "hello" would become "helxlo."

A "Q" is added at the end of any odd-numbered sentence to turn it into an even one.

![image](https://user-images.githubusercontent.com/99323462/185694767-00211e5f-4246-4ff6-85e6-36b8a65725ee.png)


<h3>Matrix</h3>

This part is used to create the alphabet matrix, which is based on 25 letters, as we will remove the letter "J" to create an equal square.

The matrix will move in alphabetical order after starting with the keyword inputted by the user as long as the letter is not found in the keyword itself.

![image](https://user-images.githubusercontent.com/99323462/185694845-f8f9cb6b-504e-4d4b-bec3-c2cee9c3f074.png)


<h3>Letter replacer:</h3>

The following is used to replace the letters according to the three situations of play (vertically associated, horizontally associated, and box-like transfer).
Every two letters are combined. Where n1 stands for the first letter, while n2 stands for the second letter. The value is divided by 5 as the matrix is created by 25 letters to create a 5*5 square, which makes it possible for the code to move across the matrix with ease .

![image](https://user-images.githubusercontent.com/99323462/185694978-55f994f7-0df1-4b68-a09d-d2a26f35c8cc.png)

<h3>When decrypting:</h3>
Remove the added X and Q ,

![image](https://user-images.githubusercontent.com/99323462/185695119-0ee3bb7b-735f-4a67-a0fb-421930022a4a.png)

</b>
<b>
<h2>Counting function:</h2>
This function is used to test the accuracy of the code and the cipher language used. The counter function checks the number of words, characters, lines, and repetitions of each letter found in the file before its encryption and after its decryption. Then the user can manually compare both results to notice any problems.

![image](https://user-images.githubusercontent.com/99323462/185695510-d2606f2b-2d76-4bf4-aadc-66956b6dbb01.png)

<h2>Closing the files:</h2>
This part is used in the Playfair function to save the output in the file associated with the variable "answer". Then the files are closed and the output is printed according to the user's previous input regarding (the encryption and decryption).

![image](https://user-images.githubusercontent.com/99323462/185695331-77a5cf0c-5409-4fc5-909c-9f65bb4b56ed.png)

</b>
<b>
<h1> Main Function flow chart (logic):</h1>

![image](https://user-images.githubusercontent.com/99323462/185695712-04e514fa-c48b-4905-83a6-451096bd4924.png)

<h1>Ceaser cipher flow chart:</h1>

![image](https://user-images.githubusercontent.com/99323462/185695828-048bed99-4c58-473d-8b07-e69938f8ed3f.png)
</b>
<b>
<h1>Bibliography:</h1>
Sidhpurwala, H. (2013, August 14). A Brief History of Cryptography. Red Hat Customer Portal. Retrieved December 5, 2021, from https://access.redhat.com/blogs/766093/posts/1976023
Simmons, G. J. (2016, August 17). cryptology. Encyclopedia Britannica. https://www.britannica.com/topic/cryptology
</head>
