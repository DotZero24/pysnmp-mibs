# SNMP MIB module (H3C-FC-ZONE-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FC-ZONE-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:51 2025
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

(H3cFcNameId,) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcNameId")

(h3cSan,
 h3cVsanIndex) = mibBuilder.importSymbols(
    "H3C-VSAN-MIB",
    "h3cSan",
    "h3cVsanIndex")

(ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(t11ZsActiveZoneIndex,
 t11ZsActiveZoneMemberIndex) = mibBuilder.importSymbols(
    "T11-FC-ZONE-SERVER-MIB",
    "t11ZsActiveZoneIndex",
    "t11ZsActiveZoneMemberIndex")


# MODULE-IDENTITY

h3cFcZoneServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9)
)
if mibBuilder.loadTexts:
    h3cFcZoneServer.setRevisions(
        ("2013-12-25 15:07",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cFcZsGenName(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class H3cFcZsGenNameOrZero(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



class H3cFcZsZoneMemberType(TextualConvention, Integer32):
    status = "current"
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
        *(("fcid", 1),
          ("fwwn", 2),
          ("pwwn", 3),
          ("aliasName", 4))
    )



# MIB Managed Objects in the order of their OIDs

_H3cFcZoneMibObjects_ObjectIdentity = ObjectIdentity
h3cFcZoneMibObjects = _H3cFcZoneMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1)
)
_H3cFcZsConfiguration_ObjectIdentity = ObjectIdentity
h3cFcZsConfiguration = _H3cFcZsConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1)
)
_H3cFcZsServerTable_Object = MibTable
h3cFcZsServerTable = _H3cFcZsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFcZsServerTable.setStatus("current")
_H3cFcZsServerEntry_Object = MibTableRow
h3cFcZsServerEntry = _H3cFcZsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1, 1)
)
h3cFcZsServerEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsServerEntry.setStatus("current")


class _H3cFcZsZoneModeCfg_Type(Integer32):
    """Custom type h3cFcZsZoneModeCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("basic", 1),
          ("enhanced", 2))
    )


_H3cFcZsZoneModeCfg_Type.__name__ = "Integer32"
_H3cFcZsZoneModeCfg_Object = MibTableColumn
h3cFcZsZoneModeCfg = _H3cFcZsZoneModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1, 1, 1),
    _H3cFcZsZoneModeCfg_Type()
)
h3cFcZsZoneModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsZoneModeCfg.setStatus("current")
_H3cFcZsHardZoneEnable_Type = TruthValue
_H3cFcZsHardZoneEnable_Object = MibTableColumn
h3cFcZsHardZoneEnable = _H3cFcZsHardZoneEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1, 1, 2),
    _H3cFcZsHardZoneEnable_Type()
)
h3cFcZsHardZoneEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsHardZoneEnable.setStatus("current")


class _H3cFcZsDistributeRule_Type(Integer32):
    """Custom type h3cFcZsDistributeRule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("activeOnly", 2),
          ("full", 3))
    )


_H3cFcZsDistributeRule_Type.__name__ = "Integer32"
_H3cFcZsDistributeRule_Object = MibTableColumn
h3cFcZsDistributeRule = _H3cFcZsDistributeRule_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1, 1, 3),
    _H3cFcZsDistributeRule_Type()
)
h3cFcZsDistributeRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsDistributeRule.setStatus("current")


class _H3cFcZsDefaultZoneSetting_Type(Integer32):
    """Custom type h3cFcZsDefaultZoneSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 1),
          ("permit", 2))
    )


_H3cFcZsDefaultZoneSetting_Type.__name__ = "Integer32"
_H3cFcZsDefaultZoneSetting_Object = MibTableColumn
h3cFcZsDefaultZoneSetting = _H3cFcZsDefaultZoneSetting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1, 1, 4),
    _H3cFcZsDefaultZoneSetting_Type()
)
h3cFcZsDefaultZoneSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsDefaultZoneSetting.setStatus("current")


class _H3cFcZsMergeControlSetting_Type(Integer32):
    """Custom type h3cFcZsMergeControlSetting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("allow", 2),
          ("restrict", 3))
    )


_H3cFcZsMergeControlSetting_Type.__name__ = "Integer32"
_H3cFcZsMergeControlSetting_Object = MibTableColumn
h3cFcZsMergeControlSetting = _H3cFcZsMergeControlSetting_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1, 1, 5),
    _H3cFcZsMergeControlSetting_Type()
)
h3cFcZsMergeControlSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsMergeControlSetting.setStatus("current")


class _H3cFcZsServerLastResult_Type(Integer32):
    """Custom type h3cFcZsServerLastResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("none", 1),
          ("success", 2),
          ("busy", 3),
          ("noSupportInFabric", 4),
          ("noSupportInBasic", 5),
          ("noSupportInEnhanced", 6),
          ("activeZoneSetTooBig", 7),
          ("otherFault", 8))
    )


_H3cFcZsServerLastResult_Type.__name__ = "Integer32"
_H3cFcZsServerLastResult_Object = MibTableColumn
h3cFcZsServerLastResult = _H3cFcZsServerLastResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 1, 1, 6),
    _H3cFcZsServerLastResult_Type()
)
h3cFcZsServerLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsServerLastResult.setStatus("current")
_H3cFcZsZonesetTable_Object = MibTable
h3cFcZsZonesetTable = _H3cFcZsZonesetTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cFcZsZonesetTable.setStatus("current")
_H3cFcZsZonesetEntry_Object = MibTableRow
h3cFcZsZonesetEntry = _H3cFcZsZonesetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 2, 1)
)
h3cFcZsZonesetEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZonesetIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsZonesetEntry.setStatus("current")


class _H3cFcZsZonesetIndex_Type(Unsigned32):
    """Custom type h3cFcZsZonesetIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZonesetIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZonesetIndex_Object = MibTableColumn
h3cFcZsZonesetIndex = _H3cFcZsZonesetIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 2, 1, 1),
    _H3cFcZsZonesetIndex_Type()
)
h3cFcZsZonesetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcZsZonesetIndex.setStatus("current")
_H3cFcZsZonesetName_Type = H3cFcZsGenName
_H3cFcZsZonesetName_Object = MibTableColumn
h3cFcZsZonesetName = _H3cFcZsZonesetName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 2, 1, 2),
    _H3cFcZsZonesetName_Type()
)
h3cFcZsZonesetName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZonesetName.setStatus("current")
_H3cFcZsZonesetRowStatus_Type = RowStatus
_H3cFcZsZonesetRowStatus_Object = MibTableColumn
h3cFcZsZonesetRowStatus = _H3cFcZsZonesetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 2, 1, 3),
    _H3cFcZsZonesetRowStatus_Type()
)
h3cFcZsZonesetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZonesetRowStatus.setStatus("current")
_H3cFcZsZoneTable_Object = MibTable
h3cFcZsZoneTable = _H3cFcZsZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cFcZsZoneTable.setStatus("current")
_H3cFcZsZoneEntry_Object = MibTableRow
h3cFcZsZoneEntry = _H3cFcZsZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 3, 1)
)
h3cFcZsZoneEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsZoneEntry.setStatus("current")


