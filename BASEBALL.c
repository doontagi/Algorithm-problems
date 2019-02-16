#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct {
	char *name;
	int win;
	int draw;
	int loss;
}Team;
char *strdupp(const char *str)
{
	int n = strlen(str) + 1;
	char *dup = malloc(n);
	if (dup)
	{
		strcpy(dup, str);
	}
	return dup;
}
int  readline(FILE *fp, char *str, int  limit) {
	int ch = 0;
	int i = 0;
	while ((ch = fgetc(fp)) != '\n'&&ch != EOF) {
		if (i < limit)
			str[i++] = ch;
	}
	str[i] = '\0';
	return i;
}
double cal_win(Team *baseball) {
	double sum = 0;
	sum += baseball->draw;
	sum += baseball->win;
	sum += baseball->loss;
	double rate = (baseball->win) / sum;
	return rate;
}
Team *add_Team(char *name) {
	char *a = strdupp(name);
	Team *ptr= (Team *)malloc(sizeof(Team));
	ptr->name=a;
	ptr->draw = 0;
	ptr->loss = 0;
	ptr->win = 0;
	return ptr;
}
int find_Team(Team *sTeam[],char *name) {
	for (int i = 0; i < 8; i++) {
		if (strcmp(sTeam[i]->name,name)==0)
			return i;
		
	}
	return 30;
}

int main() {
	char input[100];
	readline(stdin, input, 100);
	int iinput = atoi(input);
	while (iinput != 0) {
		Team *Teams[8];
		for (int i = 0; i < 8; i++) {
			char record[500];
			readline(stdin, record, 600);
			char *t_name = strtok(record, " ");
			Teams[i]=add_Team(t_name);
			Teams[i]->win = atoi(strtok(NULL, " "));
			Teams[i]->draw = atoi(strtok(NULL, " "));
			Teams[i]->loss = atoi(strtok(NULL, " "));
		}
		char myTeam[303];
		readline(stdin, myTeam, 100);
		char leftmatch[1000];
		readline(stdin, leftmatch, 100);
		int int_leftmatch = atoi(leftmatch);
		char *leftmatchs[25];
		for(int i=0;i<int_leftmatch;i++) {
			leftmatchs[i]= (char  *)malloc(sizeof(char  *));
			readline(stdin,leftmatchs[i],200);
		}
	
		for (int i = 0; i < int_leftmatch; i++) {
			char *tmp1;
			char *tmp2;
			tmp1 = strtok(leftmatchs[i], " ");
			tmp2 = strtok(NULL, " ");
			if (tmp1 == myTeam || tmp2 == myTeam) {
				Teams[find_Team(Teams, myTeam)]->win += 1;
				leftmatchs[i] = NULL;
			}
			else {
				int a = find_Team(Teams, tmp1);
				int b = find_Team(Teams, tmp2);
				Teams[a]->draw = Teams[a]->draw + 1;
				Teams[b]->draw = Teams[b]->draw + 1;
			}
		}
		double Teamrate[8];
		for (int i = 0; i < 8; i++) {
			Teamrate[i]=cal_win(Teams[i]);
		}
		double myTeam_rate = Teamrate[find_Team(Teams, myTeam)];
		double temp = 0;
		for (int i = 0; i < 8; i++)
		{
			for (int j = 0; j < 8 - i; j++)
			{
				if (Teamrate[j] < Teamrate[j + 1])
				{
					temp = Teamrate[j];
					Teamrate[j] = Teamrate[j + 1];
					Teamrate[j + 1] = temp;
				}
			}
		}
		for (int i = 0; i < 8; i++) {
			if (Teamrate[i] == myTeam_rate) {
				if (i < 5) {
					printf("YES\n");
				}
				else
					printf("NO");
			}
		}
		iinput -= 1;
	}
}
