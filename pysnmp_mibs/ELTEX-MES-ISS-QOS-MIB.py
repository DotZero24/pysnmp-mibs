# SNMP MIB module (ELTEX-MES-ISS-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:47 2025
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

(fsQoSMeterEntry,
 fsQosHwCpuMaxRate,
 fsQosHwCpuQId,
 fsQosHwCpuRateLimitEntry) = mibBuilder.importSymbols(
    "ARICENT-QOS-MIB",
    "fsQoSMeterEntry",
    "fsQosHwCpuMaxRate",
    "fsQosHwCpuQId",
    "fsQosHwCpuRateLimitEntry")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

eltMesIssQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5)
)
if mibBuilder.loadTexts:
    eltMesIssQoSMIB.setRevisions(
        ("2019-01-18 00:00",
         "2018-12-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssQoSTrustMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("cos", 2),
          ("dscp", 3),
          ("cos-dscp", 4))
    )



class EltMesIssMeterUnits(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bytes", 1),
          ("packets", 2))
    )



class EltMesIssQoSRemarkPortDefaultCosSource(TextualConvention, Integer32):
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
          ("user-priority", 2),
          ("inner-vlanPri", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssQoSObjects_ObjectIdentity = ObjectIdentity
eltMesIssQoSObjects = _EltMesIssQoSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1)
)
_EltMesIssQoSGlobals_ObjectIdentity = ObjectIdentity
eltMesIssQoSGlobals = _EltMesIssQoSGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 1)
)
_EltMesIssQoSTrustMode_Type = EltMesIssQoSTrustMode
_EltMesIssQoSTrustMode_Object = MibScalar
eltMesIssQoSTrustMode = _EltMesIssQoSTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 1, 1),
    _EltMesIssQoSTrustMode_Type()
)
eltMesIssQoSTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSTrustMode.setStatus("current")
_EltMesIssQoSMetering_ObjectIdentity = ObjectIdentity
eltMesIssQoSMetering = _EltMesIssQoSMetering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 2)
)
_EltMesIssQoSMeterTable_Object = MibTable
eltMesIssQoSMeterTable = _EltMesIssQoSMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssQoSMeterTable.setStatus("current")
_EltMesIssQoSMeterEntry_Object = MibTableRow
eltMesIssQoSMeterEntry = _EltMesIssQoSMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssQoSMeterEntry.setStatus("current")


class _EltMesIssQoSMeterUnits_Type(EltMesIssMeterUnits):
    """Custom type eltMesIssQoSMeterUnits based on EltMesIssMeterUnits"""
    defaultValue = 1


_EltMesIssQoSMeterUnits_Type.__name__ = "EltMesIssMeterUnits"
_EltMesIssQoSMeterUnits_Object = MibTableColumn
eltMesIssQoSMeterUnits = _EltMesIssQoSMeterUnits_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 2, 1, 1, 1),
    _EltMesIssQoSMeterUnits_Type()
)
eltMesIssQoSMeterUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSMeterUnits.setStatus("current")
_EltMesIssQoSTrafficMgmt_ObjectIdentity = ObjectIdentity
eltMesIssQoSTrafficMgmt = _EltMesIssQoSTrafficMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 3)
)
_EltMesIssQoSPortTrustModeTable_Object = MibTable
eltMesIssQoSPortTrustModeTable = _EltMesIssQoSPortTrustModeTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssQoSPortTrustModeTable.setStatus("current")
_EltMesIssQoSPortTrustModeEntry_Object = MibTableRow
eltMesIssQoSPortTrustModeEntry = _EltMesIssQoSPortTrustModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 3, 1, 1)
)
eltMesIssQoSPortTrustModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssQoSPortTrustModeEntry.setStatus("current")


class _EltMesIssQoSPortTrustMode_Type(EltMesIssQoSTrustMode):
    """Custom type eltMesIssQoSPortTrustMode based on EltMesIssQoSTrustMode"""
    defaultValue = 1


_EltMesIssQoSPortTrustMode_Type.__name__ = "EltMesIssQoSTrustMode"
_EltMesIssQoSPortTrustMode_Object = MibTableColumn
eltMesIssQoSPortTrustMode = _EltMesIssQoSPortTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 3, 1, 1, 1),
    _EltMesIssQoSPortTrustMode_Type()
)
eltMesIssQoSPortTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSPortTrustMode.setStatus("current")
_EltMesIssQoSRemarking_ObjectIdentity = ObjectIdentity
eltMesIssQoSRemarking = _EltMesIssQoSRemarking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 4)
)
_EltMesIssQoSRemarkPortTable_Object = MibTable
eltMesIssQoSRemarkPortTable = _EltMesIssQoSRemarkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    eltMesIssQoSRemarkPortTable.setStatus("current")
_EltMesIssQoSRemarkPortEntry_Object = MibTableRow
eltMesIssQoSRemarkPortEntry = _EltMesIssQoSRemarkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 4, 1, 1)
)
eltMesIssQoSRemarkPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssQoSRemarkPortEntry.setStatus("current")


