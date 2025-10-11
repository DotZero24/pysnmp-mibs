# SNMP MIB module (FS-SMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:59 2025
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

(Community,) = mibBuilder.importSymbols(
    "FS-SNMP-AGENT-MIB",
    "Community")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

fsSMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39)
)
if mibBuilder.loadTexts:
    fsSMPMIB.setRevisions(
        ("2004-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSMPMIBObjects_ObjectIdentity = ObjectIdentity
fsSMPMIBObjects = _FsSMPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1)
)
_FsSMPServer_Type = IpAddress
_FsSMPServer_Object = MibScalar
fsSMPServer = _FsSMPServer_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 1),
    _FsSMPServer_Type()
)
fsSMPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPServer.setStatus("current")
_FsSMPServerKey_Type = Community
_FsSMPServerKey_Object = MibScalar
fsSMPServerKey = _FsSMPServerKey_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 2),
    _FsSMPServerKey_Type()
)
fsSMPServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPServerKey.setStatus("current")
_FsSMPEventSendSlice_Type = Unsigned32
_FsSMPEventSendSlice_Object = MibScalar
fsSMPEventSendSlice = _FsSMPEventSendSlice_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 3),
    _FsSMPEventSendSlice_Type()
)
fsSMPEventSendSlice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPEventSendSlice.setStatus("current")
_FsSMPPolicyDelete_Type = Integer32
_FsSMPPolicyDelete_Object = MibScalar
fsSMPPolicyDelete = _FsSMPPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 4),
    _FsSMPPolicyDelete_Type()
)
fsSMPPolicyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyDelete.setStatus("current")


class _FsSMPPolicyChecksum_Type(OctetString):
    """Custom type fsSMPPolicyChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsSMPPolicyChecksum_Type.__name__ = "OctetString"
_FsSMPPolicyChecksum_Object = MibScalar
fsSMPPolicyChecksum = _FsSMPPolicyChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 5),
    _FsSMPPolicyChecksum_Type()
)
fsSMPPolicyChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSMPPolicyChecksum.setStatus("current")
_FsSMPPolicyTimeout_Type = Unsigned32
_FsSMPPolicyTimeout_Object = MibScalar
fsSMPPolicyTimeout = _FsSMPPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 6),
    _FsSMPPolicyTimeout_Type()
)
fsSMPPolicyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyTimeout.setStatus("current")
_FsSMPFrameRelayTable_Object = MibTable
fsSMPFrameRelayTable = _FsSMPFrameRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 7)
)
if mibBuilder.loadTexts:
    fsSMPFrameRelayTable.setStatus("current")
_FsSMPFrameRelayEntry_Object = MibTableRow
fsSMPFrameRelayEntry = _FsSMPFrameRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 7, 1)
)
fsSMPFrameRelayEntry.setIndexNames(
    (0, "FS-SMP-MIB", "fsSMPFrameRelayIndex"),
)
if mibBuilder.loadTexts:
    fsSMPFrameRelayEntry.setStatus("current")
_FsSMPFrameRelayIndex_Type = Unsigned32
_FsSMPFrameRelayIndex_Object = MibTableColumn
fsSMPFrameRelayIndex = _FsSMPFrameRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 7, 1, 1),
    _FsSMPFrameRelayIndex_Type()
)
fsSMPFrameRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSMPFrameRelayIndex.setStatus("current")


class _FsSMPFrameRelayContent_Type(OctetString):
    """Custom type fsSMPFrameRelayContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FsSMPFrameRelayContent_Type.__name__ = "OctetString"
