# SNMP MIB module (ARICENT-OSPF-TE-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-OSPF-TE-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:12 2025
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
 enterprises,
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
    "enterprises",
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

fsOspfTeSasGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20)
)
if mibBuilder.loadTexts:
    fsOspfTeSasGroup.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsOspfTeSas_ObjectIdentity = ObjectIdentity
fsOspfTeSas = _FsOspfTeSas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 1)
)
_FsOspfTeSasTable_ObjectIdentity = ObjectIdentity
fsOspfTeSasTable = _FsOspfTeSasTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2)
)
_FsOspfTeSasConstraintTable_Object = MibTable
fsOspfTeSasConstraintTable = _FsOspfTeSasConstraintTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1)
)
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintTable.setStatus("current")
_FsOspfTeSasConstraintEntry_Object = MibTableRow
fsOspfTeSasConstraintEntry = _FsOspfTeSasConstraintEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1)
)
fsOspfTeSasConstraintEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-TEST-MIB", "fsOspfTeSasConstraintId"),
)
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintEntry.setStatus("current")


class _FsOspfTeSasConstraintId_Type(Integer32):
    """Custom type fsOspfTeSasConstraintId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsOspfTeSasConstraintId_Type.__name__ = "Integer32"
_FsOspfTeSasConstraintId_Object = MibTableColumn
fsOspfTeSasConstraintId = _FsOspfTeSasConstraintId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 1),
    _FsOspfTeSasConstraintId_Type()
)
fsOspfTeSasConstraintId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintId.setStatus("current")
_FsOspfTeSasConstraintSourceIpAddr_Type = IpAddress
_FsOspfTeSasConstraintSourceIpAddr_Object = MibTableColumn
fsOspfTeSasConstraintSourceIpAddr = _FsOspfTeSasConstraintSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 2),
    _FsOspfTeSasConstraintSourceIpAddr_Type()
)
fsOspfTeSasConstraintSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintSourceIpAddr.setStatus("current")
_FsOspfTeSasConstraintDestinationIpAddr_Type = IpAddress
_FsOspfTeSasConstraintDestinationIpAddr_Object = MibTableColumn
fsOspfTeSasConstraintDestinationIpAddr = _FsOspfTeSasConstraintDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 3),
    _FsOspfTeSasConstraintDestinationIpAddr_Type()
)
fsOspfTeSasConstraintDestinationIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintDestinationIpAddr.setStatus("current")
_FsOspfTeSasConstraintWPSourceIpAddr_Type = IpAddress
_FsOspfTeSasConstraintWPSourceIpAddr_Object = MibTableColumn
fsOspfTeSasConstraintWPSourceIpAddr = _FsOspfTeSasConstraintWPSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 4),
    _FsOspfTeSasConstraintWPSourceIpAddr_Type()
)
fsOspfTeSasConstraintWPSourceIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintWPSourceIpAddr.setStatus("current")
_FsOspfTeSasConstraintWPDestinationIpAddr_Type = IpAddress
_FsOspfTeSasConstraintWPDestinationIpAddr_Object = MibTableColumn
fsOspfTeSasConstraintWPDestinationIpAddr = _FsOspfTeSasConstraintWPDestinationIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 5),
    _FsOspfTeSasConstraintWPDestinationIpAddr_Type()
)
fsOspfTeSasConstraintWPDestinationIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintWPDestinationIpAddr.setStatus("current")
_FsOspfTeSasConstraintMaxPathMetric_Type = Integer32
_FsOspfTeSasConstraintMaxPathMetric_Object = MibTableColumn
fsOspfTeSasConstraintMaxPathMetric = _FsOspfTeSasConstraintMaxPathMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 6),
    _FsOspfTeSasConstraintMaxPathMetric_Type()
)
fsOspfTeSasConstraintMaxPathMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintMaxPathMetric.setStatus("current")
_FsOspfTeSasConstraintMaxHopsInPath_Type = Integer32
_FsOspfTeSasConstraintMaxHopsInPath_Object = MibTableColumn
fsOspfTeSasConstraintMaxHopsInPath = _FsOspfTeSasConstraintMaxHopsInPath_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 7),
    _FsOspfTeSasConstraintMaxHopsInPath_Type()
)
fsOspfTeSasConstraintMaxHopsInPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintMaxHopsInPath.setStatus("current")


class _FsOspfTeSasConstraintBw_Type(Integer32):
    """Custom type fsOspfTeSasConstraintBw based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsOspfTeSasConstraintBw_Type.__name__ = "Integer32"
