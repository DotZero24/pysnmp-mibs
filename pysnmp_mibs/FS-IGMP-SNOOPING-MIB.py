# SNMP MIB module (FS-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IGMP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:05 2025
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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8)
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingMIB.setRevisions(
        ("2009-10-22 00:00",
         "2002-03-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIgmpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
fsIgmpSnoopingMIBObjects = _FsIgmpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1)
)


class _FsSNIgmpWorkingMode_Type(Integer32):
    """Custom type fsSNIgmpWorkingMode based on Integer32"""
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


_FsSNIgmpWorkingMode_Type.__name__ = "Integer32"
_FsSNIgmpWorkingMode_Object = MibScalar
fsSNIgmpWorkingMode = _FsSNIgmpWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 1),
    _FsSNIgmpWorkingMode_Type()
)
fsSNIgmpWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpWorkingMode.setStatus("deprecated")


class _FsSNIgmpSourcePortCheck_Type(EnabledStatus):
    """Custom type fsSNIgmpSourcePortCheck based on EnabledStatus"""
    defaultValue = 2


_FsSNIgmpSourcePortCheck_Type.__name__ = "EnabledStatus"
_FsSNIgmpSourcePortCheck_Object = MibScalar
fsSNIgmpSourcePortCheck = _FsSNIgmpSourcePortCheck_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 2),
    _FsSNIgmpSourcePortCheck_Type()
)
fsSNIgmpSourcePortCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpSourcePortCheck.setStatus("deprecated")


class _FsSNIgmpSourceIpCheck_Type(EnabledStatus):
    """Custom type fsSNIgmpSourceIpCheck based on EnabledStatus"""
    defaultValue = 2


_FsSNIgmpSourceIpCheck_Type.__name__ = "EnabledStatus"
_FsSNIgmpSourceIpCheck_Object = MibScalar
fsSNIgmpSourceIpCheck = _FsSNIgmpSourceIpCheck_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 3),
    _FsSNIgmpSourceIpCheck_Type()
)
fsSNIgmpSourceIpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpSourceIpCheck.setStatus("deprecated")
_FsSNIgmpSourceIpCheckDefIp_Type = IpAddress
_FsSNIgmpSourceIpCheckDefIp_Object = MibScalar
fsSNIgmpSourceIpCheckDefIp = _FsSNIgmpSourceIpCheckDefIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 4),
    _FsSNIgmpSourceIpCheckDefIp_Type()
)
fsSNIgmpSourceIpCheckDefIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpSourceIpCheckDefIp.setStatus("deprecated")
_FsSNIgmpSrcIpCheckTable_Object = MibTable
fsSNIgmpSrcIpCheckTable = _FsSNIgmpSrcIpCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    fsSNIgmpSrcIpCheckTable.setStatus("deprecated")
_FsSNIgmpSrcIpCheckEntry_Object = MibTableRow
fsSNIgmpSrcIpCheckEntry = _FsSNIgmpSrcIpCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 5, 1)
)
fsSNIgmpSrcIpCheckEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpSrcIpCheckVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpSrcIpCheckMultiIpAddr"),
)
if mibBuilder.loadTexts:
    fsSNIgmpSrcIpCheckEntry.setStatus("deprecated")
_FsSNIgmpSrcIpCheckVID_Type = VlanId
_FsSNIgmpSrcIpCheckVID_Object = MibTableColumn
fsSNIgmpSrcIpCheckVID = _FsSNIgmpSrcIpCheckVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 5, 1, 1),
    _FsSNIgmpSrcIpCheckVID_Type()
)
fsSNIgmpSrcIpCheckVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpSrcIpCheckVID.setStatus("deprecated")
_FsSNIgmpSrcIpCheckMultiIpAddr_Type = IpAddress
_FsSNIgmpSrcIpCheckMultiIpAddr_Object = MibTableColumn
fsSNIgmpSrcIpCheckMultiIpAddr = _FsSNIgmpSrcIpCheckMultiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 5, 1, 2),
    _FsSNIgmpSrcIpCheckMultiIpAddr_Type()
)
fsSNIgmpSrcIpCheckMultiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpSrcIpCheckMultiIpAddr.setStatus("deprecated")
_FsSNIgmpSrcIpCheckSrcIpAddr_Type = IpAddress
_FsSNIgmpSrcIpCheckSrcIpAddr_Object = MibTableColumn
fsSNIgmpSrcIpCheckSrcIpAddr = _FsSNIgmpSrcIpCheckSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 5, 1, 3),
    _FsSNIgmpSrcIpCheckSrcIpAddr_Type()
)
fsSNIgmpSrcIpCheckSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSNIgmpSrcIpCheckSrcIpAddr.setStatus("deprecated")


class _FsSNIgmpSrcIpCheckEntryStatus_Type(Integer32):
    """Custom type fsSNIgmpSrcIpCheckEntryStatus based on Integer32"""
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


_FsSNIgmpSrcIpCheckEntryStatus_Type.__name__ = "Integer32"
_FsSNIgmpSrcIpCheckEntryStatus_Object = MibTableColumn
fsSNIgmpSrcIpCheckEntryStatus = _FsSNIgmpSrcIpCheckEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 5, 1, 4),
    _FsSNIgmpSrcIpCheckEntryStatus_Type()
)
fsSNIgmpSrcIpCheckEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSNIgmpSrcIpCheckEntryStatus.setStatus("deprecated")
_FsSNIgmpPortTable_Object = MibTable
fsSNIgmpPortTable = _FsSNIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    fsSNIgmpPortTable.setStatus("deprecated")
_FsSNIgmpPortEntry_Object = MibTableRow
fsSNIgmpPortEntry = _FsSNIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 6, 1)
)
fsSNIgmpPortEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpPortRouterVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpPortIndex"),
)
if mibBuilder.loadTexts:
    fsSNIgmpPortEntry.setStatus("deprecated")
