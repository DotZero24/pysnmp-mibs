# SNMP MIB module (ELTEX-FASTPATH-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-FASTPATH-INVENTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:30 2025
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

(eltMesFastpath,) = mibBuilder.importSymbols(
    "ELTEX-MES-FASTPATH-MIB",
    "eltMesFastpath")

(agentInventoryUnitEntry,) = mibBuilder.importSymbols(
    "FASTPATH-INVENTORY-MIB",
    "agentInventoryUnitEntry")

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

eltFastpathInventoryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1)
)
if mibBuilder.loadTexts:
    eltFastpathInventoryMIB.setRevisions(
        ("2017-02-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EfpInventoryObjects_ObjectIdentity = ObjectIdentity
efpInventoryObjects = _EfpInventoryObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1)
)
_EfpInventoryGlobals_ObjectIdentity = ObjectIdentity
efpInventoryGlobals = _EfpInventoryGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1)
)
_EfpAgentInventoryUnitTable_Object = MibTable
efpAgentInventoryUnitTable = _EfpAgentInventoryUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    efpAgentInventoryUnitTable.setStatus("current")
_EfpAgentInventoryUnitEntry_Object = MibTableRow
efpAgentInventoryUnitEntry = _EfpAgentInventoryUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    efpAgentInventoryUnitEntry.setStatus("current")


class _EfpAgentInventoryUnitImage1CommitHash_Type(DisplayString):
    """Custom type efpAgentInventoryUnitImage1CommitHash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EfpAgentInventoryUnitImage1CommitHash_Type.__name__ = "DisplayString"
_EfpAgentInventoryUnitImage1CommitHash_Object = MibTableColumn
efpAgentInventoryUnitImage1CommitHash = _EfpAgentInventoryUnitImage1CommitHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 1),
    _EfpAgentInventoryUnitImage1CommitHash_Type()
)
efpAgentInventoryUnitImage1CommitHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryUnitImage1CommitHash.setStatus("current")


class _EfpAgentInventoryUnitImage2CommitHash_Type(DisplayString):
    """Custom type efpAgentInventoryUnitImage2CommitHash based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EfpAgentInventoryUnitImage2CommitHash_Type.__name__ = "DisplayString"
_EfpAgentInventoryUnitImage2CommitHash_Object = MibTableColumn
efpAgentInventoryUnitImage2CommitHash = _EfpAgentInventoryUnitImage2CommitHash_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 2),
    _EfpAgentInventoryUnitImage2CommitHash_Type()
)
efpAgentInventoryUnitImage2CommitHash.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryUnitImage2CommitHash.setStatus("current")


class _EfpAgentInventoryUnitImage1Timestamp_Type(DisplayString):
    """Custom type efpAgentInventoryUnitImage1Timestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EfpAgentInventoryUnitImage1Timestamp_Type.__name__ = "DisplayString"
_EfpAgentInventoryUnitImage1Timestamp_Object = MibTableColumn
efpAgentInventoryUnitImage1Timestamp = _EfpAgentInventoryUnitImage1Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 3),
    _EfpAgentInventoryUnitImage1Timestamp_Type()
)
efpAgentInventoryUnitImage1Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryUnitImage1Timestamp.setStatus("current")


class _EfpAgentInventoryUnitImage2Timestamp_Type(DisplayString):
    """Custom type efpAgentInventoryUnitImage2Timestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EfpAgentInventoryUnitImage2Timestamp_Type.__name__ = "DisplayString"
_EfpAgentInventoryUnitImage2Timestamp_Object = MibTableColumn
efpAgentInventoryUnitImage2Timestamp = _EfpAgentInventoryUnitImage2Timestamp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 4),
    _EfpAgentInventoryUnitImage2Timestamp_Type()
)
efpAgentInventoryUnitImage2Timestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryUnitImage2Timestamp.setStatus("current")


class _EfpAgentInventoryUnitImage1Md5Digest_Type(DisplayString):
    """Custom type efpAgentInventoryUnitImage1Md5Digest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EfpAgentInventoryUnitImage1Md5Digest_Type.__name__ = "DisplayString"
_EfpAgentInventoryUnitImage1Md5Digest_Object = MibTableColumn
efpAgentInventoryUnitImage1Md5Digest = _EfpAgentInventoryUnitImage1Md5Digest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 5),
    _EfpAgentInventoryUnitImage1Md5Digest_Type()
)
efpAgentInventoryUnitImage1Md5Digest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryUnitImage1Md5Digest.setStatus("current")


class _EfpAgentInventoryUnitImage2Md5Digest_Type(DisplayString):
    """Custom type efpAgentInventoryUnitImage2Md5Digest based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_EfpAgentInventoryUnitImage2Md5Digest_Type.__name__ = "DisplayString"
_EfpAgentInventoryUnitImage2Md5Digest_Object = MibTableColumn
efpAgentInventoryUnitImage2Md5Digest = _EfpAgentInventoryUnitImage2Md5Digest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 6),
    _EfpAgentInventoryUnitImage2Md5Digest_Type()
)
efpAgentInventoryUnitImage2Md5Digest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryUnitImage2Md5Digest.setStatus("current")


