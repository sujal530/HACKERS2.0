const resources = {

python:{

videos:[
{
title:"Python Full Course (freeCodeCamp)",
desc:"Complete Python course for beginners.",
link:"https://www.youtube.com/results?search_query=python+full+course+freecodecamp"
},
{
title:"Python Tutorial (CodeWithHarry)",
desc:"Python playlist from beginner to advanced.",
link:"https://www.youtube.com/results?search_query=python+codewithharry"
},
{
title:"Python Projects",
desc:"Build real-world Python projects.",
link:"https://www.youtube.com/results?search_query=python+projects"
}
],

articles:[
{
title:"Python Official Docs",
desc:"Official Python documentation.",
link:"https://docs.python.org/3/"
},
{
title:"W3Schools Python",
desc:"Beginner-friendly Python tutorial.",
link:"https://www.w3schools.com/python/"
},
{
title:"GeeksforGeeks Python",
desc:"Python tutorials and interview questions.",
link:"https://www.geeksforgeeks.org/python-programming-language/"
}
],

practice:[
{
title:"HackerRank Python",
desc:"Practice Python coding.",
link:"https://www.hackerrank.com/domains/python"
},
{
title:"LeetCode",
desc:"Coding interview questions.",
link:"https://leetcode.com/"
},
{
title:"CodeChef",
desc:"Competitive programming.",
link:"https://www.codechef.com/"
}
]

},

java:{

videos:[
{
title:"Java Full Course",
desc:"Complete Java course.",
link:"https://www.youtube.com/results?search_query=java+full+course"
},
{
title:"Java Tutorial",
desc:"Java beginner playlist.",
link:"https://www.youtube.com/results?search_query=java+tutorial"
},
{
title:"Java Projects",
desc:"Build Java applications.",
link:"https://www.youtube.com/results?search_query=java+projects"
}
],

articles:[
{
title:"Oracle Java Docs",
desc:"Official Java documentation.",
link:"https://docs.oracle.com/en/java/"
},
{
title:"W3Schools Java",
desc:"Learn Java basics.",
link:"https://www.w3schools.com/java/"
},
{
title:"GeeksforGeeks Java",
desc:"Java programming tutorials.",
link:"https://www.geeksforgeeks.org/java/"
}
],

practice:[
{
title:"HackerRank Java",
desc:"Practice Java problems.",
link:"https://www.hackerrank.com/domains/java"
},
{
title:"LeetCode",
desc:"Interview preparation.",
link:"https://leetcode.com/"
},
{
title:"CodeChef",
desc:"Competitive programming.",
link:"https://www.codechef.com/"
}
]

},

cpp:{

videos:[
{
title:"C++ Full Course",
desc:"Complete C++ course.",
link:"https://www.youtube.com/results?search_query=c%2B%2B+full+course"
},
{
title:"C++ STL",
desc:"Learn Standard Template Library.",
link:"https://www.youtube.com/results?search_query=c%2B%2B+stl"
},
{
title:"C++ Projects",
desc:"Real-world C++ projects.",
link:"https://www.youtube.com/results?search_query=c%2B%2B+projects"
}
],

articles:[
{
title:"cppreference",
desc:"Official C++ reference.",
link:"https://en.cppreference.com/"
},
{
title:"W3Schools C++",
desc:"Learn C++ basics.",
link:"https://www.w3schools.com/cpp/"
},
{
title:"GeeksforGeeks C++",
desc:"C++ tutorials.",
link:"https://www.geeksforgeeks.org/c-plus-plus/"
}
],

practice:[
{
title:"HackerRank C++",
desc:"Practice C++.",
link:"https://www.hackerrank.com/domains/cpp"
},
{
title:"LeetCode",
desc:"Coding interview questions.",
link:"https://leetcode.com/"
},
{
title:"CodeChef",
desc:"Competitive programming.",
link:"https://www.codechef.com/"
}
]

}

};

const topic=document.getElementById("topicSelect");
const search=document.getElementById("searchBox");

function createCard(item){

return `
<div class="card">

<h3>${item.title}</h3>

<p>${item.desc}</p>

<a href="${item.link}" target="_blank">

Open Resource →

</a>

</div>
`;

}

function loadResources(){

const lang=topic.value;

document.getElementById("videos").innerHTML=
resources[lang].videos.map(createCard).join("");

document.getElementById("articles").innerHTML=
resources[lang].articles.map(createCard).join("");

document.getElementById("practice").innerHTML=
resources[lang].practice.map(createCard).join("");

}

topic.addEventListener("change",loadResources);

search.addEventListener("keyup",()=>{

const value=search.value.toLowerCase();

document.querySelectorAll(".card").forEach(card=>{

card.style.display=
card.innerText.toLowerCase().includes(value)
?"block":"none";

});

});

loadResources();