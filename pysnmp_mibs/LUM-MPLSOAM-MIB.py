# SNMP MIB module (LUM-MPLSOAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-MPLSOAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:36 2025
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

(lumModules,
 lumMplsOamMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumMplsOamMIB")

(CommandString,
 FaultStatus,
 MgmtNameString) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "FaultStatus",
    "MgmtNameString")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lumMplsOamMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 44)
)
if mibBuilder.loadTexts:
    lumMplsOamMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2012-12-25 12:00",
         "2012-03-01 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BfdSessStateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("adminDown", 1),
          ("down", 2),
          ("init", 3),
          ("up", 4),
          ("failing", 5))
    )



class BfdMultiplierTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )



class BfdIntervalTC(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )



class BfdDiagTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noDiagnostic", 0),
          ("controlDetectionTimeExpired", 1),
          ("echoFunctionFailed", 2),
          ("neighborSignaledSessionDown", 3),
          ("forwardingPlaneReset", 4),
          ("pathDown", 5),
          ("concatenatedPathDown", 6),
          ("administrativelyDown", 7),
          ("reverseConcatenatedPathDown", 8),
          ("misconnectionDefect", 9))
    )



# MIB Managed Objects in the order of their OIDs

_LumMplsOamConfs_ObjectIdentity = ObjectIdentity
lumMplsOamConfs = _LumMplsOamConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1)
)
_LumMplsOamGroups_ObjectIdentity = ObjectIdentity
lumMplsOamGroups = _LumMplsOamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 1)
)
_LumMplsOamCompl_ObjectIdentity = ObjectIdentity
lumMplsOamCompl = _LumMplsOamCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 2)
)
_LumMplsOamMIBObjects_ObjectIdentity = ObjectIdentity
lumMplsOamMIBObjects = _LumMplsOamMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2)
)
_MplsOamGeneral_ObjectIdentity = ObjectIdentity
mplsOamGeneral = _MplsOamGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 1)
)
_MplsOamGeneralLastChangeTime_Type = DateAndTime
_MplsOamGeneralLastChangeTime_Object = MibScalar
mplsOamGeneralLastChangeTime = _MplsOamGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 1, 1),
    _MplsOamGeneralLastChangeTime_Type()
)
mplsOamGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamGeneralLastChangeTime.setStatus("current")
_MplsOamGeneralStateLastChangeTime_Type = DateAndTime
_MplsOamGeneralStateLastChangeTime_Object = MibScalar
mplsOamGeneralStateLastChangeTime = _MplsOamGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 1, 2),
    _MplsOamGeneralStateLastChangeTime_Type()
)
mplsOamGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamGeneralStateLastChangeTime.setStatus("current")
_MplsOamGeneralmplsOamBfdSessTableSize_Type = Unsigned32
_MplsOamGeneralmplsOamBfdSessTableSize_Object = MibScalar
mplsOamGeneralmplsOamBfdSessTableSize = _MplsOamGeneralmplsOamBfdSessTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 1, 3),
    _MplsOamGeneralmplsOamBfdSessTableSize_Type()
)
mplsOamGeneralmplsOamBfdSessTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamGeneralmplsOamBfdSessTableSize.setStatus("current")
_MplsOamGeneralmplsOamBfdTemplateTableSize_Type = Unsigned32
_MplsOamGeneralmplsOamBfdTemplateTableSize_Object = MibScalar
mplsOamGeneralmplsOamBfdTemplateTableSize = _MplsOamGeneralmplsOamBfdTemplateTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 1, 4),
    _MplsOamGeneralmplsOamBfdTemplateTableSize_Type()
)
mplsOamGeneralmplsOamBfdTemplateTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamGeneralmplsOamBfdTemplateTableSize.setStatus("current")
_MplsOamBfdSess_ObjectIdentity = ObjectIdentity
mplsOamBfdSess = _MplsOamBfdSess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2)
)
_MplsOamBfdSessTable_Object = MibTable
mplsOamBfdSessTable = _MplsOamBfdSessTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    mplsOamBfdSessTable.setStatus("current")
_MplsOamBfdSessEntry_Object = MibTableRow
mplsOamBfdSessEntry = _MplsOamBfdSessEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1)
)
mplsOamBfdSessEntry.setIndexNames(
    (0, "LUM-MPLSOAM-MIB", "mplsOamBfdSessIndex"),
)
if mibBuilder.loadTexts:
    mplsOamBfdSessEntry.setStatus("current")


