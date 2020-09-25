# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 11:01:53 2020

@author: ujwal
"""

import pickle
import streamlit as st

pickle_in = open("svm_cancer_prediction.pkl", "rb")
classifier = pickle.load(pickle_in)

def predict_cancer(Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit):
    prediction = classifier.predict([[Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit]])
    print(prediction)
    return prediction

def main():
    st.title("Cancer Cell Analysis")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white; text-align=center">Cancel Cell Analysis ML App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Clump = st.text_input("Clump", "Type Here")
    UnifSize = st.text_input("UnifSize", "Type Here")
    UnifShape = st.text_input("UnifShape", "Type Here")
    MargAdh = st.text_input("MargAdh", "Type Here")
    SingEpiSize = st.text_input("SingEpiSize", "Type Here")
    BareNuc = st.text_input("BareNuc", "Type Here")
    BlandChrom = st.text_input("BlandChrom", "Type Here")
    NormNucl = st.text_input("NormNucl", "Type Here")
    Mit = st.text_input("Mit", "Type Here")
    
    result = ""
    if st.button("Predict"):
        result = predict_cancer(Clump, UnifSize, UnifShape, MargAdh, SingEpiSize, BareNuc, BlandChrom, NormNucl, Mit)
    st.success("The output is {}".format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Build with streamlit")

if __name__=="__main__":
    main()