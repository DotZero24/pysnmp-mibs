# SNMP MIB module (FS-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:48 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

fsDhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42)
)
if mibBuilder.loadTexts:
    fsDhcpSnoopingMIB.setRevisions(
        ("2007-10-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDhcpSnoopingMIBTraps_ObjectIdentity = ObjectIdentity
fsDhcpSnoopingMIBTraps = _FsDhcpSnoopingMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 0)
)
_FsDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
fsDhcpSnoopingMIBObjects = _FsDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1)
)
_FsSNDhcpGlobal_ObjectIdentity = ObjectIdentity
fsSNDhcpGlobal = _FsSNDhcpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 1)
)
_FsSNDhcpFeatureEnable_Type = TruthValue
_FsSNDhcpFeatureEnable_Object = MibScalar
fsSNDhcpFeatureEnable = _FsSNDhcpFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 1, 1),
    _FsSNDhcpFeatureEnable_Type()
)
fsSNDhcpFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNDhcpFeatureEnable.setStatus("current")
_FsSNDhcpDatabaseUpdateInterval_Type = Unsigned32
_FsSNDhcpDatabaseUpdateInterval_Object = MibScalar
fsSNDhcpDatabaseUpdateInterval = _FsSNDhcpDatabaseUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 1, 2),
    _FsSNDhcpDatabaseUpdateInterval_Type()
)
fsSNDhcpDatabaseUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNDhcpDatabaseUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsSNDhcpDatabaseUpdateInterval.setUnits("seconds")
_FsSNDhcpRelayAgentInfoOptEnable_Type = TruthValue
_FsSNDhcpRelayAgentInfoOptEnable_Object = MibScalar
fsSNDhcpRelayAgentInfoOptEnable = _FsSNDhcpRelayAgentInfoOptEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 1, 3),
    _FsSNDhcpRelayAgentInfoOptEnable_Type()
)
fsSNDhcpRelayAgentInfoOptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNDhcpRelayAgentInfoOptEnable.setStatus("current")
_FsSNDhcpMatchMacAddressEnable_Type = TruthValue
_FsSNDhcpMatchMacAddressEnable_Object = MibScalar
fsSNDhcpMatchMacAddressEnable = _FsSNDhcpMatchMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 1, 4),
    _FsSNDhcpMatchMacAddressEnable_Type()
)
fsSNDhcpMatchMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNDhcpMatchMacAddressEnable.setStatus("current")
_FsSNDhcpInterface_ObjectIdentity = ObjectIdentity
fsSNDhcpInterface = _FsSNDhcpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2)
)
_FsSNDhcpIfTrustTable_Object = MibTable
fsSNDhcpIfTrustTable = _FsSNDhcpIfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsSNDhcpIfTrustTable.setStatus("current")
_FsSNDhcpIfTrustEntry_Object = MibTableRow
fsSNDhcpIfTrustEntry = _FsSNDhcpIfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 1, 1)
)
fsSNDhcpIfTrustEntry.setIndexNames(
    (0, "FS-DHCP-SNOOPING-MIB", "fsSNDhcpIfTrustIndex"),
)
if mibBuilder.loadTexts:
    fsSNDhcpIfTrustEntry.setStatus("current")
_FsSNDhcpIfTrustIndex_Type = InterfaceIndex
_FsSNDhcpIfTrustIndex_Object = MibTableColumn
fsSNDhcpIfTrustIndex = _FsSNDhcpIfTrustIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 1, 1, 1),
    _FsSNDhcpIfTrustIndex_Type()
)
fsSNDhcpIfTrustIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSNDhcpIfTrustIndex.setStatus("current")
_FsSNDhcpIfTrustEnable_Type = TruthValue
_FsSNDhcpIfTrustEnable_Object = MibTableColumn
fsSNDhcpIfTrustEnable = _FsSNDhcpIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 1, 1, 2),
    _FsSNDhcpIfTrustEnable_Type()
)
fsSNDhcpIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNDhcpIfTrustEnable.setStatus("current")
_FsSNDhcpIfSuppressionTable_Object = MibTable
fsSNDhcpIfSuppressionTable = _FsSNDhcpIfSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsSNDhcpIfSuppressionTable.setStatus("current")
_FsSNDhcpIfSuppressionEntry_Object = MibTableRow
fsSNDhcpIfSuppressionEntry = _FsSNDhcpIfSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 2, 1)
)
fsSNDhcpIfSuppressionEntry.setIndexNames(
    (0, "FS-DHCP-SNOOPING-MIB", "fsSNDhcpIfSuppressionIndex"),
)
if mibBuilder.loadTexts:
    fsSNDhcpIfSuppressionEntry.setStatus("current")
