# SNMP MIB module (QTECH-CAPWAP-MOBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-CAPWAP-MOBILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:51 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

qtechMobilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64)
)
if mibBuilder.loadTexts:
    qtechMobilityMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechMobilityMIBObjects_ObjectIdentity = ObjectIdentity
qtechMobilityMIBObjects = _QtechMobilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1)
)
_QtechMobility_ObjectIdentity = ObjectIdentity
qtechMobility = _QtechMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1)
)
_QtechMobilityEntryTable_Object = MibTable
qtechMobilityEntryTable = _QtechMobilityEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechMobilityEntryTable.setStatus("current")
_QtechMobilityEntry_Object = MibTableRow
qtechMobilityEntry = _QtechMobilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1)
)
qtechMobilityEntry.setIndexNames(
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupId"),
)
if mibBuilder.loadTexts:
    qtechMobilityEntry.setStatus("current")


class _QtechRoamGroupId_Type(Integer32):
    """Custom type qtechRoamGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_QtechRoamGroupId_Type.__name__ = "Integer32"
_QtechRoamGroupId_Object = MibTableColumn
qtechRoamGroupId = _QtechRoamGroupId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 1),
    _QtechRoamGroupId_Type()
)
qtechRoamGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamGroupId.setStatus("current")
_QtechRoamGroupName_Type = DisplayString
_QtechRoamGroupName_Object = MibTableColumn
qtechRoamGroupName = _QtechRoamGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 2),
    _QtechRoamGroupName_Type()
)
qtechRoamGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamGroupName.setStatus("current")
_QtechRoamGroupMyAddress_Type = IpAddress
_QtechRoamGroupMyAddress_Object = MibTableColumn
qtechRoamGroupMyAddress = _QtechRoamGroupMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 3),
    _QtechRoamGroupMyAddress_Type()
)
qtechRoamGroupMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamGroupMyAddress.setStatus("current")
_QtechRoamGroupMcEnable_Type = Integer32
_QtechRoamGroupMcEnable_Object = MibTableColumn
qtechRoamGroupMcEnable = _QtechRoamGroupMcEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 4),
    _QtechRoamGroupMcEnable_Type()
)
qtechRoamGroupMcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamGroupMcEnable.setStatus("current")
_QtechRoamGroupMcAddress_Type = IpAddress
_QtechRoamGroupMcAddress_Object = MibTableColumn
qtechRoamGroupMcAddress = _QtechRoamGroupMcAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 5),
    _QtechRoamGroupMcAddress_Type()
)
qtechRoamGroupMcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamGroupMcAddress.setStatus("current")


class _QtechRoamGroupKeepaliveCount_Type(Integer32):
    """Custom type qtechRoamGroupKeepaliveCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_QtechRoamGroupKeepaliveCount_Type.__name__ = "Integer32"
_QtechRoamGroupKeepaliveCount_Object = MibTableColumn
qtechRoamGroupKeepaliveCount = _QtechRoamGroupKeepaliveCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 6),
    _QtechRoamGroupKeepaliveCount_Type()
)
qtechRoamGroupKeepaliveCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamGroupKeepaliveCount.setStatus("current")


class _QtechRoamGroupKeepaliveInterval_Type(Integer32):
    """Custom type qtechRoamGroupKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_QtechRoamGroupKeepaliveInterval_Type.__name__ = "Integer32"
_QtechRoamGroupKeepaliveInterval_Object = MibTableColumn
qtechRoamGroupKeepaliveInterval = _QtechRoamGroupKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 7),
    _QtechRoamGroupKeepaliveInterval_Type()
)
qtechRoamGroupKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamGroupKeepaliveInterval.setStatus("current")
_QtechRoamGroupIsFast_Type = Integer32
_QtechRoamGroupIsFast_Object = MibTableColumn
qtechRoamGroupIsFast = _QtechRoamGroupIsFast_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 8),
    _QtechRoamGroupIsFast_Type()
)
qtechRoamGroupIsFast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamGroupIsFast.setStatus("current")
_QtechRoamGroupCreateStatus_Type = RowStatus
_QtechRoamGroupCreateStatus_Object = MibTableColumn
qtechRoamGroupCreateStatus = _QtechRoamGroupCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 9),
    _QtechRoamGroupCreateStatus_Type()
)
qtechRoamGroupCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamGroupCreateStatus.setStatus("current")
_QtechRoamGroupMyAddressIPv6_Type = Ipv6Address
_QtechRoamGroupMyAddressIPv6_Object = MibTableColumn
qtechRoamGroupMyAddressIPv6 = _QtechRoamGroupMyAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 1, 1, 10),
    _QtechRoamGroupMyAddressIPv6_Type()
)
qtechRoamGroupMyAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamGroupMyAddressIPv6.setStatus("current")
_QtechMobilityMemberEntryTable_Object = MibTable
qtechMobilityMemberEntryTable = _QtechMobilityMemberEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechMobilityMemberEntryTable.setStatus("current")
_QtechMobilityMemberEntry_Object = MibTableRow
qtechMobilityMemberEntry = _QtechMobilityMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1)
)
qtechMobilityMemberEntry.setIndexNames(
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberGroupId"),
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberPeerAddress"),
)
if mibBuilder.loadTexts:
    qtechMobilityMemberEntry.setStatus("current")


class _QtechRoamMemberGroupId_Type(Integer32):
    """Custom type qtechRoamMemberGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_QtechRoamMemberGroupId_Type.__name__ = "Integer32"
_QtechRoamMemberGroupId_Object = MibTableColumn
qtechRoamMemberGroupId = _QtechRoamMemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 1),
    _QtechRoamMemberGroupId_Type()
)
qtechRoamMemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamMemberGroupId.setStatus("current")
_QtechRoamMemberPeerAddress_Type = IpAddress
_QtechRoamMemberPeerAddress_Object = MibTableColumn
qtechRoamMemberPeerAddress = _QtechRoamMemberPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 2),
    _QtechRoamMemberPeerAddress_Type()
)
qtechRoamMemberPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamMemberPeerAddress.setStatus("current")


class _QtechRoamMemberIsList_Type(Integer32):
    """Custom type qtechRoamMemberIsList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRoamMemberIsList_Type.__name__ = "Integer32"
_QtechRoamMemberIsList_Object = MibTableColumn
qtechRoamMemberIsList = _QtechRoamMemberIsList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 3),
    _QtechRoamMemberIsList_Type()
)
qtechRoamMemberIsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamMemberIsList.setStatus("current")


class _QtechRoamMemberDataChannelIsOK_Type(Integer32):
    """Custom type qtechRoamMemberDataChannelIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRoamMemberDataChannelIsOK_Type.__name__ = "Integer32"
_QtechRoamMemberDataChannelIsOK_Object = MibTableColumn
qtechRoamMemberDataChannelIsOK = _QtechRoamMemberDataChannelIsOK_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 4),
    _QtechRoamMemberDataChannelIsOK_Type()
)
qtechRoamMemberDataChannelIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamMemberDataChannelIsOK.setStatus("current")
_QtechRoamMemberDataChannelFailTimes_Type = Integer32
_QtechRoamMemberDataChannelFailTimes_Object = MibTableColumn
qtechRoamMemberDataChannelFailTimes = _QtechRoamMemberDataChannelFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 5),
    _QtechRoamMemberDataChannelFailTimes_Type()
)
qtechRoamMemberDataChannelFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamMemberDataChannelFailTimes.setStatus("current")
_QtechRoamMemberDTLSIsClient_Type = Integer32
_QtechRoamMemberDTLSIsClient_Object = MibTableColumn
qtechRoamMemberDTLSIsClient = _QtechRoamMemberDTLSIsClient_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 6),
    _QtechRoamMemberDTLSIsClient_Type()
)
qtechRoamMemberDTLSIsClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamMemberDTLSIsClient.setStatus("current")


