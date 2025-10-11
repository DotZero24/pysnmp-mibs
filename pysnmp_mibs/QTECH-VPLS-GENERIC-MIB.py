# SNMP MIB module (QTECH-VPLS-GENERIC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-VPLS-GENERIC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:31 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(PwIndexType,) = mibBuilder.importSymbols(
    "PW-TC-STD-MIB",
    "PwIndexType")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechvplsGenericDraft01MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77)
)
if mibBuilder.loadTexts:
    qtechvplsGenericDraft01MIB.setRevisions(
        ("2010-04-28 12:00",
         "2010-06-04 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class QtechVplsBgpRouteDistinguisher(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class QtechVplsBgpRouteTarget(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class QtechVplsBgpRouteTargetType(TextualConvention, Integer32):
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

_QtechvplsNotifications_ObjectIdentity = ObjectIdentity
qtechvplsNotifications = _QtechvplsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 0)
)
_QtechvplsObjects_ObjectIdentity = ObjectIdentity
qtechvplsObjects = _QtechvplsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1)
)
_QtechvplsConfigIndexNext_Type = Unsigned32
_QtechvplsConfigIndexNext_Object = MibScalar
qtechvplsConfigIndexNext = _QtechvplsConfigIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 1),
    _QtechvplsConfigIndexNext_Type()
)
qtechvplsConfigIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsConfigIndexNext.setStatus("current")
_QtechvplsConfigTable_Object = MibTable
qtechvplsConfigTable = _QtechvplsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2)
)
if mibBuilder.loadTexts:
    qtechvplsConfigTable.setStatus("current")
_QtechvplsConfigEntry_Object = MibTableRow
qtechvplsConfigEntry = _QtechvplsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1)
)
qtechvplsConfigEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    qtechvplsConfigEntry.setStatus("current")


class _QtechvplsConfigIndex_Type(Unsigned32):
    """Custom type qtechvplsConfigIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_QtechvplsConfigIndex_Type.__name__ = "Unsigned32"
_QtechvplsConfigIndex_Object = MibTableColumn
qtechvplsConfigIndex = _QtechvplsConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 1),
    _QtechvplsConfigIndex_Type()
)
qtechvplsConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechvplsConfigIndex.setStatus("current")


class _QtechvplsConfigName_Type(SnmpAdminString):
    """Custom type qtechvplsConfigName based on SnmpAdminString"""
    defaultValue = OctetString("")


_QtechvplsConfigName_Type.__name__ = "SnmpAdminString"
_QtechvplsConfigName_Object = MibTableColumn
qtechvplsConfigName = _QtechvplsConfigName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 2),
    _QtechvplsConfigName_Type()
)
qtechvplsConfigName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigName.setStatus("current")


class _QtechvplsConfigDescr_Type(SnmpAdminString):
    """Custom type qtechvplsConfigDescr based on SnmpAdminString"""
    defaultValue = OctetString("")


_QtechvplsConfigDescr_Type.__name__ = "SnmpAdminString"
_QtechvplsConfigDescr_Object = MibTableColumn
qtechvplsConfigDescr = _QtechvplsConfigDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 3),
    _QtechvplsConfigDescr_Type()
)
qtechvplsConfigDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigDescr.setStatus("current")


class _QtechvplsConfigAdminStatus_Type(Integer32):
    """Custom type qtechvplsConfigAdminStatus based on Integer32"""
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


_QtechvplsConfigAdminStatus_Type.__name__ = "Integer32"
_QtechvplsConfigAdminStatus_Object = MibTableColumn
qtechvplsConfigAdminStatus = _QtechvplsConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 4),
    _QtechvplsConfigAdminStatus_Type()
)
qtechvplsConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsConfigAdminStatus.setStatus("current")


class _QtechvplsConfigMacLearning_Type(TruthValue):
    """Custom type qtechvplsConfigMacLearning based on TruthValue"""
    defaultValue = 1


_QtechvplsConfigMacLearning_Type.__name__ = "TruthValue"
_QtechvplsConfigMacLearning_Object = MibTableColumn
qtechvplsConfigMacLearning = _QtechvplsConfigMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 5),
    _QtechvplsConfigMacLearning_Type()
)
qtechvplsConfigMacLearning.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigMacLearning.setStatus("current")


class _QtechvplsConfigDiscardUnknownDest_Type(TruthValue):
    """Custom type qtechvplsConfigDiscardUnknownDest based on TruthValue"""
    defaultValue = 2


_QtechvplsConfigDiscardUnknownDest_Type.__name__ = "TruthValue"
_QtechvplsConfigDiscardUnknownDest_Object = MibTableColumn
qtechvplsConfigDiscardUnknownDest = _QtechvplsConfigDiscardUnknownDest_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 6),
    _QtechvplsConfigDiscardUnknownDest_Type()
)
qtechvplsConfigDiscardUnknownDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigDiscardUnknownDest.setStatus("current")


class _QtechvplsConfigMacAging_Type(TruthValue):
    """Custom type qtechvplsConfigMacAging based on TruthValue"""
    defaultValue = 1


_QtechvplsConfigMacAging_Type.__name__ = "TruthValue"
_QtechvplsConfigMacAging_Object = MibTableColumn
qtechvplsConfigMacAging = _QtechvplsConfigMacAging_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 7),
    _QtechvplsConfigMacAging_Type()
)
qtechvplsConfigMacAging.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsConfigMacAging.setStatus("current")


class _QtechvplsConfigFwdFullHighWatermark_Type(Unsigned32):
    """Custom type qtechvplsConfigFwdFullHighWatermark based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechvplsConfigFwdFullHighWatermark_Type.__name__ = "Unsigned32"
