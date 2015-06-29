#include <iostream>
#include <string>

// function declarations
std::string msg(std::string);
void println(std::string);

// main func
int main()
{
  for( int a = 10; a <= 11; a = a + 1 )
  {
    std::cout << "Hello World!\n";
    std::cout << "Well done!  Bravo!!!! \n";
  }

  println("Calling msg function...");
  println( msg("I'm the message returned") );
}

// other funcs
std::string msg(std::string s)
{
  return s;
}

void println(std::string s)
{
  std::cout << s << "\n";
}
