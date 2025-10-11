# SNMP MIB module (QTECH-CAPWAP-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CAPWAP-DHCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:14 2025
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

(qtechIfIndex,) = mibBuilder.importSymbols(
    "QTECH-INTERFACE-MIB",
    "qtechIfIndex")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechCapwapDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58)
)
if mibBuilder.loadTexts:
    qtechCapwapDhcpMIB.setRevisions(
        ("2009-11-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechCapwapDhcpMIBTrap_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpMIBTrap = _QtechCapwapDhcpMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 0)
)
_QtechCapwapDhcpMIBObjects_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpMIBObjects = _QtechCapwapDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1)
)
_QtechCapwapDhcpGlobalConfig_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpGlobalConfig = _QtechCapwapDhcpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 1)
)
_QtechLDhcpClearAllStats_Type = TruthValue
_QtechLDhcpClearAllStats_Object = MibScalar
qtechLDhcpClearAllStats = _QtechLDhcpClearAllStats_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 1, 1),
    _QtechLDhcpClearAllStats_Type()
)
qtechLDhcpClearAllStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLDhcpClearAllStats.setStatus("current")


class _QtechLDhcpStartService_Type(Integer32):
    """Custom type qtechLDhcpStartService based on Integer32"""
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


_QtechLDhcpStartService_Type.__name__ = "Integer32"
_QtechLDhcpStartService_Object = MibScalar
qtechLDhcpStartService = _QtechLDhcpStartService_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 1, 2),
    _QtechLDhcpStartService_Type()
)
qtechLDhcpStartService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLDhcpStartService.setStatus("current")
_QtechDhcpClientMacAddress_Type = MacAddress
_QtechDhcpClientMacAddress_Object = MibScalar
qtechDhcpClientMacAddress = _QtechDhcpClientMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 1, 3),
    _QtechDhcpClientMacAddress_Type()
)
qtechDhcpClientMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDhcpClientMacAddress.setStatus("current")


class _QtechLDhcpStartTIService_Type(Integer32):
    """Custom type qtechLDhcpStartTIService based on Integer32"""
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


