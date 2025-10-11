# SNMP MIB module (BRCM-HOMEPLUG-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-HOMEPLUG-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:48 2025
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

(cableDataFactory,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    "cableDataFactory")

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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

homeplugFactory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9)
)
if mibBuilder.loadTexts:
    homeplugFactory.setRevisions(
        ("2004-12-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HomeplugFactMacAddress_Type = MacAddress
_HomeplugFactMacAddress_Object = MibScalar
homeplugFactMacAddress = _HomeplugFactMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9, 1),
    _HomeplugFactMacAddress_Type()
)
homeplugFactMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    homeplugFactMacAddress.setStatus("current")


class _HomeplugFactDEKPassword_Type(DisplayString):
    """Custom type homeplugFactDEKPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 24),
    )


_HomeplugFactDEKPassword_Type.__name__ = "DisplayString"
_HomeplugFactDEKPassword_Object = MibScalar
homeplugFactDEKPassword = _HomeplugFactDEKPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9, 2),
    _HomeplugFactDEKPassword_Type()
)
homeplugFactDEKPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    homeplugFactDEKPassword.setStatus("current")


class _HomeplugFactNEKPassword_Type(DisplayString):
    """Custom type homeplugFactNEKPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 24),
    )


_HomeplugFactNEKPassword_Type.__name__ = "DisplayString"
_HomeplugFactNEKPassword_Object = MibScalar
homeplugFactNEKPassword = _HomeplugFactNEKPassword_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 9, 3),
    _HomeplugFactNEKPassword_Type()
)
homeplugFactNEKPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    homeplugFactNEKPassword.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-HOMEPLUG-FACTORY-MIB",
    **{"homeplugFactory": homeplugFactory,
       "homeplugFactMacAddress": homeplugFactMacAddress,
       "homeplugFactDEKPassword": homeplugFactDEKPassword,
       "homeplugFactNEKPassword": homeplugFactNEKPassword}
)
