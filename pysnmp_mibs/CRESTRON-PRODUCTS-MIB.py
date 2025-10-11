# SNMP MIB module (CRESTRON-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/crestron/CRESTRON-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:46 2025
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

(crestron,) = mibBuilder.importSymbols(
    "CRESTRON-ROOT-MIB",
    "crestron")

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

crestronProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 9)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CrestronProductPRO2_ObjectIdentity = ObjectIdentity
crestronProductPRO2 = _CrestronProductPRO2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 9, 1)
)
if mibBuilder.loadTexts:
    crestronProductPRO2.setStatus("current")
_CrestronProductQMRMC_ObjectIdentity = ObjectIdentity
crestronProductQMRMC = _CrestronProductQMRMC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 9, 2)
)
if mibBuilder.loadTexts:
    crestronProductQMRMC.setStatus("current")
_CrestronProductQMRMCRX_ObjectIdentity = ObjectIdentity
crestronProductQMRMCRX = _CrestronProductQMRMCRX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 9, 3)
)
if mibBuilder.loadTexts:
    crestronProductQMRMCRX.setStatus("current")
_CrestronProductDVP4_ObjectIdentity = ObjectIdentity
crestronProductDVP4 = _CrestronProductDVP4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 9, 4)
)
if mibBuilder.loadTexts:
    crestronProductDVP4.setStatus("current")
_CrestronProductMP2_ObjectIdentity = ObjectIdentity
crestronProductMP2 = _CrestronProductMP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 9, 5)
)
if mibBuilder.loadTexts:
    crestronProductMP2.setStatus("current")
_CrestronProductPollAcc_ObjectIdentity = ObjectIdentity
crestronProductPollAcc = _CrestronProductPollAcc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3212, 9, 6)
)
if mibBuilder.loadTexts:
    crestronProductPollAcc.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CRESTRON-PRODUCTS-MIB",
    **{"crestronProducts": crestronProducts,
       "crestronProductPRO2": crestronProductPRO2,
       "crestronProductQMRMC": crestronProductQMRMC,
       "crestronProductQMRMCRX": crestronProductQMRMCRX,
       "crestronProductDVP4": crestronProductDVP4,
       "crestronProductMP2": crestronProductMP2,
       "crestronProductPollAcc": crestronProductPollAcc}
)
