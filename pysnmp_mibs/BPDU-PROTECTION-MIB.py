# SNMP MIB module (BPDU-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/BPDU-PROTECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:33 2025
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


# MODULE-IDENTITY

swBpduProtectionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 76)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwBpduProtectionCtrl_ObjectIdentity = ObjectIdentity
swBpduProtectionCtrl = _SwBpduProtectionCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 1)
)


class _SwBpduProtectionAdminState_Type(Integer32):
    """Custom type swBpduProtectionAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwBpduProtectionAdminState_Type.__name__ = "Integer32"
_SwBpduProtectionAdminState_Object = MibScalar
swBpduProtectionAdminState = _SwBpduProtectionAdminState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 1),
    _SwBpduProtectionAdminState_Type()
)
swBpduProtectionAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBpduProtectionAdminState.setStatus("current")


class _SwBpduProtectionRecoveryTime_Type(Integer32):
    """Custom type swBpduProtectionRecoveryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_SwBpduProtectionRecoveryTime_Type.__name__ = "Integer32"
_SwBpduProtectionRecoveryTime_Object = MibScalar
swBpduProtectionRecoveryTime = _SwBpduProtectionRecoveryTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 2),
    _SwBpduProtectionRecoveryTime_Type()
)
swBpduProtectionRecoveryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBpduProtectionRecoveryTime.setStatus("current")


class _SwBpduProtectionTrapMode_Type(Integer32):
    """Custom type swBpduProtectionTrapMode based on Integer32"""
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
        *(("none", 1),
          ("attackDetected", 2),
          ("attackCleared", 3),
          ("both", 4))
    )


_SwBpduProtectionTrapMode_Type.__name__ = "Integer32"
_SwBpduProtectionTrapMode_Object = MibScalar
swBpduProtectionTrapMode = _SwBpduProtectionTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 3),
    _SwBpduProtectionTrapMode_Type()
)
swBpduProtectionTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBpduProtectionTrapMode.setStatus("current")


class _SwBpduProtectionLogMode_Type(Integer32):
    """Custom type swBpduProtectionLogMode based on Integer32"""
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
        *(("none", 1),
          ("attackDetected", 2),
          ("attackCleared", 3),
          ("both", 4))
    )


_SwBpduProtectionLogMode_Type.__name__ = "Integer32"
_SwBpduProtectionLogMode_Object = MibScalar
swBpduProtectionLogMode = _SwBpduProtectionLogMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 1, 4),
    _SwBpduProtectionLogMode_Type()
)
swBpduProtectionLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBpduProtectionLogMode.setStatus("current")
_SwBpduProtectionInfo_ObjectIdentity = ObjectIdentity
swBpduProtectionInfo = _SwBpduProtectionInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 2)
)
_SwBpduProtectionMgmt_ObjectIdentity = ObjectIdentity
swBpduProtectionMgmt = _SwBpduProtectionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 3)
)
_SwBpduProtectionPortTable_Object = MibTable
swBpduProtectionPortTable = _SwBpduProtectionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1)
)
if mibBuilder.loadTexts:
    swBpduProtectionPortTable.setStatus("current")
_SwBpduProtectionPortEntry_Object = MibTableRow
swBpduProtectionPortEntry = _SwBpduProtectionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1)
)
swBpduProtectionPortEntry.setIndexNames(
    (0, "BPDU-PROTECTION-MIB", "swBpduProtectionPortIndex"),
)
if mibBuilder.loadTexts:
    swBpduProtectionPortEntry.setStatus("current")


class _SwBpduProtectionPortIndex_Type(Integer32):
    """Custom type swBpduProtectionPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwBpduProtectionPortIndex_Type.__name__ = "Integer32"
_SwBpduProtectionPortIndex_Object = MibTableColumn
swBpduProtectionPortIndex = _SwBpduProtectionPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 1),
    _SwBpduProtectionPortIndex_Type()
)
swBpduProtectionPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBpduProtectionPortIndex.setStatus("current")


class _SwBpduProtectionPortState_Type(Integer32):
    """Custom type swBpduProtectionPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwBpduProtectionPortState_Type.__name__ = "Integer32"
_SwBpduProtectionPortState_Object = MibTableColumn
swBpduProtectionPortState = _SwBpduProtectionPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 2),
    _SwBpduProtectionPortState_Type()
)
swBpduProtectionPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBpduProtectionPortState.setStatus("current")


