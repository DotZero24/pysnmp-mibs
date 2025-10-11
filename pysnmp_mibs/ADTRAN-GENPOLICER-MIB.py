# SNMP MIB module (ADTRAN-GENPOLICER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENPOLICER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:31:02 2025
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

(adGenPolicer,
 adGenPolicerID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenPolicer",
    "adGenPolicerID")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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

adGenPolicerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 35, 1)
)
if mibBuilder.loadTexts:
    adGenPolicerMIB.setRevisions(
        ("2012-01-30 00:00",
         "2010-09-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPolicerEvents_ObjectIdentity = ObjectIdentity
adGenPolicerEvents = _AdGenPolicerEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 0)
)
_AdGenPolicerProvisioning_ObjectIdentity = ObjectIdentity
adGenPolicerProvisioning = _AdGenPolicerProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1)
)
_AdGenPolicerTable_Object = MibTable
adGenPolicerTable = _AdGenPolicerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPolicerTable.setStatus("current")
_AdGenPolicerEntry_Object = MibTableRow
adGenPolicerEntry = _AdGenPolicerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1)
)
adGenPolicerEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENPOLICER-MIB", "adGenPolicerName"),
)
if mibBuilder.loadTexts:
    adGenPolicerEntry.setStatus("current")


class _AdGenPolicerName_Type(DisplayString):
    """Custom type adGenPolicerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenPolicerName_Type.__name__ = "DisplayString"
_AdGenPolicerName_Object = MibTableColumn
adGenPolicerName = _AdGenPolicerName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 1),
    _AdGenPolicerName_Type()
)
adGenPolicerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPolicerName.setStatus("current")
_AdGenPolicerRowStatus_Type = RowStatus
_AdGenPolicerRowStatus_Object = MibTableColumn
adGenPolicerRowStatus = _AdGenPolicerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 2),
    _AdGenPolicerRowStatus_Type()
)
adGenPolicerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerRowStatus.setStatus("current")
_AdGenPolicerStatus_Type = DisplayString
_AdGenPolicerStatus_Object = MibTableColumn
adGenPolicerStatus = _AdGenPolicerStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 3),
    _AdGenPolicerStatus_Type()
)
adGenPolicerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerStatus.setStatus("current")


class _AdGenPolicerOperStatus_Type(Integer32):
    """Custom type adGenPolicerOperStatus based on Integer32"""
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


_AdGenPolicerOperStatus_Type.__name__ = "Integer32"
_AdGenPolicerOperStatus_Object = MibTableColumn
adGenPolicerOperStatus = _AdGenPolicerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 4),
    _AdGenPolicerOperStatus_Type()
)
adGenPolicerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerOperStatus.setStatus("current")
_AdGenPolicerCIR_Type = Integer32
_AdGenPolicerCIR_Object = MibTableColumn
adGenPolicerCIR = _AdGenPolicerCIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 5),
    _AdGenPolicerCIR_Type()
)
adGenPolicerCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerCIR.setStatus("current")
_AdGenPolicerCBS_Type = Integer32
_AdGenPolicerCBS_Object = MibTableColumn
adGenPolicerCBS = _AdGenPolicerCBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 6),
    _AdGenPolicerCBS_Type()
)
adGenPolicerCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerCBS.setStatus("current")
_AdGenPolicerEIR_Type = Integer32
_AdGenPolicerEIR_Object = MibTableColumn
adGenPolicerEIR = _AdGenPolicerEIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 7),
    _AdGenPolicerEIR_Type()
)
adGenPolicerEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerEIR.setStatus("current")


class _AdGenPolicerEIRNoLimit_Type(TruthValue):
    """Custom type adGenPolicerEIRNoLimit based on TruthValue"""
    defaultValue = 2


_AdGenPolicerEIRNoLimit_Type.__name__ = "TruthValue"
_AdGenPolicerEIRNoLimit_Object = MibTableColumn
adGenPolicerEIRNoLimit = _AdGenPolicerEIRNoLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 8),
    _AdGenPolicerEIRNoLimit_Type()
)
adGenPolicerEIRNoLimit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerEIRNoLimit.setStatus("current")
_AdGenPolicerEBS_Type = Integer32
_AdGenPolicerEBS_Object = MibTableColumn
adGenPolicerEBS = _AdGenPolicerEBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 9),
    _AdGenPolicerEBS_Type()
)
adGenPolicerEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerEBS.setStatus("current")


class _AdGenPolicerMode_Type(Integer32):
    """Custom type adGenPolicerMode based on Integer32"""
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
        *(("unspecified", 1),
          ("perUNI", 2),
          ("perInterface", 3),
          ("perEVC", 4),
          ("perMEVC", 5),
          ("perEVCMap", 6))
    )


_AdGenPolicerMode_Type.__name__ = "Integer32"
_AdGenPolicerMode_Object = MibTableColumn
adGenPolicerMode = _AdGenPolicerMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 10),
    _AdGenPolicerMode_Type()
)
adGenPolicerMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerMode.setStatus("current")
_AdGenPolicerUNIPort_Type = InterfaceIndexOrZero
_AdGenPolicerUNIPort_Object = MibTableColumn
adGenPolicerUNIPort = _AdGenPolicerUNIPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 11),
    _AdGenPolicerUNIPort_Type()
)
adGenPolicerUNIPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerUNIPort.setStatus("current")
_AdGenPolicerEVCName_Type = DisplayString
_AdGenPolicerEVCName_Object = MibTableColumn
adGenPolicerEVCName = _AdGenPolicerEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 12),
    _AdGenPolicerEVCName_Type()
)
adGenPolicerEVCName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerEVCName.setStatus("current")
_AdGenPolicerMEVCName_Type = DisplayString
_AdGenPolicerMEVCName_Object = MibTableColumn
adGenPolicerMEVCName = _AdGenPolicerMEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 13),
    _AdGenPolicerMEVCName_Type()
)
adGenPolicerMEVCName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerMEVCName.setStatus("current")
_AdGenPolicerCEVlanPriority_Type = DisplayString
_AdGenPolicerCEVlanPriority_Object = MibTableColumn
adGenPolicerCEVlanPriority = _AdGenPolicerCEVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 14),
    _AdGenPolicerCEVlanPriority_Type()
)
adGenPolicerCEVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerCEVlanPriority.setStatus("current")
_AdGenPolicerAddEvcMap_Type = DisplayString
_AdGenPolicerAddEvcMap_Object = MibTableColumn
adGenPolicerAddEvcMap = _AdGenPolicerAddEvcMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 15),
    _AdGenPolicerAddEvcMap_Type()
)
adGenPolicerAddEvcMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerAddEvcMap.setStatus("current")
_AdGenPolicerRemoveEvcMap_Type = DisplayString
_AdGenPolicerRemoveEvcMap_Object = MibTableColumn
adGenPolicerRemoveEvcMap = _AdGenPolicerRemoveEvcMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 16),
    _AdGenPolicerRemoveEvcMap_Type()
)
adGenPolicerRemoveEvcMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenPolicerRemoveEvcMap.setStatus("current")
_AdGenPolicerLastError_Type = DisplayString
_AdGenPolicerLastError_Object = MibTableColumn
adGenPolicerLastError = _AdGenPolicerLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 1, 1, 17),
    _AdGenPolicerLastError_Type()
)
adGenPolicerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerLastError.setStatus("current")
_AdGenPolicerThresholds_ObjectIdentity = ObjectIdentity
adGenPolicerThresholds = _AdGenPolicerThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2)
)
_AdGenPolicer15MinThresholdTable_Object = MibTable
adGenPolicer15MinThresholdTable = _AdGenPolicer15MinThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPolicer15MinThresholdTable.setStatus("current")
_AdGenPolicer15MinThresholdEntry_Object = MibTableRow
adGenPolicer15MinThresholdEntry = _AdGenPolicer15MinThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 1, 1)
)
adGenPolicer15MinThresholdEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerName"),
)
if mibBuilder.loadTexts:
    adGenPolicer15MinThresholdEntry.setStatus("current")
_AdGenPolicer15MinThresholdDiscardsGreenFrames_Type = Integer32
_AdGenPolicer15MinThresholdDiscardsGreenFrames_Object = MibTableColumn
adGenPolicer15MinThresholdDiscardsGreenFrames = _AdGenPolicer15MinThresholdDiscardsGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 1, 1, 1),
    _AdGenPolicer15MinThresholdDiscardsGreenFrames_Type()
)
adGenPolicer15MinThresholdDiscardsGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer15MinThresholdDiscardsGreenFrames.setStatus("current")
_AdGenPolicer15MinThresholdTotalGreenFrames_Type = Integer32
_AdGenPolicer15MinThresholdTotalGreenFrames_Object = MibTableColumn
adGenPolicer15MinThresholdTotalGreenFrames = _AdGenPolicer15MinThresholdTotalGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 1, 1, 2),
    _AdGenPolicer15MinThresholdTotalGreenFrames_Type()
)
adGenPolicer15MinThresholdTotalGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer15MinThresholdTotalGreenFrames.setStatus("current")
_AdGenPolicer15MinThresholdDiscardsYellowFrames_Type = Integer32
_AdGenPolicer15MinThresholdDiscardsYellowFrames_Object = MibTableColumn
adGenPolicer15MinThresholdDiscardsYellowFrames = _AdGenPolicer15MinThresholdDiscardsYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 1, 1, 3),
    _AdGenPolicer15MinThresholdDiscardsYellowFrames_Type()
)
adGenPolicer15MinThresholdDiscardsYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer15MinThresholdDiscardsYellowFrames.setStatus("current")
_AdGenPolicer15MinThresholdTotalYellowFrames_Type = Integer32
_AdGenPolicer15MinThresholdTotalYellowFrames_Object = MibTableColumn
adGenPolicer15MinThresholdTotalYellowFrames = _AdGenPolicer15MinThresholdTotalYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 1, 1, 4),
    _AdGenPolicer15MinThresholdTotalYellowFrames_Type()
)
adGenPolicer15MinThresholdTotalYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer15MinThresholdTotalYellowFrames.setStatus("current")
_AdGenPolicer15MinThresholdTotalRedFrames_Type = Integer32
_AdGenPolicer15MinThresholdTotalRedFrames_Object = MibTableColumn
adGenPolicer15MinThresholdTotalRedFrames = _AdGenPolicer15MinThresholdTotalRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 1, 1, 5),
    _AdGenPolicer15MinThresholdTotalRedFrames_Type()
)
adGenPolicer15MinThresholdTotalRedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer15MinThresholdTotalRedFrames.setStatus("current")
_AdGenPolicer24HrThresholdTable_Object = MibTable
adGenPolicer24HrThresholdTable = _AdGenPolicer24HrThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 2)
)
if mibBuilder.loadTexts:
    adGenPolicer24HrThresholdTable.setStatus("current")
_AdGenPolicer24HrThresholdEntry_Object = MibTableRow
adGenPolicer24HrThresholdEntry = _AdGenPolicer24HrThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 2, 1)
)
adGenPolicer24HrThresholdEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerName"),
)
if mibBuilder.loadTexts:
    adGenPolicer24HrThresholdEntry.setStatus("current")
_AdGenPolicer24HrThresholdDiscardsGreenFrames_Type = Integer32
_AdGenPolicer24HrThresholdDiscardsGreenFrames_Object = MibTableColumn
adGenPolicer24HrThresholdDiscardsGreenFrames = _AdGenPolicer24HrThresholdDiscardsGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 2, 1, 1),
    _AdGenPolicer24HrThresholdDiscardsGreenFrames_Type()
)
adGenPolicer24HrThresholdDiscardsGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer24HrThresholdDiscardsGreenFrames.setStatus("current")
_AdGenPolicer24HrThresholdTotalGreenFrames_Type = Integer32
_AdGenPolicer24HrThresholdTotalGreenFrames_Object = MibTableColumn
adGenPolicer24HrThresholdTotalGreenFrames = _AdGenPolicer24HrThresholdTotalGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 2, 1, 2),
    _AdGenPolicer24HrThresholdTotalGreenFrames_Type()
)
adGenPolicer24HrThresholdTotalGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer24HrThresholdTotalGreenFrames.setStatus("current")
_AdGenPolicer24HrThresholdDiscardsYellowFrames_Type = Integer32
_AdGenPolicer24HrThresholdDiscardsYellowFrames_Object = MibTableColumn
adGenPolicer24HrThresholdDiscardsYellowFrames = _AdGenPolicer24HrThresholdDiscardsYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 2, 1, 3),
    _AdGenPolicer24HrThresholdDiscardsYellowFrames_Type()
)
adGenPolicer24HrThresholdDiscardsYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer24HrThresholdDiscardsYellowFrames.setStatus("current")
_AdGenPolicer24HrThresholdTotalYellowFrames_Type = Integer32
_AdGenPolicer24HrThresholdTotalYellowFrames_Object = MibTableColumn
adGenPolicer24HrThresholdTotalYellowFrames = _AdGenPolicer24HrThresholdTotalYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 2, 1, 4),
    _AdGenPolicer24HrThresholdTotalYellowFrames_Type()
)
adGenPolicer24HrThresholdTotalYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer24HrThresholdTotalYellowFrames.setStatus("current")
_AdGenPolicer24HrThresholdTotalRedFrames_Type = Integer32
_AdGenPolicer24HrThresholdTotalRedFrames_Object = MibTableColumn
adGenPolicer24HrThresholdTotalRedFrames = _AdGenPolicer24HrThresholdTotalRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 2, 2, 1, 5),
    _AdGenPolicer24HrThresholdTotalRedFrames_Type()
)
adGenPolicer24HrThresholdTotalRedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPolicer24HrThresholdTotalRedFrames.setStatus("current")
_AdGenPolicerErrorTable_Object = MibTable
adGenPolicerErrorTable = _AdGenPolicerErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 3)
)
if mibBuilder.loadTexts:
    adGenPolicerErrorTable.setStatus("current")
_AdGenPolicerErrorEntry_Object = MibTableRow
adGenPolicerErrorEntry = _AdGenPolicerErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 3, 1)
)
adGenPolicerErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenPolicerErrorEntry.setStatus("current")
_AdGenPolicerError_Type = DisplayString
_AdGenPolicerError_Object = MibTableColumn
adGenPolicerError = _AdGenPolicerError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 3, 1, 1),
    _AdGenPolicerError_Type()
)
adGenPolicerError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerError.setStatus("current")
_AdGenPolicerLookupTable_Object = MibTable
adGenPolicerLookupTable = _AdGenPolicerLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4)
)
if mibBuilder.loadTexts:
    adGenPolicerLookupTable.setStatus("current")
_AdGenPolicerLookupEntry_Object = MibTableRow
adGenPolicerLookupEntry = _AdGenPolicerLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4, 1)
)
adGenPolicerLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerName"),
)
if mibBuilder.loadTexts:
    adGenPolicerLookupEntry.setStatus("current")
_AdGenPolicerActualCIR_Type = Integer32
_AdGenPolicerActualCIR_Object = MibTableColumn
adGenPolicerActualCIR = _AdGenPolicerActualCIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4, 1, 1),
    _AdGenPolicerActualCIR_Type()
)
adGenPolicerActualCIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerActualCIR.setStatus("current")
_AdGenPolicerActualCBS_Type = Integer32
_AdGenPolicerActualCBS_Object = MibTableColumn
adGenPolicerActualCBS = _AdGenPolicerActualCBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4, 1, 2),
    _AdGenPolicerActualCBS_Type()
)
adGenPolicerActualCBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerActualCBS.setStatus("current")
_AdGenPolicerActualEIR_Type = Integer32
_AdGenPolicerActualEIR_Object = MibTableColumn
adGenPolicerActualEIR = _AdGenPolicerActualEIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4, 1, 3),
    _AdGenPolicerActualEIR_Type()
)
adGenPolicerActualEIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerActualEIR.setStatus("current")
_AdGenPolicerActualEBS_Type = Integer32
_AdGenPolicerActualEBS_Object = MibTableColumn
adGenPolicerActualEBS = _AdGenPolicerActualEBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4, 1, 4),
    _AdGenPolicerActualEBS_Type()
)
adGenPolicerActualEBS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerActualEBS.setStatus("current")
_AdGenPolicerProvNumberOfEVCMaps_Type = Integer32
_AdGenPolicerProvNumberOfEVCMaps_Object = MibTableColumn
adGenPolicerProvNumberOfEVCMaps = _AdGenPolicerProvNumberOfEVCMaps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4, 1, 5),
    _AdGenPolicerProvNumberOfEVCMaps_Type()
)
adGenPolicerProvNumberOfEVCMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerProvNumberOfEVCMaps.setStatus("current")
_AdGenPolicerQualifiedNumberOfEVCMaps_Type = Integer32
_AdGenPolicerQualifiedNumberOfEVCMaps_Object = MibTableColumn
adGenPolicerQualifiedNumberOfEVCMaps = _AdGenPolicerQualifiedNumberOfEVCMaps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 4, 1, 6),
    _AdGenPolicerQualifiedNumberOfEVCMaps_Type()
)
adGenPolicerQualifiedNumberOfEVCMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerQualifiedNumberOfEVCMaps.setStatus("current")
_AdGenPolicerEVCMapLookupTable_Object = MibTable
adGenPolicerEVCMapLookupTable = _AdGenPolicerEVCMapLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 5)
)
if mibBuilder.loadTexts:
    adGenPolicerEVCMapLookupTable.setStatus("current")
_AdGenPolicerEVCMapLookupEntry_Object = MibTableRow
adGenPolicerEVCMapLookupEntry = _AdGenPolicerEVCMapLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 5, 1)
)
adGenPolicerEVCMapLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerFixedLengthName"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerEVCMapLookupIndex"),
)
if mibBuilder.loadTexts:
    adGenPolicerEVCMapLookupEntry.setStatus("current")


class _AdGenPolicerFixedLengthName_Type(OctetString):
    """Custom type adGenPolicerFixedLengthName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_AdGenPolicerFixedLengthName_Type.__name__ = "OctetString"