class _EfpAgentInventoryActiveImage_Type(Integer32):
    """Custom type efpAgentInventoryActiveImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("image1", 2),
          ("image2", 3))
    )


_EfpAgentInventoryActiveImage_Type.__name__ = "Integer32"
_EfpAgentInventoryActiveImage_Object = MibTableColumn
efpAgentInventoryActiveImage = _EfpAgentInventoryActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 7),
    _EfpAgentInventoryActiveImage_Type()
)
efpAgentInventoryActiveImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryActiveImage.setStatus("current")


class _EfpAgentInventoryNextActiveImage_Type(Integer32):
    """Custom type efpAgentInventoryNextActiveImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("image1", 2),
          ("image2", 3))
    )


_EfpAgentInventoryNextActiveImage_Type.__name__ = "Integer32"
_EfpAgentInventoryNextActiveImage_Object = MibTableColumn
efpAgentInventoryNextActiveImage = _EfpAgentInventoryNextActiveImage_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 1, 1, 1, 1, 8),
    _EfpAgentInventoryNextActiveImage_Type()
)
efpAgentInventoryNextActiveImage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    efpAgentInventoryNextActiveImage.setStatus("current")
_EfpInventoryNotifications_ObjectIdentity = ObjectIdentity
efpInventoryNotifications = _EfpInventoryNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 2)
)
_EfpInventoryNotificationsPrefix_ObjectIdentity = ObjectIdentity
efpInventoryNotificationsPrefix = _EfpInventoryNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 2, 0)
)
_EfpInventoryConformance_ObjectIdentity = ObjectIdentity
efpInventoryConformance = _EfpInventoryConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 3)
)
_EfpInventoryCompliances_ObjectIdentity = ObjectIdentity
efpInventoryCompliances = _EfpInventoryCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 3, 1)
)
_EfpInventoryGroups_ObjectIdentity = ObjectIdentity
efpInventoryGroups = _EfpInventoryGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 3, 2)
)
agentInventoryUnitEntry.registerAugmentions(
    ("ELTEX-FASTPATH-INVENTORY-MIB",
     "efpAgentInventoryUnitEntry")
)
efpAgentInventoryUnitEntry.setIndexNames(*agentInventoryUnitEntry.getIndexNames())

# Managed Objects groups

efpInventoryUnitGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 3, 2, 2)
)
efpInventoryUnitGroup.setObjects(
      *(("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryUnitImage1CommitHash"),
        ("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryUnitImage2CommitHash"),
        ("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryUnitImage1Timestamp"),
        ("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryUnitImage2Timestamp"),
        ("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryUnitImage1Md5Digest"),
        ("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryUnitImage2Md5Digest"),
        ("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryActiveImage"),
        ("ELTEX-FASTPATH-INVENTORY-MIB", "efpAgentInventoryNextActiveImage"))
)
if mibBuilder.loadTexts:
    efpInventoryUnitGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

efpInventoryCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 3, 1, 1)
)
efpInventoryCompliance.setObjects(
    ("ELTEX-FASTPATH-INVENTORY-MIB", "efpInventoryUnitGroup")
)
if mibBuilder.loadTexts:
    efpInventoryCompliance.setStatus(
        "obsolete"
    )

efpFastPathInventoryMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 35265, 1, 103, 1, 3, 1, 2)
)
efpFastPathInventoryMIBCompliance2.setObjects(
    ("ELTEX-FASTPATH-INVENTORY-MIB", "efpInventoryUnitGroup")
)
if mibBuilder.loadTexts:
    efpFastPathInventoryMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-FASTPATH-INVENTORY-MIB",
    **{"eltFastpathInventoryMIB": eltFastpathInventoryMIB,
       "efpInventoryObjects": efpInventoryObjects,
       "efpInventoryGlobals": efpInventoryGlobals,
       "efpAgentInventoryUnitTable": efpAgentInventoryUnitTable,
       "efpAgentInventoryUnitEntry": efpAgentInventoryUnitEntry,
       "efpAgentInventoryUnitImage1CommitHash": efpAgentInventoryUnitImage1CommitHash,
       "efpAgentInventoryUnitImage2CommitHash": efpAgentInventoryUnitImage2CommitHash,
       "efpAgentInventoryUnitImage1Timestamp": efpAgentInventoryUnitImage1Timestamp,
       "efpAgentInventoryUnitImage2Timestamp": efpAgentInventoryUnitImage2Timestamp,
       "efpAgentInventoryUnitImage1Md5Digest": efpAgentInventoryUnitImage1Md5Digest,
       "efpAgentInventoryUnitImage2Md5Digest": efpAgentInventoryUnitImage2Md5Digest,
       "efpAgentInventoryActiveImage": efpAgentInventoryActiveImage,
       "efpAgentInventoryNextActiveImage": efpAgentInventoryNextActiveImage,
       "efpInventoryNotifications": efpInventoryNotifications,
       "efpInventoryNotificationsPrefix": efpInventoryNotificationsPrefix,
       "efpInventoryConformance": efpInventoryConformance,
       "efpInventoryCompliances": efpInventoryCompliances,
       "efpInventoryCompliance": efpInventoryCompliance,
       "efpFastPathInventoryMIBCompliance2": efpFastPathInventoryMIBCompliance2,
       "efpInventoryGroups": efpInventoryGroups,
       "efpInventoryUnitGroup": efpInventoryUnitGroup}
)
