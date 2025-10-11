# SNMP MIB module (NEWTEC-IP2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-IP2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:02 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcNetworkAddress) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcNetworkAddress")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ntcIp2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450)
)
if mibBuilder.loadTexts:
    ntcIp2.setRevisions(
        ("2017-07-10 12:00",
         "2015-09-25 11:00",
         "2014-09-23 07:00",
         "2014-09-09 09:00",
         "2014-07-08 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcIP2Objects_ObjectIdentity = ObjectIdentity
ntcIP2Objects = _NtcIP2Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1)
)
if mibBuilder.loadTexts:
    ntcIP2Objects.setStatus("current")
_NtcIP2Cfg_ObjectIdentity = ObjectIdentity
ntcIP2Cfg = _NtcIP2Cfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1)
)
if mibBuilder.loadTexts:
    ntcIP2Cfg.setStatus("current")
_NtcIP2CfgIPIfTable_Object = MibTable
ntcIP2CfgIPIfTable = _NtcIP2CfgIPIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ntcIP2CfgIPIfTable.setStatus("current")
_NtcIP2CfgIPIfEntry_Object = MibTableRow
ntcIP2CfgIPIfEntry = _NtcIP2CfgIPIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 1, 1)
)
ntcIP2CfgIPIfEntry.setIndexNames(
    (0, "NEWTEC-IP2-MIB", "ntcIP2CfgIPIfInterface"),
)
if mibBuilder.loadTexts:
    ntcIP2CfgIPIfEntry.setStatus("current")


class _NtcIP2CfgIPIfInterface_Type(DisplayString):
    """Custom type ntcIP2CfgIPIfInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_NtcIP2CfgIPIfInterface_Type.__name__ = "DisplayString"
_NtcIP2CfgIPIfInterface_Object = MibTableColumn
ntcIP2CfgIPIfInterface = _NtcIP2CfgIPIfInterface_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 1, 1, 1),
    _NtcIP2CfgIPIfInterface_Type()
)
ntcIP2CfgIPIfInterface.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcIP2CfgIPIfInterface.setStatus("current")
_NtcIP2CfgIPIfRowStatus_Type = RowStatus
_NtcIP2CfgIPIfRowStatus_Object = MibTableColumn
ntcIP2CfgIPIfRowStatus = _NtcIP2CfgIPIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 1, 1, 2),
    _NtcIP2CfgIPIfRowStatus_Type()
)
ntcIP2CfgIPIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2CfgIPIfRowStatus.setStatus("current")
_NtcIP2IfPhysIPAddr_Type = NtcNetworkAddress
_NtcIP2IfPhysIPAddr_Object = MibTableColumn
ntcIP2IfPhysIPAddr = _NtcIP2IfPhysIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 1, 1, 3),
    _NtcIP2IfPhysIPAddr_Type()
)
ntcIP2IfPhysIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2IfPhysIPAddr.setStatus("current")
_NtcIP2IfIPAddr_Type = NtcNetworkAddress
_NtcIP2IfIPAddr_Object = MibTableColumn
ntcIP2IfIPAddr = _NtcIP2IfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 1, 1, 4),
    _NtcIP2IfIPAddr_Type()
)
ntcIP2IfIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2IfIPAddr.setStatus("current")


class _NtcIP2IfState_Type(Integer32):
    """Custom type ntcIP2IfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcIP2IfState_Type.__name__ = "Integer32"
_NtcIP2IfState_Object = MibTableColumn
ntcIP2IfState = _NtcIP2IfState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 1, 1, 5),
    _NtcIP2IfState_Type()
)
ntcIP2IfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIP2IfState.setStatus("current")
_NtcIP2CfgMCastIfTable_Object = MibTable
ntcIP2CfgMCastIfTable = _NtcIP2CfgMCastIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ntcIP2CfgMCastIfTable.setStatus("current")
_NtcIP2CfgMCastIfEntry_Object = MibTableRow
ntcIP2CfgMCastIfEntry = _NtcIP2CfgMCastIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1)
)
ntcIP2CfgMCastIfEntry.setIndexNames(
    (0, "NEWTEC-IP2-MIB", "ntcIP2CfgMCastIfName"),
)
if mibBuilder.loadTexts:
    ntcIP2CfgMCastIfEntry.setStatus("current")


