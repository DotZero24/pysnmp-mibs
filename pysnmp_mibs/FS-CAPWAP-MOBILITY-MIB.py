# SNMP MIB module (FS-CAPWAP-MOBILITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-CAPWAP-MOBILITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:39 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

fsMobilityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64)
)
if mibBuilder.loadTexts:
    fsMobilityMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMobilityMIBObjects_ObjectIdentity = ObjectIdentity
fsMobilityMIBObjects = _FsMobilityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1)
)
_FsMobility_ObjectIdentity = ObjectIdentity
fsMobility = _FsMobility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1)
)
_FsMobilityEntryTable_Object = MibTable
fsMobilityEntryTable = _FsMobilityEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsMobilityEntryTable.setStatus("current")
_FsMobilityEntry_Object = MibTableRow
fsMobilityEntry = _FsMobilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1)
)
fsMobilityEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupId"),
)
if mibBuilder.loadTexts:
    fsMobilityEntry.setStatus("current")


class _FsRoamGroupId_Type(Integer32):
    """Custom type fsRoamGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FsRoamGroupId_Type.__name__ = "Integer32"
_FsRoamGroupId_Object = MibTableColumn
fsRoamGroupId = _FsRoamGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 1),
    _FsRoamGroupId_Type()
)
fsRoamGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamGroupId.setStatus("current")
_FsRoamGroupName_Type = DisplayString
_FsRoamGroupName_Object = MibTableColumn
fsRoamGroupName = _FsRoamGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 2),
    _FsRoamGroupName_Type()
)
fsRoamGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamGroupName.setStatus("current")
_FsRoamGroupMyAddress_Type = IpAddress
_FsRoamGroupMyAddress_Object = MibTableColumn
fsRoamGroupMyAddress = _FsRoamGroupMyAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 3),
    _FsRoamGroupMyAddress_Type()
)
fsRoamGroupMyAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamGroupMyAddress.setStatus("current")
_FsRoamGroupMcEnable_Type = Integer32
_FsRoamGroupMcEnable_Object = MibTableColumn
fsRoamGroupMcEnable = _FsRoamGroupMcEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 4),
    _FsRoamGroupMcEnable_Type()
)
fsRoamGroupMcEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamGroupMcEnable.setStatus("current")
_FsRoamGroupMcAddress_Type = IpAddress
_FsRoamGroupMcAddress_Object = MibTableColumn
fsRoamGroupMcAddress = _FsRoamGroupMcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 5),
    _FsRoamGroupMcAddress_Type()
)
fsRoamGroupMcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamGroupMcAddress.setStatus("current")


class _FsRoamGroupKeepaliveCount_Type(Integer32):
    """Custom type fsRoamGroupKeepaliveCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 30),
    )


_FsRoamGroupKeepaliveCount_Type.__name__ = "Integer32"
_FsRoamGroupKeepaliveCount_Object = MibTableColumn
fsRoamGroupKeepaliveCount = _FsRoamGroupKeepaliveCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 6),
    _FsRoamGroupKeepaliveCount_Type()
)
fsRoamGroupKeepaliveCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamGroupKeepaliveCount.setStatus("current")


class _FsRoamGroupKeepaliveInterval_Type(Integer32):
    """Custom type fsRoamGroupKeepaliveInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_FsRoamGroupKeepaliveInterval_Type.__name__ = "Integer32"
_FsRoamGroupKeepaliveInterval_Object = MibTableColumn
fsRoamGroupKeepaliveInterval = _FsRoamGroupKeepaliveInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 7),
    _FsRoamGroupKeepaliveInterval_Type()
)
fsRoamGroupKeepaliveInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamGroupKeepaliveInterval.setStatus("current")
_FsRoamGroupIsFast_Type = Integer32
_FsRoamGroupIsFast_Object = MibTableColumn
fsRoamGroupIsFast = _FsRoamGroupIsFast_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 8),
    _FsRoamGroupIsFast_Type()
)
fsRoamGroupIsFast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamGroupIsFast.setStatus("current")
_FsRoamGroupCreateStatus_Type = RowStatus
_FsRoamGroupCreateStatus_Object = MibTableColumn
fsRoamGroupCreateStatus = _FsRoamGroupCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 9),
    _FsRoamGroupCreateStatus_Type()
)
fsRoamGroupCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamGroupCreateStatus.setStatus("current")
_FsRoamGroupMyAddressIPv6_Type = Ipv6Address
_FsRoamGroupMyAddressIPv6_Object = MibTableColumn
fsRoamGroupMyAddressIPv6 = _FsRoamGroupMyAddressIPv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 1, 1, 10),
    _FsRoamGroupMyAddressIPv6_Type()
)
fsRoamGroupMyAddressIPv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamGroupMyAddressIPv6.setStatus("current")
_FsMobilityMemberEntryTable_Object = MibTable
fsMobilityMemberEntryTable = _FsMobilityMemberEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsMobilityMemberEntryTable.setStatus("current")
_FsMobilityMemberEntry_Object = MibTableRow
fsMobilityMemberEntry = _FsMobilityMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1)
)
fsMobilityMemberEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberGroupId"),
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberPeerAddress"),
)
if mibBuilder.loadTexts:
    fsMobilityMemberEntry.setStatus("current")


class _FsRoamMemberGroupId_Type(Integer32):
    """Custom type fsRoamMemberGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FsRoamMemberGroupId_Type.__name__ = "Integer32"
_FsRoamMemberGroupId_Object = MibTableColumn
fsRoamMemberGroupId = _FsRoamMemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 1),
    _FsRoamMemberGroupId_Type()
)
fsRoamMemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamMemberGroupId.setStatus("current")
_FsRoamMemberPeerAddress_Type = IpAddress
_FsRoamMemberPeerAddress_Object = MibTableColumn
fsRoamMemberPeerAddress = _FsRoamMemberPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 2),
    _FsRoamMemberPeerAddress_Type()
)
fsRoamMemberPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamMemberPeerAddress.setStatus("current")


class _FsRoamMemberIsList_Type(Integer32):
    """Custom type fsRoamMemberIsList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRoamMemberIsList_Type.__name__ = "Integer32"
_FsRoamMemberIsList_Object = MibTableColumn
fsRoamMemberIsList = _FsRoamMemberIsList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 3),
    _FsRoamMemberIsList_Type()
)
fsRoamMemberIsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamMemberIsList.setStatus("current")


class _FsRoamMemberDataChannelIsOK_Type(Integer32):
    """Custom type fsRoamMemberDataChannelIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRoamMemberDataChannelIsOK_Type.__name__ = "Integer32"
_FsRoamMemberDataChannelIsOK_Object = MibTableColumn
fsRoamMemberDataChannelIsOK = _FsRoamMemberDataChannelIsOK_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 4),
    _FsRoamMemberDataChannelIsOK_Type()
)
fsRoamMemberDataChannelIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamMemberDataChannelIsOK.setStatus("current")
_FsRoamMemberDataChannelFailTimes_Type = Integer32
_FsRoamMemberDataChannelFailTimes_Object = MibTableColumn
fsRoamMemberDataChannelFailTimes = _FsRoamMemberDataChannelFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 5),
    _FsRoamMemberDataChannelFailTimes_Type()
)
fsRoamMemberDataChannelFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamMemberDataChannelFailTimes.setStatus("current")
_FsRoamMemberDTLSIsClient_Type = Integer32
_FsRoamMemberDTLSIsClient_Object = MibTableColumn
fsRoamMemberDTLSIsClient = _FsRoamMemberDTLSIsClient_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 6),
    _FsRoamMemberDTLSIsClient_Type()
)
fsRoamMemberDTLSIsClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamMemberDTLSIsClient.setStatus("current")


