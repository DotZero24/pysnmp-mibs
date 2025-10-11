# SNMP MIB module (DES7200-SMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-SMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:50:24 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "DES7200-SMI",
    "myMgmt")

(Community,) = mibBuilder.importSymbols(
    "DES7200-SNMP-AGENT-MIB",
    "Community")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "DES7200-TC",
    "ConfigStatus",
    "IfIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

mySMPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39)
)
if mibBuilder.loadTexts:
    mySMPMIB.setRevisions(
        ("2004-09-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MySMPMIBObjects_ObjectIdentity = ObjectIdentity
mySMPMIBObjects = _MySMPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1)
)
_MySMPServer_Type = IpAddress
_MySMPServer_Object = MibScalar
mySMPServer = _MySMPServer_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 1),
    _MySMPServer_Type()
)
mySMPServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPServer.setStatus("current")
_MySMPServerKey_Type = Community
_MySMPServerKey_Object = MibScalar
mySMPServerKey = _MySMPServerKey_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 2),
    _MySMPServerKey_Type()
)
mySMPServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPServerKey.setStatus("current")
_MySMPEventSendSlice_Type = Unsigned32
_MySMPEventSendSlice_Object = MibScalar
mySMPEventSendSlice = _MySMPEventSendSlice_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 3),
    _MySMPEventSendSlice_Type()
)
mySMPEventSendSlice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPEventSendSlice.setStatus("current")
_MySMPPolicyDelete_Type = Integer32
_MySMPPolicyDelete_Object = MibScalar
mySMPPolicyDelete = _MySMPPolicyDelete_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 4),
    _MySMPPolicyDelete_Type()
)
mySMPPolicyDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyDelete.setStatus("current")


class _MySMPPolicyChecksum_Type(OctetString):
    """Custom type mySMPPolicyChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_MySMPPolicyChecksum_Type.__name__ = "OctetString"
_MySMPPolicyChecksum_Object = MibScalar
mySMPPolicyChecksum = _MySMPPolicyChecksum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 5),
    _MySMPPolicyChecksum_Type()
)
mySMPPolicyChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySMPPolicyChecksum.setStatus("current")
_MySMPPolicyTimeout_Type = Unsigned32
_MySMPPolicyTimeout_Object = MibScalar
mySMPPolicyTimeout = _MySMPPolicyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 6),
    _MySMPPolicyTimeout_Type()
)
mySMPPolicyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyTimeout.setStatus("current")
_MySMPFrameRelayTable_Object = MibTable
mySMPFrameRelayTable = _MySMPFrameRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7)
)
if mibBuilder.loadTexts:
    mySMPFrameRelayTable.setStatus("current")
_MySMPFrameRelayEntry_Object = MibTableRow
mySMPFrameRelayEntry = _MySMPFrameRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1)
)
mySMPFrameRelayEntry.setIndexNames(
    (0, "DES7200-SMP-MIB", "mySMPFrameRelayIndex"),
)
if mibBuilder.loadTexts:
    mySMPFrameRelayEntry.setStatus("current")
_MySMPFrameRelayIndex_Type = Unsigned32
_MySMPFrameRelayIndex_Object = MibTableColumn
mySMPFrameRelayIndex = _MySMPFrameRelayIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 1),
    _MySMPFrameRelayIndex_Type()
)
mySMPFrameRelayIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySMPFrameRelayIndex.setStatus("current")


class _MySMPFrameRelayContent_Type(OctetString):
    """Custom type mySMPFrameRelayContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MySMPFrameRelayContent_Type.__name__ = "OctetString"
