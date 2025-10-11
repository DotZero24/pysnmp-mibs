# SNMP MIB module (FS-VPLS-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-VPLS-GENERIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:40 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(PwIndexType,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")

(VPNIdOrZero,) = mibBuilder.importSymbols(
    "VPN-TC-STD-MIB",
    "VPNIdOrZero")


# MODULE-IDENTITY

fsvplsGenericDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77)
)
if mibBuilder.loadTexts:
    fsvplsGenericDraft01MIB.setRevisions(
        ("2010-04-28 12:00",
         "2010-06-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class FSVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class FSVplsBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class FSVplsBgpRouteTargetType(TextualConvention, Integer32):
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
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FsvplsNotifications_ObjectIdentity = ObjectIdentity
fsvplsNotifications = _FsvplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 0)
)
_FsvplsObjects_ObjectIdentity = ObjectIdentity
fsvplsObjects = _FsvplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1)
)
_FsvplsConfigIndexNext_Type = Unsigned32
_FsvplsConfigIndexNext_Object = MibScalar
fsvplsConfigIndexNext = _FsvplsConfigIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 1),
    _FsvplsConfigIndexNext_Type()
)
fsvplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsConfigIndexNext.setStatus("current")
_FsvplsConfigTable_Object = MibTable
fsvplsConfigTable = _FsvplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2)
)
if mibBuilder.loadTexts:
    fsvplsConfigTable.setStatus("current")
_FsvplsConfigEntry_Object = MibTableRow
fsvplsConfigEntry = _FsvplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1)
)
fsvplsConfigEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    fsvplsConfigEntry.setStatus("current")


class _FsvplsConfigIndex_Type(Unsigned32):
    """Custom type fsvplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_FsvplsConfigIndex_Type.__name__ = "Unsigned32"
_FsvplsConfigIndex_Object = MibTableColumn
fsvplsConfigIndex = _FsvplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 1),
    _FsvplsConfigIndex_Type()
)
fsvplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsvplsConfigIndex.setStatus("current")


class _FsvplsConfigName_Type(SnmpAdminString):
    """Custom type fsvplsConfigName based on SnmpAdminString"""
    defaultValue = OctetString("")


_FsvplsConfigName_Type.__name__ = "SnmpAdminString"
_FsvplsConfigName_Object = MibTableColumn
fsvplsConfigName = _FsvplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 2),
    _FsvplsConfigName_Type()
)
fsvplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigName.setStatus("current")


class _FsvplsConfigDescr_Type(SnmpAdminString):
    """Custom type fsvplsConfigDescr based on SnmpAdminString"""
    defaultValue = OctetString("")


_FsvplsConfigDescr_Type.__name__ = "SnmpAdminString"
_FsvplsConfigDescr_Object = MibTableColumn
fsvplsConfigDescr = _FsvplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 3),
    _FsvplsConfigDescr_Type()
)
fsvplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigDescr.setStatus("current")


class _FsvplsConfigAdminStatus_Type(Integer32):
    """Custom type fsvplsConfigAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("testing", 3))
    )


_FsvplsConfigAdminStatus_Type.__name__ = "Integer32"
_FsvplsConfigAdminStatus_Object = MibTableColumn
fsvplsConfigAdminStatus = _FsvplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 4),
    _FsvplsConfigAdminStatus_Type()
)
fsvplsConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsConfigAdminStatus.setStatus("current")


class _FsvplsConfigMacLearning_Type(TruthValue):
    """Custom type fsvplsConfigMacLearning based on TruthValue"""
    defaultValue = 1


_FsvplsConfigMacLearning_Type.__name__ = "TruthValue"
_FsvplsConfigMacLearning_Object = MibTableColumn
fsvplsConfigMacLearning = _FsvplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 5),
    _FsvplsConfigMacLearning_Type()
)
fsvplsConfigMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigMacLearning.setStatus("current")