_FsSNDhcpIfSuppressionIndex_Type = InterfaceIndex
_FsSNDhcpIfSuppressionIndex_Object = MibTableColumn
fsSNDhcpIfSuppressionIndex = _FsSNDhcpIfSuppressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 2, 1, 1),
    _FsSNDhcpIfSuppressionIndex_Type()
)
fsSNDhcpIfSuppressionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSNDhcpIfSuppressionIndex.setStatus("current")
_FsSNDhcpIfSuppressionEnable_Type = TruthValue
_FsSNDhcpIfSuppressionEnable_Object = MibTableColumn
fsSNDhcpIfSuppressionEnable = _FsSNDhcpIfSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 2, 1, 2),
    _FsSNDhcpIfSuppressionEnable_Type()
)
fsSNDhcpIfSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNDhcpIfSuppressionEnable.setStatus("current")
_FsSNDhcpAddressBindTable_Object = MibTable
fsSNDhcpAddressBindTable = _FsSNDhcpAddressBindTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsSNDhcpAddressBindTable.setStatus("current")
_FsSNDhcpAddressBindEntry_Object = MibTableRow
fsSNDhcpAddressBindEntry = _FsSNDhcpAddressBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 3, 1)
)
fsSNDhcpAddressBindEntry.setIndexNames(
    (0, "FS-DHCP-SNOOPING-MIB", "fsSNDhcpAddressBindIndex"),
)
if mibBuilder.loadTexts:
    fsSNDhcpAddressBindEntry.setStatus("current")
_FsSNDhcpAddressBindIndex_Type = InterfaceIndex
_FsSNDhcpAddressBindIndex_Object = MibTableColumn
fsSNDhcpAddressBindIndex = _FsSNDhcpAddressBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 3, 1, 1),
    _FsSNDhcpAddressBindIndex_Type()
)
fsSNDhcpAddressBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSNDhcpAddressBindIndex.setStatus("current")
_FsSNDhcpAddressBindEnable_Type = TruthValue
_FsSNDhcpAddressBindEnable_Object = MibTableColumn
fsSNDhcpAddressBindEnable = _FsSNDhcpAddressBindEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 3, 1, 2),
    _FsSNDhcpAddressBindEnable_Type()
)
fsSNDhcpAddressBindEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNDhcpAddressBindEnable.setStatus("current")
_FsDhcpSnpFalsePktStatisticTable_Object = MibTable
fsDhcpSnpFalsePktStatisticTable = _FsDhcpSnpFalsePktStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsDhcpSnpFalsePktStatisticTable.setStatus("current")
_FsDhcpSnpFalsePktStatisticEntry_Object = MibTableRow
fsDhcpSnpFalsePktStatisticEntry = _FsDhcpSnpFalsePktStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1)
)
fsDhcpSnpFalsePktStatisticEntry.setIndexNames(
    (0, "FS-DHCP-SNOOPING-MIB", "fsDhcpSnpStatisticIfIndex"),
    (0, "FS-DHCP-SNOOPING-MIB", "fsDhcpSnpStatisticVlanIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpSnpFalsePktStatisticEntry.setStatus("current")
_FsDhcpSnpStatisticIfIndex_Type = InterfaceIndex
_FsDhcpSnpStatisticIfIndex_Object = MibTableColumn
fsDhcpSnpStatisticIfIndex = _FsDhcpSnpStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 1),
    _FsDhcpSnpStatisticIfIndex_Type()
)
fsDhcpSnpStatisticIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcpSnpStatisticIfIndex.setStatus("current")
_FsDhcpSnpStatisticVlanIndex_Type = VlanIndex
_FsDhcpSnpStatisticVlanIndex_Object = MibTableColumn
fsDhcpSnpStatisticVlanIndex = _FsDhcpSnpStatisticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 2),
    _FsDhcpSnpStatisticVlanIndex_Type()
)
fsDhcpSnpStatisticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsDhcpSnpStatisticVlanIndex.setStatus("current")


