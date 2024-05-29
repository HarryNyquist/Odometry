#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void write_to_csv(const vector<double>& x, const vector<double>& y, const vector<double>& z, const string& filename) {
    // Open the CSV file
    ofstream file(filename);
    if (!file.is_open()) {
        cerr << "Failed to open the file." << endl;
        return;
    }

    // Write the header row
    file << "x,y,z" << endl;

    // Write data from vectors
    for (size_t i = 0; i < x.size(); i++) {
        file << x[i] << "," << y[i] << "," << z[i] << endl;
    }

    // Close the file
    file.close();

    cout << "Data written to " << filename << " successfully." << endl;
}

int main() {
    // Example vectors
    vector<double> x = {1.0, 2.0, 3.0, 4.0, 5.0};
    vector<double> y = {6.0, 7.0, 8.0, 9.0, 10.0};
    vector<double> z = {11.0, 12.0, 13.0, 14.0, 15.0};

    // File name
    string filename = "output.csv";

    // Write vectors to CSV file
    write_to_csv(x, y, z, filename);

    return 0;
}
