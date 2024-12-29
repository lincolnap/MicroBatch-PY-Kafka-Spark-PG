import streamlit as st
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import plotly.express as px  
import plotly.graph_objects as go
import time


# dashboard title
st.set_page_config(
    page_title="Real-Time - Transations Events",
    page_icon="✅",
    layout="wide",
)
#st.title("Real-Time - Transations Events")
#st.write("¡Hola! Esta es una aplicación de Streamlit desplegada con Docker.")

st.title("Real-Time - Transations Events")


def get_data() -> pd.DataFrame:
    return  px.data.tips()

df = get_data()

# create the bins

placeholder = st.empty()

with placeholder.container():

        # create three columns
        #kpi1 = st.columns(1)

        # fill in those three columns with respective metrics or KPIs
        # kpi1.metric(
        #     label="Toltal Revenue",
        #     value=f"$ {round(counts,2)} "
        #    ,delta=-round(balance / count_married) * 100,
        # )
        
        # create two columns for charts
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.markdown("### Person by gender")
            fig =px.histogram(data_frame=df, x="sex", y='total_bill',color="sex", pattern_shape="smoker")
            fig.update_layout(bargap=0.2)
            st.write(fig)
            
        with fig_col2:
            st.markdown("### Second Chart")
            fig2 = px.histogram(data_frame=df, x="total_bill")
            st.write(fig2)

        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)