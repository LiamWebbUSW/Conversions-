

while ($true) {
 
$today = Get-Date
$min = Get-Date "$($today.ToString('yyyy-MM-dd')) 00:01"
$max = Get-Date "$($today.ToString('yyyy-MM-dd')) 23:59"

$now = Get-Date

$othermin = Get-Date '00:00'
 
 
if ($min.TimeOfDay -le $now.TimeOfDay -and $max.TimeOfDay -ge $now.TimeOfDay) {

 
    # Download the file

   $d = Get-Date -Format G

   $date = get-date -f yyyy_MM_dd_hh_mm

   gtfs-realtime 'https://data.bus-data.dft.gov.uk/api/v1/gtfsrtdatafeed/?api_key=8f56079c505e71d191ea1238049bb1130518a390&boundingBox=-6.234741,49.884017,-0.851440,51.805218' --output D:/swoutputs/walesrt$(get-date -f yyyy_MM_dd_hh_mm).json

   json2csv D:/swoutputs/walesrt$(get-date -f yyyy_MM_dd_hh_mm).json -o D:/swoutputs/walesrt$(get-date -f yyyy_MM_dd_hh_mm).csv -n --unwind-arrays

   Remove-Item D:/swoutputs/walesrt$date.json -verbose
 
   gtfs-realtime 'https://data.bus-data.dft.gov.uk/api/v1/gtfsrtdatafeed/?api_key=8f56079c505e71d191ea1238049bb1130518a390&boundingBox=-3.0248,54.454,-1.1242,55.5006' --output D:/neoutputs/walesrt$(get-date -f yyyy_MM_dd_hh_mm).json
 
   
  json2csv D:/neoutputs/walesrt$(get-date -f yyyy_MM_dd_hh_mm).json -o D:/neoutputs/walesrt$(get-date -f yyyy_MM_dd_hh_mm).csv -n --unwind-arrays

  Remove-Item D:/neoutputs/walesrt$date.json -verbose

    Start-Sleep -Seconds 20

    #jq -n '[inputs | .entity] | add' *.json > output.json

    }else {

    (New-Object System.Net.WebClient).DownloadString("https://data.bus-data.dft.gov.uk/api/v1/datafeed/?api_key=8f56079c505e71d191ea1238049bb1130518a390&boundingBox=-6.234741,49.884017,-0.851440,51.805218") |

  Out-File D:/sirisw/sirioutput$(get-date -f yyyy_MM_dd_hh_mm_ss).xml

  (New-Object System.Net.WebClient).DownloadString("https://data.bus-data.dft.gov.uk/api/v1/datafeed/?api_key=8f56079c505e71d191ea1238049bb1130518a390&boundingBox=-3.0248,54.454,-1.1242,55.5006") |

  Out-File D:/sirine/sirioutput$(get-date -f yyyy_MM_dd_hh_mm_ss).xml
 
   (New-Object System.Net.WebClient).DownloadString("https://data.bus-data.dft.gov.uk/api/v1/siri-sx/?api_key=8f56079c505e71d191ea1238049bb1130518a390") |

  Out-File D:/sirisx/sirioutput$(get-date -f yyyy_MM_dd_hh_mm_ss).xml

  Start-Sleep -Seconds 40

    }

    } 

 
  
 