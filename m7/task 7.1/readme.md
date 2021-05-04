 ### Linux administration with bash

 #### Created a scripts to answer the following question, using Apache example log.

 1. From which ip were the most requests:
   
            #!/bin/bash
            log_out=out_script1
            grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $1 | sort | uniq -c | sort -gr > $log_out
            {
            read line1    
            } < $log_out
            echo $line1
2. Most requested page:
      
            #!/bin/bash
            log_out=out_script2
            awk '{print $7}' $1 | sort | uniq -c | sort -gr > $log_out
            {
            read line1    
            } < $log_out
            echo $line1
3. How many reauests were there fron each ip:
   
            #!/bin/bash
            grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $1 | sort | uniq -c | sort -gr
4. What non-existent pages were clients referred to:

            #!/bin/bash
            awk '
            {
            if ($9 !~ /2../) print $7, $9
            }' $1 | sort | uniq -c | sort -gr
5. What time did site get the most requests:

            #!/bin/bash
            log_out=out_script2
            awk '{print $4, $1}' $1 | sort | uniq -c | sort -gr > $log_out
            {
            read line1    
            } < $log_out
            echo $line1
6. What serach bots have accessed the site (user agent+ip):

            #!/bin/bash
            awk -vFPAT='([^ ]+)|("[^"]+")' '{print $1, $10}' $1 | grep -i bot | sort | uniq -c | sort -gr 

Additionally, I created a script to improve my skills in the bash and placed the previous developments in it:

            #!/bin/bash
            #отлавливание сигналов
            trap "echo -e '\n <- Bye!'" EXIT
            trap "echo -e '\n <- Enter file name...'" SIGTSTP

            function chek_file {
            #проверка существования файла
            if [ -e "$file_out" ] 
            then
            #проверка что файл не пустой
            if [ -s "$file_out" ]
            then 
            log_out=log_out_temp
            echo -e "\n File found"
            pls_enter_anykey
            #From which ip were the most requests
            echo -e "\n"
            echo "From which ip were the most requests:"
                  grep -P -o "(\d{1,3}[\.]){3}\d{1,3}" $file_out | sort | uniq -c | sort -gr > $log_out
                  {
                  read line1    
                  } < $log_out
                  echo $line1
            echo -e "\n"
            pls_enter_anykey
                  #Most requested page
                  echo "Most requested page:"
                  awk '{print $7}' $file_out | sort | uniq -c | sort -gr > $log_out
                  {
                  read line1    
                  } < $log_out
                  echo $line1
            echo -e "\n"
            pls_enter_anykey
                  #How many reauests were there fron each ip
                  echo "How many reauests were there fron each ip:"
                  grep -E -o "([0-9]{1,3}[\.]){3}[0-9]{1,3}" $file_out | sort | uniq -c | sort -gr
            echo -e "\n"
            pls_enter_anykey
                  #What non-existent pages were clients referred to
            echo "What non-existent pages were clients referred to:"
                  awk '
                  {
                  if ($9 !~ /2../) print $7, $9
                  }' $file_out | sort | uniq -c | sort -gr
            echo -e "\n"
            pls_enter_anykey
            #What time did site get the most requests
            echo "What time did site get the most requests:"
                  awk '{print $4, $1}' $file_out | sort | uniq -c | sort -gr > $log_out
                  {
                  read line1    
                  } < $log_out
                  echo $line1
            echo -e "\n"
            pls_enter_anykey
            #What serach bots have accessed the site
            echo "What serach bots have accessed the site:"
            awk -vFPAT='([^ ]+)|("[^"]+")' '{print $1, $10}' $file_out | grep -i bot | sort | uniq -c | sort -gr 
            echo -e "\n"
            else
            echo -e "\n"
            echo "File is empty"
            fi
            else
            echo -e "\n"
            echo "File not found" 
            fi
            }

            function pls_enter_anykey {
            echo -e "\npress anykey for next step..."
            read line
            }

            #передаем файл аргументом
            echo -n "Enter file name: "
            if read -t 15 file_out 
            then
            chek_file
            else
            echo -e "\n\nTime is money! \nChoose:"
            ls
            #недождались ввода
            echo -e "\n"
            echo -n "Enter file name: "
            if read -t 30 file_out
            then 
            chek_file
            else
            echo -e "\n"
            echo -e "\nCome back when you remember..."
            fi
            fi
<a href="files/file_check">Final script file</a>

<a href="files/apache_logs.txt">Apache log file</a>