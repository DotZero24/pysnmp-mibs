# SNMP MIB module (ELECTROLINE-COMMON-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-COMMON-ROOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:09 2025
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

(electrolineHardwareProducts,) = mibBuilder.importSymbols(
    "ELECTROLINE-GLOBAL-REG",
    "electrolineHardwareProducts")

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

electrolineCommon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    electrolineCommon.setRevisions(
        ("2014-01-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CommonInventory_ObjectIdentity = ObjectIdentity
commonInventory = _CommonInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 1)
)
if mibBuilder.loadTexts:
    commonInventory.setStatus("current")
_CommonConfiguration_ObjectIdentity = ObjectIdentity
commonConfiguration = _CommonConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2)
)
if mibBuilder.loadTexts:
    commonConfiguration.setStatus("current")
_CommonStatus_ObjectIdentity = ObjectIdentity
commonStatus = _CommonStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 3)
)
if mibBuilder.loadTexts:
    commonStatus.setStatus("current")
_CommonPrivate_ObjectIdentity = ObjectIdentity
commonPrivate = _CommonPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 4)
)
if mibBuilder.loadTexts:
    commonPrivate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-COMMON-ROOT-MIB",
    **{"electrolineCommon": electrolineCommon,
       "commonInventory": commonInventory,
       "commonConfiguration": commonConfiguration,
       "commonStatus": commonStatus,
       "commonPrivate": commonPrivate}
)
