# SNMP MIB module (ENTERASYS-CN-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-CN-MIB-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:46 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(ieee8021CnCpEntry,
 ieee8021CnGlobalEntry) = mibBuilder.importSymbols(
    "IEEE8021-CN-MIB",
    "ieee8021CnCpEntry",
    "ieee8021CnGlobalEntry")

(IEEE8021PbbComponentIdentifier,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PbbComponentIdentifier")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

etsysCnMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95)
)
if mibBuilder.loadTexts:
    etsysCnMibExtMIB.setRevisions(
        ("2012-07-20 12:21",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysCnMibExtObjects_ObjectIdentity = ObjectIdentity
etsysCnMibExtObjects = _EtsysCnMibExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1)
)
_EtsysCnMibExtSysBranch_ObjectIdentity = ObjectIdentity
etsysCnMibExtSysBranch = _EtsysCnMibExtSysBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1)
)
_EtsysCnMibExtQpTypeTable_Object = MibTable
etsysCnMibExtQpTypeTable = _EtsysCnMibExtQpTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysCnMibExtQpTypeTable.setStatus("current")
_EtsysCnMibExtQpTypeEntry_Object = MibTableRow
etsysCnMibExtQpTypeEntry = _EtsysCnMibExtQpTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1, 1, 1)
)
etsysCnMibExtQpTypeEntry.setIndexNames(
    (0, "ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQptIdentifier"),
)
if mibBuilder.loadTexts:
    etsysCnMibExtQpTypeEntry.setStatus("current")
_EtsysCnMibExtQptIdentifier_Type = Unsigned32
_EtsysCnMibExtQptIdentifier_Object = MibTableColumn
etsysCnMibExtQptIdentifier = _EtsysCnMibExtQptIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1, 1, 1, 1),
    _EtsysCnMibExtQptIdentifier_Type()
)
etsysCnMibExtQptIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCnMibExtQptIdentifier.setStatus("current")


