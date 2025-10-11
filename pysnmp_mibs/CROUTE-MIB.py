# SNMP MIB module (CROUTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/avaya/CROUTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:04:28 2025
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

(lannet,) = mibBuilder.importSymbols(
    "GEN-MIB",
    "lannet")

(AreaID,
 DesignatedRouterPriority,
 HelloRange,
 Metric,
 PositiveInteger,
 Status,
 TOSType,
 UpToMaxAge) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "PositiveInteger",
    "Status",
    "TOSType",
    "UpToMaxAge")

(RouteTag,) = mibBuilder.importSymbols(
    "RIPv2-MIB",
    "RouteTag")

(OwnerString,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "OwnerString")

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


# Types definitions



class RowStatus(Integer32):
    """Custom type RowStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("notInService", 2),
          ("notReady", 3),
          ("createAndGo", 4),
          ("createAndWait", 5),
          ("destroy", 6))
    )





class NetNum(Integer32):
    """Custom type NetNum based on Integer32"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Croute_ObjectIdentity = ObjectIdentity
croute = _Croute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31)
)
_IpRoute_ObjectIdentity = ObjectIdentity
ipRoute = _IpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1)
)
_IpGlobals_ObjectIdentity = ObjectIdentity
ipGlobals = _IpGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1)
)


class _IpGlobalsBOOTPRelayStatus_Type(Integer32):
    """Custom type ipGlobalsBOOTPRelayStatus based on Integer32"""
    defaultValue = 2

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
        *(("enable", 1),
          ("disable", 2),
          ("backup", 3),
          ("activeBackup", 4))
    )


_IpGlobalsBOOTPRelayStatus_Type.__name__ = "Integer32"
_IpGlobalsBOOTPRelayStatus_Object = MibScalar
ipGlobalsBOOTPRelayStatus = _IpGlobalsBOOTPRelayStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 1),
    _IpGlobalsBOOTPRelayStatus_Type()
)
ipGlobalsBOOTPRelayStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsBOOTPRelayStatus.setStatus("mandatory")


class _IpGlobalsICMPErrMsgEnable_Type(Integer32):
    """Custom type ipGlobalsICMPErrMsgEnable based on Integer32"""
    defaultValue = 1

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


_IpGlobalsICMPErrMsgEnable_Type.__name__ = "Integer32"
_IpGlobalsICMPErrMsgEnable_Object = MibScalar
ipGlobalsICMPErrMsgEnable = _IpGlobalsICMPErrMsgEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 2),
    _IpGlobalsICMPErrMsgEnable_Type()
)
ipGlobalsICMPErrMsgEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsICMPErrMsgEnable.setStatus("mandatory")


class _IpGlobalsARPInactiveTimeout_Type(Integer32):
    """Custom type ipGlobalsARPInactiveTimeout based on Integer32"""
    defaultValue = 14400


_IpGlobalsARPInactiveTimeout_Type.__name__ = "Integer32"
_IpGlobalsARPInactiveTimeout_Object = MibScalar
ipGlobalsARPInactiveTimeout = _IpGlobalsARPInactiveTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 3),
    _IpGlobalsARPInactiveTimeout_Type()
)
ipGlobalsARPInactiveTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsARPInactiveTimeout.setStatus("mandatory")
_IpGlobalsPrimaryManagementIPAddress_Type = IpAddress
_IpGlobalsPrimaryManagementIPAddress_Object = MibScalar
ipGlobalsPrimaryManagementIPAddress = _IpGlobalsPrimaryManagementIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 4),
    _IpGlobalsPrimaryManagementIPAddress_Type()
)
ipGlobalsPrimaryManagementIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsPrimaryManagementIPAddress.setStatus("mandatory")
_IpGlobalsNextPrimaryManagementIPAddress_Type = IpAddress
_IpGlobalsNextPrimaryManagementIPAddress_Object = MibScalar
ipGlobalsNextPrimaryManagementIPAddress = _IpGlobalsNextPrimaryManagementIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 1, 5),
    _IpGlobalsNextPrimaryManagementIPAddress_Type()
)
ipGlobalsNextPrimaryManagementIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipGlobalsNextPrimaryManagementIPAddress.setStatus("mandatory")
_IpInterfaceTable_Object = MibTable
ipInterfaceTable = _IpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2)
)
if mibBuilder.loadTexts:
    ipInterfaceTable.setStatus("mandatory")
_IpInterfaceEntry_Object = MibTableRow
ipInterfaceEntry = _IpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1)
)
ipInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipInterfaceAddr"),
)
if mibBuilder.loadTexts:
    ipInterfaceEntry.setStatus("mandatory")
_IpInterfaceAddr_Type = IpAddress
_IpInterfaceAddr_Object = MibTableColumn
ipInterfaceAddr = _IpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 1),
    _IpInterfaceAddr_Type()
)
ipInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceAddr.setStatus("mandatory")
_IpInterfaceNetMask_Type = IpAddress
_IpInterfaceNetMask_Object = MibTableColumn
ipInterfaceNetMask = _IpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 2),
    _IpInterfaceNetMask_Type()
)
ipInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceNetMask.setStatus("mandatory")


class _IpInterfaceLowerIfAlias_Type(DisplayString):
    """Custom type ipInterfaceLowerIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpInterfaceLowerIfAlias_Type.__name__ = "DisplayString"
_IpInterfaceLowerIfAlias_Object = MibTableColumn
ipInterfaceLowerIfAlias = _IpInterfaceLowerIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 3),
    _IpInterfaceLowerIfAlias_Type()
)
ipInterfaceLowerIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceLowerIfAlias.setStatus("mandatory")


class _IpInterfaceType_Type(Integer32):
    """Custom type ipInterfaceType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nBMA", 2),
          ("ptp", 4),
          ("loopback", 8),
          ("tunnel", 16))
    )


_IpInterfaceType_Type.__name__ = "Integer32"
_IpInterfaceType_Object = MibTableColumn
ipInterfaceType = _IpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 4),
    _IpInterfaceType_Type()
)
ipInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceType.setStatus("mandatory")


class _IpInterfaceForwardIpBroadcast_Type(Integer32):
    """Custom type ipInterfaceForwardIpBroadcast based on Integer32"""
    defaultValue = 1

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


_IpInterfaceForwardIpBroadcast_Type.__name__ = "Integer32"
_IpInterfaceForwardIpBroadcast_Object = MibTableColumn
ipInterfaceForwardIpBroadcast = _IpInterfaceForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 5),
    _IpInterfaceForwardIpBroadcast_Type()
)
ipInterfaceForwardIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceForwardIpBroadcast.setStatus("mandatory")


class _IpInterfaceBroadcastAddr_Type(Integer32):
    """Custom type ipInterfaceBroadcastAddr based on Integer32"""
    defaultValue = 1


_IpInterfaceBroadcastAddr_Type.__name__ = "Integer32"
_IpInterfaceBroadcastAddr_Object = MibTableColumn
ipInterfaceBroadcastAddr = _IpInterfaceBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 6),
    _IpInterfaceBroadcastAddr_Type()
)
ipInterfaceBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceBroadcastAddr.setStatus("mandatory")


class _IpInterfaceProxyArp_Type(Integer32):
    """Custom type ipInterfaceProxyArp based on Integer32"""
    defaultValue = 2

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


_IpInterfaceProxyArp_Type.__name__ = "Integer32"
_IpInterfaceProxyArp_Object = MibTableColumn
ipInterfaceProxyArp = _IpInterfaceProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 7),
    _IpInterfaceProxyArp_Type()
)
ipInterfaceProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceProxyArp.setStatus("mandatory")
_IpInterfaceStatus_Type = RowStatus
_IpInterfaceStatus_Object = MibTableColumn
ipInterfaceStatus = _IpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 8),
    _IpInterfaceStatus_Type()
)
ipInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceStatus.setStatus("mandatory")
_IpInterfaceMainRouterAddr_Type = IpAddress
_IpInterfaceMainRouterAddr_Object = MibTableColumn
ipInterfaceMainRouterAddr = _IpInterfaceMainRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 9),
    _IpInterfaceMainRouterAddr_Type()
)
ipInterfaceMainRouterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceMainRouterAddr.setStatus("mandatory")


class _IpInterfaceARPServerStatus_Type(Integer32):
    """Custom type ipInterfaceARPServerStatus based on Integer32"""
    defaultValue = 2

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


_IpInterfaceARPServerStatus_Type.__name__ = "Integer32"
_IpInterfaceARPServerStatus_Object = MibTableColumn
ipInterfaceARPServerStatus = _IpInterfaceARPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 10),
    _IpInterfaceARPServerStatus_Type()
)
ipInterfaceARPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceARPServerStatus.setStatus("mandatory")


class _IpInterfaceName_Type(DisplayString):
    """Custom type ipInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpInterfaceName_Type.__name__ = "DisplayString"
_IpInterfaceName_Object = MibTableColumn
ipInterfaceName = _IpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 11),
    _IpInterfaceName_Type()
)
ipInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceName.setStatus("mandatory")


class _IpInterfaceNetbiosRebroadcast_Type(Integer32):
    """Custom type ipInterfaceNetbiosRebroadcast based on Integer32"""
    defaultValue = 4

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
        *(("inbound", 1),
          ("outbound", 2),
          ("both", 3),
          ("disable", 4))
    )


_IpInterfaceNetbiosRebroadcast_Type.__name__ = "Integer32"
_IpInterfaceNetbiosRebroadcast_Object = MibTableColumn
ipInterfaceNetbiosRebroadcast = _IpInterfaceNetbiosRebroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 12),
    _IpInterfaceNetbiosRebroadcast_Type()
)
ipInterfaceNetbiosRebroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceNetbiosRebroadcast.setStatus("mandatory")


class _IpInterfaceIcmpRedirects_Type(Integer32):
    """Custom type ipInterfaceIcmpRedirects based on Integer32"""
    defaultValue = 1

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


_IpInterfaceIcmpRedirects_Type.__name__ = "Integer32"
_IpInterfaceIcmpRedirects_Object = MibTableColumn
ipInterfaceIcmpRedirects = _IpInterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 13),
    _IpInterfaceIcmpRedirects_Type()
)
ipInterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceIcmpRedirects.setStatus("mandatory")


class _IpInterfaceOperStatus_Type(Integer32):
    """Custom type ipInterfaceOperStatus based on Integer32"""
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


_IpInterfaceOperStatus_Type.__name__ = "Integer32"
_IpInterfaceOperStatus_Object = MibTableColumn
ipInterfaceOperStatus = _IpInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 14),
    _IpInterfaceOperStatus_Type()
)
ipInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceOperStatus.setStatus("mandatory")


class _IpInterfaceDhcpRelay_Type(Integer32):
    """Custom type ipInterfaceDhcpRelay based on Integer32"""
    defaultValue = 2

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


_IpInterfaceDhcpRelay_Type.__name__ = "Integer32"
_IpInterfaceDhcpRelay_Object = MibTableColumn
ipInterfaceDhcpRelay = _IpInterfaceDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 15),
    _IpInterfaceDhcpRelay_Type()
)
ipInterfaceDhcpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceDhcpRelay.setStatus("mandatory")


class _IpInterfaceAddrType_Type(Integer32):
    """Custom type ipInterfaceAddrType based on Integer32"""
    defaultValue = 1

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
        *(("static", 1),
          ("pppIpcp", 2),
          ("dhcp", 3),
          ("unnumbered", 4))
    )


_IpInterfaceAddrType_Type.__name__ = "Integer32"
_IpInterfaceAddrType_Object = MibTableColumn
ipInterfaceAddrType = _IpInterfaceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 16),
    _IpInterfaceAddrType_Type()
)
ipInterfaceAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceAddrType.setStatus("mandatory")
_IpInterfaceAddrUnnumbered_Type = IpAddress
_IpInterfaceAddrUnnumbered_Object = MibTableColumn
ipInterfaceAddrUnnumbered = _IpInterfaceAddrUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 17),
    _IpInterfaceAddrUnnumbered_Type()
)
ipInterfaceAddrUnnumbered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceAddrUnnumbered.setStatus("mandatory")


class _IpInterfaceUnnumberedLowerIfAlias_Type(DisplayString):
    """Custom type ipInterfaceUnnumberedLowerIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpInterfaceUnnumberedLowerIfAlias_Type.__name__ = "DisplayString"
_IpInterfaceUnnumberedLowerIfAlias_Object = MibTableColumn
ipInterfaceUnnumberedLowerIfAlias = _IpInterfaceUnnumberedLowerIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 18),
    _IpInterfaceUnnumberedLowerIfAlias_Type()
)
ipInterfaceUnnumberedLowerIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipInterfaceUnnumberedLowerIfAlias.setStatus("mandatory")


class _IpInterfaceReasmMaxSize_Type(Integer32):
    """Custom type ipInterfaceReasmMaxSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_IpInterfaceReasmMaxSize_Type.__name__ = "Integer32"
_IpInterfaceReasmMaxSize_Object = MibTableColumn
ipInterfaceReasmMaxSize = _IpInterfaceReasmMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 2, 1, 19),
    _IpInterfaceReasmMaxSize_Type()
)
ipInterfaceReasmMaxSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipInterfaceReasmMaxSize.setStatus("mandatory")
_RipGlobals_ObjectIdentity = ObjectIdentity
ripGlobals = _RipGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3)
)


class _RipGlobalsRIPEnable_Type(Integer32):
    """Custom type ripGlobalsRIPEnable based on Integer32"""
    defaultValue = 1

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


_RipGlobalsRIPEnable_Type.__name__ = "Integer32"
_RipGlobalsRIPEnable_Object = MibScalar
ripGlobalsRIPEnable = _RipGlobalsRIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 1),
    _RipGlobalsRIPEnable_Type()
)
ripGlobalsRIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsRIPEnable.setStatus("mandatory")


class _RipGlobalsLeakOSPFIntoRIP_Type(Integer32):
    """Custom type ripGlobalsLeakOSPFIntoRIP based on Integer32"""
    defaultValue = 2

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


_RipGlobalsLeakOSPFIntoRIP_Type.__name__ = "Integer32"
_RipGlobalsLeakOSPFIntoRIP_Object = MibScalar
ripGlobalsLeakOSPFIntoRIP = _RipGlobalsLeakOSPFIntoRIP_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 2),
    _RipGlobalsLeakOSPFIntoRIP_Type()
)
ripGlobalsLeakOSPFIntoRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsLeakOSPFIntoRIP.setStatus("mandatory")


class _RipGlobalsLeakStaticIntoRIP_Type(Integer32):
    """Custom type ripGlobalsLeakStaticIntoRIP based on Integer32"""
    defaultValue = 1

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


_RipGlobalsLeakStaticIntoRIP_Type.__name__ = "Integer32"
_RipGlobalsLeakStaticIntoRIP_Object = MibScalar
ripGlobalsLeakStaticIntoRIP = _RipGlobalsLeakStaticIntoRIP_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 3),
    _RipGlobalsLeakStaticIntoRIP_Type()
)
ripGlobalsLeakStaticIntoRIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsLeakStaticIntoRIP.setStatus("mandatory")


class _RipGlobalsPeriodicUpdateTimer_Type(Integer32):
    """Custom type ripGlobalsPeriodicUpdateTimer based on Integer32"""
    defaultValue = 30


_RipGlobalsPeriodicUpdateTimer_Type.__name__ = "Integer32"
_RipGlobalsPeriodicUpdateTimer_Object = MibScalar
ripGlobalsPeriodicUpdateTimer = _RipGlobalsPeriodicUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 4),
    _RipGlobalsPeriodicUpdateTimer_Type()
)
ripGlobalsPeriodicUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsPeriodicUpdateTimer.setStatus("mandatory")


class _RipGlobalsPeriodicInvalidRouteTimer_Type(Integer32):
    """Custom type ripGlobalsPeriodicInvalidRouteTimer based on Integer32"""
    defaultValue = 180


_RipGlobalsPeriodicInvalidRouteTimer_Type.__name__ = "Integer32"
_RipGlobalsPeriodicInvalidRouteTimer_Object = MibScalar
ripGlobalsPeriodicInvalidRouteTimer = _RipGlobalsPeriodicInvalidRouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 5),
    _RipGlobalsPeriodicInvalidRouteTimer_Type()
)
ripGlobalsPeriodicInvalidRouteTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsPeriodicInvalidRouteTimer.setStatus("mandatory")


class _RipGlobalsDefaultExportMetric_Type(Integer32):
    """Custom type ripGlobalsDefaultExportMetric based on Integer32"""
    defaultValue = 1


_RipGlobalsDefaultExportMetric_Type.__name__ = "Integer32"
_RipGlobalsDefaultExportMetric_Object = MibScalar
ripGlobalsDefaultExportMetric = _RipGlobalsDefaultExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 3, 6),
    _RipGlobalsDefaultExportMetric_Type()
)
ripGlobalsDefaultExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripGlobalsDefaultExportMetric.setStatus("mandatory")
_RipInterfaceTable_Object = MibTable
ripInterfaceTable = _RipInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4)
)
if mibBuilder.loadTexts:
    ripInterfaceTable.setStatus("mandatory")
_RipInterfaceEntry_Object = MibTableRow
ripInterfaceEntry = _RipInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1)
)
ripInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "ripInterfaceAddr"),
)
if mibBuilder.loadTexts:
    ripInterfaceEntry.setStatus("mandatory")
_RipInterfaceAddr_Type = IpAddress
_RipInterfaceAddr_Object = MibTableColumn
ripInterfaceAddr = _RipInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 1),
    _RipInterfaceAddr_Type()
)
ripInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInterfaceAddr.setStatus("mandatory")


class _RipInterfaceMetric_Type(Integer32):
    """Custom type ripInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RipInterfaceMetric_Type.__name__ = "Integer32"
_RipInterfaceMetric_Object = MibTableColumn
ripInterfaceMetric = _RipInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 2),
    _RipInterfaceMetric_Type()
)
ripInterfaceMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceMetric.setStatus("mandatory")


class _RipInterfaceSplitHorizon_Type(Integer32):
    """Custom type ripInterfaceSplitHorizon based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("poisonReverse", 1),
          ("splitHorizon", 2),
          ("none", 3))
    )


_RipInterfaceSplitHorizon_Type.__name__ = "Integer32"
_RipInterfaceSplitHorizon_Object = MibTableColumn
ripInterfaceSplitHorizon = _RipInterfaceSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 3),
    _RipInterfaceSplitHorizon_Type()
)
ripInterfaceSplitHorizon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceSplitHorizon.setStatus("mandatory")


class _RipInterfaceAcceptDefaultRoute_Type(Integer32):
    """Custom type ripInterfaceAcceptDefaultRoute based on Integer32"""
    defaultValue = 1

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


_RipInterfaceAcceptDefaultRoute_Type.__name__ = "Integer32"
_RipInterfaceAcceptDefaultRoute_Object = MibTableColumn
ripInterfaceAcceptDefaultRoute = _RipInterfaceAcceptDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 4),
    _RipInterfaceAcceptDefaultRoute_Type()
)
ripInterfaceAcceptDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceAcceptDefaultRoute.setStatus("mandatory")


class _RipInterfaceSendDefaultRoute_Type(Integer32):
    """Custom type ripInterfaceSendDefaultRoute based on Integer32"""
    defaultValue = 2

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


_RipInterfaceSendDefaultRoute_Type.__name__ = "Integer32"
_RipInterfaceSendDefaultRoute_Object = MibTableColumn
ripInterfaceSendDefaultRoute = _RipInterfaceSendDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 5),
    _RipInterfaceSendDefaultRoute_Type()
)
ripInterfaceSendDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceSendDefaultRoute.setStatus("mandatory")


class _RipInterfaceState_Type(Integer32):
    """Custom type ripInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_RipInterfaceState_Type.__name__ = "Integer32"
_RipInterfaceState_Object = MibTableColumn
ripInterfaceState = _RipInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 6),
    _RipInterfaceState_Type()
)
ripInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripInterfaceState.setStatus("mandatory")


class _RipInterfaceSendMode_Type(Integer32):
    """Custom type ripInterfaceSendMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("defaultOnly", 2),
          ("doNotSend", 3))
    )


_RipInterfaceSendMode_Type.__name__ = "Integer32"
_RipInterfaceSendMode_Object = MibTableColumn
ripInterfaceSendMode = _RipInterfaceSendMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 7),
    _RipInterfaceSendMode_Type()
)
ripInterfaceSendMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceSendMode.setStatus("mandatory")


class _RipInterfaceVersion_Type(Integer32):
    """Custom type ripInterfaceVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip1", 1),
          ("rip2", 2))
    )


_RipInterfaceVersion_Type.__name__ = "Integer32"
_RipInterfaceVersion_Object = MibTableColumn
ripInterfaceVersion = _RipInterfaceVersion_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 4, 1, 8),
    _RipInterfaceVersion_Type()
)
ripInterfaceVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripInterfaceVersion.setStatus("mandatory")
_OspfGlobals_ObjectIdentity = ObjectIdentity
ospfGlobals = _OspfGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5)
)


class _OspfGlobalsLeakRIPIntoOSPF_Type(Integer32):
    """Custom type ospfGlobalsLeakRIPIntoOSPF based on Integer32"""
    defaultValue = 2

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


_OspfGlobalsLeakRIPIntoOSPF_Type.__name__ = "Integer32"
_OspfGlobalsLeakRIPIntoOSPF_Object = MibScalar
ospfGlobalsLeakRIPIntoOSPF = _OspfGlobalsLeakRIPIntoOSPF_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5, 1),
    _OspfGlobalsLeakRIPIntoOSPF_Type()
)
ospfGlobalsLeakRIPIntoOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalsLeakRIPIntoOSPF.setStatus("mandatory")


class _OspfGlobalsLeakStaticIntoOSPF_Type(Integer32):
    """Custom type ospfGlobalsLeakStaticIntoOSPF based on Integer32"""
    defaultValue = 1

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