class _FsRoamMemberDTLSIsOK_Type(Integer32):
    """Custom type fsRoamMemberDTLSIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRoamMemberDTLSIsOK_Type.__name__ = "Integer32"
_FsRoamMemberDTLSIsOK_Object = MibTableColumn
fsRoamMemberDTLSIsOK = _FsRoamMemberDTLSIsOK_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 7),
    _FsRoamMemberDTLSIsOK_Type()
)
fsRoamMemberDTLSIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamMemberDTLSIsOK.setStatus("current")
_FsRoamMemberCreateStatus_Type = RowStatus
_FsRoamMemberCreateStatus_Object = MibTableColumn
fsRoamMemberCreateStatus = _FsRoamMemberCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 2, 1, 8),
    _FsRoamMemberCreateStatus_Type()
)
fsRoamMemberCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamMemberCreateStatus.setStatus("current")
_FsAPCtrlCreatEntryTable_Object = MibTable
fsAPCtrlCreatEntryTable = _FsAPCtrlCreatEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsAPCtrlCreatEntryTable.setStatus("current")
_FsAPCtrlCreatEntry_Object = MibTableRow
fsAPCtrlCreatEntry = _FsAPCtrlCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1)
)
fsAPCtrlCreatEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsAPName"),
)
if mibBuilder.loadTexts:
    fsAPCtrlCreatEntry.setStatus("current")
_FsAPName_Type = DisplayString
_FsAPName_Object = MibTableColumn
fsAPName = _FsAPName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 1),
    _FsAPName_Type()
)
fsAPName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsAPName.setStatus("current")


class _FsPriority_Type(Integer32):
    """Custom type fsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_FsPriority_Type.__name__ = "Integer32"
_FsPriority_Object = MibTableColumn
fsPriority = _FsPriority_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 2),
    _FsPriority_Type()
)
fsPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPriority.setStatus("current")
_FsPrimaryACIP_Type = IpAddress
_FsPrimaryACIP_Object = MibTableColumn
fsPrimaryACIP = _FsPrimaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 3),
    _FsPrimaryACIP_Type()
)
fsPrimaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPrimaryACIP.setStatus("current")
_FsPrimaryACName_Type = DisplayString
_FsPrimaryACName_Object = MibTableColumn
fsPrimaryACName = _FsPrimaryACName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 4),
    _FsPrimaryACName_Type()
)
fsPrimaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPrimaryACName.setStatus("current")
_FsSecondaryACIP_Type = IpAddress
_FsSecondaryACIP_Object = MibTableColumn
fsSecondaryACIP = _FsSecondaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 5),
    _FsSecondaryACIP_Type()
)
fsSecondaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecondaryACIP.setStatus("current")
_FsSecondaryACName_Type = DisplayString
_FsSecondaryACName_Object = MibTableColumn
fsSecondaryACName = _FsSecondaryACName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 6),
    _FsSecondaryACName_Type()
)
fsSecondaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecondaryACName.setStatus("current")
_FsTertiaryACIP_Type = IpAddress
_FsTertiaryACIP_Object = MibTableColumn
fsTertiaryACIP = _FsTertiaryACIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 7),
    _FsTertiaryACIP_Type()
)
fsTertiaryACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTertiaryACIP.setStatus("current")
_FsTertiaryACName_Type = DisplayString
_FsTertiaryACName_Object = MibTableColumn
fsTertiaryACName = _FsTertiaryACName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 8),
    _FsTertiaryACName_Type()
)
fsTertiaryACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTertiaryACName.setStatus("current")
_FsAPCtrlCreatStatus_Type = RowStatus
_FsAPCtrlCreatStatus_Object = MibTableColumn
fsAPCtrlCreatStatus = _FsAPCtrlCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 3, 1, 9),
    _FsAPCtrlCreatStatus_Type()
)
fsAPCtrlCreatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAPCtrlCreatStatus.setStatus("current")
_FsWLANCtrlCreatEntryTable_Object = MibTable
fsWLANCtrlCreatEntryTable = _FsWLANCtrlCreatEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fsWLANCtrlCreatEntryTable.setStatus("current")
_FsWLANCtrlCreatEntry_Object = MibTableRow
fsWLANCtrlCreatEntry = _FsWLANCtrlCreatEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 4, 1)
)
fsWLANCtrlCreatEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsWLANID"),
)
if mibBuilder.loadTexts:
    fsWLANCtrlCreatEntry.setStatus("current")
