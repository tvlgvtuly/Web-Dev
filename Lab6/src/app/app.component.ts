import { Params } from 'express-serve-static-core';
import { Component, OnInit } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { ActivatedRoute } from '@angular/router';
import { AboutComponent } from './about-component/about-component.component';
import { HomeComponent } from './home-component/home-component.component';
import { AlbumsComponent } from './albums-component/albums-component.component';

@Component({
  selector: 'app-root',
  imports: [RouterOutlet,  CommonModule,  RouterLink, HomeComponent, AboutComponent, AlbumsComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent{

}
  