_OspfGlobalsLeakStaticIntoOSPF_Type.__name__ = "Integer32"
_OspfGlobalsLeakStaticIntoOSPF_Object = MibScalar
ospfGlobalsLeakStaticIntoOSPF = _OspfGlobalsLeakStaticIntoOSPF_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5, 2),
    _OspfGlobalsLeakStaticIntoOSPF_Type()
)
ospfGlobalsLeakStaticIntoOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalsLeakStaticIntoOSPF.setStatus("mandatory")


class _OspfGlobalsLeakDirectIntoOSPF_Type(Integer32):
    """Custom type ospfGlobalsLeakDirectIntoOSPF based on Integer32"""
    defaultValue = 1

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


_OspfGlobalsLeakDirectIntoOSPF_Type.__name__ = "Integer32"
_OspfGlobalsLeakDirectIntoOSPF_Object = MibScalar
ospfGlobalsLeakDirectIntoOSPF = _OspfGlobalsLeakDirectIntoOSPF_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5, 3),
    _OspfGlobalsLeakDirectIntoOSPF_Type()
)
ospfGlobalsLeakDirectIntoOSPF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalsLeakDirectIntoOSPF.setStatus("mandatory")


class _OspfGlobalsDefaultExportMetric_Type(Integer32):
    """Custom type ospfGlobalsDefaultExportMetric based on Integer32"""
    defaultValue = 20


_OspfGlobalsDefaultExportMetric_Type.__name__ = "Integer32"
_OspfGlobalsDefaultExportMetric_Object = MibScalar
ospfGlobalsDefaultExportMetric = _OspfGlobalsDefaultExportMetric_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 5, 4),
    _OspfGlobalsDefaultExportMetric_Type()
)
ospfGlobalsDefaultExportMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfGlobalsDefaultExportMetric.setStatus("mandatory")
_RelayTable_Object = MibTable
relayTable = _RelayTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6)
)
if mibBuilder.loadTexts:
    relayTable.setStatus("mandatory")
_RelayEntry_Object = MibTableRow
relayEntry = _RelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1)
)
relayEntry.setIndexNames(
    (0, "CROUTE-MIB", "relayVlIndex"),
)
if mibBuilder.loadTexts:
    relayEntry.setStatus("mandatory")
_RelayVlIndex_Type = Integer32
_RelayVlIndex_Object = MibTableColumn
relayVlIndex = _RelayVlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 1),
    _RelayVlIndex_Type()
)
relayVlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relayVlIndex.setStatus("mandatory")
_RelayVlPrimaryServerAddr_Type = IpAddress
_RelayVlPrimaryServerAddr_Object = MibTableColumn
relayVlPrimaryServerAddr = _RelayVlPrimaryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 2),
    _RelayVlPrimaryServerAddr_Type()
)
relayVlPrimaryServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlPrimaryServerAddr.setStatus("mandatory")
_RelayVlSeconderyServerAddr_Type = IpAddress
_RelayVlSeconderyServerAddr_Object = MibTableColumn
relayVlSeconderyServerAddr = _RelayVlSeconderyServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 3),
    _RelayVlSeconderyServerAddr_Type()
)
relayVlSeconderyServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlSeconderyServerAddr.setStatus("mandatory")
_RelayVlStatus_Type = RowStatus
_RelayVlStatus_Object = MibTableColumn
relayVlStatus = _RelayVlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 4),
    _RelayVlStatus_Type()
)
relayVlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlStatus.setStatus("mandatory")
_RelayVlRelayAddr_Type = IpAddress
_RelayVlRelayAddr_Object = MibTableColumn
relayVlRelayAddr = _RelayVlRelayAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 6, 1, 5),
    _RelayVlRelayAddr_Type()
)
relayVlRelayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relayVlRelayAddr.setStatus("mandatory")
_IpAccessGlobals_ObjectIdentity = ObjectIdentity
ipAccessGlobals = _IpAccessGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 7)
)


class _IpAccessControlEnable_Type(Integer32):
    """Custom type ipAccessControlEnable based on Integer32"""
    defaultValue = 2

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


_IpAccessControlEnable_Type.__name__ = "Integer32"
_IpAccessControlEnable_Object = MibScalar
ipAccessControlEnable = _IpAccessControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 7, 1),
    _IpAccessControlEnable_Type()
)
ipAccessControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlEnable.setStatus("mandatory")
_IpAccessControlTable_Object = MibTable
ipAccessControlTable = _IpAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8)
)
if mibBuilder.loadTexts:
    ipAccessControlTable.setStatus("mandatory")
_IpAccessControlEntry_Object = MibTableRow
ipAccessControlEntry = _IpAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1)
)
ipAccessControlEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipAccessControlIndex"),
)
if mibBuilder.loadTexts:
    ipAccessControlEntry.setStatus("mandatory")
_IpAccessControlIndex_Type = Integer32
_IpAccessControlIndex_Object = MibTableColumn
ipAccessControlIndex = _IpAccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 1),
    _IpAccessControlIndex_Type()
)
ipAccessControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipAccessControlIndex.setStatus("mandatory")
_IpAccessControlSrcAddr_Type = IpAddress
_IpAccessControlSrcAddr_Object = MibTableColumn
ipAccessControlSrcAddr = _IpAccessControlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 2),
    _IpAccessControlSrcAddr_Type()
)
ipAccessControlSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlSrcAddr.setStatus("mandatory")
_IpAccessControlSrcMask_Type = IpAddress
_IpAccessControlSrcMask_Object = MibTableColumn
ipAccessControlSrcMask = _IpAccessControlSrcMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 3),
    _IpAccessControlSrcMask_Type()
)
ipAccessControlSrcMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlSrcMask.setStatus("mandatory")
_IpAccessControlDstAddr_Type = IpAddress
_IpAccessControlDstAddr_Object = MibTableColumn
ipAccessControlDstAddr = _IpAccessControlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 4),
    _IpAccessControlDstAddr_Type()
)
ipAccessControlDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlDstAddr.setStatus("mandatory")
_IpAccessControlDstMask_Type = IpAddress
_IpAccessControlDstMask_Object = MibTableColumn
ipAccessControlDstMask = _IpAccessControlDstMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 5),
    _IpAccessControlDstMask_Type()
)
ipAccessControlDstMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlDstMask.setStatus("mandatory")


class _IpAccessControlOperation_Type(Integer32):
    """Custom type ipAccessControlOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2),
          ("blockAndReport", 3))
    )


_IpAccessControlOperation_Type.__name__ = "Integer32"
_IpAccessControlOperation_Object = MibTableColumn
ipAccessControlOperation = _IpAccessControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 6),
    _IpAccessControlOperation_Type()
)
ipAccessControlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlOperation.setStatus("mandatory")


class _IpAccessControlActivation_Type(Integer32):
    """Custom type ipAccessControlActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wire-speed", 1),
          ("regular", 2))
    )


_IpAccessControlActivation_Type.__name__ = "Integer32"
_IpAccessControlActivation_Object = MibTableColumn
ipAccessControlActivation = _IpAccessControlActivation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 7),
    _IpAccessControlActivation_Type()
)
ipAccessControlActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlActivation.setStatus("mandatory")


class _IpAccessControlProtocol_Type(Integer32):
    """Custom type ipAccessControlProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              17,
              256)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("tcp", 6),
          ("udp", 17),
          ("none", 256))
    )


_IpAccessControlProtocol_Type.__name__ = "Integer32"
_IpAccessControlProtocol_Object = MibTableColumn
ipAccessControlProtocol = _IpAccessControlProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 8),
    _IpAccessControlProtocol_Type()
)
ipAccessControlProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlProtocol.setStatus("mandatory")


class _IpAccessControlApplication_Type(Integer32):
    """Custom type ipAccessControlApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(21,
              23,
              25,
              80,
              110,
              161,
              162,
              65536,
              65537)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 21),
          ("telnet", 23),
          ("smtp", 25),
          ("http", 80),
          ("pop3", 110),
          ("snmp", 161),
          ("snmpTrap", 162),
          ("above1023", 65536),
          ("none", 65537))
    )


_IpAccessControlApplication_Type.__name__ = "Integer32"
_IpAccessControlApplication_Object = MibTableColumn
ipAccessControlApplication = _IpAccessControlApplication_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 9),
    _IpAccessControlApplication_Type()
)
ipAccessControlApplication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlApplication.setStatus("mandatory")
_IpAccessControlStatus_Type = RowStatus
_IpAccessControlStatus_Object = MibTableColumn
ipAccessControlStatus = _IpAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 8, 1, 10),
    _IpAccessControlStatus_Type()
)
ipAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAccessControlStatus.setStatus("mandatory")
_IpRedundancyGlobals_ObjectIdentity = ObjectIdentity
ipRedundancyGlobals = _IpRedundancyGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9)
)


class _IpRedundancyStatus_Type(Integer32):
    """Custom type ipRedundancyStatus based on Integer32"""
    defaultValue = 2

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
        *(("enable", 1),
          ("disable", 2),
          ("inactive", 3),
          ("active", 4))
    )


_IpRedundancyStatus_Type.__name__ = "Integer32"
_IpRedundancyStatus_Object = MibScalar
ipRedundancyStatus = _IpRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9, 1),
    _IpRedundancyStatus_Type()
)
ipRedundancyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundancyStatus.setStatus("mandatory")


class _IpRedundancyTimeout_Type(Integer32):
    """Custom type ipRedundancyTimeout based on Integer32"""
    defaultValue = 12


_IpRedundancyTimeout_Type.__name__ = "Integer32"
_IpRedundancyTimeout_Object = MibScalar
ipRedundancyTimeout = _IpRedundancyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9, 2),
    _IpRedundancyTimeout_Type()
)
ipRedundancyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundancyTimeout.setStatus("mandatory")


class _IpRedundancyPollingInterval_Type(Integer32):
    """Custom type ipRedundancyPollingInterval based on Integer32"""
    defaultValue = 3


_IpRedundancyPollingInterval_Type.__name__ = "Integer32"
_IpRedundancyPollingInterval_Object = MibScalar
ipRedundancyPollingInterval = _IpRedundancyPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 9, 3),
    _IpRedundancyPollingInterval_Type()
)
ipRedundancyPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRedundancyPollingInterval.setStatus("mandatory")
_IpShortcutGlobals_ObjectIdentity = ObjectIdentity
ipShortcutGlobals = _IpShortcutGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 10)
)


class _IpShortcutARPServerStatus_Type(Integer32):
    """Custom type ipShortcutARPServerStatus based on Integer32"""
    defaultValue = 2

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


_IpShortcutARPServerStatus_Type.__name__ = "Integer32"
_IpShortcutARPServerStatus_Object = MibScalar
ipShortcutARPServerStatus = _IpShortcutARPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 10, 1),
    _IpShortcutARPServerStatus_Type()
)
ipShortcutARPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipShortcutARPServerStatus.setStatus("mandatory")
_IpMulticastInterfaceTable_Object = MibTable
ipMulticastInterfaceTable = _IpMulticastInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11)
)
if mibBuilder.loadTexts:
    ipMulticastInterfaceTable.setStatus("mandatory")
_IpMulticastInterfaceEntry_Object = MibTableRow
ipMulticastInterfaceEntry = _IpMulticastInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1)
)
ipMulticastInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipMulticastInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ipMulticastInterfaceEntry.setStatus("mandatory")
_IpMulticastInterfaceIfIndex_Type = Integer32
_IpMulticastInterfaceIfIndex_Object = MibTableColumn
ipMulticastInterfaceIfIndex = _IpMulticastInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 1),
    _IpMulticastInterfaceIfIndex_Type()
)
ipMulticastInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMulticastInterfaceIfIndex.setStatus("mandatory")


class _IpMulticastInterfaceSendAll_Type(Integer32):
    """Custom type ipMulticastInterfaceSendAll based on Integer32"""
    defaultValue = 2

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


_IpMulticastInterfaceSendAll_Type.__name__ = "Integer32"
_IpMulticastInterfaceSendAll_Object = MibTableColumn
ipMulticastInterfaceSendAll = _IpMulticastInterfaceSendAll_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 2),
    _IpMulticastInterfaceSendAll_Type()
)
ipMulticastInterfaceSendAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMulticastInterfaceSendAll.setStatus("mandatory")


class _IpMulticastInterfaceState_Type(Integer32):
    """Custom type ipMulticastInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpMulticastInterfaceState_Type.__name__ = "Integer32"
_IpMulticastInterfaceState_Object = MibTableColumn
ipMulticastInterfaceState = _IpMulticastInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 3),
    _IpMulticastInterfaceState_Type()
)
ipMulticastInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMulticastInterfaceState.setStatus("mandatory")


class _IpMulticastInterfaceStatus_Type(RowStatus):
    """Custom type ipMulticastInterfaceStatus based on RowStatus"""
    defaultValue = 1


_IpMulticastInterfaceStatus_Type.__name__ = "RowStatus"
_IpMulticastInterfaceStatus_Object = MibTableColumn
ipMulticastInterfaceStatus = _IpMulticastInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 11, 1, 4),
    _IpMulticastInterfaceStatus_Type()
)
ipMulticastInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipMulticastInterfaceStatus.setStatus("mandatory")
_DistributionListTable_Object = MibTable
distributionListTable = _DistributionListTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12)
)
if mibBuilder.loadTexts:
    distributionListTable.setStatus("mandatory")
_DistributionListEntry_Object = MibTableRow
distributionListEntry = _DistributionListEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1)
)
distributionListEntry.setIndexNames(
    (0, "CROUTE-MIB", "distributionListRoutingProtocol"),
    (0, "CROUTE-MIB", "distributionListDirection"),
    (0, "CROUTE-MIB", "distributionListIfIndex"),
    (0, "CROUTE-MIB", "distributionListRouteProtocol"),
    (0, "CROUTE-MIB", "distributionListProtocolSpecific1"),
    (0, "CROUTE-MIB", "distributionListProtocolSpecific2"),
    (0, "CROUTE-MIB", "distributionListProtocolSpecific3"),
    (0, "CROUTE-MIB", "distributionListProtocolSpecific4"),
    (0, "CROUTE-MIB", "distributionListProtocolSpecific5"),
)
if mibBuilder.loadTexts:
    distributionListEntry.setStatus("mandatory")


class _DistributionListRoutingProtocol_Type(Integer32):
    """Custom type distributionListRoutingProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rip", 1),
          ("ospf", 2),
          ("bgp4", 3))
    )


_DistributionListRoutingProtocol_Type.__name__ = "Integer32"
_DistributionListRoutingProtocol_Object = MibTableColumn
distributionListRoutingProtocol = _DistributionListRoutingProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 1),
    _DistributionListRoutingProtocol_Type()
)
distributionListRoutingProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionListRoutingProtocol.setStatus("mandatory")


class _DistributionListDirection_Type(Integer32):
    """Custom type distributionListDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("import", 1),
          ("export", 2))
    )


_DistributionListDirection_Type.__name__ = "Integer32"
_DistributionListDirection_Object = MibTableColumn
distributionListDirection = _DistributionListDirection_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 2),
    _DistributionListDirection_Type()
)
distributionListDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionListDirection.setStatus("mandatory")
_DistributionListIfIndex_Type = Integer32
_DistributionListIfIndex_Object = MibTableColumn
distributionListIfIndex = _DistributionListIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 3),
    _DistributionListIfIndex_Type()
)
distributionListIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionListIfIndex.setStatus("mandatory")


class _DistributionListRouteProtocol_Type(Integer32):
    """Custom type distributionListRouteProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("static", 2),
          ("rip", 3),
          ("ospf", 4),
          ("connected", 5),
          ("bgp4", 6))
    )


_DistributionListRouteProtocol_Type.__name__ = "Integer32"
_DistributionListRouteProtocol_Object = MibTableColumn
distributionListRouteProtocol = _DistributionListRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 4),
    _DistributionListRouteProtocol_Type()
)
distributionListRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    distributionListRouteProtocol.setStatus("mandatory")
_DistributionListProtocolSpecific1_Type = Integer32
_DistributionListProtocolSpecific1_Object = MibTableColumn
distributionListProtocolSpecific1 = _DistributionListProtocolSpecific1_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 5),
    _DistributionListProtocolSpecific1_Type()
)
distributionListProtocolSpecific1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distributionListProtocolSpecific1.setStatus("mandatory")
_DistributionListProtocolSpecific2_Type = Integer32
_DistributionListProtocolSpecific2_Object = MibTableColumn
distributionListProtocolSpecific2 = _DistributionListProtocolSpecific2_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 6),
    _DistributionListProtocolSpecific2_Type()
)
distributionListProtocolSpecific2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distributionListProtocolSpecific2.setStatus("mandatory")
_DistributionListProtocolSpecific3_Type = Integer32
_DistributionListProtocolSpecific3_Object = MibTableColumn
distributionListProtocolSpecific3 = _DistributionListProtocolSpecific3_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 7),
    _DistributionListProtocolSpecific3_Type()
)
distributionListProtocolSpecific3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distributionListProtocolSpecific3.setStatus("mandatory")
_DistributionListProtocolSpecific4_Type = IpAddress
_DistributionListProtocolSpecific4_Object = MibTableColumn
distributionListProtocolSpecific4 = _DistributionListProtocolSpecific4_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 8),
    _DistributionListProtocolSpecific4_Type()
)
distributionListProtocolSpecific4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distributionListProtocolSpecific4.setStatus("mandatory")
_DistributionListProtocolSpecific5_Type = IpAddress
_DistributionListProtocolSpecific5_Object = MibTableColumn
distributionListProtocolSpecific5 = _DistributionListProtocolSpecific5_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 9),
    _DistributionListProtocolSpecific5_Type()
)
distributionListProtocolSpecific5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distributionListProtocolSpecific5.setStatus("mandatory")
_DistributionListAccessListNumber_Type = Integer32
_DistributionListAccessListNumber_Object = MibTableColumn
distributionListAccessListNumber = _DistributionListAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 10),
    _DistributionListAccessListNumber_Type()
)
distributionListAccessListNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distributionListAccessListNumber.setStatus("mandatory")
_DistributionListEntryStatus_Type = RowStatus
_DistributionListEntryStatus_Object = MibTableColumn
distributionListEntryStatus = _DistributionListEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 12, 1, 11),
    _DistributionListEntryStatus_Type()
)
distributionListEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    distributionListEntryStatus.setStatus("mandatory")
_IpEZ2RouteMgmt_ObjectIdentity = ObjectIdentity
ipEZ2RouteMgmt = _IpEZ2RouteMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13)
)
_IpEZ2BoostRouterTable_Object = MibTable
ipEZ2BoostRouterTable = _IpEZ2BoostRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1)
)
if mibBuilder.loadTexts:
    ipEZ2BoostRouterTable.setStatus("mandatory")
_IpEZ2BoostRouterEntry_Object = MibTableRow
ipEZ2BoostRouterEntry = _IpEZ2BoostRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1)
)
ipEZ2BoostRouterEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipEZ2BoostRouterSlot"),
    (0, "CROUTE-MIB", "ipEZ2BoostRouterBRAddress"),
)
if mibBuilder.loadTexts:
    ipEZ2BoostRouterEntry.setStatus("mandatory")
_IpEZ2BoostRouterSlot_Type = Integer32
_IpEZ2BoostRouterSlot_Object = MibTableColumn
ipEZ2BoostRouterSlot = _IpEZ2BoostRouterSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 1),
    _IpEZ2BoostRouterSlot_Type()
)
ipEZ2BoostRouterSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterSlot.setStatus("mandatory")
_IpEZ2BoostRouterBRAddress_Type = IpAddress
_IpEZ2BoostRouterBRAddress_Object = MibTableColumn
ipEZ2BoostRouterBRAddress = _IpEZ2BoostRouterBRAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 2),
    _IpEZ2BoostRouterBRAddress_Type()
)
ipEZ2BoostRouterBRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterBRAddress.setStatus("mandatory")


class _IpEZ2BoostRouterType_Type(Integer32):
    """Custom type ipEZ2BoostRouterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_IpEZ2BoostRouterType_Type.__name__ = "Integer32"
_IpEZ2BoostRouterType_Object = MibTableColumn
ipEZ2BoostRouterType = _IpEZ2BoostRouterType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 3),
    _IpEZ2BoostRouterType_Type()
)
ipEZ2BoostRouterType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterType.setStatus("mandatory")
_IpEZ2BoostRouterStatus_Type = RowStatus
_IpEZ2BoostRouterStatus_Object = MibTableColumn
ipEZ2BoostRouterStatus = _IpEZ2BoostRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 1, 1, 4),
    _IpEZ2BoostRouterStatus_Type()
)
ipEZ2BoostRouterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2BoostRouterStatus.setStatus("mandatory")
_IpEZ2RControlTable_Object = MibTable
ipEZ2RControlTable = _IpEZ2RControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ipEZ2RControlTable.setStatus("mandatory")
_IpEZ2RControlEntry_Object = MibTableRow
ipEZ2RControlEntry = _IpEZ2RControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1)
)
ipEZ2RControlEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipEZ2RControlSlot"),
)
if mibBuilder.loadTexts:
    ipEZ2RControlEntry.setStatus("mandatory")
_IpEZ2RControlSlot_Type = Integer32
_IpEZ2RControlSlot_Object = MibTableColumn
ipEZ2RControlSlot = _IpEZ2RControlSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 1),
    _IpEZ2RControlSlot_Type()
)
ipEZ2RControlSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipEZ2RControlSlot.setStatus("mandatory")


class _IpEZ2RControlBoostedRoutersTimeout_Type(Integer32):
    """Custom type ipEZ2RControlBoostedRoutersTimeout based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 9999999),
    )


_IpEZ2RControlBoostedRoutersTimeout_Type.__name__ = "Integer32"
_IpEZ2RControlBoostedRoutersTimeout_Object = MibTableColumn
ipEZ2RControlBoostedRoutersTimeout = _IpEZ2RControlBoostedRoutersTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 2),
    _IpEZ2RControlBoostedRoutersTimeout_Type()
)
ipEZ2RControlBoostedRoutersTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2RControlBoostedRoutersTimeout.setStatus("mandatory")


class _IpEZ2RControlHostsTimeout_Type(Integer32):
    """Custom type ipEZ2RControlHostsTimeout based on Integer32"""
    defaultValue = 14400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 9999999),
    )


