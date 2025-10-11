# SNMP MIB module (QTECH-SMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:07 2025
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

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(Community,) = mibBuilder.importSymbols(
    "QTECH-SNMP-AGENT-MIB",
    "Community")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
    "ConfigStatus",
    "IfIndex")

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

qtechSMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39)
)
if mibBuilder.loadTexts:
    qtechSMPMIB.setRevisions(
        ("2004-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSMPMIBObjects_ObjectIdentity = ObjectIdentity
qtechSMPMIBObjects = _QtechSMPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1)
)
_QtechSMPServer_Type = IpAddress
_QtechSMPServer_Object = MibScalar
qtechSMPServer = _QtechSMPServer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 1),
    _QtechSMPServer_Type()
)
qtechSMPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPServer.setStatus("current")
_QtechSMPServerKey_Type = Community
_QtechSMPServerKey_Object = MibScalar
qtechSMPServerKey = _QtechSMPServerKey_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 2),
    _QtechSMPServerKey_Type()
)
qtechSMPServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPServerKey.setStatus("current")
_QtechSMPEventSendSlice_Type = Unsigned32
_QtechSMPEventSendSlice_Object = MibScalar
qtechSMPEventSendSlice = _QtechSMPEventSendSlice_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 3),
    _QtechSMPEventSendSlice_Type()
)
qtechSMPEventSendSlice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPEventSendSlice.setStatus("current")
_QtechSMPPolicyDelete_Type = Integer32
_QtechSMPPolicyDelete_Object = MibScalar
qtechSMPPolicyDelete = _QtechSMPPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 4),
    _QtechSMPPolicyDelete_Type()
)
qtechSMPPolicyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyDelete.setStatus("current")


class _QtechSMPPolicyChecksum_Type(OctetString):
    """Custom type qtechSMPPolicyChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechSMPPolicyChecksum_Type.__name__ = "OctetString"
_QtechSMPPolicyChecksum_Object = MibScalar
qtechSMPPolicyChecksum = _QtechSMPPolicyChecksum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 5),
    _QtechSMPPolicyChecksum_Type()
)
qtechSMPPolicyChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSMPPolicyChecksum.setStatus("current")
_QtechSMPPolicyTimeout_Type = Unsigned32
_QtechSMPPolicyTimeout_Object = MibScalar
qtechSMPPolicyTimeout = _QtechSMPPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 6),
    _QtechSMPPolicyTimeout_Type()
)
qtechSMPPolicyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyTimeout.setStatus("current")
_QtechSMPFrameRelayTable_Object = MibTable
qtechSMPFrameRelayTable = _QtechSMPFrameRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 7)
)
if mibBuilder.loadTexts:
    qtechSMPFrameRelayTable.setStatus("current")
_QtechSMPFrameRelayEntry_Object = MibTableRow
qtechSMPFrameRelayEntry = _QtechSMPFrameRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 7, 1)
)
qtechSMPFrameRelayEntry.setIndexNames(
    (0, "QTECH-SMP-MIB", "qtechSMPFrameRelayIndex"),
)
if mibBuilder.loadTexts:
    qtechSMPFrameRelayEntry.setStatus("current")
_QtechSMPFrameRelayIndex_Type = Unsigned32
_QtechSMPFrameRelayIndex_Object = MibTableColumn
qtechSMPFrameRelayIndex = _QtechSMPFrameRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 7, 1, 1),
    _QtechSMPFrameRelayIndex_Type()
)
qtechSMPFrameRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSMPFrameRelayIndex.setStatus("current")


class _QtechSMPFrameRelayContent_Type(OctetString):
    """Custom type qtechSMPFrameRelayContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_QtechSMPFrameRelayContent_Type.__name__ = "OctetString"