class _H3cFcZsZoneIndex_Type(Unsigned32):
    """Custom type h3cFcZsZoneIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZoneIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZoneIndex_Object = MibTableColumn
h3cFcZsZoneIndex = _H3cFcZsZoneIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 3, 1, 1),
    _H3cFcZsZoneIndex_Type()
)
h3cFcZsZoneIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcZsZoneIndex.setStatus("current")
_H3cFcZsZoneName_Type = H3cFcZsGenName
_H3cFcZsZoneName_Object = MibTableColumn
h3cFcZsZoneName = _H3cFcZsZoneName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 3, 1, 2),
    _H3cFcZsZoneName_Type()
)
h3cFcZsZoneName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneName.setStatus("current")


class _H3cFcZsZonePairwiseEnable_Type(TruthValue):
    """Custom type h3cFcZsZonePairwiseEnable based on TruthValue"""
    defaultValue = 2


_H3cFcZsZonePairwiseEnable_Type.__name__ = "TruthValue"
_H3cFcZsZonePairwiseEnable_Object = MibTableColumn
h3cFcZsZonePairwiseEnable = _H3cFcZsZonePairwiseEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 3, 1, 3),
    _H3cFcZsZonePairwiseEnable_Type()
)
h3cFcZsZonePairwiseEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZonePairwiseEnable.setStatus("current")
_H3cFcZsZoneRowStatus_Type = RowStatus
_H3cFcZsZoneRowStatus_Object = MibTableColumn
h3cFcZsZoneRowStatus = _H3cFcZsZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 3, 1, 4),
    _H3cFcZsZoneRowStatus_Type()
)
h3cFcZsZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneRowStatus.setStatus("current")
_H3cFcZsSetZoneTable_Object = MibTable
h3cFcZsSetZoneTable = _H3cFcZsSetZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 4)
)
if mibBuilder.loadTexts:
    h3cFcZsSetZoneTable.setStatus("current")
_H3cFcZsSetZoneEntry_Object = MibTableRow
h3cFcZsSetZoneEntry = _H3cFcZsSetZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 4, 1)
)
h3cFcZsSetZoneEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZonesetIndex"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsSetZoneEntry.setStatus("current")
_H3cFcZsSetZoneRowStatus_Type = RowStatus
_H3cFcZsSetZoneRowStatus_Object = MibTableColumn
h3cFcZsSetZoneRowStatus = _H3cFcZsSetZoneRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 4, 1, 1),
    _H3cFcZsSetZoneRowStatus_Type()
)
h3cFcZsSetZoneRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsSetZoneRowStatus.setStatus("current")
_H3cFcZsZoneAliasTable_Object = MibTable
h3cFcZsZoneAliasTable = _H3cFcZsZoneAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 5)
)
if mibBuilder.loadTexts:
    h3cFcZsZoneAliasTable.setStatus("current")
_H3cFcZsZoneAliasEntry_Object = MibTableRow
h3cFcZsZoneAliasEntry = _H3cFcZsZoneAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 5, 1)
)
h3cFcZsZoneAliasEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneAliasIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsZoneAliasEntry.setStatus("current")


class _H3cFcZsZoneAliasIndex_Type(Unsigned32):
    """Custom type h3cFcZsZoneAliasIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZoneAliasIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZoneAliasIndex_Object = MibTableColumn
h3cFcZsZoneAliasIndex = _H3cFcZsZoneAliasIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 5, 1, 1),
    _H3cFcZsZoneAliasIndex_Type()
)
h3cFcZsZoneAliasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcZsZoneAliasIndex.setStatus("current")
_H3cFcZsZoneAliasName_Type = H3cFcZsGenName
_H3cFcZsZoneAliasName_Object = MibTableColumn
h3cFcZsZoneAliasName = _H3cFcZsZoneAliasName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 5, 1, 2),
    _H3cFcZsZoneAliasName_Type()
)
h3cFcZsZoneAliasName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneAliasName.setStatus("current")
_H3cFcZsZoneAliasRowStatus_Type = RowStatus
_H3cFcZsZoneAliasRowStatus_Object = MibTableColumn
h3cFcZsZoneAliasRowStatus = _H3cFcZsZoneAliasRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 5, 1, 3),
    _H3cFcZsZoneAliasRowStatus_Type()
)
h3cFcZsZoneAliasRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneAliasRowStatus.setStatus("current")
_H3cFcZsZoneMemberTable_Object = MibTable
h3cFcZsZoneMemberTable = _H3cFcZsZoneMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6)
)
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberTable.setStatus("current")
_H3cFcZsZoneMemberEntry_Object = MibTableRow
h3cFcZsZoneMemberEntry = _H3cFcZsZoneMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1)
)
h3cFcZsZoneMemberEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneMemberParentType"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneMemberParentIndex"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberEntry.setStatus("current")


class _H3cFcZsZoneMemberParentType_Type(Integer32):
    """Custom type h3cFcZsZoneMemberParentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("zone", 1),
          ("alias", 2))
    )


_H3cFcZsZoneMemberParentType_Type.__name__ = "Integer32"
_H3cFcZsZoneMemberParentType_Object = MibTableColumn
h3cFcZsZoneMemberParentType = _H3cFcZsZoneMemberParentType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1, 1),
    _H3cFcZsZoneMemberParentType_Type()
)
h3cFcZsZoneMemberParentType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberParentType.setStatus("current")


class _H3cFcZsZoneMemberParentIndex_Type(Unsigned32):
    """Custom type h3cFcZsZoneMemberParentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZoneMemberParentIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZoneMemberParentIndex_Object = MibTableColumn
h3cFcZsZoneMemberParentIndex = _H3cFcZsZoneMemberParentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1, 2),
    _H3cFcZsZoneMemberParentIndex_Type()
)
h3cFcZsZoneMemberParentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberParentIndex.setStatus("current")


