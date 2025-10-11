# SNMP MIB module (BUFFALO-ROOT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/buffalo/BUFFALO-ROOT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:18 2025
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

buffalo = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5227)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lsm_10_100_8_ObjectIdentity = ObjectIdentity
lsm_10_100_8 = _Lsm_10_100_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 1)
)
_Lsm_10_100_24_ObjectIdentity = ObjectIdentity
lsm_10_100_24 = _Lsm_10_100_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 2)
)
_Lsm_l3_24_ObjectIdentity = ObjectIdentity
lsm_l3_24 = _Lsm_l3_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 3)
)
_Wlm_series_ObjectIdentity = ObjectIdentity
wlm_series = _Wlm_series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 4)
)
_Vsm_p12tx2i_ObjectIdentity = ObjectIdentity
vsm_p12tx2i = _Vsm_p12tx2i_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 5)
)
_Lsm_10_100_16w_ObjectIdentity = ObjectIdentity
lsm_10_100_16w = _Lsm_10_100_16w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 6)
)
_Lsm_10_100_24w_ObjectIdentity = ObjectIdentity
lsm_10_100_24w = _Lsm_10_100_24w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 7)
)
_Lsm2_l3_24_ObjectIdentity = ObjectIdentity
lsm2_l3_24 = _Lsm2_l3_24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 8)
)
_Lsm_10_100_8w_ObjectIdentity = ObjectIdentity
lsm_10_100_8w = _Lsm_10_100_8w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 9)
)
_Lpv2_usb_tx1_ObjectIdentity = ObjectIdentity
lpv2_usb_tx1 = _Lpv2_usb_tx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 10)
)
_Bs_2024_gm_ObjectIdentity = ObjectIdentity
bs_2024_gm = _Bs_2024_gm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 11)
)
_Bs_poe_2024gm_ObjectIdentity = ObjectIdentity
bs_poe_2024gm = _Bs_poe_2024gm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 12)
)
_Lpv3_u2_ObjectIdentity = ObjectIdentity
lpv3_u2 = _Lpv3_u2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 13)
)
_Bs_poe_2008m_ObjectIdentity = ObjectIdentity
bs_poe_2008m = _Bs_poe_2008m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 14)
)
_Bpv_pd_tx1_ObjectIdentity = ObjectIdentity
bpv_pd_tx1 = _Bpv_pd_tx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 15)
)
_Bs_2108m_ObjectIdentity = ObjectIdentity
bs_2108m = _Bs_2108m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 16)
)
_Bs_2016m_ObjectIdentity = ObjectIdentity
bs_2016m = _Bs_2016m_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 17)
)
_AirstationPro_ObjectIdentity = ObjectIdentity
airstationPro = _AirstationPro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 18)
)
_Lpv3_u2_g54_ObjectIdentity = ObjectIdentity
lpv3_u2_g54 = _Lpv3_u2_g54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 19)
)
_Bs_g2016mr_ObjectIdentity = ObjectIdentity
bs_g2016mr = _Bs_g2016mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 20)
)
_Bs_g2024mr_ObjectIdentity = ObjectIdentity
bs_g2024mr = _Bs_g2024mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 21)
)
_Bs_g3024mr_ObjectIdentity = ObjectIdentity
bs_g3024mr = _Bs_g3024mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 22)
)
_Bs_g2008mr_ObjectIdentity = ObjectIdentity
bs_g2008mr = _Bs_g2008mr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 24)
)
_BusinessSwitch_ObjectIdentity = ObjectIdentity
businessSwitch = _BusinessSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 25)
)
_Lpv3_tx1_ObjectIdentity = ObjectIdentity
lpv3_tx1 = _Lpv3_tx1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 26)
)
_TeraStation_ObjectIdentity = ObjectIdentity
teraStation = _TeraStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5227, 27)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BUFFALO-ROOT-MIB",
    **{"buffalo": buffalo,
       "lsm-10-100-8": lsm_10_100_8,
       "lsm-10-100-24": lsm_10_100_24,
       "lsm-l3-24": lsm_l3_24,
       "wlm-series": wlm_series,
       "vsm-p12tx2i": vsm_p12tx2i,
       "lsm-10-100-16w": lsm_10_100_16w,
       "lsm-10-100-24w": lsm_10_100_24w,
       "lsm2-l3-24": lsm2_l3_24,
       "lsm-10-100-8w": lsm_10_100_8w,
       "lpv2-usb-tx1": lpv2_usb_tx1,
       "bs-2024-gm": bs_2024_gm,
       "bs-poe-2024gm": bs_poe_2024gm,
       "lpv3-u2": lpv3_u2,
       "bs-poe-2008m": bs_poe_2008m,
       "bpv-pd-tx1": bpv_pd_tx1,
       "bs-2108m": bs_2108m,
       "bs-2016m": bs_2016m,
       "airstationPro": airstationPro,
       "lpv3-u2-g54": lpv3_u2_g54,
       "bs-g2016mr": bs_g2016mr,
       "bs-g2024mr": bs_g2024mr,
       "bs-g3024mr": bs_g3024mr,
       "bs-g2008mr": bs_g2008mr,
       "businessSwitch": businessSwitch,
       "lpv3-tx1": lpv3_tx1,
       "teraStation": teraStation}
)
