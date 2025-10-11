# SNMP MIB module (HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:42:52 2025
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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

hpnicfARPSourceSuppression = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146)
)
if mibBuilder.loadTexts:
    hpnicfARPSourceSuppression.setRevisions(
        ("2013-10-14 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfARPSourceSuppressionObjects_ObjectIdentity = ObjectIdentity
hpnicfARPSourceSuppressionObjects = _HpnicfARPSourceSuppressionObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1)
)
_HpnicfARPSourceSuppressionGlobal_ObjectIdentity = ObjectIdentity
hpnicfARPSourceSuppressionGlobal = _HpnicfARPSourceSuppressionGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1)
)
_HpnicfARPSourceSuppressionEnable_Type = TruthValue
_HpnicfARPSourceSuppressionEnable_Object = MibScalar
hpnicfARPSourceSuppressionEnable = _HpnicfARPSourceSuppressionEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 1),
    _HpnicfARPSourceSuppressionEnable_Type()
)
hpnicfARPSourceSuppressionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfARPSourceSuppressionEnable.setStatus("current")


class _HpnicfARPSourceSuppressionLimit_Type(Unsigned32):
    """Custom type hpnicfARPSourceSuppressionLimit based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 1024),
    )


_HpnicfARPSourceSuppressionLimit_Type.__name__ = "Unsigned32"
_HpnicfARPSourceSuppressionLimit_Object = MibScalar
hpnicfARPSourceSuppressionLimit = _HpnicfARPSourceSuppressionLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 146, 1, 1, 2),
    _HpnicfARPSourceSuppressionLimit_Type()
)
hpnicfARPSourceSuppressionLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfARPSourceSuppressionLimit.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-ARP-SOURCE-SUPPRESSION-MIB",
    **{"hpnicfARPSourceSuppression": hpnicfARPSourceSuppression,
       "hpnicfARPSourceSuppressionObjects": hpnicfARPSourceSuppressionObjects,
       "hpnicfARPSourceSuppressionGlobal": hpnicfARPSourceSuppressionGlobal,
       "hpnicfARPSourceSuppressionEnable": hpnicfARPSourceSuppressionEnable,
       "hpnicfARPSourceSuppressionLimit": hpnicfARPSourceSuppressionLimit}
)
