using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CondConverter
{
    class CondConv
    {
        static void Main(string[] args)
        {

            string cond_string = "";


            //Read in initial string
            while (true) {
                string input = Console.ReadLine();

                if (input == "")                
                    break;               
                else
                    cond_string += input;
                
           }
            
            Console.WriteLine(cond_string);


            //Build new string + return






        }
    }
}
