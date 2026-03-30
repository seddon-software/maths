package com.example.timestablesquiz

import android.os.Bundle
import android.os.CountDownTimer
import android.widget.*
import androidx.appcompat.app.AppCompatActivity
import kotlin.random.Random

class MainActivity : AppCompatActivity() {

    private lateinit var questionText: TextView
    private lateinit var inputAnswer: EditText
    private lateinit var submitButton: Button
    private lateinit var resultText: TextView
    private lateinit var statsText: TextView

    private var correct = 0
    private var total = 0
    private var answer = 0

    private var timer: CountDownTimer? = null

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        // Create UI programmatically
        val layout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(40, 40, 40, 40)
        }

        questionText = TextView(this)
        inputAnswer = EditText(this).apply {
            hint = "Enter answer"
        }
        submitButton = Button(this).apply {
            text = "Submit"
        }
        resultText = TextView(this)
        statsText = TextView(this)

        layout.addView(questionText)
        layout.addView(inputAnswer)
        layout.addView(submitButton)
        layout.addView(resultText)
        layout.addView(statsText)

        setContentView(layout)

        generateQuestion()

        submitButton.setOnClickListener {
            checkAnswer()
        }
    }

    private fun generateQuestion() {
        val a = Random.nextInt(2, 10)
        val b = Random.nextInt(2, 10)
        answer = a * b

        questionText.text = "$a x $b = ?"
        inputAnswer.text.clear()
        resultText.text = ""

        startTimer()
    }

    private fun startTimer() {
        timer?.cancel()

        timer = object : CountDownTimer(10000, 1000) {
            override fun onTick(millisUntilFinished: Long) {
                statsText.text = "Time: ${millisUntilFinished / 1000}s"
            }

            override fun onFinish() {
                total++
                resultText.text = "⏰ Time's up! Answer = $answer"
                updateStats()
                generateQuestion()
            }
        }.start()
    }

    private fun checkAnswer() {
        val userInput = inputAnswer.text.toString()

        if (userInput.lowercase() == "q") {
            finish()
            return
        }

        val userAnswer = userInput.toIntOrNull()

        if (userAnswer == null) {
            resultText.text = "⚠️ Enter a number"
            return
        }

        timer?.cancel()
        total++

        if (userAnswer == answer) {
            correct++
            resultText.text = "✅ Correct!"
        } else {
            resultText.text = "❌ Wrong! Answer = $answer"
        }

        updateStats()
        generateQuestion()
    }

    private fun updateStats() {
        val accuracy = if (total > 0) (correct * 100.0 / total) else 0.0
        statsText.text =
            "Total: $total | Correct: $correct | Accuracy: %.1f%%".format(accuracy)
    }
}