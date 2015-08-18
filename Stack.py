__author__ = 'wuheyou'
class Stack():
    def __init__(st,size):
        st.stack=[];
        st.size=size;

    def push(st,content):
        if st.Full():
            print "Stack is Full!"
        else:
            st.stack.append(content)

    def out(st):
        if st.Empty():
            print "Stack is Empty!"
        else:
            print(len(st.stack)-1)
            del st.stack[len(st.stack)-1]
    def Full(st):
        if  len(st.stack)==st.size:
            return True
        else:
            return False
    def Empty(st):
        if len(st.stack)==0:
            return True
        else:
            return False