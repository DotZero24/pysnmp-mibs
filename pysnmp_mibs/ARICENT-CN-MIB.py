# SNMP MIB module (ARICENT-CN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-CN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:34 2025
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

(Ieee8021CnDefenseMode,
 ieee8021CnCpIdentifier,
 ieee8021CnGlobalEntry,
 ieee8021CnPortPriEntry) = mibBuilder.importSymbols(
    "IEEE8021-CN-MIB",
    "Ieee8021CnDefenseMode",
    "ieee8021CnCpIdentifier",
    "ieee8021CnGlobalEntry",
    "ieee8021CnPortPriEntry")

(IEEE8021PriorityValue,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PriorityValue")

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
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fscn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47)
)
if mibBuilder.loadTexts:
    fscn.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsCnMaster_ObjectIdentity = ObjectIdentity
fsCnMaster = _FsCnMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 1)
)


class _FsCnSystemControl_Type(Integer32):
    """Custom type fsCnSystemControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("shutdown", 2))
    )


_FsCnSystemControl_Type.__name__ = "Integer32"
_FsCnSystemControl_Object = MibScalar
fsCnSystemControl = _FsCnSystemControl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 1, 1),
    _FsCnSystemControl_Type()
)
fsCnSystemControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCnSystemControl.setStatus("current")


class _FsCnGlobalEnableTrap_Type(Integer32):
    """Custom type fsCnGlobalEnableTrap based on Integer32"""
    defaultValue = 3


_FsCnGlobalEnableTrap_Type.__name__ = "Integer32"
_FsCnGlobalEnableTrap_Object = MibScalar
fsCnGlobalEnableTrap = _FsCnGlobalEnableTrap_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 1, 2),
    _FsCnGlobalEnableTrap_Type()
)
fsCnGlobalEnableTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCnGlobalEnableTrap.setStatus("current")
_FsCnComponent_ObjectIdentity = ObjectIdentity
fsCnComponent = _FsCnComponent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 2)
)
_FsCnXGlobalTable_Object = MibTable
fsCnXGlobalTable = _FsCnXGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 2, 1)
)
if mibBuilder.loadTexts:
    fsCnXGlobalTable.setStatus("current")
_FsCnXGlobalEntry_Object = MibTableRow
fsCnXGlobalEntry = _FsCnXGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsCnXGlobalEntry.setStatus("current")


class _FsCnXGlobalTraceLevel_Type(Integer32):
    """Custom type fsCnXGlobalTraceLevel based on Integer32"""
    defaultValue = 32


_FsCnXGlobalTraceLevel_Type.__name__ = "Integer32"
_FsCnXGlobalTraceLevel_Object = MibTableColumn
fsCnXGlobalTraceLevel = _FsCnXGlobalTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 2, 1, 1, 1),
    _FsCnXGlobalTraceLevel_Type()
)
fsCnXGlobalTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCnXGlobalTraceLevel.setStatus("current")


class _FsCnXGlobalClearCounters_Type(TruthValue):
    """Custom type fsCnXGlobalClearCounters based on TruthValue"""
    defaultValue = 2


_FsCnXGlobalClearCounters_Type.__name__ = "TruthValue"
_FsCnXGlobalClearCounters_Object = MibTableColumn
fsCnXGlobalClearCounters = _FsCnXGlobalClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 2, 1, 1, 2),
    _FsCnXGlobalClearCounters_Type()
)
fsCnXGlobalClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCnXGlobalClearCounters.setStatus("current")
_FsCnXGlobalTLVErrors_Type = Counter32
_FsCnXGlobalTLVErrors_Object = MibTableColumn
fsCnXGlobalTLVErrors = _FsCnXGlobalTLVErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 2, 1, 1, 3),
    _FsCnXGlobalTLVErrors_Type()
)
fsCnXGlobalTLVErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXGlobalTLVErrors.setStatus("current")
_FsCnPortPriority_ObjectIdentity = ObjectIdentity
fsCnPortPriority = _FsCnPortPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3)
)
_FsCnXPortPriTable_Object = MibTable
fsCnXPortPriTable = _FsCnXPortPriTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1)
)
if mibBuilder.loadTexts:
    fsCnXPortPriTable.setStatus("current")
_FsCnXPortPriEntry_Object = MibTableRow
fsCnXPortPriEntry = _FsCnXPortPriEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsCnXPortPriEntry.setStatus("current")


class _FsCnXPortPriClearCpCounters_Type(TruthValue):
    """Custom type fsCnXPortPriClearCpCounters based on TruthValue"""
    defaultValue = 2


_FsCnXPortPriClearCpCounters_Type.__name__ = "TruthValue"
_FsCnXPortPriClearCpCounters_Object = MibTableColumn
fsCnXPortPriClearCpCounters = _FsCnXPortPriClearCpCounters_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 1),
    _FsCnXPortPriClearCpCounters_Type()
)
fsCnXPortPriClearCpCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCnXPortPriClearCpCounters.setStatus("current")


class _FsCnXPortPriErrorEntry_Type(TruthValue):
    """Custom type fsCnXPortPriErrorEntry based on TruthValue"""
    defaultValue = 2


_FsCnXPortPriErrorEntry_Type.__name__ = "TruthValue"
_FsCnXPortPriErrorEntry_Object = MibTableColumn
fsCnXPortPriErrorEntry = _FsCnXPortPriErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 2),
    _FsCnXPortPriErrorEntry_Type()
)
fsCnXPortPriErrorEntry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXPortPriErrorEntry.setStatus("current")
_FsCnXPortPriOperDefMode_Type = Ieee8021CnDefenseMode
_FsCnXPortPriOperDefMode_Object = MibTableColumn
fsCnXPortPriOperDefMode = _FsCnXPortPriOperDefMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 3),
    _FsCnXPortPriOperDefMode_Type()
)
fsCnXPortPriOperDefMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXPortPriOperDefMode.setStatus("current")
_FsCnXPortPriOperAltPri_Type = IEEE8021PriorityValue
_FsCnXPortPriOperAltPri_Object = MibTableColumn
fsCnXPortPriOperAltPri = _FsCnXPortPriOperAltPri_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 4),
    _FsCnXPortPriOperAltPri_Type()
)
fsCnXPortPriOperAltPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXPortPriOperAltPri.setStatus("current")
_FsCnXPortPriLastRcvdEvent_Type = DisplayString
_FsCnXPortPriLastRcvdEvent_Object = MibTableColumn
fsCnXPortPriLastRcvdEvent = _FsCnXPortPriLastRcvdEvent_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 5),
    _FsCnXPortPriLastRcvdEvent_Type()
)
fsCnXPortPriLastRcvdEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXPortPriLastRcvdEvent.setStatus("current")
_FsCnXPortPriLastRcvdEventTime_Type = TimeStamp
_FsCnXPortPriLastRcvdEventTime_Object = MibTableColumn
fsCnXPortPriLastRcvdEventTime = _FsCnXPortPriLastRcvdEventTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 6),
    _FsCnXPortPriLastRcvdEventTime_Type()
)
fsCnXPortPriLastRcvdEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXPortPriLastRcvdEventTime.setStatus("current")
_FsCnXPortPriLastSentEvent_Type = DisplayString
_FsCnXPortPriLastSentEvent_Object = MibTableColumn
fsCnXPortPriLastSentEvent = _FsCnXPortPriLastSentEvent_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 7),
    _FsCnXPortPriLastSentEvent_Type()
)
fsCnXPortPriLastSentEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXPortPriLastSentEvent.setStatus("current")
_FsCnXPortPriLastSentEventTime_Type = TimeStamp
_FsCnXPortPriLastSentEventTime_Object = MibTableColumn
fsCnXPortPriLastSentEventTime = _FsCnXPortPriLastSentEventTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 3, 1, 1, 8),
    _FsCnXPortPriLastSentEventTime_Type()
)
fsCnXPortPriLastSentEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCnXPortPriLastSentEventTime.setStatus("current")
_FsCnNotifications_ObjectIdentity = ObjectIdentity
fsCnNotifications = _FsCnNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 4)
)
_FsCnTraps_ObjectIdentity = ObjectIdentity
fsCnTraps = _FsCnTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 4, 0)
)
_FsCnCnmQOffset_Type = Integer32
_FsCnCnmQOffset_Object = MibScalar
fsCnCnmQOffset = _FsCnCnmQOffset_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 4, 1),
    _FsCnCnmQOffset_Type()
)
fsCnCnmQOffset.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsCnCnmQOffset.setStatus("current")
_FsCnCnmQDelta_Type = Integer32
_FsCnCnmQDelta_Object = MibScalar
fsCnCnmQDelta = _FsCnCnmQDelta_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 4, 2),
    _FsCnCnmQDelta_Type()
)
fsCnCnmQDelta.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fsCnCnmQDelta.setStatus("current")
ieee8021CnGlobalEntry.registerAugmentions(
    ("ARICENT-CN-MIB",
     "fsCnXGlobalEntry")
)
fsCnXGlobalEntry.setIndexNames(*ieee8021CnGlobalEntry.getIndexNames())
ieee8021CnPortPriEntry.registerAugmentions(
    ("ARICENT-CN-MIB",
     "fsCnXPortPriEntry")
)
fsCnXPortPriEntry.setIndexNames(*ieee8021CnPortPriEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsCnEpEntryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 4, 0, 1)
)
fsCnEpEntryTrap.setObjects(
    ("ARICENT-CN-MIB", "fsCnXPortPriErrorEntry")
)
if mibBuilder.loadTexts:
    fsCnEpEntryTrap.setStatus(
        "current"
    )

fsCnCNMTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 47, 4, 0, 2)
)
fsCnCNMTrap.setObjects(
      *(("IEEE8021-CN-MIB", "ieee8021CnCpIdentifier"),
        ("ARICENT-CN-MIB", "fsCnCnmQOffset"),
        ("ARICENT-CN-MIB", "fsCnCnmQDelta"))
)
if mibBuilder.loadTexts:
    fsCnCNMTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-CN-MIB",
    **{"fscn": fscn,
       "fsCnMaster": fsCnMaster,
       "fsCnSystemControl": fsCnSystemControl,
       "fsCnGlobalEnableTrap": fsCnGlobalEnableTrap,
       "fsCnComponent": fsCnComponent,
       "fsCnXGlobalTable": fsCnXGlobalTable,
       "fsCnXGlobalEntry": fsCnXGlobalEntry,
       "fsCnXGlobalTraceLevel": fsCnXGlobalTraceLevel,
       "fsCnXGlobalClearCounters": fsCnXGlobalClearCounters,
       "fsCnXGlobalTLVErrors": fsCnXGlobalTLVErrors,
       "fsCnPortPriority": fsCnPortPriority,
       "fsCnXPortPriTable": fsCnXPortPriTable,
       "fsCnXPortPriEntry": fsCnXPortPriEntry,
       "fsCnXPortPriClearCpCounters": fsCnXPortPriClearCpCounters,
       "fsCnXPortPriErrorEntry": fsCnXPortPriErrorEntry,
       "fsCnXPortPriOperDefMode": fsCnXPortPriOperDefMode,
       "fsCnXPortPriOperAltPri": fsCnXPortPriOperAltPri,
       "fsCnXPortPriLastRcvdEvent": fsCnXPortPriLastRcvdEvent,
       "fsCnXPortPriLastRcvdEventTime": fsCnXPortPriLastRcvdEventTime,
       "fsCnXPortPriLastSentEvent": fsCnXPortPriLastSentEvent,
       "fsCnXPortPriLastSentEventTime": fsCnXPortPriLastSentEventTime,
       "fsCnNotifications": fsCnNotifications,
       "fsCnTraps": fsCnTraps,
       "fsCnEpEntryTrap": fsCnEpEntryTrap,
       "fsCnCNMTrap": fsCnCNMTrap,
       "fsCnCnmQOffset": fsCnCnmQOffset,
       "fsCnCnmQDelta": fsCnCnmQDelta}
)
