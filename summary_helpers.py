"""Helper functions for generating and exporting summary reports."""
import json
import os
from collections import Counter

def export_summaries(df_summary, data_dir):
    """Export action items, recommendations, contentions, and theme analysis."""

    # Filter by strength
    action_items_df = df_summary[df_summary['action_strength'] >= 2].sort_values(
        ['source_file', 'action_strength'], ascending=[True, False]
    )
    recommendations_df = df_summary[df_summary['recommendation_strength'] >= 2].sort_values(
        ['source_file', 'recommendation_strength'], ascending=[True, False]
    )
    contentions_df = df_summary[df_summary['contention_strength'] >= 2].sort_values(
        ['source_file', 'contention_strength'], ascending=[True, False]
    )

    # Export action items
    action_summary = {
        'total_action_items': len(action_items_df),
        'action_items_by_strength': {
            'high': len(action_items_df[action_items_df['action_strength'] >= 4]),
            'medium': len(action_items_df[(action_items_df['action_strength'] >= 2) & (action_items_df['action_strength'] < 4)]),
            'low': len(action_items_df[action_items_df['action_strength'] < 2])
        },
        'top_items': [
            {
                'text': row['text'],
                'source': row['source_file'],
                'strength': int(row['action_strength']),
                'categories': row['action_categories']
            }
            for _, row in action_items_df.head(20).iterrows()
        ]
    }

    with open(os.path.join(data_dir, 'phase6_action_items.json'), 'w') as f:
        json.dump(action_summary, f, indent=2, default=str)

    # Export recommendations
    recommendations_summary = {
        'total_recommendations': len(recommendations_df),
        'recommendations_by_strength': {
            'high': len(recommendations_df[recommendations_df['recommendation_strength'] >= 4]),
            'medium': len(recommendations_df[(recommendations_df['recommendation_strength'] >= 2) & (recommendations_df['recommendation_strength'] < 4)]),
            'low': len(recommendations_df[recommendations_df['recommendation_strength'] < 2])
        },
        'top_items': [
            {
                'text': row['text'],
                'source': row['source_file'],
                'strength': int(row['recommendation_strength']),
                'categories': row['recommendation_categories']
            }
            for _, row in recommendations_df.head(20).iterrows()
        ]
    }

    with open(os.path.join(data_dir, 'phase6_recommendations.json'), 'w') as f:
        json.dump(recommendations_summary, f, indent=2, default=str)

    # Export contentions
    contentions_summary = {
        'total_contentions': len(contentions_df),
        'contentions_by_strength': {
            'high': len(contentions_df[contentions_df['contention_strength'] >= 4]),
            'medium': len(contentions_df[(contentions_df['contention_strength'] >= 2) & (contentions_df['contention_strength'] < 4)]),
            'low': len(contentions_df[contentions_df['contention_strength'] < 2])
        },
        'top_items': [
            {
                'text': row['text'],
                'source': row['source_file'],
                'strength': int(row['contention_strength']),
                'categories': row['contention_categories']
            }
            for _, row in contentions_df.head(20).iterrows()
        ]
    }

    with open(os.path.join(data_dir, 'phase6_contentions_issues.json'), 'w') as f:
        json.dump(contentions_summary, f, indent=2, default=str)

    return action_summary, recommendations_summary, contentions_summary

def export_theme_analysis(df_summary, themes, data_dir):
    """Export theme analysis and save enhanced dataframe."""

    # Count themes
    all_themes = []
    for theme_list in df_summary['themes']:
        all_themes.extend(theme_list)

    theme_counts = Counter(all_themes)

    theme_analysis = {
        'theme_distribution': dict(theme_counts),
        'themes_definition': themes,
        'total_documents': len(df_summary),
        'total_rows': len(df_summary)
    }

    with open(os.path.join(data_dir, 'phase6_theme_analysis.json'), 'w') as f:
        json.dump(theme_analysis, f, indent=2, default=str)

    # Save enhanced dataframe
    df_summary.to_pickle(os.path.join(data_dir, 'meeting_data_summary.pkl'))

    return theme_counts

def generate_analysis_summary(analysis_data):
    """Generate summary statistics for Phase 7 analysis."""
    summary = {
        'total_action_items': analysis_data['action_summary']['total_action_items'],
        'total_recommendations': analysis_data['recommendations_summary']['total_recommendations'],
        'total_contentions': analysis_data['contentions_summary']['total_contentions'],
        'top_themes': list(analysis_data['theme_counts'].most_common(5)),
        'action_strength_dist': {
            'high': analysis_data['action_summary']['action_items_by_strength']['high'],
            'medium': analysis_data['action_summary']['action_items_by_strength']['medium'],
            'low': analysis_data['action_summary']['action_items_by_strength']['low']
        },
        'recommendation_strength_dist': {
            'high': analysis_data['recommendations_summary']['recommendations_by_strength']['high'],
            'medium': analysis_data['recommendations_summary']['recommendations_by_strength']['medium'],
            'low': analysis_data['recommendations_summary']['recommendations_by_strength']['low']
        }
    }
    return summary