class _EltMesIssQoSRemarkPortCosEnable_Type(TruthValue):
    """Custom type eltMesIssQoSRemarkPortCosEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssQoSRemarkPortCosEnable_Type.__name__ = "TruthValue"
_EltMesIssQoSRemarkPortCosEnable_Object = MibTableColumn
eltMesIssQoSRemarkPortCosEnable = _EltMesIssQoSRemarkPortCosEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 4, 1, 1, 1),
    _EltMesIssQoSRemarkPortCosEnable_Type()
)
eltMesIssQoSRemarkPortCosEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSRemarkPortCosEnable.setStatus("current")


class _EltMesIssQoSRemarkPortDscpEnable_Type(TruthValue):
    """Custom type eltMesIssQoSRemarkPortDscpEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssQoSRemarkPortDscpEnable_Type.__name__ = "TruthValue"
_EltMesIssQoSRemarkPortDscpEnable_Object = MibTableColumn
eltMesIssQoSRemarkPortDscpEnable = _EltMesIssQoSRemarkPortDscpEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 4, 1, 1, 2),
    _EltMesIssQoSRemarkPortDscpEnable_Type()
)
eltMesIssQoSRemarkPortDscpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSRemarkPortDscpEnable.setStatus("current")


class _EltMesIssQoSRemarkPortDefaultCosSource_Type(EltMesIssQoSRemarkPortDefaultCosSource):
    """Custom type eltMesIssQoSRemarkPortDefaultCosSource based on EltMesIssQoSRemarkPortDefaultCosSource"""
    defaultValue = 1


_EltMesIssQoSRemarkPortDefaultCosSource_Type.__name__ = "EltMesIssQoSRemarkPortDefaultCosSource"
_EltMesIssQoSRemarkPortDefaultCosSource_Object = MibTableColumn
eltMesIssQoSRemarkPortDefaultCosSource = _EltMesIssQoSRemarkPortDefaultCosSource_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 4, 1, 1, 3),
    _EltMesIssQoSRemarkPortDefaultCosSource_Type()
)
eltMesIssQoSRemarkPortDefaultCosSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSRemarkPortDefaultCosSource.setStatus("current")
_EltMesIssQoSInterfaces_ObjectIdentity = ObjectIdentity
eltMesIssQoSInterfaces = _EltMesIssQoSInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5)
)
_EltMesIssQoSIfUtilizationTable_Object = MibTable
eltMesIssQoSIfUtilizationTable = _EltMesIssQoSIfUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1)
)
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationTable.setStatus("current")
_EltMesIssQoSIfUtilizationEntry_Object = MibTableRow
eltMesIssQoSIfUtilizationEntry = _EltMesIssQoSIfUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1, 1)
)
eltMesIssQoSIfUtilizationEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-QOS-MIB", "eltMesIssQoSIfUtilizationIfIndex"),
    (0, "ELTEX-MES-ISS-QOS-MIB", "eltMesIssQoSIfUtilizationInterval"),
)
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationEntry.setStatus("current")
_EltMesIssQoSIfUtilizationIfIndex_Type = Integer32
_EltMesIssQoSIfUtilizationIfIndex_Object = MibTableColumn
eltMesIssQoSIfUtilizationIfIndex = _EltMesIssQoSIfUtilizationIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1, 1, 1),
    _EltMesIssQoSIfUtilizationIfIndex_Type()
)
eltMesIssQoSIfUtilizationIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationIfIndex.setStatus("current")
_EltMesIssQoSIfUtilizationInterval_Type = Integer32
_EltMesIssQoSIfUtilizationInterval_Object = MibTableColumn
eltMesIssQoSIfUtilizationInterval = _EltMesIssQoSIfUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1, 1, 2),
    _EltMesIssQoSIfUtilizationInterval_Type()
)
eltMesIssQoSIfUtilizationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationInterval.setStatus("current")
_EltMesIssQoSIfUtilizationInPkts_Type = Counter32
_EltMesIssQoSIfUtilizationInPkts_Object = MibTableColumn
eltMesIssQoSIfUtilizationInPkts = _EltMesIssQoSIfUtilizationInPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1, 1, 3),
    _EltMesIssQoSIfUtilizationInPkts_Type()
)
eltMesIssQoSIfUtilizationInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationInPkts.setStatus("current")
_EltMesIssQoSIfUtilizationInRate_Type = Counter32
_EltMesIssQoSIfUtilizationInRate_Object = MibTableColumn
eltMesIssQoSIfUtilizationInRate = _EltMesIssQoSIfUtilizationInRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1, 1, 4),
    _EltMesIssQoSIfUtilizationInRate_Type()
)
eltMesIssQoSIfUtilizationInRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationInRate.setStatus("current")
_EltMesIssQoSIfUtilizationOutPkts_Type = Counter32
_EltMesIssQoSIfUtilizationOutPkts_Object = MibTableColumn
eltMesIssQoSIfUtilizationOutPkts = _EltMesIssQoSIfUtilizationOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1, 1, 5),
    _EltMesIssQoSIfUtilizationOutPkts_Type()
)
eltMesIssQoSIfUtilizationOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationOutPkts.setStatus("current")
_EltMesIssQoSIfUtilizationOutRate_Type = Counter32
_EltMesIssQoSIfUtilizationOutRate_Object = MibTableColumn
eltMesIssQoSIfUtilizationOutRate = _EltMesIssQoSIfUtilizationOutRate_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 5, 1, 1, 6),
    _EltMesIssQoSIfUtilizationOutRate_Type()
)
eltMesIssQoSIfUtilizationOutRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssQoSIfUtilizationOutRate.setStatus("current")
_EltMesIssQoSCpuRateControl_ObjectIdentity = ObjectIdentity
eltMesIssQoSCpuRateControl = _EltMesIssQoSCpuRateControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 6)
)
_EltMesIssQoSCpuRateLimitTable_Object = MibTable
eltMesIssQoSCpuRateLimitTable = _EltMesIssQoSCpuRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 6, 1)
)
if mibBuilder.loadTexts:
    eltMesIssQoSCpuRateLimitTable.setStatus("current")
