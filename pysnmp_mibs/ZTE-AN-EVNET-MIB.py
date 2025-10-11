# SNMP MIB module (ZTE-AN-EVNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-EVNET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:06 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

zxAnEventMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190)
)
if mibBuilder.loadTexts:
    zxAnEventMib.setRevisions(
        ("2010-01-20 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ResourceId(TextualConvention, ObjectIdentifier):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAn_ObjectIdentity = ObjectIdentity
zxAn = _ZxAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_ZxAnEventSysObjects_ObjectIdentity = ObjectIdentity
zxAnEventSysObjects = _ZxAnEventSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1)
)


class _ZxAnEventCurrentEventId_Type(Integer32):
    """Custom type zxAnEventCurrentEventId based on Integer32"""
    defaultValue = 0


_ZxAnEventCurrentEventId_Type.__name__ = "Integer32"
_ZxAnEventCurrentEventId_Object = MibScalar
zxAnEventCurrentEventId = _ZxAnEventCurrentEventId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1, 1),
    _ZxAnEventCurrentEventId_Type()
)
zxAnEventCurrentEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventCurrentEventId.setStatus("current")
_ZxAnEventNmsHelloTrapMgmt_ObjectIdentity = ObjectIdentity
zxAnEventNmsHelloTrapMgmt = _ZxAnEventNmsHelloTrapMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1, 2)
)


class _ZxAnEventNmsHelloTrapEnable_Type(Integer32):
    """Custom type zxAnEventNmsHelloTrapEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventNmsHelloTrapEnable_Type.__name__ = "Integer32"
_ZxAnEventNmsHelloTrapEnable_Object = MibScalar
zxAnEventNmsHelloTrapEnable = _ZxAnEventNmsHelloTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1, 2, 1),
    _ZxAnEventNmsHelloTrapEnable_Type()
)
zxAnEventNmsHelloTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventNmsHelloTrapEnable.setStatus("current")


class _ZxAnEventNmsHelloTrapInterval_Type(Integer32):
    """Custom type zxAnEventNmsHelloTrapInterval based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 600),
    )


_ZxAnEventNmsHelloTrapInterval_Type.__name__ = "Integer32"
_ZxAnEventNmsHelloTrapInterval_Object = MibScalar
zxAnEventNmsHelloTrapInterval = _ZxAnEventNmsHelloTrapInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1, 2, 2),
    _ZxAnEventNmsHelloTrapInterval_Type()
)
zxAnEventNmsHelloTrapInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventNmsHelloTrapInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEventNmsHelloTrapInterval.setUnits("second")


class _ZxAnEventCapabilities_Type(Bits):
    """Custom type zxAnEventCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("snmpOperType", 0),
          ("reserved", 1),
          ("receiverPort", 2),
          ("securityLevel", 3))
    )

_ZxAnEventCapabilities_Type.__name__ = "Bits"
_ZxAnEventCapabilities_Object = MibScalar
zxAnEventCapabilities = _ZxAnEventCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1, 3),
    _ZxAnEventCapabilities_Type()
)
zxAnEventCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEventCapabilities.setStatus("current")


class _ZxAnEventSendingLimit_Type(Integer32):
    """Custom type zxAnEventSendingLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ZxAnEventSendingLimit_Type.__name__ = "Integer32"
_ZxAnEventSendingLimit_Object = MibScalar
zxAnEventSendingLimit = _ZxAnEventSendingLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1, 4),
    _ZxAnEventSendingLimit_Type()
)
zxAnEventSendingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventSendingLimit.setStatus("current")


class _ZxAnEventMaskEnable_Type(Integer32):
    """Custom type zxAnEventMaskEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventMaskEnable_Type.__name__ = "Integer32"
_ZxAnEventMaskEnable_Object = MibScalar
zxAnEventMaskEnable = _ZxAnEventMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 1, 5),
    _ZxAnEventMaskEnable_Type()
)
zxAnEventMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventMaskEnable.setStatus("current")
_ZxAnEventConfirmObjects_ObjectIdentity = ObjectIdentity
zxAnEventConfirmObjects = _ZxAnEventConfirmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 2)
)
_ZxAnEventConfirmEventId_Type = Integer32
_ZxAnEventConfirmEventId_Object = MibScalar
zxAnEventConfirmEventId = _ZxAnEventConfirmEventId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 2, 1),
    _ZxAnEventConfirmEventId_Type()
)
zxAnEventConfirmEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventConfirmEventId.setStatus("current")
_ZxAnEventConfirmClearedEventId_Type = Integer32
_ZxAnEventConfirmClearedEventId_Object = MibScalar
zxAnEventConfirmClearedEventId = _ZxAnEventConfirmClearedEventId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 2, 2),
    _ZxAnEventConfirmClearedEventId_Type()
)
zxAnEventConfirmClearedEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventConfirmClearedEventId.setStatus("current")


class _ZxAnEventConfirmTimeout_Type(Integer32):
    """Custom type zxAnEventConfirmTimeout based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 1800),
    )


_ZxAnEventConfirmTimeout_Type.__name__ = "Integer32"
_ZxAnEventConfirmTimeout_Object = MibScalar
zxAnEventConfirmTimeout = _ZxAnEventConfirmTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 2, 3),
    _ZxAnEventConfirmTimeout_Type()
)
zxAnEventConfirmTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventConfirmTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEventConfirmTimeout.setUnits("seconds")