class _QtechRoamMemberDTLSIsOK_Type(Integer32):
    """Custom type qtechRoamMemberDTLSIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRoamMemberDTLSIsOK_Type.__name__ = "Integer32"
_QtechRoamMemberDTLSIsOK_Object = MibTableColumn
qtechRoamMemberDTLSIsOK = _QtechRoamMemberDTLSIsOK_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 7),
    _QtechRoamMemberDTLSIsOK_Type()
)
qtechRoamMemberDTLSIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamMemberDTLSIsOK.setStatus("current")
_QtechRoamMemberCreateStatus_Type = RowStatus
_QtechRoamMemberCreateStatus_Object = MibTableColumn
qtechRoamMemberCreateStatus = _QtechRoamMemberCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 2, 1, 8),
    _QtechRoamMemberCreateStatus_Type()
)
qtechRoamMemberCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamMemberCreateStatus.setStatus("current")
_QtechAPCtrlCreatEntryTable_Object = MibTable
qtechAPCtrlCreatEntryTable = _QtechAPCtrlCreatEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3)
)
if mibBuilder.loadTexts:
    qtechAPCtrlCreatEntryTable.setStatus("current")
_QtechAPCtrlCreatEntry_Object = MibTableRow
qtechAPCtrlCreatEntry = _QtechAPCtrlCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1)
)
qtechAPCtrlCreatEntry.setIndexNames(
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechAPName"),
)
if mibBuilder.loadTexts:
    qtechAPCtrlCreatEntry.setStatus("current")
_QtechAPName_Type = DisplayString
_QtechAPName_Object = MibTableColumn
qtechAPName = _QtechAPName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 1),
    _QtechAPName_Type()
)
qtechAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechAPName.setStatus("current")


class _QtechPriority_Type(Integer32):
    """Custom type qtechPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_QtechPriority_Type.__name__ = "Integer32"
_QtechPriority_Object = MibTableColumn
qtechPriority = _QtechPriority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 2),
    _QtechPriority_Type()
)
qtechPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPriority.setStatus("current")
_QtechPrimaryACIP_Type = IpAddress
_QtechPrimaryACIP_Object = MibTableColumn
qtechPrimaryACIP = _QtechPrimaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 3),
    _QtechPrimaryACIP_Type()
)
qtechPrimaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPrimaryACIP.setStatus("current")
_QtechPrimaryACName_Type = DisplayString
_QtechPrimaryACName_Object = MibTableColumn
qtechPrimaryACName = _QtechPrimaryACName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 4),
    _QtechPrimaryACName_Type()
)
qtechPrimaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPrimaryACName.setStatus("current")
_QtechSecondaryACIP_Type = IpAddress
_QtechSecondaryACIP_Object = MibTableColumn
qtechSecondaryACIP = _QtechSecondaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 5),
    _QtechSecondaryACIP_Type()
)
qtechSecondaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecondaryACIP.setStatus("current")
_QtechSecondaryACName_Type = DisplayString
_QtechSecondaryACName_Object = MibTableColumn
qtechSecondaryACName = _QtechSecondaryACName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 6),
    _QtechSecondaryACName_Type()
)
qtechSecondaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecondaryACName.setStatus("current")
_QtechTertiaryACIP_Type = IpAddress
_QtechTertiaryACIP_Object = MibTableColumn
qtechTertiaryACIP = _QtechTertiaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 7),
    _QtechTertiaryACIP_Type()
)
qtechTertiaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTertiaryACIP.setStatus("current")
_QtechTertiaryACName_Type = DisplayString
_QtechTertiaryACName_Object = MibTableColumn
qtechTertiaryACName = _QtechTertiaryACName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 8),
    _QtechTertiaryACName_Type()
)
qtechTertiaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTertiaryACName.setStatus("current")
_QtechAPCtrlCreatStatus_Type = RowStatus
_QtechAPCtrlCreatStatus_Object = MibTableColumn
qtechAPCtrlCreatStatus = _QtechAPCtrlCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 3, 1, 9),
    _QtechAPCtrlCreatStatus_Type()
)
qtechAPCtrlCreatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAPCtrlCreatStatus.setStatus("current")
_QtechWLANCtrlCreatEntryTable_Object = MibTable
qtechWLANCtrlCreatEntryTable = _QtechWLANCtrlCreatEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qtechWLANCtrlCreatEntryTable.setStatus("current")
_QtechWLANCtrlCreatEntry_Object = MibTableRow
qtechWLANCtrlCreatEntry = _QtechWLANCtrlCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 4, 1)
)
qtechWLANCtrlCreatEntry.setIndexNames(
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechWLANID"),
)
if mibBuilder.loadTexts:
    qtechWLANCtrlCreatEntry.setStatus("current")