class _H3cFcZsZoneMemberIndex_Type(Unsigned32):
    """Custom type h3cFcZsZoneMemberIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZoneMemberIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZoneMemberIndex_Object = MibTableColumn
h3cFcZsZoneMemberIndex = _H3cFcZsZoneMemberIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1, 3),
    _H3cFcZsZoneMemberIndex_Type()
)
h3cFcZsZoneMemberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberIndex.setStatus("current")
_H3cFcZsZoneMemberFormat_Type = H3cFcZsZoneMemberType
_H3cFcZsZoneMemberFormat_Object = MibTableColumn
h3cFcZsZoneMemberFormat = _H3cFcZsZoneMemberFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1, 4),
    _H3cFcZsZoneMemberFormat_Type()
)
h3cFcZsZoneMemberFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberFormat.setStatus("current")


class _H3cFcZsZoneMemberIdentifier_Type(OctetString):
    """Custom type h3cFcZsZoneMemberIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_H3cFcZsZoneMemberIdentifier_Type.__name__ = "OctetString"
_H3cFcZsZoneMemberIdentifier_Object = MibTableColumn
h3cFcZsZoneMemberIdentifier = _H3cFcZsZoneMemberIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1, 5),
    _H3cFcZsZoneMemberIdentifier_Type()
)
h3cFcZsZoneMemberIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberIdentifier.setStatus("current")


class _H3cFcZsZoneMemberPairwiseRole_Type(Integer32):
    """Custom type h3cFcZsZoneMemberPairwiseRole based on Integer32"""
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
        *(("none", 1),
          ("both", 2),
          ("initiator", 3),
          ("target", 4))
    )


_H3cFcZsZoneMemberPairwiseRole_Type.__name__ = "Integer32"
_H3cFcZsZoneMemberPairwiseRole_Object = MibTableColumn
h3cFcZsZoneMemberPairwiseRole = _H3cFcZsZoneMemberPairwiseRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1, 6),
    _H3cFcZsZoneMemberPairwiseRole_Type()
)
h3cFcZsZoneMemberPairwiseRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberPairwiseRole.setStatus("current")
_H3cFcZsZoneMemberRowStatus_Type = RowStatus
_H3cFcZsZoneMemberRowStatus_Object = MibTableColumn
h3cFcZsZoneMemberRowStatus = _H3cFcZsZoneMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 1, 6, 1, 7),
    _H3cFcZsZoneMemberRowStatus_Type()
)
h3cFcZsZoneMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberRowStatus.setStatus("current")
_H3cFcZsOperation_ObjectIdentity = ObjectIdentity
h3cFcZsOperation = _H3cFcZsOperation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2)
)
_H3cFcZsActivateTable_Object = MibTable
h3cFcZsActivateTable = _H3cFcZsActivateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cFcZsActivateTable.setStatus("current")
_H3cFcZsActivateEntry_Object = MibTableRow
h3cFcZsActivateEntry = _H3cFcZsActivateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 1, 1)
)
h3cFcZsActivateEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsActivateEntry.setStatus("current")
_H3cFcZsActivate_Type = H3cFcZsGenNameOrZero
_H3cFcZsActivate_Object = MibTableColumn
h3cFcZsActivate = _H3cFcZsActivate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 1, 1, 1),
    _H3cFcZsActivate_Type()
)
h3cFcZsActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsActivate.setStatus("current")


class _H3cFcZsDeactivate_Type(Integer32):
    """Custom type h3cFcZsDeactivate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 1),
          ("deactivate", 2))
    )


_H3cFcZsDeactivate_Type.__name__ = "Integer32"
_H3cFcZsDeactivate_Object = MibTableColumn
h3cFcZsDeactivate = _H3cFcZsDeactivate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 1, 1, 2),
    _H3cFcZsDeactivate_Type()
)
h3cFcZsDeactivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsDeactivate.setStatus("current")


class _H3cFcZsActivateResult_Type(Integer32):
    """Custom type h3cFcZsActivateResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("inProgress", 2),
          ("activateSuccess", 3),
          ("activateFailure", 4),
          ("deactivateSuccess", 5),
          ("deactivateFailure", 6))
    )


_H3cFcZsActivateResult_Type.__name__ = "Integer32"
_H3cFcZsActivateResult_Object = MibTableColumn
h3cFcZsActivateResult = _H3cFcZsActivateResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 1, 1, 3),
    _H3cFcZsActivateResult_Type()
)
h3cFcZsActivateResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsActivateResult.setStatus("current")


class _H3cFcZsActivateFailReason_Type(Integer32):
    """Custom type h3cFcZsActivateFailReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("busy", 2),
          ("activeZoneSetTooBig", 3),
          ("noZoneSet", 4),
          ("noMember", 5))
    )


_H3cFcZsActivateFailReason_Type.__name__ = "Integer32"
_H3cFcZsActivateFailReason_Object = MibTableColumn
h3cFcZsActivateFailReason = _H3cFcZsActivateFailReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 1, 1, 4),
    _H3cFcZsActivateFailReason_Type()
)
h3cFcZsActivateFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsActivateFailReason.setStatus("current")
_H3cFcZsDistributeTable_Object = MibTable
h3cFcZsDistributeTable = _H3cFcZsDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cFcZsDistributeTable.setStatus("current")
_H3cFcZsDistributeEntry_Object = MibTableRow
h3cFcZsDistributeEntry = _H3cFcZsDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 2, 1)
)
h3cFcZsDistributeEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsDistributeEntry.setStatus("current")


class _H3cFcZsDistribute_Type(Integer32):
    """Custom type h3cFcZsDistribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 1),
          ("distribute", 2))
    )


_H3cFcZsDistribute_Type.__name__ = "Integer32"
_H3cFcZsDistribute_Object = MibTableColumn
h3cFcZsDistribute = _H3cFcZsDistribute_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 2, 1, 1),
    _H3cFcZsDistribute_Type()
)
h3cFcZsDistribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsDistribute.setStatus("current")


