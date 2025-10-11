# SNMP MIB module (OS-RESOURCES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-RESOURCES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:42 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

osResources = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41)
)
if mibBuilder.loadTexts:
    osResources.setRevisions(
        ("2019-12-11 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsResourcesGen_ObjectIdentity = ObjectIdentity
osResourcesGen = _OsResourcesGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 1)
)


class _OsResourcesSupport_Type(Integer32):
    """Custom type osResourcesSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OsResourcesSupport_Type.__name__ = "Integer32"
_OsResourcesSupport_Object = MibScalar
osResourcesSupport = _OsResourcesSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 1, 1),
    _OsResourcesSupport_Type()
)
osResourcesSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourcesSupport.setStatus("current")
_OsResourcesTables_ObjectIdentity = ObjectIdentity
osResourcesTables = _OsResourcesTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2)
)
_OsResourceTcamTable_Object = MibTable
osResourceTcamTable = _OsResourceTcamTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1)
)
if mibBuilder.loadTexts:
    osResourceTcamTable.setStatus("current")
_OsResourceTcamEntry_Object = MibTableRow
osResourceTcamEntry = _OsResourceTcamEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1, 1)
)
osResourceTcamEntry.setIndexNames(
    (0, "OS-RESOURCES-MIB", "osResourceTcamId"),
)
if mibBuilder.loadTexts:
    osResourceTcamEntry.setStatus("current")


class _OsResourceTcamId_Type(Integer32):
    """Custom type osResourceTcamId based on Integer32"""
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
        *(("tunneling", 1),
          ("ingressOam", 2),
          ("ingressAcl", 3),
          ("egressAclOam", 4),
          ("ingressBfd", 5))
    )


_OsResourceTcamId_Type.__name__ = "Integer32"
_OsResourceTcamId_Object = MibTableColumn
osResourceTcamId = _OsResourceTcamId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1, 1, 1),
    _OsResourceTcamId_Type()
)
osResourceTcamId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osResourceTcamId.setStatus("current")
_OsResourceTcamRulesSize_Type = Unsigned32
_OsResourceTcamRulesSize_Object = MibTableColumn
osResourceTcamRulesSize = _OsResourceTcamRulesSize_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1, 1, 3),
    _OsResourceTcamRulesSize_Type()
)
osResourceTcamRulesSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTcamRulesSize.setStatus("current")
_OsResourceTcamRulesGuaranteed_Type = Unsigned32
_OsResourceTcamRulesGuaranteed_Object = MibTableColumn
osResourceTcamRulesGuaranteed = _OsResourceTcamRulesGuaranteed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1, 1, 4),
    _OsResourceTcamRulesGuaranteed_Type()
)
osResourceTcamRulesGuaranteed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTcamRulesGuaranteed.setStatus("current")
_OsResourceTcamRulesUsed_Type = Unsigned32
_OsResourceTcamRulesUsed_Object = MibTableColumn
osResourceTcamRulesUsed = _OsResourceTcamRulesUsed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1, 1, 5),
    _OsResourceTcamRulesUsed_Type()
)
osResourceTcamRulesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTcamRulesUsed.setStatus("current")
_OsResourceTcamRulesFreeGuaranteed_Type = Unsigned32
_OsResourceTcamRulesFreeGuaranteed_Object = MibTableColumn
osResourceTcamRulesFreeGuaranteed = _OsResourceTcamRulesFreeGuaranteed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1, 1, 6),
    _OsResourceTcamRulesFreeGuaranteed_Type()
)
osResourceTcamRulesFreeGuaranteed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTcamRulesFreeGuaranteed.setStatus("current")
_OsResourceTcamRulesFreeOptional_Type = Unsigned32
_OsResourceTcamRulesFreeOptional_Object = MibTableColumn
osResourceTcamRulesFreeOptional = _OsResourceTcamRulesFreeOptional_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 1, 1, 7),
    _OsResourceTcamRulesFreeOptional_Type()
)
osResourceTcamRulesFreeOptional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTcamRulesFreeOptional.setStatus("current")
_OsResourcePolicerTable_Object = MibTable
osResourcePolicerTable = _OsResourcePolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 2)
)
if mibBuilder.loadTexts:
    osResourcePolicerTable.setStatus("current")
_OsResourcePolicerEntry_Object = MibTableRow
osResourcePolicerEntry = _OsResourcePolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 2, 1)
)
osResourcePolicerEntry.setIndexNames(
    (0, "OS-RESOURCES-MIB", "osResourcePolicerType"),
)
if mibBuilder.loadTexts:
    osResourcePolicerEntry.setStatus("current")


class _OsResourcePolicerType_Type(Integer32):
    """Custom type osResourcePolicerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingressAcl", 1),
          ("egressAcl", 2))
    )


