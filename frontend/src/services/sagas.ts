import api from './api';
import type { Saga, SagaCreate } from './types';

export const getSagas = async () => {
    const response = await api.get('/api/sagas');
    return response.data as Saga[];
}

export const getSaga = async (id: number) => {
    const response = await api.get(`/api/sagas/${id}`);
    return response.data as Saga;
}

export const createSaga = async (data: SagaCreate) => {
    const response = await api.post('/api/sagas', data);
    return response.data as Saga;
}

export const updateSaga = async (id: number, data: SagaCreate) => {
    const response = await api.put(`/api/sagas/${id}`, data);
    return response.data as Saga;
}

export const deleteSaga = async (id: number) => {
    const response = await api.delete(`/api/sagas/${id}`);
    return response.data as Saga;
}