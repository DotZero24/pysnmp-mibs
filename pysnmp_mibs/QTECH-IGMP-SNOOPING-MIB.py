# SNMP MIB module (QTECH-IGMP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IGMP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:59 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

qtechIgmpSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8)
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMIB.setRevisions(
        ("2009-10-22 00:00",
         "2002-03-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechIgmpSnoopingMIBObjects_ObjectIdentity = ObjectIdentity
qtechIgmpSnoopingMIBObjects = _QtechIgmpSnoopingMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1)
)


class _QtechSNIgmpWorkingMode_Type(Integer32):
    """Custom type qtechSNIgmpWorkingMode based on Integer32"""
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


_QtechSNIgmpWorkingMode_Type.__name__ = "Integer32"
_QtechSNIgmpWorkingMode_Object = MibScalar
qtechSNIgmpWorkingMode = _QtechSNIgmpWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 1),
    _QtechSNIgmpWorkingMode_Type()
)
qtechSNIgmpWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpWorkingMode.setStatus("deprecated")


class _QtechSNIgmpSourcePortCheck_Type(EnabledStatus):
    """Custom type qtechSNIgmpSourcePortCheck based on EnabledStatus"""
    defaultValue = 2


_QtechSNIgmpSourcePortCheck_Type.__name__ = "EnabledStatus"
_QtechSNIgmpSourcePortCheck_Object = MibScalar
qtechSNIgmpSourcePortCheck = _QtechSNIgmpSourcePortCheck_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 2),
    _QtechSNIgmpSourcePortCheck_Type()
)
qtechSNIgmpSourcePortCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpSourcePortCheck.setStatus("deprecated")


class _QtechSNIgmpSourceIpCheck_Type(EnabledStatus):
    """Custom type qtechSNIgmpSourceIpCheck based on EnabledStatus"""
    defaultValue = 2


_QtechSNIgmpSourceIpCheck_Type.__name__ = "EnabledStatus"
_QtechSNIgmpSourceIpCheck_Object = MibScalar
qtechSNIgmpSourceIpCheck = _QtechSNIgmpSourceIpCheck_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 3),
    _QtechSNIgmpSourceIpCheck_Type()
)
qtechSNIgmpSourceIpCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpSourceIpCheck.setStatus("deprecated")
_QtechSNIgmpSourceIpCheckDefIp_Type = IpAddress
_QtechSNIgmpSourceIpCheckDefIp_Object = MibScalar
qtechSNIgmpSourceIpCheckDefIp = _QtechSNIgmpSourceIpCheckDefIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 4),
    _QtechSNIgmpSourceIpCheckDefIp_Type()
)
qtechSNIgmpSourceIpCheckDefIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpSourceIpCheckDefIp.setStatus("deprecated")
_QtechSNIgmpSrcIpCheckTable_Object = MibTable
qtechSNIgmpSrcIpCheckTable = _QtechSNIgmpSrcIpCheckTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 5)
)
if mibBuilder.loadTexts:
    qtechSNIgmpSrcIpCheckTable.setStatus("deprecated")
_QtechSNIgmpSrcIpCheckEntry_Object = MibTableRow
qtechSNIgmpSrcIpCheckEntry = _QtechSNIgmpSrcIpCheckEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 5, 1)
)
qtechSNIgmpSrcIpCheckEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSrcIpCheckVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSrcIpCheckMultiIpAddr"),
)
if mibBuilder.loadTexts:
    qtechSNIgmpSrcIpCheckEntry.setStatus("deprecated")
_QtechSNIgmpSrcIpCheckVID_Type = VlanId
_QtechSNIgmpSrcIpCheckVID_Object = MibTableColumn
qtechSNIgmpSrcIpCheckVID = _QtechSNIgmpSrcIpCheckVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 5, 1, 1),
    _QtechSNIgmpSrcIpCheckVID_Type()
)
qtechSNIgmpSrcIpCheckVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpSrcIpCheckVID.setStatus("deprecated")
_QtechSNIgmpSrcIpCheckMultiIpAddr_Type = IpAddress
_QtechSNIgmpSrcIpCheckMultiIpAddr_Object = MibTableColumn
qtechSNIgmpSrcIpCheckMultiIpAddr = _QtechSNIgmpSrcIpCheckMultiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 5, 1, 2),
    _QtechSNIgmpSrcIpCheckMultiIpAddr_Type()
)
qtechSNIgmpSrcIpCheckMultiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpSrcIpCheckMultiIpAddr.setStatus("deprecated")
_QtechSNIgmpSrcIpCheckSrcIpAddr_Type = IpAddress
_QtechSNIgmpSrcIpCheckSrcIpAddr_Object = MibTableColumn
qtechSNIgmpSrcIpCheckSrcIpAddr = _QtechSNIgmpSrcIpCheckSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 5, 1, 3),
    _QtechSNIgmpSrcIpCheckSrcIpAddr_Type()
)
qtechSNIgmpSrcIpCheckSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSNIgmpSrcIpCheckSrcIpAddr.setStatus("deprecated")


class _QtechSNIgmpSrcIpCheckEntryStatus_Type(Integer32):
    """Custom type qtechSNIgmpSrcIpCheckEntryStatus based on Integer32"""
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


_QtechSNIgmpSrcIpCheckEntryStatus_Type.__name__ = "Integer32"
_QtechSNIgmpSrcIpCheckEntryStatus_Object = MibTableColumn
qtechSNIgmpSrcIpCheckEntryStatus = _QtechSNIgmpSrcIpCheckEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 5, 1, 4),
    _QtechSNIgmpSrcIpCheckEntryStatus_Type()
)
qtechSNIgmpSrcIpCheckEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSNIgmpSrcIpCheckEntryStatus.setStatus("deprecated")
_QtechSNIgmpPortTable_Object = MibTable
qtechSNIgmpPortTable = _QtechSNIgmpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 6)
)
if mibBuilder.loadTexts:
    qtechSNIgmpPortTable.setStatus("deprecated")
