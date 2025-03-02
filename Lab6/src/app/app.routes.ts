import { Routes } from '@angular/router';
import { HomeComponent } from './home-component/home-component.component';
import { AboutComponent } from './about-component/about-component.component';
import { AlbumsComponent } from './albums-component/albums-component.component';
import { AlbumDetailComponent } from './album-detail-component/album-detail-component.component';
import { AlbumPhotosComponent } from './album-photos-component/album-photos-component.component';

export const routes: Routes = [
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent, title: 'HomePage'},
    {path: 'about', component: AboutComponent, title: 'About'},
    {path: 'albums', component: AlbumsComponent, title: 'Albums'},
    {path: 'albums/:id', component: AlbumDetailComponent, title: 'AlbumDetail'},
    {path: 'albums/:id/photos', component: AlbumPhotosComponent, title: 'AlbumPhotos'}
];