_QtechSMPFrameRelayContent_Object = MibTableColumn
qtechSMPFrameRelayContent = _QtechSMPFrameRelayContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 7, 1, 2),
    _QtechSMPFrameRelayContent_Type()
)
qtechSMPFrameRelayContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPFrameRelayContent.setStatus("current")
_QtechSMPFrameRelayLength_Type = Unsigned32
_QtechSMPFrameRelayLength_Object = MibTableColumn
qtechSMPFrameRelayLength = _QtechSMPFrameRelayLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 7, 1, 3),
    _QtechSMPFrameRelayLength_Type()
)
qtechSMPFrameRelayLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPFrameRelayLength.setStatus("current")
_QtechSMPFrameRelayDestPort_Type = IfIndex
_QtechSMPFrameRelayDestPort_Object = MibTableColumn
qtechSMPFrameRelayDestPort = _QtechSMPFrameRelayDestPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 7, 1, 4),
    _QtechSMPFrameRelayDestPort_Type()
)
qtechSMPFrameRelayDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPFrameRelayDestPort.setStatus("current")
_QtechSMPFrameRelayDestVlan_Type = VlanId
_QtechSMPFrameRelayDestVlan_Object = MibTableColumn
qtechSMPFrameRelayDestVlan = _QtechSMPFrameRelayDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 7, 1, 5),
    _QtechSMPFrameRelayDestVlan_Type()
)
qtechSMPFrameRelayDestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPFrameRelayDestVlan.setStatus("current")
_QtechSMPPolicyTable_Object = MibTable
qtechSMPPolicyTable = _QtechSMPPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8)
)
if mibBuilder.loadTexts:
    qtechSMPPolicyTable.setStatus("current")
_QtechSMPPolicyEntry_Object = MibTableRow
qtechSMPPolicyEntry = _QtechSMPPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1)
)
qtechSMPPolicyEntry.setIndexNames(
    (0, "QTECH-SMP-MIB", "qtechSMPGroupIndex"),
    (0, "QTECH-SMP-MIB", "qtechSMPPolicyIndex"),
)
if mibBuilder.loadTexts:
    qtechSMPPolicyEntry.setStatus("current")
_QtechSMPGroupIndex_Type = Unsigned32
_QtechSMPGroupIndex_Object = MibTableColumn
qtechSMPGroupIndex = _QtechSMPGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 1),
    _QtechSMPGroupIndex_Type()
)
qtechSMPGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSMPGroupIndex.setStatus("current")
_QtechSMPPolicyIndex_Type = Unsigned32
_QtechSMPPolicyIndex_Object = MibTableColumn
qtechSMPPolicyIndex = _QtechSMPPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 2),
    _QtechSMPPolicyIndex_Type()
)
qtechSMPPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSMPPolicyIndex.setStatus("current")
_QtechSMPPolicyStatus_Type = ConfigStatus
_QtechSMPPolicyStatus_Object = MibTableColumn
qtechSMPPolicyStatus = _QtechSMPPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 3),
    _QtechSMPPolicyStatus_Type()
)
qtechSMPPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyStatus.setStatus("current")
_QtechSMPPolicyNumber_Type = Unsigned32
_QtechSMPPolicyNumber_Object = MibTableColumn
qtechSMPPolicyNumber = _QtechSMPPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 4),
    _QtechSMPPolicyNumber_Type()
)
qtechSMPPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyNumber.setStatus("current")
_QtechSMPPolicyInstallPort_Type = IfIndex
_QtechSMPPolicyInstallPort_Object = MibTableColumn
qtechSMPPolicyInstallPort = _QtechSMPPolicyInstallPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 5),
    _QtechSMPPolicyInstallPort_Type()
)
qtechSMPPolicyInstallPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyInstallPort.setStatus("current")


class _QtechSMPPolicyType_Type(Integer32):
    """Custom type qtechSMPPolicyType based on Integer32"""
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


_QtechSMPPolicyType_Type.__name__ = "Integer32"
_QtechSMPPolicyType_Object = MibTableColumn
qtechSMPPolicyType = _QtechSMPPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 6),
    _QtechSMPPolicyType_Type()
)
qtechSMPPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyType.setStatus("current")


class _QtechSMPPolicyContent_Type(OctetString):
    """Custom type qtechSMPPolicyContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_QtechSMPPolicyContent_Type.__name__ = "OctetString"
_QtechSMPPolicyContent_Object = MibTableColumn
qtechSMPPolicyContent = _QtechSMPPolicyContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 7),
    _QtechSMPPolicyContent_Type()
)
qtechSMPPolicyContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyContent.setStatus("current")


class _QtechSMPPolicyMask_Type(OctetString):
    """Custom type qtechSMPPolicyMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_QtechSMPPolicyMask_Type.__name__ = "OctetString"