_FsSMPFrameRelayContent_Object = MibTableColumn
fsSMPFrameRelayContent = _FsSMPFrameRelayContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 7, 1, 2),
    _FsSMPFrameRelayContent_Type()
)
fsSMPFrameRelayContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPFrameRelayContent.setStatus("current")
_FsSMPFrameRelayLength_Type = Unsigned32
_FsSMPFrameRelayLength_Object = MibTableColumn
fsSMPFrameRelayLength = _FsSMPFrameRelayLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 7, 1, 3),
    _FsSMPFrameRelayLength_Type()
)
fsSMPFrameRelayLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPFrameRelayLength.setStatus("current")
_FsSMPFrameRelayDestPort_Type = IfIndex
_FsSMPFrameRelayDestPort_Object = MibTableColumn
fsSMPFrameRelayDestPort = _FsSMPFrameRelayDestPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 7, 1, 4),
    _FsSMPFrameRelayDestPort_Type()
)
fsSMPFrameRelayDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPFrameRelayDestPort.setStatus("current")
_FsSMPFrameRelayDestVlan_Type = VlanId
_FsSMPFrameRelayDestVlan_Object = MibTableColumn
fsSMPFrameRelayDestVlan = _FsSMPFrameRelayDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 7, 1, 5),
    _FsSMPFrameRelayDestVlan_Type()
)
fsSMPFrameRelayDestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPFrameRelayDestVlan.setStatus("current")
_FsSMPPolicyTable_Object = MibTable
fsSMPPolicyTable = _FsSMPPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8)
)
if mibBuilder.loadTexts:
    fsSMPPolicyTable.setStatus("current")
_FsSMPPolicyEntry_Object = MibTableRow
fsSMPPolicyEntry = _FsSMPPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1)
)
fsSMPPolicyEntry.setIndexNames(
    (0, "FS-SMP-MIB", "fsSMPGroupIndex"),
    (0, "FS-SMP-MIB", "fsSMPPolicyIndex"),
)
if mibBuilder.loadTexts:
    fsSMPPolicyEntry.setStatus("current")
_FsSMPGroupIndex_Type = Unsigned32
_FsSMPGroupIndex_Object = MibTableColumn
fsSMPGroupIndex = _FsSMPGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 1),
    _FsSMPGroupIndex_Type()
)
fsSMPGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSMPGroupIndex.setStatus("current")
_FsSMPPolicyIndex_Type = Unsigned32
_FsSMPPolicyIndex_Object = MibTableColumn
fsSMPPolicyIndex = _FsSMPPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 2),
    _FsSMPPolicyIndex_Type()
)
fsSMPPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSMPPolicyIndex.setStatus("current")
_FsSMPPolicyStatus_Type = ConfigStatus
_FsSMPPolicyStatus_Object = MibTableColumn
fsSMPPolicyStatus = _FsSMPPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 3),
    _FsSMPPolicyStatus_Type()
)
fsSMPPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyStatus.setStatus("current")
_FsSMPPolicyNumber_Type = Unsigned32
_FsSMPPolicyNumber_Object = MibTableColumn
fsSMPPolicyNumber = _FsSMPPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 4),
    _FsSMPPolicyNumber_Type()
)
fsSMPPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyNumber.setStatus("current")
_FsSMPPolicyInstallPort_Type = IfIndex
_FsSMPPolicyInstallPort_Object = MibTableColumn
fsSMPPolicyInstallPort = _FsSMPPolicyInstallPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 5),
    _FsSMPPolicyInstallPort_Type()
)
fsSMPPolicyInstallPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyInstallPort.setStatus("current")


class _FsSMPPolicyType_Type(Integer32):
    """Custom type fsSMPPolicyType based on Integer32"""
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
        *(("hi-isolate", 1),
          ("isolate", 2),
          ("blocked", 3),
          ("addrBind", 4))
    )


_FsSMPPolicyType_Type.__name__ = "Integer32"
_FsSMPPolicyType_Object = MibTableColumn
fsSMPPolicyType = _FsSMPPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 6),
    _FsSMPPolicyType_Type()
)
fsSMPPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyType.setStatus("current")


class _FsSMPPolicyContent_Type(OctetString):
    """Custom type fsSMPPolicyContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_FsSMPPolicyContent_Type.__name__ = "OctetString"
_FsSMPPolicyContent_Object = MibTableColumn
fsSMPPolicyContent = _FsSMPPolicyContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 7),
    _FsSMPPolicyContent_Type()
)
fsSMPPolicyContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyContent.setStatus("current")


class _FsSMPPolicyMask_Type(OctetString):
    """Custom type fsSMPPolicyMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_FsSMPPolicyMask_Type.__name__ = "OctetString"
