# SNMP MIB module (ME1200-SYSUTIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cisco/ME1200-SYSUTIL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:40:49 2025
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

(me1200SwitchMgmt,) = mibBuilder.importSymbols(
    "CISCOME1200-MIB",
    "me1200SwitchMgmt")

(ME1200DisplayString,
 ME1200Unsigned8) = mibBuilder.importSymbols(
    "ME1200-TC",
    "ME1200DisplayString",
    "ME1200Unsigned8")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

me1200SysutilMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24)
)
if mibBuilder.loadTexts:
    me1200SysutilMib.setRevisions(
        ("2017-07-10 00:00",
         "2016-05-06 00:00",
         "2016-04-28 00:00",
         "2016-04-26 00:00",
         "2016-03-01 00:00",
         "2014-11-06 00:00",
         "2014-04-28 00:00",
         "2014-01-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ME1200SysutilPowerSupplyStateType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 0),
          ("standby", 1),
          ("notPresent", 2))
    )



class ME1200SysutilRebootType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReboot", 0),
          ("coldReboot", 1),
          ("warmReboot", 2))
    )



class ME1200SysutilSystemLedClearType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("fatal", 1),
          ("software", 2),
          ("post", 3),
          ("ztp", 4),
          ("stackFwChk", 5))
    )



# MIB Managed Objects in the order of their OIDs

_Me1200SysutilMibObjects_ObjectIdentity = ObjectIdentity
me1200SysutilMibObjects = _Me1200SysutilMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1)
)
_Me1200SysutilCapabilities_ObjectIdentity = ObjectIdentity
me1200SysutilCapabilities = _Me1200SysutilCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 1)
)
_Me1200SysutilCapabilitiesWarmRebootSupported_Type = TruthValue
_Me1200SysutilCapabilitiesWarmRebootSupported_Object = MibScalar
me1200SysutilCapabilitiesWarmRebootSupported = _Me1200SysutilCapabilitiesWarmRebootSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 1, 1),
    _Me1200SysutilCapabilitiesWarmRebootSupported_Type()
)
me1200SysutilCapabilitiesWarmRebootSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilCapabilitiesWarmRebootSupported.setStatus("current")
_Me1200SysutilCapabilitiesPostSupported_Type = TruthValue
_Me1200SysutilCapabilitiesPostSupported_Object = MibScalar
me1200SysutilCapabilitiesPostSupported = _Me1200SysutilCapabilitiesPostSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 1, 2),
    _Me1200SysutilCapabilitiesPostSupported_Type()
)
me1200SysutilCapabilitiesPostSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilCapabilitiesPostSupported.setStatus("current")
_Me1200SysutilCapabilitiesZtpSupported_Type = TruthValue
_Me1200SysutilCapabilitiesZtpSupported_Object = MibScalar
me1200SysutilCapabilitiesZtpSupported = _Me1200SysutilCapabilitiesZtpSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 1, 3),
    _Me1200SysutilCapabilitiesZtpSupported_Type()
)
me1200SysutilCapabilitiesZtpSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilCapabilitiesZtpSupported.setStatus("current")
_Me1200SysutilCapabilitiesStackFwChkSupported_Type = TruthValue
_Me1200SysutilCapabilitiesStackFwChkSupported_Object = MibScalar
me1200SysutilCapabilitiesStackFwChkSupported = _Me1200SysutilCapabilitiesStackFwChkSupported_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 1, 4),
    _Me1200SysutilCapabilitiesStackFwChkSupported_Type()
)
me1200SysutilCapabilitiesStackFwChkSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilCapabilitiesStackFwChkSupported.setStatus("current")
_Me1200SysutilConfig_ObjectIdentity = ObjectIdentity
me1200SysutilConfig = _Me1200SysutilConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 2)
)
_Me1200SysutilConfigSystemMemoryPool_ObjectIdentity = ObjectIdentity
me1200SysutilConfigSystemMemoryPool = _Me1200SysutilConfigSystemMemoryPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 2, 1)
)
_Me1200SysutilConfigSystemMemoryPoolNotifThreshold_Type = Unsigned32
_Me1200SysutilConfigSystemMemoryPoolNotifThreshold_Object = MibScalar
me1200SysutilConfigSystemMemoryPoolNotifThreshold = _Me1200SysutilConfigSystemMemoryPoolNotifThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 2, 1, 1),
    _Me1200SysutilConfigSystemMemoryPoolNotifThreshold_Type()
)
me1200SysutilConfigSystemMemoryPoolNotifThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SysutilConfigSystemMemoryPoolNotifThreshold.setStatus("current")
_Me1200SysutilConfigSystemCpuLoad_ObjectIdentity = ObjectIdentity
me1200SysutilConfigSystemCpuLoad = _Me1200SysutilConfigSystemCpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 2, 2)
)
_Me1200SysutilConfigSystemCpuLoadMonitoringMode_Type = ME1200Unsigned8
_Me1200SysutilConfigSystemCpuLoadMonitoringMode_Object = MibScalar
me1200SysutilConfigSystemCpuLoadMonitoringMode = _Me1200SysutilConfigSystemCpuLoadMonitoringMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 2, 2, 1),
    _Me1200SysutilConfigSystemCpuLoadMonitoringMode_Type()
)
me1200SysutilConfigSystemCpuLoadMonitoringMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SysutilConfigSystemCpuLoadMonitoringMode.setStatus("current")
_Me1200SysutilConfigSystemCpuLoadMonitoringInterval_Type = Unsigned32
_Me1200SysutilConfigSystemCpuLoadMonitoringInterval_Object = MibScalar
me1200SysutilConfigSystemCpuLoadMonitoringInterval = _Me1200SysutilConfigSystemCpuLoadMonitoringInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 2, 2, 2),
    _Me1200SysutilConfigSystemCpuLoadMonitoringInterval_Type()
)
me1200SysutilConfigSystemCpuLoadMonitoringInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SysutilConfigSystemCpuLoadMonitoringInterval.setStatus("current")
_Me1200SysutilStatus_ObjectIdentity = ObjectIdentity
me1200SysutilStatus = _Me1200SysutilStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3)
)
_Me1200SysutilStatusCpuLoad_ObjectIdentity = ObjectIdentity
me1200SysutilStatusCpuLoad = _Me1200SysutilStatusCpuLoad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1)
)
_Me1200SysutilStatusCpuLoadAverage100msec_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage100msec_Object = MibScalar
me1200SysutilStatusCpuLoadAverage100msec = _Me1200SysutilStatusCpuLoadAverage100msec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 1),
    _Me1200SysutilStatusCpuLoadAverage100msec_Type()
)
me1200SysutilStatusCpuLoadAverage100msec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage100msec.setStatus("current")
_Me1200SysutilStatusCpuLoadAverage1sec_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage1sec_Object = MibScalar
me1200SysutilStatusCpuLoadAverage1sec = _Me1200SysutilStatusCpuLoadAverage1sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 2),
    _Me1200SysutilStatusCpuLoadAverage1sec_Type()
)
me1200SysutilStatusCpuLoadAverage1sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage1sec.setStatus("current")
_Me1200SysutilStatusCpuLoadAverage10sec_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage10sec_Object = MibScalar
me1200SysutilStatusCpuLoadAverage10sec = _Me1200SysutilStatusCpuLoadAverage10sec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 3),
    _Me1200SysutilStatusCpuLoadAverage10sec_Type()
)
me1200SysutilStatusCpuLoadAverage10sec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage10sec.setStatus("current")
_Me1200SysutilStatusCpuLoadAverage1min_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage1min_Object = MibScalar
me1200SysutilStatusCpuLoadAverage1min = _Me1200SysutilStatusCpuLoadAverage1min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 4),
    _Me1200SysutilStatusCpuLoadAverage1min_Type()
)
me1200SysutilStatusCpuLoadAverage1min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage1min.setStatus("current")
_Me1200SysutilStatusCpuLoadAverage5min_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage5min_Object = MibScalar
me1200SysutilStatusCpuLoadAverage5min = _Me1200SysutilStatusCpuLoadAverage5min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 5),
    _Me1200SysutilStatusCpuLoadAverage5min_Type()
)
me1200SysutilStatusCpuLoadAverage5min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage5min.setStatus("current")
_Me1200SysutilStatusCpuLoadAverage15min_Type = Unsigned32
_Me1200SysutilStatusCpuLoadAverage15min_Object = MibScalar
me1200SysutilStatusCpuLoadAverage15min = _Me1200SysutilStatusCpuLoadAverage15min_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 1, 6),
    _Me1200SysutilStatusCpuLoadAverage15min_Type()
)
me1200SysutilStatusCpuLoadAverage15min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadAverage15min.setStatus("current")
_Me1200SysutilStatusPowerSupplyTable_Object = MibTable
me1200SysutilStatusPowerSupplyTable = _Me1200SysutilStatusPowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2)
)
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyTable.setStatus("current")
_Me1200SysutilStatusPowerSupplyEntry_Object = MibTableRow
me1200SysutilStatusPowerSupplyEntry = _Me1200SysutilStatusPowerSupplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1)
)
me1200SysutilStatusPowerSupplyEntry.setIndexNames(
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplySwitchId"),
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyPsuId"),
)
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyEntry.setStatus("current")


