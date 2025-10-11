# SNMP MIB module (ADTRAN-GENPROCESSES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENPROCESSES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:55 2025
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

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenProcesses,
 adGenProcessesID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenProcesses",
    "adGenProcessesID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

adGenProcessesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 22, 1)
)
if mibBuilder.loadTexts:
    adGenProcessesMIB.setRevisions(
        ("2017-06-23 00:00",
         "2011-09-23 00:00",
         "2010-02-23 00:00",
         "2010-02-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenProcessesNotifications_ObjectIdentity = ObjectIdentity
adGenProcessesNotifications = _AdGenProcessesNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 0)
)
_AdGenProcessesProvisioning_ObjectIdentity = ObjectIdentity
adGenProcessesProvisioning = _AdGenProcessesProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 1)
)
_AdGenProcessesProvTable_Object = MibTable
adGenProcessesProvTable = _AdGenProcessesProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 1, 1)
)
if mibBuilder.loadTexts:
    adGenProcessesProvTable.setStatus("current")
_AdGenProcessesProvEntry_Object = MibTableRow
adGenProcessesProvEntry = _AdGenProcessesProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 1, 1, 1)
)
adGenProcessesProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenProcessesProvEntry.setStatus("current")


class _AdGenProcessesProvHeapFreeThreshold_Type(Unsigned32):
    """Custom type adGenProcessesProvHeapFreeThreshold based on Unsigned32"""
    defaultValue = 0


_AdGenProcessesProvHeapFreeThreshold_Type.__name__ = "Unsigned32"
_AdGenProcessesProvHeapFreeThreshold_Object = MibTableColumn
adGenProcessesProvHeapFreeThreshold = _AdGenProcessesProvHeapFreeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 1, 1, 1, 1),
    _AdGenProcessesProvHeapFreeThreshold_Type()
)
adGenProcessesProvHeapFreeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenProcessesProvHeapFreeThreshold.setStatus("current")
if mibBuilder.loadTexts:
    adGenProcessesProvHeapFreeThreshold.setUnits("bytes")


class _AdGenProcessesStarvationAlarmEnable_Type(Integer32):
    """Custom type adGenProcessesStarvationAlarmEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdGenProcessesStarvationAlarmEnable_Type.__name__ = "Integer32"
_AdGenProcessesStarvationAlarmEnable_Object = MibTableColumn
adGenProcessesStarvationAlarmEnable = _AdGenProcessesStarvationAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 1, 1, 1, 2),
    _AdGenProcessesStarvationAlarmEnable_Type()
)
adGenProcessesStarvationAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenProcessesStarvationAlarmEnable.setStatus("current")


class _AdGenProcessesDeadlockAlarmEnable_Type(Integer32):
    """Custom type adGenProcessesDeadlockAlarmEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AdGenProcessesDeadlockAlarmEnable_Type.__name__ = "Integer32"
_AdGenProcessesDeadlockAlarmEnable_Object = MibTableColumn
adGenProcessesDeadlockAlarmEnable = _AdGenProcessesDeadlockAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 1, 1, 1, 3),
    _AdGenProcessesDeadlockAlarmEnable_Type()
)
adGenProcessesDeadlockAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenProcessesDeadlockAlarmEnable.setStatus("current")
_AdGenProcessesStatus_ObjectIdentity = ObjectIdentity
adGenProcessesStatus = _AdGenProcessesStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2)
)
_AdGenProcessesMemStatTable_Object = MibTable
adGenProcessesMemStatTable = _AdGenProcessesMemStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1)
)
if mibBuilder.loadTexts:
    adGenProcessesMemStatTable.setStatus("current")
_AdGenProcessesMemStatEntry_Object = MibTableRow
adGenProcessesMemStatEntry = _AdGenProcessesMemStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1, 1)
)
adGenProcessesMemStatEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenProcessesMemStatEntry.setStatus("current")
_AdGenProcessesMemStatHeapSize_Type = Unsigned32
_AdGenProcessesMemStatHeapSize_Object = MibTableColumn
adGenProcessesMemStatHeapSize = _AdGenProcessesMemStatHeapSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1, 1, 1),
    _AdGenProcessesMemStatHeapSize_Type()
)
adGenProcessesMemStatHeapSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesMemStatHeapSize.setStatus("current")
if mibBuilder.loadTexts:
    adGenProcessesMemStatHeapSize.setUnits("bytes")
