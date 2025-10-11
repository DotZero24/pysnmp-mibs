# SNMP MIB module (FS-CAPWAP-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CAPWAP-DHCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:26 2025
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

(fsIfIndex,) = mibBuilder.importSymbols(
    "FS-INTERFACE-MIB",
    "fsIfIndex")

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsCapwapDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58)
)
if mibBuilder.loadTexts:
    fsCapwapDhcpMIB.setRevisions(
        ("2009-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCapwapDhcpMIBTrap_ObjectIdentity = ObjectIdentity
fsCapwapDhcpMIBTrap = _FsCapwapDhcpMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 0)
)
_FsCapwapDhcpMIBObjects_ObjectIdentity = ObjectIdentity
fsCapwapDhcpMIBObjects = _FsCapwapDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1)
)
_FsCapwapDhcpGlobalConfig_ObjectIdentity = ObjectIdentity
fsCapwapDhcpGlobalConfig = _FsCapwapDhcpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 1)
)
_FsLDhcpClearAllStats_Type = TruthValue
_FsLDhcpClearAllStats_Object = MibScalar
fsLDhcpClearAllStats = _FsLDhcpClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 1, 1),
    _FsLDhcpClearAllStats_Type()
)
fsLDhcpClearAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLDhcpClearAllStats.setStatus("current")


class _FsLDhcpStartService_Type(Integer32):
    """Custom type fsLDhcpStartService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsLDhcpStartService_Type.__name__ = "Integer32"
_FsLDhcpStartService_Object = MibScalar
fsLDhcpStartService = _FsLDhcpStartService_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 1, 2),
    _FsLDhcpStartService_Type()
)
fsLDhcpStartService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLDhcpStartService.setStatus("current")
_FsDhcpClientMacAddress_Type = MacAddress
_FsDhcpClientMacAddress_Object = MibScalar
fsDhcpClientMacAddress = _FsDhcpClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 1, 3),
    _FsDhcpClientMacAddress_Type()
)
fsDhcpClientMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDhcpClientMacAddress.setStatus("current")


class _FsLDhcpStartTIService_Type(Integer32):
    """Custom type fsLDhcpStartTIService based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsLDhcpStartTIService_Type.__name__ = "Integer32"
