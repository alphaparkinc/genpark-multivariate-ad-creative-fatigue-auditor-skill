from client import MultivariateAdCreativeFatigueAuditorClient

def main():
    client = MultivariateAdCreativeFatigueAuditorClient()
    res = client.audit_ad_fatigue('act_551928', 18, 7)
    print('Ad Fatigue Auditor: ' + res['audit_run_id'] + ' (' + str(res['ad_variants_analyzed_count']) + ' variants)')
    print('CTR Decay: ' + str(res['ctr_decay_rate_pct_per_day']) + '%/day | Breached Frequency: ' + str(res['frequency_threshold_breached_count']))
    print('Recommended Refreshes: ' + str(res['recommended_refresh_variants_count']))
    print('Heatmap URL: ' + res['fatigue_heatmap_report_url'])

if __name__ == '__main__':
    main()