_FsWLANID_Type = Integer32
_FsWLANID_Object = MibTableColumn
fsWLANID = _FsWLANID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 4, 1, 1),
    _FsWLANID_Type()
)
fsWLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWLANID.setStatus("current")
_FsAnchorACIPaddr_Type = IpAddress
_FsAnchorACIPaddr_Object = MibTableColumn
fsAnchorACIPaddr = _FsAnchorACIPaddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 4, 1, 2),
    _FsAnchorACIPaddr_Type()
)
fsAnchorACIPaddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAnchorACIPaddr.setStatus("current")
_FsWLANCtrlCreatStatus_Type = RowStatus
_FsWLANCtrlCreatStatus_Object = MibTableColumn
fsWLANCtrlCreatStatus = _FsWLANCtrlCreatStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 4, 1, 3),
    _FsWLANCtrlCreatStatus_Type()
)
fsWLANCtrlCreatStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsWLANCtrlCreatStatus.setStatus("current")
_FsAnchorACIPaddrIPv6_Type = Ipv6Address
_FsAnchorACIPaddrIPv6_Object = MibTableColumn
fsAnchorACIPaddrIPv6 = _FsAnchorACIPaddrIPv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 4, 1, 4),
    _FsAnchorACIPaddrIPv6_Type()
)
fsAnchorACIPaddrIPv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsAnchorACIPaddrIPv6.setStatus("current")
_FsMobilityACPing_Type = IpAddress
_FsMobilityACPing_Object = MibScalar
fsMobilityACPing = _FsMobilityACPing_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 5),
    _FsMobilityACPing_Type()
)
fsMobilityACPing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMobilityACPing.setStatus("current")
_FsGlobalHandoffRequestsReceived_Type = Integer32
_FsGlobalHandoffRequestsReceived_Object = MibScalar
fsGlobalHandoffRequestsReceived = _FsGlobalHandoffRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 6),
    _FsGlobalHandoffRequestsReceived_Type()
)
fsGlobalHandoffRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalHandoffRequestsReceived.setStatus("current")
_FsGlobalHandoffEndRequestsReceived_Type = Integer32
_FsGlobalHandoffEndRequestsReceived_Object = MibScalar
fsGlobalHandoffEndRequestsReceived = _FsGlobalHandoffEndRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 7),
    _FsGlobalHandoffEndRequestsReceived_Type()
)
fsGlobalHandoffEndRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalHandoffEndRequestsReceived.setStatus("current")
_FsGlobalStateTransitionsDisabled_Type = Integer32
_FsGlobalStateTransitionsDisabled_Object = MibScalar
fsGlobalStateTransitionsDisabled = _FsGlobalStateTransitionsDisabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 8),
    _FsGlobalStateTransitionsDisabled_Type()
)
fsGlobalStateTransitionsDisabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalStateTransitionsDisabled.setStatus("current")
_FsGlobalResourceUnavailable_Type = Integer32
_FsGlobalResourceUnavailable_Object = MibScalar
fsGlobalResourceUnavailable = _FsGlobalResourceUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 9),
    _FsGlobalResourceUnavailable_Type()
)
fsGlobalResourceUnavailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGlobalResourceUnavailable.setStatus("current")
_FsRespondeHandoffRequestIgnored_Type = Integer32
_FsRespondeHandoffRequestIgnored_Object = MibScalar
fsRespondeHandoffRequestIgnored = _FsRespondeHandoffRequestIgnored_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 10),
    _FsRespondeHandoffRequestIgnored_Type()
)
fsRespondeHandoffRequestIgnored.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeHandoffRequestIgnored.setStatus("current")
_FsRespondePingPongHandoffRequestsDropped_Type = Integer32
_FsRespondePingPongHandoffRequestsDropped_Object = MibScalar
fsRespondePingPongHandoffRequestsDropped = _FsRespondePingPongHandoffRequestsDropped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 11),
    _FsRespondePingPongHandoffRequestsDropped_Type()
)
fsRespondePingPongHandoffRequestsDropped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondePingPongHandoffRequestsDropped.setStatus("current")
_FsRespondeHandoffRequestsDroped_Type = Integer32
_FsRespondeHandoffRequestsDroped_Object = MibScalar
fsRespondeHandoffRequestsDroped = _FsRespondeHandoffRequestsDroped_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 12),
    _FsRespondeHandoffRequestsDroped_Type()
)
fsRespondeHandoffRequestsDroped.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeHandoffRequestsDroped.setStatus("current")
_FsRespondeHandoffRequestsDenied_Type = Integer32
_FsRespondeHandoffRequestsDenied_Object = MibScalar
fsRespondeHandoffRequestsDenied = _FsRespondeHandoffRequestsDenied_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 13),
    _FsRespondeHandoffRequestsDenied_Type()
)
fsRespondeHandoffRequestsDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeHandoffRequestsDenied.setStatus("current")
_FsRespondeClientHandoffasLocal_Type = Integer32
_FsRespondeClientHandoffasLocal_Object = MibScalar
fsRespondeClientHandoffasLocal = _FsRespondeClientHandoffasLocal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 14),
    _FsRespondeClientHandoffasLocal_Type()
)
fsRespondeClientHandoffasLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeClientHandoffasLocal.setStatus("current")
_FsRespondeClientHandoffasForeign_Type = Integer32
_FsRespondeClientHandoffasForeign_Object = MibScalar
fsRespondeClientHandoffasForeign = _FsRespondeClientHandoffasForeign_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 15),
    _FsRespondeClientHandoffasForeign_Type()
)
fsRespondeClientHandoffasForeign.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeClientHandoffasForeign.setStatus("current")
_FsRespondeAnchorRequestsReceived_Type = Integer32
_FsRespondeAnchorRequestsReceived_Object = MibScalar
fsRespondeAnchorRequestsReceived = _FsRespondeAnchorRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 16),
    _FsRespondeAnchorRequestsReceived_Type()
)
fsRespondeAnchorRequestsReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeAnchorRequestsReceived.setStatus("current")
_FsRespondeAnchorRequestDenied_Type = Integer32
_FsRespondeAnchorRequestDenied_Object = MibScalar
fsRespondeAnchorRequestDenied = _FsRespondeAnchorRequestDenied_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 17),
    _FsRespondeAnchorRequestDenied_Type()
)
fsRespondeAnchorRequestDenied.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeAnchorRequestDenied.setStatus("current")
_FsRespondeAnchorTransferred_Type = Integer32
_FsRespondeAnchorTransferred_Object = MibScalar
fsRespondeAnchorTransferred = _FsRespondeAnchorTransferred_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 18),
    _FsRespondeAnchorTransferred_Type()
)
fsRespondeAnchorTransferred.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsRespondeAnchorTransferred.setStatus("current")
_FsInitHandoffRequestsSent_Type = Integer32
_FsInitHandoffRequestsSent_Object = MibScalar
fsInitHandoffRequestsSent = _FsInitHandoffRequestsSent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 19),
    _FsInitHandoffRequestsSent_Type()
)
fsInitHandoffRequestsSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsInitHandoffRequestsSent.setStatus("current")
_FsInitHandoffReplyReceived_Type = Integer32
_FsInitHandoffReplyReceived_Object = MibScalar
fsInitHandoffReplyReceived = _FsInitHandoffReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 20),
    _FsInitHandoffReplyReceived_Type()
)
fsInitHandoffReplyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsInitHandoffReplyReceived.setStatus("current")
_FsInitHandoffasLocalReceived_Type = Integer32
_FsInitHandoffasLocalReceived_Object = MibScalar
fsInitHandoffasLocalReceived = _FsInitHandoffasLocalReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 21),
    _FsInitHandoffasLocalReceived_Type()
)
fsInitHandoffasLocalReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsInitHandoffasLocalReceived.setStatus("current")
_FsInitHandoffasForeignReceived_Type = Integer32
_FsInitHandoffasForeignReceived_Object = MibScalar
fsInitHandoffasForeignReceived = _FsInitHandoffasForeignReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 22),
    _FsInitHandoffasForeignReceived_Type()
)
fsInitHandoffasForeignReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsInitHandoffasForeignReceived.setStatus("current")
_FsInitHandoffDenyReceived_Type = Integer32
_FsInitHandoffDenyReceived_Object = MibScalar
fsInitHandoffDenyReceived = _FsInitHandoffDenyReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 23),
    _FsInitHandoffDenyReceived_Type()
)
fsInitHandoffDenyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsInitHandoffDenyReceived.setStatus("current")
_FsInitAnchorRequestSent_Type = Integer32
_FsInitAnchorRequestSent_Object = MibScalar
fsInitAnchorRequestSent = _FsInitAnchorRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 24),
    _FsInitAnchorRequestSent_Type()
)
fsInitAnchorRequestSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsInitAnchorRequestSent.setStatus("current")
_FsInitAnchorDenyReceived_Type = Integer32
_FsInitAnchorDenyReceived_Object = MibScalar
fsInitAnchorDenyReceived = _FsInitAnchorDenyReceived_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 25),
    _FsInitAnchorDenyReceived_Type()
)
fsInitAnchorDenyReceived.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsInitAnchorDenyReceived.setStatus("current")
_FsAPPriorityEnable_Type = Integer32
_FsAPPriorityEnable_Object = MibScalar
fsAPPriorityEnable = _FsAPPriorityEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 26),
    _FsAPPriorityEnable_Type()
)
fsAPPriorityEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsAPPriorityEnable.setStatus("current")
_FsPrimaryBackUpACIP_Type = IpAddress
_FsPrimaryBackUpACIP_Object = MibScalar
fsPrimaryBackUpACIP = _FsPrimaryBackUpACIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 27),
    _FsPrimaryBackUpACIP_Type()
)
fsPrimaryBackUpACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPrimaryBackUpACIP.setStatus("current")
_FsPrimaryBackUpACName_Type = DisplayString
_FsPrimaryBackUpACName_Object = MibScalar
fsPrimaryBackUpACName = _FsPrimaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 28),
    _FsPrimaryBackUpACName_Type()
)
fsPrimaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPrimaryBackUpACName.setStatus("current")
_FsSecondaryBackUpACIP_Type = IpAddress
_FsSecondaryBackUpACIP_Object = MibScalar
fsSecondaryBackUpACIP = _FsSecondaryBackUpACIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 29),
    _FsSecondaryBackUpACIP_Type()
)
fsSecondaryBackUpACIP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecondaryBackUpACIP.setStatus("current")
_FsSecondaryBackUpACName_Type = DisplayString
_FsSecondaryBackUpACName_Object = MibScalar
fsSecondaryBackUpACName = _FsSecondaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 30),
    _FsSecondaryBackUpACName_Type()
)
fsSecondaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecondaryBackUpACName.setStatus("current")
_FsTeriaryBackUpACip_Type = IpAddress
_FsTeriaryBackUpACip_Object = MibScalar
fsTeriaryBackUpACip = _FsTeriaryBackUpACip_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 31),
    _FsTeriaryBackUpACip_Type()
)
fsTeriaryBackUpACip.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeriaryBackUpACip.setStatus("current")
_FsTeriaryBackUpACName_Type = DisplayString
_FsTeriaryBackUpACName_Object = MibScalar
fsTeriaryBackUpACName = _FsTeriaryBackUpACName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 32),
    _FsTeriaryBackUpACName_Type()
)
fsTeriaryBackUpACName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTeriaryBackUpACName.setStatus("current")
_FsACIntraRoam_Type = Counter32
_FsACIntraRoam_Object = MibScalar
fsACIntraRoam = _FsACIntraRoam_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 33),
    _FsACIntraRoam_Type()
)
fsACIntraRoam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsACIntraRoam.setStatus("current")
_FsACInterRoamIn_Type = Counter32
_FsACInterRoamIn_Object = MibScalar
fsACInterRoamIn = _FsACInterRoamIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 34),
    _FsACInterRoamIn_Type()
)
fsACInterRoamIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsACInterRoamIn.setStatus("current")
_FsACInterRoamOut_Type = Counter32
_FsACInterRoamOut_Object = MibScalar
fsACInterRoamOut = _FsACInterRoamOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 35),
    _FsACInterRoamOut_Type()
)
fsACInterRoamOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsACInterRoamOut.setStatus("current")
_FsMobilityACPingIPv6_Type = Ipv6Address
_FsMobilityACPingIPv6_Object = MibScalar
fsMobilityACPingIPv6 = _FsMobilityACPingIPv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 36),
    _FsMobilityACPingIPv6_Type()
)
fsMobilityACPingIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMobilityACPingIPv6.setStatus("current")
_FsMobilityIPv6MemberEntryTable_Object = MibTable
fsMobilityIPv6MemberEntryTable = _FsMobilityIPv6MemberEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37)
)
if mibBuilder.loadTexts:
    fsMobilityIPv6MemberEntryTable.setStatus("current")