_QtechvplsConfigFwdFullHighWatermark_Object = MibTableColumn
qtechvplsConfigFwdFullHighWatermark = _QtechvplsConfigFwdFullHighWatermark_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 8),
    _QtechvplsConfigFwdFullHighWatermark_Type()
)
qtechvplsConfigFwdFullHighWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigFwdFullHighWatermark.setStatus("current")
if mibBuilder.loadTexts:
    qtechvplsConfigFwdFullHighWatermark.setUnits("percentage")


class _QtechvplsConfigFwdFullLowWatermark_Type(Unsigned32):
    """Custom type qtechvplsConfigFwdFullLowWatermark based on Unsigned32"""
    defaultValue = 80

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechvplsConfigFwdFullLowWatermark_Type.__name__ = "Unsigned32"
_QtechvplsConfigFwdFullLowWatermark_Object = MibTableColumn
qtechvplsConfigFwdFullLowWatermark = _QtechvplsConfigFwdFullLowWatermark_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 9),
    _QtechvplsConfigFwdFullLowWatermark_Type()
)
qtechvplsConfigFwdFullLowWatermark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigFwdFullLowWatermark.setStatus("current")
if mibBuilder.loadTexts:
    qtechvplsConfigFwdFullLowWatermark.setUnits("percentage")
_QtechvplsConfigRowStatus_Type = RowStatus
_QtechvplsConfigRowStatus_Object = MibTableColumn
qtechvplsConfigRowStatus = _QtechvplsConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 10),
    _QtechvplsConfigRowStatus_Type()
)
qtechvplsConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigRowStatus.setStatus("current")


class _QtechvplsConfigMtu_Type(Unsigned32):
    """Custom type qtechvplsConfigMtu based on Unsigned32"""
    defaultValue = 1500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(46, 1530),
    )


_QtechvplsConfigMtu_Type.__name__ = "Unsigned32"
_QtechvplsConfigMtu_Object = MibTableColumn
qtechvplsConfigMtu = _QtechvplsConfigMtu_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 11),
    _QtechvplsConfigMtu_Type()
)
qtechvplsConfigMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigMtu.setStatus("current")
_QtechvplsConfigVpnId_Type = VPNIdOrZero
_QtechvplsConfigVpnId_Object = MibTableColumn
qtechvplsConfigVpnId = _QtechvplsConfigVpnId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 12),
    _QtechvplsConfigVpnId_Type()
)
qtechvplsConfigVpnId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigVpnId.setStatus("current")


class _QtechvplsConfigServiceType_Type(Integer32):
    """Custom type qtechvplsConfigServiceType based on Integer32"""
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


_QtechvplsConfigServiceType_Type.__name__ = "Integer32"
_QtechvplsConfigServiceType_Object = MibTableColumn
qtechvplsConfigServiceType = _QtechvplsConfigServiceType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 13),
    _QtechvplsConfigServiceType_Type()
)
qtechvplsConfigServiceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigServiceType.setStatus("current")


