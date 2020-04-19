import pandas as pd 

def splitting (converted_directory,Ratio_train,train_folder,test_folder):
        #retrieve all file in the folder 
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(converted_directory):
            
            for file in f:
                files.append(file)
        #define which file (lable + image) to put in  training set(based on ratio )
        df= pd.DataFrame(files,columns = ['files'])
        df['file_name'] =df['files'].str.split('.').str[0]
        
        df_train =df.drop(columns =['files']) # drop file type 
        df_train =df_train.drop_duplicates( inplace = False)#subset ="First Name", 
        
        df_train = df_train['file_name'].sample(frac = Ratio_train , random_state=42).to_frame()
        df_train['train'] =1 
        
        df=pd.merge(df, df_train, on='file_name', how='outer')
        df=df.fillna(0)
    
        for i in df.index : 
            path = os.path.join(converted_directory,df['files'].iloc[i])
            
            if df['train'].iloc[i] == 1:
                shutil.copy(path,train_folder)    
                print('train - ',df['files'].iloc[i])
            else : 
                shutil.copy(path,test_folder)
                print('test  - ',df['files'].iloc[i])
                
