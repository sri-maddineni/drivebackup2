package controllers;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class pledgecon {
    @GetMapping("/hello")
    public String getHello(){
        return "Hello from spring";
    }
}
