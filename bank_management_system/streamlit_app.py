import streamlit as st
from app import BankSystem

st.set_page_config(page_title="Modern Bank")

if 'bank' not in st.session_state:
    st.session_state.bank = BankSystem()

bank = st.session_state.bank

st.title("Modern Banking System")

menu = ["Home", "Open Account", "Deposit", "Withdraw", "Check Balance"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Home":
    st.subheader("Welcome to your digital bank")
    st.write("Select an option from the sidebar to begin.")

elif choice == "Open Account":
    st.subheader("Create New Account")
    name = st.text_input("Full Name")
    pin = st.text_input("Set 4-digit PIN", type="password")
    deposit = st.number_input("Initial Deposit ($)", min_value=0.0)
    
    if st.button("Create Account"):
        if name in bank.accounts:
            st.error("Account already exists!")
        else:
            bank.accounts[name] = {"pin": pin, "balance": deposit}
            bank.save_data()
            st.success(f"Account created for {name}!")

elif choice == "Deposit":
    st.subheader("Deposit Money")
    name = st.text_input("Full Name")
    amount = st.number_input("Amount to deposit ($)", min_value=0.0)
    
    if st.button("Confirm Deposit"):
        if name in bank.accounts:
            bank.accounts[name]["balance"] += amount
            bank.save_data()
            st.success(f"Deposited ${amount}. New balance: ${bank.accounts[name]['balance']}")
        else:
            st.error("Account not found.")

elif choice == "Withdraw":
    st.subheader("Withdraw Money")
    name = st.text_input("Full Name")
    pin = st.text_input("Enter PIN", type="password")
    amount = st.number_input("Amount to withdraw ($)", min_value=0.0)
    
    if st.button("Confirm Withdrawal"):
        if name in bank.accounts:
            if bank.accounts[name]["pin"] == pin:
                if amount <= bank.accounts[name]["balance"]:
                    bank.accounts[name]["balance"] -= amount
                    bank.save_data()
                    st.success(f"Withdrawn ${amount}. New balance: ${bank.accounts[name]['balance']}")
                else:
                    st.error("Insufficient funds.")
            else:
                st.error("Invalid PIN.")
        else:
            st.error("Account not found.")

elif choice == "Check Balance":
    st.subheader("Check Your Balance")
    name = st.text_input("Full Name")
    pin = st.text_input("Enter PIN", type="password")
    
    if st.button("Show Balance"):
        if name in bank.accounts and bank.accounts[name]["pin"] == pin:
            st.info(f"Account: {name} | Balance: ${bank.accounts[name]['balance']}")
        else:
            st.error("Invalid credentials.")