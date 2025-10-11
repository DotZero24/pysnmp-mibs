# SNMP MIB module (FS-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-AP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:49 2025
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

(IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex",
    "MemberMap")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsApMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7)
)
if mibBuilder.loadTexts:
    fsApMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsApMIBObjects_ObjectIdentity = ObjectIdentity
fsApMIBObjects = _FsApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1)
)
_FsApMaxNumber_Type = Integer32
_FsApMaxNumber_Object = MibScalar
fsApMaxNumber = _FsApMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 1),
    _FsApMaxNumber_Type()
)
fsApMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApMaxNumber.setStatus("current")
_FsApCurrentNumber_Type = Integer32
_FsApCurrentNumber_Object = MibScalar
fsApCurrentNumber = _FsApCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 2),
    _FsApCurrentNumber_Type()
)
fsApCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApCurrentNumber.setStatus("current")
_FsApPortConfigTable_Object = MibTable
fsApPortConfigTable = _FsApPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    fsApPortConfigTable.setStatus("obsolete")
_FsApPortConfigEntry_Object = MibTableRow
fsApPortConfigEntry = _FsApPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 3, 1)
)
fsApPortConfigEntry.setIndexNames(
    (0, "FS-AP-MIB", "fsApPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    fsApPortConfigEntry.setStatus("obsolete")
_FsApPortConfigPortIndex_Type = IfIndex
_FsApPortConfigPortIndex_Object = MibTableColumn
fsApPortConfigPortIndex = _FsApPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 3, 1, 1),
    _FsApPortConfigPortIndex_Type()
)
fsApPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsApPortConfigPortIndex.setStatus("obsolete")
_FsApPortConfigApIndex_Type = IfIndex
_FsApPortConfigApIndex_Object = MibTableColumn
fsApPortConfigApIndex = _FsApPortConfigApIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 3, 1, 2),
    _FsApPortConfigApIndex_Type()
)
fsApPortConfigApIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApPortConfigApIndex.setStatus("obsolete")
_FsApTable_Object = MibTable
fsApTable = _FsApTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    fsApTable.setStatus("obsolete")
_FsApEntry_Object = MibTableRow
fsApEntry = _FsApEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 4, 1)
)
fsApEntry.setIndexNames(
    (0, "FS-AP-MIB", "fsApIndex"),
)
if mibBuilder.loadTexts:
    fsApEntry.setStatus("obsolete")
_FsApIndex_Type = IfIndex
_FsApIndex_Object = MibTableColumn
fsApIndex = _FsApIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 4, 1, 1),
    _FsApIndex_Type()
)
fsApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApIndex.setStatus("obsolete")
_FsApMemberAction_Type = MemberMap
_FsApMemberAction_Object = MibTableColumn
fsApMemberAction = _FsApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 4, 1, 2),
    _FsApMemberAction_Type()
)
fsApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApMemberAction.setStatus("obsolete")
_FsApPossibleMember_Type = MemberMap
_FsApPossibleMember_Object = MibTableColumn
fsApPossibleMember = _FsApPossibleMember_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 4, 1, 3),
    _FsApPossibleMember_Type()
)
fsApPossibleMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApPossibleMember.setStatus("obsolete")
_FsApMaxPtNumber_Type = Integer32
_FsApMaxPtNumber_Object = MibTableColumn
fsApMaxPtNumber = _FsApMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 4, 1, 4),
    _FsApMaxPtNumber_Type()
)
fsApMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApMaxPtNumber.setStatus("obsolete")


class _FsApFlowBalance_Type(Integer32):
    """Custom type fsApFlowBalance based on Integer32"""
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("source-mac", 1),
          ("destination-mac", 2),
          ("src-dest-mac", 3),
          ("source-ip", 4),
          ("destination-ip", 5),
          ("src-dest-ip", 6),
          ("src-dest-port", 7),
          ("src-dst-ip-l4port", 8),
          ("enhanced-profile", 9),
          ("src-l4port", 10),
          ("dest-l4port", 11),
          ("src-dest-l4port", 12),
          ("src-ip-l4port", 13),
          ("dest-ip-l4port", 14),
          ("src-ip-dest-l4port", 15),
          ("dest-ip-src-l4port", 16),
          ("src-dest-ip-src-l4port", 17),
          ("src-dest-ip-dest-l4port", 18),
          ("src-ip-src-dest-l4port", 19),
          ("dest-ip-src-dest-l4port", 20))
    )