class _FsDhcpSnpStatisticIfDescr_Type(DisplayString):
    """Custom type fsDhcpSnpStatisticIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsDhcpSnpStatisticIfDescr_Type.__name__ = "DisplayString"
_FsDhcpSnpStatisticIfDescr_Object = MibTableColumn
fsDhcpSnpStatisticIfDescr = _FsDhcpSnpStatisticIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 3),
    _FsDhcpSnpStatisticIfDescr_Type()
)
fsDhcpSnpStatisticIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpStatisticIfDescr.setStatus("current")
_FsDhcpSnpStatisticVlanId_Type = VlanIndex
_FsDhcpSnpStatisticVlanId_Object = MibTableColumn
fsDhcpSnpStatisticVlanId = _FsDhcpSnpStatisticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 4),
    _FsDhcpSnpStatisticVlanId_Type()
)
fsDhcpSnpStatisticVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpSnpStatisticVlanId.setStatus("current")
_FsChaddrNomatchSrcMacDhcpPktNum_Type = Counter32
_FsChaddrNomatchSrcMacDhcpPktNum_Object = MibTableColumn
fsChaddrNomatchSrcMacDhcpPktNum = _FsChaddrNomatchSrcMacDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 5),
    _FsChaddrNomatchSrcMacDhcpPktNum_Type()
)
fsChaddrNomatchSrcMacDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsChaddrNomatchSrcMacDhcpPktNum.setStatus("current")
_FsArpNomatchSnpBindTblPktNum_Type = Counter32
_FsArpNomatchSnpBindTblPktNum_Object = MibTableColumn
fsArpNomatchSnpBindTblPktNum = _FsArpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 6),
    _FsArpNomatchSnpBindTblPktNum_Type()
)
fsArpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsArpNomatchSnpBindTblPktNum.setStatus("current")
_FsIpNomatchSnpBindTblPktNum_Type = Counter32
_FsIpNomatchSnpBindTblPktNum_Object = MibTableColumn
fsIpNomatchSnpBindTblPktNum = _FsIpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 7),
    _FsIpNomatchSnpBindTblPktNum_Type()
)
fsIpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpNomatchSnpBindTblPktNum.setStatus("current")
_FsNomatchSnpBindTblDhcpPktNum_Type = Counter32
_FsNomatchSnpBindTblDhcpPktNum_Object = MibTableColumn
fsNomatchSnpBindTblDhcpPktNum = _FsNomatchSnpBindTblDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 8),
    _FsNomatchSnpBindTblDhcpPktNum_Type()
)
fsNomatchSnpBindTblDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNomatchSnpBindTblDhcpPktNum.setStatus("current")
_FsUntrustedReplyPktNum_Type = Counter32
_FsUntrustedReplyPktNum_Object = MibTableColumn
fsUntrustedReplyPktNum = _FsUntrustedReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 9),
    _FsUntrustedReplyPktNum_Type()
)
fsUntrustedReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUntrustedReplyPktNum.setStatus("current")
_FsDhcpPktIfRateDiscardNum_Type = Counter32
_FsDhcpPktIfRateDiscardNum_Object = MibTableColumn
fsDhcpPktIfRateDiscardNum = _FsDhcpPktIfRateDiscardNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 2, 4, 1, 10),
    _FsDhcpPktIfRateDiscardNum_Type()
)
fsDhcpPktIfRateDiscardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpPktIfRateDiscardNum.setStatus("current")
_FsSNDhcpBindings_ObjectIdentity = ObjectIdentity
fsSNDhcpBindings = _FsSNDhcpBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3)
)
_FsSNDhcpBindingsTable_Object = MibTable
fsSNDhcpBindingsTable = _FsSNDhcpBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsSNDhcpBindingsTable.setStatus("current")
_FsSNDhcpBindingsEntry_Object = MibTableRow
fsSNDhcpBindingsEntry = _FsSNDhcpBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1)
)
fsSNDhcpBindingsEntry.setIndexNames(
    (0, "FS-DHCP-SNOOPING-MIB", "fsSNDhcpBindingsVlan"),
    (0, "FS-DHCP-SNOOPING-MIB", "fsSNDhcpBindingsMacAddress"),
    (0, "FS-DHCP-SNOOPING-MIB", "fsSNDhcpBindingsAddrType"),
)
if mibBuilder.loadTexts:
    fsSNDhcpBindingsEntry.setStatus("current")
_FsSNDhcpBindingsVlan_Type = VlanIndex
_FsSNDhcpBindingsVlan_Object = MibTableColumn
fsSNDhcpBindingsVlan = _FsSNDhcpBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1, 1),
    _FsSNDhcpBindingsVlan_Type()
)
fsSNDhcpBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsVlan.setStatus("current")
_FsSNDhcpBindingsMacAddress_Type = MacAddress
_FsSNDhcpBindingsMacAddress_Object = MibTableColumn
fsSNDhcpBindingsMacAddress = _FsSNDhcpBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1, 2),
    _FsSNDhcpBindingsMacAddress_Type()
)
fsSNDhcpBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsMacAddress.setStatus("current")


class _FsSNDhcpBindingsAddrType_Type(Integer32):
    """Custom type fsSNDhcpBindingsAddrType based on Integer32"""
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


_FsSNDhcpBindingsAddrType_Type.__name__ = "Integer32"
_FsSNDhcpBindingsAddrType_Object = MibTableColumn
fsSNDhcpBindingsAddrType = _FsSNDhcpBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1, 3),
    _FsSNDhcpBindingsAddrType_Type()
)
fsSNDhcpBindingsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsAddrType.setStatus("current")
_FsSNDhcpBindingsIpAddress_Type = IpAddress
_FsSNDhcpBindingsIpAddress_Object = MibTableColumn
fsSNDhcpBindingsIpAddress = _FsSNDhcpBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1, 4),
    _FsSNDhcpBindingsIpAddress_Type()
)
fsSNDhcpBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsIpAddress.setStatus("current")
_FsSNDhcpBindingsInterface_Type = InterfaceIndex
_FsSNDhcpBindingsInterface_Object = MibTableColumn
fsSNDhcpBindingsInterface = _FsSNDhcpBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1, 5),
    _FsSNDhcpBindingsInterface_Type()
)
fsSNDhcpBindingsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsInterface.setStatus("current")
_FsSNDhcpBindingsLeasedTime_Type = Unsigned32
_FsSNDhcpBindingsLeasedTime_Object = MibTableColumn
fsSNDhcpBindingsLeasedTime = _FsSNDhcpBindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1, 6),
    _FsSNDhcpBindingsLeasedTime_Type()
)
fsSNDhcpBindingsLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsLeasedTime.setUnits("seconds")
_FsSNDhcpBindingsStatus_Type = RowStatus
_FsSNDhcpBindingsStatus_Object = MibTableColumn
fsSNDhcpBindingsStatus = _FsSNDhcpBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 3, 1, 1, 7),
    _FsSNDhcpBindingsStatus_Type()
)
fsSNDhcpBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSNDhcpBindingsStatus.setStatus("current")
_FsDhcpTrapMacAddress_Type = MacAddress
_FsDhcpTrapMacAddress_Object = MibScalar
fsDhcpTrapMacAddress = _FsDhcpTrapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 1, 4),
    _FsDhcpTrapMacAddress_Type()
)
fsDhcpTrapMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsDhcpTrapMacAddress.setStatus("current")
_FsDhcpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
fsDhcpSnoopingMIBConformance = _FsDhcpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 2)
)
_FsDhcpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
fsDhcpSnoopingMIBCompliances = _FsDhcpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 2, 1)
)
_FsDhcpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
fsDhcpSnoopingMIBGroups = _FsDhcpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 2, 2)
)

# Managed Objects groups

fsDhcpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 2, 2, 1)
)
fsDhcpSnoopingMIBGroup.setObjects(
      *(("FS-DHCP-SNOOPING-MIB", "fsSNDhcpFeatureEnable"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpDatabaseUpdateInterval"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpRelayAgentInfoOptEnable"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpMatchMacAddressEnable"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpIfTrustEnable"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpIfSuppressionEnable"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpAddressBindEnable"),
        ("FS-DHCP-SNOOPING-MIB", "fsDhcpSnpStatisticIfDescr"),
        ("FS-DHCP-SNOOPING-MIB", "fsDhcpSnpStatisticVlanId"),
        ("FS-DHCP-SNOOPING-MIB", "fsChaddrNomatchSrcMacDhcpPktNum"),
        ("FS-DHCP-SNOOPING-MIB", "fsArpNomatchSnpBindTblPktNum"),
        ("FS-DHCP-SNOOPING-MIB", "fsIpNomatchSnpBindTblPktNum"),
        ("FS-DHCP-SNOOPING-MIB", "fsNomatchSnpBindTblDhcpPktNum"),
        ("FS-DHCP-SNOOPING-MIB", "fsUntrustedReplyPktNum"),
        ("FS-DHCP-SNOOPING-MIB", "fsDhcpPktIfRateDiscardNum"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpBindingsIpAddress"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpBindingsInterface"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpBindingsLeasedTime"),
        ("FS-DHCP-SNOOPING-MIB", "fsSNDhcpBindingsStatus"),
        ("FS-DHCP-SNOOPING-MIB", "fsDhcpTrapMacAddress"))
)
if mibBuilder.loadTexts:
    fsDhcpSnoopingMIBGroup.setStatus("current")


# Notification objects

fsDhcpSnoopingNoResponseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 0, 1)
)
fsDhcpSnoopingNoResponseTrap.setObjects(
    ("FS-DHCP-SNOOPING-MIB", "fsDhcpTrapMacAddress")
)
if mibBuilder.loadTexts:
    fsDhcpSnoopingNoResponseTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsDhcpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 42, 2, 1, 1)
)
fsDhcpSnoopingMIBCompliance.setObjects(
    ("FS-DHCP-SNOOPING-MIB", "fsDhcpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    fsDhcpSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-DHCP-SNOOPING-MIB",
    **{"fsDhcpSnoopingMIB": fsDhcpSnoopingMIB,
       "fsDhcpSnoopingMIBTraps": fsDhcpSnoopingMIBTraps,
       "fsDhcpSnoopingNoResponseTrap": fsDhcpSnoopingNoResponseTrap,
       "fsDhcpSnoopingMIBObjects": fsDhcpSnoopingMIBObjects,
       "fsSNDhcpGlobal": fsSNDhcpGlobal,
       "fsSNDhcpFeatureEnable": fsSNDhcpFeatureEnable,
       "fsSNDhcpDatabaseUpdateInterval": fsSNDhcpDatabaseUpdateInterval,
       "fsSNDhcpRelayAgentInfoOptEnable": fsSNDhcpRelayAgentInfoOptEnable,
       "fsSNDhcpMatchMacAddressEnable": fsSNDhcpMatchMacAddressEnable,
       "fsSNDhcpInterface": fsSNDhcpInterface,
       "fsSNDhcpIfTrustTable": fsSNDhcpIfTrustTable,
       "fsSNDhcpIfTrustEntry": fsSNDhcpIfTrustEntry,
       "fsSNDhcpIfTrustIndex": fsSNDhcpIfTrustIndex,
       "fsSNDhcpIfTrustEnable": fsSNDhcpIfTrustEnable,
       "fsSNDhcpIfSuppressionTable": fsSNDhcpIfSuppressionTable,
       "fsSNDhcpIfSuppressionEntry": fsSNDhcpIfSuppressionEntry,
       "fsSNDhcpIfSuppressionIndex": fsSNDhcpIfSuppressionIndex,
       "fsSNDhcpIfSuppressionEnable": fsSNDhcpIfSuppressionEnable,
       "fsSNDhcpAddressBindTable": fsSNDhcpAddressBindTable,
       "fsSNDhcpAddressBindEntry": fsSNDhcpAddressBindEntry,
       "fsSNDhcpAddressBindIndex": fsSNDhcpAddressBindIndex,
       "fsSNDhcpAddressBindEnable": fsSNDhcpAddressBindEnable,
       "fsDhcpSnpFalsePktStatisticTable": fsDhcpSnpFalsePktStatisticTable,
       "fsDhcpSnpFalsePktStatisticEntry": fsDhcpSnpFalsePktStatisticEntry,
       "fsDhcpSnpStatisticIfIndex": fsDhcpSnpStatisticIfIndex,
       "fsDhcpSnpStatisticVlanIndex": fsDhcpSnpStatisticVlanIndex,
       "fsDhcpSnpStatisticIfDescr": fsDhcpSnpStatisticIfDescr,
       "fsDhcpSnpStatisticVlanId": fsDhcpSnpStatisticVlanId,
       "fsChaddrNomatchSrcMacDhcpPktNum": fsChaddrNomatchSrcMacDhcpPktNum,
       "fsArpNomatchSnpBindTblPktNum": fsArpNomatchSnpBindTblPktNum,
       "fsIpNomatchSnpBindTblPktNum": fsIpNomatchSnpBindTblPktNum,
       "fsNomatchSnpBindTblDhcpPktNum": fsNomatchSnpBindTblDhcpPktNum,
       "fsUntrustedReplyPktNum": fsUntrustedReplyPktNum,
       "fsDhcpPktIfRateDiscardNum": fsDhcpPktIfRateDiscardNum,
       "fsSNDhcpBindings": fsSNDhcpBindings,
       "fsSNDhcpBindingsTable": fsSNDhcpBindingsTable,
       "fsSNDhcpBindingsEntry": fsSNDhcpBindingsEntry,
       "fsSNDhcpBindingsVlan": fsSNDhcpBindingsVlan,
       "fsSNDhcpBindingsMacAddress": fsSNDhcpBindingsMacAddress,
       "fsSNDhcpBindingsAddrType": fsSNDhcpBindingsAddrType,
       "fsSNDhcpBindingsIpAddress": fsSNDhcpBindingsIpAddress,
       "fsSNDhcpBindingsInterface": fsSNDhcpBindingsInterface,
       "fsSNDhcpBindingsLeasedTime": fsSNDhcpBindingsLeasedTime,
       "fsSNDhcpBindingsStatus": fsSNDhcpBindingsStatus,
       "fsDhcpTrapMacAddress": fsDhcpTrapMacAddress,
       "fsDhcpSnoopingMIBConformance": fsDhcpSnoopingMIBConformance,
       "fsDhcpSnoopingMIBCompliances": fsDhcpSnoopingMIBCompliances,
       "fsDhcpSnoopingMIBCompliance": fsDhcpSnoopingMIBCompliance,
       "fsDhcpSnoopingMIBGroups": fsDhcpSnoopingMIBGroups,
       "fsDhcpSnoopingMIBGroup": fsDhcpSnoopingMIBGroup}
)