class _QtechvplsConfigServiceSignal_Type(Integer32):
    """Custom type qtechvplsConfigServiceSignal based on Integer32"""
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


_QtechvplsConfigServiceSignal_Type.__name__ = "Integer32"
_QtechvplsConfigServiceSignal_Object = MibTableColumn
qtechvplsConfigServiceSignal = _QtechvplsConfigServiceSignal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 2, 1, 14),
    _QtechvplsConfigServiceSignal_Type()
)
qtechvplsConfigServiceSignal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsConfigServiceSignal.setStatus("current")
_QtechvplsStatusTable_Object = MibTable
qtechvplsStatusTable = _QtechvplsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 3)
)
if mibBuilder.loadTexts:
    qtechvplsStatusTable.setStatus("current")
_QtechvplsStatusEntry_Object = MibTableRow
qtechvplsStatusEntry = _QtechvplsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 3, 1)
)
qtechvplsStatusEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    qtechvplsStatusEntry.setStatus("current")


class _QtechvplsStatusOperStatus_Type(Integer32):
    """Custom type qtechvplsStatusOperStatus based on Integer32"""
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


_QtechvplsStatusOperStatus_Type.__name__ = "Integer32"
_QtechvplsStatusOperStatus_Object = MibTableColumn
qtechvplsStatusOperStatus = _QtechvplsStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 3, 1, 1),
    _QtechvplsStatusOperStatus_Type()
)
qtechvplsStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsStatusOperStatus.setStatus("current")
_QtechvplsStatusPeerCount_Type = Counter32
_QtechvplsStatusPeerCount_Object = MibTableColumn
qtechvplsStatusPeerCount = _QtechvplsStatusPeerCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 3, 1, 2),
    _QtechvplsStatusPeerCount_Type()
)
qtechvplsStatusPeerCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsStatusPeerCount.setStatus("current")
_QtechvplsPwBindTable_Object = MibTable
qtechvplsPwBindTable = _QtechvplsPwBindTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 4)
)
if mibBuilder.loadTexts:
    qtechvplsPwBindTable.setStatus("current")
_QtechvplsPwBindEntry_Object = MibTableRow
qtechvplsPwBindEntry = _QtechvplsPwBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 4, 1)
)
qtechvplsPwBindEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsPwBindIndex"),
)
if mibBuilder.loadTexts:
    qtechvplsPwBindEntry.setStatus("current")
_QtechvplsPwBindIndex_Type = Unsigned32
_QtechvplsPwBindIndex_Object = MibTableColumn
qtechvplsPwBindIndex = _QtechvplsPwBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 4, 1, 1),
    _QtechvplsPwBindIndex_Type()
)
qtechvplsPwBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechvplsPwBindIndex.setStatus("current")


class _QtechvplsPwBindConfigType_Type(Integer32):
    """Custom type qtechvplsPwBindConfigType based on Integer32"""
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


_QtechvplsPwBindConfigType_Type.__name__ = "Integer32"
_QtechvplsPwBindConfigType_Object = MibTableColumn
qtechvplsPwBindConfigType = _QtechvplsPwBindConfigType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 4, 1, 2),
    _QtechvplsPwBindConfigType_Type()
)
qtechvplsPwBindConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsPwBindConfigType.setStatus("current")


class _QtechvplsPwBindType_Type(Integer32):
    """Custom type qtechvplsPwBindType based on Integer32"""
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


_QtechvplsPwBindType_Type.__name__ = "Integer32"
_QtechvplsPwBindType_Object = MibTableColumn
qtechvplsPwBindType = _QtechvplsPwBindType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 4, 1, 3),
    _QtechvplsPwBindType_Type()
)
qtechvplsPwBindType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechvplsPwBindType.setStatus("current")
_QtechvplsBgpADConfigTable_Object = MibTable
qtechvplsBgpADConfigTable = _QtechvplsBgpADConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 5)
)
if mibBuilder.loadTexts:
    qtechvplsBgpADConfigTable.setStatus("current")
_QtechvplsBgpADConfigEntry_Object = MibTableRow
qtechvplsBgpADConfigEntry = _QtechvplsBgpADConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 5, 1)
)
qtechvplsBgpADConfigEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
)
if mibBuilder.loadTexts:
    qtechvplsBgpADConfigEntry.setStatus("current")
