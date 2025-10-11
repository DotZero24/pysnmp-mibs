# SNMP MIB module (BRCM-CABLEHOME-FACTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-CABLEHOME-FACTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:12 2025
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

(cableDataFactory,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-FACTORY-MIB",
    "cableDataFactory")

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

cableHomeFactory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cableHomeFactory.setRevisions(
        ("2007-02-05 00:00",
         "2004-04-27 00:00",
         "2004-03-24 00:00",
         "2002-08-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChFactoryBase_ObjectIdentity = ObjectIdentity
chFactoryBase = _ChFactoryBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 1)
)
_ChFactorySecurity_ObjectIdentity = ObjectIdentity
chFactorySecurity = _ChFactorySecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2)
)
_ChSecPsCert_Type = OctetString
_ChSecPsCert_Object = MibScalar
chSecPsCert = _ChSecPsCert_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 1),
    _ChSecPsCert_Type()
)
chSecPsCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chSecPsCert.setStatus("current")
_ChSecPsPrivateKey_Type = OctetString
_ChSecPsPrivateKey_Object = MibScalar
chSecPsPrivateKey = _ChSecPsPrivateKey_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 2),
    _ChSecPsPrivateKey_Type()
)
chSecPsPrivateKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chSecPsPrivateKey.setStatus("current")
_ChSecManCaCert_Type = OctetString
_ChSecManCaCert_Object = MibScalar
chSecManCaCert = _ChSecManCaCert_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 3),
    _ChSecManCaCert_Type()
)
chSecManCaCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chSecManCaCert.setStatus("current")
_ChSecSvcProviderRootCaCert_Type = OctetString
_ChSecSvcProviderRootCaCert_Object = MibScalar
chSecSvcProviderRootCaCert = _ChSecSvcProviderRootCaCert_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 4),
    _ChSecSvcProviderRootCaCert_Type()
)
chSecSvcProviderRootCaCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chSecSvcProviderRootCaCert.setStatus("current")
_ChSpsClabCvcRootCaCert_Type = OctetString
_ChSpsClabCvcRootCaCert_Object = MibScalar
chSpsClabCvcRootCaCert = _ChSpsClabCvcRootCaCert_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 5),
    _ChSpsClabCvcRootCaCert_Type()
)
chSpsClabCvcRootCaCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chSpsClabCvcRootCaCert.setStatus("current")
_ChSpsClabCvcCaCert_Type = OctetString
_ChSpsClabCvcCaCert_Object = MibScalar
chSpsClabCvcCaCert = _ChSpsClabCvcCaCert_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 99, 1, 1, 2, 3, 2, 6),
    _ChSpsClabCvcCaCert_Type()
)
chSpsClabCvcCaCert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    chSpsClabCvcCaCert.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-CABLEHOME-FACTORY-MIB",
    **{"cableHomeFactory": cableHomeFactory,
       "chFactoryBase": chFactoryBase,
       "chFactorySecurity": chFactorySecurity,
       "chSecPsCert": chSecPsCert,
       "chSecPsPrivateKey": chSecPsPrivateKey,
       "chSecManCaCert": chSecManCaCert,
       "chSecSvcProviderRootCaCert": chSecSvcProviderRootCaCert,
       "chSpsClabCvcRootCaCert": chSpsClabCvcRootCaCert,
       "chSpsClabCvcCaCert": chSpsClabCvcCaCert}
)
