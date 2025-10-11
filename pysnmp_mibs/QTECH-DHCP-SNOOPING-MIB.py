# SNMP MIB module (QTECH-DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:49 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

qtechDhcpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42)
)
if mibBuilder.loadTexts:
    qtechDhcpSnoopingMIB.setRevisions(
        ("2007-10-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDhcpSnoopingMIBTraps_ObjectIdentity = ObjectIdentity
qtechDhcpSnoopingMIBTraps = _QtechDhcpSnoopingMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 0)
)
_QtechDhcpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
qtechDhcpSnoopingMIBObjects = _QtechDhcpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1)
)
_QtechSNDhcpGlobal_ObjectIdentity = ObjectIdentity
qtechSNDhcpGlobal = _QtechSNDhcpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 1)
)
_QtechSNDhcpFeatureEnable_Type = TruthValue
_QtechSNDhcpFeatureEnable_Object = MibScalar
qtechSNDhcpFeatureEnable = _QtechSNDhcpFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 1, 1),
    _QtechSNDhcpFeatureEnable_Type()
)
qtechSNDhcpFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNDhcpFeatureEnable.setStatus("current")
_QtechSNDhcpDatabaseUpdateInterval_Type = Unsigned32
_QtechSNDhcpDatabaseUpdateInterval_Object = MibScalar
qtechSNDhcpDatabaseUpdateInterval = _QtechSNDhcpDatabaseUpdateInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 1, 2),
    _QtechSNDhcpDatabaseUpdateInterval_Type()
)
qtechSNDhcpDatabaseUpdateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNDhcpDatabaseUpdateInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechSNDhcpDatabaseUpdateInterval.setUnits("seconds")
_QtechSNDhcpRelayAgentInfoOptEnable_Type = TruthValue
_QtechSNDhcpRelayAgentInfoOptEnable_Object = MibScalar
qtechSNDhcpRelayAgentInfoOptEnable = _QtechSNDhcpRelayAgentInfoOptEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 1, 3),
    _QtechSNDhcpRelayAgentInfoOptEnable_Type()
)
qtechSNDhcpRelayAgentInfoOptEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNDhcpRelayAgentInfoOptEnable.setStatus("current")
_QtechSNDhcpMatchMacAddressEnable_Type = TruthValue
_QtechSNDhcpMatchMacAddressEnable_Object = MibScalar
qtechSNDhcpMatchMacAddressEnable = _QtechSNDhcpMatchMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 1, 4),
    _QtechSNDhcpMatchMacAddressEnable_Type()
)
qtechSNDhcpMatchMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNDhcpMatchMacAddressEnable.setStatus("current")
_QtechSNDhcpInterface_ObjectIdentity = ObjectIdentity
qtechSNDhcpInterface = _QtechSNDhcpInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2)
)
_QtechSNDhcpIfTrustTable_Object = MibTable
qtechSNDhcpIfTrustTable = _QtechSNDhcpIfTrustTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechSNDhcpIfTrustTable.setStatus("current")
_QtechSNDhcpIfTrustEntry_Object = MibTableRow
qtechSNDhcpIfTrustEntry = _QtechSNDhcpIfTrustEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 1, 1)
)
qtechSNDhcpIfTrustEntry.setIndexNames(
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpIfTrustIndex"),
)
if mibBuilder.loadTexts:
    qtechSNDhcpIfTrustEntry.setStatus("current")
