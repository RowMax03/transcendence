import { fetchFriendships, fetchFriendsWithProfiles, addFriend, deleteFriendship, blockUser } from './friendservice.js';
import { fetchUserProfileAndStats, fetchProfiles, fetchProfileByUserId } from './profileservice.js';
import { showError,  } from './utils.js';
import { createElement, DEFAULT_AVATAR, DEFAULT_USER_AVATAR, formatDate } from './domHelpers.js';
import { createFriendGame } from "./gameService.js"
const NO_FRIENDS_HTML = '<p class="text-light">No friends available 😞.</p>';
const LOADING_FRIENDS_HTML = '<p class="text-light">Loading friends...</p>';
const NO_FRIENDS_WARNING = 'Sad ... you don\'t seem to have any friends 😞.';
let cachedFriendships = null; // Holds the friendships in memory

const refetchFriends = async () => {
    const data = await fetchFriendships(); // Fetch friendships data

    // Ensure data is an array of objects
    const friendships = Array.isArray(data)
        ? data
        : Object.values(data); // If it's an object (with numeric keys), convert it to an array
    cachedFriendships = friendships;
};

/**
 * Generates individual friend's HTML using the friendship and profile data.
 * @param {Object} friendship - Friendship object.
 * @param {Object} profile - Profile object for the friend.
 * @returns {HTMLElement} - Generated friend list item as DOM element.
 */
const generateFriendHTML = (friendship, profile) => {
    const avatarUrl = profile.avatarUrl || DEFAULT_AVATAR;
    const establishedDate = formatDate(friendship.establishedAt);

return createElement(
    'li', // tagName
    `
    <div class="avatar me-3">
        <a href="/home/profile/${profile.userId}" class="text-decoration-none">
            <img src="${avatarUrl}"
                alt="${profile.nickname || 'Friend Avatar'}"
                class="rounded-circle"
                style="width: 50px; height: 50px; object-fit: cover;" />
        </a>
    </div>
    <div>
        <a href="/home/profile/${profile.userId}" class="text-decoration-none">
            <h6>${profile.nickname || 'Unknown Friend'}</h6>
        </a>
        <p class="small mb-0" style="color:white">${profile.bio || 'No bio available.'}</p>
        <p class="small" style="color:white">Friends since: ${establishedDate}</p>
    </div>
    <div class="ms-auto d-flex gap-2">

        <button class="btn btn-primary btn-sm start-chat-room" data-friendship-id="${friendship.id}">
            Start Chat
        </button>
        <button class="btn btn-success btn-sm start-game" data-friendship-id="${profile.userId}">
            Play a Game
        </button>
        <button class="btn btn-danger btn-sm delete-friend" data-friendship-id="${friendship.id}">
            Delete
        </button>
    </div>
    `,
    'list-group-item bg-dark text-light d-flex align-items-center p-3 rounded-3 mb-2', // className
    {},
    { id: `friendship-${friendship.id}` }
);
};

/**
 * Renders the list of friends with their profiles.
 * @param {Array} friendships - Array of friendship objects fetched from the API.
 * @param {Object} combinedData - Combined API data containing friendship details and profiles.
 * @param {HTMLElement} friendsContainer - The DOM container for the friends list.
 */
const renderFriendsList = (friendships, combinedData, friendsContainer) => {
    friendsContainer.innerHTML = '';
    let friendCount = 0;
    friendships.forEach((friendship, index) => {
        const profile = combinedData[`friend${index}`];
        if (friendship.accepted && profile) {
            const friendHtmlElement = generateFriendHTML(friendship, profile);
            friendsContainer.appendChild(friendHtmlElement);
            friendCount++;
        } else if (!profile) {
            console.warn(`No profile found for friend${index}.`);
        }
    });

    if (friendCount === 0) {
        friendsContainer.innerHTML = NO_FRIENDS_HTML;
    }
};

/**
 * Loads the friends list and their profiles.
 * @param {HTMLElement} friendsContainer - The DOM container for the friends list.
 */
