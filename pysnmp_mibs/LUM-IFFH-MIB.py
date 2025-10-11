# SNMP MIB module (LUM-IFFH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFFH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:33 2025
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

(lumIfFhMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfFhMIB",
    "lumModules")

(FaultStatusWithNA,
 MgmtNameString,
 SignalStatusWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "FaultStatusWithNA",
    "MgmtNameString",
    "SignalStatusWithNA",
    "Unsigned32WithNA")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumIfFhMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 68)
)
if mibBuilder.loadTexts:
    lumIfFhMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2016-06-14 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfFhConfs_ObjectIdentity = ObjectIdentity
lumIfFhConfs = _LumIfFhConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 1)
)
_LumIfFhGroups_ObjectIdentity = ObjectIdentity
lumIfFhGroups = _LumIfFhGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 1, 1)
)
_LumIfFhCompl_ObjectIdentity = ObjectIdentity
lumIfFhCompl = _LumIfFhCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 1, 2)
)
_LumIfFhMIBObjects_ObjectIdentity = ObjectIdentity
lumIfFhMIBObjects = _LumIfFhMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2)
)
_IfFhGeneral_ObjectIdentity = ObjectIdentity
ifFhGeneral = _IfFhGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1)
)
_IfFhGeneralConfigLastChangeTime_Type = DateAndTime
_IfFhGeneralConfigLastChangeTime_Object = MibScalar
ifFhGeneralConfigLastChangeTime = _IfFhGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 1),
    _IfFhGeneralConfigLastChangeTime_Type()
)
ifFhGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralConfigLastChangeTime.setStatus("current")
_IfFhGeneralStateLastChangeTime_Type = DateAndTime
_IfFhGeneralStateLastChangeTime_Object = MibScalar
ifFhGeneralStateLastChangeTime = _IfFhGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 2),
    _IfFhGeneralStateLastChangeTime_Type()
)
ifFhGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralStateLastChangeTime.setStatus("current")
_IfFhGeneralIfFhCpriTableSize_Type = Unsigned32
_IfFhGeneralIfFhCpriTableSize_Object = MibScalar
ifFhGeneralIfFhCpriTableSize = _IfFhGeneralIfFhCpriTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 3),
    _IfFhGeneralIfFhCpriTableSize_Type()
)
ifFhGeneralIfFhCpriTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralIfFhCpriTableSize.setStatus("current")
_IfFhGeneralIfFhCpriConfigLastChangeTime_Type = DateAndTime
_IfFhGeneralIfFhCpriConfigLastChangeTime_Object = MibScalar
ifFhGeneralIfFhCpriConfigLastChangeTime = _IfFhGeneralIfFhCpriConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 4),
    _IfFhGeneralIfFhCpriConfigLastChangeTime_Type()
)
ifFhGeneralIfFhCpriConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralIfFhCpriConfigLastChangeTime.setStatus("current")
_IfFhGeneralIfFhCpriStateLastChangeTime_Type = DateAndTime
_IfFhGeneralIfFhCpriStateLastChangeTime_Object = MibScalar
ifFhGeneralIfFhCpriStateLastChangeTime = _IfFhGeneralIfFhCpriStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 5),
    _IfFhGeneralIfFhCpriStateLastChangeTime_Type()
)
ifFhGeneralIfFhCpriStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralIfFhCpriStateLastChangeTime.setStatus("current")
_IfFhGeneralIfFhObsaiTableSize_Type = Unsigned32
_IfFhGeneralIfFhObsaiTableSize_Object = MibScalar
ifFhGeneralIfFhObsaiTableSize = _IfFhGeneralIfFhObsaiTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 6),
    _IfFhGeneralIfFhObsaiTableSize_Type()
)
ifFhGeneralIfFhObsaiTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralIfFhObsaiTableSize.setStatus("current")
_IfFhGeneralIfFhObsaiConfigLastChangeTime_Type = DateAndTime
_IfFhGeneralIfFhObsaiConfigLastChangeTime_Object = MibScalar
ifFhGeneralIfFhObsaiConfigLastChangeTime = _IfFhGeneralIfFhObsaiConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 7),
    _IfFhGeneralIfFhObsaiConfigLastChangeTime_Type()
)
ifFhGeneralIfFhObsaiConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralIfFhObsaiConfigLastChangeTime.setStatus("current")
_IfFhGeneralIfFhObsaiStateLastChangeTime_Type = DateAndTime
_IfFhGeneralIfFhObsaiStateLastChangeTime_Object = MibScalar
ifFhGeneralIfFhObsaiStateLastChangeTime = _IfFhGeneralIfFhObsaiStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 1, 8),
    _IfFhGeneralIfFhObsaiStateLastChangeTime_Type()
)
ifFhGeneralIfFhObsaiStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhGeneralIfFhObsaiStateLastChangeTime.setStatus("current")
_IfFhCpriList_ObjectIdentity = ObjectIdentity
ifFhCpriList = _IfFhCpriList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2)
)
_IfFhCpriTable_Object = MibTable
ifFhCpriTable = _IfFhCpriTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifFhCpriTable.setStatus("current")
_IfFhCpriEntry_Object = MibTableRow
ifFhCpriEntry = _IfFhCpriEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1)
)
ifFhCpriEntry.setIndexNames(
    (0, "LUM-IFFH-MIB", "ifFhCpriIndex"),
)
if mibBuilder.loadTexts:
    ifFhCpriEntry.setStatus("current")