_FsSNIgmpPortRouterVID_Type = VlanId
_FsSNIgmpPortRouterVID_Object = MibTableColumn
fsSNIgmpPortRouterVID = _FsSNIgmpPortRouterVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 6, 1, 1),
    _FsSNIgmpPortRouterVID_Type()
)
fsSNIgmpPortRouterVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpPortRouterVID.setStatus("deprecated")
_FsSNIgmpPortIndex_Type = IfIndex
_FsSNIgmpPortIndex_Object = MibTableColumn
fsSNIgmpPortIndex = _FsSNIgmpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 6, 1, 2),
    _FsSNIgmpPortIndex_Type()
)
fsSNIgmpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpPortIndex.setStatus("deprecated")


class _FsSNIgmpPortRouterState_Type(Integer32):
    """Custom type fsSNIgmpPortRouterState based on Integer32"""
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


_FsSNIgmpPortRouterState_Type.__name__ = "Integer32"
_FsSNIgmpPortRouterState_Object = MibTableColumn
fsSNIgmpPortRouterState = _FsSNIgmpPortRouterState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 6, 1, 3),
    _FsSNIgmpPortRouterState_Type()
)
fsSNIgmpPortRouterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpPortRouterState.setStatus("deprecated")
_FsSNIgmpPortRouterProfile_Type = Unsigned32
_FsSNIgmpPortRouterProfile_Object = MibTableColumn
fsSNIgmpPortRouterProfile = _FsSNIgmpPortRouterProfile_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 6, 1, 4),
    _FsSNIgmpPortRouterProfile_Type()
)
fsSNIgmpPortRouterProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpPortRouterProfile.setStatus("deprecated")
_FsSNIgmpGDANumber_Type = Unsigned32
_FsSNIgmpGDANumber_Object = MibScalar
fsSNIgmpGDANumber = _FsSNIgmpGDANumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 7),
    _FsSNIgmpGDANumber_Type()
)
fsSNIgmpGDANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDANumber.setStatus("deprecated")
_FsSNIgmpGDATable_Object = MibTable
fsSNIgmpGDATable = _FsSNIgmpGDATable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    fsSNIgmpGDATable.setStatus("deprecated")
_FsSNIgmpGDAEntry_Object = MibTableRow
fsSNIgmpGDAEntry = _FsSNIgmpGDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 8, 1)
)
fsSNIgmpGDAEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAAddr"),
)
if mibBuilder.loadTexts:
    fsSNIgmpGDAEntry.setStatus("deprecated")
_FsSNIgmpGDAVID_Type = VlanId
_FsSNIgmpGDAVID_Object = MibTableColumn
fsSNIgmpGDAVID = _FsSNIgmpGDAVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 8, 1, 1),
    _FsSNIgmpGDAVID_Type()
)
fsSNIgmpGDAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDAVID.setStatus("deprecated")
_FsSNIgmpGDAAddr_Type = IpAddress
_FsSNIgmpGDAAddr_Object = MibTableColumn
fsSNIgmpGDAAddr = _FsSNIgmpGDAAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 8, 1, 2),
    _FsSNIgmpGDAAddr_Type()
)
fsSNIgmpGDAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDAAddr.setStatus("deprecated")
_FsSNIgmpGDAPortMemberAction_Type = MemberMap
_FsSNIgmpGDAPortMemberAction_Object = MibTableColumn
fsSNIgmpGDAPortMemberAction = _FsSNIgmpGDAPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 8, 1, 3),
    _FsSNIgmpGDAPortMemberAction_Type()
)
fsSNIgmpGDAPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpGDAPortMemberAction.setStatus("deprecated")
_FsSNIgmpGDATrunkMemberAction_Type = MemberMap
_FsSNIgmpGDATrunkMemberAction_Object = MibTableColumn
fsSNIgmpGDATrunkMemberAction = _FsSNIgmpGDATrunkMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 8, 1, 4),
    _FsSNIgmpGDATrunkMemberAction_Type()
)
fsSNIgmpGDATrunkMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpGDATrunkMemberAction.setStatus("deprecated")
_FsSNIgmpSvglVID_Type = Integer32
_FsSNIgmpSvglVID_Object = MibScalar
fsSNIgmpSvglVID = _FsSNIgmpSvglVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 9),
    _FsSNIgmpSvglVID_Type()
)
fsSNIgmpSvglVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpSvglVID.setStatus("deprecated")
_FsSNIgmpSvglProfile_Type = Unsigned32
_FsSNIgmpSvglProfile_Object = MibScalar
fsSNIgmpSvglProfile = _FsSNIgmpSvglProfile_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 10),
    _FsSNIgmpSvglProfile_Type()
)
fsSNIgmpSvglProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpSvglProfile.setStatus("deprecated")
_FsSNIgmpMrLearnTable_Object = MibTable
fsSNIgmpMrLearnTable = _FsSNIgmpMrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 11)
)
if mibBuilder.loadTexts:
    fsSNIgmpMrLearnTable.setStatus("deprecated")
