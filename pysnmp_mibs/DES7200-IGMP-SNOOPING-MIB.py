# SNMP MIB module (DES7200-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DES7200-IGMP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:07 2025
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

(ConfigStatus,
 IfIndex,
 MemberMap) = mibBuilder.importSymbols(
    "DES7200-TC",
    "ConfigStatus",
    "IfIndex",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

myIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8)
)
if mibBuilder.loadTexts:
    myIgmpSnoopingMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyIgmpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
myIgmpSnoopingMIBObjects = _MyIgmpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1)
)


class _MySNIgmpWorkingMode_Type(Integer32):
    """Custom type mySNIgmpWorkingMode based on Integer32"""
    defaultValue = 1

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
        *(("disabled", 1),
          ("svgl", 2),
          ("ivgl", 3),
          ("ivgl-svgl", 4))
    )


_MySNIgmpWorkingMode_Type.__name__ = "Integer32"
_MySNIgmpWorkingMode_Object = MibScalar
mySNIgmpWorkingMode = _MySNIgmpWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 1),
    _MySNIgmpWorkingMode_Type()
)
mySNIgmpWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpWorkingMode.setStatus("current")


class _MySNIgmpSourcePortCheck_Type(EnabledStatus):
    """Custom type mySNIgmpSourcePortCheck based on EnabledStatus"""
    defaultValue = 2


_MySNIgmpSourcePortCheck_Type.__name__ = "EnabledStatus"
_MySNIgmpSourcePortCheck_Object = MibScalar
mySNIgmpSourcePortCheck = _MySNIgmpSourcePortCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 2),
    _MySNIgmpSourcePortCheck_Type()
)
mySNIgmpSourcePortCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpSourcePortCheck.setStatus("current")


class _MySNIgmpSourceIpCheck_Type(EnabledStatus):
    """Custom type mySNIgmpSourceIpCheck based on EnabledStatus"""
    defaultValue = 2


_MySNIgmpSourceIpCheck_Type.__name__ = "EnabledStatus"
_MySNIgmpSourceIpCheck_Object = MibScalar
mySNIgmpSourceIpCheck = _MySNIgmpSourceIpCheck_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 3),
    _MySNIgmpSourceIpCheck_Type()
)
mySNIgmpSourceIpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpSourceIpCheck.setStatus("current")
_MySNIgmpSourceIpCheckDefIp_Type = IpAddress
_MySNIgmpSourceIpCheckDefIp_Object = MibScalar
mySNIgmpSourceIpCheckDefIp = _MySNIgmpSourceIpCheckDefIp_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 4),
    _MySNIgmpSourceIpCheckDefIp_Type()
)
mySNIgmpSourceIpCheckDefIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpSourceIpCheckDefIp.setStatus("current")
_MySNIgmpSrcIpCheckTable_Object = MibTable
mySNIgmpSrcIpCheckTable = _MySNIgmpSrcIpCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    mySNIgmpSrcIpCheckTable.setStatus("current")
_MySNIgmpSrcIpCheckEntry_Object = MibTableRow
mySNIgmpSrcIpCheckEntry = _MySNIgmpSrcIpCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 5, 1)
)
mySNIgmpSrcIpCheckEntry.setIndexNames(
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSrcIpCheckVID"),
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSrcIpCheckMultiIpAddr"),
)
if mibBuilder.loadTexts:
    mySNIgmpSrcIpCheckEntry.setStatus("current")
_MySNIgmpSrcIpCheckVID_Type = VlanId
_MySNIgmpSrcIpCheckVID_Object = MibTableColumn
mySNIgmpSrcIpCheckVID = _MySNIgmpSrcIpCheckVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 5, 1, 1),
    _MySNIgmpSrcIpCheckVID_Type()
)
mySNIgmpSrcIpCheckVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpSrcIpCheckVID.setStatus("current")
_MySNIgmpSrcIpCheckMultiIpAddr_Type = IpAddress
_MySNIgmpSrcIpCheckMultiIpAddr_Object = MibTableColumn
mySNIgmpSrcIpCheckMultiIpAddr = _MySNIgmpSrcIpCheckMultiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 5, 1, 2),
    _MySNIgmpSrcIpCheckMultiIpAddr_Type()
)
mySNIgmpSrcIpCheckMultiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpSrcIpCheckMultiIpAddr.setStatus("current")
_MySNIgmpSrcIpCheckSrcIpAddr_Type = IpAddress
_MySNIgmpSrcIpCheckSrcIpAddr_Object = MibTableColumn
mySNIgmpSrcIpCheckSrcIpAddr = _MySNIgmpSrcIpCheckSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 5, 1, 3),
    _MySNIgmpSrcIpCheckSrcIpAddr_Type()
)
mySNIgmpSrcIpCheckSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mySNIgmpSrcIpCheckSrcIpAddr.setStatus("current")


