# SNMP MIB module (RAISECOM-ALARM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-ALARM-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:30 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 Opaque,
 TimeTicks,
 Unsigned32,
 iso,
 mib_2,
 zeroDotZero) = mibBuilder.importSymbols(
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "iso",
    "mib-2",
    "zeroDotZero")

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

raisecomAlarmMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmStorageMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("loop", 2))
    )



class AlarmInverseMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("auto", 2),
          ("manual", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RaisecomAlarmMgmtObejcts_ObjectIdentity = ObjectIdentity
raisecomAlarmMgmtObejcts = _RaisecomAlarmMgmtObejcts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1)
)


class _RaisecomAlarmMgmtRaiseDelay_Type(Integer32):
    """Custom type raisecomAlarmMgmtRaiseDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_RaisecomAlarmMgmtRaiseDelay_Type.__name__ = "Integer32"
_RaisecomAlarmMgmtRaiseDelay_Object = MibScalar
raisecomAlarmMgmtRaiseDelay = _RaisecomAlarmMgmtRaiseDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 1),
    _RaisecomAlarmMgmtRaiseDelay_Type()
)
raisecomAlarmMgmtRaiseDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtRaiseDelay.setStatus("current")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtRaiseDelay.setUnits("seconds")


class _RaisecomAlarmMgmtClearDelay_Type(Integer32):
    """Custom type raisecomAlarmMgmtClearDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_RaisecomAlarmMgmtClearDelay_Type.__name__ = "Integer32"
_RaisecomAlarmMgmtClearDelay_Object = MibScalar
raisecomAlarmMgmtClearDelay = _RaisecomAlarmMgmtClearDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 2),
    _RaisecomAlarmMgmtClearDelay_Type()
)
raisecomAlarmMgmtClearDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtClearDelay.setStatus("current")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtClearDelay.setUnits("seconds")
_RaisecomAlarmMgmtActiveStoreMode_Type = AlarmStorageMode
_RaisecomAlarmMgmtActiveStoreMode_Object = MibScalar
raisecomAlarmMgmtActiveStoreMode = _RaisecomAlarmMgmtActiveStoreMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 3),
    _RaisecomAlarmMgmtActiveStoreMode_Type()
)
raisecomAlarmMgmtActiveStoreMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtActiveStoreMode.setStatus("current")


class _RaisecomAlarmMgmtInhibitEnable_Type(TruthValue):
    """Custom type raisecomAlarmMgmtInhibitEnable based on TruthValue"""
    defaultValue = 1


_RaisecomAlarmMgmtInhibitEnable_Type.__name__ = "TruthValue"
_RaisecomAlarmMgmtInhibitEnable_Object = MibScalar
raisecomAlarmMgmtInhibitEnable = _RaisecomAlarmMgmtInhibitEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 4),
    _RaisecomAlarmMgmtInhibitEnable_Type()
)
raisecomAlarmMgmtInhibitEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtInhibitEnable.setStatus("current")


class _RaisecomAlarmMgmtSyslogEnable_Type(TruthValue):
    """Custom type raisecomAlarmMgmtSyslogEnable based on TruthValue"""
    defaultValue = 1


_RaisecomAlarmMgmtSyslogEnable_Type.__name__ = "TruthValue"
_RaisecomAlarmMgmtSyslogEnable_Object = MibScalar
raisecomAlarmMgmtSyslogEnable = _RaisecomAlarmMgmtSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 5),
    _RaisecomAlarmMgmtSyslogEnable_Type()
)
raisecomAlarmMgmtSyslogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtSyslogEnable.setStatus("current")
_RaisecomAlarmMgmtActiveClear_Type = Integer32
_RaisecomAlarmMgmtActiveClear_Object = MibScalar
raisecomAlarmMgmtActiveClear = _RaisecomAlarmMgmtActiveClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 6),
    _RaisecomAlarmMgmtActiveClear_Type()
)
raisecomAlarmMgmtActiveClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtActiveClear.setStatus("current")
_RaisecomAlarmMgmtConfigTable_Object = MibTable
raisecomAlarmMgmtConfigTable = _RaisecomAlarmMgmtConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7)
)
if mibBuilder.loadTexts:
    raisecomAlarmMgmtConfigTable.setStatus("current")
_RaisecomAlarmMgmtConfigEntry_Object = MibTableRow
raisecomAlarmMgmtConfigEntry = _RaisecomAlarmMgmtConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1)
)
raisecomAlarmMgmtConfigEntry.setIndexNames(
    (0, "RAISECOM-ALARM-MGMT-MIB", "raisecomAlarmMgmtId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomAlarmMgmtConfigEntry.setStatus("current")
_RaisecomAlarmMgmtId_Type = Unsigned32
_RaisecomAlarmMgmtId_Object = MibTableColumn
raisecomAlarmMgmtId = _RaisecomAlarmMgmtId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 1),
    _RaisecomAlarmMgmtId_Type()
)
raisecomAlarmMgmtId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtId.setStatus("current")


class _RaisecomAlarmMgmtClear_Type(TruthValue):
    """Custom type raisecomAlarmMgmtClear based on TruthValue"""
    defaultValue = 2


