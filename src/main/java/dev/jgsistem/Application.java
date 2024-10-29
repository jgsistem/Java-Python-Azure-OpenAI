package dev.jgsistem;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

public class Application {

    public static void main(String[] args) throws IOException, InterruptedException {
        var apiKey = "";
        var body = """
                {
                    "model": "gpt-4o",
                    "messages": [
                        {
                            "role": "system",
                            "content":  "Eres un asistente virtual del Master en Tecnologia de la Informacion. Tu objetivo es responder todas las dudas de los integrantes del grupo. Las respuestas a los integrantes del grupo deben ser amables e incluir emojis apropiados. Tus respuestas deben estar en el mismo idioma que la pregunta del usuario."
                        },
                        {
                            "role": "user",
                            "content": "De que tema puedo hablar en el master de tecnologia de la informacion?."
                        }
                    ]
                }""";

        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create("https://demo17-openai-022.openai.azure.com/openai/deployments/gpt-4/chat/completions?api-version=2024-08-01-preview&api-key=" + apiKey))
                .header("Content-Type", "application/json")
                .POST(HttpRequest.BodyPublishers.ofString(body))
                .build();

        var client = HttpClient.newHttpClient();
        var response = client.send(request, HttpResponse.BodyHandlers.ofString());
        System.out.println(response.body());
    }



}