class _MySNIgmpSrcIpCheckEntryStatus_Type(Integer32):
    """Custom type mySNIgmpSrcIpCheckEntryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("delete", 2))
    )


_MySNIgmpSrcIpCheckEntryStatus_Type.__name__ = "Integer32"
_MySNIgmpSrcIpCheckEntryStatus_Object = MibTableColumn
mySNIgmpSrcIpCheckEntryStatus = _MySNIgmpSrcIpCheckEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 5, 1, 4),
    _MySNIgmpSrcIpCheckEntryStatus_Type()
)
mySNIgmpSrcIpCheckEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpSrcIpCheckEntryStatus.setStatus("current")
_MySNIgmpPortTable_Object = MibTable
mySNIgmpPortTable = _MySNIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    mySNIgmpPortTable.setStatus("mandatory")
_MySNIgmpPortEntry_Object = MibTableRow
mySNIgmpPortEntry = _MySNIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 6, 1)
)
mySNIgmpPortEntry.setIndexNames(
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpPortRouterVID"),
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpPortIndex"),
)
if mibBuilder.loadTexts:
    mySNIgmpPortEntry.setStatus("mandatory")
_MySNIgmpPortRouterVID_Type = VlanId
_MySNIgmpPortRouterVID_Object = MibTableColumn
mySNIgmpPortRouterVID = _MySNIgmpPortRouterVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 6, 1, 1),
    _MySNIgmpPortRouterVID_Type()
)
mySNIgmpPortRouterVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpPortRouterVID.setStatus("current")
_MySNIgmpPortIndex_Type = IfIndex
_MySNIgmpPortIndex_Object = MibTableColumn
mySNIgmpPortIndex = _MySNIgmpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 6, 1, 2),
    _MySNIgmpPortIndex_Type()
)
mySNIgmpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpPortIndex.setStatus("mandatory")


class _MySNIgmpPortRouterState_Type(Integer32):
    """Custom type mySNIgmpPortRouterState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mrnone", 1),
          ("mrstatic", 2),
          ("mrdynamic", 3))
    )


_MySNIgmpPortRouterState_Type.__name__ = "Integer32"
_MySNIgmpPortRouterState_Object = MibTableColumn
mySNIgmpPortRouterState = _MySNIgmpPortRouterState_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 6, 1, 3),
    _MySNIgmpPortRouterState_Type()
)
mySNIgmpPortRouterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpPortRouterState.setStatus("current")
_MySNIgmpPortRouterProfile_Type = Unsigned32
_MySNIgmpPortRouterProfile_Object = MibTableColumn
mySNIgmpPortRouterProfile = _MySNIgmpPortRouterProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 6, 1, 4),
    _MySNIgmpPortRouterProfile_Type()
)
mySNIgmpPortRouterProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpPortRouterProfile.setStatus("current")
_MySNIgmpGDANumber_Type = Unsigned32
_MySNIgmpGDANumber_Object = MibScalar
mySNIgmpGDANumber = _MySNIgmpGDANumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 7),
    _MySNIgmpGDANumber_Type()
)
mySNIgmpGDANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDANumber.setStatus("current")
_MySNIgmpGDATable_Object = MibTable
mySNIgmpGDATable = _MySNIgmpGDATable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    mySNIgmpGDATable.setStatus("current")
_MySNIgmpGDAEntry_Object = MibTableRow
mySNIgmpGDAEntry = _MySNIgmpGDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 8, 1)
)
mySNIgmpGDAEntry.setIndexNames(
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAVID"),
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAAddr"),
)
if mibBuilder.loadTexts:
    mySNIgmpGDAEntry.setStatus("current")