class _ZxAnEventResendingTimes_Type(Integer32):
    """Custom type zxAnEventResendingTimes based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_ZxAnEventResendingTimes_Type.__name__ = "Integer32"
_ZxAnEventResendingTimes_Object = MibScalar
zxAnEventResendingTimes = _ZxAnEventResendingTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 2, 4),
    _ZxAnEventResendingTimes_Type()
)
zxAnEventResendingTimes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventResendingTimes.setStatus("current")
_ZxAnEventSynchObjects_ObjectIdentity = ObjectIdentity
zxAnEventSynchObjects = _ZxAnEventSynchObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 3)
)
_ZxAnEventSyncUnconfirmedEvents_Type = Integer32
_ZxAnEventSyncUnconfirmedEvents_Object = MibScalar
zxAnEventSyncUnconfirmedEvents = _ZxAnEventSyncUnconfirmedEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 3, 1),
    _ZxAnEventSyncUnconfirmedEvents_Type()
)
zxAnEventSyncUnconfirmedEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventSyncUnconfirmedEvents.setStatus("current")
_ZxAnEventSyncSpecificEvents_Type = ObjectIdentifier
_ZxAnEventSyncSpecificEvents_Object = MibScalar
zxAnEventSyncSpecificEvents = _ZxAnEventSyncSpecificEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 3, 2),
    _ZxAnEventSyncSpecificEvents_Type()
)
zxAnEventSyncSpecificEvents.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventSyncSpecificEvents.setStatus("current")
_ZxAnEventSyncNextEventIdList_Type = ObjectIdentifier
_ZxAnEventSyncNextEventIdList_Object = MibScalar
zxAnEventSyncNextEventIdList = _ZxAnEventSyncNextEventIdList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 3, 3),
    _ZxAnEventSyncNextEventIdList_Type()
)
zxAnEventSyncNextEventIdList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEventSyncNextEventIdList.setStatus("current")
_ZxAnEventSyncStartEventId_Type = Integer32
_ZxAnEventSyncStartEventId_Object = MibScalar
zxAnEventSyncStartEventId = _ZxAnEventSyncStartEventId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 3, 4),
    _ZxAnEventSyncStartEventId_Type()
)
zxAnEventSyncStartEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventSyncStartEventId.setStatus("current")
_ZxAnEventConfObjects_ObjectIdentity = ObjectIdentity
zxAnEventConfObjects = _ZxAnEventConfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4)
)
_ZxAnEventConfTable_Object = MibTable
zxAnEventConfTable = _ZxAnEventConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnEventConfTable.setStatus("current")
_ZxAnEventConfEntry_Object = MibTableRow
zxAnEventConfEntry = _ZxAnEventConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 1, 1)
)
zxAnEventConfEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventConfTrapOid"),
)
if mibBuilder.loadTexts:
    zxAnEventConfEntry.setStatus("current")
_ZxAnEventConfTrapOid_Type = ObjectIdentifier
_ZxAnEventConfTrapOid_Object = MibTableColumn
zxAnEventConfTrapOid = _ZxAnEventConfTrapOid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 1, 1, 1),
    _ZxAnEventConfTrapOid_Type()
)
zxAnEventConfTrapOid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventConfTrapOid.setStatus("current")


class _ZxAnEventName_Type(DisplayString):
    """Custom type zxAnEventName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEventName_Type.__name__ = "DisplayString"
_ZxAnEventName_Object = MibTableColumn
zxAnEventName = _ZxAnEventName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 1, 1, 2),
    _ZxAnEventName_Type()
)
zxAnEventName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEventName.setStatus("current")


class _ZxAnEventConfSeverityLevel_Type(Integer32):
    """Custom type zxAnEventConfSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3),
          ("indeterminate", 4))
    )


_ZxAnEventConfSeverityLevel_Type.__name__ = "Integer32"
_ZxAnEventConfSeverityLevel_Object = MibTableColumn
zxAnEventConfSeverityLevel = _ZxAnEventConfSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 1, 1, 3),
    _ZxAnEventConfSeverityLevel_Type()
)
zxAnEventConfSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventConfSeverityLevel.setStatus("current")
_ZxAnEventDeleteEventId_Type = Integer32
_ZxAnEventDeleteEventId_Object = MibScalar
zxAnEventDeleteEventId = _ZxAnEventDeleteEventId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 2),
    _ZxAnEventDeleteEventId_Type()
)
zxAnEventDeleteEventId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventDeleteEventId.setStatus("current")
_ZxAnEventCtrlProfileTable_Object = MibTable
zxAnEventCtrlProfileTable = _ZxAnEventCtrlProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 3)
)
if mibBuilder.loadTexts:
    zxAnEventCtrlProfileTable.setStatus("current")
_ZxAnEventCtrlProfileEntry_Object = MibTableRow
zxAnEventCtrlProfileEntry = _ZxAnEventCtrlProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 3, 1)
)
zxAnEventCtrlProfileEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventCtrlProfileName"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventCode"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventReportChannelType"),
)
if mibBuilder.loadTexts:
    zxAnEventCtrlProfileEntry.setStatus("current")
_ZxAnEventCtrlProfileName_Type = DisplayString
_ZxAnEventCtrlProfileName_Object = MibTableColumn
zxAnEventCtrlProfileName = _ZxAnEventCtrlProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 3, 1, 1),
    _ZxAnEventCtrlProfileName_Type()
)
zxAnEventCtrlProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventCtrlProfileName.setStatus("current")
_ZxAnEventCode_Type = Integer32
_ZxAnEventCode_Object = MibTableColumn
zxAnEventCode = _ZxAnEventCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 3, 1, 2),
    _ZxAnEventCode_Type()
)
zxAnEventCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventCode.setStatus("current")


class _ZxAnEventReportChannelType_Type(Integer32):
    """Custom type zxAnEventReportChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("extendedOam", 2),
          ("omci", 3))
    )


_ZxAnEventReportChannelType_Type.__name__ = "Integer32"
_ZxAnEventReportChannelType_Object = MibTableColumn
zxAnEventReportChannelType = _ZxAnEventReportChannelType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 3, 1, 3),
    _ZxAnEventReportChannelType_Type()
)
zxAnEventReportChannelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventReportChannelType.setStatus("current")
_ZxAnEventCtrlProfileRowStatus_Type = RowStatus
_ZxAnEventCtrlProfileRowStatus_Object = MibTableColumn
zxAnEventCtrlProfileRowStatus = _ZxAnEventCtrlProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 3, 1, 50),
    _ZxAnEventCtrlProfileRowStatus_Type()
)
zxAnEventCtrlProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventCtrlProfileRowStatus.setStatus("current")
_ZxAnEventIfCfgTable_Object = MibTable
zxAnEventIfCfgTable = _ZxAnEventIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4)
)
if mibBuilder.loadTexts:
    zxAnEventIfCfgTable.setStatus("current")
_ZxAnEventIfCfgEntry_Object = MibTableRow
zxAnEventIfCfgEntry = _ZxAnEventIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1)
)
zxAnEventIfCfgEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventIfCfgRack"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventIfCfgShelf"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventIfCfgSlot"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventIfCfgPort"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventIfCfgOnu"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventIfCfgIfType"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventIfCfgLogicalId"),
)
if mibBuilder.loadTexts:
    zxAnEventIfCfgEntry.setStatus("current")
_ZxAnEventIfCfgRack_Type = Integer32
_ZxAnEventIfCfgRack_Object = MibTableColumn
zxAnEventIfCfgRack = _ZxAnEventIfCfgRack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 1),
    _ZxAnEventIfCfgRack_Type()
)
zxAnEventIfCfgRack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventIfCfgRack.setStatus("current")
_ZxAnEventIfCfgShelf_Type = Integer32
_ZxAnEventIfCfgShelf_Object = MibTableColumn
zxAnEventIfCfgShelf = _ZxAnEventIfCfgShelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 2),
    _ZxAnEventIfCfgShelf_Type()
)
zxAnEventIfCfgShelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventIfCfgShelf.setStatus("current")
_ZxAnEventIfCfgSlot_Type = Integer32
_ZxAnEventIfCfgSlot_Object = MibTableColumn
zxAnEventIfCfgSlot = _ZxAnEventIfCfgSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 3),
    _ZxAnEventIfCfgSlot_Type()
)
zxAnEventIfCfgSlot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventIfCfgSlot.setStatus("current")
_ZxAnEventIfCfgPort_Type = Integer32
_ZxAnEventIfCfgPort_Object = MibTableColumn
zxAnEventIfCfgPort = _ZxAnEventIfCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 4),
    _ZxAnEventIfCfgPort_Type()
)
zxAnEventIfCfgPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventIfCfgPort.setStatus("current")
_ZxAnEventIfCfgOnu_Type = Integer32
_ZxAnEventIfCfgOnu_Object = MibTableColumn
zxAnEventIfCfgOnu = _ZxAnEventIfCfgOnu_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 5),
    _ZxAnEventIfCfgOnu_Type()
)
zxAnEventIfCfgOnu.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventIfCfgOnu.setStatus("current")