_RaisecomAlarmMgmtClear_Type.__name__ = "TruthValue"
_RaisecomAlarmMgmtClear_Object = MibTableColumn
raisecomAlarmMgmtClear = _RaisecomAlarmMgmtClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 2),
    _RaisecomAlarmMgmtClear_Type()
)
raisecomAlarmMgmtClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtClear.setStatus("current")


class _RaisecomAlarmMgmtReportEnable_Type(TruthValue):
    """Custom type raisecomAlarmMgmtReportEnable based on TruthValue"""
    defaultValue = 1


_RaisecomAlarmMgmtReportEnable_Type.__name__ = "TruthValue"
_RaisecomAlarmMgmtReportEnable_Object = MibTableColumn
raisecomAlarmMgmtReportEnable = _RaisecomAlarmMgmtReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 3),
    _RaisecomAlarmMgmtReportEnable_Type()
)
raisecomAlarmMgmtReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtReportEnable.setStatus("current")


class _RaisecomAlarmMgmtMonitorEnable_Type(TruthValue):
    """Custom type raisecomAlarmMgmtMonitorEnable based on TruthValue"""
    defaultValue = 1


_RaisecomAlarmMgmtMonitorEnable_Type.__name__ = "TruthValue"
_RaisecomAlarmMgmtMonitorEnable_Object = MibTableColumn
raisecomAlarmMgmtMonitorEnable = _RaisecomAlarmMgmtMonitorEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 4),
    _RaisecomAlarmMgmtMonitorEnable_Type()
)
raisecomAlarmMgmtMonitorEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtMonitorEnable.setStatus("current")


class _RaisecomAlarmMgmtInverseMode_Type(AlarmInverseMode):
    """Custom type raisecomAlarmMgmtInverseMode based on AlarmInverseMode"""
    defaultValue = 1


_RaisecomAlarmMgmtInverseMode_Type.__name__ = "AlarmInverseMode"
_RaisecomAlarmMgmtInverseMode_Object = MibTableColumn
raisecomAlarmMgmtInverseMode = _RaisecomAlarmMgmtInverseMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 5),
    _RaisecomAlarmMgmtInverseMode_Type()
)
raisecomAlarmMgmtInverseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtInverseMode.setStatus("current")


class _RaisecomAlarmMgmtModuleName_Type(SnmpAdminString):
    """Custom type raisecomAlarmMgmtModuleName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RaisecomAlarmMgmtModuleName_Type.__name__ = "SnmpAdminString"
_RaisecomAlarmMgmtModuleName_Object = MibTableColumn
raisecomAlarmMgmtModuleName = _RaisecomAlarmMgmtModuleName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 6),
    _RaisecomAlarmMgmtModuleName_Type()
)
raisecomAlarmMgmtModuleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtModuleName.setStatus("current")


class _RaisecomAlarmMgmtGroupName_Type(SnmpAdminString):
    """Custom type raisecomAlarmMgmtGroupName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RaisecomAlarmMgmtGroupName_Type.__name__ = "SnmpAdminString"
_RaisecomAlarmMgmtGroupName_Object = MibTableColumn
raisecomAlarmMgmtGroupName = _RaisecomAlarmMgmtGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 34, 1, 7, 1, 7),
    _RaisecomAlarmMgmtGroupName_Type()
)
raisecomAlarmMgmtGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomAlarmMgmtGroupName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-ALARM-MGMT-MIB",
    **{"AlarmStorageMode": AlarmStorageMode,
       "AlarmInverseMode": AlarmInverseMode,
       "raisecomAlarmMgmt": raisecomAlarmMgmt,
       "raisecomAlarmMgmtObejcts": raisecomAlarmMgmtObejcts,
       "raisecomAlarmMgmtRaiseDelay": raisecomAlarmMgmtRaiseDelay,
       "raisecomAlarmMgmtClearDelay": raisecomAlarmMgmtClearDelay,
       "raisecomAlarmMgmtActiveStoreMode": raisecomAlarmMgmtActiveStoreMode,
       "raisecomAlarmMgmtInhibitEnable": raisecomAlarmMgmtInhibitEnable,
       "raisecomAlarmMgmtSyslogEnable": raisecomAlarmMgmtSyslogEnable,
       "raisecomAlarmMgmtActiveClear": raisecomAlarmMgmtActiveClear,
       "raisecomAlarmMgmtConfigTable": raisecomAlarmMgmtConfigTable,
       "raisecomAlarmMgmtConfigEntry": raisecomAlarmMgmtConfigEntry,
       "raisecomAlarmMgmtId": raisecomAlarmMgmtId,
       "raisecomAlarmMgmtClear": raisecomAlarmMgmtClear,
       "raisecomAlarmMgmtReportEnable": raisecomAlarmMgmtReportEnable,
       "raisecomAlarmMgmtMonitorEnable": raisecomAlarmMgmtMonitorEnable,
       "raisecomAlarmMgmtInverseMode": raisecomAlarmMgmtInverseMode,
       "raisecomAlarmMgmtModuleName": raisecomAlarmMgmtModuleName,
       "raisecomAlarmMgmtGroupName": raisecomAlarmMgmtGroupName}
)
