# SNMP MIB module (QTECH-AP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-AP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:50 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex",
    "MemberMap")

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

qtechApMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7)
)
if mibBuilder.loadTexts:
    qtechApMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechApMIBObjects_ObjectIdentity = ObjectIdentity
qtechApMIBObjects = _QtechApMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1)
)
_QtechApMaxNumber_Type = Integer32
_QtechApMaxNumber_Object = MibScalar
qtechApMaxNumber = _QtechApMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 1),
    _QtechApMaxNumber_Type()
)
qtechApMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMaxNumber.setStatus("current")
_QtechApCurrentNumber_Type = Integer32
_QtechApCurrentNumber_Object = MibScalar
qtechApCurrentNumber = _QtechApCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 2),
    _QtechApCurrentNumber_Type()
)
qtechApCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApCurrentNumber.setStatus("current")
_QtechApPortConfigTable_Object = MibTable
qtechApPortConfigTable = _QtechApPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 3)
)
if mibBuilder.loadTexts:
    qtechApPortConfigTable.setStatus("obsolete")
_QtechApPortConfigEntry_Object = MibTableRow
qtechApPortConfigEntry = _QtechApPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 3, 1)
)
qtechApPortConfigEntry.setIndexNames(
    (0, "QTECH-AP-MIB", "qtechApPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    qtechApPortConfigEntry.setStatus("obsolete")
_QtechApPortConfigPortIndex_Type = IfIndex
_QtechApPortConfigPortIndex_Object = MibTableColumn
qtechApPortConfigPortIndex = _QtechApPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 3, 1, 1),
    _QtechApPortConfigPortIndex_Type()
)
qtechApPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechApPortConfigPortIndex.setStatus("obsolete")
_QtechApPortConfigApIndex_Type = IfIndex
_QtechApPortConfigApIndex_Object = MibTableColumn
qtechApPortConfigApIndex = _QtechApPortConfigApIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 3, 1, 2),
    _QtechApPortConfigApIndex_Type()
)
qtechApPortConfigApIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApPortConfigApIndex.setStatus("obsolete")
_QtechApTable_Object = MibTable
qtechApTable = _QtechApTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 4)
)
if mibBuilder.loadTexts:
    qtechApTable.setStatus("obsolete")
_QtechApEntry_Object = MibTableRow
qtechApEntry = _QtechApEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 4, 1)
)
qtechApEntry.setIndexNames(
    (0, "QTECH-AP-MIB", "qtechApIndex"),
)
if mibBuilder.loadTexts:
    qtechApEntry.setStatus("obsolete")
_QtechApIndex_Type = IfIndex
_QtechApIndex_Object = MibTableColumn
qtechApIndex = _QtechApIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 4, 1, 1),
    _QtechApIndex_Type()
)
qtechApIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApIndex.setStatus("obsolete")
_QtechApMemberAction_Type = MemberMap
_QtechApMemberAction_Object = MibTableColumn
qtechApMemberAction = _QtechApMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 4, 1, 2),
    _QtechApMemberAction_Type()
)
qtechApMemberAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMemberAction.setStatus("obsolete")
_QtechApPossibleMember_Type = MemberMap
_QtechApPossibleMember_Object = MibTableColumn
qtechApPossibleMember = _QtechApPossibleMember_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 4, 1, 3),
    _QtechApPossibleMember_Type()
)
qtechApPossibleMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApPossibleMember.setStatus("obsolete")
_QtechApMaxPtNumber_Type = Integer32
_QtechApMaxPtNumber_Object = MibTableColumn
qtechApMaxPtNumber = _QtechApMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 4, 1, 4),
    _QtechApMaxPtNumber_Type()
)
qtechApMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApMaxPtNumber.setStatus("obsolete")


class _QtechApFlowBalance_Type(Integer32):
    """Custom type qtechApFlowBalance based on Integer32"""
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


_QtechApFlowBalance_Type.__name__ = "Integer32"
_QtechApFlowBalance_Object = MibScalar
qtechApFlowBalance = _QtechApFlowBalance_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 5),
    _QtechApFlowBalance_Type()
)
qtechApFlowBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApFlowBalance.setStatus("current")
_QtechApConfigTable_Object = MibTable
qtechApConfigTable = _QtechApConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6)
)
if mibBuilder.loadTexts:
    qtechApConfigTable.setStatus("current")
