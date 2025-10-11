# SNMP MIB module (HQOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/HQOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:04 2025
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

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(zxr10switch,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "zxr10switch")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hqos_ObjectIdentity = ObjectIdentity
hqos = _Hqos_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16)
)
_HqosFlowClassTable_Object = MibTable
hqosFlowClassTable = _HqosFlowClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 1)
)
if mibBuilder.loadTexts:
    hqosFlowClassTable.setStatus("current")
_HqosFlowClassEntry_Object = MibTableRow
hqosFlowClassEntry = _HqosFlowClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 1, 1)
)
hqosFlowClassEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosFlowClassName"),
)
if mibBuilder.loadTexts:
    hqosFlowClassEntry.setStatus("current")


class _HqosFlowClassName_Type(DisplayString):
    """Custom type hqosFlowClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosFlowClassName_Type.__name__ = "DisplayString"
_HqosFlowClassName_Object = MibTableColumn
hqosFlowClassName = _HqosFlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 1, 1, 1),
    _HqosFlowClassName_Type()
)
hqosFlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosFlowClassName.setStatus("current")
_HqosFlowMatchTable_Object = MibTable
hqosFlowMatchTable = _HqosFlowMatchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2)
)
if mibBuilder.loadTexts:
    hqosFlowMatchTable.setStatus("current")
_HqosFlowMatchEntry_Object = MibTableRow
hqosFlowMatchEntry = _HqosFlowMatchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1)
)
hqosFlowMatchEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosFlowClassName"),
)
if mibBuilder.loadTexts:
    hqosFlowMatchEntry.setStatus("current")


class _HqosMatchFlowclass_Type(DisplayString):
    """Custom type hqosMatchFlowclass based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosMatchFlowclass_Type.__name__ = "DisplayString"
_HqosMatchFlowclass_Object = MibTableColumn
hqosMatchFlowclass = _HqosMatchFlowclass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 1),
    _HqosMatchFlowclass_Type()
)
hqosMatchFlowclass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchFlowclass.setStatus("current")


class _HqosMatchType_Type(Integer32):
    """Custom type hqosMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unvalid", 0),
          ("acl", 1),
          ("vlan", 3),
          ("phb", 5),
          ("svlan", 6),
          ("cvlan", 7))
    )


_HqosMatchType_Type.__name__ = "Integer32"
_HqosMatchType_Object = MibTableColumn
hqosMatchType = _HqosMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 2),
    _HqosMatchType_Type()
)
hqosMatchType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchType.setStatus("current")
_HqosMatchAclNo_Type = Integer32
_HqosMatchAclNo_Object = MibTableColumn
hqosMatchAclNo = _HqosMatchAclNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 3),
    _HqosMatchAclNo_Type()
)
hqosMatchAclNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchAclNo.setStatus("current")
_HqosMatchRuleNo_Type = Integer32
_HqosMatchRuleNo_Object = MibTableColumn
hqosMatchRuleNo = _HqosMatchRuleNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 4),
    _HqosMatchRuleNo_Type()
)
hqosMatchRuleNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchRuleNo.setStatus("current")


class _HqosMatchVlanID_Type(Integer32):
    """Custom type hqosMatchVlanID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HqosMatchVlanID_Type.__name__ = "Integer32"
_HqosMatchVlanID_Object = MibTableColumn
hqosMatchVlanID = _HqosMatchVlanID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 5),
    _HqosMatchVlanID_Type()
)
hqosMatchVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchVlanID.setStatus("current")


class _HqosMatchPhb_Type(Integer32):
    """Custom type hqosMatchPhb based on Integer32"""
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
        *(("be", 0),
          ("af1", 1),
          ("af2", 2),
          ("af3", 3),
          ("af4", 4),
          ("ef", 5),
          ("cs6", 6),
          ("cs7", 7),
          ("notconfig", 8))
    )


_HqosMatchPhb_Type.__name__ = "Integer32"
_HqosMatchPhb_Object = MibTableColumn
hqosMatchPhb = _HqosMatchPhb_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 6),
    _HqosMatchPhb_Type()
)
hqosMatchPhb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchPhb.setStatus("current")