_IfFhCpriIndex_Type = Unsigned32
_IfFhCpriIndex_Object = MibTableColumn
ifFhCpriIndex = _IfFhCpriIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 1),
    _IfFhCpriIndex_Type()
)
ifFhCpriIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriIndex.setStatus("current")
_IfFhCpriUId_Type = Unsigned32
_IfFhCpriUId_Object = MibTableColumn
ifFhCpriUId = _IfFhCpriUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 2),
    _IfFhCpriUId_Type()
)
ifFhCpriUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriUId.setStatus("current")
_IfFhCpriName_Type = MgmtNameString
_IfFhCpriName_Object = MibTableColumn
ifFhCpriName = _IfFhCpriName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 3),
    _IfFhCpriName_Type()
)
ifFhCpriName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriName.setStatus("current")
_IfFhCpriConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfFhCpriConnIfBasicIfIndex_Object = MibTableColumn
ifFhCpriConnIfBasicIfIndex = _IfFhCpriConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 4),
    _IfFhCpriConnIfBasicIfIndex_Type()
)
ifFhCpriConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriConnIfBasicIfIndex.setStatus("current")
_IfFhCpriTxSignalStatus_Type = SignalStatusWithNA
_IfFhCpriTxSignalStatus_Object = MibTableColumn
ifFhCpriTxSignalStatus = _IfFhCpriTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 5),
    _IfFhCpriTxSignalStatus_Type()
)
ifFhCpriTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriTxSignalStatus.setStatus("current")
_IfFhCpriRxSignalStatus_Type = SignalStatusWithNA
_IfFhCpriRxSignalStatus_Object = MibTableColumn
ifFhCpriRxSignalStatus = _IfFhCpriRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 6),
    _IfFhCpriRxSignalStatus_Type()
)
ifFhCpriRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriRxSignalStatus.setStatus("current")
_IfFhCpriTxLossOfFrame_Type = FaultStatusWithNA
_IfFhCpriTxLossOfFrame_Object = MibTableColumn
ifFhCpriTxLossOfFrame = _IfFhCpriTxLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 7),
    _IfFhCpriTxLossOfFrame_Type()
)
ifFhCpriTxLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriTxLossOfFrame.setStatus("current")
_IfFhCpriRxLossOfFrame_Type = FaultStatusWithNA
_IfFhCpriRxLossOfFrame_Object = MibTableColumn
ifFhCpriRxLossOfFrame = _IfFhCpriRxLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 8),
    _IfFhCpriRxLossOfFrame_Type()
)
ifFhCpriRxLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriRxLossOfFrame.setStatus("current")
_IfFhCpriRxSAPDefectInd_Type = FaultStatusWithNA
_IfFhCpriRxSAPDefectInd_Object = MibTableColumn
ifFhCpriRxSAPDefectInd = _IfFhCpriRxSAPDefectInd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 9),
    _IfFhCpriRxSAPDefectInd_Type()
)
ifFhCpriRxSAPDefectInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriRxSAPDefectInd.setStatus("current")
_IfFhCpriRxRemoteAlarmInd_Type = FaultStatusWithNA
_IfFhCpriRxRemoteAlarmInd_Object = MibTableColumn
ifFhCpriRxRemoteAlarmInd = _IfFhCpriRxRemoteAlarmInd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 2, 1, 1, 10),
    _IfFhCpriRxRemoteAlarmInd_Type()
)
ifFhCpriRxRemoteAlarmInd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhCpriRxRemoteAlarmInd.setStatus("current")
_IfFhObsaiList_ObjectIdentity = ObjectIdentity
ifFhObsaiList = _IfFhObsaiList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3)
)
_IfFhObsaiTable_Object = MibTable
ifFhObsaiTable = _IfFhObsaiTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifFhObsaiTable.setStatus("current")
_IfFhObsaiEntry_Object = MibTableRow
ifFhObsaiEntry = _IfFhObsaiEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1)
)
ifFhObsaiEntry.setIndexNames(
    (0, "LUM-IFFH-MIB", "ifFhObsaiIndex"),
)
if mibBuilder.loadTexts:
    ifFhObsaiEntry.setStatus("current")
