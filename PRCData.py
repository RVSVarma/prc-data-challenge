import pandas as pd
df = pd.read_parquet('training_2025-01-01_2025-02-01.parquet')
# print(df.columns)

# print(df.head(20))

"""
'MVT_ID_mvt' = Movement record ID,
'FLIGHT_ID_mvt' = Unique flight record ID,
'FLIGHT_mvt' = Flight number,
'FLIGHT_RULE_mvt' = Set of regulations under which the flight is operating (IFR, VFR or NA),
'ADEP_mvt' = Departure airport,
'ADES_mvt' = Destination airport,
'PHASE_mvt' = Flight phase DEP or ARR,
'MVT_TIME_UTC_mvt' = Movement time (UTC),
'BLOCK_TIME_UTC_mvt' = Block time (off block if departure, on block if arrival) (UTC),
'SCHED_TIME_UTC_mvt' = Scheduled time (UTC),
'AIRCRAFT_TYPE_mvt' = Aircraft type e.g. A320, B738, E190,
'RUNWAY_mvt' = Runway ID used for the movement,
'STAND_mvt' = Stand ID,
'TAXITIME_SEC_mvt' = Taxi time (seconds) (taxi out if departure, taxi in if arrival),
'LOBT_flt' = Last Off Block Time (UTC),
'CALLSIGN_flt' = Call sign eg. AAL123, BAW456,
'ADEP_flt' = Departure airport,
'ADES_flt' = Destination airport,
'ADES_FILED_flt' = ADES initially filed in the Flight Plan (FPL). If different from ADES_flt, then the flight has been diverted.,
'MARKET_SEGMENT_flt' = Market segment (e.g. Mainline, Regional, Cargo, Business, Military, Other),
'IOBT_flt' = Initial of Off Block Time,
'FLIGHT_RULE_flt' = Flight rules I = IFR, V = VFR, Y = IFR first then VFR, Z = VFR first then IFR.
'FLIGHT_TYPE_flt' = Flight type S = Scheduled, N = Non-scheduled, G = General Aviation, M = Military, O = Other,
'AIRCRAFT_TYPE_flt' = ICAO aircraft type e.g. A320, B738, E190,
'WK_TBL_CAT_flt' = wake turbulence  category L= Light, M = Medium, H = Heavy, J = Super,
'AIRCRAFT_OPERATOR_flt' = Aircraft operator/ICAO Airline Designator,
'EOBT_1_flt' = Estimated Off Block Time 1 (UTC),
'ARVT_1_flt' = Actual Runway Arrival Time 1 (UTC),
'AOBT_3_flt' = Actual Off Block Time 3 (UTC),
'ARVT_3_flt' = Actual Runway Arrival Time 3 (UTC)
"""
pd.set_option('display.max_columns', None)


print("Data Types:" + "\n" + str(df.dtypes))
print(75*"-")
print("Data Shape:" + "\n" + str(df.shape))
print(75*"-")
print("Sample Data:" + "\n" + str(df.to_string))

print(75*"-")
print("Data Description:" + "\n" + str(df.describe(include='all')))
print(75*"-")

print("Null Value Counts:" + "\n" + str(df.isnull().sum()))
print(75*"-")

print("Dropping rows with null values...")
df = df.dropna()
print(75*"-")

print("Null Value Counts after dropping null values:" + "\n" + str(df.isnull().sum()))
print(75*"-")