_QtechSNIgmpPortEntry_Object = MibTableRow
qtechSNIgmpPortEntry = _QtechSNIgmpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 6, 1)
)
qtechSNIgmpPortEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpPortRouterVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpPortIndex"),
)
if mibBuilder.loadTexts:
    qtechSNIgmpPortEntry.setStatus("deprecated")
_QtechSNIgmpPortRouterVID_Type = VlanId
_QtechSNIgmpPortRouterVID_Object = MibTableColumn
qtechSNIgmpPortRouterVID = _QtechSNIgmpPortRouterVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 6, 1, 1),
    _QtechSNIgmpPortRouterVID_Type()
)
qtechSNIgmpPortRouterVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpPortRouterVID.setStatus("deprecated")
_QtechSNIgmpPortIndex_Type = IfIndex
_QtechSNIgmpPortIndex_Object = MibTableColumn
qtechSNIgmpPortIndex = _QtechSNIgmpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 6, 1, 2),
    _QtechSNIgmpPortIndex_Type()
)
qtechSNIgmpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpPortIndex.setStatus("deprecated")


class _QtechSNIgmpPortRouterState_Type(Integer32):
    """Custom type qtechSNIgmpPortRouterState based on Integer32"""
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


_QtechSNIgmpPortRouterState_Type.__name__ = "Integer32"
_QtechSNIgmpPortRouterState_Object = MibTableColumn
qtechSNIgmpPortRouterState = _QtechSNIgmpPortRouterState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 6, 1, 3),
    _QtechSNIgmpPortRouterState_Type()
)
qtechSNIgmpPortRouterState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpPortRouterState.setStatus("deprecated")
_QtechSNIgmpPortRouterProfile_Type = Unsigned32
_QtechSNIgmpPortRouterProfile_Object = MibTableColumn
qtechSNIgmpPortRouterProfile = _QtechSNIgmpPortRouterProfile_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 6, 1, 4),
    _QtechSNIgmpPortRouterProfile_Type()
)
qtechSNIgmpPortRouterProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpPortRouterProfile.setStatus("deprecated")
_QtechSNIgmpGDANumber_Type = Unsigned32
_QtechSNIgmpGDANumber_Object = MibScalar
qtechSNIgmpGDANumber = _QtechSNIgmpGDANumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 7),
    _QtechSNIgmpGDANumber_Type()
)
qtechSNIgmpGDANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDANumber.setStatus("deprecated")
_QtechSNIgmpGDATable_Object = MibTable
qtechSNIgmpGDATable = _QtechSNIgmpGDATable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 8)
)
if mibBuilder.loadTexts:
    qtechSNIgmpGDATable.setStatus("deprecated")
_QtechSNIgmpGDAEntry_Object = MibTableRow
qtechSNIgmpGDAEntry = _QtechSNIgmpGDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 8, 1)
)
qtechSNIgmpGDAEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAAddr"),
)
if mibBuilder.loadTexts:
    qtechSNIgmpGDAEntry.setStatus("deprecated")
_QtechSNIgmpGDAVID_Type = VlanId
_QtechSNIgmpGDAVID_Object = MibTableColumn
qtechSNIgmpGDAVID = _QtechSNIgmpGDAVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 8, 1, 1),
    _QtechSNIgmpGDAVID_Type()
)
qtechSNIgmpGDAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAVID.setStatus("deprecated")
_QtechSNIgmpGDAAddr_Type = IpAddress
_QtechSNIgmpGDAAddr_Object = MibTableColumn
qtechSNIgmpGDAAddr = _QtechSNIgmpGDAAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 8, 1, 2),
    _QtechSNIgmpGDAAddr_Type()
)
qtechSNIgmpGDAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAAddr.setStatus("deprecated")
_QtechSNIgmpGDAPortMemberAction_Type = MemberMap
_QtechSNIgmpGDAPortMemberAction_Object = MibTableColumn
qtechSNIgmpGDAPortMemberAction = _QtechSNIgmpGDAPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 8, 1, 3),
    _QtechSNIgmpGDAPortMemberAction_Type()
)
qtechSNIgmpGDAPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAPortMemberAction.setStatus("deprecated")
_QtechSNIgmpGDATrunkMemberAction_Type = MemberMap
_QtechSNIgmpGDATrunkMemberAction_Object = MibTableColumn
qtechSNIgmpGDATrunkMemberAction = _QtechSNIgmpGDATrunkMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 8, 1, 4),
    _QtechSNIgmpGDATrunkMemberAction_Type()
)
qtechSNIgmpGDATrunkMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpGDATrunkMemberAction.setStatus("deprecated")
_QtechSNIgmpSvglVID_Type = Integer32
_QtechSNIgmpSvglVID_Object = MibScalar
qtechSNIgmpSvglVID = _QtechSNIgmpSvglVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 9),
    _QtechSNIgmpSvglVID_Type()
)
qtechSNIgmpSvglVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpSvglVID.setStatus("deprecated")
_QtechSNIgmpSvglProfile_Type = Unsigned32
_QtechSNIgmpSvglProfile_Object = MibScalar
qtechSNIgmpSvglProfile = _QtechSNIgmpSvglProfile_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 10),
    _QtechSNIgmpSvglProfile_Type()
)
qtechSNIgmpSvglProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpSvglProfile.setStatus("deprecated")
_QtechSNIgmpMrLearnTable_Object = MibTable
qtechSNIgmpMrLearnTable = _QtechSNIgmpMrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 11)
)
if mibBuilder.loadTexts:
    qtechSNIgmpMrLearnTable.setStatus("deprecated")
