# SNMP MIB module (BRCM-CM-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CM-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:05 2025
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

(cableDataProducts,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-SMI",
    "cableDataProducts")

(AgentCapabilities,
 ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "AgentCapabilities",
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

brcmCmProducts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2)
)
if mibBuilder.loadTexts:
    brcmCmProducts.setRevisions(
        ("2007-02-05 00:00",
         "2004-02-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CmReferenceDesigns_ObjectIdentity = ObjectIdentity
cmReferenceDesigns = _CmReferenceDesigns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1)
)
_Bcm93220_ObjectIdentity = ObjectIdentity
bcm93220 = _Bcm93220_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3220)
)
_Bcm93300_ObjectIdentity = ObjectIdentity
bcm93300 = _Bcm93300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3300)
)
_Bcm93345_ObjectIdentity = ObjectIdentity
bcm93345 = _Bcm93345_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3345)
)
_Bcm93348_ObjectIdentity = ObjectIdentity
bcm93348 = _Bcm93348_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3348)
)
_Bcm93349_ObjectIdentity = ObjectIdentity
bcm93349 = _Bcm93349_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3349)
)
_Bcm93350_ObjectIdentity = ObjectIdentity
bcm93350 = _Bcm93350_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3350)
)
_Bcm93351_ObjectIdentity = ObjectIdentity
bcm93351 = _Bcm93351_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3351)
)
_Bcm93352_ObjectIdentity = ObjectIdentity
bcm93352 = _Bcm93352_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3352)
)
_Bcm93360_ObjectIdentity = ObjectIdentity
bcm93360 = _Bcm93360_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3360)
)
_Bcm93367_ObjectIdentity = ObjectIdentity
bcm93367 = _Bcm93367_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3367)
)
_Bcm93368_ObjectIdentity = ObjectIdentity
bcm93368 = _Bcm93368_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3368)
)
_Bcm93380_ObjectIdentity = ObjectIdentity
bcm93380 = _Bcm93380_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3380)
)
_Bcm93381_ObjectIdentity = ObjectIdentity
bcm93381 = _Bcm93381_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 1, 2, 1, 3381)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CM-PRODUCTS-MIB",
    **{"brcmCmProducts": brcmCmProducts,
       "cmReferenceDesigns": cmReferenceDesigns,
       "bcm93220": bcm93220,
       "bcm93300": bcm93300,
       "bcm93345": bcm93345,
       "bcm93348": bcm93348,
       "bcm93349": bcm93349,
       "bcm93350": bcm93350,
       "bcm93351": bcm93351,
       "bcm93352": bcm93352,
       "bcm93360": bcm93360,
       "bcm93367": bcm93367,
       "bcm93368": bcm93368,
       "bcm93380": bcm93380,
       "bcm93381": bcm93381}
)
