# SNMP MIB module (HPICF-ACTIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPICF-ACTIVATE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:36:36 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

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

hpicfActivateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129)
)
if mibBuilder.loadTexts:
    hpicfActivateMIB.setRevisions(
        ("2020-06-20 00:00",
         "2016-05-03 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfActivateObjects_ObjectIdentity = ObjectIdentity
hpicfActivateObjects = _HpicfActivateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1)
)


class _HpicfActivateSoftwareUpdateMode_Type(TruthValue):
    """Custom type hpicfActivateSoftwareUpdateMode based on TruthValue"""
    defaultValue = 1


_HpicfActivateSoftwareUpdateMode_Type.__name__ = "TruthValue"
_HpicfActivateSoftwareUpdateMode_Object = MibScalar
hpicfActivateSoftwareUpdateMode = _HpicfActivateSoftwareUpdateMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 1),
    _HpicfActivateSoftwareUpdateMode_Type()
)
hpicfActivateSoftwareUpdateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfActivateSoftwareUpdateMode.setStatus("current")


class _HpicfActivateProvisionMode_Type(TruthValue):
    """Custom type hpicfActivateProvisionMode based on TruthValue"""
    defaultValue = 1


_HpicfActivateProvisionMode_Type.__name__ = "TruthValue"
_HpicfActivateProvisionMode_Object = MibScalar
hpicfActivateProvisionMode = _HpicfActivateProvisionMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 2),
    _HpicfActivateProvisionMode_Type()
)
hpicfActivateProvisionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfActivateProvisionMode.setStatus("current")


class _HpicfActivateOverrideConfigCheck_Type(TruthValue):
    """Custom type hpicfActivateOverrideConfigCheck based on TruthValue"""
    defaultValue = 2


_HpicfActivateOverrideConfigCheck_Type.__name__ = "TruthValue"
_HpicfActivateOverrideConfigCheck_Object = MibScalar
hpicfActivateOverrideConfigCheck = _HpicfActivateOverrideConfigCheck_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 1, 3),
    _HpicfActivateOverrideConfigCheck_Type()
)
hpicfActivateOverrideConfigCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfActivateOverrideConfigCheck.setStatus("current")
_HpicfActivateConformance_ObjectIdentity = ObjectIdentity
hpicfActivateConformance = _HpicfActivateConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2)
)
_HpicfActivateMIBCompliances_ObjectIdentity = ObjectIdentity
hpicfActivateMIBCompliances = _HpicfActivateMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1)
)
_HpicfActivateMIBGroups_ObjectIdentity = ObjectIdentity
hpicfActivateMIBGroups = _HpicfActivateMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2)
)

# Managed Objects groups

hpicfActivateConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2, 1)
)
hpicfActivateConfigGroup.setObjects(
      *(("HPICF-ACTIVATE-MIB", "hpicfActivateSoftwareUpdateMode"),
        ("HPICF-ACTIVATE-MIB", "hpicfActivateProvisionMode"))
)
if mibBuilder.loadTexts:
    hpicfActivateConfigGroup.setStatus("deprecated")

hpicfActivateConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 2, 2)
)
hpicfActivateConfigGroup1.setObjects(
      *(("HPICF-ACTIVATE-MIB", "hpicfActivateSoftwareUpdateMode"),
        ("HPICF-ACTIVATE-MIB", "hpicfActivateProvisionMode"),
        ("HPICF-ACTIVATE-MIB", "hpicfActivateOverrideConfigCheck"))
)
if mibBuilder.loadTexts:
    hpicfActivateConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfActivateMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1, 1)
)
hpicfActivateMIBCompliance.setObjects(
    ("HPICF-ACTIVATE-MIB", "hpicfActivateConfigGroup")
)
if mibBuilder.loadTexts:
    hpicfActivateMIBCompliance.setStatus(
        "deprecated"
    )

hpicfActivateMIBCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 129, 2, 1, 2)
)
hpicfActivateMIBCompliance1.setObjects(
    ("HPICF-ACTIVATE-MIB", "hpicfActivateConfigGroup1")
)
if mibBuilder.loadTexts:
    hpicfActivateMIBCompliance1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPICF-ACTIVATE-MIB",
    **{"hpicfActivateMIB": hpicfActivateMIB,
       "hpicfActivateObjects": hpicfActivateObjects,
       "hpicfActivateSoftwareUpdateMode": hpicfActivateSoftwareUpdateMode,
       "hpicfActivateProvisionMode": hpicfActivateProvisionMode,
       "hpicfActivateOverrideConfigCheck": hpicfActivateOverrideConfigCheck,
       "hpicfActivateConformance": hpicfActivateConformance,
       "hpicfActivateMIBCompliances": hpicfActivateMIBCompliances,
       "hpicfActivateMIBCompliance": hpicfActivateMIBCompliance,
       "hpicfActivateMIBCompliance1": hpicfActivateMIBCompliance1,
       "hpicfActivateMIBGroups": hpicfActivateMIBGroups,
       "hpicfActivateConfigGroup": hpicfActivateConfigGroup,
       "hpicfActivateConfigGroup1": hpicfActivateConfigGroup1}
)
