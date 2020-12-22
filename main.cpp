#include <iostream>
using namespace std;

    int choice;
    int k;
    char c;
    char a[3][3]={{'1','2','3'},{'4','5','6'},{'7','8','9'}};
main()
    {
    cout<<"                             TIC TAC TOE"<<endl;
    cout<<"   PLAYER[X]"<<endl;
    cout<<"   PLAYER[0]"<<endl;
    cout<<"  "<<a[0][0]<<"   |   "<<a[0][1]<<"  |   "<<a[0][2]<<"     "<<endl;
    cout<<"_____ |_____ |_____"<<endl;
    cout<<"  "<<a[1][0]<<"   |   "<<a[1][1]<<"  |   "<<a[1][2]<<"     "<<endl;
    cout<<"_____ |_____ |_____"<<endl;
    cout<<"  "<<a[2][0]<<"   |   "<<a[2][1]<<"  |   "<<a[2][2]<<"     "<<endl;
    cout<<"      |      |     "<<endl;
    for(int i=1;i<=9;i++)
    {
        for(int j=0;j<3;j++)
        {
            if((a[j][0])==(a[j][1])&&((a[j][1])==(a[j][2])))
            {
                k=k+1;
                break;
            }
               if((a[0][j])==(a[1][j])&&((a[1][j])==(a[2][j])))
               {
                   k=k+1;
                   break;
               }
                if((a[0][0])==(a[1][1])&&(a[1][1])==(a[2][2]))
                {
                    k=k+1;
                    break;
                }
                if((a[0][2])==(a[1][1])&&(a[1][1])==(a[2][0]))
               {
                k=k+1;
                break;
               }
        }
        if(k==1)
        {
            cout<<"game is over"<<endl;
            cout <<"any of the one player has won";
            break;
        }
        if(i%2!=0)
        {
            cout<<"player[X] chance";
            c='X';
        }
        else
        {
            cout<<"player[0] chance";
            c='0';
        }

    cin>>choice;
    switch(choice)
    {
        case 1: a[0][0]=c;
        break;
        case 2: a[0][1]=c;
        break;
        case 3: a[0][2]=c;
        break;
        case 4: a[1][0]=c;
        break;
        case 5: a[1][1]=c;
        break;
        case 6: a[1][2]=c;
        break;
        case 7: a[2][0]=c;
        break;
        case 8: a[2][1]=c;
        break;
        case 9: a[2][2]=c;
        break;
    }
    cout<<"  "<<a[0][0]<<"   |   "<<a[0][1]<<"  |   "<<a[0][2]<<"     "<<endl;
    cout<<"_____ |_____ |_____"<<endl;
    cout<<"  "<<a[1][0]<<"   |   "<<a[1][1]<<"  |   "<<a[1][2]<<"     "<<endl;
    cout<<"_____ |_____ |_____"<<endl;
    cout<<"  "<<a[2][0]<<"   |   "<<a[2][1]<<"  |   "<<a[2][2]<<"     "<<endl;
    cout<<"      |      |     "<<endl;
    }
    }



