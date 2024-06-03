#include<vector>
#include<iostream>

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

int main(){
    Matrix mat1 = {
        {1,2,3},
        {4,5,6},
        {7,8,9}
    };

    Matrix mat2 = {
        {4,5,6},
        {7,8,9},
        {10,11,12}
    };

    Matrix addition = matrixAddition(mat1, mat2);
    Matrix multiplication = matrixMultiplication(mat1, mat2);
    Matrix scalar_mul = scalarMatrixMultiplication(mat1, 4);
    showMatrix(addition);
    showMatrix(multiplication);
    showMatrix(scalar_mul);
    cout << "\n";
    Matrix mat3(1,vector<double>(1));
    showMatrix(mat3);
}
