# SNMP MIB module (RAD-ds1Interface-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-ds1Interface-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:17:21 2025
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

(dsx1CurrentIndex,
 dsx1IntervalCSSs,
 dsx1IntervalESs,
 dsx1IntervalIndex,
 dsx1IntervalLESs,
 dsx1IntervalNumber,
 dsx1IntervalPCVs,
 dsx1IntervalSEFSs,
 dsx1IntervalSESs,
 dsx1IntervalUASs,
 dsx1LineIndex,
 dsx1LineStatus,
 dsx1LoopbackStatus,
 dsx1TotalIndex) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1CurrentIndex",
    "dsx1IntervalCSSs",
    "dsx1IntervalESs",
    "dsx1IntervalIndex",
    "dsx1IntervalLESs",
    "dsx1IntervalNumber",
    "dsx1IntervalPCVs",
    "dsx1IntervalSEFSs",
    "dsx1IntervalSESs",
    "dsx1IntervalUASs",
    "dsx1LineIndex",
    "dsx1LineStatus",
    "dsx1LoopbackStatus",
    "dsx1TotalIndex")

(InterfaceIndex,
 ifAlias) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(diverseIfWanGen,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "diverseIfWanGen")

(DayType,) = mibBuilder.importSymbols(
    "RAD-TC",
    "DayType")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ds1Interface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrtDS1Events_ObjectIdentity = ObjectIdentity
prtDS1Events = _PrtDS1Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0)
)
_PrtDs1PerfHistory_ObjectIdentity = ObjectIdentity
prtDs1PerfHistory = _PrtDs1PerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1)
)
_Dsx1XCurrentTable_Object = MibTable
dsx1XCurrentTable = _Dsx1XCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2)
)
if mibBuilder.loadTexts:
    dsx1XCurrentTable.setStatus("current")
_Dsx1XCurrentEntry_Object = MibTableRow
dsx1XCurrentEntry = _Dsx1XCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1)
)
dsx1XCurrentEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1CurrentIndex"),
)
if mibBuilder.loadTexts:
    dsx1XCurrentEntry.setStatus("current")
_Dsx1CurrentLOS_Type = PerfCurrentCount
_Dsx1CurrentLOS_Object = MibTableColumn
dsx1CurrentLOS = _Dsx1CurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 1),
    _Dsx1CurrentLOS_Type()
)
dsx1CurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOS.setStatus("current")
_Dsx1CurrentLOF_Type = PerfCurrentCount
_Dsx1CurrentLOF_Object = MibTableColumn
dsx1CurrentLOF = _Dsx1CurrentLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 2),
    _Dsx1CurrentLOF_Type()
)
dsx1CurrentLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOF.setStatus("current")
_Dsx1CurrentLOC_Type = PerfCurrentCount
_Dsx1CurrentLOC_Object = MibTableColumn
dsx1CurrentLOC = _Dsx1CurrentLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 3),
    _Dsx1CurrentLOC_Type()
)
dsx1CurrentLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOC.setStatus("current")
_Dsx1CurrentAIS_Type = PerfCurrentCount
_Dsx1CurrentAIS_Object = MibTableColumn
dsx1CurrentAIS = _Dsx1CurrentAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 4),
    _Dsx1CurrentAIS_Type()
)
dsx1CurrentAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentAIS.setStatus("current")
_Dsx1CurrentRAI_Type = PerfCurrentCount
_Dsx1CurrentRAI_Object = MibTableColumn
dsx1CurrentRAI = _Dsx1CurrentRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 5),
    _Dsx1CurrentRAI_Type()
)
dsx1CurrentRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentRAI.setStatus("current")
_Dsx1CurrentLOMF_Type = PerfCurrentCount
_Dsx1CurrentLOMF_Object = MibTableColumn
dsx1CurrentLOMF = _Dsx1CurrentLOMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 6),
    _Dsx1CurrentLOMF_Type()
)
dsx1CurrentLOMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOMF.setStatus("current")
_Dsx1CurrentFEBE_Type = PerfCurrentCount
_Dsx1CurrentFEBE_Object = MibTableColumn
dsx1CurrentFEBE = _Dsx1CurrentFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 7),
    _Dsx1CurrentFEBE_Type()
)
dsx1CurrentFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentFEBE.setStatus("current")


