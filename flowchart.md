flowchart TD
    Start([Start]) --> Input[/Input: score/]
    Input --> Check1{score < 0 OR score > 100?}
    Check1 -->|Yes| Invalid[Return "Invalid Score"]
    Check1 -->|No| Check2{score >= 90?}
    Check2 -->|Yes| GradeA[Return "A"]
    Check2 -->|No| Check3{score >= 80?}
    Check3 -->|Yes| GradeB[Return "B"]
    Check3 -->|No| Check4{score >= 70?}
    Check4 -->|Yes| GradeC[Return "C"]
    Check4 -->|No| Check5{score >= 60?}
    Check5 -->|Yes| GradeD[Return "D"]
    Check5 -->|No| GradeF[Return "F"]
    Invalid --> End([End])
    GradeA --> End
    GradeB --> End
    GradeC --> End
    GradeD --> End
    GradeF --> End