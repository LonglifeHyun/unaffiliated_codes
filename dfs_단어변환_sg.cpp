#include <string>
#include <vector>
#include <iostream>

using namespace std;

int Answer=1000;
vector< vector<int> > differences;

int check_different(string current_word, string target_word) {
    int cnt=0;
    for(int i=0;i<current_word.size();++i) {
        if(current_word[i] != target_word[i]) {
            cnt+=1;
        }
    }
    return cnt;
}
void cal_differences(const vector<string>& words, vector< vector<int> >& differences) {
    int len = words.size();
    
    for(int i=0;i<len;++i) {
        for(int j=i+1;j<len;++j) {
            if(i==j) {
                differences[i][j]=0;
                continue;
            }
            int diff = check_different(words[i],words[j]);
            differences[i][j] = diff;
            differences[j][i] = diff;
        }
    }
}
int find_target_index(string target, const vector<string>& words) {
    for(int i=0;i<words.size();++i) {
        if(target==words[i])
            return i;
    }
    return -1;
}

bool check_all_visit(const vector<bool>& check_visit) {
    for(int i=0;i<check_visit.size();++i) {
        if(check_visit[i]==false)
            return false;
    }
    return true;
}
void DFS(int current_idx, int target_idx, const vector<string>& words, vector<bool>& check_visit, int cnt) {
    if(current_idx == target_idx) {     // 타겟 찾았으면
        if(cnt < Answer) {
            Answer = cnt;
        }
        return;        
    }
    
    for(int i=0;i<words.size();++i) {   // 단어중에서
        if(differences[current_idx][i]==1) {   // 한개 차이나는애들 중에서
            if(check_visit[i]!=true) { // 안바꿨던 애들로 바꿈.
                check_visit[i]=true;
                DFS(i, target_idx, words, check_visit, cnt+1);   
                check_visit[i]=false;
            }
        }
    }
}

int solution(string begin, string target, vector<string> words) {
    int target_idx = find_target_index(target, words);
    if(target_idx==-1) {
        return 0;        
    }
    vector<bool> check_visit(words.size(),false);
    differences.resize(words.size(), vector<int>(words.size(), 0));
    cal_differences(words,differences);
    
    for(int i=0;i<words.size();++i) {
        int diff = check_different(begin, words[i]);
        if(diff!=1) continue;
        
        check_visit.clear();
        check_visit.resize(words.size(),false);
        check_visit[i]=true;
        DFS(i, target_idx, words, check_visit, 1);
    }
    
    return Answer;
}
