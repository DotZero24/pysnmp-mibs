# SNMP MIB module (ELTEX-MES-ISS-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-LLDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:27 2025
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

eltMesIssLldpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 10)
)
if mibBuilder.loadTexts:
    eltMesIssLldpMIB.setRevisions(
        ("2019-02-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssLldpObjects_ObjectIdentity = ObjectIdentity
eltMesIssLldpObjects = _EltMesIssLldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1)
)
_EltMesIssLldpGlobalConfig_ObjectIdentity = ObjectIdentity
eltMesIssLldpGlobalConfig = _EltMesIssLldpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1, 1)
)


class _EltMesIssLldpduMode_Type(Integer32):
    """Custom type eltMesIssLldpduMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filtering", 1),
          ("flooding", 2))
    )


_EltMesIssLldpduMode_Type.__name__ = "Integer32"
_EltMesIssLldpduMode_Object = MibScalar
eltMesIssLldpduMode = _EltMesIssLldpduMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 10, 1, 1, 1),
    _EltMesIssLldpduMode_Type()
)
eltMesIssLldpduMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssLldpduMode.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-LLDP-MIB",
    **{"eltMesIssLldpMIB": eltMesIssLldpMIB,
       "eltMesIssLldpObjects": eltMesIssLldpObjects,
       "eltMesIssLldpGlobalConfig": eltMesIssLldpGlobalConfig,
       "eltMesIssLldpduMode": eltMesIssLldpduMode}
)
