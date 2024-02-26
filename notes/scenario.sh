echo "Changing to correct directory"
cd /home/jovyan/3308class/lab-3-emdonkus 
if [[ $2 -eq 1 || "$2" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 1: Bad Year----------------"
    echo "_________________________________________________"
    year=19
    game_id=2426

    createData.sh $year $game_id 
    status=$? 

    echo "Error Status: $status"
    echo "Expected : 1"
    if [[ $status -eq 1 ]];
    then
        status1="CASE 1 Successful"
    else
        status1="CASE 1 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 2 || "$2" == "ALL" ]];
then

    echo "_________________________________________________"
    echo "----------------CASE 2: Bad Game_id----------------"
    echo "_________________________________________________"
    year=1999
    game_id=2

    createData.sh $year $game_id
    status=$? 

    echo "Error Status: $status"
    echo "Expected : 1"
    if [[ $status -eq 1 ]];
    then
        status2="CASE 2 Successful"
    else
        status2="CASE 2 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 3 || "$2" == "NEVER" ]];
then

    echo "_________________________________________________"
    echo "----------------CASE 3: Bad comparison----------------"
    echo "_________________________________________________"
    year=2014
    game_id=4000

    createData.sh $year $game_id
    status=$? 


    echo "Error Status: $status"
    echo "Expected : BROKEN"
    if [[ $status -ne 0 ]];
    then
        status3="CASE 3 Successful"
    else
        status3="CASE 3 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 3 || "$2" == "ALL" ]];
then


    echo "_________________________________________________"
    echo "----------------CASE 4: Bad year and game_id----------------"
    echo "_________________________________________________"
    year=199
    game_id=34
    
    createData.sh $year $game_id

    status=$? 

    echo "Error Status: $status"
    echo "Expected : 1"
    if [[ $status -eq 1 ]];
    then
        status4="CASE 4 Successful"
    else
        status4="CASE 4 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 5 || "$2" == "ALL" ]];
then

    echo "_________________________________________________"
    echo "----------------CASE 5: Good File----------------"
    echo "_________________________________________________"
    year=2015
    game_id=5002

    createData.sh $year $game_id

    status=$? 

    echo "Error Status: $status"
    echo "Expected : 0"

    if [[ $status -eq 0 ]];
    then
        status5="CASE 5 Successful"
    else
        status5="CASE 5 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 6 || "$2" == "ALL" ]];
then

    echo "_________________________________________________"
    echo "----------------CASE 6: File exists----------------"
    echo "_________________________________________________"
    year=2015
    game_id=5002

    createData.sh $year $game_id
    status=$? 

    echo "Error Status: $status"
    echo "Expected : 4"
    if [[ $status -eq 4 ]];
    then
        status6="CASE 6 Successful"
    else
        status6="CASE 6 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 7 || "$2" == "ALL" ]];
then

    echo "_________________________________________________"
    echo "----------------CASE 7: Not running from correct dir----------------"
    echo "_________________________________________________"
    cd ..

    createData.sh $year $game_id
    status=$? 
    echo "Error Status: $status"
    echo "Expected : 3"
    if [[ $status -eq 3 ]];
    then
        status7="CASE 7 Successful"
    else
        status7="CASE 7 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
    echo "Returning to previous dir"
    cd -
    pwd
fi
if [[ $2 -eq 8 || "$2" == "ALL" ]];
then

    echo "_________________________________________________"
    echo "----------------CASE 8: Empty args----------------"
    echo "_________________________________________________"
    year=""
    game_id=2426

    createData.sh $year $game_id 
    status=$? 
    echo "Error Status: $status"
    echo "Expected : 2"
    if [[ $status -eq 2 ]];
    then
        status8="CASE 8 Successful"
    else
        status8="CASE 8 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 9 || "$2" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 9: Too many args----------------"
    echo "_________________________________________________"
    year=1999
    game_id=2426
    extra="hi"

    createData.sh $year $game_id $extra
    status=$? 
    echo "Error Status: $status"
    echo "Expected : 2"
    if [[ $status -eq 2 ]];
    then
        status9="CASE 9 Successful"
    else
        status9="CASE 9 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
if [[ $2 -eq 10 || "$2" == "ALL" ]];
then
    echo "_________________________________________________"
    echo "----------------CASE 10:Out of Range Year----------------"
    echo "_________________________________________________"
    year=1934
    game_id=2426

    createData.sh $year $game_id
    status=$? 
    echo "Error Status: $status"
    echo "Expected : 1"
    if [[ $status -eq 1 ]];
    then
        status10="CASE 10 Successful"
    else
        status10="CASE 10 Unsuccesful"       
    fi

    if [[ $1 -eq 1 ]];
    then
        read -p "Press [ENTER] to continue"
    fi
fi
echo "_________________________________________________"
echo "--------------------Summary-----------------------------------"
echo "_________________________________________________"
echo "CASE 1: $status1"
echo "CASE 2: $status2"
echo "CASE 3: $status3"
echo "CASE 4: $status4"
echo "CASE 5: $status5"
echo "CASE 6: $status6"
echo "CASE 7: $status7"
echo "CASE 8: $status8"
echo "CASE 9: $status9"
echo "CASE 10: $status10"
echo "--------------------Cleaning Up------------------------------"
read -p "Press [ENTER] to clean up directory"
 
pwd
rm -rf Recipes/*
read -p "Press [ENTER] to End"
clear


