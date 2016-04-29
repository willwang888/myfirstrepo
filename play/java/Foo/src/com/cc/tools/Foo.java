package com.cc.tools;

import java.io.*;
import java.util.HashSet;


public class Foo {

  public static void main(String[] args) {
      String x = new String("ab");
       x = change(x);
      System.out.println(x);
  
      int[] arr = new int[3];
      System.out.println(arr.length);

      String str = "abc";
      System.out.println(str.length());

      PrintStream StdOut = System.out;

//
        PhoneNumber a = new PhoneNumber(609, 258, 4455);
        PhoneNumber b = new PhoneNumber(609, 876, 5309);
        PhoneNumber c = new PhoneNumber(609, 003, 5309);
        PhoneNumber d = new PhoneNumber(215, 876, 5309);
        PhoneNumber e = new PhoneNumber(609, 876, 5309);
        StdOut.println("a = " + a);
        StdOut.println("b = " + b);
        StdOut.println("c = " + c);
        StdOut.println("d = " + d);
        StdOut.println("e = " + e);

        HashSet<PhoneNumber> set = new HashSet<PhoneNumber>();
        set.add(a);
        set.add(b);
        set.add(c);
        StdOut.println("Added a, b, and c");
        StdOut.println("contains a:  " + set.contains(a));
        StdOut.println("contains b:  " + set.contains(b));
        StdOut.println("contains c:  " + set.contains(c));
        StdOut.println("contains d:  " + set.contains(d));
        StdOut.println("contains e:  " + set.contains(e));
        StdOut.println("b == e:      " + (b == e));
        StdOut.println("b.equals(e): " + (b.equals(e)));



//



  }

   public static String  change(String x) {
         x = new String("cd99999");
         return x;
  }

 
}



