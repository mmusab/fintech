import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  user:any;
  userEmail = "";
  userPassword = "";
  userInfo = {
    "email": "",
    "password": "",
    "type": "admin"
 };
  constructor(private http: HttpClient, private router : Router) { }

  ngOnInit(): void {
  }
  onLogin(){
    this.http.get('http://127.0.0.1:5002/login/' + this.userEmail + '/' + this.userPassword).subscribe((response)=>{
      this.user = (response as any)
      if(this.user['authorized'] == "True"){
        this.router.navigate(['/app-products-list']);
      }
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
