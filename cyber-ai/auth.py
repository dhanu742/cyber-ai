# auth.py

import streamlit as st

from database import (
    register_user,
    login_user
)


# =====================================
# LOGIN PAGE
# =====================================

def login_page():

    col1, col2, col3 = st.columns([1,2,1])

    with col2:

        st.markdown(

            """
            <h1 style='text-align:center;
                       color:#00ffcc;
                       text-shadow:0px 0px 20px #00ffcc;'>

            🔐 CYBER AI LOGIN

            </h1>
            """,

            unsafe_allow_html=True
        )

        option = st.radio(

            "Select Option",

            [
                "Login",
                "Register"
            ],

            horizontal=True
        )


        # =============================
        # USERNAME
        # =============================

        username = st.text_input(
            "Username"
        )


        # =============================
        # PASSWORD
        # =============================

        password = st.text_input(

            "Password",

            type="password"
        )


        # =============================
        # LOGIN
        # =============================

        if option == "Login":

            if st.button(

                "Login",

                use_container_width=True
            ):

                if login_user(
                    username,
                    password
                ):

                    st.session_state.logged_in = True

                    st.session_state.username = username

                    st.success(
                        "Login successful"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid username or password"
                    )


        # =============================
        # REGISTER
        # =============================

        else:

            if st.button(

                "Create Account",

                use_container_width=True
            ):

                # PASSWORD SECURITY

                if len(password) < 8:

                    st.error(
                        "Password too weak (minimum 8 characters)"
                    )

                else:

                    success = register_user(

                        username,

                        password
                    )

                    if success:

                        st.success(
                            "Account created successfully"
                        )

                    else:

                        st.error(
                            "Username already exists"
                        )