_FsLDhcpStartTIService_Object = MibScalar
fsLDhcpStartTIService = _FsLDhcpStartTIService_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 1, 4),
    _FsLDhcpStartTIService_Type()
)
fsLDhcpStartTIService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLDhcpStartTIService.setStatus("current")
_FsDhcpServerTlvNum_Type = Integer32
_FsDhcpServerTlvNum_Object = MibScalar
fsDhcpServerTlvNum = _FsDhcpServerTlvNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 1, 5),
    _FsDhcpServerTlvNum_Type()
)
fsDhcpServerTlvNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDhcpServerTlvNum.setStatus("current")
_FsDhcpServerTlv_Type = DisplayString
_FsDhcpServerTlv_Object = MibScalar
fsDhcpServerTlv = _FsDhcpServerTlv_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 1, 6),
    _FsDhcpServerTlv_Type()
)
fsDhcpServerTlv.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDhcpServerTlv.setStatus("current")
_FsCapwapDhcpShowStats_ObjectIdentity = ObjectIdentity
fsCapwapDhcpShowStats = _FsCapwapDhcpShowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2)
)
_FsLDhcpDiscoverPkts_Type = Unsigned32
_FsLDhcpDiscoverPkts_Object = MibScalar
fsLDhcpDiscoverPkts = _FsLDhcpDiscoverPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 1),
    _FsLDhcpDiscoverPkts_Type()
)
fsLDhcpDiscoverPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpDiscoverPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpDiscoverPkts.setUnits("packets")
_FsLDhcpRequestPkts_Type = Unsigned32
_FsLDhcpRequestPkts_Object = MibScalar
fsLDhcpRequestPkts = _FsLDhcpRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 2),
    _FsLDhcpRequestPkts_Type()
)
fsLDhcpRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpRequestPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpRequestPkts.setUnits("packets")
_FsLDhcpDeclinePkts_Type = Unsigned32
_FsLDhcpDeclinePkts_Object = MibScalar
fsLDhcpDeclinePkts = _FsLDhcpDeclinePkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 3),
    _FsLDhcpDeclinePkts_Type()
)
fsLDhcpDeclinePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpDeclinePkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpDeclinePkts.setUnits("packets")
_FsLDhcpInformPkts_Type = Unsigned32
_FsLDhcpInformPkts_Object = MibScalar
fsLDhcpInformPkts = _FsLDhcpInformPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 4),
    _FsLDhcpInformPkts_Type()
)
fsLDhcpInformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpInformPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpInformPkts.setUnits("packets")
_FsLDhcpReleasePkts_Type = Unsigned32
_FsLDhcpReleasePkts_Object = MibScalar
fsLDhcpReleasePkts = _FsLDhcpReleasePkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 5),
    _FsLDhcpReleasePkts_Type()
)
fsLDhcpReleasePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpReleasePkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpReleasePkts.setUnits("packets")
_FsLDhcpReplyPkts_Type = Unsigned32
_FsLDhcpReplyPkts_Object = MibScalar
fsLDhcpReplyPkts = _FsLDhcpReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 6),
    _FsLDhcpReplyPkts_Type()
)
fsLDhcpReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpReplyPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpReplyPkts.setUnits("packets")
_FsLDhcpOfferPkts_Type = Unsigned32
_FsLDhcpOfferPkts_Object = MibScalar
fsLDhcpOfferPkts = _FsLDhcpOfferPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 7),
    _FsLDhcpOfferPkts_Type()
)
fsLDhcpOfferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpOfferPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpOfferPkts.setUnits("packets")
_FsLDhcpAckPkts_Type = Unsigned32
_FsLDhcpAckPkts_Object = MibScalar
fsLDhcpAckPkts = _FsLDhcpAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 8),
    _FsLDhcpAckPkts_Type()
)
fsLDhcpAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpAckPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpAckPkts.setUnits("packets")
_FsLDhcpNakPkts_Type = Unsigned32
_FsLDhcpNakPkts_Object = MibScalar
fsLDhcpNakPkts = _FsLDhcpNakPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 9),
    _FsLDhcpNakPkts_Type()
)
fsLDhcpNakPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpNakPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpNakPkts.setUnits("packets")
_FsLDhcpReqTimes_Type = Unsigned32
_FsLDhcpReqTimes_Object = MibScalar
fsLDhcpReqTimes = _FsLDhcpReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 10),
    _FsLDhcpReqTimes_Type()
)
fsLDhcpReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpReqTimes.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpReqTimes.setUnits("packets")
_FsLDhcpReqSucTimes_Type = Unsigned32
_FsLDhcpReqSucTimes_Object = MibScalar
fsLDhcpReqSucTimes = _FsLDhcpReqSucTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 2, 11),
    _FsLDhcpReqSucTimes_Type()
)
fsLDhcpReqSucTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLDhcpReqSucTimes.setStatus("current")
if mibBuilder.loadTexts:
    fsLDhcpReqSucTimes.setUnits("packets")
_FsCapwapDhcpServerConfig_ObjectIdentity = ObjectIdentity
fsCapwapDhcpServerConfig = _FsCapwapDhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3)
)
_FsDhcpScopeTable_Object = MibTable
fsDhcpScopeTable = _FsDhcpScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsDhcpScopeTable.setStatus("current")
_FsDhcpScopeEntry_Object = MibTableRow
fsDhcpScopeEntry = _FsDhcpScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1)
)
fsDhcpScopeEntry.setIndexNames(
    (0, "FS-CAPWAP-DHCP-MIB", "fsDhcpScopeIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpScopeEntry.setStatus("current")


class _FsDhcpScopeIndex_Type(Unsigned32):
    """Custom type fsDhcpScopeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_FsDhcpScopeIndex_Type.__name__ = "Unsigned32"
_FsDhcpScopeIndex_Object = MibTableColumn
fsDhcpScopeIndex = _FsDhcpScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 1),
    _FsDhcpScopeIndex_Type()
)
fsDhcpScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcpScopeIndex.setStatus("current")


class _FsDhcpScopeName_Type(DisplayString):
    """Custom type fsDhcpScopeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsDhcpScopeName_Type.__name__ = "DisplayString"
_FsDhcpScopeName_Object = MibTableColumn
fsDhcpScopeName = _FsDhcpScopeName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 2),
    _FsDhcpScopeName_Type()
)
fsDhcpScopeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeName.setStatus("current")


