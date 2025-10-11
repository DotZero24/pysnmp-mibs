# SNMP MIB module (ZTE-AN-ZESR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-ZESR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:26 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

(VlanId,
 ZxAnIfindex,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "VlanId",
    "ZxAnIfindex",
    "zxAn")


# MODULE-IDENTITY

zxAnZesrMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnZesrObjects_ObjectIdentity = ObjectIdentity
zxAnZesrObjects = _ZxAnZesrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1)
)
_ZxAnZesrTable_Object = MibTable
zxAnZesrTable = _ZxAnZesrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnZesrTable.setStatus("current")
_ZxAnZesrEntry_Object = MibTableRow
zxAnZesrEntry = _ZxAnZesrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1)
)
zxAnZesrEntry.setIndexNames(
    (0, "ZTE-AN-ZESR-MIB", "zxAnZesrCtrlVlanId"),
)
if mibBuilder.loadTexts:
    zxAnZesrEntry.setStatus("current")
_ZxAnZesrCtrlVlanId_Type = VlanId
_ZxAnZesrCtrlVlanId_Object = MibTableColumn
zxAnZesrCtrlVlanId = _ZxAnZesrCtrlVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 1),
    _ZxAnZesrCtrlVlanId_Type()
)
zxAnZesrCtrlVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnZesrCtrlVlanId.setStatus("current")


class _ZxAnZesrCtrlVlanMstpInstance_Type(Integer32):
    """Custom type zxAnZesrCtrlVlanMstpInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ZxAnZesrCtrlVlanMstpInstance_Type.__name__ = "Integer32"
_ZxAnZesrCtrlVlanMstpInstance_Object = MibTableColumn
zxAnZesrCtrlVlanMstpInstance = _ZxAnZesrCtrlVlanMstpInstance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 2),
    _ZxAnZesrCtrlVlanMstpInstance_Type()
)
zxAnZesrCtrlVlanMstpInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrCtrlVlanMstpInstance.setStatus("current")


class _ZxAnZesrNodeType_Type(Integer32):
    """Custom type zxAnZesrNodeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("transit", 2))
    )


_ZxAnZesrNodeType_Type.__name__ = "Integer32"
_ZxAnZesrNodeType_Object = MibTableColumn
zxAnZesrNodeType = _ZxAnZesrNodeType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 3),
    _ZxAnZesrNodeType_Type()
)
zxAnZesrNodeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrNodeType.setStatus("current")
_ZxAnZesrPrimaryPort_Type = ZxAnIfindex
_ZxAnZesrPrimaryPort_Object = MibTableColumn
zxAnZesrPrimaryPort = _ZxAnZesrPrimaryPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 4),
    _ZxAnZesrPrimaryPort_Type()
)
zxAnZesrPrimaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrPrimaryPort.setStatus("current")
_ZxAnZesrSecondaryPort_Type = ZxAnIfindex
_ZxAnZesrSecondaryPort_Object = MibTableColumn
zxAnZesrSecondaryPort = _ZxAnZesrSecondaryPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 5),
    _ZxAnZesrSecondaryPort_Type()
)
zxAnZesrSecondaryPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrSecondaryPort.setStatus("current")


class _ZxAnZesrProtectVlanMstpInstance_Type(Integer32):
    """Custom type zxAnZesrProtectVlanMstpInstance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ZxAnZesrProtectVlanMstpInstance_Type.__name__ = "Integer32"
_ZxAnZesrProtectVlanMstpInstance_Object = MibTableColumn
zxAnZesrProtectVlanMstpInstance = _ZxAnZesrProtectVlanMstpInstance_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 6),
    _ZxAnZesrProtectVlanMstpInstance_Type()
)
zxAnZesrProtectVlanMstpInstance.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrProtectVlanMstpInstance.setStatus("current")


class _ZxAnZesrHealthCheckInterval_Type(Integer32):
    """Custom type zxAnZesrHealthCheckInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000),
    )


_ZxAnZesrHealthCheckInterval_Type.__name__ = "Integer32"
_ZxAnZesrHealthCheckInterval_Object = MibTableColumn
zxAnZesrHealthCheckInterval = _ZxAnZesrHealthCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 7),
    _ZxAnZesrHealthCheckInterval_Type()
)
zxAnZesrHealthCheckInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrHealthCheckInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnZesrHealthCheckInterval.setUnits("ms")


class _ZxAnZesrFailPeriodTime_Type(Integer32):
    """Custom type zxAnZesrFailPeriodTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3000),
    )


_ZxAnZesrFailPeriodTime_Type.__name__ = "Integer32"
_ZxAnZesrFailPeriodTime_Object = MibTableColumn
zxAnZesrFailPeriodTime = _ZxAnZesrFailPeriodTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 8),
    _ZxAnZesrFailPeriodTime_Type()
)
zxAnZesrFailPeriodTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrFailPeriodTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnZesrFailPeriodTime.setUnits("ms")


class _ZxAnZesrPreForwardingTime_Type(Integer32):
    """Custom type zxAnZesrPreForwardingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3000),
    )


_ZxAnZesrPreForwardingTime_Type.__name__ = "Integer32"
_ZxAnZesrPreForwardingTime_Object = MibTableColumn
zxAnZesrPreForwardingTime = _ZxAnZesrPreForwardingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 9),
    _ZxAnZesrPreForwardingTime_Type()
)
zxAnZesrPreForwardingTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrPreForwardingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnZesrPreForwardingTime.setUnits("ms")