_QtechLDhcpStartTIService_Type.__name__ = "Integer32"
_QtechLDhcpStartTIService_Object = MibScalar
qtechLDhcpStartTIService = _QtechLDhcpStartTIService_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 1, 4),
    _QtechLDhcpStartTIService_Type()
)
qtechLDhcpStartTIService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechLDhcpStartTIService.setStatus("current")
_QtechCapwapDhcpShowStats_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpShowStats = _QtechCapwapDhcpShowStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2)
)
_QtechLDhcpDiscoverPkts_Type = Unsigned32
_QtechLDhcpDiscoverPkts_Object = MibScalar
qtechLDhcpDiscoverPkts = _QtechLDhcpDiscoverPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 1),
    _QtechLDhcpDiscoverPkts_Type()
)
qtechLDhcpDiscoverPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpDiscoverPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpDiscoverPkts.setUnits("packets")
_QtechLDhcpRequestPkts_Type = Unsigned32
_QtechLDhcpRequestPkts_Object = MibScalar
qtechLDhcpRequestPkts = _QtechLDhcpRequestPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 2),
    _QtechLDhcpRequestPkts_Type()
)
qtechLDhcpRequestPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpRequestPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpRequestPkts.setUnits("packets")
_QtechLDhcpDeclinePkts_Type = Unsigned32
_QtechLDhcpDeclinePkts_Object = MibScalar
qtechLDhcpDeclinePkts = _QtechLDhcpDeclinePkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 3),
    _QtechLDhcpDeclinePkts_Type()
)
qtechLDhcpDeclinePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpDeclinePkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpDeclinePkts.setUnits("packets")
_QtechLDhcpInformPkts_Type = Unsigned32
_QtechLDhcpInformPkts_Object = MibScalar
qtechLDhcpInformPkts = _QtechLDhcpInformPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 4),
    _QtechLDhcpInformPkts_Type()
)
qtechLDhcpInformPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpInformPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpInformPkts.setUnits("packets")
_QtechLDhcpReleasePkts_Type = Unsigned32
_QtechLDhcpReleasePkts_Object = MibScalar
qtechLDhcpReleasePkts = _QtechLDhcpReleasePkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 5),
    _QtechLDhcpReleasePkts_Type()
)
qtechLDhcpReleasePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpReleasePkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpReleasePkts.setUnits("packets")
_QtechLDhcpReplyPkts_Type = Unsigned32
_QtechLDhcpReplyPkts_Object = MibScalar
qtechLDhcpReplyPkts = _QtechLDhcpReplyPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 6),
    _QtechLDhcpReplyPkts_Type()
)
qtechLDhcpReplyPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpReplyPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpReplyPkts.setUnits("packets")
_QtechLDhcpOfferPkts_Type = Unsigned32
_QtechLDhcpOfferPkts_Object = MibScalar
qtechLDhcpOfferPkts = _QtechLDhcpOfferPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 7),
    _QtechLDhcpOfferPkts_Type()
)
qtechLDhcpOfferPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpOfferPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpOfferPkts.setUnits("packets")
_QtechLDhcpAckPkts_Type = Unsigned32
_QtechLDhcpAckPkts_Object = MibScalar
qtechLDhcpAckPkts = _QtechLDhcpAckPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 8),
    _QtechLDhcpAckPkts_Type()
)
qtechLDhcpAckPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpAckPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpAckPkts.setUnits("packets")
_QtechLDhcpNakPkts_Type = Unsigned32
_QtechLDhcpNakPkts_Object = MibScalar
qtechLDhcpNakPkts = _QtechLDhcpNakPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 9),
    _QtechLDhcpNakPkts_Type()
)
qtechLDhcpNakPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpNakPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpNakPkts.setUnits("packets")
_QtechLDhcpReqTimes_Type = Unsigned32
_QtechLDhcpReqTimes_Object = MibScalar
qtechLDhcpReqTimes = _QtechLDhcpReqTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 10),
    _QtechLDhcpReqTimes_Type()
)
qtechLDhcpReqTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpReqTimes.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpReqTimes.setUnits("packets")
_QtechLDhcpReqSucTimes_Type = Unsigned32
_QtechLDhcpReqSucTimes_Object = MibScalar
qtechLDhcpReqSucTimes = _QtechLDhcpReqSucTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 2, 11),
    _QtechLDhcpReqSucTimes_Type()
)
qtechLDhcpReqSucTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechLDhcpReqSucTimes.setStatus("current")
if mibBuilder.loadTexts:
    qtechLDhcpReqSucTimes.setUnits("packets")
_QtechCapwapDhcpServerConfig_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpServerConfig = _QtechCapwapDhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3)
)
_QtechDhcpScopeTable_Object = MibTable
qtechDhcpScopeTable = _QtechDhcpScopeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechDhcpScopeTable.setStatus("current")
_QtechDhcpScopeEntry_Object = MibTableRow
qtechDhcpScopeEntry = _QtechDhcpScopeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1)
)
qtechDhcpScopeEntry.setIndexNames(
    (0, "QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeIndex"),
)
if mibBuilder.loadTexts:
    qtechDhcpScopeEntry.setStatus("current")


class _QtechDhcpScopeIndex_Type(Unsigned32):
    """Custom type qtechDhcpScopeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_QtechDhcpScopeIndex_Type.__name__ = "Unsigned32"
_QtechDhcpScopeIndex_Object = MibTableColumn
qtechDhcpScopeIndex = _QtechDhcpScopeIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 1),
    _QtechDhcpScopeIndex_Type()
)
qtechDhcpScopeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDhcpScopeIndex.setStatus("current")


class _QtechDhcpScopeName_Type(DisplayString):
    """Custom type qtechDhcpScopeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechDhcpScopeName_Type.__name__ = "DisplayString"
_QtechDhcpScopeName_Object = MibTableColumn
qtechDhcpScopeName = _QtechDhcpScopeName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 2),
    _QtechDhcpScopeName_Type()
)
qtechDhcpScopeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeName.setStatus("current")


