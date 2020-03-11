namespace py HelloWorld

struct Student {
    1: string name;
    2: i32 age;
}

service HelloWorld {
    i32 birth_year(1:Student stu),
    string say(1:string msg)
}