class _MplsOamBfdSessIndex_Type(Unsigned32):
    """Custom type mplsOamBfdSessIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsOamBfdSessIndex_Type.__name__ = "Unsigned32"
_MplsOamBfdSessIndex_Object = MibTableColumn
mplsOamBfdSessIndex = _MplsOamBfdSessIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 1),
    _MplsOamBfdSessIndex_Type()
)
mplsOamBfdSessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessIndex.setStatus("current")


class _MplsOamBfdSessInternalReference_Type(Unsigned32):
    """Custom type mplsOamBfdSessInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsOamBfdSessInternalReference_Type.__name__ = "Unsigned32"
_MplsOamBfdSessInternalReference_Object = MibTableColumn
mplsOamBfdSessInternalReference = _MplsOamBfdSessInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 2),
    _MplsOamBfdSessInternalReference_Type()
)
mplsOamBfdSessInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdSessInternalReference.setStatus("current")
_MplsOamBfdSessName_Type = MgmtNameString
_MplsOamBfdSessName_Object = MibTableColumn
mplsOamBfdSessName = _MplsOamBfdSessName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 3),
    _MplsOamBfdSessName_Type()
)
mplsOamBfdSessName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessName.setStatus("current")


class _MplsOamBfdSessAdminStatus_Type(Integer32):
    """Custom type mplsOamBfdSessAdminStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_MplsOamBfdSessAdminStatus_Type.__name__ = "Integer32"
_MplsOamBfdSessAdminStatus_Object = MibTableColumn
mplsOamBfdSessAdminStatus = _MplsOamBfdSessAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 4),
    _MplsOamBfdSessAdminStatus_Type()
)
mplsOamBfdSessAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsOamBfdSessAdminStatus.setStatus("current")
_MplsOamBfdSessState_Type = BfdSessStateTC
_MplsOamBfdSessState_Object = MibTableColumn
mplsOamBfdSessState = _MplsOamBfdSessState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 5),
    _MplsOamBfdSessState_Type()
)
mplsOamBfdSessState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessState.setStatus("current")
_MplsOamBfdSessRemoteState_Type = BfdSessStateTC
_MplsOamBfdSessRemoteState_Object = MibTableColumn
mplsOamBfdSessRemoteState = _MplsOamBfdSessRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 6),
    _MplsOamBfdSessRemoteState_Type()
)
mplsOamBfdSessRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessRemoteState.setStatus("current")
_MplsOamBfdSessDiag_Type = BfdDiagTC
_MplsOamBfdSessDiag_Object = MibTableColumn
mplsOamBfdSessDiag = _MplsOamBfdSessDiag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 7),
    _MplsOamBfdSessDiag_Type()
)
mplsOamBfdSessDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessDiag.setStatus("current")
_MplsOamBfdSessRemoteDiag_Type = BfdDiagTC
_MplsOamBfdSessRemoteDiag_Object = MibTableColumn
mplsOamBfdSessRemoteDiag = _MplsOamBfdSessRemoteDiag_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 8),
    _MplsOamBfdSessRemoteDiag_Type()
)
mplsOamBfdSessRemoteDiag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessRemoteDiag.setStatus("current")
_MplsOamBfdSessNegotiatedTxInterval_Type = BfdIntervalTC
_MplsOamBfdSessNegotiatedTxInterval_Object = MibTableColumn
mplsOamBfdSessNegotiatedTxInterval = _MplsOamBfdSessNegotiatedTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 9),
    _MplsOamBfdSessNegotiatedTxInterval_Type()
)
mplsOamBfdSessNegotiatedTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessNegotiatedTxInterval.setStatus("current")
_MplsOamBfdSessNegotiatedRxInterval_Type = BfdIntervalTC
_MplsOamBfdSessNegotiatedRxInterval_Object = MibTableColumn
mplsOamBfdSessNegotiatedRxInterval = _MplsOamBfdSessNegotiatedRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 10),
    _MplsOamBfdSessNegotiatedRxInterval_Type()
)
mplsOamBfdSessNegotiatedRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessNegotiatedRxInterval.setStatus("current")


class _MplsOamBfdSessMonitoringPath_Type(DisplayString):
    """Custom type mplsOamBfdSessMonitoringPath based on DisplayString"""
    defaultValue = OctetString("")


_MplsOamBfdSessMonitoringPath_Type.__name__ = "DisplayString"
_MplsOamBfdSessMonitoringPath_Object = MibTableColumn
mplsOamBfdSessMonitoringPath = _MplsOamBfdSessMonitoringPath_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 11),
    _MplsOamBfdSessMonitoringPath_Type()
)
mplsOamBfdSessMonitoringPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdSessMonitoringPath.setStatus("current")


class _MplsOamBfdSessMonitoringPathType_Type(Integer32):
    """Custom type mplsOamBfdSessMonitoringPathType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSelected", 0),
          ("lsp", 1))
    )