_QtechvplsBgpADConfigRouteDistinguisher_Type = QtechVplsBgpRouteDistinguisher
_QtechvplsBgpADConfigRouteDistinguisher_Object = MibTableColumn
qtechvplsBgpADConfigRouteDistinguisher = _QtechvplsBgpADConfigRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 5, 1, 1),
    _QtechvplsBgpADConfigRouteDistinguisher_Type()
)
qtechvplsBgpADConfigRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpADConfigRouteDistinguisher.setStatus("current")
_QtechvplsBgpADConfigRowStatus_Type = RowStatus
_QtechvplsBgpADConfigRowStatus_Object = MibTableColumn
qtechvplsBgpADConfigRowStatus = _QtechvplsBgpADConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 5, 1, 2),
    _QtechvplsBgpADConfigRowStatus_Type()
)
qtechvplsBgpADConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpADConfigRowStatus.setStatus("current")
_QtechvplsBgpRteTargetTable_Object = MibTable
qtechvplsBgpRteTargetTable = _QtechvplsBgpRteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 6)
)
if mibBuilder.loadTexts:
    qtechvplsBgpRteTargetTable.setStatus("current")
_QtechvplsBgpRteTargetEntry_Object = MibTableRow
qtechvplsBgpRteTargetEntry = _QtechvplsBgpRteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 6, 1)
)
qtechvplsBgpRteTargetEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsBgpRteTargetIndex"),
)
if mibBuilder.loadTexts:
    qtechvplsBgpRteTargetEntry.setStatus("current")
_QtechvplsBgpRteTargetIndex_Type = Unsigned32
_QtechvplsBgpRteTargetIndex_Object = MibTableColumn
qtechvplsBgpRteTargetIndex = _QtechvplsBgpRteTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 6, 1, 1),
    _QtechvplsBgpRteTargetIndex_Type()
)
qtechvplsBgpRteTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechvplsBgpRteTargetIndex.setStatus("current")
_QtechvplsBgpRteTargetRTType_Type = QtechVplsBgpRouteTargetType
_QtechvplsBgpRteTargetRTType_Object = MibTableColumn
qtechvplsBgpRteTargetRTType = _QtechvplsBgpRteTargetRTType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 6, 1, 2),
    _QtechvplsBgpRteTargetRTType_Type()
)
qtechvplsBgpRteTargetRTType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpRteTargetRTType.setStatus("current")
_QtechvplsBgpRteTargetRT_Type = QtechVplsBgpRouteTarget
_QtechvplsBgpRteTargetRT_Object = MibTableColumn
qtechvplsBgpRteTargetRT = _QtechvplsBgpRteTargetRT_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 6, 1, 3),
    _QtechvplsBgpRteTargetRT_Type()
)
qtechvplsBgpRteTargetRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpRteTargetRT.setStatus("current")
_QtechvplsBgpRteTargetRTRowStatus_Type = RowStatus
_QtechvplsBgpRteTargetRTRowStatus_Object = MibTableColumn
qtechvplsBgpRteTargetRTRowStatus = _QtechvplsBgpRteTargetRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 6, 1, 4),
    _QtechvplsBgpRteTargetRTRowStatus_Type()
)
qtechvplsBgpRteTargetRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsBgpRteTargetRTRowStatus.setStatus("current")
_QtechvplsIfBindTable_Object = MibTable
qtechvplsIfBindTable = _QtechvplsIfBindTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 7)
)
if mibBuilder.loadTexts:
    qtechvplsIfBindTable.setStatus("current")
_QtechVplsIfBindEntry_Object = MibTableRow
qtechVplsIfBindEntry = _QtechVplsIfBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 7, 1)
)
qtechVplsIfBindEntry.setIndexNames(
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndex"),
    (0, "QTECH-VPLS-GENERIC-MIB", "qtechvplsIfBindIndex"),
)
if mibBuilder.loadTexts:
    qtechVplsIfBindEntry.setStatus("current")
