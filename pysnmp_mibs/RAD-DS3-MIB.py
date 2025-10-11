# SNMP MIB module (RAD-DS3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-DS3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:21 2025
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

(dsx3ConfigEntry,
 dsx3LineStatus,
 dsx3LoopbackConfig) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3ConfigEntry",
    "dsx3LineStatus",
    "dsx3LoopbackConfig")

(InterfaceIndex,
 ifAlias,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifAlias",
    "ifIndex")

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

ds3Interface = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PrtDS3Events_ObjectIdentity = ObjectIdentity
prtDS3Events = _PrtDS3Events_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 0)
)
_PrtDs3PerfHistory_ObjectIdentity = ObjectIdentity
prtDs3PerfHistory = _PrtDs3PerfHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1)
)
_PrtSDs3IfTable_Object = MibTable
prtSDs3IfTable = _PrtSDs3IfTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1)
)
if mibBuilder.loadTexts:
    prtSDs3IfTable.setStatus("current")
_PrtDs3IfEntry_Object = MibTableRow
prtDs3IfEntry = _PrtDs3IfEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1, 1)
)
prtDs3IfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtDs3IfEntry.setStatus("current")


class _PrtDs3IfTimeElapsed_Type(Integer32):
    """Custom type prtDs3IfTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_PrtDs3IfTimeElapsed_Type.__name__ = "Integer32"
_PrtDs3IfTimeElapsed_Object = MibTableColumn
prtDs3IfTimeElapsed = _PrtDs3IfTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1, 1, 1),
    _PrtDs3IfTimeElapsed_Type()
)
prtDs3IfTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IfTimeElapsed.setStatus("current")


class _PrtDs3IfValidIntervals_Type(Integer32):
    """Custom type prtDs3IfValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PrtDs3IfValidIntervals_Type.__name__ = "Integer32"
_PrtDs3IfValidIntervals_Object = MibTableColumn
prtDs3IfValidIntervals = _PrtDs3IfValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 1, 1, 2),
    _PrtDs3IfValidIntervals_Type()
)
prtDs3IfValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IfValidIntervals.setStatus("current")
_PrtDs3CurrentTable_Object = MibTable
prtDs3CurrentTable = _PrtDs3CurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2)
)
if mibBuilder.loadTexts:
    prtDs3CurrentTable.setStatus("current")