const loadFriends = async (friendsContainer) => {
    friendsContainer.innerHTML = LOADING_FRIENDS_HTML;
    try {
        const data = await fetchFriendships(); // Fetch friendships data

        // Ensure data is an array of objects
        const friendships = Array.isArray(data)
            ? data
            : Object.values(data); // If it's an object (with numeric keys), convert it to an array


        // Check if friendships array is empty
        if (!friendships.length) {
            friendsContainer.innerHTML = `<p class="text-light">${NO_FRIENDS_WARNING}</p>`;
            return;
        }
                cachedFriendships = friendships; // Cache friendships here


        // Fetch more data based on friendships
        const combinedData = await fetchFriendsWithProfiles(friendships);

        // Render the friends list
        renderFriendsList(combinedData.friendships, combinedData, friendsContainer);
    } catch (error) {
        console.error('Failed to load friends:', error);
        showError(friendsContainer, 'Failed to load friends. Try again later.');
    }
};


/*************************************************************************************************************/
async function loadOpponentProfile(opponentId) {
    try {
        const opponent = await fetchProfileByUserId(opponentId);

        return opponent; // Use the resolved value if needed later
    } catch (error) {
        console.error('Failed to fetch opponent profile:', error);
    }
}
/**
 * Renders the profile and stats of the logged-in user.
 * @param {Object} user - User object returned from the API.
 * @param {Object} stats - User stats object returned from the API.
 * @param {HTMLElement} profileContainer - The DOM container for the user profile.
 */
const renderUserProfile = async (user, stats, statsByUser, profileContainer) => {
    const profile = user.profile;

    // Preload opponent profiles in parallel
    const opponents = await Promise.all(
        statsByUser.map(async (stat) => {
            const isWinner = stat.stat.winnerId === user.id;
            const opponentId = isWinner ? stat.stat.loserId : stat.stat.winnerId;
            return { opponentId, opponent: await fetchProfileByUserId(opponentId) };
        })
    );

    profileContainer.appendChild(
        createElement(
            'div',
            `
            <div class="d-flex align-items-center mb-3">
                <div class="avatar me-3">
                    <img src="${profile.avatarUrl || DEFAULT_USER_AVATAR}"
                        alt="User Avatar"
                        class="rounded-circle">
                </div>
                <div>
                    <h4>${profile.nickname} (${user.name})</h4>
                    <p>${profile.bio || 'No bio available.'}</p>
                    <p>Member since: ${formatDate(user.createdAt)}</p>
                </div>
            </div>
            <div>
                <h5>Contact Information</h5>
                <p>Email: ${user.mail || 'N/A'}</p>
                <h5>Additional Information</h5>
                <p>${profile.additionalInfo || 'No additional information available.'}</p>
                <h5>Stats:</h5>

                <!-- Stats Summary -->
                <div class="card bg-dark text-light shadow-sm rounded-3 p-3">
                    <div class="row text-center">
                        <div class="col">
                            <div class="p-2">
                                <h6 class="fw-bold text-light">Total Games</h6>
                                <span class="fs-5">${stats.totalGames}</span>
                            </div>
                        </div>
                        <div class="col border-start border-secondary">
                            <div class="p-2">
                                <h6 class="fw-bold text-primary">Total Wins</h6>
                                <span class="fs-5 text-primary">${stats.totalWins}</span>
                            </div>
                        </div>
                        <div class="col border-start border-secondary">
                            <div class="p-2">
                                <h6 class="fw-bold text-danger">Total Losses</h6>
                                <span class="fs-5 text-danger">${stats.totalLosses}</span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Detailed User Stats -->
                <div class="stats-list mt-3">
                    ${statsByUser.map((stat, index) => {
                        const date = stat.stat.createdAt;
                        const result = stat.didWin ? 'win' : 'loss';
                        const opponentData = opponents.find(o => o.opponentId === (stat.stat.winnerId === user.id ? stat.stat.loserId : stat.stat.winnerId));
                        const opponent = opponentData?.opponent?.profile || {};
                        return `
                            <div class="game-stat bg-dark ${result === 'win' ? 'victory' : 'defeat'}">
                                <div class="d-flex justify-content-between mb-2">
                                    <span>${new Date(date).toLocaleDateString()}</span>
                                    <span class="badge ${result === 'win' ? 'bg-success' : 'bg-danger'}">
                                        ${result === 'win' ? 'Victory' : 'Defeat'}
                                    </span>
                                </div>
                                <div class="d-flex justify-content-around">
                                    <div class="player">
                                        <img src="${profile.avatarUrl || 'https://via.placeholder.com/50'}" alt="${profile.nickname}">
                                        <span>You</span>
                                    </div>
                                    <div class="vs text-bold">
                                        <span>VS</span>
                                    </div>
                                    <div class="opponent">
                                    <a href="/home/profile/${opponent.userId}">
                                        <img src="${opponent.avatarUrl || 'https://via.placeholder.com/50'}" alt="${opponent.nickname || 'Opponent'}">
                                        <span>${opponent.nickname || 'Opponent'}</span>
                                    </a>
                                    </div>
                                </div>
                            </div>
                        `;
                    }).join('')}
                </div>
            </div>
            `
        )
    );
};
/**
 * Loads the profile and stats of the logged-in user.
 * @param {HTMLElement} profileContainer - The DOM container for the user profile.
 * @param {HTMLElement} profileLoading - The loading container for the profile.
 */
