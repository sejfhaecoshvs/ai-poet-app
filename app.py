import streamlit as st
import openai

openai.api_key = "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"

st.title("AI Poet - 사랑을 주제로 한 시")

if st.button("사랑 시 생성하기"):
    with st.spinner("시를 생성 중입니다..."):
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "너는 창의적이고 감성적인 시인이다."},
                {"role": "user", "content": "사랑을 주제로 감성적이고 아름다운 시를 써줘."}
            ],
            max_tokens=200,
            temperature=0.8,
        )
        poem = response['choices'][0]['message']['content']
        st.markdown("### 생성된 시")
        st.write(poem)