class _H3cFcZsDistributeLastResult_Type(Integer32):
    """Custom type h3cFcZsDistributeLastResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("success", 2),
          ("inProgress", 3),
          ("rejectFailure", 4),
          ("otherFault", 5))
    )


_H3cFcZsDistributeLastResult_Type.__name__ = "Integer32"
_H3cFcZsDistributeLastResult_Object = MibTableColumn
h3cFcZsDistributeLastResult = _H3cFcZsDistributeLastResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 2, 1, 2),
    _H3cFcZsDistributeLastResult_Type()
)
h3cFcZsDistributeLastResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsDistributeLastResult.setStatus("current")
_H3cFcZsDistributeReasonCode_Type = Unsigned32
_H3cFcZsDistributeReasonCode_Object = MibTableColumn
h3cFcZsDistributeReasonCode = _H3cFcZsDistributeReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 2, 1, 3),
    _H3cFcZsDistributeReasonCode_Type()
)
h3cFcZsDistributeReasonCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsDistributeReasonCode.setStatus("current")
_H3cFcZsDistributeExplainCode_Type = Unsigned32
_H3cFcZsDistributeExplainCode_Object = MibTableColumn
h3cFcZsDistributeExplainCode = _H3cFcZsDistributeExplainCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 2, 1, 4),
    _H3cFcZsDistributeExplainCode_Type()
)
h3cFcZsDistributeExplainCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsDistributeExplainCode.setStatus("current")
_H3cFcZsClearDatabaseTable_Object = MibTable
h3cFcZsClearDatabaseTable = _H3cFcZsClearDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cFcZsClearDatabaseTable.setStatus("current")
_H3cFcZsClearDatabaseEntry_Object = MibTableRow
h3cFcZsClearDatabaseEntry = _H3cFcZsClearDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 3, 1)
)
h3cFcZsClearDatabaseEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsClearDatabaseEntry.setStatus("current")


class _H3cFcZsClearDatabase_Type(Integer32):
    """Custom type h3cFcZsClearDatabase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 1),
          ("clearDb", 2))
    )


_H3cFcZsClearDatabase_Type.__name__ = "Integer32"
_H3cFcZsClearDatabase_Object = MibTableColumn
h3cFcZsClearDatabase = _H3cFcZsClearDatabase_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 3, 1, 1),
    _H3cFcZsClearDatabase_Type()
)
h3cFcZsClearDatabase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsClearDatabase.setStatus("current")
_H3cFcZsClearPktStatsTable_Object = MibTable
h3cFcZsClearPktStatsTable = _H3cFcZsClearPktStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cFcZsClearPktStatsTable.setStatus("current")
_H3cFcZsClearPktStatsEntry_Object = MibTableRow
h3cFcZsClearPktStatsEntry = _H3cFcZsClearPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 4, 1)
)
h3cFcZsClearPktStatsEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsClearPktStatsEntry.setStatus("current")


class _H3cFcZsClearPktStats_Type(Integer32):
    """Custom type h3cFcZsClearPktStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 1),
          ("clearStats", 2))
    )


_H3cFcZsClearPktStats_Type.__name__ = "Integer32"
_H3cFcZsClearPktStats_Object = MibTableColumn
h3cFcZsClearPktStats = _H3cFcZsClearPktStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 4, 1, 1),
    _H3cFcZsClearPktStats_Type()
)
h3cFcZsClearPktStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsClearPktStats.setStatus("current")


class _H3cFcZsClearAllPktStats_Type(Integer32):
    """Custom type h3cFcZsClearAllPktStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOper", 1),
          ("clearStats", 2))
    )


_H3cFcZsClearAllPktStats_Type.__name__ = "Integer32"
_H3cFcZsClearAllPktStats_Object = MibScalar
h3cFcZsClearAllPktStats = _H3cFcZsClearAllPktStats_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 2, 5),
    _H3cFcZsClearAllPktStats_Type()
)
h3cFcZsClearAllPktStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsClearAllPktStats.setStatus("current")
_H3cFcZsInformation_ObjectIdentity = ObjectIdentity
h3cFcZsInformation = _H3cFcZsInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3)
)
_H3cFcZsActiveZoneTable_Object = MibTable
h3cFcZsActiveZoneTable = _H3cFcZsActiveZoneTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cFcZsActiveZoneTable.setStatus("current")
_H3cFcZsActiveZoneEntry_Object = MibTableRow
h3cFcZsActiveZoneEntry = _H3cFcZsActiveZoneEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 1, 1)
)
h3cFcZsActiveZoneEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsActiveZoneEntry.setStatus("current")
_H3cFcZsActiveZonePairwiseEnable_Type = TruthValue
_H3cFcZsActiveZonePairwiseEnable_Object = MibTableColumn
h3cFcZsActiveZonePairwiseEnable = _H3cFcZsActiveZonePairwiseEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 1, 1, 1),
    _H3cFcZsActiveZonePairwiseEnable_Type()
)
h3cFcZsActiveZonePairwiseEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsActiveZonePairwiseEnable.setStatus("current")
_H3cFcZsActiveMemberTable_Object = MibTable
h3cFcZsActiveMemberTable = _H3cFcZsActiveMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cFcZsActiveMemberTable.setStatus("current")
_H3cFcZsActiveMemberEntry_Object = MibTableRow
h3cFcZsActiveMemberEntry = _H3cFcZsActiveMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 2, 1)
)
h3cFcZsActiveMemberEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneIndex"),
    (0, "T11-FC-ZONE-SERVER-MIB", "t11ZsActiveZoneMemberIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsActiveMemberEntry.setStatus("current")


class _H3cFcZsActiveMemberPairwiseRole_Type(Integer32):
    """Custom type h3cFcZsActiveMemberPairwiseRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 1),
          ("initiator", 2),
          ("target", 3))
    )


_H3cFcZsActiveMemberPairwiseRole_Type.__name__ = "Integer32"
_H3cFcZsActiveMemberPairwiseRole_Object = MibTableColumn
h3cFcZsActiveMemberPairwiseRole = _H3cFcZsActiveMemberPairwiseRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 2, 1, 1),
    _H3cFcZsActiveMemberPairwiseRole_Type()
)
h3cFcZsActiveMemberPairwiseRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsActiveMemberPairwiseRole.setStatus("current")
_H3cFcZsServerStatusTable_Object = MibTable
h3cFcZsServerStatusTable = _H3cFcZsServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h3cFcZsServerStatusTable.setStatus("current")
_H3cFcZsServerStatusEntry_Object = MibTableRow
h3cFcZsServerStatusEntry = _H3cFcZsServerStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 3, 1)
)
h3cFcZsServerStatusEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsServerStatusEntry.setStatus("current")


class _H3cFcZsServerStatus_Type(Integer32):
    """Custom type h3cFcZsServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("free", 1),
          ("distribute", 2),
          ("merge", 3))
    )


_H3cFcZsServerStatus_Type.__name__ = "Integer32"
_H3cFcZsServerStatus_Object = MibTableColumn
h3cFcZsServerStatus = _H3cFcZsServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 3, 1, 1),
    _H3cFcZsServerStatus_Type()
)
h3cFcZsServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsServerStatus.setStatus("current")