class _QtechDhcpScopeLeaseTime_Type(Integer32):
    """Custom type qtechDhcpScopeLeaseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 8640000),
    )


_QtechDhcpScopeLeaseTime_Type.__name__ = "Integer32"
_QtechDhcpScopeLeaseTime_Object = MibTableColumn
qtechDhcpScopeLeaseTime = _QtechDhcpScopeLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 3),
    _QtechDhcpScopeLeaseTime_Type()
)
qtechDhcpScopeLeaseTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeLeaseTime.setStatus("current")
_QtechDhcpScopeNetwork_Type = IpAddress
_QtechDhcpScopeNetwork_Object = MibTableColumn
qtechDhcpScopeNetwork = _QtechDhcpScopeNetwork_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 4),
    _QtechDhcpScopeNetwork_Type()
)
qtechDhcpScopeNetwork.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeNetwork.setStatus("current")
_QtechDhcpScopeNetmask_Type = IpAddress
_QtechDhcpScopeNetmask_Object = MibTableColumn
qtechDhcpScopeNetmask = _QtechDhcpScopeNetmask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 5),
    _QtechDhcpScopeNetmask_Type()
)
qtechDhcpScopeNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeNetmask.setStatus("current")
_QtechDhcpScopePoolStartAddress_Type = IpAddress
_QtechDhcpScopePoolStartAddress_Object = MibTableColumn
qtechDhcpScopePoolStartAddress = _QtechDhcpScopePoolStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 6),
    _QtechDhcpScopePoolStartAddress_Type()
)
qtechDhcpScopePoolStartAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopePoolStartAddress.setStatus("current")
_QtechDhcpScopePoolEndAddress_Type = IpAddress
_QtechDhcpScopePoolEndAddress_Object = MibTableColumn
qtechDhcpScopePoolEndAddress = _QtechDhcpScopePoolEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 7),
    _QtechDhcpScopePoolEndAddress_Type()
)
qtechDhcpScopePoolEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopePoolEndAddress.setStatus("current")
_QtechDhcpScopeDefaultRouterAddress1_Type = IpAddress
_QtechDhcpScopeDefaultRouterAddress1_Object = MibTableColumn
qtechDhcpScopeDefaultRouterAddress1 = _QtechDhcpScopeDefaultRouterAddress1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 8),
    _QtechDhcpScopeDefaultRouterAddress1_Type()
)
qtechDhcpScopeDefaultRouterAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeDefaultRouterAddress1.setStatus("current")
_QtechDhcpScopeDefaultRouterAddress2_Type = IpAddress
_QtechDhcpScopeDefaultRouterAddress2_Object = MibTableColumn
qtechDhcpScopeDefaultRouterAddress2 = _QtechDhcpScopeDefaultRouterAddress2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 9),
    _QtechDhcpScopeDefaultRouterAddress2_Type()
)
qtechDhcpScopeDefaultRouterAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeDefaultRouterAddress2.setStatus("current")
_QtechDhcpScopeDefaultRouterAddress3_Type = IpAddress
_QtechDhcpScopeDefaultRouterAddress3_Object = MibTableColumn
qtechDhcpScopeDefaultRouterAddress3 = _QtechDhcpScopeDefaultRouterAddress3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 10),
    _QtechDhcpScopeDefaultRouterAddress3_Type()
)
qtechDhcpScopeDefaultRouterAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeDefaultRouterAddress3.setStatus("current")


class _QtechDhcpScopeDnsDomainName_Type(DisplayString):
    """Custom type qtechDhcpScopeDnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QtechDhcpScopeDnsDomainName_Type.__name__ = "DisplayString"