class _NtcIP2CfgMCastIfName_Type(DisplayString):
    """Custom type ntcIP2CfgMCastIfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcIP2CfgMCastIfName_Type.__name__ = "DisplayString"
_NtcIP2CfgMCastIfName_Object = MibTableColumn
ntcIP2CfgMCastIfName = _NtcIP2CfgMCastIfName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1, 1),
    _NtcIP2CfgMCastIfName_Type()
)
ntcIP2CfgMCastIfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcIP2CfgMCastIfName.setStatus("current")
_NtcIP2CfgMCastIfRowStatus_Type = RowStatus
_NtcIP2CfgMCastIfRowStatus_Object = MibTableColumn
ntcIP2CfgMCastIfRowStatus = _NtcIP2CfgMCastIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1, 2),
    _NtcIP2CfgMCastIfRowStatus_Type()
)
ntcIP2CfgMCastIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2CfgMCastIfRowStatus.setStatus("current")


class _NtcIP2MCastIfName_Type(OctetString):
    """Custom type ntcIP2MCastIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcIP2MCastIfName_Type.__name__ = "OctetString"
_NtcIP2MCastIfName_Object = MibTableColumn
ntcIP2MCastIfName = _NtcIP2MCastIfName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1, 3),
    _NtcIP2MCastIfName_Type()
)
ntcIP2MCastIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2MCastIfName.setStatus("current")
_NtcIP2MCastIfIPAddr_Type = IpAddress
_NtcIP2MCastIfIPAddr_Object = MibTableColumn
ntcIP2MCastIfIPAddr = _NtcIP2MCastIfIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1, 4),
    _NtcIP2MCastIfIPAddr_Type()
)
ntcIP2MCastIfIPAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2MCastIfIPAddr.setStatus("current")
_NtcIP2MCastIfSrcAddr_Type = IpAddress
_NtcIP2MCastIfSrcAddr_Object = MibTableColumn
ntcIP2MCastIfSrcAddr = _NtcIP2MCastIfSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1, 5),
    _NtcIP2MCastIfSrcAddr_Type()
)
ntcIP2MCastIfSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2MCastIfSrcAddr.setStatus("current")


class _NtcIP2MCastIfState_Type(Integer32):
    """Custom type ntcIP2MCastIfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcIP2MCastIfState_Type.__name__ = "Integer32"
_NtcIP2MCastIfState_Object = MibTableColumn
ntcIP2MCastIfState = _NtcIP2MCastIfState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1, 6),
    _NtcIP2MCastIfState_Type()
)
ntcIP2MCastIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIP2MCastIfState.setStatus("current")
_NtcIP2MCastIfSrcAddrB_Type = IpAddress
_NtcIP2MCastIfSrcAddrB_Object = MibTableColumn
ntcIP2MCastIfSrcAddrB = _NtcIP2MCastIfSrcAddrB_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 2, 1, 7),
    _NtcIP2MCastIfSrcAddrB_Type()
)
ntcIP2MCastIfSrcAddrB.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2MCastIfSrcAddrB.setStatus("current")
_NtcIP2CfgIPRouteTable_Object = MibTable
ntcIP2CfgIPRouteTable = _NtcIP2CfgIPRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ntcIP2CfgIPRouteTable.setStatus("current")
_NtcIP2CfgIPRouteEntry_Object = MibTableRow
ntcIP2CfgIPRouteEntry = _NtcIP2CfgIPRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3, 1)
)
ntcIP2CfgIPRouteEntry.setIndexNames(
    (0, "NEWTEC-IP2-MIB", "ntcIP2CfgIPRouteName"),
)
if mibBuilder.loadTexts:
    ntcIP2CfgIPRouteEntry.setStatus("current")


class _NtcIP2CfgIPRouteName_Type(DisplayString):
    """Custom type ntcIP2CfgIPRouteName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_NtcIP2CfgIPRouteName_Type.__name__ = "DisplayString"
_NtcIP2CfgIPRouteName_Object = MibTableColumn
ntcIP2CfgIPRouteName = _NtcIP2CfgIPRouteName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3, 1, 1),
    _NtcIP2CfgIPRouteName_Type()
)
ntcIP2CfgIPRouteName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcIP2CfgIPRouteName.setStatus("current")
_NtcIP2CfgIPRouteRowStatus_Type = RowStatus
_NtcIP2CfgIPRouteRowStatus_Object = MibTableColumn
ntcIP2CfgIPRouteRowStatus = _NtcIP2CfgIPRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3, 1, 2),
    _NtcIP2CfgIPRouteRowStatus_Type()
)
ntcIP2CfgIPRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2CfgIPRouteRowStatus.setStatus("current")
_NtcIP2IPRouteDstSubnet_Type = NtcNetworkAddress
_NtcIP2IPRouteDstSubnet_Object = MibTableColumn
ntcIP2IPRouteDstSubnet = _NtcIP2IPRouteDstSubnet_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3, 1, 3),
    _NtcIP2IPRouteDstSubnet_Type()
)
ntcIP2IPRouteDstSubnet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2IPRouteDstSubnet.setStatus("current")


