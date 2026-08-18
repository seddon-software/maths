package com.example.testtables

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import kotlin.random.Random

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)

        setContent {
            QuizApp()
        }
    }

    @Composable
    fun QuizApp() {
        var question by remember { mutableStateOf("") }
        var answer by remember { mutableStateOf(0) }
        var userInput by remember { mutableStateOf("") }
        var result by remember { mutableStateOf("") }
        var total by remember { mutableStateOf(0) }
        var correct by remember { mutableStateOf(0) }
        var gameOver by remember { mutableStateOf(false) }

        val activity = this@MainActivity

        fun generateQuestion() {
            val a = Random.nextInt(2, 10)
            val b = Random.nextInt(2, 10)
            question = "$a x $b"
            answer = a * b
            userInput = ""
            result = ""
        }

        fun checkAnswer() {
            if (userInput.lowercase() == "q") {
                gameOver = true
                return
            }

            total++

            val input = userInput.toIntOrNull()
            if (input == null) {
                result = "⚠️ Enter a number"
            } else if (input == answer) {
                correct++
                result = "✅ Correct!"
            } else {
                result = "❌ Wrong! Answer = $answer"
            }

            generateQuestion()
        }

        LaunchedEffect(Unit) {
            generateQuestion()
        }

        if (gameOver) {
            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {
                val accuracy = if (total > 0) (correct * 100 / total) else 0

                Text("📊 Final Stats", style = MaterialTheme.typography.headlineMedium)
                Spacer(modifier = Modifier.height(16.dp))
                Text("Total: $total")
                Text("Correct: $correct")
                Text("Accuracy: $accuracy%")

                Spacer(modifier = Modifier.height(20.dp))

                Button(onClick = { activity.finish() }) {
                    Text("Exit App")
                }
            }

        } else {

            Column(
                modifier = Modifier
                    .fillMaxSize()
                    .padding(24.dp),
                horizontalAlignment = Alignment.CenterHorizontally,
                verticalArrangement = Arrangement.Center
            ) {

                Text(text = question, style = MaterialTheme.typography.headlineMedium)

                Spacer(modifier = Modifier.height(16.dp))

                OutlinedTextField(
                    value = userInput,
                    onValueChange = { userInput = it },
                    label = { Text("Your answer") }
                )

                Spacer(modifier = Modifier.height(16.dp))

                Button(onClick = { checkAnswer() }) {
                    Text("Submit")
                }

                Spacer(modifier = Modifier.height(8.dp))

                Button(onClick = { gameOver = true }) {
                    Text("Quit")
                }

                Spacer(modifier = Modifier.height(16.dp))

                Text(text = result)

                Spacer(modifier = Modifier.height(16.dp))

                val accuracy = if (total > 0) (correct * 100 / total) else 0
                Text("Total: $total  |  Correct: $correct  |  Accuracy: $accuracy%")
            }
        }
    }
}