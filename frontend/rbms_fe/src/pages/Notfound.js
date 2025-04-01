import React from 'react';
import { useNavigate } from 'react-router-dom';

export function Notfound (){
  const navigate = useNavigate();

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>404 - Page Not Found</h1>
      <p style={styles.text}>
        Oops! The page you're looking for doesn't exist.
      </p>
      <button style={styles.button} onClick={() => navigate('/')}>
        Go Home
      </button>
    </div>
  );
};

const styles = {
  container: {
    textAlign: 'center',
    marginTop: '10%',
    fontFamily: 'Arial, sans-serif',
    backgroundColor:" #FFFFFF",
    backgroundImage: "linear-gradient(180deg, #FFFFFF 0%, #6284FF 50%, #FF0000 100%)"
   
  },
  heading: {
    fontSize: '3rem',
    color: '#ff4d4d',
  },
  text: {
    fontSize: '1.2rem',
    color: '#333',
  },
  button: {
    marginTop: '20px',
    padding: '10px 20px',
    fontSize: '1rem',
    cursor: 'pointer',
    border: 'none',
    backgroundColor: '#007bff',
    color: 'white',
    borderRadius: '5px',
  }
}

export default Notfound;
