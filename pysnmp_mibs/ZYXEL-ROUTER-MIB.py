# SNMP MIB module (ZYXEL-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-ROUTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:02:31 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelRouter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelRouterNsf_ObjectIdentity = ObjectIdentity
zyxelRouterNsf = _ZyxelRouterNsf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1)
)
_ZyxelRouterNsfSetup_ObjectIdentity = ObjectIdentity
zyxelRouterNsfSetup = _ZyxelRouterNsfSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1)
)
_ZyRouterNsfEnable_Type = EnabledStatus
_ZyRouterNsfEnable_Object = MibScalar
zyRouterNsfEnable = _ZyRouterNsfEnable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1, 1),
    _ZyRouterNsfEnable_Type()
)
zyRouterNsfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRouterNsfEnable.setStatus("current")
_ZyRouterNsfTimer_Type = Integer32
_ZyRouterNsfTimer_Object = MibScalar
zyRouterNsfTimer = _ZyRouterNsfTimer_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 113, 1, 1, 2),
    _ZyRouterNsfTimer_Type()
)
zyRouterNsfTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyRouterNsfTimer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-ROUTER-MIB",
    **{"zyxelRouter": zyxelRouter,
       "zyxelRouterNsf": zyxelRouterNsf,
       "zyxelRouterNsfSetup": zyxelRouterNsfSetup,
       "zyRouterNsfEnable": zyRouterNsfEnable,
       "zyRouterNsfTimer": zyRouterNsfTimer}
)