class _HqosMatchSvlan_Type(Integer32):
    """Custom type hqosMatchSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HqosMatchSvlan_Type.__name__ = "Integer32"
_HqosMatchSvlan_Object = MibTableColumn
hqosMatchSvlan = _HqosMatchSvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 7),
    _HqosMatchSvlan_Type()
)
hqosMatchSvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchSvlan.setStatus("current")


class _HqosMatchCvlan_Type(Integer32):
    """Custom type hqosMatchCvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_HqosMatchCvlan_Type.__name__ = "Integer32"
_HqosMatchCvlan_Object = MibTableColumn
hqosMatchCvlan = _HqosMatchCvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 2, 1, 8),
    _HqosMatchCvlan_Type()
)
hqosMatchCvlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosMatchCvlan.setStatus("current")
_HqosWredTable_Object = MibTable
hqosWredTable = _HqosWredTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 3)
)
if mibBuilder.loadTexts:
    hqosWredTable.setStatus("current")
_HqosWredEntry_Object = MibTableRow
hqosWredEntry = _HqosWredEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 3, 1)
)
hqosWredEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosWredProfileName"),
)
if mibBuilder.loadTexts:
    hqosWredEntry.setStatus("current")


class _HqosWredProfileName_Type(DisplayString):
    """Custom type hqosWredProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosWredProfileName_Type.__name__ = "DisplayString"
_HqosWredProfileName_Object = MibTableColumn
hqosWredProfileName = _HqosWredProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 3, 1, 1),
    _HqosWredProfileName_Type()
)
hqosWredProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWredProfileName.setStatus("current")


class _HqosWredLevelID_Type(Integer32):
    """Custom type hqosWredLevelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HqosWredLevelID_Type.__name__ = "Integer32"
_HqosWredLevelID_Object = MibTableColumn
hqosWredLevelID = _HqosWredLevelID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 3, 1, 2),
    _HqosWredLevelID_Type()
)
hqosWredLevelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWredLevelID.setStatus("current")
_HqosWredColorTable_Object = MibTable
hqosWredColorTable = _HqosWredColorTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 4)
)
if mibBuilder.loadTexts:
    hqosWredColorTable.setStatus("current")
_HqosWredColorEntry_Object = MibTableRow
hqosWredColorEntry = _HqosWredColorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 4, 1)
)
hqosWredColorEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosWredProfileName"),
    (0, "HQOS-MIB", "hqosWredColor"),
)
if mibBuilder.loadTexts:
    hqosWredColorEntry.setStatus("current")


class _HqosWredColor_Type(Integer32):
    """Custom type hqosWredColor based on Integer32"""
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
        *(("red", 1),
          ("yellow", 2),
          ("green", 3),
          ("notconfig", 4))
    )


_HqosWredColor_Type.__name__ = "Integer32"
_HqosWredColor_Object = MibTableColumn
hqosWredColor = _HqosWredColor_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 4, 1, 1),
    _HqosWredColor_Type()
)
hqosWredColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWredColor.setStatus("current")


class _HqosWredMin_Type(Integer32):
    """Custom type hqosWredMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_HqosWredMin_Type.__name__ = "Integer32"
_HqosWredMin_Object = MibTableColumn
hqosWredMin = _HqosWredMin_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 4, 1, 2),
    _HqosWredMin_Type()
)
hqosWredMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWredMin.setStatus("current")


class _HqosWredMax_Type(Integer32):
    """Custom type hqosWredMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_HqosWredMax_Type.__name__ = "Integer32"
_HqosWredMax_Object = MibTableColumn
hqosWredMax = _HqosWredMax_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 4, 1, 3),
    _HqosWredMax_Type()
)
hqosWredMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWredMax.setStatus("current")


class _HqosWredPercent_Type(Integer32):
    """Custom type hqosWredPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HqosWredPercent_Type.__name__ = "Integer32"
_HqosWredPercent_Object = MibTableColumn
hqosWredPercent = _HqosWredPercent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 4, 1, 4),
    _HqosWredPercent_Type()
)
hqosWredPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWredPercent.setStatus("current")
_HqosWfqTable_Object = MibTable
hqosWfqTable = _HqosWfqTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 5)
)
if mibBuilder.loadTexts:
    hqosWfqTable.setStatus("current")
_HqosWfqEntry_Object = MibTableRow
hqosWfqEntry = _HqosWfqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 5, 1)
)
hqosWfqEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosWfqProfileName"),
)
if mibBuilder.loadTexts:
    hqosWfqEntry.setStatus("current")


class _HqosWfqProfileName_Type(DisplayString):
    """Custom type hqosWfqProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosWfqProfileName_Type.__name__ = "DisplayString"