_FsSMPPolicyMask_Object = MibTableColumn
fsSMPPolicyMask = _FsSMPPolicyMask_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 8),
    _FsSMPPolicyMask_Type()
)
fsSMPPolicyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyMask.setStatus("current")


class _FsSMPPolicyName_Type(DisplayString):
    """Custom type fsSMPPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsSMPPolicyName_Type.__name__ = "DisplayString"
_FsSMPPolicyName_Object = MibTableColumn
fsSMPPolicyName = _FsSMPPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 8, 1, 9),
    _FsSMPPolicyName_Type()
)
fsSMPPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSMPPolicyName.setStatus("current")
_FsSMPPolicyGroupTable_Object = MibTable
fsSMPPolicyGroupTable = _FsSMPPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 9)
)
if mibBuilder.loadTexts:
    fsSMPPolicyGroupTable.setStatus("current")
_FsSMPPolicyGroupEntry_Object = MibTableRow
fsSMPPolicyGroupEntry = _FsSMPPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 9, 1)
)
fsSMPPolicyGroupEntry.setIndexNames(
    (0, "FS-SMP-MIB", "fsSMPPolicyGroupIndex"),
)
if mibBuilder.loadTexts:
    fsSMPPolicyGroupEntry.setStatus("current")
_FsSMPPolicyGroupIndex_Type = Unsigned32
_FsSMPPolicyGroupIndex_Object = MibTableColumn
fsSMPPolicyGroupIndex = _FsSMPPolicyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 9, 1, 1),
    _FsSMPPolicyGroupIndex_Type()
)
fsSMPPolicyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSMPPolicyGroupIndex.setStatus("current")
_FsSMPPolicyGroupCount_Type = Unsigned32
_FsSMPPolicyGroupCount_Object = MibTableColumn
fsSMPPolicyGroupCount = _FsSMPPolicyGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 9, 1, 2),
    _FsSMPPolicyGroupCount_Type()
)
fsSMPPolicyGroupCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSMPPolicyGroupCount.setStatus("current")


class _FsSMPPolicyGroupChecksum_Type(OctetString):
    """Custom type fsSMPPolicyGroupChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsSMPPolicyGroupChecksum_Type.__name__ = "OctetString"
_FsSMPPolicyGroupChecksum_Object = MibTableColumn
fsSMPPolicyGroupChecksum = _FsSMPPolicyGroupChecksum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 9, 1, 3),
    _FsSMPPolicyGroupChecksum_Type()
)
fsSMPPolicyGroupChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSMPPolicyGroupChecksum.setStatus("current")
_FsSMPPolicyGroupStatus_Type = RowStatus
_FsSMPPolicyGroupStatus_Object = MibTableColumn
fsSMPPolicyGroupStatus = _FsSMPPolicyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 1, 9, 1, 4),
    _FsSMPPolicyGroupStatus_Type()
)
fsSMPPolicyGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSMPPolicyGroupStatus.setStatus("current")
_FsEGMIBObjects_ObjectIdentity = ObjectIdentity
fsEGMIBObjects = _FsEGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2)
)
_FsEGUserTable_Object = MibTable
fsEGUserTable = _FsEGUserTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1)
)
if mibBuilder.loadTexts:
    fsEGUserTable.setStatus("current")
_FsEGUserEntry_Object = MibTableRow
fsEGUserEntry = _FsEGUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1)
)
fsEGUserEntry.setIndexNames(
    (0, "FS-SMP-MIB", "fsEGUserIpAddrType"),
    (0, "FS-SMP-MIB", "fsEGUserIpAddr"),
)
if mibBuilder.loadTexts:
    fsEGUserEntry.setStatus("current")
