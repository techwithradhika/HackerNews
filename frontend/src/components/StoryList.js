import React, { useEffect, useState } from 'react';

function StoryList() {
  const [stories, setStories] = useState([]);
  const [loading, setLoading] = useState(true); 
  const [error, setError] = useState(false);

  useEffect(() => {
    fetch("http://localhost:8000/top-stories")
      .then(response => response.json())
      .then(data => {
        setStories(data);
        setLoading(false);
      })
      .catch(error => {
        console.error("Error fetching stories:", error);
        setError(true);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <p>Loading stories...</p>;
  }

  if (error) {
    return <p>Couldn't load stories. Please try again later.</p>;
  }

  if (stories.length === 0) {
    return <p>No stories available.</p>;
  }

  return (
    <ul className="story-list">
      {stories.map((story, index) => (
        <li key={index} className="story-item">
          <h3 className="story-title">
            <a href={story.url} target="_blank" rel="noopener noreferrer">{story.title}</a>
          </h3>
          <p className="story-author">Author: {story.author}</p>
          <p className="story-score">Score: {story.score}</p>
          <p className="story-time">Time: {story.time}</p>
        </li>
      ))}
    </ul>
  );
}

export default StoryList;