class _H3cFcZsHardZoneStatus_Type(Integer32):
    """Custom type h3cFcZsHardZoneStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("adminDisable", 2),
          ("noResourceDisable", 3))
    )


_H3cFcZsHardZoneStatus_Type.__name__ = "Integer32"
_H3cFcZsHardZoneStatus_Object = MibTableColumn
h3cFcZsHardZoneStatus = _H3cFcZsHardZoneStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 3, 1, 2),
    _H3cFcZsHardZoneStatus_Type()
)
h3cFcZsHardZoneStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsHardZoneStatus.setStatus("current")


class _H3cFcZsAliasCount_Type(Unsigned32):
    """Custom type h3cFcZsAliasCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cFcZsAliasCount_Type.__name__ = "Unsigned32"
_H3cFcZsAliasCount_Object = MibTableColumn
h3cFcZsAliasCount = _H3cFcZsAliasCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 3, 1, 3),
    _H3cFcZsAliasCount_Type()
)
h3cFcZsAliasCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsAliasCount.setStatus("current")


class _H3cFcZsZoneCount_Type(Unsigned32):
    """Custom type h3cFcZsZoneCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cFcZsZoneCount_Type.__name__ = "Unsigned32"
_H3cFcZsZoneCount_Object = MibTableColumn
h3cFcZsZoneCount = _H3cFcZsZoneCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 3, 1, 4),
    _H3cFcZsZoneCount_Type()
)
h3cFcZsZoneCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsZoneCount.setStatus("current")


class _H3cFcZsZonesetCount_Type(Unsigned32):
    """Custom type h3cFcZsZonesetCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_H3cFcZsZonesetCount_Type.__name__ = "Unsigned32"
_H3cFcZsZonesetCount_Object = MibTableColumn
h3cFcZsZonesetCount = _H3cFcZsZonesetCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 3, 1, 5),
    _H3cFcZsZonesetCount_Type()
)
h3cFcZsZonesetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsZonesetCount.setStatus("current")
_H3cFcZsPktStatsTable_Object = MibTable
h3cFcZsPktStatsTable = _H3cFcZsPktStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4)
)
if mibBuilder.loadTexts:
    h3cFcZsPktStatsTable.setStatus("current")
_H3cFcZsPktStatsEntry_Object = MibTableRow
h3cFcZsPktStatsEntry = _H3cFcZsPktStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1)
)
h3cFcZsPktStatsEntry.setIndexNames(
    (0, "H3C-VSAN-MIB", "h3cVsanIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsPktStatsEntry.setStatus("current")
_H3cFcZsPktInMergeReqCount_Type = Counter64
_H3cFcZsPktInMergeReqCount_Object = MibTableColumn
h3cFcZsPktInMergeReqCount = _H3cFcZsPktInMergeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 1),
    _H3cFcZsPktInMergeReqCount_Type()
)
h3cFcZsPktInMergeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktInMergeReqCount.setStatus("current")
_H3cFcZsPktOutMergeReqCount_Type = Counter64
_H3cFcZsPktOutMergeReqCount_Object = MibTableColumn
h3cFcZsPktOutMergeReqCount = _H3cFcZsPktOutMergeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 2),
    _H3cFcZsPktOutMergeReqCount_Type()
)
h3cFcZsPktOutMergeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktOutMergeReqCount.setStatus("current")
_H3cFcZsPktInMergeAccCount_Type = Counter64
_H3cFcZsPktInMergeAccCount_Object = MibTableColumn
h3cFcZsPktInMergeAccCount = _H3cFcZsPktInMergeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 3),
    _H3cFcZsPktInMergeAccCount_Type()
)
h3cFcZsPktInMergeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktInMergeAccCount.setStatus("current")
_H3cFcZsPktOutMergeAccCount_Type = Counter64
_H3cFcZsPktOutMergeAccCount_Object = MibTableColumn
h3cFcZsPktOutMergeAccCount = _H3cFcZsPktOutMergeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 4),
    _H3cFcZsPktOutMergeAccCount_Type()
)
h3cFcZsPktOutMergeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktOutMergeAccCount.setStatus("current")
_H3cFcZsPktInMergeRjtCount_Type = Counter64
_H3cFcZsPktInMergeRjtCount_Object = MibTableColumn
h3cFcZsPktInMergeRjtCount = _H3cFcZsPktInMergeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 5),
    _H3cFcZsPktInMergeRjtCount_Type()
)
h3cFcZsPktInMergeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktInMergeRjtCount.setStatus("current")
_H3cFcZsPktOutMergeRjtCount_Type = Counter64
_H3cFcZsPktOutMergeRjtCount_Object = MibTableColumn
h3cFcZsPktOutMergeRjtCount = _H3cFcZsPktOutMergeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 6),
    _H3cFcZsPktOutMergeRjtCount_Type()
)
h3cFcZsPktOutMergeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktOutMergeRjtCount.setStatus("current")
_H3cFcZsPktInChangeReqCount_Type = Counter64
_H3cFcZsPktInChangeReqCount_Object = MibTableColumn
h3cFcZsPktInChangeReqCount = _H3cFcZsPktInChangeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 7),
    _H3cFcZsPktInChangeReqCount_Type()
)
h3cFcZsPktInChangeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktInChangeReqCount.setStatus("current")
_H3cFcZsPktOutChangeReqCount_Type = Counter64
_H3cFcZsPktOutChangeReqCount_Object = MibTableColumn
h3cFcZsPktOutChangeReqCount = _H3cFcZsPktOutChangeReqCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 8),
    _H3cFcZsPktOutChangeReqCount_Type()
)
h3cFcZsPktOutChangeReqCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktOutChangeReqCount.setStatus("current")
_H3cFcZsPktInChangeAccCount_Type = Counter64
_H3cFcZsPktInChangeAccCount_Object = MibTableColumn
h3cFcZsPktInChangeAccCount = _H3cFcZsPktInChangeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 9),
    _H3cFcZsPktInChangeAccCount_Type()
)
h3cFcZsPktInChangeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktInChangeAccCount.setStatus("current")
_H3cFcZsPktOutChangeAccCount_Type = Counter64
_H3cFcZsPktOutChangeAccCount_Object = MibTableColumn
h3cFcZsPktOutChangeAccCount = _H3cFcZsPktOutChangeAccCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 10),
    _H3cFcZsPktOutChangeAccCount_Type()
)
h3cFcZsPktOutChangeAccCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktOutChangeAccCount.setStatus("current")
_H3cFcZsPktInChangeRjtCount_Type = Counter64
_H3cFcZsPktInChangeRjtCount_Object = MibTableColumn
h3cFcZsPktInChangeRjtCount = _H3cFcZsPktInChangeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 11),
    _H3cFcZsPktInChangeRjtCount_Type()
)
h3cFcZsPktInChangeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktInChangeRjtCount.setStatus("current")
_H3cFcZsPktOutChangeRjtCount_Type = Counter64
_H3cFcZsPktOutChangeRjtCount_Object = MibTableColumn
h3cFcZsPktOutChangeRjtCount = _H3cFcZsPktOutChangeRjtCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 4, 1, 12),
    _H3cFcZsPktOutChangeRjtCount_Type()
)
h3cFcZsPktOutChangeRjtCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsPktOutChangeRjtCount.setStatus("current")
_H3cFcZsNextFreeIndexInfo_ObjectIdentity = ObjectIdentity
h3cFcZsNextFreeIndexInfo = _H3cFcZsNextFreeIndexInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 5)
)


