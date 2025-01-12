package org.example;

import org.graalvm.polyglot.Context;
import org.graalvm.python.embedding.utils.GraalPyResources;

public class Main {
    public static void main(String[] args) {
        try (Context context = GraalPyResources.contextBuilder().build()) {
            String src = """
           from termcolor import colored
           colored_text = colored("hello java", "red", attrs=["reverse", "blink"])
           print(colored_text)
           """;
            context.eval("python", src);
        }
    }
}