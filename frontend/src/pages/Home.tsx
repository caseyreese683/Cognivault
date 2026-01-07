

















import React from "react";
import LoginWallet from "../components/LoginWallet";

export default function Home() {
  return (
    <div className="p-10 text-center">
      <h1 className="text-4xl font-bold mb-4">Cognivault</h1>
      <p className="text-gray-500 mb-8">Private AI Knowledge Vault</p>
      <LoginWallet />
    </div>
  );
}