class _Dsx1CurrentStatus_Type(OctetString):
    """Custom type dsx1CurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dsx1CurrentStatus_Type.__name__ = "OctetString"
_Dsx1CurrentStatus_Object = MibTableColumn
dsx1CurrentStatus = _Dsx1CurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 8),
    _Dsx1CurrentStatus_Type()
)
dsx1CurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentStatus.setStatus("current")
_Dsx1CurrentBPV_Type = PerfCurrentCount
_Dsx1CurrentBPV_Object = MibTableColumn
dsx1CurrentBPV = _Dsx1CurrentBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 9),
    _Dsx1CurrentBPV_Type()
)
dsx1CurrentBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentBPV.setStatus("current")
_Dsx1CurrentLOCRCMF_Type = PerfCurrentCount
_Dsx1CurrentLOCRCMF_Object = MibTableColumn
dsx1CurrentLOCRCMF = _Dsx1CurrentLOCRCMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 10),
    _Dsx1CurrentLOCRCMF_Type()
)
dsx1CurrentLOCRCMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOCRCMF.setStatus("current")
_Dsx1CurrentLOFC_Type = PerfCurrentCount
_Dsx1CurrentLOFC_Object = MibTableColumn
dsx1CurrentLOFC = _Dsx1CurrentLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 11),
    _Dsx1CurrentLOFC_Type()
)
dsx1CurrentLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLOFC.setStatus("current")
_Dsx1CurrentCRCErrors_Type = PerfCurrentCount
_Dsx1CurrentCRCErrors_Object = MibTableColumn
dsx1CurrentCRCErrors = _Dsx1CurrentCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 12),
    _Dsx1CurrentCRCErrors_Type()
)
dsx1CurrentCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentCRCErrors.setStatus("current")
_Dsx1CurrentLSES_Type = PerfCurrentCount
_Dsx1CurrentLSES_Object = MibTableColumn
dsx1CurrentLSES = _Dsx1CurrentLSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 13),
    _Dsx1CurrentLSES_Type()
)
dsx1CurrentLSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentLSES.setStatus("current")
_Dsx1CurrentFC_Type = PerfCurrentCount
_Dsx1CurrentFC_Object = MibTableColumn
dsx1CurrentFC = _Dsx1CurrentFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 2, 1, 14),
    _Dsx1CurrentFC_Type()
)
dsx1CurrentFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1CurrentFC.setStatus("current")
_Dsx1XIntervalTable_Object = MibTable
dsx1XIntervalTable = _Dsx1XIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3)
)
if mibBuilder.loadTexts:
    dsx1XIntervalTable.setStatus("deprecated")
_Dsx1XIntervalEntry_Object = MibTableRow
dsx1XIntervalEntry = _Dsx1XIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1)
)
dsx1XIntervalEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1IntervalIndex"),
    (0, "DS1-MIB", "dsx1IntervalNumber"),
)
if mibBuilder.loadTexts:
    dsx1XIntervalEntry.setStatus("deprecated")
_Dsx1IntervalLOS_Type = PerfIntervalCount
_Dsx1IntervalLOS_Object = MibTableColumn
dsx1IntervalLOS = _Dsx1IntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 1),
    _Dsx1IntervalLOS_Type()
)
dsx1IntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOS.setStatus("deprecated")
_Dsx1IntervalLOF_Type = PerfIntervalCount
_Dsx1IntervalLOF_Object = MibTableColumn
dsx1IntervalLOF = _Dsx1IntervalLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 2),
    _Dsx1IntervalLOF_Type()
)
dsx1IntervalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOF.setStatus("deprecated")
_Dsx1IntervalLOC_Type = PerfIntervalCount
_Dsx1IntervalLOC_Object = MibTableColumn
dsx1IntervalLOC = _Dsx1IntervalLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 3),
    _Dsx1IntervalLOC_Type()
)
dsx1IntervalLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOC.setStatus("current")
_Dsx1IntervalAIS_Type = PerfIntervalCount
_Dsx1IntervalAIS_Object = MibTableColumn
dsx1IntervalAIS = _Dsx1IntervalAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 4),
    _Dsx1IntervalAIS_Type()
)
dsx1IntervalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalAIS.setStatus("deprecated")
_Dsx1IntervalRAI_Type = PerfIntervalCount
_Dsx1IntervalRAI_Object = MibTableColumn
dsx1IntervalRAI = _Dsx1IntervalRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 5),
    _Dsx1IntervalRAI_Type()
)
dsx1IntervalRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalRAI.setStatus("deprecated")
_Dsx1IntervalLOMF_Type = PerfIntervalCount
_Dsx1IntervalLOMF_Object = MibTableColumn
dsx1IntervalLOMF = _Dsx1IntervalLOMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 6),
    _Dsx1IntervalLOMF_Type()
)
dsx1IntervalLOMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOMF.setStatus("current")
_Dsx1IntervalFEBE_Type = PerfIntervalCount
_Dsx1IntervalFEBE_Object = MibTableColumn
dsx1IntervalFEBE = _Dsx1IntervalFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 7),
    _Dsx1IntervalFEBE_Type()
)
dsx1IntervalFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalFEBE.setStatus("current")


class _Dsx1IntervalStatus_Type(OctetString):
    """Custom type dsx1IntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dsx1IntervalStatus_Type.__name__ = "OctetString"
_Dsx1IntervalStatus_Object = MibTableColumn
dsx1IntervalStatus = _Dsx1IntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 8),
    _Dsx1IntervalStatus_Type()
)
dsx1IntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalStatus.setStatus("current")
_Dsx1IntervalBPV_Type = PerfIntervalCount
_Dsx1IntervalBPV_Object = MibTableColumn
dsx1IntervalBPV = _Dsx1IntervalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 9),
    _Dsx1IntervalBPV_Type()
)
dsx1IntervalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalBPV.setStatus("current")
_Dsx1IntervalLOCRCMF_Type = PerfIntervalCount
_Dsx1IntervalLOCRCMF_Object = MibTableColumn
dsx1IntervalLOCRCMF = _Dsx1IntervalLOCRCMF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 10),
    _Dsx1IntervalLOCRCMF_Type()
)
dsx1IntervalLOCRCMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOCRCMF.setStatus("current")
_Dsx1IntervalLOFC_Type = PerfIntervalCount
_Dsx1IntervalLOFC_Object = MibTableColumn
dsx1IntervalLOFC = _Dsx1IntervalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 11),
    _Dsx1IntervalLOFC_Type()
)
dsx1IntervalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLOFC.setStatus("current")
_Dsx1IntervalLSES_Type = PerfIntervalCount
_Dsx1IntervalLSES_Object = MibTableColumn
dsx1IntervalLSES = _Dsx1IntervalLSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 13),
    _Dsx1IntervalLSES_Type()
)
dsx1IntervalLSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalLSES.setStatus("deprecated")
_Dsx1IntervalFC_Type = PerfIntervalCount
_Dsx1IntervalFC_Object = MibTableColumn
dsx1IntervalFC = _Dsx1IntervalFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 3, 1, 14),
    _Dsx1IntervalFC_Type()
)
dsx1IntervalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1IntervalFC.setStatus("deprecated")
_Dsx1XTotalTable_Object = MibTable
dsx1XTotalTable = _Dsx1XTotalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4)
)
if mibBuilder.loadTexts:
    dsx1XTotalTable.setStatus("current")
_Dsx1XTotalEntry_Object = MibTableRow
dsx1XTotalEntry = _Dsx1XTotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1)
)
dsx1XTotalEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1TotalIndex"),
)
if mibBuilder.loadTexts:
    dsx1XTotalEntry.setStatus("current")
_Dsx1TotalLOS_Type = PerfTotalCount
_Dsx1TotalLOS_Object = MibTableColumn
dsx1TotalLOS = _Dsx1TotalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 1),
    _Dsx1TotalLOS_Type()
)
dsx1TotalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLOS.setStatus("current")
_Dsx1TotalLOF_Type = PerfTotalCount
_Dsx1TotalLOF_Object = MibTableColumn
dsx1TotalLOF = _Dsx1TotalLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 2),
    _Dsx1TotalLOF_Type()
)
dsx1TotalLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLOF.setStatus("current")
_Dsx1TotalAIS_Type = PerfTotalCount
_Dsx1TotalAIS_Object = MibTableColumn
dsx1TotalAIS = _Dsx1TotalAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 4),
    _Dsx1TotalAIS_Type()
)
dsx1TotalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalAIS.setStatus("current")
_Dsx1TotalRAI_Type = PerfTotalCount
_Dsx1TotalRAI_Object = MibTableColumn
dsx1TotalRAI = _Dsx1TotalRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 5),
    _Dsx1TotalRAI_Type()
)
dsx1TotalRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalRAI.setStatus("current")
_Dsx1TotalBPV_Type = PerfTotalCount
_Dsx1TotalBPV_Object = MibTableColumn
dsx1TotalBPV = _Dsx1TotalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 9),
    _Dsx1TotalBPV_Type()
)
dsx1TotalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalBPV.setStatus("current")
_Dsx1TotalLOFC_Type = PerfTotalCount
_Dsx1TotalLOFC_Object = MibTableColumn
dsx1TotalLOFC = _Dsx1TotalLOFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 11),
    _Dsx1TotalLOFC_Type()
)
dsx1TotalLOFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLOFC.setStatus("current")
_Dsx1TotalLSES_Type = PerfTotalCount
_Dsx1TotalLSES_Object = MibTableColumn
dsx1TotalLSES = _Dsx1TotalLSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 13),
    _Dsx1TotalLSES_Type()
)
dsx1TotalLSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalLSES.setStatus("current")
_Dsx1TotalFC_Type = PerfTotalCount
_Dsx1TotalFC_Object = MibTableColumn
dsx1TotalFC = _Dsx1TotalFC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 4, 1, 14),
    _Dsx1TotalFC_Type()
)
dsx1TotalFC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1TotalFC.setStatus("current")
_Dsx1DataStreamStatTable_Object = MibTable
dsx1DataStreamStatTable = _Dsx1DataStreamStatTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5)
)
if mibBuilder.loadTexts:
    dsx1DataStreamStatTable.setStatus("current")