_QtechDhcpScopeDnsDomainName_Object = MibTableColumn
qtechDhcpScopeDnsDomainName = _QtechDhcpScopeDnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 11),
    _QtechDhcpScopeDnsDomainName_Type()
)
qtechDhcpScopeDnsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeDnsDomainName.setStatus("current")
_QtechDhcpScopeDnsServerAddress1_Type = IpAddress
_QtechDhcpScopeDnsServerAddress1_Object = MibTableColumn
qtechDhcpScopeDnsServerAddress1 = _QtechDhcpScopeDnsServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 12),
    _QtechDhcpScopeDnsServerAddress1_Type()
)
qtechDhcpScopeDnsServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeDnsServerAddress1.setStatus("current")
_QtechDhcpScopeDnsServerAddress2_Type = IpAddress
_QtechDhcpScopeDnsServerAddress2_Object = MibTableColumn
qtechDhcpScopeDnsServerAddress2 = _QtechDhcpScopeDnsServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 13),
    _QtechDhcpScopeDnsServerAddress2_Type()
)
qtechDhcpScopeDnsServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeDnsServerAddress2.setStatus("current")
_QtechDhcpScopeDnsServerAddress3_Type = IpAddress
_QtechDhcpScopeDnsServerAddress3_Object = MibTableColumn
qtechDhcpScopeDnsServerAddress3 = _QtechDhcpScopeDnsServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 14),
    _QtechDhcpScopeDnsServerAddress3_Type()
)
qtechDhcpScopeDnsServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeDnsServerAddress3.setStatus("current")
_QtechDhcpScopeNetbiosNameServerAddress1_Type = IpAddress
_QtechDhcpScopeNetbiosNameServerAddress1_Object = MibTableColumn
qtechDhcpScopeNetbiosNameServerAddress1 = _QtechDhcpScopeNetbiosNameServerAddress1_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 15),
    _QtechDhcpScopeNetbiosNameServerAddress1_Type()
)
qtechDhcpScopeNetbiosNameServerAddress1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeNetbiosNameServerAddress1.setStatus("current")
_QtechDhcpScopeNetbiosNameServerAddress2_Type = IpAddress
_QtechDhcpScopeNetbiosNameServerAddress2_Object = MibTableColumn
qtechDhcpScopeNetbiosNameServerAddress2 = _QtechDhcpScopeNetbiosNameServerAddress2_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 16),
    _QtechDhcpScopeNetbiosNameServerAddress2_Type()
)
qtechDhcpScopeNetbiosNameServerAddress2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeNetbiosNameServerAddress2.setStatus("current")
_QtechDhcpScopeNetbiosNameServerAddress3_Type = IpAddress
_QtechDhcpScopeNetbiosNameServerAddress3_Object = MibTableColumn
qtechDhcpScopeNetbiosNameServerAddress3 = _QtechDhcpScopeNetbiosNameServerAddress3_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 17),
    _QtechDhcpScopeNetbiosNameServerAddress3_Type()
)
qtechDhcpScopeNetbiosNameServerAddress3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeNetbiosNameServerAddress3.setStatus("current")


class _QtechDhcpScopeState_Type(Integer32):
    """Custom type qtechDhcpScopeState based on Integer32"""
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


_QtechDhcpScopeState_Type.__name__ = "Integer32"
_QtechDhcpScopeState_Object = MibTableColumn
qtechDhcpScopeState = _QtechDhcpScopeState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 18),
    _QtechDhcpScopeState_Type()
)
qtechDhcpScopeState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeState.setStatus("current")
_QtechDhcpScopeRowStatus_Type = RowStatus
_QtechDhcpScopeRowStatus_Object = MibTableColumn
qtechDhcpScopeRowStatus = _QtechDhcpScopeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 19),
    _QtechDhcpScopeRowStatus_Type()
)
qtechDhcpScopeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpScopeRowStatus.setStatus("current")


