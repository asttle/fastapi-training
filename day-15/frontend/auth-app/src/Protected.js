import React, {useEffect, useState} from "react";
import {useNavigate} from "react-router-dom";

function ProtectPage() {
  const [message, setMessage] = useState("");
  const navigate = useNavigate();

  useEffect(() => {
    const verifyToken = async () => {
      const token = localStorage.getItem("token");
      console.log("Token:", token); // Debugging line
      try {
        const response = await fetch(`http://localhost:8000/verify-token/${token}`);
        if(!response.ok) {
          throw new Error("Token verification failed");
        }
      } catch (error) {
        console.error("Error verifying token:", error);
        localStorage.removeItem("token");
        navigate("/");
      }
    }
    verifyToken();
  }, [navigate]);

  return (
    <div>
      <h2>Protected Page</h2>
      <p>{message}</p>
    </div>
  );
}

export default ProtectPage;