_FsSNIgmpMrLearnEntry_Object = MibTableRow
fsSNIgmpMrLearnEntry = _FsSNIgmpMrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 11, 1)
)
fsSNIgmpMrLearnEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpMrLearnVID"),
)
if mibBuilder.loadTexts:
    fsSNIgmpMrLearnEntry.setStatus("deprecated")
_FsSNIgmpMrLearnVID_Type = VlanId
_FsSNIgmpMrLearnVID_Object = MibTableColumn
fsSNIgmpMrLearnVID = _FsSNIgmpMrLearnVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 11, 1, 1),
    _FsSNIgmpMrLearnVID_Type()
)
fsSNIgmpMrLearnVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpMrLearnVID.setStatus("deprecated")


class _FsSNIgmpMrLearnStatus_Type(Integer32):
    """Custom type fsSNIgmpMrLearnStatus based on Integer32"""
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


_FsSNIgmpMrLearnStatus_Type.__name__ = "Integer32"
_FsSNIgmpMrLearnStatus_Object = MibTableColumn
fsSNIgmpMrLearnStatus = _FsSNIgmpMrLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 11, 1, 2),
    _FsSNIgmpMrLearnStatus_Type()
)
fsSNIgmpMrLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpMrLearnStatus.setStatus("deprecated")
_FsSNIgmpPortFilteringTable_Object = MibTable
fsSNIgmpPortFilteringTable = _FsSNIgmpPortFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 12)
)
if mibBuilder.loadTexts:
    fsSNIgmpPortFilteringTable.setStatus("deprecated")
_FsSNIgmpPortFilteringEntry_Object = MibTableRow
fsSNIgmpPortFilteringEntry = _FsSNIgmpPortFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 12, 1)
)
fsSNIgmpPortFilteringEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNPortIndex"),
)
if mibBuilder.loadTexts:
    fsSNIgmpPortFilteringEntry.setStatus("deprecated")
_FsSNPortIndex_Type = IfIndex
_FsSNPortIndex_Object = MibTableColumn
fsSNPortIndex = _FsSNPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 12, 1, 1),
    _FsSNPortIndex_Type()
)
fsSNPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNPortIndex.setStatus("deprecated")
_FsSNIgmpFilteringProfile_Type = Unsigned32
_FsSNIgmpFilteringProfile_Object = MibTableColumn
fsSNIgmpFilteringProfile = _FsSNIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 12, 1, 2),
    _FsSNIgmpFilteringProfile_Type()
)
fsSNIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpFilteringProfile.setStatus("deprecated")
_FsSNIgmpFilteringMaxGroups_Type = Unsigned32
_FsSNIgmpFilteringMaxGroups_Object = MibTableColumn
fsSNIgmpFilteringMaxGroups = _FsSNIgmpFilteringMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 12, 1, 3),
    _FsSNIgmpFilteringMaxGroups_Type()
)
fsSNIgmpFilteringMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpFilteringMaxGroups.setStatus("deprecated")
_FsSNIgmpGDAConfigTable_Object = MibTable
fsSNIgmpGDAConfigTable = _FsSNIgmpGDAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 13)
)
if mibBuilder.loadTexts:
    fsSNIgmpGDAConfigTable.setStatus("deprecated")
_FsSNIgmpGDAConfigEntry_Object = MibTableRow
fsSNIgmpGDAConfigEntry = _FsSNIgmpGDAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 13, 1)
)
fsSNIgmpGDAConfigEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAConfigVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAConfigAddr"),
)
if mibBuilder.loadTexts:
    fsSNIgmpGDAConfigEntry.setStatus("deprecated")
_FsSNIgmpGDAConfigVID_Type = VlanId
_FsSNIgmpGDAConfigVID_Object = MibTableColumn
fsSNIgmpGDAConfigVID = _FsSNIgmpGDAConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 13, 1, 1),
    _FsSNIgmpGDAConfigVID_Type()
)
fsSNIgmpGDAConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDAConfigVID.setStatus("deprecated")
_FsSNIgmpGDAConfigAddr_Type = IpAddress
_FsSNIgmpGDAConfigAddr_Object = MibTableColumn
fsSNIgmpGDAConfigAddr = _FsSNIgmpGDAConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 13, 1, 2),
    _FsSNIgmpGDAConfigAddr_Type()
)
fsSNIgmpGDAConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDAConfigAddr.setStatus("deprecated")
_FsSNIgmpGDAConfigIfIndex_Type = IfIndex
_FsSNIgmpGDAConfigIfIndex_Object = MibTableColumn
fsSNIgmpGDAConfigIfIndex = _FsSNIgmpGDAConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 13, 1, 3),
    _FsSNIgmpGDAConfigIfIndex_Type()
)
fsSNIgmpGDAConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDAConfigIfIndex.setStatus("deprecated")


class _FsSNIgmpGDAConfigType_Type(Integer32):
    """Custom type fsSNIgmpGDAConfigType based on Integer32"""
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


_FsSNIgmpGDAConfigType_Type.__name__ = "Integer32"
_FsSNIgmpGDAConfigType_Object = MibTableColumn
fsSNIgmpGDAConfigType = _FsSNIgmpGDAConfigType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 13, 1, 4),
    _FsSNIgmpGDAConfigType_Type()
)
fsSNIgmpGDAConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDAConfigType.setStatus("deprecated")


class _FsSNIgmpGDAConfigStatus_Type(Integer32):
    """Custom type fsSNIgmpGDAConfigStatus based on Integer32"""
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


