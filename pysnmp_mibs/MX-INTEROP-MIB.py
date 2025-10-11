# SNMP MIB module (MX-INTEROP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-INTEROP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:43 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

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

mxInteropMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3)
)
if mibBuilder.loadTexts:
    mxInteropMIB.setRevisions(
        ("1911-01-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MxInteropMIBObjects_ObjectIdentity = ObjectIdentity
mxInteropMIBObjects = _MxInteropMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3, 1)
)


class _MxInteropHttpUAHeaderConfig_Type(OctetString):
    """Custom type mxInteropHttpUAHeaderConfig based on OctetString"""
    defaultValue = OctetString("%product%")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MxInteropHttpUAHeaderConfig_Type.__name__ = "OctetString"
_MxInteropHttpUAHeaderConfig_Object = MibScalar
mxInteropHttpUAHeaderConfig = _MxInteropHttpUAHeaderConfig_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3, 1, 10),
    _MxInteropHttpUAHeaderConfig_Type()
)
mxInteropHttpUAHeaderConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mxInteropHttpUAHeaderConfig.setStatus("current")
_MxInteropConformance_ObjectIdentity = ObjectIdentity
mxInteropConformance = _MxInteropConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3, 2)
)
_MxInteropCompliances_ObjectIdentity = ObjectIdentity
mxInteropCompliances = _MxInteropCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 1)
)
_MxInteropGroups_ObjectIdentity = ObjectIdentity
mxInteropGroups = _MxInteropGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 2)
)

# Managed Objects groups

mxInteropGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 2, 5)
)
mxInteropGroupVer1.setObjects(
    ("MX-INTEROP-MIB", "mxInteropHttpUAHeaderConfig")
)
if mibBuilder.loadTexts:
    mxInteropGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mxInteropBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 3, 2, 1, 1)
)
mxInteropBasicComplVer1.setObjects(
    ("MX-INTEROP-MIB", "mxInteropGroupVer1")
)
if mibBuilder.loadTexts:
    mxInteropBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-INTEROP-MIB",
    **{"mxInteropMIB": mxInteropMIB,
       "mxInteropMIBObjects": mxInteropMIBObjects,
       "mxInteropHttpUAHeaderConfig": mxInteropHttpUAHeaderConfig,
       "mxInteropConformance": mxInteropConformance,
       "mxInteropCompliances": mxInteropCompliances,
       "mxInteropBasicComplVer1": mxInteropBasicComplVer1,
       "mxInteropGroups": mxInteropGroups,
       "mxInteropGroupVer1": mxInteropGroupVer1}
)
