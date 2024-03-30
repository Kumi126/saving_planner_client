import streamlit as st
from app.schema import SimulateCondition


    
accounts:list[dict[int,str]] = [{}]

with st.form(key='account_assign'):
    simulate_name = st.text_input(key='simulate_name', label=f'Name this simulation', max_chars=20)
    accounts_number = st.number_input('How many accounts will contribute to this plan?',min_value=1,step=1,max_value=8)
    saving_month = st.number_input('How long will you save (months)?',min_value=1,step=1)
    submit_button = st.form_submit_button(label='account_no_submit')
if submit_button:
    simulate_condition = SimulateCondition(simulate_name, int(saving_month))
    tr = True

def assign_account_conditions():
    with st.form(key='account_detail_assign'):
        
        count = 1
        if len(accounts) == 1 and accounts[0] == None:
            st.write(accounts)
        while count <= accounts_number:
            account_key = str(f'account{count}')
            accounts.append({count:st.text_input(key=account_key, label=f'account name{count}')})
            count += 1
        submit_button = st.form_submit_button(label='submit to make a request')

tr = False
if tr: st.write(simulate_condition.name)