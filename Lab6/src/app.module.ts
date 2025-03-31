import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './app/home-component/home-component.component';
import { AboutComponent } from './app/about-component/about-component.component';
import { AlbumsComponent } from './app/albums-component/albums-component.component';
import { AlbumDetailComponent } from './app/album-detail-component/album-detail-component.component';
import { AlbumPhotosComponent } from './app/album-photos-component/album-photos-component.component';
import { HttpClientModule} from '@angular/common/http';
import { AppComponent } from './app/app.component';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent },
  { path: 'albums', component: AlbumsComponent },
  { path: 'albums/:id', component: AlbumDetailComponent },
  { path: 'albums/:id/photos', component: AlbumPhotosComponent },
  { path: '**', redirectTo: '/home' } // Wildcard route for a 404 page
];

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    AboutComponent,
    AlbumsComponent,
    AlbumDetailComponent,
    AlbumPhotosComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    RouterModule.forRoot(routes),
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }