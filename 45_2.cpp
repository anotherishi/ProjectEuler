#include <iostream>

using namespace std;

int main()
{
	int next_tri = 40755;
	int ind_tri = 285;
	int next_pen = 40755;
	int ind_pen = 165;
	int next_hex = 40755;
	int ind_hex = 143;
	while(1)
 	{
  		next_tri += ++ind_tri;
  		if (next_tri > next_pen) next_pen += (ind_pen++*3)+1;
  		if (next_tri > next_hex) next_hex += (ind_hex++ *4)+1;

  		if(next_tri == next_pen && next_tri == next_hex)
  		{
  			cout<<"solution: "<<next_tri<<endl;
  			return 0;
      	}
    }
}