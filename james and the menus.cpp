#include <bits/stdc++.h>

using namespace std;
typedef long long ll;

const int N = 1e3 + 14;
int n, m, a[N][N], mx[N];

int main() {
    // Input the number of rows (n) and columns (m)
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> n >> m;

    // Input the elements of the 2D array 'a' and compute the maximum value in each column
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
            mx[j] = max(mx[j], a[i][j]);
        }

    // Create a vector of tuples to store information about each row
    vector<tuple<int, ll, int>> v;

    // Process each row to calculate the number of elements equal to the maximum value in their columns,
    // the sum of elements in the row, and the row index
    for (int i = 0; i < n; ++i) {
        int s = 0;
        for (int j = 0; j < m; ++j)
            s += a[i][j] == mx[j];
        v.emplace_back(s, accumulate(a[i], a[i] + m, 0ll), i);
    }

    // Find the tuple with the maximum value of the first element ('s') and print the corresponding row index
    cout << std::get<2>(*max_element(v.begin(), v.end())) + 1 << '\n';
}