_QtechSNIgmpMrLearnEntry_Object = MibTableRow
qtechSNIgmpMrLearnEntry = _QtechSNIgmpMrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 11, 1)
)
qtechSNIgmpMrLearnEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpMrLearnVID"),
)
if mibBuilder.loadTexts:
    qtechSNIgmpMrLearnEntry.setStatus("deprecated")
_QtechSNIgmpMrLearnVID_Type = VlanId
_QtechSNIgmpMrLearnVID_Object = MibTableColumn
qtechSNIgmpMrLearnVID = _QtechSNIgmpMrLearnVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 11, 1, 1),
    _QtechSNIgmpMrLearnVID_Type()
)
qtechSNIgmpMrLearnVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpMrLearnVID.setStatus("deprecated")


class _QtechSNIgmpMrLearnStatus_Type(Integer32):
    """Custom type qtechSNIgmpMrLearnStatus based on Integer32"""
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


_QtechSNIgmpMrLearnStatus_Type.__name__ = "Integer32"
_QtechSNIgmpMrLearnStatus_Object = MibTableColumn
qtechSNIgmpMrLearnStatus = _QtechSNIgmpMrLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 11, 1, 2),
    _QtechSNIgmpMrLearnStatus_Type()
)
qtechSNIgmpMrLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpMrLearnStatus.setStatus("deprecated")
_QtechSNIgmpPortFilteringTable_Object = MibTable
qtechSNIgmpPortFilteringTable = _QtechSNIgmpPortFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 12)
)
if mibBuilder.loadTexts:
    qtechSNIgmpPortFilteringTable.setStatus("deprecated")
_QtechSNIgmpPortFilteringEntry_Object = MibTableRow
qtechSNIgmpPortFilteringEntry = _QtechSNIgmpPortFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 12, 1)
)
qtechSNIgmpPortFilteringEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNPortIndex"),
)
if mibBuilder.loadTexts:
    qtechSNIgmpPortFilteringEntry.setStatus("deprecated")
_QtechSNPortIndex_Type = IfIndex
_QtechSNPortIndex_Object = MibTableColumn
qtechSNPortIndex = _QtechSNPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 12, 1, 1),
    _QtechSNPortIndex_Type()
)
qtechSNPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNPortIndex.setStatus("deprecated")
_QtechSNIgmpFilteringProfile_Type = Unsigned32
_QtechSNIgmpFilteringProfile_Object = MibTableColumn
qtechSNIgmpFilteringProfile = _QtechSNIgmpFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 12, 1, 2),
    _QtechSNIgmpFilteringProfile_Type()
)
qtechSNIgmpFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpFilteringProfile.setStatus("deprecated")
_QtechSNIgmpFilteringMaxGroups_Type = Unsigned32
_QtechSNIgmpFilteringMaxGroups_Object = MibTableColumn
qtechSNIgmpFilteringMaxGroups = _QtechSNIgmpFilteringMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 12, 1, 3),
    _QtechSNIgmpFilteringMaxGroups_Type()
)
qtechSNIgmpFilteringMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpFilteringMaxGroups.setStatus("deprecated")
_QtechSNIgmpGDAConfigTable_Object = MibTable
qtechSNIgmpGDAConfigTable = _QtechSNIgmpGDAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 13)
)
if mibBuilder.loadTexts:
    qtechSNIgmpGDAConfigTable.setStatus("deprecated")
_QtechSNIgmpGDAConfigEntry_Object = MibTableRow
qtechSNIgmpGDAConfigEntry = _QtechSNIgmpGDAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 13, 1)
)
qtechSNIgmpGDAConfigEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAConfigVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAConfigAddr"),
)
if mibBuilder.loadTexts:
    qtechSNIgmpGDAConfigEntry.setStatus("deprecated")
_QtechSNIgmpGDAConfigVID_Type = VlanId
_QtechSNIgmpGDAConfigVID_Object = MibTableColumn
qtechSNIgmpGDAConfigVID = _QtechSNIgmpGDAConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 13, 1, 1),
    _QtechSNIgmpGDAConfigVID_Type()
)
qtechSNIgmpGDAConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAConfigVID.setStatus("deprecated")
_QtechSNIgmpGDAConfigAddr_Type = IpAddress
_QtechSNIgmpGDAConfigAddr_Object = MibTableColumn
qtechSNIgmpGDAConfigAddr = _QtechSNIgmpGDAConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 13, 1, 2),
    _QtechSNIgmpGDAConfigAddr_Type()
)
qtechSNIgmpGDAConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAConfigAddr.setStatus("deprecated")
_QtechSNIgmpGDAConfigIfIndex_Type = IfIndex
_QtechSNIgmpGDAConfigIfIndex_Object = MibTableColumn
qtechSNIgmpGDAConfigIfIndex = _QtechSNIgmpGDAConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 13, 1, 3),
    _QtechSNIgmpGDAConfigIfIndex_Type()
)
qtechSNIgmpGDAConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAConfigIfIndex.setStatus("deprecated")


class _QtechSNIgmpGDAConfigType_Type(Integer32):
    """Custom type qtechSNIgmpGDAConfigType based on Integer32"""
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


_QtechSNIgmpGDAConfigType_Type.__name__ = "Integer32"
_QtechSNIgmpGDAConfigType_Object = MibTableColumn
qtechSNIgmpGDAConfigType = _QtechSNIgmpGDAConfigType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 13, 1, 4),
    _QtechSNIgmpGDAConfigType_Type()
)
qtechSNIgmpGDAConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAConfigType.setStatus("deprecated")


class _QtechSNIgmpGDAConfigStatus_Type(Integer32):
    """Custom type qtechSNIgmpGDAConfigStatus based on Integer32"""
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


