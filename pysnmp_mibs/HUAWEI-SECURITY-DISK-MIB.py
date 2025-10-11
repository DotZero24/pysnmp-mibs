# SNMP MIB module (HUAWEI-SECURITY-DISK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-DISK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:29:41 2025
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

hwDiskMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66)
)
if mibBuilder.loadTexts:
    hwDiskMib.setRevisions(
        ("2013-12-19 09:00",)
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
_HwSecDiskMibNotification_ObjectIdentity = ObjectIdentity
hwSecDiskMibNotification = _HwSecDiskMibNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1)
)
_HwSecDiskMibTrapObject_ObjectIdentity = ObjectIdentity
hwSecDiskMibTrapObject = _HwSecDiskMibTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 1)
)
_HwSecDiskSlotNumber_Type = Integer32
_HwSecDiskSlotNumber_Object = MibScalar
hwSecDiskSlotNumber = _HwSecDiskSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 1, 1),
    _HwSecDiskSlotNumber_Type()
)
hwSecDiskSlotNumber.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSecDiskSlotNumber.setStatus("current")
_HwSecDiskAsc_Type = Integer32
_HwSecDiskAsc_Object = MibScalar
hwSecDiskAsc = _HwSecDiskAsc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 1, 2),
    _HwSecDiskAsc_Type()
)
hwSecDiskAsc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSecDiskAsc.setStatus("current")
_HwSecDiskAscq_Type = Integer32
_HwSecDiskAscq_Object = MibScalar
hwSecDiskAscq = _HwSecDiskAscq_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 1, 3),
    _HwSecDiskAscq_Type()
)
hwSecDiskAscq.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSecDiskAscq.setStatus("current")
_HwSecDiskSN_Type = OctetString
_HwSecDiskSN_Object = MibScalar
hwSecDiskSN = _HwSecDiskSN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 1, 4),
    _HwSecDiskSN_Type()
)
hwSecDiskSN.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwSecDiskSN.setStatus("current")
_HwSecDiskMibTraps_ObjectIdentity = ObjectIdentity
hwSecDiskMibTraps = _HwSecDiskMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 2)
)

# Managed Objects groups


# Notification objects

hwSecDiskPredictionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 2, 1)
)
hwSecDiskPredictionError.setObjects(
      *(("HUAWEI-SECURITY-DISK-MIB", "hwSecDiskSlotNumber"),
        ("HUAWEI-SECURITY-DISK-MIB", "hwSecDiskAsc"),
        ("HUAWEI-SECURITY-DISK-MIB", "hwSecDiskAscq"),
        ("HUAWEI-SECURITY-DISK-MIB", "hwSecDiskSN"))
)
if mibBuilder.loadTexts:
    hwSecDiskPredictionError.setStatus(
        "current"
    )

hwSecDiskOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 2, 2)
)
hwSecDiskOffline.setObjects(
    ("HUAWEI-SECURITY-DISK-MIB", "hwSecDiskSlotNumber")
)
if mibBuilder.loadTexts:
    hwSecDiskOffline.setStatus(
        "current"
    )

hwSecDiskOnline = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 66, 1, 2, 3)
)
hwSecDiskOnline.setObjects(
    ("HUAWEI-SECURITY-DISK-MIB", "hwSecDiskSlotNumber")
)
if mibBuilder.loadTexts:
    hwSecDiskOnline.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-DISK-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwDiskMib": hwDiskMib,
       "hwSecDiskMibNotification": hwSecDiskMibNotification,
       "hwSecDiskMibTrapObject": hwSecDiskMibTrapObject,
       "hwSecDiskSlotNumber": hwSecDiskSlotNumber,
       "hwSecDiskAsc": hwSecDiskAsc,
       "hwSecDiskAscq": hwSecDiskAscq,
       "hwSecDiskSN": hwSecDiskSN,
       "hwSecDiskMibTraps": hwSecDiskMibTraps,
       "hwSecDiskPredictionError": hwSecDiskPredictionError,
       "hwSecDiskOffline": hwSecDiskOffline,
       "hwSecDiskOnline": hwSecDiskOnline}
)