_IpEZ2RControlHostsTimeout_Type.__name__ = "Integer32"
_IpEZ2RControlHostsTimeout_Object = MibTableColumn
ipEZ2RControlHostsTimeout = _IpEZ2RControlHostsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 3),
    _IpEZ2RControlHostsTimeout_Type()
)
ipEZ2RControlHostsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2RControlHostsTimeout.setStatus("mandatory")


class _IpEZ2RControlAutoLearnMode_Type(Integer32):
    """Custom type ipEZ2RControlAutoLearnMode based on Integer32"""
    defaultValue = 1

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


_IpEZ2RControlAutoLearnMode_Type.__name__ = "Integer32"
_IpEZ2RControlAutoLearnMode_Object = MibTableColumn
ipEZ2RControlAutoLearnMode = _IpEZ2RControlAutoLearnMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 13, 2, 1, 5),
    _IpEZ2RControlAutoLearnMode_Type()
)
ipEZ2RControlAutoLearnMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipEZ2RControlAutoLearnMode.setStatus("mandatory")
_IpVRRP_ObjectIdentity = ObjectIdentity
ipVRRP = _IpVRRP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 14)
)


class _IpVRRPAdminStatus_Type(Integer32):
    """Custom type ipVRRPAdminStatus based on Integer32"""
    defaultValue = 2

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


_IpVRRPAdminStatus_Type.__name__ = "Integer32"
_IpVRRPAdminStatus_Object = MibScalar
ipVRRPAdminStatus = _IpVRRPAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 14, 1),
    _IpVRRPAdminStatus_Type()
)
ipVRRPAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipVRRPAdminStatus.setStatus("mandatory")
_IphcObjects_ObjectIdentity = ObjectIdentity
iphcObjects = _IphcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15)
)
_IphcControlTable_Object = MibTable
iphcControlTable = _IphcControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1)
)
if mibBuilder.loadTexts:
    iphcControlTable.setStatus("mandatory")
_IphcControlEntry_Object = MibTableRow
iphcControlEntry = _IphcControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1)
)
iphcControlEntry.setIndexNames(
    (0, "CROUTE-MIB", "iphcIfIndex"),
)
if mibBuilder.loadTexts:
    iphcControlEntry.setStatus("mandatory")


class _IphcIfIndex_Type(Integer32):
    """Custom type iphcIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_IphcIfIndex_Type.__name__ = "Integer32"
_IphcIfIndex_Object = MibTableColumn
iphcIfIndex = _IphcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 1),
    _IphcIfIndex_Type()
)
iphcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphcIfIndex.setStatus("mandatory")


class _IphcControlTcpAdminStatus_Type(Integer32):
    """Custom type iphcControlTcpAdminStatus based on Integer32"""
    defaultValue = 2

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


_IphcControlTcpAdminStatus_Type.__name__ = "Integer32"
_IphcControlTcpAdminStatus_Object = MibTableColumn
iphcControlTcpAdminStatus = _IphcControlTcpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 2),
    _IphcControlTcpAdminStatus_Type()
)
iphcControlTcpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcControlTcpAdminStatus.setStatus("mandatory")


class _IphcTcpSessions_Type(Integer32):
    """Custom type iphcTcpSessions based on Integer32"""
    defaultValue = 16


_IphcTcpSessions_Type.__name__ = "Integer32"
_IphcTcpSessions_Object = MibTableColumn
iphcTcpSessions = _IphcTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 3),
    _IphcTcpSessions_Type()
)
iphcTcpSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcTcpSessions.setStatus("mandatory")
_IphcNegotiatedTcpSessions_Type = Integer32
_IphcNegotiatedTcpSessions_Object = MibTableColumn
iphcNegotiatedTcpSessions = _IphcNegotiatedTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 4),
    _IphcNegotiatedTcpSessions_Type()
)
iphcNegotiatedTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphcNegotiatedTcpSessions.setStatus("mandatory")


class _IphcControlRtpAdminStatus_Type(Integer32):
    """Custom type iphcControlRtpAdminStatus based on Integer32"""
    defaultValue = 2

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


_IphcControlRtpAdminStatus_Type.__name__ = "Integer32"
_IphcControlRtpAdminStatus_Object = MibTableColumn
iphcControlRtpAdminStatus = _IphcControlRtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 5),
    _IphcControlRtpAdminStatus_Type()
)
iphcControlRtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcControlRtpAdminStatus.setStatus("mandatory")


class _IphcRtpSessions_Type(Integer32):
    """Custom type iphcRtpSessions based on Integer32"""
    defaultValue = 16


_IphcRtpSessions_Type.__name__ = "Integer32"
_IphcRtpSessions_Object = MibTableColumn
iphcRtpSessions = _IphcRtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 6),
    _IphcRtpSessions_Type()
)
iphcRtpSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcRtpSessions.setStatus("mandatory")
_IphcNegotiatedRtpSessions_Type = Integer32
_IphcNegotiatedRtpSessions_Object = MibTableColumn
iphcNegotiatedRtpSessions = _IphcNegotiatedRtpSessions_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 7),
    _IphcNegotiatedRtpSessions_Type()
)
iphcNegotiatedRtpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphcNegotiatedRtpSessions.setStatus("mandatory")


class _IphcControlNonTcpAdminStatus_Type(Integer32):
    """Custom type iphcControlNonTcpAdminStatus based on Integer32"""
    defaultValue = 2

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


_IphcControlNonTcpAdminStatus_Type.__name__ = "Integer32"
_IphcControlNonTcpAdminStatus_Object = MibTableColumn
iphcControlNonTcpAdminStatus = _IphcControlNonTcpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 8),
    _IphcControlNonTcpAdminStatus_Type()
)
iphcControlNonTcpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcControlNonTcpAdminStatus.setStatus("mandatory")


class _IphcNonTcpSessions_Type(Integer32):
    """Custom type iphcNonTcpSessions based on Integer32"""
    defaultValue = 0


_IphcNonTcpSessions_Type.__name__ = "Integer32"
_IphcNonTcpSessions_Object = MibTableColumn
iphcNonTcpSessions = _IphcNonTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 9),
    _IphcNonTcpSessions_Type()
)
iphcNonTcpSessions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcNonTcpSessions.setStatus("mandatory")
_IphcNegotiatedNonTcpSessions_Type = Integer32
_IphcNegotiatedNonTcpSessions_Object = MibTableColumn
iphcNegotiatedNonTcpSessions = _IphcNegotiatedNonTcpSessions_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 10),
    _IphcNegotiatedNonTcpSessions_Type()
)
iphcNegotiatedNonTcpSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphcNegotiatedNonTcpSessions.setStatus("mandatory")


class _IphcMaxPeriod_Type(Integer32):
    """Custom type iphcMaxPeriod based on Integer32"""
    defaultValue = 256


_IphcMaxPeriod_Type.__name__ = "Integer32"
_IphcMaxPeriod_Object = MibTableColumn
iphcMaxPeriod = _IphcMaxPeriod_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 11),
    _IphcMaxPeriod_Type()
)
iphcMaxPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcMaxPeriod.setStatus("mandatory")


class _IphcMaxTime_Type(Integer32):
    """Custom type iphcMaxTime based on Integer32"""
    defaultValue = 5


_IphcMaxTime_Type.__name__ = "Integer32"
_IphcMaxTime_Object = MibTableColumn
iphcMaxTime = _IphcMaxTime_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 12),
    _IphcMaxTime_Type()
)
iphcMaxTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcMaxTime.setStatus("mandatory")


class _IphcControRtpMinPortNumber_Type(Integer32):
    """Custom type iphcControRtpMinPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IphcControRtpMinPortNumber_Type.__name__ = "Integer32"
_IphcControRtpMinPortNumber_Object = MibTableColumn
iphcControRtpMinPortNumber = _IphcControRtpMinPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 13),
    _IphcControRtpMinPortNumber_Type()
)
iphcControRtpMinPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcControRtpMinPortNumber.setStatus("mandatory")


class _IphcControRtpMaxPortNumber_Type(Integer32):
    """Custom type iphcControRtpMaxPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IphcControRtpMaxPortNumber_Type.__name__ = "Integer32"
_IphcControRtpMaxPortNumber_Object = MibTableColumn
iphcControRtpMaxPortNumber = _IphcControRtpMaxPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 14),
    _IphcControRtpMaxPortNumber_Type()
)
iphcControRtpMaxPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcControRtpMaxPortNumber.setStatus("mandatory")


class _IphcControlRtpCompressionRatio_Type(Integer32):
    """Custom type iphcControlRtpCompressionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IphcControlRtpCompressionRatio_Type.__name__ = "Integer32"
_IphcControlRtpCompressionRatio_Object = MibTableColumn
iphcControlRtpCompressionRatio = _IphcControlRtpCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 15),
    _IphcControlRtpCompressionRatio_Type()
)
iphcControlRtpCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphcControlRtpCompressionRatio.setStatus("mandatory")


class _IphcControlNonTcpMode_Type(Integer32):
    """Custom type iphcControlNonTcpMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("other", 2))
    )


_IphcControlNonTcpMode_Type.__name__ = "Integer32"
_IphcControlNonTcpMode_Object = MibTableColumn
iphcControlNonTcpMode = _IphcControlNonTcpMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 16),
    _IphcControlNonTcpMode_Type()
)
iphcControlNonTcpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    iphcControlNonTcpMode.setStatus("mandatory")


class _IphcControlTcpCompressionRatio_Type(Integer32):
    """Custom type iphcControlTcpCompressionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IphcControlTcpCompressionRatio_Type.__name__ = "Integer32"
_IphcControlTcpCompressionRatio_Object = MibTableColumn
iphcControlTcpCompressionRatio = _IphcControlTcpCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 17),
    _IphcControlTcpCompressionRatio_Type()
)
iphcControlTcpCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphcControlTcpCompressionRatio.setStatus("mandatory")


class _IphcControlTotalCompressionRatio_Type(Integer32):
    """Custom type iphcControlTotalCompressionRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_IphcControlTotalCompressionRatio_Type.__name__ = "Integer32"
_IphcControlTotalCompressionRatio_Object = MibTableColumn
iphcControlTotalCompressionRatio = _IphcControlTotalCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 15, 1, 1, 18),
    _IphcControlTotalCompressionRatio_Type()
)
iphcControlTotalCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iphcControlTotalCompressionRatio.setStatus("mandatory")
_OspfXtndIfTable_Object = MibTable
ospfXtndIfTable = _OspfXtndIfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 16)
)
if mibBuilder.loadTexts:
    ospfXtndIfTable.setStatus("mandatory")
_OspfXtndIfEntry_Object = MibTableRow
ospfXtndIfEntry = _OspfXtndIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 16, 1)
)
ospfXtndIfEntry.setIndexNames(
    (0, "CROUTE-MIB", "ospfXtndIfIpAddress"),
    (0, "CROUTE-MIB", "ospfXtndIfAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfXtndIfEntry.setStatus("mandatory")
_OspfXtndIfIpAddress_Type = IpAddress
_OspfXtndIfIpAddress_Object = MibTableColumn
ospfXtndIfIpAddress = _OspfXtndIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 16, 1, 1),
    _OspfXtndIfIpAddress_Type()
)
ospfXtndIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfXtndIfIpAddress.setStatus("mandatory")
_OspfXtndIfAddressLessIf_Type = Integer32
_OspfXtndIfAddressLessIf_Object = MibTableColumn
ospfXtndIfAddressLessIf = _OspfXtndIfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 16, 1, 2),
    _OspfXtndIfAddressLessIf_Type()
)
ospfXtndIfAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfXtndIfAddressLessIf.setStatus("mandatory")


class _OspfXtndIfPassiveMode_Type(Integer32):
    """Custom type ospfXtndIfPassiveMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("passive", 2))
    )


_OspfXtndIfPassiveMode_Type.__name__ = "Integer32"
_OspfXtndIfPassiveMode_Object = MibTableColumn
ospfXtndIfPassiveMode = _OspfXtndIfPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 16, 1, 3),
    _OspfXtndIfPassiveMode_Type()
)
ospfXtndIfPassiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfXtndIfPassiveMode.setStatus("mandatory")
_NextHop_ObjectIdentity = ObjectIdentity
nextHop = _NextHop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17)
)
_NextHopListTable_Object = MibTable
nextHopListTable = _NextHopListTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 1)
)
if mibBuilder.loadTexts:
    nextHopListTable.setStatus("mandatory")
_NextHopListEntry_Object = MibTableRow
nextHopListEntry = _NextHopListEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 1, 1)
)
nextHopListEntry.setIndexNames(
    (0, "CROUTE-MIB", "nextHopListIndex"),
)
if mibBuilder.loadTexts:
    nextHopListEntry.setStatus("mandatory")
_NextHopListIndex_Type = Integer32
_NextHopListIndex_Object = MibTableColumn
nextHopListIndex = _NextHopListIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 1, 1, 1),
    _NextHopListIndex_Type()
)
nextHopListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopListIndex.setStatus("mandatory")
_NextHopListName_Type = DisplayString
_NextHopListName_Object = MibTableColumn
nextHopListName = _NextHopListName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 1, 1, 2),
    _NextHopListName_Type()
)
nextHopListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextHopListName.setStatus("mandatory")
_NextHopListRowStatus_Type = RowStatus
_NextHopListRowStatus_Object = MibTableColumn
nextHopListRowStatus = _NextHopListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 1, 1, 3),
    _NextHopListRowStatus_Type()
)
nextHopListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextHopListRowStatus.setStatus("mandatory")


class _NextHopListActive_Type(Integer32):
    """Custom type nextHopListActive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("nonActive", 2))
    )


_NextHopListActive_Type.__name__ = "Integer32"
_NextHopListActive_Object = MibTableColumn
nextHopListActive = _NextHopListActive_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 1, 1, 4),
    _NextHopListActive_Type()
)
nextHopListActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopListActive.setStatus("mandatory")
_NextHopTable_Object = MibTable
nextHopTable = _NextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2)
)
if mibBuilder.loadTexts:
    nextHopTable.setStatus("mandatory")
_NextHopEntry_Object = MibTableRow
nextHopEntry = _NextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1)
)
nextHopEntry.setIndexNames(
    (0, "CROUTE-MIB", "nextHopListIndex"),
    (0, "CROUTE-MIB", "nextHopIndex"),
)
if mibBuilder.loadTexts:
    nextHopEntry.setStatus("mandatory")
_NextHopIndex_Type = Integer32
_NextHopIndex_Object = MibTableColumn
nextHopIndex = _NextHopIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1, 1),
    _NextHopIndex_Type()
)
nextHopIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopIndex.setStatus("mandatory")


class _NextHopType_Type(Integer32):
    """Custom type nextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("iPAddress", 1),
          ("interface", 2),
          ("null0", 3))
    )


_NextHopType_Type.__name__ = "Integer32"
_NextHopType_Object = MibTableColumn
nextHopType = _NextHopType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1, 2),
    _NextHopType_Type()
)
nextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopType.setStatus("mandatory")
_NextHopIP_Type = IpAddress
_NextHopIP_Object = MibTableColumn
nextHopIP = _NextHopIP_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1, 3),
    _NextHopIP_Type()
)
nextHopIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextHopIP.setStatus("mandatory")
_NextHopInterface_Type = DisplayString
_NextHopInterface_Object = MibTableColumn
nextHopInterface = _NextHopInterface_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1, 4),
    _NextHopInterface_Type()
)
nextHopInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextHopInterface.setStatus("mandatory")


class _NextHopStatus_Type(Integer32):
    """Custom type nextHopStatus based on Integer32"""
    defaultValue = 2

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


_NextHopStatus_Type.__name__ = "Integer32"
_NextHopStatus_Object = MibTableColumn
nextHopStatus = _NextHopStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1, 5),
    _NextHopStatus_Type()
)
nextHopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextHopStatus.setStatus("mandatory")
_NextHopRowStatus_Type = Integer32
_NextHopRowStatus_Object = MibTableColumn
nextHopRowStatus = _NextHopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1, 6),
    _NextHopRowStatus_Type()
)
nextHopRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextHopRowStatus.setStatus("mandatory")


class _NextHopTrackId_Type(Unsigned32):
    """Custom type nextHopTrackId based on Unsigned32"""
    defaultValue = 4294967295


_NextHopTrackId_Type.__name__ = "Unsigned32"
_NextHopTrackId_Object = MibTableColumn
nextHopTrackId = _NextHopTrackId_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 17, 2, 1, 7),
    _NextHopTrackId_Type()
)
nextHopTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextHopTrackId.setStatus("mandatory")
_OspfCompleteIfTable_Object = MibTable
ospfCompleteIfTable = _OspfCompleteIfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18)
)
if mibBuilder.loadTexts:
    ospfCompleteIfTable.setStatus("mandatory")
_OspfCompleteIfEntry_Object = MibTableRow
ospfCompleteIfEntry = _OspfCompleteIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1)
)
ospfCompleteIfEntry.setIndexNames(
    (0, "CROUTE-MIB", "ospfCompleteIfIpAddress"),
    (0, "CROUTE-MIB", "ospfCompleteAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfCompleteIfEntry.setStatus("mandatory")
_OspfCompleteIfIpAddress_Type = IpAddress
_OspfCompleteIfIpAddress_Object = MibTableColumn
ospfCompleteIfIpAddress = _OspfCompleteIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 1),
    _OspfCompleteIfIpAddress_Type()
)
ospfCompleteIfIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfIpAddress.setStatus("mandatory")
_OspfCompleteAddressLessIf_Type = Integer32
_OspfCompleteAddressLessIf_Object = MibTableColumn
ospfCompleteAddressLessIf = _OspfCompleteAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 2),
    _OspfCompleteAddressLessIf_Type()
)
ospfCompleteAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteAddressLessIf.setStatus("mandatory")


class _OspfCompleteIfAreaId_Type(AreaID):
    """Custom type ospfCompleteIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_OspfCompleteIfAreaId_Type.__name__ = "AreaID"
_OspfCompleteIfAreaId_Object = MibTableColumn
ospfCompleteIfAreaId = _OspfCompleteIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 3),
    _OspfCompleteIfAreaId_Type()
)
ospfCompleteIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfAreaId.setStatus("mandatory")


class _OspfCompleteIfType_Type(Integer32):
    """Custom type ospfCompleteIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3),
          ("pointToMultipoint", 5))
    )


_OspfCompleteIfType_Type.__name__ = "Integer32"
_OspfCompleteIfType_Object = MibTableColumn
ospfCompleteIfType = _OspfCompleteIfType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 4),
    _OspfCompleteIfType_Type()
)
ospfCompleteIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfType.setStatus("mandatory")


class _OspfCompleteIfAdminStat_Type(Status):
    """Custom type ospfCompleteIfAdminStat based on Status"""
    defaultValue = 1


_OspfCompleteIfAdminStat_Type.__name__ = "Status"
_OspfCompleteIfAdminStat_Object = MibTableColumn
ospfCompleteIfAdminStat = _OspfCompleteIfAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 5),
    _OspfCompleteIfAdminStat_Type()
)
ospfCompleteIfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfAdminStat.setStatus("mandatory")


class _OspfCompleteIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfCompleteIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_OspfCompleteIfRtrPriority_Type.__name__ = "DesignatedRouterPriority"
_OspfCompleteIfRtrPriority_Object = MibTableColumn
ospfCompleteIfRtrPriority = _OspfCompleteIfRtrPriority_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 6),
    _OspfCompleteIfRtrPriority_Type()
)
ospfCompleteIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfRtrPriority.setStatus("mandatory")


class _OspfCompleteIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfCompleteIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfCompleteIfTransitDelay_Type.__name__ = "UpToMaxAge"
_OspfCompleteIfTransitDelay_Object = MibTableColumn
ospfCompleteIfTransitDelay = _OspfCompleteIfTransitDelay_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 7),
    _OspfCompleteIfTransitDelay_Type()
)
ospfCompleteIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfTransitDelay.setStatus("mandatory")


class _OspfCompleteIfRetransInterval_Type(UpToMaxAge):
    """Custom type ospfCompleteIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfCompleteIfRetransInterval_Type.__name__ = "UpToMaxAge"
_OspfCompleteIfRetransInterval_Object = MibTableColumn
ospfCompleteIfRetransInterval = _OspfCompleteIfRetransInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 8),
    _OspfCompleteIfRetransInterval_Type()
)
ospfCompleteIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfRetransInterval.setStatus("mandatory")


class _OspfCompleteIfHelloInterval_Type(HelloRange):
    """Custom type ospfCompleteIfHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfCompleteIfHelloInterval_Type.__name__ = "HelloRange"
_OspfCompleteIfHelloInterval_Object = MibTableColumn
ospfCompleteIfHelloInterval = _OspfCompleteIfHelloInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 9),
    _OspfCompleteIfHelloInterval_Type()
)
ospfCompleteIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfHelloInterval.setStatus("mandatory")


class _OspfCompleteIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type ospfCompleteIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_OspfCompleteIfRtrDeadInterval_Type.__name__ = "PositiveInteger"
_OspfCompleteIfRtrDeadInterval_Object = MibTableColumn
ospfCompleteIfRtrDeadInterval = _OspfCompleteIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 10),
    _OspfCompleteIfRtrDeadInterval_Type()
)
ospfCompleteIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfRtrDeadInterval.setStatus("mandatory")


class _OspfCompleteIfPollInterval_Type(PositiveInteger):
    """Custom type ospfCompleteIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_OspfCompleteIfPollInterval_Type.__name__ = "PositiveInteger"
_OspfCompleteIfPollInterval_Object = MibTableColumn
ospfCompleteIfPollInterval = _OspfCompleteIfPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 11),
    _OspfCompleteIfPollInterval_Type()
)
ospfCompleteIfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfPollInterval.setStatus("mandatory")


class _OspfCompleteIfState_Type(Integer32):
    """Custom type ospfCompleteIfState based on Integer32"""
    defaultValue = 1

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
        *(("down", 1),
          ("loopback", 2),
          ("waiting", 3),
          ("pointToPoint", 4),
          ("designatedRouter", 5),
          ("backupDesignatedRouter", 6),
          ("otherDesignatedRouter", 7))
    )


_OspfCompleteIfState_Type.__name__ = "Integer32"
_OspfCompleteIfState_Object = MibTableColumn
ospfCompleteIfState = _OspfCompleteIfState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 12),
    _OspfCompleteIfState_Type()
)
ospfCompleteIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfState.setStatus("mandatory")


class _OspfCompleteIfDesignatedRouter_Type(IpAddress):
    """Custom type ospfCompleteIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfCompleteIfDesignatedRouter_Type.__name__ = "IpAddress"
