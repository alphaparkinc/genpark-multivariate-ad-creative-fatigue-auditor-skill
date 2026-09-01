class MultivariateAdCreativeFatigueAuditorClient:
    def audit_ad_fatigue(self, ad_account_id='act_991823', active_ad_variants_count=24, lookback_window_days=14):
        return {
            'audit_run_id': 'fat_aud_9918',
            'ad_variants_analyzed_count': active_ad_variants_count,
            'ctr_decay_rate_pct_per_day': 1.84,
            'frequency_threshold_breached_count': 5,
            'recommended_refresh_variants_count': 6,
            'fatigue_heatmap_report_url': 'https://ads.genpark.ai/fatigue/9918.html'
        }
