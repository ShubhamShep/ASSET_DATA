import streamlit as st
import pandas as pd
import plotly.express as px

# Set page config (this must be the first Streamlit command)
st.set_page_config(page_title="Power Infrastructure Dashboard", layout="wide")

# Load the data
@st.cache_data
def load_data():
    data = pd.DataFrame([
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"CH. SAMBHAJINAGAR ZONE","C_NAME":"CH. SAMBHAJINAGAR (U) CIRCLE","SUBSTATION":34,"DTC":1833,"HT_POLE":0,"LT_POLE":59},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"CH. SAMBHAJINAGAR ZONE","C_NAME":"CH. SAMBHAJINAGAR CIRCLE","SUBSTATION":152,"DTC":22916,"HT_POLE":129470,"LT_POLE":445},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"CH. SAMBHAJINAGAR ZONE","C_NAME":"JALNA CIRCLE","SUBSTATION":126,"DTC":17485,"HT_POLE":86400,"LT_POLE":2368},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"LATUR ZONE, LATUR","C_NAME":"BEED  CIRCLE","SUBSTATION":182,"DTC":22043,"HT_POLE":125460,"LT_POLE":355},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"LATUR ZONE, LATUR","C_NAME":"DHARASHIV CIRCLE","SUBSTATION":123,"DTC":15327,"HT_POLE":120176,"LT_POLE":86},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"LATUR ZONE, LATUR","C_NAME":"LATUR CIRCLE","SUBSTATION":159,"DTC":19956,"HT_POLE":114140,"LT_POLE":344},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"NANDED ZONE","C_NAME":"HINGOLI CIRCLE","SUBSTATION":75,"DTC":13476,"HT_POLE":77163,"LT_POLE":1421},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"NANDED ZONE","C_NAME":"NANDED CIRCLE","SUBSTATION":164,"DTC":23419,"HT_POLE":112206,"LT_POLE":1360},
        {"REGION_NAME":"CH.SAMBHAJINAGAR","Z_NAME":"NANDED ZONE","C_NAME":"PARBHANI CIRCLE","SUBSTATION":104,"DTC":12745,"HT_POLE":92546,"LT_POLE":1021},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"BHANDUP (U) ZONE","C_NAME":"BHIWANDI CIRCLE","SUBSTATION":4,"DTC":0,"HT_POLE":0,"LT_POLE":0},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"BHANDUP (U) ZONE","C_NAME":"PEN CIRCLE","SUBSTATION":50,"DTC":7022,"HT_POLE":0,"LT_POLE":55021},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"BHANDUP (U) ZONE","C_NAME":"THANE (U) CIRCLE","SUBSTATION":83,"DTC":3307,"HT_POLE":0,"LT_POLE":102},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"BHANDUP (U) ZONE","C_NAME":"THANE DF CIRCLE","SUBSTATION":9,"DTC":347,"HT_POLE":0,"LT_POLE":0},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"BHANDUP (U) ZONE","C_NAME":"WASHI CIRCLE","SUBSTATION":100,"DTC":5241,"HT_POLE":0,"LT_POLE":577},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"JALGAON ZONE","C_NAME":"DHULE CIRCLE","SUBSTATION":98,"DTC":18840,"HT_POLE":83053,"LT_POLE":1365},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"JALGAON ZONE","C_NAME":"JALGAON CIRCLE","SUBSTATION":204,"DTC":40321,"HT_POLE":182611,"LT_POLE":16730},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"JALGAON ZONE","C_NAME":"NANDURBAR CIRCLE","SUBSTATION":66,"DTC":14766,"HT_POLE":71274,"LT_POLE":1349},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"KALYAN ZONE","C_NAME":"KALYAN CIRCLE - I","SUBSTATION":29,"DTC":2620,"HT_POLE":0,"LT_POLE":3856},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"KALYAN ZONE","C_NAME":"KALYAN CIRCLE - II","SUBSTATION":38,"DTC":4888,"HT_POLE":0,"LT_POLE":6423},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"KALYAN ZONE","C_NAME":"PALGHAR (MINI) CIRCLE","SUBSTATION":47,"DTC":5827,"HT_POLE":0,"LT_POLE":24462},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"KALYAN ZONE","C_NAME":"VASAI CIRCLE","SUBSTATION":33,"DTC":5678,"HT_POLE":0,"LT_POLE":8435},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"KOKAN ZONE,RATNAGIRI","C_NAME":"RATNAGIRI CIRCLE","SUBSTATION":67,"DTC":8853,"HT_POLE":0,"LT_POLE":53566},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"KOKAN ZONE,RATNAGIRI","C_NAME":"SINDUDURG CIRCLE","SUBSTATION":35,"DTC":2894,"HT_POLE":0,"LT_POLE":2842},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"NASIK ZONE","C_NAME":"A' NAGAR CIRCLE","SUBSTATION":253,"DTC":44418,"HT_POLE":304981,"LT_POLE":530},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"NASIK ZONE","C_NAME":"MALEGAON CIRCLE","SUBSTATION":100,"DTC":20697,"HT_POLE":113064,"LT_POLE":55},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"NASIK ZONE","C_NAME":"MALEGAON DF CIRCLE","SUBSTATION":17,"DTC":665,"HT_POLE":0,"LT_POLE":0},
        {"REGION_NAME":"KOKAN REGION","Z_NAME":"NASIK ZONE","C_NAME":"NASHIK CIRCLE","SUBSTATION":159,"DTC":22912,"HT_POLE":111841,"LT_POLE":119},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"AKOLA ZONE","C_NAME":"AKOLA CIRCLE","SUBSTATION":86,"DTC":13073,"HT_POLE":94792,"LT_POLE":0},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"AKOLA ZONE","C_NAME":"BULDHANA CIRCLE","SUBSTATION":127,"DTC":20221,"HT_POLE":188925,"LT_POLE":0},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"AKOLA ZONE","C_NAME":"WASHIM CIRCLE","SUBSTATION":71,"DTC":9354,"HT_POLE":84634,"LT_POLE":331},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"AMARAVATI ZONE","C_NAME":"AMARAVATI CIRCLE","SUBSTATION":138,"DTC":21327,"HT_POLE":171280,"LT_POLE":0},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"AMARAVATI ZONE","C_NAME":"YAVATMAL CIRCLE","SUBSTATION":127,"DTC":21982,"HT_POLE":200962,"LT_POLE":26},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"CHANDRAPUR ZONE","C_NAME":"CHANDRAPUR CIRCLE","SUBSTATION":95,"DTC":13875,"HT_POLE":90536,"LT_POLE":615},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"CHANDRAPUR ZONE","C_NAME":"GADCHIROLI CIRCLE","SUBSTATION":67,"DTC":9562,"HT_POLE":0,"LT_POLE":1369},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"GONDIA ZONE","C_NAME":"BHANDARA CIRCLE","SUBSTATION":53,"DTC":11460,"HT_POLE":74048,"LT_POLE":7016},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"GONDIA ZONE","C_NAME":"GONDIA CIRCLE","SUBSTATION":51,"DTC":8186,"HT_POLE":47472,"LT_POLE":954},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"NAGPUR ZONE","C_NAME":"NAGPUR (R) CIRCLE","SUBSTATION":101,"DTC":15329,"HT_POLE":107084,"LT_POLE":43016},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"NAGPUR ZONE","C_NAME":"NAGPUR (U) CIRCLE","SUBSTATION":109,"DTC":10366,"HT_POLE":55956,"LT_POLE":2684},
        {"REGION_NAME":"NAGPUR REGION","Z_NAME":"NAGPUR ZONE","C_NAME":"WARDHA CIRCLE","SUBSTATION":75,"DTC":11637,"HT_POLE":97786,"LT_POLE":10407},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"BARAMATI ZONE","C_NAME":"BARAMATI CIRCLE","SUBSTATION":126,"DTC":23663,"HT_POLE":160802,"LT_POLE":1651},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"BARAMATI ZONE","C_NAME":"SATARA CIRCLE","SUBSTATION":122,"DTC":24419,"HT_POLE":155780,"LT_POLE":7599},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"BARAMATI ZONE","C_NAME":"SOLAPUR CIRCLE","SUBSTATION":309,"DTC":43155,"HT_POLE":317294,"LT_POLE":2940},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"KOLHAPUR ZONE","C_NAME":"KOLHAPUR CIRCLE","SUBSTATION":155,"DTC":28948,"HT_POLE":108996,"LT_POLE":28230},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"KOLHAPUR ZONE","C_NAME":"SANGLI CIRCLE","SUBSTATION":167,"DTC":26136,"HT_POLE":123374,"LT_POLE":8193},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"PUNE ZONE","C_NAME":"GANESHKHIND (U) CIRCLE","SUBSTATION":114,"DTC":9137,"HT_POLE":587,"LT_POLE":0},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"PUNE ZONE","C_NAME":"PUNE (R) CIRCLE","SUBSTATION":122,"DTC":18126,"HT_POLE":114942,"LT_POLE":661},
        {"REGION_NAME":"PUNE REGION","Z_NAME":"PUNE ZONE","C_NAME":"RASTAPETH (U) CIRCLE","SUBSTATION":114,"DTC":6251,"HT_POLE":2508,"LT_POLE":1}
    ])
    return data

