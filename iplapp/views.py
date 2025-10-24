from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from iplapp.models import Match, Delivery
from django.db.models import Count, Sum, ExpressionWrapper, F, FloatField

def landing_page1(request):
    matches_data = (
        Match.objects.values('season')
        .annotate(count=Count('id'))
        .order_by('season')
    )
    return render(request, 'landing_page1.html', {'matches_data': matches_data})

def landing_page2(request):
    team_data = (
        Match.objects.values('season', 'winner')
        .annotate(wins=Count('id'))
        .exclude(winner__isnull=True)
        .order_by('season', 'winner')
    )

    teams = sorted(set([d['winner'] for d in team_data]))
    team_wins = {}
    for d in team_data:
        team_wins.setdefault(d['season'], [0]*len(teams))
        team_wins[d['season']][teams.index(d['winner'])] = d['wins']

    return render(request, 'landing_page2.html', {'teams': teams, 'team_wins': team_wins})

def stats_dashboard(request):
    years = (
        Match.objects.values_list('season', flat=True)
        .distinct()
        .order_by('season')
    )

    selected_year = request.GET.get('year')
    context = {'years': years, 'selected_year': selected_year}
    if selected_year:
        extra_runs = (
            Match.objects
            .filter(season=selected_year)
            .values('delivery__bowling_team')
            .annotate(total_extra_runs=Count('delivery__extra_runs'))
        )

        bowlers = (
            Delivery.objects
            .filter(match__season=selected_year)
            .values('bowler')
            .annotate(total_runs=Sum('total_runs'), total_balls=Count('id'))
            .annotate(
                economy=ExpressionWrapper(
                    F('total_runs') * 6.0 / F('total_balls'),
                    output_field=FloatField()
                )
            )
            .order_by('economy')[:10]
        )

        matches = Match.objects.filter(season=selected_year)
        played_per_team = {}
        for m in matches:
            for team in [m.team1, m.team2]:
                played_per_team[team] = played_per_team.get(team, 0) + 1
        won_per_team = (
            matches.values('winner')
            .annotate(won=Count('id'))
            .exclude(winner__isnull=True)
        )

        results = []
        for team, played in played_per_team.items():
            won = next((w['won'] for w in won_per_team if w['winner'] == team), 0)
            results.append({'team': team, 'played': played, 'won': won})
        context.update({
            'extra_runs': extra_runs,
            'bowlers': bowlers,
            'results': results,
        })

    return render(request, 'stats_dashboard.html', context)