class _H3cFcZsZonesetNextFreeIndex_Type(Unsigned32):
    """Custom type h3cFcZsZonesetNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZonesetNextFreeIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZonesetNextFreeIndex_Object = MibScalar
h3cFcZsZonesetNextFreeIndex = _H3cFcZsZonesetNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 5, 1),
    _H3cFcZsZonesetNextFreeIndex_Type()
)
h3cFcZsZonesetNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsZonesetNextFreeIndex.setStatus("current")


class _H3cFcZsZoneNextFreeIndex_Type(Unsigned32):
    """Custom type h3cFcZsZoneNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZoneNextFreeIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZoneNextFreeIndex_Object = MibScalar
h3cFcZsZoneNextFreeIndex = _H3cFcZsZoneNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 5, 2),
    _H3cFcZsZoneNextFreeIndex_Type()
)
h3cFcZsZoneNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsZoneNextFreeIndex.setStatus("current")


class _H3cFcZsZoneAliasNextFreeIndex_Type(Unsigned32):
    """Custom type h3cFcZsZoneAliasNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZoneAliasNextFreeIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZoneAliasNextFreeIndex_Object = MibScalar
h3cFcZsZoneAliasNextFreeIndex = _H3cFcZsZoneAliasNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 5, 3),
    _H3cFcZsZoneAliasNextFreeIndex_Type()
)
h3cFcZsZoneAliasNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsZoneAliasNextFreeIndex.setStatus("current")
_H3cFcZsZoneMemberNextFreeIndexTable_Object = MibTable
h3cFcZsZoneMemberNextFreeIndexTable = _H3cFcZsZoneMemberNextFreeIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberNextFreeIndexTable.setStatus("current")
_H3cFcZsZoneMemberNextFreeIndexEntry_Object = MibTableRow
h3cFcZsZoneMemberNextFreeIndexEntry = _H3cFcZsZoneMemberNextFreeIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 5, 4, 1)
)
h3cFcZsZoneMemberNextFreeIndexEntry.setIndexNames(
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneMemberParentType"),
    (0, "H3C-FC-ZONE-SERVER-MIB", "h3cFcZsZoneMemberParentIndex"),
)
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberNextFreeIndexEntry.setStatus("current")


class _H3cFcZsZoneMemberNextFreeIndex_Type(Unsigned32):
    """Custom type h3cFcZsZoneMemberNextFreeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_H3cFcZsZoneMemberNextFreeIndex_Type.__name__ = "Unsigned32"
_H3cFcZsZoneMemberNextFreeIndex_Object = MibTableColumn
h3cFcZsZoneMemberNextFreeIndex = _H3cFcZsZoneMemberNextFreeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 3, 5, 4, 1, 1),
    _H3cFcZsZoneMemberNextFreeIndex_Type()
)
h3cFcZsZoneMemberNextFreeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFcZsZoneMemberNextFreeIndex.setStatus("current")
_H3cFcZsNotification_ObjectIdentity = ObjectIdentity
h3cFcZsNotification = _H3cFcZsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4)
)
_H3cFcZsNotificationPrefix_ObjectIdentity = ObjectIdentity
h3cFcZsNotificationPrefix = _H3cFcZsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 0)
)
_H3cFcZsNotificationSwitch_ObjectIdentity = ObjectIdentity
h3cFcZsNotificationSwitch = _H3cFcZsNotificationSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 1)
)
_H3cFcZsDefaultZoneChangedEnable_Type = TruthValue
_H3cFcZsDefaultZoneChangedEnable_Object = MibScalar
h3cFcZsDefaultZoneChangedEnable = _H3cFcZsDefaultZoneChangedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 1, 1),
    _H3cFcZsDefaultZoneChangedEnable_Type()
)
h3cFcZsDefaultZoneChangedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsDefaultZoneChangedEnable.setStatus("current")
_H3cFcZsHardZoneChangedEnable_Type = TruthValue
_H3cFcZsHardZoneChangedEnable_Object = MibScalar
h3cFcZsHardZoneChangedEnable = _H3cFcZsHardZoneChangedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 1, 2),
    _H3cFcZsHardZoneChangedEnable_Type()
)
h3cFcZsHardZoneChangedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsHardZoneChangedEnable.setStatus("current")
_H3cFcZsMergeFailedEnable_Type = TruthValue
_H3cFcZsMergeFailedEnable_Object = MibScalar
h3cFcZsMergeFailedEnable = _H3cFcZsMergeFailedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 1, 3),
    _H3cFcZsMergeFailedEnable_Type()
)
h3cFcZsMergeFailedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsMergeFailedEnable.setStatus("current")
_H3cFcZsMergeSucceededEnable_Type = TruthValue
_H3cFcZsMergeSucceededEnable_Object = MibScalar
h3cFcZsMergeSucceededEnable = _H3cFcZsMergeSucceededEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 1, 4),
    _H3cFcZsMergeSucceededEnable_Type()
)
h3cFcZsMergeSucceededEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsMergeSucceededEnable.setStatus("current")
_H3cFcZsActivationCompletedEnable_Type = TruthValue
_H3cFcZsActivationCompletedEnable_Object = MibScalar
h3cFcZsActivationCompletedEnable = _H3cFcZsActivationCompletedEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 1, 5),
    _H3cFcZsActivationCompletedEnable_Type()
)
h3cFcZsActivationCompletedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFcZsActivationCompletedEnable.setStatus("current")
_H3cFcZsObjsForNotification_ObjectIdentity = ObjectIdentity
h3cFcZsObjsForNotification = _H3cFcZsObjsForNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 2)
)
_H3cFcZsLocalSwitchWWN_Type = H3cFcNameId
_H3cFcZsLocalSwitchWWN_Object = MibScalar
h3cFcZsLocalSwitchWWN = _H3cFcZsLocalSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 2, 1),
    _H3cFcZsLocalSwitchWWN_Type()
)
h3cFcZsLocalSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFcZsLocalSwitchWWN.setStatus("current")
_H3cFcZsPeerSwitchWWN_Type = H3cFcNameId
_H3cFcZsPeerSwitchWWN_Object = MibScalar
h3cFcZsPeerSwitchWWN = _H3cFcZsPeerSwitchWWN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 2, 2),
    _H3cFcZsPeerSwitchWWN_Type()
)
h3cFcZsPeerSwitchWWN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFcZsPeerSwitchWWN.setStatus("current")