class _QtechDhcpIPPoolUsage_Type(Integer32):
    """Custom type qtechDhcpIPPoolUsage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_QtechDhcpIPPoolUsage_Type.__name__ = "Integer32"
_QtechDhcpIPPoolUsage_Object = MibTableColumn
qtechDhcpIPPoolUsage = _QtechDhcpIPPoolUsage_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 20),
    _QtechDhcpIPPoolUsage_Type()
)
qtechDhcpIPPoolUsage.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpIPPoolUsage.setStatus("current")
_QtechDhcpoption43_Type = IpAddress
_QtechDhcpoption43_Object = MibTableColumn
qtechDhcpoption43 = _QtechDhcpoption43_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 21),
    _QtechDhcpoption43_Type()
)
qtechDhcpoption43.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpoption43.setStatus("current")
_QtechDhcpoption138_Type = IpAddress
_QtechDhcpoption138_Object = MibTableColumn
qtechDhcpoption138 = _QtechDhcpoption138_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 22),
    _QtechDhcpoption138_Type()
)
qtechDhcpoption138.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpoption138.setStatus("current")
_QtechDhcpReqtimes_Type = Unsigned32
_QtechDhcpReqtimes_Object = MibTableColumn
qtechDhcpReqtimes = _QtechDhcpReqtimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 23),
    _QtechDhcpReqtimes_Type()
)
qtechDhcpReqtimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpReqtimes.setStatus("current")
_QtechDhcpReqSuctimes_Type = Unsigned32
_QtechDhcpReqSuctimes_Object = MibTableColumn
qtechDhcpReqSuctimes = _QtechDhcpReqSuctimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 24),
    _QtechDhcpReqSuctimes_Type()
)
qtechDhcpReqSuctimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpReqSuctimes.setStatus("current")
_QtechDhcpTotalIPNum_Type = Integer32
_QtechDhcpTotalIPNum_Object = MibTableColumn
qtechDhcpTotalIPNum = _QtechDhcpTotalIPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 25),
    _QtechDhcpTotalIPNum_Type()
)
qtechDhcpTotalIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpTotalIPNum.setStatus("current")
_QtechDhcpCurrentUsedIPNum_Type = Integer32
_QtechDhcpCurrentUsedIPNum_Object = MibTableColumn
qtechDhcpCurrentUsedIPNum = _QtechDhcpCurrentUsedIPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 3, 1, 1, 26),
    _QtechDhcpCurrentUsedIPNum_Type()
)
qtechDhcpCurrentUsedIPNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpCurrentUsedIPNum.setStatus("current")
_QtechCapwapDhcpRelayConfig_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpRelayConfig = _QtechCapwapDhcpRelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4)
)
_QtechDhcpGlobalServerAddrTable_Object = MibTable
qtechDhcpGlobalServerAddrTable = _QtechDhcpGlobalServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qtechDhcpGlobalServerAddrTable.setStatus("current")
_QtechDhcpGlobalServerAddrEntry_Object = MibTableRow
qtechDhcpGlobalServerAddrEntry = _QtechDhcpGlobalServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 1, 1)
)
qtechDhcpGlobalServerAddrEntry.setIndexNames(
    (0, "QTECH-CAPWAP-DHCP-MIB", "qtechDhcpGlobalServerIndex"),
)
if mibBuilder.loadTexts:
    qtechDhcpGlobalServerAddrEntry.setStatus("current")


class _QtechDhcpGlobalServerIndex_Type(Integer32):
    """Custom type qtechDhcpGlobalServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_QtechDhcpGlobalServerIndex_Type.__name__ = "Integer32"
_QtechDhcpGlobalServerIndex_Object = MibTableColumn
qtechDhcpGlobalServerIndex = _QtechDhcpGlobalServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 1, 1, 1),
    _QtechDhcpGlobalServerIndex_Type()
)
qtechDhcpGlobalServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDhcpGlobalServerIndex.setStatus("current")
_QtechDhcpGlobalServerAddress_Type = IpAddress
_QtechDhcpGlobalServerAddress_Object = MibTableColumn
qtechDhcpGlobalServerAddress = _QtechDhcpGlobalServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 1, 1, 2),
    _QtechDhcpGlobalServerAddress_Type()
)
qtechDhcpGlobalServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpGlobalServerAddress.setStatus("current")
_QtechDhcpGlobalServerRowStatus_Type = RowStatus
_QtechDhcpGlobalServerRowStatus_Object = MibTableColumn
qtechDhcpGlobalServerRowStatus = _QtechDhcpGlobalServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 1, 1, 3),
    _QtechDhcpGlobalServerRowStatus_Type()
)
qtechDhcpGlobalServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpGlobalServerRowStatus.setStatus("current")
_QtechDhcpIntfServerAddrTable_Object = MibTable
qtechDhcpIntfServerAddrTable = _QtechDhcpIntfServerAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 2)
)
if mibBuilder.loadTexts:
    qtechDhcpIntfServerAddrTable.setStatus("current")