class _Me1200SysutilStatusPowerSupplySwitchId_Type(Integer32):
    """Custom type me1200SysutilStatusPowerSupplySwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200SysutilStatusPowerSupplySwitchId_Type.__name__ = "Integer32"
_Me1200SysutilStatusPowerSupplySwitchId_Object = MibTableColumn
me1200SysutilStatusPowerSupplySwitchId = _Me1200SysutilStatusPowerSupplySwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 1),
    _Me1200SysutilStatusPowerSupplySwitchId_Type()
)
me1200SysutilStatusPowerSupplySwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplySwitchId.setStatus("current")


class _Me1200SysutilStatusPowerSupplyPsuId_Type(Integer32):
    """Custom type me1200SysutilStatusPowerSupplyPsuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Me1200SysutilStatusPowerSupplyPsuId_Type.__name__ = "Integer32"
_Me1200SysutilStatusPowerSupplyPsuId_Object = MibTableColumn
me1200SysutilStatusPowerSupplyPsuId = _Me1200SysutilStatusPowerSupplyPsuId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 2),
    _Me1200SysutilStatusPowerSupplyPsuId_Type()
)
me1200SysutilStatusPowerSupplyPsuId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyPsuId.setStatus("current")
_Me1200SysutilStatusPowerSupplyState_Type = ME1200SysutilPowerSupplyStateType
_Me1200SysutilStatusPowerSupplyState_Object = MibTableColumn
me1200SysutilStatusPowerSupplyState = _Me1200SysutilStatusPowerSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 3),
    _Me1200SysutilStatusPowerSupplyState_Type()
)
me1200SysutilStatusPowerSupplyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyState.setStatus("current")


class _Me1200SysutilStatusPowerSupplyDescription_Type(ME1200DisplayString):
    """Custom type me1200SysutilStatusPowerSupplyDescription based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_Me1200SysutilStatusPowerSupplyDescription_Type.__name__ = "ME1200DisplayString"
_Me1200SysutilStatusPowerSupplyDescription_Object = MibTableColumn
me1200SysutilStatusPowerSupplyDescription = _Me1200SysutilStatusPowerSupplyDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 4),
    _Me1200SysutilStatusPowerSupplyDescription_Type()
)
me1200SysutilStatusPowerSupplyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyDescription.setStatus("current")


class _Me1200SysutilVoltageStatus_Type(ME1200DisplayString):
    """Custom type me1200SysutilVoltageStatus based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_Me1200SysutilVoltageStatus_Type.__name__ = "ME1200DisplayString"
_Me1200SysutilVoltageStatus_Object = MibTableColumn
me1200SysutilVoltageStatus = _Me1200SysutilVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 2, 1, 5),
    _Me1200SysutilVoltageStatus_Type()
)
me1200SysutilVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilVoltageStatus.setStatus("current")
_Me1200SysutilStatusSystemLedTable_Object = MibTable
me1200SysutilStatusSystemLedTable = _Me1200SysutilStatusSystemLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 3)
)
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemLedTable.setStatus("current")
_Me1200SysutilStatusSystemLedEntry_Object = MibTableRow
me1200SysutilStatusSystemLedEntry = _Me1200SysutilStatusSystemLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 3, 1)
)
me1200SysutilStatusSystemLedEntry.setIndexNames(
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemLedSwitchId"),
)
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemLedEntry.setStatus("current")


