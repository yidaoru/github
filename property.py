def compoundInterest(interest, years, base, base_growth = 0):
    '''
    interest:年资产收益率,如把钱存银行一年期利息是0.04
    years：年数,>=0
    base:基础资产,每年非资产性固定收入，即当年挣得的可用于投资的金额，如工资
    base_growth:基础资产增幅，如平均每年加薪幅度。
    return:返回N年后预期资产总额。
    算法如下：设interest为0.1, years为3，base为1，base_growth为0.05
    property = (1.1**3 + 1.05*1.1**2 + (1.05*1.05)*1.1**1)
    '''

    property = base  # 投资开始
    for i in range(years):
        base_yearly = (base*(1 + base_growth)**(years - i -1))
        income_yearly = base_yearly*((1+ interest)**(i+1))
        property += income_yearly

    base_yearly = (base*(1 + base_growth)**(years -1))  #N年后非资产性年固定收入
    print("base_yearly:{}".format(base_yearly))
    print("property:{}".format(property))
    return property

if __name__ == "__main__":
    compoundInterest(0.1, 10, 10, 0.1)