_AdGenProcessesMemStatHeapUsed_Type = Unsigned32
_AdGenProcessesMemStatHeapUsed_Object = MibTableColumn
adGenProcessesMemStatHeapUsed = _AdGenProcessesMemStatHeapUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1, 1, 2),
    _AdGenProcessesMemStatHeapUsed_Type()
)
adGenProcessesMemStatHeapUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesMemStatHeapUsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenProcessesMemStatHeapUsed.setUnits("bytes")
_AdGenProcessesMemStatHeapFree_Type = Unsigned32
_AdGenProcessesMemStatHeapFree_Object = MibTableColumn
adGenProcessesMemStatHeapFree = _AdGenProcessesMemStatHeapFree_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1, 1, 3),
    _AdGenProcessesMemStatHeapFree_Type()
)
adGenProcessesMemStatHeapFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesMemStatHeapFree.setStatus("current")
if mibBuilder.loadTexts:
    adGenProcessesMemStatHeapFree.setUnits("bytes")
_AdGenProcessesMemStatBlockMgrSize_Type = Unsigned32
_AdGenProcessesMemStatBlockMgrSize_Object = MibTableColumn
adGenProcessesMemStatBlockMgrSize = _AdGenProcessesMemStatBlockMgrSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1, 1, 4),
    _AdGenProcessesMemStatBlockMgrSize_Type()
)
adGenProcessesMemStatBlockMgrSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesMemStatBlockMgrSize.setStatus("current")
if mibBuilder.loadTexts:
    adGenProcessesMemStatBlockMgrSize.setUnits("bytes")
_AdGenProcessesMemStatBlockMgrUsed_Type = Unsigned32
_AdGenProcessesMemStatBlockMgrUsed_Object = MibTableColumn
adGenProcessesMemStatBlockMgrUsed = _AdGenProcessesMemStatBlockMgrUsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1, 1, 5),
    _AdGenProcessesMemStatBlockMgrUsed_Type()
)
adGenProcessesMemStatBlockMgrUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesMemStatBlockMgrUsed.setStatus("current")
if mibBuilder.loadTexts:
    adGenProcessesMemStatBlockMgrUsed.setUnits("bytes")
_AdGenProcessesMemStatBlockMgrFree_Type = Unsigned32
_AdGenProcessesMemStatBlockMgrFree_Object = MibTableColumn
adGenProcessesMemStatBlockMgrFree = _AdGenProcessesMemStatBlockMgrFree_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 1, 1, 6),
    _AdGenProcessesMemStatBlockMgrFree_Type()
)
adGenProcessesMemStatBlockMgrFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesMemStatBlockMgrFree.setStatus("current")
if mibBuilder.loadTexts:
    adGenProcessesMemStatBlockMgrFree.setUnits("bytes")
_AdGenProcessesCpuStatTable_Object = MibTable
adGenProcessesCpuStatTable = _AdGenProcessesCpuStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 2)
)
if mibBuilder.loadTexts:
    adGenProcessesCpuStatTable.setStatus("current")
_AdGenProcessesCpuStatEntry_Object = MibTableRow
adGenProcessesCpuStatEntry = _AdGenProcessesCpuStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 2, 1)
)
adGenProcessesCpuStatEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenProcessesCpuStatEntry.setStatus("current")


class _AdGenProcessesCpuStatCurUtilization_Type(Integer32):
    """Custom type adGenProcessesCpuStatCurUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AdGenProcessesCpuStatCurUtilization_Type.__name__ = "Integer32"
_AdGenProcessesCpuStatCurUtilization_Object = MibTableColumn
adGenProcessesCpuStatCurUtilization = _AdGenProcessesCpuStatCurUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 2, 1, 1),
    _AdGenProcessesCpuStatCurUtilization_Type()
)
adGenProcessesCpuStatCurUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesCpuStatCurUtilization.setStatus("current")


class _AdGenProcessesCpuStatMaxUtilization_Type(Integer32):
    """Custom type adGenProcessesCpuStatMaxUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AdGenProcessesCpuStatMaxUtilization_Type.__name__ = "Integer32"
