# SNMP MIB module (SAFEGUARD-ENGINE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/SAFEGUARD-ENGINE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:48 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swSafeGuardMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwSafeGuardGblMgmt_ObjectIdentity = ObjectIdentity
swSafeGuardGblMgmt = _SwSafeGuardGblMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 1)
)


class _SwSafeGuardAdminState_Type(Integer32):
    """Custom type swSafeGuardAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwSafeGuardAdminState_Type.__name__ = "Integer32"
_SwSafeGuardAdminState_Object = MibScalar
swSafeGuardAdminState = _SwSafeGuardAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 1, 1),
    _SwSafeGuardAdminState_Type()
)
swSafeGuardAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardAdminState.setStatus("current")
_SwSafeGuardctrl_ObjectIdentity = ObjectIdentity
swSafeGuardctrl = _SwSafeGuardctrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2)
)


class _SwSafeGuardRisingThreshold_Type(Integer32):
    """Custom type swSafeGuardRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SwSafeGuardRisingThreshold_Type.__name__ = "Integer32"
_SwSafeGuardRisingThreshold_Object = MibScalar
swSafeGuardRisingThreshold = _SwSafeGuardRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 1),
    _SwSafeGuardRisingThreshold_Type()
)
swSafeGuardRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardRisingThreshold.setStatus("current")


class _SwSafeGuardFallingThreshold_Type(Integer32):
    """Custom type swSafeGuardFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 100),
    )


_SwSafeGuardFallingThreshold_Type.__name__ = "Integer32"
_SwSafeGuardFallingThreshold_Object = MibScalar
swSafeGuardFallingThreshold = _SwSafeGuardFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 2),
    _SwSafeGuardFallingThreshold_Type()
)
swSafeGuardFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardFallingThreshold.setStatus("current")


class _SwSafeGuardmode_Type(Integer32):
    """Custom type swSafeGuardmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("fuzzy", 2))
    )


_SwSafeGuardmode_Type.__name__ = "Integer32"
_SwSafeGuardmode_Object = MibScalar
swSafeGuardmode = _SwSafeGuardmode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 3),
    _SwSafeGuardmode_Type()
)
swSafeGuardmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardmode.setStatus("current")


class _SwSafeGuardAlarmAdminState_Type(Integer32):
    """Custom type swSafeGuardAlarmAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwSafeGuardAlarmAdminState_Type.__name__ = "Integer32"
_SwSafeGuardAlarmAdminState_Object = MibScalar
swSafeGuardAlarmAdminState = _SwSafeGuardAlarmAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 4),
    _SwSafeGuardAlarmAdminState_Type()
)
swSafeGuardAlarmAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSafeGuardAlarmAdminState.setStatus("current")


class _SwSafeGuardCurrentStatus_Type(Integer32):
    """Custom type swSafeGuardCurrentStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("exhausted", 2))
    )


_SwSafeGuardCurrentStatus_Type.__name__ = "Integer32"
_SwSafeGuardCurrentStatus_Object = MibScalar
swSafeGuardCurrentStatus = _SwSafeGuardCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 5),
    _SwSafeGuardCurrentStatus_Type()
)
swSafeGuardCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSafeGuardCurrentStatus.setStatus("current")


class _SwSafeGuardInterval_Type(Integer32):
    """Custom type swSafeGuardInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SwSafeGuardInterval_Type.__name__ = "Integer32"
_SwSafeGuardInterval_Object = MibScalar
swSafeGuardInterval = _SwSafeGuardInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 2, 6),
    _SwSafeGuardInterval_Type()
)
swSafeGuardInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSafeGuardInterval.setStatus("current")
_SwSafeGuardNotify_ObjectIdentity = ObjectIdentity
swSafeGuardNotify = _SwSafeGuardNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4)
)
_SwSafeGuardNotification_ObjectIdentity = ObjectIdentity
swSafeGuardNotification = _SwSafeGuardNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1)
)
_SwSafeGuardNotifyPrefix_ObjectIdentity = ObjectIdentity
swSafeGuardNotifyPrefix = _SwSafeGuardNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0)
)

# Managed Objects groups


# Notification objects

swSafeGuardChgToExhausted = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0, 1)
)
swSafeGuardChgToExhausted.setObjects(
    ("SAFEGUARD-ENGINE-MIB", "swSafeGuardCurrentStatus")
)
if mibBuilder.loadTexts:
    swSafeGuardChgToExhausted.setStatus(
        "current"
    )

swSafeGuardChgToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 19, 4, 1, 0, 2)
)
swSafeGuardChgToNormal.setObjects(
    ("SAFEGUARD-ENGINE-MIB", "swSafeGuardCurrentStatus")
)
if mibBuilder.loadTexts:
    swSafeGuardChgToNormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SAFEGUARD-ENGINE-MIB",
    **{"swSafeGuardMIB": swSafeGuardMIB,
       "swSafeGuardGblMgmt": swSafeGuardGblMgmt,
       "swSafeGuardAdminState": swSafeGuardAdminState,
       "swSafeGuardctrl": swSafeGuardctrl,
       "swSafeGuardRisingThreshold": swSafeGuardRisingThreshold,
       "swSafeGuardFallingThreshold": swSafeGuardFallingThreshold,
       "swSafeGuardmode": swSafeGuardmode,
       "swSafeGuardAlarmAdminState": swSafeGuardAlarmAdminState,
       "swSafeGuardCurrentStatus": swSafeGuardCurrentStatus,
       "swSafeGuardInterval": swSafeGuardInterval,
       "swSafeGuardNotify": swSafeGuardNotify,
       "swSafeGuardNotification": swSafeGuardNotification,
       "swSafeGuardNotifyPrefix": swSafeGuardNotifyPrefix,
       "swSafeGuardChgToExhausted": swSafeGuardChgToExhausted,
       "swSafeGuardChgToNormal": swSafeGuardChgToNormal}
)
