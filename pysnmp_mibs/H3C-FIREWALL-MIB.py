# SNMP MIB module (H3C-FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FIREWALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:07 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

h3cFireWall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cFirewallobject_ObjectIdentity = ObjectIdentity
h3cFirewallobject = _H3cFirewallobject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1)
)
_H3cFirewallSpecs_ObjectIdentity = ObjectIdentity
h3cFirewallSpecs = _H3cFirewallSpecs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1)
)
_H3cFWMaxConnNum_Type = Unsigned32
_H3cFWMaxConnNum_Object = MibScalar
h3cFWMaxConnNum = _H3cFWMaxConnNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 1, 1),
    _H3cFWMaxConnNum_Type()
)
h3cFWMaxConnNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFWMaxConnNum.setStatus("current")
_H3cFirewallGlobalStats_ObjectIdentity = ObjectIdentity
h3cFirewallGlobalStats = _H3cFirewallGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2)
)
_H3cFWConnNumCurr_Type = Gauge32
_H3cFWConnNumCurr_Object = MibScalar
h3cFWConnNumCurr = _H3cFWConnNumCurr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2, 1),
    _H3cFWConnNumCurr_Type()
)
h3cFWConnNumCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFWConnNumCurr.setStatus("current")
_H3cFWConnRate_Type = Gauge32
_H3cFWConnRate_Object = MibScalar
h3cFWConnRate = _H3cFWConnRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 88, 1, 2, 2),
    _H3cFWConnRate_Type()
)
h3cFWConnRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFWConnRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FIREWALL-MIB",
    **{"h3cFireWall": h3cFireWall,
       "h3cFirewallobject": h3cFirewallobject,
       "h3cFirewallSpecs": h3cFirewallSpecs,
       "h3cFWMaxConnNum": h3cFWMaxConnNum,
       "h3cFirewallGlobalStats": h3cFirewallGlobalStats,
       "h3cFWConnNumCurr": h3cFWConnNumCurr,
       "h3cFWConnRate": h3cFWConnRate}
)