_FsEGUserIpAddrType_Type = InetAddressType
_FsEGUserIpAddrType_Object = MibTableColumn
fsEGUserIpAddrType = _FsEGUserIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 1),
    _FsEGUserIpAddrType_Type()
)
fsEGUserIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEGUserIpAddrType.setStatus("current")
_FsEGUserIpAddr_Type = InetAddress
_FsEGUserIpAddr_Object = MibTableColumn
fsEGUserIpAddr = _FsEGUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 2),
    _FsEGUserIpAddr_Type()
)
fsEGUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsEGUserIpAddr.setStatus("current")


class _FsEGUserId_Type(OctetString):
    """Custom type fsEGUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsEGUserId_Type.__name__ = "OctetString"
_FsEGUserId_Object = MibTableColumn
fsEGUserId = _FsEGUserId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 3),
    _FsEGUserId_Type()
)
fsEGUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGUserId.setStatus("current")


class _FsEGUserName_Type(OctetString):
    """Custom type fsEGUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsEGUserName_Type.__name__ = "OctetString"
_FsEGUserName_Object = MibTableColumn
fsEGUserName = _FsEGUserName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 4),
    _FsEGUserName_Type()
)
fsEGUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGUserName.setStatus("current")


class _FsEGUserGroupName_Type(OctetString):
    """Custom type fsEGUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_FsEGUserGroupName_Type.__name__ = "OctetString"
_FsEGUserGroupName_Object = MibTableColumn
fsEGUserGroupName = _FsEGUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 5),
    _FsEGUserGroupName_Type()
)
fsEGUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGUserGroupName.setStatus("current")
_FsEGUserMac_Type = MacAddress
_FsEGUserMac_Object = MibTableColumn
fsEGUserMac = _FsEGUserMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 6),
    _FsEGUserMac_Type()
)
fsEGUserMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGUserMac.setStatus("current")
_FsEGNasIp_Type = InetAddress
_FsEGNasIp_Object = MibTableColumn
fsEGNasIp = _FsEGNasIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 7),
    _FsEGNasIp_Type()
)
fsEGNasIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGNasIp.setStatus("current")
_FsEGNasPort_Type = Gauge32
_FsEGNasPort_Object = MibTableColumn
fsEGNasPort = _FsEGNasPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 8),
    _FsEGNasPort_Type()
)
fsEGNasPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGNasPort.setStatus("current")
_FsEGGatewayIp_Type = InetAddress
_FsEGGatewayIp_Object = MibTableColumn
fsEGGatewayIp = _FsEGGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 9),
    _FsEGGatewayIp_Type()
)
fsEGGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGGatewayIp.setStatus("current")
_FsEGVlanId_Type = Gauge32
_FsEGVlanId_Object = MibTableColumn
fsEGVlanId = _FsEGVlanId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 10),
    _FsEGVlanId_Type()
)
fsEGVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGVlanId.setStatus("current")
_FsEGLoginTime_Type = OctetString
_FsEGLoginTime_Object = MibTableColumn
fsEGLoginTime = _FsEGLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 11),
    _FsEGLoginTime_Type()
)
fsEGLoginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGLoginTime.setStatus("current")
_FsEGLogoutTime_Type = OctetString
_FsEGLogoutTime_Object = MibTableColumn
fsEGLogoutTime = _FsEGLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 12),
    _FsEGLogoutTime_Type()
)
fsEGLogoutTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGLogoutTime.setStatus("current")
_FsEGMessageType_Type = Gauge32
_FsEGMessageType_Object = MibTableColumn
fsEGMessageType = _FsEGMessageType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 13),
    _FsEGMessageType_Type()
)
fsEGMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGMessageType.setStatus("current")
_FsEGUserStatus_Type = RowStatus
_FsEGUserStatus_Object = MibTableColumn
fsEGUserStatus = _FsEGUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 1, 1, 14),
    _FsEGUserStatus_Type()
)
fsEGUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEGUserStatus.setStatus("current")
_FsEGUserDelete_Type = Integer32
_FsEGUserDelete_Object = MibScalar
fsEGUserDelete = _FsEGUserDelete_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 2, 2),
    _FsEGUserDelete_Type()
)
fsEGUserDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEGUserDelete.setStatus("current")
_FsSMPMIBConformance_ObjectIdentity = ObjectIdentity
fsSMPMIBConformance = _FsSMPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3)
)
_FsSMPMIBCompliances_ObjectIdentity = ObjectIdentity
fsSMPMIBCompliances = _FsSMPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3, 1)
)
_FsSMPMIBGroups_ObjectIdentity = ObjectIdentity
fsSMPMIBGroups = _FsSMPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3, 2)
)
_FsSMPTraps_ObjectIdentity = ObjectIdentity
fsSMPTraps = _FsSMPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535)
)
_FsSMPSwitchIP_Type = IpAddress
_FsSMPSwitchIP_Object = MibScalar
fsSMPSwitchIP = _FsSMPSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 1),
    _FsSMPSwitchIP_Type()
)
fsSMPSwitchIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPSwitchIP.setStatus("current")
_FsSMPSwitchInterfaceID_Type = IfIndex
_FsSMPSwitchInterfaceID_Object = MibScalar
fsSMPSwitchInterfaceID = _FsSMPSwitchInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 2),
    _FsSMPSwitchInterfaceID_Type()
)
fsSMPSwitchInterfaceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPSwitchInterfaceID.setStatus("current")
_FsSMPSwitchInterfaceVLANID_Type = VlanId
_FsSMPSwitchInterfaceVLANID_Object = MibScalar
fsSMPSwitchInterfaceVLANID = _FsSMPSwitchInterfaceVLANID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 3),
    _FsSMPSwitchInterfaceVLANID_Type()
)
fsSMPSwitchInterfaceVLANID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPSwitchInterfaceVLANID.setStatus("current")
_FsSMPFrameContentLength_Type = Unsigned32
_FsSMPFrameContentLength_Object = MibScalar
fsSMPFrameContentLength = _FsSMPFrameContentLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 4),
    _FsSMPFrameContentLength_Type()
)
fsSMPFrameContentLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPFrameContentLength.setStatus("current")


class _FsSMPFrameContent_Type(OctetString):
    """Custom type fsSMPFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_FsSMPFrameContent_Type.__name__ = "OctetString"