class _FsvplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type fsvplsConfigDiscardUnknownDest based on TruthValue"""
    defaultValue = 2


_FsvplsConfigDiscardUnknownDest_Type.__name__ = "TruthValue"
_FsvplsConfigDiscardUnknownDest_Object = MibTableColumn
fsvplsConfigDiscardUnknownDest = _FsvplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 6),
    _FsvplsConfigDiscardUnknownDest_Type()
)
fsvplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigDiscardUnknownDest.setStatus("current")


class _FsvplsConfigMacAging_Type(TruthValue):
    """Custom type fsvplsConfigMacAging based on TruthValue"""
    defaultValue = 1


_FsvplsConfigMacAging_Type.__name__ = "TruthValue"
_FsvplsConfigMacAging_Object = MibTableColumn
fsvplsConfigMacAging = _FsvplsConfigMacAging_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 7),
    _FsvplsConfigMacAging_Type()
)
fsvplsConfigMacAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsConfigMacAging.setStatus("current")


class _FsvplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type fsvplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsvplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_FsvplsConfigFwdFullHighWatermark_Object = MibTableColumn
fsvplsConfigFwdFullHighWatermark = _FsvplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 8),
    _FsvplsConfigFwdFullHighWatermark_Type()
)
fsvplsConfigFwdFullHighWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    fsvplsConfigFwdFullHighWatermark.setUnits("percentage")


class _FsvplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type fsvplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsvplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_FsvplsConfigFwdFullLowWatermark_Object = MibTableColumn
fsvplsConfigFwdFullLowWatermark = _FsvplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 9),
    _FsvplsConfigFwdFullLowWatermark_Type()
)
fsvplsConfigFwdFullLowWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    fsvplsConfigFwdFullLowWatermark.setUnits("percentage")
_FsvplsConfigRowStatus_Type = RowStatus
_FsvplsConfigRowStatus_Object = MibTableColumn
fsvplsConfigRowStatus = _FsvplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 10),
    _FsvplsConfigRowStatus_Type()
)
fsvplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigRowStatus.setStatus("current")


class _FsvplsConfigMtu_Type(Unsigned32):
    """Custom type fsvplsConfigMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(46, 1530),
    )


_FsvplsConfigMtu_Type.__name__ = "Unsigned32"
_FsvplsConfigMtu_Object = MibTableColumn
fsvplsConfigMtu = _FsvplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 11),
    _FsvplsConfigMtu_Type()
)
fsvplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigMtu.setStatus("current")
_FsvplsConfigVpnId_Type = VPNIdOrZero
_FsvplsConfigVpnId_Object = MibTableColumn
fsvplsConfigVpnId = _FsvplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 12),
    _FsvplsConfigVpnId_Type()
)
fsvplsConfigVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigVpnId.setStatus("current")


class _FsvplsConfigServiceType_Type(Integer32):
    """Custom type fsvplsConfigServiceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("ethernet", 2))
    )


_FsvplsConfigServiceType_Type.__name__ = "Integer32"
_FsvplsConfigServiceType_Object = MibTableColumn
fsvplsConfigServiceType = _FsvplsConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 13),
    _FsvplsConfigServiceType_Type()
)
fsvplsConfigServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigServiceType.setStatus("current")


class _FsvplsConfigServiceSignal_Type(Integer32):
    """Custom type fsvplsConfigServiceSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("autodiscovery", 2))
    )


_FsvplsConfigServiceSignal_Type.__name__ = "Integer32"
_FsvplsConfigServiceSignal_Object = MibTableColumn
fsvplsConfigServiceSignal = _FsvplsConfigServiceSignal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 2, 1, 14),
    _FsvplsConfigServiceSignal_Type()
)
fsvplsConfigServiceSignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsConfigServiceSignal.setStatus("current")
_FsvplsStatusTable_Object = MibTable
fsvplsStatusTable = _FsvplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 3)
)
if mibBuilder.loadTexts:
    fsvplsStatusTable.setStatus("current")
_FsvplsStatusEntry_Object = MibTableRow
fsvplsStatusEntry = _FsvplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 3, 1)
)
fsvplsStatusEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    fsvplsStatusEntry.setStatus("current")


class _FsvplsStatusOperStatus_Type(Integer32):
    """Custom type fsvplsStatusOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_FsvplsStatusOperStatus_Type.__name__ = "Integer32"
_FsvplsStatusOperStatus_Object = MibTableColumn
fsvplsStatusOperStatus = _FsvplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 3, 1, 1),
    _FsvplsStatusOperStatus_Type()
)
fsvplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsStatusOperStatus.setStatus("current")
_FsvplsStatusPeerCount_Type = Counter32
_FsvplsStatusPeerCount_Object = MibTableColumn
fsvplsStatusPeerCount = _FsvplsStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 3, 1, 2),
    _FsvplsStatusPeerCount_Type()
)
fsvplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsStatusPeerCount.setStatus("current")
_FsvplsPwBindTable_Object = MibTable
fsvplsPwBindTable = _FsvplsPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 4)
)
if mibBuilder.loadTexts:
    fsvplsPwBindTable.setStatus("current")
_FsvplsPwBindEntry_Object = MibTableRow
fsvplsPwBindEntry = _FsvplsPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 4, 1)
)
fsvplsPwBindEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    fsvplsPwBindEntry.setStatus("current")
_FsvplsPwBindIndex_Type = Unsigned32
_FsvplsPwBindIndex_Object = MibTableColumn
fsvplsPwBindIndex = _FsvplsPwBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 4, 1, 1),
    _FsvplsPwBindIndex_Type()
)
fsvplsPwBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsvplsPwBindIndex.setStatus("current")


class _FsvplsPwBindConfigType_Type(Integer32):
    """Custom type fsvplsPwBindConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("autodiscovery", 2))
    )


