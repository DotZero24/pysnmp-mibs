# SNMP MIB module (A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/a3com/A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:44:06 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_A3Com_ObjectIdentity = ObjectIdentity
a3Com = _A3Com_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1)
)
_Switches_ObjectIdentity = ObjectIdentity
switches = _Switches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16)
)
_CorebuilderProductsIII_ObjectIdentity = ObjectIdentity
corebuilderProductsIII = _CorebuilderProductsIII_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1)
)
_CorebuilderModularProducts_ObjectIdentity = ObjectIdentity
corebuilderModularProducts = _CorebuilderModularProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1)
)
_CbModular3500Family_ObjectIdentity = ObjectIdentity
cbModular3500Family = _CbModular3500Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1, 1)
)
_Cb3500_ObjectIdentity = ObjectIdentity
cb3500 = _Cb3500_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 1, 1, 1)
)
_CorebuilderSystemProducts_ObjectIdentity = ObjectIdentity
corebuilderSystemProducts = _CorebuilderSystemProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2)
)
_CbSystem9400Family_ObjectIdentity = ObjectIdentity
cbSystem9400Family = _CbSystem9400Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2, 1)
)
_Cb9400_ObjectIdentity = ObjectIdentity
cb9400 = _Cb9400_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 2, 1, 1)
)
_CorebuilderChassisProducts_ObjectIdentity = ObjectIdentity
corebuilderChassisProducts = _CorebuilderChassisProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 1, 3)
)
_SuperstackProducts_ObjectIdentity = ObjectIdentity
superstackProducts = _SuperstackProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2)
)
_SuperstackModularProducts_ObjectIdentity = ObjectIdentity
superstackModularProducts = _SuperstackModularProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 1)
)
_SuperstackSystemProducts_ObjectIdentity = ObjectIdentity
superstackSystemProducts = _SuperstackSystemProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2)
)
_SsSystem3900Family_ObjectIdentity = ObjectIdentity
ssSystem3900Family = _SsSystem3900Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1)
)
_Ss3900_24_ObjectIdentity = ObjectIdentity
ss3900_24 = _Ss3900_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1, 1)
)
_Ss3900_36_ObjectIdentity = ObjectIdentity
ss3900_36 = _Ss3900_36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 1, 2)
)
_SsSystem9300Family_ObjectIdentity = ObjectIdentity
ssSystem9300Family = _SsSystem9300Family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 2)
)
_Ss9300_ObjectIdentity = ObjectIdentity
ss9300 = _Ss9300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 2, 2, 1)
)
_SuperstackChassisProducts_ObjectIdentity = ObjectIdentity
superstackChassisProducts = _SuperstackChassisProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43, 1, 16, 2, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM-SWITCHING-SYSTEMS-PRODUCTS-MIB",
    **{"a3Com": a3Com,
       "products": products,
       "switches": switches,
       "corebuilderProductsIII": corebuilderProductsIII,
       "corebuilderModularProducts": corebuilderModularProducts,
       "cbModular3500Family": cbModular3500Family,
       "cb3500": cb3500,
       "corebuilderSystemProducts": corebuilderSystemProducts,
       "cbSystem9400Family": cbSystem9400Family,
       "cb9400": cb9400,
       "corebuilderChassisProducts": corebuilderChassisProducts,
       "superstackProducts": superstackProducts,
       "superstackModularProducts": superstackModularProducts,
       "superstackSystemProducts": superstackSystemProducts,
       "ssSystem3900Family": ssSystem3900Family,
       "ss3900-24": ss3900_24,
       "ss3900-36": ss3900_36,
       "ssSystem9300Family": ssSystem9300Family,
       "ss9300": ss9300,
       "superstackChassisProducts": superstackChassisProducts}
)