_FsMobilityIPv6MemberEntry_Object = MibTableRow
fsMobilityIPv6MemberEntry = _FsMobilityIPv6MemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1)
)
fsMobilityIPv6MemberEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberGroupId"),
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberPeerAddress"),
)
if mibBuilder.loadTexts:
    fsMobilityIPv6MemberEntry.setStatus("current")


class _FsRoamIPv6MemberGroupId_Type(Integer32):
    """Custom type fsRoamIPv6MemberGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_FsRoamIPv6MemberGroupId_Type.__name__ = "Integer32"
_FsRoamIPv6MemberGroupId_Object = MibTableColumn
fsRoamIPv6MemberGroupId = _FsRoamIPv6MemberGroupId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 1),
    _FsRoamIPv6MemberGroupId_Type()
)
fsRoamIPv6MemberGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberGroupId.setStatus("current")
_FsRoamIPv6MemberPeerAddress_Type = Ipv6Address
_FsRoamIPv6MemberPeerAddress_Object = MibTableColumn
fsRoamIPv6MemberPeerAddress = _FsRoamIPv6MemberPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 2),
    _FsRoamIPv6MemberPeerAddress_Type()
)
fsRoamIPv6MemberPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberPeerAddress.setStatus("current")


class _FsRoamIPv6MemberIsList_Type(Integer32):
    """Custom type fsRoamIPv6MemberIsList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRoamIPv6MemberIsList_Type.__name__ = "Integer32"
_FsRoamIPv6MemberIsList_Object = MibTableColumn
fsRoamIPv6MemberIsList = _FsRoamIPv6MemberIsList_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 3),
    _FsRoamIPv6MemberIsList_Type()
)
fsRoamIPv6MemberIsList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberIsList.setStatus("current")


class _FsRoamIPv6MemberDataChannelIsOK_Type(Integer32):
    """Custom type fsRoamIPv6MemberDataChannelIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRoamIPv6MemberDataChannelIsOK_Type.__name__ = "Integer32"
_FsRoamIPv6MemberDataChannelIsOK_Object = MibTableColumn
fsRoamIPv6MemberDataChannelIsOK = _FsRoamIPv6MemberDataChannelIsOK_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 4),
    _FsRoamIPv6MemberDataChannelIsOK_Type()
)
fsRoamIPv6MemberDataChannelIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberDataChannelIsOK.setStatus("current")
_FsRoamIPv6MemberDataChannelFailTimes_Type = Integer32
_FsRoamIPv6MemberDataChannelFailTimes_Object = MibTableColumn
fsRoamIPv6MemberDataChannelFailTimes = _FsRoamIPv6MemberDataChannelFailTimes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 5),
    _FsRoamIPv6MemberDataChannelFailTimes_Type()
)
fsRoamIPv6MemberDataChannelFailTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberDataChannelFailTimes.setStatus("current")
_FsRoamIPv6MemberDTLSIsClient_Type = Integer32
_FsRoamIPv6MemberDTLSIsClient_Object = MibTableColumn
fsRoamIPv6MemberDTLSIsClient = _FsRoamIPv6MemberDTLSIsClient_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 6),
    _FsRoamIPv6MemberDTLSIsClient_Type()
)
fsRoamIPv6MemberDTLSIsClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberDTLSIsClient.setStatus("current")


class _FsRoamIPv6MemberDTLSIsOK_Type(Integer32):
    """Custom type fsRoamIPv6MemberDTLSIsOK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsRoamIPv6MemberDTLSIsOK_Type.__name__ = "Integer32"
_FsRoamIPv6MemberDTLSIsOK_Object = MibTableColumn
fsRoamIPv6MemberDTLSIsOK = _FsRoamIPv6MemberDTLSIsOK_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 7),
    _FsRoamIPv6MemberDTLSIsOK_Type()
)
fsRoamIPv6MemberDTLSIsOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberDTLSIsOK.setStatus("current")
_FsRoamIPv6MemberCreateStatus_Type = RowStatus
_FsRoamIPv6MemberCreateStatus_Object = MibTableColumn
fsRoamIPv6MemberCreateStatus = _FsRoamIPv6MemberCreateStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 37, 1, 8),
    _FsRoamIPv6MemberCreateStatus_Type()
)
fsRoamIPv6MemberCreateStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsRoamIPv6MemberCreateStatus.setStatus("current")
_FsMobilityUserEntryTable_Object = MibTable
fsMobilityUserEntryTable = _FsMobilityUserEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38)
)
if mibBuilder.loadTexts:
    fsMobilityUserEntryTable.setStatus("current")
_FsMobilityUserEntry_Object = MibTableRow
fsMobilityUserEntry = _FsMobilityUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1)
)
fsMobilityUserEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamUserMac"),
)
if mibBuilder.loadTexts:
    fsMobilityUserEntry.setStatus("current")