_QtechApConfigEntry_Object = MibTableRow
qtechApConfigEntry = _QtechApConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6, 1)
)
qtechApConfigEntry.setIndexNames(
    (0, "QTECH-AP-MIB", "qtechApConfigNumber"),
)
if mibBuilder.loadTexts:
    qtechApConfigEntry.setStatus("current")
_QtechApConfigNumber_Type = Integer32
_QtechApConfigNumber_Object = MibTableColumn
qtechApConfigNumber = _QtechApConfigNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6, 1, 1),
    _QtechApConfigNumber_Type()
)
qtechApConfigNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApConfigNumber.setStatus("current")
_QtechApConfigIndex_Type = IfIndex
_QtechApConfigIndex_Object = MibTableColumn
qtechApConfigIndex = _QtechApConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6, 1, 2),
    _QtechApConfigIndex_Type()
)
qtechApConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApConfigIndex.setStatus("current")
_QtechApConfigMaxPtNumber_Type = Integer32
_QtechApConfigMaxPtNumber_Object = MibTableColumn
qtechApConfigMaxPtNumber = _QtechApConfigMaxPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6, 1, 3),
    _QtechApConfigMaxPtNumber_Type()
)
qtechApConfigMaxPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApConfigMaxPtNumber.setStatus("current")
_QtechApConfigCurrentPtNumber_Type = Integer32
_QtechApConfigCurrentPtNumber_Object = MibTableColumn
qtechApConfigCurrentPtNumber = _QtechApConfigCurrentPtNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6, 1, 4),
    _QtechApConfigCurrentPtNumber_Type()
)
qtechApConfigCurrentPtNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApConfigCurrentPtNumber.setStatus("current")
_QtechApConfigPortMember_Type = PortList
_QtechApConfigPortMember_Object = MibTableColumn
qtechApConfigPortMember = _QtechApConfigPortMember_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6, 1, 5),
    _QtechApConfigPortMember_Type()
)
qtechApConfigPortMember.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApConfigPortMember.setStatus("current")
_QtechApConfigAction_Type = Integer32
_QtechApConfigAction_Object = MibTableColumn
qtechApConfigAction = _QtechApConfigAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 6, 1, 6),
    _QtechApConfigAction_Type()
)
qtechApConfigAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApConfigAction.setStatus("current")
_QtechApPortMemberTable_Object = MibTable
qtechApPortMemberTable = _QtechApPortMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 7)
)
if mibBuilder.loadTexts:
    qtechApPortMemberTable.setStatus("current")
_QtechApPortMemberEntry_Object = MibTableRow
qtechApPortMemberEntry = _QtechApPortMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 7, 1)
)
qtechApPortMemberEntry.setIndexNames(
    (0, "QTECH-AP-MIB", "qtechApPortMemberPortIndex"),
)
if mibBuilder.loadTexts:
    qtechApPortMemberEntry.setStatus("current")
_QtechApPortMemberPortIndex_Type = IfIndex
_QtechApPortMemberPortIndex_Object = MibTableColumn
qtechApPortMemberPortIndex = _QtechApPortMemberPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 7, 1, 1),
    _QtechApPortMemberPortIndex_Type()
)
qtechApPortMemberPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApPortMemberPortIndex.setStatus("current")
_QtechApPortMemberApNumber_Type = Integer32
_QtechApPortMemberApNumber_Object = MibTableColumn
qtechApPortMemberApNumber = _QtechApPortMemberApNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 7, 1, 2),
    _QtechApPortMemberApNumber_Type()
)
qtechApPortMemberApNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApPortMemberApNumber.setStatus("current")
_QtechApPortMemberAction_Type = Integer32
_QtechApPortMemberAction_Object = MibTableColumn
qtechApPortMemberAction = _QtechApPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 7, 1, 3),
    _QtechApPortMemberAction_Type()
)
qtechApPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApPortMemberAction.setStatus("current")
_QtechApBalcProfName_Type = DisplayString
_QtechApBalcProfName_Object = MibScalar
qtechApBalcProfName = _QtechApBalcProfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 8),
    _QtechApBalcProfName_Type()
)
qtechApBalcProfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApBalcProfName.setStatus("current")
_QtechApProfTable_Object = MibTable
qtechApProfTable = _QtechApProfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9)
)
if mibBuilder.loadTexts:
    qtechApProfTable.setStatus("current")
_QtechApProfEntry_Object = MibTableRow
qtechApProfEntry = _QtechApProfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1)
)
qtechApProfEntry.setIndexNames(
    (0, "QTECH-AP-MIB", "qtechApProfIdx"),
)
if mibBuilder.loadTexts:
    qtechApProfEntry.setStatus("current")
