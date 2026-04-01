#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
using namespace std;

map<short int, vector<short int>> connections = {{1, {-1}}};
vector<short int> all_depts;
vector<vector<short int>> network;
short int depts, lines;

void line(short int pos, vector<short int> c_line) {

    bool found_all = true;
    for (short int dept : all_depts) {
        if (find(c_line.begin(), c_line.end(), dept) == c_line.end()) {
            found_all = false;
            break;
        }
    }
    if (found_all) return;

    if (pos == depts) {
        vector<short int> new_line = c_line;
        new_line.push_back(depts);
        network.push_back(new_line);
        return;
    }

    // Explore the connections from the current position
    for (short int wire : connections[pos]) {
        if (find(c_line.begin(), c_line.end(), wire) != c_line.end())
            continue;
        vector<short int> new_line = c_line;
        new_line.push_back(wire);
        
        if (wire == depts) {
            network.push_back(new_line);
            continue;
        }

        line(wire, new_line);
    }
}

int main() {
    cin >> depts >> lines;

    for (short int i = 1; i <= depts; ++i) {
        if (i != 1 && i != depts)
            all_depts.push_back(i);
    }

    for (short int i = 0; i < lines; ++i) {
        short int a, b;
        cin >> a >> b;

        if (connections.find(a) == connections.end())
            connections[a] = {};
        connections[a].push_back(b);

        if (connections.find(b) == connections.end())
            connections[b] = {};
        connections[b].push_back(a);
    }

    short int start = 1;
    for (short int wire : connections[start]) {
        vector<short int> initial_line = {start, wire};
        line(wire, initial_line);
    }

    if (network.empty()) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        vector<short int> mini = *min_element(network.begin(), network.end(), 
            [](const vector<short int>& a, const vector<short int>& b) {
                return a.size() < b.size();
            });
        
        for (short int i = 0; i < mini.size(); ++i) {
            if (i > 0) cout << " ";
            cout << mini[i];
        }
        cout << endl;
    }

    return 0;
}
