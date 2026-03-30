package com.example.mathsquiz

import android.app.Activity
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import kotlin.math.PI
import kotlin.math.abs
import kotlin.random.Random

class MainActivity : ComponentActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent { QuizApp() }
    }

    @Composable
    fun QuizApp() {
        val activity = LocalContext.current as Activity

        var question by remember { mutableStateOf("") }
        var answer by remember { mutableStateOf<Any>(0) }
        var type by remember { mutableStateOf("") }
        var input by remember { mutableStateOf("") }
        var result by remember { mutableStateOf("") }
        var total by remember { mutableStateOf(0) }
        var correct by remember { mutableStateOf(0) }
        var showExitDialog by remember { mutableStateOf(false) }

        fun gcd(a: Int, b: Int): Int {
            return if (b == 0) a else gcd(b, a % b)
        }

        fun generateQuestion() {
            val types = listOf("times","fraction","percent","hcf","lcd","rectangle","triangle","circle")
            type = types.random()

            when (type) {
                "times" -> {
                    val a = Random.nextInt(2,10)
                    val b = Random.nextInt(2,10)
                    question = "$a × $b = ?"
                    answer = a * b
                }

                "fraction" -> {
                    val n1 = Random.nextInt(1,10)
                    val d1 = Random.nextInt(1,10)
                    val n2 = Random.nextInt(1,10)
                    val d2 = Random.nextInt(1,10)
                    val op = listOf("+","-","*","/").random()

                    val num: Int
                    val den: Int

                    when (op) {
                        "+" -> { num = n1*d2 + n2*d1; den = d1*d2 }
                        "-" -> { num = n1*d2 - n2*d1; den = d1*d2 }
                        "*" -> { num = n1*n2; den = d1*d2 }
                        else -> { num = n1*d2; den = d1*n2 }
                    }

                    question = "$n1/$d1 $op $n2/$d2 = ?"
                    answer = Pair(num, den)
                }

                "percent" -> {
                    val percent = listOf(10,20,25,50).random()
                    val number = Random.nextInt(10,201)
                    question = "What is $percent% of $number?"
                    answer = number * percent / 100.0
                }

                "hcf" -> {
                    val a = Random.nextInt(2,50)
                    val b = Random.nextInt(2,50)
                    question = "HCF of $a and $b?"
                    answer = gcd(a,b)
                }

                "lcd" -> {
                    val a = Random.nextInt(2,12)
                    val b = Random.nextInt(2,12)
                    question = "LCD of $a and $b?"
                    answer = abs(a*b)/gcd(a,b)
                }

                "rectangle" -> {
                    val l = Random.nextInt(2,20)
                    val w = Random.nextInt(2,20)
                    if (Random.nextBoolean()) {
                        question = "Rectangle $l x $w area?"
                        answer = l*w
                    } else {
                        question = "Rectangle $l x $w perimeter?"
                        answer = 2*(l+w)
                    }
                }

                "triangle" -> {
                    val b = Random.nextInt(2,20)
                    val h = Random.nextInt(2,20)
                    question = "Triangle base $b height $h area?"
                    answer = 0.5*b*h
                }

                else -> {
                    val r = Random.nextInt(1,10)
                    question = "Circle radius $r area (2dp)?"
                    answer = PI*r*r
                }
            }

            input = ""
            result = ""
        }

        fun checkAnswer() {
            if (input.lowercase() == "q") {
                showExitDialog = true
                return
            }

            total++

            try {
                when (type) {
                    "fraction" -> {
                        val parts = input.split("/")
                        val user = parts[0].toDouble() / parts[1].toDouble()
                        val ans = answer as Pair<Int,Int>
                        val real = ans.first.toDouble()/ans.second

                        if (abs(user - real) < 0.01) {
                            correct++
                            result = "✅ Correct"
                        } else {
                            result = "❌ Answer = ${ans.first}/${ans.second}"
                        }
                    }

                    else -> {
                        val user = input.toDouble()
                        val ans = (answer as Number).toDouble()

                        if (abs(user - ans) < 0.01) {
                            correct++
                            result = "✅ Correct"
                        } else {
                            result = "❌ Answer = %.2f".format(ans)
                        }
                    }
                }
            } catch (e: Exception) {
                result = "⚠️ Invalid input"
            }

            generateQuestion()
        }

        LaunchedEffect(Unit) {
            generateQuestion()
        }

        // Exit dialog with stats
        if (showExitDialog) {
            val acc = if (total > 0) (correct * 100 / total) else 0

            AlertDialog(
                onDismissRequest = { showExitDialog = false },
                title = { Text("Exit Quiz") },
                text = {
                    Column {
                        Text("📊 Final Stats")
                        Spacer(modifier = Modifier.height(8.dp))
                        Text("Total: $total")
                        Text("Correct: $correct")
                        Text("Accuracy: $acc%")
                    }
                },
                confirmButton = {
                    Button(onClick = { activity.finish() }) {
                        Text("Exit")
                    }
                },
                dismissButton = {
                    Button(onClick = { showExitDialog = false }) {
                        Text("Cancel")
                    }
                }
            )
        }

        Column(
            modifier = Modifier.fillMaxSize().padding(24.dp),
            horizontalAlignment = Alignment.CenterHorizontally,
            verticalArrangement = Arrangement.Center
        ) {

            Text(question)

            Spacer(modifier = Modifier.height(16.dp))

            OutlinedTextField(
                value = input,
                onValueChange = { input = it },
                label = { Text("Answer") }
            )

            Spacer(modifier = Modifier.height(16.dp))

            // ✅ SIDE-BY-SIDE BUTTONS
            Row(modifier = Modifier.fillMaxWidth()) {

                Button(
                    onClick = { checkAnswer() },
                    modifier = Modifier.weight(1f)
                ) {
                    Text("Submit")
                }

                Spacer(modifier = Modifier.width(12.dp))

                Button(
                    onClick = { showExitDialog = true },
                    modifier = Modifier.weight(1f)
                ) {
                    Text("Quit")
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            Text(result)

            Spacer(modifier = Modifier.height(16.dp))

            val acc = if (total>0) (correct*100/total) else 0
            Text("Score: $correct/$total ($acc%)")
        }
    }
}