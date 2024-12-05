### Manual Test Cases for Expense Calculator App  

Below are test cases written as templates for Xray in Jira, covering the described scenarios. Each test case includes prerequisites, steps, and expected outcomes.

---

#### **Test Case 1: Verify Welcome Message**
**Preconditions:**  
1. User has installed the app on their mobile device.  
2. App is launched for the first time.  

**Steps:**  
1. Launch the app on the device.  
2. Verify that a welcome message appears suggesting purchasing the license.  
3. Tap the "X" icon to close the welcome message.  

**Expected Outcome:**  
1. The welcome message is displayed with a prompt to purchase the app license.  
2. Tapping "X" successfully closes the message and redirects the user to the home screen.  

**Test Variants:**  
- Test on Android (OS versions 10, 11, 12).  
- Test on iPhone (iOS versions 14, 15, 16).

---

#### **Test Case 2: Verify Home Screen Layout**  
**Preconditions:**  
1. User is on the home screen after dismissing the welcome message.  

**Steps:**  
1. Verify that the current month (e.g., December) is displayed at the top.  
2. Check for the "+" and "-" buttons for adding incomes and expenses.  

**Expected Outcome:**  
1. The current month is displayed correctly.  
2. The "+" and "-" buttons are visible on the home screen.

---

#### **Test Case 3: Add an Income**  
**Preconditions:**  
1. User is on the home screen.  

**Steps:**  
1. Tap the "+" button to add an income.  
2. Enter an income value using the calculator.  
3. Add a note describing the income.  
4. Tap the "Category" field and select one of the options: "Deposit," "Salary," or "Savings."  
5. Confirm the income addition.  

**Expected Outcome:**  
1. User is redirected to the home screen after adding the income.  
2. The added income is displayed in green.  
3. The income total is updated correctly in the middle of the home screen.  

---

#### **Test Case 4: Verify Income Categories**  
**Preconditions:**  
1. User is on the income addition screen.  

**Steps:**  
1. Tap the "Category" field while adding an income.  
2. Verify that the following categories are displayed:  
   - Deposit  
   - Salary  
   - Savings  
3. Select a category and verify that the selection is saved.  

**Expected Outcome:**  
1. Categories are displayed correctly.  
2. The selected category is saved and displayed when redirected to the home screen.

---

#### **Test Case 5: Add an Expense**  
**Preconditions:**  
1. User is on the home screen.  

**Steps:**  
1. Tap the "-" button to add an expense.  
2. Enter an expense value using the calculator.  
3. Add a note describing the expense.  
4. Tap the "Category" field and select a category.  
5. Confirm the expense addition.  

**Expected Outcome:**  
1. User is redirected to the home screen after adding the expense.  
2. The added expense is displayed in red.  
3. The expense total is updated correctly in the middle of the home screen.  

---

#### **Test Case 6: Verify Swipe Gesture for Detailed View**  
**Preconditions:**  
1. User has added at least one income and one expense.  

**Steps:**  
1. Swipe up on the home screen.  
2. Verify that a detailed view of all transactions is displayed.  
3. Check that the view includes:  
   - Categories for each transaction.  
   - Dates of the transactions.  
   - Amounts of incomes and expenses.  

**Expected Outcome:**  
1. The swipe gesture displays a detailed view of transactions.  
2. All transactions include the correct categories, dates, and amounts.

---

#### **Test Case 7 Cancel the `Add an Income`**  
**Preconditions:**  
1. User is on the home screen.  

**Steps:**  
1. Tap the "+" button to add an income.  
2. Verify that the "Cancel" button is displayed in the header of the calculator screen.  
3. Tap the "Cancel" button.  
4. Verify that the user is redirected to the home screen without adding any income.  

**Expected Outcome:**  
1. The "Cancel" button is visible on the calculator screen.  
2. Tapping "Cancel" redirects the user to the home screen.  
3. No new income is added, and the total remains unchanged.  

---

#### **Test Case 8 Cancel the `Add an Expense`**  
**Preconditions:**  
1. User is on the home screen.  

**Steps:**  
1. Tap the "-" button to add an expense.  
2. Verify that the "Cancel" button is displayed in the header of the calculator screen.  
3. Tap the "Cancel" button.  
4. Verify that the user is redirected to the home screen without adding any expense.  

**Expected Outcome:**  
1. The "Cancel" button is visible on the calculator screen.  
2. Tapping "Cancel" redirects the user to the home screen.  
3. No new expense is added, and the total remains unchanged.  

--- 

#### **Test Case 10: Validate the Header Buttons on Home Screen**  
**Preconditions:**  
1. User is on the home screen.  

**Steps:**  
1. Verify the presence of the following buttons in the header:  
   - Filter  
   - Search  
   - Add Transfer  
   - Options (three dots).  

**Expected Outcome:**  
1. All buttons are visible and functional in the header.  

---

#### **Test Case 11: Validate the Options Menu Buttons**  
**Preconditions:**  
1. User is on the home screen.  

**Steps:**  
1. Tap the "Options" button (three dots) in the header.  
2. Verify that the following buttons appear on the right margin of the screen:  
   - Categories  
   - Accounts  
   - Currencies  
   - Settings.  

**Expected Outcome:**  
1. The "Options" menu displays all listed buttons correctly.  

---

#### **Test Case 12: Dismiss Options Menu by Tapping Outside**  
**Preconditions:**  
1. User is on the home screen.  
2. Options menu is open.  

**Steps:**  
1. Tap anywhere outside the options menu.  
2. Verify that the options menu closes, and the user remains on the home screen.  

**Expected Outcome:**  
1. Options menu closes.  
2. The user is redirected back to the home screen.  

---

#### **Test Case 13: Validate Default Language Setting**  
**Preconditions:**  
1. User has freshly installed the app and is accessing it for the first time.  

**Steps:**  
1. Navigate to the settings menu via "Options > Settings".  
2. Locate the language settings.  
3. Verify the default language is the same as the phone's OS language.  

**Expected Outcome:**  
1. The default language matches the phone's OS language.  

---

#### **Test Case 14: Change App Language**  
**Preconditions:**  
1. User is on the language settings page in the app.  

**Steps:**  
1. Change the language to Italian.  
2. Observe the app interface and its categories (e.g., "Savings", "Deposits").  
3. Verify the changes suggested by the app (e.g., restart prompt).  
4. Restart the app.  
5. Reverify if the language changes have taken effect.  

**Expected Outcome:**  
1. App categories remain in English (BUG).  
2. Only push notifications are updated to Italian.  
3. The restart suggestion does not resolve the issue (BAD USER EXPERIENCE).  

---