_MySMPFrameRelayContent_Object = MibTableColumn
mySMPFrameRelayContent = _MySMPFrameRelayContent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 2),
    _MySMPFrameRelayContent_Type()
)
mySMPFrameRelayContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPFrameRelayContent.setStatus("current")
_MySMPFrameRelayLength_Type = Unsigned32
_MySMPFrameRelayLength_Object = MibTableColumn
mySMPFrameRelayLength = _MySMPFrameRelayLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 3),
    _MySMPFrameRelayLength_Type()
)
mySMPFrameRelayLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPFrameRelayLength.setStatus("current")
_MySMPFrameRelayDestPort_Type = IfIndex
_MySMPFrameRelayDestPort_Object = MibTableColumn
mySMPFrameRelayDestPort = _MySMPFrameRelayDestPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 4),
    _MySMPFrameRelayDestPort_Type()
)
mySMPFrameRelayDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPFrameRelayDestPort.setStatus("current")
_MySMPFrameRelayDestVlan_Type = VlanId
_MySMPFrameRelayDestVlan_Object = MibTableColumn
mySMPFrameRelayDestVlan = _MySMPFrameRelayDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 7, 1, 5),
    _MySMPFrameRelayDestVlan_Type()
)
mySMPFrameRelayDestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPFrameRelayDestVlan.setStatus("current")
_MySMPPolicyTable_Object = MibTable
mySMPPolicyTable = _MySMPPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8)
)
if mibBuilder.loadTexts:
    mySMPPolicyTable.setStatus("current")
_MySMPPolicyEntry_Object = MibTableRow
mySMPPolicyEntry = _MySMPPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1)
)
mySMPPolicyEntry.setIndexNames(
    (0, "DES7200-SMP-MIB", "mySMPGroupIndex"),
    (0, "DES7200-SMP-MIB", "mySMPPolicyIndex"),
)
if mibBuilder.loadTexts:
    mySMPPolicyEntry.setStatus("current")
_MySMPGroupIndex_Type = Unsigned32
_MySMPGroupIndex_Object = MibTableColumn
mySMPGroupIndex = _MySMPGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 1),
    _MySMPGroupIndex_Type()
)
mySMPGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySMPGroupIndex.setStatus("current")
_MySMPPolicyIndex_Type = Unsigned32
_MySMPPolicyIndex_Object = MibTableColumn
mySMPPolicyIndex = _MySMPPolicyIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 2),
    _MySMPPolicyIndex_Type()
)
mySMPPolicyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySMPPolicyIndex.setStatus("current")
_MySMPPolicyStatus_Type = ConfigStatus
_MySMPPolicyStatus_Object = MibTableColumn
mySMPPolicyStatus = _MySMPPolicyStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 3),
    _MySMPPolicyStatus_Type()
)
mySMPPolicyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyStatus.setStatus("current")
_MySMPPolicyNumber_Type = Unsigned32
_MySMPPolicyNumber_Object = MibTableColumn
mySMPPolicyNumber = _MySMPPolicyNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 4),
    _MySMPPolicyNumber_Type()
)
mySMPPolicyNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyNumber.setStatus("current")
_MySMPPolicyInstallPort_Type = IfIndex
_MySMPPolicyInstallPort_Object = MibTableColumn
mySMPPolicyInstallPort = _MySMPPolicyInstallPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 5),
    _MySMPPolicyInstallPort_Type()
)
mySMPPolicyInstallPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyInstallPort.setStatus("current")


class _MySMPPolicyType_Type(Integer32):
    """Custom type mySMPPolicyType based on Integer32"""
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


_MySMPPolicyType_Type.__name__ = "Integer32"
_MySMPPolicyType_Object = MibTableColumn
mySMPPolicyType = _MySMPPolicyType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 6),
    _MySMPPolicyType_Type()
)
mySMPPolicyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyType.setStatus("current")


class _MySMPPolicyContent_Type(OctetString):
    """Custom type mySMPPolicyContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_MySMPPolicyContent_Type.__name__ = "OctetString"
_MySMPPolicyContent_Object = MibTableColumn
mySMPPolicyContent = _MySMPPolicyContent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 7),
    _MySMPPolicyContent_Type()
)
mySMPPolicyContent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyContent.setStatus("current")


class _MySMPPolicyMask_Type(OctetString):
    """Custom type mySMPPolicyMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(80, 80),
    )
    fixed_length = 80


_MySMPPolicyMask_Type.__name__ = "OctetString"
_MySMPPolicyMask_Object = MibTableColumn
mySMPPolicyMask = _MySMPPolicyMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 8),
    _MySMPPolicyMask_Type()
)
mySMPPolicyMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyMask.setStatus("current")