_AdGenProcessesCpuStatMaxUtilization_Object = MibTableColumn
adGenProcessesCpuStatMaxUtilization = _AdGenProcessesCpuStatMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 2, 2, 1, 2),
    _AdGenProcessesCpuStatMaxUtilization_Type()
)
adGenProcessesCpuStatMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenProcessesCpuStatMaxUtilization.setStatus("current")

# Managed Objects groups


# Notification objects

adGenProcessesHeapFreeThreshCrossed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 0, 1)
)
adGenProcessesHeapFreeThreshCrossed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPROCESSES-MIB", "adGenProcessesProvHeapFreeThreshold"),
        ("ADTRAN-GENPROCESSES-MIB", "adGenProcessesMemStatHeapFree"))
)
if mibBuilder.loadTexts:
    adGenProcessesHeapFreeThreshCrossed.setStatus(
        "current"
    )

adGenProcessesStarvationAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 0, 2)
)
adGenProcessesStarvationAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenProcessesStarvationAlarmClr.setStatus(
        "current"
    )

adGenProcessesStarvationAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 0, 3)
)
adGenProcessesStarvationAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenProcessesStarvationAlarmAct.setStatus(
        "current"
    )

adGenProcessesDeadlockAlarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 0, 4)
)
adGenProcessesDeadlockAlarmClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenProcessesDeadlockAlarmClr.setStatus(
        "current"
    )

adGenProcessesDeadlockAlarmAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 22, 0, 5)
)
adGenProcessesDeadlockAlarmAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adGenProcessesDeadlockAlarmAct.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENPROCESSES-MIB",
    **{"adGenProcessesNotifications": adGenProcessesNotifications,
       "adGenProcessesHeapFreeThreshCrossed": adGenProcessesHeapFreeThreshCrossed,
       "adGenProcessesStarvationAlarmClr": adGenProcessesStarvationAlarmClr,
       "adGenProcessesStarvationAlarmAct": adGenProcessesStarvationAlarmAct,
       "adGenProcessesDeadlockAlarmClr": adGenProcessesDeadlockAlarmClr,
       "adGenProcessesDeadlockAlarmAct": adGenProcessesDeadlockAlarmAct,
       "adGenProcessesProvisioning": adGenProcessesProvisioning,
       "adGenProcessesProvTable": adGenProcessesProvTable,
       "adGenProcessesProvEntry": adGenProcessesProvEntry,
       "adGenProcessesProvHeapFreeThreshold": adGenProcessesProvHeapFreeThreshold,
       "adGenProcessesStarvationAlarmEnable": adGenProcessesStarvationAlarmEnable,
       "adGenProcessesDeadlockAlarmEnable": adGenProcessesDeadlockAlarmEnable,
       "adGenProcessesStatus": adGenProcessesStatus,
       "adGenProcessesMemStatTable": adGenProcessesMemStatTable,
       "adGenProcessesMemStatEntry": adGenProcessesMemStatEntry,
       "adGenProcessesMemStatHeapSize": adGenProcessesMemStatHeapSize,
       "adGenProcessesMemStatHeapUsed": adGenProcessesMemStatHeapUsed,
       "adGenProcessesMemStatHeapFree": adGenProcessesMemStatHeapFree,
       "adGenProcessesMemStatBlockMgrSize": adGenProcessesMemStatBlockMgrSize,
       "adGenProcessesMemStatBlockMgrUsed": adGenProcessesMemStatBlockMgrUsed,
       "adGenProcessesMemStatBlockMgrFree": adGenProcessesMemStatBlockMgrFree,
       "adGenProcessesCpuStatTable": adGenProcessesCpuStatTable,
       "adGenProcessesCpuStatEntry": adGenProcessesCpuStatEntry,
       "adGenProcessesCpuStatCurUtilization": adGenProcessesCpuStatCurUtilization,
       "adGenProcessesCpuStatMaxUtilization": adGenProcessesCpuStatMaxUtilization,
       "adGenProcessesMIB": adGenProcessesMIB}
)
