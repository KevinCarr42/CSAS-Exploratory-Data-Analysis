"""Helper functions for Phase 7 analysis and recommendations."""
import json
import os
from collections import Counter

def analyze_patterns(df_analysis):
    """Analyze patterns in action items, recommendations, and contentions."""

    patterns = {
        'action_item_distribution': {
            'by_source_file': df_analysis[df_analysis['action_strength'] > 0].groupby('source_file')['action_strength'].sum().to_dict(),
            'by_theme': df_analysis[df_analysis['action_strength'] > 0].explode('themes').groupby('themes')['action_strength'].sum().to_dict(),
            'by_language': df_analysis[df_analysis['action_strength'] > 0].groupby('language')['action_strength'].sum().to_dict(),
        },
        'recommendation_distribution': {
            'by_source_file': df_analysis[df_analysis['recommendation_strength'] > 0].groupby('source_file')['recommendation_strength'].sum().to_dict(),
            'by_theme': df_analysis[df_analysis['recommendation_strength'] > 0].explode('themes').groupby('themes')['recommendation_strength'].sum().to_dict(),
            'by_language': df_analysis[df_analysis['recommendation_strength'] > 0].groupby('language')['recommendation_strength'].sum().to_dict(),
        },
        'contention_distribution': {
            'by_source_file': df_analysis[df_analysis['contention_strength'] > 0].groupby('source_file')['contention_strength'].sum().to_dict(),
            'by_theme': df_analysis[df_analysis['contention_strength'] > 0].explode('themes').groupby('themes')['contention_strength'].sum().to_dict(),
            'by_language': df_analysis[df_analysis['contention_strength'] > 0].groupby('language')['contention_strength'].sum().to_dict(),
        }
    }

    return patterns

def identify_conflicts(df_analysis):
    """Identify potential conflicts: items with both action and contention signals."""

    conflicts = df_analysis[
        (df_analysis['action_strength'] >= 2) &
        (df_analysis['contention_strength'] >= 2)
    ][['source_file', 'text', 'action_categories', 'contention_categories', 'themes']].copy()

    return conflicts

def identify_high_priority_items(df_analysis):
    """Identify high-priority items (strength >= 3)."""

    high_priority = {
        'action_items': df_analysis[df_analysis['action_strength'] >= 3][
            ['source_file', 'text', 'action_categories', 'themes', 'action_strength']
        ].sort_values('action_strength', ascending=False).head(15).to_dict('records'),

        'recommendations': df_analysis[df_analysis['recommendation_strength'] >= 3][
            ['source_file', 'text', 'recommendation_categories', 'themes', 'recommendation_strength']
        ].sort_values('recommendation_strength', ascending=False).head(15).to_dict('records'),

        'contentions': df_analysis[df_analysis['contention_strength'] >= 3][
            ['source_file', 'text', 'contention_categories', 'themes', 'contention_strength']
        ].sort_values('contention_strength', ascending=False).head(15).to_dict('records')
    }

    return high_priority

def generate_stakeholder_summary(df_analysis):
    """Generate summary by theme for stakeholder briefings."""

    themes = set()
    for theme_list in df_analysis['themes']:
        themes.update(theme_list)

    stakeholder_summary = {}

    for theme in sorted(themes):
        theme_data = df_analysis[df_analysis['themes'].apply(lambda x: theme in x)]

        stakeholder_summary[theme] = {
            'total_items': len(theme_data),
            'action_items': (theme_data['action_strength'] > 0).sum(),
            'recommendations': (theme_data['recommendation_strength'] > 0).sum(),
            'issues': (theme_data['contention_strength'] > 0).sum(),
            'languages': theme_data['language'].value_counts().to_dict(),
            'top_action_item': theme_data[theme_data['action_strength'] > 0]['text'].iloc[0] if (theme_data['action_strength'] > 0).any() else None,
            'top_recommendation': theme_data[theme_data['recommendation_strength'] > 0]['text'].iloc[0] if (theme_data['recommendation_strength'] > 0).any() else None,
            'top_issue': theme_data[theme_data['contention_strength'] > 0]['text'].iloc[0] if (theme_data['contention_strength'] > 0).any() else None,
        }

    return stakeholder_summary

def generate_follow_up_actions(df_analysis):
    """Generate recommended follow-up actions."""

    follow_ups = []

    # Get high-strength items as follow-up triggers
    high_actions = df_analysis[df_analysis['action_strength'] >= 3]
    if len(high_actions) > 0:
        follow_ups.append({
            'type': 'High Priority Actions',
            'count': len(high_actions),
            'description': 'Multiple strong action signals requiring immediate attention',
            'sources': high_actions['source_file'].unique().tolist()[:5]
        })

    high_contentions = df_analysis[df_analysis['contention_strength'] >= 3]
    if len(high_contentions) > 0:
        follow_ups.append({
            'type': 'Unresolved Issues',
            'count': len(high_contentions),
            'description': 'Contentious items that need clarification and resolution',
            'sources': high_contentions['source_file'].unique().tolist()[:5]
        })

    # Identify themes with high contention
    for theme_list in df_analysis['themes']:
        for theme in theme_list:
            theme_data = df_analysis[df_analysis['themes'].apply(lambda x: theme in x)]
            contention_rate = (theme_data['contention_strength'] > 0).sum() / len(theme_data) if len(theme_data) > 0 else 0

            if contention_rate > 0.3:  # More than 30% contentious
                follow_ups.append({
                    'type': f'{theme} - High Contention',
                    'count': (theme_data['contention_strength'] > 0).sum(),
                    'description': f'{contention_rate*100:.0f}% of {theme} content flagged with concerns',
                    'sources': theme_data['source_file'].unique().tolist()[:5]
                })
                break  # Only one follow-up per theme

    return follow_ups

def export_analysis(patterns, conflicts, high_priority, stakeholder_summary, follow_ups, data_dir):
    """Export all analysis to JSON files."""

    # Export patterns
    with open(os.path.join(data_dir, 'phase7_patterns.json'), 'w') as f:
        json.dump(patterns, f, indent=2, default=str)

    # Export conflicts
    conflicts_json = {
        'total_conflicts': len(conflicts),
        'conflicts': conflicts.to_dict('records')[:20]
    }
    with open(os.path.join(data_dir, 'phase7_conflicts.json'), 'w') as f:
        json.dump(conflicts_json, f, indent=2, default=str)

    # Export high priority
    with open(os.path.join(data_dir, 'phase7_high_priority.json'), 'w') as f:
        json.dump(high_priority, f, indent=2, default=str)

    # Export stakeholder summary
    with open(os.path.join(data_dir, 'phase7_stakeholder_summary.json'), 'w') as f:
        json.dump(stakeholder_summary, f, indent=2, default=str)

    # Export follow-up actions
    with open(os.path.join(data_dir, 'phase7_follow_up_actions.json'), 'w') as f:
        json.dump(follow_ups, f, indent=2, default=str)

    return {
        'patterns_file': 'phase7_patterns.json',
        'conflicts_file': 'phase7_conflicts.json',
        'high_priority_file': 'phase7_high_priority.json',
        'stakeholder_summary_file': 'phase7_stakeholder_summary.json',
        'follow_up_actions_file': 'phase7_follow_up_actions.json'
    }