_QtechSNIgmpGDAConfigStatus_Type.__name__ = "Integer32"
_QtechSNIgmpGDAConfigStatus_Object = MibTableColumn
qtechSNIgmpGDAConfigStatus = _QtechSNIgmpGDAConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 13, 1, 5),
    _QtechSNIgmpGDAConfigStatus_Type()
)
qtechSNIgmpGDAConfigStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNIgmpGDAConfigStatus.setStatus("deprecated")
_QtechSNIgmpQueryResponeTime_Type = Unsigned32
_QtechSNIgmpQueryResponeTime_Object = MibScalar
qtechSNIgmpQueryResponeTime = _QtechSNIgmpQueryResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 14),
    _QtechSNIgmpQueryResponeTime_Type()
)
qtechSNIgmpQueryResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSNIgmpQueryResponeTime.setStatus("deprecated")


class _QtechIgmpSnoopingWorkingMode_Type(Integer32):
    """Custom type qtechIgmpSnoopingWorkingMode based on Integer32"""
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


_QtechIgmpSnoopingWorkingMode_Type.__name__ = "Integer32"
_QtechIgmpSnoopingWorkingMode_Object = MibScalar
qtechIgmpSnoopingWorkingMode = _QtechIgmpSnoopingWorkingMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 15),
    _QtechIgmpSnoopingWorkingMode_Type()
)
qtechIgmpSnoopingWorkingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingWorkingMode.setStatus("current")
_QtechIgmpSnoopingGDANumber_Type = Unsigned32
_QtechIgmpSnoopingGDANumber_Object = MibScalar
qtechIgmpSnoopingGDANumber = _QtechIgmpSnoopingGDANumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 16),
    _QtechIgmpSnoopingGDANumber_Type()
)
qtechIgmpSnoopingGDANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDANumber.setStatus("current")
_QtechIgmpSnoopingGDATable_Object = MibTable
qtechIgmpSnoopingGDATable = _QtechIgmpSnoopingGDATable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 17)
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDATable.setStatus("current")
_QtechIgmpSnoopingGDAEntry_Object = MibTableRow
qtechIgmpSnoopingGDAEntry = _QtechIgmpSnoopingGDAEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 17, 1)
)
qtechIgmpSnoopingGDAEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAAddr"),
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAEntry.setStatus("current")
_QtechIgmpSnoopingGDAVID_Type = VlanId
_QtechIgmpSnoopingGDAVID_Object = MibTableColumn
qtechIgmpSnoopingGDAVID = _QtechIgmpSnoopingGDAVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 17, 1, 1),
    _QtechIgmpSnoopingGDAVID_Type()
)
qtechIgmpSnoopingGDAVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAVID.setStatus("current")
_QtechIgmpSnoopingGDAAddr_Type = IpAddress
_QtechIgmpSnoopingGDAAddr_Object = MibTableColumn
qtechIgmpSnoopingGDAAddr = _QtechIgmpSnoopingGDAAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 17, 1, 2),
    _QtechIgmpSnoopingGDAAddr_Type()
)
qtechIgmpSnoopingGDAAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAAddr.setStatus("current")
_QtechIgmpSnoopingGDAPortMemberAction_Type = MemberMap
_QtechIgmpSnoopingGDAPortMemberAction_Object = MibTableColumn
qtechIgmpSnoopingGDAPortMemberAction = _QtechIgmpSnoopingGDAPortMemberAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 17, 1, 3),
    _QtechIgmpSnoopingGDAPortMemberAction_Type()
)
qtechIgmpSnoopingGDAPortMemberAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAPortMemberAction.setStatus("current")
_QtechIgmpSnoopingVlanStatusTable_Object = MibTable
qtechIgmpSnoopingVlanStatusTable = _QtechIgmpSnoopingVlanStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 18)
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingVlanStatusTable.setStatus("current")
_QtechIgmpSnoopingVlanStatusEntry_Object = MibTableRow
qtechIgmpSnoopingVlanStatusEntry = _QtechIgmpSnoopingVlanStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 18, 1)
)
qtechIgmpSnoopingVlanStatusEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingVlanStatusVID"),
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingVlanStatusEntry.setStatus("current")
_QtechIgmpSnoopingVlanStatusVID_Type = VlanId
_QtechIgmpSnoopingVlanStatusVID_Object = MibTableColumn
qtechIgmpSnoopingVlanStatusVID = _QtechIgmpSnoopingVlanStatusVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 18, 1, 1),
    _QtechIgmpSnoopingVlanStatusVID_Type()
)
qtechIgmpSnoopingVlanStatusVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingVlanStatusVID.setStatus("current")
_QtechIgmpSnoopingVlanStatusStatus_Type = EnabledStatus
_QtechIgmpSnoopingVlanStatusStatus_Object = MibTableColumn
qtechIgmpSnoopingVlanStatusStatus = _QtechIgmpSnoopingVlanStatusStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 18, 1, 2),
    _QtechIgmpSnoopingVlanStatusStatus_Type()
)
qtechIgmpSnoopingVlanStatusStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingVlanStatusStatus.setStatus("current")
_QtechIgmpSnoopingSvglVID_Type = Integer32
_QtechIgmpSnoopingSvglVID_Object = MibScalar
qtechIgmpSnoopingSvglVID = _QtechIgmpSnoopingSvglVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 19),
    _QtechIgmpSnoopingSvglVID_Type()
)
qtechIgmpSnoopingSvglVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingSvglVID.setStatus("current")
_QtechIgmpSnoopingSvglProfile_Type = Unsigned32
_QtechIgmpSnoopingSvglProfile_Object = MibScalar
qtechIgmpSnoopingSvglProfile = _QtechIgmpSnoopingSvglProfile_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 20),
    _QtechIgmpSnoopingSvglProfile_Type()
)
qtechIgmpSnoopingSvglProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingSvglProfile.setStatus("current")
_QtechIgmpSnoopingMrLearnTable_Object = MibTable
qtechIgmpSnoopingMrLearnTable = _QtechIgmpSnoopingMrLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 21)
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMrLearnTable.setStatus("current")
_QtechIgmpSnoopingMrLearnEntry_Object = MibTableRow
qtechIgmpSnoopingMrLearnEntry = _QtechIgmpSnoopingMrLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 21, 1)
)
qtechIgmpSnoopingMrLearnEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingMrLearnVID"),
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMrLearnEntry.setStatus("current")
_QtechIgmpSnoopingMrLearnVID_Type = VlanId
_QtechIgmpSnoopingMrLearnVID_Object = MibTableColumn
qtechIgmpSnoopingMrLearnVID = _QtechIgmpSnoopingMrLearnVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 21, 1, 1),
    _QtechIgmpSnoopingMrLearnVID_Type()
)
qtechIgmpSnoopingMrLearnVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMrLearnVID.setStatus("current")