_OspfCompleteIfDesignatedRouter_Object = MibTableColumn
ospfCompleteIfDesignatedRouter = _OspfCompleteIfDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 13),
    _OspfCompleteIfDesignatedRouter_Type()
)
ospfCompleteIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfDesignatedRouter.setStatus("mandatory")


class _OspfCompleteIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type ospfCompleteIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfCompleteIfBackupDesignatedRouter_Type.__name__ = "IpAddress"
_OspfCompleteIfBackupDesignatedRouter_Object = MibTableColumn
ospfCompleteIfBackupDesignatedRouter = _OspfCompleteIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 14),
    _OspfCompleteIfBackupDesignatedRouter_Type()
)
ospfCompleteIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfBackupDesignatedRouter.setStatus("mandatory")
_OspfCompleteIfEvents_Type = Counter32
_OspfCompleteIfEvents_Object = MibTableColumn
ospfCompleteIfEvents = _OspfCompleteIfEvents_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 15),
    _OspfCompleteIfEvents_Type()
)
ospfCompleteIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfEvents.setStatus("mandatory")


class _OspfCompleteIfAuthKey_Type(OctetString):
    """Custom type ospfCompleteIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_OspfCompleteIfAuthKey_Type.__name__ = "OctetString"
_OspfCompleteIfAuthKey_Object = MibTableColumn
ospfCompleteIfAuthKey = _OspfCompleteIfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 16),
    _OspfCompleteIfAuthKey_Type()
)
ospfCompleteIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfAuthKey.setStatus("mandatory")
_OspfCompleteIfStatus_Type = RowStatus
_OspfCompleteIfStatus_Object = MibTableColumn
ospfCompleteIfStatus = _OspfCompleteIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 17),
    _OspfCompleteIfStatus_Type()
)
ospfCompleteIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfStatus.setStatus("mandatory")


class _OspfCompleteIfMulticastForwarding_Type(Integer32):
    """Custom type ospfCompleteIfMulticastForwarding based on Integer32"""
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
        *(("blocked", 1),
          ("multicast", 2),
          ("unicast", 3))
    )


_OspfCompleteIfMulticastForwarding_Type.__name__ = "Integer32"
_OspfCompleteIfMulticastForwarding_Object = MibTableColumn
ospfCompleteIfMulticastForwarding = _OspfCompleteIfMulticastForwarding_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 18),
    _OspfCompleteIfMulticastForwarding_Type()
)
ospfCompleteIfMulticastForwarding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfMulticastForwarding.setStatus("mandatory")


class _OspfCompleteIfDemand_Type(TruthValue):
    """Custom type ospfCompleteIfDemand based on TruthValue"""
    defaultValue = 2


_OspfCompleteIfDemand_Type.__name__ = "TruthValue"
_OspfCompleteIfDemand_Object = MibTableColumn
ospfCompleteIfDemand = _OspfCompleteIfDemand_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 19),
    _OspfCompleteIfDemand_Type()
)
ospfCompleteIfDemand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfDemand.setStatus("mandatory")


class _OspfCompleteIfAuthType_Type(Integer32):
    """Custom type ospfCompleteIfAuthType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_OspfCompleteIfAuthType_Type.__name__ = "Integer32"
_OspfCompleteIfAuthType_Object = MibTableColumn
ospfCompleteIfAuthType = _OspfCompleteIfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 18, 1, 20),
    _OspfCompleteIfAuthType_Type()
)
ospfCompleteIfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfAuthType.setStatus("mandatory")
_OspfCompleteIfMetricTable_Object = MibTable
ospfCompleteIfMetricTable = _OspfCompleteIfMetricTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 19)
)
if mibBuilder.loadTexts:
    ospfCompleteIfMetricTable.setStatus("mandatory")
_OspfCompleteIfMetricEntry_Object = MibTableRow
ospfCompleteIfMetricEntry = _OspfCompleteIfMetricEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 19, 1)
)
ospfCompleteIfMetricEntry.setIndexNames(
    (0, "CROUTE-MIB", "ospfCompleteIfMetricIpAddress"),
    (0, "CROUTE-MIB", "ospfCompleteIfMetricAddressLessIf"),
    (0, "CROUTE-MIB", "ospfCompleteIfMetricTOS"),
)
if mibBuilder.loadTexts:
    ospfCompleteIfMetricEntry.setStatus("mandatory")
_OspfCompleteIfMetricIpAddress_Type = IpAddress
_OspfCompleteIfMetricIpAddress_Object = MibTableColumn
ospfCompleteIfMetricIpAddress = _OspfCompleteIfMetricIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 19, 1, 1),
    _OspfCompleteIfMetricIpAddress_Type()
)
ospfCompleteIfMetricIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfMetricIpAddress.setStatus("mandatory")
_OspfCompleteIfMetricAddressLessIf_Type = Integer32
_OspfCompleteIfMetricAddressLessIf_Object = MibTableColumn
ospfCompleteIfMetricAddressLessIf = _OspfCompleteIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 19, 1, 2),
    _OspfCompleteIfMetricAddressLessIf_Type()
)
ospfCompleteIfMetricAddressLessIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfMetricAddressLessIf.setStatus("mandatory")
_OspfCompleteIfMetricTOS_Type = TOSType
_OspfCompleteIfMetricTOS_Object = MibTableColumn
ospfCompleteIfMetricTOS = _OspfCompleteIfMetricTOS_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 19, 1, 3),
    _OspfCompleteIfMetricTOS_Type()
)
ospfCompleteIfMetricTOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfCompleteIfMetricTOS.setStatus("mandatory")
_OspfCompleteIfMetricValue_Type = Metric
_OspfCompleteIfMetricValue_Object = MibTableColumn
ospfCompleteIfMetricValue = _OspfCompleteIfMetricValue_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 19, 1, 4),
    _OspfCompleteIfMetricValue_Type()
)
ospfCompleteIfMetricValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfMetricValue.setStatus("mandatory")
_OspfCompleteIfMetricStatus_Type = RowStatus
_OspfCompleteIfMetricStatus_Object = MibTableColumn
ospfCompleteIfMetricStatus = _OspfCompleteIfMetricStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 19, 1, 5),
    _OspfCompleteIfMetricStatus_Type()
)
ospfCompleteIfMetricStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfCompleteIfMetricStatus.setStatus("mandatory")
_Rip2CompleteIfStatTable_Object = MibTable
rip2CompleteIfStatTable = _Rip2CompleteIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 20)
)
if mibBuilder.loadTexts:
    rip2CompleteIfStatTable.setStatus("mandatory")
_Rip2CompleteIfStatEntry_Object = MibTableRow
rip2CompleteIfStatEntry = _Rip2CompleteIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 20, 1)
)
rip2CompleteIfStatEntry.setIndexNames(
    (0, "CROUTE-MIB", "rip2CompleteIfStatAddress"),
)
if mibBuilder.loadTexts:
    rip2CompleteIfStatEntry.setStatus("mandatory")
_Rip2CompleteIfStatAddress_Type = IpAddress
_Rip2CompleteIfStatAddress_Object = MibTableColumn
rip2CompleteIfStatAddress = _Rip2CompleteIfStatAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 20, 1, 1),
    _Rip2CompleteIfStatAddress_Type()
)
rip2CompleteIfStatAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CompleteIfStatAddress.setStatus("mandatory")
_Rip2CompleteIfStatRcvBadPackets_Type = Counter32
_Rip2CompleteIfStatRcvBadPackets_Object = MibTableColumn
rip2CompleteIfStatRcvBadPackets = _Rip2CompleteIfStatRcvBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 20, 1, 2),
    _Rip2CompleteIfStatRcvBadPackets_Type()
)
rip2CompleteIfStatRcvBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CompleteIfStatRcvBadPackets.setStatus("mandatory")
_Rip2CompleteIfStatRcvBadRoutes_Type = Counter32
_Rip2CompleteIfStatRcvBadRoutes_Object = MibTableColumn
rip2CompleteIfStatRcvBadRoutes = _Rip2CompleteIfStatRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 20, 1, 3),
    _Rip2CompleteIfStatRcvBadRoutes_Type()
)
rip2CompleteIfStatRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CompleteIfStatRcvBadRoutes.setStatus("mandatory")
_Rip2CompleteIfStatSentUpdates_Type = Counter32
_Rip2CompleteIfStatSentUpdates_Object = MibTableColumn
rip2CompleteIfStatSentUpdates = _Rip2CompleteIfStatSentUpdates_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 20, 1, 4),
    _Rip2CompleteIfStatSentUpdates_Type()
)
rip2CompleteIfStatSentUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CompleteIfStatSentUpdates.setStatus("mandatory")
_Rip2CompleteIfStatStatus_Type = RowStatus
_Rip2CompleteIfStatStatus_Object = MibTableColumn
rip2CompleteIfStatStatus = _Rip2CompleteIfStatStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 20, 1, 5),
    _Rip2CompleteIfStatStatus_Type()
)
rip2CompleteIfStatStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfStatStatus.setStatus("mandatory")
_Rip2CompleteIfConfTable_Object = MibTable
rip2CompleteIfConfTable = _Rip2CompleteIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21)
)
if mibBuilder.loadTexts:
    rip2CompleteIfConfTable.setStatus("mandatory")
_Rip2CompleteIfConfEntry_Object = MibTableRow
rip2CompleteIfConfEntry = _Rip2CompleteIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1)
)
rip2CompleteIfConfEntry.setIndexNames(
    (0, "CROUTE-MIB", "rip2CompleteIfConfAddress"),
)
if mibBuilder.loadTexts:
    rip2CompleteIfConfEntry.setStatus("mandatory")
_Rip2CompleteIfConfAddress_Type = IpAddress
_Rip2CompleteIfConfAddress_Object = MibTableColumn
rip2CompleteIfConfAddress = _Rip2CompleteIfConfAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 1),
    _Rip2CompleteIfConfAddress_Type()
)
rip2CompleteIfConfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rip2CompleteIfConfAddress.setStatus("mandatory")


class _Rip2CompleteIfConfDomain_Type(RouteTag):
    """Custom type rip2CompleteIfConfDomain based on RouteTag"""
    defaultHexValue = "0000"


_Rip2CompleteIfConfDomain_Type.__name__ = "RouteTag"
_Rip2CompleteIfConfDomain_Object = MibTableColumn
rip2CompleteIfConfDomain = _Rip2CompleteIfConfDomain_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 2),
    _Rip2CompleteIfConfDomain_Type()
)
rip2CompleteIfConfDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfDomain.setStatus("obsolete")


class _Rip2CompleteIfConfAuthType_Type(Integer32):
    """Custom type rip2CompleteIfConfAuthType based on Integer32"""
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
        *(("noAuthentication", 1),
          ("simplePassword", 2),
          ("md5", 3))
    )


_Rip2CompleteIfConfAuthType_Type.__name__ = "Integer32"
_Rip2CompleteIfConfAuthType_Object = MibTableColumn
rip2CompleteIfConfAuthType = _Rip2CompleteIfConfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 3),
    _Rip2CompleteIfConfAuthType_Type()
)
rip2CompleteIfConfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfAuthType.setStatus("mandatory")


class _Rip2CompleteIfConfAuthKey_Type(OctetString):
    """Custom type rip2CompleteIfConfAuthKey based on OctetString"""
    defaultHexValue = ""

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_Rip2CompleteIfConfAuthKey_Type.__name__ = "OctetString"
_Rip2CompleteIfConfAuthKey_Object = MibTableColumn
rip2CompleteIfConfAuthKey = _Rip2CompleteIfConfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 4),
    _Rip2CompleteIfConfAuthKey_Type()
)
rip2CompleteIfConfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfAuthKey.setStatus("mandatory")


class _Rip2CompleteIfConfSend_Type(Integer32):
    """Custom type rip2CompleteIfConfSend based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("doNotSend", 1),
          ("ripVersion1", 2),
          ("rip1Compatible", 3),
          ("ripVersion2", 4),
          ("ripV1Demand", 5),
          ("ripV2Demand", 6))
    )


_Rip2CompleteIfConfSend_Type.__name__ = "Integer32"
_Rip2CompleteIfConfSend_Object = MibTableColumn
rip2CompleteIfConfSend = _Rip2CompleteIfConfSend_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 5),
    _Rip2CompleteIfConfSend_Type()
)
rip2CompleteIfConfSend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfSend.setStatus("mandatory")


class _Rip2CompleteIfConfReceive_Type(Integer32):
    """Custom type rip2CompleteIfConfReceive based on Integer32"""
    defaultValue = 3

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
        *(("rip1", 1),
          ("rip2", 2),
          ("rip1OrRip2", 3),
          ("doNotRecieve", 4))
    )


_Rip2CompleteIfConfReceive_Type.__name__ = "Integer32"
_Rip2CompleteIfConfReceive_Object = MibTableColumn
rip2CompleteIfConfReceive = _Rip2CompleteIfConfReceive_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 6),
    _Rip2CompleteIfConfReceive_Type()
)
rip2CompleteIfConfReceive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfReceive.setStatus("mandatory")


class _Rip2CompleteIfConfDefaultMetric_Type(Integer32):
    """Custom type rip2CompleteIfConfDefaultMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Rip2CompleteIfConfDefaultMetric_Type.__name__ = "Integer32"
_Rip2CompleteIfConfDefaultMetric_Object = MibTableColumn
rip2CompleteIfConfDefaultMetric = _Rip2CompleteIfConfDefaultMetric_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 7),
    _Rip2CompleteIfConfDefaultMetric_Type()
)
rip2CompleteIfConfDefaultMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfDefaultMetric.setStatus("mandatory")
_Rip2CompleteIfConfStatus_Type = RowStatus
_Rip2CompleteIfConfStatus_Object = MibTableColumn
rip2CompleteIfConfStatus = _Rip2CompleteIfConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 8),
    _Rip2CompleteIfConfStatus_Type()
)
rip2CompleteIfConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfStatus.setStatus("mandatory")
_Rip2CompleteIfConfSrcAddress_Type = IpAddress
_Rip2CompleteIfConfSrcAddress_Object = MibTableColumn
rip2CompleteIfConfSrcAddress = _Rip2CompleteIfConfSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 21, 1, 9),
    _Rip2CompleteIfConfSrcAddress_Type()
)
rip2CompleteIfConfSrcAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rip2CompleteIfConfSrcAddress.setStatus("mandatory")
_IpCidrRouteStaticTable_Object = MibTable
ipCidrRouteStaticTable = _IpCidrRouteStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22)
)
if mibBuilder.loadTexts:
    ipCidrRouteStaticTable.setStatus("mandatory")
_IpCidrRouteStaticEntry_Object = MibTableRow
ipCidrRouteStaticEntry = _IpCidrRouteStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1)
)
ipCidrRouteStaticEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipCidrRouteStaticDest"),
    (0, "CROUTE-MIB", "ipCidrRouteStaticMask"),
    (0, "CROUTE-MIB", "ipCidrRouteStaticIfIndex"),
    (0, "CROUTE-MIB", "ipCidrRouteStaticNextHop"),
    (0, "CROUTE-MIB", "ipCidrRouteStaticPreference"),
)
if mibBuilder.loadTexts:
    ipCidrRouteStaticEntry.setStatus("mandatory")
_IpCidrRouteStaticDest_Type = IpAddress
_IpCidrRouteStaticDest_Object = MibTableColumn
ipCidrRouteStaticDest = _IpCidrRouteStaticDest_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 1),
    _IpCidrRouteStaticDest_Type()
)
ipCidrRouteStaticDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteStaticDest.setStatus("mandatory")
_IpCidrRouteStaticMask_Type = IpAddress
_IpCidrRouteStaticMask_Object = MibTableColumn
ipCidrRouteStaticMask = _IpCidrRouteStaticMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 2),
    _IpCidrRouteStaticMask_Type()
)
ipCidrRouteStaticMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteStaticMask.setStatus("mandatory")


class _IpCidrRouteStaticIfIndex_Type(Integer32):
    """Custom type ipCidrRouteStaticIfIndex based on Integer32"""
    defaultValue = 0


_IpCidrRouteStaticIfIndex_Type.__name__ = "Integer32"
_IpCidrRouteStaticIfIndex_Object = MibTableColumn
ipCidrRouteStaticIfIndex = _IpCidrRouteStaticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 3),
    _IpCidrRouteStaticIfIndex_Type()
)
ipCidrRouteStaticIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteStaticIfIndex.setStatus("mandatory")
_IpCidrRouteStaticNextHop_Type = IpAddress
_IpCidrRouteStaticNextHop_Object = MibTableColumn
ipCidrRouteStaticNextHop = _IpCidrRouteStaticNextHop_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 4),
    _IpCidrRouteStaticNextHop_Type()
)
ipCidrRouteStaticNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteStaticNextHop.setStatus("mandatory")


class _IpCidrRouteStaticPreference_Type(Integer32):
    """Custom type ipCidrRouteStaticPreference based on Integer32"""
    defaultValue = 0


_IpCidrRouteStaticPreference_Type.__name__ = "Integer32"
_IpCidrRouteStaticPreference_Object = MibTableColumn
ipCidrRouteStaticPreference = _IpCidrRouteStaticPreference_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 5),
    _IpCidrRouteStaticPreference_Type()
)
ipCidrRouteStaticPreference.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteStaticPreference.setStatus("mandatory")


class _IpCidrRouteStaticUsedIfIndex_Type(Integer32):
    """Custom type ipCidrRouteStaticUsedIfIndex based on Integer32"""
    defaultValue = 0


_IpCidrRouteStaticUsedIfIndex_Type.__name__ = "Integer32"
_IpCidrRouteStaticUsedIfIndex_Object = MibTableColumn
ipCidrRouteStaticUsedIfIndex = _IpCidrRouteStaticUsedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 6),
    _IpCidrRouteStaticUsedIfIndex_Type()
)
ipCidrRouteStaticUsedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteStaticUsedIfIndex.setStatus("mandatory")
_IpCidrRouteStaticUsedNextHop_Type = IpAddress
_IpCidrRouteStaticUsedNextHop_Object = MibTableColumn
ipCidrRouteStaticUsedNextHop = _IpCidrRouteStaticUsedNextHop_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 7),
    _IpCidrRouteStaticUsedNextHop_Type()
)
ipCidrRouteStaticUsedNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteStaticUsedNextHop.setStatus("mandatory")


class _IpCidrRouteStaticType_Type(Integer32):
    """Custom type ipCidrRouteStaticType based on Integer32"""
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
        *(("via", 1),
          ("discard", 2),
          ("dhcp", 3),
          ("regular", 4))
    )


_IpCidrRouteStaticType_Type.__name__ = "Integer32"
_IpCidrRouteStaticType_Object = MibTableColumn
ipCidrRouteStaticType = _IpCidrRouteStaticType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 8),
    _IpCidrRouteStaticType_Type()
)
ipCidrRouteStaticType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteStaticType.setStatus("mandatory")


class _IpCidrRouteStaticCost_Type(Integer32):
    """Custom type ipCidrRouteStaticCost based on Integer32"""
    defaultValue = 1


_IpCidrRouteStaticCost_Type.__name__ = "Integer32"
_IpCidrRouteStaticCost_Object = MibTableColumn
ipCidrRouteStaticCost = _IpCidrRouteStaticCost_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 9),
    _IpCidrRouteStaticCost_Type()
)
ipCidrRouteStaticCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipCidrRouteStaticCost.setStatus("mandatory")


class _IpCidrRouteStaticPermanent_Type(Integer32):
    """Custom type ipCidrRouteStaticPermanent based on Integer32"""
    defaultValue = 2


_IpCidrRouteStaticPermanent_Type.__name__ = "Integer32"
_IpCidrRouteStaticPermanent_Object = MibTableColumn
ipCidrRouteStaticPermanent = _IpCidrRouteStaticPermanent_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 10),
    _IpCidrRouteStaticPermanent_Type()
)
ipCidrRouteStaticPermanent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipCidrRouteStaticPermanent.setStatus("mandatory")


class _IpCidrRouteStaticTrackId_Type(Unsigned32):
    """Custom type ipCidrRouteStaticTrackId based on Unsigned32"""
    defaultValue = 4294967295


_IpCidrRouteStaticTrackId_Type.__name__ = "Unsigned32"
_IpCidrRouteStaticTrackId_Object = MibTableColumn
ipCidrRouteStaticTrackId = _IpCidrRouteStaticTrackId_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 11),
    _IpCidrRouteStaticTrackId_Type()
)
ipCidrRouteStaticTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipCidrRouteStaticTrackId.setStatus("mandatory")


class _IpCidrRouteStaticActive_Type(Integer32):
    """Custom type ipCidrRouteStaticActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_IpCidrRouteStaticActive_Type.__name__ = "Integer32"
_IpCidrRouteStaticActive_Object = MibTableColumn
ipCidrRouteStaticActive = _IpCidrRouteStaticActive_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 12),
    _IpCidrRouteStaticActive_Type()
)
ipCidrRouteStaticActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteStaticActive.setStatus("mandatory")
_IpCidrRouteStaticRowStatus_Type = RowStatus
_IpCidrRouteStaticRowStatus_Object = MibTableColumn
ipCidrRouteStaticRowStatus = _IpCidrRouteStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 1, 22, 1, 13),
    _IpCidrRouteStaticRowStatus_Type()
)
ipCidrRouteStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipCidrRouteStaticRowStatus.setStatus("mandatory")
_IpxRoute_ObjectIdentity = ObjectIdentity
ipxRoute = _IpxRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 2)
)
_IpxCircTable_Object = MibTable
ipxCircTable = _IpxCircTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1)
)
if mibBuilder.loadTexts:
    ipxCircTable.setStatus("mandatory")
_IpxCircEntry_Object = MibTableRow
ipxCircEntry = _IpxCircEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1)
)
ipxCircEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxCircIndex"),
)
if mibBuilder.loadTexts:
    ipxCircEntry.setStatus("mandatory")
_IpxCircIndex_Type = Integer32
_IpxCircIndex_Object = MibTableColumn
ipxCircIndex = _IpxCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 1),
    _IpxCircIndex_Type()
)
ipxCircIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircIndex.setStatus("mandatory")
_IpxCircNetNumber_Type = NetNum
_IpxCircNetNumber_Object = MibTableColumn
ipxCircNetNumber = _IpxCircNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 2),
    _IpxCircNetNumber_Type()
)
ipxCircNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetNumber.setStatus("mandatory")


class _IpxCircLowerIfAlias_Type(DisplayString):
    """Custom type ipxCircLowerIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IpxCircLowerIfAlias_Type.__name__ = "DisplayString"