_OsResourcePolicerType_Type.__name__ = "Integer32"
_OsResourcePolicerType_Object = MibTableColumn
osResourcePolicerType = _OsResourcePolicerType_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 2, 1, 1),
    _OsResourcePolicerType_Type()
)
osResourcePolicerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osResourcePolicerType.setStatus("current")
_OsResourcePolicerEntriesTotal_Type = Unsigned32
_OsResourcePolicerEntriesTotal_Object = MibTableColumn
osResourcePolicerEntriesTotal = _OsResourcePolicerEntriesTotal_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 2, 1, 3),
    _OsResourcePolicerEntriesTotal_Type()
)
osResourcePolicerEntriesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourcePolicerEntriesTotal.setStatus("current")
_OsResourcePolicerEntriesUsed_Type = Unsigned32
_OsResourcePolicerEntriesUsed_Object = MibTableColumn
osResourcePolicerEntriesUsed = _OsResourcePolicerEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 2, 1, 4),
    _OsResourcePolicerEntriesUsed_Type()
)
osResourcePolicerEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourcePolicerEntriesUsed.setStatus("current")
_OsResourcePolicerEntriesFree_Type = Unsigned32
_OsResourcePolicerEntriesFree_Object = MibTableColumn
osResourcePolicerEntriesFree = _OsResourcePolicerEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 2, 1, 5),
    _OsResourcePolicerEntriesFree_Type()
)
osResourcePolicerEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourcePolicerEntriesFree.setStatus("current")
_OsResourceTxSdmaTable_Object = MibTable
osResourceTxSdmaTable = _OsResourceTxSdmaTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 3)
)
if mibBuilder.loadTexts:
    osResourceTxSdmaTable.setStatus("current")
_OsResourceTxSdmaEntry_Object = MibTableRow
osResourceTxSdmaEntry = _OsResourceTxSdmaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 3, 1)
)
osResourceTxSdmaEntry.setIndexNames(
    (0, "OS-RESOURCES-MIB", "osResourceTxSdmaId"),
)
if mibBuilder.loadTexts:
    osResourceTxSdmaEntry.setStatus("current")
_OsResourceTxSdmaId_Type = Unsigned32
_OsResourceTxSdmaId_Object = MibTableColumn
osResourceTxSdmaId = _OsResourceTxSdmaId_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 3, 1, 1),
    _OsResourceTxSdmaId_Type()
)
osResourceTxSdmaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osResourceTxSdmaId.setStatus("current")


class _OsResourceTxSdmaMode_Type(Integer32):
    """Custom type osResourceTxSdmaMode based on Integer32"""
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
          ("periodic", 2),
          ("rate", 3))
    )


_OsResourceTxSdmaMode_Type.__name__ = "Integer32"
_OsResourceTxSdmaMode_Object = MibTableColumn
osResourceTxSdmaMode = _OsResourceTxSdmaMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 3, 1, 2),
    _OsResourceTxSdmaMode_Type()
)
osResourceTxSdmaMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTxSdmaMode.setStatus("current")
_OsResourceTxSdmaInterval_Type = Unsigned32
_OsResourceTxSdmaInterval_Object = MibTableColumn
osResourceTxSdmaInterval = _OsResourceTxSdmaInterval_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 3, 1, 3),
    _OsResourceTxSdmaInterval_Type()
)
osResourceTxSdmaInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTxSdmaInterval.setStatus("current")
_OsResourceTxSdmaUsers_Type = Unsigned32
_OsResourceTxSdmaUsers_Object = MibTableColumn
osResourceTxSdmaUsers = _OsResourceTxSdmaUsers_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 2, 3, 1, 4),
    _OsResourceTxSdmaUsers_Type()
)
osResourceTxSdmaUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceTxSdmaUsers.setStatus("current")
_OsResourcesMac_ObjectIdentity = ObjectIdentity
osResourcesMac = _OsResourcesMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 3)
)
_OsResourceMacEntriesTotal_Type = Unsigned32
_OsResourceMacEntriesTotal_Object = MibScalar
osResourceMacEntriesTotal = _OsResourceMacEntriesTotal_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 3, 1),
    _OsResourceMacEntriesTotal_Type()
)
osResourceMacEntriesTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceMacEntriesTotal.setStatus("current")
_OsResourceMacEntriesUsed_Type = Unsigned32
_OsResourceMacEntriesUsed_Object = MibScalar
osResourceMacEntriesUsed = _OsResourceMacEntriesUsed_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 3, 2),
    _OsResourceMacEntriesUsed_Type()
)
osResourceMacEntriesUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceMacEntriesUsed.setStatus("current")
_OsResourceMacEntriesFree_Type = Unsigned32
_OsResourceMacEntriesFree_Object = MibScalar
osResourceMacEntriesFree = _OsResourceMacEntriesFree_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 3, 3),
    _OsResourceMacEntriesFree_Type()
)
osResourceMacEntriesFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osResourceMacEntriesFree.setStatus("current")
_OsResourcesConformance_ObjectIdentity = ObjectIdentity
osResourcesConformance = _OsResourcesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 100)
)
_OsResourcesMIBCompliances_ObjectIdentity = ObjectIdentity
osResourcesMIBCompliances = _OsResourcesMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 100, 1)
)
_OsResourcesMIBGroups_ObjectIdentity = ObjectIdentity
osResourcesMIBGroups = _OsResourcesMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 100, 2)
)