_QtechSMPPolicyMask_Object = MibTableColumn
qtechSMPPolicyMask = _QtechSMPPolicyMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 8),
    _QtechSMPPolicyMask_Type()
)
qtechSMPPolicyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyMask.setStatus("current")


class _QtechSMPPolicyName_Type(DisplayString):
    """Custom type qtechSMPPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechSMPPolicyName_Type.__name__ = "DisplayString"
_QtechSMPPolicyName_Object = MibTableColumn
qtechSMPPolicyName = _QtechSMPPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 8, 1, 9),
    _QtechSMPPolicyName_Type()
)
qtechSMPPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSMPPolicyName.setStatus("current")
_QtechSMPPolicyGroupTable_Object = MibTable
qtechSMPPolicyGroupTable = _QtechSMPPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 9)
)
if mibBuilder.loadTexts:
    qtechSMPPolicyGroupTable.setStatus("current")
_QtechSMPPolicyGroupEntry_Object = MibTableRow
qtechSMPPolicyGroupEntry = _QtechSMPPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 9, 1)
)
qtechSMPPolicyGroupEntry.setIndexNames(
    (0, "QTECH-SMP-MIB", "qtechSMPPolicyGroupIndex"),
)
if mibBuilder.loadTexts:
    qtechSMPPolicyGroupEntry.setStatus("current")
_QtechSMPPolicyGroupIndex_Type = Unsigned32
_QtechSMPPolicyGroupIndex_Object = MibTableColumn
qtechSMPPolicyGroupIndex = _QtechSMPPolicyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 9, 1, 1),
    _QtechSMPPolicyGroupIndex_Type()
)
qtechSMPPolicyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSMPPolicyGroupIndex.setStatus("current")
_QtechSMPPolicyGroupCount_Type = Unsigned32
_QtechSMPPolicyGroupCount_Object = MibTableColumn
qtechSMPPolicyGroupCount = _QtechSMPPolicyGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 9, 1, 2),
    _QtechSMPPolicyGroupCount_Type()
)
qtechSMPPolicyGroupCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSMPPolicyGroupCount.setStatus("current")


class _QtechSMPPolicyGroupChecksum_Type(OctetString):
    """Custom type qtechSMPPolicyGroupChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_QtechSMPPolicyGroupChecksum_Type.__name__ = "OctetString"
_QtechSMPPolicyGroupChecksum_Object = MibTableColumn
qtechSMPPolicyGroupChecksum = _QtechSMPPolicyGroupChecksum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 9, 1, 3),
    _QtechSMPPolicyGroupChecksum_Type()
)
qtechSMPPolicyGroupChecksum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSMPPolicyGroupChecksum.setStatus("current")
_QtechSMPPolicyGroupStatus_Type = RowStatus
_QtechSMPPolicyGroupStatus_Object = MibTableColumn
qtechSMPPolicyGroupStatus = _QtechSMPPolicyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 1, 9, 1, 4),
    _QtechSMPPolicyGroupStatus_Type()
)
qtechSMPPolicyGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSMPPolicyGroupStatus.setStatus("current")
_QtechEGMIBObjects_ObjectIdentity = ObjectIdentity
qtechEGMIBObjects = _QtechEGMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2)
)
_QtechEGUserTable_Object = MibTable
qtechEGUserTable = _QtechEGUserTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1)
)
if mibBuilder.loadTexts:
    qtechEGUserTable.setStatus("current")
_QtechEGUserEntry_Object = MibTableRow
qtechEGUserEntry = _QtechEGUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1)
)
qtechEGUserEntry.setIndexNames(
    (0, "QTECH-SMP-MIB", "qtechEGUserIpAddrType"),
    (0, "QTECH-SMP-MIB", "qtechEGUserIpAddr"),
)
if mibBuilder.loadTexts:
    qtechEGUserEntry.setStatus("current")
