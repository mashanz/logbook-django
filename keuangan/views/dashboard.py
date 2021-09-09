from django.shortcuts import render, redirect

from ..models import *

def dashboard(request):
    total_01 = 0
    total_02 = 0
    total_03 = 0
    total_04 = 0
    total_05 = 0
    total_06 = 0
    total_07 = 0
    total_08 = 0
    total_09 = 0
    total_10 = 0
    total_11 = 0
    total_12 = 0

    html_template = 'keuangan/dashboard.html'
    cashflow = CashFlow.objects.all().order_by('-tanggal').filter(tanggal__year = request.GET.get('tahun', 2021))
    
    cashflow_01 = cashflow.filter(tanggal__month = 1)
    cashflow_02 = cashflow.filter(tanggal__month = 2)
    cashflow_03 = cashflow.filter(tanggal__month = 3)
    cashflow_04 = cashflow.filter(tanggal__month = 4)
    cashflow_05 = cashflow.filter(tanggal__month = 5)
    cashflow_06 = cashflow.filter(tanggal__month = 6)
    cashflow_07 = cashflow.filter(tanggal__month = 7)
    cashflow_08 = cashflow.filter(tanggal__month = 8)
    cashflow_09 = cashflow.filter(tanggal__month = 9)
    cashflow_10 = cashflow.filter(tanggal__month = 10)
    cashflow_11 = cashflow.filter(tanggal__month = 11)
    cashflow_12 = cashflow.filter(tanggal__month = 12)

    for cash in cashflow_01:
        total_01 += cash.harga_total
    for cash in cashflow_02:
        total_02 += cash.harga_total
    for cash in cashflow_03:
        total_03 += cash.harga_total
    for cash in cashflow_04:
        total_04 += cash.harga_total
    for cash in cashflow_05:
        total_05 += cash.harga_total
    for cash in cashflow_06:
        total_06 += cash.harga_total
    for cash in cashflow_07:
        total_07 += cash.harga_total
    for cash in cashflow_08:
        total_08 += cash.harga_total
    for cash in cashflow_09:
        total_09 += cash.harga_total
    for cash in cashflow_10:
        total_10 += cash.harga_total
    for cash in cashflow_11:
        total_11 += cash.harga_total
    for cash in cashflow_12:
        total_12 += cash.harga_total

    context = {
        'year': request.GET.get('tahun', '2021'),
        'cashflow': [
            {
                "no": 1,
                "bulan": "Januari",
                "total": total_01
            },
            {
                "no": 2,
                "bulan": "Februari",
                "total": total_02
            },
            {
                "no": 3,
                "bulan": "Maret",
                "total": total_03
            },
            {
                "no": 4,
                "bulan": "April",
                "total": total_04
            },
            {
                "no": 5,
                "bulan": "Mei",
                "total": total_05
            },
            {
                "no": 6,
                "bulan": "Juni",
                "total": total_06
            },
            {
                "no": 7,
                "bulan": "Juli",
                "total": total_07
            },
            {
                "no": 8,
                "bulan": "Agustus",
                "total": total_08
            },
            {
                "no": 9,
                "bulan": "September",
                "total": total_09
            },
            {
                "no": 10,
                "bulan": "Oktober",
                "total": total_10
            },
            {
                "no": 11,
                "bulan": "November",
                "total": total_11
            },
            {
                "no": 12,
                "bulan": "Desember",
                "total": total_12
            },
        ]
    }

    nama_bulan = []
    total_bulan = []
    for bln in context['cashflow']:
        nama_bulan.append(bln['bulan'])
        total_bulan.append(bln['total'])

    context['nama_bulan'] = nama_bulan
    context['total_bulan'] = total_bulan

    return render(request, html_template, context)