#include <string>
#include <vector>
#include <stack>
#include <iostream>
#include <queue>
#include "string.h"
using namespace std;
int comp_len;
int app_len;
int on_match_num;
int on_done_num;
bool on_match[26];
bool on_done[26];
vector<int> priority[26];
int max_prior[26];
int max_need[26];
bool cur_app[26][26];
queue<int> need[26];
vector<string> solution(vector<string> companies, vector<string> applicants) {
    comp_len = companies.size();
    app_len = applicants.size();
    for(int i=0; i<companies.size(); i++) {
        int here = 0;
        for(int j=0; j<companies[i].size(); j++) {
            if(companies[i][j] >= 'A' && companies[i][j] <= 'Z') {
                here = companies[i][j] -'A';
            }
            else if(companies[i][j] >= 'a' && companies[i][j] <= 'z')
                 {
                    priority[here].push_back(companies[i][j]-'a');
            }
            else {
                max_prior[here] = companies[i][j]-'0';
            }
        }
    }

    for(int i=0; i<applicants.size(); i++) {
        int here = 0;
        for(int j=0; j<applicants[i].size(); j++) {
            if(applicants[i][j] >= 'a' && applicants[i][j] <= 'z') {
                here = applicants[i][j] -'a';
            }
            else if(applicants[i][j] >= 'A' && applicants[i][j] <= 'Z')
            {
                need[here].push(applicants[i][j]-'A');
            }
            else {
                max_need[here] = applicants[i][j]-'0';
            }
        }
    }

    memset(on_match, 0 , sizeof(on_match));
    while(1) {

        on_match_num = 0;
        for(int i=0; i<26; i++) {
            if(!need[i].empty() && !on_match[i] && max_need[i]) {

                cur_app[need[i].front()][i] = true;
                need[i].pop();
                max_need[i]--;
            }
        }
        memset(on_match, 0 , sizeof(on_match));

        for(int i=0; i<26; i++) {
                int amount = max_prior[i];
                if(priority[i].empty()) continue;
                for(int k=0; k<app_len; k++) {
                    if(cur_app[i][priority[i][k]]) {

                        amount--;
                        on_match[priority[i][k]] = true;
                        on_match_num++;
                        if(amount<=0) break;
                    }
                }
        }

        for(int i=0; i<26; i++) {
            for(int j=0; j<26; j++) {
                if(!on_match[i]) cur_app[i][j] = false;
            }
        }
        for(int i=0; i<app_len; i++) {
            if(!max_need[i] && !on_match[i] && !on_done[i]) {
                on_done_num++;
                on_done[i] = true;
            }
        }
        if(on_match_num+on_done_num >= applicants.size()) break;
    }
    vector<string> answer;
    for(int i=0; i<comp_len; i++) {
        string ii = "";
        char a = 'A';
        a+=i;
        ii+=a;
        ii+='_';
        for(int j=0; j<26; j++) {
            for(int i=0; i<26; i++){
                 {
                    char b = 'a';
                    b += i;
                    ii+=b;
                }
            }

        }
        answer.push_back(ii);
    }
    return answer;
}

int main() {

    vector<string> maze = {"A fabdec 2", "B cebdfa 2", "C ecfadb 2"};
    vector<string> appl = {"a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"};
    vector<string> ans = solution(maze,appl);
    for(int i=0; i<ans.size();i++) {
        cout << ans[i] << endl;
    }

}