_Dsx1DataStreamStatEntry_Object = MibTableRow
dsx1DataStreamStatEntry = _Dsx1DataStreamStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1)
)
dsx1DataStreamStatEntry.setIndexNames(
    (0, "RAD-ds1Interface-MIB", "dsx1DataStreamStatIfIndex"),
    (0, "RAD-ds1Interface-MIB", "dsx1DataStreamStatIndex"),
)
if mibBuilder.loadTexts:
    dsx1DataStreamStatEntry.setStatus("current")
_Dsx1DataStreamStatIfIndex_Type = Integer32
_Dsx1DataStreamStatIfIndex_Object = MibTableColumn
dsx1DataStreamStatIfIndex = _Dsx1DataStreamStatIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 1),
    _Dsx1DataStreamStatIfIndex_Type()
)
dsx1DataStreamStatIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx1DataStreamStatIfIndex.setStatus("current")
_Dsx1DataStreamStatIndex_Type = Integer32
_Dsx1DataStreamStatIndex_Object = MibTableColumn
dsx1DataStreamStatIndex = _Dsx1DataStreamStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 2),
    _Dsx1DataStreamStatIndex_Type()
)
dsx1DataStreamStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx1DataStreamStatIndex.setStatus("current")
_Dsx1DataStreamStatValid_Type = TruthValue
_Dsx1DataStreamStatValid_Object = MibTableColumn
dsx1DataStreamStatValid = _Dsx1DataStreamStatValid_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 3),
    _Dsx1DataStreamStatValid_Type()
)
dsx1DataStreamStatValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatValid.setStatus("current")
_Dsx1DataStreamStatInFrames_Type = Counter32
_Dsx1DataStreamStatInFrames_Object = MibTableColumn
dsx1DataStreamStatInFrames = _Dsx1DataStreamStatInFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 4),
    _Dsx1DataStreamStatInFrames_Type()
)
dsx1DataStreamStatInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInFrames.setStatus("current")
_Dsx1DataStreamStatInBytes_Type = Counter32
_Dsx1DataStreamStatInBytes_Object = MibTableColumn
dsx1DataStreamStatInBytes = _Dsx1DataStreamStatInBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 5),
    _Dsx1DataStreamStatInBytes_Type()
)
dsx1DataStreamStatInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInBytes.setStatus("current")
_Dsx1DataStreamStatInDiscards_Type = Counter32
_Dsx1DataStreamStatInDiscards_Object = MibTableColumn
dsx1DataStreamStatInDiscards = _Dsx1DataStreamStatInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 6),
    _Dsx1DataStreamStatInDiscards_Type()
)
dsx1DataStreamStatInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInDiscards.setStatus("current")
_Dsx1DataStreamStatInErrors_Type = Counter32
_Dsx1DataStreamStatInErrors_Object = MibTableColumn
dsx1DataStreamStatInErrors = _Dsx1DataStreamStatInErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 7),
    _Dsx1DataStreamStatInErrors_Type()
)
dsx1DataStreamStatInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatInErrors.setStatus("current")
_Dsx1DataStreamStatOutFrames_Type = Counter32
_Dsx1DataStreamStatOutFrames_Object = MibTableColumn
dsx1DataStreamStatOutFrames = _Dsx1DataStreamStatOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 8),
    _Dsx1DataStreamStatOutFrames_Type()
)
dsx1DataStreamStatOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatOutFrames.setStatus("current")
_Dsx1DataStreamStatOutBytes_Type = Counter32
_Dsx1DataStreamStatOutBytes_Object = MibTableColumn
dsx1DataStreamStatOutBytes = _Dsx1DataStreamStatOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 9),
    _Dsx1DataStreamStatOutBytes_Type()
)
dsx1DataStreamStatOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatOutBytes.setStatus("current")
_Dsx1DataStreamStatOutDiscards_Type = Counter32
_Dsx1DataStreamStatOutDiscards_Object = MibTableColumn
dsx1DataStreamStatOutDiscards = _Dsx1DataStreamStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 10),
    _Dsx1DataStreamStatOutDiscards_Type()
)
dsx1DataStreamStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatOutDiscards.setStatus("current")
_Dsx1DataStreamStatOutErrors_Type = Counter32
_Dsx1DataStreamStatOutErrors_Object = MibTableColumn
dsx1DataStreamStatOutErrors = _Dsx1DataStreamStatOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 1, 5, 1, 11),
    _Dsx1DataStreamStatOutErrors_Type()
)
dsx1DataStreamStatOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1DataStreamStatOutErrors.setStatus("current")
_Dsx1XConfigTable_Object = MibTable
dsx1XConfigTable = _Dsx1XConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    dsx1XConfigTable.setStatus("current")
_Dsx1XConfigEntry_Object = MibTableRow
dsx1XConfigEntry = _Dsx1XConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1)
)
dsx1XConfigEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    dsx1XConfigEntry.setStatus("current")
_Dsx1IdleCode_Type = Integer32
_Dsx1IdleCode_Object = MibTableColumn
dsx1IdleCode = _Dsx1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 1),
    _Dsx1IdleCode_Type()
)
dsx1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1IdleCode.setStatus("current")


class _Dsx1LineMode_Type(Integer32):
    """Custom type dsx1LineMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("csu", 1),
          ("dsu", 2))
    )


_Dsx1LineMode_Type.__name__ = "Integer32"
_Dsx1LineMode_Object = MibTableColumn
dsx1LineMode = _Dsx1LineMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 2),
    _Dsx1LineMode_Type()
)
dsx1LineMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineMode.setStatus("current")


class _Dsx1dBTxGain_Type(Integer32):
    """Custom type dsx1dBTxGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("neg75dB", 2),
          ("neg15dB", 3),
          ("neg225dB", 4),
          ("zerodB", 5))
    )


