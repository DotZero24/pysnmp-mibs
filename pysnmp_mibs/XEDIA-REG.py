# SNMP MIB module (XEDIA-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/extreme/XEDIA-REG
# Produced by pysmi-1.6.2 at Fri Oct 10 22:09:25 2025
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

xediaRegistrations = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 838, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class LongDisplayString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 2048),
    )



# MIB Managed Objects in the order of their OIDs

_Xedia_ObjectIdentity = ObjectIdentity
xedia = _Xedia_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838)
)
if mibBuilder.loadTexts:
    xedia.setStatus("current")
_XediaMibs_ObjectIdentity = ObjectIdentity
xediaMibs = _XediaMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 3)
)
if mibBuilder.loadTexts:
    xediaMibs.setStatus("current")
_XediaClasses_ObjectIdentity = ObjectIdentity
xediaClasses = _XediaClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 4)
)
if mibBuilder.loadTexts:
    xediaClasses.setStatus("current")
_XediaProducts_ObjectIdentity = ObjectIdentity
xediaProducts = _XediaProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 838, 5)
)
if mibBuilder.loadTexts:
    xediaProducts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XEDIA-REG",
    **{"LongDisplayString": LongDisplayString,
       "xedia": xedia,
       "xediaRegistrations": xediaRegistrations,
       "xediaMibs": xediaMibs,
       "xediaClasses": xediaClasses,
       "xediaProducts": xediaProducts}
)
