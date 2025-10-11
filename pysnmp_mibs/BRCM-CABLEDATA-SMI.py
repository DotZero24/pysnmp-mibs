# SNMP MIB module (BRCM-CABLEDATA-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CABLEDATA-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:53 2025
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

(broadcom,) = mibBuilder.importSymbols(
    "BRCM-SMI",
    "broadcom")

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

cableData = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2)
)
if mibBuilder.loadTexts:
    cableData.setRevisions(
        ("2007-05-21 00:00",
         "2007-02-05 00:00",
         "2002-07-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CableDataProducts_ObjectIdentity = ObjectIdentity
cableDataProducts = _CableDataProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1)
)
if mibBuilder.loadTexts:
    cableDataProducts.setStatus("current")
_CableDataMgmt_ObjectIdentity = ObjectIdentity
cableDataMgmt = _CableDataMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2)
)
if mibBuilder.loadTexts:
    cableDataMgmt.setStatus("current")
_CableDataAgentCapability_ObjectIdentity = ObjectIdentity
cableDataAgentCapability = _CableDataAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 3)
)
if mibBuilder.loadTexts:
    cableDataAgentCapability.setStatus("current")
_CableDataExperimental_ObjectIdentity = ObjectIdentity
cableDataExperimental = _CableDataExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 4)
)
if mibBuilder.loadTexts:
    cableDataExperimental.setStatus("current")
_CableDataPrivate_ObjectIdentity = ObjectIdentity
cableDataPrivate = _CableDataPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99)
)
if mibBuilder.loadTexts:
    cableDataPrivate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CABLEDATA-SMI",
    **{"cableData": cableData,
       "cableDataProducts": cableDataProducts,
       "cableDataMgmt": cableDataMgmt,
       "cableDataAgentCapability": cableDataAgentCapability,
       "cableDataExperimental": cableDataExperimental,
       "cableDataPrivate": cableDataPrivate}
)
