import colorama
from colorama import Fore

from regspam import pkmain
from revshell import revshmain

Flag = True

title = """
                                                                                                           
  ****           *                                                        ***** ***                 **    
 *  *************                                                      ******  * **                  **   
*     *********                                                       **   *  *  **                  **   
*     *  *                                                           *    *  *   **                  **   
 **  *  **                    ***    ***                  ****           *  *    *                   **   
    *  ***            ***    * ***  **** *     ****      * **** *       ** **   *       ***      *** **   
   **   **           * ***      *** *****     * ***  *  **  ****        ** **  *       * ***    ********* 
   **   **          *   ***      ***  **     *   ****  ****             ** ****       *   ***  **   ****  
   **   **         **    ***      ***       **    **     ***            ** **  ***   **    *** **    **   
   **   **         ********      * ***      **    **       ***          ** **    **  ********  **    **   
    **  **         *******      *   ***     **    **         ***        *  **    **  *******   **    **   
     ** *      *   **          *     ***    **    **    ****  **           *     **  **        **    **   
      ***     *    ****    *  *       *** * **    **   * **** *        ****      *** ****    * **    **   
       *******      *******  *         ***   ***** **     ****        *  ****    **   *******   *****     
         ***         *****                    ***   **               *    **     *     *****     ***      
                                                                     *                                    
                                                                      **                                  
 by 4ozRabclip                                                                                       
                                                                                                          
                                                                                                          
"""

def menu():
    while Flag:
        colorama.init()
        print(Fore.RED + title)
        print(Fore.WHITE)
        print("1. HTTP Post Flood (aka Phishkiller)\n")
        print("2. Reverse Shell\n")
        choice = input("Select (q to quit): ")

        if choice == "1":
            print("\n")
            pkmain(returnToMenu)
        elif choice == "2":
            print("\n")
            revshmain(returnToMenu)
        elif choice.lower() == "q":
            exit()

def returnToMenu():
    print("\033[H\033[J")  
    menu()





if __name__ == '__main__':
    menu()