_QtechDhcpIntfServerAddrEntry_Object = MibTableRow
qtechDhcpIntfServerAddrEntry = _QtechDhcpIntfServerAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 2, 1)
)
qtechDhcpIntfServerAddrEntry.setIndexNames(
    (0, "QTECH-INTERFACE-MIB", "qtechIfIndex"),
    (0, "QTECH-CAPWAP-DHCP-MIB", "qtechDhcpIntfServerIndex"),
)
if mibBuilder.loadTexts:
    qtechDhcpIntfServerAddrEntry.setStatus("current")


class _QtechDhcpIntfServerIndex_Type(Integer32):
    """Custom type qtechDhcpIntfServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_QtechDhcpIntfServerIndex_Type.__name__ = "Integer32"
_QtechDhcpIntfServerIndex_Object = MibTableColumn
qtechDhcpIntfServerIndex = _QtechDhcpIntfServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 2, 1, 1),
    _QtechDhcpIntfServerIndex_Type()
)
qtechDhcpIntfServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDhcpIntfServerIndex.setStatus("current")
_QtechDhcpIntfServerAddress_Type = IpAddress
_QtechDhcpIntfServerAddress_Object = MibTableColumn
qtechDhcpIntfServerAddress = _QtechDhcpIntfServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 2, 1, 2),
    _QtechDhcpIntfServerAddress_Type()
)
qtechDhcpIntfServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpIntfServerAddress.setStatus("current")
_QtechDhcpIntfServerRowStatus_Type = RowStatus
_QtechDhcpIntfServerRowStatus_Object = MibTableColumn
qtechDhcpIntfServerRowStatus = _QtechDhcpIntfServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 1, 4, 2, 1, 3),
    _QtechDhcpIntfServerRowStatus_Type()
)
qtechDhcpIntfServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpIntfServerRowStatus.setStatus("current")
_QtechCapwapDhcpMIBConformance_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpMIBConformance = _QtechCapwapDhcpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2)
)
_QtechCapwapDhcpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpMIBCompliances = _QtechCapwapDhcpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2, 1)
)
_QtechCapwapDhcpMIBGroups_ObjectIdentity = ObjectIdentity
qtechCapwapDhcpMIBGroups = _QtechCapwapDhcpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2, 2)
)

# Managed Objects groups

qtechCapwapDhcpMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2, 2, 1)
)
qtechCapwapDhcpMIBGroup.setObjects(
      *(("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpClearAllStats"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpStartService"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpDiscoverPkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpRequestPkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpDeclinePkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpInformPkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpReleasePkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpReplyPkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpOfferPkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpAckPkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpNakPkts"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpReqTimes"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechLDhcpReqSucTimes"))
)
if mibBuilder.loadTexts:
    qtechCapwapDhcpMIBGroup.setStatus("current")

qtechCapwapDhcpServerConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2, 2, 2)
)
qtechCapwapDhcpServerConfigGroup.setObjects(
      *(("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeName"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeLeaseTime"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeNetwork"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeNetmask"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeDefaultRouterAddress1"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeDefaultRouterAddress2"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeDefaultRouterAddress3"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeDnsDomainName"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeDnsServerAddress1"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeDnsServerAddress2"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeDnsServerAddress3"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeNetbiosNameServerAddress1"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeNetbiosNameServerAddress2"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeNetbiosNameServerAddress3"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeState"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeRowStatus"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpIPPoolUsage"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpoption43"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpoption138"))
)
if mibBuilder.loadTexts:
    qtechCapwapDhcpServerConfigGroup.setStatus("current")

qtechCapwapDhcpRelayGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2, 2, 3)
)
qtechCapwapDhcpRelayGlobalConfigGroup.setObjects(
      *(("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpGlobalServerAddress"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpGlobalServerRowStatus"))
)
if mibBuilder.loadTexts:
    qtechCapwapDhcpRelayGlobalConfigGroup.setStatus("current")

qtechCapwapDhcpRelayIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2, 2, 4)
)
qtechCapwapDhcpRelayIntfConfigGroup.setObjects(
      *(("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpIntfServerAddress"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpIntfServerRowStatus"))
)
if mibBuilder.loadTexts:
    qtechCapwapDhcpRelayIntfConfigGroup.setStatus("current")


# Notification objects

qtechDhcpAddressExhaustTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 0, 1)
)
qtechDhcpAddressExhaustTrap.setObjects(
    ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeName")
)
if mibBuilder.loadTexts:
    qtechDhcpAddressExhaustTrap.setStatus(
        "current"
    )

qtechDhcpAddressExhaustRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 0, 2)
)
qtechDhcpAddressExhaustRecovTrap.setObjects(
    ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpScopeName")
)
if mibBuilder.loadTexts:
    qtechDhcpAddressExhaustRecovTrap.setStatus(
        "current"
    )

qtechDhcpClientFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 0, 3)
)
qtechDhcpClientFailTrap.setObjects(
    ("QTECH-CAPWAP-DHCP-MIB", "qtechDhcpClientMacAddress")
)
if mibBuilder.loadTexts:
    qtechDhcpClientFailTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechCapwapDhcpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 58, 2, 1, 1)
)
qtechCapwapDhcpMIBCompliance.setObjects(
      *(("QTECH-CAPWAP-DHCP-MIB", "qtechCapwapDhcpMIBGroup"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechCapwapDhcpServerConfigGroup"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechCapwapDhcpRelayGlobalConfigGroup"),
        ("QTECH-CAPWAP-DHCP-MIB", "qtechCapwapDhcpRelayIntfConfigGroup"))
)
if mibBuilder.loadTexts:
    qtechCapwapDhcpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CAPWAP-DHCP-MIB",
    **{"qtechCapwapDhcpMIB": qtechCapwapDhcpMIB,
       "qtechCapwapDhcpMIBTrap": qtechCapwapDhcpMIBTrap,
       "qtechDhcpAddressExhaustTrap": qtechDhcpAddressExhaustTrap,
       "qtechDhcpAddressExhaustRecovTrap": qtechDhcpAddressExhaustRecovTrap,
       "qtechDhcpClientFailTrap": qtechDhcpClientFailTrap,
       "qtechCapwapDhcpMIBObjects": qtechCapwapDhcpMIBObjects,
       "qtechCapwapDhcpGlobalConfig": qtechCapwapDhcpGlobalConfig,
       "qtechLDhcpClearAllStats": qtechLDhcpClearAllStats,
       "qtechLDhcpStartService": qtechLDhcpStartService,
       "qtechDhcpClientMacAddress": qtechDhcpClientMacAddress,
       "qtechLDhcpStartTIService": qtechLDhcpStartTIService,
       "qtechCapwapDhcpShowStats": qtechCapwapDhcpShowStats,
       "qtechLDhcpDiscoverPkts": qtechLDhcpDiscoverPkts,
       "qtechLDhcpRequestPkts": qtechLDhcpRequestPkts,
       "qtechLDhcpDeclinePkts": qtechLDhcpDeclinePkts,
       "qtechLDhcpInformPkts": qtechLDhcpInformPkts,
       "qtechLDhcpReleasePkts": qtechLDhcpReleasePkts,
       "qtechLDhcpReplyPkts": qtechLDhcpReplyPkts,
       "qtechLDhcpOfferPkts": qtechLDhcpOfferPkts,
       "qtechLDhcpAckPkts": qtechLDhcpAckPkts,
       "qtechLDhcpNakPkts": qtechLDhcpNakPkts,
       "qtechLDhcpReqTimes": qtechLDhcpReqTimes,
       "qtechLDhcpReqSucTimes": qtechLDhcpReqSucTimes,
       "qtechCapwapDhcpServerConfig": qtechCapwapDhcpServerConfig,
       "qtechDhcpScopeTable": qtechDhcpScopeTable,
       "qtechDhcpScopeEntry": qtechDhcpScopeEntry,
       "qtechDhcpScopeIndex": qtechDhcpScopeIndex,
       "qtechDhcpScopeName": qtechDhcpScopeName,
       "qtechDhcpScopeLeaseTime": qtechDhcpScopeLeaseTime,
       "qtechDhcpScopeNetwork": qtechDhcpScopeNetwork,
       "qtechDhcpScopeNetmask": qtechDhcpScopeNetmask,
       "qtechDhcpScopePoolStartAddress": qtechDhcpScopePoolStartAddress,
       "qtechDhcpScopePoolEndAddress": qtechDhcpScopePoolEndAddress,
       "qtechDhcpScopeDefaultRouterAddress1": qtechDhcpScopeDefaultRouterAddress1,
       "qtechDhcpScopeDefaultRouterAddress2": qtechDhcpScopeDefaultRouterAddress2,
       "qtechDhcpScopeDefaultRouterAddress3": qtechDhcpScopeDefaultRouterAddress3,
       "qtechDhcpScopeDnsDomainName": qtechDhcpScopeDnsDomainName,
       "qtechDhcpScopeDnsServerAddress1": qtechDhcpScopeDnsServerAddress1,
       "qtechDhcpScopeDnsServerAddress2": qtechDhcpScopeDnsServerAddress2,
       "qtechDhcpScopeDnsServerAddress3": qtechDhcpScopeDnsServerAddress3,
       "qtechDhcpScopeNetbiosNameServerAddress1": qtechDhcpScopeNetbiosNameServerAddress1,
       "qtechDhcpScopeNetbiosNameServerAddress2": qtechDhcpScopeNetbiosNameServerAddress2,
       "qtechDhcpScopeNetbiosNameServerAddress3": qtechDhcpScopeNetbiosNameServerAddress3,
       "qtechDhcpScopeState": qtechDhcpScopeState,
       "qtechDhcpScopeRowStatus": qtechDhcpScopeRowStatus,
       "qtechDhcpIPPoolUsage": qtechDhcpIPPoolUsage,
       "qtechDhcpoption43": qtechDhcpoption43,
       "qtechDhcpoption138": qtechDhcpoption138,
       "qtechDhcpReqtimes": qtechDhcpReqtimes,
       "qtechDhcpReqSuctimes": qtechDhcpReqSuctimes,
       "qtechDhcpTotalIPNum": qtechDhcpTotalIPNum,
       "qtechDhcpCurrentUsedIPNum": qtechDhcpCurrentUsedIPNum,
       "qtechCapwapDhcpRelayConfig": qtechCapwapDhcpRelayConfig,
       "qtechDhcpGlobalServerAddrTable": qtechDhcpGlobalServerAddrTable,
       "qtechDhcpGlobalServerAddrEntry": qtechDhcpGlobalServerAddrEntry,
       "qtechDhcpGlobalServerIndex": qtechDhcpGlobalServerIndex,
       "qtechDhcpGlobalServerAddress": qtechDhcpGlobalServerAddress,
       "qtechDhcpGlobalServerRowStatus": qtechDhcpGlobalServerRowStatus,
       "qtechDhcpIntfServerAddrTable": qtechDhcpIntfServerAddrTable,
       "qtechDhcpIntfServerAddrEntry": qtechDhcpIntfServerAddrEntry,
       "qtechDhcpIntfServerIndex": qtechDhcpIntfServerIndex,
       "qtechDhcpIntfServerAddress": qtechDhcpIntfServerAddress,
       "qtechDhcpIntfServerRowStatus": qtechDhcpIntfServerRowStatus,
       "qtechCapwapDhcpMIBConformance": qtechCapwapDhcpMIBConformance,
       "qtechCapwapDhcpMIBCompliances": qtechCapwapDhcpMIBCompliances,
       "qtechCapwapDhcpMIBCompliance": qtechCapwapDhcpMIBCompliance,
       "qtechCapwapDhcpMIBGroups": qtechCapwapDhcpMIBGroups,
       "qtechCapwapDhcpMIBGroup": qtechCapwapDhcpMIBGroup,
       "qtechCapwapDhcpServerConfigGroup": qtechCapwapDhcpServerConfigGroup,
       "qtechCapwapDhcpRelayGlobalConfigGroup": qtechCapwapDhcpRelayGlobalConfigGroup,
       "qtechCapwapDhcpRelayIntfConfigGroup": qtechCapwapDhcpRelayIntfConfigGroup}
)