class _SwBpduProtectionPortMode_Type(Integer32):
    """Custom type swBpduProtectionPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("block", 2),
          ("shutdown", 3))
    )


_SwBpduProtectionPortMode_Type.__name__ = "Integer32"
_SwBpduProtectionPortMode_Object = MibTableColumn
swBpduProtectionPortMode = _SwBpduProtectionPortMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 3),
    _SwBpduProtectionPortMode_Type()
)
swBpduProtectionPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swBpduProtectionPortMode.setStatus("current")


class _SwBpduProtectionPortStatus_Type(Integer32):
    """Custom type swBpduProtectionPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("underAttack", 2))
    )


_SwBpduProtectionPortStatus_Type.__name__ = "Integer32"
_SwBpduProtectionPortStatus_Object = MibTableColumn
swBpduProtectionPortStatus = _SwBpduProtectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 3, 1, 1, 4),
    _SwBpduProtectionPortStatus_Type()
)
swBpduProtectionPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBpduProtectionPortStatus.setStatus("current")
_SwBpduProtectionNotify_ObjectIdentity = ObjectIdentity
swBpduProtectionNotify = _SwBpduProtectionNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 4)
)
_SwBpduProtectionNotifyPrefix_ObjectIdentity = ObjectIdentity
swBpduProtectionNotifyPrefix = _SwBpduProtectionNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 0)
)
_SwBpduProtectionNotificationBidings_ObjectIdentity = ObjectIdentity
swBpduProtectionNotificationBidings = _SwBpduProtectionNotificationBidings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 2)
)


class _SwBpduProtectionRecoveryMethod_Type(Integer32):
    """Custom type swBpduProtectionRecoveryMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatically", 1),
          ("manually", 2))
    )


_SwBpduProtectionRecoveryMethod_Type.__name__ = "Integer32"
_SwBpduProtectionRecoveryMethod_Object = MibScalar
swBpduProtectionRecoveryMethod = _SwBpduProtectionRecoveryMethod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 2, 1),
    _SwBpduProtectionRecoveryMethod_Type()
)
swBpduProtectionRecoveryMethod.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swBpduProtectionRecoveryMethod.setStatus("current")

# Managed Objects groups


# Notification objects

swBpduProtectionUnderAttackingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 0, 1)
)
swBpduProtectionUnderAttackingTrap.setObjects(
      *(("BPDU-PROTECTION-MIB", "swBpduProtectionPortIndex"),
        ("BPDU-PROTECTION-MIB", "swBpduProtectionPortMode"))
)
if mibBuilder.loadTexts:
    swBpduProtectionUnderAttackingTrap.setStatus(
        "current"
    )

swBpduProtectionRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 76, 4, 0, 2)
)
swBpduProtectionRecoveryTrap.setObjects(
      *(("BPDU-PROTECTION-MIB", "swBpduProtectionPortIndex"),
        ("BPDU-PROTECTION-MIB", "swBpduProtectionRecoveryMethod"))
)
if mibBuilder.loadTexts:
    swBpduProtectionRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BPDU-PROTECTION-MIB",
    **{"swBpduProtectionMIB": swBpduProtectionMIB,
       "swBpduProtectionCtrl": swBpduProtectionCtrl,
       "swBpduProtectionAdminState": swBpduProtectionAdminState,
       "swBpduProtectionRecoveryTime": swBpduProtectionRecoveryTime,
       "swBpduProtectionTrapMode": swBpduProtectionTrapMode,
       "swBpduProtectionLogMode": swBpduProtectionLogMode,
       "swBpduProtectionInfo": swBpduProtectionInfo,
       "swBpduProtectionMgmt": swBpduProtectionMgmt,
       "swBpduProtectionPortTable": swBpduProtectionPortTable,
       "swBpduProtectionPortEntry": swBpduProtectionPortEntry,
       "swBpduProtectionPortIndex": swBpduProtectionPortIndex,
       "swBpduProtectionPortState": swBpduProtectionPortState,
       "swBpduProtectionPortMode": swBpduProtectionPortMode,
       "swBpduProtectionPortStatus": swBpduProtectionPortStatus,
       "swBpduProtectionNotify": swBpduProtectionNotify,
       "swBpduProtectionNotifyPrefix": swBpduProtectionNotifyPrefix,
       "swBpduProtectionUnderAttackingTrap": swBpduProtectionUnderAttackingTrap,
       "swBpduProtectionRecoveryTrap": swBpduProtectionRecoveryTrap,
       "swBpduProtectionNotificationBidings": swBpduProtectionNotificationBidings,
       "swBpduProtectionRecoveryMethod": swBpduProtectionRecoveryMethod}
)
