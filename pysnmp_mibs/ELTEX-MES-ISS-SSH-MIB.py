# SNMP MIB module (ELTEX-MES-ISS-SSH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-SSH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:59 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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

eltMesIssSshMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 30)
)
if mibBuilder.loadTexts:
    eltMesIssSshMIB.setRevisions(
        ("2022-04-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssSshObjects_ObjectIdentity = ObjectIdentity
eltMesIssSshObjects = _EltMesIssSshObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1)
)
_EltMesIssSshGlobals_ObjectIdentity = ObjectIdentity
eltMesIssSshGlobals = _EltMesIssSshGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1, 1)
)


class _EltMesIssSshAuthTypes_Type(Bits):
    """Custom type eltMesIssSshAuthTypes based on Bits"""
    defaultHexValue = "80"

    namedValues = NamedValues(
        *(("password", 0),
          ("publickey", 1))
    )

_EltMesIssSshAuthTypes_Type.__name__ = "Bits"
_EltMesIssSshAuthTypes_Object = MibScalar
eltMesIssSshAuthTypes = _EltMesIssSshAuthTypes_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 30, 1, 1, 1),
    _EltMesIssSshAuthTypes_Type()
)
eltMesIssSshAuthTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSshAuthTypes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-SSH-MIB",
    **{"eltMesIssSshMIB": eltMesIssSshMIB,
       "eltMesIssSshObjects": eltMesIssSshObjects,
       "eltMesIssSshGlobals": eltMesIssSshGlobals,
       "eltMesIssSshAuthTypes": eltMesIssSshAuthTypes}
)
