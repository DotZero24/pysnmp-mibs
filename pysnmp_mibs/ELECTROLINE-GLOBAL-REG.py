# SNMP MIB module (ELECTROLINE-GLOBAL-REG) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-GLOBAL-REG
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

electrolineGlobalRegModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    electrolineGlobalRegModule.setRevisions(
        ("1919-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ElectrolineCoRoot_ObjectIdentity = ObjectIdentity
electrolineCoRoot = _ElectrolineCoRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802)
)
if mibBuilder.loadTexts:
    electrolineCoRoot.setStatus("current")
_ElectrolineRoot_ObjectIdentity = ObjectIdentity
electrolineRoot = _ElectrolineRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1)
)
if mibBuilder.loadTexts:
    electrolineRoot.setStatus("current")
_ElectrolineReg_ObjectIdentity = ObjectIdentity
electrolineReg = _ElectrolineReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 1)
)
if mibBuilder.loadTexts:
    electrolineReg.setStatus("current")
_ElectrolineModules_ObjectIdentity = ObjectIdentity
electrolineModules = _ElectrolineModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 1, 1)
)
if mibBuilder.loadTexts:
    electrolineModules.setStatus("current")
_ElectrolineHardwareProductsReg_ObjectIdentity = ObjectIdentity
electrolineHardwareProductsReg = _ElectrolineHardwareProductsReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    electrolineHardwareProductsReg.setStatus("current")
_ElectrolineSoftwareProductsReg_ObjectIdentity = ObjectIdentity
electrolineSoftwareProductsReg = _ElectrolineSoftwareProductsReg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    electrolineSoftwareProductsReg.setStatus("current")
_ElectrolineGeneric_ObjectIdentity = ObjectIdentity
electrolineGeneric = _ElectrolineGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 2)
)
if mibBuilder.loadTexts:
    electrolineGeneric.setStatus("current")
_ElectrolineProducts_ObjectIdentity = ObjectIdentity
electrolineProducts = _ElectrolineProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3)
)
if mibBuilder.loadTexts:
    electrolineProducts.setStatus("current")
_ElectrolineHardwareProducts_ObjectIdentity = ObjectIdentity
electrolineHardwareProducts = _ElectrolineHardwareProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1)
)
if mibBuilder.loadTexts:
    electrolineHardwareProducts.setStatus("current")
_ElectrolineSoftwareProducts_ObjectIdentity = ObjectIdentity
electrolineSoftwareProducts = _ElectrolineSoftwareProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 2)
)
if mibBuilder.loadTexts:
    electrolineSoftwareProducts.setStatus("current")
_ElectrolineCaps_ObjectIdentity = ObjectIdentity
electrolineCaps = _ElectrolineCaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 4)
)
if mibBuilder.loadTexts:
    electrolineCaps.setStatus("current")
_ElectrolineReqs_ObjectIdentity = ObjectIdentity
electrolineReqs = _ElectrolineReqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 5)
)
if mibBuilder.loadTexts:
    electrolineReqs.setStatus("current")
_ElectrolineExpr_ObjectIdentity = ObjectIdentity
electrolineExpr = _ElectrolineExpr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 6)
)
if mibBuilder.loadTexts:
    electrolineExpr.setStatus("current")
_DmonMib_ObjectIdentity = ObjectIdentity
dmonMib = _DmonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 999999)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-GLOBAL-REG",
    **{"electrolineCoRoot": electrolineCoRoot,
       "electrolineRoot": electrolineRoot,
       "electrolineReg": electrolineReg,
       "electrolineModules": electrolineModules,
       "electrolineGlobalRegModule": electrolineGlobalRegModule,
       "electrolineHardwareProductsReg": electrolineHardwareProductsReg,
       "electrolineSoftwareProductsReg": electrolineSoftwareProductsReg,
       "electrolineGeneric": electrolineGeneric,
       "electrolineProducts": electrolineProducts,
       "electrolineHardwareProducts": electrolineHardwareProducts,
       "electrolineSoftwareProducts": electrolineSoftwareProducts,
       "electrolineCaps": electrolineCaps,
       "electrolineReqs": electrolineReqs,
       "electrolineExpr": electrolineExpr,
       "dmonMib": dmonMib}
)