const loadUserProfile = async (profileContainer, profileLoading) => {
    try {
        const data = await fetchUserProfileAndStats(userId);
        profileLoading.remove();

        if (data?.user) {
            renderUserProfile(data.user, data.calculateUserStats, data.statsByUser, profileContainer);
        } else {
            throw new Error('User data is missing.');
        }
    } catch (error) {
        console.error('Failed to load profile:', error);
        showError(profileLoading, 'Failed to load profile. Please try again later.');
    }
};


document.addEventListener('DOMContentLoaded', async () => {
    const friendsContainer = document.querySelector('#friends ul');
    const profileContainer = document.getElementById('profile');
    const profileLoading = document.getElementById('profile-loading');

    await Promise.all([loadFriends(friendsContainer), loadUserProfile(profileContainer, profileLoading)]);

    friendsContainer.addEventListener('click', async (event) => {
        if (event.target.classList.contains('delete-friend')) {
            const friendshipId = parseInt(event.target.getAttribute('data-friendship-id'), 10);

            if (!isNaN(friendshipId)) {
                try {

                    const response = await deleteFriendship(friendshipId);

                    if (response && response.success) {

                        const elementToRemove = document.getElementById(`friendship-${friendshipId}`);
                        if (elementToRemove) {
                            elementToRemove.remove(); // Remove from the DOM
                        } else {
                            console.error(`Element with id "friendship-${friendshipId}" not found.`);
                        }
                    } else {
                        console.error(`Failed to delete friendship: ${response ? response.message : 'Unknown error'}`);
                        alert(`Error: ${response.message || 'Failed to delete friendship.'}`);
                    }
                } catch (error) {
                    console.error("An unexpected error occurred while deleting friendship:", error);
                    alert("An error occurred while deleting the friendship. Please try again later.");
                }
            }
        }
    });
    friendsContainer.addEventListener('click', async (event) => {
    // Handle "Play a Game" button click
    if (event.target.classList.contains('start-game')) {
        const friendUserId = parseInt(event.target.getAttribute('data-friendship-id'), 10);

        if (!isNaN(friendUserId)) {
            try {

                // Call the createFriendGame GraphQL mutation
                const game = await createFriendGame(userId, friendUserId);


                alert(`Game created successfully! Game ID: ${game.id}`);

                // Optionally redirect to the game screen
                window.location.href = `/home/game`;
            } catch (error) {
                console.error("Error creating the game:", error);
                alert("Failed to create the game. Please try again later.");
            }
        } else {
            console.error("Invalid friendUserId in the data-friendship-id attribute.");
        }
    }
});
});