_IpxCircLowerIfAlias_Object = MibTableColumn
ipxCircLowerIfAlias = _IpxCircLowerIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 3),
    _IpxCircLowerIfAlias_Type()
)
ipxCircLowerIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircLowerIfAlias.setStatus("mandatory")


class _IpxCircEncapsulation_Type(Integer32):
    """Custom type ipxCircEncapsulation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("novell", 2),
          ("ethernet", 3),
          ("llc", 4),
          ("snap", 5))
    )


_IpxCircEncapsulation_Type.__name__ = "Integer32"
_IpxCircEncapsulation_Object = MibTableColumn
ipxCircEncapsulation = _IpxCircEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 4),
    _IpxCircEncapsulation_Type()
)
ipxCircEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircEncapsulation.setStatus("mandatory")


class _IpxCircNetbios_Type(Integer32):
    """Custom type ipxCircNetbios based on Integer32"""
    defaultValue = 1

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


_IpxCircNetbios_Type.__name__ = "Integer32"
_IpxCircNetbios_Object = MibTableColumn
ipxCircNetbios = _IpxCircNetbios_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 5),
    _IpxCircNetbios_Type()
)
ipxCircNetbios.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircNetbios.setStatus("mandatory")
_IpxCircStatus_Type = RowStatus
_IpxCircStatus_Object = MibTableColumn
ipxCircStatus = _IpxCircStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 6),
    _IpxCircStatus_Type()
)
ipxCircStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircStatus.setStatus("mandatory")


class _IpxCircRipUpdate_Type(Integer32):
    """Custom type ipxCircRipUpdate based on Integer32"""
    defaultValue = 60


_IpxCircRipUpdate_Type.__name__ = "Integer32"
_IpxCircRipUpdate_Object = MibTableColumn
ipxCircRipUpdate = _IpxCircRipUpdate_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 7),
    _IpxCircRipUpdate_Type()
)
ipxCircRipUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircRipUpdate.setStatus("mandatory")


class _IpxCircRipAgeMultiplier_Type(Integer32):
    """Custom type ipxCircRipAgeMultiplier based on Integer32"""
    defaultValue = 4


_IpxCircRipAgeMultiplier_Type.__name__ = "Integer32"
_IpxCircRipAgeMultiplier_Object = MibTableColumn
ipxCircRipAgeMultiplier = _IpxCircRipAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 8),
    _IpxCircRipAgeMultiplier_Type()
)
ipxCircRipAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircRipAgeMultiplier.setStatus("mandatory")


class _IpxCircRipStatus_Type(Integer32):
    """Custom type ipxCircRipStatus based on Integer32"""
    defaultValue = 1

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


_IpxCircRipStatus_Type.__name__ = "Integer32"
_IpxCircRipStatus_Object = MibTableColumn
ipxCircRipStatus = _IpxCircRipStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 9),
    _IpxCircRipStatus_Type()
)
ipxCircRipStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircRipStatus.setStatus("mandatory")


class _IpxCircSapUpdate_Type(Integer32):
    """Custom type ipxCircSapUpdate based on Integer32"""
    defaultValue = 60


_IpxCircSapUpdate_Type.__name__ = "Integer32"
_IpxCircSapUpdate_Object = MibTableColumn
ipxCircSapUpdate = _IpxCircSapUpdate_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 10),
    _IpxCircSapUpdate_Type()
)
ipxCircSapUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSapUpdate.setStatus("mandatory")


class _IpxCircSapAgeMultiplier_Type(Integer32):
    """Custom type ipxCircSapAgeMultiplier based on Integer32"""
    defaultValue = 4


_IpxCircSapAgeMultiplier_Type.__name__ = "Integer32"
_IpxCircSapAgeMultiplier_Object = MibTableColumn
ipxCircSapAgeMultiplier = _IpxCircSapAgeMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 11),
    _IpxCircSapAgeMultiplier_Type()
)
ipxCircSapAgeMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSapAgeMultiplier.setStatus("mandatory")


class _IpxCircGetNearestServerReply_Type(Integer32):
    """Custom type ipxCircGetNearestServerReply based on Integer32"""
    defaultValue = 1

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


_IpxCircGetNearestServerReply_Type.__name__ = "Integer32"
_IpxCircGetNearestServerReply_Object = MibTableColumn
ipxCircGetNearestServerReply = _IpxCircGetNearestServerReply_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 12),
    _IpxCircGetNearestServerReply_Type()
)
ipxCircGetNearestServerReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircGetNearestServerReply.setStatus("mandatory")


class _IpxCircSapStatus_Type(Integer32):
    """Custom type ipxCircSapStatus based on Integer32"""
    defaultValue = 1

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


_IpxCircSapStatus_Type.__name__ = "Integer32"
_IpxCircSapStatus_Object = MibTableColumn
ipxCircSapStatus = _IpxCircSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 13),
    _IpxCircSapStatus_Type()
)
ipxCircSapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxCircSapStatus.setStatus("mandatory")


class _IpxCircRipState_Type(Integer32):
    """Custom type ipxCircRipState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpxCircRipState_Type.__name__ = "Integer32"
_IpxCircRipState_Object = MibTableColumn
ipxCircRipState = _IpxCircRipState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 14),
    _IpxCircRipState_Type()
)
ipxCircRipState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircRipState.setStatus("mandatory")


class _IpxCircSapState_Type(Integer32):
    """Custom type ipxCircSapState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_IpxCircSapState_Type.__name__ = "Integer32"
_IpxCircSapState_Object = MibTableColumn
ipxCircSapState = _IpxCircSapState_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 1, 1, 15),
    _IpxCircSapState_Type()
)
ipxCircSapState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxCircSapState.setStatus("mandatory")
_IpxDestTable_Object = MibTable
ipxDestTable = _IpxDestTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2)
)
if mibBuilder.loadTexts:
    ipxDestTable.setStatus("mandatory")
_IpxDestEntry_Object = MibTableRow
ipxDestEntry = _IpxDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1)
)
ipxDestEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxDestNetNum"),
)
if mibBuilder.loadTexts:
    ipxDestEntry.setStatus("mandatory")
_IpxDestNetNum_Type = NetNum
_IpxDestNetNum_Object = MibTableColumn
ipxDestNetNum = _IpxDestNetNum_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 1),
    _IpxDestNetNum_Type()
)
ipxDestNetNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestNetNum.setStatus("mandatory")


class _IpxDestProtocol_Type(Integer32):
    """Custom type ipxDestProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("rip", 3),
          ("nlsp", 4),
          ("static", 5))
    )


_IpxDestProtocol_Type.__name__ = "Integer32"
_IpxDestProtocol_Object = MibTableColumn
ipxDestProtocol = _IpxDestProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 2),
    _IpxDestProtocol_Type()
)
ipxDestProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestProtocol.setStatus("mandatory")
_IpxDestTicks_Type = Integer32
_IpxDestTicks_Object = MibTableColumn
ipxDestTicks = _IpxDestTicks_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 3),
    _IpxDestTicks_Type()
)
ipxDestTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestTicks.setStatus("mandatory")
_IpxDestHopCount_Type = Integer32
_IpxDestHopCount_Object = MibTableColumn
ipxDestHopCount = _IpxDestHopCount_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 4),
    _IpxDestHopCount_Type()
)
ipxDestHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestHopCount.setStatus("mandatory")
_IpxDestNextHopCircIndex_Type = Integer32
_IpxDestNextHopCircIndex_Object = MibTableColumn
ipxDestNextHopCircIndex = _IpxDestNextHopCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 5),
    _IpxDestNextHopCircIndex_Type()
)
ipxDestNextHopCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopCircIndex.setStatus("mandatory")
_IpxDestNextHopNICAddress_Type = PhysAddress
_IpxDestNextHopNICAddress_Object = MibTableColumn
ipxDestNextHopNICAddress = _IpxDestNextHopNICAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 6),
    _IpxDestNextHopNICAddress_Type()
)
ipxDestNextHopNICAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNICAddress.setStatus("mandatory")
_IpxDestNextHopNetNum_Type = NetNum
_IpxDestNextHopNetNum_Object = MibTableColumn
ipxDestNextHopNetNum = _IpxDestNextHopNetNum_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 7),
    _IpxDestNextHopNetNum_Type()
)
ipxDestNextHopNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestNextHopNetNum.setStatus("mandatory")
_IpxDestStatus_Type = RowStatus
_IpxDestStatus_Object = MibTableColumn
ipxDestStatus = _IpxDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 8),
    _IpxDestStatus_Type()
)
ipxDestStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxDestStatus.setStatus("mandatory")
_IpxDestAge_Type = Integer32
_IpxDestAge_Object = MibTableColumn
ipxDestAge = _IpxDestAge_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 2, 1, 9),
    _IpxDestAge_Type()
)
ipxDestAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxDestAge.setStatus("mandatory")
_IpxServTable_Object = MibTable
ipxServTable = _IpxServTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3)
)
if mibBuilder.loadTexts:
    ipxServTable.setStatus("mandatory")
_IpxServEntry_Object = MibTableRow
ipxServEntry = _IpxServEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1)
)
ipxServEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxServType"),
    (0, "CROUTE-MIB", "ipxServName"),
)
if mibBuilder.loadTexts:
    ipxServEntry.setStatus("mandatory")
_IpxServType_Type = Integer32
_IpxServType_Object = MibTableColumn
ipxServType = _IpxServType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 1),
    _IpxServType_Type()
)
ipxServType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServType.setStatus("mandatory")


class _IpxServName_Type(DisplayString):
    """Custom type ipxServName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxServName_Type.__name__ = "DisplayString"
_IpxServName_Object = MibTableColumn
ipxServName = _IpxServName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 2),
    _IpxServName_Type()
)
ipxServName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServName.setStatus("mandatory")


class _IpxServProtocol_Type(Integer32):
    """Custom type ipxServProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("local", 2),
          ("nlsp", 4),
          ("static", 5),
          ("sap", 6))
    )


_IpxServProtocol_Type.__name__ = "Integer32"
_IpxServProtocol_Object = MibTableColumn
ipxServProtocol = _IpxServProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 3),
    _IpxServProtocol_Type()
)
ipxServProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServProtocol.setStatus("mandatory")
_IpxServNetNum_Type = NetNum
_IpxServNetNum_Object = MibTableColumn
ipxServNetNum = _IpxServNetNum_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 4),
    _IpxServNetNum_Type()
)
ipxServNetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNetNum.setStatus("mandatory")


class _IpxServNode_Type(OctetString):
    """Custom type ipxServNode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_IpxServNode_Type.__name__ = "OctetString"
_IpxServNode_Object = MibTableColumn
ipxServNode = _IpxServNode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 5),
    _IpxServNode_Type()
)
ipxServNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServNode.setStatus("mandatory")
_IpxServSocket_Type = Integer32
_IpxServSocket_Object = MibTableColumn
ipxServSocket = _IpxServSocket_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 6),
    _IpxServSocket_Type()
)
ipxServSocket.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServSocket.setStatus("mandatory")
_IpxServHopCount_Type = Integer32
_IpxServHopCount_Object = MibTableColumn
ipxServHopCount = _IpxServHopCount_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 7),
    _IpxServHopCount_Type()
)
ipxServHopCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServHopCount.setStatus("mandatory")
_IpxServStatus_Type = RowStatus
_IpxServStatus_Object = MibTableColumn
ipxServStatus = _IpxServStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 8),
    _IpxServStatus_Type()
)
ipxServStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxServStatus.setStatus("mandatory")
_IpxServAge_Type = Integer32
_IpxServAge_Object = MibTableColumn
ipxServAge = _IpxServAge_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 3, 1, 9),
    _IpxServAge_Type()
)
ipxServAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxServAge.setStatus("mandatory")
_IpxAccessGlobals_ObjectIdentity = ObjectIdentity
ipxAccessGlobals = _IpxAccessGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 4)
)


class _IpxAccessControlEnable_Type(Integer32):
    """Custom type ipxAccessControlEnable based on Integer32"""
    defaultValue = 2

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


_IpxAccessControlEnable_Type.__name__ = "Integer32"
_IpxAccessControlEnable_Object = MibScalar
ipxAccessControlEnable = _IpxAccessControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 4, 1),
    _IpxAccessControlEnable_Type()
)
ipxAccessControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlEnable.setStatus("mandatory")
_IpxAccessControlTable_Object = MibTable
ipxAccessControlTable = _IpxAccessControlTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5)
)
if mibBuilder.loadTexts:
    ipxAccessControlTable.setStatus("mandatory")
_IpxAccessControlEntry_Object = MibTableRow
ipxAccessControlEntry = _IpxAccessControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1)
)
ipxAccessControlEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxAccessControlIndex"),
)
if mibBuilder.loadTexts:
    ipxAccessControlEntry.setStatus("mandatory")
_IpxAccessControlIndex_Type = Integer32
_IpxAccessControlIndex_Object = MibTableColumn
ipxAccessControlIndex = _IpxAccessControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 1),
    _IpxAccessControlIndex_Type()
)
ipxAccessControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxAccessControlIndex.setStatus("mandatory")
_IpxAccessControlSrcAddr_Type = NetNum
_IpxAccessControlSrcAddr_Object = MibTableColumn
ipxAccessControlSrcAddr = _IpxAccessControlSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 2),
    _IpxAccessControlSrcAddr_Type()
)
ipxAccessControlSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlSrcAddr.setStatus("mandatory")
_IpxAccessControlDstAddr_Type = NetNum
_IpxAccessControlDstAddr_Object = MibTableColumn
ipxAccessControlDstAddr = _IpxAccessControlDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 3),
    _IpxAccessControlDstAddr_Type()
)
ipxAccessControlDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlDstAddr.setStatus("mandatory")


class _IpxAccessControlOperation_Type(Integer32):
    """Custom type ipxAccessControlOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forward", 1),
          ("block", 2),
          ("blockAndReport", 3))
    )


_IpxAccessControlOperation_Type.__name__ = "Integer32"
_IpxAccessControlOperation_Object = MibTableColumn
ipxAccessControlOperation = _IpxAccessControlOperation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 4),
    _IpxAccessControlOperation_Type()
)
ipxAccessControlOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlOperation.setStatus("mandatory")


class _IpxAccessControlActivation_Type(Integer32):
    """Custom type ipxAccessControlActivation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wire-speed", 1),
          ("regular", 2))
    )


_IpxAccessControlActivation_Type.__name__ = "Integer32"
_IpxAccessControlActivation_Object = MibTableColumn
ipxAccessControlActivation = _IpxAccessControlActivation_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 5),
    _IpxAccessControlActivation_Type()
)
ipxAccessControlActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlActivation.setStatus("mandatory")
_IpxAccessControlStatus_Type = RowStatus
_IpxAccessControlStatus_Object = MibTableColumn
ipxAccessControlStatus = _IpxAccessControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 5, 1, 6),
    _IpxAccessControlStatus_Type()
)
ipxAccessControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxAccessControlStatus.setStatus("mandatory")
_IpxSapFilterGlobals_ObjectIdentity = ObjectIdentity
ipxSapFilterGlobals = _IpxSapFilterGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 6)
)


class _IpxSapFilterEnable_Type(Integer32):
    """Custom type ipxSapFilterEnable based on Integer32"""
    defaultValue = 2

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


_IpxSapFilterEnable_Type.__name__ = "Integer32"
_IpxSapFilterEnable_Object = MibScalar
ipxSapFilterEnable = _IpxSapFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 6, 1),
    _IpxSapFilterEnable_Type()
)
ipxSapFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterEnable.setStatus("mandatory")
_IpxSapFilterTable_Object = MibTable
ipxSapFilterTable = _IpxSapFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7)
)
if mibBuilder.loadTexts:
    ipxSapFilterTable.setStatus("mandatory")
_IpxSapFilterEntry_Object = MibTableRow
ipxSapFilterEntry = _IpxSapFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1)
)
ipxSapFilterEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipxSapFilterID"),
)
if mibBuilder.loadTexts:
    ipxSapFilterEntry.setStatus("mandatory")
_IpxSapFilterID_Type = Integer32
_IpxSapFilterID_Object = MibTableColumn
ipxSapFilterID = _IpxSapFilterID_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 1),
    _IpxSapFilterID_Type()
)
ipxSapFilterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipxSapFilterID.setStatus("mandatory")
_IpxSapFilterCircIndex_Type = Integer32
_IpxSapFilterCircIndex_Object = MibTableColumn
ipxSapFilterCircIndex = _IpxSapFilterCircIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 2),
    _IpxSapFilterCircIndex_Type()
)
ipxSapFilterCircIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterCircIndex.setStatus("mandatory")
_IpxSapFilterServiceNetNumber_Type = NetNum
_IpxSapFilterServiceNetNumber_Object = MibTableColumn
ipxSapFilterServiceNetNumber = _IpxSapFilterServiceNetNumber_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 3),
    _IpxSapFilterServiceNetNumber_Type()
)
ipxSapFilterServiceNetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterServiceNetNumber.setStatus("mandatory")
_IpxSapFilterServiceType_Type = Integer32
_IpxSapFilterServiceType_Object = MibTableColumn
ipxSapFilterServiceType = _IpxSapFilterServiceType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 4),
    _IpxSapFilterServiceType_Type()
)
ipxSapFilterServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterServiceType.setStatus("mandatory")


class _IpxSapFilterServerName_Type(DisplayString):
    """Custom type ipxSapFilterServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 48),
    )


_IpxSapFilterServerName_Type.__name__ = "DisplayString"
_IpxSapFilterServerName_Object = MibTableColumn
ipxSapFilterServerName = _IpxSapFilterServerName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 5),
    _IpxSapFilterServerName_Type()
)
ipxSapFilterServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterServerName.setStatus("mandatory")


class _IpxSapFilterDirection_Type(Integer32):
    """Custom type ipxSapFilterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_IpxSapFilterDirection_Type.__name__ = "Integer32"
_IpxSapFilterDirection_Object = MibTableColumn
ipxSapFilterDirection = _IpxSapFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 6),
    _IpxSapFilterDirection_Type()
)
ipxSapFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterDirection.setStatus("mandatory")


class _IpxSapFilterAction_Type(Integer32):
    """Custom type ipxSapFilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IpxSapFilterAction_Type.__name__ = "Integer32"
_IpxSapFilterAction_Object = MibTableColumn
ipxSapFilterAction = _IpxSapFilterAction_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 7),
    _IpxSapFilterAction_Type()
)
ipxSapFilterAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterAction.setStatus("mandatory")
_IpxSapFilterStatus_Type = RowStatus
_IpxSapFilterStatus_Object = MibTableColumn
ipxSapFilterStatus = _IpxSapFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 2, 7, 1, 8),
    _IpxSapFilterStatus_Type()
)
ipxSapFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipxSapFilterStatus.setStatus("mandatory")
_Layer2_ObjectIdentity = ObjectIdentity
layer2 = _Layer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 3)
)
_VlConfTable_Object = MibTable
vlConfTable = _VlConfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1)
)
if mibBuilder.loadTexts:
    vlConfTable.setStatus("mandatory")
_VlConfEntry_Object = MibTableRow
vlConfEntry = _VlConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1)
)
vlConfEntry.setIndexNames(
    (0, "CROUTE-MIB", "vlConfIndex"),
)
if mibBuilder.loadTexts:
    vlConfEntry.setStatus("mandatory")
_VlConfIndex_Type = Integer32
_VlConfIndex_Object = MibTableColumn
vlConfIndex = _VlConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1, 1),
    _VlConfIndex_Type()
)
vlConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlConfIndex.setStatus("mandatory")


class _VlConfAlias_Type(DisplayString):
    """Custom type vlConfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_VlConfAlias_Type.__name__ = "DisplayString"
_VlConfAlias_Object = MibTableColumn
vlConfAlias = _VlConfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1, 2),
    _VlConfAlias_Type()
)
vlConfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlConfAlias.setStatus("mandatory")
_VlConfStatus_Type = RowStatus
_VlConfStatus_Object = MibTableColumn
vlConfStatus = _VlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 1, 1, 3),
    _VlConfStatus_Type()
)
vlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlConfStatus.setStatus("mandatory")
_VlBridgeTable_Object = MibTable
vlBridgeTable = _VlBridgeTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2)
)
if mibBuilder.loadTexts:
    vlBridgeTable.setStatus("mandatory")
_VlBridgeEntry_Object = MibTableRow
vlBridgeEntry = _VlBridgeEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1)
)
vlBridgeEntry.setIndexNames(
    (0, "CROUTE-MIB", "vlBridgeProtocol"),
    (0, "CROUTE-MIB", "vlBridgeGroupIndex"),
    (0, "CROUTE-MIB", "vlBridgeIndex"),
)
if mibBuilder.loadTexts:
    vlBridgeEntry.setStatus("mandatory")


class _VlBridgeProtocol_Type(Integer32):
    """Custom type vlBridgeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dec", 2),
          ("netBios", 3),
          ("appleTalk", 4),
          ("sna", 5),
          ("ipx", 6))
    )