_FsOspfTeSasConstraintBw_Object = MibTableColumn
fsOspfTeSasConstraintBw = _FsOspfTeSasConstraintBw_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 8),
    _FsOspfTeSasConstraintBw_Type()
)
fsOspfTeSasConstraintBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintBw.setStatus("current")
_FsOspfTeSasConstraintIncludeAllSet_Type = Integer32
_FsOspfTeSasConstraintIncludeAllSet_Object = MibTableColumn
fsOspfTeSasConstraintIncludeAllSet = _FsOspfTeSasConstraintIncludeAllSet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 9),
    _FsOspfTeSasConstraintIncludeAllSet_Type()
)
fsOspfTeSasConstraintIncludeAllSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintIncludeAllSet.setStatus("current")
_FsOspfTeSasConstraintIncludeAnySet_Type = Integer32
_FsOspfTeSasConstraintIncludeAnySet_Object = MibTableColumn
fsOspfTeSasConstraintIncludeAnySet = _FsOspfTeSasConstraintIncludeAnySet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 10),
    _FsOspfTeSasConstraintIncludeAnySet_Type()
)
fsOspfTeSasConstraintIncludeAnySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintIncludeAnySet.setStatus("current")
_FsOspfTeSasConstraintExcludeAnySet_Type = Integer32
_FsOspfTeSasConstraintExcludeAnySet_Object = MibTableColumn
fsOspfTeSasConstraintExcludeAnySet = _FsOspfTeSasConstraintExcludeAnySet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 11),
    _FsOspfTeSasConstraintExcludeAnySet_Type()
)
fsOspfTeSasConstraintExcludeAnySet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintExcludeAnySet.setStatus("current")
_FsOspfTeSasConstraintPriority_Type = Integer32
_FsOspfTeSasConstraintPriority_Object = MibTableColumn
fsOspfTeSasConstraintPriority = _FsOspfTeSasConstraintPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 12),
    _FsOspfTeSasConstraintPriority_Type()
)
fsOspfTeSasConstraintPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintPriority.setStatus("current")
_FsOspfTeSasConstraintExplicitRoute_Type = OctetString
_FsOspfTeSasConstraintExplicitRoute_Object = MibTableColumn
fsOspfTeSasConstraintExplicitRoute = _FsOspfTeSasConstraintExplicitRoute_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 13),
    _FsOspfTeSasConstraintExplicitRoute_Type()
)
fsOspfTeSasConstraintExplicitRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintExplicitRoute.setStatus("current")
_FsOspfTeSasConstraintSwitchingCapability_Type = Integer32
_FsOspfTeSasConstraintSwitchingCapability_Object = MibTableColumn
fsOspfTeSasConstraintSwitchingCapability = _FsOspfTeSasConstraintSwitchingCapability_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 14),
    _FsOspfTeSasConstraintSwitchingCapability_Type()
)
fsOspfTeSasConstraintSwitchingCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintSwitchingCapability.setStatus("current")
_FsOspfTeSasConstraintEncodingType_Type = Integer32
_FsOspfTeSasConstraintEncodingType_Object = MibTableColumn
fsOspfTeSasConstraintEncodingType = _FsOspfTeSasConstraintEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 15),
    _FsOspfTeSasConstraintEncodingType_Type()
)
fsOspfTeSasConstraintEncodingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintEncodingType.setStatus("current")
_FsOspfTeSasConstraintLinkProtectionType_Type = Integer32
_FsOspfTeSasConstraintLinkProtectionType_Object = MibTableColumn
fsOspfTeSasConstraintLinkProtectionType = _FsOspfTeSasConstraintLinkProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 16),
    _FsOspfTeSasConstraintLinkProtectionType_Type()
)
fsOspfTeSasConstraintLinkProtectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintLinkProtectionType.setStatus("current")