const NO_PROFILES_HTML = '<p class="text-light">No profiles found.</p>';
const LOADING_PROFILES_HTML = '<p class="text-light">Loading profiles, please wait...</p>';

const updateFlattendFriendships = async (flattenedFriendships) => {
    await refetchFriends();
    flattenedFriendships = Array.isArray(cachedFriendships) ? cachedFriendships.flat() : [];
    return flattenedFriendships;
};

/**
 * Renders profiles into the DOM.
 * Disables the "Add Friend" button for profiles already in friendships.
 * @param {Array} profiles - The profiles to render.
 * @param {HTMLElement} profilesContainer - The container to render profiles in.
 */
const renderProfiles = (profiles, profilesContainer) => {
    profilesContainer.innerHTML = '';

    if (profiles.length === 0) {
        profilesContainer.innerHTML = NO_PROFILES_HTML;
        return;
    }

    let flattenedFriendships = Array.isArray(cachedFriendships) ? cachedFriendships.flat() : [];

    profiles.forEach((profile) => {
        // Check if the profile userId exists in cachedFriendships
    const isFriendAlready = flattenedFriendships.some(
            (friendship) => friendship.friendId == profile.userId && friendship.accepted
    );

    const isBlocked = flattenedFriendships.some(
        (friendship) => friendship.friendId == profile.userId && friendship.blocked
    );

    const friendship = flattenedFriendships.find(
        (friendship) => friendship.friendId == profile.userId
    );

    const friendshipId = friendship ? friendship.id : 0;

        const profileHTML = `
            <li class="list-group-item bg-dark text-light d-flex justify-content-between align-items-center p-3 rounded-3 mb-2">
                <div class="d-flex align-items-center">
                    <div class="avatar me-3">
                        <a href="/home/profile/${profile.userId}" class="text-decoration-none">
                            <img src="${profile.avatarUrl || 'https://via.placeholder.com/50'}"
                                 alt="Profile Avatar"
                                 class="rounded-circle"
                                 style="width: 50px; height: 50px; object-fit: cover;">
                        </a>
                    </div>
                    <div>
                        <a href="/home/profile/${profile.userId}" class="text-decoration-none">
                            <h6>${profile.nickname || 'Unknown User'}</h6>
                        </a>
                        <p class="small mb-0" style="color:white;">${profile.bio || 'No bio available.'}</p>
                    </div>
                </div>
                <div>
                    <button
                        class="btn ${isFriendAlready ? 'btn-secondary' : 'btn-success'} btn-sm"
                        data-friend-id="${profile.userId}"
                        ${isFriendAlready ? 'disabled' : ''}>
                        ${isFriendAlready ? 'Friend Added' : 'Add Friend'}
                    </button>
                    <button id="block-user"
                        class="btn ${isBlocked ? 'btn-outline-danger' : 'btn-danger'} btn-sm"
                        data-user-id="${profile.userId}"
                        data-blocked="${isBlocked}"
                        data-friendship-id="${friendshipId}">
                            ${isBlocked ? 'Unblock' : 'Block'}
                    </button>
                </div>
            </li>
        `;
        profilesContainer.innerHTML += profileHTML;
    });

    // Attach event listeners to "Add Friend" buttons
    const buttons = profilesContainer.querySelectorAll('.btn-success');
    buttons.forEach((button) => {
        button.addEventListener('click', async (event) => {
            event.preventDefault();

            const friendId = parseInt(button.getAttribute('data-friend-id'), 10);
            if (isNaN(friendId)) {
                console.error("Invalid friend ID.");
                return;
            }

            try {
                // Call the addFriend service function
                const response = await addFriend(friendId);

                if (response && response.success) {

                    button.textContent = "Friend Added!";
                    button.classList.remove("btn-success");
                    button.classList.add("btn-secondary");
                    button.disabled = true; // Disable the button after a successful add
                    // Optionally update cachedFriendships
                    cachedFriendships.push({ friendId }); // Add the new friend to the cache
                } else {
                    console.error(`Failed to add friend: ${response.message}`);
                    alert(`Error: ${response.message}`);
                }
            } catch (error) {
                console.error("An unexpected error occurred:", error);
                alert("An unexpected error occurred. Please try again later.");
            }
        });
    });

    // Attach event listeners to "Block/Unblock" buttons
    const blockButtons = profilesContainer.querySelectorAll('#block-user');
    blockButtons.forEach((button) => {
        button.addEventListener('click', async (event) => {
            event.preventDefault();

            const block = button.getAttribute('data-blocked') === 'false';
            const id = parseInt(button.getAttribute('data-friendship-id'), 10);
            const userId = parseInt(button.getAttribute('data-user-id'), 10);
            if (isNaN(userId)) {
                console.error("Invalid user ID.");
                return;
            }

            try {
                console.log(`Block status: ${block}`);
                console.log(`Friendship ID: ${id}`);
                console.log(`User ID: ${userId}`);
                // Call the blockUser service function
                const response = await blockUser(id, block, userId);

                if (response && response.success) {
                    flattenedFriendships = await updateFlattendFriendships(flattenedFriendships); // Refresh the cached friendships
                    const updatedFriendship = flattenedFriendships.find((friendship) => friendship.friendId == userId);
                    if (block) {
                        button.textContent = "Unblock";
                        button.setAttribute('data-blocked', 'true');
                        button.classList.remove("btn-danger");
                        button.classList.add("btn-outline-danger");
                        if (updatedFriendship) {
                            button.setAttribute('data-friendship-id', updatedFriendship.id);
                        }
                    } else {
                        button.textContent = "Block";
                        button.setAttribute('data-blocked', 'false');
                        button.classList.remove("btn-outline-danger");
                        button.classList.add("btn-danger");
                    }
                } else {
                    console.error(`Failed to update block status: ${response.message}`);
                    alert(`Error: ${response.message}`);
                }
            } catch (error) {
                console.error("An unexpected error occurred:", error);
                alert("An unexpected error occurred. Please try again later.");
            }
        });
    });
};