_MplsOamBfdSessMonitoringPathType_Type.__name__ = "Integer32"
_MplsOamBfdSessMonitoringPathType_Object = MibTableColumn
mplsOamBfdSessMonitoringPathType = _MplsOamBfdSessMonitoringPathType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 12),
    _MplsOamBfdSessMonitoringPathType_Type()
)
mplsOamBfdSessMonitoringPathType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdSessMonitoringPathType.setStatus("current")


class _MplsOamBfdSessMonitoringPathIndex_Type(Unsigned32):
    """Custom type mplsOamBfdSessMonitoringPathIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsOamBfdSessMonitoringPathIndex_Type.__name__ = "Unsigned32"
_MplsOamBfdSessMonitoringPathIndex_Object = MibTableColumn
mplsOamBfdSessMonitoringPathIndex = _MplsOamBfdSessMonitoringPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 13),
    _MplsOamBfdSessMonitoringPathIndex_Type()
)
mplsOamBfdSessMonitoringPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessMonitoringPathIndex.setStatus("current")


class _MplsOamBfdSessTemplate_Type(DisplayString):
    """Custom type mplsOamBfdSessTemplate based on DisplayString"""
    defaultValue = OctetString("")


_MplsOamBfdSessTemplate_Type.__name__ = "DisplayString"
_MplsOamBfdSessTemplate_Object = MibTableColumn
mplsOamBfdSessTemplate = _MplsOamBfdSessTemplate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 14),
    _MplsOamBfdSessTemplate_Type()
)
mplsOamBfdSessTemplate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdSessTemplate.setStatus("current")


class _MplsOamBfdSessTemplateIndex_Type(Unsigned32):
    """Custom type mplsOamBfdSessTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsOamBfdSessTemplateIndex_Type.__name__ = "Unsigned32"
