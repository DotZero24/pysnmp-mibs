# SNMP MIB module (TIPPINGPOINT-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TIPPINGPOINT-REG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:25 2025
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

tippingpoint = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734)
)
if mibBuilder.loadTexts:
    tippingpoint.setRevisions(
        ("2016-05-25 18:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tpt_reg_ObjectIdentity = ObjectIdentity
tpt_reg = _Tpt_reg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1)
)
if mibBuilder.loadTexts:
    tpt_reg.setStatus("current")
_Tpt_generic_ObjectIdentity = ObjectIdentity
tpt_generic = _Tpt_generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 2)
)
if mibBuilder.loadTexts:
    tpt_generic.setStatus("current")
_Tpt_products_ObjectIdentity = ObjectIdentity
tpt_products = _Tpt_products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3)
)
if mibBuilder.loadTexts:
    tpt_products.setStatus("current")
_Tpt_caps_ObjectIdentity = ObjectIdentity
tpt_caps = _Tpt_caps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 4)
)
if mibBuilder.loadTexts:
    tpt_caps.setStatus("current")
_Tpt_reqs_ObjectIdentity = ObjectIdentity
tpt_reqs = _Tpt_reqs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 5)
)
if mibBuilder.loadTexts:
    tpt_reqs.setStatus("current")
_Tpt_expr_ObjectIdentity = ObjectIdentity
tpt_expr = _Tpt_expr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 6)
)
if mibBuilder.loadTexts:
    tpt_expr.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIPPINGPOINT-REG-MIB",
    **{"tippingpoint": tippingpoint,
       "tpt-reg": tpt_reg,
       "tpt-generic": tpt_generic,
       "tpt-products": tpt_products,
       "tpt-caps": tpt_caps,
       "tpt-reqs": tpt_reqs,
       "tpt-expr": tpt_expr}
)
