/*
This program created by Matthew Mahan of team Pterodactyl. 
We discovered the password without the use of java reflection.
This program was created after completing the challenge. 
*/


import java.lang.reflect.*;

public class Reflect {

	public static void main(String[] args) throws Exception {
		
		Hint h = new Hint();

		// get name
		Class c = h.getClass();
		print("Class name: " + c.getName());

		// get the constructor 
		try {
			Constructor con = c.getConstructor();
			print("The name of the Constructor is " + con.getName());	
		} catch (Exception e) {

		}

		print("----------------------------------------------------------------------------");

		// get all the methods 
		Method [] allmethods = c.getDeclaredMethods();
		for (Method m : allmethods) {
			print("Method name is " + m.getName() + " and the parameters are " + m.getParameters());
		}

		print("----------------------------------------------------------------------------");

		// try the methods out
		Method methodcall1 = c.getDeclaredMethod("getLength");
		methodcall1.invoke(h);

		Method methodcall2 = c.getDeclaredMethod("setLength", int.class);
		methodcall2.invoke(h, 9999); 
		// Seems that "length" is responsible for how much of a string is printed 
		// by superprivatefunction

		Method methodcall3 = c.getDeclaredMethod("superprivatefunction");
		methodcall3.setAccessible(true);
		methodcall3.invoke(h);

		// resulting text: 
		/*
		hint: You are so close. 
		You should have received a sha256 hash of the final password you'll need to open the pdf. 
		The actual password is actually a concatenation of two of the top 100 passwords of 2022. 
		A list can be found at: https://tinyurl.com/ee58bacp 
		You should be able to write a quick script to hash all possible combinations of those passwords and compare it to the provided hash in order to find the correct final password to unlock the pdf 
		*/

	}

	// print macro for convenience 
	public static void print(String s) {
		System.out.println(s);
	}

}