class _MySMPPolicyName_Type(DisplayString):
    """Custom type mySMPPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MySMPPolicyName_Type.__name__ = "DisplayString"
_MySMPPolicyName_Object = MibTableColumn
mySMPPolicyName = _MySMPPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 8, 1, 9),
    _MySMPPolicyName_Type()
)
mySMPPolicyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyName.setStatus("current")
_MySMPPolicyGroupTable_Object = MibTable
mySMPPolicyGroupTable = _MySMPPolicyGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9)
)
if mibBuilder.loadTexts:
    mySMPPolicyGroupTable.setStatus("current")
_MySMPPolicyGroupEntry_Object = MibTableRow
mySMPPolicyGroupEntry = _MySMPPolicyGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1)
)
mySMPPolicyGroupEntry.setIndexNames(
    (0, "DES7200-SMP-MIB", "mySMPPolicyGroupIndex"),
)
if mibBuilder.loadTexts:
    mySMPPolicyGroupEntry.setStatus("current")
_MySMPPolicyGroupIndex_Type = Unsigned32
_MySMPPolicyGroupIndex_Object = MibTableColumn
mySMPPolicyGroupIndex = _MySMPPolicyGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 1),
    _MySMPPolicyGroupIndex_Type()
)
mySMPPolicyGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySMPPolicyGroupIndex.setStatus("current")
_MySMPPolicyGroupCount_Type = Unsigned32
_MySMPPolicyGroupCount_Object = MibTableColumn
mySMPPolicyGroupCount = _MySMPPolicyGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 2),
    _MySMPPolicyGroupCount_Type()
)
mySMPPolicyGroupCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyGroupCount.setStatus("current")


class _MySMPPolicyGroupChecksum_Type(OctetString):
    """Custom type mySMPPolicyGroupChecksum based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_MySMPPolicyGroupChecksum_Type.__name__ = "OctetString"
_MySMPPolicyGroupChecksum_Object = MibTableColumn
mySMPPolicyGroupChecksum = _MySMPPolicyGroupChecksum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 3),
    _MySMPPolicyGroupChecksum_Type()
)
mySMPPolicyGroupChecksum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySMPPolicyGroupChecksum.setStatus("current")
_MySMPPolicyGroupStatus_Type = RowStatus
_MySMPPolicyGroupStatus_Object = MibTableColumn
mySMPPolicyGroupStatus = _MySMPPolicyGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 1, 9, 1, 4),
    _MySMPPolicyGroupStatus_Type()
)
mySMPPolicyGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mySMPPolicyGroupStatus.setStatus("current")
_MySMPMIBConformance_ObjectIdentity = ObjectIdentity
mySMPMIBConformance = _MySMPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3)
)
_MySMPMIBCompliances_ObjectIdentity = ObjectIdentity
mySMPMIBCompliances = _MySMPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 1)
)
_MySMPMIBGroups_ObjectIdentity = ObjectIdentity
mySMPMIBGroups = _MySMPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2)
)
_MySMPTraps_ObjectIdentity = ObjectIdentity
mySMPTraps = _MySMPTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535)
)
_MySMPSwitchIP_Type = IpAddress
_MySMPSwitchIP_Object = MibScalar
mySMPSwitchIP = _MySMPSwitchIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 1),
    _MySMPSwitchIP_Type()
)
mySMPSwitchIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPSwitchIP.setStatus("current")
_MySMPSwitchInterfaceID_Type = IfIndex
_MySMPSwitchInterfaceID_Object = MibScalar
mySMPSwitchInterfaceID = _MySMPSwitchInterfaceID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 2),
    _MySMPSwitchInterfaceID_Type()
)
mySMPSwitchInterfaceID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPSwitchInterfaceID.setStatus("current")
_MySMPSwitchInterfaceVLANID_Type = VlanId
_MySMPSwitchInterfaceVLANID_Object = MibScalar
mySMPSwitchInterfaceVLANID = _MySMPSwitchInterfaceVLANID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 3),
    _MySMPSwitchInterfaceVLANID_Type()
)
mySMPSwitchInterfaceVLANID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPSwitchInterfaceVLANID.setStatus("current")
_MySMPFrameContentLength_Type = Unsigned32
_MySMPFrameContentLength_Object = MibScalar
mySMPFrameContentLength = _MySMPFrameContentLength_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 4),
    _MySMPFrameContentLength_Type()
)
mySMPFrameContentLength.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPFrameContentLength.setStatus("current")


