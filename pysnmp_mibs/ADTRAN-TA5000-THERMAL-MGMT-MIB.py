# SNMP MIB module (ADTRAN-TA5000-THERMAL-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TA5000-THERMAL-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:05 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTa5kThermalManagement,
 adTa5kThermalManagementID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adTa5kThermalManagement",
    "adTa5kThermalManagementID")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adIdentity,
 adMgmt,
 adProducts) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity",
    "adMgmt",
    "adProducts")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adTa5kThermalMgmtModuleIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 39, 1)
)
if mibBuilder.loadTexts:
    adTa5kThermalMgmtModuleIdentity.setRevisions(
        ("2013-11-25 00:00",
         "2013-08-01 21:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTA5kThermalMgmtmg_ObjectIdentity = ObjectIdentity
adTA5kThermalMgmtmg = _AdTA5kThermalMgmtmg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1)
)
_AdTA5kThermal_ObjectIdentity = ObjectIdentity
adTA5kThermal = _AdTA5kThermal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1)
)
_AdTA5kThermalSlotTable_Object = MibTable
adTA5kThermalSlotTable = _AdTA5kThermalSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adTA5kThermalSlotTable.setStatus("current")
_AdTA5kThermalSlotEntry_Object = MibTableRow
adTA5kThermalSlotEntry = _AdTA5kThermalSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 1, 1)
)
adTA5kThermalSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adTA5kThermalSlotEntry.setStatus("current")
_AdTA5kThermalSlotNumSensors_Type = Integer32
_AdTA5kThermalSlotNumSensors_Object = MibTableColumn
adTA5kThermalSlotNumSensors = _AdTA5kThermalSlotNumSensors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 1, 1, 1),
    _AdTA5kThermalSlotNumSensors_Type()
)
adTA5kThermalSlotNumSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kThermalSlotNumSensors.setStatus("current")
_AdTA5kThermalManagementTable_Object = MibTable
adTA5kThermalManagementTable = _AdTA5kThermalManagementTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 2)
)
if mibBuilder.loadTexts:
    adTA5kThermalManagementTable.setStatus("current")
_AdTA5kThermalManagementEntry_Object = MibTableRow
adTA5kThermalManagementEntry = _AdTA5kThermalManagementEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 2, 1)
)
adTA5kThermalManagementEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-TA5000-THERMAL-MGMT-MIB", "adTA5kThermalManagementSensorId"),
)
if mibBuilder.loadTexts:
    adTA5kThermalManagementEntry.setStatus("current")
_AdTA5kThermalManagementSensorId_Type = Integer32
_AdTA5kThermalManagementSensorId_Object = MibTableColumn
adTA5kThermalManagementSensorId = _AdTA5kThermalManagementSensorId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 2, 1, 1),
    _AdTA5kThermalManagementSensorId_Type()
)
adTA5kThermalManagementSensorId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTA5kThermalManagementSensorId.setStatus("current")
_AdTA5kThermalManagementSensorName_Type = DisplayString
_AdTA5kThermalManagementSensorName_Object = MibTableColumn
adTA5kThermalManagementSensorName = _AdTA5kThermalManagementSensorName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 2, 1, 2),
    _AdTA5kThermalManagementSensorName_Type()
)
adTA5kThermalManagementSensorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kThermalManagementSensorName.setStatus("current")
_AdTA5kThermalManagementSensorCurrTemp_Type = Integer32
_AdTA5kThermalManagementSensorCurrTemp_Object = MibTableColumn
adTA5kThermalManagementSensorCurrTemp = _AdTA5kThermalManagementSensorCurrTemp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 1, 1, 2, 1, 3),
    _AdTA5kThermalManagementSensorCurrTemp_Type()
)
adTA5kThermalManagementSensorCurrTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTA5kThermalManagementSensorCurrTemp.setStatus("current")
if mibBuilder.loadTexts:
    adTA5kThermalManagementSensorCurrTemp.setUnits("0.1C")
_AdTA5kThermalEventsFix_ObjectIdentity = ObjectIdentity
adTA5kThermalEventsFix = _AdTA5kThermalEventsFix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 2)
)
_AdTa5kThermalEvents_ObjectIdentity = ObjectIdentity
adTa5kThermalEvents = _AdTa5kThermalEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 2, 0)
)

# Managed Objects groups


# Notification objects

adTA5kSlotCriticalTempActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 2, 0, 1)
)
adTA5kSlotCriticalTempActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TA5000-THERMAL-MGMT-MIB", "adTA5kThermalManagementSensorCurrTemp"))
)
if mibBuilder.loadTexts:
    adTA5kSlotCriticalTempActive.setStatus(
        "current"
    )

adTA5kSlotCriticalTempClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 2, 0, 2)
)
adTA5kSlotCriticalTempClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TA5000-THERMAL-MGMT-MIB", "adTA5kThermalManagementSensorCurrTemp"))
)
if mibBuilder.loadTexts:
    adTA5kSlotCriticalTempClear.setStatus(
        "current"
    )

adTa5kRemoteDeviceCriticalTempActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 2, 0, 3)
)
adTa5kRemoteDeviceCriticalTempActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRemoteDeviceCriticalTempActive.setStatus(
        "current"
    )

adTa5kRemoteDeviceCriticalTempClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 39, 2, 0, 4)
)
adTa5kRemoteDeviceCriticalTempClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adTa5kRemoteDeviceCriticalTempClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TA5000-THERMAL-MGMT-MIB",
    **{"adTA5kThermalMgmtmg": adTA5kThermalMgmtmg,
       "adTA5kThermal": adTA5kThermal,
       "adTA5kThermalSlotTable": adTA5kThermalSlotTable,
       "adTA5kThermalSlotEntry": adTA5kThermalSlotEntry,
       "adTA5kThermalSlotNumSensors": adTA5kThermalSlotNumSensors,
       "adTA5kThermalManagementTable": adTA5kThermalManagementTable,
       "adTA5kThermalManagementEntry": adTA5kThermalManagementEntry,
       "adTA5kThermalManagementSensorId": adTA5kThermalManagementSensorId,
       "adTA5kThermalManagementSensorName": adTA5kThermalManagementSensorName,
       "adTA5kThermalManagementSensorCurrTemp": adTA5kThermalManagementSensorCurrTemp,
       "adTA5kThermalEventsFix": adTA5kThermalEventsFix,
       "adTa5kThermalEvents": adTa5kThermalEvents,
       "adTA5kSlotCriticalTempActive": adTA5kSlotCriticalTempActive,
       "adTA5kSlotCriticalTempClear": adTA5kSlotCriticalTempClear,
       "adTa5kRemoteDeviceCriticalTempActive": adTa5kRemoteDeviceCriticalTempActive,
       "adTa5kRemoteDeviceCriticalTempClear": adTa5kRemoteDeviceCriticalTempClear,
       "adTa5kThermalMgmtModuleIdentity": adTa5kThermalMgmtModuleIdentity}
)