class _FsOspfTeSasConstraintDiversity_Type(Integer32):
    """Custom type fsOspfTeSasConstraintDiversity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("nodeDisjoint", 1),
          ("linkDisjoint", 2),
          ("sRLGDisjoint", 4))
    )


_FsOspfTeSasConstraintDiversity_Type.__name__ = "Integer32"
_FsOspfTeSasConstraintDiversity_Object = MibTableColumn
fsOspfTeSasConstraintDiversity = _FsOspfTeSasConstraintDiversity_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 17),
    _FsOspfTeSasConstraintDiversity_Type()
)
fsOspfTeSasConstraintDiversity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintDiversity.setStatus("current")
_FsOspfTeSasConstraintIndication_Type = Integer32
_FsOspfTeSasConstraintIndication_Object = MibTableColumn
fsOspfTeSasConstraintIndication = _FsOspfTeSasConstraintIndication_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 18),
    _FsOspfTeSasConstraintIndication_Type()
)
fsOspfTeSasConstraintIndication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintIndication.setStatus("current")
_FsOspfTeSasConstraintFlag_Type = Integer32
_FsOspfTeSasConstraintFlag_Object = MibTableColumn
fsOspfTeSasConstraintFlag = _FsOspfTeSasConstraintFlag_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 19),
    _FsOspfTeSasConstraintFlag_Type()
)
fsOspfTeSasConstraintFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintFlag.setStatus("current")
_FsOspfTeSasConstraintStatus_Type = RowStatus
_FsOspfTeSasConstraintStatus_Object = MibTableColumn
fsOspfTeSasConstraintStatus = _FsOspfTeSasConstraintStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 1, 1, 20),
    _FsOspfTeSasConstraintStatus_Type()
)
fsOspfTeSasConstraintStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsOspfTeSasConstraintStatus.setStatus("current")
_FsOspfTeSasCspfPathTable_Object = MibTable
fsOspfTeSasCspfPathTable = _FsOspfTeSasCspfPathTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2)
)
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathTable.setStatus("current")
_FsOspfTeSasCspfPathEntry_Object = MibTableRow
fsOspfTeSasCspfPathEntry = _FsOspfTeSasCspfPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2, 1)
)
fsOspfTeSasCspfPathEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-TEST-MIB", "fsOspfTeSasCspfPathConstraintId"),
    (0, "ARICENT-OSPF-TE-TEST-MIB", "fsOspfTeSasCspfPathType"),
)
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathEntry.setStatus("current")


class _FsOspfTeSasCspfPathConstraintId_Type(Integer32):
    """Custom type fsOspfTeSasCspfPathConstraintId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsOspfTeSasCspfPathConstraintId_Type.__name__ = "Integer32"
_FsOspfTeSasCspfPathConstraintId_Object = MibTableColumn
fsOspfTeSasCspfPathConstraintId = _FsOspfTeSasCspfPathConstraintId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2, 1, 1),
    _FsOspfTeSasCspfPathConstraintId_Type()
)
fsOspfTeSasCspfPathConstraintId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathConstraintId.setStatus("current")


