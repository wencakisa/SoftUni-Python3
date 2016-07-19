def main():
    ivan = ['пушене', 'пиене', 'тия три неща', 'коли', 'facebook', 'игри', 'разходки по плажа', 'скандинавска поезия']
    maria = ['пиене', 'мода', 'facebook', 'игри', 'лов със соколи', 'шопинг', 'кино']

    print('Common interests: {}'.format(', '.join(set(ivan).intersection(set(maria)))))

if __name__ == '__main__':
    main()
