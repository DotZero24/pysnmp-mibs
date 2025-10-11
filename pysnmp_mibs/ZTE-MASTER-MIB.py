# SNMP MIB module (ZTE-MASTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-MASTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:47 2025
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

(zxAn,) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "zxAn")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnPonMib_ObjectIdentity = ObjectIdentity
zxAnPonMib = _ZxAnPonMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010)
)
_ZxAnEponMib_ObjectIdentity = ObjectIdentity
zxAnEponMib = _ZxAnEponMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1)
)
_ZxAnGponMib_ObjectIdentity = ObjectIdentity
zxAnGponMib = _ZxAnGponMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 2)
)
_ZxAnPonProtection_ObjectIdentity = ObjectIdentity
zxAnPonProtection = _ZxAnPonProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 3)
)
_ZxAnVlanTrans_ObjectIdentity = ObjectIdentity
zxAnVlanTrans = _ZxAnVlanTrans_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 10)
)
_ZxAnTransceiver_ObjectIdentity = ObjectIdentity
zxAnTransceiver = _ZxAnTransceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 11)
)
_ZxAnCesMib_ObjectIdentity = ObjectIdentity
zxAnCesMib = _ZxAnCesMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013)
)
_ZxPwCSC_ObjectIdentity = ObjectIdentity
zxPwCSC = _ZxPwCSC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2)
)
_ZxPwCTDM_ObjectIdentity = ObjectIdentity
zxPwCTDM = _ZxPwCTDM_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 2, 1)
)
_ZxPwCPSN_ObjectIdentity = ObjectIdentity
zxPwCPSN = _ZxPwCPSN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3)
)
_ZxPwCETH_ObjectIdentity = ObjectIdentity
zxPwCETH = _ZxPwCETH_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 3, 1)
)
_ZxAnCesProtection_ObjectIdentity = ObjectIdentity
zxAnCesProtection = _ZxAnCesProtection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1013, 11)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-MASTER-MIB",
    **{"zxAnPonMib": zxAnPonMib,
       "zxAnEponMib": zxAnEponMib,
       "zxAnGponMib": zxAnGponMib,
       "zxAnPonProtection": zxAnPonProtection,
       "zxAnVlanTrans": zxAnVlanTrans,
       "zxAnTransceiver": zxAnTransceiver,
       "zxAnCesMib": zxAnCesMib,
       "zxPwCSC": zxPwCSC,
       "zxPwCTDM": zxPwCTDM,
       "zxPwCPSN": zxPwCPSN,
       "zxPwCETH": zxPwCETH,
       "zxAnCesProtection": zxAnCesProtection}
)
