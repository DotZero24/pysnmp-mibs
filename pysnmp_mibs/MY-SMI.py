# SNMP MIB module (MY-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:31 2025
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

switchMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10)
)
if mibBuilder.loadTexts:
    switchMib.setRevisions(
        ("2002-03-19 00:00",)
    )

routerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1)
)
if mibBuilder.loadTexts:
    routerMib.setRevisions(
        ("2005-01-06 00:00",)
    )

wirelessMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wirelessMib.setRevisions(
        ("2007-07-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_My_ObjectIdentity = ObjectIdentity
my = _My_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1)
)
_MySwitchProducts_ObjectIdentity = ObjectIdentity
mySwitchProducts = _MySwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    mySwitchProducts.setStatus("current")
_MyMgmt_ObjectIdentity = ObjectIdentity
myMgmt = _MyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    myMgmt.setStatus("current")
_MyAgentCapability_ObjectIdentity = ObjectIdentity
myAgentCapability = _MyAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    myAgentCapability.setStatus("current")
_MyModules_ObjectIdentity = ObjectIdentity
myModules = _MyModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    myModules.setStatus("current")
_MyExperiment_ObjectIdentity = ObjectIdentity
myExperiment = _MyExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    myExperiment.setStatus("current")
_Router_ObjectIdentity = ObjectIdentity
router = _Router_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2)
)
_MyRouterProducts_ObjectIdentity = ObjectIdentity
myRouterProducts = _MyRouterProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    myRouterProducts.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3)
)
_MyWirelessProducts_ObjectIdentity = ObjectIdentity
myWirelessProducts = _MyWirelessProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    myWirelessProducts.setStatus("current")
_MyWirelessMgmt_ObjectIdentity = ObjectIdentity
myWirelessMgmt = _MyWirelessMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    myWirelessMgmt.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-SMI",
    **{"my": my,
       "products": products,
       "switch": switch,
       "switchMib": switchMib,
       "mySwitchProducts": mySwitchProducts,
       "myMgmt": myMgmt,
       "myAgentCapability": myAgentCapability,
       "myModules": myModules,
       "myExperiment": myExperiment,
       "router": router,
       "routerMib": routerMib,
       "myRouterProducts": myRouterProducts,
       "wireless": wireless,
       "wirelessMib": wirelessMib,
       "myWirelessProducts": myWirelessProducts,
       "myWirelessMgmt": myWirelessMgmt}
)