_Dsx1dBTxGain_Type.__name__ = "Integer32"
_Dsx1dBTxGain_Object = MibTableColumn
dsx1dBTxGain = _Dsx1dBTxGain_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 3),
    _Dsx1dBTxGain_Type()
)
dsx1dBTxGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1dBTxGain.setStatus("current")


class _Dsx1RxSensitivity_Type(Integer32):
    """Custom type dsx1RxSensitivity based on Integer32"""
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
        *(("notApplicable", 1),
          ("longHaul", 2),
          ("shortHaul", 3),
          ("monitor", 4))
    )


_Dsx1RxSensitivity_Type.__name__ = "Integer32"
_Dsx1RxSensitivity_Object = MibTableColumn
dsx1RxSensitivity = _Dsx1RxSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 4),
    _Dsx1RxSensitivity_Type()
)
dsx1RxSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1RxSensitivity.setStatus("current")


class _Dsx1RestoreTime_Type(Integer32):
    """Custom type dsx1RestoreTime based on Integer32"""
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
        *(("other", 1),
          ("sec1", 2),
          ("sec10", 3),
          ("immediate", 4))
    )


_Dsx1RestoreTime_Type.__name__ = "Integer32"
_Dsx1RestoreTime_Object = MibTableColumn
dsx1RestoreTime = _Dsx1RestoreTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 5),
    _Dsx1RestoreTime_Type()
)
dsx1RestoreTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1RestoreTime.setStatus("current")
_Dsx1TcFirstSignal_Type = Integer32
_Dsx1TcFirstSignal_Object = MibTableColumn
dsx1TcFirstSignal = _Dsx1TcFirstSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 6),
    _Dsx1TcFirstSignal_Type()
)
dsx1TcFirstSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcFirstSignal.setStatus("current")
_Dsx1TcSignal_Type = Integer32
_Dsx1TcSignal_Object = MibTableColumn
dsx1TcSignal = _Dsx1TcSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 7),
    _Dsx1TcSignal_Type()
)
dsx1TcSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcSignal.setStatus("current")
_Dsx1TcPattern_Type = Integer32
_Dsx1TcPattern_Object = MibTableColumn
dsx1TcPattern = _Dsx1TcPattern_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 8),
    _Dsx1TcPattern_Type()
)
dsx1TcPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TcPattern.setStatus("current")


class _Dsx1Scramble_Type(Integer32):
    """Custom type dsx1Scramble based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("notActive", 2),
          ("active", 3))
    )


_Dsx1Scramble_Type.__name__ = "Integer32"
_Dsx1Scramble_Object = MibTableColumn
dsx1Scramble = _Dsx1Scramble_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 9),
    _Dsx1Scramble_Type()
)
dsx1Scramble.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1Scramble.setStatus("current")


class _Dsx1LineAdaptiveTimingMode_Type(Integer32):
    """Custom type dsx1LineAdaptiveTimingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_Dsx1LineAdaptiveTimingMode_Type.__name__ = "Integer32"
_Dsx1LineAdaptiveTimingMode_Object = MibTableColumn
dsx1LineAdaptiveTimingMode = _Dsx1LineAdaptiveTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 10),
    _Dsx1LineAdaptiveTimingMode_Type()
)
dsx1LineAdaptiveTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineAdaptiveTimingMode.setStatus("current")


class _Dsx1TxClockSource_Type(Integer32):
    """Custom type dsx1TxClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("loopTiming", 1),
          ("localTiming", 2),
          ("throughTiming", 3),
          ("adaptive", 4),
          ("system", 5))
    )


_Dsx1TxClockSource_Type.__name__ = "Integer32"
_Dsx1TxClockSource_Object = MibTableColumn
dsx1TxClockSource = _Dsx1TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 11),
    _Dsx1TxClockSource_Type()
)
dsx1TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TxClockSource.setStatus("current")


class _Dsx1AisEnable_Type(Integer32):
    """Custom type dsx1AisEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Dsx1AisEnable_Type.__name__ = "Integer32"
_Dsx1AisEnable_Object = MibTableColumn
dsx1AisEnable = _Dsx1AisEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 12),
    _Dsx1AisEnable_Type()
)
dsx1AisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1AisEnable.setStatus("current")


class _Dsx1TsEchoCancel_Type(OctetString):
    """Custom type dsx1TsEchoCancel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_Dsx1TsEchoCancel_Type.__name__ = "OctetString"
_Dsx1TsEchoCancel_Object = MibTableColumn
dsx1TsEchoCancel = _Dsx1TsEchoCancel_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 13),
    _Dsx1TsEchoCancel_Type()
)
dsx1TsEchoCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TsEchoCancel.setStatus("current")


class _Dsx1EchoCancelerModule_Type(Integer32):
    """Custom type dsx1EchoCancelerModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notExist", 2),
          ("exist", 3))
    )


_Dsx1EchoCancelerModule_Type.__name__ = "Integer32"
_Dsx1EchoCancelerModule_Object = MibTableColumn
dsx1EchoCancelerModule = _Dsx1EchoCancelerModule_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 14),
    _Dsx1EchoCancelerModule_Type()
)
dsx1EchoCancelerModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1EchoCancelerModule.setStatus("current")


class _Dsx1PortFunction_Type(Integer32):
    """Custom type dsx1PortFunction based on Integer32"""
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
        *(("notApplicable", 1),
          ("uni", 2),
          ("ces", 3),
          ("ima", 4),
          ("cesPsn", 5),
          ("abis", 6))
    )


_Dsx1PortFunction_Type.__name__ = "Integer32"
_Dsx1PortFunction_Object = MibTableColumn
dsx1PortFunction = _Dsx1PortFunction_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 15),
    _Dsx1PortFunction_Type()
)
dsx1PortFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PortFunction.setStatus("current")


class _Dsx1PortMultiplier_Type(Integer32):
    """Custom type dsx1PortMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("r56", 2),
          ("r64", 3))
    )


_Dsx1PortMultiplier_Type.__name__ = "Integer32"
_Dsx1PortMultiplier_Object = MibTableColumn
dsx1PortMultiplier = _Dsx1PortMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 16),
    _Dsx1PortMultiplier_Type()
)
dsx1PortMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PortMultiplier.setStatus("current")


class _Dsx1LeasedLine_Type(Integer32):
    """Custom type dsx1LeasedLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_Dsx1LeasedLine_Type.__name__ = "Integer32"
_Dsx1LeasedLine_Object = MibTableColumn
dsx1LeasedLine = _Dsx1LeasedLine_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 17),
    _Dsx1LeasedLine_Type()
)
dsx1LeasedLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LeasedLine.setStatus("current")


