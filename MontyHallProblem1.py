import streamlit as st
import numpy as np
import random 
import matplotlib.pyplot as plt


st.set_page_config(page_title="Monty Hall", layout="wide")

#functions
def reset():
    for k in ["steps", "car", "pick", "reveal", "final", "switch", "stay", "tries", "win","switchwin","staywin","win_switch_hist","win_stay_hist","tries_hist","win_hist"]:
        st.session_state.pop(k,None)

    st.session_state.step = 1

def retry():
    st.session_state.tries += 1
    st.session_state.tries_hist.append(st.session_state.tries)

    if (st.session_state.final == st.session_state.car):
        st.session_state.win += 1    
    st.session_state.win_hist.append(st.session_state.win/st.session_state.tries)

    if (st.session_state.pick == st.session_state.final):
        st.session_state.stay += 1
    else:
        st.session_state.switch += 1
        

    if (st.session_state.pick == st.session_state.car):
        st.session_state.staywin += 1
    else:
        st.session_state.switchwin += 1

    switchwinprob = st.session_state.switchwin / st.session_state.tries
    staywinprob = st.session_state.staywin / st.session_state.tries
    st.session_state.win_switch_hist.append(switchwinprob)
    st.session_state.win_stay_hist.append(staywinprob)

    for k in ["steps", "car", "pick", "reveal", "final"]:
        st.session_state.pop(k,None)
    st.session_state.step = 1

def host_reveal(car, pick):
    """Host reveals a goat door that is not the player's pick and not the car."""
    options = [d for d in DOORS if d != pick and d != car]
    return random.choice(options)

def other_door(pick, reveal):
    """The remaining unopened door besides pick and reveal."""
    return [d for d in DOORS if d not in (pick, reveal)][0]


#Initialization
st.session_state.setdefault("step", 1)
st.session_state.setdefault("tries", 0)
st.session_state.setdefault("win", 0)
st.session_state.setdefault("stay", 0)
st.session_state.setdefault("switch", 0)
st.session_state.setdefault("switchwin", 0)
st.session_state.setdefault("staywin", 0)
st.session_state.setdefault("win_switch_hist", [])
st.session_state.setdefault("win_stay_hist", [])
st.session_state.setdefault("tries_hist", [])
st.session_state.setdefault("win_hist", [])

st.title("Monty Hall Problem")
st.caption("Pick a door → host reveals a goat → you choose stay/switch → see if you win. Created by Sobhan.")
if st.button("Reset / Start over"):
    reset()
    st.rerun()


col1, col2 = st.columns(2,gap ="xxlarge",width="stretch")
#Step 1
with col1:
    if st.session_state.step == 1:
        st.subheader("Step 1: Pick a door")
        Doors = st.columns(3)
        DOORS = [0, 1, 2]
        with Doors[0]:
            st.image("door.png")
            if st.button("1"):
                st.session_state.car = random.choice(DOORS)
                st.session_state.pick = 0
                st.session_state.reveal = host_reveal(st.session_state.car, st.session_state.pick)
                st.session_state.step = 2
                st.rerun()

        with Doors[1]:
            st.image("door.png")
            if st.button("2"):
                st.session_state.car = random.choice(DOORS)
                st.session_state.pick = 1
                st.session_state.reveal = host_reveal(st.session_state.car, st.session_state.pick)
                st.session_state.step = 2
                st.rerun()

        with Doors[2]:    
            st.image("door.png")
            if st.button("3"):
                st.session_state.car = random.choice(DOORS)
                st.session_state.pick = 2
                st.session_state.reveal = host_reveal(st.session_state.car, st.session_state.pick)
                st.session_state.step = 2
                st.rerun()
    