_QtechSNDhcpIfTrustIndex_Type = InterfaceIndex
_QtechSNDhcpIfTrustIndex_Object = MibTableColumn
qtechSNDhcpIfTrustIndex = _QtechSNDhcpIfTrustIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 1, 1, 1),
    _QtechSNDhcpIfTrustIndex_Type()
)
qtechSNDhcpIfTrustIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSNDhcpIfTrustIndex.setStatus("current")
_QtechSNDhcpIfTrustEnable_Type = TruthValue
_QtechSNDhcpIfTrustEnable_Object = MibTableColumn
qtechSNDhcpIfTrustEnable = _QtechSNDhcpIfTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 1, 1, 2),
    _QtechSNDhcpIfTrustEnable_Type()
)
qtechSNDhcpIfTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNDhcpIfTrustEnable.setStatus("current")
_QtechSNDhcpIfSuppressionTable_Object = MibTable
qtechSNDhcpIfSuppressionTable = _QtechSNDhcpIfSuppressionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechSNDhcpIfSuppressionTable.setStatus("current")
_QtechSNDhcpIfSuppressionEntry_Object = MibTableRow
qtechSNDhcpIfSuppressionEntry = _QtechSNDhcpIfSuppressionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 2, 1)
)
qtechSNDhcpIfSuppressionEntry.setIndexNames(
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpIfSuppressionIndex"),
)
if mibBuilder.loadTexts:
    qtechSNDhcpIfSuppressionEntry.setStatus("current")
_QtechSNDhcpIfSuppressionIndex_Type = InterfaceIndex
_QtechSNDhcpIfSuppressionIndex_Object = MibTableColumn
qtechSNDhcpIfSuppressionIndex = _QtechSNDhcpIfSuppressionIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 2, 1, 1),
    _QtechSNDhcpIfSuppressionIndex_Type()
)
qtechSNDhcpIfSuppressionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSNDhcpIfSuppressionIndex.setStatus("current")
_QtechSNDhcpIfSuppressionEnable_Type = TruthValue
_QtechSNDhcpIfSuppressionEnable_Object = MibTableColumn
qtechSNDhcpIfSuppressionEnable = _QtechSNDhcpIfSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 2, 1, 2),
    _QtechSNDhcpIfSuppressionEnable_Type()
)
qtechSNDhcpIfSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNDhcpIfSuppressionEnable.setStatus("current")
_QtechSNDhcpAddressBindTable_Object = MibTable
qtechSNDhcpAddressBindTable = _QtechSNDhcpAddressBindTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qtechSNDhcpAddressBindTable.setStatus("current")
_QtechSNDhcpAddressBindEntry_Object = MibTableRow
qtechSNDhcpAddressBindEntry = _QtechSNDhcpAddressBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 3, 1)
)
qtechSNDhcpAddressBindEntry.setIndexNames(
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpAddressBindIndex"),
)
if mibBuilder.loadTexts:
    qtechSNDhcpAddressBindEntry.setStatus("current")
_QtechSNDhcpAddressBindIndex_Type = InterfaceIndex
_QtechSNDhcpAddressBindIndex_Object = MibTableColumn
qtechSNDhcpAddressBindIndex = _QtechSNDhcpAddressBindIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 3, 1, 1),
    _QtechSNDhcpAddressBindIndex_Type()
)
qtechSNDhcpAddressBindIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSNDhcpAddressBindIndex.setStatus("current")
_QtechSNDhcpAddressBindEnable_Type = TruthValue
_QtechSNDhcpAddressBindEnable_Object = MibTableColumn
qtechSNDhcpAddressBindEnable = _QtechSNDhcpAddressBindEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 3, 1, 2),
    _QtechSNDhcpAddressBindEnable_Type()
)
qtechSNDhcpAddressBindEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNDhcpAddressBindEnable.setStatus("current")
_QtechDhcpSnpFalsePktStatisticTable_Object = MibTable
qtechDhcpSnpFalsePktStatisticTable = _QtechDhcpSnpFalsePktStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4)
)
if mibBuilder.loadTexts:
    qtechDhcpSnpFalsePktStatisticTable.setStatus("current")
_QtechDhcpSnpFalsePktStatisticEntry_Object = MibTableRow
qtechDhcpSnpFalsePktStatisticEntry = _QtechDhcpSnpFalsePktStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1)
)
qtechDhcpSnpFalsePktStatisticEntry.setIndexNames(
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechDhcpSnpStatisticIfIndex"),
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechDhcpSnpStatisticVlanIndex"),
)
if mibBuilder.loadTexts:
    qtechDhcpSnpFalsePktStatisticEntry.setStatus("current")
