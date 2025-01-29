import {getTournamentById, createTournamentGame, updateTournamentUser} from "./tournamentService.js";
import {fetchProfileByUserId} from "./profileservice.js";

let currentMatch = null;
let currentUser = null;
let tournamentFull = null;

async function buildTournamentView() {
    try {
        const tournament = await getTournamentById(tournamentId);
        if (!tournament || !tournament.tournament) {
            console.error('Tournament data not found');
            return;
        }
        const {name, created_at, users} = tournament.tournament;
        const tournamentNameElement = document.getElementById('tournamentName');
        if (tournamentNameElement) {
            tournamentNameElement.textContent = name;
        }
        currentUser = users.find(user => user.user_id == userId);
        if (!currentUser) {
            console.error(`User with ID ${userId} not found in tournament users.`);
            return;
        }
        const tournamentDateElement = document.getElementById('tournamentDate');
        if (tournamentDateElement) {
            tournamentDateElement.textContent = new Date(tournament.tournament.start_time).toLocaleString();
        }
        const playerCountElement = document.getElementById('playerCount');
        if (playerCountElement) {
            playerCountElement.textContent = (users ? users.length : 0) + "/" + tournament.tournament.tournament_size;
        }
        if (users.length == tournament.tournament.tournament_size) {
            tournamentFull = 1;
            matches(users);
        } else {
            tournamentFull = 0;
        }
    } catch (error) {
        console.error('Error building tournament view:', error);
    }
}


async function matches(users) {
    try {
        const roundContainer = document.getElementById('currentMatches');
        if (!roundContainer) {
            console.error('Round container not found in the DOM!');
            return;
        }
        roundContainer.innerHTML = '';
        const totalRounds = Math.max(...users.map(user => user.games_played));
        let currentRound = 0;
        while (currentRound <= totalRounds) {
            const sortedPlayers = users.sort((a, b) => a.play_order - b.play_order);
            const eligiblePlayers = sortedPlayers.filter(
                player => player.games_played >= currentRound
            );
            const currentRoundContainer = document.createElement('div');
            currentRoundContainer.className = `round-container mb-4`;
            currentRoundContainer.innerHTML = `
        <h3 class="text-center">Round ${currentRound + 1}</h3>
        <div class="d-flex flex-wrap justify-content-center round-matches"></div>
      `;
            const currentMatchesSection = currentRoundContainer.querySelector('.round-matches');
            if (eligiblePlayers.length < 2) {
                if (eligiblePlayers.length === 1) {
                    const [winner] = eligiblePlayers;
                    console.log(`Winner Found: ${winner.name}`);
                    currentRoundContainer.innerHTML += `
            <div class="winner card bg-success text-light mb-3">
              <div class="card-body">
                <h5 class="card-title text-center">Winner</h5>
                <p class="card-text text-center">${winner.user_id} (Games Played: ${winner.games_played})</p>
              </div>
            </div>
          `;
                } else {
                    console.log(`Not enough players for Round ${currentRound}. No matches possible.`);
                }
                roundContainer.appendChild(currentRoundContainer);
                currentRound++;
                continue;
            }
            let matchedPlayerIds = new Set();
            for (let i = 0; i < eligiblePlayers.length; i += 2) {
                if (i + 1 >= eligiblePlayers.length) break;

                const player1 = eligiblePlayers[i];
                const player2 = eligiblePlayers[i + 1];
                if (player1.user_id === userId || player2.user_id === userId) {
                    currentMatch = {player1, player2};
                }
                matchedPlayerIds.add(player1.id);
                matchedPlayerIds.add(player2.id);
                const matchElement = document.createElement('div');
                matchElement.className = 'match card bg-secondary text-light mb-3 me-3';
                let player1Profile = await fetchProfileByUserId(player1.user_id);
                let player2Profile = await fetchProfileByUserId(player2.user_id);
                matchElement.innerHTML = `
                    <div class="" style="display: flex; align-items: center; justify-content: center;">
                      <!-- Player 1 -->
                      <div style="display: flex; flex-direction: column; align-items: center;">
                        <div class="player" style="border-top: 2px solid red; border-bottom: 2px solid red; border-left: 2px solid red; box-shadow: -5px 0 10px red;">
                          <img src="${player1Profile.profile.avatarUrl}" alt="${player1Profile.profile.nickname}'s Avatar" style="width: 120px; height: 120px; object-fit: cover;">
                        </div>
                        <p class="nickname" style="margin-top: 8px; font-weight: bold; text-align: center;">${player1Profile.profile.nickname}</p>
                            <span>${player1.state}</span>
                    
                      </div>
                    
                      <!-- Player 2 -->
                      <div style="display: flex; flex-direction: column; align-items: center;">
                        <div class="player" style="border-top: 2px solid blue; border-bottom: 2px solid blue; border-right: 2px solid blue; box-shadow: 5px 0 10px blue;">
                          <img src="${player2Profile.profile.avatarUrl}" alt="${player2Profile.profile.nickname}'s Avatar" style="width: 120px; height: 120px; object-fit: cover;">
                        </div>
                        <p class="nickname" style="margin-top: 8px; font-weight: bold; text-align: center;">${player2Profile.profile.nickname}</p>
                        <span>${player2.state}</span>
                      </div>
                    </div>
                `;
                currentMatchesSection.appendChild(matchElement);
            }
            roundContainer.appendChild(currentRoundContainer);
            currentRound++;
        }
        if (!currentMatch) {
            console.log(`No current match found for userId: ${userId}`);
        }
    } catch (error) {
        console.error("Error generating matches:", error);
    }
}

