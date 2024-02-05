#include <iostream>
#include <string>
using namespace std;


int main() {
    int n;
    cin >> n;

    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];
    }


    for(int i=0;i<n;i++){
        int min;
        min = i;
        for(int j=i+1; j<n; j++) {
            if(arr[j] < arr[min]){
                int temp = arr[min];
                arr[min] = arr[j];
                arr[j] = temp;
            }
        }

    }

    for(int i=0; i<n; i++){
        cout << arr[i] << " ";
    }

    
    // 여기에 코드를 작성해주세요.
    return 0;
}