class _ZxAnEventIfCfgIfType_Type(Integer32):
    """Custom type zxAnEventIfCfgIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              11,
              12,
              255)
        )
    )
    namedValues = NamedValues(
        *(("physicalPort", 1),
          ("bridgePort", 2),
          ("ponOnu", 3),
          ("ponVPort", 4),
          ("onuUni", 5),
          ("servicePort", 11),
          ("vlan", 12),
          ("card", 255))
    )


_ZxAnEventIfCfgIfType_Type.__name__ = "Integer32"
_ZxAnEventIfCfgIfType_Object = MibTableColumn
zxAnEventIfCfgIfType = _ZxAnEventIfCfgIfType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 6),
    _ZxAnEventIfCfgIfType_Type()
)
zxAnEventIfCfgIfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventIfCfgIfType.setStatus("current")
_ZxAnEventIfCfgLogicalId_Type = ObjectIdentifier
_ZxAnEventIfCfgLogicalId_Object = MibTableColumn
zxAnEventIfCfgLogicalId = _ZxAnEventIfCfgLogicalId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 7),
    _ZxAnEventIfCfgLogicalId_Type()
)
zxAnEventIfCfgLogicalId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventIfCfgLogicalId.setStatus("current")


class _ZxAnEventIfCfgMaskEnable_Type(Integer32):
    """Custom type zxAnEventIfCfgMaskEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventIfCfgMaskEnable_Type.__name__ = "Integer32"
_ZxAnEventIfCfgMaskEnable_Object = MibTableColumn
zxAnEventIfCfgMaskEnable = _ZxAnEventIfCfgMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 8),
    _ZxAnEventIfCfgMaskEnable_Type()
)
zxAnEventIfCfgMaskEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventIfCfgMaskEnable.setStatus("current")
_ZxAnEventIfCfgProfileName_Type = DisplayString
_ZxAnEventIfCfgProfileName_Object = MibTableColumn
zxAnEventIfCfgProfileName = _ZxAnEventIfCfgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 9),
    _ZxAnEventIfCfgProfileName_Type()
)
zxAnEventIfCfgProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventIfCfgProfileName.setStatus("current")
_ZxAnEventIfCfgRowStatus_Type = RowStatus
_ZxAnEventIfCfgRowStatus_Object = MibTableColumn
zxAnEventIfCfgRowStatus = _ZxAnEventIfCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 4, 1, 50),
    _ZxAnEventIfCfgRowStatus_Type()
)
zxAnEventIfCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventIfCfgRowStatus.setStatus("current")
_ZxAnEventVlanCfgTable_Object = MibTable
zxAnEventVlanCfgTable = _ZxAnEventVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 5)
)
if mibBuilder.loadTexts:
    zxAnEventVlanCfgTable.setStatus("current")
_ZxAnEventVlanCfgEntry_Object = MibTableRow
zxAnEventVlanCfgEntry = _ZxAnEventVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 5, 1)
)
zxAnEventVlanCfgEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventVlanCfgVlanId"),
)
if mibBuilder.loadTexts:
    zxAnEventVlanCfgEntry.setStatus("current")


class _ZxAnEventVlanCfgVlanId_Type(Integer32):
    """Custom type zxAnEventVlanCfgVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEventVlanCfgVlanId_Type.__name__ = "Integer32"
_ZxAnEventVlanCfgVlanId_Object = MibTableColumn
zxAnEventVlanCfgVlanId = _ZxAnEventVlanCfgVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 5, 1, 1),
    _ZxAnEventVlanCfgVlanId_Type()
)
zxAnEventVlanCfgVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventVlanCfgVlanId.setStatus("current")


class _ZxAnEventVlanCfgMaskEnable_Type(Integer32):
    """Custom type zxAnEventVlanCfgMaskEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventVlanCfgMaskEnable_Type.__name__ = "Integer32"
_ZxAnEventVlanCfgMaskEnable_Object = MibTableColumn
zxAnEventVlanCfgMaskEnable = _ZxAnEventVlanCfgMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 5, 1, 2),
    _ZxAnEventVlanCfgMaskEnable_Type()
)
zxAnEventVlanCfgMaskEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventVlanCfgMaskEnable.setStatus("current")
_ZxAnEventVlanCfgProfileName_Type = DisplayString
_ZxAnEventVlanCfgProfileName_Object = MibTableColumn
zxAnEventVlanCfgProfileName = _ZxAnEventVlanCfgProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 5, 1, 3),
    _ZxAnEventVlanCfgProfileName_Type()
)
zxAnEventVlanCfgProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventVlanCfgProfileName.setStatus("current")
_ZxAnEventVlanCfgRowStatus_Type = RowStatus
_ZxAnEventVlanCfgRowStatus_Object = MibTableColumn
zxAnEventVlanCfgRowStatus = _ZxAnEventVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 4, 5, 1, 50),
    _ZxAnEventVlanCfgRowStatus_Type()
)
zxAnEventVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventVlanCfgRowStatus.setStatus("current")
_ZxAnEventRecieverObjects_ObjectIdentity = ObjectIdentity
zxAnEventRecieverObjects = _ZxAnEventRecieverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5)
)
_ZxAnEventRecieverTable_Object = MibTable
zxAnEventRecieverTable = _ZxAnEventRecieverTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnEventRecieverTable.setStatus("current")
_ZxAnEventRecieverEntry_Object = MibTableRow
zxAnEventRecieverEntry = _ZxAnEventRecieverEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1)
)
zxAnEventRecieverEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventReceiverIndex"),
)
if mibBuilder.loadTexts:
    zxAnEventRecieverEntry.setStatus("current")


class _ZxAnEventReceiverIndex_Type(Integer32):
    """Custom type zxAnEventReceiverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnEventReceiverIndex_Type.__name__ = "Integer32"
_ZxAnEventReceiverIndex_Object = MibTableColumn
zxAnEventReceiverIndex = _ZxAnEventReceiverIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 1),
    _ZxAnEventReceiverIndex_Type()
)
zxAnEventReceiverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventReceiverIndex.setStatus("current")
_ZxAnEventReceiverIpAddr_Type = IpAddress
_ZxAnEventReceiverIpAddr_Object = MibTableColumn
zxAnEventReceiverIpAddr = _ZxAnEventReceiverIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 2),
    _ZxAnEventReceiverIpAddr_Type()
)
zxAnEventReceiverIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverIpAddr.setStatus("current")


class _ZxAnEventReceiverSnmpVer_Type(Integer32):
    """Custom type zxAnEventReceiverSnmpVer based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpV1", 1),
          ("snmpV2c", 2),
          ("snmpV3", 3))
    )