class _Me1200SysutilStatusSystemLedSwitchId_Type(Integer32):
    """Custom type me1200SysutilStatusSystemLedSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200SysutilStatusSystemLedSwitchId_Type.__name__ = "Integer32"
_Me1200SysutilStatusSystemLedSwitchId_Object = MibTableColumn
me1200SysutilStatusSystemLedSwitchId = _Me1200SysutilStatusSystemLedSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 3, 1, 1),
    _Me1200SysutilStatusSystemLedSwitchId_Type()
)
me1200SysutilStatusSystemLedSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemLedSwitchId.setStatus("current")


class _Me1200SysutilStatusSystemLedDescription_Type(ME1200DisplayString):
    """Custom type me1200SysutilStatusSystemLedDescription based on ME1200DisplayString"""
    subtypeSpec = ME1200DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_Me1200SysutilStatusSystemLedDescription_Type.__name__ = "ME1200DisplayString"
_Me1200SysutilStatusSystemLedDescription_Object = MibTableColumn
me1200SysutilStatusSystemLedDescription = _Me1200SysutilStatusSystemLedDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 3, 1, 2),
    _Me1200SysutilStatusSystemLedDescription_Type()
)
me1200SysutilStatusSystemLedDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemLedDescription.setStatus("current")
_Me1200SysutilStatusSystemMemoryPool_ObjectIdentity = ObjectIdentity
me1200SysutilStatusSystemMemoryPool = _Me1200SysutilStatusSystemMemoryPool_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 4)
)
_Me1200SysutilStatusSystemMemoryPoolValid_Type = Unsigned32
_Me1200SysutilStatusSystemMemoryPoolValid_Object = MibScalar
me1200SysutilStatusSystemMemoryPoolValid = _Me1200SysutilStatusSystemMemoryPoolValid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 4, 1),
    _Me1200SysutilStatusSystemMemoryPoolValid_Type()
)
me1200SysutilStatusSystemMemoryPoolValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemMemoryPoolValid.setStatus("current")
_Me1200SysutilStatusSystemMemoryPoolUsed_Type = Unsigned32
_Me1200SysutilStatusSystemMemoryPoolUsed_Object = MibScalar
me1200SysutilStatusSystemMemoryPoolUsed = _Me1200SysutilStatusSystemMemoryPoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 4, 2),
    _Me1200SysutilStatusSystemMemoryPoolUsed_Type()
)
me1200SysutilStatusSystemMemoryPoolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemMemoryPoolUsed.setStatus("current")
_Me1200SysutilStatusSystemMemoryPoolFree_Type = Unsigned32
_Me1200SysutilStatusSystemMemoryPoolFree_Object = MibScalar
me1200SysutilStatusSystemMemoryPoolFree = _Me1200SysutilStatusSystemMemoryPoolFree_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 3, 4, 3),
    _Me1200SysutilStatusSystemMemoryPoolFree_Type()
)
me1200SysutilStatusSystemMemoryPoolFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemMemoryPoolFree.setStatus("current")
_Me1200SysutilControl_ObjectIdentity = ObjectIdentity
me1200SysutilControl = _Me1200SysutilControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4)
)
_Me1200SysutilControlRebootTable_Object = MibTable
me1200SysutilControlRebootTable = _Me1200SysutilControlRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1)
)
if mibBuilder.loadTexts:
    me1200SysutilControlRebootTable.setStatus("current")
_Me1200SysutilControlRebootEntry_Object = MibTableRow
me1200SysutilControlRebootEntry = _Me1200SysutilControlRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1, 1)
)
me1200SysutilControlRebootEntry.setIndexNames(
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilControlRebootSwitchId"),
)
if mibBuilder.loadTexts:
    me1200SysutilControlRebootEntry.setStatus("current")


class _Me1200SysutilControlRebootSwitchId_Type(Integer32):
    """Custom type me1200SysutilControlRebootSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200SysutilControlRebootSwitchId_Type.__name__ = "Integer32"
