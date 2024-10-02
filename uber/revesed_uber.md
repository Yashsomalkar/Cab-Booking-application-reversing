


# Uber OTP Request Analysis

## Overview
This document outlines the reverse engineering of OTP (One-Time Password) request and response flows for Uber's authentication system. The HTTP requests simulate actions like mobile number input and OTP verification.

---

## 1. **OTP Request - Submit Form**

**Request Method:** `POST`  
**Endpoint:** `/rt/silk-screen/submit-form`  
**Protocol:** HTTP/2

### **Headers**
- `Host`: `cn-geo1.uber.com`
- `Accept`: `*/*`
- `X-Uber-Usl-Id`: `00d805ab-08e4-453a-b711-34c4104a4828`
- `X-Uber-Client-Id`: `com.ubercab`
- `User-Agent`: `Mozilla/5.0 (Linux; Android 9; SM-G977N)`
- `X-Uber-App-Device-Id`: `78b10f18-819e-4c46-82bd-fee557642c51`
- `X-Uber-Request-Uuid`: `d72b7cd5-f753-4d97-b118-da83e9b368b1`
- `Origin`: `https://auth.uber.com`
- `Content-Type`: `application/json`
- `Content-Length`: `2064`

### **Payload**
```json
{
  "formContainerAnswer": {
    "formAnswer": {
      "codeChallenge": "VZ7VgKLnWCQrZ3YT0bI2rGg1a-IdZhs46Sj4yJ_QMqs",
      "deviceData": {
        "androidId": "90344cc1522d9a99",
        "deviceModel": "SM-G977N",
        "deviceOsName": "android",
        "deviceOsVersion": "9",
        "googleAdvertisingId": "40467698-273f-48ba-92ba-ab894c355c95",
        "wifiConnected": false
      },
      "productConstraints": {
        "autoSMSVerificationSupported": true
      },
      "screenAnswers": [
        {
          "eventType": "TypeSMSOTP",
          "screenType": "PHONE_OTP",
          "fieldAnswers": [
            {
              "fieldType": "PHONE_SMS_OTP",
              "phoneSMSOTP": "2563"
            }
          ]
        }
      ]
    }
  }
}
```

---

## 2. **First Request - Mobile Number Submission**

**Request Method:** `POST`  
**Endpoint:** `/rt/silk-screen/submit-form`  
**Protocol:** HTTP/1.1

### **Headers**
- `Host`: `cn-geo1.uber.com`
- `X-Uber-Request-Uuid`: `db8ee4b0-288e-4482-821e-1f47c63f7160`
- `Content-Type`: `application/json`
- `Content-Length`: `2108`

### **Payload**
```json
{
  "formContainerAnswer": {
    "formAnswer": {
      "codeChallenge": "VZ7VgKLnWCQrZ3YT0bI2rGg1a-IdZhs46Sj4yJ_QMqs",
      "deviceData": {
        "androidId": "90344cc1522d9a99",
        "deviceModel": "SM-G977N",
        "deviceOsVersion": "9"
      },
      "screenAnswers": [
        {
          "eventType": "TypeInputMobile",
          "screenType": "PHONE_NUMBER_INITIAL",
          "fieldAnswers": [
            {
              "fieldType": "PHONE_COUNTRY_CODE",
              "phoneCountryCode": "91"
            },
            {
              "fieldType": "PHONE_NUMBER",
              "phoneNumber": "REDACTED"
            }
          ]
        }
      ]
    }
  }
}
```

---

## 3. **Second Request - OTP Validation Response**

**Response Method:** `HTTP/2 200 OK`

### **Headers**
- `Date`: `Thu, 18 Apr 2024`
- `Content-Type`: `application/json`
- `X-Request-Id`: `c5e3aa20-9fe5-4d42-939b-ee7f0e0fa130`
- `Access-Control-Allow-Origin`: `https://auth.uber.com`

### **Response Payload**
```json
{
  "form": {
    "flowType": "SIGN_IN",
    "screens": [
      {
        "screenType": "RESET_ACCOUNT",
        "fields": [
          {
            "fieldType": "RESET_ACCOUNT"
          }
        ],
        "eventType": "TypeResetAccount"
      }
    ]
  },
  "inAuthSessionID": "d31e8e18-8dc4-498d-881c-2890e566169c"
}
```

---

## 4. **Key Insights**
- **Device Fingerprinting**: Uber captures extensive device metadata like `androidId`, `deviceModel`, `osVersion`, and `googleAdvertisingId`.
- **Security Mechanisms**: The requests include challenges such as `codeChallenge` and session IDs like `inAuthSessionID` to ensure the flow’s integrity.
- **OTP Submission**: Uber's form captures the OTP (`phoneSMSOTP`), with potential for auto-verification through `autoSMSVerificationSupported`.
- **Account Flow**: The flowType switches from `INITIAL` to `SIGN_IN`, indicating successful progression of the login/OTP flow.

---

## 5. **Conclusion**
Understanding Uber’s OTP verification API reveals the complexity of their authentication system, focusing on device data validation and secure session management to prevent abuse or bypassing.

