import api from './api';
import type { Movie, MovieCreate } from './types';

export const getMovies = async () => {
    const response = await api.get('/api/movies');
    return response.data as Movie[];
}

export const searchMovies = async (query: string) => {
    const response = await api.get('/api/movies/search', { params: { q: query } });
    return response.data as Movie[];
}

export const getMovie = async (id: number) => {
    const response = await api.get(`/api/movies/${id}`);
    return response.data as Movie;
}

export const createMovie = async (data: MovieCreate) => {
    const response = await api.post('/api/movies', data);
    return response.data as Movie;
}

export const updateMovie = async (id: number, data: MovieCreate) => {
    const response = await api.put(`/api/movies/${id}`, data);
    return response.data as Movie;
}

export const deleteMovie = async (id: number) => {
    const response = await api.delete(`/api/movies/${id}`);
    return response.data as Movie;
}