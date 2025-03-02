export interface Album {
    userId: number;
    id: number;
    title: string;
}

export interface Photos{
    albumId: number;
    title: string;
    url: string;
}