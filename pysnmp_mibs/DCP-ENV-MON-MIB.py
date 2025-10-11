# SNMP MIB module (DCP-ENV-MON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/DCP-ENV-MON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:31:27 2025
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

(dcpGeneric,) = mibBuilder.importSymbols(
    "DCP-MIB",
    "dcpGeneric")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TimeTicks,
 Unsigned32,
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
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(DcpTenths,
 FanMode,
 FanStatus) = mibBuilder.importSymbols(
    "SO-TC-MIB",
    "DcpTenths",
    "FanMode",
    "FanStatus")


# MODULE-IDENTITY

dcpEnv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6)
)
if mibBuilder.loadTexts:
    dcpEnv.setRevisions(
        ("2023-03-30 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcpEnvMon_ObjectIdentity = ObjectIdentity
dcpEnvMon = _DcpEnvMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1)
)
_DcpEnvMonTemperature_ObjectIdentity = ObjectIdentity
dcpEnvMonTemperature = _DcpEnvMonTemperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 1)
)
_DcpEnvMonTemperatureObjects_ObjectIdentity = ObjectIdentity
dcpEnvMonTemperatureObjects = _DcpEnvMonTemperatureObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 1, 1)
)
_DcpEnvMonTemperatureTable_Object = MibTable
dcpEnvMonTemperatureTable = _DcpEnvMonTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dcpEnvMonTemperatureTable.setStatus("current")
_DcpEnvMonTemperatureEntry_Object = MibTableRow
dcpEnvMonTemperatureEntry = _DcpEnvMonTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 1, 1, 1, 1)
)
dcpEnvMonTemperatureEntry.setIndexNames(
    (0, "DCP-ENV-MON-MIB", "dcpEnvMonTemperatureIndex"),
)
if mibBuilder.loadTexts:
    dcpEnvMonTemperatureEntry.setStatus("current")
_DcpEnvMonTemperatureIndex_Type = Unsigned32
_DcpEnvMonTemperatureIndex_Object = MibTableColumn
dcpEnvMonTemperatureIndex = _DcpEnvMonTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 1, 1, 1, 1, 1),
    _DcpEnvMonTemperatureIndex_Type()
)
dcpEnvMonTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonTemperatureIndex.setStatus("current")
_DcpEnvMonTemperatureDescription_Type = DisplayString
_DcpEnvMonTemperatureDescription_Object = MibTableColumn
dcpEnvMonTemperatureDescription = _DcpEnvMonTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 1, 1, 1, 1, 2),
    _DcpEnvMonTemperatureDescription_Type()
)
dcpEnvMonTemperatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonTemperatureDescription.setStatus("current")
_DcpEnvMonTemperatureValue_Type = DcpTenths
_DcpEnvMonTemperatureValue_Object = MibTableColumn
dcpEnvMonTemperatureValue = _DcpEnvMonTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 1, 1, 1, 1, 3),
    _DcpEnvMonTemperatureValue_Type()
)
dcpEnvMonTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonTemperatureValue.setStatus("current")
_DcpEnvMonPowerConsumption_ObjectIdentity = ObjectIdentity
dcpEnvMonPowerConsumption = _DcpEnvMonPowerConsumption_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 2)
)
_DcpEnvMonPowerConsumptionObjects_ObjectIdentity = ObjectIdentity
dcpEnvMonPowerConsumptionObjects = _DcpEnvMonPowerConsumptionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 2, 1)
)
_DcpEnvMonPowerConsumptionTable_Object = MibTable
dcpEnvMonPowerConsumptionTable = _DcpEnvMonPowerConsumptionTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dcpEnvMonPowerConsumptionTable.setStatus("current")
_DcpEnvMonPowerConsumptionEntry_Object = MibTableRow
dcpEnvMonPowerConsumptionEntry = _DcpEnvMonPowerConsumptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 2, 1, 1, 1)
)
dcpEnvMonPowerConsumptionEntry.setIndexNames(
    (0, "DCP-ENV-MON-MIB", "dcpEnvMonPowerConsumptionIndex"),
)
if mibBuilder.loadTexts:
    dcpEnvMonPowerConsumptionEntry.setStatus("current")