_ZxAnEventReceiverSnmpVer_Type.__name__ = "Integer32"
_ZxAnEventReceiverSnmpVer_Object = MibTableColumn
zxAnEventReceiverSnmpVer = _ZxAnEventReceiverSnmpVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 3),
    _ZxAnEventReceiverSnmpVer_Type()
)
zxAnEventReceiverSnmpVer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverSnmpVer.setStatus("current")


class _ZxAnEventReceiverCommunity_Type(DisplayString):
    """Custom type zxAnEventReceiverCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_ZxAnEventReceiverCommunity_Type.__name__ = "DisplayString"
_ZxAnEventReceiverCommunity_Object = MibTableColumn
zxAnEventReceiverCommunity = _ZxAnEventReceiverCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 4),
    _ZxAnEventReceiverCommunity_Type()
)
zxAnEventReceiverCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverCommunity.setStatus("current")


class _ZxAnEventReceiverEventFormat_Type(Integer32):
    """Custom type zxAnEventReceiverEventFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpTrap", 1),
          ("snmpInform", 2),
          ("snmpTrapForPccw", 3))
    )


_ZxAnEventReceiverEventFormat_Type.__name__ = "Integer32"
_ZxAnEventReceiverEventFormat_Object = MibTableColumn
zxAnEventReceiverEventFormat = _ZxAnEventReceiverEventFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 5),
    _ZxAnEventReceiverEventFormat_Type()
)
zxAnEventReceiverEventFormat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverEventFormat.setStatus("current")


class _ZxAnEventReceiverEventType_Type(Bits):
    """Custom type zxAnEventReceiverEventType based on Bits"""
    defaultBinValue = "11111"

    namedValues = NamedValues(
        *(("equipmentEvent", 0),
          ("qualityOfServiceEvent", 1),
          ("communicationsEvent", 2),
          ("environmentEvent", 3),
          ("processingErrorEvent", 4))
    )

_ZxAnEventReceiverEventType_Type.__name__ = "Bits"
_ZxAnEventReceiverEventType_Object = MibTableColumn
zxAnEventReceiverEventType = _ZxAnEventReceiverEventType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 6),
    _ZxAnEventReceiverEventType_Type()
)
zxAnEventReceiverEventType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverEventType.setStatus("current")


class _ZxAnEventReceiverMinEventLevel_Type(Integer32):
    """Custom type zxAnEventReceiverMinEventLevel based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3),
          ("indeterminate", 4),
          ("cleared", 5),
          ("notification", 6))
    )


_ZxAnEventReceiverMinEventLevel_Type.__name__ = "Integer32"
_ZxAnEventReceiverMinEventLevel_Object = MibTableColumn
zxAnEventReceiverMinEventLevel = _ZxAnEventReceiverMinEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 7),
    _ZxAnEventReceiverMinEventLevel_Type()
)
zxAnEventReceiverMinEventLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverMinEventLevel.setStatus("current")


class _ZxAnEventReceiverEnable_Type(Integer32):
    """Custom type zxAnEventReceiverEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventReceiverEnable_Type.__name__ = "Integer32"
_ZxAnEventReceiverEnable_Object = MibTableColumn
zxAnEventReceiverEnable = _ZxAnEventReceiverEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 8),
    _ZxAnEventReceiverEnable_Type()
)
zxAnEventReceiverEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverEnable.setStatus("current")
_ZxAnEventReceiverIsZteNmsSever_Type = TruthValue
_ZxAnEventReceiverIsZteNmsSever_Object = MibTableColumn
zxAnEventReceiverIsZteNmsSever = _ZxAnEventReceiverIsZteNmsSever_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 9),
    _ZxAnEventReceiverIsZteNmsSever_Type()
)
zxAnEventReceiverIsZteNmsSever.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverIsZteNmsSever.setStatus("current")


class _ZxAnEventReceiverSecurityLevel_Type(Integer32):
    """Custom type zxAnEventReceiverSecurityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAuthNoPriv", 1),
          ("authNoPriv", 2),
          ("authPriv", 3))
    )


_ZxAnEventReceiverSecurityLevel_Type.__name__ = "Integer32"
_ZxAnEventReceiverSecurityLevel_Object = MibTableColumn
zxAnEventReceiverSecurityLevel = _ZxAnEventReceiverSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 10),
    _ZxAnEventReceiverSecurityLevel_Type()
)
zxAnEventReceiverSecurityLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverSecurityLevel.setStatus("current")


class _ZxAnEventReceiverPort_Type(Integer32):
    """Custom type zxAnEventReceiverPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnEventReceiverPort_Type.__name__ = "Integer32"
_ZxAnEventReceiverPort_Object = MibTableColumn
zxAnEventReceiverPort = _ZxAnEventReceiverPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 11),
    _ZxAnEventReceiverPort_Type()
)
zxAnEventReceiverPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverPort.setStatus("current")
_ZxAnEventReceiverRowStatus_Type = RowStatus
_ZxAnEventReceiverRowStatus_Object = MibTableColumn
zxAnEventReceiverRowStatus = _ZxAnEventReceiverRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 5, 1, 1, 15),
    _ZxAnEventReceiverRowStatus_Type()
)
zxAnEventReceiverRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventReceiverRowStatus.setStatus("current")
_ZxAnEventTrapObjects_ObjectIdentity = ObjectIdentity
zxAnEventTrapObjects = _ZxAnEventTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 6)
)
_ZxAnEventSyslogObjects_ObjectIdentity = ObjectIdentity
zxAnEventSyslogObjects = _ZxAnEventSyslogObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7)
)
_ZxAnEventSyslogTable_Object = MibTable
zxAnEventSyslogTable = _ZxAnEventSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1)
)
if mibBuilder.loadTexts:
    zxAnEventSyslogTable.setStatus("current")
_ZxAnEventSyslogEntry_Object = MibTableRow
zxAnEventSyslogEntry = _ZxAnEventSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1)
)
zxAnEventSyslogEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventSyslogSvrIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnEventSyslogEntry.setStatus("current")
_ZxAnEventSyslogSvrIpAddr_Type = IpAddress
_ZxAnEventSyslogSvrIpAddr_Object = MibTableColumn
zxAnEventSyslogSvrIpAddr = _ZxAnEventSyslogSvrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1, 1),
    _ZxAnEventSyslogSvrIpAddr_Type()
)
zxAnEventSyslogSvrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventSyslogSvrIpAddr.setStatus("current")


