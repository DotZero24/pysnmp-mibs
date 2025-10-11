# SNMP MIB module (RDN-CHASSIS-TYPE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/riverdelta/RDN-CHASSIS-TYPE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:03:21 2025
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

(rdnDefinitions,) = mibBuilder.importSymbols(
    "RDN-DEFINITIONS-MIB",
    "rdnDefinitions")

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

rdnChassisTypes = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 2)
)
if mibBuilder.loadTexts:
    rdnChassisTypes.setRevisions(
        ("2008-08-08 00:00",
         "2003-11-05 00:00",
         "2003-04-29 00:00",
         "2001-04-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RdnChassisTypesUnknown_ObjectIdentity = ObjectIdentity
rdnChassisTypesUnknown = _RdnChassisTypesUnknown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 2, 0)
)
_RdnChassisTypesBSR64000_ObjectIdentity = ObjectIdentity
rdnChassisTypesBSR64000 = _RdnChassisTypesBSR64000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 2, 1)
)
_RdnChassisTypesBSR1000_ObjectIdentity = ObjectIdentity
rdnChassisTypesBSR1000 = _RdnChassisTypesBSR1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 2, 2)
)
_RdnChassisTypesOSR2000_ObjectIdentity = ObjectIdentity
rdnChassisTypesOSR2000 = _RdnChassisTypesOSR2000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4981, 4, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RDN-CHASSIS-TYPE-MIB",
    **{"rdnChassisTypes": rdnChassisTypes,
       "rdnChassisTypesUnknown": rdnChassisTypesUnknown,
       "rdnChassisTypesBSR64000": rdnChassisTypesBSR64000,
       "rdnChassisTypesBSR1000": rdnChassisTypesBSR1000,
       "rdnChassisTypesOSR2000": rdnChassisTypesOSR2000}
)
