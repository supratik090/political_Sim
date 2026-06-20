package com.politicalsim.auth;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

import java.util.Optional;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.mindrot.jbcrypt.BCrypt;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;

class AuthControllerTest {

    private UserRepository userRepository;
    private AuthController authController;

    @BeforeEach
    void setUp() {
        userRepository = mock(UserRepository.class);
        authController = new AuthController(userRepository);
    }

    @Test
    void testRegisterSuccess() {
        AuthController.RegisterRequest req = new AuthController.RegisterRequest();
        req.setEmail("TEST@Example.com ");
        req.setName(" John Doe ");
        req.setPassword("password123");

        when(userRepository.existsByEmail("test@example.com")).thenReturn(false);
        
        User savedUser = new User("test@example.com", "John Doe", "hashedPassword");
        savedUser.setId("mock-id-123");
        when(userRepository.save(any(User.class))).thenReturn(savedUser);

        ResponseEntity<?> response = authController.register(req);

        assertEquals(HttpStatus.CREATED, response.getStatusCode());
        assertNotNull(response.getBody());
        AuthController.AuthResponse resBody = (AuthController.AuthResponse) response.getBody();
        assertEquals("mock-id-123", resBody.getId());
        assertEquals("test@example.com", resBody.getEmail());
        assertEquals("John Doe", resBody.getName());

        verify(userRepository).existsByEmail("test@example.com");
        verify(userRepository).save(any(User.class));
    }

    @Test
    void testRegisterConflict() {
        AuthController.RegisterRequest req = new AuthController.RegisterRequest();
        req.setEmail("test@example.com");
        req.setName("John Doe");
        req.setPassword("password123");

        when(userRepository.existsByEmail("test@example.com")).thenReturn(true);

        ResponseEntity<?> response = authController.register(req);

        assertEquals(HttpStatus.CONFLICT, response.getStatusCode());
        verify(userRepository, never()).save(any(User.class));
    }

    @Test
    void testLoginSuccess() {
        AuthController.LoginRequest req = new AuthController.LoginRequest();
        req.setEmail("test@example.com");
        req.setPassword("password123");

        String hashed = BCrypt.hashpw("password123", BCrypt.gensalt());
        User mockUser = new User("test@example.com", "John Doe", hashed);
        mockUser.setId("user-id-abc");

        when(userRepository.findByEmail("test@example.com")).thenReturn(Optional.of(mockUser));

        ResponseEntity<?> response = authController.login(req);

        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
        AuthController.AuthResponse resBody = (AuthController.AuthResponse) response.getBody();
        assertEquals("user-id-abc", resBody.getId());
        assertEquals("John Doe", resBody.getName());
    }

    @Test
    void testLoginFailureWrongPassword() {
        AuthController.LoginRequest req = new AuthController.LoginRequest();
        req.setEmail("test@example.com");
        req.setPassword("wrongpassword");

        String hashed = BCrypt.hashpw("password123", BCrypt.gensalt());
        User mockUser = new User("test@example.com", "John Doe", hashed);

        when(userRepository.findByEmail("test@example.com")).thenReturn(Optional.of(mockUser));

        ResponseEntity<?> response = authController.login(req);

        assertEquals(HttpStatus.UNAUTHORIZED, response.getStatusCode());
    }
}
