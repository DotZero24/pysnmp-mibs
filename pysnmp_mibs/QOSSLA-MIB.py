# SNMP MIB module (QOSSLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/QOSSLA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:18:36 2025
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

nnqosSLAMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24)
)
if mibBuilder.loadTexts:
    nnqosSLAMib.setRevisions(
        ("1900-08-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NnqosSLANotifications_ObjectIdentity = ObjectIdentity
nnqosSLANotifications = _NnqosSLANotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 1)
)
_NnqosSLATraps_ObjectIdentity = ObjectIdentity
nnqosSLATraps = _NnqosSLATraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 1, 0)
)
_NnqosSLANotificationsVars_ObjectIdentity = ObjectIdentity
nnqosSLANotificationsVars = _NnqosSLANotificationsVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2)
)


class _NnqosSlaIndex_Type(Integer32):
    """Custom type nnqosSlaIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_NnqosSlaIndex_Type.__name__ = "Integer32"
_NnqosSlaIndex_Object = MibScalar
nnqosSlaIndex = _NnqosSlaIndex_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 1),
    _NnqosSlaIndex_Type()
)
nnqosSlaIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnqosSlaIndex.setStatus("current")


class _NnqosSlaThresholdType_Type(Integer32):
    """Custom type nnqosSlaThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("average", 1),
          ("immediate", 2),
          ("consecutive", 3),
          ("xofy", 4))
    )


_NnqosSlaThresholdType_Type.__name__ = "Integer32"
_NnqosSlaThresholdType_Object = MibScalar
nnqosSlaThresholdType = _NnqosSlaThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 2),
    _NnqosSlaThresholdType_Type()
)
nnqosSlaThresholdType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnqosSlaThresholdType.setStatus("current")


class _NnqosSlaEffectType_Type(Integer32):
    """Custom type nnqosSlaEffectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              17)
        )
    )
    namedValues = NamedValues(
        *(("jitterAvg", 1),
          ("jitterAvgSrcDest", 2),
          ("jitterAvgDestSrc", 3),
          ("jitterMaxPosSrcDest", 4),
          ("jitterMaxPosDestSrc", 5),
          ("jitterMaxNegSrcDest", 6),
          ("jitterMaxNegDestSrc", 7),
          ("delayAvg", 8),
          ("delayAvgSrcDest", 9),
          ("delayAvgDestSrc", 10),
          ("delayMaxSrcDest", 11),
          ("delayMaxDestSrc", 12),
          ("packetLoss", 13),
          ("packetOutOfOrder", 14),
          ("packetLateArrival", 15),
          ("responseTime", 16),
          ("timeout", 17))
    )


_NnqosSlaEffectType_Type.__name__ = "Integer32"
_NnqosSlaEffectType_Object = MibScalar
nnqosSlaEffectType = _NnqosSlaEffectType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 3),
    _NnqosSlaEffectType_Type()
)
nnqosSlaEffectType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnqosSlaEffectType.setStatus("current")
_NnqosSlaThresholdValue1_Type = Integer32
_NnqosSlaThresholdValue1_Object = MibScalar
nnqosSlaThresholdValue1 = _NnqosSlaThresholdValue1_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 4),
    _NnqosSlaThresholdValue1_Type()
)
nnqosSlaThresholdValue1.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnqosSlaThresholdValue1.setStatus("current")
_NnqosSlaThresholdValue2_Type = Integer32
_NnqosSlaThresholdValue2_Object = MibScalar
nnqosSlaThresholdValue2 = _NnqosSlaThresholdValue2_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 2, 5),
    _NnqosSlaThresholdValue2_Type()
)
nnqosSlaThresholdValue2.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    nnqosSlaThresholdValue2.setStatus("current")

# Managed Objects groups


# Notification objects

nnqosSLANotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 1, 0, 1)
)
nnqosSLANotification.setObjects(
      *(("QOSSLA-MIB", "nnqosSlaIndex"),
        ("QOSSLA-MIB", "nnqosSlaThresholdType"),
        ("QOSSLA-MIB", "nnqosSlaEffectType"),
        ("QOSSLA-MIB", "nnqosSlaThresholdValue1"),
        ("QOSSLA-MIB", "nnqosSlaThresholdValue2"))
)
if mibBuilder.loadTexts:
    nnqosSLANotification.setStatus(
        "current"
    )


# Notifications groups

nnqosNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 24, 3)
)
nnqosNotificationGroup.setObjects(
    ("QOSSLA-MIB", "nnqosSLANotification")
)
if mibBuilder.loadTexts:
    nnqosNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QOSSLA-MIB",
    **{"nnqosSLAMib": nnqosSLAMib,
       "nnqosSLANotifications": nnqosSLANotifications,
       "nnqosSLATraps": nnqosSLATraps,
       "nnqosSLANotification": nnqosSLANotification,
       "nnqosSLANotificationsVars": nnqosSLANotificationsVars,
       "nnqosSlaIndex": nnqosSlaIndex,
       "nnqosSlaThresholdType": nnqosSlaThresholdType,
       "nnqosSlaEffectType": nnqosSlaEffectType,
       "nnqosSlaThresholdValue1": nnqosSlaThresholdValue1,
       "nnqosSlaThresholdValue2": nnqosSlaThresholdValue2,
       "nnqosNotificationGroup": nnqosNotificationGroup}
)
