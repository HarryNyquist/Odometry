#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

vector<string> split(const string& s, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

int nearest_index(const vector<double>& arr, double value) {
    int nearest_idx = -1;
    for (size_t i = 0; i < arr.size(); i++) {
        if (arr[i] > value) {
            break;
        }
        nearest_idx = static_cast<int>(i);
    }
    return nearest_idx;
}

vector<double> linear_interpolation(const vector<double>& signal, const vector<double>& time, double sampling_time) {
    size_t no_of_samples = static_cast<size_t>((*max_element(time.begin(), time.end()) - *min_element(time.begin(), time.end())) / sampling_time);
    vector<double> new_signal(no_of_samples);
    for (size_t n = 1; n < no_of_samples; n++) {
        int idx = nearest_index(time, n * sampling_time);
        new_signal[n] = signal[idx] + (signal[idx + 1] - signal[idx]) * (n * sampling_time - time[idx]) / (time[idx + 1] - time[idx]);
    }
    return new_signal;
}

double SamplingTime(const vector<double>& arr) {
    double T_min = arr[1] - arr[0];
    for (size_t i = 1; i < arr.size(); i++) {
        T_min = min(T_min, arr[i] - arr[i - 1]);
    }
    return T_min / 2.0; 
}

pair<int, vector<double>> trim_time_array(const vector<double>& original_array, const vector<double>& new_array) {
    int idx = nearest_index(new_array, original_array[1]) + 1;
    vector<double> trimmed_array(new_array.begin() + idx, new_array.end());
    return make_pair(idx, trimmed_array);
}

vector<double> uniform_samples(const vector<double>& time, double sampling_time) {
    double min_time = *min_element(time.begin(), time.end());
    double max_time = *max_element(time.begin(), time.end());
    int no_of_samples = static_cast<int>((max_time - min_time) / sampling_time);
    vector<double> new_time(no_of_samples);
    for (int n = 1; n < no_of_samples; n++) {
        new_time[n] = (n + 1) * sampling_time;
    }
    return new_time;
}

void write_to_csv(const vector<double>& t,const vector<double>& x, const vector<double>& y, const vector<double>& z, const string& filename) {
    ofstream file(filename); // filename shld be smtg.csv
    if (!file.is_open()) {
        cerr << "Failed to open the file." << endl;
        return;
    }
    file << "t,x,y,z" << endl;
    for (size_t i = 0; i < x.size(); i++) {
        file << t[i] << "," << x[i] << "," << y[i] << "," << z[i] << endl;
    }
    file.close();

    cout << "Data written to " << filename << " successfully." << endl;
}


int main() {
    ifstream file("May_28_15-30.csv");
    if (!file.is_open()) {
        cerr << "Failed to open the file." << endl;
        return 1;
    }
    string dummy;
    getline(file, dummy);

    vector<double> t, a_x, a_y, a_z, a_mag;

    string line;
    while (getline(file, line)) {
        vector<string> parts = split(line, ',');
        t.push_back(stod(parts[0]));
        a_x.push_back(stod(parts[1]));
        a_y.push_back(stod(parts[2]));
        a_z.push_back(stod(parts[3]));
        a_mag.push_back(stod(parts[4]));
    }
    file.close();
    double sampling_time = SamplingTime(t);

    vector<double> a_x_new = linear_interpolation(a_x, t, sampling_time);
    vector<double> a_y_new = linear_interpolation(a_y, t, sampling_time);
    vector<double> a_z_new = linear_interpolation(a_z,t,sampling_time);
    vector<double> t_new = uniform_samples(t,sampling_time);

    cout << a_x_new.size() << endl;
    cout << a_y_new.size() << endl;
    cout << a_z_new.size() << endl;

    return 0;
}
