#include<iostream>
#include<vector>
#include <sstream>
#include <fstream>
#include <string>
#include<cmath>

using namespace std;


class KalmanFilter{ //We are not using any matrices as the entire operation is just a 1*1 array, i.e, numbers, so that simplifies things greatly.
    public:
        double X_prev, P_prev;
        double X_pred, P_pred;
        double KalmanGain, R ;
        double Y_k, z_k;
        //double w_k;
        double Q_k;
        double dt;

        KalmanFilter(double X_0, double sampling_time, double acc_error, double sigma) :
        X_prev(X_0), 
        P_prev(sigma * sigma),
        R(acc_error * acc_error),
        dt(sampling_time),
        Q_k(sigma * sigma){
                
                }  
        void prediction(double jerk, double dt){
            X_pred = X_prev + jerk*dt; //ill include w_k later
            P_pred = P_prev + Q_k;
        }

        void update(){
            KalmanGain = P_pred/(P_pred + R);
            X_prev = X_pred + KalmanGain*(Y_k + z_k - X_pred);
            P_prev = (1-KalmanGain)*P_pred;
        }
};


vector<string> split(const string& s, char delimiter) {
    vector<string> tokens;
    string token;
    istringstream tokenStream(s);
    while (getline(tokenStream, token, delimiter)) {
        tokens.push_back(token);
    }
    return tokens;
}

vector<double> Return_Sigma(vector<double> acc_array, vector<double> time_array){
    double sigma = 0;
    for(size_t i = 1; i < acc_array.size(); i++){
        sigma = max(sigma, fabs(acc_array[i] - acc_array[i-1]));
    }
    sigma = sigma * 0.75; // read in a book that it should be between 0.5(del(a)) < sigma < del(a)

    double acc_error = 0;
    for(size_t i = 0; i < time_array.size(); i++){
        if(time_array[i] >= 5){
            break;
        }
        
        acc_error = max(acc_error, fabs(acc_array[i]));
    }
    return {sigma, acc_error};
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

 vector<double> Filtered_Output(vector<double> accn, vector<double> time){
    vector<double> errors = Return_Sigma(accn,time);
    KalmanFilter KF(accn[0], (time[1] - time[0]), errors[1], errors[0]);
    vector<double> Filtered_Accn = {accn[0]};
    for(size_t i = 1; i < accn.size() - 1; i++){
        KF.prediction(((accn[i+1] - accn[i-1])/(time[i+1]-time[i-1])) , time[i] - time[i-1]);
        KF.update();
        Filtered_Accn.push_back(KF.X_prev);
    }
    return Filtered_Accn;    
 }



int main(){
    ifstream file("May_26_09-16.csv");
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
    }
    file.close();
     
    vector<double> filtered_a_x = Filtered_Output(a_x, t);
    vector<double> filtered_a_y = Filtered_Output(a_y, t);
    vector<double> filtered_a_z = Filtered_Output(a_z, t);
    t.pop_back();


    // size_t N = filtered_a_x.size();
    // for(size_t i = 0; i < N; i ++){
    //     filtered_a_x[i] = filtered_a_x[i]*(static_cast<int>(N));
    //     filtered_a_y[i] = filtered_a_y[i]*(static_cast<int>(N));
    //     filtered_a_z[i] = filtered_a_z[i]*(static_cast<int>(N));
    // }

    filtered_a_x.erase(filtered_a_x.begin());
    filtered_a_y.erase(filtered_a_y.begin());
    filtered_a_z.erase(filtered_a_z.begin());
    t.erase(t.begin());

    cout << filtered_a_x.size() << endl;
    cout << a_x.size() << endl;
    cout << t.size() << endl;
    write_to_csv(t, filtered_a_x, filtered_a_y, filtered_a_z, "Filtered_Accn.csv");
}

    // ifstream file2("New_Accn_Data.csv");
    // if (!file2.is_open()) {
    //     cerr << "Failed to open New_Accn_data.csv." << endl;
    //     return 1;
    // }
    // string dummy2;
    // getline(file2, dummy2);
    // vector<double>  a_x, a_y, a_z;
    // string line2;
    // while (getline(file2, line2)) {
    //     vector<string> parts = split(line2, ',');
    //     a_x.push_back(stod(parts[1]));
    //     a_y.push_back(stod(parts[2]));
    //     a_z.push_back(stod(parts[3]));
    // }
    // file2.close();