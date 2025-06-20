from monitor_utils.alert_tripper import trigger_alert, clear_alert
from run import get_last_rss_entry

if __name__ == "__main__":
    tag = "rss_test_01"
    trigger_alert(tag=tag, table="federal_registry")
    get_last_rss_entry("https://www.federalregister.gov/api/v1/documents.rss?conditions[sections][]=documents&order=newest")
    clear_alert(tag=tag, table="federal_registry")