_PrtDs3CurrentEntry_Object = MibTableRow
prtDs3CurrentEntry = _PrtDs3CurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1)
)
prtDs3CurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtDs3CurrentEntry.setStatus("current")
_PrtDs3CurrentLOS_Type = Gauge32
_PrtDs3CurrentLOS_Object = MibTableColumn
prtDs3CurrentLOS = _PrtDs3CurrentLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 1),
    _PrtDs3CurrentLOS_Type()
)
prtDs3CurrentLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentLOS.setStatus("current")
_PrtDs3CurrentOOF_Type = Gauge32
_PrtDs3CurrentOOF_Object = MibTableColumn
prtDs3CurrentOOF = _PrtDs3CurrentOOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 2),
    _PrtDs3CurrentOOF_Type()
)
prtDs3CurrentOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentOOF.setStatus("current")
_PrtDs3CurrentLOC_Type = Gauge32
_PrtDs3CurrentLOC_Object = MibTableColumn
prtDs3CurrentLOC = _PrtDs3CurrentLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 3),
    _PrtDs3CurrentLOC_Type()
)
prtDs3CurrentLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentLOC.setStatus("current")
_PrtDs3CurrentAIS_Type = Gauge32
_PrtDs3CurrentAIS_Object = MibTableColumn
prtDs3CurrentAIS = _PrtDs3CurrentAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 4),
    _PrtDs3CurrentAIS_Type()
)
prtDs3CurrentAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentAIS.setStatus("current")
_PrtDs3CurrentRDI_Type = Gauge32
_PrtDs3CurrentRDI_Object = MibTableColumn
prtDs3CurrentRDI = _PrtDs3CurrentRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 5),
    _PrtDs3CurrentRDI_Type()
)
prtDs3CurrentRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentRDI.setStatus("current")
_PrtDs3CurrentUAS_Type = Gauge32
_PrtDs3CurrentUAS_Object = MibTableColumn
prtDs3CurrentUAS = _PrtDs3CurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 6),
    _PrtDs3CurrentUAS_Type()
)
prtDs3CurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentUAS.setStatus("current")
_PrtDs3CurrentBIP_Type = Gauge32
_PrtDs3CurrentBIP_Object = MibTableColumn
prtDs3CurrentBIP = _PrtDs3CurrentBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 7),
    _PrtDs3CurrentBIP_Type()
)
prtDs3CurrentBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentBIP.setStatus("current")
_PrtDs3CurrentFEBE_Type = Gauge32
_PrtDs3CurrentFEBE_Object = MibTableColumn
prtDs3CurrentFEBE = _PrtDs3CurrentFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 8),
    _PrtDs3CurrentFEBE_Type()
)
prtDs3CurrentFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentFEBE.setStatus("current")
_PrtDs3CurrentSLM_Type = Gauge32
_PrtDs3CurrentSLM_Object = MibTableColumn
prtDs3CurrentSLM = _PrtDs3CurrentSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 9),
    _PrtDs3CurrentSLM_Type()
)
prtDs3CurrentSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentSLM.setStatus("current")
_PrtDs3CurrentSES_Type = Gauge32
_PrtDs3CurrentSES_Object = MibTableColumn
prtDs3CurrentSES = _PrtDs3CurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 10),
    _PrtDs3CurrentSES_Type()
)
prtDs3CurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentSES.setStatus("current")
_PrtDs3CurrentES_Type = Gauge32
_PrtDs3CurrentES_Object = MibTableColumn
prtDs3CurrentES = _PrtDs3CurrentES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 11),
    _PrtDs3CurrentES_Type()
)
prtDs3CurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentES.setStatus("current")
_PrtDs3CurrentBitParity_Type = Gauge32
_PrtDs3CurrentBitParity_Object = MibTableColumn
prtDs3CurrentBitParity = _PrtDs3CurrentBitParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 12),
    _PrtDs3CurrentBitParity_Type()
)
prtDs3CurrentBitParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentBitParity.setStatus("current")
_PrtDs3CurrentPlcpLOF_Type = Gauge32
_PrtDs3CurrentPlcpLOF_Object = MibTableColumn
prtDs3CurrentPlcpLOF = _PrtDs3CurrentPlcpLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 13),
    _PrtDs3CurrentPlcpLOF_Type()
)
prtDs3CurrentPlcpLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpLOF.setStatus("current")
_PrtDs3CurrentPlcpRAI_Type = Gauge32
_PrtDs3CurrentPlcpRAI_Object = MibTableColumn
prtDs3CurrentPlcpRAI = _PrtDs3CurrentPlcpRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 14),
    _PrtDs3CurrentPlcpRAI_Type()
)
prtDs3CurrentPlcpRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpRAI.setStatus("current")
_PrtDs3CurrentPlcpBIP_Type = Gauge32
_PrtDs3CurrentPlcpBIP_Object = MibTableColumn
prtDs3CurrentPlcpBIP = _PrtDs3CurrentPlcpBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 15),
    _PrtDs3CurrentPlcpBIP_Type()
)
prtDs3CurrentPlcpBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpBIP.setStatus("current")
_PrtDs3CurrentPlcpFEBE_Type = Gauge32
_PrtDs3CurrentPlcpFEBE_Object = MibTableColumn
prtDs3CurrentPlcpFEBE = _PrtDs3CurrentPlcpFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 16),
    _PrtDs3CurrentPlcpFEBE_Type()
)
prtDs3CurrentPlcpFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentPlcpFEBE.setStatus("current")
_PrtDs3CurrentBPV_Type = Gauge32
_PrtDs3CurrentBPV_Object = MibTableColumn
prtDs3CurrentBPV = _PrtDs3CurrentBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 17),
    _PrtDs3CurrentBPV_Type()
)
prtDs3CurrentBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentBPV.setStatus("current")
_PrtDs3CurrentLCE_Type = Gauge32
_PrtDs3CurrentLCE_Object = MibTableColumn
prtDs3CurrentLCE = _PrtDs3CurrentLCE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 18),
    _PrtDs3CurrentLCE_Type()
)
prtDs3CurrentLCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentLCE.setStatus("current")


