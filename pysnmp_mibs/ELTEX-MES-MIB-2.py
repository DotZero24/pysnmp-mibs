# SNMP MIB module (ELTEX-MES-MIB-2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-MIB-2
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:13 2025
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

(eltMesMng,) = mibBuilder.importSymbols(
    "ELTEX-MES",
    "eltMesMng")

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

elt_mes_mib_2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIfMIB_ObjectIdentity = ObjectIdentity
eltMesIfMIB = _EltMesIfMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 31)
)
_EltMesSystem_ObjectIdentity = ObjectIdentity
eltMesSystem = _EltMesSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 32)
)


class _EltSysDescr_Type(DisplayString):
    """Custom type eltSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltSysDescr_Type.__name__ = "DisplayString"
_EltSysDescr_Object = MibScalar
eltSysDescr = _EltSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 23, 1, 1, 32, 1),
    _EltSysDescr_Type()
)
eltSysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltSysDescr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-MIB-2",
    **{"elt-mes-mib-2": elt_mes_mib_2,
       "eltMesIfMIB": eltMesIfMIB,
       "eltMesSystem": eltMesSystem,
       "eltSysDescr": eltSysDescr}
)
