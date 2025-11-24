import win32com.client as win32

# Start Excel
excel = win32.Dispatch("Excel.Application")
excel.Visible = False   # Change to True if you want to see it

# Open file
wb = excel.Workbooks.Open(r"C:\Users\Admin\Documents\office\sidwal\Route Card\project_mom.xlsx")
ws = wb.Sheets("Sheet1")

# Range you want to inspect
rng = ws.Range("I5:J10")

for cell in rng:
    print(f"Cell {cell.Address}:")
    print("  Value:", cell.Value)
    print("  NumberFormat:", cell.NumberFormat)
    print("  Font Name:", cell.Font.Name)
    print("  Font Size:", cell.Font.Size)
    print("  Font Color (RGB):", cell.Font.Color)
    print("  Bold:", cell.Font.Bold)
    print("  Background color:", cell.Interior.Color)
    print("  Horizontal Alignment:", cell.HorizontalAlignment)
    print("  Vertical Alignment:", cell.VerticalAlignment)
    print("  Column Width:", cell.ColumnWidth)
    print("  Row Height:", cell.RowHeight)
    print("-" * 40)

# Cleanup
wb.Close(False)
excel.Quit()