class _EtsysCnMibExtQptDesc_Type(SnmpAdminString):
    """Custom type etsysCnMibExtQptDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_EtsysCnMibExtQptDesc_Type.__name__ = "SnmpAdminString"
_EtsysCnMibExtQptDesc_Object = MibTableColumn
etsysCnMibExtQptDesc = _EtsysCnMibExtQptDesc_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1, 1, 1, 2),
    _EtsysCnMibExtQptDesc_Type()
)
etsysCnMibExtQptDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCnMibExtQptDesc.setStatus("current")
_EtsysCnMibExtQptMaxQpEntries_Type = Unsigned32
_EtsysCnMibExtQptMaxQpEntries_Object = MibTableColumn
etsysCnMibExtQptMaxQpEntries = _EtsysCnMibExtQptMaxQpEntries_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1, 1, 1, 3),
    _EtsysCnMibExtQptMaxQpEntries_Type()
)
etsysCnMibExtQptMaxQpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCnMibExtQptMaxQpEntries.setStatus("current")


class _EtsysCnMibExtQptSupport_Type(Bits):
    """Custom type etsysCnMibExtQptSupport based on Bits"""
    namedValues = NamedValues(
        *(("supportSizeSetPoint", 0),
          ("supportFeedbackWeight", 1),
          ("supportMinSampleBase", 2),
          ("supportMinHeaderOctets", 3))
    )

_EtsysCnMibExtQptSupport_Type.__name__ = "Bits"
_EtsysCnMibExtQptSupport_Object = MibTableColumn
etsysCnMibExtQptSupport = _EtsysCnMibExtQptSupport_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1, 1, 1, 4),
    _EtsysCnMibExtQptSupport_Type()
)
etsysCnMibExtQptSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCnMibExtQptSupport.setStatus("current")
_EtsysCnMibExtMaxCompActivePriVals_Type = Unsigned32
_EtsysCnMibExtMaxCompActivePriVals_Object = MibScalar
etsysCnMibExtMaxCompActivePriVals = _EtsysCnMibExtMaxCompActivePriVals_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 1, 2),
    _EtsysCnMibExtMaxCompActivePriVals_Type()
)
etsysCnMibExtMaxCompActivePriVals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCnMibExtMaxCompActivePriVals.setStatus("current")
_EtsysCnMibExtCompBranch_ObjectIdentity = ObjectIdentity
etsysCnMibExtCompBranch = _EtsysCnMibExtCompBranch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2)
)
_EtsysCnMibExtQpTable_Object = MibTable
etsysCnMibExtQpTable = _EtsysCnMibExtQpTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysCnMibExtQpTable.setStatus("current")
_EtsysCnMibExtQpEntry_Object = MibTableRow
etsysCnMibExtQpEntry = _EtsysCnMibExtQpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1)
)
etsysCnMibExtQpEntry.setIndexNames(
    (0, "ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpComponentId"),
    (0, "ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpTypeId"),
    (0, "ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpIndex"),
)
if mibBuilder.loadTexts:
    etsysCnMibExtQpEntry.setStatus("current")
_EtsysCnMibExtQpComponentId_Type = IEEE8021PbbComponentIdentifier
_EtsysCnMibExtQpComponentId_Object = MibTableColumn
etsysCnMibExtQpComponentId = _EtsysCnMibExtQpComponentId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 1),
    _EtsysCnMibExtQpComponentId_Type()
)
etsysCnMibExtQpComponentId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCnMibExtQpComponentId.setStatus("current")
_EtsysCnMibExtQpTypeId_Type = Unsigned32
_EtsysCnMibExtQpTypeId_Object = MibTableColumn
etsysCnMibExtQpTypeId = _EtsysCnMibExtQpTypeId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 2),
    _EtsysCnMibExtQpTypeId_Type()
)
etsysCnMibExtQpTypeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCnMibExtQpTypeId.setStatus("current")
_EtsysCnMibExtQpIndex_Type = Unsigned32
_EtsysCnMibExtQpIndex_Object = MibTableColumn
etsysCnMibExtQpIndex = _EtsysCnMibExtQpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 3),
    _EtsysCnMibExtQpIndex_Type()
)
etsysCnMibExtQpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysCnMibExtQpIndex.setStatus("current")


class _EtsysCnMibExtQpSizeSetPoint_Type(Unsigned32):
    """Custom type etsysCnMibExtQpSizeSetPoint based on Unsigned32"""
    defaultValue = 26000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 4294967295),
    )


_EtsysCnMibExtQpSizeSetPoint_Type.__name__ = "Unsigned32"
_EtsysCnMibExtQpSizeSetPoint_Object = MibTableColumn
etsysCnMibExtQpSizeSetPoint = _EtsysCnMibExtQpSizeSetPoint_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 4),
    _EtsysCnMibExtQpSizeSetPoint_Type()
)
etsysCnMibExtQpSizeSetPoint.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCnMibExtQpSizeSetPoint.setStatus("current")
if mibBuilder.loadTexts:
    etsysCnMibExtQpSizeSetPoint.setUnits("octets")


class _EtsysCnMibExtQpFeedbackWeight_Type(Integer32):
    """Custom type etsysCnMibExtQpFeedbackWeight based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10, 10),
    )


_EtsysCnMibExtQpFeedbackWeight_Type.__name__ = "Integer32"
_EtsysCnMibExtQpFeedbackWeight_Object = MibTableColumn
etsysCnMibExtQpFeedbackWeight = _EtsysCnMibExtQpFeedbackWeight_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 5),
    _EtsysCnMibExtQpFeedbackWeight_Type()
)
etsysCnMibExtQpFeedbackWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCnMibExtQpFeedbackWeight.setStatus("current")


class _EtsysCnMibExtQpMinSampleBase_Type(Unsigned32):
    """Custom type etsysCnMibExtQpMinSampleBase based on Unsigned32"""
    defaultValue = 150000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10000, 4294967295),
    )


_EtsysCnMibExtQpMinSampleBase_Type.__name__ = "Unsigned32"
_EtsysCnMibExtQpMinSampleBase_Object = MibTableColumn
etsysCnMibExtQpMinSampleBase = _EtsysCnMibExtQpMinSampleBase_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 6),
    _EtsysCnMibExtQpMinSampleBase_Type()
)
etsysCnMibExtQpMinSampleBase.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCnMibExtQpMinSampleBase.setStatus("current")
if mibBuilder.loadTexts:
    etsysCnMibExtQpMinSampleBase.setUnits("octets")


