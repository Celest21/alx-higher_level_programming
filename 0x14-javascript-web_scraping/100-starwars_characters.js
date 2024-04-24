#!/usr/bin/node

const fetch = require('node-fetch');
const process = require('process');

async function getCharacters(movieId) {
    try {
        const response = await fetch(`https://swapi-api.alx-tools.com/films/${movieId}/`);
        if (!response.ok) {
            throw new Error(`Failed to fetch movie data: ${response.status}`);
        }
        const data = await response.json();
        const characters = data.characters;
        for (const characterUrl of characters) {
            const characterResponse = await fetch(characterUrl);
            if (!characterResponse.ok) {
                throw new Error(`Failed to fetch character data: ${characterResponse.status}`);
            }
            const characterData = await characterResponse.json();
            console.log(characterData.name);
        }
    } catch (error) {
        console.error(error.message);
        process.exit(1);
    }
}

if (process.argv.length < 3) {
    console.error("Usage: node script.js <movie_id>");
    process.exit(1);
}

const movieId = process.argv[2];
getCharacters(movieId);

