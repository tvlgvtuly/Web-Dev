import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Album } from '../app/models';
import { Photos } from '../app/models';
import { HttpClientModule } from '@angular/common/http';



@Injectable({
  providedIn: 'root'
})
export class AlbumsService {
  private apiUrl = 'https://jsonplaceholder.typicode.com/albums';
  

  constructor(private http: HttpClient) { }


  createAlbum(album: Album): Observable <Album>{
    return this.http.post<Album>(this.apiUrl, album);

  }

  getAlbums(): Observable<Album[]> {
    return this.http.get<Album[]>(this.apiUrl);
  }

  getAlbum(id: number): Observable<Album> {
    return this.http.get<Album>(`${this.apiUrl}/${id}`);
  }

  updateAlbum(album: Album): Observable<Album> {
    return this.http.put<Album>(`${this.apiUrl}/${album.id}`, album);
  }

  deleteAlbum(id: number){
    return this.http.delete(`${this.apiUrl}/${id}`);
  }

  getAlbumPhotos(albumId: number){
    return this.http.get<Photos[]>(`https://jsonplaceholder.typicode.com/albums/${albumId}/photos`)
  }
}