class _FsOspfTeSasCspfPathType_Type(Integer32):
    """Custom type fsOspfTeSasCspfPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2))
    )


_FsOspfTeSasCspfPathType_Type.__name__ = "Integer32"
_FsOspfTeSasCspfPathType_Object = MibTableColumn
fsOspfTeSasCspfPathType = _FsOspfTeSasCspfPathType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2, 1, 2),
    _FsOspfTeSasCspfPathType_Type()
)
fsOspfTeSasCspfPathType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathType.setStatus("current")
_FsOspfTeSasCspfPathNumHops_Type = Integer32
_FsOspfTeSasCspfPathNumHops_Object = MibTableColumn
fsOspfTeSasCspfPathNumHops = _FsOspfTeSasCspfPathNumHops_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2, 1, 3),
    _FsOspfTeSasCspfPathNumHops_Type()
)
fsOspfTeSasCspfPathNumHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathNumHops.setStatus("current")
_FsOspfTeSasCspfPathRouterId_Type = OctetString
_FsOspfTeSasCspfPathRouterId_Object = MibTableColumn
fsOspfTeSasCspfPathRouterId = _FsOspfTeSasCspfPathRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2, 1, 4),
    _FsOspfTeSasCspfPathRouterId_Type()
)
fsOspfTeSasCspfPathRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathRouterId.setStatus("current")
_FsOspfTeSasCspfPathNextHopIpAddress_Type = OctetString
_FsOspfTeSasCspfPathNextHopIpAddress_Object = MibTableColumn
fsOspfTeSasCspfPathNextHopIpAddress = _FsOspfTeSasCspfPathNextHopIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2, 1, 5),
    _FsOspfTeSasCspfPathNextHopIpAddress_Type()
)
fsOspfTeSasCspfPathNextHopIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathNextHopIpAddress.setStatus("current")
_FsOspfTeSasCspfPathLocalIdentifier_Type = OctetString
_FsOspfTeSasCspfPathLocalIdentifier_Object = MibTableColumn
fsOspfTeSasCspfPathLocalIdentifier = _FsOspfTeSasCspfPathLocalIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 20, 2, 2, 1, 6),
    _FsOspfTeSasCspfPathLocalIdentifier_Type()
)
fsOspfTeSasCspfPathLocalIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsOspfTeSasCspfPathLocalIdentifier.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-OSPF-TE-TEST-MIB",
    **{"fsOspfTeSasGroup": fsOspfTeSasGroup,
       "fsOspfTeSas": fsOspfTeSas,
       "fsOspfTeSasTable": fsOspfTeSasTable,
       "fsOspfTeSasConstraintTable": fsOspfTeSasConstraintTable,
       "fsOspfTeSasConstraintEntry": fsOspfTeSasConstraintEntry,
       "fsOspfTeSasConstraintId": fsOspfTeSasConstraintId,
       "fsOspfTeSasConstraintSourceIpAddr": fsOspfTeSasConstraintSourceIpAddr,
       "fsOspfTeSasConstraintDestinationIpAddr": fsOspfTeSasConstraintDestinationIpAddr,
       "fsOspfTeSasConstraintWPSourceIpAddr": fsOspfTeSasConstraintWPSourceIpAddr,
       "fsOspfTeSasConstraintWPDestinationIpAddr": fsOspfTeSasConstraintWPDestinationIpAddr,
       "fsOspfTeSasConstraintMaxPathMetric": fsOspfTeSasConstraintMaxPathMetric,
       "fsOspfTeSasConstraintMaxHopsInPath": fsOspfTeSasConstraintMaxHopsInPath,
       "fsOspfTeSasConstraintBw": fsOspfTeSasConstraintBw,
       "fsOspfTeSasConstraintIncludeAllSet": fsOspfTeSasConstraintIncludeAllSet,
       "fsOspfTeSasConstraintIncludeAnySet": fsOspfTeSasConstraintIncludeAnySet,
       "fsOspfTeSasConstraintExcludeAnySet": fsOspfTeSasConstraintExcludeAnySet,
       "fsOspfTeSasConstraintPriority": fsOspfTeSasConstraintPriority,
       "fsOspfTeSasConstraintExplicitRoute": fsOspfTeSasConstraintExplicitRoute,
       "fsOspfTeSasConstraintSwitchingCapability": fsOspfTeSasConstraintSwitchingCapability,
       "fsOspfTeSasConstraintEncodingType": fsOspfTeSasConstraintEncodingType,
       "fsOspfTeSasConstraintLinkProtectionType": fsOspfTeSasConstraintLinkProtectionType,
       "fsOspfTeSasConstraintDiversity": fsOspfTeSasConstraintDiversity,
       "fsOspfTeSasConstraintIndication": fsOspfTeSasConstraintIndication,
       "fsOspfTeSasConstraintFlag": fsOspfTeSasConstraintFlag,
       "fsOspfTeSasConstraintStatus": fsOspfTeSasConstraintStatus,
       "fsOspfTeSasCspfPathTable": fsOspfTeSasCspfPathTable,
       "fsOspfTeSasCspfPathEntry": fsOspfTeSasCspfPathEntry,
       "fsOspfTeSasCspfPathConstraintId": fsOspfTeSasCspfPathConstraintId,
       "fsOspfTeSasCspfPathType": fsOspfTeSasCspfPathType,
       "fsOspfTeSasCspfPathNumHops": fsOspfTeSasCspfPathNumHops,
       "fsOspfTeSasCspfPathRouterId": fsOspfTeSasCspfPathRouterId,
       "fsOspfTeSasCspfPathNextHopIpAddress": fsOspfTeSasCspfPathNextHopIpAddress,
       "fsOspfTeSasCspfPathLocalIdentifier": fsOspfTeSasCspfPathLocalIdentifier}
)
