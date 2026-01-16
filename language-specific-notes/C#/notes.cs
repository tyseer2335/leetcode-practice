// -- IMPORT  STATEMENTS --
using System; // import math in python
using System.Collections.Generic; // from collections import ... this imports List, Dictionary, Stack ect
using System.Linq;


// -- Hello World -- 
Console.WriteLine("Hello, World!");


// -- Data Types -- 
// Declaring variables with explicit types
int x = 5;   
Console.WriteLine("int x = " + x);

string s = "Hello, World!";   
Console.WriteLine("string s = " + s);

char c = 'A';
Console.WriteLine("char c = " + c);

float f = 1.67F; // Need to cast this to a float since compiler thinks its a double by default
Console.WriteLine("float f = " + f);

long y = 5000000000L; // Same here but for a int
Console.WriteLine("long y = " + y);

double d = 3.14159;  
Console.WriteLine("double d = " + d);

decimal dec = 19.99M; // Decimal
Console.WriteLine("decimal dec = " + dec);

bool b = true; 
Console.WriteLine("bool b = " + b);

// Note that: byte → short → int → long → float → double → decimal 

// We can use var to dynamically infer the type
var name = "Tyseer"; // type inference 
Console.WriteLine("var name = " + name);


// -- Arithmetic Operations -- 
// Performing basic math operations between different numeric types
int a = 10; 
double num = 3.0; 

double sum = a + num; 
Console.WriteLine("Sum (10 + 3.0) = " + sum);

double difference = a - num;  
Console.WriteLine("Difference (10 - 3.0) = " + difference);

// Cast it to an int (this truncates the decimal, rounds toward zero)
int intDifference = (int)difference; 
Console.WriteLine("Casted to int = " + intDifference);


// -- Floor and Ceiling --
// Floor rounds down to the nearest integer, Ceiling rounds up
double value = 7.8;
Console.WriteLine("Original value = " + value);
Console.WriteLine("Math.Floor(7.8) = " + Math.Floor(value));   // 7  - rounds down
Console.WriteLine("Math.Ceiling(7.8) = " + Math.Ceiling(value)); // 8  - rounds up  

// Note that Floor and Ceiling return a double type, we can cast back to an int 
int flooredValue = (int)Math.Floor(value); // 7
int ceiledValue = (int)Math.Ceiling(value); // 8
Console.WriteLine("Floored as int = " + flooredValue);
Console.WriteLine("Ceiled as int = " + ceiledValue);


// -- Modulus Operator --
// Returns the remainder after division
int remainder = 10 % 3;  // 1  (10 ÷ 3 = 3 remainder 1)
Console.WriteLine("10 % 3 = " + remainder);

int isEven = 8 % 2;      // 0  (even numbers have no remainder)
Console.WriteLine("8 % 2 = " + isEven + " (0 means even)");