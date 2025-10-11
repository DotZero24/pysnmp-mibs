# SNMP MIB module (ADTRAN-GENIF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENIF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:44 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenIf,
 adGenIfID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenIf",
    "adGenIfID")

(ifAdminStatus,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifDescr",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenIfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 7, 1)
)
if mibBuilder.loadTexts:
    adGenIfMIB.setRevisions(
        ("2013-05-31 00:00",
         "2011-12-16 00:00",
         "2011-12-06 00:00",
         "2011-02-28 00:00",
         "2008-11-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenIfAlarms_ObjectIdentity = ObjectIdentity
adGenIfAlarms = _AdGenIfAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 0)
)
_AdGenIfMIBObjects_ObjectIdentity = ObjectIdentity
adGenIfMIBObjects = _AdGenIfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1)
)
_AdGenIfTable_Object = MibTable
adGenIfTable = _AdGenIfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1)
)
if mibBuilder.loadTexts:
    adGenIfTable.setStatus("current")
_AdGenIfEntry_Object = MibTableRow
adGenIfEntry = _AdGenIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1)
)
adGenIfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenIfEntry.setStatus("current")


class _AdGenIfResetCounters_Type(Integer32):
    """Custom type adGenIfResetCounters based on Integer32"""
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
          ("pmhistory", 2),
          ("current", 3))
    )


_AdGenIfResetCounters_Type.__name__ = "Integer32"
_AdGenIfResetCounters_Object = MibTableColumn
adGenIfResetCounters = _AdGenIfResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 1),
    _AdGenIfResetCounters_Type()
)
adGenIfResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIfResetCounters.setStatus("deprecated")


class _AdGenIfAutoInServiceEnable_Type(TruthValue):
    """Custom type adGenIfAutoInServiceEnable based on TruthValue"""
    defaultValue = 2


_AdGenIfAutoInServiceEnable_Type.__name__ = "TruthValue"
_AdGenIfAutoInServiceEnable_Object = MibTableColumn
adGenIfAutoInServiceEnable = _AdGenIfAutoInServiceEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 2),
    _AdGenIfAutoInServiceEnable_Type()
)
adGenIfAutoInServiceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIfAutoInServiceEnable.setStatus("current")


class _AdGenIfAutoInServiceTimeOut_Type(Integer32):
    """Custom type adGenIfAutoInServiceTimeOut based on Integer32"""
    defaultValue = 480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9999),
    )


_AdGenIfAutoInServiceTimeOut_Type.__name__ = "Integer32"
_AdGenIfAutoInServiceTimeOut_Object = MibTableColumn
adGenIfAutoInServiceTimeOut = _AdGenIfAutoInServiceTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 3),
    _AdGenIfAutoInServiceTimeOut_Type()
)
adGenIfAutoInServiceTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIfAutoInServiceTimeOut.setStatus("current")
_AdGenIfAutoInServiceTimeOutCounter_Type = Integer32
_AdGenIfAutoInServiceTimeOutCounter_Object = MibTableColumn
adGenIfAutoInServiceTimeOutCounter = _AdGenIfAutoInServiceTimeOutCounter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 4),
    _AdGenIfAutoInServiceTimeOutCounter_Type()
)
adGenIfAutoInServiceTimeOutCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfAutoInServiceTimeOutCounter.setStatus("current")


class _AdGenIfAutoInServiceStatus_Type(Integer32):
    """Custom type adGenIfAutoInServiceStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("oosAuAinsFaf", 4),
          ("oosAuAins", 5),
          ("oosAuAinsTs", 6))
    )


_AdGenIfAutoInServiceStatus_Type.__name__ = "Integer32"
_AdGenIfAutoInServiceStatus_Object = MibTableColumn
adGenIfAutoInServiceStatus = _AdGenIfAutoInServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 5),
    _AdGenIfAutoInServiceStatus_Type()
)
adGenIfAutoInServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfAutoInServiceStatus.setStatus("current")


class _AdGenIfServiceStateOOSMAAlarmEnable_Type(Integer32):
    """Custom type adGenIfServiceStateOOSMAAlarmEnable based on Integer32"""
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


_AdGenIfServiceStateOOSMAAlarmEnable_Type.__name__ = "Integer32"
_AdGenIfServiceStateOOSMAAlarmEnable_Object = MibTableColumn
adGenIfServiceStateOOSMAAlarmEnable = _AdGenIfServiceStateOOSMAAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 6),
    _AdGenIfServiceStateOOSMAAlarmEnable_Type()
)
adGenIfServiceStateOOSMAAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIfServiceStateOOSMAAlarmEnable.setStatus("obsolete")


class _AdGenIfResetAllPM_Type(Integer32):
    """Custom type adGenIfResetAllPM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenIfResetAllPM_Type.__name__ = "Integer32"