_FsRoamUserMac_Type = MacAddress
_FsRoamUserMac_Object = MibTableColumn
fsRoamUserMac = _FsRoamUserMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 1),
    _FsRoamUserMac_Type()
)
fsRoamUserMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserMac.setStatus("current")
_FsRoamUserRoamType_Type = Integer32
_FsRoamUserRoamType_Object = MibTableColumn
fsRoamUserRoamType = _FsRoamUserRoamType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 2),
    _FsRoamUserRoamType_Type()
)
fsRoamUserRoamType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamType.setStatus("current")
_FsRoamUserRoamOutAcAddressType_Type = InetAddressType
_FsRoamUserRoamOutAcAddressType_Object = MibTableColumn
fsRoamUserRoamOutAcAddressType = _FsRoamUserRoamOutAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 3),
    _FsRoamUserRoamOutAcAddressType_Type()
)
fsRoamUserRoamOutAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamOutAcAddressType.setStatus("current")
_FsRoamUserRoamOutAcAddress_Type = InetAddress
_FsRoamUserRoamOutAcAddress_Object = MibTableColumn
fsRoamUserRoamOutAcAddress = _FsRoamUserRoamOutAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 4),
    _FsRoamUserRoamOutAcAddress_Type()
)
fsRoamUserRoamOutAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamOutAcAddress.setStatus("current")
_FsRoamUserRoamInAcAddressType_Type = InetAddressType
_FsRoamUserRoamInAcAddressType_Object = MibTableColumn
fsRoamUserRoamInAcAddressType = _FsRoamUserRoamInAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 5),
    _FsRoamUserRoamInAcAddressType_Type()
)
fsRoamUserRoamInAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamInAcAddressType.setStatus("current")
_FsRoamUserRoamInAcAddress_Type = InetAddress
_FsRoamUserRoamInAcAddress_Object = MibTableColumn
fsRoamUserRoamInAcAddress = _FsRoamUserRoamInAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 6),
    _FsRoamUserRoamInAcAddress_Type()
)
fsRoamUserRoamInAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamInAcAddress.setStatus("current")
_FsRoamUserRoamOutApMac_Type = MacAddress
_FsRoamUserRoamOutApMac_Object = MibTableColumn
fsRoamUserRoamOutApMac = _FsRoamUserRoamOutApMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 7),
    _FsRoamUserRoamOutApMac_Type()
)
fsRoamUserRoamOutApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamOutApMac.setStatus("current")
_FsRoamUserRoamInApMac_Type = MacAddress
_FsRoamUserRoamInApMac_Object = MibTableColumn
fsRoamUserRoamInApMac = _FsRoamUserRoamInApMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 8),
    _FsRoamUserRoamInApMac_Type()
)
fsRoamUserRoamInApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamInApMac.setStatus("current")
_FsRoamUserRoamOutVid_Type = Integer32
_FsRoamUserRoamOutVid_Object = MibTableColumn
fsRoamUserRoamOutVid = _FsRoamUserRoamOutVid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 9),
    _FsRoamUserRoamOutVid_Type()
)
fsRoamUserRoamOutVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamOutVid.setStatus("current")
_FsRoamUserRoamInVid_Type = Integer32
_FsRoamUserRoamInVid_Object = MibTableColumn
fsRoamUserRoamInVid = _FsRoamUserRoamInVid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 38, 1, 10),
    _FsRoamUserRoamInVid_Type()
)
fsRoamUserRoamInVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamUserRoamInVid.setStatus("current")
_FsMobilityTrackEntryTable_Object = MibTable
fsMobilityTrackEntryTable = _FsMobilityTrackEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39)
)
if mibBuilder.loadTexts:
    fsMobilityTrackEntryTable.setStatus("current")
_FsMobilityTrackEntry_Object = MibTableRow
fsMobilityTrackEntry = _FsMobilityTrackEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1)
)
fsMobilityTrackEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackStaMac"),
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackId"),
)
if mibBuilder.loadTexts:
    fsMobilityTrackEntry.setStatus("current")
_FsRoamTrackStaMac_Type = MacAddress
_FsRoamTrackStaMac_Object = MibTableColumn
fsRoamTrackStaMac = _FsRoamTrackStaMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 1),
    _FsRoamTrackStaMac_Type()
)
fsRoamTrackStaMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackStaMac.setStatus("current")
_FsRoamTrackId_Type = Integer32
_FsRoamTrackId_Object = MibTableColumn
fsRoamTrackId = _FsRoamTrackId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 2),
    _FsRoamTrackId_Type()
)
fsRoamTrackId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackId.setStatus("current")
_FsRoamTrackAcAddressType_Type = InetAddressType
_FsRoamTrackAcAddressType_Object = MibTableColumn
fsRoamTrackAcAddressType = _FsRoamTrackAcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 3),
    _FsRoamTrackAcAddressType_Type()
)
fsRoamTrackAcAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackAcAddressType.setStatus("current")
_FsRoamTrackAcAddress_Type = InetAddress
_FsRoamTrackAcAddress_Object = MibTableColumn
fsRoamTrackAcAddress = _FsRoamTrackAcAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 4),
    _FsRoamTrackAcAddress_Type()
)
fsRoamTrackAcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackAcAddress.setStatus("current")
_FsRoamTrackApMac_Type = MacAddress
_FsRoamTrackApMac_Object = MibTableColumn
fsRoamTrackApMac = _FsRoamTrackApMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 5),
    _FsRoamTrackApMac_Type()
)
fsRoamTrackApMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackApMac.setStatus("current")
_FsRoamTrackRadioId_Type = Integer32
_FsRoamTrackRadioId_Object = MibTableColumn
fsRoamTrackRadioId = _FsRoamTrackRadioId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 6),
    _FsRoamTrackRadioId_Type()
)
fsRoamTrackRadioId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackRadioId.setStatus("current")
_FsRoamTrackStaIp_Type = IpAddress
_FsRoamTrackStaIp_Object = MibTableColumn
fsRoamTrackStaIp = _FsRoamTrackStaIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 7),
    _FsRoamTrackStaIp_Type()
)
fsRoamTrackStaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackStaIp.setStatus("current")
_FsRoamTrackStaIpv6_Type = Ipv6Address
_FsRoamTrackStaIpv6_Object = MibTableColumn
fsRoamTrackStaIpv6 = _FsRoamTrackStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 8),
    _FsRoamTrackStaIpv6_Type()
)
fsRoamTrackStaIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackStaIpv6.setStatus("current")
_FsRoamTrackStaOnlineTime_Type = Integer32
_FsRoamTrackStaOnlineTime_Object = MibTableColumn
fsRoamTrackStaOnlineTime = _FsRoamTrackStaOnlineTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 39, 1, 9),
    _FsRoamTrackStaOnlineTime_Type()
)
fsRoamTrackStaOnlineTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsRoamTrackStaOnlineTime.setStatus("current")
_FsMobilityUserJsonTable_Object = MibTable
fsMobilityUserJsonTable = _FsMobilityUserJsonTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 40)
)
if mibBuilder.loadTexts:
    fsMobilityUserJsonTable.setStatus("current")
_FsMobilityUserJsonEntry_Object = MibTableRow
fsMobilityUserJsonEntry = _FsMobilityUserJsonEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 40, 1)
)
fsMobilityUserJsonEntry.setIndexNames(
    (0, "FS-CAPWAP-MOBILITY-MIB", "fsMobilityUserJsonMacAddr"),
)
if mibBuilder.loadTexts:
    fsMobilityUserJsonEntry.setStatus("current")
_FsMobilityUserJsonMacAddr_Type = MacAddress
_FsMobilityUserJsonMacAddr_Object = MibTableColumn
fsMobilityUserJsonMacAddr = _FsMobilityUserJsonMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 40, 1, 1),
    _FsMobilityUserJsonMacAddr_Type()
)
fsMobilityUserJsonMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMobilityUserJsonMacAddr.setStatus("current")