class _Dsx1CsuLoop_Type(Integer32):
    """Custom type dsx1CsuLoop based on Integer32"""
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
        *(("notApplicable", 1),
          ("local", 2),
          ("transparent", 3),
          ("remote", 4))
    )


_Dsx1CsuLoop_Type.__name__ = "Integer32"
_Dsx1CsuLoop_Object = MibTableColumn
dsx1CsuLoop = _Dsx1CsuLoop_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 18),
    _Dsx1CsuLoop_Type()
)
dsx1CsuLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1CsuLoop.setStatus("current")
_Dsx1ClockSource_Type = Integer32
_Dsx1ClockSource_Object = MibTableColumn
dsx1ClockSource = _Dsx1ClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 19),
    _Dsx1ClockSource_Type()
)
dsx1ClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1ClockSource.setStatus("current")


class _Dsx1OosSignal_Type(Integer32):
    """Custom type dsx1OosSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("space", 2),
          ("mark", 3),
          ("spaceMark", 4),
          ("markSpace", 5))
    )


_Dsx1OosSignal_Type.__name__ = "Integer32"
_Dsx1OosSignal_Object = MibTableColumn
dsx1OosSignal = _Dsx1OosSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 20),
    _Dsx1OosSignal_Type()
)
dsx1OosSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1OosSignal.setStatus("current")
_Dsx1BundleNextIndex_Type = Integer32
_Dsx1BundleNextIndex_Object = MibTableColumn
dsx1BundleNextIndex = _Dsx1BundleNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 21),
    _Dsx1BundleNextIndex_Type()
)
dsx1BundleNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsx1BundleNextIndex.setStatus("current")


class _Dsx1CRC6CalcMode_Type(Integer32):
    """Custom type dsx1CRC6CalcMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("jtG704", 1),
          ("ituG704", 2))
    )


_Dsx1CRC6CalcMode_Type.__name__ = "Integer32"
_Dsx1CRC6CalcMode_Object = MibTableColumn
dsx1CRC6CalcMode = _Dsx1CRC6CalcMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 22),
    _Dsx1CRC6CalcMode_Type()
)
dsx1CRC6CalcMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1CRC6CalcMode.setStatus("current")


class _Dsx1SendUponFail_Type(Integer32):
    """Custom type dsx1SendUponFail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oosCode", 2),
          ("ais", 3))
    )


_Dsx1SendUponFail_Type.__name__ = "Integer32"
_Dsx1SendUponFail_Object = MibTableColumn
dsx1SendUponFail = _Dsx1SendUponFail_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 23),
    _Dsx1SendUponFail_Type()
)
dsx1SendUponFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1SendUponFail.setStatus("current")


class _Dsx1InbandLoopSignal_Type(Integer32):
    """Custom type dsx1InbandLoopSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              99)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("csu", 2),
          ("fdlLine", 3),
          ("fdlNetwork", 4),
          ("niuFac1", 5),
          ("niuFac2", 6),
          ("program", 99))
    )


_Dsx1InbandLoopSignal_Type.__name__ = "Integer32"
_Dsx1InbandLoopSignal_Object = MibTableColumn
dsx1InbandLoopSignal = _Dsx1InbandLoopSignal_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 24),
    _Dsx1InbandLoopSignal_Type()
)
dsx1InbandLoopSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1InbandLoopSignal.setStatus("current")
_Dsx1InbandLoopUpCode_Type = OctetString
_Dsx1InbandLoopUpCode_Object = MibTableColumn
dsx1InbandLoopUpCode = _Dsx1InbandLoopUpCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 25),
    _Dsx1InbandLoopUpCode_Type()
)
dsx1InbandLoopUpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1InbandLoopUpCode.setStatus("current")


class _Dsx1InbandLoopUpLength_Type(Unsigned32):
    """Custom type dsx1InbandLoopUpLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_Dsx1InbandLoopUpLength_Type.__name__ = "Unsigned32"
_Dsx1InbandLoopUpLength_Object = MibTableColumn
dsx1InbandLoopUpLength = _Dsx1InbandLoopUpLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 26),
    _Dsx1InbandLoopUpLength_Type()
)
dsx1InbandLoopUpLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1InbandLoopUpLength.setStatus("current")
if mibBuilder.loadTexts:
    dsx1InbandLoopUpLength.setUnits("bits")
_Dsx1InbandLoopDownCode_Type = OctetString
_Dsx1InbandLoopDownCode_Object = MibTableColumn
dsx1InbandLoopDownCode = _Dsx1InbandLoopDownCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 27),
    _Dsx1InbandLoopDownCode_Type()
)
dsx1InbandLoopDownCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1InbandLoopDownCode.setStatus("current")


class _Dsx1InbandLoopDownLength_Type(Unsigned32):
    """Custom type dsx1InbandLoopDownLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 8),
    )


_Dsx1InbandLoopDownLength_Type.__name__ = "Unsigned32"
_Dsx1InbandLoopDownLength_Object = MibTableColumn
dsx1InbandLoopDownLength = _Dsx1InbandLoopDownLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 28),
    _Dsx1InbandLoopDownLength_Type()
)
dsx1InbandLoopDownLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1InbandLoopDownLength.setStatus("current")
if mibBuilder.loadTexts:
    dsx1InbandLoopDownLength.setUnits("bits")
_Dsx1TxClockInstance_Type = Unsigned32
_Dsx1TxClockInstance_Object = MibTableColumn
dsx1TxClockInstance = _Dsx1TxClockInstance_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 29),
    _Dsx1TxClockInstance_Type()
)
dsx1TxClockInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TxClockInstance.setStatus("current")


class _Dsx1TxPortQuality_Type(Integer32):
    """Custom type dsx1TxPortQuality based on Integer32"""
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
        *(("notApplicable", 1),
          ("stratum1", 2),
          ("stratum2", 3),
          ("stratum3", 4),
          ("stratum3e", 5),
          ("stratum4", 6))
    )


_Dsx1TxPortQuality_Type.__name__ = "Integer32"
_Dsx1TxPortQuality_Object = MibTableColumn
dsx1TxPortQuality = _Dsx1TxPortQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 2, 1, 30),
    _Dsx1TxPortQuality_Type()
)
dsx1TxPortQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1TxPortQuality.setStatus("current")
_Dsx1XStatThresholdTable_Object = MibTable
dsx1XStatThresholdTable = _Dsx1XStatThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3)
)
if mibBuilder.loadTexts:
    dsx1XStatThresholdTable.setStatus("current")
_Dsx1XStatThresholdEntry_Object = MibTableRow
dsx1XStatThresholdEntry = _Dsx1XStatThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1)
)
dsx1XStatThresholdEntry.setIndexNames(
    (0, "DS1-MIB", "dsx1LineIndex"),
)
if mibBuilder.loadTexts:
    dsx1XStatThresholdEntry.setStatus("current")


