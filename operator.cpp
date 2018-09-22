#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <cmath>

using namespace std;


class BigNum {
	friend ostream &operator<<(ostream &os, BigNum &num);
public:
	BigNum(string str):sign(0){
		num.clear();
		if (str[0] == '-') {
			sign = 1;
			str.erase(str.begin());
		}
		for (int i = 0; i < str.size(); i++)
			num.insert(num.begin(),str[i] - '0');
	}
	BigNum(BigNum &B){
		num.clear();
		sign = B.sign;
		for (int i = 0; i < B.num.size(); i++)
			num.push_back(B.num[i]);
	}
	BigNum(int n) {
		num.clear();
		if (n == 0) {
			sign = 0; 
			num.push_back(0);
		}
		else {
			sign = n < 0;
			n = (n < 0) ? -n : n;
			while (n > 0) {
				num.push_back(n % 10);
				n = n / 10;
			}
		}
	}

	BigNum &operator =(BigNum B) {
		num.clear();
		sign = B.sign;
		for (int i = 0; i < B.num.size(); i++)
			num.push_back(B.num[i]);
	}

	bool operator ==(BigNum B) {
		if (num.size() == B.num.size() && ((sign == B.sign)|| (B.num.size()==1 && B.num[0] == 0 ))){
			for (int i = 0; i < num.size(); i++)
				if (num[i] != B.num[i]) return 0;
			return 1;
		}
		else return 0;
	}

	bool operator !=(BigNum B) {
		return !operator ==(B);
	}

	bool operator ==(int n) {
		BigNum T(n);
		return  operator == (T);
	}

	bool operator !=(int n) {
		BigNum T(n);
		return  !operator == (T);
	}

	BigNum &operator +(BigNum B){
		if (!(sign^B.sign)){
			for (int i = 0; i < num.size(); i++) {
				if (i < B.num.size()) B.num[i] += num[i];
				else B.num.push_back(num[i]);
			}
			B.flush();
		}
		else {
			int length = (num.size() > B.num.size()) ? num.size() : B.num.size();
			for (int i = 0; i < length; i++) {
				if (i < B.num.size()) {
					if (i < num.size())
						B.num[i] = num[i] - B.num[i];
					else
						B.num[i] = -B.num[i];
				}
				else B.num.push_back(num[i]);
			}
			bool temp = (B.num.back() < 0)?B.sign:sign;
			B.flush();
			B.sign = temp;
		}
		return *(new BigNum(B));
	}

	BigNum &operator +(int n) {
		BigNum T(n);
		return operator +(T);
	}

	BigNum &operator ++(int none) {
		BigNum T(1);
		*this = operator +(T);
		return *this;
	}
	BigNum &operator ++() {
		BigNum T(1);
		*this = operator +(T);
		return *this;
	}

	BigNum &operator --(int none) {
		BigNum T(-1);
		*this = operator +(T);
		return *this;
	}
	BigNum &operator --() {
		BigNum T(-1);
		*this = operator +(T);
		return *this;
	}

	BigNum &operator +=(int n) {
		BigNum T(n);
		return operator +=(T);
	}

	BigNum &operator +=(BigNum &B) {
		*this = operator +(B);
		return *this;
	}

	BigNum &operator -=(int n) {
		BigNum T(n);
		return  operator -=(T);
	}

	BigNum &operator -=(BigNum &B) {
		*this = operator +(-B);
		return *this;
	}

	BigNum &operator -(BigNum B) {
		B.sign = !B.sign;
		return operator +(B);
	}

	BigNum &operator -(int n) {
		BigNum T(-n);
		return operator +(T);
	}

	BigNum &operator -() {
		BigNum *B = new BigNum(*this);
		B->sign = !this->sign;
		return *B;
	}

	BigNum &operator +() {
		BigNum *B = new BigNum(*this);
		return *B;
	}

	BigNum &operator *(BigNum B) {
		BigNum *temp = new BigNum(0);
		for (int i = 0; i < B.num.size(); i++) {
			for (int j = 0; j < num.size(); j++) {
				int result = num[j] * B.num[i];
				if (i + j >= temp->num.size()) temp->num.push_back(result);
				else temp->num[i+j] += result;
				temp->flush();
			}
		}
		temp->sign = (sign^B.sign);
		return *temp;
	}

	BigNum &operator *(int n) {
		BigNum T(n);
		return operator *(T);
	}

	BigNum &operator *=(BigNum B) {
		*this = operator *(B);
		return *this;
	}

	BigNum &operator *=(int n) {
		BigNum T(n);
		return operator *=(T);
	}

	BigNum &operator /(BigNum B) {
		BigNum *ans = new BigNum(0);
		BigNum temp(0);
		for (int i = 0; i < num.size();i++) {

			temp = temp * 10 + num[num.size() - 1 - i];
			if (!(temp - B).sign) {
				BigNum q_temp(0);
				while (!(temp - B).sign){
					temp -= B;
					q_temp++;
				}
				*ans = (*ans)*10 + q_temp;
			}
		}
		ans->sign = sign ^ B.sign;
		return *ans;
	}

	BigNum &operator /(int n) {
		BigNum T(n);
		return operator /(T);
	}

	BigNum &operator /=(BigNum B) {
		*this = operator /(B);
		return *this;
	}

	BigNum &operator /=(int n) {
		BigNum T(n);
		return operator /=(T);
	}

private:
	vector<int> num;
	bool sign;
	void flush() {
		if (num[num.size()-1] < 0) {
			sign = !sign;
			for (int i = 0; i < num.size(); i++)
				num[i] = num[i] * (-1);
			flush();
		}
		else {
			int temp = 0;
			for (int i = 0; i < num.size(); i++) {
				num[i] += temp;
				temp = 0;
				if (num[i]<0) {
					temp = num[i] / 10 -1;
					num[i] = 10 - (-num[i]) % 10;
				}
				else if (num[i] > 9) {
					temp = num[i] / 10;
					num[i] = num[i] % 10;
				}
			}
			if (temp != 0) {
				num.push_back(temp);
				flush();
			}
		}
		int k=1;
		while (num[num.size() - k] == 0 && num.size()>1)
			num.pop_back(),k++;
		if (*this == 0) sign = 0;
	}

};

ostream &operator<<(ostream &os, BigNum &num) {
	if (num.sign) cout << "-";
	for (int i = num.num.size()-1; i >=0 ; i--)
		cout << num.num[i];
	return os;
}

int main() {
	BigNum num(90);
	BigNum n(7);
	cout << num/n  << endl;
	
	//cout << num << endl;
	system("pause");
}