class _FsMobilityUserJsonContent_Type(OctetString):
    """Custom type fsMobilityUserJsonContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1023),
    )


_FsMobilityUserJsonContent_Type.__name__ = "OctetString"
_FsMobilityUserJsonContent_Object = MibTableColumn
fsMobilityUserJsonContent = _FsMobilityUserJsonContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 1, 40, 1, 2),
    _FsMobilityUserJsonContent_Type()
)
fsMobilityUserJsonContent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMobilityUserJsonContent.setStatus("current")
_FsMobilityIf_ObjectIdentity = ObjectIdentity
fsMobilityIf = _FsMobilityIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 2)
)
_FsMobilityMIBCompliances_ObjectIdentity = ObjectIdentity
fsMobilityMIBCompliances = _FsMobilityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 2, 1)
)
_FsMobilityMIBGroups_ObjectIdentity = ObjectIdentity
fsMobilityMIBGroups = _FsMobilityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 2, 2)
)
_FsMobilityTrap_ObjectIdentity = ObjectIdentity
fsMobilityTrap = _FsMobilityTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3)
)
_FsMobilityTrapSta_ObjectIdentity = ObjectIdentity
fsMobilityTrapSta = _FsMobilityTrapSta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1)
)
_FsMobilityNotifyApMac_Type = MacAddress
_FsMobilityNotifyApMac_Object = MibScalar
fsMobilityNotifyApMac = _FsMobilityNotifyApMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 1),
    _FsMobilityNotifyApMac_Type()
)
fsMobilityNotifyApMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyApMac.setStatus("current")
_FsMobilityNotifyStaMac_Type = MacAddress
_FsMobilityNotifyStaMac_Object = MibScalar
fsMobilityNotifyStaMac = _FsMobilityNotifyStaMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 2),
    _FsMobilityNotifyStaMac_Type()
)
fsMobilityNotifyStaMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaMac.setStatus("current")
_FsMobilityNotifyApIp_Type = IpAddress
_FsMobilityNotifyApIp_Object = MibScalar
fsMobilityNotifyApIp = _FsMobilityNotifyApIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 3),
    _FsMobilityNotifyApIp_Type()
)
fsMobilityNotifyApIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyApIp.setStatus("current")
_FsMobilityNotifyStaIp_Type = IpAddress
_FsMobilityNotifyStaIp_Object = MibScalar
fsMobilityNotifyStaIp = _FsMobilityNotifyStaIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 4),
    _FsMobilityNotifyStaIp_Type()
)
fsMobilityNotifyStaIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaIp.setStatus("current")
_FsMobilityNotifyStaOperType_Type = Integer32
_FsMobilityNotifyStaOperType_Object = MibScalar
fsMobilityNotifyStaOperType = _FsMobilityNotifyStaOperType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 5),
    _FsMobilityNotifyStaOperType_Type()
)
fsMobilityNotifyStaOperType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaOperType.setStatus("current")


class _FsMobilityNotifyStaApRadioId_Type(Integer32):
    """Custom type fsMobilityNotifyStaApRadioId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsMobilityNotifyStaApRadioId_Type.__name__ = "Integer32"
_FsMobilityNotifyStaApRadioId_Object = MibScalar
fsMobilityNotifyStaApRadioId = _FsMobilityNotifyStaApRadioId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 6),
    _FsMobilityNotifyStaApRadioId_Type()
)
fsMobilityNotifyStaApRadioId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaApRadioId.setStatus("current")


class _FsMobilityNotifyStaApRadioType_Type(Integer32):
    """Custom type fsMobilityNotifyStaApRadioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_FsMobilityNotifyStaApRadioType_Type.__name__ = "Integer32"
_FsMobilityNotifyStaApRadioType_Object = MibScalar
fsMobilityNotifyStaApRadioType = _FsMobilityNotifyStaApRadioType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 7),
    _FsMobilityNotifyStaApRadioType_Type()
)
fsMobilityNotifyStaApRadioType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaApRadioType.setStatus("current")


class _FsMobilityNotifyStaVlanId_Type(Integer32):
    """Custom type fsMobilityNotifyStaVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMobilityNotifyStaVlanId_Type.__name__ = "Integer32"
_FsMobilityNotifyStaVlanId_Object = MibScalar
fsMobilityNotifyStaVlanId = _FsMobilityNotifyStaVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 8),
    _FsMobilityNotifyStaVlanId_Type()
)
fsMobilityNotifyStaVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaVlanId.setStatus("current")