_VlBridgeProtocol_Type.__name__ = "Integer32"
_VlBridgeProtocol_Object = MibTableColumn
vlBridgeProtocol = _VlBridgeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 1),
    _VlBridgeProtocol_Type()
)
vlBridgeProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBridgeProtocol.setStatus("mandatory")
_VlBridgeGroupIndex_Type = Integer32
_VlBridgeGroupIndex_Object = MibTableColumn
vlBridgeGroupIndex = _VlBridgeGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 2),
    _VlBridgeGroupIndex_Type()
)
vlBridgeGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBridgeGroupIndex.setStatus("mandatory")
_VlBridgeIndex_Type = Integer32
_VlBridgeIndex_Object = MibTableColumn
vlBridgeIndex = _VlBridgeIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 3),
    _VlBridgeIndex_Type()
)
vlBridgeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlBridgeIndex.setStatus("mandatory")
_VlBridgeStatus_Type = RowStatus
_VlBridgeStatus_Object = MibTableColumn
vlBridgeStatus = _VlBridgeStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 2, 1, 4),
    _VlBridgeStatus_Type()
)
vlBridgeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlBridgeStatus.setStatus("mandatory")
_Layer2Globals_ObjectIdentity = ObjectIdentity
layer2Globals = _Layer2Globals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 3)
)


class _Layer2GlobalsBridgeEnable_Type(Integer32):
    """Custom type layer2GlobalsBridgeEnable based on Integer32"""
    defaultValue = 2

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
        *(("enable", 1),
          ("disable", 2),
          ("backup", 3),
          ("activeBackup", 4))
    )


_Layer2GlobalsBridgeEnable_Type.__name__ = "Integer32"
_Layer2GlobalsBridgeEnable_Object = MibScalar
layer2GlobalsBridgeEnable = _Layer2GlobalsBridgeEnable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 3, 3, 1),
    _Layer2GlobalsBridgeEnable_Type()
)
layer2GlobalsBridgeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    layer2GlobalsBridgeEnable.setStatus("mandatory")
_RouteGroupMgmt_ObjectIdentity = ObjectIdentity
routeGroupMgmt = _RouteGroupMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 4)
)
_RouteGroupTable_Object = MibTable
routeGroupTable = _RouteGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1)
)
if mibBuilder.loadTexts:
    routeGroupTable.setStatus("mandatory")
_RouteGroupEntry_Object = MibTableRow
routeGroupEntry = _RouteGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1, 1)
)
routeGroupEntry.setIndexNames(
    (0, "CROUTE-MIB", "routeGroupId"),
)
if mibBuilder.loadTexts:
    routeGroupEntry.setStatus("mandatory")
_RouteGroupId_Type = Integer32
_RouteGroupId_Object = MibTableColumn
routeGroupId = _RouteGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1, 1, 1),
    _RouteGroupId_Type()
)
routeGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routeGroupId.setStatus("mandatory")


class _RouteGroupRouteMode_Type(Integer32):
    """Custom type routeGroupRouteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              5,
              21,
              255)
        )
    )
    namedValues = NamedValues(
        *(("secondLayer", 1),
          ("ez2route", 3),
          ("router", 5),
          ("routerAndWebSwitch", 21),
          ("notSupported", 255))
    )


_RouteGroupRouteMode_Type.__name__ = "Integer32"
_RouteGroupRouteMode_Object = MibTableColumn
routeGroupRouteMode = _RouteGroupRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 4, 1, 1, 2),
    _RouteGroupRouteMode_Type()
)
routeGroupRouteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    routeGroupRouteMode.setStatus("mandatory")
_DrLayer2_ObjectIdentity = ObjectIdentity
drLayer2 = _DrLayer2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 5)
)
_DrVlConfTable_Object = MibTable
drVlConfTable = _DrVlConfTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1)
)
if mibBuilder.loadTexts:
    drVlConfTable.setStatus("mandatory")
_DrVlConfEntry_Object = MibTableRow
drVlConfEntry = _DrVlConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1)
)
drVlConfEntry.setIndexNames(
    (0, "CROUTE-MIB", "drVlConfSlot"),
    (0, "CROUTE-MIB", "drVlConfIndex"),
)
if mibBuilder.loadTexts:
    drVlConfEntry.setStatus("mandatory")
_DrVlConfSlot_Type = Integer32
_DrVlConfSlot_Object = MibTableColumn
drVlConfSlot = _DrVlConfSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 1),
    _DrVlConfSlot_Type()
)
drVlConfSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drVlConfSlot.setStatus("mandatory")
_DrVlConfIndex_Type = Integer32
_DrVlConfIndex_Object = MibTableColumn
drVlConfIndex = _DrVlConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 2),
    _DrVlConfIndex_Type()
)
drVlConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drVlConfIndex.setStatus("mandatory")


class _DrVlConfAlias_Type(DisplayString):
    """Custom type drVlConfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DrVlConfAlias_Type.__name__ = "DisplayString"
_DrVlConfAlias_Object = MibTableColumn
drVlConfAlias = _DrVlConfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 3),
    _DrVlConfAlias_Type()
)
drVlConfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drVlConfAlias.setStatus("mandatory")
_DrVlConfStatus_Type = RowStatus
_DrVlConfStatus_Object = MibTableColumn
drVlConfStatus = _DrVlConfStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 5, 1, 1, 4),
    _DrVlConfStatus_Type()
)
drVlConfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drVlConfStatus.setStatus("mandatory")
_DrIpRoute_ObjectIdentity = ObjectIdentity
drIpRoute = _DrIpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 6)
)
_DrIpInterfaceTable_Object = MibTable
drIpInterfaceTable = _DrIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1)
)
if mibBuilder.loadTexts:
    drIpInterfaceTable.setStatus("mandatory")
_DrIpInterfaceEntry_Object = MibTableRow
drIpInterfaceEntry = _DrIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1)
)
drIpInterfaceEntry.setIndexNames(
    (0, "CROUTE-MIB", "drIpInterfaceSlot"),
    (0, "CROUTE-MIB", "drIpInterfaceAddr"),
)
if mibBuilder.loadTexts:
    drIpInterfaceEntry.setStatus("mandatory")
_DrIpInterfaceSlot_Type = Integer32
_DrIpInterfaceSlot_Object = MibTableColumn
drIpInterfaceSlot = _DrIpInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 1),
    _DrIpInterfaceSlot_Type()
)
drIpInterfaceSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drIpInterfaceSlot.setStatus("mandatory")
_DrIpInterfaceAddr_Type = IpAddress
_DrIpInterfaceAddr_Object = MibTableColumn
drIpInterfaceAddr = _DrIpInterfaceAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 2),
    _DrIpInterfaceAddr_Type()
)
drIpInterfaceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drIpInterfaceAddr.setStatus("mandatory")
_DrIpInterfaceNetMask_Type = IpAddress
_DrIpInterfaceNetMask_Object = MibTableColumn
drIpInterfaceNetMask = _DrIpInterfaceNetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 3),
    _DrIpInterfaceNetMask_Type()
)
drIpInterfaceNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceNetMask.setStatus("mandatory")


class _DrIpInterfaceLowerIfAlias_Type(DisplayString):
    """Custom type drIpInterfaceLowerIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DrIpInterfaceLowerIfAlias_Type.__name__ = "DisplayString"
_DrIpInterfaceLowerIfAlias_Object = MibTableColumn
drIpInterfaceLowerIfAlias = _DrIpInterfaceLowerIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 4),
    _DrIpInterfaceLowerIfAlias_Type()
)
drIpInterfaceLowerIfAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceLowerIfAlias.setStatus("mandatory")


class _DrIpInterfaceType_Type(Integer32):
    """Custom type drIpInterfaceType based on Integer32"""
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
        *(("broadcast", 1),
          ("nBMA", 2),
          ("ptp", 3))
    )


_DrIpInterfaceType_Type.__name__ = "Integer32"
_DrIpInterfaceType_Object = MibTableColumn
drIpInterfaceType = _DrIpInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 5),
    _DrIpInterfaceType_Type()
)
drIpInterfaceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceType.setStatus("mandatory")


class _DrIpInterfaceForwardIpBroadcast_Type(Integer32):
    """Custom type drIpInterfaceForwardIpBroadcast based on Integer32"""
    defaultValue = 1

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


_DrIpInterfaceForwardIpBroadcast_Type.__name__ = "Integer32"
_DrIpInterfaceForwardIpBroadcast_Object = MibTableColumn
drIpInterfaceForwardIpBroadcast = _DrIpInterfaceForwardIpBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 6),
    _DrIpInterfaceForwardIpBroadcast_Type()
)
drIpInterfaceForwardIpBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceForwardIpBroadcast.setStatus("mandatory")


class _DrIpInterfaceBroadcastAddr_Type(Integer32):
    """Custom type drIpInterfaceBroadcastAddr based on Integer32"""
    defaultValue = 1


_DrIpInterfaceBroadcastAddr_Type.__name__ = "Integer32"
_DrIpInterfaceBroadcastAddr_Object = MibTableColumn
drIpInterfaceBroadcastAddr = _DrIpInterfaceBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 7),
    _DrIpInterfaceBroadcastAddr_Type()
)
drIpInterfaceBroadcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceBroadcastAddr.setStatus("mandatory")


class _DrIpInterfaceProxyArp_Type(Integer32):
    """Custom type drIpInterfaceProxyArp based on Integer32"""
    defaultValue = 2

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


_DrIpInterfaceProxyArp_Type.__name__ = "Integer32"
_DrIpInterfaceProxyArp_Object = MibTableColumn
drIpInterfaceProxyArp = _DrIpInterfaceProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 8),
    _DrIpInterfaceProxyArp_Type()
)
drIpInterfaceProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceProxyArp.setStatus("mandatory")
_DrIpInterfaceStatus_Type = RowStatus
_DrIpInterfaceStatus_Object = MibTableColumn
drIpInterfaceStatus = _DrIpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 9),
    _DrIpInterfaceStatus_Type()
)
drIpInterfaceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceStatus.setStatus("mandatory")
_DrIpInterfaceMainRouterAddr_Type = IpAddress
_DrIpInterfaceMainRouterAddr_Object = MibTableColumn
drIpInterfaceMainRouterAddr = _DrIpInterfaceMainRouterAddr_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 10),
    _DrIpInterfaceMainRouterAddr_Type()
)
drIpInterfaceMainRouterAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceMainRouterAddr.setStatus("mandatory")


class _DrIpInterfaceARPServerStatus_Type(Integer32):
    """Custom type drIpInterfaceARPServerStatus based on Integer32"""
    defaultValue = 2

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


_DrIpInterfaceARPServerStatus_Type.__name__ = "Integer32"
_DrIpInterfaceARPServerStatus_Object = MibTableColumn
drIpInterfaceARPServerStatus = _DrIpInterfaceARPServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 11),
    _DrIpInterfaceARPServerStatus_Type()
)
drIpInterfaceARPServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceARPServerStatus.setStatus("mandatory")


class _DrIpInterfaceName_Type(DisplayString):
    """Custom type drIpInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DrIpInterfaceName_Type.__name__ = "DisplayString"
_DrIpInterfaceName_Object = MibTableColumn
drIpInterfaceName = _DrIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 12),
    _DrIpInterfaceName_Type()
)
drIpInterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceName.setStatus("mandatory")


class _DrIpInterfaceNetbiosRebroadcast_Type(Integer32):
    """Custom type drIpInterfaceNetbiosRebroadcast based on Integer32"""
    defaultValue = 4

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
        *(("inbound", 1),
          ("outbound", 2),
          ("both", 3),
          ("disable", 4))
    )


_DrIpInterfaceNetbiosRebroadcast_Type.__name__ = "Integer32"
_DrIpInterfaceNetbiosRebroadcast_Object = MibTableColumn
drIpInterfaceNetbiosRebroadcast = _DrIpInterfaceNetbiosRebroadcast_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 13),
    _DrIpInterfaceNetbiosRebroadcast_Type()
)
drIpInterfaceNetbiosRebroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceNetbiosRebroadcast.setStatus("mandatory")


class _DrIpInterfaceIcmpRedirects_Type(Integer32):
    """Custom type drIpInterfaceIcmpRedirects based on Integer32"""
    defaultValue = 1

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


_DrIpInterfaceIcmpRedirects_Type.__name__ = "Integer32"
_DrIpInterfaceIcmpRedirects_Object = MibTableColumn
drIpInterfaceIcmpRedirects = _DrIpInterfaceIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 14),
    _DrIpInterfaceIcmpRedirects_Type()
)
drIpInterfaceIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceIcmpRedirects.setStatus("mandatory")


class _DrIpInterfaceOperStatus_Type(Integer32):
    """Custom type drIpInterfaceOperStatus based on Integer32"""
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


_DrIpInterfaceOperStatus_Type.__name__ = "Integer32"
_DrIpInterfaceOperStatus_Object = MibTableColumn
drIpInterfaceOperStatus = _DrIpInterfaceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 15),
    _DrIpInterfaceOperStatus_Type()
)
drIpInterfaceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drIpInterfaceOperStatus.setStatus("mandatory")


class _DrIpInterfaceDhcpRelay_Type(Integer32):
    """Custom type drIpInterfaceDhcpRelay based on Integer32"""
    defaultValue = 2

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


_DrIpInterfaceDhcpRelay_Type.__name__ = "Integer32"
_DrIpInterfaceDhcpRelay_Object = MibTableColumn
drIpInterfaceDhcpRelay = _DrIpInterfaceDhcpRelay_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 6, 1, 1, 16),
    _DrIpInterfaceDhcpRelay_Type()
)
drIpInterfaceDhcpRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drIpInterfaceDhcpRelay.setStatus("mandatory")
_DrStaticCidr_ObjectIdentity = ObjectIdentity
drStaticCidr = _DrStaticCidr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 7)
)
_DrStaticCidrTable_Object = MibTable
drStaticCidrTable = _DrStaticCidrTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1)
)
if mibBuilder.loadTexts:
    drStaticCidrTable.setStatus("mandatory")
_DrStaticCidrEntry_Object = MibTableRow
drStaticCidrEntry = _DrStaticCidrEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1)
)
drStaticCidrEntry.setIndexNames(
    (0, "CROUTE-MIB", "drStaticCidrEntID"),
    (0, "CROUTE-MIB", "drStaticCidrDest"),
    (0, "CROUTE-MIB", "drStaticCidrMask"),
    (0, "CROUTE-MIB", "drStaticCidrTos"),
    (0, "CROUTE-MIB", "drStaticCidrNextHop"),
)
if mibBuilder.loadTexts:
    drStaticCidrEntry.setStatus("mandatory")


class _DrStaticCidrEntID_Type(Integer32):
    """Custom type drStaticCidrEntID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DrStaticCidrEntID_Type.__name__ = "Integer32"
_DrStaticCidrEntID_Object = MibTableColumn
drStaticCidrEntID = _DrStaticCidrEntID_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 1),
    _DrStaticCidrEntID_Type()
)
drStaticCidrEntID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrEntID.setStatus("mandatory")
_DrStaticCidrDest_Type = IpAddress
_DrStaticCidrDest_Object = MibTableColumn
drStaticCidrDest = _DrStaticCidrDest_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 2),
    _DrStaticCidrDest_Type()
)
drStaticCidrDest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrDest.setStatus("mandatory")
_DrStaticCidrMask_Type = IpAddress
_DrStaticCidrMask_Object = MibTableColumn
drStaticCidrMask = _DrStaticCidrMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 3),
    _DrStaticCidrMask_Type()
)
drStaticCidrMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrMask.setStatus("mandatory")


class _DrStaticCidrTos_Type(Integer32):
    """Custom type drStaticCidrTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DrStaticCidrTos_Type.__name__ = "Integer32"
_DrStaticCidrTos_Object = MibTableColumn
drStaticCidrTos = _DrStaticCidrTos_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 4),
    _DrStaticCidrTos_Type()
)
drStaticCidrTos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrTos.setStatus("mandatory")
_DrStaticCidrNextHop_Type = IpAddress
_DrStaticCidrNextHop_Object = MibTableColumn
drStaticCidrNextHop = _DrStaticCidrNextHop_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 5),
    _DrStaticCidrNextHop_Type()
)
drStaticCidrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrNextHop.setStatus("mandatory")


class _DrStaticCidrIfIndex_Type(Integer32):
    """Custom type drStaticCidrIfIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DrStaticCidrIfIndex_Type.__name__ = "Integer32"
_DrStaticCidrIfIndex_Object = MibTableColumn
drStaticCidrIfIndex = _DrStaticCidrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 6),
    _DrStaticCidrIfIndex_Type()
)
drStaticCidrIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrIfIndex.setStatus("mandatory")


class _DrStaticCidrType_Type(Integer32):
    """Custom type drStaticCidrType based on Integer32"""
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
        *(("other", 1),
          ("reject", 2),
          ("local", 3),
          ("remote", 4))
    )


_DrStaticCidrType_Type.__name__ = "Integer32"
_DrStaticCidrType_Object = MibTableColumn
drStaticCidrType = _DrStaticCidrType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 7),
    _DrStaticCidrType_Type()
)
drStaticCidrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrType.setStatus("mandatory")


class _DrStaticCidrMetric1_Type(Integer32):
    """Custom type drStaticCidrMetric1 based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_DrStaticCidrMetric1_Type.__name__ = "Integer32"
_DrStaticCidrMetric1_Object = MibTableColumn
drStaticCidrMetric1 = _DrStaticCidrMetric1_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 8),
    _DrStaticCidrMetric1_Type()
)
drStaticCidrMetric1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrMetric1.setStatus("mandatory")


class _DrStaticCidrPrecedence_Type(Integer32):
    """Custom type drStaticCidrPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DrStaticCidrPrecedence_Type.__name__ = "Integer32"
_DrStaticCidrPrecedence_Object = MibTableColumn
drStaticCidrPrecedence = _DrStaticCidrPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 9),
    _DrStaticCidrPrecedence_Type()
)
drStaticCidrPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrPrecedence.setStatus("mandatory")


class _DrStaticCidrCRPType_Type(Integer32):
    """Custom type drStaticCidrCRPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("routingFWLB", 1),
          ("bridgingFWLB", 2),
          ("regularStatic", 3))
    )


_DrStaticCidrCRPType_Type.__name__ = "Integer32"
_DrStaticCidrCRPType_Object = MibTableColumn
drStaticCidrCRPType = _DrStaticCidrCRPType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 10),
    _DrStaticCidrCRPType_Type()
)
drStaticCidrCRPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrCRPType.setStatus("mandatory")


class _DrStaticCidrOperStatus_Type(Integer32):
    """Custom type drStaticCidrOperStatus based on Integer32"""
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


_DrStaticCidrOperStatus_Type.__name__ = "Integer32"
_DrStaticCidrOperStatus_Object = MibTableColumn
drStaticCidrOperStatus = _DrStaticCidrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 11),
    _DrStaticCidrOperStatus_Type()
)
drStaticCidrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    drStaticCidrOperStatus.setStatus("mandatory")


class _DrStaticCidrName_Type(DisplayString):
    """Custom type drStaticCidrName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DrStaticCidrName_Type.__name__ = "DisplayString"
_DrStaticCidrName_Object = MibTableColumn
drStaticCidrName = _DrStaticCidrName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 12),
    _DrStaticCidrName_Type()
)
drStaticCidrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrName.setStatus("mandatory")


class _DrStaticOwner_Type(OwnerString):
    """Custom type drStaticOwner based on OwnerString"""
    subtypeSpec = OwnerString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_DrStaticOwner_Type.__name__ = "OwnerString"
_DrStaticOwner_Object = MibTableColumn
drStaticOwner = _DrStaticOwner_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 13),
    _DrStaticOwner_Type()
)
drStaticOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticOwner.setStatus("mandatory")
_DrStaticCidrStatus_Type = RowStatus
_DrStaticCidrStatus_Object = MibTableColumn
drStaticCidrStatus = _DrStaticCidrStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 7, 1, 1, 14),
    _DrStaticCidrStatus_Type()
)
drStaticCidrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    drStaticCidrStatus.setStatus("mandatory")
_IpTunnel_ObjectIdentity = ObjectIdentity
ipTunnel = _IpTunnel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 8)
)
_IpTunnelTable_Object = MibTable
ipTunnelTable = _IpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1)
)
if mibBuilder.loadTexts:
    ipTunnelTable.setStatus("mandatory")
_IpTunnelEntry_Object = MibTableRow
ipTunnelEntry = _IpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1)
)
ipTunnelEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipTunnelIfIndex"),
)
if mibBuilder.loadTexts:
    ipTunnelEntry.setStatus("mandatory")
_IpTunnelIfIndex_Type = Integer32
_IpTunnelIfIndex_Object = MibTableColumn
ipTunnelIfIndex = _IpTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 1),
    _IpTunnelIfIndex_Type()
)
ipTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTunnelIfIndex.setStatus("mandatory")
_IpTunnelIfStatus_Type = RowStatus
_IpTunnelIfStatus_Object = MibTableColumn
ipTunnelIfStatus = _IpTunnelIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 2),
    _IpTunnelIfStatus_Type()
)
ipTunnelIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfStatus.setStatus("mandatory")


class _IpTunnelIfLocalAddress_Type(IpAddress):
    """Custom type ipTunnelIfLocalAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpTunnelIfLocalAddress_Type.__name__ = "IpAddress"
_IpTunnelIfLocalAddress_Object = MibTableColumn
ipTunnelIfLocalAddress = _IpTunnelIfLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 3),
    _IpTunnelIfLocalAddress_Type()
)
ipTunnelIfLocalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfLocalAddress.setStatus("mandatory")


class _IpTunnelIfRemoteAddress_Type(IpAddress):
    """Custom type ipTunnelIfRemoteAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpTunnelIfRemoteAddress_Type.__name__ = "IpAddress"
_IpTunnelIfRemoteAddress_Object = MibTableColumn
ipTunnelIfRemoteAddress = _IpTunnelIfRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 4),
    _IpTunnelIfRemoteAddress_Type()
)
ipTunnelIfRemoteAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfRemoteAddress.setStatus("mandatory")


class _IpTunnelIfEncapsMethod_Type(Integer32):
    """Custom type ipTunnelIfEncapsMethod based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("direct", 2),
          ("gre", 3),
          ("minimal", 4),
          ("l2tp", 5),
          ("pptp", 6),
          ("l2f", 7),
          ("udp", 8),
          ("atmp", 9))
    )