_HqosWfqProfileName_Object = MibTableColumn
hqosWfqProfileName = _HqosWfqProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 5, 1, 1),
    _HqosWfqProfileName_Type()
)
hqosWfqProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWfqProfileName.setStatus("current")


class _HqosWfqLevelID_Type(Integer32):
    """Custom type hqosWfqLevelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HqosWfqLevelID_Type.__name__ = "Integer32"
_HqosWfqLevelID_Object = MibTableColumn
hqosWfqLevelID = _HqosWfqLevelID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 5, 1, 2),
    _HqosWfqLevelID_Type()
)
hqosWfqLevelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWfqLevelID.setStatus("current")


class _HqosWfqWeight_Type(Integer32):
    """Custom type hqosWfqWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HqosWfqWeight_Type.__name__ = "Integer32"
_HqosWfqWeight_Object = MibTableColumn
hqosWfqWeight = _HqosWfqWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 5, 1, 3),
    _HqosWfqWeight_Type()
)
hqosWfqWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosWfqWeight.setStatus("current")
_HqosShapingTable_Object = MibTable
hqosShapingTable = _HqosShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6)
)
if mibBuilder.loadTexts:
    hqosShapingTable.setStatus("current")
_HqosShapingEntry_Object = MibTableRow
hqosShapingEntry = _HqosShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6, 1)
)
hqosShapingEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosShapingProfileName"),
)
if mibBuilder.loadTexts:
    hqosShapingEntry.setStatus("current")


class _HqosShapingProfileName_Type(DisplayString):
    """Custom type hqosShapingProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosShapingProfileName_Type.__name__ = "DisplayString"
_HqosShapingProfileName_Object = MibTableColumn
hqosShapingProfileName = _HqosShapingProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6, 1, 1),
    _HqosShapingProfileName_Type()
)
hqosShapingProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosShapingProfileName.setStatus("current")


class _HqosShapingLevelID_Type(Integer32):
    """Custom type hqosShapingLevelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4),
    )


_HqosShapingLevelID_Type.__name__ = "Integer32"
_HqosShapingLevelID_Object = MibTableColumn
hqosShapingLevelID = _HqosShapingLevelID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6, 1, 2),
    _HqosShapingLevelID_Type()
)
hqosShapingLevelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosShapingLevelID.setStatus("current")


class _HqosShapingCir_Type(Integer32):
    """Custom type hqosShapingCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 10000000),
    )


_HqosShapingCir_Type.__name__ = "Integer32"
_HqosShapingCir_Object = MibTableColumn
hqosShapingCir = _HqosShapingCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6, 1, 3),
    _HqosShapingCir_Type()
)
hqosShapingCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosShapingCir.setStatus("current")


class _HqosShapingCbs_Type(Integer32):
    """Custom type hqosShapingCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 16711680),
    )


_HqosShapingCbs_Type.__name__ = "Integer32"
_HqosShapingCbs_Object = MibTableColumn
hqosShapingCbs = _HqosShapingCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6, 1, 4),
    _HqosShapingCbs_Type()
)
hqosShapingCbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosShapingCbs.setStatus("current")


class _HqosShapingPir_Type(Integer32):
    """Custom type hqosShapingPir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(180, 10000000),
    )


_HqosShapingPir_Type.__name__ = "Integer32"
_HqosShapingPir_Object = MibTableColumn
hqosShapingPir = _HqosShapingPir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6, 1, 5),
    _HqosShapingPir_Type()
)
hqosShapingPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosShapingPir.setStatus("current")


class _HqosShapingPbs_Type(Integer32):
    """Custom type hqosShapingPbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 16711680),
    )


_HqosShapingPbs_Type.__name__ = "Integer32"
_HqosShapingPbs_Object = MibTableColumn
hqosShapingPbs = _HqosShapingPbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 6, 1, 6),
    _HqosShapingPbs_Type()
)
hqosShapingPbs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosShapingPbs.setStatus("current")
_HqosPriorityTable_Object = MibTable
hqosPriorityTable = _HqosPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 7)
)
if mibBuilder.loadTexts:
    hqosPriorityTable.setStatus("current")
