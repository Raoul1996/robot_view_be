namespace py robot_data
//struct BaseResp {
//    1: string StatusMessage = "",
//    2: i32 StatusCode = 0,
//}
//struct RobotInfo{
//    1: required i32 RobotID,
//    2: required string RobotInfo,
//    3: optional i32 time
//}
//struct CommonResponse {
//    1: i32 errno = 0,
//    2: string errmsg = 'ok';
//    3: optional map<string,string> data,
//    255: optional BaseResp BaseResp
//}
service RobotReceiver {
    map<string,string> saveRobotData(),
    string ping(),
    string say(1:string msg),
    map<i32,string> RobotInfo(1: required i32 RobotID, 2: required string RobotInfo)
}