_IpTunnelIfEncapsMethod_Type.__name__ = "Integer32"
_IpTunnelIfEncapsMethod_Object = MibTableColumn
ipTunnelIfEncapsMethod = _IpTunnelIfEncapsMethod_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 5),
    _IpTunnelIfEncapsMethod_Type()
)
ipTunnelIfEncapsMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTunnelIfEncapsMethod.setStatus("mandatory")


class _IpTunnelIfConfigID_Type(Integer32):
    """Custom type ipTunnelIfConfigID based on Integer32"""
    defaultValue = 1


_IpTunnelIfConfigID_Type.__name__ = "Integer32"
_IpTunnelIfConfigID_Object = MibTableColumn
ipTunnelIfConfigID = _IpTunnelIfConfigID_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 6),
    _IpTunnelIfConfigID_Type()
)
ipTunnelIfConfigID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfConfigID.setStatus("mandatory")


class _IpTunnelIfHopLimit_Type(Integer32):
    """Custom type ipTunnelIfHopLimit based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_IpTunnelIfHopLimit_Type.__name__ = "Integer32"
_IpTunnelIfHopLimit_Object = MibTableColumn
ipTunnelIfHopLimit = _IpTunnelIfHopLimit_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 7),
    _IpTunnelIfHopLimit_Type()
)
ipTunnelIfHopLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfHopLimit.setStatus("mandatory")


class _IpTunnelIfSecurity_Type(Integer32):
    """Custom type ipTunnelIfSecurity based on Integer32"""
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
        *(("none", 1),
          ("ipsec", 2),
          ("other", 3))
    )


_IpTunnelIfSecurity_Type.__name__ = "Integer32"
_IpTunnelIfSecurity_Object = MibTableColumn
ipTunnelIfSecurity = _IpTunnelIfSecurity_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 8),
    _IpTunnelIfSecurity_Type()
)
ipTunnelIfSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfSecurity.setStatus("mandatory")


class _IpTunnelIfDSCP_Type(Integer32):
    """Custom type ipTunnelIfDSCP based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_IpTunnelIfDSCP_Type.__name__ = "Integer32"
_IpTunnelIfDSCP_Object = MibTableColumn
ipTunnelIfDSCP = _IpTunnelIfDSCP_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 9),
    _IpTunnelIfDSCP_Type()
)
ipTunnelIfDSCP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfDSCP.setStatus("mandatory")


class _IpTunnelIfChecksum_Type(Integer32):
    """Custom type ipTunnelIfChecksum based on Integer32"""
    defaultValue = 2

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


_IpTunnelIfChecksum_Type.__name__ = "Integer32"
_IpTunnelIfChecksum_Object = MibTableColumn
ipTunnelIfChecksum = _IpTunnelIfChecksum_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 10),
    _IpTunnelIfChecksum_Type()
)
ipTunnelIfChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfChecksum.setStatus("mandatory")
_IpTunnelIfKey_Type = Integer32
_IpTunnelIfKey_Object = MibTableColumn
ipTunnelIfKey = _IpTunnelIfKey_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 11),
    _IpTunnelIfKey_Type()
)
ipTunnelIfKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfKey.setStatus("mandatory")


class _IpTunnelIfKeyMode_Type(Integer32):
    """Custom type ipTunnelIfKeyMode based on Integer32"""
    defaultValue = 2

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


_IpTunnelIfKeyMode_Type.__name__ = "Integer32"
_IpTunnelIfKeyMode_Object = MibTableColumn
ipTunnelIfKeyMode = _IpTunnelIfKeyMode_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 12),
    _IpTunnelIfKeyMode_Type()
)
ipTunnelIfKeyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfKeyMode.setStatus("mandatory")


class _IpTunnelIfOutOfOrderDrop_Type(Integer32):
    """Custom type ipTunnelIfOutOfOrderDrop based on Integer32"""
    defaultValue = 2

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


_IpTunnelIfOutOfOrderDrop_Type.__name__ = "Integer32"
_IpTunnelIfOutOfOrderDrop_Object = MibTableColumn
ipTunnelIfOutOfOrderDrop = _IpTunnelIfOutOfOrderDrop_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 13),
    _IpTunnelIfOutOfOrderDrop_Type()
)
ipTunnelIfOutOfOrderDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfOutOfOrderDrop.setStatus("mandatory")


class _IpTunnelIfAgingTimer_Type(Integer32):
    """Custom type ipTunnelIfAgingTimer based on Integer32"""
    defaultValue = 10


_IpTunnelIfAgingTimer_Type.__name__ = "Integer32"
_IpTunnelIfAgingTimer_Object = MibTableColumn
ipTunnelIfAgingTimer = _IpTunnelIfAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 14),
    _IpTunnelIfAgingTimer_Type()
)
ipTunnelIfAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfAgingTimer.setStatus("mandatory")


class _IpTunnelIfMTUDiscovery_Type(Integer32):
    """Custom type ipTunnelIfMTUDiscovery based on Integer32"""
    defaultValue = 2

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


_IpTunnelIfMTUDiscovery_Type.__name__ = "Integer32"
_IpTunnelIfMTUDiscovery_Object = MibTableColumn
ipTunnelIfMTUDiscovery = _IpTunnelIfMTUDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 15),
    _IpTunnelIfMTUDiscovery_Type()
)
ipTunnelIfMTUDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfMTUDiscovery.setStatus("mandatory")
_IpTunnelIfMTU_Type = Integer32
_IpTunnelIfMTU_Object = MibTableColumn
ipTunnelIfMTU = _IpTunnelIfMTU_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 16),
    _IpTunnelIfMTU_Type()
)
ipTunnelIfMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipTunnelIfMTU.setStatus("mandatory")


class _IpTunnelIfKeepAliveRetries_Type(Integer32):
    """Custom type ipTunnelIfKeepAliveRetries based on Integer32"""
    defaultValue = 3


_IpTunnelIfKeepAliveRetries_Type.__name__ = "Integer32"
_IpTunnelIfKeepAliveRetries_Object = MibTableColumn
ipTunnelIfKeepAliveRetries = _IpTunnelIfKeepAliveRetries_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 17),
    _IpTunnelIfKeepAliveRetries_Type()
)
ipTunnelIfKeepAliveRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfKeepAliveRetries.setStatus("mandatory")


class _IpTunnelIfKeepAliveRate_Type(Integer32):
    """Custom type ipTunnelIfKeepAliveRate based on Integer32"""
    defaultValue = 10


_IpTunnelIfKeepAliveRate_Type.__name__ = "Integer32"
_IpTunnelIfKeepAliveRate_Object = MibTableColumn
ipTunnelIfKeepAliveRate = _IpTunnelIfKeepAliveRate_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 8, 1, 1, 18),
    _IpTunnelIfKeepAliveRate_Type()
)
ipTunnelIfKeepAliveRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipTunnelIfKeepAliveRate.setStatus("mandatory")
_IpDynamic_ObjectIdentity = ObjectIdentity
ipDynamic = _IpDynamic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 9)
)
_IpDynamicTable_Object = MibTable
ipDynamicTable = _IpDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1)
)
if mibBuilder.loadTexts:
    ipDynamicTable.setStatus("mandatory")
_IpDynamicEntry_Object = MibTableRow
ipDynamicEntry = _IpDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1)
)
ipDynamicEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipDynamicIfIndex"),
)
if mibBuilder.loadTexts:
    ipDynamicEntry.setStatus("mandatory")
_IpDynamicIfIndex_Type = Integer32
_IpDynamicIfIndex_Object = MibTableColumn
ipDynamicIfIndex = _IpDynamicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 1),
    _IpDynamicIfIndex_Type()
)
ipDynamicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicIfIndex.setStatus("mandatory")


class _IpDynamicIfAlias_Type(DisplayString):
    """Custom type ipDynamicIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpDynamicIfAlias_Type.__name__ = "DisplayString"
_IpDynamicIfAlias_Object = MibTableColumn
ipDynamicIfAlias = _IpDynamicIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 2),
    _IpDynamicIfAlias_Type()
)
ipDynamicIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicIfAlias.setStatus("mandatory")


class _IpDynamicAddrType_Type(Integer32):
    """Custom type ipDynamicAddrType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("pppIpcp", 2),
          ("dhcp", 3))
    )


_IpDynamicAddrType_Type.__name__ = "Integer32"
_IpDynamicAddrType_Object = MibTableColumn
ipDynamicAddrType = _IpDynamicAddrType_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 3),
    _IpDynamicAddrType_Type()
)
ipDynamicAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicAddrType.setStatus("mandatory")


class _IpDynamicIPAddress_Type(IpAddress):
    """Custom type ipDynamicIPAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpDynamicIPAddress_Type.__name__ = "IpAddress"
_IpDynamicIPAddress_Object = MibTableColumn
ipDynamicIPAddress = _IpDynamicIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 4),
    _IpDynamicIPAddress_Type()
)
ipDynamicIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicIPAddress.setStatus("mandatory")
_IpDynamicNetMask_Type = IpAddress
_IpDynamicNetMask_Object = MibTableColumn
ipDynamicNetMask = _IpDynamicNetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 5),
    _IpDynamicNetMask_Type()
)
ipDynamicNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicNetMask.setStatus("mandatory")


class _IpDynamicInterfaceName_Type(DisplayString):
    """Custom type ipDynamicInterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpDynamicInterfaceName_Type.__name__ = "DisplayString"
_IpDynamicInterfaceName_Object = MibTableColumn
ipDynamicInterfaceName = _IpDynamicInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 6),
    _IpDynamicInterfaceName_Type()
)
ipDynamicInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicInterfaceName.setStatus("mandatory")


class _IpDynamicOperStatus_Type(Integer32):
    """Custom type ipDynamicOperStatus based on Integer32"""
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


_IpDynamicOperStatus_Type.__name__ = "Integer32"
_IpDynamicOperStatus_Object = MibTableColumn
ipDynamicOperStatus = _IpDynamicOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 7),
    _IpDynamicOperStatus_Type()
)
ipDynamicOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDynamicOperStatus.setStatus("mandatory")


class _IpDynamicIcmpRedirects_Type(Integer32):
    """Custom type ipDynamicIcmpRedirects based on Integer32"""
    defaultValue = 1

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


_IpDynamicIcmpRedirects_Type.__name__ = "Integer32"
_IpDynamicIcmpRedirects_Object = MibTableColumn
ipDynamicIcmpRedirects = _IpDynamicIcmpRedirects_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 9, 1, 1, 8),
    _IpDynamicIcmpRedirects_Type()
)
ipDynamicIcmpRedirects.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDynamicIcmpRedirects.setStatus("mandatory")
_IpNegotiated_ObjectIdentity = ObjectIdentity
ipNegotiated = _IpNegotiated_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 10)
)
_IpNegotiatedTable_Object = MibTable
ipNegotiatedTable = _IpNegotiatedTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 10, 1)
)
if mibBuilder.loadTexts:
    ipNegotiatedTable.setStatus("mandatory")
_IpNegotiatedEntry_Object = MibTableRow
ipNegotiatedEntry = _IpNegotiatedEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 10, 1, 1)
)
ipNegotiatedEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipNegotiatedIfIndex"),
)
if mibBuilder.loadTexts:
    ipNegotiatedEntry.setStatus("mandatory")
_IpNegotiatedIfIndex_Type = Integer32
_IpNegotiatedIfIndex_Object = MibTableColumn
ipNegotiatedIfIndex = _IpNegotiatedIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 10, 1, 1, 1),
    _IpNegotiatedIfIndex_Type()
)
ipNegotiatedIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNegotiatedIfIndex.setStatus("mandatory")
_IpNegotiatedRowStatus_Type = RowStatus
_IpNegotiatedRowStatus_Object = MibTableColumn
ipNegotiatedRowStatus = _IpNegotiatedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 10, 1, 1, 2),
    _IpNegotiatedRowStatus_Type()
)
ipNegotiatedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNegotiatedRowStatus.setStatus("mandatory")