# Managed Objects groups

osResourceMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 100, 2, 1)
)
osResourceMandatoryGroup.setObjects(
    ("OS-RESOURCES-MIB", "osResourcesSupport")
)
if mibBuilder.loadTexts:
    osResourceMandatoryGroup.setStatus("current")

osResourceOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 100, 2, 2)
)
osResourceOptGroup.setObjects(
      *(("OS-RESOURCES-MIB", "osResourcesSupport"),
        ("OS-RESOURCES-MIB", "osResourceTcamRulesSize"),
        ("OS-RESOURCES-MIB", "osResourceTcamRulesGuaranteed"),
        ("OS-RESOURCES-MIB", "osResourceTcamRulesUsed"),
        ("OS-RESOURCES-MIB", "osResourceTcamRulesFreeGuaranteed"),
        ("OS-RESOURCES-MIB", "osResourceTcamRulesFreeOptional"),
        ("OS-RESOURCES-MIB", "osResourcePolicerEntriesTotal"),
        ("OS-RESOURCES-MIB", "osResourcePolicerEntriesUsed"),
        ("OS-RESOURCES-MIB", "osResourcePolicerEntriesFree"),
        ("OS-RESOURCES-MIB", "osResourceMacEntriesTotal"),
        ("OS-RESOURCES-MIB", "osResourceMacEntriesUsed"),
        ("OS-RESOURCES-MIB", "osResourceMacEntriesFree"),
        ("OS-RESOURCES-MIB", "osResourceTxSdmaMode"),
        ("OS-RESOURCES-MIB", "osResourceTxSdmaInterval"),
        ("OS-RESOURCES-MIB", "osResourceTxSdmaUsers"))
)
if mibBuilder.loadTexts:
    osResourceOptGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osResourceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 41, 100, 1, 1)
)
osResourceMIBCompliance.setObjects(
      *(("OS-RESOURCES-MIB", "osResourceMandatoryGroup"),
        ("OS-RESOURCES-MIB", "osResourceOptGroup"))
)
if mibBuilder.loadTexts:
    osResourceMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-RESOURCES-MIB",
    **{"osResources": osResources,
       "osResourcesGen": osResourcesGen,
       "osResourcesSupport": osResourcesSupport,
       "osResourcesTables": osResourcesTables,
       "osResourceTcamTable": osResourceTcamTable,
       "osResourceTcamEntry": osResourceTcamEntry,
       "osResourceTcamId": osResourceTcamId,
       "osResourceTcamRulesSize": osResourceTcamRulesSize,
       "osResourceTcamRulesGuaranteed": osResourceTcamRulesGuaranteed,
       "osResourceTcamRulesUsed": osResourceTcamRulesUsed,
       "osResourceTcamRulesFreeGuaranteed": osResourceTcamRulesFreeGuaranteed,
       "osResourceTcamRulesFreeOptional": osResourceTcamRulesFreeOptional,
       "osResourcePolicerTable": osResourcePolicerTable,
       "osResourcePolicerEntry": osResourcePolicerEntry,
       "osResourcePolicerType": osResourcePolicerType,
       "osResourcePolicerEntriesTotal": osResourcePolicerEntriesTotal,
       "osResourcePolicerEntriesUsed": osResourcePolicerEntriesUsed,
       "osResourcePolicerEntriesFree": osResourcePolicerEntriesFree,
       "osResourceTxSdmaTable": osResourceTxSdmaTable,
       "osResourceTxSdmaEntry": osResourceTxSdmaEntry,
       "osResourceTxSdmaId": osResourceTxSdmaId,
       "osResourceTxSdmaMode": osResourceTxSdmaMode,
       "osResourceTxSdmaInterval": osResourceTxSdmaInterval,
       "osResourceTxSdmaUsers": osResourceTxSdmaUsers,
       "osResourcesMac": osResourcesMac,
       "osResourceMacEntriesTotal": osResourceMacEntriesTotal,
       "osResourceMacEntriesUsed": osResourceMacEntriesUsed,
       "osResourceMacEntriesFree": osResourceMacEntriesFree,
       "osResourcesConformance": osResourcesConformance,
       "osResourcesMIBCompliances": osResourcesMIBCompliances,
       "osResourceMIBCompliance": osResourceMIBCompliance,
       "osResourcesMIBGroups": osResourcesMIBGroups,
       "osResourceMandatoryGroup": osResourceMandatoryGroup,
       "osResourceOptGroup": osResourceOptGroup}
)
