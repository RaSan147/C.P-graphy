/*
1			0 +> 1
1 1			1 => 1
1 2 1		1 +> 2	1 ++ 2 OK
1 2 2 1		2 => 2
2- 3 2 1	2 +> 3	1 ++ 2 ++ 3 OK ODD -- 2 -- 1
3- 3 2 1	3 => 3	1 ++ 2 ++ 3 OK EVE
*/
// #include <bits/stdc++.h>

// using namespace std;

// int main()
// {
//     int n;
//     cin >> n;

//     for (int i = 1; i <= n; i++)
//     {
//         for (int j = 1; j <= i / 2; j++)
//         {
//             cout << j << ' ';
//         }
//         if (i % 2 == 0)
//         {
//             for (int j = i / 2; j > 0; j--)
//             {
//                 cout << j << ' ';
//             }
//         }
//         else
//         {
//             for (int j = i / 2 + 1; j > 0; j--)
//             {
//                 cout << j << ' ';
//             }
//         }
//         cout << endl;
//     }

//     return 0;
// }

#include <iostream>

using namespace std;

int main()
{
    int rows = 69;

    for (int n=1; n <= rows; n++){
        for (int i=1; i<=n/2; i++){
            cout << i << ' ';
        }

        int s = n&1 ? n/2 + 1 : n/2;

        while (--s){
            cout << s << ' ';
        }

        cout << endl;
    }

}