_MplsOamBfdSessTemplateIndex_Object = MibTableColumn
mplsOamBfdSessTemplateIndex = _MplsOamBfdSessTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 15),
    _MplsOamBfdSessTemplateIndex_Type()
)
mplsOamBfdSessTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessTemplateIndex.setStatus("current")
_MplsOamBfdSessSourceMepId_Type = DisplayString
_MplsOamBfdSessSourceMepId_Object = MibTableColumn
mplsOamBfdSessSourceMepId = _MplsOamBfdSessSourceMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 16),
    _MplsOamBfdSessSourceMepId_Type()
)
mplsOamBfdSessSourceMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessSourceMepId.setStatus("current")
_MplsOamBfdSessTargetMepId_Type = DisplayString
_MplsOamBfdSessTargetMepId_Object = MibTableColumn
mplsOamBfdSessTargetMepId = _MplsOamBfdSessTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 17),
    _MplsOamBfdSessTargetMepId_Type()
)
mplsOamBfdSessTargetMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessTargetMepId.setStatus("current")
_MplsOamBfdSessRcvTargetMepId_Type = DisplayString
_MplsOamBfdSessRcvTargetMepId_Object = MibTableColumn
mplsOamBfdSessRcvTargetMepId = _MplsOamBfdSessRcvTargetMepId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 18),
    _MplsOamBfdSessRcvTargetMepId_Type()
)
mplsOamBfdSessRcvTargetMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessRcvTargetMepId.setStatus("current")
_MplsOamBfdSessMepNotConfigured_Type = FaultStatus
_MplsOamBfdSessMepNotConfigured_Object = MibTableColumn
mplsOamBfdSessMepNotConfigured = _MplsOamBfdSessMepNotConfigured_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 19),
    _MplsOamBfdSessMepNotConfigured_Type()
)
mplsOamBfdSessMepNotConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessMepNotConfigured.setStatus("current")
_MplsOamBfdSessLocalNotConnected_Type = FaultStatus
_MplsOamBfdSessLocalNotConnected_Object = MibTableColumn
mplsOamBfdSessLocalNotConnected = _MplsOamBfdSessLocalNotConnected_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 20),
    _MplsOamBfdSessLocalNotConnected_Type()
)
mplsOamBfdSessLocalNotConnected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessLocalNotConnected.setStatus("current")
_MplsOamBfdSessLocalMisConnectivity_Type = FaultStatus
_MplsOamBfdSessLocalMisConnectivity_Object = MibTableColumn
mplsOamBfdSessLocalMisConnectivity = _MplsOamBfdSessLocalMisConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 21),
    _MplsOamBfdSessLocalMisConnectivity_Type()
)
mplsOamBfdSessLocalMisConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessLocalMisConnectivity.setStatus("current")
_MplsOamBfdSessLocalTimerExpired_Type = FaultStatus
_MplsOamBfdSessLocalTimerExpired_Object = MibTableColumn
mplsOamBfdSessLocalTimerExpired = _MplsOamBfdSessLocalTimerExpired_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 22),
    _MplsOamBfdSessLocalTimerExpired_Type()
)
mplsOamBfdSessLocalTimerExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessLocalTimerExpired.setStatus("current")
_MplsOamBfdSessRemoteMisConnectivity_Type = FaultStatus
_MplsOamBfdSessRemoteMisConnectivity_Object = MibTableColumn
mplsOamBfdSessRemoteMisConnectivity = _MplsOamBfdSessRemoteMisConnectivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 23),
    _MplsOamBfdSessRemoteMisConnectivity_Type()
)
mplsOamBfdSessRemoteMisConnectivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessRemoteMisConnectivity.setStatus("current")
_MplsOamBfdSessRemoteTimerExpired_Type = FaultStatus
_MplsOamBfdSessRemoteTimerExpired_Object = MibTableColumn
mplsOamBfdSessRemoteTimerExpired = _MplsOamBfdSessRemoteTimerExpired_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 24),
    _MplsOamBfdSessRemoteTimerExpired_Type()
)
mplsOamBfdSessRemoteTimerExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessRemoteTimerExpired.setStatus("current")
_MplsOamBfdSessRemoteAdminDown_Type = FaultStatus
_MplsOamBfdSessRemoteAdminDown_Object = MibTableColumn
mplsOamBfdSessRemoteAdminDown = _MplsOamBfdSessRemoteAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 25),
    _MplsOamBfdSessRemoteAdminDown_Type()
)
mplsOamBfdSessRemoteAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessRemoteAdminDown.setStatus("current")
_MplsOamBfdSessRowStatus_Type = RowStatus
_MplsOamBfdSessRowStatus_Object = MibTableColumn
mplsOamBfdSessRowStatus = _MplsOamBfdSessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 26),
    _MplsOamBfdSessRowStatus_Type()
)
mplsOamBfdSessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdSessRowStatus.setStatus("current")


class _MplsOamBfdSessDesiredMinTxInterval_Type(BfdIntervalTC):
    """Custom type mplsOamBfdSessDesiredMinTxInterval based on BfdIntervalTC"""
    defaultValue = 100000


_MplsOamBfdSessDesiredMinTxInterval_Type.__name__ = "BfdIntervalTC"
_MplsOamBfdSessDesiredMinTxInterval_Object = MibTableColumn
mplsOamBfdSessDesiredMinTxInterval = _MplsOamBfdSessDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 27),
    _MplsOamBfdSessDesiredMinTxInterval_Type()
)
mplsOamBfdSessDesiredMinTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessDesiredMinTxInterval.setStatus("current")