_QtechEGUserIpAddrType_Type = InetAddressType
_QtechEGUserIpAddrType_Object = MibTableColumn
qtechEGUserIpAddrType = _QtechEGUserIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 1),
    _QtechEGUserIpAddrType_Type()
)
qtechEGUserIpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechEGUserIpAddrType.setStatus("current")
_QtechEGUserIpAddr_Type = InetAddress
_QtechEGUserIpAddr_Object = MibTableColumn
qtechEGUserIpAddr = _QtechEGUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 2),
    _QtechEGUserIpAddr_Type()
)
qtechEGUserIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechEGUserIpAddr.setStatus("current")


class _QtechEGUserId_Type(OctetString):
    """Custom type qtechEGUserId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechEGUserId_Type.__name__ = "OctetString"
_QtechEGUserId_Object = MibTableColumn
qtechEGUserId = _QtechEGUserId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 3),
    _QtechEGUserId_Type()
)
qtechEGUserId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGUserId.setStatus("current")


class _QtechEGUserName_Type(OctetString):
    """Custom type qtechEGUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechEGUserName_Type.__name__ = "OctetString"
_QtechEGUserName_Object = MibTableColumn
qtechEGUserName = _QtechEGUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 4),
    _QtechEGUserName_Type()
)
qtechEGUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGUserName.setStatus("current")


class _QtechEGUserGroupName_Type(OctetString):
    """Custom type qtechEGUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_QtechEGUserGroupName_Type.__name__ = "OctetString"
_QtechEGUserGroupName_Object = MibTableColumn
qtechEGUserGroupName = _QtechEGUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 5),
    _QtechEGUserGroupName_Type()
)
qtechEGUserGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGUserGroupName.setStatus("current")
_QtechEGUserMac_Type = MacAddress
_QtechEGUserMac_Object = MibTableColumn
qtechEGUserMac = _QtechEGUserMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 6),
    _QtechEGUserMac_Type()
)
qtechEGUserMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGUserMac.setStatus("current")
_QtechEGNasIp_Type = InetAddress
_QtechEGNasIp_Object = MibTableColumn
qtechEGNasIp = _QtechEGNasIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 7),
    _QtechEGNasIp_Type()
)
qtechEGNasIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGNasIp.setStatus("current")
_QtechEGNasPort_Type = Gauge32
_QtechEGNasPort_Object = MibTableColumn
qtechEGNasPort = _QtechEGNasPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 8),
    _QtechEGNasPort_Type()
)
qtechEGNasPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGNasPort.setStatus("current")
_QtechEGGatewayIp_Type = InetAddress
_QtechEGGatewayIp_Object = MibTableColumn
qtechEGGatewayIp = _QtechEGGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 9),
    _QtechEGGatewayIp_Type()
)
qtechEGGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGGatewayIp.setStatus("current")
_QtechEGVlanId_Type = Gauge32
_QtechEGVlanId_Object = MibTableColumn
qtechEGVlanId = _QtechEGVlanId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 10),
    _QtechEGVlanId_Type()
)
qtechEGVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGVlanId.setStatus("current")
_QtechEGLoginTime_Type = OctetString
_QtechEGLoginTime_Object = MibTableColumn
qtechEGLoginTime = _QtechEGLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 11),
    _QtechEGLoginTime_Type()
)
qtechEGLoginTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGLoginTime.setStatus("current")
_QtechEGLogoutTime_Type = OctetString
_QtechEGLogoutTime_Object = MibTableColumn
qtechEGLogoutTime = _QtechEGLogoutTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 12),
    _QtechEGLogoutTime_Type()
)
qtechEGLogoutTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGLogoutTime.setStatus("current")
_QtechEGMessageType_Type = Gauge32
_QtechEGMessageType_Object = MibTableColumn
qtechEGMessageType = _QtechEGMessageType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 13),
    _QtechEGMessageType_Type()
)
qtechEGMessageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGMessageType.setStatus("current")
_QtechEGUserStatus_Type = RowStatus
_QtechEGUserStatus_Object = MibTableColumn
qtechEGUserStatus = _QtechEGUserStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 1, 1, 14),
    _QtechEGUserStatus_Type()
)
qtechEGUserStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechEGUserStatus.setStatus("current")
_QtechEGUserDelete_Type = Integer32
_QtechEGUserDelete_Object = MibScalar
qtechEGUserDelete = _QtechEGUserDelete_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 2, 2),
    _QtechEGUserDelete_Type()
)
qtechEGUserDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechEGUserDelete.setStatus("current")
_QtechSMPMIBConformance_ObjectIdentity = ObjectIdentity
qtechSMPMIBConformance = _QtechSMPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3)
)
_QtechSMPMIBCompliances_ObjectIdentity = ObjectIdentity
qtechSMPMIBCompliances = _QtechSMPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3, 1)
)
_QtechSMPMIBGroups_ObjectIdentity = ObjectIdentity
qtechSMPMIBGroups = _QtechSMPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3, 2)
)
_QtechSMPTraps_ObjectIdentity = ObjectIdentity
qtechSMPTraps = _QtechSMPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535)
)
_QtechSMPSwitchIP_Type = IpAddress
_QtechSMPSwitchIP_Object = MibScalar
qtechSMPSwitchIP = _QtechSMPSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 1),
    _QtechSMPSwitchIP_Type()
)
qtechSMPSwitchIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPSwitchIP.setStatus("current")
_QtechSMPSwitchInterfaceID_Type = IfIndex
_QtechSMPSwitchInterfaceID_Object = MibScalar
qtechSMPSwitchInterfaceID = _QtechSMPSwitchInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 2),
    _QtechSMPSwitchInterfaceID_Type()
)
qtechSMPSwitchInterfaceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPSwitchInterfaceID.setStatus("current")
_QtechSMPSwitchInterfaceVLANID_Type = VlanId
_QtechSMPSwitchInterfaceVLANID_Object = MibScalar
qtechSMPSwitchInterfaceVLANID = _QtechSMPSwitchInterfaceVLANID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 3),
    _QtechSMPSwitchInterfaceVLANID_Type()
)
qtechSMPSwitchInterfaceVLANID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPSwitchInterfaceVLANID.setStatus("current")
_QtechSMPFrameContentLength_Type = Unsigned32
_QtechSMPFrameContentLength_Object = MibScalar
qtechSMPFrameContentLength = _QtechSMPFrameContentLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 4),
    _QtechSMPFrameContentLength_Type()
)
qtechSMPFrameContentLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPFrameContentLength.setStatus("current")


class _QtechSMPFrameContent_Type(OctetString):
    """Custom type qtechSMPFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_QtechSMPFrameContent_Type.__name__ = "OctetString"
