char* reverseString(char* s)
{
    if (s == 0)
    {    
        // check if s is NULL
        return s;
    }
    if (*s == 0)
    {
        // check is s is empty string
        return s;
    }
    
    char tmp;
    size_t len = strlen(s) - 1;
    size_t i;
    size_t k = len;
    for(i = 0, k = len; i <= (len / 2); i++, k--)
    {
        // switch the string from both side, when i reaches len / 2, s is reversed
        tmp = s[i];
        s[i] = s[k];
        s[k] = tmp;
    }
    return s;
}