class _MplsOamBfdSessReqMinRxInterval_Type(BfdIntervalTC):
    """Custom type mplsOamBfdSessReqMinRxInterval based on BfdIntervalTC"""
    defaultValue = 100000


_MplsOamBfdSessReqMinRxInterval_Type.__name__ = "BfdIntervalTC"
_MplsOamBfdSessReqMinRxInterval_Object = MibTableColumn
mplsOamBfdSessReqMinRxInterval = _MplsOamBfdSessReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 28),
    _MplsOamBfdSessReqMinRxInterval_Type()
)
mplsOamBfdSessReqMinRxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdSessReqMinRxInterval.setStatus("current")


class _MplsOamBfdSessTrafficClass_Type(Unsigned32):
    """Custom type mplsOamBfdSessTrafficClass based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MplsOamBfdSessTrafficClass_Type.__name__ = "Unsigned32"
_MplsOamBfdSessTrafficClass_Object = MibTableColumn
mplsOamBfdSessTrafficClass = _MplsOamBfdSessTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 2, 1, 1, 29),
    _MplsOamBfdSessTrafficClass_Type()
)
mplsOamBfdSessTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mplsOamBfdSessTrafficClass.setStatus("current")
_MplsOamBfdTemplate_ObjectIdentity = ObjectIdentity
mplsOamBfdTemplate = _MplsOamBfdTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3)
)
_MplsOamBfdTemplateTable_Object = MibTable
mplsOamBfdTemplateTable = _MplsOamBfdTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2)
)
if mibBuilder.loadTexts:
    mplsOamBfdTemplateTable.setStatus("current")
_MplsOamBfdTemplateEntry_Object = MibTableRow
mplsOamBfdTemplateEntry = _MplsOamBfdTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1)
)
mplsOamBfdTemplateEntry.setIndexNames(
    (0, "LUM-MPLSOAM-MIB", "mplsOamBfdTemplateIndex"),
)
if mibBuilder.loadTexts:
    mplsOamBfdTemplateEntry.setStatus("current")


class _MplsOamBfdTemplateIndex_Type(Unsigned32):
    """Custom type mplsOamBfdTemplateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_MplsOamBfdTemplateIndex_Type.__name__ = "Unsigned32"
_MplsOamBfdTemplateIndex_Object = MibTableColumn
mplsOamBfdTemplateIndex = _MplsOamBfdTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 1),
    _MplsOamBfdTemplateIndex_Type()
)
mplsOamBfdTemplateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateIndex.setStatus("current")


class _MplsOamBfdTemplateInternalReference_Type(Unsigned32):
    """Custom type mplsOamBfdTemplateInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_MplsOamBfdTemplateInternalReference_Type.__name__ = "Unsigned32"
_MplsOamBfdTemplateInternalReference_Object = MibTableColumn
mplsOamBfdTemplateInternalReference = _MplsOamBfdTemplateInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 2),
    _MplsOamBfdTemplateInternalReference_Type()
)
mplsOamBfdTemplateInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateInternalReference.setStatus("current")
_MplsOamBfdTemplateName_Type = MgmtNameString
_MplsOamBfdTemplateName_Object = MibTableColumn
mplsOamBfdTemplateName = _MplsOamBfdTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 3),
    _MplsOamBfdTemplateName_Type()
)
mplsOamBfdTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateName.setStatus("current")


class _MplsOamBfdTemplateIdentifier_Type(DisplayString):
    """Custom type mplsOamBfdTemplateIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_MplsOamBfdTemplateIdentifier_Type.__name__ = "DisplayString"
_MplsOamBfdTemplateIdentifier_Object = MibTableColumn
mplsOamBfdTemplateIdentifier = _MplsOamBfdTemplateIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 4),
    _MplsOamBfdTemplateIdentifier_Type()
)
mplsOamBfdTemplateIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateIdentifier.setStatus("current")