_QtechDhcpSnpStatisticIfIndex_Type = InterfaceIndex
_QtechDhcpSnpStatisticIfIndex_Object = MibTableColumn
qtechDhcpSnpStatisticIfIndex = _QtechDhcpSnpStatisticIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 1),
    _QtechDhcpSnpStatisticIfIndex_Type()
)
qtechDhcpSnpStatisticIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDhcpSnpStatisticIfIndex.setStatus("current")
_QtechDhcpSnpStatisticVlanIndex_Type = VlanIndex
_QtechDhcpSnpStatisticVlanIndex_Object = MibTableColumn
qtechDhcpSnpStatisticVlanIndex = _QtechDhcpSnpStatisticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 2),
    _QtechDhcpSnpStatisticVlanIndex_Type()
)
qtechDhcpSnpStatisticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechDhcpSnpStatisticVlanIndex.setStatus("current")


class _QtechDhcpSnpStatisticIfDescr_Type(DisplayString):
    """Custom type qtechDhcpSnpStatisticIfDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_QtechDhcpSnpStatisticIfDescr_Type.__name__ = "DisplayString"
_QtechDhcpSnpStatisticIfDescr_Object = MibTableColumn
qtechDhcpSnpStatisticIfDescr = _QtechDhcpSnpStatisticIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 3),
    _QtechDhcpSnpStatisticIfDescr_Type()
)
qtechDhcpSnpStatisticIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpSnpStatisticIfDescr.setStatus("current")
_QtechDhcpSnpStatisticVlanId_Type = VlanIndex
_QtechDhcpSnpStatisticVlanId_Object = MibTableColumn
qtechDhcpSnpStatisticVlanId = _QtechDhcpSnpStatisticVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 4),
    _QtechDhcpSnpStatisticVlanId_Type()
)
qtechDhcpSnpStatisticVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpSnpStatisticVlanId.setStatus("current")
_QtechChaddrNomatchSrcMacDhcpPktNum_Type = Counter32
_QtechChaddrNomatchSrcMacDhcpPktNum_Object = MibTableColumn
qtechChaddrNomatchSrcMacDhcpPktNum = _QtechChaddrNomatchSrcMacDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 5),
    _QtechChaddrNomatchSrcMacDhcpPktNum_Type()
)
qtechChaddrNomatchSrcMacDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechChaddrNomatchSrcMacDhcpPktNum.setStatus("current")
_QtechArpNomatchSnpBindTblPktNum_Type = Counter32
_QtechArpNomatchSnpBindTblPktNum_Object = MibTableColumn
qtechArpNomatchSnpBindTblPktNum = _QtechArpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 6),
    _QtechArpNomatchSnpBindTblPktNum_Type()
)
qtechArpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechArpNomatchSnpBindTblPktNum.setStatus("current")
_QtechIpNomatchSnpBindTblPktNum_Type = Counter32
_QtechIpNomatchSnpBindTblPktNum_Object = MibTableColumn
qtechIpNomatchSnpBindTblPktNum = _QtechIpNomatchSnpBindTblPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 7),
    _QtechIpNomatchSnpBindTblPktNum_Type()
)
qtechIpNomatchSnpBindTblPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIpNomatchSnpBindTblPktNum.setStatus("current")
_QtechNomatchSnpBindTblDhcpPktNum_Type = Counter32
_QtechNomatchSnpBindTblDhcpPktNum_Object = MibTableColumn
qtechNomatchSnpBindTblDhcpPktNum = _QtechNomatchSnpBindTblDhcpPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 8),
    _QtechNomatchSnpBindTblDhcpPktNum_Type()
)
qtechNomatchSnpBindTblDhcpPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNomatchSnpBindTblDhcpPktNum.setStatus("current")
_QtechUntrustedReplyPktNum_Type = Counter32
_QtechUntrustedReplyPktNum_Object = MibTableColumn
qtechUntrustedReplyPktNum = _QtechUntrustedReplyPktNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 9),
    _QtechUntrustedReplyPktNum_Type()
)
qtechUntrustedReplyPktNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUntrustedReplyPktNum.setStatus("current")
_QtechDhcpPktIfRateDiscardNum_Type = Counter32
_QtechDhcpPktIfRateDiscardNum_Object = MibTableColumn
qtechDhcpPktIfRateDiscardNum = _QtechDhcpPktIfRateDiscardNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 2, 4, 1, 10),
    _QtechDhcpPktIfRateDiscardNum_Type()
)
qtechDhcpPktIfRateDiscardNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpPktIfRateDiscardNum.setStatus("current")
_QtechSNDhcpBindings_ObjectIdentity = ObjectIdentity
qtechSNDhcpBindings = _QtechSNDhcpBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3)
)
_QtechSNDhcpBindingsTable_Object = MibTable
qtechSNDhcpBindingsTable = _QtechSNDhcpBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsTable.setStatus("current")
_QtechSNDhcpBindingsEntry_Object = MibTableRow
qtechSNDhcpBindingsEntry = _QtechSNDhcpBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1)
)
qtechSNDhcpBindingsEntry.setIndexNames(
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpBindingsVlan"),
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpBindingsMacAddress"),
    (0, "QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpBindingsAddrType"),
)
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsEntry.setStatus("current")
_QtechSNDhcpBindingsVlan_Type = VlanIndex
_QtechSNDhcpBindingsVlan_Object = MibTableColumn
qtechSNDhcpBindingsVlan = _QtechSNDhcpBindingsVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1, 1),
    _QtechSNDhcpBindingsVlan_Type()
)
qtechSNDhcpBindingsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsVlan.setStatus("current")
_QtechSNDhcpBindingsMacAddress_Type = MacAddress
_QtechSNDhcpBindingsMacAddress_Object = MibTableColumn
qtechSNDhcpBindingsMacAddress = _QtechSNDhcpBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1, 2),
    _QtechSNDhcpBindingsMacAddress_Type()
)
qtechSNDhcpBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsMacAddress.setStatus("current")


class _QtechSNDhcpBindingsAddrType_Type(Integer32):
    """Custom type qtechSNDhcpBindingsAddrType based on Integer32"""
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


_QtechSNDhcpBindingsAddrType_Type.__name__ = "Integer32"
_QtechSNDhcpBindingsAddrType_Object = MibTableColumn
qtechSNDhcpBindingsAddrType = _QtechSNDhcpBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1, 3),
    _QtechSNDhcpBindingsAddrType_Type()
)
qtechSNDhcpBindingsAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsAddrType.setStatus("current")
_QtechSNDhcpBindingsIpAddress_Type = IpAddress
_QtechSNDhcpBindingsIpAddress_Object = MibTableColumn
qtechSNDhcpBindingsIpAddress = _QtechSNDhcpBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1, 4),
    _QtechSNDhcpBindingsIpAddress_Type()
)
qtechSNDhcpBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsIpAddress.setStatus("current")
_QtechSNDhcpBindingsInterface_Type = InterfaceIndex
_QtechSNDhcpBindingsInterface_Object = MibTableColumn
qtechSNDhcpBindingsInterface = _QtechSNDhcpBindingsInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1, 5),
    _QtechSNDhcpBindingsInterface_Type()
)
qtechSNDhcpBindingsInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsInterface.setStatus("current")
_QtechSNDhcpBindingsLeasedTime_Type = Unsigned32
_QtechSNDhcpBindingsLeasedTime_Object = MibTableColumn
qtechSNDhcpBindingsLeasedTime = _QtechSNDhcpBindingsLeasedTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1, 6),
    _QtechSNDhcpBindingsLeasedTime_Type()
)
qtechSNDhcpBindingsLeasedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsLeasedTime.setStatus("current")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsLeasedTime.setUnits("seconds")
_QtechSNDhcpBindingsStatus_Type = RowStatus
_QtechSNDhcpBindingsStatus_Object = MibTableColumn
qtechSNDhcpBindingsStatus = _QtechSNDhcpBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 3, 1, 1, 7),
    _QtechSNDhcpBindingsStatus_Type()
)
qtechSNDhcpBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSNDhcpBindingsStatus.setStatus("current")
_QtechDhcpTrapMacAddress_Type = MacAddress
_QtechDhcpTrapMacAddress_Object = MibScalar
qtechDhcpTrapMacAddress = _QtechDhcpTrapMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 1, 4),
    _QtechDhcpTrapMacAddress_Type()
)
qtechDhcpTrapMacAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechDhcpTrapMacAddress.setStatus("current")
_QtechDhcpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
qtechDhcpSnoopingMIBConformance = _QtechDhcpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 2)
)
_QtechDhcpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
qtechDhcpSnoopingMIBCompliances = _QtechDhcpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 2, 1)
)
_QtechDhcpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
qtechDhcpSnoopingMIBGroups = _QtechDhcpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 2, 2)
)

# Managed Objects groups

qtechDhcpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 2, 2, 1)
)
qtechDhcpSnoopingMIBGroup.setObjects(
      *(("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpFeatureEnable"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpDatabaseUpdateInterval"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpRelayAgentInfoOptEnable"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpMatchMacAddressEnable"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpIfTrustEnable"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpIfSuppressionEnable"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpAddressBindEnable"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechDhcpSnpStatisticIfDescr"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechDhcpSnpStatisticVlanId"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechChaddrNomatchSrcMacDhcpPktNum"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechArpNomatchSnpBindTblPktNum"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechIpNomatchSnpBindTblPktNum"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechNomatchSnpBindTblDhcpPktNum"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechUntrustedReplyPktNum"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechDhcpPktIfRateDiscardNum"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpBindingsIpAddress"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpBindingsInterface"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpBindingsLeasedTime"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechSNDhcpBindingsStatus"),
        ("QTECH-DHCP-SNOOPING-MIB", "qtechDhcpTrapMacAddress"))
)
if mibBuilder.loadTexts:
    qtechDhcpSnoopingMIBGroup.setStatus("current")


# Notification objects

qtechDhcpSnoopingNoResponseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 0, 1)
)
qtechDhcpSnoopingNoResponseTrap.setObjects(
    ("QTECH-DHCP-SNOOPING-MIB", "qtechDhcpTrapMacAddress")
)
if mibBuilder.loadTexts:
    qtechDhcpSnoopingNoResponseTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechDhcpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 42, 2, 1, 1)
)
qtechDhcpSnoopingMIBCompliance.setObjects(
    ("QTECH-DHCP-SNOOPING-MIB", "qtechDhcpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    qtechDhcpSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-DHCP-SNOOPING-MIB",
    **{"qtechDhcpSnoopingMIB": qtechDhcpSnoopingMIB,
       "qtechDhcpSnoopingMIBTraps": qtechDhcpSnoopingMIBTraps,
       "qtechDhcpSnoopingNoResponseTrap": qtechDhcpSnoopingNoResponseTrap,
       "qtechDhcpSnoopingMIBObjects": qtechDhcpSnoopingMIBObjects,
       "qtechSNDhcpGlobal": qtechSNDhcpGlobal,
       "qtechSNDhcpFeatureEnable": qtechSNDhcpFeatureEnable,
       "qtechSNDhcpDatabaseUpdateInterval": qtechSNDhcpDatabaseUpdateInterval,
       "qtechSNDhcpRelayAgentInfoOptEnable": qtechSNDhcpRelayAgentInfoOptEnable,
       "qtechSNDhcpMatchMacAddressEnable": qtechSNDhcpMatchMacAddressEnable,
       "qtechSNDhcpInterface": qtechSNDhcpInterface,
       "qtechSNDhcpIfTrustTable": qtechSNDhcpIfTrustTable,
       "qtechSNDhcpIfTrustEntry": qtechSNDhcpIfTrustEntry,
       "qtechSNDhcpIfTrustIndex": qtechSNDhcpIfTrustIndex,
       "qtechSNDhcpIfTrustEnable": qtechSNDhcpIfTrustEnable,
       "qtechSNDhcpIfSuppressionTable": qtechSNDhcpIfSuppressionTable,
       "qtechSNDhcpIfSuppressionEntry": qtechSNDhcpIfSuppressionEntry,
       "qtechSNDhcpIfSuppressionIndex": qtechSNDhcpIfSuppressionIndex,
       "qtechSNDhcpIfSuppressionEnable": qtechSNDhcpIfSuppressionEnable,
       "qtechSNDhcpAddressBindTable": qtechSNDhcpAddressBindTable,
       "qtechSNDhcpAddressBindEntry": qtechSNDhcpAddressBindEntry,
       "qtechSNDhcpAddressBindIndex": qtechSNDhcpAddressBindIndex,
       "qtechSNDhcpAddressBindEnable": qtechSNDhcpAddressBindEnable,
       "qtechDhcpSnpFalsePktStatisticTable": qtechDhcpSnpFalsePktStatisticTable,
       "qtechDhcpSnpFalsePktStatisticEntry": qtechDhcpSnpFalsePktStatisticEntry,
       "qtechDhcpSnpStatisticIfIndex": qtechDhcpSnpStatisticIfIndex,
       "qtechDhcpSnpStatisticVlanIndex": qtechDhcpSnpStatisticVlanIndex,
       "qtechDhcpSnpStatisticIfDescr": qtechDhcpSnpStatisticIfDescr,
       "qtechDhcpSnpStatisticVlanId": qtechDhcpSnpStatisticVlanId,
       "qtechChaddrNomatchSrcMacDhcpPktNum": qtechChaddrNomatchSrcMacDhcpPktNum,
       "qtechArpNomatchSnpBindTblPktNum": qtechArpNomatchSnpBindTblPktNum,
       "qtechIpNomatchSnpBindTblPktNum": qtechIpNomatchSnpBindTblPktNum,
       "qtechNomatchSnpBindTblDhcpPktNum": qtechNomatchSnpBindTblDhcpPktNum,
       "qtechUntrustedReplyPktNum": qtechUntrustedReplyPktNum,
       "qtechDhcpPktIfRateDiscardNum": qtechDhcpPktIfRateDiscardNum,
       "qtechSNDhcpBindings": qtechSNDhcpBindings,
       "qtechSNDhcpBindingsTable": qtechSNDhcpBindingsTable,
       "qtechSNDhcpBindingsEntry": qtechSNDhcpBindingsEntry,
       "qtechSNDhcpBindingsVlan": qtechSNDhcpBindingsVlan,
       "qtechSNDhcpBindingsMacAddress": qtechSNDhcpBindingsMacAddress,
       "qtechSNDhcpBindingsAddrType": qtechSNDhcpBindingsAddrType,
       "qtechSNDhcpBindingsIpAddress": qtechSNDhcpBindingsIpAddress,
       "qtechSNDhcpBindingsInterface": qtechSNDhcpBindingsInterface,
       "qtechSNDhcpBindingsLeasedTime": qtechSNDhcpBindingsLeasedTime,
       "qtechSNDhcpBindingsStatus": qtechSNDhcpBindingsStatus,
       "qtechDhcpTrapMacAddress": qtechDhcpTrapMacAddress,
       "qtechDhcpSnoopingMIBConformance": qtechDhcpSnoopingMIBConformance,
       "qtechDhcpSnoopingMIBCompliances": qtechDhcpSnoopingMIBCompliances,
       "qtechDhcpSnoopingMIBCompliance": qtechDhcpSnoopingMIBCompliance,
       "qtechDhcpSnoopingMIBGroups": qtechDhcpSnoopingMIBGroups,
       "qtechDhcpSnoopingMIBGroup": qtechDhcpSnoopingMIBGroup}
)
