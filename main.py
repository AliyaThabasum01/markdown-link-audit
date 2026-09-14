from auditor import audit_links

print("🔗 Markdown Link Audit")
print("=" * 35)

filename = input("Enter Markdown file: ").strip()

result = audit_links(filename)

if result is None:
    print("❌ File not found.")
elif not result:
    print("✅ No broken Markdown links found.")
else:
    print("\n⚠️ Problems found:")
    for link in result:
        print(f"- {link}")