class _MplsOamBfdTemplateDesiredMinTxInterval_Type(BfdIntervalTC):
    """Custom type mplsOamBfdTemplateDesiredMinTxInterval based on BfdIntervalTC"""
    defaultValue = 100000


_MplsOamBfdTemplateDesiredMinTxInterval_Type.__name__ = "BfdIntervalTC"
_MplsOamBfdTemplateDesiredMinTxInterval_Object = MibTableColumn
mplsOamBfdTemplateDesiredMinTxInterval = _MplsOamBfdTemplateDesiredMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 5),
    _MplsOamBfdTemplateDesiredMinTxInterval_Type()
)
mplsOamBfdTemplateDesiredMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateDesiredMinTxInterval.setStatus("current")


class _MplsOamBfdTemplateDetectMult_Type(BfdMultiplierTC):
    """Custom type mplsOamBfdTemplateDetectMult based on BfdMultiplierTC"""
    defaultValue = 3


_MplsOamBfdTemplateDetectMult_Type.__name__ = "BfdMultiplierTC"
_MplsOamBfdTemplateDetectMult_Object = MibTableColumn
mplsOamBfdTemplateDetectMult = _MplsOamBfdTemplateDetectMult_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 6),
    _MplsOamBfdTemplateDetectMult_Type()
)
mplsOamBfdTemplateDetectMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateDetectMult.setStatus("current")


class _MplsOamBfdTemplateReqMinRxInterval_Type(BfdIntervalTC):
    """Custom type mplsOamBfdTemplateReqMinRxInterval based on BfdIntervalTC"""
    defaultValue = 100000


_MplsOamBfdTemplateReqMinRxInterval_Type.__name__ = "BfdIntervalTC"
_MplsOamBfdTemplateReqMinRxInterval_Object = MibTableColumn
mplsOamBfdTemplateReqMinRxInterval = _MplsOamBfdTemplateReqMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 7),
    _MplsOamBfdTemplateReqMinRxInterval_Type()
)
mplsOamBfdTemplateReqMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateReqMinRxInterval.setStatus("current")
_MplsOamBfdTemplateCreateNewTemplate_Type = CommandString
_MplsOamBfdTemplateCreateNewTemplate_Object = MibTableColumn
mplsOamBfdTemplateCreateNewTemplate = _MplsOamBfdTemplateCreateNewTemplate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 8),
    _MplsOamBfdTemplateCreateNewTemplate_Type()
)
mplsOamBfdTemplateCreateNewTemplate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateCreateNewTemplate.setStatus("current")
_MplsOamBfdTemplateRowStatus_Type = RowStatus
_MplsOamBfdTemplateRowStatus_Object = MibTableColumn
mplsOamBfdTemplateRowStatus = _MplsOamBfdTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 2, 3, 2, 1, 9),
    _MplsOamBfdTemplateRowStatus_Type()
)
mplsOamBfdTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mplsOamBfdTemplateRowStatus.setStatus("current")

# Managed Objects groups

mplsIOamGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 1, 1)
)
mplsIOamGeneralGroupV1.setObjects(
      *(("LUM-MPLSOAM-MIB", "mplsOamGeneralLastChangeTime"),
        ("LUM-MPLSOAM-MIB", "mplsOamGeneralStateLastChangeTime"),
        ("LUM-MPLSOAM-MIB", "mplsOamGeneralmplsOamBfdSessTableSize"))
)
if mibBuilder.loadTexts:
    mplsIOamGeneralGroupV1.setStatus("current")

mplsBfdSessGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 1, 2)
)
mplsBfdSessGroupV1.setObjects(
      *(("LUM-MPLSOAM-MIB", "mplsOamBfdSessIndex"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessInternalReference"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessName"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessAdminStatus"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessState"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteState"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessDiag"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteDiag"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessNegotiatedTxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessNegotiatedRxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMonitoringPath"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMonitoringPathType"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMonitoringPathIndex"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessTemplate"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessTemplateIndex"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessSourceMepId"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessTargetMepId"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRcvTargetMepId"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMepNotConfigured"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessLocalNotConnected"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessLocalMisConnectivity"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessLocalTimerExpired"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteMisConnectivity"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteTimerExpired"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteAdminDown"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRowStatus"))
)
if mibBuilder.loadTexts:
    mplsBfdSessGroupV1.setStatus("deprecated")

mplsBfdTemplateGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 1, 3)
)
mplsBfdTemplateGroupV1.setObjects(
      *(("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateIndex"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateInternalReference"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateName"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateIdentifier"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateDesiredMinTxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateDetectMult"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateReqMinRxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateCreateNewTemplate"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdTemplateRowStatus"))
)
if mibBuilder.loadTexts:
    mplsBfdTemplateGroupV1.setStatus("current")

mplsBfdSessGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 1, 4)
)
mplsBfdSessGroupV2.setObjects(
      *(("LUM-MPLSOAM-MIB", "mplsOamBfdSessIndex"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessInternalReference"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessName"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessAdminStatus"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessState"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteState"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessDiag"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteDiag"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessNegotiatedTxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessNegotiatedRxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMonitoringPath"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMonitoringPathType"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMonitoringPathIndex"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessTemplate"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessTemplateIndex"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessSourceMepId"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessTargetMepId"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRcvTargetMepId"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessMepNotConfigured"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessLocalNotConnected"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessLocalMisConnectivity"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessLocalTimerExpired"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteMisConnectivity"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteTimerExpired"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRemoteAdminDown"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessRowStatus"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessDesiredMinTxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessReqMinRxInterval"),
        ("LUM-MPLSOAM-MIB", "mplsOamBfdSessTrafficClass"))
)
if mibBuilder.loadTexts:
    mplsBfdSessGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumMplsBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 2, 1)
)
lumMplsBasicComplV1.setObjects(
      *(("LUM-MPLSOAM-MIB", "mplsIOamGeneralGroupV1"),
        ("LUM-MPLSOAM-MIB", "mplsBfdSessGroupV1"),
        ("LUM-MPLSOAM-MIB", "mplsBfdTemplateGroupV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV1.setStatus(
        "deprecated"
    )

lumMplsBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 44, 1, 2, 2)
)
lumMplsBasicComplV2.setObjects(
      *(("LUM-MPLSOAM-MIB", "mplsIOamGeneralGroupV1"),
        ("LUM-MPLSOAM-MIB", "mplsBfdSessGroupV2"),
        ("LUM-MPLSOAM-MIB", "mplsBfdTemplateGroupV1"))
)
if mibBuilder.loadTexts:
    lumMplsBasicComplV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-MPLSOAM-MIB",
    **{"BfdSessStateTC": BfdSessStateTC,
       "BfdMultiplierTC": BfdMultiplierTC,
       "BfdIntervalTC": BfdIntervalTC,
       "BfdDiagTC": BfdDiagTC,
       "lumMplsOamMIBModule": lumMplsOamMIBModule,
       "lumMplsOamConfs": lumMplsOamConfs,
       "lumMplsOamGroups": lumMplsOamGroups,
       "mplsIOamGeneralGroupV1": mplsIOamGeneralGroupV1,
       "mplsBfdSessGroupV1": mplsBfdSessGroupV1,
       "mplsBfdTemplateGroupV1": mplsBfdTemplateGroupV1,
       "mplsBfdSessGroupV2": mplsBfdSessGroupV2,
       "lumMplsOamCompl": lumMplsOamCompl,
       "lumMplsBasicComplV1": lumMplsBasicComplV1,
       "lumMplsBasicComplV2": lumMplsBasicComplV2,
       "lumMplsOamMIBObjects": lumMplsOamMIBObjects,
       "mplsOamGeneral": mplsOamGeneral,
       "mplsOamGeneralLastChangeTime": mplsOamGeneralLastChangeTime,
       "mplsOamGeneralStateLastChangeTime": mplsOamGeneralStateLastChangeTime,
       "mplsOamGeneralmplsOamBfdSessTableSize": mplsOamGeneralmplsOamBfdSessTableSize,
       "mplsOamGeneralmplsOamBfdTemplateTableSize": mplsOamGeneralmplsOamBfdTemplateTableSize,
       "mplsOamBfdSess": mplsOamBfdSess,
       "mplsOamBfdSessTable": mplsOamBfdSessTable,
       "mplsOamBfdSessEntry": mplsOamBfdSessEntry,
       "mplsOamBfdSessIndex": mplsOamBfdSessIndex,
       "mplsOamBfdSessInternalReference": mplsOamBfdSessInternalReference,
       "mplsOamBfdSessName": mplsOamBfdSessName,
       "mplsOamBfdSessAdminStatus": mplsOamBfdSessAdminStatus,
       "mplsOamBfdSessState": mplsOamBfdSessState,
       "mplsOamBfdSessRemoteState": mplsOamBfdSessRemoteState,
       "mplsOamBfdSessDiag": mplsOamBfdSessDiag,
       "mplsOamBfdSessRemoteDiag": mplsOamBfdSessRemoteDiag,
       "mplsOamBfdSessNegotiatedTxInterval": mplsOamBfdSessNegotiatedTxInterval,
       "mplsOamBfdSessNegotiatedRxInterval": mplsOamBfdSessNegotiatedRxInterval,
       "mplsOamBfdSessMonitoringPath": mplsOamBfdSessMonitoringPath,
       "mplsOamBfdSessMonitoringPathType": mplsOamBfdSessMonitoringPathType,
       "mplsOamBfdSessMonitoringPathIndex": mplsOamBfdSessMonitoringPathIndex,
       "mplsOamBfdSessTemplate": mplsOamBfdSessTemplate,
       "mplsOamBfdSessTemplateIndex": mplsOamBfdSessTemplateIndex,
       "mplsOamBfdSessSourceMepId": mplsOamBfdSessSourceMepId,
       "mplsOamBfdSessTargetMepId": mplsOamBfdSessTargetMepId,
       "mplsOamBfdSessRcvTargetMepId": mplsOamBfdSessRcvTargetMepId,
       "mplsOamBfdSessMepNotConfigured": mplsOamBfdSessMepNotConfigured,
       "mplsOamBfdSessLocalNotConnected": mplsOamBfdSessLocalNotConnected,
       "mplsOamBfdSessLocalMisConnectivity": mplsOamBfdSessLocalMisConnectivity,
       "mplsOamBfdSessLocalTimerExpired": mplsOamBfdSessLocalTimerExpired,
       "mplsOamBfdSessRemoteMisConnectivity": mplsOamBfdSessRemoteMisConnectivity,
       "mplsOamBfdSessRemoteTimerExpired": mplsOamBfdSessRemoteTimerExpired,
       "mplsOamBfdSessRemoteAdminDown": mplsOamBfdSessRemoteAdminDown,
       "mplsOamBfdSessRowStatus": mplsOamBfdSessRowStatus,
       "mplsOamBfdSessDesiredMinTxInterval": mplsOamBfdSessDesiredMinTxInterval,
       "mplsOamBfdSessReqMinRxInterval": mplsOamBfdSessReqMinRxInterval,
       "mplsOamBfdSessTrafficClass": mplsOamBfdSessTrafficClass,
       "mplsOamBfdTemplate": mplsOamBfdTemplate,
       "mplsOamBfdTemplateTable": mplsOamBfdTemplateTable,
       "mplsOamBfdTemplateEntry": mplsOamBfdTemplateEntry,
       "mplsOamBfdTemplateIndex": mplsOamBfdTemplateIndex,
       "mplsOamBfdTemplateInternalReference": mplsOamBfdTemplateInternalReference,
       "mplsOamBfdTemplateName": mplsOamBfdTemplateName,
       "mplsOamBfdTemplateIdentifier": mplsOamBfdTemplateIdentifier,
       "mplsOamBfdTemplateDesiredMinTxInterval": mplsOamBfdTemplateDesiredMinTxInterval,
       "mplsOamBfdTemplateDetectMult": mplsOamBfdTemplateDetectMult,
       "mplsOamBfdTemplateReqMinRxInterval": mplsOamBfdTemplateReqMinRxInterval,
       "mplsOamBfdTemplateCreateNewTemplate": mplsOamBfdTemplateCreateNewTemplate,
       "mplsOamBfdTemplateRowStatus": mplsOamBfdTemplateRowStatus}
)