# Load data
data = load_data()

# Title
st.title("Power Infrastructure Dashboard")

# Sidebar for filtering
st.sidebar.header("Filters")
selected_region = st.sidebar.multiselect("Select Region", options=data["REGION_NAME"].unique(), default=data["REGION_NAME"].unique())
selected_zone = st.sidebar.multiselect("Select Zone", options=data["Z_NAME"].unique(), default=data["Z_NAME"].unique())

# Filter data
filtered_data = data[data["REGION_NAME"].isin(selected_region) & data["Z_NAME"].isin(selected_zone)]

# Calculate totals
total_substation = filtered_data["SUBSTATION"].sum()
total_dtc = filtered_data["DTC"].sum()
total_ht_pole = filtered_data["HT_POLE"].sum()
total_lt_pole = filtered_data["LT_POLE"].sum()

# Display metrics
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Substations", f"{total_substation:,}")
col2.metric("Total DTCs", f"{total_dtc:,}")
col3.metric("Total HT Poles", f"{total_ht_pole:,}")
col4.metric("Total LT Poles", f"{total_lt_pole:,}")

# Aggregate data by region
region_data = filtered_data.groupby("REGION_NAME").sum().reset_index()

# Create visualizations
st.header("Distribution of Assets by Region")
fig1 = px.bar(region_data, x="REGION_NAME", y=["SUBSTATION", "DTC", "HT_POLE", "LT_POLE"], 
              title="Asset Distribution by Region",
              labels={"value": "Count", "variable": "Asset Type"},
              barmode="group")