_AdGenPolicerFixedLengthName_Object = MibTableColumn
adGenPolicerFixedLengthName = _AdGenPolicerFixedLengthName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 5, 1, 1),
    _AdGenPolicerFixedLengthName_Type()
)
adGenPolicerFixedLengthName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPolicerFixedLengthName.setStatus("current")
_AdGenPolicerEVCMapLookupIndex_Type = Integer32
_AdGenPolicerEVCMapLookupIndex_Object = MibTableColumn
adGenPolicerEVCMapLookupIndex = _AdGenPolicerEVCMapLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 5, 1, 2),
    _AdGenPolicerEVCMapLookupIndex_Type()
)
adGenPolicerEVCMapLookupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPolicerEVCMapLookupIndex.setStatus("current")
_AdGenPolicerEVCMapLookupName_Type = DisplayString
_AdGenPolicerEVCMapLookupName_Object = MibTableColumn
adGenPolicerEVCMapLookupName = _AdGenPolicerEVCMapLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 5, 1, 3),
    _AdGenPolicerEVCMapLookupName_Type()
)
adGenPolicerEVCMapLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerEVCMapLookupName.setStatus("current")
_AdGenPolicerQualifiedEVCMapLookupTable_Object = MibTable
adGenPolicerQualifiedEVCMapLookupTable = _AdGenPolicerQualifiedEVCMapLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 6)
)
if mibBuilder.loadTexts:
    adGenPolicerQualifiedEVCMapLookupTable.setStatus("current")