class _FsDhcpScopeLeaseTime_Type(Integer32):
    """Custom type fsDhcpScopeLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 8640000),
    )


_FsDhcpScopeLeaseTime_Type.__name__ = "Integer32"
_FsDhcpScopeLeaseTime_Object = MibTableColumn
fsDhcpScopeLeaseTime = _FsDhcpScopeLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 3),
    _FsDhcpScopeLeaseTime_Type()
)
fsDhcpScopeLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeLeaseTime.setStatus("current")
_FsDhcpScopeNetwork_Type = IpAddress
_FsDhcpScopeNetwork_Object = MibTableColumn
fsDhcpScopeNetwork = _FsDhcpScopeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 4),
    _FsDhcpScopeNetwork_Type()
)
fsDhcpScopeNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeNetwork.setStatus("current")
_FsDhcpScopeNetmask_Type = IpAddress
_FsDhcpScopeNetmask_Object = MibTableColumn
fsDhcpScopeNetmask = _FsDhcpScopeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 5),
    _FsDhcpScopeNetmask_Type()
)
fsDhcpScopeNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeNetmask.setStatus("current")
_FsDhcpScopePoolStartAddress_Type = IpAddress
_FsDhcpScopePoolStartAddress_Object = MibTableColumn
fsDhcpScopePoolStartAddress = _FsDhcpScopePoolStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 6),
    _FsDhcpScopePoolStartAddress_Type()
)
fsDhcpScopePoolStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopePoolStartAddress.setStatus("current")
_FsDhcpScopePoolEndAddress_Type = IpAddress
_FsDhcpScopePoolEndAddress_Object = MibTableColumn
fsDhcpScopePoolEndAddress = _FsDhcpScopePoolEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 7),
    _FsDhcpScopePoolEndAddress_Type()
)
fsDhcpScopePoolEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopePoolEndAddress.setStatus("current")
_FsDhcpScopeDefaultRouterAddress1_Type = IpAddress
_FsDhcpScopeDefaultRouterAddress1_Object = MibTableColumn
fsDhcpScopeDefaultRouterAddress1 = _FsDhcpScopeDefaultRouterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 8),
    _FsDhcpScopeDefaultRouterAddress1_Type()
)
fsDhcpScopeDefaultRouterAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeDefaultRouterAddress1.setStatus("current")
_FsDhcpScopeDefaultRouterAddress2_Type = IpAddress
_FsDhcpScopeDefaultRouterAddress2_Object = MibTableColumn
fsDhcpScopeDefaultRouterAddress2 = _FsDhcpScopeDefaultRouterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 9),
    _FsDhcpScopeDefaultRouterAddress2_Type()
)
fsDhcpScopeDefaultRouterAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeDefaultRouterAddress2.setStatus("current")
_FsDhcpScopeDefaultRouterAddress3_Type = IpAddress
_FsDhcpScopeDefaultRouterAddress3_Object = MibTableColumn
fsDhcpScopeDefaultRouterAddress3 = _FsDhcpScopeDefaultRouterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 10),
    _FsDhcpScopeDefaultRouterAddress3_Type()
)
fsDhcpScopeDefaultRouterAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeDefaultRouterAddress3.setStatus("current")


class _FsDhcpScopeDnsDomainName_Type(DisplayString):
    """Custom type fsDhcpScopeDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsDhcpScopeDnsDomainName_Type.__name__ = "DisplayString"
_FsDhcpScopeDnsDomainName_Object = MibTableColumn
fsDhcpScopeDnsDomainName = _FsDhcpScopeDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 11),
    _FsDhcpScopeDnsDomainName_Type()
)
fsDhcpScopeDnsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeDnsDomainName.setStatus("current")
_FsDhcpScopeDnsServerAddress1_Type = IpAddress
_FsDhcpScopeDnsServerAddress1_Object = MibTableColumn
fsDhcpScopeDnsServerAddress1 = _FsDhcpScopeDnsServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 12),
    _FsDhcpScopeDnsServerAddress1_Type()
)
fsDhcpScopeDnsServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeDnsServerAddress1.setStatus("current")
_FsDhcpScopeDnsServerAddress2_Type = IpAddress
_FsDhcpScopeDnsServerAddress2_Object = MibTableColumn
fsDhcpScopeDnsServerAddress2 = _FsDhcpScopeDnsServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 13),
    _FsDhcpScopeDnsServerAddress2_Type()
)
fsDhcpScopeDnsServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeDnsServerAddress2.setStatus("current")
_FsDhcpScopeDnsServerAddress3_Type = IpAddress
_FsDhcpScopeDnsServerAddress3_Object = MibTableColumn
fsDhcpScopeDnsServerAddress3 = _FsDhcpScopeDnsServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 14),
    _FsDhcpScopeDnsServerAddress3_Type()
)
fsDhcpScopeDnsServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeDnsServerAddress3.setStatus("current")
_FsDhcpScopeNetbiosNameServerAddress1_Type = IpAddress
_FsDhcpScopeNetbiosNameServerAddress1_Object = MibTableColumn
fsDhcpScopeNetbiosNameServerAddress1 = _FsDhcpScopeNetbiosNameServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 15),
    _FsDhcpScopeNetbiosNameServerAddress1_Type()
)
fsDhcpScopeNetbiosNameServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeNetbiosNameServerAddress1.setStatus("current")
_FsDhcpScopeNetbiosNameServerAddress2_Type = IpAddress
_FsDhcpScopeNetbiosNameServerAddress2_Object = MibTableColumn
fsDhcpScopeNetbiosNameServerAddress2 = _FsDhcpScopeNetbiosNameServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 16),
    _FsDhcpScopeNetbiosNameServerAddress2_Type()
)
fsDhcpScopeNetbiosNameServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeNetbiosNameServerAddress2.setStatus("current")
_FsDhcpScopeNetbiosNameServerAddress3_Type = IpAddress
_FsDhcpScopeNetbiosNameServerAddress3_Object = MibTableColumn
fsDhcpScopeNetbiosNameServerAddress3 = _FsDhcpScopeNetbiosNameServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 17),
    _FsDhcpScopeNetbiosNameServerAddress3_Type()
)
fsDhcpScopeNetbiosNameServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeNetbiosNameServerAddress3.setStatus("current")


