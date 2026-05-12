import api from './api';
import type { Book, BookCreate } from './types';

export const getBooks = async () => {
    const response = await api.get('/api/books');
    return response.data as Book[];
}

export const searchBooks = async (query: string) => {
    const response = await api.get('/api/books/search', { params: { q: query } });
    return response.data as Book[];
}

export const searchBook = async (id: number) => {
    const response = await api.get(`/api/books/openlibrary/${id}`);
    return response.data as Book;
}

export const getBook = async (id: number) => {
    const response = await api.get(`/api/books/${id}`);
    return response.data as Book;
}

export const createBook = async (data: BookCreate) => {
    const response = await api.post('/api/books', data);
    return response.data as Book;
}

export const updateBook = async (id: number, data: BookCreate) => {
    const response = await api.put(`/api/books/${id}`, data);
    return response.data as Book;
}

export const deleteBook = async (id: number) => {
    const response = await api.delete(`/api/books/${id}`);
    return response.data as Book;
}