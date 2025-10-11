# SNMP MIB module (Juniper-LICENSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/junose/JUNIPER-LICENSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:46 2025
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniLicenseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76)
)
if mibBuilder.loadTexts:
    juniLicenseMIB.setRevisions(
        ("2004-09-14 19:24",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniLicenseObjects_ObjectIdentity = ObjectIdentity
juniLicenseObjects = _JuniLicenseObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1)
)


class _JuniLicenseLineModuleIfLimitKey_Type(DisplayString):
    """Custom type juniLicenseLineModuleIfLimitKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniLicenseLineModuleIfLimitKey_Type.__name__ = "DisplayString"
_JuniLicenseLineModuleIfLimitKey_Object = MibScalar
juniLicenseLineModuleIfLimitKey = _JuniLicenseLineModuleIfLimitKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 1),
    _JuniLicenseLineModuleIfLimitKey_Type()
)
juniLicenseLineModuleIfLimitKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniLicenseLineModuleIfLimitKey.setStatus("current")
_JuniLicenseLineModuleIfLimitValue_Type = Integer32
_JuniLicenseLineModuleIfLimitValue_Object = MibScalar
juniLicenseLineModuleIfLimitValue = _JuniLicenseLineModuleIfLimitValue_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 1, 2),
    _JuniLicenseLineModuleIfLimitValue_Type()
)
juniLicenseLineModuleIfLimitValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniLicenseLineModuleIfLimitValue.setStatus("current")
_JuniLicenseMIBConformance_ObjectIdentity = ObjectIdentity
juniLicenseMIBConformance = _JuniLicenseMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2)
)
_JuniLicenseMIBCompliances_ObjectIdentity = ObjectIdentity
juniLicenseMIBCompliances = _JuniLicenseMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1)
)
_JuniLicenseMIBGroups_ObjectIdentity = ObjectIdentity
juniLicenseMIBGroups = _JuniLicenseMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2)
)

# Managed Objects groups

juniLicenseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 2, 1)
)
juniLicenseGroup.setObjects(
      *(("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitKey"),
        ("Juniper-LICENSE-MIB", "juniLicenseLineModuleIfLimitValue"))
)
if mibBuilder.loadTexts:
    juniLicenseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniLicenseCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 76, 2, 1, 1)
)
juniLicenseCompliance.setObjects(
    ("Juniper-LICENSE-MIB", "juniLicenseGroup")
)
if mibBuilder.loadTexts:
    juniLicenseCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-LICENSE-MIB",
    **{"juniLicenseMIB": juniLicenseMIB,
       "juniLicenseObjects": juniLicenseObjects,
       "juniLicenseLineModuleIfLimitKey": juniLicenseLineModuleIfLimitKey,
       "juniLicenseLineModuleIfLimitValue": juniLicenseLineModuleIfLimitValue,
       "juniLicenseMIBConformance": juniLicenseMIBConformance,
       "juniLicenseMIBCompliances": juniLicenseMIBCompliances,
       "juniLicenseCompliance": juniLicenseCompliance,
       "juniLicenseMIBGroups": juniLicenseMIBGroups,
       "juniLicenseGroup": juniLicenseGroup}
)
