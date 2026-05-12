export interface Item {
    id: number,
    type: 'book' | 'movie' | 'serie',
    status: 'to_watch' | 'watching' | 'watched',
    emision_status: 'not_emited' | 'emiting' | 'emited',
    is_favorite: boolean,
}

export interface ItemCreate {
    type: 'book' | 'movie' | 'serie',
    status: 'to_watch' | 'watching' | 'watched',
    emision_status: 'not_emited' | 'emiting' | 'emited',
    is_favorite: boolean,
}
export interface Book {
    id: number
    title: string
    author: string
    year: number
    cover?: string
}
export interface BookCreate {
    title: string
    author: string
    year: number
    cover?: string
}

export interface Movie {
    id: number
    title: string
    director: string
    year: number
    cover?: string
}

export interface MovieCreate {
    title: string
    director: string
    year: number
    cover?: string
}

export interface Serie {
    id: number
    title: string
    director: string
    year: number
    cover?: string
    has_seasons: boolean
}
export interface SerieCreate {
    title: string
    director: string
    year: number
    cover?: string
    has_seasons: boolean
}

export interface Season {
    id: number
    season_name: string
    year: number
    cover?: string
    director: string
    order: number
}

export interface SeasonCreate {
    season_name: string
    year: number
    cover?: string
    director: string
    order: number
}

export interface Saga {
    id: number
    name: string
    type: string
    cover?: string
}

export interface SagaCreate {
    name: string
    type: string
    cover?: string
}

export interface Comment {
    id: number
    item_id: number
    content: string
    created_at: Date
}

export interface CommentCreate {
    content: string
}

export interface Genre {
    id: number
    name: string
}

export interface ItemGenre {
    item_id: number
    genre_id: number
}