_AdGenIfResetAllPM_Object = MibTableColumn
adGenIfResetAllPM = _AdGenIfResetAllPM_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 7),
    _AdGenIfResetAllPM_Type()
)
adGenIfResetAllPM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIfResetAllPM.setStatus("current")


class _AdGenIfResetAllCounters_Type(Integer32):
    """Custom type adGenIfResetAllCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenIfResetAllCounters_Type.__name__ = "Integer32"
_AdGenIfResetAllCounters_Object = MibTableColumn
adGenIfResetAllCounters = _AdGenIfResetAllCounters_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 8),
    _AdGenIfResetAllCounters_Type()
)
adGenIfResetAllCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenIfResetAllCounters.setStatus("current")
_AdGenIfInUnicastOctets_Type = Counter64
_AdGenIfInUnicastOctets_Object = MibTableColumn
adGenIfInUnicastOctets = _AdGenIfInUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 9),
    _AdGenIfInUnicastOctets_Type()
)
adGenIfInUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfInUnicastOctets.setStatus("current")
_AdGenIfOutUnicastOctets_Type = Counter64
_AdGenIfOutUnicastOctets_Object = MibTableColumn
adGenIfOutUnicastOctets = _AdGenIfOutUnicastOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 10),
    _AdGenIfOutUnicastOctets_Type()
)
adGenIfOutUnicastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfOutUnicastOctets.setStatus("current")
_AdGenIfInBroadcastOctets_Type = Counter64
_AdGenIfInBroadcastOctets_Object = MibTableColumn
adGenIfInBroadcastOctets = _AdGenIfInBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 11),
    _AdGenIfInBroadcastOctets_Type()
)
adGenIfInBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfInBroadcastOctets.setStatus("current")
_AdGenIfOutBroadcastOctets_Type = Counter64
_AdGenIfOutBroadcastOctets_Object = MibTableColumn
adGenIfOutBroadcastOctets = _AdGenIfOutBroadcastOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 12),
    _AdGenIfOutBroadcastOctets_Type()
)
adGenIfOutBroadcastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfOutBroadcastOctets.setStatus("current")
_AdGenIfInMulticastOctets_Type = Counter64
_AdGenIfInMulticastOctets_Object = MibTableColumn
adGenIfInMulticastOctets = _AdGenIfInMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 13),
    _AdGenIfInMulticastOctets_Type()
)
adGenIfInMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfInMulticastOctets.setStatus("current")
_AdGenIfOutMulticastOctets_Type = Counter64
_AdGenIfOutMulticastOctets_Object = MibTableColumn
adGenIfOutMulticastOctets = _AdGenIfOutMulticastOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 14),
    _AdGenIfOutMulticastOctets_Type()
)
adGenIfOutMulticastOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfOutMulticastOctets.setStatus("current")
_AdGenIfOutDiscardedOctets_Type = Counter64
_AdGenIfOutDiscardedOctets_Object = MibTableColumn
adGenIfOutDiscardedOctets = _AdGenIfOutDiscardedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 15),
    _AdGenIfOutDiscardedOctets_Type()
)
adGenIfOutDiscardedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfOutDiscardedOctets.setStatus("current")
_AdGenIfInFrames_Type = Counter64
_AdGenIfInFrames_Object = MibTableColumn
adGenIfInFrames = _AdGenIfInFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 16),
    _AdGenIfInFrames_Type()
)
adGenIfInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfInFrames.setStatus("current")
_AdGenIfOutFrames_Type = Counter64
_AdGenIfOutFrames_Object = MibTableColumn
adGenIfOutFrames = _AdGenIfOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 1, 1, 17),
    _AdGenIfOutFrames_Type()
)
adGenIfOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfOutFrames.setStatus("current")
_AdGenIfCurr15MinPMTable_Object = MibTable
adGenIfCurr15MinPMTable = _AdGenIfCurr15MinPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 2)
)
if mibBuilder.loadTexts:
    adGenIfCurr15MinPMTable.setStatus("current")
_AdGenIfCurr15MinPMEntry_Object = MibTableRow
adGenIfCurr15MinPMEntry = _AdGenIfCurr15MinPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 2, 1)
)
adGenIfCurr15MinPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenIfCurr15MinPMEntry.setStatus("current")
_AdGenIfCurr15MinPMOutDiscards_Type = Gauge32
_AdGenIfCurr15MinPMOutDiscards_Object = MibTableColumn
adGenIfCurr15MinPMOutDiscards = _AdGenIfCurr15MinPMOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 2, 1, 1),
    _AdGenIfCurr15MinPMOutDiscards_Type()
)
adGenIfCurr15MinPMOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfCurr15MinPMOutDiscards.setStatus("current")
_AdGenIfCurr15MinPMOutDiscardOctets_Type = Gauge32
_AdGenIfCurr15MinPMOutDiscardOctets_Object = MibTableColumn
adGenIfCurr15MinPMOutDiscardOctets = _AdGenIfCurr15MinPMOutDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 2, 1, 2),
    _AdGenIfCurr15MinPMOutDiscardOctets_Type()
)
adGenIfCurr15MinPMOutDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfCurr15MinPMOutDiscardOctets.setStatus("current")
_AdGenIf15MinPMTable_Object = MibTable
adGenIf15MinPMTable = _AdGenIf15MinPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 3)
)
if mibBuilder.loadTexts:
    adGenIf15MinPMTable.setStatus("current")
_AdGenIf15MinPMEntry_Object = MibTableRow
adGenIf15MinPMEntry = _AdGenIf15MinPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 3, 1)
)
adGenIf15MinPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENIF-MIB", "adGenIf15MinPMIntNumber"),
)
if mibBuilder.loadTexts:
    adGenIf15MinPMEntry.setStatus("current")
_AdGenIf15MinPMIntNumber_Type = Integer32
_AdGenIf15MinPMIntNumber_Object = MibTableColumn
adGenIf15MinPMIntNumber = _AdGenIf15MinPMIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 3, 1, 1),
    _AdGenIf15MinPMIntNumber_Type()
)
adGenIf15MinPMIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIf15MinPMIntNumber.setStatus("current")
_AdGenIf15MinPMOutDiscards_Type = Gauge32
_AdGenIf15MinPMOutDiscards_Object = MibTableColumn
adGenIf15MinPMOutDiscards = _AdGenIf15MinPMOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 3, 1, 2),
    _AdGenIf15MinPMOutDiscards_Type()
)
adGenIf15MinPMOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIf15MinPMOutDiscards.setStatus("current")
_AdGenIf15MinPMOutDiscardOctets_Type = Gauge32
_AdGenIf15MinPMOutDiscardOctets_Object = MibTableColumn
adGenIf15MinPMOutDiscardOctets = _AdGenIf15MinPMOutDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 3, 1, 3),
    _AdGenIf15MinPMOutDiscardOctets_Type()
)
adGenIf15MinPMOutDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIf15MinPMOutDiscardOctets.setStatus("current")
_AdGenIfCurr24HrPMTable_Object = MibTable
adGenIfCurr24HrPMTable = _AdGenIfCurr24HrPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 4)
)
if mibBuilder.loadTexts:
    adGenIfCurr24HrPMTable.setStatus("current")
_AdGenIfCurr24HrPMEntry_Object = MibTableRow
adGenIfCurr24HrPMEntry = _AdGenIfCurr24HrPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 4, 1)
)
adGenIfCurr24HrPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenIfCurr24HrPMEntry.setStatus("current")
_AdGenIfCurr24HrPMOutDiscards_Type = Gauge32
_AdGenIfCurr24HrPMOutDiscards_Object = MibTableColumn
adGenIfCurr24HrPMOutDiscards = _AdGenIfCurr24HrPMOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 4, 1, 1),
    _AdGenIfCurr24HrPMOutDiscards_Type()
)
adGenIfCurr24HrPMOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfCurr24HrPMOutDiscards.setStatus("current")
_AdGenIfCurr24HrPMOutDiscardOctets_Type = Gauge32
_AdGenIfCurr24HrPMOutDiscardOctets_Object = MibTableColumn
adGenIfCurr24HrPMOutDiscardOctets = _AdGenIfCurr24HrPMOutDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 4, 1, 2),
    _AdGenIfCurr24HrPMOutDiscardOctets_Type()
)
adGenIfCurr24HrPMOutDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIfCurr24HrPMOutDiscardOctets.setStatus("current")
_AdGenIf24HrPMTable_Object = MibTable
adGenIf24HrPMTable = _AdGenIf24HrPMTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 5)
)
if mibBuilder.loadTexts:
    adGenIf24HrPMTable.setStatus("current")
_AdGenIf24HrPMEntry_Object = MibTableRow
adGenIf24HrPMEntry = _AdGenIf24HrPMEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 5, 1)
)
adGenIf24HrPMEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENIF-MIB", "adGenIf24HrPMIntNumber"),
)
if mibBuilder.loadTexts:
    adGenIf24HrPMEntry.setStatus("current")
_AdGenIf24HrPMIntNumber_Type = Integer32
_AdGenIf24HrPMIntNumber_Object = MibTableColumn
adGenIf24HrPMIntNumber = _AdGenIf24HrPMIntNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 5, 1, 1),
    _AdGenIf24HrPMIntNumber_Type()
)
adGenIf24HrPMIntNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIf24HrPMIntNumber.setStatus("current")
_AdGenIf24HrPMOutDiscards_Type = Gauge32
_AdGenIf24HrPMOutDiscards_Object = MibTableColumn
adGenIf24HrPMOutDiscards = _AdGenIf24HrPMOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 5, 1, 2),
    _AdGenIf24HrPMOutDiscards_Type()
)
adGenIf24HrPMOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIf24HrPMOutDiscards.setStatus("current")
_AdGenIf24HrPMOutDiscardOctets_Type = Gauge32
_AdGenIf24HrPMOutDiscardOctets_Object = MibTableColumn
adGenIf24HrPMOutDiscardOctets = _AdGenIf24HrPMOutDiscardOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 1, 5, 1, 3),
    _AdGenIf24HrPMOutDiscardOctets_Type()
)
adGenIf24HrPMOutDiscardOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenIf24HrPMOutDiscardOctets.setStatus("current")

# Managed Objects groups


# Notification objects

adGenIfServiceStateOOSMAClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 0, 1)
)
adGenIfServiceStateOOSMAClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenIfServiceStateOOSMAClear.setStatus(
        "obsolete"
    )

adGenIfServiceStateOOSMAActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 7, 0, 2)
)
adGenIfServiceStateOOSMAActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifDescr"))
)
if mibBuilder.loadTexts:
    adGenIfServiceStateOOSMAActive.setStatus(
        "obsolete"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENIF-MIB",
    **{"adGenIfAlarms": adGenIfAlarms,
       "adGenIfServiceStateOOSMAClear": adGenIfServiceStateOOSMAClear,
       "adGenIfServiceStateOOSMAActive": adGenIfServiceStateOOSMAActive,
       "adGenIfMIBObjects": adGenIfMIBObjects,
       "adGenIfTable": adGenIfTable,
       "adGenIfEntry": adGenIfEntry,
       "adGenIfResetCounters": adGenIfResetCounters,
       "adGenIfAutoInServiceEnable": adGenIfAutoInServiceEnable,
       "adGenIfAutoInServiceTimeOut": adGenIfAutoInServiceTimeOut,
       "adGenIfAutoInServiceTimeOutCounter": adGenIfAutoInServiceTimeOutCounter,
       "adGenIfAutoInServiceStatus": adGenIfAutoInServiceStatus,
       "adGenIfServiceStateOOSMAAlarmEnable": adGenIfServiceStateOOSMAAlarmEnable,
       "adGenIfResetAllPM": adGenIfResetAllPM,
       "adGenIfResetAllCounters": adGenIfResetAllCounters,
       "adGenIfInUnicastOctets": adGenIfInUnicastOctets,
       "adGenIfOutUnicastOctets": adGenIfOutUnicastOctets,
       "adGenIfInBroadcastOctets": adGenIfInBroadcastOctets,
       "adGenIfOutBroadcastOctets": adGenIfOutBroadcastOctets,
       "adGenIfInMulticastOctets": adGenIfInMulticastOctets,
       "adGenIfOutMulticastOctets": adGenIfOutMulticastOctets,
       "adGenIfOutDiscardedOctets": adGenIfOutDiscardedOctets,
       "adGenIfInFrames": adGenIfInFrames,
       "adGenIfOutFrames": adGenIfOutFrames,
       "adGenIfCurr15MinPMTable": adGenIfCurr15MinPMTable,
       "adGenIfCurr15MinPMEntry": adGenIfCurr15MinPMEntry,
       "adGenIfCurr15MinPMOutDiscards": adGenIfCurr15MinPMOutDiscards,
       "adGenIfCurr15MinPMOutDiscardOctets": adGenIfCurr15MinPMOutDiscardOctets,
       "adGenIf15MinPMTable": adGenIf15MinPMTable,
       "adGenIf15MinPMEntry": adGenIf15MinPMEntry,
       "adGenIf15MinPMIntNumber": adGenIf15MinPMIntNumber,
       "adGenIf15MinPMOutDiscards": adGenIf15MinPMOutDiscards,
       "adGenIf15MinPMOutDiscardOctets": adGenIf15MinPMOutDiscardOctets,
       "adGenIfCurr24HrPMTable": adGenIfCurr24HrPMTable,
       "adGenIfCurr24HrPMEntry": adGenIfCurr24HrPMEntry,
       "adGenIfCurr24HrPMOutDiscards": adGenIfCurr24HrPMOutDiscards,
       "adGenIfCurr24HrPMOutDiscardOctets": adGenIfCurr24HrPMOutDiscardOctets,
       "adGenIf24HrPMTable": adGenIf24HrPMTable,
       "adGenIf24HrPMEntry": adGenIf24HrPMEntry,
       "adGenIf24HrPMIntNumber": adGenIf24HrPMIntNumber,
       "adGenIf24HrPMOutDiscards": adGenIf24HrPMOutDiscards,
       "adGenIf24HrPMOutDiscardOctets": adGenIf24HrPMOutDiscardOctets,
       "adGenIfMIB": adGenIfMIB}
)