_AdGenPolicerQualifiedEVCMapLookupEntry_Object = MibTableRow
adGenPolicerQualifiedEVCMapLookupEntry = _AdGenPolicerQualifiedEVCMapLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 6, 1)
)
adGenPolicerQualifiedEVCMapLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerFixedLengthName"),
    (0, "ADTRAN-GENPOLICER-MIB", "adGenPolicerQualifiedEVCMapLookupIndex"),
)
if mibBuilder.loadTexts:
    adGenPolicerQualifiedEVCMapLookupEntry.setStatus("current")
_AdGenPolicerQualifiedEVCMapLookupIndex_Type = Integer32
_AdGenPolicerQualifiedEVCMapLookupIndex_Object = MibTableColumn
adGenPolicerQualifiedEVCMapLookupIndex = _AdGenPolicerQualifiedEVCMapLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 6, 1, 1),
    _AdGenPolicerQualifiedEVCMapLookupIndex_Type()
)
adGenPolicerQualifiedEVCMapLookupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenPolicerQualifiedEVCMapLookupIndex.setStatus("current")
_AdGenPolicerQualifiedEVCMapLookupName_Type = DisplayString
_AdGenPolicerQualifiedEVCMapLookupName_Object = MibTableColumn
adGenPolicerQualifiedEVCMapLookupName = _AdGenPolicerQualifiedEVCMapLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 6, 1, 2),
    _AdGenPolicerQualifiedEVCMapLookupName_Type()
)
adGenPolicerQualifiedEVCMapLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerQualifiedEVCMapLookupName.setStatus("current")