_HqosPriorityEntry_Object = MibTableRow
hqosPriorityEntry = _HqosPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 7, 1)
)
hqosPriorityEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosPriorityProfileName"),
)
if mibBuilder.loadTexts:
    hqosPriorityEntry.setStatus("current")


class _HqosPriorityProfileName_Type(DisplayString):
    """Custom type hqosPriorityProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosPriorityProfileName_Type.__name__ = "DisplayString"
_HqosPriorityProfileName_Object = MibTableColumn
hqosPriorityProfileName = _HqosPriorityProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 7, 1, 1),
    _HqosPriorityProfileName_Type()
)
hqosPriorityProfileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosPriorityProfileName.setStatus("current")
_HqosPriorityFlowTable_Object = MibTable
hqosPriorityFlowTable = _HqosPriorityFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 8)
)
if mibBuilder.loadTexts:
    hqosPriorityFlowTable.setStatus("current")
_HqosPriorityFlowEntry_Object = MibTableRow
hqosPriorityFlowEntry = _HqosPriorityFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 8, 1)
)
hqosPriorityFlowEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosPriorityProfileName"),
    (0, "HQOS-MIB", "hqosPriorityFlowClass"),
)
if mibBuilder.loadTexts:
    hqosPriorityFlowEntry.setStatus("current")


class _HqosPriorityFlowClass_Type(Integer32):
    """Custom type hqosPriorityFlowClass based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("be", 0),
          ("af1", 1),
          ("af2", 2),
          ("af3", 3),
          ("af4", 4),
          ("ef", 5),
          ("cs6", 6),
          ("cs7", 7))
    )


_HqosPriorityFlowClass_Type.__name__ = "Integer32"
_HqosPriorityFlowClass_Object = MibTableColumn
hqosPriorityFlowClass = _HqosPriorityFlowClass_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 8, 1, 1),
    _HqosPriorityFlowClass_Type()
)
hqosPriorityFlowClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosPriorityFlowClass.setStatus("current")


class _HqosPriorityMode_Type(Integer32):
    """Custom type hqosPriorityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("single", 0),
          ("dual", 1))
    )


_HqosPriorityMode_Type.__name__ = "Integer32"
_HqosPriorityMode_Object = MibTableColumn
hqosPriorityMode = _HqosPriorityMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 8, 1, 2),
    _HqosPriorityMode_Type()
)
hqosPriorityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosPriorityMode.setStatus("current")


class _HqosPriorityGreen_Type(DisplayString):
    """Custom type hqosPriorityGreen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosPriorityGreen_Type.__name__ = "DisplayString"
_HqosPriorityGreen_Object = MibTableColumn
hqosPriorityGreen = _HqosPriorityGreen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 8, 1, 3),
    _HqosPriorityGreen_Type()
)
hqosPriorityGreen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosPriorityGreen.setStatus("current")


class _HqosPriorityYellow_Type(DisplayString):
    """Custom type hqosPriorityYellow based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosPriorityYellow_Type.__name__ = "DisplayString"
_HqosPriorityYellow_Object = MibTableColumn
hqosPriorityYellow = _HqosPriorityYellow_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 8, 1, 4),
    _HqosPriorityYellow_Type()
)
hqosPriorityYellow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosPriorityYellow.setStatus("current")
_HqosHQosTable_Object = MibTable
hqosHQosTable = _HqosHQosTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 9)
)
if mibBuilder.loadTexts:
    hqosHQosTable.setStatus("current")
_HqosHQosEntry_Object = MibTableRow
hqosHQosEntry = _HqosHQosEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 9, 1)
)
hqosHQosEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosHQosPolicyName"),
)
if mibBuilder.loadTexts:
    hqosHQosEntry.setStatus("current")


class _HqosHQosPolicyName_Type(DisplayString):
    """Custom type hqosHQosPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosPolicyName_Type.__name__ = "DisplayString"
_HqosHQosPolicyName_Object = MibTableColumn
hqosHQosPolicyName = _HqosHQosPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 9, 1, 1),
    _HqosHQosPolicyName_Type()
)
hqosHQosPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosPolicyName.setStatus("current")