class _FsMobilityNotifyStaWlanId_Type(Integer32):
    """Custom type fsMobilityNotifyStaWlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_FsMobilityNotifyStaWlanId_Type.__name__ = "Integer32"
_FsMobilityNotifyStaWlanId_Object = MibScalar
fsMobilityNotifyStaWlanId = _FsMobilityNotifyStaWlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 9),
    _FsMobilityNotifyStaWlanId_Type()
)
fsMobilityNotifyStaWlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaWlanId.setStatus("current")
_FsMobilityNotifyStaIpv6_Type = Ipv6Address
_FsMobilityNotifyStaIpv6_Object = MibScalar
fsMobilityNotifyStaIpv6 = _FsMobilityNotifyStaIpv6_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 10),
    _FsMobilityNotifyStaIpv6_Type()
)
fsMobilityNotifyStaIpv6.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaIpv6.setStatus("current")


class _FsMobilityNotifyStaAssoAuthMode_Type(Integer32):
    """Custom type fsMobilityNotifyStaAssoAuthMode based on Integer32"""
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


_FsMobilityNotifyStaAssoAuthMode_Type.__name__ = "Integer32"
_FsMobilityNotifyStaAssoAuthMode_Object = MibScalar
fsMobilityNotifyStaAssoAuthMode = _FsMobilityNotifyStaAssoAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 11),
    _FsMobilityNotifyStaAssoAuthMode_Type()
)
fsMobilityNotifyStaAssoAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaAssoAuthMode.setStatus("current")


class _FsMobilityNotifyStaNetAuthMode_Type(Integer32):
    """Custom type fsMobilityNotifyStaNetAuthMode based on Integer32"""
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


_FsMobilityNotifyStaNetAuthMode_Type.__name__ = "Integer32"
_FsMobilityNotifyStaNetAuthMode_Object = MibScalar
fsMobilityNotifyStaNetAuthMode = _FsMobilityNotifyStaNetAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 12),
    _FsMobilityNotifyStaNetAuthMode_Type()
)
fsMobilityNotifyStaNetAuthMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaNetAuthMode.setStatus("current")
_FsMobilityNotifyStaSsid_Type = DisplayString
_FsMobilityNotifyStaSsid_Object = MibScalar
fsMobilityNotifyStaSsid = _FsMobilityNotifyStaSsid_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 13),
    _FsMobilityNotifyStaSsid_Type()
)
fsMobilityNotifyStaSsid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaSsid.setStatus("current")
_FsMobilityNotifyStaLinkRate_Type = Integer32
_FsMobilityNotifyStaLinkRate_Object = MibScalar
fsMobilityNotifyStaLinkRate = _FsMobilityNotifyStaLinkRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 14),
    _FsMobilityNotifyStaLinkRate_Type()
)
fsMobilityNotifyStaLinkRate.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaLinkRate.setStatus("current")
_FsMobilityNotifyStaCurChan_Type = Integer32
_FsMobilityNotifyStaCurChan_Object = MibScalar
fsMobilityNotifyStaCurChan = _FsMobilityNotifyStaCurChan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 15),
    _FsMobilityNotifyStaCurChan_Type()
)
fsMobilityNotifyStaCurChan.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaCurChan.setStatus("current")
_FsMobilityNotifyStaClientType_Type = DisplayString
_FsMobilityNotifyStaClientType_Object = MibScalar
fsMobilityNotifyStaClientType = _FsMobilityNotifyStaClientType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 16),
    _FsMobilityNotifyStaClientType_Type()
)
fsMobilityNotifyStaClientType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaClientType.setStatus("current")
_FsMobilityNotifyStaRssi_Type = Integer32
_FsMobilityNotifyStaRssi_Object = MibScalar
fsMobilityNotifyStaRssi = _FsMobilityNotifyStaRssi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 17),
    _FsMobilityNotifyStaRssi_Type()
)
fsMobilityNotifyStaRssi.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaRssi.setStatus("current")
_FsMobilityNotifyStaReason_Type = DisplayString
_FsMobilityNotifyStaReason_Object = MibScalar
fsMobilityNotifyStaReason = _FsMobilityNotifyStaReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 1, 18),
    _FsMobilityNotifyStaReason_Type()
)
fsMobilityNotifyStaReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsMobilityNotifyStaReason.setStatus("current")
_FsMobilityTrapStaIf_ObjectIdentity = ObjectIdentity
fsMobilityTrapStaIf = _FsMobilityTrapStaIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 2)
)

# Managed Objects groups

fsMobilityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 2, 2, 1)
)
fsMobilityMIBGroup.setObjects(
      *(("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupName"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupMyAddress"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupMcEnable"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupMcAddress"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupKeepaliveCount"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupKeepaliveInterval"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupIsFast"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamGroupCreateStatus"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberIsList"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberDataChannelIsOK"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberDataChannelFailTimes"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberDTLSIsClient"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberDTLSIsOK"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamMemberCreateStatus"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsPriority"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsPrimaryACIP"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsPrimaryACName"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsSecondaryACIP"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsSecondaryACName"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsTertiaryACIP"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsTertiaryACName"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsAPCtrlCreatStatus"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsAnchorACIPaddr"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsWLANCtrlCreatStatus"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsGlobalHandoffRequestsReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsGlobalHandoffEndRequestsReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsGlobalStateTransitionsDisabled"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsGlobalResourceUnavailable"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeHandoffRequestIgnored"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondePingPongHandoffRequestsDropped"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeHandoffRequestsDroped"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeHandoffRequestsDenied"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeClientHandoffasLocal"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeClientHandoffasForeign"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeAnchorRequestsReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeAnchorRequestDenied"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRespondeAnchorTransferred"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsInitHandoffRequestsSent"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsInitHandoffReplyReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsInitHandoffasLocalReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsInitHandoffasForeignReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsInitHandoffDenyReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsInitAnchorRequestSent"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsInitAnchorDenyReceived"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsAPPriorityEnable"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsPrimaryBackUpACIP"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsPrimaryBackUpACName"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsSecondaryBackUpACIP"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsSecondaryBackUpACName"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsTeriaryBackUpACip"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsTeriaryBackUpACName"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsACIntraRoam"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsACInterRoamIn"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsACInterRoamOut"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityACPingIPv6"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberGroupId"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberPeerAddress"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberIsList"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberDataChannelIsOK"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberDataChannelFailTimes"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberDTLSIsClient"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberDTLSIsOK"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamIPv6MemberCreateStatus"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserMac"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamType"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamOutAcAddressType"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamOutAcAddress"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamInAcAddressType"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamInAcAddress"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamOutApMac"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamInApMac"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamOutVid"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamUserRoamInVid"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackStaMac"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackId"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackAcAddressType"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackAcAddress"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackApMac"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackRadioId"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackStaIp"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackStaIpv6"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsRoamTrackStaOnlineTime"))
)
if mibBuilder.loadTexts:
    fsMobilityMIBGroup.setStatus("current")


# Notification objects

fsMobilityNotifyStaOper = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 3, 2, 1)
)
fsMobilityNotifyStaOper.setObjects(
      *(("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyApMac"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaMac"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyApIp"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaIp"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaOperType"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaApRadioId"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaApRadioType"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaVlanId"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaWlanId"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaIpv6"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaAssoAuthMode"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaNetAuthMode"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaSsid"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaLinkRate"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaCurChan"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaClientType"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaRssi"),
        ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityNotifyStaReason"))
)
if mibBuilder.loadTexts:
    fsMobilityNotifyStaOper.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsMobilityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 64, 1, 2, 1, 1)
)
fsMobilityMIBCompliance.setObjects(
    ("FS-CAPWAP-MOBILITY-MIB", "fsMobilityMIBGroup")
)
if mibBuilder.loadTexts:
    fsMobilityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-CAPWAP-MOBILITY-MIB",
    **{"fsMobilityMIB": fsMobilityMIB,
       "fsMobilityMIBObjects": fsMobilityMIBObjects,
       "fsMobility": fsMobility,
       "fsMobilityEntryTable": fsMobilityEntryTable,
       "fsMobilityEntry": fsMobilityEntry,
       "fsRoamGroupId": fsRoamGroupId,
       "fsRoamGroupName": fsRoamGroupName,
       "fsRoamGroupMyAddress": fsRoamGroupMyAddress,
       "fsRoamGroupMcEnable": fsRoamGroupMcEnable,
       "fsRoamGroupMcAddress": fsRoamGroupMcAddress,
       "fsRoamGroupKeepaliveCount": fsRoamGroupKeepaliveCount,
       "fsRoamGroupKeepaliveInterval": fsRoamGroupKeepaliveInterval,
       "fsRoamGroupIsFast": fsRoamGroupIsFast,
       "fsRoamGroupCreateStatus": fsRoamGroupCreateStatus,
       "fsRoamGroupMyAddressIPv6": fsRoamGroupMyAddressIPv6,
       "fsMobilityMemberEntryTable": fsMobilityMemberEntryTable,
       "fsMobilityMemberEntry": fsMobilityMemberEntry,
       "fsRoamMemberGroupId": fsRoamMemberGroupId,
       "fsRoamMemberPeerAddress": fsRoamMemberPeerAddress,
       "fsRoamMemberIsList": fsRoamMemberIsList,
       "fsRoamMemberDataChannelIsOK": fsRoamMemberDataChannelIsOK,
       "fsRoamMemberDataChannelFailTimes": fsRoamMemberDataChannelFailTimes,
       "fsRoamMemberDTLSIsClient": fsRoamMemberDTLSIsClient,
       "fsRoamMemberDTLSIsOK": fsRoamMemberDTLSIsOK,
       "fsRoamMemberCreateStatus": fsRoamMemberCreateStatus,
       "fsAPCtrlCreatEntryTable": fsAPCtrlCreatEntryTable,
       "fsAPCtrlCreatEntry": fsAPCtrlCreatEntry,
       "fsAPName": fsAPName,
       "fsPriority": fsPriority,
       "fsPrimaryACIP": fsPrimaryACIP,
       "fsPrimaryACName": fsPrimaryACName,
       "fsSecondaryACIP": fsSecondaryACIP,
       "fsSecondaryACName": fsSecondaryACName,
       "fsTertiaryACIP": fsTertiaryACIP,
       "fsTertiaryACName": fsTertiaryACName,
       "fsAPCtrlCreatStatus": fsAPCtrlCreatStatus,
       "fsWLANCtrlCreatEntryTable": fsWLANCtrlCreatEntryTable,
       "fsWLANCtrlCreatEntry": fsWLANCtrlCreatEntry,
       "fsWLANID": fsWLANID,
       "fsAnchorACIPaddr": fsAnchorACIPaddr,
       "fsWLANCtrlCreatStatus": fsWLANCtrlCreatStatus,
       "fsAnchorACIPaddrIPv6": fsAnchorACIPaddrIPv6,
       "fsMobilityACPing": fsMobilityACPing,
       "fsGlobalHandoffRequestsReceived": fsGlobalHandoffRequestsReceived,
       "fsGlobalHandoffEndRequestsReceived": fsGlobalHandoffEndRequestsReceived,
       "fsGlobalStateTransitionsDisabled": fsGlobalStateTransitionsDisabled,
       "fsGlobalResourceUnavailable": fsGlobalResourceUnavailable,
       "fsRespondeHandoffRequestIgnored": fsRespondeHandoffRequestIgnored,
       "fsRespondePingPongHandoffRequestsDropped": fsRespondePingPongHandoffRequestsDropped,
       "fsRespondeHandoffRequestsDroped": fsRespondeHandoffRequestsDroped,
       "fsRespondeHandoffRequestsDenied": fsRespondeHandoffRequestsDenied,
       "fsRespondeClientHandoffasLocal": fsRespondeClientHandoffasLocal,
       "fsRespondeClientHandoffasForeign": fsRespondeClientHandoffasForeign,
       "fsRespondeAnchorRequestsReceived": fsRespondeAnchorRequestsReceived,
       "fsRespondeAnchorRequestDenied": fsRespondeAnchorRequestDenied,
       "fsRespondeAnchorTransferred": fsRespondeAnchorTransferred,
       "fsInitHandoffRequestsSent": fsInitHandoffRequestsSent,
       "fsInitHandoffReplyReceived": fsInitHandoffReplyReceived,
       "fsInitHandoffasLocalReceived": fsInitHandoffasLocalReceived,
       "fsInitHandoffasForeignReceived": fsInitHandoffasForeignReceived,
       "fsInitHandoffDenyReceived": fsInitHandoffDenyReceived,
       "fsInitAnchorRequestSent": fsInitAnchorRequestSent,
       "fsInitAnchorDenyReceived": fsInitAnchorDenyReceived,
       "fsAPPriorityEnable": fsAPPriorityEnable,
       "fsPrimaryBackUpACIP": fsPrimaryBackUpACIP,
       "fsPrimaryBackUpACName": fsPrimaryBackUpACName,
       "fsSecondaryBackUpACIP": fsSecondaryBackUpACIP,
       "fsSecondaryBackUpACName": fsSecondaryBackUpACName,
       "fsTeriaryBackUpACip": fsTeriaryBackUpACip,
       "fsTeriaryBackUpACName": fsTeriaryBackUpACName,
       "fsACIntraRoam": fsACIntraRoam,
       "fsACInterRoamIn": fsACInterRoamIn,
       "fsACInterRoamOut": fsACInterRoamOut,
       "fsMobilityACPingIPv6": fsMobilityACPingIPv6,
       "fsMobilityIPv6MemberEntryTable": fsMobilityIPv6MemberEntryTable,
       "fsMobilityIPv6MemberEntry": fsMobilityIPv6MemberEntry,
       "fsRoamIPv6MemberGroupId": fsRoamIPv6MemberGroupId,
       "fsRoamIPv6MemberPeerAddress": fsRoamIPv6MemberPeerAddress,
       "fsRoamIPv6MemberIsList": fsRoamIPv6MemberIsList,
       "fsRoamIPv6MemberDataChannelIsOK": fsRoamIPv6MemberDataChannelIsOK,
       "fsRoamIPv6MemberDataChannelFailTimes": fsRoamIPv6MemberDataChannelFailTimes,
       "fsRoamIPv6MemberDTLSIsClient": fsRoamIPv6MemberDTLSIsClient,
       "fsRoamIPv6MemberDTLSIsOK": fsRoamIPv6MemberDTLSIsOK,
       "fsRoamIPv6MemberCreateStatus": fsRoamIPv6MemberCreateStatus,
       "fsMobilityUserEntryTable": fsMobilityUserEntryTable,
       "fsMobilityUserEntry": fsMobilityUserEntry,
       "fsRoamUserMac": fsRoamUserMac,
       "fsRoamUserRoamType": fsRoamUserRoamType,
       "fsRoamUserRoamOutAcAddressType": fsRoamUserRoamOutAcAddressType,
       "fsRoamUserRoamOutAcAddress": fsRoamUserRoamOutAcAddress,
       "fsRoamUserRoamInAcAddressType": fsRoamUserRoamInAcAddressType,
       "fsRoamUserRoamInAcAddress": fsRoamUserRoamInAcAddress,
       "fsRoamUserRoamOutApMac": fsRoamUserRoamOutApMac,
       "fsRoamUserRoamInApMac": fsRoamUserRoamInApMac,
       "fsRoamUserRoamOutVid": fsRoamUserRoamOutVid,
       "fsRoamUserRoamInVid": fsRoamUserRoamInVid,
       "fsMobilityTrackEntryTable": fsMobilityTrackEntryTable,
       "fsMobilityTrackEntry": fsMobilityTrackEntry,
       "fsRoamTrackStaMac": fsRoamTrackStaMac,
       "fsRoamTrackId": fsRoamTrackId,
       "fsRoamTrackAcAddressType": fsRoamTrackAcAddressType,
       "fsRoamTrackAcAddress": fsRoamTrackAcAddress,
       "fsRoamTrackApMac": fsRoamTrackApMac,
       "fsRoamTrackRadioId": fsRoamTrackRadioId,
       "fsRoamTrackStaIp": fsRoamTrackStaIp,
       "fsRoamTrackStaIpv6": fsRoamTrackStaIpv6,
       "fsRoamTrackStaOnlineTime": fsRoamTrackStaOnlineTime,
       "fsMobilityUserJsonTable": fsMobilityUserJsonTable,
       "fsMobilityUserJsonEntry": fsMobilityUserJsonEntry,
       "fsMobilityUserJsonMacAddr": fsMobilityUserJsonMacAddr,
       "fsMobilityUserJsonContent": fsMobilityUserJsonContent,
       "fsMobilityIf": fsMobilityIf,
       "fsMobilityMIBCompliances": fsMobilityMIBCompliances,
       "fsMobilityMIBCompliance": fsMobilityMIBCompliance,
       "fsMobilityMIBGroups": fsMobilityMIBGroups,
       "fsMobilityMIBGroup": fsMobilityMIBGroup,
       "fsMobilityTrap": fsMobilityTrap,
       "fsMobilityTrapSta": fsMobilityTrapSta,
       "fsMobilityNotifyApMac": fsMobilityNotifyApMac,
       "fsMobilityNotifyStaMac": fsMobilityNotifyStaMac,
       "fsMobilityNotifyApIp": fsMobilityNotifyApIp,
       "fsMobilityNotifyStaIp": fsMobilityNotifyStaIp,
       "fsMobilityNotifyStaOperType": fsMobilityNotifyStaOperType,
       "fsMobilityNotifyStaApRadioId": fsMobilityNotifyStaApRadioId,
       "fsMobilityNotifyStaApRadioType": fsMobilityNotifyStaApRadioType,
       "fsMobilityNotifyStaVlanId": fsMobilityNotifyStaVlanId,
       "fsMobilityNotifyStaWlanId": fsMobilityNotifyStaWlanId,
       "fsMobilityNotifyStaIpv6": fsMobilityNotifyStaIpv6,
       "fsMobilityNotifyStaAssoAuthMode": fsMobilityNotifyStaAssoAuthMode,
       "fsMobilityNotifyStaNetAuthMode": fsMobilityNotifyStaNetAuthMode,
       "fsMobilityNotifyStaSsid": fsMobilityNotifyStaSsid,
       "fsMobilityNotifyStaLinkRate": fsMobilityNotifyStaLinkRate,
       "fsMobilityNotifyStaCurChan": fsMobilityNotifyStaCurChan,
       "fsMobilityNotifyStaClientType": fsMobilityNotifyStaClientType,
       "fsMobilityNotifyStaRssi": fsMobilityNotifyStaRssi,
       "fsMobilityNotifyStaReason": fsMobilityNotifyStaReason,
       "fsMobilityTrapStaIf": fsMobilityTrapStaIf,
       "fsMobilityNotifyStaOper": fsMobilityNotifyStaOper}
)
