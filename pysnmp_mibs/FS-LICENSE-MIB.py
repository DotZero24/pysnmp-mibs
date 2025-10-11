# SNMP MIB module (FS-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-LICENSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:12 2025
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

fsLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57)
)
if mibBuilder.loadTexts:
    fsLicenseMIB.setRevisions(
        ("2009-09-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsLicenseMIBObjects_ObjectIdentity = ObjectIdentity
fsLicenseMIBObjects = _FsLicenseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1)
)
_FsShowLicense_Type = Integer32
_FsShowLicense_Object = MibScalar
fsShowLicense = _FsShowLicense_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 1),
    _FsShowLicense_Type()
)
fsShowLicense.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsShowLicense.setStatus("current")
_FsLicenseTable_Object = MibTable
fsLicenseTable = _FsLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2)
)
if mibBuilder.loadTexts:
    fsLicenseTable.setStatus("current")
_FsLicenseEntry_Object = MibTableRow
fsLicenseEntry = _FsLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1)
)
fsLicenseEntry.setIndexNames(
    (0, "FS-LICENSE-MIB", "fsLicenseIndex"),
)
if mibBuilder.loadTexts:
    fsLicenseEntry.setStatus("current")
_FsLicenseIndex_Type = Integer32
_FsLicenseIndex_Object = MibTableColumn
fsLicenseIndex = _FsLicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1, 1),
    _FsLicenseIndex_Type()
)
fsLicenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsLicenseIndex.setStatus("current")
_FsLicenseString_Type = DisplayString
_FsLicenseString_Object = MibTableColumn
fsLicenseString = _FsLicenseString_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1, 2),
    _FsLicenseString_Type()
)
fsLicenseString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLicenseString.setStatus("current")
_FsLicenseValue_Type = Integer32
_FsLicenseValue_Object = MibTableColumn
fsLicenseValue = _FsLicenseValue_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 1, 2, 1, 3),
    _FsLicenseValue_Type()
)
fsLicenseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLicenseValue.setStatus("current")
_FsLicenseMIBConformance_ObjectIdentity = ObjectIdentity
fsLicenseMIBConformance = _FsLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2)
)
_FsLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
fsLicenseMIBCompliances = _FsLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 1)
)
_FsLicenseMIBGroups_ObjectIdentity = ObjectIdentity
fsLicenseMIBGroups = _FsLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 2)
)

# Managed Objects groups

fsLicenseMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 2, 1)
)
fsLicenseMIBGroup.setObjects(
      *(("FS-LICENSE-MIB", "fsShowLicense"),
        ("FS-LICENSE-MIB", "fsLicenseString"),
        ("FS-LICENSE-MIB", "fsLicenseValue"))
)
if mibBuilder.loadTexts:
    fsLicenseMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsLicenseMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 57, 2, 1, 1)
)
fsLicenseMIBCompliance.setObjects(
    ("FS-LICENSE-MIB", "fsLicenseMIBGroup")
)
if mibBuilder.loadTexts:
    fsLicenseMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-LICENSE-MIB",
    **{"fsLicenseMIB": fsLicenseMIB,
       "fsLicenseMIBObjects": fsLicenseMIBObjects,
       "fsShowLicense": fsShowLicense,
       "fsLicenseTable": fsLicenseTable,
       "fsLicenseEntry": fsLicenseEntry,
       "fsLicenseIndex": fsLicenseIndex,
       "fsLicenseString": fsLicenseString,
       "fsLicenseValue": fsLicenseValue,
       "fsLicenseMIBConformance": fsLicenseMIBConformance,
       "fsLicenseMIBCompliances": fsLicenseMIBCompliances,
       "fsLicenseMIBCompliance": fsLicenseMIBCompliance,
       "fsLicenseMIBGroups": fsLicenseMIBGroups,
       "fsLicenseMIBGroup": fsLicenseMIBGroup}
)