class _MySMPFrameContent_Type(OctetString):
    """Custom type mySMPFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_MySMPFrameContent_Type.__name__ = "OctetString"
_MySMPFrameContent_Object = MibScalar
mySMPFrameContent = _MySMPFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 5),
    _MySMPFrameContent_Type()
)
mySMPFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPFrameContent.setStatus("current")


class _MySMPArpAttackSubnetIP_Type(OctetString):
    """Custom type mySMPArpAttackSubnetIP based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_MySMPArpAttackSubnetIP_Type.__name__ = "OctetString"
_MySMPArpAttackSubnetIP_Object = MibScalar
mySMPArpAttackSubnetIP = _MySMPArpAttackSubnetIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 7),
    _MySMPArpAttackSubnetIP_Type()
)
mySMPArpAttackSubnetIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackSubnetIP.setStatus("current")
_MySMPArpAttackSubnetIPNum_Type = Integer32
_MySMPArpAttackSubnetIPNum_Object = MibScalar
mySMPArpAttackSubnetIPNum = _MySMPArpAttackSubnetIPNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 8),
    _MySMPArpAttackSubnetIPNum_Type()
)
mySMPArpAttackSubnetIPNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackSubnetIPNum.setStatus("current")
_MySMPArpAttackInterfaceSlot_Type = Integer32
_MySMPArpAttackInterfaceSlot_Object = MibScalar
mySMPArpAttackInterfaceSlot = _MySMPArpAttackInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 9),
    _MySMPArpAttackInterfaceSlot_Type()
)
mySMPArpAttackInterfaceSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackInterfaceSlot.setStatus("current")
_MySMPArpAttackInterfacePort_Type = Integer32
_MySMPArpAttackInterfacePort_Object = MibScalar
mySMPArpAttackInterfacePort = _MySMPArpAttackInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 10),
    _MySMPArpAttackInterfacePort_Type()
)
mySMPArpAttackInterfacePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackInterfacePort.setStatus("current")
_MySMPArpAttackInterfaceVlanID_Type = VlanId
_MySMPArpAttackInterfaceVlanID_Object = MibScalar
mySMPArpAttackInterfaceVlanID = _MySMPArpAttackInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 11),
    _MySMPArpAttackInterfaceVlanID_Type()
)
mySMPArpAttackInterfaceVlanID.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackInterfaceVlanID.setStatus("current")