class _HqosHQosLevelID_Type(Integer32):
    """Custom type hqosHQosLevelID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HqosHQosLevelID_Type.__name__ = "Integer32"
_HqosHQosLevelID_Object = MibTableColumn
hqosHQosLevelID = _HqosHQosLevelID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 9, 1, 2),
    _HqosHQosLevelID_Type()
)
hqosHQosLevelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosLevelID.setStatus("current")


class _HqosHQosMode_Type(Integer32):
    """Custom type hqosHQosMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlan", 1),
          ("svlan", 2))
    )


_HqosHQosMode_Type.__name__ = "Integer32"
_HqosHQosMode_Object = MibTableColumn
hqosHQosMode = _HqosHQosMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 9, 1, 3),
    _HqosHQosMode_Type()
)
hqosHQosMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosMode.setStatus("current")


class _HqosHQosDiscripString_Type(DisplayString):
    """Custom type hqosHQosDiscripString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 200),
    )


_HqosHQosDiscripString_Type.__name__ = "DisplayString"
_HqosHQosDiscripString_Object = MibTableColumn
hqosHQosDiscripString = _HqosHQosDiscripString_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 9, 1, 4),
    _HqosHQosDiscripString_Type()
)
hqosHQosDiscripString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosDiscripString.setStatus("current")
_HqosHQosFlowTable_Object = MibTable
hqosHQosFlowTable = _HqosHQosFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10)
)
if mibBuilder.loadTexts:
    hqosHQosFlowTable.setStatus("current")
_HqosHQosFlowEntry_Object = MibTableRow
hqosHQosFlowEntry = _HqosHQosFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1)
)
hqosHQosFlowEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosHQosPolicyName"),
    (0, "HQOS-MIB", "hqosHQosFlowClassName"),
)
if mibBuilder.loadTexts:
    hqosHQosFlowEntry.setStatus("current")


class _HqosHQosFlowClassName_Type(DisplayString):
    """Custom type hqosHQosFlowClassName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosFlowClassName_Type.__name__ = "DisplayString"
_HqosHQosFlowClassName_Object = MibTableColumn
hqosHQosFlowClassName = _HqosHQosFlowClassName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1, 1),
    _HqosHQosFlowClassName_Type()
)
hqosHQosFlowClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosFlowClassName.setStatus("current")


class _HqosHQosFlowPriority_Type(DisplayString):
    """Custom type hqosHQosFlowPriority based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosFlowPriority_Type.__name__ = "DisplayString"
_HqosHQosFlowPriority_Object = MibTableColumn
hqosHQosFlowPriority = _HqosHQosFlowPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1, 2),
    _HqosHQosFlowPriority_Type()
)
hqosHQosFlowPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosFlowPriority.setStatus("current")


class _HqosHQosFlowWredProfName_Type(DisplayString):
    """Custom type hqosHQosFlowWredProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosFlowWredProfName_Type.__name__ = "DisplayString"
_HqosHQosFlowWredProfName_Object = MibTableColumn
hqosHQosFlowWredProfName = _HqosHQosFlowWredProfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1, 3),
    _HqosHQosFlowWredProfName_Type()
)
hqosHQosFlowWredProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosFlowWredProfName.setStatus("current")


class _HqosHQosFlowWfqProfName_Type(DisplayString):
    """Custom type hqosHQosFlowWfqProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosFlowWfqProfName_Type.__name__ = "DisplayString"
_HqosHQosFlowWfqProfName_Object = MibTableColumn
hqosHQosFlowWfqProfName = _HqosHQosFlowWfqProfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1, 4),
    _HqosHQosFlowWfqProfName_Type()
)
hqosHQosFlowWfqProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosFlowWfqProfName.setStatus("current")


class _HqosHQosFlowShapingProfName_Type(DisplayString):
    """Custom type hqosHQosFlowShapingProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosFlowShapingProfName_Type.__name__ = "DisplayString"
_HqosHQosFlowShapingProfName_Object = MibTableColumn
hqosHQosFlowShapingProfName = _HqosHQosFlowShapingProfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1, 5),
    _HqosHQosFlowShapingProfName_Type()
)
hqosHQosFlowShapingProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosFlowShapingProfName.setStatus("current")


