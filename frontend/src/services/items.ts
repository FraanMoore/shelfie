import api from './api';
import type { Item, ItemCreate } from './types';

export const getItems = async (filters?: {
    type?: string,
    status?: string,
    is_favorite?: boolean,
    genre?: string,
}) => {
    const response = await api.get('api/items', { params: filters });
    return response.data
}

export const getItem = async (id: number) => {
    const response = await api.get(`api/items/${id}`);
    return response.data
}

export const createItem = async (data: ItemCreate) => {
    const response = await api.post('api/items', data);
    return response.data as Item;
}

export const updateItem = async (id: number, data: ItemCreate) => {
    const response = await api.put(`api/items/${id}`, data);
    return response.data as Item;
}

export const deleteItem = async (id: number) => {
    const response = await api.delete(`api/items/${id}`);
    return response.data as Item;
}