package com.politicalsim.auth;

import org.mindrot.jbcrypt.BCrypt;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Map;
import java.util.Optional;

@RestController
@RequestMapping("/api/auth")
public class AuthController {

    private final UserRepository userRepository;
    private final EmailService emailService;

    @Autowired
    public AuthController(UserRepository userRepository, EmailService emailService) {
        this.userRepository = userRepository;
        this.emailService = emailService;
    }

    public AuthController(UserRepository userRepository) {
        this(userRepository, null);
    }

    @PostMapping("/register")
    public ResponseEntity<?> register(@RequestBody RegisterRequest request) {
        if (request.getEmail() == null || request.getEmail().isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Email is required"));
        }
        if (request.getPassword() == null || request.getPassword().isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Password is required"));
        }
        if (request.getName() == null || request.getName().isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Name is required"));
        }

        String email = request.getEmail().trim().toLowerCase();
        if (userRepository.existsByEmail(email)) {
            return ResponseEntity.status(HttpStatus.CONFLICT).body(Map.of("error", "Email is already registered"));
        }

        String hashedPassword = BCrypt.hashpw(request.getPassword(), BCrypt.gensalt());
        User user = new User(email, request.getName().trim(), hashedPassword);
        User savedUser = userRepository.save(user);

        return ResponseEntity.status(HttpStatus.CREATED).body(new AuthResponse(
                savedUser.getId(),
                savedUser.getEmail(),
                savedUser.getName()
        ));
    }

    @PostMapping("/login")
    public ResponseEntity<?> login(@RequestBody LoginRequest request) {
        if (request.getEmail() == null || request.getEmail().isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Email or User ID is required"));
        }
        if (request.getPassword() == null || request.getPassword().isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Password is required"));
        }

        String input = request.getEmail().trim();
        Optional<User> userOpt = userRepository.findByEmail(input.toLowerCase());
        if (userOpt.isEmpty()) {
            userOpt = userRepository.findById(input);
        }
        if (userOpt.isEmpty()) {
            userOpt = userRepository.findByNameIgnoreCase(input);
        }

        if (userOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(Map.of("error", "Invalid email/user ID or password"));
        }

        User user = userOpt.get();
        if (!BCrypt.checkpw(request.getPassword(), user.getPasswordHash())) {
            return ResponseEntity.status(HttpStatus.UNAUTHORIZED).body(Map.of("error", "Invalid email/user ID or password"));
        }

        return ResponseEntity.ok(new AuthResponse(
                user.getId(),
                user.getEmail(),
                user.getName()
        ));
    }

    @PostMapping("/forgot-password")
    public ResponseEntity<?> forgotPassword(@RequestBody Map<String, String> request) {
        String email = request.get("email");
        if (email == null || email.isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Email is required"));
        }

        String normalizedEmail = email.trim().toLowerCase();
        Optional<User> userOpt = userRepository.findByEmail(normalizedEmail);
        if (userOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(Map.of("error", "No account found with this email address"));
        }

        User user = userOpt.get();
        String otp = String.format("%06d", new java.security.SecureRandom().nextInt(1000000));
        long expiry = System.currentTimeMillis() + (15 * 60 * 1000); // 15 minutes validity

        user.setResetOtp(otp);
        user.setResetOtpExpiry(expiry);
        userRepository.save(user);

        if (emailService != null) {
            emailService.sendOtpEmail(normalizedEmail, otp);
        }

        return ResponseEntity.ok(Map.of(
            "message", "OTP sent successfully to " + normalizedEmail,
            "otp", otp,
            "email", normalizedEmail
        ));
    }

    @PostMapping("/reset-password")
    public ResponseEntity<?> resetPassword(@RequestBody Map<String, String> request) {
        String email = request.get("email");
        String otp = request.get("otp");
        String newPassword = request.get("newPassword");

        if (email == null || email.isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "Email is required"));
        }
        if (otp == null || otp.isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "OTP code is required"));
        }
        if (newPassword == null || newPassword.isBlank()) {
            return ResponseEntity.badRequest().body(Map.of("error", "New password is required"));
        }

        String normalizedEmail = email.trim().toLowerCase();
        Optional<User> userOpt = userRepository.findByEmail(normalizedEmail);
        if (userOpt.isEmpty()) {
            return ResponseEntity.status(HttpStatus.NOT_FOUND).body(Map.of("error", "User not found"));
        }

        User user = userOpt.get();
        if (user.getResetOtp() == null || !user.getResetOtp().trim().equals(otp.trim())) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", "Invalid OTP code. Please check and try again."));
        }

        if (user.getResetOtpExpiry() == null || System.currentTimeMillis() > user.getResetOtpExpiry()) {
            return ResponseEntity.status(HttpStatus.BAD_REQUEST).body(Map.of("error", "OTP has expired. Please request a new OTP."));
        }

        String hashedPassword = BCrypt.hashpw(newPassword, BCrypt.gensalt());
        user.setPasswordHash(hashedPassword);
        user.setResetOtp(null);
        user.setResetOtpExpiry(null);
        userRepository.save(user);

        return ResponseEntity.ok(Map.of("message", "Password reset successfully! You can now log in with your new password."));
    }

    public static class RegisterRequest {
        private String email;
        private String name;
        private String password;

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }

        public String getPassword() {
            return password;
        }

        public void setPassword(String password) {
            this.password = password;
        }
    }

    public static class LoginRequest {
        private String email;
        private String password;

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getPassword() {
            return password;
        }

        public void setPassword(String password) {
            this.password = password;
        }
    }

    public static class AuthResponse {
        private String id;
        private String email;
        private String name;

        public AuthResponse(String id, String email, String name) {
            this.id = id;
            this.email = email;
            this.name = name;
        }

        public String getId() {
            return id;
        }

        public void setId(String id) {
            this.id = id;
        }

        public String getEmail() {
            return email;
        }

        public void setEmail(String email) {
            this.email = email;
        }

        public String getName() {
            return name;
        }

        public void setName(String name) {
            this.name = name;
        }
    }
}
