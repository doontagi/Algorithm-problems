#include <string>
#include <vector>
#include <algorithm>
#include "string.h"
#include <iostream>
#include <queue>

using namespace std;
int on_end[360001];
int on_start[360001];

int end_start[360001];
int end_done[360001];
int flat_start(string log) {
    int start = (log[0]-'0')*10*3600+(log[1]-'0')*3600+(log[3]-'0')*10*60+
                (log[4]-'0')*60+(log[6]-'0')*10+(log[7]-'0');
    return start;
}

int flat_end(string log) {
    int end = (log[9]-'0')*10*3600+(log[10]-'0')*3600+(log[12]-'0')*10*60+
              (log[13]-'0')*60+(log[15]-'0')*10+(log[16]-'0');
    return end;
}

string changeToTime(int max_start) {
    string answer = "";
    int hour_10 = max_start/36000;
    max_start = max_start % 36000;
    int hour_1 = max_start/3600;
    max_start = max_start %3600;

    int minute_10 = max_start/600;
    max_start = max_start % 600;
    int minute_1 = max_start/60;
    max_start = max_start %60;

    int second_10 = max_start/10;
    max_start = max_start % 10;
    int second = max_start;

    answer+= to_string(hour_10);
    answer+= to_string(hour_1);
    answer+= ':';
    answer+= to_string(minute_10);
    answer+= to_string(minute_1);
    answer+= ':';
    answer+= to_string(second_10);
    answer+= to_string(second);

    return answer;
}
string solution(string play_time, string adv_time, vector<string> logs) {
    string answer = "";
    int play_time_ = flat_start(play_time);
    int adv_time_ = flat_start(adv_time);
    for(int i=0; i<logs.size(); i++) {

        int start = flat_start(logs[i]);
        int end = flat_end(logs[i]);
        on_end[end]++;
        on_start[start]++;
        end_start[end]++;
        end_done[end+adv_time_];
    }


    int cur_watching = 0;
    int cur_time = 0;
    int max_time = 0;
    int max_start = 0;
    int cur_gone = 0;
    for(int i=0; i<adv_time_; i++) {
        cur_watching+=on_start[i];
        cur_watching-=on_end[i];
        cur_time+=cur_watching;
        if(cur_time > max_time) {
            max_time = cur_time;
            max_start = i;
        }
    }
    int j = 0;
    for(int i=adv_time_; i<=play_time_; i++) {
        cur_time+=cur_watching;
        cur_watching+=on_start[i];
        cur_watching-=on_end[i];
        cur_time-=cur_gone;
        cur_gone+=on_start[j];
        cur_gone-=on_end[j];

        if(cur_time > max_time) {
//            cout << changeToTime(i) << endl;
            max_time = cur_time;
            max_start = i;
        }
        j++;
    }

    max_start = max_start - adv_time_;
    if(max_start <= 0) max_start = 0;

    int hour_10 = max_start/36000;
    max_start = max_start % 36000;
    int hour_1 = max_start/3600;
    max_start = max_start %3600;

    int minute_10 = max_start/600;
    max_start = max_start % 600;
    int minute_1 = max_start/60;
    max_start = max_start %60;

    int second_10 = max_start/10;
    max_start = max_start % 10;
    int second = max_start;

    answer+= to_string(hour_10);
    answer+= to_string(hour_1);
    answer+= ':';
    answer+= to_string(minute_10);
    answer+= to_string(minute_1);
    answer+= ':';
    answer+= to_string(second_10);
    answer+= to_string(second);

    return answer;
}

int main() {
    vector<string> test_log = {"99:59:00-99:59:59", "99:59:58-99:59:59", "99:59:58-99:59:59"};
    string testp = "99:59:59";
    string testa = "00:00:02";
    cout << flat_start("99:59:59") << endl;
    cout << solution(testp, testa, test_log) << endl;
}
