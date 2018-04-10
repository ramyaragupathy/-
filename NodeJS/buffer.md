https://medium.freecodecamp.org/do-you-want-a-better-understanding-of-buffer-in-node-js-check-this-out-2e29de2968e8
--
## Binary data, what’s that?
You probably already know that computers store and represent data in binaries. Binary is simply a set or a collection of 1s and 0s. For example, the following are five different binaries, five different sets of 1s and 0s:

10, 01, 001, 1110, 00101011

Each number in a binary, each 1 and 0 in a set are called a Bit, which is a short form of **Binary digIT**.

To store or represent a piece of data, a computer needs to convert that data to its binary representation. For example, to store the number 12, a computer needs to convert 12 to its binary representation which is 1100.

How does a computer know how to do this conversion? Well, it’s pure math. It’s the simple binary numeral system we learned in basic math — expressing a number in the base-2 numeral system. Computers understand that math.

But numbers are not the only data type we work with. We also have strings, images, and even videos. Computers know how to represent all types of data in binaries. Let’s take strings, for example. How will a computer represent the string “L” in binaries? To store any character in binaries, Computers will first convert that character to a number, then convert that number to its binary representation. So for the string “L”, computers will first convert L to a number that represents L. Let’s see how.

Open your browser console and paste the following code snippet and then hit enter:`"L".charCodeAt(0)`. What did you see? The number 76? That is the **_number representation or Character Code or Code Point of the character L_**. But how does a computer know what exact number will represent each character? How does it know to use the number 76 to represent L?

### Character Sets
Character Sets are already defined rules of what exact number represents each character. We have different definitions of these rules.The very popular ones include Unicode and ASCII. JavaScript plays really well with Unicode Character Sets. In fact, it is the Unicode in your browser that states that 76 should represent L.

So we’ve seen how computers represent characters in numbers. Now, the computer will, in turn, represent the number 76 to its binary representation. You might think, well, just convert 76 to the base-2 numeral system. Not so fast!

### Character Encoding
Just as there are rules that define what number should represent a character, there are also rules that define how that number should be represented in binaries. Specifically, how many bits to use to represent the number. This is called Character Encoding.

One of the definitions for Character Encoding is the UTF-8. UTF-8 states that characters should be encoded in bytes. A byte is a set of eight bits — eight 1s and 0s. So eight 1s and 0s should be used to represent the Code Point of any character in binary.

To understand this, as we mentioned earlier, the binary representation of the number 12 is 1100. So when UTF-8 state that 12 should be in eight bits, UTF-8 is saying that a computer needs to add more bits to the left side of the actual base-2 representation of the number 12 to make it a byte. So 12 should be stored as 00001100. Makes sense?

Therefore, 76 should be stored as 01001100.

This, my friends, is how computers store strings or characters in binaries. Likewise, computers also have specified rules on how images and videos should be converted or encoded and stored in binaries. The point here is, computers stores all data types in binaries, and this is known as binary data.

If you’re super interested in the nitty-gritty of Character Encoding, you might like [this gentle and detailed introduction](https://www.w3.org/International/questions/qa-what-is-encoding).

Now we understand what binary data is, but what are streams of binary data from our introduction to buffer?

## Stream
Stream in Node.js simply means a sequence of data being moved from one point to the other over time. The whole concept is, you have a huge amount of data to process, but you don’t need to wait for all the data to be available before you start processing it.

Basically, this big data is broken down and sent in chunks. So from the original definition of a buffer (“streams of binary data… in the context of… file system”) this simply means binary data being moved in the file system. For example, moving the texts stored in file1.txt to file2.txt.

But how exactly does buffer help us interact with or manipulate binary data while streaming? What exactly is this buffer btw?

## Buffer
We’ve seen that a stream of data is the movement of data from one point to the other, but how exactly are they moved?

Typically, the movement of data is usually with the intention to process it, or read it, and make decisions based on it. But there is a minimum and a maximum amount of data a process could take over time. So if the rate the data arrives is faster than the rate the process consumes the data, the excess data need to wait somewhere for its turn to be processed.

On the other hand, if the process is consuming the data faster than it arrives, the few data that arrive earlier need to wait for a certain amount of data to arrive before being sent out for processing.

That “waiting area” is the buffer! It is a small physical location in your computer, usually in the RAM, where data are temporally gathered, wait, and are eventually sent out for processing during streaming.

We can think of the whole stream and buffer process as a bus station. In some bus stations, a bus is not allowed to depart until a certain amount of passengers arrive or until a specific departure time. Also, the passengers may arrive at different times with different speed. Neither the passengers nor the bus station has control over passengers’ arrival at the station.

In any case, passengers who arrive earlier will need to wait until the bus station decides to send the bus on its way. While passengers who arrive when the bus is already loading or when the bus has already departed need to wait for the next bus.

In whatever the case may be, there is always a waiting place. That is the Buffer to Node.js! Node.js can’t control the speed or time of data arrival, the speed of the stream. It only can decide when it’s time to send out the data. If it’s not yet time, Node.js will put them in the buffer — the “waiting area” — a small location in the RAM, until it’s time to send them out for processing.

A typical example where you could see buffer in action is when you’re streaming a video online. If your internet connection is fast enough, the speed of the stream will be fast enough to instantly fill up the buffer and send it out for processing, then fill another one, and send it out, then another, and yet another… till the stream is finished.

But if your connection is slow, after processing the first set of data that arrived, the video player will display a loading icon, or display the text “buffering”, which means gathering more data, or waiting for more data to arrive. And when the buffer is filled up and processed, the player shows the data, the video. While playing that, more data will continue to arrive and wait in the buffer.

If the player is done processing or playing the previous data, and the buffer is not yet filled up, the text “buffering” will be displayed again, waiting to gather more data to process.

That is **Buffer**!

From the original definition of a buffer, it shows that while in the buffer, we can manipulate or interact with the binary data being streamed. What kind of interaction could we possibly have with this raw binary data? The Buffer implementation in Node.js provides us with a whole list of what is doable. Let’s see some of them.

### Interacting with a Buffer
It is even possible to create your own buffer! Aside from the one Node.js will automatically create during a stream, it is possible to create and manipulate your own buffer. Interesting right? Let’s create one!

Depending on what you want to achieve, there are different ways to create a buffer. Let’s see some.

```javascript
// Create an empty buffer of size 10. 
// A buffer that only can accommodate 10 bytes.
const buf1 = Buffer.alloc(10);
// Create a buffer with content
const buf2 = Buffer.from("hello buffer");
```

Once your buffer has been created, you can start interacting with it

```javascript
// Examine the structure of a buffer
buf1.toJSON()
// { type: 'Buffer', data: [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] }
// an empty buffer
buf2.toJSON()
// { type: 'Buffer',
     data: [ 
       104, 101, 108, 108, 111, 32, 98, 117, 102, 102, 101, 114 
     ] 
   }
// the toJSON() method presents the data as the Unicode Code Points of the characters
// Examine the size of a buffer
buf1.length // 10
buf2.length // 12. Auto-assigned based on the initial content when created.
// Write to a buffer
buf1.write("Buffer really rocks!") 

// Decode a buffer
buf1.toString() // 'Buffer rea'
//oops, because buf1 is created to contain only 10 bytes, it couldn't accommodate the rest of the characters
// Compare two buffers
```
