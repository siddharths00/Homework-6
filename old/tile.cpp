#include <bits/stdc++.h>
using namespace std;

bool solve(vector<vector<int> >floor, vector<pair<pair<int, int>, pair<int, int> > > &tiles, int total, int r, int c, int n) {
    if(r>n and c>n)return false;
    if(c>n){
        c=1;
        r+=1;
    }
    bool one=false, two=false;
    if(total==0) {
        // cout<<"TRUE\n";
        return true;
    }
    for(int i=r; i<=n; i++) {
        for(int j=c; j<=n; j++) {
            if(floor[i][j]==1 and floor[i][j+1]==1) {
                floor[i][j]=0;
                floor[i][j+1]=0;
                // cout<<"Checking for\n";
                // for(int k=1; k<=n; k++) {
                //     for(int l=1; l<=n; l++) {
                //         cout<<floor[k][l];
                //     }
                //     cout<<"\n";
                // }
                // cout<<"\n";
                one=solve(floor, tiles, total-2, i, j+2, n);
                // cout<<one<<"<=\n";
                floor[i][j]=1;
                floor[i][j+1]=1;
                if(one) {
                    tiles.push_back(make_pair(make_pair(i, j), make_pair(i, j+1)));
                    return true;
                }
            }
            if(floor[i][j]==1 and floor[i+1][j]==1) {
                floor[i][j]=0;
                floor[i+1][j]=0;
                // cout<<"Checking for\n";
                // for(int k=1; k<=n; k++) {
                //     for(int l=1; l<=n; l++) {
                //         cout<<floor[k][l];
                //     }
                //     cout<<"\n";
                // }
                // cout<<"\n";
                two=solve(floor, tiles, total-2, i, j+1, n);
                // cout<<two<<"<=\n";
                floor[i][j]=1;
                floor[i+1][j]=1;
                if(two) {
                    tiles.push_back(make_pair(make_pair(i, j), make_pair(i+1, j)));
                    return true;
                }
            }
        }
    }
    return false;
}

int main(){
#ifndef GRADESCOPE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int n;
    string input;
    cin >> input;

    n = stoi(input);
    int total=0;
    vector<vector<int> >floor(n+2, vector<int>(n+2,0));
    for(int i=1; i<=n; i++) {
       cin >> input;
       for(int j=1; j<=n; j++) {       
		    floor[i][j]=input[j-1]-'0';	
            total+=floor[i][j];
	    }
    }
    if(total%2) {
        cout<<0;
        return 0;
    }
    // cout<<total<<"=====\n";
    vector<pair<pair<int, int>, pair<int, int> > >tiles;
    if(solve(floor, tiles, total, 1, 1, n)) {
        cout<<"1\n";
        for(auto p:tiles) {
            cout<<"("<<p.first.first<<","<<p.first.second<<")";
            cout<<"("<<p.second.first<<","<<p.second.second<<")\n";
        }
    }
    else
    cout<<0;
    return 0;
}