_FsSNIgmpGDAConfigStatus_Type.__name__ = "Integer32"
_FsSNIgmpGDAConfigStatus_Object = MibTableColumn
fsSNIgmpGDAConfigStatus = _FsSNIgmpGDAConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 13, 1, 5),
    _FsSNIgmpGDAConfigStatus_Type()
)
fsSNIgmpGDAConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNIgmpGDAConfigStatus.setStatus("deprecated")
_FsSNIgmpQueryResponeTime_Type = Unsigned32
_FsSNIgmpQueryResponeTime_Object = MibScalar
fsSNIgmpQueryResponeTime = _FsSNIgmpQueryResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 14),
    _FsSNIgmpQueryResponeTime_Type()
)
fsSNIgmpQueryResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSNIgmpQueryResponeTime.setStatus("deprecated")


class _FsIgmpSnoopingWorkingMode_Type(Integer32):
    """Custom type fsIgmpSnoopingWorkingMode based on Integer32"""
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


_FsIgmpSnoopingWorkingMode_Type.__name__ = "Integer32"
_FsIgmpSnoopingWorkingMode_Object = MibScalar
fsIgmpSnoopingWorkingMode = _FsIgmpSnoopingWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 15),
    _FsIgmpSnoopingWorkingMode_Type()
)
fsIgmpSnoopingWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingWorkingMode.setStatus("current")
_FsIgmpSnoopingGDANumber_Type = Unsigned32
_FsIgmpSnoopingGDANumber_Object = MibScalar
fsIgmpSnoopingGDANumber = _FsIgmpSnoopingGDANumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 16),
    _FsIgmpSnoopingGDANumber_Type()
)
fsIgmpSnoopingGDANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDANumber.setStatus("current")
_FsIgmpSnoopingGDATable_Object = MibTable
fsIgmpSnoopingGDATable = _FsIgmpSnoopingGDATable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 17)
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDATable.setStatus("current")
_FsIgmpSnoopingGDAEntry_Object = MibTableRow
fsIgmpSnoopingGDAEntry = _FsIgmpSnoopingGDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 17, 1)
)
fsIgmpSnoopingGDAEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAAddr"),
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAEntry.setStatus("current")
_FsIgmpSnoopingGDAVID_Type = VlanId
_FsIgmpSnoopingGDAVID_Object = MibTableColumn
fsIgmpSnoopingGDAVID = _FsIgmpSnoopingGDAVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 17, 1, 1),
    _FsIgmpSnoopingGDAVID_Type()
)
fsIgmpSnoopingGDAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAVID.setStatus("current")
_FsIgmpSnoopingGDAAddr_Type = IpAddress
_FsIgmpSnoopingGDAAddr_Object = MibTableColumn
fsIgmpSnoopingGDAAddr = _FsIgmpSnoopingGDAAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 17, 1, 2),
    _FsIgmpSnoopingGDAAddr_Type()
)
fsIgmpSnoopingGDAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAAddr.setStatus("current")
_FsIgmpSnoopingGDAPortMemberAction_Type = MemberMap
_FsIgmpSnoopingGDAPortMemberAction_Object = MibTableColumn
fsIgmpSnoopingGDAPortMemberAction = _FsIgmpSnoopingGDAPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 17, 1, 3),
    _FsIgmpSnoopingGDAPortMemberAction_Type()
)
fsIgmpSnoopingGDAPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAPortMemberAction.setStatus("current")
_FsIgmpSnoopingVlanStatusTable_Object = MibTable
fsIgmpSnoopingVlanStatusTable = _FsIgmpSnoopingVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 18)
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingVlanStatusTable.setStatus("current")
_FsIgmpSnoopingVlanStatusEntry_Object = MibTableRow
fsIgmpSnoopingVlanStatusEntry = _FsIgmpSnoopingVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 18, 1)
)
fsIgmpSnoopingVlanStatusEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingVlanStatusVID"),
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingVlanStatusEntry.setStatus("current")
_FsIgmpSnoopingVlanStatusVID_Type = VlanId
_FsIgmpSnoopingVlanStatusVID_Object = MibTableColumn
fsIgmpSnoopingVlanStatusVID = _FsIgmpSnoopingVlanStatusVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 18, 1, 1),
    _FsIgmpSnoopingVlanStatusVID_Type()
)
fsIgmpSnoopingVlanStatusVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingVlanStatusVID.setStatus("current")
_FsIgmpSnoopingVlanStatusStatus_Type = EnabledStatus
_FsIgmpSnoopingVlanStatusStatus_Object = MibTableColumn
fsIgmpSnoopingVlanStatusStatus = _FsIgmpSnoopingVlanStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 18, 1, 2),
    _FsIgmpSnoopingVlanStatusStatus_Type()
)
fsIgmpSnoopingVlanStatusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingVlanStatusStatus.setStatus("current")
_FsIgmpSnoopingSvglVID_Type = Integer32
_FsIgmpSnoopingSvglVID_Object = MibScalar
fsIgmpSnoopingSvglVID = _FsIgmpSnoopingSvglVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 19),
    _FsIgmpSnoopingSvglVID_Type()
)
fsIgmpSnoopingSvglVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingSvglVID.setStatus("current")
_FsIgmpSnoopingSvglProfile_Type = Unsigned32
_FsIgmpSnoopingSvglProfile_Object = MibScalar
fsIgmpSnoopingSvglProfile = _FsIgmpSnoopingSvglProfile_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 20),
    _FsIgmpSnoopingSvglProfile_Type()
)
fsIgmpSnoopingSvglProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingSvglProfile.setStatus("current")
_FsIgmpSnoopingMrLearnTable_Object = MibTable
fsIgmpSnoopingMrLearnTable = _FsIgmpSnoopingMrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 21)
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingMrLearnTable.setStatus("current")
_FsIgmpSnoopingMrLearnEntry_Object = MibTableRow
fsIgmpSnoopingMrLearnEntry = _FsIgmpSnoopingMrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 21, 1)
)
fsIgmpSnoopingMrLearnEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingMrLearnVID"),
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingMrLearnEntry.setStatus("current")
_FsIgmpSnoopingMrLearnVID_Type = VlanId
_FsIgmpSnoopingMrLearnVID_Object = MibTableColumn
fsIgmpSnoopingMrLearnVID = _FsIgmpSnoopingMrLearnVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 21, 1, 1),
    _FsIgmpSnoopingMrLearnVID_Type()
)
fsIgmpSnoopingMrLearnVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingMrLearnVID.setStatus("current")