_EltMesIssQoSCpuRateLimitEntry_Object = MibTableRow
eltMesIssQoSCpuRateLimitEntry = _EltMesIssQoSCpuRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssQoSCpuRateLimitEntry.setStatus("current")


class _EltMesIssQoSCpuRateLimitLoggingEnable_Type(TruthValue):
    """Custom type eltMesIssQoSCpuRateLimitLoggingEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssQoSCpuRateLimitLoggingEnable_Type.__name__ = "TruthValue"
_EltMesIssQoSCpuRateLimitLoggingEnable_Object = MibTableColumn
eltMesIssQoSCpuRateLimitLoggingEnable = _EltMesIssQoSCpuRateLimitLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 6, 1, 1, 1),
    _EltMesIssQoSCpuRateLimitLoggingEnable_Type()
)
eltMesIssQoSCpuRateLimitLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSCpuRateLimitLoggingEnable.setStatus("current")


class _EltMesIssQoSCpuRateLimitTrapEnable_Type(TruthValue):
    """Custom type eltMesIssQoSCpuRateLimitTrapEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssQoSCpuRateLimitTrapEnable_Type.__name__ = "TruthValue"
_EltMesIssQoSCpuRateLimitTrapEnable_Object = MibTableColumn
eltMesIssQoSCpuRateLimitTrapEnable = _EltMesIssQoSCpuRateLimitTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 1, 6, 1, 1, 2),
    _EltMesIssQoSCpuRateLimitTrapEnable_Type()
)
eltMesIssQoSCpuRateLimitTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssQoSCpuRateLimitTrapEnable.setStatus("current")
_EltMesIssQoSNotifications_ObjectIdentity = ObjectIdentity
eltMesIssQoSNotifications = _EltMesIssQoSNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 2)
)
_EltMesIssQoSNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltMesIssQoSNotificationsPrefix = _EltMesIssQoSNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 2, 0)
)
fsQoSMeterEntry.registerAugmentions(
    ("ELTEX-MES-ISS-QOS-MIB",
     "eltMesIssQoSMeterEntry")
)
eltMesIssQoSMeterEntry.setIndexNames(*fsQoSMeterEntry.getIndexNames())
fsQosHwCpuRateLimitEntry.registerAugmentions(
    ("ELTEX-MES-ISS-QOS-MIB",
     "eltMesIssQoSCpuRateLimitEntry")
)
eltMesIssQoSCpuRateLimitEntry.setIndexNames(*fsQosHwCpuRateLimitEntry.getIndexNames())