_Me1200SysutilControlRebootSwitchId_Object = MibTableColumn
me1200SysutilControlRebootSwitchId = _Me1200SysutilControlRebootSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1, 1, 1),
    _Me1200SysutilControlRebootSwitchId_Type()
)
me1200SysutilControlRebootSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilControlRebootSwitchId.setStatus("current")
_Me1200SysutilControlRebootType_Type = ME1200SysutilRebootType
_Me1200SysutilControlRebootType_Object = MibTableColumn
me1200SysutilControlRebootType = _Me1200SysutilControlRebootType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 1, 1, 2),
    _Me1200SysutilControlRebootType_Type()
)
me1200SysutilControlRebootType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SysutilControlRebootType.setStatus("current")
_Me1200SysutilControlSystemLedTable_Object = MibTable
me1200SysutilControlSystemLedTable = _Me1200SysutilControlSystemLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 2)
)
if mibBuilder.loadTexts:
    me1200SysutilControlSystemLedTable.setStatus("current")
_Me1200SysutilControlSystemLedEntry_Object = MibTableRow
me1200SysutilControlSystemLedEntry = _Me1200SysutilControlSystemLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 2, 1)
)
me1200SysutilControlSystemLedEntry.setIndexNames(
    (0, "ME1200-SYSUTIL-MIB", "me1200SysutilControlSystemLedSwitchId"),
)
if mibBuilder.loadTexts:
    me1200SysutilControlSystemLedEntry.setStatus("current")


