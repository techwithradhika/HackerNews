import React, { useEffect, useState } from 'react';
import './App.css';
import StoryList from './components/StoryList';

function App() {
  const [stories, setStories] = useState([]);

  useEffect(() => {
    fetch('http://localhost:8000/top-stories') 
      .then((response) => response.json())
      .then((data) => setStories(data))
      .catch((error) => console.error('Error fetching stories:', error));
  }, []);

  return (
    <div className="container">
      <h1>HackerNews Top 10 New Stories</h1>
      <StoryList stories={stories} />
    </div>
  );
}

export default App;
