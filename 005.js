function leapYear(year)
{
    var output = "";

    if(((year % 4 == 0) && (year % 100 != 0)) || (year % 400 == 0)) output = year + " adalah tahun kabisat"
    else output = year + " adalah bukan tahun kabisat";
    console.log(output);

}
leapYear(2020);