_QtechWLANID_Type = Integer32
_QtechWLANID_Object = MibTableColumn
qtechWLANID = _QtechWLANID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 4, 1, 1),
    _QtechWLANID_Type()
)
qtechWLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWLANID.setStatus("current")
_QtechAnchorACIPaddr_Type = IpAddress
_QtechAnchorACIPaddr_Object = MibTableColumn
qtechAnchorACIPaddr = _QtechAnchorACIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 4, 1, 2),
    _QtechAnchorACIPaddr_Type()
)
qtechAnchorACIPaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAnchorACIPaddr.setStatus("current")
_QtechWLANCtrlCreatStatus_Type = RowStatus
_QtechWLANCtrlCreatStatus_Object = MibTableColumn
qtechWLANCtrlCreatStatus = _QtechWLANCtrlCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 4, 1, 3),
    _QtechWLANCtrlCreatStatus_Type()
)
qtechWLANCtrlCreatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechWLANCtrlCreatStatus.setStatus("current")
_QtechAnchorACIPaddrIPv6_Type = Ipv6Address
_QtechAnchorACIPaddrIPv6_Object = MibTableColumn
qtechAnchorACIPaddrIPv6 = _QtechAnchorACIPaddrIPv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 4, 1, 4),
    _QtechAnchorACIPaddrIPv6_Type()
)
qtechAnchorACIPaddrIPv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechAnchorACIPaddrIPv6.setStatus("current")
_QtechMobilityACPing_Type = IpAddress
_QtechMobilityACPing_Object = MibScalar
qtechMobilityACPing = _QtechMobilityACPing_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 5),
    _QtechMobilityACPing_Type()
)
qtechMobilityACPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMobilityACPing.setStatus("current")
_QtechGlobalHandoffRequestsReceived_Type = Integer32
_QtechGlobalHandoffRequestsReceived_Object = MibScalar
qtechGlobalHandoffRequestsReceived = _QtechGlobalHandoffRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 6),
    _QtechGlobalHandoffRequestsReceived_Type()
)
qtechGlobalHandoffRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalHandoffRequestsReceived.setStatus("current")
_QtechGlobalHandoffEndRequestsReceived_Type = Integer32
_QtechGlobalHandoffEndRequestsReceived_Object = MibScalar
qtechGlobalHandoffEndRequestsReceived = _QtechGlobalHandoffEndRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 7),
    _QtechGlobalHandoffEndRequestsReceived_Type()
)
qtechGlobalHandoffEndRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalHandoffEndRequestsReceived.setStatus("current")
_QtechGlobalStateTransitionsDisabled_Type = Integer32
_QtechGlobalStateTransitionsDisabled_Object = MibScalar
qtechGlobalStateTransitionsDisabled = _QtechGlobalStateTransitionsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 8),
    _QtechGlobalStateTransitionsDisabled_Type()
)
qtechGlobalStateTransitionsDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalStateTransitionsDisabled.setStatus("current")
_QtechGlobalResourceUnavailable_Type = Integer32
_QtechGlobalResourceUnavailable_Object = MibScalar
qtechGlobalResourceUnavailable = _QtechGlobalResourceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 9),
    _QtechGlobalResourceUnavailable_Type()
)
qtechGlobalResourceUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechGlobalResourceUnavailable.setStatus("current")
_QtechRespondeHandoffRequestIgnored_Type = Integer32
_QtechRespondeHandoffRequestIgnored_Object = MibScalar
qtechRespondeHandoffRequestIgnored = _QtechRespondeHandoffRequestIgnored_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 10),
    _QtechRespondeHandoffRequestIgnored_Type()
)
qtechRespondeHandoffRequestIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeHandoffRequestIgnored.setStatus("current")
_QtechRespondePingPongHandoffRequestsDropped_Type = Integer32
_QtechRespondePingPongHandoffRequestsDropped_Object = MibScalar
qtechRespondePingPongHandoffRequestsDropped = _QtechRespondePingPongHandoffRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 11),
    _QtechRespondePingPongHandoffRequestsDropped_Type()
)
qtechRespondePingPongHandoffRequestsDropped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondePingPongHandoffRequestsDropped.setStatus("current")
_QtechRespondeHandoffRequestsDroped_Type = Integer32
_QtechRespondeHandoffRequestsDroped_Object = MibScalar
qtechRespondeHandoffRequestsDroped = _QtechRespondeHandoffRequestsDroped_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 12),
    _QtechRespondeHandoffRequestsDroped_Type()
)
qtechRespondeHandoffRequestsDroped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeHandoffRequestsDroped.setStatus("current")
_QtechRespondeHandoffRequestsDenied_Type = Integer32
_QtechRespondeHandoffRequestsDenied_Object = MibScalar
qtechRespondeHandoffRequestsDenied = _QtechRespondeHandoffRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 13),
    _QtechRespondeHandoffRequestsDenied_Type()
)
qtechRespondeHandoffRequestsDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeHandoffRequestsDenied.setStatus("current")
_QtechRespondeClientHandoffasLocal_Type = Integer32
_QtechRespondeClientHandoffasLocal_Object = MibScalar
qtechRespondeClientHandoffasLocal = _QtechRespondeClientHandoffasLocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 14),
    _QtechRespondeClientHandoffasLocal_Type()
)
qtechRespondeClientHandoffasLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeClientHandoffasLocal.setStatus("current")
_QtechRespondeClientHandoffasForeign_Type = Integer32
_QtechRespondeClientHandoffasForeign_Object = MibScalar
qtechRespondeClientHandoffasForeign = _QtechRespondeClientHandoffasForeign_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 15),
    _QtechRespondeClientHandoffasForeign_Type()
)
qtechRespondeClientHandoffasForeign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeClientHandoffasForeign.setStatus("current")
_QtechRespondeAnchorRequestsReceived_Type = Integer32
_QtechRespondeAnchorRequestsReceived_Object = MibScalar
qtechRespondeAnchorRequestsReceived = _QtechRespondeAnchorRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 16),
    _QtechRespondeAnchorRequestsReceived_Type()
)
qtechRespondeAnchorRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeAnchorRequestsReceived.setStatus("current")
_QtechRespondeAnchorRequestDenied_Type = Integer32
_QtechRespondeAnchorRequestDenied_Object = MibScalar
qtechRespondeAnchorRequestDenied = _QtechRespondeAnchorRequestDenied_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 17),
    _QtechRespondeAnchorRequestDenied_Type()
)
qtechRespondeAnchorRequestDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeAnchorRequestDenied.setStatus("current")
_QtechRespondeAnchorTransferred_Type = Integer32
_QtechRespondeAnchorTransferred_Object = MibScalar
qtechRespondeAnchorTransferred = _QtechRespondeAnchorTransferred_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 18),
    _QtechRespondeAnchorTransferred_Type()
)
qtechRespondeAnchorTransferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechRespondeAnchorTransferred.setStatus("current")
_QtechInitHandoffRequestsSent_Type = Integer32
_QtechInitHandoffRequestsSent_Object = MibScalar
qtechInitHandoffRequestsSent = _QtechInitHandoffRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 19),
    _QtechInitHandoffRequestsSent_Type()
)
qtechInitHandoffRequestsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechInitHandoffRequestsSent.setStatus("current")
_QtechInitHandoffReplyReceived_Type = Integer32
_QtechInitHandoffReplyReceived_Object = MibScalar
qtechInitHandoffReplyReceived = _QtechInitHandoffReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 20),
    _QtechInitHandoffReplyReceived_Type()
)
qtechInitHandoffReplyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechInitHandoffReplyReceived.setStatus("current")
_QtechInitHandoffasLocalReceived_Type = Integer32
_QtechInitHandoffasLocalReceived_Object = MibScalar
qtechInitHandoffasLocalReceived = _QtechInitHandoffasLocalReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 21),
    _QtechInitHandoffasLocalReceived_Type()
)
qtechInitHandoffasLocalReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechInitHandoffasLocalReceived.setStatus("current")
_QtechInitHandoffasForeignReceived_Type = Integer32
_QtechInitHandoffasForeignReceived_Object = MibScalar
qtechInitHandoffasForeignReceived = _QtechInitHandoffasForeignReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 22),
    _QtechInitHandoffasForeignReceived_Type()
)
qtechInitHandoffasForeignReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechInitHandoffasForeignReceived.setStatus("current")
_QtechInitHandoffDenyReceived_Type = Integer32
_QtechInitHandoffDenyReceived_Object = MibScalar
qtechInitHandoffDenyReceived = _QtechInitHandoffDenyReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 23),
    _QtechInitHandoffDenyReceived_Type()
)
qtechInitHandoffDenyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechInitHandoffDenyReceived.setStatus("current")
_QtechInitAnchorRequestSent_Type = Integer32
_QtechInitAnchorRequestSent_Object = MibScalar
qtechInitAnchorRequestSent = _QtechInitAnchorRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 24),
    _QtechInitAnchorRequestSent_Type()
)
qtechInitAnchorRequestSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechInitAnchorRequestSent.setStatus("current")
_QtechInitAnchorDenyReceived_Type = Integer32
_QtechInitAnchorDenyReceived_Object = MibScalar
qtechInitAnchorDenyReceived = _QtechInitAnchorDenyReceived_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 25),
    _QtechInitAnchorDenyReceived_Type()
)
qtechInitAnchorDenyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechInitAnchorDenyReceived.setStatus("current")
_QtechAPPriorityEnable_Type = Integer32
_QtechAPPriorityEnable_Object = MibScalar
qtechAPPriorityEnable = _QtechAPPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 26),
    _QtechAPPriorityEnable_Type()
)
qtechAPPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechAPPriorityEnable.setStatus("current")
_QtechPrimaryBackUpACIP_Type = IpAddress
_QtechPrimaryBackUpACIP_Object = MibScalar
qtechPrimaryBackUpACIP = _QtechPrimaryBackUpACIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 27),
    _QtechPrimaryBackUpACIP_Type()
)
qtechPrimaryBackUpACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPrimaryBackUpACIP.setStatus("current")
_QtechPrimaryBackUpACName_Type = DisplayString
_QtechPrimaryBackUpACName_Object = MibScalar
qtechPrimaryBackUpACName = _QtechPrimaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 28),
    _QtechPrimaryBackUpACName_Type()
)
qtechPrimaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechPrimaryBackUpACName.setStatus("current")
_QtechSecondaryBackUpACIP_Type = IpAddress
_QtechSecondaryBackUpACIP_Object = MibScalar
qtechSecondaryBackUpACIP = _QtechSecondaryBackUpACIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 29),
    _QtechSecondaryBackUpACIP_Type()
)
qtechSecondaryBackUpACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecondaryBackUpACIP.setStatus("current")
_QtechSecondaryBackUpACName_Type = DisplayString
_QtechSecondaryBackUpACName_Object = MibScalar
qtechSecondaryBackUpACName = _QtechSecondaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 30),
    _QtechSecondaryBackUpACName_Type()
)
qtechSecondaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecondaryBackUpACName.setStatus("current")
_QtechTeriaryBackUpACip_Type = IpAddress
_QtechTeriaryBackUpACip_Object = MibScalar
qtechTeriaryBackUpACip = _QtechTeriaryBackUpACip_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 31),
    _QtechTeriaryBackUpACip_Type()
)
qtechTeriaryBackUpACip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTeriaryBackUpACip.setStatus("current")
_QtechTeriaryBackUpACName_Type = DisplayString
_QtechTeriaryBackUpACName_Object = MibScalar
qtechTeriaryBackUpACName = _QtechTeriaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 32),
    _QtechTeriaryBackUpACName_Type()
)
qtechTeriaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTeriaryBackUpACName.setStatus("current")
_QtechACIntraRoam_Type = Counter32
_QtechACIntraRoam_Object = MibScalar
qtechACIntraRoam = _QtechACIntraRoam_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 33),
    _QtechACIntraRoam_Type()
)
qtechACIntraRoam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechACIntraRoam.setStatus("current")
_QtechACInterRoamIn_Type = Counter32
_QtechACInterRoamIn_Object = MibScalar
qtechACInterRoamIn = _QtechACInterRoamIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 34),
    _QtechACInterRoamIn_Type()
)
qtechACInterRoamIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechACInterRoamIn.setStatus("current")
_QtechACInterRoamOut_Type = Counter32
_QtechACInterRoamOut_Object = MibScalar
qtechACInterRoamOut = _QtechACInterRoamOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 35),
    _QtechACInterRoamOut_Type()
)
qtechACInterRoamOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechACInterRoamOut.setStatus("current")
_QtechMobilityACPingIPv6_Type = Ipv6Address
_QtechMobilityACPingIPv6_Object = MibScalar
qtechMobilityACPingIPv6 = _QtechMobilityACPingIPv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 36),
    _QtechMobilityACPingIPv6_Type()
)
qtechMobilityACPingIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMobilityACPingIPv6.setStatus("current")
_QtechMobilityIPv6MemberEntryTable_Object = MibTable
qtechMobilityIPv6MemberEntryTable = _QtechMobilityIPv6MemberEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37)
)
if mibBuilder.loadTexts:
    qtechMobilityIPv6MemberEntryTable.setStatus("current")