async function playerReady() {
    // @Todo update player state to READY
    console.log("Marking player as ready...");

    try {
        if (!userId || !currentUser.id) {
            throw new Error("Missing userId or tournamentId");
        }
        const response = await updateTournamentUser(currentUser.id, userId, { state: "READY" });

        if (response.update_tournament_user?.success) {
            console.log(`Player ${userId} in tournament ${tournamentId} is now READY!`);
        } else {
            console.error("Failed to update player state to READY. Response:", response);
        }
            run();
    } catch (error) {
        console.error("Error in playerReady:", error);
    }
}

async function playerStartGame() {
    //@todo create game or check if already there and then open the game screen
    // @todo if the game finished, the winner gets the count of games_player +1
    console.log("currentOpponent", currentMatch);

    try {
        const opponentId =
            currentMatch?.player1?.user_id === userId
                ? currentMatch?.player2?.user_id
                : currentMatch?.player1?.user_id;
        if ( !tournamentId || !userId || !opponentId) {
            throw new Error("Missing required parameters (gameId, tournamentId, userId, opponentId)");
        }
        const tournamentGame = await createTournamentGame(tournamentId, currentUser.id, opponentId);
        if (tournamentGame) {
            const response = await updateTournamentUser(currentUser.id, userId, { state: "PLAYING" });
            console.log("Tournament game created successfully:", tournamentGame);
            window.location.href = "/home/game";
        } else {
            console.error("Failed to create tournament game!");
        }

    } catch (error) {
        console.error("Error in playerStartGame:", error);
    }
}

/**
 * Placeholder for opening the game's user interface after successful creation.
 */

async function playedMatches() {
    //@todo the already played matches
}

async function renderStateButton() {
    const buttonContainer = document.getElementById('stateButtonContainer');
    buttonContainer.innerHTML = '';
    if (!currentUser) {
        console.error("Current user is not defined.");
        buttonContainer.innerHTML = '<p>Current user is not available.</p>';
        return;
    }
    if (currentUser.state === 'LOST') {
        console.log(`Player ${currentUser.user_id} has lost. No button will be displayed.`);
        return;
    }
    const actionButton = document.createElement('button');
    actionButton.className = 'btn btn-primary';
    actionButton.textContent = currentUser.state === 'WAITING' ? 'Ready' : 'Play';
    actionButton.onclick = async function () {
        if (currentUser.state === 'WAITING') {
            try {
                await playerReady();
                currentUser.state = 'READY';
                actionButton.textContent = 'Play';
                console.log(`Player ${currentUser.user_id} is now ready.`);
            } catch (e) {
                console.error("Error setting player as ready:", e);
            }
        } else if (currentUser.state === 'READY') {
            try {
                await playerStartGame();
                console.log(`Player ${currentUser.user_id} is now playing.`);
            } catch (e) {
                console.error("Error starting the game:", e);
            }
        }
    };

    buttonContainer.appendChild(actionButton);
}

async function run() {
    await buildTournamentView();
    if (tournamentFull == 1)
        renderStateButton();
}

document.addEventListener("DOMContentLoaded", () => {
    run();

    setInterval(() => {
        run();
    }, 30000);
});