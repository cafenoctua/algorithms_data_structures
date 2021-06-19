#include <iostream>
#include <vector>
using namespace std;

int main() {
    int N, W;
    cin >> N >> W;
    vector<int> a(N);
    for (int i = 0; i < N; ++i) cin >> a[i];

    // bitは2^N通りの部分集合全体を動く
    bool exist = false;
    for (int bit = 0; bit < (1 << N); ++bit) {
        int sum = 0; // 部分集合に含まれているかどうか
        for (int i = 0; i < N; ++i) {
            if (bit & (1 << i)) {
                sum += a[i];
            }
        }
        // sumがWに一致するかどうか
        if (sum == W) exist = true;
    }

    if (exist) cout << "Yes" << endl;
    else cout << "No" << endl;
}