_QtechMobilityIPv6MemberEntry_Object = MibTableRow
qtechMobilityIPv6MemberEntry = _QtechMobilityIPv6MemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1)
)
qtechMobilityIPv6MemberEntry.setIndexNames(
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberGroupId"),
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberPeerAddress"),
)
if mibBuilder.loadTexts:
    qtechMobilityIPv6MemberEntry.setStatus("current")


class _QtechRoamIPv6MemberGroupId_Type(Integer32):
    """Custom type qtechRoamIPv6MemberGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_QtechRoamIPv6MemberGroupId_Type.__name__ = "Integer32"
_QtechRoamIPv6MemberGroupId_Object = MibTableColumn
qtechRoamIPv6MemberGroupId = _QtechRoamIPv6MemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 1),
    _QtechRoamIPv6MemberGroupId_Type()
)
qtechRoamIPv6MemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberGroupId.setStatus("current")
_QtechRoamIPv6MemberPeerAddress_Type = Ipv6Address
_QtechRoamIPv6MemberPeerAddress_Object = MibTableColumn
qtechRoamIPv6MemberPeerAddress = _QtechRoamIPv6MemberPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 2),
    _QtechRoamIPv6MemberPeerAddress_Type()
)
qtechRoamIPv6MemberPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberPeerAddress.setStatus("current")


class _QtechRoamIPv6MemberIsList_Type(Integer32):
    """Custom type qtechRoamIPv6MemberIsList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRoamIPv6MemberIsList_Type.__name__ = "Integer32"
_QtechRoamIPv6MemberIsList_Object = MibTableColumn
qtechRoamIPv6MemberIsList = _QtechRoamIPv6MemberIsList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 3),
    _QtechRoamIPv6MemberIsList_Type()
)
qtechRoamIPv6MemberIsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberIsList.setStatus("current")


class _QtechRoamIPv6MemberDataChannelIsOK_Type(Integer32):
    """Custom type qtechRoamIPv6MemberDataChannelIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRoamIPv6MemberDataChannelIsOK_Type.__name__ = "Integer32"
_QtechRoamIPv6MemberDataChannelIsOK_Object = MibTableColumn
qtechRoamIPv6MemberDataChannelIsOK = _QtechRoamIPv6MemberDataChannelIsOK_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 4),
    _QtechRoamIPv6MemberDataChannelIsOK_Type()
)
qtechRoamIPv6MemberDataChannelIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberDataChannelIsOK.setStatus("current")
_QtechRoamIPv6MemberDataChannelFailTimes_Type = Integer32
_QtechRoamIPv6MemberDataChannelFailTimes_Object = MibTableColumn
qtechRoamIPv6MemberDataChannelFailTimes = _QtechRoamIPv6MemberDataChannelFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 5),
    _QtechRoamIPv6MemberDataChannelFailTimes_Type()
)
qtechRoamIPv6MemberDataChannelFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberDataChannelFailTimes.setStatus("current")
_QtechRoamIPv6MemberDTLSIsClient_Type = Integer32
_QtechRoamIPv6MemberDTLSIsClient_Object = MibTableColumn
qtechRoamIPv6MemberDTLSIsClient = _QtechRoamIPv6MemberDTLSIsClient_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 6),
    _QtechRoamIPv6MemberDTLSIsClient_Type()
)
qtechRoamIPv6MemberDTLSIsClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberDTLSIsClient.setStatus("current")


class _QtechRoamIPv6MemberDTLSIsOK_Type(Integer32):
    """Custom type qtechRoamIPv6MemberDTLSIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_QtechRoamIPv6MemberDTLSIsOK_Type.__name__ = "Integer32"
_QtechRoamIPv6MemberDTLSIsOK_Object = MibTableColumn
qtechRoamIPv6MemberDTLSIsOK = _QtechRoamIPv6MemberDTLSIsOK_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 7),
    _QtechRoamIPv6MemberDTLSIsOK_Type()
)
qtechRoamIPv6MemberDTLSIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberDTLSIsOK.setStatus("current")
_QtechRoamIPv6MemberCreateStatus_Type = RowStatus
_QtechRoamIPv6MemberCreateStatus_Object = MibTableColumn
qtechRoamIPv6MemberCreateStatus = _QtechRoamIPv6MemberCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 37, 1, 8),
    _QtechRoamIPv6MemberCreateStatus_Type()
)
qtechRoamIPv6MemberCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechRoamIPv6MemberCreateStatus.setStatus("current")
_QtechMobilityUserEntryTable_Object = MibTable
qtechMobilityUserEntryTable = _QtechMobilityUserEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38)
)
if mibBuilder.loadTexts:
    qtechMobilityUserEntryTable.setStatus("current")
_QtechMobilityUserEntry_Object = MibTableRow
qtechMobilityUserEntry = _QtechMobilityUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1)
)
qtechMobilityUserEntry.setIndexNames(
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserMac"),
)
if mibBuilder.loadTexts:
    qtechMobilityUserEntry.setStatus("current")
