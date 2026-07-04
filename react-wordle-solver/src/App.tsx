import React, { useState, useEffect } from 'react';
import './App.css';

// Define types for our Wordle game
type LetterStatus = 'correct' | 'present' | 'absent' | 'empty' | 'unused';
type Guess = {
  letter: string;
  status: LetterStatus;
}[];
type GameStatus = 'playing' | 'won' | 'lost';

const WordleInterface: React.FC = () => {
  // Game state
  const [guesses, setGuesses] = useState<Guess[]>([
    [{ letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }],
    [{ letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }],
    [{ letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }],
    [{ letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }],
    [{ letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }],
    [{ letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }, { letter: '', status: 'empty' }],
  ]);
  
  const [currentGuessIndex, setCurrentGuessIndex] = useState(0);
  const [currentLetterIndex, setCurrentLetterIndex] = useState(0);
  const [gameStatus, setGameStatus] = useState<GameStatus>('playing');
  const [targetWord, setTargetWord] = useState('APPLE'); // This would be set by your solver
  const [keyboardStatus, setKeyboardStatus] = useState<Record<string, LetterStatus>>({});
  const [isLoading, setIsLoading] = useState(false);

  // Handle keyboard input
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (gameStatus !== 'playing' || isLoading) return;

      if (e.key === 'Enter') {
        submitGuess();
      } else if (e.key === 'Backspace') {
        deleteLetter();
      } else if (/^[a-zA-Z]$/.test(e.key)) {
        addLetter(e.key.toUpperCase());
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
    };
  }, [currentGuessIndex, currentLetterIndex, gameStatus, isLoading]);

  const addLetter = (letter: string) => {
    if (currentLetterIndex < 5 && gameStatus === 'playing' && !isLoading) {
      const newGuesses = [...guesses];
      newGuesses[currentGuessIndex][currentLetterIndex] = { letter, status: 'empty' };
      setGuesses(newGuesses);
      setCurrentLetterIndex(currentLetterIndex + 1);
    }
  };

  const deleteLetter = () => {
    if (currentLetterIndex > 0 && gameStatus === 'playing' && !isLoading) {
      const newGuesses = [...guesses];
      newGuesses[currentGuessIndex][currentLetterIndex - 1] = { letter: '', status: 'empty' };
      setGuesses(newGuesses);
      setCurrentLetterIndex(currentLetterIndex - 1);
    }
  };

  // Mock function to simulate calling your Python solver
  const callSolver = async (guess: string) => {
    setIsLoading(true);
    
    // Simulate API call delay
    await new Promise(resolve => setTimeout(resolve, 500));
    
    // In a real implementation, this would be an actual API call:
    // const response = await fetch('/api/solve', {
    //   method: 'POST',
    //   headers: { 'Content-Type': 'application/json' },
    //   body: JSON.stringify({ guess })
    // });
    // const result = await response.json();
    
    // For demo purposes, we'll simulate some feedback
    const mockFeedback = [
      { letter: guess[0], status: Math.random() > 0.7 ? 'correct' : (Math.random() > 0.5 ? 'present' : 'absent') },
      { letter: guess[1], status: Math.random() > 0.7 ? 'correct' : (Math.random() > 0.5 ? 'present' : 'absent') },
      { letter: guess[2], status: Math.random() > 0.7 ? 'correct' : (Math.random() > 0.5 ? 'present' : 'absent') },
      { letter: guess[3], status: Math.random() > 0.7 ? 'correct' : (Math.random() > 0.5 ? 'present' : 'absent') },
      { letter: guess[4], status: Math.random() > 0.7 ? 'correct' : (Math.random() > 0.5 ? 'present' : 'absent') },
    ];
    
    setIsLoading(false);
    return mockFeedback;
  };

  const submitGuess = async () => {
    if (currentLetterIndex < 5 || gameStatus !== 'playing' || isLoading) return;

    const guessWord = guesses[currentGuessIndex].map(cell => cell.letter).join('');
    
    // In a real implementation, you'd validate the word against your dictionary
    // For now, we'll assume it's valid
    
    try {
      const feedback = await callSolver(guessWord);
      
      // Update the guess with feedback
      const newGuesses = [...guesses];
      feedback.forEach((item, index) => {
        newGuesses[currentGuessIndex][index] = { 
          letter: item.letter, 
          status: item.status 
        };
      });
      
      setGuesses(newGuesses);
      
      // Update keyboard status
      const newKeyboardStatus = { ...keyboardStatus };
      feedback.forEach(item => {
        if (newKeyboardStatus[item.letter]) {
          // If already marked correct, keep it correct
          if (newKeyboardStatus[item.letter] !== 'correct') {
            newKeyboardStatus[item.letter] = item.status;
          }
        } else {
          newKeyboardStatus[item.letter] = item.status;
        }
      });
      
      setKeyboardStatus(newKeyboardStatus);
      
      // Check win condition
      const isWin = feedback.every(item => item.status === 'correct');
      
      if (isWin) {
        setGameStatus('won');
      } else if (currentGuessIndex >= 5) {
        setGameStatus('lost');
      } else {
        setCurrentGuessIndex(currentGuessIndex + 1);
        setCurrentLetterIndex(0);
      }
    } catch (error) {
      console.error('Error submitting guess:', error);
      setIsLoading(false);
    }
  };

  // Render a single letter cell
  const renderCell = (guess: Guess, index: number) => {
    const letter = guess[index].letter;
    const status = guess[index].status;
    
    let cellClass = 'cell';
    if (status === 'correct') cellClass += ' correct';
    else if (status === 'present') cellClass += ' present';
    else if (status === 'absent') cellClass += ' absent';
    else if (status === 'empty') cellClass += ' empty';

    return (
      <div key={index} className={cellClass}>
        {letter}
      </div>
    );
  };

  // Render the keyboard
  const renderKeyboard = () => {
    const rows = [
      ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
      ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
      ['Enter', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'Backspace']
    ];

    return (
      <div className="keyboard">
        {rows.map((row, rowIndex) => (
          <div key={rowIndex} className="keyboard-row">
            {row.map((key) => {
              let keyClass = 'key';
              if (key === 'Enter' || key === 'Backspace') {
                keyClass += ' wide-key';
              }
              if (keyboardStatus[key]) {
                if (keyboardStatus[key] === 'correct') keyClass += ' correct';
                else if (keyboardStatus[key] === 'present') keyClass += ' present';
                else if (keyboardStatus[key] === 'absent') keyClass += ' absent';
              }

              return (
                <button 
                  key={key} 
                  className={keyClass}
                  onClick={() => {
                    if (key === 'Enter') submitGuess();
                    else if (key === 'Backspace') deleteLetter();
                    else addLetter(key);
                  }}
                  disabled={isLoading}
                >
                  {key}
                </button>
              );
            })}
          </div>
        ))}
      </div>
    );
  };

  return (
    <div className="wordle-container">
      <h1>Wordle Solver</h1>
      
      <div className="game-area">
        {/* Game grid */}
        <div className="grid">
          {guesses.map((guess, guessIndex) => (
            <div key={guessIndex} className="row">
              {guess.map((_, letterIndex) => renderCell(guess, letterIndex))}
            </div>
          ))}
        </div>

        {/* Game status messages */}
        {gameStatus === 'won' && (
          <div className="message win-message">
            Congratulations! You solved it!
          </div>
        )}
        {gameStatus === 'lost' && (
          <div className="message lose-message">
            Game over! The word was: {targetWord}
          </div>
        )}

        {/* Loading indicator */}
        {isLoading && (
          <div className="loading">Analyzing with solver...</div>
        )}

        {/* Keyboard */}
        {renderKeyboard()}
      </div>
    </div>
  );
};

export default WordleInterface;