/**
 * Fetches profiles using pagination and renders them to the DOM.
 * @param {HTMLElement} profilesContainer - The container to display profiles.
 * @param {HTMLElement} prevPageBtn - The "Previous" page button.
 * @param {HTMLElement} nextPageBtn - The "Next" page button.
 * @param {number} limit - Number of profiles per page.
 * @param {number} offset - The offset for pagination.
 */
const fetchAndRenderProfiles = async (
    profilesContainer,
    prevPageBtn,
    nextPageBtn,
    limit,
    offset
) => {
    profilesContainer.innerHTML = LOADING_PROFILES_HTML;

    try {
        const data = await fetchProfiles(limit, offset);
        if (data && data.getAllProfiles) {
            const profiles = data.getAllProfiles.profiles;

            renderProfiles(profiles, profilesContainer);
            prevPageBtn.disabled = offset === 0;
            nextPageBtn.disabled = profiles.length < limit;
        } else {
            throw new Error('Unable to fetch profiles.');
        }
    } catch (error) {
        console.error('Failed to fetch profiles:', error);
        profilesContainer.innerHTML = `<p class="text-danger">Failed to load profiles. Please try again later.</p>`;
    }
};




document.addEventListener('DOMContentLoaded', async () => {
    const profilesContainer = document.querySelector('#profilesContainer');
    const prevPageBtn = document.getElementById('prevPageBtn');
    const nextPageBtn = document.getElementById('nextPageBtn');
    const limit = 10;
    let currentOffset = 0;
    await fetchAndRenderProfiles(profilesContainer, prevPageBtn, nextPageBtn, limit, currentOffset);
    prevPageBtn.addEventListener('click', async () => {
        if (currentOffset > 0) {
            currentOffset -= limit;
            await fetchAndRenderProfiles(profilesContainer, prevPageBtn, nextPageBtn, limit, currentOffset);
        }
    });
    nextPageBtn.addEventListener('click', async () => {
        currentOffset += limit;
        await fetchAndRenderProfiles(profilesContainer, prevPageBtn, nextPageBtn, limit, currentOffset);
    });
});
