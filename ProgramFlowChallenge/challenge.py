ip = input("Digite um IP válido: ")
j = 0;
ip1 = ''
ip2 = ''
ip3 = ''
ip4 = ''
if ip == '':
    print('1 - O endereço de IP não é válido.')
else:
    if ((ip[0]=='.') or (ip[len(ip)-1]=='.')):
             print('2 - O endereço de IP não é'
                   ' válido.')
    else:
        for i in range(0, len(ip)):
            if ip[i] not in '.0123456789':
                break
            if (j==3) and (i>15):
                break
            if ip[i]=='.':
                j+=1
                continue

            if j == 0:
                ip1+=ip[i]
                continue
            if j== 1:
                ip2+=ip[i]
                continue
            if j==2:
                ip3+=ip[i]
                continue
            if j==3:
                ip4+=ip[i]
                continue
        if j>3:
            print("O IP digitado é inválido.")
        else:
            if (len(ip1)>3) or (len(ip1)==0) or (len(ip2)>3) or (len(ip2)==0) or(len(ip3)>3) or (len(ip3)==0) or (len(ip4)>3) or (len(ip4)==0):
                print("O IP digitado é inválido.")
            else:
                print("O IP é válido")





    # if len(ip) >= 7:
    #     if ((ip[0]=='.') or (ip[len(ip)-1]=='.')):
    #         print('2 - O endereço de IP não é válido.')
    #     else:
    #         for i in range (0, len(ip)):
    #             j+=1
    #             if ip[i] == '.' and j>4:
    #                 print('3 - O endereço de IP não é válido. j: {0}'.format(j))
    #             else:
    #                 if ip[i]!="." and j>3:
    #                     print('4 - O endereço de IP não é válido. j: {0}'.format(j))
    #                 else:
    #                     j=0
    #                     continue
    #         print('6 - Saiu do for. j: {0}'.format(j))
    # else:
    #     print('5 - O endereço de IP {0} é inválido.'.format(ip))