class _HqosHQosFlowPriorityProfName_Type(DisplayString):
    """Custom type hqosHQosFlowPriorityProfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosFlowPriorityProfName_Type.__name__ = "DisplayString"
_HqosHQosFlowPriorityProfName_Object = MibTableColumn
hqosHQosFlowPriorityProfName = _HqosHQosFlowPriorityProfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1, 6),
    _HqosHQosFlowPriorityProfName_Type()
)
hqosHQosFlowPriorityProfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosFlowPriorityProfName.setStatus("current")


class _HqosHQosSubPolicyName_Type(DisplayString):
    """Custom type hqosHQosSubPolicyName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosSubPolicyName_Type.__name__ = "DisplayString"
_HqosHQosSubPolicyName_Object = MibTableColumn
hqosHQosSubPolicyName = _HqosHQosSubPolicyName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 10, 1, 7),
    _HqosHQosSubPolicyName_Type()
)
hqosHQosSubPolicyName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosSubPolicyName.setStatus("current")
_HqosHQosInterfaceTable_Object = MibTable
hqosHQosInterfaceTable = _HqosHQosInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 11)
)
if mibBuilder.loadTexts:
    hqosHQosInterfaceTable.setStatus("current")
_HqosHQosInterfaceEntry_Object = MibTableRow
hqosHQosInterfaceEntry = _HqosHQosInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 11, 1)
)
hqosHQosInterfaceEntry.setIndexNames(
    (0, "HQOS-MIB", "hqosHQosInterface"),
)
if mibBuilder.loadTexts:
    hqosHQosInterfaceEntry.setStatus("current")


class _HqosHQosInterface_Type(DisplayString):
    """Custom type hqosHQosInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosInterface_Type.__name__ = "DisplayString"
_HqosHQosInterface_Object = MibTableColumn
hqosHQosInterface = _HqosHQosInterface_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 11, 1, 1),
    _HqosHQosInterface_Type()
)
hqosHQosInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosInterface.setStatus("current")


class _HqosHQosPolicyNameIN_Type(DisplayString):
    """Custom type hqosHQosPolicyNameIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosPolicyNameIN_Type.__name__ = "DisplayString"
_HqosHQosPolicyNameIN_Object = MibTableColumn
hqosHQosPolicyNameIN = _HqosHQosPolicyNameIN_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 11, 1, 2),
    _HqosHQosPolicyNameIN_Type()
)
hqosHQosPolicyNameIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosPolicyNameIN.setStatus("current")


class _HqosInterfaceShapingIN_Type(DisplayString):
    """Custom type hqosInterfaceShapingIN based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosInterfaceShapingIN_Type.__name__ = "DisplayString"
_HqosInterfaceShapingIN_Object = MibTableColumn
hqosInterfaceShapingIN = _HqosInterfaceShapingIN_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 11, 1, 3),
    _HqosInterfaceShapingIN_Type()
)
hqosInterfaceShapingIN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosInterfaceShapingIN.setStatus("current")


class _HqosHQosPolicyNameOUT_Type(DisplayString):
    """Custom type hqosHQosPolicyNameOUT based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosHQosPolicyNameOUT_Type.__name__ = "DisplayString"
_HqosHQosPolicyNameOUT_Object = MibTableColumn
hqosHQosPolicyNameOUT = _HqosHQosPolicyNameOUT_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 11, 1, 4),
    _HqosHQosPolicyNameOUT_Type()
)
hqosHQosPolicyNameOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosHQosPolicyNameOUT.setStatus("current")


