# SNMP MIB module (CENTRECOM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/CENTRECOM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:41 2025
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

(sysDescr,
 sysUpTime) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysUpTime")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ati_ObjectIdentity = ObjectIdentity
ati = _Ati_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1)
)
_CentreCom_ObjectIdentity = ObjectIdentity
centreCom = _CentreCom_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4)
)
_Centrecom8500sx_ObjectIdentity = ObjectIdentity
centrecom8500sx = _Centrecom8500sx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 16)
)
_Centrecom8500lx_ObjectIdentity = ObjectIdentity
centrecom8500lx = _Centrecom8500lx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 17)
)
_Centrecom9100sx_ObjectIdentity = ObjectIdentity
centrecom9100sx = _Centrecom9100sx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 18)
)
_Centrecom9100lx_ObjectIdentity = ObjectIdentity
centrecom9100lx = _Centrecom9100lx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 1, 4, 19)
)
_MibObjects_ObjectIdentity = ObjectIdentity
mibObjects = _MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8)
)
_AtkkSwitchMIB_ObjectIdentity = ObjectIdentity
atkkSwitchMIB = _AtkkSwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12)
)
_ExtSwitchMIB_ObjectIdentity = ObjectIdentity
extSwitchMIB = _ExtSwitchMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 12, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CENTRECOM-MIB",
    **{"ati": ati,
       "products": products,
       "centreCom": centreCom,
       "centrecom8500sx": centrecom8500sx,
       "centrecom8500lx": centrecom8500lx,
       "centrecom9100sx": centrecom9100sx,
       "centrecom9100lx": centrecom9100lx,
       "mibObjects": mibObjects,
       "atkkSwitchMIB": atkkSwitchMIB,
       "extSwitchMIB": extSwitchMIB}
)