_FsApFlowBalance_Type.__name__ = "Integer32"
_FsApFlowBalance_Object = MibScalar
fsApFlowBalance = _FsApFlowBalance_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 5),
    _FsApFlowBalance_Type()
)
fsApFlowBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApFlowBalance.setStatus("current")
_FsApConfigTable_Object = MibTable
fsApConfigTable = _FsApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    fsApConfigTable.setStatus("current")
_FsApConfigEntry_Object = MibTableRow
fsApConfigEntry = _FsApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6, 1)
)
fsApConfigEntry.setIndexNames(
    (0, "FS-AP-MIB", "fsApConfigNumber"),
)
if mibBuilder.loadTexts:
    fsApConfigEntry.setStatus("current")
_FsApConfigNumber_Type = Integer32
_FsApConfigNumber_Object = MibTableColumn
fsApConfigNumber = _FsApConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6, 1, 1),
    _FsApConfigNumber_Type()
)
fsApConfigNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApConfigNumber.setStatus("current")
_FsApConfigIndex_Type = IfIndex
_FsApConfigIndex_Object = MibTableColumn
fsApConfigIndex = _FsApConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6, 1, 2),
    _FsApConfigIndex_Type()
)
fsApConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApConfigIndex.setStatus("current")
_FsApConfigMaxPtNumber_Type = Integer32
_FsApConfigMaxPtNumber_Object = MibTableColumn
fsApConfigMaxPtNumber = _FsApConfigMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6, 1, 3),
    _FsApConfigMaxPtNumber_Type()
)
fsApConfigMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApConfigMaxPtNumber.setStatus("current")
_FsApConfigCurrentPtNumber_Type = Integer32
_FsApConfigCurrentPtNumber_Object = MibTableColumn
fsApConfigCurrentPtNumber = _FsApConfigCurrentPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6, 1, 4),
    _FsApConfigCurrentPtNumber_Type()
)
fsApConfigCurrentPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApConfigCurrentPtNumber.setStatus("current")
_FsApConfigPortMember_Type = PortList
_FsApConfigPortMember_Object = MibTableColumn
fsApConfigPortMember = _FsApConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6, 1, 5),
    _FsApConfigPortMember_Type()
)
fsApConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApConfigPortMember.setStatus("current")
_FsApConfigAction_Type = Integer32
_FsApConfigAction_Object = MibTableColumn
fsApConfigAction = _FsApConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 6, 1, 6),
    _FsApConfigAction_Type()
)
fsApConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApConfigAction.setStatus("current")
_FsApPortMemberTable_Object = MibTable
fsApPortMemberTable = _FsApPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 7)
)
if mibBuilder.loadTexts:
    fsApPortMemberTable.setStatus("current")
_FsApPortMemberEntry_Object = MibTableRow
fsApPortMemberEntry = _FsApPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 7, 1)
)
fsApPortMemberEntry.setIndexNames(
    (0, "FS-AP-MIB", "fsApPortMemberPortIndex"),
)
if mibBuilder.loadTexts:
    fsApPortMemberEntry.setStatus("current")
_FsApPortMemberPortIndex_Type = IfIndex
_FsApPortMemberPortIndex_Object = MibTableColumn
fsApPortMemberPortIndex = _FsApPortMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 7, 1, 1),
    _FsApPortMemberPortIndex_Type()
)
fsApPortMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApPortMemberPortIndex.setStatus("current")
_FsApPortMemberApNumber_Type = Integer32
_FsApPortMemberApNumber_Object = MibTableColumn
fsApPortMemberApNumber = _FsApPortMemberApNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 7, 1, 2),
    _FsApPortMemberApNumber_Type()
)
fsApPortMemberApNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApPortMemberApNumber.setStatus("current")
_FsApPortMemberAction_Type = Integer32
_FsApPortMemberAction_Object = MibTableColumn
fsApPortMemberAction = _FsApPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 7, 1, 3),
    _FsApPortMemberAction_Type()
)
fsApPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApPortMemberAction.setStatus("current")