_FsSMPFrameContent_Object = MibScalar
fsSMPFrameContent = _FsSMPFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 5),
    _FsSMPFrameContent_Type()
)
fsSMPFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPFrameContent.setStatus("current")


class _FsSMPArpAttackSubnetIP_Type(OctetString):
    """Custom type fsSMPArpAttackSubnetIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_FsSMPArpAttackSubnetIP_Type.__name__ = "OctetString"
_FsSMPArpAttackSubnetIP_Object = MibScalar
fsSMPArpAttackSubnetIP = _FsSMPArpAttackSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 7),
    _FsSMPArpAttackSubnetIP_Type()
)
fsSMPArpAttackSubnetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackSubnetIP.setStatus("current")
_FsSMPArpAttackSubnetIPNum_Type = Integer32
_FsSMPArpAttackSubnetIPNum_Object = MibScalar
fsSMPArpAttackSubnetIPNum = _FsSMPArpAttackSubnetIPNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 8),
    _FsSMPArpAttackSubnetIPNum_Type()
)
fsSMPArpAttackSubnetIPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackSubnetIPNum.setStatus("current")
_FsSMPArpAttackInterfaceSlot_Type = Integer32
_FsSMPArpAttackInterfaceSlot_Object = MibScalar
fsSMPArpAttackInterfaceSlot = _FsSMPArpAttackInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 9),
    _FsSMPArpAttackInterfaceSlot_Type()
)
fsSMPArpAttackInterfaceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackInterfaceSlot.setStatus("current")
_FsSMPArpAttackInterfacePort_Type = Integer32
_FsSMPArpAttackInterfacePort_Object = MibScalar
fsSMPArpAttackInterfacePort = _FsSMPArpAttackInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 10),
    _FsSMPArpAttackInterfacePort_Type()
)
fsSMPArpAttackInterfacePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackInterfacePort.setStatus("current")
_FsSMPArpAttackInterfaceVlanID_Type = VlanId
_FsSMPArpAttackInterfaceVlanID_Object = MibScalar
fsSMPArpAttackInterfaceVlanID = _FsSMPArpAttackInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 11),
    _FsSMPArpAttackInterfaceVlanID_Type()
)
fsSMPArpAttackInterfaceVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackInterfaceVlanID.setStatus("current")


class _FsSMPArpAttackFrameContent_Type(OctetString):
    """Custom type fsSMPArpAttackFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsSMPArpAttackFrameContent_Type.__name__ = "OctetString"