class _H3cFcZsMergeFailCause_Type(Integer32):
    """Custom type h3cFcZsMergeFailCause based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("zoneModeInconsistent", 1),
          ("zonePolicyNotEqual", 2),
          ("hardZoneInconsistent", 3),
          ("dataNotEqualInRestrict", 4),
          ("activeZoneSetMergeFailed", 5),
          ("zoneMergeDataTooBig", 6),
          ("zoningObjectNumberTooBig", 7),
          ("zoneDbMergeFaildInBasic", 8),
          ("zoneDbMergeFaildInEnhanced", 9),
          ("other", 10))
    )


_H3cFcZsMergeFailCause_Type.__name__ = "Integer32"
_H3cFcZsMergeFailCause_Object = MibScalar
h3cFcZsMergeFailCause = _H3cFcZsMergeFailCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 2, 3),
    _H3cFcZsMergeFailCause_Type()
)
h3cFcZsMergeFailCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cFcZsMergeFailCause.setStatus("current")

# Managed Objects groups


# Notification objects

h3cFcZsDefaultZoneChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 0, 1)
)
h3cFcZsDefaultZoneChangedNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsLocalSwitchWWN"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsDefaultZoneSetting"))
)
if mibBuilder.loadTexts:
    h3cFcZsDefaultZoneChangedNotify.setStatus(
        "current"
    )

h3cFcZsHardZoneChangedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 0, 2)
)
h3cFcZsHardZoneChangedNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsLocalSwitchWWN"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsHardZoneStatus"))
)
if mibBuilder.loadTexts:
    h3cFcZsHardZoneChangedNotify.setStatus(
        "current"
    )

h3cFcZsMergeFailedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 0, 3)
)
h3cFcZsMergeFailedNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsLocalSwitchWWN"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsPeerSwitchWWN"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsMergeFailCause"))
)
if mibBuilder.loadTexts:
    h3cFcZsMergeFailedNotify.setStatus(
        "current"
    )

h3cFcZsMergeSucceededNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 0, 4)
)
h3cFcZsMergeSucceededNotify.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"),
        ("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsLocalSwitchWWN"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsPeerSwitchWWN"))
)
if mibBuilder.loadTexts:
    h3cFcZsMergeSucceededNotify.setStatus(
        "current"
    )

h3cFcZsActivationCompletedNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 127, 9, 1, 4, 0, 5)
)
h3cFcZsActivationCompletedNotify.setObjects(
      *(("H3C-VSAN-MIB", "h3cVsanIndex"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsLocalSwitchWWN"),
        ("H3C-FC-ZONE-SERVER-MIB", "h3cFcZsActivateResult"))
)
if mibBuilder.loadTexts:
    h3cFcZsActivationCompletedNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FC-ZONE-SERVER-MIB",
    **{"H3cFcZsGenName": H3cFcZsGenName,
       "H3cFcZsGenNameOrZero": H3cFcZsGenNameOrZero,
       "H3cFcZsZoneMemberType": H3cFcZsZoneMemberType,
       "h3cFcZoneServer": h3cFcZoneServer,
       "h3cFcZoneMibObjects": h3cFcZoneMibObjects,
       "h3cFcZsConfiguration": h3cFcZsConfiguration,
       "h3cFcZsServerTable": h3cFcZsServerTable,
       "h3cFcZsServerEntry": h3cFcZsServerEntry,
       "h3cFcZsZoneModeCfg": h3cFcZsZoneModeCfg,
       "h3cFcZsHardZoneEnable": h3cFcZsHardZoneEnable,
       "h3cFcZsDistributeRule": h3cFcZsDistributeRule,
       "h3cFcZsDefaultZoneSetting": h3cFcZsDefaultZoneSetting,
       "h3cFcZsMergeControlSetting": h3cFcZsMergeControlSetting,
       "h3cFcZsServerLastResult": h3cFcZsServerLastResult,
       "h3cFcZsZonesetTable": h3cFcZsZonesetTable,
       "h3cFcZsZonesetEntry": h3cFcZsZonesetEntry,
       "h3cFcZsZonesetIndex": h3cFcZsZonesetIndex,
       "h3cFcZsZonesetName": h3cFcZsZonesetName,
       "h3cFcZsZonesetRowStatus": h3cFcZsZonesetRowStatus,
       "h3cFcZsZoneTable": h3cFcZsZoneTable,
       "h3cFcZsZoneEntry": h3cFcZsZoneEntry,
       "h3cFcZsZoneIndex": h3cFcZsZoneIndex,
       "h3cFcZsZoneName": h3cFcZsZoneName,
       "h3cFcZsZonePairwiseEnable": h3cFcZsZonePairwiseEnable,
       "h3cFcZsZoneRowStatus": h3cFcZsZoneRowStatus,
       "h3cFcZsSetZoneTable": h3cFcZsSetZoneTable,
       "h3cFcZsSetZoneEntry": h3cFcZsSetZoneEntry,
       "h3cFcZsSetZoneRowStatus": h3cFcZsSetZoneRowStatus,
       "h3cFcZsZoneAliasTable": h3cFcZsZoneAliasTable,
       "h3cFcZsZoneAliasEntry": h3cFcZsZoneAliasEntry,
       "h3cFcZsZoneAliasIndex": h3cFcZsZoneAliasIndex,
       "h3cFcZsZoneAliasName": h3cFcZsZoneAliasName,
       "h3cFcZsZoneAliasRowStatus": h3cFcZsZoneAliasRowStatus,
       "h3cFcZsZoneMemberTable": h3cFcZsZoneMemberTable,
       "h3cFcZsZoneMemberEntry": h3cFcZsZoneMemberEntry,
       "h3cFcZsZoneMemberParentType": h3cFcZsZoneMemberParentType,
       "h3cFcZsZoneMemberParentIndex": h3cFcZsZoneMemberParentIndex,
       "h3cFcZsZoneMemberIndex": h3cFcZsZoneMemberIndex,
       "h3cFcZsZoneMemberFormat": h3cFcZsZoneMemberFormat,
       "h3cFcZsZoneMemberIdentifier": h3cFcZsZoneMemberIdentifier,
       "h3cFcZsZoneMemberPairwiseRole": h3cFcZsZoneMemberPairwiseRole,
       "h3cFcZsZoneMemberRowStatus": h3cFcZsZoneMemberRowStatus,
       "h3cFcZsOperation": h3cFcZsOperation,
       "h3cFcZsActivateTable": h3cFcZsActivateTable,
       "h3cFcZsActivateEntry": h3cFcZsActivateEntry,
       "h3cFcZsActivate": h3cFcZsActivate,
       "h3cFcZsDeactivate": h3cFcZsDeactivate,
       "h3cFcZsActivateResult": h3cFcZsActivateResult,
       "h3cFcZsActivateFailReason": h3cFcZsActivateFailReason,
       "h3cFcZsDistributeTable": h3cFcZsDistributeTable,
       "h3cFcZsDistributeEntry": h3cFcZsDistributeEntry,
       "h3cFcZsDistribute": h3cFcZsDistribute,
       "h3cFcZsDistributeLastResult": h3cFcZsDistributeLastResult,
       "h3cFcZsDistributeReasonCode": h3cFcZsDistributeReasonCode,
       "h3cFcZsDistributeExplainCode": h3cFcZsDistributeExplainCode,
       "h3cFcZsClearDatabaseTable": h3cFcZsClearDatabaseTable,
       "h3cFcZsClearDatabaseEntry": h3cFcZsClearDatabaseEntry,
       "h3cFcZsClearDatabase": h3cFcZsClearDatabase,
       "h3cFcZsClearPktStatsTable": h3cFcZsClearPktStatsTable,
       "h3cFcZsClearPktStatsEntry": h3cFcZsClearPktStatsEntry,
       "h3cFcZsClearPktStats": h3cFcZsClearPktStats,
       "h3cFcZsClearAllPktStats": h3cFcZsClearAllPktStats,
       "h3cFcZsInformation": h3cFcZsInformation,
       "h3cFcZsActiveZoneTable": h3cFcZsActiveZoneTable,
       "h3cFcZsActiveZoneEntry": h3cFcZsActiveZoneEntry,
       "h3cFcZsActiveZonePairwiseEnable": h3cFcZsActiveZonePairwiseEnable,
       "h3cFcZsActiveMemberTable": h3cFcZsActiveMemberTable,
       "h3cFcZsActiveMemberEntry": h3cFcZsActiveMemberEntry,
       "h3cFcZsActiveMemberPairwiseRole": h3cFcZsActiveMemberPairwiseRole,
       "h3cFcZsServerStatusTable": h3cFcZsServerStatusTable,
       "h3cFcZsServerStatusEntry": h3cFcZsServerStatusEntry,
       "h3cFcZsServerStatus": h3cFcZsServerStatus,
       "h3cFcZsHardZoneStatus": h3cFcZsHardZoneStatus,
       "h3cFcZsAliasCount": h3cFcZsAliasCount,
       "h3cFcZsZoneCount": h3cFcZsZoneCount,
       "h3cFcZsZonesetCount": h3cFcZsZonesetCount,
       "h3cFcZsPktStatsTable": h3cFcZsPktStatsTable,
       "h3cFcZsPktStatsEntry": h3cFcZsPktStatsEntry,
       "h3cFcZsPktInMergeReqCount": h3cFcZsPktInMergeReqCount,
       "h3cFcZsPktOutMergeReqCount": h3cFcZsPktOutMergeReqCount,
       "h3cFcZsPktInMergeAccCount": h3cFcZsPktInMergeAccCount,
       "h3cFcZsPktOutMergeAccCount": h3cFcZsPktOutMergeAccCount,
       "h3cFcZsPktInMergeRjtCount": h3cFcZsPktInMergeRjtCount,
       "h3cFcZsPktOutMergeRjtCount": h3cFcZsPktOutMergeRjtCount,
       "h3cFcZsPktInChangeReqCount": h3cFcZsPktInChangeReqCount,
       "h3cFcZsPktOutChangeReqCount": h3cFcZsPktOutChangeReqCount,
       "h3cFcZsPktInChangeAccCount": h3cFcZsPktInChangeAccCount,
       "h3cFcZsPktOutChangeAccCount": h3cFcZsPktOutChangeAccCount,
       "h3cFcZsPktInChangeRjtCount": h3cFcZsPktInChangeRjtCount,
       "h3cFcZsPktOutChangeRjtCount": h3cFcZsPktOutChangeRjtCount,
       "h3cFcZsNextFreeIndexInfo": h3cFcZsNextFreeIndexInfo,
       "h3cFcZsZonesetNextFreeIndex": h3cFcZsZonesetNextFreeIndex,
       "h3cFcZsZoneNextFreeIndex": h3cFcZsZoneNextFreeIndex,
       "h3cFcZsZoneAliasNextFreeIndex": h3cFcZsZoneAliasNextFreeIndex,
       "h3cFcZsZoneMemberNextFreeIndexTable": h3cFcZsZoneMemberNextFreeIndexTable,
       "h3cFcZsZoneMemberNextFreeIndexEntry": h3cFcZsZoneMemberNextFreeIndexEntry,
       "h3cFcZsZoneMemberNextFreeIndex": h3cFcZsZoneMemberNextFreeIndex,
       "h3cFcZsNotification": h3cFcZsNotification,
       "h3cFcZsNotificationPrefix": h3cFcZsNotificationPrefix,
       "h3cFcZsDefaultZoneChangedNotify": h3cFcZsDefaultZoneChangedNotify,
       "h3cFcZsHardZoneChangedNotify": h3cFcZsHardZoneChangedNotify,
       "h3cFcZsMergeFailedNotify": h3cFcZsMergeFailedNotify,
       "h3cFcZsMergeSucceededNotify": h3cFcZsMergeSucceededNotify,
       "h3cFcZsActivationCompletedNotify": h3cFcZsActivationCompletedNotify,
       "h3cFcZsNotificationSwitch": h3cFcZsNotificationSwitch,
       "h3cFcZsDefaultZoneChangedEnable": h3cFcZsDefaultZoneChangedEnable,
       "h3cFcZsHardZoneChangedEnable": h3cFcZsHardZoneChangedEnable,
       "h3cFcZsMergeFailedEnable": h3cFcZsMergeFailedEnable,
       "h3cFcZsMergeSucceededEnable": h3cFcZsMergeSucceededEnable,
       "h3cFcZsActivationCompletedEnable": h3cFcZsActivationCompletedEnable,
       "h3cFcZsObjsForNotification": h3cFcZsObjsForNotification,
       "h3cFcZsLocalSwitchWWN": h3cFcZsLocalSwitchWWN,
       "h3cFcZsPeerSwitchWWN": h3cFcZsPeerSwitchWWN,
       "h3cFcZsMergeFailCause": h3cFcZsMergeFailCause}
)