# Managed Objects groups


# Notification objects

eltMesIssQoSCpuRateLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 5, 2, 0, 1)
)
eltMesIssQoSCpuRateLimitTrap.setObjects(
      *(("ARICENT-QOS-MIB", "fsQosHwCpuQId"),
        ("ARICENT-QOS-MIB", "fsQosHwCpuMaxRate"))
)
if mibBuilder.loadTexts:
    eltMesIssQoSCpuRateLimitTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-QOS-MIB",
    **{"EltMesIssQoSTrustMode": EltMesIssQoSTrustMode,
       "EltMesIssMeterUnits": EltMesIssMeterUnits,
       "EltMesIssQoSRemarkPortDefaultCosSource": EltMesIssQoSRemarkPortDefaultCosSource,
       "eltMesIssQoSMIB": eltMesIssQoSMIB,
       "eltMesIssQoSObjects": eltMesIssQoSObjects,
       "eltMesIssQoSGlobals": eltMesIssQoSGlobals,
       "eltMesIssQoSTrustMode": eltMesIssQoSTrustMode,
       "eltMesIssQoSMetering": eltMesIssQoSMetering,
       "eltMesIssQoSMeterTable": eltMesIssQoSMeterTable,
       "eltMesIssQoSMeterEntry": eltMesIssQoSMeterEntry,
       "eltMesIssQoSMeterUnits": eltMesIssQoSMeterUnits,
       "eltMesIssQoSTrafficMgmt": eltMesIssQoSTrafficMgmt,
       "eltMesIssQoSPortTrustModeTable": eltMesIssQoSPortTrustModeTable,
       "eltMesIssQoSPortTrustModeEntry": eltMesIssQoSPortTrustModeEntry,
       "eltMesIssQoSPortTrustMode": eltMesIssQoSPortTrustMode,
       "eltMesIssQoSRemarking": eltMesIssQoSRemarking,
       "eltMesIssQoSRemarkPortTable": eltMesIssQoSRemarkPortTable,
       "eltMesIssQoSRemarkPortEntry": eltMesIssQoSRemarkPortEntry,
       "eltMesIssQoSRemarkPortCosEnable": eltMesIssQoSRemarkPortCosEnable,
       "eltMesIssQoSRemarkPortDscpEnable": eltMesIssQoSRemarkPortDscpEnable,
       "eltMesIssQoSRemarkPortDefaultCosSource": eltMesIssQoSRemarkPortDefaultCosSource,
       "eltMesIssQoSInterfaces": eltMesIssQoSInterfaces,
       "eltMesIssQoSIfUtilizationTable": eltMesIssQoSIfUtilizationTable,
       "eltMesIssQoSIfUtilizationEntry": eltMesIssQoSIfUtilizationEntry,
       "eltMesIssQoSIfUtilizationIfIndex": eltMesIssQoSIfUtilizationIfIndex,
       "eltMesIssQoSIfUtilizationInterval": eltMesIssQoSIfUtilizationInterval,
       "eltMesIssQoSIfUtilizationInPkts": eltMesIssQoSIfUtilizationInPkts,
       "eltMesIssQoSIfUtilizationInRate": eltMesIssQoSIfUtilizationInRate,
       "eltMesIssQoSIfUtilizationOutPkts": eltMesIssQoSIfUtilizationOutPkts,
       "eltMesIssQoSIfUtilizationOutRate": eltMesIssQoSIfUtilizationOutRate,
       "eltMesIssQoSCpuRateControl": eltMesIssQoSCpuRateControl,
       "eltMesIssQoSCpuRateLimitTable": eltMesIssQoSCpuRateLimitTable,
       "eltMesIssQoSCpuRateLimitEntry": eltMesIssQoSCpuRateLimitEntry,
       "eltMesIssQoSCpuRateLimitLoggingEnable": eltMesIssQoSCpuRateLimitLoggingEnable,
       "eltMesIssQoSCpuRateLimitTrapEnable": eltMesIssQoSCpuRateLimitTrapEnable,
       "eltMesIssQoSNotifications": eltMesIssQoSNotifications,
       "eltMesIssQoSNotificationsPrefix": eltMesIssQoSNotificationsPrefix,
       "eltMesIssQoSCpuRateLimitTrap": eltMesIssQoSCpuRateLimitTrap}
)
