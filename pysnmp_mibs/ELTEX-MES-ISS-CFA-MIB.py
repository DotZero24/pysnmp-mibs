# SNMP MIB module (ELTEX-MES-ISS-CFA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-CFA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:48:55 2025
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

eltMesIssCfaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 20)
)
if mibBuilder.loadTexts:
    eltMesIssCfaMIB.setRevisions(
        ("2020-05-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssCfaObjects_ObjectIdentity = ObjectIdentity
eltMesIssCfaObjects = _EltMesIssCfaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1)
)
_EltMesIssCfaGlobals_ObjectIdentity = ObjectIdentity
eltMesIssCfaGlobals = _EltMesIssCfaGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1, 1)
)


class _EltMesIssCfaGlobalMtu_Type(Integer32):
    """Custom type eltMesIssCfaGlobalMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 12288),
    )


_EltMesIssCfaGlobalMtu_Type.__name__ = "Integer32"
_EltMesIssCfaGlobalMtu_Object = MibScalar
eltMesIssCfaGlobalMtu = _EltMesIssCfaGlobalMtu_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 1, 1, 1),
    _EltMesIssCfaGlobalMtu_Type()
)
eltMesIssCfaGlobalMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssCfaGlobalMtu.setStatus("current")
_EltMesIssCfaNotifications_ObjectIdentity = ObjectIdentity
eltMesIssCfaNotifications = _EltMesIssCfaNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 20, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-CFA-MIB",
    **{"eltMesIssCfaMIB": eltMesIssCfaMIB,
       "eltMesIssCfaObjects": eltMesIssCfaObjects,
       "eltMesIssCfaGlobals": eltMesIssCfaGlobals,
       "eltMesIssCfaGlobalMtu": eltMesIssCfaGlobalMtu,
       "eltMesIssCfaNotifications": eltMesIssCfaNotifications}
)