_QtechRoamUserMac_Type = MacAddress
_QtechRoamUserMac_Object = MibTableColumn
qtechRoamUserMac = _QtechRoamUserMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 1),
    _QtechRoamUserMac_Type()
)
qtechRoamUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserMac.setStatus("current")
_QtechRoamUserRoamType_Type = Integer32
_QtechRoamUserRoamType_Object = MibTableColumn
qtechRoamUserRoamType = _QtechRoamUserRoamType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 2),
    _QtechRoamUserRoamType_Type()
)
qtechRoamUserRoamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamType.setStatus("current")
_QtechRoamUserRoamOutAcAddressType_Type = InetAddressType
_QtechRoamUserRoamOutAcAddressType_Object = MibTableColumn
qtechRoamUserRoamOutAcAddressType = _QtechRoamUserRoamOutAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 3),
    _QtechRoamUserRoamOutAcAddressType_Type()
)
qtechRoamUserRoamOutAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamOutAcAddressType.setStatus("current")
_QtechRoamUserRoamOutAcAddress_Type = InetAddress
_QtechRoamUserRoamOutAcAddress_Object = MibTableColumn
qtechRoamUserRoamOutAcAddress = _QtechRoamUserRoamOutAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 4),
    _QtechRoamUserRoamOutAcAddress_Type()
)
qtechRoamUserRoamOutAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamOutAcAddress.setStatus("current")
_QtechRoamUserRoamInAcAddressType_Type = InetAddressType
_QtechRoamUserRoamInAcAddressType_Object = MibTableColumn
qtechRoamUserRoamInAcAddressType = _QtechRoamUserRoamInAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 5),
    _QtechRoamUserRoamInAcAddressType_Type()
)
qtechRoamUserRoamInAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamInAcAddressType.setStatus("current")
_QtechRoamUserRoamInAcAddress_Type = InetAddress
_QtechRoamUserRoamInAcAddress_Object = MibTableColumn
qtechRoamUserRoamInAcAddress = _QtechRoamUserRoamInAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 6),
    _QtechRoamUserRoamInAcAddress_Type()
)
qtechRoamUserRoamInAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamInAcAddress.setStatus("current")
_QtechRoamUserRoamOutApMac_Type = MacAddress
_QtechRoamUserRoamOutApMac_Object = MibTableColumn
qtechRoamUserRoamOutApMac = _QtechRoamUserRoamOutApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 7),
    _QtechRoamUserRoamOutApMac_Type()
)
qtechRoamUserRoamOutApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamOutApMac.setStatus("current")
_QtechRoamUserRoamInApMac_Type = MacAddress
_QtechRoamUserRoamInApMac_Object = MibTableColumn
qtechRoamUserRoamInApMac = _QtechRoamUserRoamInApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 8),
    _QtechRoamUserRoamInApMac_Type()
)
qtechRoamUserRoamInApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamInApMac.setStatus("current")
_QtechRoamUserRoamOutVid_Type = Integer32
_QtechRoamUserRoamOutVid_Object = MibTableColumn
qtechRoamUserRoamOutVid = _QtechRoamUserRoamOutVid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 9),
    _QtechRoamUserRoamOutVid_Type()
)
qtechRoamUserRoamOutVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamOutVid.setStatus("current")
_QtechRoamUserRoamInVid_Type = Integer32
_QtechRoamUserRoamInVid_Object = MibTableColumn
qtechRoamUserRoamInVid = _QtechRoamUserRoamInVid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 38, 1, 10),
    _QtechRoamUserRoamInVid_Type()
)
qtechRoamUserRoamInVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamUserRoamInVid.setStatus("current")
_QtechMobilityTrackEntryTable_Object = MibTable
qtechMobilityTrackEntryTable = _QtechMobilityTrackEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39)
)
if mibBuilder.loadTexts:
    qtechMobilityTrackEntryTable.setStatus("current")
_QtechMobilityTrackEntry_Object = MibTableRow
qtechMobilityTrackEntry = _QtechMobilityTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1)
)
qtechMobilityTrackEntry.setIndexNames(
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackStaMac"),
    (0, "QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackId"),
)
if mibBuilder.loadTexts:
    qtechMobilityTrackEntry.setStatus("current")
_QtechRoamTrackStaMac_Type = MacAddress
_QtechRoamTrackStaMac_Object = MibTableColumn
qtechRoamTrackStaMac = _QtechRoamTrackStaMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 1),
    _QtechRoamTrackStaMac_Type()
)
qtechRoamTrackStaMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackStaMac.setStatus("current")
_QtechRoamTrackId_Type = Integer32
_QtechRoamTrackId_Object = MibTableColumn
qtechRoamTrackId = _QtechRoamTrackId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 2),
    _QtechRoamTrackId_Type()
)
qtechRoamTrackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackId.setStatus("current")
_QtechRoamTrackAcAddressType_Type = InetAddressType
_QtechRoamTrackAcAddressType_Object = MibTableColumn
qtechRoamTrackAcAddressType = _QtechRoamTrackAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 3),
    _QtechRoamTrackAcAddressType_Type()
)
qtechRoamTrackAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackAcAddressType.setStatus("current")
_QtechRoamTrackAcAddress_Type = InetAddress
_QtechRoamTrackAcAddress_Object = MibTableColumn
qtechRoamTrackAcAddress = _QtechRoamTrackAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 4),
    _QtechRoamTrackAcAddress_Type()
)
qtechRoamTrackAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackAcAddress.setStatus("current")
_QtechRoamTrackApMac_Type = MacAddress
_QtechRoamTrackApMac_Object = MibTableColumn
qtechRoamTrackApMac = _QtechRoamTrackApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 5),
    _QtechRoamTrackApMac_Type()
)
qtechRoamTrackApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackApMac.setStatus("current")
_QtechRoamTrackRadioId_Type = Integer32
_QtechRoamTrackRadioId_Object = MibTableColumn
qtechRoamTrackRadioId = _QtechRoamTrackRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 6),
    _QtechRoamTrackRadioId_Type()
)
qtechRoamTrackRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackRadioId.setStatus("current")
_QtechRoamTrackStaIp_Type = IpAddress
_QtechRoamTrackStaIp_Object = MibTableColumn
qtechRoamTrackStaIp = _QtechRoamTrackStaIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 7),
    _QtechRoamTrackStaIp_Type()
)
qtechRoamTrackStaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackStaIp.setStatus("current")
_QtechRoamTrackStaIpv6_Type = Ipv6Address
_QtechRoamTrackStaIpv6_Object = MibTableColumn
qtechRoamTrackStaIpv6 = _QtechRoamTrackStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 8),
    _QtechRoamTrackStaIpv6_Type()
)
qtechRoamTrackStaIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackStaIpv6.setStatus("current")
_QtechRoamTrackStaOnlineTime_Type = Integer32
_QtechRoamTrackStaOnlineTime_Object = MibTableColumn
qtechRoamTrackStaOnlineTime = _QtechRoamTrackStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 1, 39, 1, 9),
    _QtechRoamTrackStaOnlineTime_Type()
)
qtechRoamTrackStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechRoamTrackStaOnlineTime.setStatus("current")
_QtechMobilityIf_ObjectIdentity = ObjectIdentity
qtechMobilityIf = _QtechMobilityIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 2)
)
_QtechMobilityMIBCompliances_ObjectIdentity = ObjectIdentity
qtechMobilityMIBCompliances = _QtechMobilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 2, 1)
)
_QtechMobilityMIBGroups_ObjectIdentity = ObjectIdentity
qtechMobilityMIBGroups = _QtechMobilityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 2, 2)
)
_QtechMobilityTrap_ObjectIdentity = ObjectIdentity
qtechMobilityTrap = _QtechMobilityTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3)
)
_QtechMobilityTrapSta_ObjectIdentity = ObjectIdentity
qtechMobilityTrapSta = _QtechMobilityTrapSta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1)
)
_QtechMobilityNotifyApMac_Type = MacAddress
_QtechMobilityNotifyApMac_Object = MibScalar
qtechMobilityNotifyApMac = _QtechMobilityNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 1),
    _QtechMobilityNotifyApMac_Type()
)
qtechMobilityNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyApMac.setStatus("current")
_QtechMobilityNotifyStaMac_Type = MacAddress
_QtechMobilityNotifyStaMac_Object = MibScalar
qtechMobilityNotifyStaMac = _QtechMobilityNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 2),
    _QtechMobilityNotifyStaMac_Type()
)
qtechMobilityNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaMac.setStatus("current")
_QtechMobilityNotifyApIp_Type = IpAddress
_QtechMobilityNotifyApIp_Object = MibScalar
qtechMobilityNotifyApIp = _QtechMobilityNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 3),
    _QtechMobilityNotifyApIp_Type()
)
qtechMobilityNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyApIp.setStatus("current")
_QtechMobilityNotifyStaIp_Type = IpAddress
_QtechMobilityNotifyStaIp_Object = MibScalar
qtechMobilityNotifyStaIp = _QtechMobilityNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 4),
    _QtechMobilityNotifyStaIp_Type()
)
qtechMobilityNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaIp.setStatus("current")
_QtechMobilityNotifyStaOperType_Type = Integer32
_QtechMobilityNotifyStaOperType_Object = MibScalar
qtechMobilityNotifyStaOperType = _QtechMobilityNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 5),
    _QtechMobilityNotifyStaOperType_Type()
)
qtechMobilityNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaOperType.setStatus("current")


