#include<iostream>
#include<vector>
#include <sstream>
#include <fstream>
#include <string>
using namespace std;

typedef vector<vector<double>> Matrix;

void showMatrix(const Matrix& mat){
    for(const auto& row:mat){
        for(double val: row){
            cout << val << " ";
        }
        cout << endl;
    }
}

Matrix matrixAddition(const Matrix& mat1, const Matrix& mat2){
    Matrix result(mat1.size(), vector<double>(mat1[0].size()));
        for(size_t i = 0; i < mat1.size(); i++){
            for(size_t j = 0; j <  mat1[i].size(); j++){
                result[i][j] = mat1[i][j] + mat2[i][j];
            }
        }
    return result;
}

Matrix matrixMultiplication(const Matrix& mat1, const Matrix& mat2){
    Matrix result(mat1.size(), vector<double>(mat2[0].size(),0));
    for(size_t i = 0; i < mat1.size(); i++){
        for(size_t j = 0; j < mat2[0].size();j++){
            for(size_t k = 0; k < mat2.size(); k++){
                result[i][j] += mat1[i][k]*mat2[k][j];
            }
        }
    }
    return result;
}

Matrix scalarMatrixMultiplication(const Matrix&mat, double scalar){
    Matrix result(mat.size(), vector<double>(mat[0].size()));
    for(size_t i = 0; i < mat.size(); i++){
        for(size_t j = 0; j < mat[0].size(); j++){
            result[i][j] = mat[i][j] * scalar;
         }
    }
    return result;
}

class KalmanFilter{ //Do remember that this is NOT a multipurpose class, all matrix dimensions are adjusted for this particular example.
    //We'll consider a model where jerk is constant.
    public:
    Matrix X_prev;
    Matrix P_prev; 
    // Matrix X;
    // Matrix P;
    Matrix X_pred;
    Matrix P_pred;
    Matrix w_k;
    Matrix A;
    Matrix A_transpose;
    //Matrix B;
    //Matrix C;
    Matrix Q;
    Matrix KalmanGain;
    Matrix Y_k;
    Matrix z_k;
    Matrix R;

    Matrix I;

    KalmanFilter(Matrix X_0, Matrix P_0, double sampling_time, double acc_error, double jerk_error) :
        X_prev(2, vector<double>(1)),
        P_prev(2, vector<double>(2)),
        // X(2,vector<double>(1)),
        // P(2, vector<double>(2)),
        X_pred(2,vector<double>(1)),
        P_pred(1,vector<double>(2)),
        w_k(1, vector<double>(1)),
        A(2, vector<double>(2)),
        A_transpose(2,vector<double>(2))
        //B(2, vector<double>(2)),
        //C{ {1, 0}, {0, 1} },
        w_k(2,vector<double>(1)),
        Q(2, vector<double>(2)),
        KalmanGain(2, vector<double>(2)),
        Y_k(2,vector<double>(1)),
        z_k(2,vector<double>(1)),
        R(2, vector<double>(2))
        I{{1, 0},{0 , 1}}
    {
        X_prev = X_0;
        P_prev = P_0;
        A = {
            {1, sampling_time},
            {0, 1}
        };
        // B = {
        //     {0.5 * sampling_time * sampling_time},
        //     {sampling_time}
        // };
        R = {
            {acc_error * acc_error, 0},
            {0, jerk_error * jerk_error}
        };
        A_transpose = {
            {1 , 0},
            {sampling_time, 1}
        };
    }

    void Prediction_Xp(){
            Matrix AX = matrixMultiplication(A,X_prev);
            //Matrix Bu_k = matrixMultiplication(B,u_k);
            //Matrix temp_result = matrixAddition(AX,Bu_k);
            X_pred = matrixAddition(AX, w_k);
    }
    void Prediction_Pp(){
            Matrix AP = matrixMultiplication(A,P_prev);
            Matrix temp_res = matrixMultiplication(AP,A_transpose);
            P_pred = matrixAddition(temp_res, Q);
            P_pred[0][1] = 0;
            P_pred[1][0] = 0;
    }
    void KalmanGaincalcu(){
            KalmanGain[0][1] = 0;
            KalmanGain[1][0] = 0;
            Matrix PR = matrixAddition(P_pred, R);
            KalmanGain[0][0] = P_pred[0][0]/PR[0][0];
            KalmanGain[1][1] = P_pred[0][0]/PR[0][0];
    }
    void X_prev_calcu(){
        Matrix Y = Y_k + z_k;
        Matrix negX_k = scalarMatrixMultiplication(X_prev, -1);
        Matrix temp_res = matrixMultiplication(KalmanGain, matrixAddition(Y,negX_k));
        X_prev = matrixAddition(X_pred,temp_res);
    }
    void P_prev_calcu(){
        Matrix negKG = scalarMatrixMultiplication(KalmanGain, -1);
        P_prev = matrixMultiplication(matrixAddition(I, negKG),P_pred);    
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

vector<double> sym_diff(const vector<double> y, const vector<double> x){
    vector<double> jerk;
    size_t size = y.size();
    for(size_t i = 1; i < size; i++ ){
        double derivative = (y[i] - y[i-1])/(x[i] - x[i-1]);
        jerk.push_back(derivative);
    }
    return jerk;
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

int main(){
    ifstream file("To_send.csv");
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

    // vector<double> jerk_x = sym_diff(a_x, t);
    // vector<double> jerk_y = sym_diff(a_y,t);
    // vector<double> jerk_z = sym_diff(a_z,t);
    // t.erase(t.begin());

    // write_to_csv(t,jerk_x,jerk_y,jerk_z,"Differentiated_output.csv");

    // vector<double> jderiv_x = sym_diff(jerk_x, t);
    // vector<double> jderiv_y = sym_diff(jerk_y,t);
    // vector<double> jderiv_z = sym_diff(jerk_z,t);
    // t.erase(t.begin());

    // write_to_csv(t,jderiv_x,jderiv_y,jderiv_z,"jerk_Differentiation.csv");
    
}
