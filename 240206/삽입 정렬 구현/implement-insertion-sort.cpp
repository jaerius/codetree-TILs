#include <iostream>
using namespace std;

#define MAX_N 100

int arr[MAX_N];
int num;

void insertSort(){
    for(int i=1; i<num; i++){
        int j = i -1;
        int key = arr[i];
        while(j >=0 && arr[j]>key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
    
}

int main() {
    

    cin >> num;
    
    for(int i=0; i<num; i++){
        cin >> arr[i];
        
    }

    insertSort();

    for(int i=0; i<num; i++){
        cout << arr[i] << " ";
    }

    // 여기에 코드를 작성해주세요.
    return 0;
}