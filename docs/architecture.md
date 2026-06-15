                    +----------------+
                    | Weather API    |
                    +-------+--------+
                            |
                            v

                    +----------------+
                    | Python ETL     |
                    | Extract Layer  |
                    +-------+--------+
                            |
                            v
                    +----------------+
                    | Docker         |
                    +-------+--------+
                            |
                            v

                    +----------------+
                    | Raw Data       |
                    | JSON Files     |
                    +-------+--------+
                            |
                            v

                    +----------------+
                    | Databricks     |
                    +-------+--------+
                            |
                            v

                    +----------------+
                    | Bronze Layer   |
                    +-------+--------+
                            |
                            v

                    +----------------+
                    | Silver Layer   |
                    +-------+--------+
                            |
                            v
                +------------------------+
                | Data Quality Checks    |
                |                        |
                | Temperature Validation |
                | Humidity Validation    |
                | Null Checks            |
                +-----------+------------+
                            |
                            v

                    +----------------+
                    | Gold Layer     |
                    +-------+--------+
                            |
                            v

                    +----------------+
                    | CSV Export     |
                    +-------+--------+
                            |
                            v

                    +----------------+
                    | Streamlit      |
                    | Dashboard      |
                    +-------+--------+