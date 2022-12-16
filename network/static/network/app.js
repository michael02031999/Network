
comments = document.querySelectorAll("#comment")
username = document.querySelectorAll('#username')
usernameDiv = document.querySelectorAll('#usernameDiv')

likesThumb = document.querySelectorAll("#like")
dislikesThumb = document.querySelectorAll("#dislike")
posts = document.querySelectorAll("#post")

for (let i = 0; i < posts.length; i++) 
{
    try {
        likesThumb[i].addEventListener("click", (e) => {
            dislike(e);
        })
    }
    catch(err) {
        console.log(err);
    }

    try {
        dislikesThumb[i].addEventListener("click", (e) => {
            like(e);
        })
    }
    catch (err) {
        console.log(err);
    }

    
}

function like(e) {
    console.log(e);

    console.log("something fires");

    numLikes = e['path'][2].querySelector("#numLikes").innerText

    numLikes = parseInt(numLikes);


    if (e['path'][0].style.color == "gold") {
        e['path'][0].style.color = "gray";

        fetch(`change_likes/${e['path'][2].querySelector("#id").innerHTML}/${"dislike"}`)
        numLikes = numLikes - 1; 
        e['path'][2].querySelector("#numLikes").innerText = numLikes;
    }
    else {
        e['path'][0].style.color = "gold";
        fetch(`change_likes/${e['path'][2].querySelector("#id").innerHTML}/${"like"}`)
        numLikes = numLikes + 1; 
        e['path'][2].querySelector("#numLikes").innerText = numLikes;
    }
}    

function dislike(e) {
    console.log(e);

    console.log("something fires");

    numLikes = e['path'][2].querySelector("#numLikes").innerText

    numLikes = parseInt(numLikes);


    if (e['path'][0].style.color == "gray") {
        e['path'][0].style.color = "gold";
        fetch(`change_likes/${e['path'][2].querySelector("#id").innerHTML}/${"like"}`)

        numLikes = numLikes + 1; 
        e['path'][2].querySelector("#numLikes").innerText = numLikes;
    }
    else {
        e['path'][0].style.color = "gray";
        fetch(`change_likes/${e['path'][2].querySelector("#id").innerHTML}/${"dislike"}`)

        numLikes = numLikes - 1; 
        e['path'][2].querySelector("#numLikes").innerText = numLikes;
    }
}





for (let i = 0; i < usernameDiv.length; i++) {
    //console.log("hello");
    if (document.querySelector("#user").innerText == username[i].innerText) {
            //console.log(i);
            edit = document.createElement('div');
            
            edit.setAttribute("id", 'edit')
            edit.innerHTML = "Edit";
            usernameDiv[i].append(edit);

            edit.addEventListener("click", (e) => {
                open_textarea(e)
                
            })
    } 
}

function open_textarea(e) {

        let text = e['path'][2].querySelector('#comment').innerHTML;

        textarea = document.createElement('textarea')
        textarea.setAttribute('id', 'comment_textarea');
        textarea.value=e['path'][2].querySelector('#comment').textContent;
    
        e['path'][2].querySelector('#comment').remove();

        //e['path'][0].remove();
        e['path'][0].style.display = "none";
    
        save = document.createElement('button');
        save.innerHTML = "Save";
        save.setAttribute("id", "save");
        cancel = document.createElement('button');
        cancel.innerHTML = "Cancel";
        cancel.setAttribute("id", "cancel")


        e['path'][2].querySelector('#usernameDiv').append(textarea);
        e['path'][2].querySelector('#usernameDiv').append(save);
        e['path'][2].querySelector('#usernameDiv').append(cancel);

        //console.log(textarea.value)

        save.addEventListener("click", () => {

            fetch(`comment/${e['path'][2].querySelector("#id").innerHTML}/${textarea.value}`)
            new_comment = document.createElement('div');
            new_comment.innerText = textarea.value;
            new_comment.setAttribute('id', 'comment');
            e['path'][2].querySelector('#usernameDiv').append(new_comment);
            textarea.remove();
 
            //.then((data) => console.log(data));
            e['path'][0].style.display = "block";
            save.remove();
            cancel.remove();
        }) 
        
        cancel.addEventListener("click", () => {
            new_comment = document.createElement('div');
            new_comment.innerText = text;
            new_comment.setAttribute('id', 'comment');
            e['path'][0].style.display = "block";
            textarea.remove();
            save.remove();
            cancel.remove();
            e['path'][2].querySelector('#usernameDiv').append(new_comment);
        })
}