class _NtcIP2IPRouteIfName_Type(OctetString):
    """Custom type ntcIP2IPRouteIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_NtcIP2IPRouteIfName_Type.__name__ = "OctetString"
_NtcIP2IPRouteIfName_Object = MibTableColumn
ntcIP2IPRouteIfName = _NtcIP2IPRouteIfName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3, 1, 4),
    _NtcIP2IPRouteIfName_Type()
)
ntcIP2IPRouteIfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2IPRouteIfName.setStatus("current")
_NtcIP2IPRouteGateway_Type = IpAddress
_NtcIP2IPRouteGateway_Object = MibTableColumn
ntcIP2IPRouteGateway = _NtcIP2IPRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3, 1, 5),
    _NtcIP2IPRouteGateway_Type()
)
ntcIP2IPRouteGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntcIP2IPRouteGateway.setStatus("current")


class _NtcIP2IPRouteState_Type(Integer32):
    """Custom type ntcIP2IPRouteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_NtcIP2IPRouteState_Type.__name__ = "Integer32"
_NtcIP2IPRouteState_Object = MibTableColumn
ntcIP2IPRouteState = _NtcIP2IPRouteState_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 3, 1, 6),
    _NtcIP2IPRouteState_Type()
)
ntcIP2IPRouteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIP2IPRouteState.setStatus("current")
_NtcIP2CfgIgmp_ObjectIdentity = ObjectIdentity
ntcIP2CfgIgmp = _NtcIP2CfgIgmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ntcIP2CfgIgmp.setStatus("current")


