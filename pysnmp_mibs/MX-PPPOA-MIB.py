# SNMP MIB module (MX-PPPOA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-PPPOA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:32 2025
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

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

pppoaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350)
)
if mibBuilder.loadTexts:
    pppoaMIB.setRevisions(
        ("2006-03-06 00:00",
         "2005-04-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppoaMIBObjects_ObjectIdentity = ObjectIdentity
pppoaMIBObjects = _PppoaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350, 1)
)


class _PppoaEnable_Type(MxEnableState):
    """Custom type pppoaEnable based on MxEnableState"""
    defaultValue = 0


_PppoaEnable_Type.__name__ = "MxEnableState"
_PppoaEnable_Object = MibScalar
pppoaEnable = _PppoaEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350, 1, 50),
    _PppoaEnable_Type()
)
pppoaEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoaEnable.setStatus("current")
_PppoaConformance_ObjectIdentity = ObjectIdentity
pppoaConformance = _PppoaConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350, 5)
)
_PppoaCompliances_ObjectIdentity = ObjectIdentity
pppoaCompliances = _PppoaCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 1)
)
_PppoaGroups_ObjectIdentity = ObjectIdentity
pppoaGroups = _PppoaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 5)
)

# Managed Objects groups

pppoaConnectionCustomizationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 5, 10)
)
pppoaConnectionCustomizationVer1.setObjects(
    ("MX-PPPOA-MIB", "pppoaEnable")
)
if mibBuilder.loadTexts:
    pppoaConnectionCustomizationVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pppoaComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 350, 5, 1, 1)
)
pppoaComplVer1.setObjects(
    ("MX-PPPOA-MIB", "pppoaConnectionCustomizationVer1")
)
if mibBuilder.loadTexts:
    pppoaComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-PPPOA-MIB",
    **{"pppoaMIB": pppoaMIB,
       "pppoaMIBObjects": pppoaMIBObjects,
       "pppoaEnable": pppoaEnable,
       "pppoaConformance": pppoaConformance,
       "pppoaCompliances": pppoaCompliances,
       "pppoaComplVer1": pppoaComplVer1,
       "pppoaGroups": pppoaGroups,
       "pppoaConnectionCustomizationVer1": pppoaConnectionCustomizationVer1}
)