class _MySMPArpAttackFrameContent_Type(OctetString):
    """Custom type mySMPArpAttackFrameContent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MySMPArpAttackFrameContent_Type.__name__ = "OctetString"
_MySMPArpAttackFrameContent_Object = MibScalar
mySMPArpAttackFrameContent = _MySMPArpAttackFrameContent_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 12),
    _MySMPArpAttackFrameContent_Type()
)
mySMPArpAttackFrameContent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackFrameContent.setStatus("current")
_MySMPArpAttackStatus_Type = TruthValue
_MySMPArpAttackStatus_Object = MibScalar
mySMPArpAttackStatus = _MySMPArpAttackStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 13),
    _MySMPArpAttackStatus_Type()
)
mySMPArpAttackStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackStatus.setStatus("current")


class _MySMPArpAttackCriticalStatus_Type(Integer32):
    """Custom type mySMPArpAttackCriticalStatus based on Integer32"""
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


_MySMPArpAttackCriticalStatus_Type.__name__ = "Integer32"
_MySMPArpAttackCriticalStatus_Object = MibScalar
mySMPArpAttackCriticalStatus = _MySMPArpAttackCriticalStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 14),
    _MySMPArpAttackCriticalStatus_Type()
)
mySMPArpAttackCriticalStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackCriticalStatus.setStatus("current")
_MySMPArpAttackMac_Type = MacAddress
_MySMPArpAttackMac_Object = MibScalar
mySMPArpAttackMac = _MySMPArpAttackMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 15),
    _MySMPArpAttackMac_Type()
)
mySMPArpAttackMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackMac.setStatus("current")
_MySMPArpAttackInterfaceIndex_Type = Integer32
_MySMPArpAttackInterfaceIndex_Object = MibScalar
mySMPArpAttackInterfaceIndex = _MySMPArpAttackInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 16),
    _MySMPArpAttackInterfaceIndex_Type()
)
mySMPArpAttackInterfaceIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    mySMPArpAttackInterfaceIndex.setStatus("current")

# Managed Objects groups

mySMPServerMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 1)
)
mySMPServerMibGroup.setObjects(
      *(("DES7200-SMP-MIB", "mySMPServer"),
        ("DES7200-SMP-MIB", "mySMPServerKey"))
)
if mibBuilder.loadTexts:
    mySMPServerMibGroup.setStatus("current")

mySMPClientMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 2)
)
mySMPClientMibGroup.setObjects(
    ("DES7200-SMP-MIB", "mySMPEventSendSlice")
)
if mibBuilder.loadTexts:
    mySMPClientMibGroup.setStatus("current")

mySMPPolicyMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 3)
)
mySMPPolicyMibGroup.setObjects(
      *(("DES7200-SMP-MIB", "mySMPPolicyDelete"),
        ("DES7200-SMP-MIB", "mySMPPolicyChecksum"),
        ("DES7200-SMP-MIB", "mySMPPolicyIndex"),
        ("DES7200-SMP-MIB", "mySMPPolicyStatus"),
        ("DES7200-SMP-MIB", "mySMPPolicyInstallPort"),
        ("DES7200-SMP-MIB", "mySMPPolicyType"),
        ("DES7200-SMP-MIB", "mySMPPolicyContent"),
        ("DES7200-SMP-MIB", "mySMPPolicyMask"),
        ("DES7200-SMP-MIB", "mySMPPolicyName"))
)
if mibBuilder.loadTexts:
    mySMPPolicyMibGroup.setStatus("current")

mySMPFrameRelayMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 2, 4)
)
mySMPFrameRelayMibGroup.setObjects(
      *(("DES7200-SMP-MIB", "mySMPFrameRelayIndex"),
        ("DES7200-SMP-MIB", "mySMPFrameRelayContent"),
        ("DES7200-SMP-MIB", "mySMPFrameRelayLength"),
        ("DES7200-SMP-MIB", "mySMPFrameRelayDestPort"),
        ("DES7200-SMP-MIB", "mySMPFrameRelayDestVlan"))
)
if mibBuilder.loadTexts:
    mySMPFrameRelayMibGroup.setStatus("current")


# Notification objects

mySMPFrameRelayTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 6)
)
mySMPFrameRelayTrap.setObjects(
      *(("DES7200-SMP-MIB", "mySMPSwitchIP"),
        ("DES7200-SMP-MIB", "mySMPSwitchInterfaceID"),
        ("DES7200-SMP-MIB", "mySMPSwitchInterfaceVLANID"),
        ("DES7200-SMP-MIB", "mySMPFrameContentLength"),
        ("DES7200-SMP-MIB", "mySMPFrameContent"))
)
if mibBuilder.loadTexts:
    mySMPFrameRelayTrap.setStatus(
        "current"
    )

mySMPArpAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 65535, 17)
)
mySMPArpAttackTrap.setObjects(
      *(("DES7200-SMP-MIB", "mySMPArpAttackSubnetIP"),
        ("DES7200-SMP-MIB", "mySMPArpAttackSubnetIPNum"),
        ("DES7200-SMP-MIB", "mySMPArpAttackInterfaceSlot"),
        ("DES7200-SMP-MIB", "mySMPArpAttackInterfacePort"),
        ("DES7200-SMP-MIB", "mySMPArpAttackInterfaceVlanID"),
        ("DES7200-SMP-MIB", "mySMPArpAttackFrameContent"),
        ("DES7200-SMP-MIB", "mySMPArpAttackStatus"),
        ("DES7200-SMP-MIB", "mySMPArpAttackCriticalStatus"),
        ("DES7200-SMP-MIB", "mySMPArpAttackMac"),
        ("DES7200-SMP-MIB", "mySMPArpAttackInterfaceIndex"))
)
if mibBuilder.loadTexts:
    mySMPArpAttackTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

myDeviceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 39, 3, 1, 1)
)
myDeviceMIBCompliance.setObjects(
      *(("DES7200-SMP-MIB", "mySMPServerMibGroup"),
        ("DES7200-SMP-MIB", "mySMPClientMibGroup"),
        ("DES7200-SMP-MIB", "mySMPPolicyMibGroup"),
        ("DES7200-SMP-MIB", "mySMPFrameRelayMibGroup"))
)
if mibBuilder.loadTexts:
    myDeviceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-SMP-MIB",
    **{"mySMPMIB": mySMPMIB,
       "mySMPMIBObjects": mySMPMIBObjects,
       "mySMPServer": mySMPServer,
       "mySMPServerKey": mySMPServerKey,
       "mySMPEventSendSlice": mySMPEventSendSlice,
       "mySMPPolicyDelete": mySMPPolicyDelete,
       "mySMPPolicyChecksum": mySMPPolicyChecksum,
       "mySMPPolicyTimeout": mySMPPolicyTimeout,
       "mySMPFrameRelayTable": mySMPFrameRelayTable,
       "mySMPFrameRelayEntry": mySMPFrameRelayEntry,
       "mySMPFrameRelayIndex": mySMPFrameRelayIndex,
       "mySMPFrameRelayContent": mySMPFrameRelayContent,
       "mySMPFrameRelayLength": mySMPFrameRelayLength,
       "mySMPFrameRelayDestPort": mySMPFrameRelayDestPort,
       "mySMPFrameRelayDestVlan": mySMPFrameRelayDestVlan,
       "mySMPPolicyTable": mySMPPolicyTable,
       "mySMPPolicyEntry": mySMPPolicyEntry,
       "mySMPGroupIndex": mySMPGroupIndex,
       "mySMPPolicyIndex": mySMPPolicyIndex,
       "mySMPPolicyStatus": mySMPPolicyStatus,
       "mySMPPolicyNumber": mySMPPolicyNumber,
       "mySMPPolicyInstallPort": mySMPPolicyInstallPort,
       "mySMPPolicyType": mySMPPolicyType,
       "mySMPPolicyContent": mySMPPolicyContent,
       "mySMPPolicyMask": mySMPPolicyMask,
       "mySMPPolicyName": mySMPPolicyName,
       "mySMPPolicyGroupTable": mySMPPolicyGroupTable,
       "mySMPPolicyGroupEntry": mySMPPolicyGroupEntry,
       "mySMPPolicyGroupIndex": mySMPPolicyGroupIndex,
       "mySMPPolicyGroupCount": mySMPPolicyGroupCount,
       "mySMPPolicyGroupChecksum": mySMPPolicyGroupChecksum,
       "mySMPPolicyGroupStatus": mySMPPolicyGroupStatus,
       "mySMPMIBConformance": mySMPMIBConformance,
       "mySMPMIBCompliances": mySMPMIBCompliances,
       "myDeviceMIBCompliance": myDeviceMIBCompliance,
       "mySMPMIBGroups": mySMPMIBGroups,
       "mySMPServerMibGroup": mySMPServerMibGroup,
       "mySMPClientMibGroup": mySMPClientMibGroup,
       "mySMPPolicyMibGroup": mySMPPolicyMibGroup,
       "mySMPFrameRelayMibGroup": mySMPFrameRelayMibGroup,
       "mySMPTraps": mySMPTraps,
       "mySMPSwitchIP": mySMPSwitchIP,
       "mySMPSwitchInterfaceID": mySMPSwitchInterfaceID,
       "mySMPSwitchInterfaceVLANID": mySMPSwitchInterfaceVLANID,
       "mySMPFrameContentLength": mySMPFrameContentLength,
       "mySMPFrameContent": mySMPFrameContent,
       "mySMPFrameRelayTrap": mySMPFrameRelayTrap,
       "mySMPArpAttackSubnetIP": mySMPArpAttackSubnetIP,
       "mySMPArpAttackSubnetIPNum": mySMPArpAttackSubnetIPNum,
       "mySMPArpAttackInterfaceSlot": mySMPArpAttackInterfaceSlot,
       "mySMPArpAttackInterfacePort": mySMPArpAttackInterfacePort,
       "mySMPArpAttackInterfaceVlanID": mySMPArpAttackInterfaceVlanID,
       "mySMPArpAttackFrameContent": mySMPArpAttackFrameContent,
       "mySMPArpAttackStatus": mySMPArpAttackStatus,
       "mySMPArpAttackCriticalStatus": mySMPArpAttackCriticalStatus,
       "mySMPArpAttackMac": mySMPArpAttackMac,
       "mySMPArpAttackInterfaceIndex": mySMPArpAttackInterfaceIndex,
       "mySMPArpAttackTrap": mySMPArpAttackTrap}
)
