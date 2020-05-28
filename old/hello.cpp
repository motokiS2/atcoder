#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; i++)
#define repr(i, a, b) for (int i = a; i < b; i++)

int main() {
    string S;
    cin >> S;
    int ans;
    if(S == "SUN") ans = 7;
    if(S == "MON") ans = 6;
    if(S == "TUE") ans = 5;
    if(S == "WED") ans = 4;
    if(S == "THU") ans = 3;
    if(S == "FRI") ans = 2;
    if(S == "SAT") ans = 1;
    cout << ans << endl;
    return 0;
}