st.plotly_chart(fig1, use_container_width=True)

st.header("Asset Type Distribution")
asset_totals = region_data[["SUBSTATION", "DTC", "HT_POLE", "LT_POLE"]].sum()
fig2 = px.pie(values=asset_totals.values, names=asset_totals.index, 
              title="Overall Asset Type Distribution",
              hole=0.3)
st.plotly_chart(fig2, use_container_width=True)

# Zone-wise comparison
st.header("Zone-wise Asset Comparison")
zone_data = filtered_data.groupby("Z_NAME").sum().reset_index()
fig3 = px.bar(zone_data, x="Z_NAME", y=["SUBSTATION", "DTC", "HT_POLE", "LT_POLE"],
              title="Asset Distribution by Zone",
              labels={"value": "Count", "variable": "Asset Type"},
              barmode="group")
st.plotly_chart(fig3, use_container_width=True)

# Heatmap of asset distribution
st.header("Heatmap: Asset Distribution Across Regions and Zones")
heatmap_data = filtered_data.pivot_table(
    values=["SUBSTATION", "DTC", "HT_POLE", "LT_POLE"],
    index="REGION_NAME",
    columns="Z_NAME",
    aggfunc="sum",
    fill_value=0
)
fig4 = px.imshow(heatmap_data, 
                 labels=dict(color="Count"),
                 title="Asset Distribution Heatmap")
st.plotly_chart(fig4, use_container_width=True)

# Scatter plot: Correlation between DTCs and Substations
st.header("Correlation: DTCs vs Substations")
fig5 = px.scatter(filtered_data, x="DTC", y="SUBSTATION", color="REGION_NAME", 
                  hover_data=["Z_NAME", "C_NAME"],
                  title="Correlation between DTCs and Substations")
st.plotly_chart(fig5, use_container_width=True)

# Display raw data
st.header("Raw Data")
st.dataframe(filtered_data)

# Add a download button for the filtered data
csv = filtered_data.to_csv(index=False)
st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="filtered_power_infrastructure_data.csv",
    mime="text/csv",
)