class _AdGenPolicerQualifiedEVCMapLookupStatus_Type(Integer32):
    """Custom type adGenPolicerQualifiedEVCMapLookupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("notApplied", 2),
          ("applied", 3))
    )


_AdGenPolicerQualifiedEVCMapLookupStatus_Type.__name__ = "Integer32"
_AdGenPolicerQualifiedEVCMapLookupStatus_Object = MibTableColumn
adGenPolicerQualifiedEVCMapLookupStatus = _AdGenPolicerQualifiedEVCMapLookupStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 1, 6, 1, 3),
    _AdGenPolicerQualifiedEVCMapLookupStatus_Type()
)
adGenPolicerQualifiedEVCMapLookupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenPolicerQualifiedEVCMapLookupStatus.setStatus("current")
_AdGenPolicerAlarm_ObjectIdentity = ObjectIdentity
adGenPolicerAlarm = _AdGenPolicerAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100)
)
_AdGenPolicerAlarmEvents_ObjectIdentity = ObjectIdentity
adGenPolicerAlarmEvents = _AdGenPolicerAlarmEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100, 0)
)

# Managed Objects groups


# Notification objects

adGenPolicer15MinThresGreenTotalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100, 0, 1)
)
adGenPolicer15MinThresGreenTotalAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPOLICER-MIB", "adGenPolicer15MinThresholdTotalGreenFrames"))
)
if mibBuilder.loadTexts:
    adGenPolicer15MinThresGreenTotalAlarm.setStatus(
        "current"
    )

adGenPolicer15MinThresYellowTotalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100, 0, 3)
)
adGenPolicer15MinThresYellowTotalAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPOLICER-MIB", "adGenPolicer15MinThresholdTotalYellowFrames"))
)
if mibBuilder.loadTexts:
    adGenPolicer15MinThresYellowTotalAlarm.setStatus(
        "current"
    )

adGenPolicer15MinThresRedTotalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100, 0, 5)
)
adGenPolicer15MinThresRedTotalAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPOLICER-MIB", "adGenPolicer15MinThresholdTotalRedFrames"))
)
if mibBuilder.loadTexts:
    adGenPolicer15MinThresRedTotalAlarm.setStatus(
        "current"
    )

adGenPolicer24HrThresGreenTotalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100, 0, 7)
)
adGenPolicer24HrThresGreenTotalAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPOLICER-MIB", "adGenPolicer24HrThresholdTotalGreenFrames"))
)
if mibBuilder.loadTexts:
    adGenPolicer24HrThresGreenTotalAlarm.setStatus(
        "current"
    )

adGenPolicer24HrThresYellowTotalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100, 0, 9)
)
adGenPolicer24HrThresYellowTotalAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPOLICER-MIB", "adGenPolicer24HrThresholdTotalYellowFrames"))
)
if mibBuilder.loadTexts:
    adGenPolicer24HrThresYellowTotalAlarm.setStatus(
        "current"
    )

adGenPolicer24HrThresRedTotalAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 35, 100, 0, 11)
)
adGenPolicer24HrThresRedTotalAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPOLICER-MIB", "adGenPolicer24HrThresholdTotalRedFrames"))
)
if mibBuilder.loadTexts:
    adGenPolicer24HrThresRedTotalAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENPOLICER-MIB",
    **{"adGenPolicerEvents": adGenPolicerEvents,
       "adGenPolicerProvisioning": adGenPolicerProvisioning,
       "adGenPolicerTable": adGenPolicerTable,
       "adGenPolicerEntry": adGenPolicerEntry,
       "adGenPolicerName": adGenPolicerName,
       "adGenPolicerRowStatus": adGenPolicerRowStatus,
       "adGenPolicerStatus": adGenPolicerStatus,
       "adGenPolicerOperStatus": adGenPolicerOperStatus,
       "adGenPolicerCIR": adGenPolicerCIR,
       "adGenPolicerCBS": adGenPolicerCBS,
       "adGenPolicerEIR": adGenPolicerEIR,
       "adGenPolicerEIRNoLimit": adGenPolicerEIRNoLimit,
       "adGenPolicerEBS": adGenPolicerEBS,
       "adGenPolicerMode": adGenPolicerMode,
       "adGenPolicerUNIPort": adGenPolicerUNIPort,
       "adGenPolicerEVCName": adGenPolicerEVCName,
       "adGenPolicerMEVCName": adGenPolicerMEVCName,
       "adGenPolicerCEVlanPriority": adGenPolicerCEVlanPriority,
       "adGenPolicerAddEvcMap": adGenPolicerAddEvcMap,
       "adGenPolicerRemoveEvcMap": adGenPolicerRemoveEvcMap,
       "adGenPolicerLastError": adGenPolicerLastError,
       "adGenPolicerThresholds": adGenPolicerThresholds,
       "adGenPolicer15MinThresholdTable": adGenPolicer15MinThresholdTable,
       "adGenPolicer15MinThresholdEntry": adGenPolicer15MinThresholdEntry,
       "adGenPolicer15MinThresholdDiscardsGreenFrames": adGenPolicer15MinThresholdDiscardsGreenFrames,
       "adGenPolicer15MinThresholdTotalGreenFrames": adGenPolicer15MinThresholdTotalGreenFrames,
       "adGenPolicer15MinThresholdDiscardsYellowFrames": adGenPolicer15MinThresholdDiscardsYellowFrames,
       "adGenPolicer15MinThresholdTotalYellowFrames": adGenPolicer15MinThresholdTotalYellowFrames,
       "adGenPolicer15MinThresholdTotalRedFrames": adGenPolicer15MinThresholdTotalRedFrames,
       "adGenPolicer24HrThresholdTable": adGenPolicer24HrThresholdTable,
       "adGenPolicer24HrThresholdEntry": adGenPolicer24HrThresholdEntry,
       "adGenPolicer24HrThresholdDiscardsGreenFrames": adGenPolicer24HrThresholdDiscardsGreenFrames,
       "adGenPolicer24HrThresholdTotalGreenFrames": adGenPolicer24HrThresholdTotalGreenFrames,
       "adGenPolicer24HrThresholdDiscardsYellowFrames": adGenPolicer24HrThresholdDiscardsYellowFrames,
       "adGenPolicer24HrThresholdTotalYellowFrames": adGenPolicer24HrThresholdTotalYellowFrames,
       "adGenPolicer24HrThresholdTotalRedFrames": adGenPolicer24HrThresholdTotalRedFrames,
       "adGenPolicerErrorTable": adGenPolicerErrorTable,
       "adGenPolicerErrorEntry": adGenPolicerErrorEntry,
       "adGenPolicerError": adGenPolicerError,
       "adGenPolicerLookupTable": adGenPolicerLookupTable,
       "adGenPolicerLookupEntry": adGenPolicerLookupEntry,
       "adGenPolicerActualCIR": adGenPolicerActualCIR,
       "adGenPolicerActualCBS": adGenPolicerActualCBS,
       "adGenPolicerActualEIR": adGenPolicerActualEIR,
       "adGenPolicerActualEBS": adGenPolicerActualEBS,
       "adGenPolicerProvNumberOfEVCMaps": adGenPolicerProvNumberOfEVCMaps,
       "adGenPolicerQualifiedNumberOfEVCMaps": adGenPolicerQualifiedNumberOfEVCMaps,
       "adGenPolicerEVCMapLookupTable": adGenPolicerEVCMapLookupTable,
       "adGenPolicerEVCMapLookupEntry": adGenPolicerEVCMapLookupEntry,
       "adGenPolicerFixedLengthName": adGenPolicerFixedLengthName,
       "adGenPolicerEVCMapLookupIndex": adGenPolicerEVCMapLookupIndex,
       "adGenPolicerEVCMapLookupName": adGenPolicerEVCMapLookupName,
       "adGenPolicerQualifiedEVCMapLookupTable": adGenPolicerQualifiedEVCMapLookupTable,
       "adGenPolicerQualifiedEVCMapLookupEntry": adGenPolicerQualifiedEVCMapLookupEntry,
       "adGenPolicerQualifiedEVCMapLookupIndex": adGenPolicerQualifiedEVCMapLookupIndex,
       "adGenPolicerQualifiedEVCMapLookupName": adGenPolicerQualifiedEVCMapLookupName,
       "adGenPolicerQualifiedEVCMapLookupStatus": adGenPolicerQualifiedEVCMapLookupStatus,
       "adGenPolicerAlarm": adGenPolicerAlarm,
       "adGenPolicerAlarmEvents": adGenPolicerAlarmEvents,
       "adGenPolicer15MinThresGreenTotalAlarm": adGenPolicer15MinThresGreenTotalAlarm,
       "adGenPolicer15MinThresYellowTotalAlarm": adGenPolicer15MinThresYellowTotalAlarm,
       "adGenPolicer15MinThresRedTotalAlarm": adGenPolicer15MinThresRedTotalAlarm,
       "adGenPolicer24HrThresGreenTotalAlarm": adGenPolicer24HrThresGreenTotalAlarm,
       "adGenPolicer24HrThresYellowTotalAlarm": adGenPolicer24HrThresYellowTotalAlarm,
       "adGenPolicer24HrThresRedTotalAlarm": adGenPolicer24HrThresRedTotalAlarm,
       "adGenPolicerMIB": adGenPolicerMIB}
)
