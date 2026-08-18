package com.example.testtables

import android.app.Activity
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import kotlin.random.Random

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            QuizApp()
        }
    }
}

@Composable
fun QuizApp() {
    val activity = LocalContext.current as Activity

    var question by remember { mutableStateOf("") }
    var answer by remember { mutableStateOf(0) }
    var userInput by remember { mutableStateOf("") }
    var feedback by remember { mutableStateOf("Press Start") }
    var total by remember { mutableStateOf(0) }
    var correct by remember { mutableStateOf(0) }

    // ✅ NEW: dialog state
    var showExitDialog by remember { mutableStateOf(false) }

    fun generateQuestion() {
        val a = Random.nextInt(2, 10)
        val b = Random.nextInt(2, 10)
        question = "$a x $b"
        answer = a * b
        userInput = ""
    }

    // ✅ EXIT DIALOG
    if (showExitDialog) {
        val accuracy = if (total > 0) (correct.toFloat() / total) * 100 else 0f

        AlertDialog(
            onDismissRequest = { showExitDialog = false },
            title = { Text("Exit Quiz") },
            text = {
                Column {
                    Text("📊 Final Stats")
                    Spacer(modifier = Modifier.height(8.dp))
                    Text("Total: $total")
                    Text("Correct: $correct")
                    Text("Accuracy: ${"%.1f".format(accuracy)}%")
                }
            },
            confirmButton = {
                Button(onClick = {
                    activity.finish()
                }) {
                    Text("Exit")
                }
            },
            dismissButton = {
                Button(onClick = {
                    showExitDialog = false
                }) {
                    Text("Cancel")
                }
            }
        )
    }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp)
    ) {
        Text("Times Tables Quiz (2–9)", style = MaterialTheme.typography.titleLarge)

        Spacer(modifier = Modifier.height(16.dp))

        Text(question, style = MaterialTheme.typography.headlineMedium)

        Spacer(modifier = Modifier.weight(1f))

        TextField(
            value = userInput,
            onValueChange = { userInput = it },
            label = { Text("Your answer") },
            modifier = Modifier.fillMaxWidth()
        )

        Spacer(modifier = Modifier.height(12.dp))

        Row(
            modifier = Modifier.fillMaxWidth(),
            horizontalArrangement = Arrangement.Center
        ) {
            Button(onClick = {
                generateQuestion()
                feedback = ""
            }) {
                Text("Start")
            }

            Spacer(modifier = Modifier.width(12.dp))

            Button(onClick = {
                val input = userInput.toIntOrNull()
                if (input != null) {
                    total++
                    if (input == answer) {
                        feedback = "✅ Correct!"
                        correct++
                    } else {
                        feedback = "❌ Wrong! Answer = $answer"
                    }
                    generateQuestion()
                } else {
                    feedback = "⚠️ Enter a number"
                }
            }) {
                Text("Submit")
            }

            Spacer(modifier = Modifier.width(12.dp))

            // ✅ UPDATED EXIT BUTTON
            Button(onClick = {
                showExitDialog = true
            }) {
                Text("Exit")
            }
        }

        Spacer(modifier = Modifier.weight(3f))

        Text(feedback, style = MaterialTheme.typography.bodyLarge)

        Spacer(modifier = Modifier.height(16.dp))

        if (total > 0) {
            val accuracy = (correct.toFloat() / total) * 100

            Text("📊 Stats", style = MaterialTheme.typography.titleMedium)
            Text("Total: $total")
            Text("Correct: $correct")
            Text("Accuracy: ${"%.1f".format(accuracy)}%")
        }
    }
}