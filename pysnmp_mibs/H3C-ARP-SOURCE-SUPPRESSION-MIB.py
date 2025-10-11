# SNMP MIB module (H3C-ARP-SOURCE-SUPPRESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:36 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cARPSourceSuppression = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 146)
)
if mibBuilder.loadTexts:
    h3cARPSourceSuppression.setRevisions(
        ("2013-10-14 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cARPSourceSuppressionObjects_ObjectIdentity = ObjectIdentity
h3cARPSourceSuppressionObjects = _H3cARPSourceSuppressionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1)
)
_H3cARPSourceSuppressionGlobal_ObjectIdentity = ObjectIdentity
h3cARPSourceSuppressionGlobal = _H3cARPSourceSuppressionGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1)
)
_H3cARPSourceSuppressionEnable_Type = TruthValue
_H3cARPSourceSuppressionEnable_Object = MibScalar
h3cARPSourceSuppressionEnable = _H3cARPSourceSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1, 1),
    _H3cARPSourceSuppressionEnable_Type()
)
h3cARPSourceSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cARPSourceSuppressionEnable.setStatus("current")


class _H3cARPSourceSuppressionLimit_Type(Unsigned32):
    """Custom type h3cARPSourceSuppressionLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_H3cARPSourceSuppressionLimit_Type.__name__ = "Unsigned32"
_H3cARPSourceSuppressionLimit_Object = MibScalar
h3cARPSourceSuppressionLimit = _H3cARPSourceSuppressionLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 146, 1, 1, 2),
    _H3cARPSourceSuppressionLimit_Type()
)
h3cARPSourceSuppressionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cARPSourceSuppressionLimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-ARP-SOURCE-SUPPRESSION-MIB",
    **{"h3cARPSourceSuppression": h3cARPSourceSuppression,
       "h3cARPSourceSuppressionObjects": h3cARPSourceSuppressionObjects,
       "h3cARPSourceSuppressionGlobal": h3cARPSourceSuppressionGlobal,
       "h3cARPSourceSuppressionEnable": h3cARPSourceSuppressionEnable,
       "h3cARPSourceSuppressionLimit": h3cARPSourceSuppressionLimit}
)
