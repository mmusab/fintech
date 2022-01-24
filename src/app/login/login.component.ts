import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  userEmail = "";
  userPassword = "";
  userInfo = {
    "email": "",
    "password": "",
    "type": "admin"
 };
  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }
  onLogin(){
    this.http.get('http://127.0.0.1:5002/login/' + this.userEmail + '/' + this.userPassword).subscribe((response)=>{
      console.log((response as any));
      });
    console.log("in login")
  }
  onSignup(){
    this.userInfo.email = this.userEmail
    this.userInfo.password = this.userPassword
    this.http.post('http://127.0.0.1:5002/signup', this.userInfo).subscribe((response)=>{
   });
    console.log("in signup")
  }

}
