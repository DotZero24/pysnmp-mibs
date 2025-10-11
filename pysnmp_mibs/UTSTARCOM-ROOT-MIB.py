# SNMP MIB module (UTSTARCOM-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/utstarcom/UTSTARCOM-ROOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:46:42 2025
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

utstarcom = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1949)
)
if mibBuilder.loadTexts:
    utstarcom.setRevisions(
        ("2005-09-01 16:21",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UtsRoot_ObjectIdentity = ObjectIdentity
utsRoot = _UtsRoot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1)
)
_UtsProducts_ObjectIdentity = ObjectIdentity
utsProducts = _UtsProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3)
)
_UtsBroadbandSwitch_ObjectIdentity = ObjectIdentity
utsBroadbandSwitch = _UtsBroadbandSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10)
)
_UtsBBSProductSysId_ObjectIdentity = ObjectIdentity
utsBBSProductSysId = _UtsBBSProductSysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2)
)
_UtBBSEponOnuSysId_ObjectIdentity = ObjectIdentity
utBBSEponOnuSysId = _UtBBSEponOnuSysId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100)
)
_UtBBSEponOnuSysId2004_ObjectIdentity = ObjectIdentity
utBBSEponOnuSysId2004 = _UtBBSEponOnuSysId2004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 2, 100, 6)
)
if mibBuilder.loadTexts:
    utBBSEponOnuSysId2004.setStatus("current")
_UtBBSGeponOnu_ObjectIdentity = ObjectIdentity
utBBSGeponOnu = _UtBBSGeponOnu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100)
)
if mibBuilder.loadTexts:
    utBBSGeponOnu.setStatus("current")
_UtBBSGeponOnu2004_ObjectIdentity = ObjectIdentity
utBBSGeponOnu2004 = _UtBBSGeponOnu2004_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100, 6)
)
if mibBuilder.loadTexts:
    utBBSGeponOnu2004.setStatus("current")
_UtBBSGeponOnu404_ObjectIdentity = ObjectIdentity
utBBSGeponOnu404 = _UtBBSGeponOnu404_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1949, 1, 3, 10, 100, 7)
)
if mibBuilder.loadTexts:
    utBBSGeponOnu404.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UTSTARCOM-ROOT-MIB",
    **{"utstarcom": utstarcom,
       "utsRoot": utsRoot,
       "utsProducts": utsProducts,
       "utsBroadbandSwitch": utsBroadbandSwitch,
       "utsBBSProductSysId": utsBBSProductSysId,
       "utBBSEponOnuSysId": utBBSEponOnuSysId,
       "utBBSEponOnuSysId2004": utBBSEponOnuSysId2004,
       "utBBSGeponOnu": utBBSGeponOnu,
       "utBBSGeponOnu2004": utBBSGeponOnu2004,
       "utBBSGeponOnu404": utBBSGeponOnu404}
)