_MySNIgmpGDAVID_Type = VlanId
_MySNIgmpGDAVID_Object = MibTableColumn
mySNIgmpGDAVID = _MySNIgmpGDAVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 8, 1, 1),
    _MySNIgmpGDAVID_Type()
)
mySNIgmpGDAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDAVID.setStatus("current")
_MySNIgmpGDAAddr_Type = IpAddress
_MySNIgmpGDAAddr_Object = MibTableColumn
mySNIgmpGDAAddr = _MySNIgmpGDAAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 8, 1, 2),
    _MySNIgmpGDAAddr_Type()
)
mySNIgmpGDAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDAAddr.setStatus("current")
_MySNIgmpGDAPortMemberAction_Type = MemberMap
_MySNIgmpGDAPortMemberAction_Object = MibTableColumn
mySNIgmpGDAPortMemberAction = _MySNIgmpGDAPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 8, 1, 3),
    _MySNIgmpGDAPortMemberAction_Type()
)
mySNIgmpGDAPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpGDAPortMemberAction.setStatus("current")
_MySNIgmpGDATrunkMemberAction_Type = MemberMap
_MySNIgmpGDATrunkMemberAction_Object = MibTableColumn
mySNIgmpGDATrunkMemberAction = _MySNIgmpGDATrunkMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 8, 1, 4),
    _MySNIgmpGDATrunkMemberAction_Type()
)
mySNIgmpGDATrunkMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpGDATrunkMemberAction.setStatus("current")
_MySNIgmpSvglVID_Type = Integer32
_MySNIgmpSvglVID_Object = MibScalar
mySNIgmpSvglVID = _MySNIgmpSvglVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 9),
    _MySNIgmpSvglVID_Type()
)
mySNIgmpSvglVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpSvglVID.setStatus("current")
_MySNIgmpSvglProfile_Type = Unsigned32
_MySNIgmpSvglProfile_Object = MibScalar
mySNIgmpSvglProfile = _MySNIgmpSvglProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 10),
    _MySNIgmpSvglProfile_Type()
)
mySNIgmpSvglProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpSvglProfile.setStatus("current")
_MySNIgmpMrLearnTable_Object = MibTable
mySNIgmpMrLearnTable = _MySNIgmpMrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 11)
)
if mibBuilder.loadTexts:
    mySNIgmpMrLearnTable.setStatus("current")
_MySNIgmpMrLearnEntry_Object = MibTableRow
mySNIgmpMrLearnEntry = _MySNIgmpMrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 11, 1)
)
mySNIgmpMrLearnEntry.setIndexNames(
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpMrLearnVID"),
)
if mibBuilder.loadTexts:
    mySNIgmpMrLearnEntry.setStatus("current")
_MySNIgmpMrLearnVID_Type = VlanId
_MySNIgmpMrLearnVID_Object = MibTableColumn
mySNIgmpMrLearnVID = _MySNIgmpMrLearnVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 11, 1, 1),
    _MySNIgmpMrLearnVID_Type()
)
mySNIgmpMrLearnVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpMrLearnVID.setStatus("current")


