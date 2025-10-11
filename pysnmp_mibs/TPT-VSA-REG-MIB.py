# SNMP MIB module (TPT-VSA-REG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TPT-VSA-REG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:03 2025
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

(tpt_products,
 tpt_reg) = mibBuilder.importSymbols(
    "TIPPINGPOINT-REG-MIB",
    "tpt-products",
    "tpt-reg")


# MODULE-IDENTITY

tpt_vsaMIBs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 10)
)
if mibBuilder.loadTexts:
    tpt_vsaMIBs.setRevisions(
        ("2016-05-25 18:54",
         "2014-11-11 19:37")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tpt_vsa_family_ObjectIdentity = ObjectIdentity
tpt_vsa_family = _Tpt_vsa_family_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 10)
)
if mibBuilder.loadTexts:
    tpt_vsa_family.setStatus("current")
_Tpt_model_V10F_ObjectIdentity = ObjectIdentity
tpt_model_V10F = _Tpt_model_V10F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tpt_model_V10F.setStatus("current")
_Tpt_model_V1000F_ObjectIdentity = ObjectIdentity
tpt_model_V1000F = _Tpt_model_V1000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tpt_model_V1000F.setStatus("current")
_Tpt_model_V2000F_ObjectIdentity = ObjectIdentity
tpt_model_V2000F = _Tpt_model_V2000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 10, 3)
)
if mibBuilder.loadTexts:
    tpt_model_V2000F.setStatus("current")
_Tpt_model_V5000F_ObjectIdentity = ObjectIdentity
tpt_model_V5000F = _Tpt_model_V5000F_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 1, 10, 4)
)
if mibBuilder.loadTexts:
    tpt_model_V5000F.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-VSA-REG-MIB",
    **{"tpt-vsa-family": tpt_vsa_family,
       "tpt-model-V10F": tpt_model_V10F,
       "tpt-model-V1000F": tpt_model_V1000F,
       "tpt-model-V2000F": tpt_model_V2000F,
       "tpt-model-V5000F": tpt_model_V5000F,
       "tpt-vsaMIBs": tpt_vsaMIBs}
)