class _PrtDs3CurrentStatus_Type(OctetString):
    """Custom type prtDs3CurrentStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtDs3CurrentStatus_Type.__name__ = "OctetString"
_PrtDs3CurrentStatus_Object = MibTableColumn
prtDs3CurrentStatus = _PrtDs3CurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 2, 1, 19),
    _PrtDs3CurrentStatus_Type()
)
prtDs3CurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3CurrentStatus.setStatus("current")
_PrtDs3IntervalTable_Object = MibTable
prtDs3IntervalTable = _PrtDs3IntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3)
)
if mibBuilder.loadTexts:
    prtDs3IntervalTable.setStatus("current")
_PrtDs3IntervalEntry_Object = MibTableRow
prtDs3IntervalEntry = _PrtDs3IntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1)
)
prtDs3IntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAD-DS3-MIB", "prtDs3IntervalNumber"),
)
if mibBuilder.loadTexts:
    prtDs3IntervalEntry.setStatus("current")


class _PrtDs3IntervalNumber_Type(Integer32):
    """Custom type prtDs3IntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_PrtDs3IntervalNumber_Type.__name__ = "Integer32"
_PrtDs3IntervalNumber_Object = MibTableColumn
prtDs3IntervalNumber = _PrtDs3IntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 1),
    _PrtDs3IntervalNumber_Type()
)
prtDs3IntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalNumber.setStatus("current")
_PrtDs3IntervalLOS_Type = Gauge32
_PrtDs3IntervalLOS_Object = MibTableColumn
prtDs3IntervalLOS = _PrtDs3IntervalLOS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 2),
    _PrtDs3IntervalLOS_Type()
)
prtDs3IntervalLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalLOS.setStatus("current")
_PrtDs3IntervalOOF_Type = Gauge32
_PrtDs3IntervalOOF_Object = MibTableColumn
prtDs3IntervalOOF = _PrtDs3IntervalOOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 3),
    _PrtDs3IntervalOOF_Type()
)
prtDs3IntervalOOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalOOF.setStatus("current")
_PrtDs3IntervalLOC_Type = Gauge32
_PrtDs3IntervalLOC_Object = MibTableColumn
prtDs3IntervalLOC = _PrtDs3IntervalLOC_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 4),
    _PrtDs3IntervalLOC_Type()
)
prtDs3IntervalLOC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalLOC.setStatus("current")
_PrtDs3IntervalAIS_Type = Gauge32
_PrtDs3IntervalAIS_Object = MibTableColumn
prtDs3IntervalAIS = _PrtDs3IntervalAIS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 5),
    _PrtDs3IntervalAIS_Type()
)
prtDs3IntervalAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalAIS.setStatus("current")
_PrtDs3IntervalRDI_Type = Gauge32
_PrtDs3IntervalRDI_Object = MibTableColumn
prtDs3IntervalRDI = _PrtDs3IntervalRDI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 6),
    _PrtDs3IntervalRDI_Type()
)
prtDs3IntervalRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalRDI.setStatus("current")
_PrtDs3IntervalUAS_Type = Gauge32
_PrtDs3IntervalUAS_Object = MibTableColumn
prtDs3IntervalUAS = _PrtDs3IntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 7),
    _PrtDs3IntervalUAS_Type()
)
prtDs3IntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalUAS.setStatus("current")
_PrtDs3IntervalBIP_Type = Gauge32
_PrtDs3IntervalBIP_Object = MibTableColumn
prtDs3IntervalBIP = _PrtDs3IntervalBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 8),
    _PrtDs3IntervalBIP_Type()
)
prtDs3IntervalBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalBIP.setStatus("current")
_PrtDs3IntervalFEBE_Type = Gauge32
_PrtDs3IntervalFEBE_Object = MibTableColumn
prtDs3IntervalFEBE = _PrtDs3IntervalFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 9),
    _PrtDs3IntervalFEBE_Type()
)
prtDs3IntervalFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalFEBE.setStatus("current")
_PrtDs3IntervalSLM_Type = Gauge32
_PrtDs3IntervalSLM_Object = MibTableColumn
prtDs3IntervalSLM = _PrtDs3IntervalSLM_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 10),
    _PrtDs3IntervalSLM_Type()
)
prtDs3IntervalSLM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalSLM.setStatus("current")
_PrtDs3IntervalSES_Type = Gauge32
_PrtDs3IntervalSES_Object = MibTableColumn
prtDs3IntervalSES = _PrtDs3IntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 11),
    _PrtDs3IntervalSES_Type()
)
prtDs3IntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalSES.setStatus("current")
_PrtDs3IntervalES_Type = Gauge32
_PrtDs3IntervalES_Object = MibTableColumn
prtDs3IntervalES = _PrtDs3IntervalES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 12),
    _PrtDs3IntervalES_Type()
)
prtDs3IntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalES.setStatus("current")
_PrtDs3IntervalBitParity_Type = Gauge32
_PrtDs3IntervalBitParity_Object = MibTableColumn
prtDs3IntervalBitParity = _PrtDs3IntervalBitParity_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 13),
    _PrtDs3IntervalBitParity_Type()
)
prtDs3IntervalBitParity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalBitParity.setStatus("current")
_PrtDs3IntervalPlcpLOF_Type = Gauge32
_PrtDs3IntervalPlcpLOF_Object = MibTableColumn
prtDs3IntervalPlcpLOF = _PrtDs3IntervalPlcpLOF_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 14),
    _PrtDs3IntervalPlcpLOF_Type()
)
prtDs3IntervalPlcpLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpLOF.setStatus("current")
_PrtDs3IntervalPlcpRAI_Type = Gauge32
_PrtDs3IntervalPlcpRAI_Object = MibTableColumn
prtDs3IntervalPlcpRAI = _PrtDs3IntervalPlcpRAI_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 15),
    _PrtDs3IntervalPlcpRAI_Type()
)
prtDs3IntervalPlcpRAI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpRAI.setStatus("current")
_PrtDs3IntervalPlcpBIP_Type = Gauge32
_PrtDs3IntervalPlcpBIP_Object = MibTableColumn
prtDs3IntervalPlcpBIP = _PrtDs3IntervalPlcpBIP_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 16),
    _PrtDs3IntervalPlcpBIP_Type()
)
prtDs3IntervalPlcpBIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpBIP.setStatus("current")
_PrtDs3IntervalPlcpFEBE_Type = Gauge32
_PrtDs3IntervalPlcpFEBE_Object = MibTableColumn
prtDs3IntervalPlcpFEBE = _PrtDs3IntervalPlcpFEBE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 17),
    _PrtDs3IntervalPlcpFEBE_Type()
)
prtDs3IntervalPlcpFEBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalPlcpFEBE.setStatus("current")
_PrtDs3IntervalBPV_Type = Gauge32
_PrtDs3IntervalBPV_Object = MibTableColumn
prtDs3IntervalBPV = _PrtDs3IntervalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 18),
    _PrtDs3IntervalBPV_Type()
)
prtDs3IntervalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalBPV.setStatus("current")
_PrtDs3IntervalLCE_Type = Gauge32
_PrtDs3IntervalLCE_Object = MibTableColumn
prtDs3IntervalLCE = _PrtDs3IntervalLCE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 19),
    _PrtDs3IntervalLCE_Type()
)
prtDs3IntervalLCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalLCE.setStatus("current")


