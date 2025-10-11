# SNMP MIB module (QTECH-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:51 2025
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
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10)
)
if mibBuilder.loadTexts:
    switchMib.setRevisions(
        ("2002-03-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Qtech_ObjectIdentity = ObjectIdentity
qtech = _Qtech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1)
)
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1)
)
_QtechSwitchProducts_ObjectIdentity = ObjectIdentity
qtechSwitchProducts = _QtechSwitchProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    qtechSwitchProducts.setStatus("current")
_QtechMgmt_ObjectIdentity = ObjectIdentity
qtechMgmt = _QtechMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    qtechMgmt.setStatus("current")
_QtechAgentCapability_ObjectIdentity = ObjectIdentity
qtechAgentCapability = _QtechAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    qtechAgentCapability.setStatus("current")
_QtechModules_ObjectIdentity = ObjectIdentity
qtechModules = _QtechModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    qtechModules.setStatus("current")
_QtechExperiment_ObjectIdentity = ObjectIdentity
qtechExperiment = _QtechExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    qtechExperiment.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SMI",
    **{"qtech": qtech,
       "products": products,
       "switch": switch,
       "switchMib": switchMib,
       "qtechSwitchProducts": qtechSwitchProducts,
       "qtechMgmt": qtechMgmt,
       "qtechAgentCapability": qtechAgentCapability,
       "qtechModules": qtechModules,
       "qtechExperiment": qtechExperiment}
)
