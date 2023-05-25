class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        // New temperature variable declarations
        double Kelvin = celsius + 273.15;
        double Fahrenheit = celsius * 1.80 + 32.00;

        //Vector declaration
        vector<double> convertedTemperature;
        convertedTemperature.push_back(Kelvin);
        convertedTemperature.push_back(Fahrenheit);
        return convertedTemperature;
    }
};