class _FsIgmpSnoopingMrLearnStatus_Type(Integer32):
    """Custom type fsIgmpSnoopingMrLearnStatus based on Integer32"""
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


_FsIgmpSnoopingMrLearnStatus_Type.__name__ = "Integer32"
_FsIgmpSnoopingMrLearnStatus_Object = MibTableColumn
fsIgmpSnoopingMrLearnStatus = _FsIgmpSnoopingMrLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 21, 1, 2),
    _FsIgmpSnoopingMrLearnStatus_Type()
)
fsIgmpSnoopingMrLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingMrLearnStatus.setStatus("current")
_FsIgmpSnoopingPortFilteringTable_Object = MibTable
fsIgmpSnoopingPortFilteringTable = _FsIgmpSnoopingPortFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 22)
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingPortFilteringTable.setStatus("current")
_FsIgmpSnoopingPortFilteringEntry_Object = MibTableRow
fsIgmpSnoopingPortFilteringEntry = _FsIgmpSnoopingPortFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 22, 1)
)
fsIgmpSnoopingPortFilteringEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingportIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingPortFilteringEntry.setStatus("current")
_FsIgmpSnoopingportIndex_Type = IfIndex
_FsIgmpSnoopingportIndex_Object = MibTableColumn
fsIgmpSnoopingportIndex = _FsIgmpSnoopingportIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 22, 1, 1),
    _FsIgmpSnoopingportIndex_Type()
)
fsIgmpSnoopingportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingportIndex.setStatus("current")
_FsIgmpSnoopingFilteringProfile_Type = Unsigned32
_FsIgmpSnoopingFilteringProfile_Object = MibTableColumn
fsIgmpSnoopingFilteringProfile = _FsIgmpSnoopingFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 22, 1, 2),
    _FsIgmpSnoopingFilteringProfile_Type()
)
fsIgmpSnoopingFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingFilteringProfile.setStatus("current")
_FsIgmpSnoopingFilteringMaxGroups_Type = Unsigned32
_FsIgmpSnoopingFilteringMaxGroups_Object = MibTableColumn
fsIgmpSnoopingFilteringMaxGroups = _FsIgmpSnoopingFilteringMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 22, 1, 3),
    _FsIgmpSnoopingFilteringMaxGroups_Type()
)
fsIgmpSnoopingFilteringMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingFilteringMaxGroups.setStatus("current")
_FsIgmpSnoopingGDAConfigTable_Object = MibTable
fsIgmpSnoopingGDAConfigTable = _FsIgmpSnoopingGDAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 23)
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAConfigTable.setStatus("current")
_FsIgmpSnoopingGDAConfigEntry_Object = MibTableRow
fsIgmpSnoopingGDAConfigEntry = _FsIgmpSnoopingGDAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 23, 1)
)
fsIgmpSnoopingGDAConfigEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAConfigVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAConfigAddr"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAConfigIfIndex"),
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAConfigEntry.setStatus("current")
_FsIgmpSnoopingGDAConfigVID_Type = VlanId
_FsIgmpSnoopingGDAConfigVID_Object = MibTableColumn
fsIgmpSnoopingGDAConfigVID = _FsIgmpSnoopingGDAConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 23, 1, 1),
    _FsIgmpSnoopingGDAConfigVID_Type()
)
fsIgmpSnoopingGDAConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAConfigVID.setStatus("current")
_FsIgmpSnoopingGDAConfigAddr_Type = IpAddress
_FsIgmpSnoopingGDAConfigAddr_Object = MibTableColumn
fsIgmpSnoopingGDAConfigAddr = _FsIgmpSnoopingGDAConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 23, 1, 2),
    _FsIgmpSnoopingGDAConfigAddr_Type()
)
fsIgmpSnoopingGDAConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAConfigAddr.setStatus("current")
_FsIgmpSnoopingGDAConfigIfIndex_Type = IfIndex
_FsIgmpSnoopingGDAConfigIfIndex_Object = MibTableColumn
fsIgmpSnoopingGDAConfigIfIndex = _FsIgmpSnoopingGDAConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 23, 1, 3),
    _FsIgmpSnoopingGDAConfigIfIndex_Type()
)
fsIgmpSnoopingGDAConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAConfigIfIndex.setStatus("current")
_FsIgmpSnoopingQueryResponeTime_Type = Unsigned32
_FsIgmpSnoopingQueryResponeTime_Object = MibScalar
fsIgmpSnoopingQueryResponeTime = _FsIgmpSnoopingQueryResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 24),
    _FsIgmpSnoopingQueryResponeTime_Type()
)
fsIgmpSnoopingQueryResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingQueryResponeTime.setStatus("current")
_FsIgmpSnoopingReportSuppress_Type = TruthValue
_FsIgmpSnoopingReportSuppress_Object = MibScalar
fsIgmpSnoopingReportSuppress = _FsIgmpSnoopingReportSuppress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 25),
    _FsIgmpSnoopingReportSuppress_Type()
)
fsIgmpSnoopingReportSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingReportSuppress.setStatus("current")
_FsIgmpSnoopingFastleave_Type = TruthValue
_FsIgmpSnoopingFastleave_Object = MibScalar
fsIgmpSnoopingFastleave = _FsIgmpSnoopingFastleave_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 26),
    _FsIgmpSnoopingFastleave_Type()
)
fsIgmpSnoopingFastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingFastleave.setStatus("current")
_FsIgmpSnoopingGDANewTable_Object = MibTable
fsIgmpSnoopingGDANewTable = _FsIgmpSnoopingGDANewTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27)
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDANewTable.setStatus("current")
_FsIgmpSnoopingGDANewEntry_Object = MibTableRow
fsIgmpSnoopingGDANewEntry = _FsIgmpSnoopingGDANewEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27, 1)
)
fsIgmpSnoopingGDANewEntry.setIndexNames(
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDANewInVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDANewOutVID"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgsmpSnoopingGDASrc"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAGrp"),
    (0, "FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAIfx"),
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDANewEntry.setStatus("current")
_FsIgmpSnoopingGDANewInVID_Type = VlanId
_FsIgmpSnoopingGDANewInVID_Object = MibTableColumn
fsIgmpSnoopingGDANewInVID = _FsIgmpSnoopingGDANewInVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27, 1, 1),
    _FsIgmpSnoopingGDANewInVID_Type()
)
fsIgmpSnoopingGDANewInVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDANewInVID.setStatus("current")
_FsIgmpSnoopingGDANewOutVID_Type = VlanId
_FsIgmpSnoopingGDANewOutVID_Object = MibTableColumn
fsIgmpSnoopingGDANewOutVID = _FsIgmpSnoopingGDANewOutVID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27, 1, 2),
    _FsIgmpSnoopingGDANewOutVID_Type()
)
fsIgmpSnoopingGDANewOutVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDANewOutVID.setStatus("current")
_FsIgsmpSnoopingGDASrc_Type = IpAddress
_FsIgsmpSnoopingGDASrc_Object = MibTableColumn
fsIgsmpSnoopingGDASrc = _FsIgsmpSnoopingGDASrc_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27, 1, 3),
    _FsIgsmpSnoopingGDASrc_Type()
)
fsIgsmpSnoopingGDASrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgsmpSnoopingGDASrc.setStatus("current")
_FsIgmpSnoopingGDAGrp_Type = IpAddress
_FsIgmpSnoopingGDAGrp_Object = MibTableColumn
fsIgmpSnoopingGDAGrp = _FsIgmpSnoopingGDAGrp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27, 1, 4),
    _FsIgmpSnoopingGDAGrp_Type()
)
fsIgmpSnoopingGDAGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAGrp.setStatus("current")
_FsIgmpSnoopingGDAIfx_Type = IfIndex
_FsIgmpSnoopingGDAIfx_Object = MibTableColumn
fsIgmpSnoopingGDAIfx = _FsIgmpSnoopingGDAIfx_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27, 1, 5),
    _FsIgmpSnoopingGDAIfx_Type()
)
fsIgmpSnoopingGDAIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAIfx.setStatus("current")
_FsIgmpSnoopingGDAIfxAction_Type = Integer32
_FsIgmpSnoopingGDAIfxAction_Object = MibTableColumn
fsIgmpSnoopingGDAIfxAction = _FsIgmpSnoopingGDAIfxAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 27, 1, 6),
    _FsIgmpSnoopingGDAIfxAction_Type()
)
fsIgmpSnoopingGDAIfxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingGDAIfxAction.setStatus("current")


