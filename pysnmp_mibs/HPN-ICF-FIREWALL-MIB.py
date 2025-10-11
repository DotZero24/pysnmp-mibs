# SNMP MIB module (HPN-ICF-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPN-ICF-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:47 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfFireWall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfFirewallobject_ObjectIdentity = ObjectIdentity
hpnicfFirewallobject = _HpnicfFirewallobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1)
)
_HpnicfFirewallSpecs_ObjectIdentity = ObjectIdentity
hpnicfFirewallSpecs = _HpnicfFirewallSpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 1)
)
_HpnicfFWMaxConnNum_Type = Unsigned32
_HpnicfFWMaxConnNum_Object = MibScalar
hpnicfFWMaxConnNum = _HpnicfFWMaxConnNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 1, 1),
    _HpnicfFWMaxConnNum_Type()
)
hpnicfFWMaxConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFWMaxConnNum.setStatus("current")
_HpnicfFirewallGlobalStats_ObjectIdentity = ObjectIdentity
hpnicfFirewallGlobalStats = _HpnicfFirewallGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2)
)
_HpnicfFWConnNumCurr_Type = Gauge32
_HpnicfFWConnNumCurr_Object = MibScalar
hpnicfFWConnNumCurr = _HpnicfFWConnNumCurr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2, 1),
    _HpnicfFWConnNumCurr_Type()
)
hpnicfFWConnNumCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFWConnNumCurr.setStatus("current")
_HpnicfFWConnRate_Type = Gauge32
_HpnicfFWConnRate_Object = MibScalar
hpnicfFWConnRate = _HpnicfFWConnRate_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 88, 1, 2, 2),
    _HpnicfFWConnRate_Type()
)
hpnicfFWConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfFWConnRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-FIREWALL-MIB",
    **{"hpnicfFireWall": hpnicfFireWall,
       "hpnicfFirewallobject": hpnicfFirewallobject,
       "hpnicfFirewallSpecs": hpnicfFirewallSpecs,
       "hpnicfFWMaxConnNum": hpnicfFWMaxConnNum,
       "hpnicfFirewallGlobalStats": hpnicfFirewallGlobalStats,
       "hpnicfFWConnNumCurr": hpnicfFWConnNumCurr,
       "hpnicfFWConnRate": hpnicfFWConnRate}
)