class _ZxAnEventSyslogSvrPort_Type(Integer32):
    """Custom type zxAnEventSyslogSvrPort based on Integer32"""
    defaultValue = 514


_ZxAnEventSyslogSvrPort_Type.__name__ = "Integer32"
_ZxAnEventSyslogSvrPort_Object = MibTableColumn
zxAnEventSyslogSvrPort = _ZxAnEventSyslogSvrPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1, 2),
    _ZxAnEventSyslogSvrPort_Type()
)
zxAnEventSyslogSvrPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventSyslogSvrPort.setStatus("current")


class _ZxAnEventSyslogType_Type(Bits):
    """Custom type zxAnEventSyslogType based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("cmdlog", 0),
          ("snmplog", 1),
          ("debugmsg", 2),
          ("alarmlog", 3))
    )

_ZxAnEventSyslogType_Type.__name__ = "Bits"
_ZxAnEventSyslogType_Object = MibTableColumn
zxAnEventSyslogType = _ZxAnEventSyslogType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1, 3),
    _ZxAnEventSyslogType_Type()
)
zxAnEventSyslogType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventSyslogType.setStatus("current")


class _ZxAnEventSyslogMinAlarmLevel_Type(Integer32):
    """Custom type zxAnEventSyslogMinAlarmLevel based on Integer32"""
    defaultValue = 6

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
        *(("major", 1),
          ("minor", 2),
          ("warning", 3),
          ("indeterminate", 4),
          ("cleared", 5),
          ("notification", 6))
    )


_ZxAnEventSyslogMinAlarmLevel_Type.__name__ = "Integer32"
_ZxAnEventSyslogMinAlarmLevel_Object = MibTableColumn
zxAnEventSyslogMinAlarmLevel = _ZxAnEventSyslogMinAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1, 4),
    _ZxAnEventSyslogMinAlarmLevel_Type()
)
zxAnEventSyslogMinAlarmLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventSyslogMinAlarmLevel.setStatus("current")


class _ZxAnEventSyslogEnable_Type(Integer32):
    """Custom type zxAnEventSyslogEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventSyslogEnable_Type.__name__ = "Integer32"
_ZxAnEventSyslogEnable_Object = MibTableColumn
zxAnEventSyslogEnable = _ZxAnEventSyslogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1, 5),
    _ZxAnEventSyslogEnable_Type()
)
zxAnEventSyslogEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventSyslogEnable.setStatus("current")


class _ZxAnEventSyslogSnmpOperType_Type(Integer32):
    """Custom type zxAnEventSyslogSnmpOperType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("get", 2),
          ("set", 3))
    )


_ZxAnEventSyslogSnmpOperType_Type.__name__ = "Integer32"
_ZxAnEventSyslogSnmpOperType_Object = MibTableColumn
zxAnEventSyslogSnmpOperType = _ZxAnEventSyslogSnmpOperType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1, 6),
    _ZxAnEventSyslogSnmpOperType_Type()
)
zxAnEventSyslogSnmpOperType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventSyslogSnmpOperType.setStatus("current")
_ZxAnEventSyslogRowStatus_Type = RowStatus
_ZxAnEventSyslogRowStatus_Object = MibTableColumn
zxAnEventSyslogRowStatus = _ZxAnEventSyslogRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 1, 1, 30),
    _ZxAnEventSyslogRowStatus_Type()
)
zxAnEventSyslogRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventSyslogRowStatus.setStatus("current")
_ZxAnEventSyslogGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnEventSyslogGlobalObjects = _ZxAnEventSyslogGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 2)
)


class _ZxAnEventSyslogFacility_Type(Integer32):
    """Custom type zxAnEventSyslogFacility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_ZxAnEventSyslogFacility_Type.__name__ = "Integer32"
_ZxAnEventSyslogFacility_Object = MibScalar
zxAnEventSyslogFacility = _ZxAnEventSyslogFacility_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 2, 1),
    _ZxAnEventSyslogFacility_Type()
)
zxAnEventSyslogFacility.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventSyslogFacility.setStatus("current")


class _ZxAnEventSyslogSeverity_Type(Integer32):
    """Custom type zxAnEventSyslogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEventSyslogSeverity_Type.__name__ = "Integer32"
_ZxAnEventSyslogSeverity_Object = MibScalar
zxAnEventSyslogSeverity = _ZxAnEventSyslogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 2, 2),
    _ZxAnEventSyslogSeverity_Type()
)
zxAnEventSyslogSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventSyslogSeverity.setStatus("current")


class _ZxAnEventSyslogSourcePort_Type(Integer32):
    """Custom type zxAnEventSyslogSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEventSyslogSourcePort_Type.__name__ = "Integer32"
_ZxAnEventSyslogSourcePort_Object = MibScalar
zxAnEventSyslogSourcePort = _ZxAnEventSyslogSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 7, 2, 3),
    _ZxAnEventSyslogSourcePort_Type()
)
zxAnEventSyslogSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventSyslogSourcePort.setStatus("current")
_ZxAnEventDefineObjects_ObjectIdentity = ObjectIdentity
zxAnEventDefineObjects = _ZxAnEventDefineObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8)
)
_ZxAnEventDefineTable_Object = MibTable
zxAnEventDefineTable = _ZxAnEventDefineTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2)
)
if mibBuilder.loadTexts:
    zxAnEventDefineTable.setStatus("current")
_ZxAnEventDefineEntry_Object = MibTableRow
zxAnEventDefineEntry = _ZxAnEventDefineEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1)
)
zxAnEventDefineEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventDefineCode"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventDefineReportChannelType"),
)
if mibBuilder.loadTexts:
    zxAnEventDefineEntry.setStatus("current")
_ZxAnEventDefineCode_Type = Integer32
_ZxAnEventDefineCode_Object = MibTableColumn
zxAnEventDefineCode = _ZxAnEventDefineCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 1),
    _ZxAnEventDefineCode_Type()
)
zxAnEventDefineCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventDefineCode.setStatus("current")