class _QtechMobilityNotifyStaApRadioId_Type(Integer32):
    """Custom type qtechMobilityNotifyStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechMobilityNotifyStaApRadioId_Type.__name__ = "Integer32"
_QtechMobilityNotifyStaApRadioId_Object = MibScalar
qtechMobilityNotifyStaApRadioId = _QtechMobilityNotifyStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 6),
    _QtechMobilityNotifyStaApRadioId_Type()
)
qtechMobilityNotifyStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaApRadioId.setStatus("current")


class _QtechMobilityNotifyStaApRadioType_Type(Integer32):
    """Custom type qtechMobilityNotifyStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_QtechMobilityNotifyStaApRadioType_Type.__name__ = "Integer32"
_QtechMobilityNotifyStaApRadioType_Object = MibScalar
qtechMobilityNotifyStaApRadioType = _QtechMobilityNotifyStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 7),
    _QtechMobilityNotifyStaApRadioType_Type()
)
qtechMobilityNotifyStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaApRadioType.setStatus("current")


class _QtechMobilityNotifyStaVlanId_Type(Integer32):
    """Custom type qtechMobilityNotifyStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_QtechMobilityNotifyStaVlanId_Type.__name__ = "Integer32"
_QtechMobilityNotifyStaVlanId_Object = MibScalar
qtechMobilityNotifyStaVlanId = _QtechMobilityNotifyStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 8),
    _QtechMobilityNotifyStaVlanId_Type()
)
qtechMobilityNotifyStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaVlanId.setStatus("current")


class _QtechMobilityNotifyStaWlanId_Type(Integer32):
    """Custom type qtechMobilityNotifyStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_QtechMobilityNotifyStaWlanId_Type.__name__ = "Integer32"
_QtechMobilityNotifyStaWlanId_Object = MibScalar
qtechMobilityNotifyStaWlanId = _QtechMobilityNotifyStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 9),
    _QtechMobilityNotifyStaWlanId_Type()
)
qtechMobilityNotifyStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaWlanId.setStatus("current")
_QtechMobilityNotifyStaIpv6_Type = Ipv6Address
_QtechMobilityNotifyStaIpv6_Object = MibScalar
qtechMobilityNotifyStaIpv6 = _QtechMobilityNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 10),
    _QtechMobilityNotifyStaIpv6_Type()
)
qtechMobilityNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaIpv6.setStatus("current")


class _QtechMobilityNotifyStaAssoAuthMode_Type(Integer32):
    """Custom type qtechMobilityNotifyStaAssoAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("wep", 1),
          ("dot1x-wep", 2),
          ("dot1x-wpa", 3),
          ("dot1x-wpa2", 4),
          ("mab", 5),
          ("psk-wpa", 6),
          ("psk-wpa2", 7),
          ("wapi", 8))
    )


_QtechMobilityNotifyStaAssoAuthMode_Type.__name__ = "Integer32"
_QtechMobilityNotifyStaAssoAuthMode_Object = MibScalar
qtechMobilityNotifyStaAssoAuthMode = _QtechMobilityNotifyStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 11),
    _QtechMobilityNotifyStaAssoAuthMode_Type()
)
qtechMobilityNotifyStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaAssoAuthMode.setStatus("current")


class _QtechMobilityNotifyStaNetAuthMode_Type(Integer32):
    """Custom type qtechMobilityNotifyStaNetAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("open", 0),
          ("web", 1))
    )


_QtechMobilityNotifyStaNetAuthMode_Type.__name__ = "Integer32"
_QtechMobilityNotifyStaNetAuthMode_Object = MibScalar
qtechMobilityNotifyStaNetAuthMode = _QtechMobilityNotifyStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 12),
    _QtechMobilityNotifyStaNetAuthMode_Type()
)
qtechMobilityNotifyStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaNetAuthMode.setStatus("current")
_QtechMobilityNotifyStaSsid_Type = DisplayString
_QtechMobilityNotifyStaSsid_Object = MibScalar
qtechMobilityNotifyStaSsid = _QtechMobilityNotifyStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 13),
    _QtechMobilityNotifyStaSsid_Type()
)
qtechMobilityNotifyStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaSsid.setStatus("current")
_QtechMobilityNotifyStaLinkRate_Type = Integer32
_QtechMobilityNotifyStaLinkRate_Object = MibScalar
qtechMobilityNotifyStaLinkRate = _QtechMobilityNotifyStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 14),
    _QtechMobilityNotifyStaLinkRate_Type()
)
qtechMobilityNotifyStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaLinkRate.setStatus("current")
_QtechMobilityNotifyStaCurChan_Type = Integer32
_QtechMobilityNotifyStaCurChan_Object = MibScalar
qtechMobilityNotifyStaCurChan = _QtechMobilityNotifyStaCurChan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 15),
    _QtechMobilityNotifyStaCurChan_Type()
)
qtechMobilityNotifyStaCurChan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaCurChan.setStatus("current")
_QtechMobilityNotifyStaClientType_Type = DisplayString
_QtechMobilityNotifyStaClientType_Object = MibScalar
qtechMobilityNotifyStaClientType = _QtechMobilityNotifyStaClientType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 16),
    _QtechMobilityNotifyStaClientType_Type()
)
qtechMobilityNotifyStaClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaClientType.setStatus("current")
_QtechMobilityNotifyStaRssi_Type = Integer32
_QtechMobilityNotifyStaRssi_Object = MibScalar
qtechMobilityNotifyStaRssi = _QtechMobilityNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 17),
    _QtechMobilityNotifyStaRssi_Type()
)
qtechMobilityNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaRssi.setStatus("current")
_QtechMobilityNotifyStaReason_Type = DisplayString
_QtechMobilityNotifyStaReason_Object = MibScalar
qtechMobilityNotifyStaReason = _QtechMobilityNotifyStaReason_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 1, 18),
    _QtechMobilityNotifyStaReason_Type()
)
qtechMobilityNotifyStaReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaReason.setStatus("current")
_QtechMobilityTrapStaIf_ObjectIdentity = ObjectIdentity
qtechMobilityTrapStaIf = _QtechMobilityTrapStaIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 2)
)