_QtechApProfIdx_Type = Integer32
_QtechApProfIdx_Object = MibTableColumn
qtechApProfIdx = _QtechApProfIdx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 1),
    _QtechApProfIdx_Type()
)
qtechApProfIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApProfIdx.setStatus("current")
_QtechApProfName_Type = DisplayString
_QtechApProfName_Object = MibTableColumn
qtechApProfName = _QtechApProfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 2),
    _QtechApProfName_Type()
)
qtechApProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechApProfName.setStatus("current")
_QtechApProfL2SrcMac_Type = TruthValue
_QtechApProfL2SrcMac_Object = MibTableColumn
qtechApProfL2SrcMac = _QtechApProfL2SrcMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 3),
    _QtechApProfL2SrcMac_Type()
)
qtechApProfL2SrcMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfL2SrcMac.setStatus("current")
_QtechApProfL2DestMac_Type = TruthValue
_QtechApProfL2DestMac_Object = MibTableColumn
qtechApProfL2DestMac = _QtechApProfL2DestMac_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 4),
    _QtechApProfL2DestMac_Type()
)
qtechApProfL2DestMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfL2DestMac.setStatus("current")
_QtechApProfL2Pro_Type = TruthValue
_QtechApProfL2Pro_Object = MibTableColumn
qtechApProfL2Pro = _QtechApProfL2Pro_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 5),
    _QtechApProfL2Pro_Type()
)
qtechApProfL2Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfL2Pro.setStatus("current")
_QtechApProfL2Vlan_Type = TruthValue
_QtechApProfL2Vlan_Object = MibTableColumn
qtechApProfL2Vlan = _QtechApProfL2Vlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 6),
    _QtechApProfL2Vlan_Type()
)
qtechApProfL2Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfL2Vlan.setStatus("current")
_QtechApProfL2SrcPort_Type = TruthValue
_QtechApProfL2SrcPort_Object = MibTableColumn
qtechApProfL2SrcPort = _QtechApProfL2SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 7),
    _QtechApProfL2SrcPort_Type()
)
qtechApProfL2SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfL2SrcPort.setStatus("current")
_QtechApProfIpv4SrcIp_Type = TruthValue
_QtechApProfIpv4SrcIp_Object = MibTableColumn
qtechApProfIpv4SrcIp = _QtechApProfIpv4SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 8),
    _QtechApProfIpv4SrcIp_Type()
)
qtechApProfIpv4SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv4SrcIp.setStatus("current")
_QtechApProfIpv4DestIp_Type = TruthValue
_QtechApProfIpv4DestIp_Object = MibTableColumn
qtechApProfIpv4DestIp = _QtechApProfIpv4DestIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 9),
    _QtechApProfIpv4DestIp_Type()
)
qtechApProfIpv4DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv4DestIp.setStatus("current")
_QtechApProfIpv4Pro_Type = TruthValue
_QtechApProfIpv4Pro_Object = MibTableColumn
qtechApProfIpv4Pro = _QtechApProfIpv4Pro_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 10),
    _QtechApProfIpv4Pro_Type()
)
qtechApProfIpv4Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv4Pro.setStatus("current")
_QtechApProfIpv4L4SrcPort_Type = TruthValue
_QtechApProfIpv4L4SrcPort_Object = MibTableColumn
qtechApProfIpv4L4SrcPort = _QtechApProfIpv4L4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 11),
    _QtechApProfIpv4L4SrcPort_Type()
)
qtechApProfIpv4L4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv4L4SrcPort.setStatus("current")
_QtechApProfIpv4L4DestPort_Type = TruthValue
_QtechApProfIpv4L4DestPort_Object = MibTableColumn
qtechApProfIpv4L4DestPort = _QtechApProfIpv4L4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 12),
    _QtechApProfIpv4L4DestPort_Type()
)
qtechApProfIpv4L4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv4L4DestPort.setStatus("current")
_QtechApProfIpv4Vlan_Type = TruthValue
_QtechApProfIpv4Vlan_Object = MibTableColumn
qtechApProfIpv4Vlan = _QtechApProfIpv4Vlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 13),
    _QtechApProfIpv4Vlan_Type()
)
qtechApProfIpv4Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv4Vlan.setStatus("current")
_QtechApProfIpv4SrcPort_Type = TruthValue
_QtechApProfIpv4SrcPort_Object = MibTableColumn
qtechApProfIpv4SrcPort = _QtechApProfIpv4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 14),
    _QtechApProfIpv4SrcPort_Type()
)
qtechApProfIpv4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv4SrcPort.setStatus("current")
_QtechApProfIpv6SrcIp_Type = TruthValue
_QtechApProfIpv6SrcIp_Object = MibTableColumn
qtechApProfIpv6SrcIp = _QtechApProfIpv6SrcIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 15),
    _QtechApProfIpv6SrcIp_Type()
)
qtechApProfIpv6SrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv6SrcIp.setStatus("current")
_QtechApProfIpv6DestIp_Type = TruthValue
_QtechApProfIpv6DestIp_Object = MibTableColumn
qtechApProfIpv6DestIp = _QtechApProfIpv6DestIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 16),
    _QtechApProfIpv6DestIp_Type()
)
qtechApProfIpv6DestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv6DestIp.setStatus("current")
_QtechApProfIpv6Pro_Type = TruthValue
_QtechApProfIpv6Pro_Object = MibTableColumn
qtechApProfIpv6Pro = _QtechApProfIpv6Pro_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 17),
    _QtechApProfIpv6Pro_Type()
)
qtechApProfIpv6Pro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv6Pro.setStatus("current")
_QtechApProfIpv6L4SrcPort_Type = TruthValue
_QtechApProfIpv6L4SrcPort_Object = MibTableColumn
qtechApProfIpv6L4SrcPort = _QtechApProfIpv6L4SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 18),
    _QtechApProfIpv6L4SrcPort_Type()
)
qtechApProfIpv6L4SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv6L4SrcPort.setStatus("current")
_QtechApProfIpv6L4DestPort_Type = TruthValue
_QtechApProfIpv6L4DestPort_Object = MibTableColumn
qtechApProfIpv6L4DestPort = _QtechApProfIpv6L4DestPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 19),
    _QtechApProfIpv6L4DestPort_Type()
)
qtechApProfIpv6L4DestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv6L4DestPort.setStatus("current")
_QtechApProfIpv6Vlan_Type = TruthValue
_QtechApProfIpv6Vlan_Object = MibTableColumn
qtechApProfIpv6Vlan = _QtechApProfIpv6Vlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 20),
    _QtechApProfIpv6Vlan_Type()
)
qtechApProfIpv6Vlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv6Vlan.setStatus("current")
_QtechApProfIpv6SrcPort_Type = TruthValue
_QtechApProfIpv6SrcPort_Object = MibTableColumn
qtechApProfIpv6SrcPort = _QtechApProfIpv6SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 21),
    _QtechApProfIpv6SrcPort_Type()
)
qtechApProfIpv6SrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfIpv6SrcPort.setStatus("current")
_QtechApProfMplsTopLabel_Type = TruthValue
_QtechApProfMplsTopLabel_Object = MibTableColumn
qtechApProfMplsTopLabel = _QtechApProfMplsTopLabel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 22),
    _QtechApProfMplsTopLabel_Type()
)
qtechApProfMplsTopLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfMplsTopLabel.setStatus("current")
_QtechApProfMpls2ndLabel_Type = TruthValue
_QtechApProfMpls2ndLabel_Object = MibTableColumn
qtechApProfMpls2ndLabel = _QtechApProfMpls2ndLabel_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 23),
    _QtechApProfMpls2ndLabel_Type()
)
qtechApProfMpls2ndLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfMpls2ndLabel.setStatus("current")
_QtechApProfMplsSrcIp_Type = TruthValue
_QtechApProfMplsSrcIp_Object = MibTableColumn
qtechApProfMplsSrcIp = _QtechApProfMplsSrcIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 24),
    _QtechApProfMplsSrcIp_Type()
)
qtechApProfMplsSrcIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfMplsSrcIp.setStatus("current")
_QtechApProfMplsDestIp_Type = TruthValue
_QtechApProfMplsDestIp_Object = MibTableColumn
qtechApProfMplsDestIp = _QtechApProfMplsDestIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 25),
    _QtechApProfMplsDestIp_Type()
)
qtechApProfMplsDestIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfMplsDestIp.setStatus("current")
_QtechApProfMplsVlan_Type = TruthValue
_QtechApProfMplsVlan_Object = MibTableColumn
qtechApProfMplsVlan = _QtechApProfMplsVlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 26),
    _QtechApProfMplsVlan_Type()
)
qtechApProfMplsVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfMplsVlan.setStatus("current")
_QtechApProfMplsSrcPort_Type = TruthValue
_QtechApProfMplsSrcPort_Object = MibTableColumn
qtechApProfMplsSrcPort = _QtechApProfMplsSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 1, 9, 1, 27),
    _QtechApProfMplsSrcPort_Type()
)
qtechApProfMplsSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechApProfMplsSrcPort.setStatus("current")
_QtechApMIBConformance_ObjectIdentity = ObjectIdentity
qtechApMIBConformance = _QtechApMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 2)
)
_QtechApMIBCompliances_ObjectIdentity = ObjectIdentity
qtechApMIBCompliances = _QtechApMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 2, 1)
)
_QtechApMIBGroups_ObjectIdentity = ObjectIdentity
qtechApMIBGroups = _QtechApMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 2, 2)
)