class _ZxAnEventDefineReportChannelType_Type(Integer32):
    """Custom type zxAnEventDefineReportChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("ponExtendedOam", 2),
          ("ponOmci", 3))
    )


_ZxAnEventDefineReportChannelType_Type.__name__ = "Integer32"
_ZxAnEventDefineReportChannelType_Object = MibTableColumn
zxAnEventDefineReportChannelType = _ZxAnEventDefineReportChannelType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 2),
    _ZxAnEventDefineReportChannelType_Type()
)
zxAnEventDefineReportChannelType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventDefineReportChannelType.setStatus("current")
_ZxAnEventDefineName_Type = DisplayString
_ZxAnEventDefineName_Object = MibTableColumn
zxAnEventDefineName = _ZxAnEventDefineName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 3),
    _ZxAnEventDefineName_Type()
)
zxAnEventDefineName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEventDefineName.setStatus("current")
_ZxAnEventDefineStandardAlarmCode_Type = Integer32
_ZxAnEventDefineStandardAlarmCode_Object = MibTableColumn
zxAnEventDefineStandardAlarmCode = _ZxAnEventDefineStandardAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 4),
    _ZxAnEventDefineStandardAlarmCode_Type()
)
zxAnEventDefineStandardAlarmCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEventDefineStandardAlarmCode.setStatus("current")


class _ZxAnEventDefineEventType_Type(Bits):
    """Custom type zxAnEventDefineEventType based on Bits"""
    namedValues = NamedValues(
        *(("equipmentEvent", 0),
          ("qualityOfServiceEvent", 1),
          ("communicationsEvent", 2),
          ("environmentEvent", 3),
          ("processingErrorEvent", 4))
    )

_ZxAnEventDefineEventType_Type.__name__ = "Bits"
_ZxAnEventDefineEventType_Object = MibTableColumn
zxAnEventDefineEventType = _ZxAnEventDefineEventType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 5),
    _ZxAnEventDefineEventType_Type()
)
zxAnEventDefineEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEventDefineEventType.setStatus("current")


class _ZxAnEventDefineAdminStatus_Type(Integer32):
    """Custom type zxAnEventDefineAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventDefineAdminStatus_Type.__name__ = "Integer32"
_ZxAnEventDefineAdminStatus_Object = MibTableColumn
zxAnEventDefineAdminStatus = _ZxAnEventDefineAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 6),
    _ZxAnEventDefineAdminStatus_Type()
)
zxAnEventDefineAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventDefineAdminStatus.setStatus("current")


class _ZxAnEventDefineMaskEnable_Type(Integer32):
    """Custom type zxAnEventDefineMaskEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventDefineMaskEnable_Type.__name__ = "Integer32"
_ZxAnEventDefineMaskEnable_Object = MibTableColumn
zxAnEventDefineMaskEnable = _ZxAnEventDefineMaskEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 7),
    _ZxAnEventDefineMaskEnable_Type()
)
zxAnEventDefineMaskEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventDefineMaskEnable.setStatus("current")


class _ZxAnEventDefineSendingDelay_Type(Integer32):
    """Custom type zxAnEventDefineSendingDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_ZxAnEventDefineSendingDelay_Type.__name__ = "Integer32"
_ZxAnEventDefineSendingDelay_Object = MibTableColumn
zxAnEventDefineSendingDelay = _ZxAnEventDefineSendingDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 8),
    _ZxAnEventDefineSendingDelay_Type()
)
zxAnEventDefineSendingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventDefineSendingDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEventDefineSendingDelay.setUnits("seconds")


class _ZxAnEventDefineSendingLimit_Type(Integer32):
    """Custom type zxAnEventDefineSendingLimit based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_ZxAnEventDefineSendingLimit_Type.__name__ = "Integer32"
_ZxAnEventDefineSendingLimit_Object = MibTableColumn
zxAnEventDefineSendingLimit = _ZxAnEventDefineSendingLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 9),
    _ZxAnEventDefineSendingLimit_Type()
)
zxAnEventDefineSendingLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventDefineSendingLimit.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEventDefineSendingLimit.setUnits("seconds")


class _ZxAnEventDefineReversalEnable_Type(Integer32):
    """Custom type zxAnEventDefineReversalEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnEventDefineReversalEnable_Type.__name__ = "Integer32"
_ZxAnEventDefineReversalEnable_Object = MibTableColumn
zxAnEventDefineReversalEnable = _ZxAnEventDefineReversalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 8, 2, 1, 10),
    _ZxAnEventDefineReversalEnable_Type()
)
zxAnEventDefineReversalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEventDefineReversalEnable.setStatus("current")
_ZxAnEventReportingObjects_ObjectIdentity = ObjectIdentity
zxAnEventReportingObjects = _ZxAnEventReportingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9)
)
_ZxAnEventReportCtrlObjects_ObjectIdentity = ObjectIdentity
zxAnEventReportCtrlObjects = _ZxAnEventReportCtrlObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2)
)
_ZxAnEventRptCtrlProfileTable_Object = MibTable
zxAnEventRptCtrlProfileTable = _ZxAnEventRptCtrlProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnEventRptCtrlProfileTable.setStatus("current")
_ZxAnEventRptCtrlProfileEntry_Object = MibTableRow
zxAnEventRptCtrlProfileEntry = _ZxAnEventRptCtrlProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 1, 1)
)
zxAnEventRptCtrlProfileEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventRptCtrlPrfName"),
)
if mibBuilder.loadTexts:
    zxAnEventRptCtrlProfileEntry.setStatus("current")


class _ZxAnEventRptCtrlPrfName_Type(DisplayString):
    """Custom type zxAnEventRptCtrlPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEventRptCtrlPrfName_Type.__name__ = "DisplayString"
_ZxAnEventRptCtrlPrfName_Object = MibTableColumn
zxAnEventRptCtrlPrfName = _ZxAnEventRptCtrlPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 1, 1, 1),
    _ZxAnEventRptCtrlPrfName_Type()
)
zxAnEventRptCtrlPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlPrfName.setStatus("current")
_ZxAnEventRptCtrlPrfRowStatus_Type = RowStatus
_ZxAnEventRptCtrlPrfRowStatus_Object = MibTableColumn
zxAnEventRptCtrlPrfRowStatus = _ZxAnEventRptCtrlPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 1, 1, 50),
    _ZxAnEventRptCtrlPrfRowStatus_Type()
)
zxAnEventRptCtrlPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlPrfRowStatus.setStatus("current")
_ZxAnEventRptCtrlProfileRuleTable_Object = MibTable
zxAnEventRptCtrlProfileRuleTable = _ZxAnEventRptCtrlProfileRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnEventRptCtrlProfileRuleTable.setStatus("current")
_ZxAnEventRptCtrlProfileRuleEntry_Object = MibTableRow
zxAnEventRptCtrlProfileRuleEntry = _ZxAnEventRptCtrlProfileRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 2, 1)
)
zxAnEventRptCtrlProfileRuleEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventRptCtrlPrfName"),
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventRptCtrlPrfRuleIndex"),
)
if mibBuilder.loadTexts:
    zxAnEventRptCtrlProfileRuleEntry.setStatus("current")


class _ZxAnEventRptCtrlPrfRuleIndex_Type(Integer32):
    """Custom type zxAnEventRptCtrlPrfRuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_ZxAnEventRptCtrlPrfRuleIndex_Type.__name__ = "Integer32"
_ZxAnEventRptCtrlPrfRuleIndex_Object = MibTableColumn
zxAnEventRptCtrlPrfRuleIndex = _ZxAnEventRptCtrlPrfRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 2, 1, 1),
    _ZxAnEventRptCtrlPrfRuleIndex_Type()
)
zxAnEventRptCtrlPrfRuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlPrfRuleIndex.setStatus("current")
_ZxAnEventRptCtrlEventCode_Type = Integer32
_ZxAnEventRptCtrlEventCode_Object = MibTableColumn
zxAnEventRptCtrlEventCode = _ZxAnEventRptCtrlEventCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 2, 1, 2),
    _ZxAnEventRptCtrlEventCode_Type()
)
zxAnEventRptCtrlEventCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlEventCode.setStatus("current")