_IfFhObsaiIndex_Type = Unsigned32
_IfFhObsaiIndex_Object = MibTableColumn
ifFhObsaiIndex = _IfFhObsaiIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 1),
    _IfFhObsaiIndex_Type()
)
ifFhObsaiIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiIndex.setStatus("current")
_IfFhObsaiUId_Type = Unsigned32
_IfFhObsaiUId_Object = MibTableColumn
ifFhObsaiUId = _IfFhObsaiUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 2),
    _IfFhObsaiUId_Type()
)
ifFhObsaiUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiUId.setStatus("current")
_IfFhObsaiName_Type = MgmtNameString
_IfFhObsaiName_Object = MibTableColumn
ifFhObsaiName = _IfFhObsaiName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 3),
    _IfFhObsaiName_Type()
)
ifFhObsaiName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiName.setStatus("current")
_IfFhObsaiConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfFhObsaiConnIfBasicIfIndex_Object = MibTableColumn
ifFhObsaiConnIfBasicIfIndex = _IfFhObsaiConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 4),
    _IfFhObsaiConnIfBasicIfIndex_Type()
)
ifFhObsaiConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiConnIfBasicIfIndex.setStatus("current")
_IfFhObsaiTxSignalStatus_Type = SignalStatusWithNA
_IfFhObsaiTxSignalStatus_Object = MibTableColumn
ifFhObsaiTxSignalStatus = _IfFhObsaiTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 5),
    _IfFhObsaiTxSignalStatus_Type()
)
ifFhObsaiTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiTxSignalStatus.setStatus("current")
_IfFhObsaiRxSignalStatus_Type = SignalStatusWithNA
_IfFhObsaiRxSignalStatus_Object = MibTableColumn
ifFhObsaiRxSignalStatus = _IfFhObsaiRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 6),
    _IfFhObsaiRxSignalStatus_Type()
)
ifFhObsaiRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiRxSignalStatus.setStatus("current")
_IfFhObsaiRxLossOfFrame_Type = FaultStatusWithNA
_IfFhObsaiRxLossOfFrame_Object = MibTableColumn
ifFhObsaiRxLossOfFrame = _IfFhObsaiRxLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 7),
    _IfFhObsaiRxLossOfFrame_Type()
)
ifFhObsaiRxLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiRxLossOfFrame.setStatus("current")
_IfFhObsaiTxLossOfFrame_Type = FaultStatusWithNA
_IfFhObsaiTxLossOfFrame_Object = MibTableColumn
ifFhObsaiTxLossOfFrame = _IfFhObsaiTxLossOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 2, 3, 1, 1, 8),
    _IfFhObsaiTxLossOfFrame_Type()
)
ifFhObsaiTxLossOfFrame.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifFhObsaiTxLossOfFrame.setStatus("current")

# Managed Objects groups

ifFhGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 1, 1, 1)
)
ifFhGeneralGroupV1.setObjects(
      *(("LUM-IFFH-MIB", "ifFhGeneralConfigLastChangeTime"),
        ("LUM-IFFH-MIB", "ifFhGeneralStateLastChangeTime"),
        ("LUM-IFFH-MIB", "ifFhGeneralIfFhCpriTableSize"),
        ("LUM-IFFH-MIB", "ifFhGeneralIfFhCpriConfigLastChangeTime"),
        ("LUM-IFFH-MIB", "ifFhGeneralIfFhCpriStateLastChangeTime"),
        ("LUM-IFFH-MIB", "ifFhGeneralIfFhObsaiTableSize"),
        ("LUM-IFFH-MIB", "ifFhGeneralIfFhObsaiConfigLastChangeTime"),
        ("LUM-IFFH-MIB", "ifFhGeneralIfFhObsaiStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifFhGeneralGroupV1.setStatus("current")

ifFhCpriGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 1, 1, 2)
)
ifFhCpriGroupV1.setObjects(
      *(("LUM-IFFH-MIB", "ifFhCpriIndex"),
        ("LUM-IFFH-MIB", "ifFhCpriUId"),
        ("LUM-IFFH-MIB", "ifFhCpriName"),
        ("LUM-IFFH-MIB", "ifFhCpriConnIfBasicIfIndex"),
        ("LUM-IFFH-MIB", "ifFhCpriTxSignalStatus"),
        ("LUM-IFFH-MIB", "ifFhCpriRxSignalStatus"),
        ("LUM-IFFH-MIB", "ifFhCpriTxLossOfFrame"),
        ("LUM-IFFH-MIB", "ifFhCpriRxLossOfFrame"),
        ("LUM-IFFH-MIB", "ifFhCpriRxSAPDefectInd"),
        ("LUM-IFFH-MIB", "ifFhCpriRxRemoteAlarmInd"))
)
if mibBuilder.loadTexts:
    ifFhCpriGroupV1.setStatus("current")

ifFhObsaiGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 1, 1, 3)
)
ifFhObsaiGroupV1.setObjects(
      *(("LUM-IFFH-MIB", "ifFhObsaiIndex"),
        ("LUM-IFFH-MIB", "ifFhObsaiUId"),
        ("LUM-IFFH-MIB", "ifFhObsaiName"),
        ("LUM-IFFH-MIB", "ifFhObsaiConnIfBasicIfIndex"),
        ("LUM-IFFH-MIB", "ifFhObsaiTxSignalStatus"),
        ("LUM-IFFH-MIB", "ifFhObsaiRxSignalStatus"),
        ("LUM-IFFH-MIB", "ifFhObsaiRxLossOfFrame"),
        ("LUM-IFFH-MIB", "ifFhObsaiTxLossOfFrame"))
)
if mibBuilder.loadTexts:
    ifFhObsaiGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfFhComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 68, 1, 2, 1)
)
lumIfFhComplV1.setObjects(
      *(("LUM-IFFH-MIB", "ifFhGeneralGroupV1"),
        ("LUM-IFFH-MIB", "ifFhCpriGroupV1"),
        ("LUM-IFFH-MIB", "ifFhObsaiGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfFhComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFFH-MIB",
    **{"lumIfFhMIBModule": lumIfFhMIBModule,
       "lumIfFhConfs": lumIfFhConfs,
       "lumIfFhGroups": lumIfFhGroups,
       "ifFhGeneralGroupV1": ifFhGeneralGroupV1,
       "ifFhCpriGroupV1": ifFhCpriGroupV1,
       "ifFhObsaiGroupV1": ifFhObsaiGroupV1,
       "lumIfFhCompl": lumIfFhCompl,
       "lumIfFhComplV1": lumIfFhComplV1,
       "lumIfFhMIBObjects": lumIfFhMIBObjects,
       "ifFhGeneral": ifFhGeneral,
       "ifFhGeneralConfigLastChangeTime": ifFhGeneralConfigLastChangeTime,
       "ifFhGeneralStateLastChangeTime": ifFhGeneralStateLastChangeTime,
       "ifFhGeneralIfFhCpriTableSize": ifFhGeneralIfFhCpriTableSize,
       "ifFhGeneralIfFhCpriConfigLastChangeTime": ifFhGeneralIfFhCpriConfigLastChangeTime,
       "ifFhGeneralIfFhCpriStateLastChangeTime": ifFhGeneralIfFhCpriStateLastChangeTime,
       "ifFhGeneralIfFhObsaiTableSize": ifFhGeneralIfFhObsaiTableSize,
       "ifFhGeneralIfFhObsaiConfigLastChangeTime": ifFhGeneralIfFhObsaiConfigLastChangeTime,
       "ifFhGeneralIfFhObsaiStateLastChangeTime": ifFhGeneralIfFhObsaiStateLastChangeTime,
       "ifFhCpriList": ifFhCpriList,
       "ifFhCpriTable": ifFhCpriTable,
       "ifFhCpriEntry": ifFhCpriEntry,
       "ifFhCpriIndex": ifFhCpriIndex,
       "ifFhCpriUId": ifFhCpriUId,
       "ifFhCpriName": ifFhCpriName,
       "ifFhCpriConnIfBasicIfIndex": ifFhCpriConnIfBasicIfIndex,
       "ifFhCpriTxSignalStatus": ifFhCpriTxSignalStatus,
       "ifFhCpriRxSignalStatus": ifFhCpriRxSignalStatus,
       "ifFhCpriTxLossOfFrame": ifFhCpriTxLossOfFrame,
       "ifFhCpriRxLossOfFrame": ifFhCpriRxLossOfFrame,
       "ifFhCpriRxSAPDefectInd": ifFhCpriRxSAPDefectInd,
       "ifFhCpriRxRemoteAlarmInd": ifFhCpriRxRemoteAlarmInd,
       "ifFhObsaiList": ifFhObsaiList,
       "ifFhObsaiTable": ifFhObsaiTable,
       "ifFhObsaiEntry": ifFhObsaiEntry,
       "ifFhObsaiIndex": ifFhObsaiIndex,
       "ifFhObsaiUId": ifFhObsaiUId,
       "ifFhObsaiName": ifFhObsaiName,
       "ifFhObsaiConnIfBasicIfIndex": ifFhObsaiConnIfBasicIfIndex,
       "ifFhObsaiTxSignalStatus": ifFhObsaiTxSignalStatus,
       "ifFhObsaiRxSignalStatus": ifFhObsaiRxSignalStatus,
       "ifFhObsaiRxLossOfFrame": ifFhObsaiRxLossOfFrame,
       "ifFhObsaiTxLossOfFrame": ifFhObsaiTxLossOfFrame}
)