_DcpEnvMonPowerConsumptionIndex_Type = Unsigned32
_DcpEnvMonPowerConsumptionIndex_Object = MibTableColumn
dcpEnvMonPowerConsumptionIndex = _DcpEnvMonPowerConsumptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 2, 1, 1, 1, 1),
    _DcpEnvMonPowerConsumptionIndex_Type()
)
dcpEnvMonPowerConsumptionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonPowerConsumptionIndex.setStatus("current")
_DcpEnvMonPowerConsumptionDescription_Type = DisplayString
_DcpEnvMonPowerConsumptionDescription_Object = MibTableColumn
dcpEnvMonPowerConsumptionDescription = _DcpEnvMonPowerConsumptionDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 2, 1, 1, 1, 2),
    _DcpEnvMonPowerConsumptionDescription_Type()
)
dcpEnvMonPowerConsumptionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonPowerConsumptionDescription.setStatus("current")
_DcpEnvMonPowerConsumptionValue_Type = Integer32
_DcpEnvMonPowerConsumptionValue_Object = MibTableColumn
dcpEnvMonPowerConsumptionValue = _DcpEnvMonPowerConsumptionValue_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 2, 1, 1, 1, 3),
    _DcpEnvMonPowerConsumptionValue_Type()
)
dcpEnvMonPowerConsumptionValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonPowerConsumptionValue.setStatus("current")
_DcpEnvMonFan_ObjectIdentity = ObjectIdentity
dcpEnvMonFan = _DcpEnvMonFan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3)
)
_DcpEnvMonFanObjects_ObjectIdentity = ObjectIdentity
dcpEnvMonFanObjects = _DcpEnvMonFanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1)
)
_DcpEnvMonFanTable_Object = MibTable
dcpEnvMonFanTable = _DcpEnvMonFanTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    dcpEnvMonFanTable.setStatus("current")
_DcpEnvMonFanEntry_Object = MibTableRow
dcpEnvMonFanEntry = _DcpEnvMonFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1, 1, 1)
)
dcpEnvMonFanEntry.setIndexNames(
    (0, "DCP-ENV-MON-MIB", "dcpEnvMonFanIndex"),
)
if mibBuilder.loadTexts:
    dcpEnvMonFanEntry.setStatus("current")
_DcpEnvMonFanIndex_Type = Unsigned32
_DcpEnvMonFanIndex_Object = MibTableColumn
dcpEnvMonFanIndex = _DcpEnvMonFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1, 1, 1, 1),
    _DcpEnvMonFanIndex_Type()
)
dcpEnvMonFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonFanIndex.setStatus("current")
_DcpEnvMonFanDescription_Type = DisplayString
_DcpEnvMonFanDescription_Object = MibTableColumn
dcpEnvMonFanDescription = _DcpEnvMonFanDescription_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1, 1, 1, 2),
    _DcpEnvMonFanDescription_Type()
)
dcpEnvMonFanDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonFanDescription.setStatus("current")
_DcpEnvMonFanStatus_Type = FanStatus
_DcpEnvMonFanStatus_Object = MibTableColumn
dcpEnvMonFanStatus = _DcpEnvMonFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1, 1, 1, 3),
    _DcpEnvMonFanStatus_Type()
)
dcpEnvMonFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonFanStatus.setStatus("current")
_DcpEnvMonFanMode_Type = FanMode
_DcpEnvMonFanMode_Object = MibTableColumn
dcpEnvMonFanMode = _DcpEnvMonFanMode_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1, 1, 1, 4),
    _DcpEnvMonFanMode_Type()
)
dcpEnvMonFanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonFanMode.setStatus("current")
_DcpEnvMonFanSpeed_Type = Unsigned32
_DcpEnvMonFanSpeed_Object = MibTableColumn
dcpEnvMonFanSpeed = _DcpEnvMonFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 30826, 2, 2, 6, 1, 3, 1, 1, 1, 5),
    _DcpEnvMonFanSpeed_Type()
)
dcpEnvMonFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcpEnvMonFanSpeed.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DCP-ENV-MON-MIB",
    **{"dcpEnv": dcpEnv,
       "dcpEnvMon": dcpEnvMon,
       "dcpEnvMonTemperature": dcpEnvMonTemperature,
       "dcpEnvMonTemperatureObjects": dcpEnvMonTemperatureObjects,
       "dcpEnvMonTemperatureTable": dcpEnvMonTemperatureTable,
       "dcpEnvMonTemperatureEntry": dcpEnvMonTemperatureEntry,
       "dcpEnvMonTemperatureIndex": dcpEnvMonTemperatureIndex,
       "dcpEnvMonTemperatureDescription": dcpEnvMonTemperatureDescription,
       "dcpEnvMonTemperatureValue": dcpEnvMonTemperatureValue,
       "dcpEnvMonPowerConsumption": dcpEnvMonPowerConsumption,
       "dcpEnvMonPowerConsumptionObjects": dcpEnvMonPowerConsumptionObjects,
       "dcpEnvMonPowerConsumptionTable": dcpEnvMonPowerConsumptionTable,
       "dcpEnvMonPowerConsumptionEntry": dcpEnvMonPowerConsumptionEntry,
       "dcpEnvMonPowerConsumptionIndex": dcpEnvMonPowerConsumptionIndex,
       "dcpEnvMonPowerConsumptionDescription": dcpEnvMonPowerConsumptionDescription,
       "dcpEnvMonPowerConsumptionValue": dcpEnvMonPowerConsumptionValue,
       "dcpEnvMonFan": dcpEnvMonFan,
       "dcpEnvMonFanObjects": dcpEnvMonFanObjects,
       "dcpEnvMonFanTable": dcpEnvMonFanTable,
       "dcpEnvMonFanEntry": dcpEnvMonFanEntry,
       "dcpEnvMonFanIndex": dcpEnvMonFanIndex,
       "dcpEnvMonFanDescription": dcpEnvMonFanDescription,
       "dcpEnvMonFanStatus": dcpEnvMonFanStatus,
       "dcpEnvMonFanMode": dcpEnvMonFanMode,
       "dcpEnvMonFanSpeed": dcpEnvMonFanSpeed}
)
