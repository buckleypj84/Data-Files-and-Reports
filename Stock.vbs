Option Explicit
    
    Dim mintNbrOfRows As Long       'modular variable for worksheet row count
    
    Sub GetTickerSum()
    '======================================================
    ' Loop thru data and summarize volume for each ticker
    '======================================================
    
    Dim readFromRow As Long
    Dim writeToRow As Long
    Dim currVol As Double
    Dim currTicker As String
    Dim greatestPctInc As Long
    Dim greatestPctDec As Long
    Dim greatestVol As Double
    
    Dim ws As Worksheet
    Dim priceOpen As Double
    Dim priceClose As Double
    Dim yearlyChange As Double
    Dim changePct As Double

    '==========================================================
    ' Determine the number of worksheets in the workbook using
    ' the collection ActiveWorkbook.Workshetts as the outer
    ' For loop and initialize shared variables
    '==========================================================
    For Each ws In ActiveWorkbook.Worksheets
        Sheets(ws.Name).Select                  ' makes the worksheet active
        Call GetWSTotalRowCnt                   ' determines the number of rows on the active worksheet
        
        ' load first row data into variable
        currTicker = Range("A2").Value
        priceOpen = Range("C2").Value
        priceClose = Range("F2").Value
        currVol = Range("G2").Value
        
        ' add headings for aggregated ticker data
        Cells(1, 9).Value = "Ticker"
        Cells(1, 10).Value = "Yearly Change"
        Cells(1, 11).Value = "Percent Change"
        Cells(1, 12).Value = "Total Stock Volume"
        
        Cells(2, 15).Value = "Greatest % Increase"
        Cells(3, 15).Value = "Greatest % Decrease"
        Cells(4, 15).Value = "Greatest Total Volume"
        Cells(1, 16).Value = "Ticker"
        Cells(1, 17).Value = "Value"
               
        ' used to position the output of the aggregated ticket data
        writeToRow = 2
        
        '================================================================
        ' counter will begin with 3 because the first row contains labels
        ' and the 2nd row's data has been moved to the variables
        ' currTicker, priceOpen, priceClose & currVol, once the last row of
        ' the ticket has been reached the aggregrated data is written to
        ' the row indicated by the writeToRow variable
        '================================================================
        For readFromRow = 3 To mintNbrOfRows + 1
            If Cells(readFromRow, 1).Value = currTicker Then
                currVol = currVol + Cells(readFromRow, 7)
            Else
                '=============================================================
                ' we have reached the last row of the current ticker so write
                ' out the ticker's aggregrated values
                '=============================================================
                Cells(writeToRow, 9).Value = currTicker                     ' Ticker
                
                ' calculate yearly change
                priceClose = Cells((readFromRow) - 1, 6).Value
                yearlyChange = priceClose - priceOpen
                
                Cells(writeToRow, 10).Value = yearlyChange                  ' Yearly Change
                
                ' Add Conditional formatting to Yearly Change
                If yearlyChange > 0 Then
                     Cells(writeToRow, 10).Interior.Color = vbGreen
                Else
                     Cells(writeToRow, 10).Interior.Color = vbRed
                End If
                
                ' calculate change percent
                ' prevent div/0 error
                '=====================================================================
                ' question: I attempted to use this function but don't understand why
                '           it did not work.  Do you have an idea what about this issue?
                ' changePct = WorksheetFunction.IfError((yearlyChange / priceOpen), 0)
                '=====================================================================
                If yearlyChange = 0 Or priceOpen = 0 Then
                   changePct = 0
                Else
                   changePct = (yearlyChange / priceOpen)
                End If
                       
                Cells(writeToRow, 11).Value = Format(changePct, "Percent")  ' Percent change
              
                Cells(writeToRow, 12).Value = Format(currVol, "Currency")   ' Total Stock Volume
              
                writeToRow = writeToRow + 1
              
                ' reset variables to next ticker
                currTicker = Cells(readFromRow, 1).Value
                priceOpen = Cells(readFromRow, 3).Value
                currVol = Cells(readFromRow, 7).Value
           End If
           
        Next readFromRow  'inner loop for number of rows on worksheet
        
        ' return the stock with the Greatest % increase
        greatestPctInc = GetRowWithMaxValue(Range("K:K"))
        Range("P2").Value = Range("I" & greatestPctInc).Value                       ' Ticker
        Range("Q2").Value = Format(Range("K" & greatestPctInc).Value, "Percent")    ' Greatest % increase
         
        ' return the stock with the Greatest % Decrease
        greatestPctDec = GetRowWithMinValue(Range("K:K"))
        Range("P3").Value = Range("I" & greatestPctDec).Value                       ' Ticker
        Range("Q3").Value = Format(Range("K" & greatestPctDec).Value, "Percent")    ' Greatest % decrease
        
        ' return the stock with the Greatest total volume
        greatestPctInc = GetRowWithMaxValue(Range("L:L"))
        Range("P4").Value = Range("I" & greatestPctInc).Value                       ' Ticker
        Range("Q4").Value = Format(Range("L" & greatestPctInc).Value, "Currency")   ' Greatest total volume
         
        ' Apply Auto Fit for better readability
        Columns("I:I").EntireColumn.AutoFit     ' Ticker
        Columns("J:J").EntireColumn.AutoFit     ' Yearly Change
        Columns("K:K").EntireColumn.AutoFit     ' Percent Change
        Columns("L:L").EntireColumn.AutoFit     ' Total Stock Volume
        Columns("O:O").EntireColumn.AutoFit     ' Labels for: Greatest % Increase , Greatest % Decrease & Greatest Total Volume
        Columns("P:P").EntireColumn.AutoFit     ' Values for: Greatest % Increase , Greatest % Decrease & Greatest Total Volume
        Columns("Q:Q").EntireColumn.AutoFit     ' Greatest Total Stock Volume
        
    Next ws 'outer loop for number of worksheets
     

 
End Sub

Sub GetWSTotalRowCnt()

    '=======================================================
    ' return number of used rows in active worksheet
    ' empty rows are considered used if data follows empty
    ' row
    '=======================================================

    mintNbrOfRows = ActiveSheet.UsedRange.Rows.Count

    
End Sub

Function GetRowWithMaxValue(rng)

    Dim myVal
    Dim lRow As Long
    myVal = Application.WorksheetFunction.Max(rng)
    lRow = Application.WorksheetFunction.Match(myVal, rng, 0)
    GetRowWithMaxValue = lRow
    
End Function
        
Function GetRowWithMinValue(rng)

    Dim myVal
    Dim lRow As Long
    myVal = Application.WorksheetFunction.Min(rng)
    lRow = Application.WorksheetFunction.Match(myVal, rng, 0)
    GetRowWithMinValue = lRow
    
End Function