_FsSMPArpAttackFrameContent_Object = MibScalar
fsSMPArpAttackFrameContent = _FsSMPArpAttackFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 12),
    _FsSMPArpAttackFrameContent_Type()
)
fsSMPArpAttackFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackFrameContent.setStatus("current")
_FsSMPArpAttackStatus_Type = TruthValue
_FsSMPArpAttackStatus_Object = MibScalar
fsSMPArpAttackStatus = _FsSMPArpAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 13),
    _FsSMPArpAttackStatus_Type()
)
fsSMPArpAttackStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackStatus.setStatus("current")


class _FsSMPArpAttackCriticalStatus_Type(Integer32):
    """Custom type fsSMPArpAttackCriticalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("critical", 1),
          ("emergencies", 2))
    )


_FsSMPArpAttackCriticalStatus_Type.__name__ = "Integer32"
_FsSMPArpAttackCriticalStatus_Object = MibScalar
fsSMPArpAttackCriticalStatus = _FsSMPArpAttackCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 14),
    _FsSMPArpAttackCriticalStatus_Type()
)
fsSMPArpAttackCriticalStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackCriticalStatus.setStatus("current")
_FsSMPArpAttackMac_Type = MacAddress
_FsSMPArpAttackMac_Object = MibScalar
fsSMPArpAttackMac = _FsSMPArpAttackMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 15),
    _FsSMPArpAttackMac_Type()
)
fsSMPArpAttackMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackMac.setStatus("current")
_FsSMPArpAttackInterfaceIndex_Type = Integer32
_FsSMPArpAttackInterfaceIndex_Object = MibScalar
fsSMPArpAttackInterfaceIndex = _FsSMPArpAttackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 16),
    _FsSMPArpAttackInterfaceIndex_Type()
)
fsSMPArpAttackInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsSMPArpAttackInterfaceIndex.setStatus("current")

# Managed Objects groups

fsSMPServerMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3, 2, 1)
)
fsSMPServerMibGroup.setObjects(
      *(("FS-SMP-MIB", "fsSMPServer"),
        ("FS-SMP-MIB", "fsSMPServerKey"))
)
if mibBuilder.loadTexts:
    fsSMPServerMibGroup.setStatus("current")

fsSMPClientMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3, 2, 2)
)
fsSMPClientMibGroup.setObjects(
    ("FS-SMP-MIB", "fsSMPEventSendSlice")
)
if mibBuilder.loadTexts:
    fsSMPClientMibGroup.setStatus("current")

fsSMPPolicyMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3, 2, 3)
)
fsSMPPolicyMibGroup.setObjects(
      *(("FS-SMP-MIB", "fsSMPPolicyDelete"),
        ("FS-SMP-MIB", "fsSMPPolicyChecksum"),
        ("FS-SMP-MIB", "fsSMPPolicyIndex"),
        ("FS-SMP-MIB", "fsSMPPolicyStatus"),
        ("FS-SMP-MIB", "fsSMPPolicyInstallPort"),
        ("FS-SMP-MIB", "fsSMPPolicyType"),
        ("FS-SMP-MIB", "fsSMPPolicyContent"),
        ("FS-SMP-MIB", "fsSMPPolicyMask"),
        ("FS-SMP-MIB", "fsSMPPolicyName"))
)
if mibBuilder.loadTexts:
    fsSMPPolicyMibGroup.setStatus("current")

fsSMPFrameRelayMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3, 2, 4)
)
fsSMPFrameRelayMibGroup.setObjects(
      *(("FS-SMP-MIB", "fsSMPFrameRelayIndex"),
        ("FS-SMP-MIB", "fsSMPFrameRelayContent"),
        ("FS-SMP-MIB", "fsSMPFrameRelayLength"),
        ("FS-SMP-MIB", "fsSMPFrameRelayDestPort"),
        ("FS-SMP-MIB", "fsSMPFrameRelayDestVlan"))
)
if mibBuilder.loadTexts:
    fsSMPFrameRelayMibGroup.setStatus("current")


# Notification objects

fsSMPFrameRelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 6)
)
fsSMPFrameRelayTrap.setObjects(
      *(("FS-SMP-MIB", "fsSMPSwitchIP"),
        ("FS-SMP-MIB", "fsSMPSwitchInterfaceID"),
        ("FS-SMP-MIB", "fsSMPSwitchInterfaceVLANID"),
        ("FS-SMP-MIB", "fsSMPFrameContentLength"),
        ("FS-SMP-MIB", "fsSMPFrameContent"))
)
if mibBuilder.loadTexts:
    fsSMPFrameRelayTrap.setStatus(
        "current"
    )

fsSMPArpAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 65535, 17)
)
fsSMPArpAttackTrap.setObjects(
      *(("FS-SMP-MIB", "fsSMPArpAttackSubnetIP"),
        ("FS-SMP-MIB", "fsSMPArpAttackSubnetIPNum"),
        ("FS-SMP-MIB", "fsSMPArpAttackInterfaceSlot"),
        ("FS-SMP-MIB", "fsSMPArpAttackInterfacePort"),
        ("FS-SMP-MIB", "fsSMPArpAttackInterfaceVlanID"),
        ("FS-SMP-MIB", "fsSMPArpAttackFrameContent"),
        ("FS-SMP-MIB", "fsSMPArpAttackStatus"),
        ("FS-SMP-MIB", "fsSMPArpAttackCriticalStatus"),
        ("FS-SMP-MIB", "fsSMPArpAttackMac"),
        ("FS-SMP-MIB", "fsSMPArpAttackInterfaceIndex"))
)
if mibBuilder.loadTexts:
    fsSMPArpAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 39, 3, 1, 1)
)
fsDeviceMIBCompliance.setObjects(
      *(("FS-SMP-MIB", "fsSMPServerMibGroup"),
        ("FS-SMP-MIB", "fsSMPClientMibGroup"),
        ("FS-SMP-MIB", "fsSMPPolicyMibGroup"),
        ("FS-SMP-MIB", "fsSMPFrameRelayMibGroup"))
)
if mibBuilder.loadTexts:
    fsDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SMP-MIB",
    **{"fsSMPMIB": fsSMPMIB,
       "fsSMPMIBObjects": fsSMPMIBObjects,
       "fsSMPServer": fsSMPServer,
       "fsSMPServerKey": fsSMPServerKey,
       "fsSMPEventSendSlice": fsSMPEventSendSlice,
       "fsSMPPolicyDelete": fsSMPPolicyDelete,
       "fsSMPPolicyChecksum": fsSMPPolicyChecksum,
       "fsSMPPolicyTimeout": fsSMPPolicyTimeout,
       "fsSMPFrameRelayTable": fsSMPFrameRelayTable,
       "fsSMPFrameRelayEntry": fsSMPFrameRelayEntry,
       "fsSMPFrameRelayIndex": fsSMPFrameRelayIndex,
       "fsSMPFrameRelayContent": fsSMPFrameRelayContent,
       "fsSMPFrameRelayLength": fsSMPFrameRelayLength,
       "fsSMPFrameRelayDestPort": fsSMPFrameRelayDestPort,
       "fsSMPFrameRelayDestVlan": fsSMPFrameRelayDestVlan,
       "fsSMPPolicyTable": fsSMPPolicyTable,
       "fsSMPPolicyEntry": fsSMPPolicyEntry,
       "fsSMPGroupIndex": fsSMPGroupIndex,
       "fsSMPPolicyIndex": fsSMPPolicyIndex,
       "fsSMPPolicyStatus": fsSMPPolicyStatus,
       "fsSMPPolicyNumber": fsSMPPolicyNumber,
       "fsSMPPolicyInstallPort": fsSMPPolicyInstallPort,
       "fsSMPPolicyType": fsSMPPolicyType,
       "fsSMPPolicyContent": fsSMPPolicyContent,
       "fsSMPPolicyMask": fsSMPPolicyMask,
       "fsSMPPolicyName": fsSMPPolicyName,
       "fsSMPPolicyGroupTable": fsSMPPolicyGroupTable,
       "fsSMPPolicyGroupEntry": fsSMPPolicyGroupEntry,
       "fsSMPPolicyGroupIndex": fsSMPPolicyGroupIndex,
       "fsSMPPolicyGroupCount": fsSMPPolicyGroupCount,
       "fsSMPPolicyGroupChecksum": fsSMPPolicyGroupChecksum,
       "fsSMPPolicyGroupStatus": fsSMPPolicyGroupStatus,
       "fsEGMIBObjects": fsEGMIBObjects,
       "fsEGUserTable": fsEGUserTable,
       "fsEGUserEntry": fsEGUserEntry,
       "fsEGUserIpAddrType": fsEGUserIpAddrType,
       "fsEGUserIpAddr": fsEGUserIpAddr,
       "fsEGUserId": fsEGUserId,
       "fsEGUserName": fsEGUserName,
       "fsEGUserGroupName": fsEGUserGroupName,
       "fsEGUserMac": fsEGUserMac,
       "fsEGNasIp": fsEGNasIp,
       "fsEGNasPort": fsEGNasPort,
       "fsEGGatewayIp": fsEGGatewayIp,
       "fsEGVlanId": fsEGVlanId,
       "fsEGLoginTime": fsEGLoginTime,
       "fsEGLogoutTime": fsEGLogoutTime,
       "fsEGMessageType": fsEGMessageType,
       "fsEGUserStatus": fsEGUserStatus,
       "fsEGUserDelete": fsEGUserDelete,
       "fsSMPMIBConformance": fsSMPMIBConformance,
       "fsSMPMIBCompliances": fsSMPMIBCompliances,
       "fsDeviceMIBCompliance": fsDeviceMIBCompliance,
       "fsSMPMIBGroups": fsSMPMIBGroups,
       "fsSMPServerMibGroup": fsSMPServerMibGroup,
       "fsSMPClientMibGroup": fsSMPClientMibGroup,
       "fsSMPPolicyMibGroup": fsSMPPolicyMibGroup,
       "fsSMPFrameRelayMibGroup": fsSMPFrameRelayMibGroup,
       "fsSMPTraps": fsSMPTraps,
       "fsSMPSwitchIP": fsSMPSwitchIP,
       "fsSMPSwitchInterfaceID": fsSMPSwitchInterfaceID,
       "fsSMPSwitchInterfaceVLANID": fsSMPSwitchInterfaceVLANID,
       "fsSMPFrameContentLength": fsSMPFrameContentLength,
       "fsSMPFrameContent": fsSMPFrameContent,
       "fsSMPFrameRelayTrap": fsSMPFrameRelayTrap,
       "fsSMPArpAttackSubnetIP": fsSMPArpAttackSubnetIP,
       "fsSMPArpAttackSubnetIPNum": fsSMPArpAttackSubnetIPNum,
       "fsSMPArpAttackInterfaceSlot": fsSMPArpAttackInterfaceSlot,
       "fsSMPArpAttackInterfacePort": fsSMPArpAttackInterfacePort,
       "fsSMPArpAttackInterfaceVlanID": fsSMPArpAttackInterfaceVlanID,
       "fsSMPArpAttackFrameContent": fsSMPArpAttackFrameContent,
       "fsSMPArpAttackStatus": fsSMPArpAttackStatus,
       "fsSMPArpAttackCriticalStatus": fsSMPArpAttackCriticalStatus,
       "fsSMPArpAttackMac": fsSMPArpAttackMac,
       "fsSMPArpAttackInterfaceIndex": fsSMPArpAttackInterfaceIndex,
       "fsSMPArpAttackTrap": fsSMPArpAttackTrap}
)
