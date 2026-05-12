import api from './api';
import type { Serie, SerieCreate } from './types';

export const getSeries = async () => {
    const response = await api.get('/api/series');
    return response.data as Serie[];
}

export const searchSeries = async (query: string) => {
    const response = await api.get('/api/series/search', { params: { q: query } });
    return response.data as Serie[];
}

export const getSerie = async (id: number) => {
    const response = await api.get(`/api/series/${id}`);
    return response.data as Serie;
}

export const getSerieSeasons = async (id: number) => {
    const response = await api.get(`/api/series/${id}/seasons`);
    return response.data;
}

export const createSerie = async (data: SerieCreate) => {
    const response = await api.post('/api/series', data);
    return response.data as Serie;
}

export const updateSerie = async (id: number, data: SerieCreate) => {
    const response = await api.put(`/api/series/${id}`, data);
    return response.data as Serie;
}

export const deleteSerie = async (id: number) => {
    const response = await api.delete(`/api/series/${id}`);
    return response.data as Serie;
}