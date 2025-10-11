# SNMP MIB module (ZX-PWE3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZX-PWE3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:42 2025
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

(zxAnCesMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnCesMib")


# MODULE-IDENTITY

zxPwe3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IANAPwTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              253,
              254)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("frameRelayDlci", 1),
          ("atmAal5SduVcc", 2),
          ("atmTransparent", 3),
          ("ethernetTagged", 4),
          ("ethernet", 5),
          ("hdlc", 6),
          ("ppp", 7),
          ("cem", 8),
          ("atmCellNto1Vcc", 9),
          ("atmCellNto1Vpc", 10),
          ("ipLayer2Transport", 11),
          ("atmCell1to1Vcc", 12),
          ("atmCell1to1Vpc", 13),
          ("atmAal5PduVcc", 14),
          ("frameRelayPortMode", 15),
          ("cep", 16),
          ("e1Satop", 17),
          ("t1Satop", 18),
          ("e3Satop", 19),
          ("t3Satop", 20),
          ("basicCesPsn", 21),
          ("basicTdmIp", 22),
          ("tdmCasCesPsn", 23),
          ("tdmCasTdmIp", 24),
          ("frDlci", 25),
          ("e1Cesop", 253),
          ("t1Cesop", 254))
    )



class IANAPwPsnTypeTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mpls", 1),
          ("l2tp", 2),
          ("ip", 3),
          ("mplsOverIp", 4),
          ("gre", 5),
          ("other", 6))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZX-PWE3-MIB",
    **{"IANAPwTypeTC": IANAPwTypeTC,
       "IANAPwPsnTypeTC": IANAPwPsnTypeTC,
       "zxPwe3MIB": zxPwe3MIB}
)
