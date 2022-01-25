import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { ProductsListComponent } from './products-list/products-list.component';

const routes: Routes = [{path:'', component: LoginComponent},
                        {path:'app-products-list', component: ProductsListComponent}];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
