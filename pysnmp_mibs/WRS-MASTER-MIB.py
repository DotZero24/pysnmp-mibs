# SNMP MIB module (WRS-MASTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/WRS-MASTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:14 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

zte = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
if mibBuilder.loadTexts:
    zte.setRevisions(
        ("1901-10-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxEdsl_ObjectIdentity = ObjectIdentity
zxEdsl = _ZxEdsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008)
)
_ZxEdslOwn_ObjectIdentity = ObjectIdentity
zxEdslOwn = _ZxEdslOwn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1)
)
_ZxEdslLR1_ObjectIdentity = ObjectIdentity
zxEdslLR1 = _ZxEdslLR1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1)
)
_Tms_ObjectIdentity = ObjectIdentity
tms = _Tms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1)
)
_Idb_ObjectIdentity = ObjectIdentity
idb = _Idb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 1)
)
_RmonMib_ObjectIdentity = ObjectIdentity
rmonMib = _RmonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 1, 1)
)
_TmsGeneric_ObjectIdentity = ObjectIdentity
tmsGeneric = _TmsGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 2)
)
_OemSwapi_ObjectIdentity = ObjectIdentity
oemSwapi = _OemSwapi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 3)
)
_OemProd_ObjectIdentity = ObjectIdentity
oemProd = _OemProd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1008, 1, 1, 1, 4)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WRS-MASTER-MIB",
    **{"zte": zte,
       "zxEdsl": zxEdsl,
       "zxEdslOwn": zxEdslOwn,
       "zxEdslLR1": zxEdslLR1,
       "tms": tms,
       "idb": idb,
       "rmonMib": rmonMib,
       "tmsGeneric": tmsGeneric,
       "oemSwapi": oemSwapi,
       "oemProd": oemProd}
)