class _FsApPortMemberLacpStatus_Type(Integer32):
    """Custom type fsApPortMemberLacpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-lacp-member", 0),
          ("down", 1),
          ("bndl", 2),
          ("susp", 3),
          ("individual", 4))
    )


_FsApPortMemberLacpStatus_Type.__name__ = "Integer32"
_FsApPortMemberLacpStatus_Object = MibTableColumn
fsApPortMemberLacpStatus = _FsApPortMemberLacpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 7, 1, 4),
    _FsApPortMemberLacpStatus_Type()
)
fsApPortMemberLacpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApPortMemberLacpStatus.setStatus("current")
_FsApBalcProfName_Type = DisplayString
_FsApBalcProfName_Object = MibScalar
fsApBalcProfName = _FsApBalcProfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 8),
    _FsApBalcProfName_Type()
)
fsApBalcProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApBalcProfName.setStatus("current")
_FsApProfTable_Object = MibTable
fsApProfTable = _FsApProfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9)
)
if mibBuilder.loadTexts:
    fsApProfTable.setStatus("current")
_FsApProfEntry_Object = MibTableRow
fsApProfEntry = _FsApProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1)
)
fsApProfEntry.setIndexNames(
    (0, "FS-AP-MIB", "fsApProfIdx"),
)
if mibBuilder.loadTexts:
    fsApProfEntry.setStatus("current")
_FsApProfIdx_Type = Integer32
_FsApProfIdx_Object = MibTableColumn
fsApProfIdx = _FsApProfIdx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 1),
    _FsApProfIdx_Type()
)
fsApProfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApProfIdx.setStatus("current")
_FsApProfName_Type = DisplayString
_FsApProfName_Object = MibTableColumn
fsApProfName = _FsApProfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 2),
    _FsApProfName_Type()
)
fsApProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsApProfName.setStatus("current")
_FsApProfL2SrcMac_Type = TruthValue
_FsApProfL2SrcMac_Object = MibTableColumn
fsApProfL2SrcMac = _FsApProfL2SrcMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 3),
    _FsApProfL2SrcMac_Type()
)
fsApProfL2SrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfL2SrcMac.setStatus("current")
_FsApProfL2DestMac_Type = TruthValue
_FsApProfL2DestMac_Object = MibTableColumn
fsApProfL2DestMac = _FsApProfL2DestMac_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 4),
    _FsApProfL2DestMac_Type()
)
fsApProfL2DestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfL2DestMac.setStatus("current")
_FsApProfL2Pro_Type = TruthValue
_FsApProfL2Pro_Object = MibTableColumn
fsApProfL2Pro = _FsApProfL2Pro_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 5),
    _FsApProfL2Pro_Type()
)
fsApProfL2Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfL2Pro.setStatus("current")
_FsApProfL2Vlan_Type = TruthValue
_FsApProfL2Vlan_Object = MibTableColumn
fsApProfL2Vlan = _FsApProfL2Vlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 6),
    _FsApProfL2Vlan_Type()
)
fsApProfL2Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfL2Vlan.setStatus("current")
_FsApProfL2SrcPort_Type = TruthValue
_FsApProfL2SrcPort_Object = MibTableColumn
fsApProfL2SrcPort = _FsApProfL2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 7),
    _FsApProfL2SrcPort_Type()
)
fsApProfL2SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfL2SrcPort.setStatus("current")
_FsApProfIpv4SrcIp_Type = TruthValue
_FsApProfIpv4SrcIp_Object = MibTableColumn
fsApProfIpv4SrcIp = _FsApProfIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 8),
    _FsApProfIpv4SrcIp_Type()
)
fsApProfIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv4SrcIp.setStatus("current")
_FsApProfIpv4DestIp_Type = TruthValue
_FsApProfIpv4DestIp_Object = MibTableColumn
fsApProfIpv4DestIp = _FsApProfIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 9),
    _FsApProfIpv4DestIp_Type()
)
fsApProfIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv4DestIp.setStatus("current")
_FsApProfIpv4Pro_Type = TruthValue
_FsApProfIpv4Pro_Object = MibTableColumn
fsApProfIpv4Pro = _FsApProfIpv4Pro_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 10),
    _FsApProfIpv4Pro_Type()
)
fsApProfIpv4Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv4Pro.setStatus("current")
_FsApProfIpv4L4SrcPort_Type = TruthValue
_FsApProfIpv4L4SrcPort_Object = MibTableColumn
fsApProfIpv4L4SrcPort = _FsApProfIpv4L4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 11),
    _FsApProfIpv4L4SrcPort_Type()
)
fsApProfIpv4L4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv4L4SrcPort.setStatus("current")
_FsApProfIpv4L4DestPort_Type = TruthValue
_FsApProfIpv4L4DestPort_Object = MibTableColumn
fsApProfIpv4L4DestPort = _FsApProfIpv4L4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 12),
    _FsApProfIpv4L4DestPort_Type()
)
fsApProfIpv4L4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv4L4DestPort.setStatus("current")
_FsApProfIpv4Vlan_Type = TruthValue
_FsApProfIpv4Vlan_Object = MibTableColumn
fsApProfIpv4Vlan = _FsApProfIpv4Vlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 13),
    _FsApProfIpv4Vlan_Type()
)
fsApProfIpv4Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv4Vlan.setStatus("current")
_FsApProfIpv4SrcPort_Type = TruthValue
_FsApProfIpv4SrcPort_Object = MibTableColumn
fsApProfIpv4SrcPort = _FsApProfIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 14),
    _FsApProfIpv4SrcPort_Type()
)
fsApProfIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv4SrcPort.setStatus("current")
_FsApProfIpv6SrcIp_Type = TruthValue
_FsApProfIpv6SrcIp_Object = MibTableColumn
fsApProfIpv6SrcIp = _FsApProfIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 15),
    _FsApProfIpv6SrcIp_Type()
)
fsApProfIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv6SrcIp.setStatus("current")
_FsApProfIpv6DestIp_Type = TruthValue
_FsApProfIpv6DestIp_Object = MibTableColumn
fsApProfIpv6DestIp = _FsApProfIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 16),
    _FsApProfIpv6DestIp_Type()
)
fsApProfIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv6DestIp.setStatus("current")
_FsApProfIpv6Pro_Type = TruthValue
_FsApProfIpv6Pro_Object = MibTableColumn
fsApProfIpv6Pro = _FsApProfIpv6Pro_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 17),
    _FsApProfIpv6Pro_Type()
)
fsApProfIpv6Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv6Pro.setStatus("current")
_FsApProfIpv6L4SrcPort_Type = TruthValue
_FsApProfIpv6L4SrcPort_Object = MibTableColumn
fsApProfIpv6L4SrcPort = _FsApProfIpv6L4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 18),
    _FsApProfIpv6L4SrcPort_Type()
)
fsApProfIpv6L4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv6L4SrcPort.setStatus("current")
_FsApProfIpv6L4DestPort_Type = TruthValue
_FsApProfIpv6L4DestPort_Object = MibTableColumn
fsApProfIpv6L4DestPort = _FsApProfIpv6L4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 19),
    _FsApProfIpv6L4DestPort_Type()
)
fsApProfIpv6L4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv6L4DestPort.setStatus("current")
_FsApProfIpv6Vlan_Type = TruthValue
_FsApProfIpv6Vlan_Object = MibTableColumn
fsApProfIpv6Vlan = _FsApProfIpv6Vlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 20),
    _FsApProfIpv6Vlan_Type()
)
fsApProfIpv6Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv6Vlan.setStatus("current")
_FsApProfIpv6SrcPort_Type = TruthValue
_FsApProfIpv6SrcPort_Object = MibTableColumn
fsApProfIpv6SrcPort = _FsApProfIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 21),
    _FsApProfIpv6SrcPort_Type()
)
fsApProfIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfIpv6SrcPort.setStatus("current")
_FsApProfMplsTopLabel_Type = TruthValue
_FsApProfMplsTopLabel_Object = MibTableColumn
fsApProfMplsTopLabel = _FsApProfMplsTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 22),
    _FsApProfMplsTopLabel_Type()
)
fsApProfMplsTopLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfMplsTopLabel.setStatus("current")
_FsApProfMpls2ndLabel_Type = TruthValue
_FsApProfMpls2ndLabel_Object = MibTableColumn
fsApProfMpls2ndLabel = _FsApProfMpls2ndLabel_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 23),
    _FsApProfMpls2ndLabel_Type()
)
fsApProfMpls2ndLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfMpls2ndLabel.setStatus("current")
_FsApProfMplsSrcIp_Type = TruthValue
_FsApProfMplsSrcIp_Object = MibTableColumn
fsApProfMplsSrcIp = _FsApProfMplsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 24),
    _FsApProfMplsSrcIp_Type()
)
fsApProfMplsSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfMplsSrcIp.setStatus("current")
_FsApProfMplsDestIp_Type = TruthValue
_FsApProfMplsDestIp_Object = MibTableColumn
fsApProfMplsDestIp = _FsApProfMplsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 25),
    _FsApProfMplsDestIp_Type()
)
fsApProfMplsDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfMplsDestIp.setStatus("current")
_FsApProfMplsVlan_Type = TruthValue
_FsApProfMplsVlan_Object = MibTableColumn
fsApProfMplsVlan = _FsApProfMplsVlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 26),
    _FsApProfMplsVlan_Type()
)
fsApProfMplsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfMplsVlan.setStatus("current")
_FsApProfMplsSrcPort_Type = TruthValue
_FsApProfMplsSrcPort_Object = MibTableColumn
fsApProfMplsSrcPort = _FsApProfMplsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 1, 9, 1, 27),
    _FsApProfMplsSrcPort_Type()
)
fsApProfMplsSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsApProfMplsSrcPort.setStatus("current")
_FsApMIBConformance_ObjectIdentity = ObjectIdentity
fsApMIBConformance = _FsApMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 2)
)
_FsApMIBCompliances_ObjectIdentity = ObjectIdentity
fsApMIBCompliances = _FsApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 2, 1)
)
_FsApMIBGroups_ObjectIdentity = ObjectIdentity
fsApMIBGroups = _FsApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 2, 2)
)

# Managed Objects groups

fsApMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 2, 2, 1)
)
fsApMIBGroup.setObjects(
      *(("FS-AP-MIB", "fsApMaxNumber"),
        ("FS-AP-MIB", "fsApCurrentNumber"),
        ("FS-AP-MIB", "fsApPortConfigApIndex"),
        ("FS-AP-MIB", "fsApIndex"),
        ("FS-AP-MIB", "fsApMemberAction"),
        ("FS-AP-MIB", "fsApMaxPtNumber"),
        ("FS-AP-MIB", "fsApFlowBalance"),
        ("FS-AP-MIB", "fsApConfigNumber"),
        ("FS-AP-MIB", "fsApConfigIndex"),
        ("FS-AP-MIB", "fsApConfigMaxPtNumber"),
        ("FS-AP-MIB", "fsApConfigCurrentPtNumber"),
        ("FS-AP-MIB", "fsApConfigPortMember"),
        ("FS-AP-MIB", "fsApConfigAction"),
        ("FS-AP-MIB", "fsApPortMemberPortIndex"),
        ("FS-AP-MIB", "fsApPortMemberApNumber"),
        ("FS-AP-MIB", "fsApPortMemberAction"),
        ("FS-AP-MIB", "fsApPortMemberLacpStatus"),
        ("FS-AP-MIB", "fsApProfL2SrcMac"),
        ("FS-AP-MIB", "fsApProfL2DestMac"),
        ("FS-AP-MIB", "fsApProfL2Pro"),
        ("FS-AP-MIB", "fsApProfL2Vlan"),
        ("FS-AP-MIB", "fsApProfL2SrcPort"),
        ("FS-AP-MIB", "fsApProfIpv4SrcIp"),
        ("FS-AP-MIB", "fsApProfIpv4DestIp"),
        ("FS-AP-MIB", "fsApProfIpv4Pro"),
        ("FS-AP-MIB", "fsApProfIpv4L4SrcPort"),
        ("FS-AP-MIB", "fsApProfIpv4L4DestPort"),
        ("FS-AP-MIB", "fsApProfIpv4Vlan"),
        ("FS-AP-MIB", "fsApProfIpv4SrcPort"),
        ("FS-AP-MIB", "fsApProfIpv6SrcIp"),
        ("FS-AP-MIB", "fsApProfIpv6DestIp"),
        ("FS-AP-MIB", "fsApProfIpv6Pro"),
        ("FS-AP-MIB", "fsApProfIpv6L4SrcPort"),
        ("FS-AP-MIB", "fsApProfIpv6L4DestPort"),
        ("FS-AP-MIB", "fsApProfIpv6Vlan"),
        ("FS-AP-MIB", "fsApProfIpv6SrcPort"),
        ("FS-AP-MIB", "fsApProfMplsTopLabel"),
        ("FS-AP-MIB", "fsApProfMpls2ndLabel"),
        ("FS-AP-MIB", "fsApProfMplsSrcIp"),
        ("FS-AP-MIB", "fsApProfMplsDestIp"),
        ("FS-AP-MIB", "fsApProfMplsVlan"),
        ("FS-AP-MIB", "fsApProfMplsSrcPort"))
)
if mibBuilder.loadTexts:
    fsApMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsApMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 7, 2, 1, 1)
)
fsApMIBCompliance.setObjects(
    ("FS-AP-MIB", "fsApMIBGroup")
)
if mibBuilder.loadTexts:
    fsApMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-AP-MIB",
    **{"fsApMIB": fsApMIB,
       "fsApMIBObjects": fsApMIBObjects,
       "fsApMaxNumber": fsApMaxNumber,
       "fsApCurrentNumber": fsApCurrentNumber,
       "fsApPortConfigTable": fsApPortConfigTable,
       "fsApPortConfigEntry": fsApPortConfigEntry,
       "fsApPortConfigPortIndex": fsApPortConfigPortIndex,
       "fsApPortConfigApIndex": fsApPortConfigApIndex,
       "fsApTable": fsApTable,
       "fsApEntry": fsApEntry,
       "fsApIndex": fsApIndex,
       "fsApMemberAction": fsApMemberAction,
       "fsApPossibleMember": fsApPossibleMember,
       "fsApMaxPtNumber": fsApMaxPtNumber,
       "fsApFlowBalance": fsApFlowBalance,
       "fsApConfigTable": fsApConfigTable,
       "fsApConfigEntry": fsApConfigEntry,
       "fsApConfigNumber": fsApConfigNumber,
       "fsApConfigIndex": fsApConfigIndex,
       "fsApConfigMaxPtNumber": fsApConfigMaxPtNumber,
       "fsApConfigCurrentPtNumber": fsApConfigCurrentPtNumber,
       "fsApConfigPortMember": fsApConfigPortMember,
       "fsApConfigAction": fsApConfigAction,
       "fsApPortMemberTable": fsApPortMemberTable,
       "fsApPortMemberEntry": fsApPortMemberEntry,
       "fsApPortMemberPortIndex": fsApPortMemberPortIndex,
       "fsApPortMemberApNumber": fsApPortMemberApNumber,
       "fsApPortMemberAction": fsApPortMemberAction,
       "fsApPortMemberLacpStatus": fsApPortMemberLacpStatus,
       "fsApBalcProfName": fsApBalcProfName,
       "fsApProfTable": fsApProfTable,
       "fsApProfEntry": fsApProfEntry,
       "fsApProfIdx": fsApProfIdx,
       "fsApProfName": fsApProfName,
       "fsApProfL2SrcMac": fsApProfL2SrcMac,
       "fsApProfL2DestMac": fsApProfL2DestMac,
       "fsApProfL2Pro": fsApProfL2Pro,
       "fsApProfL2Vlan": fsApProfL2Vlan,
       "fsApProfL2SrcPort": fsApProfL2SrcPort,
       "fsApProfIpv4SrcIp": fsApProfIpv4SrcIp,
       "fsApProfIpv4DestIp": fsApProfIpv4DestIp,
       "fsApProfIpv4Pro": fsApProfIpv4Pro,
       "fsApProfIpv4L4SrcPort": fsApProfIpv4L4SrcPort,
       "fsApProfIpv4L4DestPort": fsApProfIpv4L4DestPort,
       "fsApProfIpv4Vlan": fsApProfIpv4Vlan,
       "fsApProfIpv4SrcPort": fsApProfIpv4SrcPort,
       "fsApProfIpv6SrcIp": fsApProfIpv6SrcIp,
       "fsApProfIpv6DestIp": fsApProfIpv6DestIp,
       "fsApProfIpv6Pro": fsApProfIpv6Pro,
       "fsApProfIpv6L4SrcPort": fsApProfIpv6L4SrcPort,
       "fsApProfIpv6L4DestPort": fsApProfIpv6L4DestPort,
       "fsApProfIpv6Vlan": fsApProfIpv6Vlan,
       "fsApProfIpv6SrcPort": fsApProfIpv6SrcPort,
       "fsApProfMplsTopLabel": fsApProfMplsTopLabel,
       "fsApProfMpls2ndLabel": fsApProfMpls2ndLabel,
       "fsApProfMplsSrcIp": fsApProfMplsSrcIp,
       "fsApProfMplsDestIp": fsApProfMplsDestIp,
       "fsApProfMplsVlan": fsApProfMplsVlan,
       "fsApProfMplsSrcPort": fsApProfMplsSrcPort,
       "fsApMIBConformance": fsApMIBConformance,
       "fsApMIBCompliances": fsApMIBCompliances,
       "fsApMIBCompliance": fsApMIBCompliance,
       "fsApMIBGroups": fsApMIBGroups,
       "fsApMIBGroup": fsApMIBGroup}
)