_FsvplsPwBindConfigType_Type.__name__ = "Integer32"
_FsvplsPwBindConfigType_Object = MibTableColumn
fsvplsPwBindConfigType = _FsvplsPwBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 4, 1, 2),
    _FsvplsPwBindConfigType_Type()
)
fsvplsPwBindConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsPwBindConfigType.setStatus("current")


class _FsvplsPwBindType_Type(Integer32):
    """Custom type fsvplsPwBindType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mesh", 1),
          ("spoke", 2))
    )


_FsvplsPwBindType_Type.__name__ = "Integer32"
_FsvplsPwBindType_Object = MibTableColumn
fsvplsPwBindType = _FsvplsPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 4, 1, 3),
    _FsvplsPwBindType_Type()
)
fsvplsPwBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsvplsPwBindType.setStatus("current")
_FsvplsBgpADConfigTable_Object = MibTable
fsvplsBgpADConfigTable = _FsvplsBgpADConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 5)
)
if mibBuilder.loadTexts:
    fsvplsBgpADConfigTable.setStatus("current")
_FsvplsBgpADConfigEntry_Object = MibTableRow
fsvplsBgpADConfigEntry = _FsvplsBgpADConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 5, 1)
)
fsvplsBgpADConfigEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    fsvplsBgpADConfigEntry.setStatus("current")
_FsvplsBgpADConfigRouteDistinguisher_Type = FSVplsBgpRouteDistinguisher
_FsvplsBgpADConfigRouteDistinguisher_Object = MibTableColumn
fsvplsBgpADConfigRouteDistinguisher = _FsvplsBgpADConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 5, 1, 1),
    _FsvplsBgpADConfigRouteDistinguisher_Type()
)
fsvplsBgpADConfigRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpADConfigRouteDistinguisher.setStatus("current")
_FsvplsBgpADConfigRowStatus_Type = RowStatus
_FsvplsBgpADConfigRowStatus_Object = MibTableColumn
fsvplsBgpADConfigRowStatus = _FsvplsBgpADConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 5, 1, 2),
    _FsvplsBgpADConfigRowStatus_Type()
)
fsvplsBgpADConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpADConfigRowStatus.setStatus("current")
_FsvplsBgpRteTargetTable_Object = MibTable
fsvplsBgpRteTargetTable = _FsvplsBgpRteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 6)
)
if mibBuilder.loadTexts:
    fsvplsBgpRteTargetTable.setStatus("current")
_FsvplsBgpRteTargetEntry_Object = MibTableRow
fsvplsBgpRteTargetEntry = _FsvplsBgpRteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 6, 1)
)
fsvplsBgpRteTargetEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsBgpRteTargetIndex"),
)
if mibBuilder.loadTexts:
    fsvplsBgpRteTargetEntry.setStatus("current")
_FsvplsBgpRteTargetIndex_Type = Unsigned32
_FsvplsBgpRteTargetIndex_Object = MibTableColumn
fsvplsBgpRteTargetIndex = _FsvplsBgpRteTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 6, 1, 1),
    _FsvplsBgpRteTargetIndex_Type()
)
fsvplsBgpRteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsvplsBgpRteTargetIndex.setStatus("current")
_FsvplsBgpRteTargetRTType_Type = FSVplsBgpRouteTargetType
_FsvplsBgpRteTargetRTType_Object = MibTableColumn
fsvplsBgpRteTargetRTType = _FsvplsBgpRteTargetRTType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 6, 1, 2),
    _FsvplsBgpRteTargetRTType_Type()
)
fsvplsBgpRteTargetRTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpRteTargetRTType.setStatus("current")
_FsvplsBgpRteTargetRT_Type = FSVplsBgpRouteTarget
_FsvplsBgpRteTargetRT_Object = MibTableColumn
fsvplsBgpRteTargetRT = _FsvplsBgpRteTargetRT_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 6, 1, 3),
    _FsvplsBgpRteTargetRT_Type()
)
fsvplsBgpRteTargetRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpRteTargetRT.setStatus("current")
_FsvplsBgpRteTargetRTRowStatus_Type = RowStatus
_FsvplsBgpRteTargetRTRowStatus_Object = MibTableColumn
fsvplsBgpRteTargetRTRowStatus = _FsvplsBgpRteTargetRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 6, 1, 4),
    _FsvplsBgpRteTargetRTRowStatus_Type()
)
fsvplsBgpRteTargetRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsBgpRteTargetRTRowStatus.setStatus("current")
_FsvplsIfBindTable_Object = MibTable
fsvplsIfBindTable = _FsvplsIfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 7)
)
if mibBuilder.loadTexts:
    fsvplsIfBindTable.setStatus("current")
_FsVplsIfBindEntry_Object = MibTableRow
fsVplsIfBindEntry = _FsVplsIfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 7, 1)
)
fsVplsIfBindEntry.setIndexNames(
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsConfigIndex"),
    (0, "FS-VPLS-GENERIC-MIB", "fsvplsIfBindIndex"),
)
if mibBuilder.loadTexts:
    fsVplsIfBindEntry.setStatus("current")
_FsvplsIfBindIndex_Type = InterfaceIndexOrZero
_FsvplsIfBindIndex_Object = MibTableColumn
fsvplsIfBindIndex = _FsvplsIfBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 7, 1, 1),
    _FsvplsIfBindIndex_Type()
)
fsvplsIfBindIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsIfBindIndex.setStatus("current")
_FsvplsSiteId_Type = Unsigned32
_FsvplsSiteId_Object = MibTableColumn
fsvplsSiteId = _FsvplsSiteId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 7, 1, 2),
    _FsvplsSiteId_Type()
)
fsvplsSiteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsSiteId.setStatus("current")
_FsvplsIfRowStatus_Type = RowStatus
_FsvplsIfRowStatus_Object = MibTableColumn
fsvplsIfRowStatus = _FsvplsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 1, 7, 1, 3),
    _FsvplsIfRowStatus_Type()
)
fsvplsIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsvplsIfRowStatus.setStatus("current")
_FsvplsConformance_ObjectIdentity = ObjectIdentity
fsvplsConformance = _FsvplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2)
)
_FsvplsCompliances_ObjectIdentity = ObjectIdentity
fsvplsCompliances = _FsvplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2, 1)
)
_FsvplsGroups_ObjectIdentity = ObjectIdentity
fsvplsGroups = _FsvplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2, 2)
)

# Managed Objects groups

fsvplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2, 2, 1)
)
fsvplsGroup.setObjects(
      *(("FS-VPLS-GENERIC-MIB", "fsvplsConfigName"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigDescr"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigAdminStatus"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigMacLearning"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigDiscardUnknownDest"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigMacAging"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigVpnId"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigFwdFullHighWatermark"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigFwdFullLowWatermark"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigRowStatus"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigIndexNext"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigMtu"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigServiceType"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsStatusOperStatus"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsStatusPeerCount"))
)
if mibBuilder.loadTexts:
    fsvplsGroup.setStatus("current")

fsvplsPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2, 2, 2)
)
fsvplsPwBindGroup.setObjects(
      *(("FS-VPLS-GENERIC-MIB", "fsvplsPwBindConfigType"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsPwBindType"))
)
if mibBuilder.loadTexts:
    fsvplsPwBindGroup.setStatus("current")


# Notification objects

fsvplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 0, 1)
)
fsvplsFwdFullAlarmRaised.setObjects(
      *(("FS-VPLS-GENERIC-MIB", "fsvplsConfigVpnId"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigFwdFullHighWatermark"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    fsvplsFwdFullAlarmRaised.setStatus(
        "current"
    )

fsvplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 0, 2)
)
fsvplsFwdFullAlarmCleared.setObjects(
      *(("FS-VPLS-GENERIC-MIB", "fsvplsConfigVpnId"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigFwdFullHighWatermark"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    fsvplsFwdFullAlarmCleared.setStatus(
        "current"
    )


# Notifications groups

fsvplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2, 2, 3)
)
fsvplsNotificationGroup.setObjects(
      *(("FS-VPLS-GENERIC-MIB", "fsvplsFwdFullAlarmRaised"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsFwdFullAlarmCleared"))
)
if mibBuilder.loadTexts:
    fsvplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsvplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2, 1, 1)
)
fsvplsModuleFullCompliance.setObjects(
      *(("FS-VPLS-GENERIC-MIB", "fsvplsGroup"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsPwBindGroup"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    fsvplsModuleFullCompliance.setStatus(
        "current"
    )

fsvplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 77, 2, 1, 2)
)
fsvplsModuleReadOnlyCompliance.setObjects(
      *(("FS-VPLS-GENERIC-MIB", "fsvplsGroup"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsPwBindGroup"),
        ("FS-VPLS-GENERIC-MIB", "fsvplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    fsvplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-VPLS-GENERIC-MIB",
    **{"FSVplsBgpRouteDistinguisher": FSVplsBgpRouteDistinguisher,
       "FSVplsBgpRouteTarget": FSVplsBgpRouteTarget,
       "FSVplsBgpRouteTargetType": FSVplsBgpRouteTargetType,
       "fsvplsGenericDraft01MIB": fsvplsGenericDraft01MIB,
       "fsvplsNotifications": fsvplsNotifications,
       "fsvplsFwdFullAlarmRaised": fsvplsFwdFullAlarmRaised,
       "fsvplsFwdFullAlarmCleared": fsvplsFwdFullAlarmCleared,
       "fsvplsObjects": fsvplsObjects,
       "fsvplsConfigIndexNext": fsvplsConfigIndexNext,
       "fsvplsConfigTable": fsvplsConfigTable,
       "fsvplsConfigEntry": fsvplsConfigEntry,
       "fsvplsConfigIndex": fsvplsConfigIndex,
       "fsvplsConfigName": fsvplsConfigName,
       "fsvplsConfigDescr": fsvplsConfigDescr,
       "fsvplsConfigAdminStatus": fsvplsConfigAdminStatus,
       "fsvplsConfigMacLearning": fsvplsConfigMacLearning,
       "fsvplsConfigDiscardUnknownDest": fsvplsConfigDiscardUnknownDest,
       "fsvplsConfigMacAging": fsvplsConfigMacAging,
       "fsvplsConfigFwdFullHighWatermark": fsvplsConfigFwdFullHighWatermark,
       "fsvplsConfigFwdFullLowWatermark": fsvplsConfigFwdFullLowWatermark,
       "fsvplsConfigRowStatus": fsvplsConfigRowStatus,
       "fsvplsConfigMtu": fsvplsConfigMtu,
       "fsvplsConfigVpnId": fsvplsConfigVpnId,
       "fsvplsConfigServiceType": fsvplsConfigServiceType,
       "fsvplsConfigServiceSignal": fsvplsConfigServiceSignal,
       "fsvplsStatusTable": fsvplsStatusTable,
       "fsvplsStatusEntry": fsvplsStatusEntry,
       "fsvplsStatusOperStatus": fsvplsStatusOperStatus,
       "fsvplsStatusPeerCount": fsvplsStatusPeerCount,
       "fsvplsPwBindTable": fsvplsPwBindTable,
       "fsvplsPwBindEntry": fsvplsPwBindEntry,
       "fsvplsPwBindIndex": fsvplsPwBindIndex,
       "fsvplsPwBindConfigType": fsvplsPwBindConfigType,
       "fsvplsPwBindType": fsvplsPwBindType,
       "fsvplsBgpADConfigTable": fsvplsBgpADConfigTable,
       "fsvplsBgpADConfigEntry": fsvplsBgpADConfigEntry,
       "fsvplsBgpADConfigRouteDistinguisher": fsvplsBgpADConfigRouteDistinguisher,
       "fsvplsBgpADConfigRowStatus": fsvplsBgpADConfigRowStatus,
       "fsvplsBgpRteTargetTable": fsvplsBgpRteTargetTable,
       "fsvplsBgpRteTargetEntry": fsvplsBgpRteTargetEntry,
       "fsvplsBgpRteTargetIndex": fsvplsBgpRteTargetIndex,
       "fsvplsBgpRteTargetRTType": fsvplsBgpRteTargetRTType,
       "fsvplsBgpRteTargetRT": fsvplsBgpRteTargetRT,
       "fsvplsBgpRteTargetRTRowStatus": fsvplsBgpRteTargetRTRowStatus,
       "fsvplsIfBindTable": fsvplsIfBindTable,
       "fsVplsIfBindEntry": fsVplsIfBindEntry,
       "fsvplsIfBindIndex": fsvplsIfBindIndex,
       "fsvplsSiteId": fsvplsSiteId,
       "fsvplsIfRowStatus": fsvplsIfRowStatus,
       "fsvplsConformance": fsvplsConformance,
       "fsvplsCompliances": fsvplsCompliances,
       "fsvplsModuleFullCompliance": fsvplsModuleFullCompliance,
       "fsvplsModuleReadOnlyCompliance": fsvplsModuleReadOnlyCompliance,
       "fsvplsGroups": fsvplsGroups,
       "fsvplsGroup": fsvplsGroup,
       "fsvplsPwBindGroup": fsvplsPwBindGroup,
       "fsvplsNotificationGroup": fsvplsNotificationGroup}
)
