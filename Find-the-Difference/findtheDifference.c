char findTheDifference(char* s, char* t) {
    /* use XOR sparity, watch out ""
    int diff = 0;
    while(*s)
    {
        diff ^= *(s++) ^ *(t++);
    }
    return diff ^= *t; */
    
    char out;
    int len = strlen(s) + 1;
    for(int i = 0; i < len; i++)
    {
        out ^= s[i] ^ t[i];
    }
    return out;
}
