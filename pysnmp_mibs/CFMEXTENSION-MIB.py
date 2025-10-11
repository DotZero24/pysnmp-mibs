# SNMP MIB module (CFMEXTENSION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/CFMEXTENSION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:16 2025
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

(Dot1agCfmMDLevel,
 Dot1agCfmMepId,
 dot1agCfmMaIndex,
 dot1agCfmMaMepListIdentifier,
 dot1agCfmMdIndex,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMepId",
    "dot1agCfmMaIndex",
    "dot1agCfmMaMepListIdentifier",
    "dot1agCfmMdIndex",
    "dot1agCfmMepIdentifier")

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

swCFMExtensionMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 86)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwCFMExtFaultMgmt_ObjectIdentity = ObjectIdentity
swCFMExtFaultMgmt = _SwCFMExtFaultMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1)
)
_SwCFMExtMgmtTable_Object = MibTable
swCFMExtMgmtTable = _SwCFMExtMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1)
)
if mibBuilder.loadTexts:
    swCFMExtMgmtTable.setStatus("current")
_SwCFMExtMgmtEntry_Object = MibTableRow
swCFMExtMgmtEntry = _SwCFMExtMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1)
)
swCFMExtMgmtEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
)
if mibBuilder.loadTexts:
    swCFMExtMgmtEntry.setStatus("current")


class _SwCFMExtMgmtAISState_Type(Integer32):
    """Custom type swCFMExtMgmtAISState based on Integer32"""
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


_SwCFMExtMgmtAISState_Type.__name__ = "Integer32"
_SwCFMExtMgmtAISState_Object = MibTableColumn
swCFMExtMgmtAISState = _SwCFMExtMgmtAISState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 1),
    _SwCFMExtMgmtAISState_Type()
)
swCFMExtMgmtAISState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtMgmtAISState.setStatus("current")


class _SwCFMExtMgmtAISPeriod_Type(Integer32):
    """Custom type swCFMExtMgmtAISPeriod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-second", 1),
          ("one-minute", 2))
    )


_SwCFMExtMgmtAISPeriod_Type.__name__ = "Integer32"
_SwCFMExtMgmtAISPeriod_Object = MibTableColumn
swCFMExtMgmtAISPeriod = _SwCFMExtMgmtAISPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 2),
    _SwCFMExtMgmtAISPeriod_Type()
)
swCFMExtMgmtAISPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtMgmtAISPeriod.setStatus("current")
_SwCFMExtMgmtAISLevel_Type = Dot1agCfmMDLevel
_SwCFMExtMgmtAISLevel_Object = MibTableColumn
swCFMExtMgmtAISLevel = _SwCFMExtMgmtAISLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 3),
    _SwCFMExtMgmtAISLevel_Type()
)
swCFMExtMgmtAISLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtMgmtAISLevel.setStatus("current")


class _SwCFMExtMgmtAISStatus_Type(Integer32):
    """Custom type swCFMExtMgmtAISStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("cleared", 2))
    )


_SwCFMExtMgmtAISStatus_Type.__name__ = "Integer32"
_SwCFMExtMgmtAISStatus_Object = MibTableColumn
swCFMExtMgmtAISStatus = _SwCFMExtMgmtAISStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 4),
    _SwCFMExtMgmtAISStatus_Type()
)
swCFMExtMgmtAISStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCFMExtMgmtAISStatus.setStatus("current")


class _SwCFMExtMgmtLockState_Type(Integer32):
    """Custom type swCFMExtMgmtLockState based on Integer32"""
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


_SwCFMExtMgmtLockState_Type.__name__ = "Integer32"
_SwCFMExtMgmtLockState_Object = MibTableColumn
swCFMExtMgmtLockState = _SwCFMExtMgmtLockState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 5),
    _SwCFMExtMgmtLockState_Type()
)
swCFMExtMgmtLockState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtMgmtLockState.setStatus("current")


class _SwCFMExtMgmtLockPeriod_Type(Integer32):
    """Custom type swCFMExtMgmtLockPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("one-second", 1),
          ("one-minute", 2))
    )


_SwCFMExtMgmtLockPeriod_Type.__name__ = "Integer32"
_SwCFMExtMgmtLockPeriod_Object = MibTableColumn
swCFMExtMgmtLockPeriod = _SwCFMExtMgmtLockPeriod_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 6),
    _SwCFMExtMgmtLockPeriod_Type()
)
swCFMExtMgmtLockPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtMgmtLockPeriod.setStatus("current")
_SwCFMExtMgmtLockLevel_Type = Dot1agCfmMDLevel
_SwCFMExtMgmtLockLevel_Object = MibTableColumn
swCFMExtMgmtLockLevel = _SwCFMExtMgmtLockLevel_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 7),
    _SwCFMExtMgmtLockLevel_Type()
)
swCFMExtMgmtLockLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtMgmtLockLevel.setStatus("current")


class _SwCFMExtMgmtLockStatus_Type(Integer32):
    """Custom type swCFMExtMgmtLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("cleared", 2))
    )


_SwCFMExtMgmtLockStatus_Type.__name__ = "Integer32"
_SwCFMExtMgmtLockStatus_Object = MibTableColumn
swCFMExtMgmtLockStatus = _SwCFMExtMgmtLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 1, 1, 8),
    _SwCFMExtMgmtLockStatus_Type()
)
swCFMExtMgmtLockStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swCFMExtMgmtLockStatus.setStatus("current")
_SwCFMExtMgmtLockCtrlTable_Object = MibTable
swCFMExtMgmtLockCtrlTable = _SwCFMExtMgmtLockCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2)
)
if mibBuilder.loadTexts:
    swCFMExtMgmtLockCtrlTable.setStatus("current")