class _NtcIP2CfgIgmpVersion_Type(Integer32):
    """Custom type ntcIP2CfgIgmpVersion based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("v2", 0),
          ("v3", 1))
    )


_NtcIP2CfgIgmpVersion_Type.__name__ = "Integer32"
_NtcIP2CfgIgmpVersion_Object = MibScalar
ntcIP2CfgIgmpVersion = _NtcIP2CfgIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 1, 4, 1),
    _NtcIP2CfgIgmpVersion_Type()
)
ntcIP2CfgIgmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcIP2CfgIgmpVersion.setStatus("current")
_NtcIP2Alarm_ObjectIdentity = ObjectIdentity
ntcIP2Alarm = _NtcIP2Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 2)
)
if mibBuilder.loadTexts:
    ntcIP2Alarm.setStatus("current")
_NtcIP2AlmInconsistent_Type = NtcAlarmState
_NtcIP2AlmInconsistent_Object = MibScalar
ntcIP2AlmInconsistent = _NtcIP2AlmInconsistent_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 2, 1),
    _NtcIP2AlmInconsistent_Type()
)
ntcIP2AlmInconsistent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIP2AlmInconsistent.setStatus("current")
_NtcIP2AlmGwUnreachable_Type = NtcAlarmState
_NtcIP2AlmGwUnreachable_Object = MibScalar
ntcIP2AlmGwUnreachable = _NtcIP2AlmGwUnreachable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 1, 2, 2),
    _NtcIP2AlmGwUnreachable_Type()
)
ntcIP2AlmGwUnreachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcIP2AlmGwUnreachable.setStatus("current")
_NtcIP2Conformance_ObjectIdentity = ObjectIdentity
ntcIP2Conformance = _NtcIP2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 2)
)
if mibBuilder.loadTexts:
    ntcIP2Conformance.setStatus("current")
_NtcIP2ConfCompliance_ObjectIdentity = ObjectIdentity
ntcIP2ConfCompliance = _NtcIP2ConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 2, 1)
)
if mibBuilder.loadTexts:
    ntcIP2ConfCompliance.setStatus("current")
_NtcIP2ConfGroup_ObjectIdentity = ObjectIdentity
ntcIP2ConfGroup = _NtcIP2ConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 2, 2)
)
if mibBuilder.loadTexts:
    ntcIP2ConfGroup.setStatus("current")

# Managed Objects groups

ntcIP2ConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 2, 2, 1)
)
ntcIP2ConfGrpV1Standard.setObjects(
      *(("NEWTEC-IP2-MIB", "ntcIP2CfgIPIfRowStatus"),
        ("NEWTEC-IP2-MIB", "ntcIP2IfPhysIPAddr"),
        ("NEWTEC-IP2-MIB", "ntcIP2IfIPAddr"),
        ("NEWTEC-IP2-MIB", "ntcIP2IfState"),
        ("NEWTEC-IP2-MIB", "ntcIP2CfgMCastIfRowStatus"),
        ("NEWTEC-IP2-MIB", "ntcIP2MCastIfName"),
        ("NEWTEC-IP2-MIB", "ntcIP2MCastIfIPAddr"),
        ("NEWTEC-IP2-MIB", "ntcIP2MCastIfSrcAddr"),
        ("NEWTEC-IP2-MIB", "ntcIP2MCastIfState"),
        ("NEWTEC-IP2-MIB", "ntcIP2MCastIfSrcAddrB"),
        ("NEWTEC-IP2-MIB", "ntcIP2CfgIPRouteRowStatus"),
        ("NEWTEC-IP2-MIB", "ntcIP2IPRouteDstSubnet"),
        ("NEWTEC-IP2-MIB", "ntcIP2IPRouteIfName"),
        ("NEWTEC-IP2-MIB", "ntcIP2IPRouteGateway"),
        ("NEWTEC-IP2-MIB", "ntcIP2IPRouteState"),
        ("NEWTEC-IP2-MIB", "ntcIP2CfgIgmpVersion"),
        ("NEWTEC-IP2-MIB", "ntcIP2AlmInconsistent"),
        ("NEWTEC-IP2-MIB", "ntcIP2AlmGwUnreachable"))
)
if mibBuilder.loadTexts:
    ntcIP2ConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcIP2ConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 450, 2, 1, 1)
)
ntcIP2ConfCompV1Standard.setObjects(
    ("NEWTEC-IP2-MIB", "ntcIP2ConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcIP2ConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-IP2-MIB",
    **{"ntcIp2": ntcIp2,
       "ntcIP2Objects": ntcIP2Objects,
       "ntcIP2Cfg": ntcIP2Cfg,
       "ntcIP2CfgIPIfTable": ntcIP2CfgIPIfTable,
       "ntcIP2CfgIPIfEntry": ntcIP2CfgIPIfEntry,
       "ntcIP2CfgIPIfInterface": ntcIP2CfgIPIfInterface,
       "ntcIP2CfgIPIfRowStatus": ntcIP2CfgIPIfRowStatus,
       "ntcIP2IfPhysIPAddr": ntcIP2IfPhysIPAddr,
       "ntcIP2IfIPAddr": ntcIP2IfIPAddr,
       "ntcIP2IfState": ntcIP2IfState,
       "ntcIP2CfgMCastIfTable": ntcIP2CfgMCastIfTable,
       "ntcIP2CfgMCastIfEntry": ntcIP2CfgMCastIfEntry,
       "ntcIP2CfgMCastIfName": ntcIP2CfgMCastIfName,
       "ntcIP2CfgMCastIfRowStatus": ntcIP2CfgMCastIfRowStatus,
       "ntcIP2MCastIfName": ntcIP2MCastIfName,
       "ntcIP2MCastIfIPAddr": ntcIP2MCastIfIPAddr,
       "ntcIP2MCastIfSrcAddr": ntcIP2MCastIfSrcAddr,
       "ntcIP2MCastIfState": ntcIP2MCastIfState,
       "ntcIP2MCastIfSrcAddrB": ntcIP2MCastIfSrcAddrB,
       "ntcIP2CfgIPRouteTable": ntcIP2CfgIPRouteTable,
       "ntcIP2CfgIPRouteEntry": ntcIP2CfgIPRouteEntry,
       "ntcIP2CfgIPRouteName": ntcIP2CfgIPRouteName,
       "ntcIP2CfgIPRouteRowStatus": ntcIP2CfgIPRouteRowStatus,
       "ntcIP2IPRouteDstSubnet": ntcIP2IPRouteDstSubnet,
       "ntcIP2IPRouteIfName": ntcIP2IPRouteIfName,
       "ntcIP2IPRouteGateway": ntcIP2IPRouteGateway,
       "ntcIP2IPRouteState": ntcIP2IPRouteState,
       "ntcIP2CfgIgmp": ntcIP2CfgIgmp,
       "ntcIP2CfgIgmpVersion": ntcIP2CfgIgmpVersion,
       "ntcIP2Alarm": ntcIP2Alarm,
       "ntcIP2AlmInconsistent": ntcIP2AlmInconsistent,
       "ntcIP2AlmGwUnreachable": ntcIP2AlmGwUnreachable,
       "ntcIP2Conformance": ntcIP2Conformance,
       "ntcIP2ConfCompliance": ntcIP2ConfCompliance,
       "ntcIP2ConfCompV1Standard": ntcIP2ConfCompV1Standard,
       "ntcIP2ConfGroup": ntcIP2ConfGroup,
       "ntcIP2ConfGrpV1Standard": ntcIP2ConfGrpV1Standard}
)
