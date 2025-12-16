from linkedin_collector import LinkedInCollector

collector = LinkedInCollector()
feed = collector.fetch_feed()
print("Gefundene Beiträge:", feed)
