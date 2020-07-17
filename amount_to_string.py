# -*- coding: utf-8 -*-

UNITS = (
    '',
    'UN ',
    'DOS ',
    'TRES ',
    'CUATRO ',
    'CINCO ',
    'SEIS ',
    'SIETE ',
    'OCHO ',
    'NUEVE ',
    'DIEZ ',
    'ONCE ',
    'DOCE ',
    'TRECE ',
    'CATORCE ',
    'QUINCE ',
    'DIECISEIS ',
    'DIECISIETE ',
    'DIECIOCHO ',
    'DIECINUEVE ',
    'VEINTE '
)

TENS = (
    'VENTI',
    'TREINTA ',
    'CUARENTA ',
    'CINCUENTA ',
    'SESENTA ',
    'SETENTA ',
    'OCHENTA ',
    'NOVENTA ',
    'CIEN '
)

HUNDREDS = (
    'CIENTO ',
    'DOSCIENTOS ',
    'TRESCIENTOS ',
    'CUATROCIENTOS ',
    'QUINIENTOS ',
    'SEISCIENTOS ',
    'SETECIENTOS ',
    'OCHOCIENTOS ',
    'NOVECIENTOS '
)


def to_word(number):
    currency_single = 'EURO'
    currency_plural = 'EUROS'
    cents = 'CÉNTIMOS'
    ans = to_word_int(int(number), currency_single, currency_plural, cents)
    centimos = int(round((number - int(number)), 2) * 100)
    if centimos > 0:
        ans += currency_plural + ' CON ' + \
            to_word_int(centimos, currency_single,
                        currency_plural, cents) + ' ' + cents
    else:
        ans += currency_plural
    return ans.title()


def to_word_int(number, currency_single, currency_plural, cents):
    """
    Converts a number into string representation
    """
    converted = ''
    flag = 0

    if number == 0:
        return 'CERO '

    if not (0 < number < 999999999):
        return 'No es posible convertir el numero a letras'

    number_str = str(number).zfill(9)
    millones = number_str[:3]
    miles = number_str[3:6]
    cientos = number_str[6:]

    if millones:
        flag = 1
        if millones == '001':
            converted += 'UN MILLON '
        elif int(millones) > 0:
            converted += '%sMILLONES ' % __convertNumber(millones)

    if miles:
        flag = 1
        if miles == '001':
            converted += 'MIL '
        elif int(miles) > 0:
            converted += '%sMIL ' % __convertNumber(miles)

    if cientos:
        flag = 0
        if cientos == '001':
            converted += 'UN ' + currency_single
        elif int(cientos) > 0:
            converted += '%s' % __convertNumber(cientos)
    if flag:
        converted += currency_plural
    return converted


def __convertNumber(n):
    """
    Max length must be 3 digits
    """
    output = ''

    if n == '100':
        output = "CIEN "
    elif n[0] != '0':
        output = HUNDREDS[int(n[0]) - 1]

    k = int(n[1:])
    if k <= 20:
        output += UNITS[k]
    else:
        if (k > 30) & (n[2] != '0'):
            output += '%sY %s' % (TENS[int(n[1]) - 2], UNITS[int(n[2])])
        else:
            output += '%s%s' % (TENS[int(n[1]) - 2], TENS[int(n[2])])

    return output
