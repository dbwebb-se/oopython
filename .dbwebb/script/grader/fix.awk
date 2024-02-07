#!/usr/bin/env awk

BEGIN {
  FS=","
  total = 0

  while ((getline temp < "teachers.data") > 0) {
    gsub(/^ | $/, "", temp)
    kmoms[temp][0] = 0 # Kmom01
    kmoms[temp][1] = 0 # Kmom02
    kmoms[temp][2] = 0 # Kmom03
    kmoms[temp][3] = 0 # Kmom04
    kmoms[temp][4] = 0 # Kmom05
    kmoms[temp][5] = 0 # Kmom06
    kmoms[temp][6] = 0 # Kmom07
    kmoms[temp][7] = 0 # Kmom10
    kmoms[temp][8] = 0 # total %
    kmoms[temp]["G"] = 0 # amount of G's
  }
}

{
  #print $0

    gsub(/"/, "", $1)
    gsub(/"/, "", $2)
    gsub(/"/, "", $3)

    kmoms[$2][$3]++

    if ($1 == "kmom01") {
      kmoms[$2][0]++
    } else if ($1 == "kmom02") {
      kmoms[$2][1]++
    } else if ($1 == "kmom03") {
      kmoms[$2][2]++
    } else if ($1 == "kmom04") {
      kmoms[$2][3]++
    } else if ($1 == "kmom05") {
      kmoms[$2][4]++
    } else if ($1 == "kmom06") {
      kmoms[$2][5]++
    } else if ($1 == "kmom07") {
      kmoms[$2][6]++
    } else if ($1 == "kmom10") {
      kmoms[$2][7]++
    }
}

END {
  total=0
  total1=0
  total2=0
  total3=0
  total4=0
  total5=0
  total6=0
  total7=0
  total8=0
  teachertotal=0

  all=0
  printf ("%-20s%s%8s%8s%8s%8s%8s%8s%8s%8s%s%8s%7s%6s%7s\n", "Name", "|", "Kmom01", "Kmom02", "Kmom03", "Kmom04", "Kmom05", "Kmom06", "Kmom07", "Kmom10", "|", "Totalt", "%", "G", "%G")
  printf ("%s\n", "--------------------------------------------------------------------------------------------------------------")
  for (name in kmoms) {
    total1+=kmoms[name][0]
    total2+=kmoms[name][1]
    total3+=kmoms[name][2]
    total4+=kmoms[name][3]
    total5+=kmoms[name][4]
    total6+=kmoms[name][5]
    total7+=kmoms[name][6]
    total8+=kmoms[name][7]
    kmoms[name][8]+=kmoms[name]["0"]+kmoms[name][1]+kmoms[name][2]+kmoms[name][3]+kmoms[name][4]+kmoms[name][5]+kmoms[name][6]+kmoms[name][7]

  }

  alltotal = total1+total2+total3+total4+total5+total6+total7+total8
  alltotal_g = 0

  for (name in kmoms) {
    alltotal_g += kmoms[name]["G"]
    tot_percentage = 0

    amountG = 0
    g_percentage = 0
    if (kmoms[name][8] > 0) {
      tot_percentage = (kmoms[name][8] / alltotal)*100
    }
    if (kmoms[name]["G"] > 0) {
      amountG = kmoms[name]["G"]
      if (alltotal_g != 0) {
        alltotal_g_percentage = (alltotal_g / alltotal)*100
      } else {
        alltotal_g_percentage = 0
      }
    }
    printf ("%-20s%s%8s%8s%8s%8s%8s%8s%8s%8s%s%8s%6.0f%%%6s%6.0f%%\n", name, "|", kmoms[name][0], kmoms[name][1], kmoms[name][2], kmoms[name][3], kmoms[name][4], kmoms[name][5], kmoms[name][6], "|", kmoms[name][7], "|", kmoms[name][8] tot_percentage, amountG, g_percentage)

  }
    alltotal_g_percentage = (alltotal_g / alltotal)*100
    printf ("%s\n", "---------------------------------------------------------------------------------------------------------------")

    printf ("%-20s%s%8s%8s%8s%8s%8s%8s%8s%s%8s%6.0f%%%6s%6.0f%%\n", "Totalt", "|", total1, total2, total3, total4, total5, total6, total7, total8 "|", alltotal, 100.00, alltotal_g, alltotal_g_percentage)
    printf ("%s\n", "---------------------------------------------------------------------------------------------------------------")
    printf ("%-20s%s%7.0f%%%7.0f%%%7.0f%%%7.0f%%%7.0f%%%7.0f%%%7.0f%%%7.0f%%\n", "Genomströmming", "|", (total1/total1*100), (total2/total1*100), (total3/total1*100), (total4/total1*100), (total5/total1*100), (total6/total1*100), (total7/total1*100), (total8/total1*100))

}