class _FsIgmpSnoopingMulticastWlan_Type(Integer32):
    """Custom type fsIgmpSnoopingMulticastWlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enable", 1))
    )


_FsIgmpSnoopingMulticastWlan_Type.__name__ = "Integer32"
_FsIgmpSnoopingMulticastWlan_Object = MibScalar
fsIgmpSnoopingMulticastWlan = _FsIgmpSnoopingMulticastWlan_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 1, 28),
    _FsIgmpSnoopingMulticastWlan_Type()
)
fsIgmpSnoopingMulticastWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIgmpSnoopingMulticastWlan.setStatus("current")
_FsIgmpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
fsIgmpSnoopingMIBConformance = _FsIgmpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 2)
)
_FsIgmpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
fsIgmpSnoopingMIBCompliances = _FsIgmpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 2, 1)
)
_FsIgmpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
fsIgmpSnoopingMIBGroups = _FsIgmpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 2, 2)
)

# Managed Objects groups

fsIgmpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 2, 2, 1)
)
fsIgmpSnoopingMIBGroup.setObjects(
      *(("FS-IGMP-SNOOPING-MIB", "fsSNIgmpWorkingMode"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSourcePortCheck"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSourceIpCheck"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSourceIpCheckDefIp"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSrcIpCheckVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSrcIpCheckMultiIpAddr"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSrcIpCheckSrcIpAddr"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSrcIpCheckEntryStatus"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpPortRouterVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpPortIndex"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpPortRouterState"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpPortRouterProfile"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDANumber"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAAddr"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAPortMemberAction"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDATrunkMemberAction"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSvglVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpSvglProfile"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpMrLearnVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpMrLearnStatus"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNPortIndex"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpFilteringProfile"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpFilteringMaxGroups"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAConfigVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAConfigAddr"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAConfigIfIndex"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAConfigType"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpGDAConfigStatus"),
        ("FS-IGMP-SNOOPING-MIB", "fsSNIgmpQueryResponeTime"))
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingMIBGroup.setStatus("deprecated")

fsIgmpSnoopingMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 2, 2, 2)
)
fsIgmpSnoopingMIBGroup2.setObjects(
      *(("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingWorkingMode"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDANumber"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAAddr"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAPortMemberAction"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingVlanStatusVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingVlanStatusStatus"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingSvglVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingSvglProfile"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingMrLearnVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingMrLearnStatus"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingportIndex"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingFilteringProfile"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingFilteringMaxGroups"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAConfigVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAConfigAddr"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAConfigIfIndex"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingQueryResponeTime"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingReportSuppress"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingFastleave"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDANewInVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDANewOutVID"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgsmpSnoopingGDASrc"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAGrp"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAIfx"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingGDAIfxAction"),
        ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingMulticastWlan"))
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingMIBGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsIgmpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 2, 1, 1)
)
fsIgmpSnoopingMIBCompliance.setObjects(
    ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingMIBCompliance.setStatus(
        "deprecated"
    )

fsIgmpSnoopingMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 8, 2, 1, 2)
)
fsIgmpSnoopingMIBCompliance2.setObjects(
    ("FS-IGMP-SNOOPING-MIB", "fsIgmpSnoopingMIBGroup2")
)
if mibBuilder.loadTexts:
    fsIgmpSnoopingMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IGMP-SNOOPING-MIB",
    **{"fsIgmpSnoopingMIB": fsIgmpSnoopingMIB,
       "fsIgmpSnoopingMIBObjects": fsIgmpSnoopingMIBObjects,
       "fsSNIgmpWorkingMode": fsSNIgmpWorkingMode,
       "fsSNIgmpSourcePortCheck": fsSNIgmpSourcePortCheck,
       "fsSNIgmpSourceIpCheck": fsSNIgmpSourceIpCheck,
       "fsSNIgmpSourceIpCheckDefIp": fsSNIgmpSourceIpCheckDefIp,
       "fsSNIgmpSrcIpCheckTable": fsSNIgmpSrcIpCheckTable,
       "fsSNIgmpSrcIpCheckEntry": fsSNIgmpSrcIpCheckEntry,
       "fsSNIgmpSrcIpCheckVID": fsSNIgmpSrcIpCheckVID,
       "fsSNIgmpSrcIpCheckMultiIpAddr": fsSNIgmpSrcIpCheckMultiIpAddr,
       "fsSNIgmpSrcIpCheckSrcIpAddr": fsSNIgmpSrcIpCheckSrcIpAddr,
       "fsSNIgmpSrcIpCheckEntryStatus": fsSNIgmpSrcIpCheckEntryStatus,
       "fsSNIgmpPortTable": fsSNIgmpPortTable,
       "fsSNIgmpPortEntry": fsSNIgmpPortEntry,
       "fsSNIgmpPortRouterVID": fsSNIgmpPortRouterVID,
       "fsSNIgmpPortIndex": fsSNIgmpPortIndex,
       "fsSNIgmpPortRouterState": fsSNIgmpPortRouterState,
       "fsSNIgmpPortRouterProfile": fsSNIgmpPortRouterProfile,
       "fsSNIgmpGDANumber": fsSNIgmpGDANumber,
       "fsSNIgmpGDATable": fsSNIgmpGDATable,
       "fsSNIgmpGDAEntry": fsSNIgmpGDAEntry,
       "fsSNIgmpGDAVID": fsSNIgmpGDAVID,
       "fsSNIgmpGDAAddr": fsSNIgmpGDAAddr,
       "fsSNIgmpGDAPortMemberAction": fsSNIgmpGDAPortMemberAction,
       "fsSNIgmpGDATrunkMemberAction": fsSNIgmpGDATrunkMemberAction,
       "fsSNIgmpSvglVID": fsSNIgmpSvglVID,
       "fsSNIgmpSvglProfile": fsSNIgmpSvglProfile,
       "fsSNIgmpMrLearnTable": fsSNIgmpMrLearnTable,
       "fsSNIgmpMrLearnEntry": fsSNIgmpMrLearnEntry,
       "fsSNIgmpMrLearnVID": fsSNIgmpMrLearnVID,
       "fsSNIgmpMrLearnStatus": fsSNIgmpMrLearnStatus,
       "fsSNIgmpPortFilteringTable": fsSNIgmpPortFilteringTable,
       "fsSNIgmpPortFilteringEntry": fsSNIgmpPortFilteringEntry,
       "fsSNPortIndex": fsSNPortIndex,
       "fsSNIgmpFilteringProfile": fsSNIgmpFilteringProfile,
       "fsSNIgmpFilteringMaxGroups": fsSNIgmpFilteringMaxGroups,
       "fsSNIgmpGDAConfigTable": fsSNIgmpGDAConfigTable,
       "fsSNIgmpGDAConfigEntry": fsSNIgmpGDAConfigEntry,
       "fsSNIgmpGDAConfigVID": fsSNIgmpGDAConfigVID,
       "fsSNIgmpGDAConfigAddr": fsSNIgmpGDAConfigAddr,
       "fsSNIgmpGDAConfigIfIndex": fsSNIgmpGDAConfigIfIndex,
       "fsSNIgmpGDAConfigType": fsSNIgmpGDAConfigType,
       "fsSNIgmpGDAConfigStatus": fsSNIgmpGDAConfigStatus,
       "fsSNIgmpQueryResponeTime": fsSNIgmpQueryResponeTime,
       "fsIgmpSnoopingWorkingMode": fsIgmpSnoopingWorkingMode,
       "fsIgmpSnoopingGDANumber": fsIgmpSnoopingGDANumber,
       "fsIgmpSnoopingGDATable": fsIgmpSnoopingGDATable,
       "fsIgmpSnoopingGDAEntry": fsIgmpSnoopingGDAEntry,
       "fsIgmpSnoopingGDAVID": fsIgmpSnoopingGDAVID,
       "fsIgmpSnoopingGDAAddr": fsIgmpSnoopingGDAAddr,
       "fsIgmpSnoopingGDAPortMemberAction": fsIgmpSnoopingGDAPortMemberAction,
       "fsIgmpSnoopingVlanStatusTable": fsIgmpSnoopingVlanStatusTable,
       "fsIgmpSnoopingVlanStatusEntry": fsIgmpSnoopingVlanStatusEntry,
       "fsIgmpSnoopingVlanStatusVID": fsIgmpSnoopingVlanStatusVID,
       "fsIgmpSnoopingVlanStatusStatus": fsIgmpSnoopingVlanStatusStatus,
       "fsIgmpSnoopingSvglVID": fsIgmpSnoopingSvglVID,
       "fsIgmpSnoopingSvglProfile": fsIgmpSnoopingSvglProfile,
       "fsIgmpSnoopingMrLearnTable": fsIgmpSnoopingMrLearnTable,
       "fsIgmpSnoopingMrLearnEntry": fsIgmpSnoopingMrLearnEntry,
       "fsIgmpSnoopingMrLearnVID": fsIgmpSnoopingMrLearnVID,
       "fsIgmpSnoopingMrLearnStatus": fsIgmpSnoopingMrLearnStatus,
       "fsIgmpSnoopingPortFilteringTable": fsIgmpSnoopingPortFilteringTable,
       "fsIgmpSnoopingPortFilteringEntry": fsIgmpSnoopingPortFilteringEntry,
       "fsIgmpSnoopingportIndex": fsIgmpSnoopingportIndex,
       "fsIgmpSnoopingFilteringProfile": fsIgmpSnoopingFilteringProfile,
       "fsIgmpSnoopingFilteringMaxGroups": fsIgmpSnoopingFilteringMaxGroups,
       "fsIgmpSnoopingGDAConfigTable": fsIgmpSnoopingGDAConfigTable,
       "fsIgmpSnoopingGDAConfigEntry": fsIgmpSnoopingGDAConfigEntry,
       "fsIgmpSnoopingGDAConfigVID": fsIgmpSnoopingGDAConfigVID,
       "fsIgmpSnoopingGDAConfigAddr": fsIgmpSnoopingGDAConfigAddr,
       "fsIgmpSnoopingGDAConfigIfIndex": fsIgmpSnoopingGDAConfigIfIndex,
       "fsIgmpSnoopingQueryResponeTime": fsIgmpSnoopingQueryResponeTime,
       "fsIgmpSnoopingReportSuppress": fsIgmpSnoopingReportSuppress,
       "fsIgmpSnoopingFastleave": fsIgmpSnoopingFastleave,
       "fsIgmpSnoopingGDANewTable": fsIgmpSnoopingGDANewTable,
       "fsIgmpSnoopingGDANewEntry": fsIgmpSnoopingGDANewEntry,
       "fsIgmpSnoopingGDANewInVID": fsIgmpSnoopingGDANewInVID,
       "fsIgmpSnoopingGDANewOutVID": fsIgmpSnoopingGDANewOutVID,
       "fsIgsmpSnoopingGDASrc": fsIgsmpSnoopingGDASrc,
       "fsIgmpSnoopingGDAGrp": fsIgmpSnoopingGDAGrp,
       "fsIgmpSnoopingGDAIfx": fsIgmpSnoopingGDAIfx,
       "fsIgmpSnoopingGDAIfxAction": fsIgmpSnoopingGDAIfxAction,
       "fsIgmpSnoopingMulticastWlan": fsIgmpSnoopingMulticastWlan,
       "fsIgmpSnoopingMIBConformance": fsIgmpSnoopingMIBConformance,
       "fsIgmpSnoopingMIBCompliances": fsIgmpSnoopingMIBCompliances,
       "fsIgmpSnoopingMIBCompliance": fsIgmpSnoopingMIBCompliance,
       "fsIgmpSnoopingMIBCompliance2": fsIgmpSnoopingMIBCompliance2,
       "fsIgmpSnoopingMIBGroups": fsIgmpSnoopingMIBGroups,
       "fsIgmpSnoopingMIBGroup": fsIgmpSnoopingMIBGroup,
       "fsIgmpSnoopingMIBGroup2": fsIgmpSnoopingMIBGroup2}
)