class _FsDhcpScopeState_Type(Integer32):
    """Custom type fsDhcpScopeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_FsDhcpScopeState_Type.__name__ = "Integer32"
_FsDhcpScopeState_Object = MibTableColumn
fsDhcpScopeState = _FsDhcpScopeState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 18),
    _FsDhcpScopeState_Type()
)
fsDhcpScopeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeState.setStatus("current")
_FsDhcpScopeRowStatus_Type = RowStatus
_FsDhcpScopeRowStatus_Object = MibTableColumn
fsDhcpScopeRowStatus = _FsDhcpScopeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 19),
    _FsDhcpScopeRowStatus_Type()
)
fsDhcpScopeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpScopeRowStatus.setStatus("current")


class _FsDhcpIPPoolUsage_Type(Integer32):
    """Custom type fsDhcpIPPoolUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FsDhcpIPPoolUsage_Type.__name__ = "Integer32"
_FsDhcpIPPoolUsage_Object = MibTableColumn
fsDhcpIPPoolUsage = _FsDhcpIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 20),
    _FsDhcpIPPoolUsage_Type()
)
fsDhcpIPPoolUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpIPPoolUsage.setStatus("current")
_FsDhcpoption43_Type = IpAddress
_FsDhcpoption43_Object = MibTableColumn
fsDhcpoption43 = _FsDhcpoption43_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 21),
    _FsDhcpoption43_Type()
)
fsDhcpoption43.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpoption43.setStatus("current")
_FsDhcpoption138_Type = IpAddress
_FsDhcpoption138_Object = MibTableColumn
fsDhcpoption138 = _FsDhcpoption138_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 22),
    _FsDhcpoption138_Type()
)
fsDhcpoption138.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpoption138.setStatus("current")
_FsDhcpReqtimes_Type = Unsigned32
_FsDhcpReqtimes_Object = MibTableColumn
fsDhcpReqtimes = _FsDhcpReqtimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 23),
    _FsDhcpReqtimes_Type()
)
fsDhcpReqtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpReqtimes.setStatus("current")
_FsDhcpReqSuctimes_Type = Unsigned32
_FsDhcpReqSuctimes_Object = MibTableColumn
fsDhcpReqSuctimes = _FsDhcpReqSuctimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 24),
    _FsDhcpReqSuctimes_Type()
)
fsDhcpReqSuctimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpReqSuctimes.setStatus("current")
_FsDhcpTotalIPNum_Type = Integer32
_FsDhcpTotalIPNum_Object = MibTableColumn
fsDhcpTotalIPNum = _FsDhcpTotalIPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 25),
    _FsDhcpTotalIPNum_Type()
)
fsDhcpTotalIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpTotalIPNum.setStatus("current")
_FsDhcpCurrentUsedIPNum_Type = Integer32
_FsDhcpCurrentUsedIPNum_Object = MibTableColumn
fsDhcpCurrentUsedIPNum = _FsDhcpCurrentUsedIPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 26),
    _FsDhcpCurrentUsedIPNum_Type()
)
fsDhcpCurrentUsedIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpCurrentUsedIPNum.setStatus("current")
_FsDhcpOffertimes_Type = Unsigned32
_FsDhcpOffertimes_Object = MibTableColumn
fsDhcpOffertimes = _FsDhcpOffertimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 27),
    _FsDhcpOffertimes_Type()
)
fsDhcpOffertimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpOffertimes.setStatus("current")
_FsDhcpAcktimes_Type = Unsigned32
_FsDhcpAcktimes_Object = MibTableColumn
fsDhcpAcktimes = _FsDhcpAcktimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 1, 1, 28),
    _FsDhcpAcktimes_Type()
)
fsDhcpAcktimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpAcktimes.setStatus("current")
_FsDhcpServerIpVlanTable_Object = MibTable
fsDhcpServerIpVlanTable = _FsDhcpServerIpVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fsDhcpServerIpVlanTable.setStatus("current")
_FsDhcpServerIpVlanEntry_Object = MibTableRow
fsDhcpServerIpVlanEntry = _FsDhcpServerIpVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 2, 1)
)
fsDhcpServerIpVlanEntry.setIndexNames(
    (0, "FS-CAPWAP-DHCP-MIB", "fsDhcpServerIpVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpServerIpVlanEntry.setStatus("current")


class _FsDhcpServerIpVlanIndex_Type(Unsigned32):
    """Custom type fsDhcpServerIpVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsDhcpServerIpVlanIndex_Type.__name__ = "Unsigned32"
_FsDhcpServerIpVlanIndex_Object = MibTableColumn
fsDhcpServerIpVlanIndex = _FsDhcpServerIpVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 2, 1, 1),
    _FsDhcpServerIpVlanIndex_Type()
)
fsDhcpServerIpVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcpServerIpVlanIndex.setStatus("current")
_FsDhcpServerIpVlanOnlineUserNum_Type = Unsigned32
_FsDhcpServerIpVlanOnlineUserNum_Object = MibTableColumn
fsDhcpServerIpVlanOnlineUserNum = _FsDhcpServerIpVlanOnlineUserNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 3, 2, 1, 2),
    _FsDhcpServerIpVlanOnlineUserNum_Type()
)
fsDhcpServerIpVlanOnlineUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpServerIpVlanOnlineUserNum.setStatus("current")
_FsCapwapDhcpRelayConfig_ObjectIdentity = ObjectIdentity
fsCapwapDhcpRelayConfig = _FsCapwapDhcpRelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4)
)
_FsDhcpGlobalServerAddrTable_Object = MibTable
fsDhcpGlobalServerAddrTable = _FsDhcpGlobalServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsDhcpGlobalServerAddrTable.setStatus("current")
_FsDhcpGlobalServerAddrEntry_Object = MibTableRow
fsDhcpGlobalServerAddrEntry = _FsDhcpGlobalServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 1, 1)
)
fsDhcpGlobalServerAddrEntry.setIndexNames(
    (0, "FS-CAPWAP-DHCP-MIB", "fsDhcpGlobalServerIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpGlobalServerAddrEntry.setStatus("current")


class _FsDhcpGlobalServerIndex_Type(Integer32):
    """Custom type fsDhcpGlobalServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FsDhcpGlobalServerIndex_Type.__name__ = "Integer32"
_FsDhcpGlobalServerIndex_Object = MibTableColumn
fsDhcpGlobalServerIndex = _FsDhcpGlobalServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 1, 1, 1),
    _FsDhcpGlobalServerIndex_Type()
)
fsDhcpGlobalServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcpGlobalServerIndex.setStatus("current")
_FsDhcpGlobalServerAddress_Type = IpAddress
_FsDhcpGlobalServerAddress_Object = MibTableColumn
fsDhcpGlobalServerAddress = _FsDhcpGlobalServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 1, 1, 2),
    _FsDhcpGlobalServerAddress_Type()
)
fsDhcpGlobalServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpGlobalServerAddress.setStatus("current")
_FsDhcpGlobalServerRowStatus_Type = RowStatus
_FsDhcpGlobalServerRowStatus_Object = MibTableColumn
fsDhcpGlobalServerRowStatus = _FsDhcpGlobalServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 1, 1, 3),
    _FsDhcpGlobalServerRowStatus_Type()
)
fsDhcpGlobalServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpGlobalServerRowStatus.setStatus("current")
_FsDhcpIntfServerAddrTable_Object = MibTable
fsDhcpIntfServerAddrTable = _FsDhcpIntfServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 2)
)
if mibBuilder.loadTexts:
    fsDhcpIntfServerAddrTable.setStatus("current")