# Managed Objects groups

qtechApMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 2, 2, 1)
)
qtechApMIBGroup.setObjects(
      *(("QTECH-AP-MIB", "qtechApMaxNumber"),
        ("QTECH-AP-MIB", "qtechApCurrentNumber"),
        ("QTECH-AP-MIB", "qtechApPortConfigApIndex"),
        ("QTECH-AP-MIB", "qtechApIndex"),
        ("QTECH-AP-MIB", "qtechApMemberAction"),
        ("QTECH-AP-MIB", "qtechApMaxPtNumber"),
        ("QTECH-AP-MIB", "qtechApFlowBalance"),
        ("QTECH-AP-MIB", "qtechApConfigNumber"),
        ("QTECH-AP-MIB", "qtechApConfigIndex"),
        ("QTECH-AP-MIB", "qtechApConfigMaxPtNumber"),
        ("QTECH-AP-MIB", "qtechApConfigCurrentPtNumber"),
        ("QTECH-AP-MIB", "qtechApConfigPortMember"),
        ("QTECH-AP-MIB", "qtechApConfigAction"),
        ("QTECH-AP-MIB", "qtechApPortMemberPortIndex"),
        ("QTECH-AP-MIB", "qtechApPortMemberApNumber"),
        ("QTECH-AP-MIB", "qtechApPortMemberAction"),
        ("QTECH-AP-MIB", "qtechApProfL2SrcMac"),
        ("QTECH-AP-MIB", "qtechApProfL2DestMac"),
        ("QTECH-AP-MIB", "qtechApProfL2Pro"),
        ("QTECH-AP-MIB", "qtechApProfL2Vlan"),
        ("QTECH-AP-MIB", "qtechApProfL2SrcPort"),
        ("QTECH-AP-MIB", "qtechApProfIpv4SrcIp"),
        ("QTECH-AP-MIB", "qtechApProfIpv4DestIp"),
        ("QTECH-AP-MIB", "qtechApProfIpv4Pro"),
        ("QTECH-AP-MIB", "qtechApProfIpv4L4SrcPort"),
        ("QTECH-AP-MIB", "qtechApProfIpv4L4DestPort"),
        ("QTECH-AP-MIB", "qtechApProfIpv4Vlan"),
        ("QTECH-AP-MIB", "qtechApProfIpv4SrcPort"),
        ("QTECH-AP-MIB", "qtechApProfIpv6SrcIp"),
        ("QTECH-AP-MIB", "qtechApProfIpv6DestIp"),
        ("QTECH-AP-MIB", "qtechApProfIpv6Pro"),
        ("QTECH-AP-MIB", "qtechApProfIpv6L4SrcPort"),
        ("QTECH-AP-MIB", "qtechApProfIpv6L4DestPort"),
        ("QTECH-AP-MIB", "qtechApProfIpv6Vlan"),
        ("QTECH-AP-MIB", "qtechApProfIpv6SrcPort"),
        ("QTECH-AP-MIB", "qtechApProfMplsTopLabel"),
        ("QTECH-AP-MIB", "qtechApProfMpls2ndLabel"),
        ("QTECH-AP-MIB", "qtechApProfMplsSrcIp"),
        ("QTECH-AP-MIB", "qtechApProfMplsDestIp"),
        ("QTECH-AP-MIB", "qtechApProfMplsVlan"),
        ("QTECH-AP-MIB", "qtechApProfMplsSrcPort"))
)
if mibBuilder.loadTexts:
    qtechApMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechApMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 7, 2, 1, 1)
)
qtechApMIBCompliance.setObjects(
    ("QTECH-AP-MIB", "qtechApMIBGroup")
)
if mibBuilder.loadTexts:
    qtechApMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-AP-MIB",
    **{"qtechApMIB": qtechApMIB,
       "qtechApMIBObjects": qtechApMIBObjects,
       "qtechApMaxNumber": qtechApMaxNumber,
       "qtechApCurrentNumber": qtechApCurrentNumber,
       "qtechApPortConfigTable": qtechApPortConfigTable,
       "qtechApPortConfigEntry": qtechApPortConfigEntry,
       "qtechApPortConfigPortIndex": qtechApPortConfigPortIndex,
       "qtechApPortConfigApIndex": qtechApPortConfigApIndex,
       "qtechApTable": qtechApTable,
       "qtechApEntry": qtechApEntry,
       "qtechApIndex": qtechApIndex,
       "qtechApMemberAction": qtechApMemberAction,
       "qtechApPossibleMember": qtechApPossibleMember,
       "qtechApMaxPtNumber": qtechApMaxPtNumber,
       "qtechApFlowBalance": qtechApFlowBalance,
       "qtechApConfigTable": qtechApConfigTable,
       "qtechApConfigEntry": qtechApConfigEntry,
       "qtechApConfigNumber": qtechApConfigNumber,
       "qtechApConfigIndex": qtechApConfigIndex,
       "qtechApConfigMaxPtNumber": qtechApConfigMaxPtNumber,
       "qtechApConfigCurrentPtNumber": qtechApConfigCurrentPtNumber,
       "qtechApConfigPortMember": qtechApConfigPortMember,
       "qtechApConfigAction": qtechApConfigAction,
       "qtechApPortMemberTable": qtechApPortMemberTable,
       "qtechApPortMemberEntry": qtechApPortMemberEntry,
       "qtechApPortMemberPortIndex": qtechApPortMemberPortIndex,
       "qtechApPortMemberApNumber": qtechApPortMemberApNumber,
       "qtechApPortMemberAction": qtechApPortMemberAction,
       "qtechApBalcProfName": qtechApBalcProfName,
       "qtechApProfTable": qtechApProfTable,
       "qtechApProfEntry": qtechApProfEntry,
       "qtechApProfIdx": qtechApProfIdx,
       "qtechApProfName": qtechApProfName,
       "qtechApProfL2SrcMac": qtechApProfL2SrcMac,
       "qtechApProfL2DestMac": qtechApProfL2DestMac,
       "qtechApProfL2Pro": qtechApProfL2Pro,
       "qtechApProfL2Vlan": qtechApProfL2Vlan,
       "qtechApProfL2SrcPort": qtechApProfL2SrcPort,
       "qtechApProfIpv4SrcIp": qtechApProfIpv4SrcIp,
       "qtechApProfIpv4DestIp": qtechApProfIpv4DestIp,
       "qtechApProfIpv4Pro": qtechApProfIpv4Pro,
       "qtechApProfIpv4L4SrcPort": qtechApProfIpv4L4SrcPort,
       "qtechApProfIpv4L4DestPort": qtechApProfIpv4L4DestPort,
       "qtechApProfIpv4Vlan": qtechApProfIpv4Vlan,
       "qtechApProfIpv4SrcPort": qtechApProfIpv4SrcPort,
       "qtechApProfIpv6SrcIp": qtechApProfIpv6SrcIp,
       "qtechApProfIpv6DestIp": qtechApProfIpv6DestIp,
       "qtechApProfIpv6Pro": qtechApProfIpv6Pro,
       "qtechApProfIpv6L4SrcPort": qtechApProfIpv6L4SrcPort,
       "qtechApProfIpv6L4DestPort": qtechApProfIpv6L4DestPort,
       "qtechApProfIpv6Vlan": qtechApProfIpv6Vlan,
       "qtechApProfIpv6SrcPort": qtechApProfIpv6SrcPort,
       "qtechApProfMplsTopLabel": qtechApProfMplsTopLabel,
       "qtechApProfMpls2ndLabel": qtechApProfMpls2ndLabel,
       "qtechApProfMplsSrcIp": qtechApProfMplsSrcIp,
       "qtechApProfMplsDestIp": qtechApProfMplsDestIp,
       "qtechApProfMplsVlan": qtechApProfMplsVlan,
       "qtechApProfMplsSrcPort": qtechApProfMplsSrcPort,
       "qtechApMIBConformance": qtechApMIBConformance,
       "qtechApMIBCompliances": qtechApMIBCompliances,
       "qtechApMIBCompliance": qtechApMIBCompliance,
       "qtechApMIBGroups": qtechApMIBGroups,
       "qtechApMIBGroup": qtechApMIBGroup}
)