class _Me1200SysutilControlSystemLedSwitchId_Type(Integer32):
    """Custom type me1200SysutilControlSystemLedSwitchId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_Me1200SysutilControlSystemLedSwitchId_Type.__name__ = "Integer32"
_Me1200SysutilControlSystemLedSwitchId_Object = MibTableColumn
me1200SysutilControlSystemLedSwitchId = _Me1200SysutilControlSystemLedSwitchId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 2, 1, 1),
    _Me1200SysutilControlSystemLedSwitchId_Type()
)
me1200SysutilControlSystemLedSwitchId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    me1200SysutilControlSystemLedSwitchId.setStatus("current")
_Me1200SysutilControlSystemLedClearStatus_Type = ME1200SysutilSystemLedClearType
_Me1200SysutilControlSystemLedClearStatus_Object = MibTableColumn
me1200SysutilControlSystemLedClearStatus = _Me1200SysutilControlSystemLedClearStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 4, 2, 1, 2),
    _Me1200SysutilControlSystemLedClearStatus_Type()
)
me1200SysutilControlSystemLedClearStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    me1200SysutilControlSystemLedClearStatus.setStatus("current")
_Me1200SysutilNotificationPrefix_ObjectIdentity = ObjectIdentity
me1200SysutilNotificationPrefix = _Me1200SysutilNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5)
)
_Me1200SysutilNotification_ObjectIdentity = ObjectIdentity
me1200SysutilNotification = _Me1200SysutilNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0)
)
_Me1200SysutilMibConformance_ObjectIdentity = ObjectIdentity
me1200SysutilMibConformance = _Me1200SysutilMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2)
)
_Me1200SysutilMibCompliances_ObjectIdentity = ObjectIdentity
me1200SysutilMibCompliances = _Me1200SysutilMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 1)
)
_Me1200SysutilMibGroups_ObjectIdentity = ObjectIdentity
me1200SysutilMibGroups = _Me1200SysutilMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2)
)

# Managed Objects groups

me1200SysutilCapabilitiesInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 1)
)
me1200SysutilCapabilitiesInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilCapabilitiesWarmRebootSupported"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilCapabilitiesPostSupported"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilCapabilitiesZtpSupported"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilCapabilitiesStackFwChkSupported"))
)
if mibBuilder.loadTexts:
    me1200SysutilCapabilitiesInfoGroup.setStatus("current")

me1200SysutilConfigSystemMemoryPoolInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 2)
)
me1200SysutilConfigSystemMemoryPoolInfoGroup.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemMemoryPoolNotifThreshold")
)
if mibBuilder.loadTexts:
    me1200SysutilConfigSystemMemoryPoolInfoGroup.setStatus("current")

me1200SysutilConfigSystemCpuLoadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 3)
)
me1200SysutilConfigSystemCpuLoadInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemCpuLoadMonitoringMode"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemCpuLoadMonitoringInterval"))
)
if mibBuilder.loadTexts:
    me1200SysutilConfigSystemCpuLoadInfoGroup.setStatus("current")

me1200SysutilStatusCpuLoadInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 4)
)
me1200SysutilStatusCpuLoadInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage100msec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage1sec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage10sec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage1min"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage5min"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage15min"))
)
if mibBuilder.loadTexts:
    me1200SysutilStatusCpuLoadInfoGroup.setStatus("current")

me1200SysutilStatusPowerSupplyInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 5)
)
me1200SysutilStatusPowerSupplyInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyState"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyDescription"))
)
if mibBuilder.loadTexts:
    me1200SysutilStatusPowerSupplyInfoGroup.setStatus("current")

me1200SysutilStatusSystemLedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 6)
)
me1200SysutilStatusSystemLedInfoGroup.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemLedDescription")
)
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemLedInfoGroup.setStatus("current")

me1200SysutilStatusSystemMemoryPoolInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 7)
)
me1200SysutilStatusSystemMemoryPoolInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemMemoryPoolValid"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemMemoryPoolUsed"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemMemoryPoolFree"))
)
if mibBuilder.loadTexts:
    me1200SysutilStatusSystemMemoryPoolInfoGroup.setStatus("current")

me1200SysutilControlRebootInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 8)
)
me1200SysutilControlRebootInfoGroup.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilControlRebootType")
)
if mibBuilder.loadTexts:
    me1200SysutilControlRebootInfoGroup.setStatus("current")

me1200SysutilControlSystemLedInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 9)
)
me1200SysutilControlSystemLedInfoGroup.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilControlSystemLedClearStatus")
)
if mibBuilder.loadTexts:
    me1200SysutilControlSystemLedInfoGroup.setStatus("current")


# Notification objects

me1200SysutilNotificationPowerSupplyStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 1)
)
me1200SysutilNotificationPowerSupplyStateChange.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyState"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyDescription"))
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationPowerSupplyStateChange.setStatus(
        "current"
    )

me1200SysutilNotificationReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 2)
)
me1200SysutilNotificationReboot.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilControlRebootType")
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationReboot.setStatus(
        "current"
    )

me1200SysutilNotificationMemoryPoolLowMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 3)
)
me1200SysutilNotificationMemoryPoolLowMemory.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemMemoryPoolNotifThreshold"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemMemoryPoolFree"))
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationMemoryPoolLowMemory.setStatus(
        "current"
    )

me1200SysutilNotificationMemoryPoolLowMemoryRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 4)
)
me1200SysutilNotificationMemoryPoolLowMemoryRecovery.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemMemoryPoolNotifThreshold"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemMemoryPoolFree"))
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationMemoryPoolLowMemoryRecovery.setStatus(
        "current"
    )

me1200SysutilNotificationCpuLoadOverAverage1min = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 5)
)
me1200SysutilNotificationCpuLoadOverAverage1min.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemCpuLoadMonitoringInterval"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage100msec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage1min"))
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationCpuLoadOverAverage1min.setStatus(
        "current"
    )

me1200SysutilNotificationCpuLoadOverAverage5min = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 6)
)
me1200SysutilNotificationCpuLoadOverAverage5min.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemCpuLoadMonitoringInterval"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage100msec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage5min"))
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationCpuLoadOverAverage5min.setStatus(
        "current"
    )

me1200SysutilNotificationCpuLoadOverAverage15min = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 7)
)
me1200SysutilNotificationCpuLoadOverAverage15min.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemCpuLoadMonitoringInterval"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage100msec"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadAverage15min"))
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationCpuLoadOverAverage15min.setStatus(
        "current"
    )

me1200SysutilNotificationVoltageFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 1, 5, 0, 8)
)
me1200SysutilNotificationVoltageFailure.setObjects(
    ("ME1200-SYSUTIL-MIB", "me1200SysutilVoltageStatus")
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationVoltageFailure.setStatus(
        "current"
    )


# Notifications groups

me1200SysutilNotificationInfoGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 2, 10)
)
me1200SysutilNotificationInfoGroup.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationPowerSupplyStateChange"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationReboot"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationMemoryPoolLowMemory"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationMemoryPoolLowMemoryRecovery"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationCpuLoadOverAverage1min"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationCpuLoadOverAverage5min"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationCpuLoadOverAverage15min"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationVoltageFailure"))
)
if mibBuilder.loadTexts:
    me1200SysutilNotificationInfoGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

me1200SysutilMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 815, 1, 24, 2, 1, 1)
)
me1200SysutilMibCompliance.setObjects(
      *(("ME1200-SYSUTIL-MIB", "me1200SysutilCapabilitiesInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemMemoryPoolInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilConfigSystemCpuLoadInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusCpuLoadInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusPowerSupplyInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemLedInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilStatusSystemMemoryPoolInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilControlRebootInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilControlSystemLedInfoGroup"),
        ("ME1200-SYSUTIL-MIB", "me1200SysutilNotificationInfoGroup"))
)
if mibBuilder.loadTexts:
    me1200SysutilMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ME1200-SYSUTIL-MIB",
    **{"ME1200SysutilPowerSupplyStateType": ME1200SysutilPowerSupplyStateType,
       "ME1200SysutilRebootType": ME1200SysutilRebootType,
       "ME1200SysutilSystemLedClearType": ME1200SysutilSystemLedClearType,
       "me1200SysutilMib": me1200SysutilMib,
       "me1200SysutilMibObjects": me1200SysutilMibObjects,
       "me1200SysutilCapabilities": me1200SysutilCapabilities,
       "me1200SysutilCapabilitiesWarmRebootSupported": me1200SysutilCapabilitiesWarmRebootSupported,
       "me1200SysutilCapabilitiesPostSupported": me1200SysutilCapabilitiesPostSupported,
       "me1200SysutilCapabilitiesZtpSupported": me1200SysutilCapabilitiesZtpSupported,
       "me1200SysutilCapabilitiesStackFwChkSupported": me1200SysutilCapabilitiesStackFwChkSupported,
       "me1200SysutilConfig": me1200SysutilConfig,
       "me1200SysutilConfigSystemMemoryPool": me1200SysutilConfigSystemMemoryPool,
       "me1200SysutilConfigSystemMemoryPoolNotifThreshold": me1200SysutilConfigSystemMemoryPoolNotifThreshold,
       "me1200SysutilConfigSystemCpuLoad": me1200SysutilConfigSystemCpuLoad,
       "me1200SysutilConfigSystemCpuLoadMonitoringMode": me1200SysutilConfigSystemCpuLoadMonitoringMode,
       "me1200SysutilConfigSystemCpuLoadMonitoringInterval": me1200SysutilConfigSystemCpuLoadMonitoringInterval,
       "me1200SysutilStatus": me1200SysutilStatus,
       "me1200SysutilStatusCpuLoad": me1200SysutilStatusCpuLoad,
       "me1200SysutilStatusCpuLoadAverage100msec": me1200SysutilStatusCpuLoadAverage100msec,
       "me1200SysutilStatusCpuLoadAverage1sec": me1200SysutilStatusCpuLoadAverage1sec,
       "me1200SysutilStatusCpuLoadAverage10sec": me1200SysutilStatusCpuLoadAverage10sec,
       "me1200SysutilStatusCpuLoadAverage1min": me1200SysutilStatusCpuLoadAverage1min,
       "me1200SysutilStatusCpuLoadAverage5min": me1200SysutilStatusCpuLoadAverage5min,
       "me1200SysutilStatusCpuLoadAverage15min": me1200SysutilStatusCpuLoadAverage15min,
       "me1200SysutilStatusPowerSupplyTable": me1200SysutilStatusPowerSupplyTable,
       "me1200SysutilStatusPowerSupplyEntry": me1200SysutilStatusPowerSupplyEntry,
       "me1200SysutilStatusPowerSupplySwitchId": me1200SysutilStatusPowerSupplySwitchId,
       "me1200SysutilStatusPowerSupplyPsuId": me1200SysutilStatusPowerSupplyPsuId,
       "me1200SysutilStatusPowerSupplyState": me1200SysutilStatusPowerSupplyState,
       "me1200SysutilStatusPowerSupplyDescription": me1200SysutilStatusPowerSupplyDescription,
       "me1200SysutilVoltageStatus": me1200SysutilVoltageStatus,
       "me1200SysutilStatusSystemLedTable": me1200SysutilStatusSystemLedTable,
       "me1200SysutilStatusSystemLedEntry": me1200SysutilStatusSystemLedEntry,
       "me1200SysutilStatusSystemLedSwitchId": me1200SysutilStatusSystemLedSwitchId,
       "me1200SysutilStatusSystemLedDescription": me1200SysutilStatusSystemLedDescription,
       "me1200SysutilStatusSystemMemoryPool": me1200SysutilStatusSystemMemoryPool,
       "me1200SysutilStatusSystemMemoryPoolValid": me1200SysutilStatusSystemMemoryPoolValid,
       "me1200SysutilStatusSystemMemoryPoolUsed": me1200SysutilStatusSystemMemoryPoolUsed,
       "me1200SysutilStatusSystemMemoryPoolFree": me1200SysutilStatusSystemMemoryPoolFree,
       "me1200SysutilControl": me1200SysutilControl,
       "me1200SysutilControlRebootTable": me1200SysutilControlRebootTable,
       "me1200SysutilControlRebootEntry": me1200SysutilControlRebootEntry,
       "me1200SysutilControlRebootSwitchId": me1200SysutilControlRebootSwitchId,
       "me1200SysutilControlRebootType": me1200SysutilControlRebootType,
       "me1200SysutilControlSystemLedTable": me1200SysutilControlSystemLedTable,
       "me1200SysutilControlSystemLedEntry": me1200SysutilControlSystemLedEntry,
       "me1200SysutilControlSystemLedSwitchId": me1200SysutilControlSystemLedSwitchId,
       "me1200SysutilControlSystemLedClearStatus": me1200SysutilControlSystemLedClearStatus,
       "me1200SysutilNotificationPrefix": me1200SysutilNotificationPrefix,
       "me1200SysutilNotification": me1200SysutilNotification,
       "me1200SysutilNotificationPowerSupplyStateChange": me1200SysutilNotificationPowerSupplyStateChange,
       "me1200SysutilNotificationReboot": me1200SysutilNotificationReboot,
       "me1200SysutilNotificationMemoryPoolLowMemory": me1200SysutilNotificationMemoryPoolLowMemory,
       "me1200SysutilNotificationMemoryPoolLowMemoryRecovery": me1200SysutilNotificationMemoryPoolLowMemoryRecovery,
       "me1200SysutilNotificationCpuLoadOverAverage1min": me1200SysutilNotificationCpuLoadOverAverage1min,
       "me1200SysutilNotificationCpuLoadOverAverage5min": me1200SysutilNotificationCpuLoadOverAverage5min,
       "me1200SysutilNotificationCpuLoadOverAverage15min": me1200SysutilNotificationCpuLoadOverAverage15min,
       "me1200SysutilNotificationVoltageFailure": me1200SysutilNotificationVoltageFailure,
       "me1200SysutilMibConformance": me1200SysutilMibConformance,
       "me1200SysutilMibCompliances": me1200SysutilMibCompliances,
       "me1200SysutilMibCompliance": me1200SysutilMibCompliance,
       "me1200SysutilMibGroups": me1200SysutilMibGroups,
       "me1200SysutilCapabilitiesInfoGroup": me1200SysutilCapabilitiesInfoGroup,
       "me1200SysutilConfigSystemMemoryPoolInfoGroup": me1200SysutilConfigSystemMemoryPoolInfoGroup,
       "me1200SysutilConfigSystemCpuLoadInfoGroup": me1200SysutilConfigSystemCpuLoadInfoGroup,
       "me1200SysutilStatusCpuLoadInfoGroup": me1200SysutilStatusCpuLoadInfoGroup,
       "me1200SysutilStatusPowerSupplyInfoGroup": me1200SysutilStatusPowerSupplyInfoGroup,
       "me1200SysutilStatusSystemLedInfoGroup": me1200SysutilStatusSystemLedInfoGroup,
       "me1200SysutilStatusSystemMemoryPoolInfoGroup": me1200SysutilStatusSystemMemoryPoolInfoGroup,
       "me1200SysutilControlRebootInfoGroup": me1200SysutilControlRebootInfoGroup,
       "me1200SysutilControlSystemLedInfoGroup": me1200SysutilControlSystemLedInfoGroup,
       "me1200SysutilNotificationInfoGroup": me1200SysutilNotificationInfoGroup}
)