class _Dsx1LineIntervalLesThreshold_Type(Unsigned32):
    """Custom type dsx1LineIntervalLesThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1LineIntervalLesThreshold_Type.__name__ = "Unsigned32"
_Dsx1LineIntervalLesThreshold_Object = MibTableColumn
dsx1LineIntervalLesThreshold = _Dsx1LineIntervalLesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1, 1),
    _Dsx1LineIntervalLesThreshold_Type()
)
dsx1LineIntervalLesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1LineIntervalLesThreshold.setStatus("current")


class _Dsx1PathIntervalCvThreshold_Type(Unsigned32):
    """Custom type dsx1PathIntervalCvThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_Dsx1PathIntervalCvThreshold_Type.__name__ = "Unsigned32"
_Dsx1PathIntervalCvThreshold_Object = MibTableColumn
dsx1PathIntervalCvThreshold = _Dsx1PathIntervalCvThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1, 2),
    _Dsx1PathIntervalCvThreshold_Type()
)
dsx1PathIntervalCvThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PathIntervalCvThreshold.setStatus("current")


class _Dsx1PathIntervalEsThreshold_Type(Unsigned32):
    """Custom type dsx1PathIntervalEsThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1PathIntervalEsThreshold_Type.__name__ = "Unsigned32"
_Dsx1PathIntervalEsThreshold_Object = MibTableColumn
dsx1PathIntervalEsThreshold = _Dsx1PathIntervalEsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1, 3),
    _Dsx1PathIntervalEsThreshold_Type()
)
dsx1PathIntervalEsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PathIntervalEsThreshold.setStatus("current")


class _Dsx1PathIntervalSesThreshold_Type(Unsigned32):
    """Custom type dsx1PathIntervalSesThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1PathIntervalSesThreshold_Type.__name__ = "Unsigned32"
_Dsx1PathIntervalSesThreshold_Object = MibTableColumn
dsx1PathIntervalSesThreshold = _Dsx1PathIntervalSesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1, 4),
    _Dsx1PathIntervalSesThreshold_Type()
)
dsx1PathIntervalSesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PathIntervalSesThreshold.setStatus("current")


class _Dsx1PathIntervalSefsThreshold_Type(Unsigned32):
    """Custom type dsx1PathIntervalSefsThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1PathIntervalSefsThreshold_Type.__name__ = "Unsigned32"
_Dsx1PathIntervalSefsThreshold_Object = MibTableColumn
dsx1PathIntervalSefsThreshold = _Dsx1PathIntervalSefsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1, 5),
    _Dsx1PathIntervalSefsThreshold_Type()
)
dsx1PathIntervalSefsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PathIntervalSefsThreshold.setStatus("current")


class _Dsx1PathIntervalCssThreshold_Type(Unsigned32):
    """Custom type dsx1PathIntervalCssThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1PathIntervalCssThreshold_Type.__name__ = "Unsigned32"
_Dsx1PathIntervalCssThreshold_Object = MibTableColumn
dsx1PathIntervalCssThreshold = _Dsx1PathIntervalCssThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1, 6),
    _Dsx1PathIntervalCssThreshold_Type()
)
dsx1PathIntervalCssThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PathIntervalCssThreshold.setStatus("current")


