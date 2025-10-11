# SNMP MIB module (MX-PPPOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-PPPOE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:55 2025
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

pppoeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105)
)
if mibBuilder.loadTexts:
    pppoeMIB.setRevisions(
        ("1903-07-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PppoeMIBObjects_ObjectIdentity = ObjectIdentity
pppoeMIBObjects = _PppoeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 1)
)


class _PppoeEnable_Type(MxEnableState):
    """Custom type pppoeEnable based on MxEnableState"""
    defaultValue = 0


_PppoeEnable_Type.__name__ = "MxEnableState"
_PppoeEnable_Object = MibScalar
pppoeEnable = _PppoeEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 1, 5),
    _PppoeEnable_Type()
)
pppoeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeEnable.setStatus("current")


class _PppoeAcName_Type(OctetString):
    """Custom type pppoeAcName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PppoeAcName_Type.__name__ = "OctetString"
_PppoeAcName_Object = MibScalar
pppoeAcName = _PppoeAcName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 1, 10),
    _PppoeAcName_Type()
)
pppoeAcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeAcName.setStatus("current")


class _PppoeServiceName_Type(OctetString):
    """Custom type pppoeServiceName based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PppoeServiceName_Type.__name__ = "OctetString"
_PppoeServiceName_Object = MibScalar
pppoeServiceName = _PppoeServiceName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 1, 15),
    _PppoeServiceName_Type()
)
pppoeServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pppoeServiceName.setStatus("current")
_PppoeConformance_ObjectIdentity = ObjectIdentity
pppoeConformance = _PppoeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 5)
)
_PppoeCompliances_ObjectIdentity = ObjectIdentity
pppoeCompliances = _PppoeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 1)
)
_PppoeGroups_ObjectIdentity = ObjectIdentity
pppoeGroups = _PppoeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 5)
)

# Managed Objects groups

pppoeConnectionCustomizationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 5, 10)
)
pppoeConnectionCustomizationVer1.setObjects(
      *(("MX-PPPOE-MIB", "pppoeEnable"),
        ("MX-PPPOE-MIB", "pppoeAcName"),
        ("MX-PPPOE-MIB", "pppoeServiceName"))
)
if mibBuilder.loadTexts:
    pppoeConnectionCustomizationVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pppoeComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 105, 5, 1, 1)
)
pppoeComplVer1.setObjects(
    ("MX-PPPOE-MIB", "pppoeConnectionCustomizationVer1")
)
if mibBuilder.loadTexts:
    pppoeComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-PPPOE-MIB",
    **{"pppoeMIB": pppoeMIB,
       "pppoeMIBObjects": pppoeMIBObjects,
       "pppoeEnable": pppoeEnable,
       "pppoeAcName": pppoeAcName,
       "pppoeServiceName": pppoeServiceName,
       "pppoeConformance": pppoeConformance,
       "pppoeCompliances": pppoeCompliances,
       "pppoeComplVer1": pppoeComplVer1,
       "pppoeGroups": pppoeGroups,
       "pppoeConnectionCustomizationVer1": pppoeConnectionCustomizationVer1}
)