class _PrtDs3IntervalStatus_Type(OctetString):
    """Custom type prtDs3IntervalStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_PrtDs3IntervalStatus_Type.__name__ = "OctetString"
_PrtDs3IntervalStatus_Object = MibTableColumn
prtDs3IntervalStatus = _PrtDs3IntervalStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 3, 1, 20),
    _PrtDs3IntervalStatus_Type()
)
prtDs3IntervalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3IntervalStatus.setStatus("current")
_PrtDs3TotalTable_Object = MibTable
prtDs3TotalTable = _PrtDs3TotalTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4)
)
if mibBuilder.loadTexts:
    prtDs3TotalTable.setStatus("current")
_PrtDs3TotalEntry_Object = MibTableRow
prtDs3TotalEntry = _PrtDs3TotalEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1)
)
prtDs3TotalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    prtDs3TotalEntry.setStatus("current")
_PrtDs3TotalUAS_Type = Gauge32
_PrtDs3TotalUAS_Object = MibTableColumn
prtDs3TotalUAS = _PrtDs3TotalUAS_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1, 6),
    _PrtDs3TotalUAS_Type()
)
prtDs3TotalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3TotalUAS.setStatus("current")
_PrtDs3TotalBPV_Type = Gauge32
_PrtDs3TotalBPV_Object = MibTableColumn
prtDs3TotalBPV = _PrtDs3TotalBPV_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1, 17),
    _PrtDs3TotalBPV_Type()
)
prtDs3TotalBPV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3TotalBPV.setStatus("current")
_PrtDs3TotalLCE_Type = Gauge32
_PrtDs3TotalLCE_Object = MibTableColumn
prtDs3TotalLCE = _PrtDs3TotalLCE_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1, 18),
    _PrtDs3TotalLCE_Type()
)
prtDs3TotalLCE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3TotalLCE.setStatus("current")
_PrtDs3TotalSES_Type = Gauge32
_PrtDs3TotalSES_Object = MibTableColumn
prtDs3TotalSES = _PrtDs3TotalSES_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 1, 4, 1, 19),
    _PrtDs3TotalSES_Type()
)
prtDs3TotalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prtDs3TotalSES.setStatus("current")
_Dsx3XConfigTable_Object = MibTable
dsx3XConfigTable = _Dsx3XConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    dsx3XConfigTable.setStatus("current")
_Dsx3XConfigEntry_Object = MibTableRow
dsx3XConfigEntry = _Dsx3XConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 2, 1)
)
if mibBuilder.loadTexts:
    dsx3XConfigEntry.setStatus("current")


class _Dsx3AisEnable_Type(Integer32):
    """Custom type dsx3AisEnable based on Integer32"""
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


_Dsx3AisEnable_Type.__name__ = "Integer32"
_Dsx3AisEnable_Object = MibTableColumn
dsx3AisEnable = _Dsx3AisEnable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 2, 1, 1),
    _Dsx3AisEnable_Type()
)
dsx3AisEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3AisEnable.setStatus("current")


class _Dsx3TxClockSource_Type(Integer32):
    """Custom type dsx3TxClockSource based on Integer32"""
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
          ("system", 4),
          ("adaptive", 5))
    )


_Dsx3TxClockSource_Type.__name__ = "Integer32"
_Dsx3TxClockSource_Object = MibTableColumn
dsx3TxClockSource = _Dsx3TxClockSource_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 2, 1, 2),
    _Dsx3TxClockSource_Type()
)
dsx3TxClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TxClockSource.setStatus("current")


class _Dsx3TxPortQuality_Type(Integer32):
    """Custom type dsx3TxPortQuality based on Integer32"""
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


_Dsx3TxPortQuality_Type.__name__ = "Integer32"
_Dsx3TxPortQuality_Object = MibTableColumn
dsx3TxPortQuality = _Dsx3TxPortQuality_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 2, 1, 3),
    _Dsx3TxPortQuality_Type()
)
dsx3TxPortQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TxPortQuality.setStatus("current")
_Dsx3TxClockInstance_Type = Unsigned32
_Dsx3TxClockInstance_Object = MibTableColumn
dsx3TxClockInstance = _Dsx3TxClockInstance_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 2, 1, 4),
    _Dsx3TxClockInstance_Type()
)
dsx3TxClockInstance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3TxClockInstance.setStatus("current")
_Dsx3MappingTable_Object = MibTable
dsx3MappingTable = _Dsx3MappingTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    dsx3MappingTable.setStatus("current")
_Dsx3MappingEntry_Object = MibTableRow
dsx3MappingEntry = _Dsx3MappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 3, 1)
)
dsx3MappingEntry.setIndexNames(
    (0, "RAD-DS3-MIB", "dsx3MappingDs3Index"),
    (0, "RAD-DS3-MIB", "dsx3MappingNumber"),
)
if mibBuilder.loadTexts:
    dsx3MappingEntry.setStatus("deprecated")
_Dsx3MappingDs3Index_Type = InterfaceIndex
_Dsx3MappingDs3Index_Object = MibTableColumn
dsx3MappingDs3Index = _Dsx3MappingDs3Index_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 3, 1, 1),
    _Dsx3MappingDs3Index_Type()
)
dsx3MappingDs3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx3MappingDs3Index.setStatus("current")
_Dsx3MappingNumber_Type = Unsigned32
_Dsx3MappingNumber_Object = MibTableColumn
dsx3MappingNumber = _Dsx3MappingNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 3, 1, 2),
    _Dsx3MappingNumber_Type()
)
dsx3MappingNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsx3MappingNumber.setStatus("current")
_Dsx3MappingIfIndex_Type = InterfaceIndex
_Dsx3MappingIfIndex_Object = MibTableColumn
dsx3MappingIfIndex = _Dsx3MappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 3, 1, 3),
    _Dsx3MappingIfIndex_Type()
)
dsx3MappingIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dsx3MappingIfIndex.setStatus("current")
dsx3ConfigEntry.registerAugmentions(
    ("RAD-DS3-MIB",
     "dsx3XConfigEntry")
)
dsx3XConfigEntry.setIndexNames(*dsx3ConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

e3t3Rai = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 0, 1)
)
e3t3Rai.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS3-MIB", "dsx3LineStatus"))
)
if mibBuilder.loadTexts:
    e3t3Rai.setStatus(
        "current"
    )

e3t3Ais = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 0, 2)
)
e3t3Ais.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS3-MIB", "dsx3LineStatus"))
)
if mibBuilder.loadTexts:
    e3t3Ais.setStatus(
        "current"
    )

e3t3Lof = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 0, 3)
)
e3t3Lof.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS3-MIB", "dsx3LineStatus"))
)
if mibBuilder.loadTexts:
    e3t3Lof.setStatus(
        "current"
    )

e3t3Los = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 3, 1, 6, 3, 0, 4)
)
e3t3Los.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("IF-MIB", "ifAlias"),
        ("DS3-MIB", "dsx3LineStatus"))
)
if mibBuilder.loadTexts:
    e3t3Los.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-DS3-MIB",
    **{"ds3Interface": ds3Interface,
       "prtDS3Events": prtDS3Events,
       "e3t3Rai": e3t3Rai,
       "e3t3Ais": e3t3Ais,
       "e3t3Lof": e3t3Lof,
       "e3t3Los": e3t3Los,
       "prtDs3PerfHistory": prtDs3PerfHistory,
       "prtSDs3IfTable": prtSDs3IfTable,
       "prtDs3IfEntry": prtDs3IfEntry,
       "prtDs3IfTimeElapsed": prtDs3IfTimeElapsed,
       "prtDs3IfValidIntervals": prtDs3IfValidIntervals,
       "prtDs3CurrentTable": prtDs3CurrentTable,
       "prtDs3CurrentEntry": prtDs3CurrentEntry,
       "prtDs3CurrentLOS": prtDs3CurrentLOS,
       "prtDs3CurrentOOF": prtDs3CurrentOOF,
       "prtDs3CurrentLOC": prtDs3CurrentLOC,
       "prtDs3CurrentAIS": prtDs3CurrentAIS,
       "prtDs3CurrentRDI": prtDs3CurrentRDI,
       "prtDs3CurrentUAS": prtDs3CurrentUAS,
       "prtDs3CurrentBIP": prtDs3CurrentBIP,
       "prtDs3CurrentFEBE": prtDs3CurrentFEBE,
       "prtDs3CurrentSLM": prtDs3CurrentSLM,
       "prtDs3CurrentSES": prtDs3CurrentSES,
       "prtDs3CurrentES": prtDs3CurrentES,
       "prtDs3CurrentBitParity": prtDs3CurrentBitParity,
       "prtDs3CurrentPlcpLOF": prtDs3CurrentPlcpLOF,
       "prtDs3CurrentPlcpRAI": prtDs3CurrentPlcpRAI,
       "prtDs3CurrentPlcpBIP": prtDs3CurrentPlcpBIP,
       "prtDs3CurrentPlcpFEBE": prtDs3CurrentPlcpFEBE,
       "prtDs3CurrentBPV": prtDs3CurrentBPV,
       "prtDs3CurrentLCE": prtDs3CurrentLCE,
       "prtDs3CurrentStatus": prtDs3CurrentStatus,
       "prtDs3IntervalTable": prtDs3IntervalTable,
       "prtDs3IntervalEntry": prtDs3IntervalEntry,
       "prtDs3IntervalNumber": prtDs3IntervalNumber,
       "prtDs3IntervalLOS": prtDs3IntervalLOS,
       "prtDs3IntervalOOF": prtDs3IntervalOOF,
       "prtDs3IntervalLOC": prtDs3IntervalLOC,
       "prtDs3IntervalAIS": prtDs3IntervalAIS,
       "prtDs3IntervalRDI": prtDs3IntervalRDI,
       "prtDs3IntervalUAS": prtDs3IntervalUAS,
       "prtDs3IntervalBIP": prtDs3IntervalBIP,
       "prtDs3IntervalFEBE": prtDs3IntervalFEBE,
       "prtDs3IntervalSLM": prtDs3IntervalSLM,
       "prtDs3IntervalSES": prtDs3IntervalSES,
       "prtDs3IntervalES": prtDs3IntervalES,
       "prtDs3IntervalBitParity": prtDs3IntervalBitParity,
       "prtDs3IntervalPlcpLOF": prtDs3IntervalPlcpLOF,
       "prtDs3IntervalPlcpRAI": prtDs3IntervalPlcpRAI,
       "prtDs3IntervalPlcpBIP": prtDs3IntervalPlcpBIP,
       "prtDs3IntervalPlcpFEBE": prtDs3IntervalPlcpFEBE,
       "prtDs3IntervalBPV": prtDs3IntervalBPV,
       "prtDs3IntervalLCE": prtDs3IntervalLCE,
       "prtDs3IntervalStatus": prtDs3IntervalStatus,
       "prtDs3TotalTable": prtDs3TotalTable,
       "prtDs3TotalEntry": prtDs3TotalEntry,
       "prtDs3TotalUAS": prtDs3TotalUAS,
       "prtDs3TotalBPV": prtDs3TotalBPV,
       "prtDs3TotalLCE": prtDs3TotalLCE,
       "prtDs3TotalSES": prtDs3TotalSES,
       "dsx3XConfigTable": dsx3XConfigTable,
       "dsx3XConfigEntry": dsx3XConfigEntry,
       "dsx3AisEnable": dsx3AisEnable,
       "dsx3TxClockSource": dsx3TxClockSource,
       "dsx3TxPortQuality": dsx3TxPortQuality,
       "dsx3TxClockInstance": dsx3TxClockInstance,
       "dsx3MappingTable": dsx3MappingTable,
       "dsx3MappingEntry": dsx3MappingEntry,
       "dsx3MappingDs3Index": dsx3MappingDs3Index,
       "dsx3MappingNumber": dsx3MappingNumber,
       "dsx3MappingIfIndex": dsx3MappingIfIndex}
)