class _QtechIgmpSnoopingMrLearnStatus_Type(Integer32):
    """Custom type qtechIgmpSnoopingMrLearnStatus based on Integer32"""
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


_QtechIgmpSnoopingMrLearnStatus_Type.__name__ = "Integer32"
_QtechIgmpSnoopingMrLearnStatus_Object = MibTableColumn
qtechIgmpSnoopingMrLearnStatus = _QtechIgmpSnoopingMrLearnStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 21, 1, 2),
    _QtechIgmpSnoopingMrLearnStatus_Type()
)
qtechIgmpSnoopingMrLearnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMrLearnStatus.setStatus("current")
_QtechIgmpSnoopingPortFilteringTable_Object = MibTable
qtechIgmpSnoopingPortFilteringTable = _QtechIgmpSnoopingPortFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 22)
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingPortFilteringTable.setStatus("current")
_QtechIgmpSnoopingPortFilteringEntry_Object = MibTableRow
qtechIgmpSnoopingPortFilteringEntry = _QtechIgmpSnoopingPortFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 22, 1)
)
qtechIgmpSnoopingPortFilteringEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingportIndex"),
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingPortFilteringEntry.setStatus("current")
_QtechIgmpSnoopingportIndex_Type = IfIndex
_QtechIgmpSnoopingportIndex_Object = MibTableColumn
qtechIgmpSnoopingportIndex = _QtechIgmpSnoopingportIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 22, 1, 1),
    _QtechIgmpSnoopingportIndex_Type()
)
qtechIgmpSnoopingportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingportIndex.setStatus("current")
_QtechIgmpSnoopingFilteringProfile_Type = Unsigned32
_QtechIgmpSnoopingFilteringProfile_Object = MibTableColumn
qtechIgmpSnoopingFilteringProfile = _QtechIgmpSnoopingFilteringProfile_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 22, 1, 2),
    _QtechIgmpSnoopingFilteringProfile_Type()
)
qtechIgmpSnoopingFilteringProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingFilteringProfile.setStatus("current")
_QtechIgmpSnoopingFilteringMaxGroups_Type = Unsigned32
_QtechIgmpSnoopingFilteringMaxGroups_Object = MibTableColumn
qtechIgmpSnoopingFilteringMaxGroups = _QtechIgmpSnoopingFilteringMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 22, 1, 3),
    _QtechIgmpSnoopingFilteringMaxGroups_Type()
)
qtechIgmpSnoopingFilteringMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingFilteringMaxGroups.setStatus("current")
_QtechIgmpSnoopingGDAConfigTable_Object = MibTable
qtechIgmpSnoopingGDAConfigTable = _QtechIgmpSnoopingGDAConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 23)
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAConfigTable.setStatus("current")
_QtechIgmpSnoopingGDAConfigEntry_Object = MibTableRow
qtechIgmpSnoopingGDAConfigEntry = _QtechIgmpSnoopingGDAConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 23, 1)
)
qtechIgmpSnoopingGDAConfigEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAConfigVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAConfigAddr"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAConfigIfIndex"),
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAConfigEntry.setStatus("current")
_QtechIgmpSnoopingGDAConfigVID_Type = VlanId
_QtechIgmpSnoopingGDAConfigVID_Object = MibTableColumn
qtechIgmpSnoopingGDAConfigVID = _QtechIgmpSnoopingGDAConfigVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 23, 1, 1),
    _QtechIgmpSnoopingGDAConfigVID_Type()
)
qtechIgmpSnoopingGDAConfigVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAConfigVID.setStatus("current")
_QtechIgmpSnoopingGDAConfigAddr_Type = IpAddress
_QtechIgmpSnoopingGDAConfigAddr_Object = MibTableColumn
qtechIgmpSnoopingGDAConfigAddr = _QtechIgmpSnoopingGDAConfigAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 23, 1, 2),
    _QtechIgmpSnoopingGDAConfigAddr_Type()
)
qtechIgmpSnoopingGDAConfigAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAConfigAddr.setStatus("current")
_QtechIgmpSnoopingGDAConfigIfIndex_Type = IfIndex
_QtechIgmpSnoopingGDAConfigIfIndex_Object = MibTableColumn
qtechIgmpSnoopingGDAConfigIfIndex = _QtechIgmpSnoopingGDAConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 23, 1, 3),
    _QtechIgmpSnoopingGDAConfigIfIndex_Type()
)
qtechIgmpSnoopingGDAConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAConfigIfIndex.setStatus("current")
_QtechIgmpSnoopingQueryResponeTime_Type = Unsigned32
_QtechIgmpSnoopingQueryResponeTime_Object = MibScalar
qtechIgmpSnoopingQueryResponeTime = _QtechIgmpSnoopingQueryResponeTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 24),
    _QtechIgmpSnoopingQueryResponeTime_Type()
)
qtechIgmpSnoopingQueryResponeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingQueryResponeTime.setStatus("current")
_QtechIgmpSnoopingReportSuppress_Type = TruthValue
_QtechIgmpSnoopingReportSuppress_Object = MibScalar
qtechIgmpSnoopingReportSuppress = _QtechIgmpSnoopingReportSuppress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 25),
    _QtechIgmpSnoopingReportSuppress_Type()
)
qtechIgmpSnoopingReportSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingReportSuppress.setStatus("current")
_QtechIgmpSnoopingFastleave_Type = TruthValue
_QtechIgmpSnoopingFastleave_Object = MibScalar
qtechIgmpSnoopingFastleave = _QtechIgmpSnoopingFastleave_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 26),
    _QtechIgmpSnoopingFastleave_Type()
)
qtechIgmpSnoopingFastleave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingFastleave.setStatus("current")
_QtechIgmpSnoopingGDANewTable_Object = MibTable
qtechIgmpSnoopingGDANewTable = _QtechIgmpSnoopingGDANewTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27)
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDANewTable.setStatus("current")
_QtechIgmpSnoopingGDANewEntry_Object = MibTableRow
qtechIgmpSnoopingGDANewEntry = _QtechIgmpSnoopingGDANewEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27, 1)
)
qtechIgmpSnoopingGDANewEntry.setIndexNames(
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDANewInVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDANewOutVID"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgsmpSnoopingGDASrc"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAGrp"),
    (0, "QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAIfx"),
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDANewEntry.setStatus("current")
_QtechIgmpSnoopingGDANewInVID_Type = VlanId
_QtechIgmpSnoopingGDANewInVID_Object = MibTableColumn
qtechIgmpSnoopingGDANewInVID = _QtechIgmpSnoopingGDANewInVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27, 1, 1),
    _QtechIgmpSnoopingGDANewInVID_Type()
)
qtechIgmpSnoopingGDANewInVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDANewInVID.setStatus("current")
_QtechIgmpSnoopingGDANewOutVID_Type = VlanId
_QtechIgmpSnoopingGDANewOutVID_Object = MibTableColumn
qtechIgmpSnoopingGDANewOutVID = _QtechIgmpSnoopingGDANewOutVID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27, 1, 2),
    _QtechIgmpSnoopingGDANewOutVID_Type()
)
qtechIgmpSnoopingGDANewOutVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDANewOutVID.setStatus("current")
_QtechIgsmpSnoopingGDASrc_Type = IpAddress
_QtechIgsmpSnoopingGDASrc_Object = MibTableColumn
qtechIgsmpSnoopingGDASrc = _QtechIgsmpSnoopingGDASrc_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27, 1, 3),
    _QtechIgsmpSnoopingGDASrc_Type()
)
qtechIgsmpSnoopingGDASrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgsmpSnoopingGDASrc.setStatus("current")
_QtechIgmpSnoopingGDAGrp_Type = IpAddress
_QtechIgmpSnoopingGDAGrp_Object = MibTableColumn
qtechIgmpSnoopingGDAGrp = _QtechIgmpSnoopingGDAGrp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27, 1, 4),
    _QtechIgmpSnoopingGDAGrp_Type()
)
qtechIgmpSnoopingGDAGrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAGrp.setStatus("current")
_QtechIgmpSnoopingGDAIfx_Type = IfIndex
_QtechIgmpSnoopingGDAIfx_Object = MibTableColumn
qtechIgmpSnoopingGDAIfx = _QtechIgmpSnoopingGDAIfx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27, 1, 5),
    _QtechIgmpSnoopingGDAIfx_Type()
)
qtechIgmpSnoopingGDAIfx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAIfx.setStatus("current")
_QtechIgmpSnoopingGDAIfxAction_Type = Integer32
_QtechIgmpSnoopingGDAIfxAction_Object = MibTableColumn
qtechIgmpSnoopingGDAIfxAction = _QtechIgmpSnoopingGDAIfxAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 27, 1, 6),
    _QtechIgmpSnoopingGDAIfxAction_Type()
)
qtechIgmpSnoopingGDAIfxAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingGDAIfxAction.setStatus("current")


