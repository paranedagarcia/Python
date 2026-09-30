import React from 'react';
import Quiz from 'react-quiz-component';
import esLocale from './locales/es';

import './quiz.css';

export default function QuizComponent({quiz}) {
  const localizedQuiz = {
    ...quiz,
    appLocale: esLocale
  };
  return (
    <div className="quiz-container">
      <Quiz
        quiz={localizedQuiz}
        shuffle={false}
        shuffleAnswer={false}
        showInstantFeedback={true}
        continueTillCorrect={true}
        
        allowNavigation={true}
        enableProgressBar={true}
      />
    </div>
  );
}