class _MySNIgmpMrLearnStatus_Type(Integer32):
    """Custom type mySNIgmpMrLearnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("pim-dvmrp", 2))
    )


_MySNIgmpMrLearnStatus_Type.__name__ = "Integer32"
_MySNIgmpMrLearnStatus_Object = MibTableColumn
mySNIgmpMrLearnStatus = _MySNIgmpMrLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 11, 1, 2),
    _MySNIgmpMrLearnStatus_Type()
)
mySNIgmpMrLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpMrLearnStatus.setStatus("current")
_MySNIgmpPortFilteringTable_Object = MibTable
mySNIgmpPortFilteringTable = _MySNIgmpPortFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 12)
)
if mibBuilder.loadTexts:
    mySNIgmpPortFilteringTable.setStatus("current")
_MySNIgmpPortFilteringEntry_Object = MibTableRow
mySNIgmpPortFilteringEntry = _MySNIgmpPortFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 12, 1)
)
mySNIgmpPortFilteringEntry.setIndexNames(
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNPortIndex"),
)
if mibBuilder.loadTexts:
    mySNIgmpPortFilteringEntry.setStatus("current")
_MySNPortIndex_Type = IfIndex
_MySNPortIndex_Object = MibTableColumn
mySNPortIndex = _MySNPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 12, 1, 1),
    _MySNPortIndex_Type()
)
mySNPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNPortIndex.setStatus("current")
_MySNIgmpFilteringProfile_Type = Unsigned32
_MySNIgmpFilteringProfile_Object = MibTableColumn
mySNIgmpFilteringProfile = _MySNIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 12, 1, 2),
    _MySNIgmpFilteringProfile_Type()
)
mySNIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpFilteringProfile.setStatus("current")
_MySNIgmpFilteringMaxGroups_Type = Unsigned32
_MySNIgmpFilteringMaxGroups_Object = MibTableColumn
mySNIgmpFilteringMaxGroups = _MySNIgmpFilteringMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 12, 1, 3),
    _MySNIgmpFilteringMaxGroups_Type()
)
mySNIgmpFilteringMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpFilteringMaxGroups.setStatus("current")
_MySNIgmpGDAConfigTable_Object = MibTable
mySNIgmpGDAConfigTable = _MySNIgmpGDAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 13)
)
if mibBuilder.loadTexts:
    mySNIgmpGDAConfigTable.setStatus("current")
_MySNIgmpGDAConfigEntry_Object = MibTableRow
mySNIgmpGDAConfigEntry = _MySNIgmpGDAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 13, 1)
)
mySNIgmpGDAConfigEntry.setIndexNames(
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAConfigVID"),
    (0, "DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAConfigAddr"),
)
if mibBuilder.loadTexts:
    mySNIgmpGDAConfigEntry.setStatus("current")
_MySNIgmpGDAConfigVID_Type = VlanId
_MySNIgmpGDAConfigVID_Object = MibTableColumn
mySNIgmpGDAConfigVID = _MySNIgmpGDAConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 13, 1, 1),
    _MySNIgmpGDAConfigVID_Type()
)
mySNIgmpGDAConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDAConfigVID.setStatus("current")
_MySNIgmpGDAConfigAddr_Type = IpAddress
_MySNIgmpGDAConfigAddr_Object = MibTableColumn
mySNIgmpGDAConfigAddr = _MySNIgmpGDAConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 13, 1, 2),
    _MySNIgmpGDAConfigAddr_Type()
)
mySNIgmpGDAConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDAConfigAddr.setStatus("current")
_MySNIgmpGDAConfigIfIndex_Type = IfIndex
_MySNIgmpGDAConfigIfIndex_Object = MibTableColumn
mySNIgmpGDAConfigIfIndex = _MySNIgmpGDAConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 13, 1, 3),
    _MySNIgmpGDAConfigIfIndex_Type()
)
mySNIgmpGDAConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDAConfigIfIndex.setStatus("current")


class _MySNIgmpGDAConfigType_Type(Integer32):
    """Custom type mySNIgmpGDAConfigType based on Integer32"""
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
        *(("null", 1),
          ("static", 2),
          ("dynamic", 3),
          ("mrouter", 4))
    )


_MySNIgmpGDAConfigType_Type.__name__ = "Integer32"
_MySNIgmpGDAConfigType_Object = MibTableColumn
mySNIgmpGDAConfigType = _MySNIgmpGDAConfigType_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 13, 1, 4),
    _MySNIgmpGDAConfigType_Type()
)
mySNIgmpGDAConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDAConfigType.setStatus("current")


class _MySNIgmpGDAConfigStatus_Type(Integer32):
    """Custom type mySNIgmpGDAConfigStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_MySNIgmpGDAConfigStatus_Type.__name__ = "Integer32"
_MySNIgmpGDAConfigStatus_Object = MibTableColumn
mySNIgmpGDAConfigStatus = _MySNIgmpGDAConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 13, 1, 5),
    _MySNIgmpGDAConfigStatus_Type()
)
mySNIgmpGDAConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mySNIgmpGDAConfigStatus.setStatus("current")
_MySNIgmpQueryResponeTime_Type = Unsigned32
_MySNIgmpQueryResponeTime_Object = MibScalar
mySNIgmpQueryResponeTime = _MySNIgmpQueryResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 1, 14),
    _MySNIgmpQueryResponeTime_Type()
)
mySNIgmpQueryResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mySNIgmpQueryResponeTime.setStatus("current")
_MyIgmpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
myIgmpSnoopingMIBConformance = _MyIgmpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 2)
)
_MyIgmpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
myIgmpSnoopingMIBCompliances = _MyIgmpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 2, 1)
)
_MyIgmpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
myIgmpSnoopingMIBGroups = _MyIgmpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 2, 2)
)

# Managed Objects groups

myIgmpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 2, 2, 1)
)
myIgmpSnoopingMIBGroup.setObjects(
      *(("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpWorkingMode"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSourcePortCheck"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSourceIpCheck"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSourceIpCheckDefIp"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSrcIpCheckVID"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSrcIpCheckMultiIpAddr"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSrcIpCheckSrcIpAddr"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSrcIpCheckEntryStatus"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpPortRouterVID"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpPortIndex"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpPortRouterState"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpPortRouterProfile"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDANumber"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAVID"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAAddr"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAPortMemberAction"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDATrunkMemberAction"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSvglVID"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpSvglProfile"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpMrLearnVID"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpMrLearnStatus"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNPortIndex"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpFilteringProfile"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpFilteringMaxGroups"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAConfigVID"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAConfigAddr"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAConfigIfIndex"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAConfigType"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpGDAConfigStatus"),
        ("DES7200-IGMP-SNOOPING-MIB", "mySNIgmpQueryResponeTime"))
)
if mibBuilder.loadTexts:
    myIgmpSnoopingMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myIgmpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 10, 97, 2, 8, 2, 1, 1)
)
myIgmpSnoopingMIBCompliance.setObjects(
    ("DES7200-IGMP-SNOOPING-MIB", "myIgmpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    myIgmpSnoopingMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DES7200-IGMP-SNOOPING-MIB",
    **{"myIgmpSnoopingMIB": myIgmpSnoopingMIB,
       "myIgmpSnoopingMIBObjects": myIgmpSnoopingMIBObjects,
       "mySNIgmpWorkingMode": mySNIgmpWorkingMode,
       "mySNIgmpSourcePortCheck": mySNIgmpSourcePortCheck,
       "mySNIgmpSourceIpCheck": mySNIgmpSourceIpCheck,
       "mySNIgmpSourceIpCheckDefIp": mySNIgmpSourceIpCheckDefIp,
       "mySNIgmpSrcIpCheckTable": mySNIgmpSrcIpCheckTable,
       "mySNIgmpSrcIpCheckEntry": mySNIgmpSrcIpCheckEntry,
       "mySNIgmpSrcIpCheckVID": mySNIgmpSrcIpCheckVID,
       "mySNIgmpSrcIpCheckMultiIpAddr": mySNIgmpSrcIpCheckMultiIpAddr,
       "mySNIgmpSrcIpCheckSrcIpAddr": mySNIgmpSrcIpCheckSrcIpAddr,
       "mySNIgmpSrcIpCheckEntryStatus": mySNIgmpSrcIpCheckEntryStatus,
       "mySNIgmpPortTable": mySNIgmpPortTable,
       "mySNIgmpPortEntry": mySNIgmpPortEntry,
       "mySNIgmpPortRouterVID": mySNIgmpPortRouterVID,
       "mySNIgmpPortIndex": mySNIgmpPortIndex,
       "mySNIgmpPortRouterState": mySNIgmpPortRouterState,
       "mySNIgmpPortRouterProfile": mySNIgmpPortRouterProfile,
       "mySNIgmpGDANumber": mySNIgmpGDANumber,
       "mySNIgmpGDATable": mySNIgmpGDATable,
       "mySNIgmpGDAEntry": mySNIgmpGDAEntry,
       "mySNIgmpGDAVID": mySNIgmpGDAVID,
       "mySNIgmpGDAAddr": mySNIgmpGDAAddr,
       "mySNIgmpGDAPortMemberAction": mySNIgmpGDAPortMemberAction,
       "mySNIgmpGDATrunkMemberAction": mySNIgmpGDATrunkMemberAction,
       "mySNIgmpSvglVID": mySNIgmpSvglVID,
       "mySNIgmpSvglProfile": mySNIgmpSvglProfile,
       "mySNIgmpMrLearnTable": mySNIgmpMrLearnTable,
       "mySNIgmpMrLearnEntry": mySNIgmpMrLearnEntry,
       "mySNIgmpMrLearnVID": mySNIgmpMrLearnVID,
       "mySNIgmpMrLearnStatus": mySNIgmpMrLearnStatus,
       "mySNIgmpPortFilteringTable": mySNIgmpPortFilteringTable,
       "mySNIgmpPortFilteringEntry": mySNIgmpPortFilteringEntry,
       "mySNPortIndex": mySNPortIndex,
       "mySNIgmpFilteringProfile": mySNIgmpFilteringProfile,
       "mySNIgmpFilteringMaxGroups": mySNIgmpFilteringMaxGroups,
       "mySNIgmpGDAConfigTable": mySNIgmpGDAConfigTable,
       "mySNIgmpGDAConfigEntry": mySNIgmpGDAConfigEntry,
       "mySNIgmpGDAConfigVID": mySNIgmpGDAConfigVID,
       "mySNIgmpGDAConfigAddr": mySNIgmpGDAConfigAddr,
       "mySNIgmpGDAConfigIfIndex": mySNIgmpGDAConfigIfIndex,
       "mySNIgmpGDAConfigType": mySNIgmpGDAConfigType,
       "mySNIgmpGDAConfigStatus": mySNIgmpGDAConfigStatus,
       "mySNIgmpQueryResponeTime": mySNIgmpQueryResponeTime,
       "myIgmpSnoopingMIBConformance": myIgmpSnoopingMIBConformance,
       "myIgmpSnoopingMIBCompliances": myIgmpSnoopingMIBCompliances,
       "myIgmpSnoopingMIBCompliance": myIgmpSnoopingMIBCompliance,
       "myIgmpSnoopingMIBGroups": myIgmpSnoopingMIBGroups,
       "myIgmpSnoopingMIBGroup": myIgmpSnoopingMIBGroup}
)
