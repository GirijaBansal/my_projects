#include <iostream>

using namespace std;

int main()
{
    int n=21;
    int a;
    int ch;
    int k=0;
    cout<<"\t\t\t\t21 MATCH  STICKS  GAME \n\n\n\n\n";
    cout<<"players can choose minimum 1 and maximum 3 sticks\n\n";
    for(int i=1;i<21;i++)
    {
        if(i%2!=0)
        {
        cout<<"player 1 chance\n";
        cin>>ch;
        }
        else
        {
        cout<<"player 2 chance\n";
        cin>>ch;
        }
        k=k+ch;
        if(k==21)
        {
            if(i%2!=0)
            {
                cout<<"\t\t\t\nplayer 2 won";
            }
            else
            {
                cout<<"\t\t\t\nplayer 1 won";
            }
        cout<<"GAME  OVER";
        break;
        }
        a=n-k;

    switch(ch)
    {
    case 1:cout<<"no of sticks remaining = " ;
           cout<<a<<"\n";
        break;
    case 2:cout<<"no of sticks remaining = \n" ;
           cout<<a<<"\n";
        break;
    case 3:cout<<"no of sticks remaining = \n" ;
           cout<<a<<"\n";
        break;
    }
}
}