_FsDhcpIntfServerAddrEntry_Object = MibTableRow
fsDhcpIntfServerAddrEntry = _FsDhcpIntfServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 2, 1)
)
fsDhcpIntfServerAddrEntry.setIndexNames(
    (0, "FS-INTERFACE-MIB", "fsIfIndex"),
    (0, "FS-CAPWAP-DHCP-MIB", "fsDhcpIntfServerIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpIntfServerAddrEntry.setStatus("current")


class _FsDhcpIntfServerIndex_Type(Integer32):
    """Custom type fsDhcpIntfServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_FsDhcpIntfServerIndex_Type.__name__ = "Integer32"
_FsDhcpIntfServerIndex_Object = MibTableColumn
fsDhcpIntfServerIndex = _FsDhcpIntfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 2, 1, 1),
    _FsDhcpIntfServerIndex_Type()
)
fsDhcpIntfServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcpIntfServerIndex.setStatus("current")
_FsDhcpIntfServerAddress_Type = IpAddress
_FsDhcpIntfServerAddress_Object = MibTableColumn
fsDhcpIntfServerAddress = _FsDhcpIntfServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 2, 1, 2),
    _FsDhcpIntfServerAddress_Type()
)
fsDhcpIntfServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpIntfServerAddress.setStatus("current")
_FsDhcpIntfServerRowStatus_Type = RowStatus
_FsDhcpIntfServerRowStatus_Object = MibTableColumn
fsDhcpIntfServerRowStatus = _FsDhcpIntfServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 1, 4, 2, 1, 3),
    _FsDhcpIntfServerRowStatus_Type()
)
fsDhcpIntfServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpIntfServerRowStatus.setStatus("current")
_FsCapwapDhcpMIBConformance_ObjectIdentity = ObjectIdentity
fsCapwapDhcpMIBConformance = _FsCapwapDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2)
)
_FsCapwapDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
fsCapwapDhcpMIBCompliances = _FsCapwapDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2, 1)
)
_FsCapwapDhcpMIBGroups_ObjectIdentity = ObjectIdentity
fsCapwapDhcpMIBGroups = _FsCapwapDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2, 2)
)

# Managed Objects groups

fsCapwapDhcpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2, 2, 1)
)
fsCapwapDhcpMIBGroup.setObjects(
      *(("FS-CAPWAP-DHCP-MIB", "fsLDhcpClearAllStats"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpStartService"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpDiscoverPkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpRequestPkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpDeclinePkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpInformPkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpReleasePkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpReplyPkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpOfferPkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpAckPkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpNakPkts"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpReqTimes"),
        ("FS-CAPWAP-DHCP-MIB", "fsLDhcpReqSucTimes"))
)
if mibBuilder.loadTexts:
    fsCapwapDhcpMIBGroup.setStatus("current")

fsCapwapDhcpServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2, 2, 2)
)
fsCapwapDhcpServerConfigGroup.setObjects(
      *(("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeName"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeLeaseTime"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeNetwork"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeNetmask"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeDefaultRouterAddress1"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeDefaultRouterAddress2"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeDefaultRouterAddress3"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeDnsDomainName"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeDnsServerAddress1"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeDnsServerAddress2"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeDnsServerAddress3"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeNetbiosNameServerAddress1"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeNetbiosNameServerAddress2"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeNetbiosNameServerAddress3"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeState"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeRowStatus"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpIPPoolUsage"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpoption43"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpoption138"))
)
if mibBuilder.loadTexts:
    fsCapwapDhcpServerConfigGroup.setStatus("current")

fsCapwapDhcpRelayGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2, 2, 3)
)
fsCapwapDhcpRelayGlobalConfigGroup.setObjects(
      *(("FS-CAPWAP-DHCP-MIB", "fsDhcpGlobalServerAddress"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpGlobalServerRowStatus"))
)
if mibBuilder.loadTexts:
    fsCapwapDhcpRelayGlobalConfigGroup.setStatus("current")

fsCapwapDhcpRelayIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2, 2, 4)
)
fsCapwapDhcpRelayIntfConfigGroup.setObjects(
      *(("FS-CAPWAP-DHCP-MIB", "fsDhcpIntfServerAddress"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpIntfServerRowStatus"))
)
if mibBuilder.loadTexts:
    fsCapwapDhcpRelayIntfConfigGroup.setStatus("current")


# Notification objects

fsDhcpAddressExhaustTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 0, 1)
)
fsDhcpAddressExhaustTrap.setObjects(
    ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeName")
)
if mibBuilder.loadTexts:
    fsDhcpAddressExhaustTrap.setStatus(
        "current"
    )

fsDhcpAddressExhaustRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 0, 2)
)
fsDhcpAddressExhaustRecovTrap.setObjects(
    ("FS-CAPWAP-DHCP-MIB", "fsDhcpScopeName")
)
if mibBuilder.loadTexts:
    fsDhcpAddressExhaustRecovTrap.setStatus(
        "current"
    )

fsDhcpClientFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 0, 3)
)
fsDhcpClientFailTrap.setObjects(
    ("FS-CAPWAP-DHCP-MIB", "fsDhcpClientMacAddress")
)
if mibBuilder.loadTexts:
    fsDhcpClientFailTrap.setStatus(
        "current"
    )

fsDhcpServerInfoTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 0, 4)
)
fsDhcpServerInfoTrap.setObjects(
      *(("FS-CAPWAP-DHCP-MIB", "fsDhcpServerTlvNum"),
        ("FS-CAPWAP-DHCP-MIB", "fsDhcpServerTlv"))
)
if mibBuilder.loadTexts:
    fsDhcpServerInfoTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsCapwapDhcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 58, 2, 1, 1)
)
fsCapwapDhcpMIBCompliance.setObjects(
      *(("FS-CAPWAP-DHCP-MIB", "fsCapwapDhcpMIBGroup"),
        ("FS-CAPWAP-DHCP-MIB", "fsCapwapDhcpServerConfigGroup"),
        ("FS-CAPWAP-DHCP-MIB", "fsCapwapDhcpRelayGlobalConfigGroup"),
        ("FS-CAPWAP-DHCP-MIB", "fsCapwapDhcpRelayIntfConfigGroup"))
)
if mibBuilder.loadTexts:
    fsCapwapDhcpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CAPWAP-DHCP-MIB",
    **{"fsCapwapDhcpMIB": fsCapwapDhcpMIB,
       "fsCapwapDhcpMIBTrap": fsCapwapDhcpMIBTrap,
       "fsDhcpAddressExhaustTrap": fsDhcpAddressExhaustTrap,
       "fsDhcpAddressExhaustRecovTrap": fsDhcpAddressExhaustRecovTrap,
       "fsDhcpClientFailTrap": fsDhcpClientFailTrap,
       "fsDhcpServerInfoTrap": fsDhcpServerInfoTrap,
       "fsCapwapDhcpMIBObjects": fsCapwapDhcpMIBObjects,
       "fsCapwapDhcpGlobalConfig": fsCapwapDhcpGlobalConfig,
       "fsLDhcpClearAllStats": fsLDhcpClearAllStats,
       "fsLDhcpStartService": fsLDhcpStartService,
       "fsDhcpClientMacAddress": fsDhcpClientMacAddress,
       "fsLDhcpStartTIService": fsLDhcpStartTIService,
       "fsDhcpServerTlvNum": fsDhcpServerTlvNum,
       "fsDhcpServerTlv": fsDhcpServerTlv,
       "fsCapwapDhcpShowStats": fsCapwapDhcpShowStats,
       "fsLDhcpDiscoverPkts": fsLDhcpDiscoverPkts,
       "fsLDhcpRequestPkts": fsLDhcpRequestPkts,
       "fsLDhcpDeclinePkts": fsLDhcpDeclinePkts,
       "fsLDhcpInformPkts": fsLDhcpInformPkts,
       "fsLDhcpReleasePkts": fsLDhcpReleasePkts,
       "fsLDhcpReplyPkts": fsLDhcpReplyPkts,
       "fsLDhcpOfferPkts": fsLDhcpOfferPkts,
       "fsLDhcpAckPkts": fsLDhcpAckPkts,
       "fsLDhcpNakPkts": fsLDhcpNakPkts,
       "fsLDhcpReqTimes": fsLDhcpReqTimes,
       "fsLDhcpReqSucTimes": fsLDhcpReqSucTimes,
       "fsCapwapDhcpServerConfig": fsCapwapDhcpServerConfig,
       "fsDhcpScopeTable": fsDhcpScopeTable,
       "fsDhcpScopeEntry": fsDhcpScopeEntry,
       "fsDhcpScopeIndex": fsDhcpScopeIndex,
       "fsDhcpScopeName": fsDhcpScopeName,
       "fsDhcpScopeLeaseTime": fsDhcpScopeLeaseTime,
       "fsDhcpScopeNetwork": fsDhcpScopeNetwork,
       "fsDhcpScopeNetmask": fsDhcpScopeNetmask,
       "fsDhcpScopePoolStartAddress": fsDhcpScopePoolStartAddress,
       "fsDhcpScopePoolEndAddress": fsDhcpScopePoolEndAddress,
       "fsDhcpScopeDefaultRouterAddress1": fsDhcpScopeDefaultRouterAddress1,
       "fsDhcpScopeDefaultRouterAddress2": fsDhcpScopeDefaultRouterAddress2,
       "fsDhcpScopeDefaultRouterAddress3": fsDhcpScopeDefaultRouterAddress3,
       "fsDhcpScopeDnsDomainName": fsDhcpScopeDnsDomainName,
       "fsDhcpScopeDnsServerAddress1": fsDhcpScopeDnsServerAddress1,
       "fsDhcpScopeDnsServerAddress2": fsDhcpScopeDnsServerAddress2,
       "fsDhcpScopeDnsServerAddress3": fsDhcpScopeDnsServerAddress3,
       "fsDhcpScopeNetbiosNameServerAddress1": fsDhcpScopeNetbiosNameServerAddress1,
       "fsDhcpScopeNetbiosNameServerAddress2": fsDhcpScopeNetbiosNameServerAddress2,
       "fsDhcpScopeNetbiosNameServerAddress3": fsDhcpScopeNetbiosNameServerAddress3,
       "fsDhcpScopeState": fsDhcpScopeState,
       "fsDhcpScopeRowStatus": fsDhcpScopeRowStatus,
       "fsDhcpIPPoolUsage": fsDhcpIPPoolUsage,
       "fsDhcpoption43": fsDhcpoption43,
       "fsDhcpoption138": fsDhcpoption138,
       "fsDhcpReqtimes": fsDhcpReqtimes,
       "fsDhcpReqSuctimes": fsDhcpReqSuctimes,
       "fsDhcpTotalIPNum": fsDhcpTotalIPNum,
       "fsDhcpCurrentUsedIPNum": fsDhcpCurrentUsedIPNum,
       "fsDhcpOffertimes": fsDhcpOffertimes,
       "fsDhcpAcktimes": fsDhcpAcktimes,
       "fsDhcpServerIpVlanTable": fsDhcpServerIpVlanTable,
       "fsDhcpServerIpVlanEntry": fsDhcpServerIpVlanEntry,
       "fsDhcpServerIpVlanIndex": fsDhcpServerIpVlanIndex,
       "fsDhcpServerIpVlanOnlineUserNum": fsDhcpServerIpVlanOnlineUserNum,
       "fsCapwapDhcpRelayConfig": fsCapwapDhcpRelayConfig,
       "fsDhcpGlobalServerAddrTable": fsDhcpGlobalServerAddrTable,
       "fsDhcpGlobalServerAddrEntry": fsDhcpGlobalServerAddrEntry,
       "fsDhcpGlobalServerIndex": fsDhcpGlobalServerIndex,
       "fsDhcpGlobalServerAddress": fsDhcpGlobalServerAddress,
       "fsDhcpGlobalServerRowStatus": fsDhcpGlobalServerRowStatus,
       "fsDhcpIntfServerAddrTable": fsDhcpIntfServerAddrTable,
       "fsDhcpIntfServerAddrEntry": fsDhcpIntfServerAddrEntry,
       "fsDhcpIntfServerIndex": fsDhcpIntfServerIndex,
       "fsDhcpIntfServerAddress": fsDhcpIntfServerAddress,
       "fsDhcpIntfServerRowStatus": fsDhcpIntfServerRowStatus,
       "fsCapwapDhcpMIBConformance": fsCapwapDhcpMIBConformance,
       "fsCapwapDhcpMIBCompliances": fsCapwapDhcpMIBCompliances,
       "fsCapwapDhcpMIBCompliance": fsCapwapDhcpMIBCompliance,
       "fsCapwapDhcpMIBGroups": fsCapwapDhcpMIBGroups,
       "fsCapwapDhcpMIBGroup": fsCapwapDhcpMIBGroup,
       "fsCapwapDhcpServerConfigGroup": fsCapwapDhcpServerConfigGroup,
       "fsCapwapDhcpRelayGlobalConfigGroup": fsCapwapDhcpRelayGlobalConfigGroup,
       "fsCapwapDhcpRelayIntfConfigGroup": fsCapwapDhcpRelayIntfConfigGroup}
)