class _ZxAnZesrDomainState_Type(Integer32):
    """Custom type zxAnZesrDomainState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("complete", 2),
          ("failed", 3),
          ("linksup", 4),
          ("linkdown", 5),
          ("preforwarding", 6),
          ("init", 7))
    )


_ZxAnZesrDomainState_Type.__name__ = "Integer32"
_ZxAnZesrDomainState_Object = MibTableColumn
zxAnZesrDomainState = _ZxAnZesrDomainState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 10),
    _ZxAnZesrDomainState_Type()
)
zxAnZesrDomainState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnZesrDomainState.setStatus("current")


class _ZxAnZesrPrimaryPortState_Type(Integer32):
    """Custom type zxAnZesrPrimaryPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("preforward", 2),
          ("forward", 3))
    )


_ZxAnZesrPrimaryPortState_Type.__name__ = "Integer32"
_ZxAnZesrPrimaryPortState_Object = MibTableColumn
zxAnZesrPrimaryPortState = _ZxAnZesrPrimaryPortState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 11),
    _ZxAnZesrPrimaryPortState_Type()
)
zxAnZesrPrimaryPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnZesrPrimaryPortState.setStatus("current")


class _ZxAnZesrSecondaryPortState_Type(Integer32):
    """Custom type zxAnZesrSecondaryPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("block", 1),
          ("preforward", 2),
          ("forward", 3))
    )


_ZxAnZesrSecondaryPortState_Type.__name__ = "Integer32"
_ZxAnZesrSecondaryPortState_Object = MibTableColumn
zxAnZesrSecondaryPortState = _ZxAnZesrSecondaryPortState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 12),
    _ZxAnZesrSecondaryPortState_Type()
)
zxAnZesrSecondaryPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnZesrSecondaryPortState.setStatus("current")


class _ZxAnZesrProtectVlanList_Type(OctetString):
    """Custom type zxAnZesrProtectVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(512, 512),
    )
    fixed_length = 512


_ZxAnZesrProtectVlanList_Type.__name__ = "OctetString"
_ZxAnZesrProtectVlanList_Object = MibTableColumn
zxAnZesrProtectVlanList = _ZxAnZesrProtectVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 13),
    _ZxAnZesrProtectVlanList_Type()
)
zxAnZesrProtectVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrProtectVlanList.setStatus("current")


class _ZxAnZesrStandbyEnable_Type(Integer32):
    """Custom type zxAnZesrStandbyEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnZesrStandbyEnable_Type.__name__ = "Integer32"
_ZxAnZesrStandbyEnable_Object = MibTableColumn
zxAnZesrStandbyEnable = _ZxAnZesrStandbyEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 14),
    _ZxAnZesrStandbyEnable_Type()
)
zxAnZesrStandbyEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrStandbyEnable.setStatus("current")
_ZxAnZesrRowStatus_Type = RowStatus
_ZxAnZesrRowStatus_Object = MibTableColumn
zxAnZesrRowStatus = _ZxAnZesrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 1, 1, 1, 50),
    _ZxAnZesrRowStatus_Type()
)
zxAnZesrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnZesrRowStatus.setStatus("current")
_ZxAnZesrTraps_ObjectIdentity = ObjectIdentity
zxAnZesrTraps = _ZxAnZesrTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 2)
)

# Managed Objects groups


# Notification objects

zxAnZesrSwappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 9, 2, 1)
)
zxAnZesrSwappedTrap.setObjects(
      *(("ZTE-AN-ZESR-MIB", "zxAnZesrDomainState"),
        ("ZTE-AN-ZESR-MIB", "zxAnZesrPrimaryPortState"),
        ("ZTE-AN-ZESR-MIB", "zxAnZesrSecondaryPortState"))
)
if mibBuilder.loadTexts:
    zxAnZesrSwappedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-ZESR-MIB",
    **{"zxAnZesrMib": zxAnZesrMib,
       "zxAnZesrObjects": zxAnZesrObjects,
       "zxAnZesrTable": zxAnZesrTable,
       "zxAnZesrEntry": zxAnZesrEntry,
       "zxAnZesrCtrlVlanId": zxAnZesrCtrlVlanId,
       "zxAnZesrCtrlVlanMstpInstance": zxAnZesrCtrlVlanMstpInstance,
       "zxAnZesrNodeType": zxAnZesrNodeType,
       "zxAnZesrPrimaryPort": zxAnZesrPrimaryPort,
       "zxAnZesrSecondaryPort": zxAnZesrSecondaryPort,
       "zxAnZesrProtectVlanMstpInstance": zxAnZesrProtectVlanMstpInstance,
       "zxAnZesrHealthCheckInterval": zxAnZesrHealthCheckInterval,
       "zxAnZesrFailPeriodTime": zxAnZesrFailPeriodTime,
       "zxAnZesrPreForwardingTime": zxAnZesrPreForwardingTime,
       "zxAnZesrDomainState": zxAnZesrDomainState,
       "zxAnZesrPrimaryPortState": zxAnZesrPrimaryPortState,
       "zxAnZesrSecondaryPortState": zxAnZesrSecondaryPortState,
       "zxAnZesrProtectVlanList": zxAnZesrProtectVlanList,
       "zxAnZesrStandbyEnable": zxAnZesrStandbyEnable,
       "zxAnZesrRowStatus": zxAnZesrRowStatus,
       "zxAnZesrTraps": zxAnZesrTraps,
       "zxAnZesrSwappedTrap": zxAnZesrSwappedTrap}
)
