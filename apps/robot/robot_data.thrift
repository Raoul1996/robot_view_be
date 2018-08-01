service RobotReceiver {
    map<string,string> saveRobotData(),
    string ping(),
    string say(1:string msg)
}