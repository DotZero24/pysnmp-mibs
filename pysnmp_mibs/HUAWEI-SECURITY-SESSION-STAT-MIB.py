# SNMP MIB module (HUAWEI-SECURITY-SESSION-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-SESSION-STAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:30:14 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hwSecSessStatMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 69)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwSecurity_ObjectIdentity = ObjectIdentity
hwSecurity = _HwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122)
)
_HwSecSessStatTable_ObjectIdentity = ObjectIdentity
hwSecSessStatTable = _HwSecSessStatTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1)
)
_HwSecSessStatEntry_ObjectIdentity = ObjectIdentity
hwSecSessStatEntry = _HwSecSessStatEntry_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1)
)
_HwSecCurrSessThreshold_Type = Integer32
_HwSecCurrSessThreshold_Object = MibScalar
hwSecCurrSessThreshold = _HwSecCurrSessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 1),
    _HwSecCurrSessThreshold_Type()
)
hwSecCurrSessThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecCurrSessThreshold.setStatus("current")
_HwSecCurrSessNum_Type = Integer32
_HwSecCurrSessNum_Object = MibScalar
hwSecCurrSessNum = _HwSecCurrSessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 2),
    _HwSecCurrSessNum_Type()
)
hwSecCurrSessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecCurrSessNum.setStatus("current")
_HwSecConSessThreshold_Type = Integer32
_HwSecConSessThreshold_Object = MibScalar
hwSecConSessThreshold = _HwSecConSessThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 3),
    _HwSecConSessThreshold_Type()
)
hwSecConSessThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecConSessThreshold.setStatus("current")
_HwSecConSessNum_Type = Integer32
_HwSecConSessNum_Object = MibScalar
hwSecConSessNum = _HwSecConSessNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 69, 1, 1, 4),
    _HwSecConSessNum_Type()
)
hwSecConSessNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSecConSessNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-SESSION-STAT-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwSecSessStatMIB": hwSecSessStatMIB,
       "hwSecSessStatTable": hwSecSessStatTable,
       "hwSecSessStatEntry": hwSecSessStatEntry,
       "hwSecCurrSessThreshold": hwSecCurrSessThreshold,
       "hwSecCurrSessNum": hwSecCurrSessNum,
       "hwSecConSessThreshold": hwSecConSessThreshold,
       "hwSecConSessNum": hwSecConSessNum}
)
