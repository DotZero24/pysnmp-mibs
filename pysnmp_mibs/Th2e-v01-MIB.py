# SNMP MIB module (Th2e-v01-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/papouch/Th2e-v01-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:25:19 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PapouchProjekt_ObjectIdentity = ObjectIdentity
papouchProjekt = _PapouchProjekt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248)
)
_The_ObjectIdentity = ObjectIdentity
the = _The_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 20)
)
_Version1_ObjectIdentity = ObjectIdentity
version1 = _Version1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1)
)
_Device_var_ObjectIdentity = ObjectIdentity
device_var = _Device_var_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 1)
)
_DeviceName_Type = DisplayString
_DeviceName_Object = MibScalar
deviceName = _DeviceName_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 1, 1),
    _DeviceName_Type()
)
deviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceName.setStatus("mandatory")
_PsAlarmString_Type = DisplayString
_PsAlarmString_Object = MibScalar
psAlarmString = _PsAlarmString_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 1, 2),
    _PsAlarmString_Type()
)
psAlarmString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psAlarmString.setStatus("mandatory")
_Table_channel_ObjectIdentity = ObjectIdentity
table_channel = _Table_channel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 2)
)
_ChannelTable_Object = MibTable
channelTable = _ChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 2, 1)
)
if mibBuilder.loadTexts:
    channelTable.setStatus("current")
_ChannelEntry_Object = MibTableRow
channelEntry = _ChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 2, 1, 1)
)
channelEntry.setIndexNames(
    (0, "Th2e-v01-MIB", "index"),
)
if mibBuilder.loadTexts:
    channelEntry.setStatus("current")
_InChStatus_Type = Integer32
_InChStatus_Object = MibTableColumn
inChStatus = _InChStatus_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 2, 1, 1, 1),
    _InChStatus_Type()
)
inChStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inChStatus.setStatus("current")
_InChValue_Type = Integer32
_InChValue_Object = MibTableColumn
inChValue = _InChValue_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 2, 1, 1, 2),
    _InChValue_Type()
)
inChValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inChValue.setStatus("current")
_InChUnits_Type = Integer32
_InChUnits_Object = MibTableColumn
inChUnits = _InChUnits_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 2, 1, 1, 3),
    _InChUnits_Type()
)
inChUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    inChUnits.setStatus("current")
_Table_watchValue_ObjectIdentity = ObjectIdentity
table_watchValue = _Table_watchValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 3)
)
_WatchValTable_Object = MibTable
watchValTable = _WatchValTable_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    watchValTable.setStatus("current")
_WatchValEntry_Object = MibTableRow
watchValEntry = _WatchValEntry_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 3, 1, 1)
)
watchValEntry.setIndexNames(
    (0, "Th2e-v01-MIB", "index"),
)
if mibBuilder.loadTexts:
    watchValEntry.setStatus("current")


class _ModeWatch_Type(Integer32):
    """Custom type modeWatch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ModeWatch_Type.__name__ = "Integer32"
_ModeWatch_Object = MibTableColumn
modeWatch = _ModeWatch_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 3, 1, 1, 1),
    _ModeWatch_Type()
)
modeWatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modeWatch.setStatus("current")
_LimitHi_Type = Integer32
_LimitHi_Object = MibTableColumn
limitHi = _LimitHi_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 3, 1, 1, 2),
    _LimitHi_Type()
)
limitHi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitHi.setStatus("current")
_LimitLo_Type = Integer32
_LimitLo_Object = MibTableColumn
limitLo = _LimitLo_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 3, 1, 1, 3),
    _LimitLo_Type()
)
limitLo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitLo.setStatus("current")
_LimitHy_Type = Integer32
_LimitHy_Object = MibTableColumn
limitHy = _LimitHy_Object(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 3, 1, 1, 4),
    _LimitHy_Type()
)
limitHy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    limitHy.setStatus("current")

# Managed Objects groups


# Notification objects

temp_msg = NotificationType(
    (1, 3, 6, 1, 4, 1, 18248, 20, 1, 1, 0, 1)
)
temp_msg.setObjects(
      *(("Th2e-v01-MIB", "deviceName"),
        ("Th2e-v01-MIB", "psAlarmString"))
)
if mibBuilder.loadTexts:
    temp_msg.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Th2e-v01-MIB",
    **{"PositiveInteger": PositiveInteger,
       "papouchProjekt": papouchProjekt,
       "the": the,
       "version1": version1,
       "device-var": device_var,
       "temp-msg": temp_msg,
       "deviceName": deviceName,
       "psAlarmString": psAlarmString,
       "table-channel": table_channel,
       "channelTable": channelTable,
       "channelEntry": channelEntry,
       "inChStatus": inChStatus,
       "inChValue": inChValue,
       "inChUnits": inChUnits,
       "table-watchValue": table_watchValue,
       "watchValTable": watchValTable,
       "watchValEntry": watchValEntry,
       "modeWatch": modeWatch,
       "limitHi": limitHi,
       "limitLo": limitLo,
       "limitHy": limitHy}
)