class _Dsx1PathIntervalUasThreshold_Type(Unsigned32):
    """Custom type dsx1PathIntervalUasThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_Dsx1PathIntervalUasThreshold_Type.__name__ = "Unsigned32"
_Dsx1PathIntervalUasThreshold_Object = MibTableColumn
dsx1PathIntervalUasThreshold = _Dsx1PathIntervalUasThreshold_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 3, 1, 7),
    _Dsx1PathIntervalUasThreshold_Type()
)
dsx1PathIntervalUasThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx1PathIntervalUasThreshold.setStatus("current")

# Managed Objects groups


# Notification objects

ds1LocalMultiframeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 1)
)
ds1LocalMultiframeAlarmTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LocalMultiframeAlarmTrap.setStatus(
        "current"
    )

ds1RemoteMultiframeAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 2)
)
ds1RemoteMultiframeAlarmTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1RemoteMultiframeAlarmTrap.setStatus(
        "current"
    )

ds1LinkFrameSlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 3)
)
ds1LinkFrameSlipTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LinkFrameSlipTrap.setStatus(
        "current"
    )

ds1BpvErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 4)
)
ds1BpvErrorTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1BpvErrorTrap.setStatus(
        "current"
    )

ds1ExcessiveBpvTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 5)
)
ds1ExcessiveBpvTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveBpvTrap.setStatus(
        "current"
    )

ds1Crc4ErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 6)
)
ds1Crc4ErrorTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1Crc4ErrorTrap.setStatus(
        "current"
    )

ds1ExcessiveErrorRatioTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 7)
)
ds1ExcessiveErrorRatioTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveErrorRatioTrap.setStatus(
        "current"
    )

ds1RemoteSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 8)
)
ds1RemoteSyncLossTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1RemoteSyncLossTrap.setStatus(
        "current"
    )

ds1LocalSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 9)
)
ds1LocalSyncLossTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LocalSyncLossTrap.setStatus(
        "current"
    )

ds1AisSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 10)
)
ds1AisSyncLossTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1AisSyncLossTrap.setStatus(
        "current"
    )

ds1AisTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 11)
)
ds1AisTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1AisTrap.setStatus(
        "current"
    )

ds1NetworkRemoteLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 12)
)
ds1NetworkRemoteLoopTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1NetworkRemoteLoopTrap.setStatus(
        "current"
    )

ds1RemoteLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 13)
)
ds1RemoteLoopTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1RemoteLoopTrap.setStatus(
        "current"
    )

ds1LocalLoopTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 14)
)
ds1LocalLoopTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1LocalLoopTrap.setStatus(
        "current"
    )

ds1ExcessiveFrameSlipTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 15)
)
ds1ExcessiveFrameSlipTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveFrameSlipTrap.setStatus(
        "current"
    )

ds1ExcessiveCrc4ErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 16)
)
ds1ExcessiveCrc4ErrorTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveCrc4ErrorTrap.setStatus(
        "current"
    )

ds1ExcessiveLocalMfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 17)
)
ds1ExcessiveLocalMfAlarmTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveLocalMfAlarmTrap.setStatus(
        "current"
    )

ds1ExcessiveRemoteMfAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 18)
)
ds1ExcessiveRemoteMfAlarmTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveRemoteMfAlarmTrap.setStatus(
        "current"
    )

ds1ExcessiveRemoteSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 19)
)
ds1ExcessiveRemoteSyncLossTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveRemoteSyncLossTrap.setStatus(
        "current"
    )

ds1ExcessiveLocalSyncLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 20)
)
ds1ExcessiveLocalSyncLossTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1ExcessiveLocalSyncLossTrap.setStatus(
        "current"
    )

ds1SignalLossTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 21)
)
ds1SignalLossTrap.setObjects(
      *(("RAD-ds1Interface-MIB", "alarmSeverity"),
        ("RAD-ds1Interface-MIB", "alarmState"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    ds1SignalLossTrap.setStatus(
        "current"
    )

e1t1Ais = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 25)
)
e1t1Ais.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    e1t1Ais.setStatus(
        "current"
    )

e1t1Lof = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 26)
)
e1t1Lof.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    e1t1Lof.setStatus(
        "current"
    )

e1t1Rai = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 27)
)
e1t1Rai.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    e1t1Rai.setStatus(
        "current"
    )

e1t1Lomf = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 28)
)
e1t1Lomf.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    e1t1Lomf.setStatus(
        "current"
    )

e1t1Los = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 30)
)
e1t1Los.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LineStatus"))
)
if mibBuilder.loadTexts:
    e1t1Los.setStatus(
        "current"
    )

e1t1Loopback = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 36)
)
e1t1Loopback.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1LoopbackStatus"))
)
if mibBuilder.loadTexts:
    e1t1Loopback.setStatus(
        "current"
    )

e1t1LoopbackOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 37)
)
e1t1LoopbackOff.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"))
)
if mibBuilder.loadTexts:
    e1t1LoopbackOff.setStatus(
        "current"
    )

e1t1EsLineTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 38)
)
e1t1EsLineTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1IntervalLESs"),
        ("RAD-ds1Interface-MIB", "dsx1LineIntervalLesThreshold"))
)
if mibBuilder.loadTexts:
    e1t1EsLineTca.setStatus(
        "current"
    )

e1t1CvPathTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 39)
)
e1t1CvPathTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1IntervalPCVs"),
        ("RAD-ds1Interface-MIB", "dsx1PathIntervalCvThreshold"))
)
if mibBuilder.loadTexts:
    e1t1CvPathTca.setStatus(
        "current"
    )

e1t1EsPathTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 40)
)
e1t1EsPathTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1IntervalESs"),
        ("RAD-ds1Interface-MIB", "dsx1PathIntervalEsThreshold"))
)
if mibBuilder.loadTexts:
    e1t1EsPathTca.setStatus(
        "current"
    )

e1t1SesPathTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 41)
)
e1t1SesPathTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1IntervalSESs"),
        ("RAD-ds1Interface-MIB", "dsx1PathIntervalSesThreshold"))
)
if mibBuilder.loadTexts:
    e1t1SesPathTca.setStatus(
        "current"
    )

e1t1SefsPathTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 42)
)
e1t1SefsPathTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1IntervalSEFSs"),
        ("RAD-ds1Interface-MIB", "dsx1PathIntervalSefsThreshold"))
)
if mibBuilder.loadTexts:
    e1t1SefsPathTca.setStatus(
        "current"
    )

e1t1CssPathTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 43)
)
e1t1CssPathTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1IntervalCSSs"),
        ("RAD-ds1Interface-MIB", "dsx1PathIntervalCssThreshold"))
)
if mibBuilder.loadTexts:
    e1t1CssPathTca.setStatus(
        "current"
    )

e1t1UasPathTca = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 4, 0, 44)
)
e1t1UasPathTca.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS1-MIB", "dsx1IntervalUASs"),
        ("RAD-ds1Interface-MIB", "dsx1PathIntervalUasThreshold"))
)
if mibBuilder.loadTexts:
    e1t1UasPathTca.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-ds1Interface-MIB",
    **{"ds1Interface": ds1Interface,
       "prtDS1Events": prtDS1Events,
       "ds1LocalMultiframeAlarmTrap": ds1LocalMultiframeAlarmTrap,
       "ds1RemoteMultiframeAlarmTrap": ds1RemoteMultiframeAlarmTrap,
       "ds1LinkFrameSlipTrap": ds1LinkFrameSlipTrap,
       "ds1BpvErrorTrap": ds1BpvErrorTrap,
       "ds1ExcessiveBpvTrap": ds1ExcessiveBpvTrap,
       "ds1Crc4ErrorTrap": ds1Crc4ErrorTrap,
       "ds1ExcessiveErrorRatioTrap": ds1ExcessiveErrorRatioTrap,
       "ds1RemoteSyncLossTrap": ds1RemoteSyncLossTrap,
       "ds1LocalSyncLossTrap": ds1LocalSyncLossTrap,
       "ds1AisSyncLossTrap": ds1AisSyncLossTrap,
       "ds1AisTrap": ds1AisTrap,
       "ds1NetworkRemoteLoopTrap": ds1NetworkRemoteLoopTrap,
       "ds1RemoteLoopTrap": ds1RemoteLoopTrap,
       "ds1LocalLoopTrap": ds1LocalLoopTrap,
       "ds1ExcessiveFrameSlipTrap": ds1ExcessiveFrameSlipTrap,
       "ds1ExcessiveCrc4ErrorTrap": ds1ExcessiveCrc4ErrorTrap,
       "ds1ExcessiveLocalMfAlarmTrap": ds1ExcessiveLocalMfAlarmTrap,
       "ds1ExcessiveRemoteMfAlarmTrap": ds1ExcessiveRemoteMfAlarmTrap,
       "ds1ExcessiveRemoteSyncLossTrap": ds1ExcessiveRemoteSyncLossTrap,
       "ds1ExcessiveLocalSyncLossTrap": ds1ExcessiveLocalSyncLossTrap,
       "ds1SignalLossTrap": ds1SignalLossTrap,
       "e1t1Ais": e1t1Ais,
       "e1t1Lof": e1t1Lof,
       "e1t1Rai": e1t1Rai,
       "e1t1Lomf": e1t1Lomf,
       "e1t1Los": e1t1Los,
       "e1t1Loopback": e1t1Loopback,
       "e1t1LoopbackOff": e1t1LoopbackOff,
       "e1t1EsLineTca": e1t1EsLineTca,
       "e1t1CvPathTca": e1t1CvPathTca,
       "e1t1EsPathTca": e1t1EsPathTca,
       "e1t1SesPathTca": e1t1SesPathTca,
       "e1t1SefsPathTca": e1t1SefsPathTca,
       "e1t1CssPathTca": e1t1CssPathTca,
       "e1t1UasPathTca": e1t1UasPathTca,
       "prtDs1PerfHistory": prtDs1PerfHistory,
       "dsx1XCurrentTable": dsx1XCurrentTable,
       "dsx1XCurrentEntry": dsx1XCurrentEntry,
       "dsx1CurrentLOS": dsx1CurrentLOS,
       "dsx1CurrentLOF": dsx1CurrentLOF,
       "dsx1CurrentLOC": dsx1CurrentLOC,
       "dsx1CurrentAIS": dsx1CurrentAIS,
       "dsx1CurrentRAI": dsx1CurrentRAI,
       "dsx1CurrentLOMF": dsx1CurrentLOMF,
       "dsx1CurrentFEBE": dsx1CurrentFEBE,
       "dsx1CurrentStatus": dsx1CurrentStatus,
       "dsx1CurrentBPV": dsx1CurrentBPV,
       "dsx1CurrentLOCRCMF": dsx1CurrentLOCRCMF,
       "dsx1CurrentLOFC": dsx1CurrentLOFC,
       "dsx1CurrentCRCErrors": dsx1CurrentCRCErrors,
       "dsx1CurrentLSES": dsx1CurrentLSES,
       "dsx1CurrentFC": dsx1CurrentFC,
       "dsx1XIntervalTable": dsx1XIntervalTable,
       "dsx1XIntervalEntry": dsx1XIntervalEntry,
       "dsx1IntervalLOS": dsx1IntervalLOS,
       "dsx1IntervalLOF": dsx1IntervalLOF,
       "dsx1IntervalLOC": dsx1IntervalLOC,
       "dsx1IntervalAIS": dsx1IntervalAIS,
       "dsx1IntervalRAI": dsx1IntervalRAI,
       "dsx1IntervalLOMF": dsx1IntervalLOMF,
       "dsx1IntervalFEBE": dsx1IntervalFEBE,
       "dsx1IntervalStatus": dsx1IntervalStatus,
       "dsx1IntervalBPV": dsx1IntervalBPV,
       "dsx1IntervalLOCRCMF": dsx1IntervalLOCRCMF,
       "dsx1IntervalLOFC": dsx1IntervalLOFC,
       "dsx1IntervalLSES": dsx1IntervalLSES,
       "dsx1IntervalFC": dsx1IntervalFC,
       "dsx1XTotalTable": dsx1XTotalTable,
       "dsx1XTotalEntry": dsx1XTotalEntry,
       "dsx1TotalLOS": dsx1TotalLOS,
       "dsx1TotalLOF": dsx1TotalLOF,
       "dsx1TotalAIS": dsx1TotalAIS,
       "dsx1TotalRAI": dsx1TotalRAI,
       "dsx1TotalBPV": dsx1TotalBPV,
       "dsx1TotalLOFC": dsx1TotalLOFC,
       "dsx1TotalLSES": dsx1TotalLSES,
       "dsx1TotalFC": dsx1TotalFC,
       "dsx1DataStreamStatTable": dsx1DataStreamStatTable,
       "dsx1DataStreamStatEntry": dsx1DataStreamStatEntry,
       "dsx1DataStreamStatIfIndex": dsx1DataStreamStatIfIndex,
       "dsx1DataStreamStatIndex": dsx1DataStreamStatIndex,
       "dsx1DataStreamStatValid": dsx1DataStreamStatValid,
       "dsx1DataStreamStatInFrames": dsx1DataStreamStatInFrames,
       "dsx1DataStreamStatInBytes": dsx1DataStreamStatInBytes,
       "dsx1DataStreamStatInDiscards": dsx1DataStreamStatInDiscards,
       "dsx1DataStreamStatInErrors": dsx1DataStreamStatInErrors,
       "dsx1DataStreamStatOutFrames": dsx1DataStreamStatOutFrames,
       "dsx1DataStreamStatOutBytes": dsx1DataStreamStatOutBytes,
       "dsx1DataStreamStatOutDiscards": dsx1DataStreamStatOutDiscards,
       "dsx1DataStreamStatOutErrors": dsx1DataStreamStatOutErrors,
       "dsx1XConfigTable": dsx1XConfigTable,
       "dsx1XConfigEntry": dsx1XConfigEntry,
       "dsx1IdleCode": dsx1IdleCode,
       "dsx1LineMode": dsx1LineMode,
       "dsx1dBTxGain": dsx1dBTxGain,
       "dsx1RxSensitivity": dsx1RxSensitivity,
       "dsx1RestoreTime": dsx1RestoreTime,
       "dsx1TcFirstSignal": dsx1TcFirstSignal,
       "dsx1TcSignal": dsx1TcSignal,
       "dsx1TcPattern": dsx1TcPattern,
       "dsx1Scramble": dsx1Scramble,
       "dsx1LineAdaptiveTimingMode": dsx1LineAdaptiveTimingMode,
       "dsx1TxClockSource": dsx1TxClockSource,
       "dsx1AisEnable": dsx1AisEnable,
       "dsx1TsEchoCancel": dsx1TsEchoCancel,
       "dsx1EchoCancelerModule": dsx1EchoCancelerModule,
       "dsx1PortFunction": dsx1PortFunction,
       "dsx1PortMultiplier": dsx1PortMultiplier,
       "dsx1LeasedLine": dsx1LeasedLine,
       "dsx1CsuLoop": dsx1CsuLoop,
       "dsx1ClockSource": dsx1ClockSource,
       "dsx1OosSignal": dsx1OosSignal,
       "dsx1BundleNextIndex": dsx1BundleNextIndex,
       "dsx1CRC6CalcMode": dsx1CRC6CalcMode,
       "dsx1SendUponFail": dsx1SendUponFail,
       "dsx1InbandLoopSignal": dsx1InbandLoopSignal,
       "dsx1InbandLoopUpCode": dsx1InbandLoopUpCode,
       "dsx1InbandLoopUpLength": dsx1InbandLoopUpLength,
       "dsx1InbandLoopDownCode": dsx1InbandLoopDownCode,
       "dsx1InbandLoopDownLength": dsx1InbandLoopDownLength,
       "dsx1TxClockInstance": dsx1TxClockInstance,
       "dsx1TxPortQuality": dsx1TxPortQuality,
       "dsx1XStatThresholdTable": dsx1XStatThresholdTable,
       "dsx1XStatThresholdEntry": dsx1XStatThresholdEntry,
       "dsx1LineIntervalLesThreshold": dsx1LineIntervalLesThreshold,
       "dsx1PathIntervalCvThreshold": dsx1PathIntervalCvThreshold,
       "dsx1PathIntervalEsThreshold": dsx1PathIntervalEsThreshold,
       "dsx1PathIntervalSesThreshold": dsx1PathIntervalSesThreshold,
       "dsx1PathIntervalSefsThreshold": dsx1PathIntervalSefsThreshold,
       "dsx1PathIntervalCssThreshold": dsx1PathIntervalCssThreshold,
       "dsx1PathIntervalUasThreshold": dsx1PathIntervalUasThreshold}
)