_QtechSMPFrameContent_Object = MibScalar
qtechSMPFrameContent = _QtechSMPFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 5),
    _QtechSMPFrameContent_Type()
)
qtechSMPFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPFrameContent.setStatus("current")


class _QtechSMPArpAttackSubnetIP_Type(OctetString):
    """Custom type qtechSMPArpAttackSubnetIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_QtechSMPArpAttackSubnetIP_Type.__name__ = "OctetString"
_QtechSMPArpAttackSubnetIP_Object = MibScalar
qtechSMPArpAttackSubnetIP = _QtechSMPArpAttackSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 7),
    _QtechSMPArpAttackSubnetIP_Type()
)
qtechSMPArpAttackSubnetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackSubnetIP.setStatus("current")
_QtechSMPArpAttackSubnetIPNum_Type = Integer32
_QtechSMPArpAttackSubnetIPNum_Object = MibScalar
qtechSMPArpAttackSubnetIPNum = _QtechSMPArpAttackSubnetIPNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 8),
    _QtechSMPArpAttackSubnetIPNum_Type()
)
qtechSMPArpAttackSubnetIPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackSubnetIPNum.setStatus("current")
_QtechSMPArpAttackInterfaceSlot_Type = Integer32
_QtechSMPArpAttackInterfaceSlot_Object = MibScalar
qtechSMPArpAttackInterfaceSlot = _QtechSMPArpAttackInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 9),
    _QtechSMPArpAttackInterfaceSlot_Type()
)
qtechSMPArpAttackInterfaceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackInterfaceSlot.setStatus("current")
_QtechSMPArpAttackInterfacePort_Type = Integer32
_QtechSMPArpAttackInterfacePort_Object = MibScalar
qtechSMPArpAttackInterfacePort = _QtechSMPArpAttackInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 10),
    _QtechSMPArpAttackInterfacePort_Type()
)
qtechSMPArpAttackInterfacePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackInterfacePort.setStatus("current")
_QtechSMPArpAttackInterfaceVlanID_Type = VlanId
_QtechSMPArpAttackInterfaceVlanID_Object = MibScalar
qtechSMPArpAttackInterfaceVlanID = _QtechSMPArpAttackInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 11),
    _QtechSMPArpAttackInterfaceVlanID_Type()
)
qtechSMPArpAttackInterfaceVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackInterfaceVlanID.setStatus("current")


class _QtechSMPArpAttackFrameContent_Type(OctetString):
    """Custom type qtechSMPArpAttackFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QtechSMPArpAttackFrameContent_Type.__name__ = "OctetString"