class _HqosInterfaceShapingOUT_Type(DisplayString):
    """Custom type hqosInterfaceShapingOUT based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HqosInterfaceShapingOUT_Type.__name__ = "DisplayString"
_HqosInterfaceShapingOUT_Object = MibTableColumn
hqosInterfaceShapingOUT = _HqosInterfaceShapingOUT_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 102, 16, 11, 1, 5),
    _HqosInterfaceShapingOUT_Type()
)
hqosInterfaceShapingOUT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hqosInterfaceShapingOUT.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HQOS-MIB",
    **{"hqos": hqos,
       "hqosFlowClassTable": hqosFlowClassTable,
       "hqosFlowClassEntry": hqosFlowClassEntry,
       "hqosFlowClassName": hqosFlowClassName,
       "hqosFlowMatchTable": hqosFlowMatchTable,
       "hqosFlowMatchEntry": hqosFlowMatchEntry,
       "hqosMatchFlowclass": hqosMatchFlowclass,
       "hqosMatchType": hqosMatchType,
       "hqosMatchAclNo": hqosMatchAclNo,
       "hqosMatchRuleNo": hqosMatchRuleNo,
       "hqosMatchVlanID": hqosMatchVlanID,
       "hqosMatchPhb": hqosMatchPhb,
       "hqosMatchSvlan": hqosMatchSvlan,
       "hqosMatchCvlan": hqosMatchCvlan,
       "hqosWredTable": hqosWredTable,
       "hqosWredEntry": hqosWredEntry,
       "hqosWredProfileName": hqosWredProfileName,
       "hqosWredLevelID": hqosWredLevelID,
       "hqosWredColorTable": hqosWredColorTable,
       "hqosWredColorEntry": hqosWredColorEntry,
       "hqosWredColor": hqosWredColor,
       "hqosWredMin": hqosWredMin,
       "hqosWredMax": hqosWredMax,
       "hqosWredPercent": hqosWredPercent,
       "hqosWfqTable": hqosWfqTable,
       "hqosWfqEntry": hqosWfqEntry,
       "hqosWfqProfileName": hqosWfqProfileName,
       "hqosWfqLevelID": hqosWfqLevelID,
       "hqosWfqWeight": hqosWfqWeight,
       "hqosShapingTable": hqosShapingTable,
       "hqosShapingEntry": hqosShapingEntry,
       "hqosShapingProfileName": hqosShapingProfileName,
       "hqosShapingLevelID": hqosShapingLevelID,
       "hqosShapingCir": hqosShapingCir,
       "hqosShapingCbs": hqosShapingCbs,
       "hqosShapingPir": hqosShapingPir,
       "hqosShapingPbs": hqosShapingPbs,
       "hqosPriorityTable": hqosPriorityTable,
       "hqosPriorityEntry": hqosPriorityEntry,
       "hqosPriorityProfileName": hqosPriorityProfileName,
       "hqosPriorityFlowTable": hqosPriorityFlowTable,
       "hqosPriorityFlowEntry": hqosPriorityFlowEntry,
       "hqosPriorityFlowClass": hqosPriorityFlowClass,
       "hqosPriorityMode": hqosPriorityMode,
       "hqosPriorityGreen": hqosPriorityGreen,
       "hqosPriorityYellow": hqosPriorityYellow,
       "hqosHQosTable": hqosHQosTable,
       "hqosHQosEntry": hqosHQosEntry,
       "hqosHQosPolicyName": hqosHQosPolicyName,
       "hqosHQosLevelID": hqosHQosLevelID,
       "hqosHQosMode": hqosHQosMode,
       "hqosHQosDiscripString": hqosHQosDiscripString,
       "hqosHQosFlowTable": hqosHQosFlowTable,
       "hqosHQosFlowEntry": hqosHQosFlowEntry,
       "hqosHQosFlowClassName": hqosHQosFlowClassName,
       "hqosHQosFlowPriority": hqosHQosFlowPriority,
       "hqosHQosFlowWredProfName": hqosHQosFlowWredProfName,
       "hqosHQosFlowWfqProfName": hqosHQosFlowWfqProfName,
       "hqosHQosFlowShapingProfName": hqosHQosFlowShapingProfName,
       "hqosHQosFlowPriorityProfName": hqosHQosFlowPriorityProfName,
       "hqosHQosSubPolicyName": hqosHQosSubPolicyName,
       "hqosHQosInterfaceTable": hqosHQosInterfaceTable,
       "hqosHQosInterfaceEntry": hqosHQosInterfaceEntry,
       "hqosHQosInterface": hqosHQosInterface,
       "hqosHQosPolicyNameIN": hqosHQosPolicyNameIN,
       "hqosInterfaceShapingIN": hqosInterfaceShapingIN,
       "hqosHQosPolicyNameOUT": hqosHQosPolicyNameOUT,
       "hqosInterfaceShapingOUT": hqosInterfaceShapingOUT}
)