#step 2
with col1:
    if st.session_state.step == 2:
        st.subheader("Step 2: Host reveals a goat")

        Doors = st.columns(3)
        DOORS = [0, 1, 2]
        with Doors[0]:
            if st.session_state.reveal == 0:
                st.image("goat.png")
                st.button("goat", disabled=True)


            elif st.session_state.pick == 0: 
                st.image("door.png")
                if st.button("Stay") :
                    st.session_state.final = 0  
                    st.session_state.step = 3
                    st.rerun() 

            elif st.session_state.pick != 0 and st.session_state.reveal != 0: 
                st.image("door.png")
                if st.button("Switch") :  
                    st.session_state.final = 0 
                    st.session_state.step = 3
                    st.rerun()

        with Doors[1]:
            if st.session_state.reveal== 1:
                st.image("goat.png")
                st.button("goat", disabled=True)

            elif st.session_state.pick == 1: 
                st.image("door.png")
                if st.button("Stay") :   
                    st.session_state.final = 1
                    st.session_state.step = 3
                    st.rerun()
            elif st.session_state.pick != 1 and st.session_state.reveal != 1: 
                st.image("door.png")
                if st.button("Switch") :  
                    st.session_state.final = 1 
                    st.session_state.step = 3
                    st.rerun()

        with Doors[2]:
            if st.session_state.reveal== 2:
                st.image("goat.png")
                st.button("goat", disabled=True)

            elif st.session_state.pick == 2: 
                st.image("door.png")
                if st.button("Stay") :  
                    st.session_state.final = 2
                    st.session_state.step = 3
                    st.rerun()   

            elif st.session_state.pick != 2 and st.session_state.reveal != 2: 
                st.image("door.png")
                if st.button("Switch") :  
                    st.session_state.final = 2 
                    st.session_state.step = 3
                    st.rerun()
        st.write(f"You picked **Door {st.session_state.pick +1 }**.")
        st.write(f"The host opens **Door {st.session_state.reveal +1 }**. it's a goat!")





#step 3
with col1:
    if st.session_state.step == 3:
        st.subheader("Step 3: Host reveals the Car ")

        


        Doors = st.columns(3)
        DOORS = [0, 1, 2]
        with Doors[0]:
            if st.session_state.car  != 0:
                st.image("goat.png")
                st.button("goat", disabled=True, key=10)


            else: 
                st.image("car.png")
                st.button("goat", disabled=True, key=20)


        with Doors[1]:
            if st.session_state.car  != 1:
                st.image("goat.png")
                st.button("goat", disabled=True, key=11)


            else: 
                st.image("car.png")
                st.button("car", disabled=True, key=21)



        with Doors[2]:
            if st.session_state.car  != 2:
                st.image("goat.png")
                st.button("goat", disabled=True, key=12)


            else: 
                st.image("car.png")
                st.button("car", disabled=True, key=22)

        if st.button("Try Again",width=1000):
            retry()
            st.rerun()
        
        st.write(f"You picked **Door {st.session_state.final + 1}**.")
        if (st.session_state.final == st.session_state.car):
            st.write(f"The host opens all the doors. You won!")
        else:
            st.write(f"The host opens all the doors. You lost!")
with col2:
    fig, ax = plt.subplots()
    ax.plot(
        st.session_state.tries_hist,
        st.session_state.win_hist, 'green',linestyle='solid' , label = 'Your Win Rate',marker='s'
    )
    ax.plot(
        st.session_state.tries_hist,
        st.session_state.win_stay_hist, 'blue',linestyle='dotted', label = 'Stay Win Rate',marker='^'
    )
    ax.plot(
        st.session_state.tries_hist,
        st.session_state.win_switch_hist, 'red',linestyle='dashed' , label = 'Switch Win Rate',marker='+'
    )

    ax.set_xlabel("Trial")
    ax.set_ylabel("Win Probability")
    ax.set_ylim(-.10, 1.25)
    ax.set_xlim(0, st.session_state.tries+2)
    ax.set_xticks(range(1,st.session_state.tries +1))
    ax.set_yticks([0, .1, .2 ,.3,.4,.5,.6,.7,.8,.9,1])
    ax.legend()
    st.pyplot(fig)

    