_QtechSMPArpAttackFrameContent_Object = MibScalar
qtechSMPArpAttackFrameContent = _QtechSMPArpAttackFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 12),
    _QtechSMPArpAttackFrameContent_Type()
)
qtechSMPArpAttackFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackFrameContent.setStatus("current")
_QtechSMPArpAttackStatus_Type = TruthValue
_QtechSMPArpAttackStatus_Object = MibScalar
qtechSMPArpAttackStatus = _QtechSMPArpAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 13),
    _QtechSMPArpAttackStatus_Type()
)
qtechSMPArpAttackStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackStatus.setStatus("current")


class _QtechSMPArpAttackCriticalStatus_Type(Integer32):
    """Custom type qtechSMPArpAttackCriticalStatus based on Integer32"""
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


_QtechSMPArpAttackCriticalStatus_Type.__name__ = "Integer32"
_QtechSMPArpAttackCriticalStatus_Object = MibScalar
qtechSMPArpAttackCriticalStatus = _QtechSMPArpAttackCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 14),
    _QtechSMPArpAttackCriticalStatus_Type()
)
qtechSMPArpAttackCriticalStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackCriticalStatus.setStatus("current")
_QtechSMPArpAttackMac_Type = MacAddress
_QtechSMPArpAttackMac_Object = MibScalar
qtechSMPArpAttackMac = _QtechSMPArpAttackMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 15),
    _QtechSMPArpAttackMac_Type()
)
qtechSMPArpAttackMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackMac.setStatus("current")
_QtechSMPArpAttackInterfaceIndex_Type = Integer32
_QtechSMPArpAttackInterfaceIndex_Object = MibScalar
qtechSMPArpAttackInterfaceIndex = _QtechSMPArpAttackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 16),
    _QtechSMPArpAttackInterfaceIndex_Type()
)
qtechSMPArpAttackInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    qtechSMPArpAttackInterfaceIndex.setStatus("current")

# Managed Objects groups

qtechSMPServerMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3, 2, 1)
)
qtechSMPServerMibGroup.setObjects(
      *(("QTECH-SMP-MIB", "qtechSMPServer"),
        ("QTECH-SMP-MIB", "qtechSMPServerKey"))
)
if mibBuilder.loadTexts:
    qtechSMPServerMibGroup.setStatus("current")

qtechSMPClientMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3, 2, 2)
)
qtechSMPClientMibGroup.setObjects(
    ("QTECH-SMP-MIB", "qtechSMPEventSendSlice")
)
if mibBuilder.loadTexts:
    qtechSMPClientMibGroup.setStatus("current")

qtechSMPPolicyMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3, 2, 3)
)
qtechSMPPolicyMibGroup.setObjects(
      *(("QTECH-SMP-MIB", "qtechSMPPolicyDelete"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyChecksum"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyIndex"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyStatus"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyInstallPort"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyType"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyContent"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyMask"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyName"))
)
if mibBuilder.loadTexts:
    qtechSMPPolicyMibGroup.setStatus("current")

qtechSMPFrameRelayMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3, 2, 4)
)
qtechSMPFrameRelayMibGroup.setObjects(
      *(("QTECH-SMP-MIB", "qtechSMPFrameRelayIndex"),
        ("QTECH-SMP-MIB", "qtechSMPFrameRelayContent"),
        ("QTECH-SMP-MIB", "qtechSMPFrameRelayLength"),
        ("QTECH-SMP-MIB", "qtechSMPFrameRelayDestPort"),
        ("QTECH-SMP-MIB", "qtechSMPFrameRelayDestVlan"))
)
if mibBuilder.loadTexts:
    qtechSMPFrameRelayMibGroup.setStatus("current")


# Notification objects

qtechSMPFrameRelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 6)
)
qtechSMPFrameRelayTrap.setObjects(
      *(("QTECH-SMP-MIB", "qtechSMPSwitchIP"),
        ("QTECH-SMP-MIB", "qtechSMPSwitchInterfaceID"),
        ("QTECH-SMP-MIB", "qtechSMPSwitchInterfaceVLANID"),
        ("QTECH-SMP-MIB", "qtechSMPFrameContentLength"),
        ("QTECH-SMP-MIB", "qtechSMPFrameContent"))
)
if mibBuilder.loadTexts:
    qtechSMPFrameRelayTrap.setStatus(
        "current"
    )

qtechSMPArpAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 65535, 17)
)
qtechSMPArpAttackTrap.setObjects(
      *(("QTECH-SMP-MIB", "qtechSMPArpAttackSubnetIP"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackSubnetIPNum"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackInterfaceSlot"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackInterfacePort"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackInterfaceVlanID"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackFrameContent"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackStatus"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackCriticalStatus"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackMac"),
        ("QTECH-SMP-MIB", "qtechSMPArpAttackInterfaceIndex"))
)
if mibBuilder.loadTexts:
    qtechSMPArpAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 39, 3, 1, 1)
)
qtechDeviceMIBCompliance.setObjects(
      *(("QTECH-SMP-MIB", "qtechSMPServerMibGroup"),
        ("QTECH-SMP-MIB", "qtechSMPClientMibGroup"),
        ("QTECH-SMP-MIB", "qtechSMPPolicyMibGroup"),
        ("QTECH-SMP-MIB", "qtechSMPFrameRelayMibGroup"))
)
if mibBuilder.loadTexts:
    qtechDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SMP-MIB",
    **{"qtechSMPMIB": qtechSMPMIB,
       "qtechSMPMIBObjects": qtechSMPMIBObjects,
       "qtechSMPServer": qtechSMPServer,
       "qtechSMPServerKey": qtechSMPServerKey,
       "qtechSMPEventSendSlice": qtechSMPEventSendSlice,
       "qtechSMPPolicyDelete": qtechSMPPolicyDelete,
       "qtechSMPPolicyChecksum": qtechSMPPolicyChecksum,
       "qtechSMPPolicyTimeout": qtechSMPPolicyTimeout,
       "qtechSMPFrameRelayTable": qtechSMPFrameRelayTable,
       "qtechSMPFrameRelayEntry": qtechSMPFrameRelayEntry,
       "qtechSMPFrameRelayIndex": qtechSMPFrameRelayIndex,
       "qtechSMPFrameRelayContent": qtechSMPFrameRelayContent,
       "qtechSMPFrameRelayLength": qtechSMPFrameRelayLength,
       "qtechSMPFrameRelayDestPort": qtechSMPFrameRelayDestPort,
       "qtechSMPFrameRelayDestVlan": qtechSMPFrameRelayDestVlan,
       "qtechSMPPolicyTable": qtechSMPPolicyTable,
       "qtechSMPPolicyEntry": qtechSMPPolicyEntry,
       "qtechSMPGroupIndex": qtechSMPGroupIndex,
       "qtechSMPPolicyIndex": qtechSMPPolicyIndex,
       "qtechSMPPolicyStatus": qtechSMPPolicyStatus,
       "qtechSMPPolicyNumber": qtechSMPPolicyNumber,
       "qtechSMPPolicyInstallPort": qtechSMPPolicyInstallPort,
       "qtechSMPPolicyType": qtechSMPPolicyType,
       "qtechSMPPolicyContent": qtechSMPPolicyContent,
       "qtechSMPPolicyMask": qtechSMPPolicyMask,
       "qtechSMPPolicyName": qtechSMPPolicyName,
       "qtechSMPPolicyGroupTable": qtechSMPPolicyGroupTable,
       "qtechSMPPolicyGroupEntry": qtechSMPPolicyGroupEntry,
       "qtechSMPPolicyGroupIndex": qtechSMPPolicyGroupIndex,
       "qtechSMPPolicyGroupCount": qtechSMPPolicyGroupCount,
       "qtechSMPPolicyGroupChecksum": qtechSMPPolicyGroupChecksum,
       "qtechSMPPolicyGroupStatus": qtechSMPPolicyGroupStatus,
       "qtechEGMIBObjects": qtechEGMIBObjects,
       "qtechEGUserTable": qtechEGUserTable,
       "qtechEGUserEntry": qtechEGUserEntry,
       "qtechEGUserIpAddrType": qtechEGUserIpAddrType,
       "qtechEGUserIpAddr": qtechEGUserIpAddr,
       "qtechEGUserId": qtechEGUserId,
       "qtechEGUserName": qtechEGUserName,
       "qtechEGUserGroupName": qtechEGUserGroupName,
       "qtechEGUserMac": qtechEGUserMac,
       "qtechEGNasIp": qtechEGNasIp,
       "qtechEGNasPort": qtechEGNasPort,
       "qtechEGGatewayIp": qtechEGGatewayIp,
       "qtechEGVlanId": qtechEGVlanId,
       "qtechEGLoginTime": qtechEGLoginTime,
       "qtechEGLogoutTime": qtechEGLogoutTime,
       "qtechEGMessageType": qtechEGMessageType,
       "qtechEGUserStatus": qtechEGUserStatus,
       "qtechEGUserDelete": qtechEGUserDelete,
       "qtechSMPMIBConformance": qtechSMPMIBConformance,
       "qtechSMPMIBCompliances": qtechSMPMIBCompliances,
       "qtechDeviceMIBCompliance": qtechDeviceMIBCompliance,
       "qtechSMPMIBGroups": qtechSMPMIBGroups,
       "qtechSMPServerMibGroup": qtechSMPServerMibGroup,
       "qtechSMPClientMibGroup": qtechSMPClientMibGroup,
       "qtechSMPPolicyMibGroup": qtechSMPPolicyMibGroup,
       "qtechSMPFrameRelayMibGroup": qtechSMPFrameRelayMibGroup,
       "qtechSMPTraps": qtechSMPTraps,
       "qtechSMPSwitchIP": qtechSMPSwitchIP,
       "qtechSMPSwitchInterfaceID": qtechSMPSwitchInterfaceID,
       "qtechSMPSwitchInterfaceVLANID": qtechSMPSwitchInterfaceVLANID,
       "qtechSMPFrameContentLength": qtechSMPFrameContentLength,
       "qtechSMPFrameContent": qtechSMPFrameContent,
       "qtechSMPFrameRelayTrap": qtechSMPFrameRelayTrap,
       "qtechSMPArpAttackSubnetIP": qtechSMPArpAttackSubnetIP,
       "qtechSMPArpAttackSubnetIPNum": qtechSMPArpAttackSubnetIPNum,
       "qtechSMPArpAttackInterfaceSlot": qtechSMPArpAttackInterfaceSlot,
       "qtechSMPArpAttackInterfacePort": qtechSMPArpAttackInterfacePort,
       "qtechSMPArpAttackInterfaceVlanID": qtechSMPArpAttackInterfaceVlanID,
       "qtechSMPArpAttackFrameContent": qtechSMPArpAttackFrameContent,
       "qtechSMPArpAttackStatus": qtechSMPArpAttackStatus,
       "qtechSMPArpAttackCriticalStatus": qtechSMPArpAttackCriticalStatus,
       "qtechSMPArpAttackMac": qtechSMPArpAttackMac,
       "qtechSMPArpAttackInterfaceIndex": qtechSMPArpAttackInterfaceIndex,
       "qtechSMPArpAttackTrap": qtechSMPArpAttackTrap}
)
