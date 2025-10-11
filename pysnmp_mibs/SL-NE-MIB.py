# SNMP MIB module (SL-NE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smartoptics/SL-NE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:11:35 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

smartoptics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Sitelight_ObjectIdentity = ObjectIdentity
sitelight = _Sitelight_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1)
)
_SlService_ObjectIdentity = ObjectIdentity
slService = _SlService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1)
)
_Soproduct_ObjectIdentity = ObjectIdentity
soproduct = _Soproduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100)
)
_Sone_ObjectIdentity = ObjectIdentity
sone = _Sone_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1)
)
_T_4400r_ObjectIdentity = ObjectIdentity
T_4400r = _T_4400r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 404)
)
_T_4408_ObjectIdentity = ObjectIdentity
T_4408 = _T_4408_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 404, 1)
)
_T_4900r_ObjectIdentity = ObjectIdentity
T_4900r = _T_4900r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000)
)
_T_4904_ObjectIdentity = ObjectIdentity
T_4904 = _T_4904_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 1)
)
_T_4808_ObjectIdentity = ObjectIdentity
T_4808 = _T_4808_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 2)
)
_T_4910_ObjectIdentity = ObjectIdentity
T_4910 = _T_4910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 3)
)
_T_ROADM_2_ObjectIdentity = ObjectIdentity
T_ROADM_2 = _T_ROADM_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 4)
)
_T_4906_ObjectIdentity = ObjectIdentity
T_4906 = _T_4906_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 5)
)
_T_1608_ObjectIdentity = ObjectIdentity
T_1608 = _T_1608_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 6)
)
_T_4900_IL_ObjectIdentity = ObjectIdentity
T_4900_IL = _T_4900_IL_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 7)
)
_T_1608_CRY_ObjectIdentity = ObjectIdentity
T_1608_CRY = _T_1608_CRY_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 1000, 8)
)
_T_4920r_ObjectIdentity = ObjectIdentity
T_4920r = _T_4920r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2000)
)
_T_4920_ObjectIdentity = ObjectIdentity
T_4920 = _T_4920_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2000, 1)
)
_T_9900r_ObjectIdentity = ObjectIdentity
T_9900r = _T_9900r_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2100)
)
_T_9910_ObjectIdentity = ObjectIdentity
T_9910 = _T_9910_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2100, 1)
)
_T_9910_C_ObjectIdentity = ObjectIdentity
T_9910_C = _T_9910_C_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2100, 2)
)
_T_9901_ObjectIdentity = ObjectIdentity
T_9901 = _T_9901_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2100, 3)
)
_T_ROADM_nro_ObjectIdentity = ObjectIdentity
T_ROADM_nro = _T_ROADM_nro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2200)
)
_T_ROADM_4ro1_ObjectIdentity = ObjectIdentity
T_ROADM_4ro1 = _T_ROADM_4ro1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2200, 1)
)
_T_ROADM_4ro2_ObjectIdentity = ObjectIdentity
T_ROADM_4ro2 = _T_ROADM_4ro2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2200, 2)
)
_T_ROADM_4ro3_ObjectIdentity = ObjectIdentity
T_ROADM_4ro3 = _T_ROADM_4ro3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 100, 1, 2200, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-NE-MIB",
    **{"smartoptics": smartoptics,
       "sitelight": sitelight,
       "slService": slService,
       "soproduct": soproduct,
       "sone": sone,
       "T-4400r": T_4400r,
       "T-4408": T_4408,
       "T-4900r": T_4900r,
       "T-4904": T_4904,
       "T-4808": T_4808,
       "T-4910": T_4910,
       "T-ROADM-2": T_ROADM_2,
       "T-4906": T_4906,
       "T-1608": T_1608,
       "T-4900-IL": T_4900_IL,
       "T-1608-CRY": T_1608_CRY,
       "T-4920r": T_4920r,
       "T-4920": T_4920,
       "T-9900r": T_9900r,
       "T-9910": T_9910,
       "T-9910-C": T_9910_C,
       "T-9901": T_9901,
       "T-ROADM-nro": T_ROADM_nro,
       "T-ROADM-4ro1": T_ROADM_4ro1,
       "T-ROADM-4ro2": T_ROADM_4ro2,
       "T-ROADM-4ro3": T_ROADM_4ro3}
)