# Managed Objects groups

qtechMobilityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 2, 2, 1)
)
qtechMobilityMIBGroup.setObjects(
      *(("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupName"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupMyAddress"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupMcEnable"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupMcAddress"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupKeepaliveCount"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupKeepaliveInterval"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupIsFast"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamGroupCreateStatus"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberIsList"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberDataChannelIsOK"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberDataChannelFailTimes"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberDTLSIsClient"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberDTLSIsOK"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamMemberCreateStatus"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechPriority"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechPrimaryACIP"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechPrimaryACName"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechSecondaryACIP"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechSecondaryACName"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechTertiaryACIP"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechTertiaryACName"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechAPCtrlCreatStatus"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechAnchorACIPaddr"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechWLANCtrlCreatStatus"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechGlobalHandoffRequestsReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechGlobalHandoffEndRequestsReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechGlobalStateTransitionsDisabled"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechGlobalResourceUnavailable"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeHandoffRequestIgnored"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondePingPongHandoffRequestsDropped"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeHandoffRequestsDroped"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeHandoffRequestsDenied"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeClientHandoffasLocal"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeClientHandoffasForeign"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeAnchorRequestsReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeAnchorRequestDenied"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRespondeAnchorTransferred"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechInitHandoffRequestsSent"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechInitHandoffReplyReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechInitHandoffasLocalReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechInitHandoffasForeignReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechInitHandoffDenyReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechInitAnchorRequestSent"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechInitAnchorDenyReceived"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechAPPriorityEnable"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechPrimaryBackUpACIP"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechPrimaryBackUpACName"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechSecondaryBackUpACIP"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechSecondaryBackUpACName"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechTeriaryBackUpACip"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechTeriaryBackUpACName"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechACIntraRoam"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechACInterRoamIn"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechACInterRoamOut"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityACPingIPv6"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberGroupId"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberPeerAddress"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberIsList"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberDataChannelIsOK"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberDataChannelFailTimes"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberDTLSIsClient"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberDTLSIsOK"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamIPv6MemberCreateStatus"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserMac"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamType"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamOutAcAddressType"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamOutAcAddress"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamInAcAddressType"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamInAcAddress"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamOutApMac"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamInApMac"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamOutVid"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamUserRoamInVid"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackStaMac"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackId"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackAcAddressType"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackAcAddress"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackApMac"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackRadioId"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackStaIp"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackStaIpv6"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechRoamTrackStaOnlineTime"))
)
if mibBuilder.loadTexts:
    qtechMobilityMIBGroup.setStatus("current")


# Notification objects

qtechMobilityNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 3, 2, 1)
)
qtechMobilityNotifyStaOper.setObjects(
      *(("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyApMac"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaMac"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyApIp"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaIp"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaOperType"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaApRadioId"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaApRadioType"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaVlanId"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaWlanId"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaIpv6"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaAssoAuthMode"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaNetAuthMode"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaSsid"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaLinkRate"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaCurChan"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaClientType"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaRssi"),
        ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityNotifyStaReason"))
)
if mibBuilder.loadTexts:
    qtechMobilityNotifyStaOper.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechMobilityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 64, 1, 2, 1, 1)
)
qtechMobilityMIBCompliance.setObjects(
    ("QTECH-CAPWAP-MOBILITY-MIB", "qtechMobilityMIBGroup")
)
if mibBuilder.loadTexts:
    qtechMobilityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-CAPWAP-MOBILITY-MIB",
    **{"qtechMobilityMIB": qtechMobilityMIB,
       "qtechMobilityMIBObjects": qtechMobilityMIBObjects,
       "qtechMobility": qtechMobility,
       "qtechMobilityEntryTable": qtechMobilityEntryTable,
       "qtechMobilityEntry": qtechMobilityEntry,
       "qtechRoamGroupId": qtechRoamGroupId,
       "qtechRoamGroupName": qtechRoamGroupName,
       "qtechRoamGroupMyAddress": qtechRoamGroupMyAddress,
       "qtechRoamGroupMcEnable": qtechRoamGroupMcEnable,
       "qtechRoamGroupMcAddress": qtechRoamGroupMcAddress,
       "qtechRoamGroupKeepaliveCount": qtechRoamGroupKeepaliveCount,
       "qtechRoamGroupKeepaliveInterval": qtechRoamGroupKeepaliveInterval,
       "qtechRoamGroupIsFast": qtechRoamGroupIsFast,
       "qtechRoamGroupCreateStatus": qtechRoamGroupCreateStatus,
       "qtechRoamGroupMyAddressIPv6": qtechRoamGroupMyAddressIPv6,
       "qtechMobilityMemberEntryTable": qtechMobilityMemberEntryTable,
       "qtechMobilityMemberEntry": qtechMobilityMemberEntry,
       "qtechRoamMemberGroupId": qtechRoamMemberGroupId,
       "qtechRoamMemberPeerAddress": qtechRoamMemberPeerAddress,
       "qtechRoamMemberIsList": qtechRoamMemberIsList,
       "qtechRoamMemberDataChannelIsOK": qtechRoamMemberDataChannelIsOK,
       "qtechRoamMemberDataChannelFailTimes": qtechRoamMemberDataChannelFailTimes,
       "qtechRoamMemberDTLSIsClient": qtechRoamMemberDTLSIsClient,
       "qtechRoamMemberDTLSIsOK": qtechRoamMemberDTLSIsOK,
       "qtechRoamMemberCreateStatus": qtechRoamMemberCreateStatus,
       "qtechAPCtrlCreatEntryTable": qtechAPCtrlCreatEntryTable,
       "qtechAPCtrlCreatEntry": qtechAPCtrlCreatEntry,
       "qtechAPName": qtechAPName,
       "qtechPriority": qtechPriority,
       "qtechPrimaryACIP": qtechPrimaryACIP,
       "qtechPrimaryACName": qtechPrimaryACName,
       "qtechSecondaryACIP": qtechSecondaryACIP,
       "qtechSecondaryACName": qtechSecondaryACName,
       "qtechTertiaryACIP": qtechTertiaryACIP,
       "qtechTertiaryACName": qtechTertiaryACName,
       "qtechAPCtrlCreatStatus": qtechAPCtrlCreatStatus,
       "qtechWLANCtrlCreatEntryTable": qtechWLANCtrlCreatEntryTable,
       "qtechWLANCtrlCreatEntry": qtechWLANCtrlCreatEntry,
       "qtechWLANID": qtechWLANID,
       "qtechAnchorACIPaddr": qtechAnchorACIPaddr,
       "qtechWLANCtrlCreatStatus": qtechWLANCtrlCreatStatus,
       "qtechAnchorACIPaddrIPv6": qtechAnchorACIPaddrIPv6,
       "qtechMobilityACPing": qtechMobilityACPing,
       "qtechGlobalHandoffRequestsReceived": qtechGlobalHandoffRequestsReceived,
       "qtechGlobalHandoffEndRequestsReceived": qtechGlobalHandoffEndRequestsReceived,
       "qtechGlobalStateTransitionsDisabled": qtechGlobalStateTransitionsDisabled,
       "qtechGlobalResourceUnavailable": qtechGlobalResourceUnavailable,
       "qtechRespondeHandoffRequestIgnored": qtechRespondeHandoffRequestIgnored,
       "qtechRespondePingPongHandoffRequestsDropped": qtechRespondePingPongHandoffRequestsDropped,
       "qtechRespondeHandoffRequestsDroped": qtechRespondeHandoffRequestsDroped,
       "qtechRespondeHandoffRequestsDenied": qtechRespondeHandoffRequestsDenied,
       "qtechRespondeClientHandoffasLocal": qtechRespondeClientHandoffasLocal,
       "qtechRespondeClientHandoffasForeign": qtechRespondeClientHandoffasForeign,
       "qtechRespondeAnchorRequestsReceived": qtechRespondeAnchorRequestsReceived,
       "qtechRespondeAnchorRequestDenied": qtechRespondeAnchorRequestDenied,
       "qtechRespondeAnchorTransferred": qtechRespondeAnchorTransferred,
       "qtechInitHandoffRequestsSent": qtechInitHandoffRequestsSent,
       "qtechInitHandoffReplyReceived": qtechInitHandoffReplyReceived,
       "qtechInitHandoffasLocalReceived": qtechInitHandoffasLocalReceived,
       "qtechInitHandoffasForeignReceived": qtechInitHandoffasForeignReceived,
       "qtechInitHandoffDenyReceived": qtechInitHandoffDenyReceived,
       "qtechInitAnchorRequestSent": qtechInitAnchorRequestSent,
       "qtechInitAnchorDenyReceived": qtechInitAnchorDenyReceived,
       "qtechAPPriorityEnable": qtechAPPriorityEnable,
       "qtechPrimaryBackUpACIP": qtechPrimaryBackUpACIP,
       "qtechPrimaryBackUpACName": qtechPrimaryBackUpACName,
       "qtechSecondaryBackUpACIP": qtechSecondaryBackUpACIP,
       "qtechSecondaryBackUpACName": qtechSecondaryBackUpACName,
       "qtechTeriaryBackUpACip": qtechTeriaryBackUpACip,
       "qtechTeriaryBackUpACName": qtechTeriaryBackUpACName,
       "qtechACIntraRoam": qtechACIntraRoam,
       "qtechACInterRoamIn": qtechACInterRoamIn,
       "qtechACInterRoamOut": qtechACInterRoamOut,
       "qtechMobilityACPingIPv6": qtechMobilityACPingIPv6,
       "qtechMobilityIPv6MemberEntryTable": qtechMobilityIPv6MemberEntryTable,
       "qtechMobilityIPv6MemberEntry": qtechMobilityIPv6MemberEntry,
       "qtechRoamIPv6MemberGroupId": qtechRoamIPv6MemberGroupId,
       "qtechRoamIPv6MemberPeerAddress": qtechRoamIPv6MemberPeerAddress,
       "qtechRoamIPv6MemberIsList": qtechRoamIPv6MemberIsList,
       "qtechRoamIPv6MemberDataChannelIsOK": qtechRoamIPv6MemberDataChannelIsOK,
       "qtechRoamIPv6MemberDataChannelFailTimes": qtechRoamIPv6MemberDataChannelFailTimes,
       "qtechRoamIPv6MemberDTLSIsClient": qtechRoamIPv6MemberDTLSIsClient,
       "qtechRoamIPv6MemberDTLSIsOK": qtechRoamIPv6MemberDTLSIsOK,
       "qtechRoamIPv6MemberCreateStatus": qtechRoamIPv6MemberCreateStatus,
       "qtechMobilityUserEntryTable": qtechMobilityUserEntryTable,
       "qtechMobilityUserEntry": qtechMobilityUserEntry,
       "qtechRoamUserMac": qtechRoamUserMac,
       "qtechRoamUserRoamType": qtechRoamUserRoamType,
       "qtechRoamUserRoamOutAcAddressType": qtechRoamUserRoamOutAcAddressType,
       "qtechRoamUserRoamOutAcAddress": qtechRoamUserRoamOutAcAddress,
       "qtechRoamUserRoamInAcAddressType": qtechRoamUserRoamInAcAddressType,
       "qtechRoamUserRoamInAcAddress": qtechRoamUserRoamInAcAddress,
       "qtechRoamUserRoamOutApMac": qtechRoamUserRoamOutApMac,
       "qtechRoamUserRoamInApMac": qtechRoamUserRoamInApMac,
       "qtechRoamUserRoamOutVid": qtechRoamUserRoamOutVid,
       "qtechRoamUserRoamInVid": qtechRoamUserRoamInVid,
       "qtechMobilityTrackEntryTable": qtechMobilityTrackEntryTable,
       "qtechMobilityTrackEntry": qtechMobilityTrackEntry,
       "qtechRoamTrackStaMac": qtechRoamTrackStaMac,
       "qtechRoamTrackId": qtechRoamTrackId,
       "qtechRoamTrackAcAddressType": qtechRoamTrackAcAddressType,
       "qtechRoamTrackAcAddress": qtechRoamTrackAcAddress,
       "qtechRoamTrackApMac": qtechRoamTrackApMac,
       "qtechRoamTrackRadioId": qtechRoamTrackRadioId,
       "qtechRoamTrackStaIp": qtechRoamTrackStaIp,
       "qtechRoamTrackStaIpv6": qtechRoamTrackStaIpv6,
       "qtechRoamTrackStaOnlineTime": qtechRoamTrackStaOnlineTime,
       "qtechMobilityIf": qtechMobilityIf,
       "qtechMobilityMIBCompliances": qtechMobilityMIBCompliances,
       "qtechMobilityMIBCompliance": qtechMobilityMIBCompliance,
       "qtechMobilityMIBGroups": qtechMobilityMIBGroups,
       "qtechMobilityMIBGroup": qtechMobilityMIBGroup,
       "qtechMobilityTrap": qtechMobilityTrap,
       "qtechMobilityTrapSta": qtechMobilityTrapSta,
       "qtechMobilityNotifyApMac": qtechMobilityNotifyApMac,
       "qtechMobilityNotifyStaMac": qtechMobilityNotifyStaMac,
       "qtechMobilityNotifyApIp": qtechMobilityNotifyApIp,
       "qtechMobilityNotifyStaIp": qtechMobilityNotifyStaIp,
       "qtechMobilityNotifyStaOperType": qtechMobilityNotifyStaOperType,
       "qtechMobilityNotifyStaApRadioId": qtechMobilityNotifyStaApRadioId,
       "qtechMobilityNotifyStaApRadioType": qtechMobilityNotifyStaApRadioType,
       "qtechMobilityNotifyStaVlanId": qtechMobilityNotifyStaVlanId,
       "qtechMobilityNotifyStaWlanId": qtechMobilityNotifyStaWlanId,
       "qtechMobilityNotifyStaIpv6": qtechMobilityNotifyStaIpv6,
       "qtechMobilityNotifyStaAssoAuthMode": qtechMobilityNotifyStaAssoAuthMode,
       "qtechMobilityNotifyStaNetAuthMode": qtechMobilityNotifyStaNetAuthMode,
       "qtechMobilityNotifyStaSsid": qtechMobilityNotifyStaSsid,
       "qtechMobilityNotifyStaLinkRate": qtechMobilityNotifyStaLinkRate,
       "qtechMobilityNotifyStaCurChan": qtechMobilityNotifyStaCurChan,
       "qtechMobilityNotifyStaClientType": qtechMobilityNotifyStaClientType,
       "qtechMobilityNotifyStaRssi": qtechMobilityNotifyStaRssi,
       "qtechMobilityNotifyStaReason": qtechMobilityNotifyStaReason,
       "qtechMobilityTrapStaIf": qtechMobilityTrapStaIf,
       "qtechMobilityNotifyStaOper": qtechMobilityNotifyStaOper}
)
