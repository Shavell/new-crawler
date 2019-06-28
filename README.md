# GonderiTakibi
> tracking and logging your shipments for international PTT shipments 

![Screenshot](https://raw.githubusercontent.com/Shavell/repo-assets/master/gonderiTakibi/tracking.gif)

> Sqlite3-cli result for related query 
![SQLOUTPUT](https://raw.githubusercontent.com/Shavell/repo-assets/master/gonderiTakibi/sqlite-cli.PNG)

## Example of SQL Queries

> Return all result with definition and tracking code!

```` 
select la.tracking_code_id, r.last_process_comment, r.last_process_date, r.total_fees, tc.definition from main.log_result r join log_action la on r.log_action_id = la.id left join tracking_code tc on la.tracking_code_id = tc.tracking_id
````

## Requirements
- Python 3.6 or earlier
- ChromeDriver for chrome
- PhantomJS (Optional)
- Trained captcha recognizer model (i don't share my trained model, I believe you can do it)


## License

The gonderiTakibi is open-sourced software licensed under the [GPL-3.0 license](https://opensource.org/licenses/MIT).