class _QtechIgmpSnoopingMulticastWlan_Type(Integer32):
    """Custom type qtechIgmpSnoopingMulticastWlan based on Integer32"""
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


_QtechIgmpSnoopingMulticastWlan_Type.__name__ = "Integer32"
_QtechIgmpSnoopingMulticastWlan_Object = MibScalar
qtechIgmpSnoopingMulticastWlan = _QtechIgmpSnoopingMulticastWlan_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 1, 28),
    _QtechIgmpSnoopingMulticastWlan_Type()
)
qtechIgmpSnoopingMulticastWlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMulticastWlan.setStatus("current")
_QtechIgmpSnoopingMIBConformance_ObjectIdentity = ObjectIdentity
qtechIgmpSnoopingMIBConformance = _QtechIgmpSnoopingMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 2)
)
_QtechIgmpSnoopingMIBCompliances_ObjectIdentity = ObjectIdentity
qtechIgmpSnoopingMIBCompliances = _QtechIgmpSnoopingMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 2, 1)
)
_QtechIgmpSnoopingMIBGroups_ObjectIdentity = ObjectIdentity
qtechIgmpSnoopingMIBGroups = _QtechIgmpSnoopingMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 2, 2)
)

# Managed Objects groups

qtechIgmpSnoopingMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 2, 2, 1)
)
qtechIgmpSnoopingMIBGroup.setObjects(
      *(("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpWorkingMode"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSourcePortCheck"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSourceIpCheck"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSourceIpCheckDefIp"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSrcIpCheckVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSrcIpCheckMultiIpAddr"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSrcIpCheckSrcIpAddr"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSrcIpCheckEntryStatus"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpPortRouterVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpPortIndex"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpPortRouterState"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpPortRouterProfile"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDANumber"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAAddr"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAPortMemberAction"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDATrunkMemberAction"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSvglVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpSvglProfile"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpMrLearnVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpMrLearnStatus"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNPortIndex"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpFilteringProfile"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpFilteringMaxGroups"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAConfigVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAConfigAddr"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAConfigIfIndex"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAConfigType"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpGDAConfigStatus"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechSNIgmpQueryResponeTime"))
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMIBGroup.setStatus("deprecated")

qtechIgmpSnoopingMIBGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 2, 2, 2)
)
qtechIgmpSnoopingMIBGroup2.setObjects(
      *(("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingWorkingMode"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDANumber"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAAddr"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAPortMemberAction"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingVlanStatusVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingVlanStatusStatus"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingSvglVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingSvglProfile"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingMrLearnVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingMrLearnStatus"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingportIndex"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingFilteringProfile"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingFilteringMaxGroups"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAConfigVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAConfigAddr"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAConfigIfIndex"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingQueryResponeTime"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingReportSuppress"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingFastleave"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDANewInVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDANewOutVID"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgsmpSnoopingGDASrc"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAGrp"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAIfx"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingGDAIfxAction"),
        ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingMulticastWlan"))
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMIBGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechIgmpSnoopingMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 2, 1, 1)
)
qtechIgmpSnoopingMIBCompliance.setObjects(
    ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingMIBGroup")
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMIBCompliance.setStatus(
        "deprecated"
    )

qtechIgmpSnoopingMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 8, 2, 1, 2)
)
qtechIgmpSnoopingMIBCompliance2.setObjects(
    ("QTECH-IGMP-SNOOPING-MIB", "qtechIgmpSnoopingMIBGroup2")
)
if mibBuilder.loadTexts:
    qtechIgmpSnoopingMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IGMP-SNOOPING-MIB",
    **{"qtechIgmpSnoopingMIB": qtechIgmpSnoopingMIB,
       "qtechIgmpSnoopingMIBObjects": qtechIgmpSnoopingMIBObjects,
       "qtechSNIgmpWorkingMode": qtechSNIgmpWorkingMode,
       "qtechSNIgmpSourcePortCheck": qtechSNIgmpSourcePortCheck,
       "qtechSNIgmpSourceIpCheck": qtechSNIgmpSourceIpCheck,
       "qtechSNIgmpSourceIpCheckDefIp": qtechSNIgmpSourceIpCheckDefIp,
       "qtechSNIgmpSrcIpCheckTable": qtechSNIgmpSrcIpCheckTable,
       "qtechSNIgmpSrcIpCheckEntry": qtechSNIgmpSrcIpCheckEntry,
       "qtechSNIgmpSrcIpCheckVID": qtechSNIgmpSrcIpCheckVID,
       "qtechSNIgmpSrcIpCheckMultiIpAddr": qtechSNIgmpSrcIpCheckMultiIpAddr,
       "qtechSNIgmpSrcIpCheckSrcIpAddr": qtechSNIgmpSrcIpCheckSrcIpAddr,
       "qtechSNIgmpSrcIpCheckEntryStatus": qtechSNIgmpSrcIpCheckEntryStatus,
       "qtechSNIgmpPortTable": qtechSNIgmpPortTable,
       "qtechSNIgmpPortEntry": qtechSNIgmpPortEntry,
       "qtechSNIgmpPortRouterVID": qtechSNIgmpPortRouterVID,
       "qtechSNIgmpPortIndex": qtechSNIgmpPortIndex,
       "qtechSNIgmpPortRouterState": qtechSNIgmpPortRouterState,
       "qtechSNIgmpPortRouterProfile": qtechSNIgmpPortRouterProfile,
       "qtechSNIgmpGDANumber": qtechSNIgmpGDANumber,
       "qtechSNIgmpGDATable": qtechSNIgmpGDATable,
       "qtechSNIgmpGDAEntry": qtechSNIgmpGDAEntry,
       "qtechSNIgmpGDAVID": qtechSNIgmpGDAVID,
       "qtechSNIgmpGDAAddr": qtechSNIgmpGDAAddr,
       "qtechSNIgmpGDAPortMemberAction": qtechSNIgmpGDAPortMemberAction,
       "qtechSNIgmpGDATrunkMemberAction": qtechSNIgmpGDATrunkMemberAction,
       "qtechSNIgmpSvglVID": qtechSNIgmpSvglVID,
       "qtechSNIgmpSvglProfile": qtechSNIgmpSvglProfile,
       "qtechSNIgmpMrLearnTable": qtechSNIgmpMrLearnTable,
       "qtechSNIgmpMrLearnEntry": qtechSNIgmpMrLearnEntry,
       "qtechSNIgmpMrLearnVID": qtechSNIgmpMrLearnVID,
       "qtechSNIgmpMrLearnStatus": qtechSNIgmpMrLearnStatus,
       "qtechSNIgmpPortFilteringTable": qtechSNIgmpPortFilteringTable,
       "qtechSNIgmpPortFilteringEntry": qtechSNIgmpPortFilteringEntry,
       "qtechSNPortIndex": qtechSNPortIndex,
       "qtechSNIgmpFilteringProfile": qtechSNIgmpFilteringProfile,
       "qtechSNIgmpFilteringMaxGroups": qtechSNIgmpFilteringMaxGroups,
       "qtechSNIgmpGDAConfigTable": qtechSNIgmpGDAConfigTable,
       "qtechSNIgmpGDAConfigEntry": qtechSNIgmpGDAConfigEntry,
       "qtechSNIgmpGDAConfigVID": qtechSNIgmpGDAConfigVID,
       "qtechSNIgmpGDAConfigAddr": qtechSNIgmpGDAConfigAddr,
       "qtechSNIgmpGDAConfigIfIndex": qtechSNIgmpGDAConfigIfIndex,
       "qtechSNIgmpGDAConfigType": qtechSNIgmpGDAConfigType,
       "qtechSNIgmpGDAConfigStatus": qtechSNIgmpGDAConfigStatus,
       "qtechSNIgmpQueryResponeTime": qtechSNIgmpQueryResponeTime,
       "qtechIgmpSnoopingWorkingMode": qtechIgmpSnoopingWorkingMode,
       "qtechIgmpSnoopingGDANumber": qtechIgmpSnoopingGDANumber,
       "qtechIgmpSnoopingGDATable": qtechIgmpSnoopingGDATable,
       "qtechIgmpSnoopingGDAEntry": qtechIgmpSnoopingGDAEntry,
       "qtechIgmpSnoopingGDAVID": qtechIgmpSnoopingGDAVID,
       "qtechIgmpSnoopingGDAAddr": qtechIgmpSnoopingGDAAddr,
       "qtechIgmpSnoopingGDAPortMemberAction": qtechIgmpSnoopingGDAPortMemberAction,
       "qtechIgmpSnoopingVlanStatusTable": qtechIgmpSnoopingVlanStatusTable,
       "qtechIgmpSnoopingVlanStatusEntry": qtechIgmpSnoopingVlanStatusEntry,
       "qtechIgmpSnoopingVlanStatusVID": qtechIgmpSnoopingVlanStatusVID,
       "qtechIgmpSnoopingVlanStatusStatus": qtechIgmpSnoopingVlanStatusStatus,
       "qtechIgmpSnoopingSvglVID": qtechIgmpSnoopingSvglVID,
       "qtechIgmpSnoopingSvglProfile": qtechIgmpSnoopingSvglProfile,
       "qtechIgmpSnoopingMrLearnTable": qtechIgmpSnoopingMrLearnTable,
       "qtechIgmpSnoopingMrLearnEntry": qtechIgmpSnoopingMrLearnEntry,
       "qtechIgmpSnoopingMrLearnVID": qtechIgmpSnoopingMrLearnVID,
       "qtechIgmpSnoopingMrLearnStatus": qtechIgmpSnoopingMrLearnStatus,
       "qtechIgmpSnoopingPortFilteringTable": qtechIgmpSnoopingPortFilteringTable,
       "qtechIgmpSnoopingPortFilteringEntry": qtechIgmpSnoopingPortFilteringEntry,
       "qtechIgmpSnoopingportIndex": qtechIgmpSnoopingportIndex,
       "qtechIgmpSnoopingFilteringProfile": qtechIgmpSnoopingFilteringProfile,
       "qtechIgmpSnoopingFilteringMaxGroups": qtechIgmpSnoopingFilteringMaxGroups,
       "qtechIgmpSnoopingGDAConfigTable": qtechIgmpSnoopingGDAConfigTable,
       "qtechIgmpSnoopingGDAConfigEntry": qtechIgmpSnoopingGDAConfigEntry,
       "qtechIgmpSnoopingGDAConfigVID": qtechIgmpSnoopingGDAConfigVID,
       "qtechIgmpSnoopingGDAConfigAddr": qtechIgmpSnoopingGDAConfigAddr,
       "qtechIgmpSnoopingGDAConfigIfIndex": qtechIgmpSnoopingGDAConfigIfIndex,
       "qtechIgmpSnoopingQueryResponeTime": qtechIgmpSnoopingQueryResponeTime,
       "qtechIgmpSnoopingReportSuppress": qtechIgmpSnoopingReportSuppress,
       "qtechIgmpSnoopingFastleave": qtechIgmpSnoopingFastleave,
       "qtechIgmpSnoopingGDANewTable": qtechIgmpSnoopingGDANewTable,
       "qtechIgmpSnoopingGDANewEntry": qtechIgmpSnoopingGDANewEntry,
       "qtechIgmpSnoopingGDANewInVID": qtechIgmpSnoopingGDANewInVID,
       "qtechIgmpSnoopingGDANewOutVID": qtechIgmpSnoopingGDANewOutVID,
       "qtechIgsmpSnoopingGDASrc": qtechIgsmpSnoopingGDASrc,
       "qtechIgmpSnoopingGDAGrp": qtechIgmpSnoopingGDAGrp,
       "qtechIgmpSnoopingGDAIfx": qtechIgmpSnoopingGDAIfx,
       "qtechIgmpSnoopingGDAIfxAction": qtechIgmpSnoopingGDAIfxAction,
       "qtechIgmpSnoopingMulticastWlan": qtechIgmpSnoopingMulticastWlan,
       "qtechIgmpSnoopingMIBConformance": qtechIgmpSnoopingMIBConformance,
       "qtechIgmpSnoopingMIBCompliances": qtechIgmpSnoopingMIBCompliances,
       "qtechIgmpSnoopingMIBCompliance": qtechIgmpSnoopingMIBCompliance,
       "qtechIgmpSnoopingMIBCompliance2": qtechIgmpSnoopingMIBCompliance2,
       "qtechIgmpSnoopingMIBGroups": qtechIgmpSnoopingMIBGroups,
       "qtechIgmpSnoopingMIBGroup": qtechIgmpSnoopingMIBGroup,
       "qtechIgmpSnoopingMIBGroup2": qtechIgmpSnoopingMIBGroup2}
)