class _IpNegotiatedIfAlias_Type(DisplayString):
    """Custom type ipNegotiatedIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IpNegotiatedIfAlias_Type.__name__ = "DisplayString"
_IpNegotiatedIfAlias_Object = MibTableColumn
ipNegotiatedIfAlias = _IpNegotiatedIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 10, 1, 1, 3),
    _IpNegotiatedIfAlias_Type()
)
ipNegotiatedIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNegotiatedIfAlias.setStatus("mandatory")


class _IpNegotiatedIPAddress_Type(IpAddress):
    """Custom type ipNegotiatedIPAddress based on IpAddress"""
    defaultHexValue = "00000000"


_IpNegotiatedIPAddress_Type.__name__ = "IpAddress"
_IpNegotiatedIPAddress_Object = MibTableColumn
ipNegotiatedIPAddress = _IpNegotiatedIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 10, 1, 1, 4),
    _IpNegotiatedIPAddress_Type()
)
ipNegotiatedIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNegotiatedIPAddress.setStatus("mandatory")
_IpNAT_ObjectIdentity = ObjectIdentity
ipNAT = _IpNAT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 31, 11)
)
_IpNATPoolListTable_Object = MibTable
ipNATPoolListTable = _IpNATPoolListTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 1)
)
if mibBuilder.loadTexts:
    ipNATPoolListTable.setStatus("mandatory")
_IpNATPoolListEntry_Object = MibTableRow
ipNATPoolListEntry = _IpNATPoolListEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 1, 1)
)
ipNATPoolListEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipNATPoolListIndex"),
)
if mibBuilder.loadTexts:
    ipNATPoolListEntry.setStatus("mandatory")
_IpNATPoolListIndex_Type = Integer32
_IpNATPoolListIndex_Object = MibTableColumn
ipNATPoolListIndex = _IpNATPoolListIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 1, 1, 1),
    _IpNATPoolListIndex_Type()
)
ipNATPoolListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNATPoolListIndex.setStatus("mandatory")
_IpNATPoolListName_Type = DisplayString
_IpNATPoolListName_Object = MibTableColumn
ipNATPoolListName = _IpNATPoolListName_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 1, 1, 2),
    _IpNATPoolListName_Type()
)
ipNATPoolListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNATPoolListName.setStatus("mandatory")
_IpNATPoolListRowStatus_Type = RowStatus
_IpNATPoolListRowStatus_Object = MibTableColumn
ipNATPoolListRowStatus = _IpNATPoolListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 1, 1, 3),
    _IpNATPoolListRowStatus_Type()
)
ipNATPoolListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNATPoolListRowStatus.setStatus("mandatory")
_IpNATPoolTable_Object = MibTable
ipNATPoolTable = _IpNATPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2)
)
if mibBuilder.loadTexts:
    ipNATPoolTable.setStatus("mandatory")
_IpNATPoolEntry_Object = MibTableRow
ipNATPoolEntry = _IpNATPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2, 1)
)
ipNATPoolEntry.setIndexNames(
    (0, "CROUTE-MIB", "ipNATPoolListIndex"),
    (0, "CROUTE-MIB", "ipNATPoolIndex"),
)
if mibBuilder.loadTexts:
    ipNATPoolEntry.setStatus("mandatory")
_IpNATPoolIndex_Type = Integer32
_IpNATPoolIndex_Object = MibTableColumn
ipNATPoolIndex = _IpNATPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2, 1, 1),
    _IpNATPoolIndex_Type()
)
ipNATPoolIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNATPoolIndex.setStatus("mandatory")
_IpNATPoolIPAddress_Type = IpAddress
_IpNATPoolIPAddress_Object = MibTableColumn
ipNATPoolIPAddress = _IpNATPoolIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2, 1, 2),
    _IpNATPoolIPAddress_Type()
)
ipNATPoolIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNATPoolIPAddress.setStatus("mandatory")
_IpNATPoolIPMask_Type = IpAddress
_IpNATPoolIPMask_Object = MibTableColumn
ipNATPoolIPMask = _IpNATPoolIPMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2, 1, 3),
    _IpNATPoolIPMask_Type()
)
ipNATPoolIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNATPoolIPMask.setStatus("mandatory")
_IpNATPoolMapIPAddress_Type = IpAddress
_IpNATPoolMapIPAddress_Object = MibTableColumn
ipNATPoolMapIPAddress = _IpNATPoolMapIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2, 1, 4),
    _IpNATPoolMapIPAddress_Type()
)
ipNATPoolMapIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNATPoolMapIPAddress.setStatus("mandatory")
_IpNATPoolMapIPMask_Type = IpAddress
_IpNATPoolMapIPMask_Object = MibTableColumn
ipNATPoolMapIPMask = _IpNATPoolMapIPMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2, 1, 5),
    _IpNATPoolMapIPMask_Type()
)
ipNATPoolMapIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNATPoolMapIPMask.setStatus("mandatory")
_IpNATPoolRowStatus_Type = Integer32
_IpNATPoolRowStatus_Object = MibTableColumn
ipNATPoolRowStatus = _IpNATPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 81, 31, 11, 2, 1, 6),
    _IpNATPoolRowStatus_Type()
)
ipNATPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNATPoolRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CROUTE-MIB",
    **{"RowStatus": RowStatus,
       "NetNum": NetNum,
       "croute": croute,
       "ipRoute": ipRoute,
       "ipGlobals": ipGlobals,
       "ipGlobalsBOOTPRelayStatus": ipGlobalsBOOTPRelayStatus,
       "ipGlobalsICMPErrMsgEnable": ipGlobalsICMPErrMsgEnable,
       "ipGlobalsARPInactiveTimeout": ipGlobalsARPInactiveTimeout,
       "ipGlobalsPrimaryManagementIPAddress": ipGlobalsPrimaryManagementIPAddress,
       "ipGlobalsNextPrimaryManagementIPAddress": ipGlobalsNextPrimaryManagementIPAddress,
       "ipInterfaceTable": ipInterfaceTable,
       "ipInterfaceEntry": ipInterfaceEntry,
       "ipInterfaceAddr": ipInterfaceAddr,
       "ipInterfaceNetMask": ipInterfaceNetMask,
       "ipInterfaceLowerIfAlias": ipInterfaceLowerIfAlias,
       "ipInterfaceType": ipInterfaceType,
       "ipInterfaceForwardIpBroadcast": ipInterfaceForwardIpBroadcast,
       "ipInterfaceBroadcastAddr": ipInterfaceBroadcastAddr,
       "ipInterfaceProxyArp": ipInterfaceProxyArp,
       "ipInterfaceStatus": ipInterfaceStatus,
       "ipInterfaceMainRouterAddr": ipInterfaceMainRouterAddr,
       "ipInterfaceARPServerStatus": ipInterfaceARPServerStatus,
       "ipInterfaceName": ipInterfaceName,
       "ipInterfaceNetbiosRebroadcast": ipInterfaceNetbiosRebroadcast,
       "ipInterfaceIcmpRedirects": ipInterfaceIcmpRedirects,
       "ipInterfaceOperStatus": ipInterfaceOperStatus,
       "ipInterfaceDhcpRelay": ipInterfaceDhcpRelay,
       "ipInterfaceAddrType": ipInterfaceAddrType,
       "ipInterfaceAddrUnnumbered": ipInterfaceAddrUnnumbered,
       "ipInterfaceUnnumberedLowerIfAlias": ipInterfaceUnnumberedLowerIfAlias,
       "ipInterfaceReasmMaxSize": ipInterfaceReasmMaxSize,
       "ripGlobals": ripGlobals,
       "ripGlobalsRIPEnable": ripGlobalsRIPEnable,
       "ripGlobalsLeakOSPFIntoRIP": ripGlobalsLeakOSPFIntoRIP,
       "ripGlobalsLeakStaticIntoRIP": ripGlobalsLeakStaticIntoRIP,
       "ripGlobalsPeriodicUpdateTimer": ripGlobalsPeriodicUpdateTimer,
       "ripGlobalsPeriodicInvalidRouteTimer": ripGlobalsPeriodicInvalidRouteTimer,
       "ripGlobalsDefaultExportMetric": ripGlobalsDefaultExportMetric,
       "ripInterfaceTable": ripInterfaceTable,
       "ripInterfaceEntry": ripInterfaceEntry,
       "ripInterfaceAddr": ripInterfaceAddr,
       "ripInterfaceMetric": ripInterfaceMetric,
       "ripInterfaceSplitHorizon": ripInterfaceSplitHorizon,
       "ripInterfaceAcceptDefaultRoute": ripInterfaceAcceptDefaultRoute,
       "ripInterfaceSendDefaultRoute": ripInterfaceSendDefaultRoute,
       "ripInterfaceState": ripInterfaceState,
       "ripInterfaceSendMode": ripInterfaceSendMode,
       "ripInterfaceVersion": ripInterfaceVersion,
       "ospfGlobals": ospfGlobals,
       "ospfGlobalsLeakRIPIntoOSPF": ospfGlobalsLeakRIPIntoOSPF,
       "ospfGlobalsLeakStaticIntoOSPF": ospfGlobalsLeakStaticIntoOSPF,
       "ospfGlobalsLeakDirectIntoOSPF": ospfGlobalsLeakDirectIntoOSPF,
       "ospfGlobalsDefaultExportMetric": ospfGlobalsDefaultExportMetric,
       "relayTable": relayTable,
       "relayEntry": relayEntry,
       "relayVlIndex": relayVlIndex,
       "relayVlPrimaryServerAddr": relayVlPrimaryServerAddr,
       "relayVlSeconderyServerAddr": relayVlSeconderyServerAddr,
       "relayVlStatus": relayVlStatus,
       "relayVlRelayAddr": relayVlRelayAddr,
       "ipAccessGlobals": ipAccessGlobals,
       "ipAccessControlEnable": ipAccessControlEnable,
       "ipAccessControlTable": ipAccessControlTable,
       "ipAccessControlEntry": ipAccessControlEntry,
       "ipAccessControlIndex": ipAccessControlIndex,
       "ipAccessControlSrcAddr": ipAccessControlSrcAddr,
       "ipAccessControlSrcMask": ipAccessControlSrcMask,
       "ipAccessControlDstAddr": ipAccessControlDstAddr,
       "ipAccessControlDstMask": ipAccessControlDstMask,
       "ipAccessControlOperation": ipAccessControlOperation,
       "ipAccessControlActivation": ipAccessControlActivation,
       "ipAccessControlProtocol": ipAccessControlProtocol,
       "ipAccessControlApplication": ipAccessControlApplication,
       "ipAccessControlStatus": ipAccessControlStatus,
       "ipRedundancyGlobals": ipRedundancyGlobals,
       "ipRedundancyStatus": ipRedundancyStatus,
       "ipRedundancyTimeout": ipRedundancyTimeout,
       "ipRedundancyPollingInterval": ipRedundancyPollingInterval,
       "ipShortcutGlobals": ipShortcutGlobals,
       "ipShortcutARPServerStatus": ipShortcutARPServerStatus,
       "ipMulticastInterfaceTable": ipMulticastInterfaceTable,
       "ipMulticastInterfaceEntry": ipMulticastInterfaceEntry,
       "ipMulticastInterfaceIfIndex": ipMulticastInterfaceIfIndex,
       "ipMulticastInterfaceSendAll": ipMulticastInterfaceSendAll,
       "ipMulticastInterfaceState": ipMulticastInterfaceState,
       "ipMulticastInterfaceStatus": ipMulticastInterfaceStatus,
       "distributionListTable": distributionListTable,
       "distributionListEntry": distributionListEntry,
       "distributionListRoutingProtocol": distributionListRoutingProtocol,
       "distributionListDirection": distributionListDirection,
       "distributionListIfIndex": distributionListIfIndex,
       "distributionListRouteProtocol": distributionListRouteProtocol,
       "distributionListProtocolSpecific1": distributionListProtocolSpecific1,
       "distributionListProtocolSpecific2": distributionListProtocolSpecific2,
       "distributionListProtocolSpecific3": distributionListProtocolSpecific3,
       "distributionListProtocolSpecific4": distributionListProtocolSpecific4,
       "distributionListProtocolSpecific5": distributionListProtocolSpecific5,
       "distributionListAccessListNumber": distributionListAccessListNumber,
       "distributionListEntryStatus": distributionListEntryStatus,
       "ipEZ2RouteMgmt": ipEZ2RouteMgmt,
       "ipEZ2BoostRouterTable": ipEZ2BoostRouterTable,
       "ipEZ2BoostRouterEntry": ipEZ2BoostRouterEntry,
       "ipEZ2BoostRouterSlot": ipEZ2BoostRouterSlot,
       "ipEZ2BoostRouterBRAddress": ipEZ2BoostRouterBRAddress,
       "ipEZ2BoostRouterType": ipEZ2BoostRouterType,
       "ipEZ2BoostRouterStatus": ipEZ2BoostRouterStatus,
       "ipEZ2RControlTable": ipEZ2RControlTable,
       "ipEZ2RControlEntry": ipEZ2RControlEntry,
       "ipEZ2RControlSlot": ipEZ2RControlSlot,
       "ipEZ2RControlBoostedRoutersTimeout": ipEZ2RControlBoostedRoutersTimeout,
       "ipEZ2RControlHostsTimeout": ipEZ2RControlHostsTimeout,
       "ipEZ2RControlAutoLearnMode": ipEZ2RControlAutoLearnMode,
       "ipVRRP": ipVRRP,
       "ipVRRPAdminStatus": ipVRRPAdminStatus,
       "iphcObjects": iphcObjects,
       "iphcControlTable": iphcControlTable,
       "iphcControlEntry": iphcControlEntry,
       "iphcIfIndex": iphcIfIndex,
       "iphcControlTcpAdminStatus": iphcControlTcpAdminStatus,
       "iphcTcpSessions": iphcTcpSessions,
       "iphcNegotiatedTcpSessions": iphcNegotiatedTcpSessions,
       "iphcControlRtpAdminStatus": iphcControlRtpAdminStatus,
       "iphcRtpSessions": iphcRtpSessions,
       "iphcNegotiatedRtpSessions": iphcNegotiatedRtpSessions,
       "iphcControlNonTcpAdminStatus": iphcControlNonTcpAdminStatus,
       "iphcNonTcpSessions": iphcNonTcpSessions,
       "iphcNegotiatedNonTcpSessions": iphcNegotiatedNonTcpSessions,
       "iphcMaxPeriod": iphcMaxPeriod,
       "iphcMaxTime": iphcMaxTime,
       "iphcControRtpMinPortNumber": iphcControRtpMinPortNumber,
       "iphcControRtpMaxPortNumber": iphcControRtpMaxPortNumber,
       "iphcControlRtpCompressionRatio": iphcControlRtpCompressionRatio,
       "iphcControlNonTcpMode": iphcControlNonTcpMode,
       "iphcControlTcpCompressionRatio": iphcControlTcpCompressionRatio,
       "iphcControlTotalCompressionRatio": iphcControlTotalCompressionRatio,
       "ospfXtndIfTable": ospfXtndIfTable,
       "ospfXtndIfEntry": ospfXtndIfEntry,
       "ospfXtndIfIpAddress": ospfXtndIfIpAddress,
       "ospfXtndIfAddressLessIf": ospfXtndIfAddressLessIf,
       "ospfXtndIfPassiveMode": ospfXtndIfPassiveMode,
       "nextHop": nextHop,
       "nextHopListTable": nextHopListTable,
       "nextHopListEntry": nextHopListEntry,
       "nextHopListIndex": nextHopListIndex,
       "nextHopListName": nextHopListName,
       "nextHopListRowStatus": nextHopListRowStatus,
       "nextHopListActive": nextHopListActive,
       "nextHopTable": nextHopTable,
       "nextHopEntry": nextHopEntry,
       "nextHopIndex": nextHopIndex,
       "nextHopType": nextHopType,
       "nextHopIP": nextHopIP,
       "nextHopInterface": nextHopInterface,
       "nextHopStatus": nextHopStatus,
       "nextHopRowStatus": nextHopRowStatus,
       "nextHopTrackId": nextHopTrackId,
       "ospfCompleteIfTable": ospfCompleteIfTable,
       "ospfCompleteIfEntry": ospfCompleteIfEntry,
       "ospfCompleteIfIpAddress": ospfCompleteIfIpAddress,
       "ospfCompleteAddressLessIf": ospfCompleteAddressLessIf,
       "ospfCompleteIfAreaId": ospfCompleteIfAreaId,
       "ospfCompleteIfType": ospfCompleteIfType,
       "ospfCompleteIfAdminStat": ospfCompleteIfAdminStat,
       "ospfCompleteIfRtrPriority": ospfCompleteIfRtrPriority,
       "ospfCompleteIfTransitDelay": ospfCompleteIfTransitDelay,
       "ospfCompleteIfRetransInterval": ospfCompleteIfRetransInterval,
       "ospfCompleteIfHelloInterval": ospfCompleteIfHelloInterval,
       "ospfCompleteIfRtrDeadInterval": ospfCompleteIfRtrDeadInterval,
       "ospfCompleteIfPollInterval": ospfCompleteIfPollInterval,
       "ospfCompleteIfState": ospfCompleteIfState,
       "ospfCompleteIfDesignatedRouter": ospfCompleteIfDesignatedRouter,
       "ospfCompleteIfBackupDesignatedRouter": ospfCompleteIfBackupDesignatedRouter,
       "ospfCompleteIfEvents": ospfCompleteIfEvents,
       "ospfCompleteIfAuthKey": ospfCompleteIfAuthKey,
       "ospfCompleteIfStatus": ospfCompleteIfStatus,
       "ospfCompleteIfMulticastForwarding": ospfCompleteIfMulticastForwarding,
       "ospfCompleteIfDemand": ospfCompleteIfDemand,
       "ospfCompleteIfAuthType": ospfCompleteIfAuthType,
       "ospfCompleteIfMetricTable": ospfCompleteIfMetricTable,
       "ospfCompleteIfMetricEntry": ospfCompleteIfMetricEntry,
       "ospfCompleteIfMetricIpAddress": ospfCompleteIfMetricIpAddress,
       "ospfCompleteIfMetricAddressLessIf": ospfCompleteIfMetricAddressLessIf,
       "ospfCompleteIfMetricTOS": ospfCompleteIfMetricTOS,
       "ospfCompleteIfMetricValue": ospfCompleteIfMetricValue,
       "ospfCompleteIfMetricStatus": ospfCompleteIfMetricStatus,
       "rip2CompleteIfStatTable": rip2CompleteIfStatTable,
       "rip2CompleteIfStatEntry": rip2CompleteIfStatEntry,
       "rip2CompleteIfStatAddress": rip2CompleteIfStatAddress,
       "rip2CompleteIfStatRcvBadPackets": rip2CompleteIfStatRcvBadPackets,
       "rip2CompleteIfStatRcvBadRoutes": rip2CompleteIfStatRcvBadRoutes,
       "rip2CompleteIfStatSentUpdates": rip2CompleteIfStatSentUpdates,
       "rip2CompleteIfStatStatus": rip2CompleteIfStatStatus,
       "rip2CompleteIfConfTable": rip2CompleteIfConfTable,
       "rip2CompleteIfConfEntry": rip2CompleteIfConfEntry,
       "rip2CompleteIfConfAddress": rip2CompleteIfConfAddress,
       "rip2CompleteIfConfDomain": rip2CompleteIfConfDomain,
       "rip2CompleteIfConfAuthType": rip2CompleteIfConfAuthType,
       "rip2CompleteIfConfAuthKey": rip2CompleteIfConfAuthKey,
       "rip2CompleteIfConfSend": rip2CompleteIfConfSend,
       "rip2CompleteIfConfReceive": rip2CompleteIfConfReceive,
       "rip2CompleteIfConfDefaultMetric": rip2CompleteIfConfDefaultMetric,
       "rip2CompleteIfConfStatus": rip2CompleteIfConfStatus,
       "rip2CompleteIfConfSrcAddress": rip2CompleteIfConfSrcAddress,
       "ipCidrRouteStaticTable": ipCidrRouteStaticTable,
       "ipCidrRouteStaticEntry": ipCidrRouteStaticEntry,
       "ipCidrRouteStaticDest": ipCidrRouteStaticDest,
       "ipCidrRouteStaticMask": ipCidrRouteStaticMask,
       "ipCidrRouteStaticIfIndex": ipCidrRouteStaticIfIndex,
       "ipCidrRouteStaticNextHop": ipCidrRouteStaticNextHop,
       "ipCidrRouteStaticPreference": ipCidrRouteStaticPreference,
       "ipCidrRouteStaticUsedIfIndex": ipCidrRouteStaticUsedIfIndex,
       "ipCidrRouteStaticUsedNextHop": ipCidrRouteStaticUsedNextHop,
       "ipCidrRouteStaticType": ipCidrRouteStaticType,
       "ipCidrRouteStaticCost": ipCidrRouteStaticCost,
       "ipCidrRouteStaticPermanent": ipCidrRouteStaticPermanent,
       "ipCidrRouteStaticTrackId": ipCidrRouteStaticTrackId,
       "ipCidrRouteStaticActive": ipCidrRouteStaticActive,
       "ipCidrRouteStaticRowStatus": ipCidrRouteStaticRowStatus,
       "ipxRoute": ipxRoute,
       "ipxCircTable": ipxCircTable,
       "ipxCircEntry": ipxCircEntry,
       "ipxCircIndex": ipxCircIndex,
       "ipxCircNetNumber": ipxCircNetNumber,
       "ipxCircLowerIfAlias": ipxCircLowerIfAlias,
       "ipxCircEncapsulation": ipxCircEncapsulation,
       "ipxCircNetbios": ipxCircNetbios,
       "ipxCircStatus": ipxCircStatus,
       "ipxCircRipUpdate": ipxCircRipUpdate,
       "ipxCircRipAgeMultiplier": ipxCircRipAgeMultiplier,
       "ipxCircRipStatus": ipxCircRipStatus,
       "ipxCircSapUpdate": ipxCircSapUpdate,
       "ipxCircSapAgeMultiplier": ipxCircSapAgeMultiplier,
       "ipxCircGetNearestServerReply": ipxCircGetNearestServerReply,
       "ipxCircSapStatus": ipxCircSapStatus,
       "ipxCircRipState": ipxCircRipState,
       "ipxCircSapState": ipxCircSapState,
       "ipxDestTable": ipxDestTable,
       "ipxDestEntry": ipxDestEntry,
       "ipxDestNetNum": ipxDestNetNum,
       "ipxDestProtocol": ipxDestProtocol,
       "ipxDestTicks": ipxDestTicks,
       "ipxDestHopCount": ipxDestHopCount,
       "ipxDestNextHopCircIndex": ipxDestNextHopCircIndex,
       "ipxDestNextHopNICAddress": ipxDestNextHopNICAddress,
       "ipxDestNextHopNetNum": ipxDestNextHopNetNum,
       "ipxDestStatus": ipxDestStatus,
       "ipxDestAge": ipxDestAge,
       "ipxServTable": ipxServTable,
       "ipxServEntry": ipxServEntry,
       "ipxServType": ipxServType,
       "ipxServName": ipxServName,
       "ipxServProtocol": ipxServProtocol,
       "ipxServNetNum": ipxServNetNum,
       "ipxServNode": ipxServNode,
       "ipxServSocket": ipxServSocket,
       "ipxServHopCount": ipxServHopCount,
       "ipxServStatus": ipxServStatus,
       "ipxServAge": ipxServAge,
       "ipxAccessGlobals": ipxAccessGlobals,
       "ipxAccessControlEnable": ipxAccessControlEnable,
       "ipxAccessControlTable": ipxAccessControlTable,
       "ipxAccessControlEntry": ipxAccessControlEntry,
       "ipxAccessControlIndex": ipxAccessControlIndex,
       "ipxAccessControlSrcAddr": ipxAccessControlSrcAddr,
       "ipxAccessControlDstAddr": ipxAccessControlDstAddr,
       "ipxAccessControlOperation": ipxAccessControlOperation,
       "ipxAccessControlActivation": ipxAccessControlActivation,
       "ipxAccessControlStatus": ipxAccessControlStatus,
       "ipxSapFilterGlobals": ipxSapFilterGlobals,
       "ipxSapFilterEnable": ipxSapFilterEnable,
       "ipxSapFilterTable": ipxSapFilterTable,
       "ipxSapFilterEntry": ipxSapFilterEntry,
       "ipxSapFilterID": ipxSapFilterID,
       "ipxSapFilterCircIndex": ipxSapFilterCircIndex,
       "ipxSapFilterServiceNetNumber": ipxSapFilterServiceNetNumber,
       "ipxSapFilterServiceType": ipxSapFilterServiceType,
       "ipxSapFilterServerName": ipxSapFilterServerName,
       "ipxSapFilterDirection": ipxSapFilterDirection,
       "ipxSapFilterAction": ipxSapFilterAction,
       "ipxSapFilterStatus": ipxSapFilterStatus,
       "layer2": layer2,
       "vlConfTable": vlConfTable,
       "vlConfEntry": vlConfEntry,
       "vlConfIndex": vlConfIndex,
       "vlConfAlias": vlConfAlias,
       "vlConfStatus": vlConfStatus,
       "vlBridgeTable": vlBridgeTable,
       "vlBridgeEntry": vlBridgeEntry,
       "vlBridgeProtocol": vlBridgeProtocol,
       "vlBridgeGroupIndex": vlBridgeGroupIndex,
       "vlBridgeIndex": vlBridgeIndex,
       "vlBridgeStatus": vlBridgeStatus,
       "layer2Globals": layer2Globals,
       "layer2GlobalsBridgeEnable": layer2GlobalsBridgeEnable,
       "routeGroupMgmt": routeGroupMgmt,
       "routeGroupTable": routeGroupTable,
       "routeGroupEntry": routeGroupEntry,
       "routeGroupId": routeGroupId,
       "routeGroupRouteMode": routeGroupRouteMode,
       "drLayer2": drLayer2,
       "drVlConfTable": drVlConfTable,
       "drVlConfEntry": drVlConfEntry,
       "drVlConfSlot": drVlConfSlot,
       "drVlConfIndex": drVlConfIndex,
       "drVlConfAlias": drVlConfAlias,
       "drVlConfStatus": drVlConfStatus,
       "drIpRoute": drIpRoute,
       "drIpInterfaceTable": drIpInterfaceTable,
       "drIpInterfaceEntry": drIpInterfaceEntry,
       "drIpInterfaceSlot": drIpInterfaceSlot,
       "drIpInterfaceAddr": drIpInterfaceAddr,
       "drIpInterfaceNetMask": drIpInterfaceNetMask,
       "drIpInterfaceLowerIfAlias": drIpInterfaceLowerIfAlias,
       "drIpInterfaceType": drIpInterfaceType,
       "drIpInterfaceForwardIpBroadcast": drIpInterfaceForwardIpBroadcast,
       "drIpInterfaceBroadcastAddr": drIpInterfaceBroadcastAddr,
       "drIpInterfaceProxyArp": drIpInterfaceProxyArp,
       "drIpInterfaceStatus": drIpInterfaceStatus,
       "drIpInterfaceMainRouterAddr": drIpInterfaceMainRouterAddr,
       "drIpInterfaceARPServerStatus": drIpInterfaceARPServerStatus,
       "drIpInterfaceName": drIpInterfaceName,
       "drIpInterfaceNetbiosRebroadcast": drIpInterfaceNetbiosRebroadcast,
       "drIpInterfaceIcmpRedirects": drIpInterfaceIcmpRedirects,
       "drIpInterfaceOperStatus": drIpInterfaceOperStatus,
       "drIpInterfaceDhcpRelay": drIpInterfaceDhcpRelay,
       "drStaticCidr": drStaticCidr,
       "drStaticCidrTable": drStaticCidrTable,
       "drStaticCidrEntry": drStaticCidrEntry,
       "drStaticCidrEntID": drStaticCidrEntID,
       "drStaticCidrDest": drStaticCidrDest,
       "drStaticCidrMask": drStaticCidrMask,
       "drStaticCidrTos": drStaticCidrTos,
       "drStaticCidrNextHop": drStaticCidrNextHop,
       "drStaticCidrIfIndex": drStaticCidrIfIndex,
       "drStaticCidrType": drStaticCidrType,
       "drStaticCidrMetric1": drStaticCidrMetric1,
       "drStaticCidrPrecedence": drStaticCidrPrecedence,
       "drStaticCidrCRPType": drStaticCidrCRPType,
       "drStaticCidrOperStatus": drStaticCidrOperStatus,
       "drStaticCidrName": drStaticCidrName,
       "drStaticOwner": drStaticOwner,
       "drStaticCidrStatus": drStaticCidrStatus,
       "ipTunnel": ipTunnel,
       "ipTunnelTable": ipTunnelTable,
       "ipTunnelEntry": ipTunnelEntry,
       "ipTunnelIfIndex": ipTunnelIfIndex,
       "ipTunnelIfStatus": ipTunnelIfStatus,
       "ipTunnelIfLocalAddress": ipTunnelIfLocalAddress,
       "ipTunnelIfRemoteAddress": ipTunnelIfRemoteAddress,
       "ipTunnelIfEncapsMethod": ipTunnelIfEncapsMethod,
       "ipTunnelIfConfigID": ipTunnelIfConfigID,
       "ipTunnelIfHopLimit": ipTunnelIfHopLimit,
       "ipTunnelIfSecurity": ipTunnelIfSecurity,
       "ipTunnelIfDSCP": ipTunnelIfDSCP,
       "ipTunnelIfChecksum": ipTunnelIfChecksum,
       "ipTunnelIfKey": ipTunnelIfKey,
       "ipTunnelIfKeyMode": ipTunnelIfKeyMode,
       "ipTunnelIfOutOfOrderDrop": ipTunnelIfOutOfOrderDrop,
       "ipTunnelIfAgingTimer": ipTunnelIfAgingTimer,
       "ipTunnelIfMTUDiscovery": ipTunnelIfMTUDiscovery,
       "ipTunnelIfMTU": ipTunnelIfMTU,
       "ipTunnelIfKeepAliveRetries": ipTunnelIfKeepAliveRetries,
       "ipTunnelIfKeepAliveRate": ipTunnelIfKeepAliveRate,
       "ipDynamic": ipDynamic,
       "ipDynamicTable": ipDynamicTable,
       "ipDynamicEntry": ipDynamicEntry,
       "ipDynamicIfIndex": ipDynamicIfIndex,
       "ipDynamicIfAlias": ipDynamicIfAlias,
       "ipDynamicAddrType": ipDynamicAddrType,
       "ipDynamicIPAddress": ipDynamicIPAddress,
       "ipDynamicNetMask": ipDynamicNetMask,
       "ipDynamicInterfaceName": ipDynamicInterfaceName,
       "ipDynamicOperStatus": ipDynamicOperStatus,
       "ipDynamicIcmpRedirects": ipDynamicIcmpRedirects,
       "ipNegotiated": ipNegotiated,
       "ipNegotiatedTable": ipNegotiatedTable,
       "ipNegotiatedEntry": ipNegotiatedEntry,
       "ipNegotiatedIfIndex": ipNegotiatedIfIndex,
       "ipNegotiatedRowStatus": ipNegotiatedRowStatus,
       "ipNegotiatedIfAlias": ipNegotiatedIfAlias,
       "ipNegotiatedIPAddress": ipNegotiatedIPAddress,
       "ipNAT": ipNAT,
       "ipNATPoolListTable": ipNATPoolListTable,
       "ipNATPoolListEntry": ipNATPoolListEntry,
       "ipNATPoolListIndex": ipNATPoolListIndex,
       "ipNATPoolListName": ipNATPoolListName,
       "ipNATPoolListRowStatus": ipNATPoolListRowStatus,
       "ipNATPoolTable": ipNATPoolTable,
       "ipNATPoolEntry": ipNATPoolEntry,
       "ipNATPoolIndex": ipNATPoolIndex,
       "ipNATPoolIPAddress": ipNATPoolIPAddress,
       "ipNATPoolIPMask": ipNATPoolIPMask,
       "ipNATPoolMapIPAddress": ipNATPoolMapIPAddress,
       "ipNATPoolMapIPMask": ipNATPoolMapIPMask,
       "ipNATPoolRowStatus": ipNATPoolRowStatus}
)
