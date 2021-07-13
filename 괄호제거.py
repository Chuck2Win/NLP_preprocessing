# 제목 전처리
# (),[],<>의 안 내용도 죄다 빈칸으로
n_train_data['과제명'] = n_train_data['과제명'].apply(lambda i : re.sub(r'\([^)]*\)', '',i)) 
n_train_data['과제명'] = n_train_data['과제명'].apply(lambda i : re.sub(r'\[[^)]*\]', '',i)) 
n_train_data['과제명'] = n_train_data['과제명'].apply(lambda i : re.sub(r'\<[^)]*\>', '',i)) 
# 숫자, 영어, 한글 제외하곤 죄다 빈칸으로
n_train_data['과제명'] = n_train_data['과제명'].apply(lambda i : re.sub('[^a-zA-Zㄱ-ㅎ가-힇0-9 ,.?!]','',i)) 
# 대문자 소문자화
n_train_data['과제명'] = n_train_data['과제명'].apply(lambda i : i.lower()) 
n_train_data['과제명']=n_train_data['과제명']+[' [SEP]']
