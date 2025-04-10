const searchBtn = document.getElementById("search-but");
const searchInput = document.getElementById("search-area");
const resultDiv = document.getElementById("lower");
const toggleBtn = document.getElementById("light");

// Fetch user data from GitHub API
async function getGitHubUser(username) {
  try {
    const response = await fetch(`https://api.github.com/users/${username}`);
    if (!response.ok) throw new Error("User not found");

    const user = await response.json();
    displayUser(user);
  } catch (error) {
    displayError(error.message);
  }
}

// Display the user info in the .lower div
function displayUser(user) {
  resultDiv.innerHTML = `

    <img src="${user.avatar_url}" alt="Avatar" style="width: 120px; height: 120px; border-radius: 50%;">
    <div  style="flex: 1;">
        <div id='login'>
          <h2>${user.name || user.login}</h2>
          <p id='join-time'>Joined ${new Date(user.created_at).toLocaleDateString()}</p>
        </div>
        <a href="${user.html_url}" target="_blank" style="color: hsl(211, 100%, 60%);">@${user.login}</a>
        <p style="margin-top: 10px;">${user.bio || "This profile has no bio"}</p>

        <div id='following'>
          <div><p>Repos</p><h3>${user.public_repos}</h3></div>
          <div><p>Followers</p><h3>${user.followers}</h3></div>
          <div><p>Following</p><h3>${user.following}</h3></div>
        </div>

        <div id='socials'>
          <p class='social'><img src='./assets/icon-location.svg'> ${user.location || "Not Available"}</p>
          <p class='social'><img src='./assets/icon-website.svg'> ${user.blog ? `<a href="${user.blog}" target="_blank">${user.blog}</a>` : "Not Available"}</p>
          <p class='social'><img src='./assets/icon-twitter.svg'> ${user.twitter_username ? `@${user.twitter_username}` : "Not Available"}</p>
          <p class='social'><img src='./assets/icon-company.svg'> ${user.company || "Not Available"}</p>
        </div>
    </div>

  `;
}

// Show error message if user not found
function displayError(message) {
  resultDiv.innerHTML = `
    <div style="padding: 40px; color: red; text-align: center;">
      <h2>${message}</h2>
    </div>
  `;
}

// Event: Search button click
searchBtn.addEventListener("click", () => {
  const username = searchInput.value.trim();
  if (username) {
    getGitHubUser(username);
  }
});

// Optional: Light/Dark toggle (it just changes icon for now.)
toggleBtn.addEventListener("click", () => {
  document.body.classList.toggle("light");
  toggleBtn.innerHTML = document.body.classList.contains("light")
    ? 'DARK <img src="./assets/icon-moon.svg" alt="moon">' : 'LIGHT <img src="./assets/icon-sun.svg" alt="sun">';
});