_SwCFMExtMgmtLockCtrlEntry_Object = MibTableRow
swCFMExtMgmtLockCtrlEntry = _SwCFMExtMgmtLockCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2, 1)
)
swCFMExtMgmtLockCtrlEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaMepListIdentifier"),
)
if mibBuilder.loadTexts:
    swCFMExtMgmtLockCtrlEntry.setStatus("current")


class _SwCFMExtMgmtLockCtrlAction_Type(Integer32):
    """Custom type swCFMExtMgmtLockCtrlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_SwCFMExtMgmtLockCtrlAction_Type.__name__ = "Integer32"
_SwCFMExtMgmtLockCtrlAction_Object = MibTableColumn
swCFMExtMgmtLockCtrlAction = _SwCFMExtMgmtLockCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 1, 2, 1, 1),
    _SwCFMExtMgmtLockCtrlAction_Type()
)
swCFMExtMgmtLockCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtMgmtLockCtrlAction.setStatus("current")
_SwCFMExtNotify_ObjectIdentity = ObjectIdentity
swCFMExtNotify = _SwCFMExtNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100)
)
_SwCFMExtNotifyPrefix_ObjectIdentity = ObjectIdentity
swCFMExtNotifyPrefix = _SwCFMExtNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0)
)
_SwCFMExtNotifyMgmt_ObjectIdentity = ObjectIdentity
swCFMExtNotifyMgmt = _SwCFMExtNotifyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 1)
)


class _SwCFMExtAISNotifyState_Type(Integer32):
    """Custom type swCFMExtAISNotifyState based on Integer32"""
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


_SwCFMExtAISNotifyState_Type.__name__ = "Integer32"
_SwCFMExtAISNotifyState_Object = MibScalar
swCFMExtAISNotifyState = _SwCFMExtAISNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 1, 1),
    _SwCFMExtAISNotifyState_Type()
)
swCFMExtAISNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtAISNotifyState.setStatus("current")


class _SwCFMExtLockNotifyState_Type(Integer32):
    """Custom type swCFMExtLockNotifyState based on Integer32"""
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


_SwCFMExtLockNotifyState_Type.__name__ = "Integer32"
_SwCFMExtLockNotifyState_Object = MibScalar
swCFMExtLockNotifyState = _SwCFMExtLockNotifyState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 1, 2),
    _SwCFMExtLockNotifyState_Type()
)
swCFMExtLockNotifyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCFMExtLockNotifyState.setStatus("current")

# Managed Objects groups


# Notification objects

swCFMExtAISOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 1)
)
swCFMExtAISOccurred.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    swCFMExtAISOccurred.setStatus(
        "current"
    )

swCFMExtAISCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 2)
)
swCFMExtAISCleared.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    swCFMExtAISCleared.setStatus(
        "current"
    )

swCFMExtLockOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 3)
)
swCFMExtLockOccurred.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    swCFMExtLockOccurred.setStatus(
        "current"
    )

swCFMExtLockCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 86, 100, 0, 4)
)
swCFMExtLockCleared.setObjects(
      *(("IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
        ("IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"))
)
if mibBuilder.loadTexts:
    swCFMExtLockCleared.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CFMEXTENSION-MIB",
    **{"swCFMExtensionMIB": swCFMExtensionMIB,
       "swCFMExtFaultMgmt": swCFMExtFaultMgmt,
       "swCFMExtMgmtTable": swCFMExtMgmtTable,
       "swCFMExtMgmtEntry": swCFMExtMgmtEntry,
       "swCFMExtMgmtAISState": swCFMExtMgmtAISState,
       "swCFMExtMgmtAISPeriod": swCFMExtMgmtAISPeriod,
       "swCFMExtMgmtAISLevel": swCFMExtMgmtAISLevel,
       "swCFMExtMgmtAISStatus": swCFMExtMgmtAISStatus,
       "swCFMExtMgmtLockState": swCFMExtMgmtLockState,
       "swCFMExtMgmtLockPeriod": swCFMExtMgmtLockPeriod,
       "swCFMExtMgmtLockLevel": swCFMExtMgmtLockLevel,
       "swCFMExtMgmtLockStatus": swCFMExtMgmtLockStatus,
       "swCFMExtMgmtLockCtrlTable": swCFMExtMgmtLockCtrlTable,
       "swCFMExtMgmtLockCtrlEntry": swCFMExtMgmtLockCtrlEntry,
       "swCFMExtMgmtLockCtrlAction": swCFMExtMgmtLockCtrlAction,
       "swCFMExtNotify": swCFMExtNotify,
       "swCFMExtNotifyPrefix": swCFMExtNotifyPrefix,
       "swCFMExtAISOccurred": swCFMExtAISOccurred,
       "swCFMExtAISCleared": swCFMExtAISCleared,
       "swCFMExtLockOccurred": swCFMExtLockOccurred,
       "swCFMExtLockCleared": swCFMExtLockCleared,
       "swCFMExtNotifyMgmt": swCFMExtNotifyMgmt,
       "swCFMExtAISNotifyState": swCFMExtAISNotifyState,
       "swCFMExtLockNotifyState": swCFMExtLockNotifyState}
)