_QtechvplsIfBindIndex_Type = InterfaceIndexOrZero
_QtechvplsIfBindIndex_Object = MibTableColumn
qtechvplsIfBindIndex = _QtechvplsIfBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 7, 1, 1),
    _QtechvplsIfBindIndex_Type()
)
qtechvplsIfBindIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsIfBindIndex.setStatus("current")
_QtechvplsSiteId_Type = Unsigned32
_QtechvplsSiteId_Object = MibTableColumn
qtechvplsSiteId = _QtechvplsSiteId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 7, 1, 2),
    _QtechvplsSiteId_Type()
)
qtechvplsSiteId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsSiteId.setStatus("current")
_QtechvplsIfRowStatus_Type = RowStatus
_QtechvplsIfRowStatus_Object = MibTableColumn
qtechvplsIfRowStatus = _QtechvplsIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 1, 7, 1, 3),
    _QtechvplsIfRowStatus_Type()
)
qtechvplsIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechvplsIfRowStatus.setStatus("current")
_QtechvplsConformance_ObjectIdentity = ObjectIdentity
qtechvplsConformance = _QtechvplsConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2)
)
_QtechvplsCompliances_ObjectIdentity = ObjectIdentity
qtechvplsCompliances = _QtechvplsCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2, 1)
)
_QtechvplsGroups_ObjectIdentity = ObjectIdentity
qtechvplsGroups = _QtechvplsGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2, 2)
)

# Managed Objects groups

qtechvplsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2, 2, 1)
)
qtechvplsGroup.setObjects(
      *(("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigName"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigDescr"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigAdminStatus"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigMacLearning"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigDiscardUnknownDest"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigMacAging"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigVpnId"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigFwdFullHighWatermark"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigFwdFullLowWatermark"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigRowStatus"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigIndexNext"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigMtu"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigServiceType"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsStatusOperStatus"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsStatusPeerCount"))
)
if mibBuilder.loadTexts:
    qtechvplsGroup.setStatus("current")

qtechvplsPwBindGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2, 2, 2)
)
qtechvplsPwBindGroup.setObjects(
      *(("QTECH-VPLS-GENERIC-MIB", "qtechvplsPwBindConfigType"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsPwBindType"))
)
if mibBuilder.loadTexts:
    qtechvplsPwBindGroup.setStatus("current")


# Notification objects

qtechvplsFwdFullAlarmRaised = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 0, 1)
)
qtechvplsFwdFullAlarmRaised.setObjects(
      *(("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigVpnId"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigFwdFullHighWatermark"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    qtechvplsFwdFullAlarmRaised.setStatus(
        "current"
    )

qtechvplsFwdFullAlarmCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 0, 2)
)
qtechvplsFwdFullAlarmCleared.setObjects(
      *(("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigVpnId"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigFwdFullHighWatermark"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsConfigFwdFullLowWatermark"))
)
if mibBuilder.loadTexts:
    qtechvplsFwdFullAlarmCleared.setStatus(
        "current"
    )


# Notifications groups

qtechvplsNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2, 2, 3)
)
qtechvplsNotificationGroup.setObjects(
      *(("QTECH-VPLS-GENERIC-MIB", "qtechvplsFwdFullAlarmRaised"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsFwdFullAlarmCleared"))
)
if mibBuilder.loadTexts:
    qtechvplsNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechvplsModuleFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2, 1, 1)
)
qtechvplsModuleFullCompliance.setObjects(
      *(("QTECH-VPLS-GENERIC-MIB", "qtechvplsGroup"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsPwBindGroup"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    qtechvplsModuleFullCompliance.setStatus(
        "current"
    )

qtechvplsModuleReadOnlyCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 77, 2, 1, 2)
)
qtechvplsModuleReadOnlyCompliance.setObjects(
      *(("QTECH-VPLS-GENERIC-MIB", "qtechvplsGroup"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsPwBindGroup"),
        ("QTECH-VPLS-GENERIC-MIB", "qtechvplsNotificationGroup"))
)
if mibBuilder.loadTexts:
    qtechvplsModuleReadOnlyCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-VPLS-GENERIC-MIB",
    **{"QtechVplsBgpRouteDistinguisher": QtechVplsBgpRouteDistinguisher,
       "QtechVplsBgpRouteTarget": QtechVplsBgpRouteTarget,
       "QtechVplsBgpRouteTargetType": QtechVplsBgpRouteTargetType,
       "qtechvplsGenericDraft01MIB": qtechvplsGenericDraft01MIB,
       "qtechvplsNotifications": qtechvplsNotifications,
       "qtechvplsFwdFullAlarmRaised": qtechvplsFwdFullAlarmRaised,
       "qtechvplsFwdFullAlarmCleared": qtechvplsFwdFullAlarmCleared,
       "qtechvplsObjects": qtechvplsObjects,
       "qtechvplsConfigIndexNext": qtechvplsConfigIndexNext,
       "qtechvplsConfigTable": qtechvplsConfigTable,
       "qtechvplsConfigEntry": qtechvplsConfigEntry,
       "qtechvplsConfigIndex": qtechvplsConfigIndex,
       "qtechvplsConfigName": qtechvplsConfigName,
       "qtechvplsConfigDescr": qtechvplsConfigDescr,
       "qtechvplsConfigAdminStatus": qtechvplsConfigAdminStatus,
       "qtechvplsConfigMacLearning": qtechvplsConfigMacLearning,
       "qtechvplsConfigDiscardUnknownDest": qtechvplsConfigDiscardUnknownDest,
       "qtechvplsConfigMacAging": qtechvplsConfigMacAging,
       "qtechvplsConfigFwdFullHighWatermark": qtechvplsConfigFwdFullHighWatermark,
       "qtechvplsConfigFwdFullLowWatermark": qtechvplsConfigFwdFullLowWatermark,
       "qtechvplsConfigRowStatus": qtechvplsConfigRowStatus,
       "qtechvplsConfigMtu": qtechvplsConfigMtu,
       "qtechvplsConfigVpnId": qtechvplsConfigVpnId,
       "qtechvplsConfigServiceType": qtechvplsConfigServiceType,
       "qtechvplsConfigServiceSignal": qtechvplsConfigServiceSignal,
       "qtechvplsStatusTable": qtechvplsStatusTable,
       "qtechvplsStatusEntry": qtechvplsStatusEntry,
       "qtechvplsStatusOperStatus": qtechvplsStatusOperStatus,
       "qtechvplsStatusPeerCount": qtechvplsStatusPeerCount,
       "qtechvplsPwBindTable": qtechvplsPwBindTable,
       "qtechvplsPwBindEntry": qtechvplsPwBindEntry,
       "qtechvplsPwBindIndex": qtechvplsPwBindIndex,
       "qtechvplsPwBindConfigType": qtechvplsPwBindConfigType,
       "qtechvplsPwBindType": qtechvplsPwBindType,
       "qtechvplsBgpADConfigTable": qtechvplsBgpADConfigTable,
       "qtechvplsBgpADConfigEntry": qtechvplsBgpADConfigEntry,
       "qtechvplsBgpADConfigRouteDistinguisher": qtechvplsBgpADConfigRouteDistinguisher,
       "qtechvplsBgpADConfigRowStatus": qtechvplsBgpADConfigRowStatus,
       "qtechvplsBgpRteTargetTable": qtechvplsBgpRteTargetTable,
       "qtechvplsBgpRteTargetEntry": qtechvplsBgpRteTargetEntry,
       "qtechvplsBgpRteTargetIndex": qtechvplsBgpRteTargetIndex,
       "qtechvplsBgpRteTargetRTType": qtechvplsBgpRteTargetRTType,
       "qtechvplsBgpRteTargetRT": qtechvplsBgpRteTargetRT,
       "qtechvplsBgpRteTargetRTRowStatus": qtechvplsBgpRteTargetRTRowStatus,
       "qtechvplsIfBindTable": qtechvplsIfBindTable,
       "qtechVplsIfBindEntry": qtechVplsIfBindEntry,
       "qtechvplsIfBindIndex": qtechvplsIfBindIndex,
       "qtechvplsSiteId": qtechvplsSiteId,
       "qtechvplsIfRowStatus": qtechvplsIfRowStatus,
       "qtechvplsConformance": qtechvplsConformance,
       "qtechvplsCompliances": qtechvplsCompliances,
       "qtechvplsModuleFullCompliance": qtechvplsModuleFullCompliance,
       "qtechvplsModuleReadOnlyCompliance": qtechvplsModuleReadOnlyCompliance,
       "qtechvplsGroups": qtechvplsGroups,
       "qtechvplsGroup": qtechvplsGroup,
       "qtechvplsPwBindGroup": qtechvplsPwBindGroup,
       "qtechvplsNotificationGroup": qtechvplsNotificationGroup}
)