class _ZxAnEventRptCtrlAdminStatus_Type(Integer32):
    """Custom type zxAnEventRptCtrlAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nalm", 1),
          ("nalmQI", 2))
    )


_ZxAnEventRptCtrlAdminStatus_Type.__name__ = "Integer32"
_ZxAnEventRptCtrlAdminStatus_Object = MibTableColumn
zxAnEventRptCtrlAdminStatus = _ZxAnEventRptCtrlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 2, 1, 21),
    _ZxAnEventRptCtrlAdminStatus_Type()
)
zxAnEventRptCtrlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlAdminStatus.setStatus("current")
_ZxAnEventRptCtrlPrfRuleRowStatus_Type = RowStatus
_ZxAnEventRptCtrlPrfRuleRowStatus_Object = MibTableColumn
zxAnEventRptCtrlPrfRuleRowStatus = _ZxAnEventRptCtrlPrfRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 2, 1, 50),
    _ZxAnEventRptCtrlPrfRuleRowStatus_Type()
)
zxAnEventRptCtrlPrfRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlPrfRuleRowStatus.setStatus("current")
_ZxAnEventRptCtrlResourceTable_Object = MibTable
zxAnEventRptCtrlResourceTable = _ZxAnEventRptCtrlResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnEventRptCtrlResourceTable.setStatus("current")
_ZxAnEventRptCtrlResourceEntry_Object = MibTableRow
zxAnEventRptCtrlResourceEntry = _ZxAnEventRptCtrlResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 3, 1)
)
zxAnEventRptCtrlResourceEntry.setIndexNames(
    (0, "ZTE-AN-EVNET-MIB", "zxAnEventRptCtrlResId"),
)
if mibBuilder.loadTexts:
    zxAnEventRptCtrlResourceEntry.setStatus("current")
_ZxAnEventRptCtrlResId_Type = ResourceId
_ZxAnEventRptCtrlResId_Object = MibTableColumn
zxAnEventRptCtrlResId = _ZxAnEventRptCtrlResId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 3, 1, 1),
    _ZxAnEventRptCtrlResId_Type()
)
zxAnEventRptCtrlResId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlResId.setStatus("current")


class _ZxAnEventRptCtrlResPrfName_Type(DisplayString):
    """Custom type zxAnEventRptCtrlResPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEventRptCtrlResPrfName_Type.__name__ = "DisplayString"
_ZxAnEventRptCtrlResPrfName_Object = MibTableColumn
zxAnEventRptCtrlResPrfName = _ZxAnEventRptCtrlResPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 3, 1, 2),
    _ZxAnEventRptCtrlResPrfName_Type()
)
zxAnEventRptCtrlResPrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlResPrfName.setStatus("current")
_ZxAnEventRptCtrlResRowStatus_Type = RowStatus
_ZxAnEventRptCtrlResRowStatus_Object = MibTableColumn
zxAnEventRptCtrlResRowStatus = _ZxAnEventRptCtrlResRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 9, 2, 3, 1, 50),
    _ZxAnEventRptCtrlResRowStatus_Type()
)
zxAnEventRptCtrlResRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEventRptCtrlResRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

zxAnEventRequestCurrentEventId = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 6, 1)
)
if mibBuilder.loadTexts:
    zxAnEventRequestCurrentEventId.setStatus(
        "current"
    )

zxAnEventNmsHelloTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 6, 2)
)
if mibBuilder.loadTexts:
    zxAnEventNmsHelloTrap.setStatus(
        "current"
    )

zxAnEventReceiverDeleteNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 190, 6, 3)
)
zxAnEventReceiverDeleteNotify.setObjects(
    ("ZTE-AN-EVNET-MIB", "zxAnEventReceiverIpAddr")
)
if mibBuilder.loadTexts:
    zxAnEventReceiverDeleteNotify.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-EVNET-MIB",
    **{"ResourceId": ResourceId,
       "zte": zte,
       "zxAn": zxAn,
       "zxAnEventMib": zxAnEventMib,
       "zxAnEventSysObjects": zxAnEventSysObjects,
       "zxAnEventCurrentEventId": zxAnEventCurrentEventId,
       "zxAnEventNmsHelloTrapMgmt": zxAnEventNmsHelloTrapMgmt,
       "zxAnEventNmsHelloTrapEnable": zxAnEventNmsHelloTrapEnable,
       "zxAnEventNmsHelloTrapInterval": zxAnEventNmsHelloTrapInterval,
       "zxAnEventCapabilities": zxAnEventCapabilities,
       "zxAnEventSendingLimit": zxAnEventSendingLimit,
       "zxAnEventMaskEnable": zxAnEventMaskEnable,
       "zxAnEventConfirmObjects": zxAnEventConfirmObjects,
       "zxAnEventConfirmEventId": zxAnEventConfirmEventId,
       "zxAnEventConfirmClearedEventId": zxAnEventConfirmClearedEventId,
       "zxAnEventConfirmTimeout": zxAnEventConfirmTimeout,
       "zxAnEventResendingTimes": zxAnEventResendingTimes,
       "zxAnEventSynchObjects": zxAnEventSynchObjects,
       "zxAnEventSyncUnconfirmedEvents": zxAnEventSyncUnconfirmedEvents,
       "zxAnEventSyncSpecificEvents": zxAnEventSyncSpecificEvents,
       "zxAnEventSyncNextEventIdList": zxAnEventSyncNextEventIdList,
       "zxAnEventSyncStartEventId": zxAnEventSyncStartEventId,
       "zxAnEventConfObjects": zxAnEventConfObjects,
       "zxAnEventConfTable": zxAnEventConfTable,
       "zxAnEventConfEntry": zxAnEventConfEntry,
       "zxAnEventConfTrapOid": zxAnEventConfTrapOid,
       "zxAnEventName": zxAnEventName,
       "zxAnEventConfSeverityLevel": zxAnEventConfSeverityLevel,
       "zxAnEventDeleteEventId": zxAnEventDeleteEventId,
       "zxAnEventCtrlProfileTable": zxAnEventCtrlProfileTable,
       "zxAnEventCtrlProfileEntry": zxAnEventCtrlProfileEntry,
       "zxAnEventCtrlProfileName": zxAnEventCtrlProfileName,
       "zxAnEventCode": zxAnEventCode,
       "zxAnEventReportChannelType": zxAnEventReportChannelType,
       "zxAnEventCtrlProfileRowStatus": zxAnEventCtrlProfileRowStatus,
       "zxAnEventIfCfgTable": zxAnEventIfCfgTable,
       "zxAnEventIfCfgEntry": zxAnEventIfCfgEntry,
       "zxAnEventIfCfgRack": zxAnEventIfCfgRack,
       "zxAnEventIfCfgShelf": zxAnEventIfCfgShelf,
       "zxAnEventIfCfgSlot": zxAnEventIfCfgSlot,
       "zxAnEventIfCfgPort": zxAnEventIfCfgPort,
       "zxAnEventIfCfgOnu": zxAnEventIfCfgOnu,
       "zxAnEventIfCfgIfType": zxAnEventIfCfgIfType,
       "zxAnEventIfCfgLogicalId": zxAnEventIfCfgLogicalId,
       "zxAnEventIfCfgMaskEnable": zxAnEventIfCfgMaskEnable,
       "zxAnEventIfCfgProfileName": zxAnEventIfCfgProfileName,
       "zxAnEventIfCfgRowStatus": zxAnEventIfCfgRowStatus,
       "zxAnEventVlanCfgTable": zxAnEventVlanCfgTable,
       "zxAnEventVlanCfgEntry": zxAnEventVlanCfgEntry,
       "zxAnEventVlanCfgVlanId": zxAnEventVlanCfgVlanId,
       "zxAnEventVlanCfgMaskEnable": zxAnEventVlanCfgMaskEnable,
       "zxAnEventVlanCfgProfileName": zxAnEventVlanCfgProfileName,
       "zxAnEventVlanCfgRowStatus": zxAnEventVlanCfgRowStatus,
       "zxAnEventRecieverObjects": zxAnEventRecieverObjects,
       "zxAnEventRecieverTable": zxAnEventRecieverTable,
       "zxAnEventRecieverEntry": zxAnEventRecieverEntry,
       "zxAnEventReceiverIndex": zxAnEventReceiverIndex,
       "zxAnEventReceiverIpAddr": zxAnEventReceiverIpAddr,
       "zxAnEventReceiverSnmpVer": zxAnEventReceiverSnmpVer,
       "zxAnEventReceiverCommunity": zxAnEventReceiverCommunity,
       "zxAnEventReceiverEventFormat": zxAnEventReceiverEventFormat,
       "zxAnEventReceiverEventType": zxAnEventReceiverEventType,
       "zxAnEventReceiverMinEventLevel": zxAnEventReceiverMinEventLevel,
       "zxAnEventReceiverEnable": zxAnEventReceiverEnable,
       "zxAnEventReceiverIsZteNmsSever": zxAnEventReceiverIsZteNmsSever,
       "zxAnEventReceiverSecurityLevel": zxAnEventReceiverSecurityLevel,
       "zxAnEventReceiverPort": zxAnEventReceiverPort,
       "zxAnEventReceiverRowStatus": zxAnEventReceiverRowStatus,
       "zxAnEventTrapObjects": zxAnEventTrapObjects,
       "zxAnEventRequestCurrentEventId": zxAnEventRequestCurrentEventId,
       "zxAnEventNmsHelloTrap": zxAnEventNmsHelloTrap,
       "zxAnEventReceiverDeleteNotify": zxAnEventReceiverDeleteNotify,
       "zxAnEventSyslogObjects": zxAnEventSyslogObjects,
       "zxAnEventSyslogTable": zxAnEventSyslogTable,
       "zxAnEventSyslogEntry": zxAnEventSyslogEntry,
       "zxAnEventSyslogSvrIpAddr": zxAnEventSyslogSvrIpAddr,
       "zxAnEventSyslogSvrPort": zxAnEventSyslogSvrPort,
       "zxAnEventSyslogType": zxAnEventSyslogType,
       "zxAnEventSyslogMinAlarmLevel": zxAnEventSyslogMinAlarmLevel,
       "zxAnEventSyslogEnable": zxAnEventSyslogEnable,
       "zxAnEventSyslogSnmpOperType": zxAnEventSyslogSnmpOperType,
       "zxAnEventSyslogRowStatus": zxAnEventSyslogRowStatus,
       "zxAnEventSyslogGlobalObjects": zxAnEventSyslogGlobalObjects,
       "zxAnEventSyslogFacility": zxAnEventSyslogFacility,
       "zxAnEventSyslogSeverity": zxAnEventSyslogSeverity,
       "zxAnEventSyslogSourcePort": zxAnEventSyslogSourcePort,
       "zxAnEventDefineObjects": zxAnEventDefineObjects,
       "zxAnEventDefineTable": zxAnEventDefineTable,
       "zxAnEventDefineEntry": zxAnEventDefineEntry,
       "zxAnEventDefineCode": zxAnEventDefineCode,
       "zxAnEventDefineReportChannelType": zxAnEventDefineReportChannelType,
       "zxAnEventDefineName": zxAnEventDefineName,
       "zxAnEventDefineStandardAlarmCode": zxAnEventDefineStandardAlarmCode,
       "zxAnEventDefineEventType": zxAnEventDefineEventType,
       "zxAnEventDefineAdminStatus": zxAnEventDefineAdminStatus,
       "zxAnEventDefineMaskEnable": zxAnEventDefineMaskEnable,
       "zxAnEventDefineSendingDelay": zxAnEventDefineSendingDelay,
       "zxAnEventDefineSendingLimit": zxAnEventDefineSendingLimit,
       "zxAnEventDefineReversalEnable": zxAnEventDefineReversalEnable,
       "zxAnEventReportingObjects": zxAnEventReportingObjects,
       "zxAnEventReportCtrlObjects": zxAnEventReportCtrlObjects,
       "zxAnEventRptCtrlProfileTable": zxAnEventRptCtrlProfileTable,
       "zxAnEventRptCtrlProfileEntry": zxAnEventRptCtrlProfileEntry,
       "zxAnEventRptCtrlPrfName": zxAnEventRptCtrlPrfName,
       "zxAnEventRptCtrlPrfRowStatus": zxAnEventRptCtrlPrfRowStatus,
       "zxAnEventRptCtrlProfileRuleTable": zxAnEventRptCtrlProfileRuleTable,
       "zxAnEventRptCtrlProfileRuleEntry": zxAnEventRptCtrlProfileRuleEntry,
       "zxAnEventRptCtrlPrfRuleIndex": zxAnEventRptCtrlPrfRuleIndex,
       "zxAnEventRptCtrlEventCode": zxAnEventRptCtrlEventCode,
       "zxAnEventRptCtrlAdminStatus": zxAnEventRptCtrlAdminStatus,
       "zxAnEventRptCtrlPrfRuleRowStatus": zxAnEventRptCtrlPrfRuleRowStatus,
       "zxAnEventRptCtrlResourceTable": zxAnEventRptCtrlResourceTable,
       "zxAnEventRptCtrlResourceEntry": zxAnEventRptCtrlResourceEntry,
       "zxAnEventRptCtrlResId": zxAnEventRptCtrlResId,
       "zxAnEventRptCtrlResPrfName": zxAnEventRptCtrlResPrfName,
       "zxAnEventRptCtrlResRowStatus": zxAnEventRptCtrlResRowStatus}
)