class _EtsysCnMibExtQpMinHeaderOctets_Type(Unsigned32):
    """Custom type etsysCnMibExtQpMinHeaderOctets based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_EtsysCnMibExtQpMinHeaderOctets_Type.__name__ = "Unsigned32"
_EtsysCnMibExtQpMinHeaderOctets_Object = MibTableColumn
etsysCnMibExtQpMinHeaderOctets = _EtsysCnMibExtQpMinHeaderOctets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 7),
    _EtsysCnMibExtQpMinHeaderOctets_Type()
)
etsysCnMibExtQpMinHeaderOctets.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCnMibExtQpMinHeaderOctets.setStatus("current")
if mibBuilder.loadTexts:
    etsysCnMibExtQpMinHeaderOctets.setUnits("octets")
_EtsysCnMibExtQpRowStatus_Type = RowStatus
_EtsysCnMibExtQpRowStatus_Object = MibTableColumn
etsysCnMibExtQpRowStatus = _EtsysCnMibExtQpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 1, 1, 8),
    _EtsysCnMibExtQpRowStatus_Type()
)
etsysCnMibExtQpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysCnMibExtQpRowStatus.setStatus("current")
_EtsysCnMibExtCpTable_Object = MibTable
etsysCnMibExtCpTable = _EtsysCnMibExtCpTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysCnMibExtCpTable.setStatus("current")
_EtsysCnMibExtCpEntry_Object = MibTableRow
etsysCnMibExtCpEntry = _EtsysCnMibExtCpEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysCnMibExtCpEntry.setStatus("current")
_EtsysCnMibExtCpQpTypeId_Type = Unsigned32
_EtsysCnMibExtCpQpTypeId_Object = MibTableColumn
etsysCnMibExtCpQpTypeId = _EtsysCnMibExtCpQpTypeId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 2, 1, 1),
    _EtsysCnMibExtCpQpTypeId_Type()
)
etsysCnMibExtCpQpTypeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCnMibExtCpQpTypeId.setStatus("current")
_EtsysCnMibExtCpQpIndex_Type = Unsigned32
_EtsysCnMibExtCpQpIndex_Object = MibTableColumn
etsysCnMibExtCpQpIndex = _EtsysCnMibExtCpQpIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 2, 1, 2),
    _EtsysCnMibExtCpQpIndex_Type()
)
etsysCnMibExtCpQpIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysCnMibExtCpQpIndex.setStatus("current")
_EtsysCnMibExtGlobalTable_Object = MibTable
etsysCnMibExtGlobalTable = _EtsysCnMibExtGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 3)
)
if mibBuilder.loadTexts:
    etsysCnMibExtGlobalTable.setStatus("current")
_EtsysCnMibExtGlobalEntry_Object = MibTableRow
etsysCnMibExtGlobalEntry = _EtsysCnMibExtGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    etsysCnMibExtGlobalEntry.setStatus("current")
_EtsysCnMibExtGlobalActivePriVals_Type = Unsigned32
_EtsysCnMibExtGlobalActivePriVals_Object = MibTableColumn
etsysCnMibExtGlobalActivePriVals = _EtsysCnMibExtGlobalActivePriVals_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 1, 2, 3, 1, 1),
    _EtsysCnMibExtGlobalActivePriVals_Type()
)
etsysCnMibExtGlobalActivePriVals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysCnMibExtGlobalActivePriVals.setStatus("current")
_EtsysCnMibExtConformance_ObjectIdentity = ObjectIdentity
etsysCnMibExtConformance = _EtsysCnMibExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2)
)
_EtsysCnMibExtGroups_ObjectIdentity = ObjectIdentity
etsysCnMibExtGroups = _EtsysCnMibExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 1)
)
_EtsysCnMibExtCompliances_ObjectIdentity = ObjectIdentity
etsysCnMibExtCompliances = _EtsysCnMibExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 2)
)
ieee8021CnCpEntry.registerAugmentions(
    ("ENTERASYS-CN-MIB-EXT-MIB",
     "etsysCnMibExtCpEntry")
)
etsysCnMibExtCpEntry.setIndexNames(*ieee8021CnCpEntry.getIndexNames())
ieee8021CnGlobalEntry.registerAugmentions(
    ("ENTERASYS-CN-MIB-EXT-MIB",
     "etsysCnMibExtGlobalEntry")
)
etsysCnMibExtGlobalEntry.setIndexNames(*ieee8021CnGlobalEntry.getIndexNames())

# Managed Objects groups

etsysCnMibExtQpTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 1, 1)
)
etsysCnMibExtQpTypeGroup.setObjects(
      *(("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQptDesc"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQptMaxQpEntries"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQptSupport"))
)
if mibBuilder.loadTexts:
    etsysCnMibExtQpTypeGroup.setStatus("current")

etsysCnMibExtSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 1, 2)
)
etsysCnMibExtSysGroup.setObjects(
    ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtMaxCompActivePriVals")
)
if mibBuilder.loadTexts:
    etsysCnMibExtSysGroup.setStatus("current")

etsysCnMibExtGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 1, 3)
)
etsysCnMibExtGlobalGroup.setObjects(
    ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtGlobalActivePriVals")
)
if mibBuilder.loadTexts:
    etsysCnMibExtGlobalGroup.setStatus("current")

etsysCnMibExtQpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 1, 4)
)
etsysCnMibExtQpGroup.setObjects(
      *(("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpSizeSetPoint"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpFeedbackWeight"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpMinSampleBase"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpMinHeaderOctets"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpRowStatus"))
)
if mibBuilder.loadTexts:
    etsysCnMibExtQpGroup.setStatus("current")

etsysCnMibExtCpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 1, 5)
)
etsysCnMibExtCpGroup.setObjects(
      *(("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtCpQpTypeId"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtCpQpIndex"))
)
if mibBuilder.loadTexts:
    etsysCnMibExtCpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysCnMibExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 95, 2, 2, 1)
)
etsysCnMibExtCompliance.setObjects(
      *(("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpTypeGroup"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtSysGroup"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtGlobalGroup"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtQpGroup"),
        ("ENTERASYS-CN-MIB-EXT-MIB", "etsysCnMibExtCpGroup"))
)
if mibBuilder.loadTexts:
    etsysCnMibExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-CN-MIB-EXT-MIB",
    **{"etsysCnMibExtMIB": etsysCnMibExtMIB,
       "etsysCnMibExtObjects": etsysCnMibExtObjects,
       "etsysCnMibExtSysBranch": etsysCnMibExtSysBranch,
       "etsysCnMibExtQpTypeTable": etsysCnMibExtQpTypeTable,
       "etsysCnMibExtQpTypeEntry": etsysCnMibExtQpTypeEntry,
       "etsysCnMibExtQptIdentifier": etsysCnMibExtQptIdentifier,
       "etsysCnMibExtQptDesc": etsysCnMibExtQptDesc,
       "etsysCnMibExtQptMaxQpEntries": etsysCnMibExtQptMaxQpEntries,
       "etsysCnMibExtQptSupport": etsysCnMibExtQptSupport,
       "etsysCnMibExtMaxCompActivePriVals": etsysCnMibExtMaxCompActivePriVals,
       "etsysCnMibExtCompBranch": etsysCnMibExtCompBranch,
       "etsysCnMibExtQpTable": etsysCnMibExtQpTable,
       "etsysCnMibExtQpEntry": etsysCnMibExtQpEntry,
       "etsysCnMibExtQpComponentId": etsysCnMibExtQpComponentId,
       "etsysCnMibExtQpTypeId": etsysCnMibExtQpTypeId,
       "etsysCnMibExtQpIndex": etsysCnMibExtQpIndex,
       "etsysCnMibExtQpSizeSetPoint": etsysCnMibExtQpSizeSetPoint,
       "etsysCnMibExtQpFeedbackWeight": etsysCnMibExtQpFeedbackWeight,
       "etsysCnMibExtQpMinSampleBase": etsysCnMibExtQpMinSampleBase,
       "etsysCnMibExtQpMinHeaderOctets": etsysCnMibExtQpMinHeaderOctets,
       "etsysCnMibExtQpRowStatus": etsysCnMibExtQpRowStatus,
       "etsysCnMibExtCpTable": etsysCnMibExtCpTable,
       "etsysCnMibExtCpEntry": etsysCnMibExtCpEntry,
       "etsysCnMibExtCpQpTypeId": etsysCnMibExtCpQpTypeId,
       "etsysCnMibExtCpQpIndex": etsysCnMibExtCpQpIndex,
       "etsysCnMibExtGlobalTable": etsysCnMibExtGlobalTable,
       "etsysCnMibExtGlobalEntry": etsysCnMibExtGlobalEntry,
       "etsysCnMibExtGlobalActivePriVals": etsysCnMibExtGlobalActivePriVals,
       "etsysCnMibExtConformance": etsysCnMibExtConformance,
       "etsysCnMibExtGroups": etsysCnMibExtGroups,
       "etsysCnMibExtQpTypeGroup": etsysCnMibExtQpTypeGroup,
       "etsysCnMibExtSysGroup": etsysCnMibExtSysGroup,
       "etsysCnMibExtGlobalGroup": etsysCnMibExtGlobalGroup,
       "etsysCnMibExtQpGroup": etsysCnMibExtQpGroup,
       "etsysCnMibExtCpGroup": etsysCnMibExtCpGroup,
       "etsysCnMibExtCompliances": etsysCnMibExtCompliances,
       "etsysCnMibExtCompliance": etsysCnMibExtCompliance}
)
