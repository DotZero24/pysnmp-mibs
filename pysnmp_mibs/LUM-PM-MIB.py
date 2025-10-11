# SNMP MIB module (LUM-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-PM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:34 2025
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
 lumPmMIB) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumModules",
    "lumPmMIB")

(BoardOrInterfaceAdminStatus,
 BoardOrInterfaceOperStatus,
 CommandString,
 FaultStatus,
 MgmtNameString,
 ObjectProperty,
 OnOff,
 PortNumber,
 SlotNumber,
 SubrackNumber) = mibBuilder.importSymbols(
    "LUM-TC",
    "BoardOrInterfaceAdminStatus",
    "BoardOrInterfaceOperStatus",
    "CommandString",
    "FaultStatus",
    "MgmtNameString",
    "ObjectProperty",
    "OnOff",
    "PortNumber",
    "SlotNumber",
    "SubrackNumber")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

lumPmMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 16)
)
if mibBuilder.loadTexts:
    lumPmMIBModule.setRevisions(
        ("2018-12-21 00:00",
         "2017-09-01 00:00",
         "2017-06-15 00:00",
         "2016-05-24 00:00",
         "2016-04-29 00:00",
         "2016-01-11 00:00",
         "2015-12-03 00:00",
         "2014-05-16 00:00",
         "2013-03-27 00:00",
         "2011-10-03 00:00",
         "2011-03-01 00:00",
         "2008-03-18 00:00",
         "2007-09-17 00:00",
         "2005-03-09 00:00",
         "2004-10-27 00:00",
         "2004-06-02 00:00",
         "2002-09-23 00:00",
         "2002-08-09 00:00",
         "2002-05-31 00:00",
         "2002-05-17 00:00",
         "2002-01-17 00:00",
         "2002-01-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PmInterval15mNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )



class PmInterval24hNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )



# MIB Managed Objects in the order of their OIDs

_LumPmConfs_ObjectIdentity = ObjectIdentity
lumPmConfs = _LumPmConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1)
)
_LumPmGroups_ObjectIdentity = ObjectIdentity
lumPmGroups = _LumPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1)
)
_LumPmCompl_ObjectIdentity = ObjectIdentity
lumPmCompl = _LumPmCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2)
)
_LumPmMIBObjects_ObjectIdentity = ObjectIdentity
lumPmMIBObjects = _LumPmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2)
)
_PmGeneral_ObjectIdentity = ObjectIdentity
pmGeneral = _PmGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1)
)
_PmGeneralLastChangeTime_Type = DateAndTime
_PmGeneralLastChangeTime_Object = MibScalar
pmGeneralLastChangeTime = _PmGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 1),
    _PmGeneralLastChangeTime_Type()
)
pmGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralLastChangeTime.setStatus("current")
_PmGeneralStateLastChangeTime_Type = DateAndTime
_PmGeneralStateLastChangeTime_Object = MibScalar
pmGeneralStateLastChangeTime = _PmGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 2),
    _PmGeneralStateLastChangeTime_Type()
)
pmGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralStateLastChangeTime.setStatus("current")
_PmGeneralPmIfTableSize_Type = Unsigned32
_PmGeneralPmIfTableSize_Object = MibScalar
pmGeneralPmIfTableSize = _PmGeneralPmIfTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 3),
    _PmGeneralPmIfTableSize_Type()
)
pmGeneralPmIfTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralPmIfTableSize.setStatus("current")
_PmGeneralPmEthTdTableSize_Type = Unsigned32
_PmGeneralPmEthTdTableSize_Object = MibScalar
pmGeneralPmEthTdTableSize = _PmGeneralPmEthTdTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 4),
    _PmGeneralPmEthTdTableSize_Type()
)
pmGeneralPmEthTdTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralPmEthTdTableSize.setStatus("current")
_PmGeneralPmEthTmTableSize_Type = Unsigned32
_PmGeneralPmEthTmTableSize_Object = MibScalar
pmGeneralPmEthTmTableSize = _PmGeneralPmEthTmTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 5),
    _PmGeneralPmEthTmTableSize_Type()
)
pmGeneralPmEthTmTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralPmEthTmTableSize.setStatus("obsolete")
_PmGeneralPmEthOamTableSize_Type = Unsigned32
_PmGeneralPmEthOamTableSize_Object = MibScalar
pmGeneralPmEthOamTableSize = _PmGeneralPmEthOamTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 6),
    _PmGeneralPmEthOamTableSize_Type()
)
pmGeneralPmEthOamTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralPmEthOamTableSize.setStatus("obsolete")
_PmGeneralPmEthDropTableSize_Type = Unsigned32
_PmGeneralPmEthDropTableSize_Object = MibScalar
pmGeneralPmEthDropTableSize = _PmGeneralPmEthDropTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 7),
    _PmGeneralPmEthDropTableSize_Type()
)
pmGeneralPmEthDropTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralPmEthDropTableSize.setStatus("current")
_PmGeneralPmEthClassificationTableSize_Type = Unsigned32
_PmGeneralPmEthClassificationTableSize_Object = MibScalar
pmGeneralPmEthClassificationTableSize = _PmGeneralPmEthClassificationTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 8),
    _PmGeneralPmEthClassificationTableSize_Type()
)
pmGeneralPmEthClassificationTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralPmEthClassificationTableSize.setStatus("current")
_PmGeneralPmMpoLanesTableSize_Type = Unsigned32
_PmGeneralPmMpoLanesTableSize_Object = MibScalar
pmGeneralPmMpoLanesTableSize = _PmGeneralPmMpoLanesTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 1, 9),
    _PmGeneralPmMpoLanesTableSize_Type()
)
pmGeneralPmMpoLanesTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmGeneralPmMpoLanesTableSize.setStatus("current")
_PmInterval_ObjectIdentity = ObjectIdentity
pmInterval = _PmInterval_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2)
)
_PmIntervalTable_Object = MibTable
pmIntervalTable = _PmIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1)
)
if mibBuilder.loadTexts:
    pmIntervalTable.setStatus("deprecated")
_PmIntervalEntry_Object = MibTableRow
pmIntervalEntry = _PmIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1)
)
pmIntervalEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmIntervalNumber"),
    (0, "LUM-PM-MIB", "pmIntervalSubrack"),
    (0, "LUM-PM-MIB", "pmIntervalSlot"),
    (0, "LUM-PM-MIB", "pmIntervalPort"),
)
if mibBuilder.loadTexts:
    pmIntervalEntry.setStatus("deprecated")
_PmIntervalSubrack_Type = SubrackNumber
_PmIntervalSubrack_Object = MibTableColumn
pmIntervalSubrack = _PmIntervalSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 1),
    _PmIntervalSubrack_Type()
)
pmIntervalSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalSubrack.setStatus("current")
_PmIntervalSlot_Type = SlotNumber
_PmIntervalSlot_Object = MibTableColumn
pmIntervalSlot = _PmIntervalSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 2),
    _PmIntervalSlot_Type()
)
pmIntervalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalSlot.setStatus("current")
_PmIntervalPort_Type = PortNumber
_PmIntervalPort_Object = MibTableColumn
pmIntervalPort = _PmIntervalPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 3),
    _PmIntervalPort_Type()
)
pmIntervalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalPort.setStatus("current")


class _PmIntervalNumber_Type(Unsigned32):
    """Custom type pmIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_PmIntervalNumber_Type.__name__ = "Unsigned32"
_PmIntervalNumber_Object = MibTableColumn
pmIntervalNumber = _PmIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 4),
    _PmIntervalNumber_Type()
)
pmIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalNumber.setStatus("current")
_PmIntervalIsSuspect_Type = TruthValue
_PmIntervalIsSuspect_Object = MibTableColumn
pmIntervalIsSuspect = _PmIntervalIsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 5),
    _PmIntervalIsSuspect_Type()
)
pmIntervalIsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalIsSuspect.setStatus("current")
_PmIntervalRxES_Type = Gauge32
_PmIntervalRxES_Object = MibTableColumn
pmIntervalRxES = _PmIntervalRxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 6),
    _PmIntervalRxES_Type()
)
pmIntervalRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxES.setStatus("current")
_PmIntervalRxSES_Type = Gauge32
_PmIntervalRxSES_Object = MibTableColumn
pmIntervalRxSES = _PmIntervalRxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 7),
    _PmIntervalRxSES_Type()
)
pmIntervalRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxSES.setStatus("current")
_PmIntervalRxBBE_Type = Gauge32
_PmIntervalRxBBE_Object = MibTableColumn
pmIntervalRxBBE = _PmIntervalRxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 8),
    _PmIntervalRxBBE_Type()
)
pmIntervalRxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxBBE.setStatus("current")
_PmIntervalRxUAS_Type = Gauge32
_PmIntervalRxUAS_Object = MibTableColumn
pmIntervalRxUAS = _PmIntervalRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 9),
    _PmIntervalRxUAS_Type()
)
pmIntervalRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxUAS.setStatus("current")
_PmIntervalTxES_Type = Gauge32
_PmIntervalTxES_Object = MibTableColumn
pmIntervalTxES = _PmIntervalTxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 10),
    _PmIntervalTxES_Type()
)
pmIntervalTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxES.setStatus("current")
_PmIntervalTxSES_Type = Gauge32
_PmIntervalTxSES_Object = MibTableColumn
pmIntervalTxSES = _PmIntervalTxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 11),
    _PmIntervalTxSES_Type()
)
pmIntervalTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxSES.setStatus("current")
_PmIntervalTxBBE_Type = Gauge32
_PmIntervalTxBBE_Object = MibTableColumn
pmIntervalTxBBE = _PmIntervalTxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 12),
    _PmIntervalTxBBE_Type()
)
pmIntervalTxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxBBE.setStatus("current")
_PmIntervalTxUAS_Type = Gauge32
_PmIntervalTxUAS_Object = MibTableColumn
pmIntervalTxUAS = _PmIntervalTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 13),
    _PmIntervalTxUAS_Type()
)
pmIntervalTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxUAS.setStatus("current")
_PmIntervalName_Type = MgmtNameString
_PmIntervalName_Object = MibTableColumn
pmIntervalName = _PmIntervalName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 14),
    _PmIntervalName_Type()
)
pmIntervalName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalName.setStatus("current")
_PmIntervalRxPowerLevel_Type = Integer32
_PmIntervalRxPowerLevel_Object = MibTableColumn
pmIntervalRxPowerLevel = _PmIntervalRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 15),
    _PmIntervalRxPowerLevel_Type()
)
pmIntervalRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxPowerLevel.setStatus("current")
_PmIntervalGbeMaxUtilization_Type = Unsigned32
_PmIntervalGbeMaxUtilization_Object = MibTableColumn
pmIntervalGbeMaxUtilization = _PmIntervalGbeMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 16),
    _PmIntervalGbeMaxUtilization_Type()
)
pmIntervalGbeMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalGbeMaxUtilization.setStatus("current")
_PmIntervalTxPowerLevel_Type = Integer32
_PmIntervalTxPowerLevel_Object = MibTableColumn
pmIntervalTxPowerLevel = _PmIntervalTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 17),
    _PmIntervalTxPowerLevel_Type()
)
pmIntervalTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxPowerLevel.setStatus("current")
_PmIntervalRxUndersizedFrames_Type = Counter64
_PmIntervalRxUndersizedFrames_Object = MibTableColumn
pmIntervalRxUndersizedFrames = _PmIntervalRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 18),
    _PmIntervalRxUndersizedFrames_Type()
)
pmIntervalRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxUndersizedFrames.setStatus("current")
_PmIntervalRxOversizedFrames_Type = Counter64
_PmIntervalRxOversizedFrames_Object = MibTableColumn
pmIntervalRxOversizedFrames = _PmIntervalRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 19),
    _PmIntervalRxOversizedFrames_Type()
)
pmIntervalRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxOversizedFrames.setStatus("current")
_PmIntervalRxFragments_Type = Counter64
_PmIntervalRxFragments_Object = MibTableColumn
pmIntervalRxFragments = _PmIntervalRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 20),
    _PmIntervalRxFragments_Type()
)
pmIntervalRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxFragments.setStatus("current")
_PmIntervalRxFcsErrors_Type = Counter64
_PmIntervalRxFcsErrors_Object = MibTableColumn
pmIntervalRxFcsErrors = _PmIntervalRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 21),
    _PmIntervalRxFcsErrors_Type()
)
pmIntervalRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxFcsErrors.setStatus("current")
_PmIntervalRxInvalidCeVlanId_Type = Counter64
_PmIntervalRxInvalidCeVlanId_Object = MibTableColumn
pmIntervalRxInvalidCeVlanId = _PmIntervalRxInvalidCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 22),
    _PmIntervalRxInvalidCeVlanId_Type()
)
pmIntervalRxInvalidCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxInvalidCeVlanId.setStatus("current")
_PmIntervalTxOctets_Type = Counter64
_PmIntervalTxOctets_Object = MibTableColumn
pmIntervalTxOctets = _PmIntervalTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 23),
    _PmIntervalTxOctets_Type()
)
pmIntervalTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxOctets.setStatus("current")
_PmIntervalTxFrames_Type = Counter64
_PmIntervalTxFrames_Object = MibTableColumn
pmIntervalTxFrames = _PmIntervalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 24),
    _PmIntervalTxFrames_Type()
)
pmIntervalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxFrames.setStatus("current")
_PmIntervalTxUnicastFrames_Type = Counter64
_PmIntervalTxUnicastFrames_Object = MibTableColumn
pmIntervalTxUnicastFrames = _PmIntervalTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 25),
    _PmIntervalTxUnicastFrames_Type()
)
pmIntervalTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxUnicastFrames.setStatus("current")
_PmIntervalTxMulticastFrames_Type = Counter64
_PmIntervalTxMulticastFrames_Object = MibTableColumn
pmIntervalTxMulticastFrames = _PmIntervalTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 26),
    _PmIntervalTxMulticastFrames_Type()
)
pmIntervalTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxMulticastFrames.setStatus("current")
_PmIntervalTxBroadcastFrames_Type = Counter64
_PmIntervalTxBroadcastFrames_Object = MibTableColumn
pmIntervalTxBroadcastFrames = _PmIntervalTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 27),
    _PmIntervalTxBroadcastFrames_Type()
)
pmIntervalTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxBroadcastFrames.setStatus("current")
_PmIntervalRxOctets_Type = Counter64
_PmIntervalRxOctets_Object = MibTableColumn
pmIntervalRxOctets = _PmIntervalRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 28),
    _PmIntervalRxOctets_Type()
)
pmIntervalRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxOctets.setStatus("current")
_PmIntervalRxFrames_Type = Counter64
_PmIntervalRxFrames_Object = MibTableColumn
pmIntervalRxFrames = _PmIntervalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 29),
    _PmIntervalRxFrames_Type()
)
pmIntervalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxFrames.setStatus("current")
_PmIntervalRxUnicastFrames_Type = Counter64
_PmIntervalRxUnicastFrames_Object = MibTableColumn
pmIntervalRxUnicastFrames = _PmIntervalRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 30),
    _PmIntervalRxUnicastFrames_Type()
)
pmIntervalRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxUnicastFrames.setStatus("current")
_PmIntervalRxMulticastFrames_Type = Counter64
_PmIntervalRxMulticastFrames_Object = MibTableColumn
pmIntervalRxMulticastFrames = _PmIntervalRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 31),
    _PmIntervalRxMulticastFrames_Type()
)
pmIntervalRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxMulticastFrames.setStatus("current")
_PmIntervalRxBroadcastFrames_Type = Counter64
_PmIntervalRxBroadcastFrames_Object = MibTableColumn
pmIntervalRxBroadcastFrames = _PmIntervalRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 32),
    _PmIntervalRxBroadcastFrames_Type()
)
pmIntervalRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxBroadcastFrames.setStatus("current")
_PmIntervalIngressGreenFrameCount_Type = Counter64
_PmIntervalIngressGreenFrameCount_Object = MibTableColumn
pmIntervalIngressGreenFrameCount = _PmIntervalIngressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 33),
    _PmIntervalIngressGreenFrameCount_Type()
)
pmIntervalIngressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalIngressGreenFrameCount.setStatus("current")
_PmIntervalIngressYellowFrameCount_Type = Counter64
_PmIntervalIngressYellowFrameCount_Object = MibTableColumn
pmIntervalIngressYellowFrameCount = _PmIntervalIngressYellowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 34),
    _PmIntervalIngressYellowFrameCount_Type()
)
pmIntervalIngressYellowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalIngressYellowFrameCount.setStatus("current")
_PmIntervalIngressRedFrameCount_Type = Counter64
_PmIntervalIngressRedFrameCount_Object = MibTableColumn
pmIntervalIngressRedFrameCount = _PmIntervalIngressRedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 35),
    _PmIntervalIngressRedFrameCount_Type()
)
pmIntervalIngressRedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalIngressRedFrameCount.setStatus("current")
_PmIntervalIngressGreenOctetCount_Type = Counter64
_PmIntervalIngressGreenOctetCount_Object = MibTableColumn
pmIntervalIngressGreenOctetCount = _PmIntervalIngressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 36),
    _PmIntervalIngressGreenOctetCount_Type()
)
pmIntervalIngressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalIngressGreenOctetCount.setStatus("current")
_PmIntervalIngressYellowOctetCount_Type = Counter64
_PmIntervalIngressYellowOctetCount_Object = MibTableColumn
pmIntervalIngressYellowOctetCount = _PmIntervalIngressYellowOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 37),
    _PmIntervalIngressYellowOctetCount_Type()
)
pmIntervalIngressYellowOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalIngressYellowOctetCount.setStatus("current")
_PmIntervalIngressRedOctetCount_Type = Counter64
_PmIntervalIngressRedOctetCount_Object = MibTableColumn
pmIntervalIngressRedOctetCount = _PmIntervalIngressRedOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 38),
    _PmIntervalIngressRedOctetCount_Type()
)
pmIntervalIngressRedOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalIngressRedOctetCount.setStatus("current")
_PmIntervalEgressGreenFrameCount_Type = Counter64
_PmIntervalEgressGreenFrameCount_Object = MibTableColumn
pmIntervalEgressGreenFrameCount = _PmIntervalEgressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 39),
    _PmIntervalEgressGreenFrameCount_Type()
)
pmIntervalEgressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalEgressGreenFrameCount.setStatus("current")
_PmIntervalEgressGreenOctetCount_Type = Counter64
_PmIntervalEgressGreenOctetCount_Object = MibTableColumn
pmIntervalEgressGreenOctetCount = _PmIntervalEgressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 40),
    _PmIntervalEgressGreenOctetCount_Type()
)
pmIntervalEgressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalEgressGreenOctetCount.setStatus("current")
_PmIntervalGreenFrameDiscards_Type = Counter64
_PmIntervalGreenFrameDiscards_Object = MibTableColumn
pmIntervalGreenFrameDiscards = _PmIntervalGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 41),
    _PmIntervalGreenFrameDiscards_Type()
)
pmIntervalGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalGreenFrameDiscards.setStatus("current")
_PmIntervalYellowFrameDiscards_Type = Counter64
_PmIntervalYellowFrameDiscards_Object = MibTableColumn
pmIntervalYellowFrameDiscards = _PmIntervalYellowFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 42),
    _PmIntervalYellowFrameDiscards_Type()
)
pmIntervalYellowFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalYellowFrameDiscards.setStatus("current")
_PmIntervalGreenOctetDiscards_Type = Counter64
_PmIntervalGreenOctetDiscards_Object = MibTableColumn
pmIntervalGreenOctetDiscards = _PmIntervalGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 43),
    _PmIntervalGreenOctetDiscards_Type()
)
pmIntervalGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalGreenOctetDiscards.setStatus("current")
_PmIntervalYellowOctetDiscards_Type = Counter64
_PmIntervalYellowOctetDiscards_Object = MibTableColumn
pmIntervalYellowOctetDiscards = _PmIntervalYellowOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 44),
    _PmIntervalYellowOctetDiscards_Type()
)
pmIntervalYellowOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalYellowOctetDiscards.setStatus("current")
_PmIntervalTwoWayFrameDelay_Type = Gauge32
_PmIntervalTwoWayFrameDelay_Object = MibTableColumn
pmIntervalTwoWayFrameDelay = _PmIntervalTwoWayFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 45),
    _PmIntervalTwoWayFrameDelay_Type()
)
pmIntervalTwoWayFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTwoWayFrameDelay.setStatus("current")
_PmIntervalTwoWayFrameDelayVariation_Type = Gauge32
_PmIntervalTwoWayFrameDelayVariation_Object = MibTableColumn
pmIntervalTwoWayFrameDelayVariation = _PmIntervalTwoWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 46),
    _PmIntervalTwoWayFrameDelayVariation_Type()
)
pmIntervalTwoWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTwoWayFrameDelayVariation.setStatus("current")
_PmIntervalFrameLossRatioNearEnd_Type = Gauge32
_PmIntervalFrameLossRatioNearEnd_Object = MibTableColumn
pmIntervalFrameLossRatioNearEnd = _PmIntervalFrameLossRatioNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 47),
    _PmIntervalFrameLossRatioNearEnd_Type()
)
pmIntervalFrameLossRatioNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalFrameLossRatioNearEnd.setStatus("current")
_PmIntervalFrameLossRatioFarEnd_Type = Gauge32
_PmIntervalFrameLossRatioFarEnd_Object = MibTableColumn
pmIntervalFrameLossRatioFarEnd = _PmIntervalFrameLossRatioFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 48),
    _PmIntervalFrameLossRatioFarEnd_Type()
)
pmIntervalFrameLossRatioFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalFrameLossRatioFarEnd.setStatus("current")
_PmIntervalUnavailabilityNearEnd_Type = Gauge32
_PmIntervalUnavailabilityNearEnd_Object = MibTableColumn
pmIntervalUnavailabilityNearEnd = _PmIntervalUnavailabilityNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 49),
    _PmIntervalUnavailabilityNearEnd_Type()
)
pmIntervalUnavailabilityNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalUnavailabilityNearEnd.setStatus("current")
_PmIntervalUnavailabilityFarEnd_Type = Gauge32
_PmIntervalUnavailabilityFarEnd_Object = MibTableColumn
pmIntervalUnavailabilityFarEnd = _PmIntervalUnavailabilityFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 50),
    _PmIntervalUnavailabilityFarEnd_Type()
)
pmIntervalUnavailabilityFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalUnavailabilityFarEnd.setStatus("current")
_PmIntervalOneWayFrameDelayVariation_Type = Gauge32
_PmIntervalOneWayFrameDelayVariation_Object = MibTableColumn
pmIntervalOneWayFrameDelayVariation = _PmIntervalOneWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 51),
    _PmIntervalOneWayFrameDelayVariation_Type()
)
pmIntervalOneWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalOneWayFrameDelayVariation.setStatus("current")
_PmIntervalTxEthMaxUtilization_Type = Unsigned32
_PmIntervalTxEthMaxUtilization_Object = MibTableColumn
pmIntervalTxEthMaxUtilization = _PmIntervalTxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 52),
    _PmIntervalTxEthMaxUtilization_Type()
)
pmIntervalTxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalTxEthMaxUtilization.setStatus("current")
_PmIntervalRxEthMaxUtilization_Type = Unsigned32
_PmIntervalRxEthMaxUtilization_Object = MibTableColumn
pmIntervalRxEthMaxUtilization = _PmIntervalRxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 53),
    _PmIntervalRxEthMaxUtilization_Type()
)
pmIntervalRxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalRxEthMaxUtilization.setStatus("current")
_PmIntervalStartTime_Type = DateAndTime
_PmIntervalStartTime_Object = MibTableColumn
pmIntervalStartTime = _PmIntervalStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 54),
    _PmIntervalStartTime_Type()
)
pmIntervalStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalStartTime.setStatus("current")
_PmIntervalStopTime_Type = DateAndTime
_PmIntervalStopTime_Object = MibTableColumn
pmIntervalStopTime = _PmIntervalStopTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 2, 1, 1, 55),
    _PmIntervalStopTime_Type()
)
pmIntervalStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIntervalStopTime.setStatus("current")
_PmInterval24h_ObjectIdentity = ObjectIdentity
pmInterval24h = _PmInterval24h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3)
)
_PmInterval24hTable_Object = MibTable
pmInterval24hTable = _PmInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1)
)
if mibBuilder.loadTexts:
    pmInterval24hTable.setStatus("deprecated")
_PmInterval24hEntry_Object = MibTableRow
pmInterval24hEntry = _PmInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1)
)
pmInterval24hEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmInterval24hNumber"),
    (0, "LUM-PM-MIB", "pmInterval24hSubrack"),
    (0, "LUM-PM-MIB", "pmInterval24hSlot"),
    (0, "LUM-PM-MIB", "pmInterval24hPort"),
)
if mibBuilder.loadTexts:
    pmInterval24hEntry.setStatus("deprecated")
_PmInterval24hSubrack_Type = SubrackNumber
_PmInterval24hSubrack_Object = MibTableColumn
pmInterval24hSubrack = _PmInterval24hSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 1),
    _PmInterval24hSubrack_Type()
)
pmInterval24hSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hSubrack.setStatus("current")
_PmInterval24hSlot_Type = SlotNumber
_PmInterval24hSlot_Object = MibTableColumn
pmInterval24hSlot = _PmInterval24hSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 2),
    _PmInterval24hSlot_Type()
)
pmInterval24hSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hSlot.setStatus("current")
_PmInterval24hPort_Type = PortNumber
_PmInterval24hPort_Object = MibTableColumn
pmInterval24hPort = _PmInterval24hPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 3),
    _PmInterval24hPort_Type()
)
pmInterval24hPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hPort.setStatus("current")
_PmInterval24hNumber_Type = PmInterval24hNumber
_PmInterval24hNumber_Object = MibTableColumn
pmInterval24hNumber = _PmInterval24hNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 4),
    _PmInterval24hNumber_Type()
)
pmInterval24hNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hNumber.setStatus("current")
_PmInterval24hIsSuspect_Type = TruthValue
_PmInterval24hIsSuspect_Object = MibTableColumn
pmInterval24hIsSuspect = _PmInterval24hIsSuspect_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 5),
    _PmInterval24hIsSuspect_Type()
)
pmInterval24hIsSuspect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hIsSuspect.setStatus("current")
_PmInterval24hRxES_Type = Gauge32
_PmInterval24hRxES_Object = MibTableColumn
pmInterval24hRxES = _PmInterval24hRxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 6),
    _PmInterval24hRxES_Type()
)
pmInterval24hRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxES.setStatus("current")
_PmInterval24hRxSES_Type = Gauge32
_PmInterval24hRxSES_Object = MibTableColumn
pmInterval24hRxSES = _PmInterval24hRxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 7),
    _PmInterval24hRxSES_Type()
)
pmInterval24hRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxSES.setStatus("current")
_PmInterval24hRxBBE_Type = Gauge32
_PmInterval24hRxBBE_Object = MibTableColumn
pmInterval24hRxBBE = _PmInterval24hRxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 8),
    _PmInterval24hRxBBE_Type()
)
pmInterval24hRxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxBBE.setStatus("current")
_PmInterval24hRxUAS_Type = Gauge32
_PmInterval24hRxUAS_Object = MibTableColumn
pmInterval24hRxUAS = _PmInterval24hRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 9),
    _PmInterval24hRxUAS_Type()
)
pmInterval24hRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxUAS.setStatus("current")
_PmInterval24hTxES_Type = Gauge32
_PmInterval24hTxES_Object = MibTableColumn
pmInterval24hTxES = _PmInterval24hTxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 10),
    _PmInterval24hTxES_Type()
)
pmInterval24hTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxES.setStatus("current")
_PmInterval24hTxSES_Type = Gauge32
_PmInterval24hTxSES_Object = MibTableColumn
pmInterval24hTxSES = _PmInterval24hTxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 11),
    _PmInterval24hTxSES_Type()
)
pmInterval24hTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxSES.setStatus("current")
_PmInterval24hTxBBE_Type = Gauge32
_PmInterval24hTxBBE_Object = MibTableColumn
pmInterval24hTxBBE = _PmInterval24hTxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 12),
    _PmInterval24hTxBBE_Type()
)
pmInterval24hTxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxBBE.setStatus("current")
_PmInterval24hTxUAS_Type = Gauge32
_PmInterval24hTxUAS_Object = MibTableColumn
pmInterval24hTxUAS = _PmInterval24hTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 13),
    _PmInterval24hTxUAS_Type()
)
pmInterval24hTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxUAS.setStatus("current")
_PmInterval24hName_Type = MgmtNameString
_PmInterval24hName_Object = MibTableColumn
pmInterval24hName = _PmInterval24hName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 14),
    _PmInterval24hName_Type()
)
pmInterval24hName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hName.setStatus("current")
_PmInterval24hRxPowerLevel_Type = Integer32
_PmInterval24hRxPowerLevel_Object = MibTableColumn
pmInterval24hRxPowerLevel = _PmInterval24hRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 15),
    _PmInterval24hRxPowerLevel_Type()
)
pmInterval24hRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxPowerLevel.setStatus("current")
_PmInterval24hGbeMaxUtilization_Type = Unsigned32
_PmInterval24hGbeMaxUtilization_Object = MibTableColumn
pmInterval24hGbeMaxUtilization = _PmInterval24hGbeMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 16),
    _PmInterval24hGbeMaxUtilization_Type()
)
pmInterval24hGbeMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hGbeMaxUtilization.setStatus("current")
_PmInterval24hTxPowerLevel_Type = Integer32
_PmInterval24hTxPowerLevel_Object = MibTableColumn
pmInterval24hTxPowerLevel = _PmInterval24hTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 17),
    _PmInterval24hTxPowerLevel_Type()
)
pmInterval24hTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxPowerLevel.setStatus("current")
_PmInterval24hRxUndersizedFrames_Type = Counter64
_PmInterval24hRxUndersizedFrames_Object = MibTableColumn
pmInterval24hRxUndersizedFrames = _PmInterval24hRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 18),
    _PmInterval24hRxUndersizedFrames_Type()
)
pmInterval24hRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxUndersizedFrames.setStatus("current")
_PmInterval24hRxOversizedFrames_Type = Counter64
_PmInterval24hRxOversizedFrames_Object = MibTableColumn
pmInterval24hRxOversizedFrames = _PmInterval24hRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 19),
    _PmInterval24hRxOversizedFrames_Type()
)
pmInterval24hRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxOversizedFrames.setStatus("current")
_PmInterval24hRxFragments_Type = Counter64
_PmInterval24hRxFragments_Object = MibTableColumn
pmInterval24hRxFragments = _PmInterval24hRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 20),
    _PmInterval24hRxFragments_Type()
)
pmInterval24hRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxFragments.setStatus("current")
_PmInterval24hRxFcsErrors_Type = Counter64
_PmInterval24hRxFcsErrors_Object = MibTableColumn
pmInterval24hRxFcsErrors = _PmInterval24hRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 21),
    _PmInterval24hRxFcsErrors_Type()
)
pmInterval24hRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxFcsErrors.setStatus("current")
_PmInterval24hRxInvalidCeVlanId_Type = Counter64
_PmInterval24hRxInvalidCeVlanId_Object = MibTableColumn
pmInterval24hRxInvalidCeVlanId = _PmInterval24hRxInvalidCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 22),
    _PmInterval24hRxInvalidCeVlanId_Type()
)
pmInterval24hRxInvalidCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxInvalidCeVlanId.setStatus("current")
_PmInterval24hTxOctets_Type = Counter64
_PmInterval24hTxOctets_Object = MibTableColumn
pmInterval24hTxOctets = _PmInterval24hTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 23),
    _PmInterval24hTxOctets_Type()
)
pmInterval24hTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxOctets.setStatus("current")
_PmInterval24hTxFrames_Type = Counter64
_PmInterval24hTxFrames_Object = MibTableColumn
pmInterval24hTxFrames = _PmInterval24hTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 24),
    _PmInterval24hTxFrames_Type()
)
pmInterval24hTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxFrames.setStatus("current")
_PmInterval24hTxUnicastFrames_Type = Counter64
_PmInterval24hTxUnicastFrames_Object = MibTableColumn
pmInterval24hTxUnicastFrames = _PmInterval24hTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 25),
    _PmInterval24hTxUnicastFrames_Type()
)
pmInterval24hTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxUnicastFrames.setStatus("current")
_PmInterval24hTxMulticastFrames_Type = Counter64
_PmInterval24hTxMulticastFrames_Object = MibTableColumn
pmInterval24hTxMulticastFrames = _PmInterval24hTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 26),
    _PmInterval24hTxMulticastFrames_Type()
)
pmInterval24hTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxMulticastFrames.setStatus("current")
_PmInterval24hTxBroadcastFrames_Type = Counter64
_PmInterval24hTxBroadcastFrames_Object = MibTableColumn
pmInterval24hTxBroadcastFrames = _PmInterval24hTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 27),
    _PmInterval24hTxBroadcastFrames_Type()
)
pmInterval24hTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxBroadcastFrames.setStatus("current")
_PmInterval24hRxOctets_Type = Counter64
_PmInterval24hRxOctets_Object = MibTableColumn
pmInterval24hRxOctets = _PmInterval24hRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 28),
    _PmInterval24hRxOctets_Type()
)
pmInterval24hRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxOctets.setStatus("current")
_PmInterval24hRxFrames_Type = Counter64
_PmInterval24hRxFrames_Object = MibTableColumn
pmInterval24hRxFrames = _PmInterval24hRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 29),
    _PmInterval24hRxFrames_Type()
)
pmInterval24hRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxFrames.setStatus("current")
_PmInterval24hRxUnicastFrames_Type = Counter64
_PmInterval24hRxUnicastFrames_Object = MibTableColumn
pmInterval24hRxUnicastFrames = _PmInterval24hRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 30),
    _PmInterval24hRxUnicastFrames_Type()
)
pmInterval24hRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxUnicastFrames.setStatus("current")
_PmInterval24hRxMulticastFrames_Type = Counter64
_PmInterval24hRxMulticastFrames_Object = MibTableColumn
pmInterval24hRxMulticastFrames = _PmInterval24hRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 31),
    _PmInterval24hRxMulticastFrames_Type()
)
pmInterval24hRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxMulticastFrames.setStatus("current")
_PmInterval24hRxBroadcastFrames_Type = Counter64
_PmInterval24hRxBroadcastFrames_Object = MibTableColumn
pmInterval24hRxBroadcastFrames = _PmInterval24hRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 32),
    _PmInterval24hRxBroadcastFrames_Type()
)
pmInterval24hRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxBroadcastFrames.setStatus("current")
_PmInterval24hIngressGreenFrameCount_Type = Counter64
_PmInterval24hIngressGreenFrameCount_Object = MibTableColumn
pmInterval24hIngressGreenFrameCount = _PmInterval24hIngressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 33),
    _PmInterval24hIngressGreenFrameCount_Type()
)
pmInterval24hIngressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hIngressGreenFrameCount.setStatus("current")
_PmInterval24hIngressYellowFrameCount_Type = Counter64
_PmInterval24hIngressYellowFrameCount_Object = MibTableColumn
pmInterval24hIngressYellowFrameCount = _PmInterval24hIngressYellowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 34),
    _PmInterval24hIngressYellowFrameCount_Type()
)
pmInterval24hIngressYellowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hIngressYellowFrameCount.setStatus("current")
_PmInterval24hIngressRedFrameCount_Type = Counter64
_PmInterval24hIngressRedFrameCount_Object = MibTableColumn
pmInterval24hIngressRedFrameCount = _PmInterval24hIngressRedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 35),
    _PmInterval24hIngressRedFrameCount_Type()
)
pmInterval24hIngressRedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hIngressRedFrameCount.setStatus("current")
_PmInterval24hIngressGreenOctetCount_Type = Counter64
_PmInterval24hIngressGreenOctetCount_Object = MibTableColumn
pmInterval24hIngressGreenOctetCount = _PmInterval24hIngressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 36),
    _PmInterval24hIngressGreenOctetCount_Type()
)
pmInterval24hIngressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hIngressGreenOctetCount.setStatus("current")
_PmInterval24hIngressYellowOctetCount_Type = Counter64
_PmInterval24hIngressYellowOctetCount_Object = MibTableColumn
pmInterval24hIngressYellowOctetCount = _PmInterval24hIngressYellowOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 37),
    _PmInterval24hIngressYellowOctetCount_Type()
)
pmInterval24hIngressYellowOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hIngressYellowOctetCount.setStatus("current")
_PmInterval24hIngressRedOctetCount_Type = Counter64
_PmInterval24hIngressRedOctetCount_Object = MibTableColumn
pmInterval24hIngressRedOctetCount = _PmInterval24hIngressRedOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 38),
    _PmInterval24hIngressRedOctetCount_Type()
)
pmInterval24hIngressRedOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hIngressRedOctetCount.setStatus("current")
_PmInterval24hEgressGreenFrameCount_Type = Counter64
_PmInterval24hEgressGreenFrameCount_Object = MibTableColumn
pmInterval24hEgressGreenFrameCount = _PmInterval24hEgressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 39),
    _PmInterval24hEgressGreenFrameCount_Type()
)
pmInterval24hEgressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hEgressGreenFrameCount.setStatus("current")
_PmInterval24hEgressGreenOctetCount_Type = Counter64
_PmInterval24hEgressGreenOctetCount_Object = MibTableColumn
pmInterval24hEgressGreenOctetCount = _PmInterval24hEgressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 40),
    _PmInterval24hEgressGreenOctetCount_Type()
)
pmInterval24hEgressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hEgressGreenOctetCount.setStatus("current")
_PmInterval24hGreenFrameDiscards_Type = Counter64
_PmInterval24hGreenFrameDiscards_Object = MibTableColumn
pmInterval24hGreenFrameDiscards = _PmInterval24hGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 41),
    _PmInterval24hGreenFrameDiscards_Type()
)
pmInterval24hGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hGreenFrameDiscards.setStatus("current")
_PmInterval24hYellowFrameDiscards_Type = Counter64
_PmInterval24hYellowFrameDiscards_Object = MibTableColumn
pmInterval24hYellowFrameDiscards = _PmInterval24hYellowFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 42),
    _PmInterval24hYellowFrameDiscards_Type()
)
pmInterval24hYellowFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hYellowFrameDiscards.setStatus("current")
_PmInterval24hGreenOctetDiscards_Type = Counter64
_PmInterval24hGreenOctetDiscards_Object = MibTableColumn
pmInterval24hGreenOctetDiscards = _PmInterval24hGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 43),
    _PmInterval24hGreenOctetDiscards_Type()
)
pmInterval24hGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hGreenOctetDiscards.setStatus("current")
_PmInterval24hYellowOctetDiscards_Type = Counter64
_PmInterval24hYellowOctetDiscards_Object = MibTableColumn
pmInterval24hYellowOctetDiscards = _PmInterval24hYellowOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 44),
    _PmInterval24hYellowOctetDiscards_Type()
)
pmInterval24hYellowOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hYellowOctetDiscards.setStatus("current")
_PmInterval24hTwoWayFrameDelay_Type = Gauge32
_PmInterval24hTwoWayFrameDelay_Object = MibTableColumn
pmInterval24hTwoWayFrameDelay = _PmInterval24hTwoWayFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 45),
    _PmInterval24hTwoWayFrameDelay_Type()
)
pmInterval24hTwoWayFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTwoWayFrameDelay.setStatus("current")
_PmInterval24hTwoWayFrameDelayVariation_Type = Gauge32
_PmInterval24hTwoWayFrameDelayVariation_Object = MibTableColumn
pmInterval24hTwoWayFrameDelayVariation = _PmInterval24hTwoWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 46),
    _PmInterval24hTwoWayFrameDelayVariation_Type()
)
pmInterval24hTwoWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTwoWayFrameDelayVariation.setStatus("current")
_PmInterval24hFrameLossRatioNearEnd_Type = Gauge32
_PmInterval24hFrameLossRatioNearEnd_Object = MibTableColumn
pmInterval24hFrameLossRatioNearEnd = _PmInterval24hFrameLossRatioNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 47),
    _PmInterval24hFrameLossRatioNearEnd_Type()
)
pmInterval24hFrameLossRatioNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hFrameLossRatioNearEnd.setStatus("current")
_PmInterval24hFrameLossRatioFarEnd_Type = Gauge32
_PmInterval24hFrameLossRatioFarEnd_Object = MibTableColumn
pmInterval24hFrameLossRatioFarEnd = _PmInterval24hFrameLossRatioFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 48),
    _PmInterval24hFrameLossRatioFarEnd_Type()
)
pmInterval24hFrameLossRatioFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hFrameLossRatioFarEnd.setStatus("current")
_PmInterval24hUnavailabilityNearEnd_Type = Gauge32
_PmInterval24hUnavailabilityNearEnd_Object = MibTableColumn
pmInterval24hUnavailabilityNearEnd = _PmInterval24hUnavailabilityNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 49),
    _PmInterval24hUnavailabilityNearEnd_Type()
)
pmInterval24hUnavailabilityNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hUnavailabilityNearEnd.setStatus("current")
_PmInterval24hUnavailabilityFarEnd_Type = Gauge32
_PmInterval24hUnavailabilityFarEnd_Object = MibTableColumn
pmInterval24hUnavailabilityFarEnd = _PmInterval24hUnavailabilityFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 50),
    _PmInterval24hUnavailabilityFarEnd_Type()
)
pmInterval24hUnavailabilityFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hUnavailabilityFarEnd.setStatus("current")
_PmInterval24hOneWayFrameDelayVariation_Type = Gauge32
_PmInterval24hOneWayFrameDelayVariation_Object = MibTableColumn
pmInterval24hOneWayFrameDelayVariation = _PmInterval24hOneWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 51),
    _PmInterval24hOneWayFrameDelayVariation_Type()
)
pmInterval24hOneWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hOneWayFrameDelayVariation.setStatus("current")
_PmInterval24hTxEthMaxUtilization_Type = Unsigned32
_PmInterval24hTxEthMaxUtilization_Object = MibTableColumn
pmInterval24hTxEthMaxUtilization = _PmInterval24hTxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 52),
    _PmInterval24hTxEthMaxUtilization_Type()
)
pmInterval24hTxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hTxEthMaxUtilization.setStatus("current")
_PmInterval24hRxEthMaxUtilization_Type = Unsigned32
_PmInterval24hRxEthMaxUtilization_Object = MibTableColumn
pmInterval24hRxEthMaxUtilization = _PmInterval24hRxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 53),
    _PmInterval24hRxEthMaxUtilization_Type()
)
pmInterval24hRxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hRxEthMaxUtilization.setStatus("current")
_PmInterval24hStartTime_Type = DateAndTime
_PmInterval24hStartTime_Object = MibTableColumn
pmInterval24hStartTime = _PmInterval24hStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 54),
    _PmInterval24hStartTime_Type()
)
pmInterval24hStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hStartTime.setStatus("current")
_PmInterval24hStopTime_Type = DateAndTime
_PmInterval24hStopTime_Object = MibTableColumn
pmInterval24hStopTime = _PmInterval24hStopTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 3, 1, 1, 55),
    _PmInterval24hStopTime_Type()
)
pmInterval24hStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmInterval24hStopTime.setStatus("current")
_LumentisPmNotifications_ObjectIdentity = ObjectIdentity
lumentisPmNotifications = _LumentisPmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 4)
)
_PmNotifyPrefix_ObjectIdentity = ObjectIdentity
pmNotifyPrefix = _PmNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 4, 0)
)
_PmFile_ObjectIdentity = ObjectIdentity
pmFile = _PmFile_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5)
)
_PmFileTable_Object = MibTable
pmFileTable = _PmFileTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1)
)
if mibBuilder.loadTexts:
    pmFileTable.setStatus("current")
_PmFileEntry_Object = MibTableRow
pmFileEntry = _PmFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1)
)
pmFileEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmFileIndex"),
)
if mibBuilder.loadTexts:
    pmFileEntry.setStatus("current")
_PmFileIndex_Type = PmInterval15mNumber
_PmFileIndex_Object = MibTableColumn
pmFileIndex = _PmFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1, 1),
    _PmFileIndex_Type()
)
pmFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFileIndex.setStatus("current")
_PmFileName_Type = DisplayString
_PmFileName_Object = MibTableColumn
pmFileName = _PmFileName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1, 2),
    _PmFileName_Type()
)
pmFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFileName.setStatus("current")
_PmFileCreatedTime_Type = DateAndTime
_PmFileCreatedTime_Object = MibTableColumn
pmFileCreatedTime = _PmFileCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1, 3),
    _PmFileCreatedTime_Type()
)
pmFileCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFileCreatedTime.setStatus("current")
_PmFileSeqNumber_Type = Counter32
_PmFileSeqNumber_Object = MibTableColumn
pmFileSeqNumber = _PmFileSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1, 4),
    _PmFileSeqNumber_Type()
)
pmFileSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFileSeqNumber.setStatus("current")
_PmFileStartTime_Type = DateAndTime
_PmFileStartTime_Object = MibTableColumn
pmFileStartTime = _PmFileStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1, 5),
    _PmFileStartTime_Type()
)
pmFileStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFileStartTime.setStatus("current")
_PmFileStopTime_Type = DateAndTime
_PmFileStopTime_Object = MibTableColumn
pmFileStopTime = _PmFileStopTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1, 6),
    _PmFileStopTime_Type()
)
pmFileStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFileStopTime.setStatus("current")
_PmFileUrl_Type = DisplayString
_PmFileUrl_Object = MibTableColumn
pmFileUrl = _PmFileUrl_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 5, 1, 1, 7),
    _PmFileUrl_Type()
)
pmFileUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFileUrl.setStatus("current")
_PmIfList_ObjectIdentity = ObjectIdentity
pmIfList = _PmIfList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6)
)
_PmIfTable_Object = MibTable
pmIfTable = _PmIfTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1)
)
if mibBuilder.loadTexts:
    pmIfTable.setStatus("current")
_PmIfEntry_Object = MibTableRow
pmIfEntry = _PmIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1)
)
pmIfEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmIfIndex"),
)
if mibBuilder.loadTexts:
    pmIfEntry.setStatus("current")


class _PmIfIndex_Type(Unsigned32):
    """Custom type pmIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmIfIndex_Type.__name__ = "Unsigned32"
_PmIfIndex_Object = MibTableColumn
pmIfIndex = _PmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 1),
    _PmIfIndex_Type()
)
pmIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfIndex.setStatus("current")
_PmIfName_Type = MgmtNameString
_PmIfName_Object = MibTableColumn
pmIfName = _PmIfName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 2),
    _PmIfName_Type()
)
pmIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfName.setStatus("current")
_PmIfSubrack_Type = SubrackNumber
_PmIfSubrack_Object = MibTableColumn
pmIfSubrack = _PmIfSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 3),
    _PmIfSubrack_Type()
)
pmIfSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmIfSubrack.setStatus("current")
_PmIfSlot_Type = SlotNumber
_PmIfSlot_Object = MibTableColumn
pmIfSlot = _PmIfSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 4),
    _PmIfSlot_Type()
)
pmIfSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmIfSlot.setStatus("current")
_PmIfPort_Type = PortNumber
_PmIfPort_Object = MibTableColumn
pmIfPort = _PmIfPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 5),
    _PmIfPort_Type()
)
pmIfPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmIfPort.setStatus("current")


class _PmIfPmReportMode_Type(Integer32):
    """Custom type pmIfPmReportMode based on Integer32"""
    defaultValue = 2

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


_PmIfPmReportMode_Type.__name__ = "Integer32"
_PmIfPmReportMode_Object = MibTableColumn
pmIfPmReportMode = _PmIfPmReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 6),
    _PmIfPmReportMode_Type()
)
pmIfPmReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfPmReportMode.setStatus("current")
_PmIfRxCurrentES_Type = Gauge32
_PmIfRxCurrentES_Object = MibTableColumn
pmIfRxCurrentES = _PmIfRxCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 7),
    _PmIfRxCurrentES_Type()
)
pmIfRxCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxCurrentES.setStatus("current")
_PmIfRxCurrentSES_Type = Gauge32
_PmIfRxCurrentSES_Object = MibTableColumn
pmIfRxCurrentSES = _PmIfRxCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 8),
    _PmIfRxCurrentSES_Type()
)
pmIfRxCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxCurrentSES.setStatus("current")
_PmIfRxCurrentBBE_Type = Gauge32
_PmIfRxCurrentBBE_Object = MibTableColumn
pmIfRxCurrentBBE = _PmIfRxCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 9),
    _PmIfRxCurrentBBE_Type()
)
pmIfRxCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxCurrentBBE.setStatus("current")
_PmIfRxCurrentUAS_Type = Gauge32
_PmIfRxCurrentUAS_Object = MibTableColumn
pmIfRxCurrentUAS = _PmIfRxCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 10),
    _PmIfRxCurrentUAS_Type()
)
pmIfRxCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxCurrentUAS.setStatus("current")
_PmIfTxCurrentES_Type = Gauge32
_PmIfTxCurrentES_Object = MibTableColumn
pmIfTxCurrentES = _PmIfTxCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 11),
    _PmIfTxCurrentES_Type()
)
pmIfTxCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxCurrentES.setStatus("current")
_PmIfTxCurrentSES_Type = Gauge32
_PmIfTxCurrentSES_Object = MibTableColumn
pmIfTxCurrentSES = _PmIfTxCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 12),
    _PmIfTxCurrentSES_Type()
)
pmIfTxCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxCurrentSES.setStatus("current")
_PmIfTxCurrentBBE_Type = Gauge32
_PmIfTxCurrentBBE_Object = MibTableColumn
pmIfTxCurrentBBE = _PmIfTxCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 13),
    _PmIfTxCurrentBBE_Type()
)
pmIfTxCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxCurrentBBE.setStatus("current")
_PmIfTxCurrentUAS_Type = Gauge32
_PmIfTxCurrentUAS_Object = MibTableColumn
pmIfTxCurrentUAS = _PmIfTxCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 14),
    _PmIfTxCurrentUAS_Type()
)
pmIfTxCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxCurrentUAS.setStatus("current")
_PmIfRx24hCurrentES_Type = Gauge32
_PmIfRx24hCurrentES_Object = MibTableColumn
pmIfRx24hCurrentES = _PmIfRx24hCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 15),
    _PmIfRx24hCurrentES_Type()
)
pmIfRx24hCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hCurrentES.setStatus("current")
_PmIfRx24hCurrentSES_Type = Gauge32
_PmIfRx24hCurrentSES_Object = MibTableColumn
pmIfRx24hCurrentSES = _PmIfRx24hCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 16),
    _PmIfRx24hCurrentSES_Type()
)
pmIfRx24hCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hCurrentSES.setStatus("current")
_PmIfRx24hCurrentBBE_Type = Gauge32
_PmIfRx24hCurrentBBE_Object = MibTableColumn
pmIfRx24hCurrentBBE = _PmIfRx24hCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 17),
    _PmIfRx24hCurrentBBE_Type()
)
pmIfRx24hCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hCurrentBBE.setStatus("current")
_PmIfRx24hCurrentUAS_Type = Gauge32
_PmIfRx24hCurrentUAS_Object = MibTableColumn
pmIfRx24hCurrentUAS = _PmIfRx24hCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 18),
    _PmIfRx24hCurrentUAS_Type()
)
pmIfRx24hCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hCurrentUAS.setStatus("current")
_PmIfTx24hCurrentES_Type = Gauge32
_PmIfTx24hCurrentES_Object = MibTableColumn
pmIfTx24hCurrentES = _PmIfTx24hCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 19),
    _PmIfTx24hCurrentES_Type()
)
pmIfTx24hCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hCurrentES.setStatus("current")
_PmIfTx24hCurrentSES_Type = Gauge32
_PmIfTx24hCurrentSES_Object = MibTableColumn
pmIfTx24hCurrentSES = _PmIfTx24hCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 20),
    _PmIfTx24hCurrentSES_Type()
)
pmIfTx24hCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hCurrentSES.setStatus("current")
_PmIfTx24hCurrentBBE_Type = Gauge32
_PmIfTx24hCurrentBBE_Object = MibTableColumn
pmIfTx24hCurrentBBE = _PmIfTx24hCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 21),
    _PmIfTx24hCurrentBBE_Type()
)
pmIfTx24hCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hCurrentBBE.setStatus("current")
_PmIfTx24hCurrentUAS_Type = Gauge32
_PmIfTx24hCurrentUAS_Object = MibTableColumn
pmIfTx24hCurrentUAS = _PmIfTx24hCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 22),
    _PmIfTx24hCurrentUAS_Type()
)
pmIfTx24hCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hCurrentUAS.setStatus("current")


class _PmIfRxESThreshold_Type(Unsigned32):
    """Custom type pmIfRxESThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmIfRxESThreshold_Type.__name__ = "Unsigned32"
_PmIfRxESThreshold_Object = MibTableColumn
pmIfRxESThreshold = _PmIfRxESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 23),
    _PmIfRxESThreshold_Type()
)
pmIfRxESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRxESThreshold.setStatus("current")


class _PmIfRxSESThreshold_Type(Unsigned32):
    """Custom type pmIfRxSESThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmIfRxSESThreshold_Type.__name__ = "Unsigned32"
_PmIfRxSESThreshold_Object = MibTableColumn
pmIfRxSESThreshold = _PmIfRxSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 24),
    _PmIfRxSESThreshold_Type()
)
pmIfRxSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRxSESThreshold.setStatus("current")


class _PmIfRxBBEThreshold_Type(Unsigned32):
    """Custom type pmIfRxBBEThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmIfRxBBEThreshold_Type.__name__ = "Unsigned32"
_PmIfRxBBEThreshold_Object = MibTableColumn
pmIfRxBBEThreshold = _PmIfRxBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 25),
    _PmIfRxBBEThreshold_Type()
)
pmIfRxBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRxBBEThreshold.setStatus("current")


class _PmIfRxUASThreshold_Type(Unsigned32):
    """Custom type pmIfRxUASThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmIfRxUASThreshold_Type.__name__ = "Unsigned32"
_PmIfRxUASThreshold_Object = MibTableColumn
pmIfRxUASThreshold = _PmIfRxUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 26),
    _PmIfRxUASThreshold_Type()
)
pmIfRxUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRxUASThreshold.setStatus("current")


class _PmIfTxESThreshold_Type(Unsigned32):
    """Custom type pmIfTxESThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmIfTxESThreshold_Type.__name__ = "Unsigned32"
_PmIfTxESThreshold_Object = MibTableColumn
pmIfTxESThreshold = _PmIfTxESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 27),
    _PmIfTxESThreshold_Type()
)
pmIfTxESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTxESThreshold.setStatus("current")


class _PmIfTxSESThreshold_Type(Unsigned32):
    """Custom type pmIfTxSESThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmIfTxSESThreshold_Type.__name__ = "Unsigned32"
_PmIfTxSESThreshold_Object = MibTableColumn
pmIfTxSESThreshold = _PmIfTxSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 28),
    _PmIfTxSESThreshold_Type()
)
pmIfTxSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTxSESThreshold.setStatus("current")


class _PmIfTxBBEThreshold_Type(Unsigned32):
    """Custom type pmIfTxBBEThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmIfTxBBEThreshold_Type.__name__ = "Unsigned32"
_PmIfTxBBEThreshold_Object = MibTableColumn
pmIfTxBBEThreshold = _PmIfTxBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 29),
    _PmIfTxBBEThreshold_Type()
)
pmIfTxBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTxBBEThreshold.setStatus("current")


class _PmIfTxUASThreshold_Type(Unsigned32):
    """Custom type pmIfTxUASThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmIfTxUASThreshold_Type.__name__ = "Unsigned32"
_PmIfTxUASThreshold_Object = MibTableColumn
pmIfTxUASThreshold = _PmIfTxUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 30),
    _PmIfTxUASThreshold_Type()
)
pmIfTxUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTxUASThreshold.setStatus("current")


class _PmIfRx24hESThreshold_Type(Unsigned32):
    """Custom type pmIfRx24hESThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmIfRx24hESThreshold_Type.__name__ = "Unsigned32"
_PmIfRx24hESThreshold_Object = MibTableColumn
pmIfRx24hESThreshold = _PmIfRx24hESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 31),
    _PmIfRx24hESThreshold_Type()
)
pmIfRx24hESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRx24hESThreshold.setStatus("current")


class _PmIfRx24hSESThreshold_Type(Unsigned32):
    """Custom type pmIfRx24hSESThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmIfRx24hSESThreshold_Type.__name__ = "Unsigned32"
_PmIfRx24hSESThreshold_Object = MibTableColumn
pmIfRx24hSESThreshold = _PmIfRx24hSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 32),
    _PmIfRx24hSESThreshold_Type()
)
pmIfRx24hSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRx24hSESThreshold.setStatus("current")


class _PmIfRx24hBBEThreshold_Type(Unsigned32):
    """Custom type pmIfRx24hBBEThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmIfRx24hBBEThreshold_Type.__name__ = "Unsigned32"
_PmIfRx24hBBEThreshold_Object = MibTableColumn
pmIfRx24hBBEThreshold = _PmIfRx24hBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 33),
    _PmIfRx24hBBEThreshold_Type()
)
pmIfRx24hBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRx24hBBEThreshold.setStatus("current")


class _PmIfRx24hUASThreshold_Type(Unsigned32):
    """Custom type pmIfRx24hUASThreshold based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmIfRx24hUASThreshold_Type.__name__ = "Unsigned32"
_PmIfRx24hUASThreshold_Object = MibTableColumn
pmIfRx24hUASThreshold = _PmIfRx24hUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 34),
    _PmIfRx24hUASThreshold_Type()
)
pmIfRx24hUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfRx24hUASThreshold.setStatus("current")


class _PmIfTx24hESThreshold_Type(Unsigned32):
    """Custom type pmIfTx24hESThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmIfTx24hESThreshold_Type.__name__ = "Unsigned32"
_PmIfTx24hESThreshold_Object = MibTableColumn
pmIfTx24hESThreshold = _PmIfTx24hESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 35),
    _PmIfTx24hESThreshold_Type()
)
pmIfTx24hESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTx24hESThreshold.setStatus("current")


class _PmIfTx24hSESThreshold_Type(Unsigned32):
    """Custom type pmIfTx24hSESThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmIfTx24hSESThreshold_Type.__name__ = "Unsigned32"
_PmIfTx24hSESThreshold_Object = MibTableColumn
pmIfTx24hSESThreshold = _PmIfTx24hSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 36),
    _PmIfTx24hSESThreshold_Type()
)
pmIfTx24hSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTx24hSESThreshold.setStatus("current")


class _PmIfTx24hBBEThreshold_Type(Unsigned32):
    """Custom type pmIfTx24hBBEThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmIfTx24hBBEThreshold_Type.__name__ = "Unsigned32"
_PmIfTx24hBBEThreshold_Object = MibTableColumn
pmIfTx24hBBEThreshold = _PmIfTx24hBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 37),
    _PmIfTx24hBBEThreshold_Type()
)
pmIfTx24hBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTx24hBBEThreshold.setStatus("current")


class _PmIfTx24hUASThreshold_Type(Unsigned32):
    """Custom type pmIfTx24hUASThreshold based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmIfTx24hUASThreshold_Type.__name__ = "Unsigned32"
_PmIfTx24hUASThreshold_Object = MibTableColumn
pmIfTx24hUASThreshold = _PmIfTx24hUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 38),
    _PmIfTx24hUASThreshold_Type()
)
pmIfTx24hUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfTx24hUASThreshold.setStatus("current")
_PmIfRxES_Type = FaultStatus
_PmIfRxES_Object = MibTableColumn
pmIfRxES = _PmIfRxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 39),
    _PmIfRxES_Type()
)
pmIfRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxES.setStatus("current")
_PmIfRxSES_Type = FaultStatus
_PmIfRxSES_Object = MibTableColumn
pmIfRxSES = _PmIfRxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 40),
    _PmIfRxSES_Type()
)
pmIfRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxSES.setStatus("current")
_PmIfRxBBE_Type = FaultStatus
_PmIfRxBBE_Object = MibTableColumn
pmIfRxBBE = _PmIfRxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 41),
    _PmIfRxBBE_Type()
)
pmIfRxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxBBE.setStatus("current")
_PmIfRxUAS_Type = FaultStatus
_PmIfRxUAS_Object = MibTableColumn
pmIfRxUAS = _PmIfRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 42),
    _PmIfRxUAS_Type()
)
pmIfRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxUAS.setStatus("current")
_PmIfTxES_Type = FaultStatus
_PmIfTxES_Object = MibTableColumn
pmIfTxES = _PmIfTxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 43),
    _PmIfTxES_Type()
)
pmIfTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxES.setStatus("current")
_PmIfTxSES_Type = FaultStatus
_PmIfTxSES_Object = MibTableColumn
pmIfTxSES = _PmIfTxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 44),
    _PmIfTxSES_Type()
)
pmIfTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxSES.setStatus("current")
_PmIfTxBBE_Type = FaultStatus
_PmIfTxBBE_Object = MibTableColumn
pmIfTxBBE = _PmIfTxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 45),
    _PmIfTxBBE_Type()
)
pmIfTxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxBBE.setStatus("current")
_PmIfTxUAS_Type = FaultStatus
_PmIfTxUAS_Object = MibTableColumn
pmIfTxUAS = _PmIfTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 46),
    _PmIfTxUAS_Type()
)
pmIfTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxUAS.setStatus("current")
_PmIfRx24hES_Type = FaultStatus
_PmIfRx24hES_Object = MibTableColumn
pmIfRx24hES = _PmIfRx24hES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 47),
    _PmIfRx24hES_Type()
)
pmIfRx24hES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hES.setStatus("current")
_PmIfRx24hSES_Type = FaultStatus
_PmIfRx24hSES_Object = MibTableColumn
pmIfRx24hSES = _PmIfRx24hSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 48),
    _PmIfRx24hSES_Type()
)
pmIfRx24hSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hSES.setStatus("current")
_PmIfRx24hBBE_Type = FaultStatus
_PmIfRx24hBBE_Object = MibTableColumn
pmIfRx24hBBE = _PmIfRx24hBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 49),
    _PmIfRx24hBBE_Type()
)
pmIfRx24hBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hBBE.setStatus("current")
_PmIfRx24hUAS_Type = FaultStatus
_PmIfRx24hUAS_Object = MibTableColumn
pmIfRx24hUAS = _PmIfRx24hUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 50),
    _PmIfRx24hUAS_Type()
)
pmIfRx24hUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hUAS.setStatus("current")
_PmIfTx24hES_Type = FaultStatus
_PmIfTx24hES_Object = MibTableColumn
pmIfTx24hES = _PmIfTx24hES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 51),
    _PmIfTx24hES_Type()
)
pmIfTx24hES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hES.setStatus("current")
_PmIfTx24hSES_Type = FaultStatus
_PmIfTx24hSES_Object = MibTableColumn
pmIfTx24hSES = _PmIfTx24hSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 52),
    _PmIfTx24hSES_Type()
)
pmIfTx24hSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hSES.setStatus("current")
_PmIfTx24hBBE_Type = FaultStatus
_PmIfTx24hBBE_Object = MibTableColumn
pmIfTx24hBBE = _PmIfTx24hBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 53),
    _PmIfTx24hBBE_Type()
)
pmIfTx24hBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hBBE.setStatus("current")
_PmIfTx24hUAS_Type = FaultStatus
_PmIfTx24hUAS_Object = MibTableColumn
pmIfTx24hUAS = _PmIfTx24hUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 54),
    _PmIfTx24hUAS_Type()
)
pmIfTx24hUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTx24hUAS.setStatus("current")
_PmIfRxPort_Type = PortNumber
_PmIfRxPort_Object = MibTableColumn
pmIfRxPort = _PmIfRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 55),
    _PmIfRxPort_Type()
)
pmIfRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmIfRxPort.setStatus("current")


class _PmIfReset15Min_Type(Integer32):
    """Custom type pmIfReset15Min based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmIfReset15Min_Type.__name__ = "Integer32"
_PmIfReset15Min_Object = MibTableColumn
pmIfReset15Min = _PmIfReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 56),
    _PmIfReset15Min_Type()
)
pmIfReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfReset15Min.setStatus("current")


class _PmIfReset24H_Type(Integer32):
    """Custom type pmIfReset24H based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmIfReset24H_Type.__name__ = "Integer32"
_PmIfReset24H_Object = MibTableColumn
pmIfReset24H = _PmIfReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 57),
    _PmIfReset24H_Type()
)
pmIfReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfReset24H.setStatus("current")


class _PmIfAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type pmIfAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_PmIfAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_PmIfAdminStatus_Object = MibTableColumn
pmIfAdminStatus = _PmIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 58),
    _PmIfAdminStatus_Type()
)
pmIfAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmIfAdminStatus.setStatus("current")


class _PmIfOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type pmIfOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_PmIfOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_PmIfOperStatus_Object = MibTableColumn
pmIfOperStatus = _PmIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 59),
    _PmIfOperStatus_Type()
)
pmIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfOperStatus.setStatus("current")
_PmIfIsSuspect15Min_Type = TruthValue
_PmIfIsSuspect15Min_Object = MibTableColumn
pmIfIsSuspect15Min = _PmIfIsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 60),
    _PmIfIsSuspect15Min_Type()
)
pmIfIsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfIsSuspect15Min.setStatus("current")
_PmIfIsSuspect24H_Type = TruthValue
_PmIfIsSuspect24H_Object = MibTableColumn
pmIfIsSuspect24H = _PmIfIsSuspect24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 61),
    _PmIfIsSuspect24H_Type()
)
pmIfIsSuspect24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfIsSuspect24H.setStatus("current")
_PmIfInstallCommand_Type = CommandString
_PmIfInstallCommand_Object = MibTableColumn
pmIfInstallCommand = _PmIfInstallCommand_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 62),
    _PmIfInstallCommand_Type()
)
pmIfInstallCommand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfInstallCommand.setStatus("current")
_PmIfRxPowerLevel_Type = Integer32
_PmIfRxPowerLevel_Object = MibTableColumn
pmIfRxPowerLevel = _PmIfRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 63),
    _PmIfRxPowerLevel_Type()
)
pmIfRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxPowerLevel.setStatus("current")


class _PmIfInitialPowerLevel_Type(Integer32):
    """Custom type pmIfInitialPowerLevel based on Integer32"""
    defaultValue = -10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-10000, 10000),
    )


_PmIfInitialPowerLevel_Type.__name__ = "Integer32"
_PmIfInitialPowerLevel_Object = MibTableColumn
pmIfInitialPowerLevel = _PmIfInitialPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 64),
    _PmIfInitialPowerLevel_Type()
)
pmIfInitialPowerLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmIfInitialPowerLevel.setStatus("current")
_PmIfRxGbeMaxUtilization_Type = Gauge32
_PmIfRxGbeMaxUtilization_Object = MibTableColumn
pmIfRxGbeMaxUtilization = _PmIfRxGbeMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 65),
    _PmIfRxGbeMaxUtilization_Type()
)
pmIfRxGbeMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxGbeMaxUtilization.setStatus("current")
_PmIfRx24hGbeMaxUtilization_Type = Gauge32
_PmIfRx24hGbeMaxUtilization_Object = MibTableColumn
pmIfRx24hGbeMaxUtilization = _PmIfRx24hGbeMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 66),
    _PmIfRx24hGbeMaxUtilization_Type()
)
pmIfRx24hGbeMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRx24hGbeMaxUtilization.setStatus("current")
_PmIfTxPowerLevel_Type = Integer32
_PmIfTxPowerLevel_Object = MibTableColumn
pmIfTxPowerLevel = _PmIfTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 67),
    _PmIfTxPowerLevel_Type()
)
pmIfTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfTxPowerLevel.setStatus("current")
_PmIfObjectProperty_Type = ObjectProperty
_PmIfObjectProperty_Object = MibTableColumn
pmIfObjectProperty = _PmIfObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 68),
    _PmIfObjectProperty_Type()
)
pmIfObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfObjectProperty.setStatus("current")
_PmIfDelay_Type = Gauge32
_PmIfDelay_Object = MibTableColumn
pmIfDelay = _PmIfDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 69),
    _PmIfDelay_Type()
)
pmIfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfDelay.setStatus("current")
_PmIfRxBEREstimation_Type = Unsigned32
_PmIfRxBEREstimation_Object = MibTableColumn
pmIfRxBEREstimation = _PmIfRxBEREstimation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 70),
    _PmIfRxBEREstimation_Type()
)
pmIfRxBEREstimation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmIfRxBEREstimation.setStatus("current")
_PmIfIfNo_Type = PortNumber
_PmIfIfNo_Object = MibTableColumn
pmIfIfNo = _PmIfIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 71),
    _PmIfIfNo_Type()
)
pmIfIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmIfIfNo.setStatus("current")


class _PmIfUpPortId_Type(Integer32):
    """Custom type pmIfUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PmIfUpPortId_Type.__name__ = "Integer32"
_PmIfUpPortId_Object = MibTableColumn
pmIfUpPortId = _PmIfUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 6, 1, 1, 72),
    _PmIfUpPortId_Type()
)
pmIfUpPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmIfUpPortId.setStatus("current")
_PmLogGeneral_ObjectIdentity = ObjectIdentity
pmLogGeneral = _PmLogGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7)
)
_PmLogGeneralLastChangeTime_Type = DateAndTime
_PmLogGeneralLastChangeTime_Object = MibScalar
pmLogGeneralLastChangeTime = _PmLogGeneralLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 1),
    _PmLogGeneralLastChangeTime_Type()
)
pmLogGeneralLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmLogGeneralLastChangeTime.setStatus("current")


class _PmLogGeneralSize_Type(Unsigned32):
    """Custom type pmLogGeneralSize based on Unsigned32"""
    defaultValue = 32

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_PmLogGeneralSize_Type.__name__ = "Unsigned32"
_PmLogGeneralSize_Object = MibScalar
pmLogGeneralSize = _PmLogGeneralSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 2),
    _PmLogGeneralSize_Type()
)
pmLogGeneralSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmLogGeneralSize.setStatus("current")


class _PmLogGeneralSize24h_Type(Unsigned32):
    """Custom type pmLogGeneralSize24h based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_PmLogGeneralSize24h_Type.__name__ = "Unsigned32"
_PmLogGeneralSize24h_Object = MibScalar
pmLogGeneralSize24h = _PmLogGeneralSize24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 3),
    _PmLogGeneralSize24h_Type()
)
pmLogGeneralSize24h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmLogGeneralSize24h.setStatus("current")
_PmLogGeneralFileTableSize_Type = Unsigned32
_PmLogGeneralFileTableSize_Object = MibScalar
pmLogGeneralFileTableSize = _PmLogGeneralFileTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 4),
    _PmLogGeneralFileTableSize_Type()
)
pmLogGeneralFileTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmLogGeneralFileTableSize.setStatus("current")
_PmLogGeneralFile24hTableSize_Type = Unsigned32
_PmLogGeneralFile24hTableSize_Object = MibScalar
pmLogGeneralFile24hTableSize = _PmLogGeneralFile24hTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 5),
    _PmLogGeneralFile24hTableSize_Type()
)
pmLogGeneralFile24hTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmLogGeneralFile24hTableSize.setStatus("current")
_PmLogGeneralInterval15mTableSize_Type = Unsigned32
_PmLogGeneralInterval15mTableSize_Object = MibScalar
pmLogGeneralInterval15mTableSize = _PmLogGeneralInterval15mTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 6),
    _PmLogGeneralInterval15mTableSize_Type()
)
pmLogGeneralInterval15mTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmLogGeneralInterval15mTableSize.setStatus("deprecated")
_PmLogGeneralInterval24hTableSize_Type = Unsigned32
_PmLogGeneralInterval24hTableSize_Object = MibScalar
pmLogGeneralInterval24hTableSize = _PmLogGeneralInterval24hTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 7),
    _PmLogGeneralInterval24hTableSize_Type()
)
pmLogGeneralInterval24hTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmLogGeneralInterval24hTableSize.setStatus("deprecated")


class _PmLogGeneralInterval15mShowNonZeroOnly_Type(Integer32):
    """Custom type pmLogGeneralInterval15mShowNonZeroOnly based on Integer32"""
    defaultValue = 2

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


_PmLogGeneralInterval15mShowNonZeroOnly_Type.__name__ = "Integer32"
_PmLogGeneralInterval15mShowNonZeroOnly_Object = MibScalar
pmLogGeneralInterval15mShowNonZeroOnly = _PmLogGeneralInterval15mShowNonZeroOnly_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 8),
    _PmLogGeneralInterval15mShowNonZeroOnly_Type()
)
pmLogGeneralInterval15mShowNonZeroOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmLogGeneralInterval15mShowNonZeroOnly.setStatus("deprecated")


class _PmLogGeneralInterval24hShowNonZeroOnly_Type(Integer32):
    """Custom type pmLogGeneralInterval24hShowNonZeroOnly based on Integer32"""
    defaultValue = 2

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


_PmLogGeneralInterval24hShowNonZeroOnly_Type.__name__ = "Integer32"
_PmLogGeneralInterval24hShowNonZeroOnly_Object = MibScalar
pmLogGeneralInterval24hShowNonZeroOnly = _PmLogGeneralInterval24hShowNonZeroOnly_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 9),
    _PmLogGeneralInterval24hShowNonZeroOnly_Type()
)
pmLogGeneralInterval24hShowNonZeroOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmLogGeneralInterval24hShowNonZeroOnly.setStatus("deprecated")
_PmLogGeneralFile15mLastSeqNumber_Type = Counter32
_PmLogGeneralFile15mLastSeqNumber_Object = MibScalar
pmLogGeneralFile15mLastSeqNumber = _PmLogGeneralFile15mLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 10),
    _PmLogGeneralFile15mLastSeqNumber_Type()
)
pmLogGeneralFile15mLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmLogGeneralFile15mLastSeqNumber.setStatus("current")
_PmLogGeneralFile24hLastSeqNumber_Type = Counter32
_PmLogGeneralFile24hLastSeqNumber_Object = MibScalar
pmLogGeneralFile24hLastSeqNumber = _PmLogGeneralFile24hLastSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 7, 11),
    _PmLogGeneralFile24hLastSeqNumber_Type()
)
pmLogGeneralFile24hLastSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmLogGeneralFile24hLastSeqNumber.setStatus("current")
_PmFile24h_ObjectIdentity = ObjectIdentity
pmFile24h = _PmFile24h_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8)
)
_PmFile24hTable_Object = MibTable
pmFile24hTable = _PmFile24hTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1)
)
if mibBuilder.loadTexts:
    pmFile24hTable.setStatus("current")
_PmFile24hEntry_Object = MibTableRow
pmFile24hEntry = _PmFile24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1)
)
pmFile24hEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmFile24hIndex"),
)
if mibBuilder.loadTexts:
    pmFile24hEntry.setStatus("current")
_PmFile24hIndex_Type = PmInterval24hNumber
_PmFile24hIndex_Object = MibTableColumn
pmFile24hIndex = _PmFile24hIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1, 1),
    _PmFile24hIndex_Type()
)
pmFile24hIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFile24hIndex.setStatus("current")
_PmFile24hName_Type = DisplayString
_PmFile24hName_Object = MibTableColumn
pmFile24hName = _PmFile24hName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1, 2),
    _PmFile24hName_Type()
)
pmFile24hName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFile24hName.setStatus("current")
_PmFile24hCreatedTime_Type = DateAndTime
_PmFile24hCreatedTime_Object = MibTableColumn
pmFile24hCreatedTime = _PmFile24hCreatedTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1, 3),
    _PmFile24hCreatedTime_Type()
)
pmFile24hCreatedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFile24hCreatedTime.setStatus("current")
_PmFile24hSeqNumber_Type = Counter32
_PmFile24hSeqNumber_Object = MibTableColumn
pmFile24hSeqNumber = _PmFile24hSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1, 4),
    _PmFile24hSeqNumber_Type()
)
pmFile24hSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFile24hSeqNumber.setStatus("current")
_PmFile24hStartTime_Type = DateAndTime
_PmFile24hStartTime_Object = MibTableColumn
pmFile24hStartTime = _PmFile24hStartTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1, 5),
    _PmFile24hStartTime_Type()
)
pmFile24hStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFile24hStartTime.setStatus("current")
_PmFile24hStopTime_Type = DateAndTime
_PmFile24hStopTime_Object = MibTableColumn
pmFile24hStopTime = _PmFile24hStopTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1, 6),
    _PmFile24hStopTime_Type()
)
pmFile24hStopTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFile24hStopTime.setStatus("current")
_PmFile24hUrl_Type = DisplayString
_PmFile24hUrl_Object = MibTableColumn
pmFile24hUrl = _PmFile24hUrl_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 8, 1, 1, 7),
    _PmFile24hUrl_Type()
)
pmFile24hUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmFile24hUrl.setStatus("current")
_PmControl_ObjectIdentity = ObjectIdentity
pmControl = _PmControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 9)
)


class _PmControlReset15Min_Type(Integer32):
    """Custom type pmControlReset15Min based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmControlReset15Min_Type.__name__ = "Integer32"
_PmControlReset15Min_Object = MibScalar
pmControlReset15Min = _PmControlReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 9, 1),
    _PmControlReset15Min_Type()
)
pmControlReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmControlReset15Min.setStatus("current")


class _PmControlReset24H_Type(Integer32):
    """Custom type pmControlReset24H based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmControlReset24H_Type.__name__ = "Integer32"
_PmControlReset24H_Object = MibScalar
pmControlReset24H = _PmControlReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 9, 2),
    _PmControlReset24H_Type()
)
pmControlReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmControlReset24H.setStatus("current")


class _PmControlResetCont_Type(Integer32):
    """Custom type pmControlResetCont based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmControlResetCont_Type.__name__ = "Integer32"
_PmControlResetCont_Object = MibScalar
pmControlResetCont = _PmControlResetCont_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 9, 3),
    _PmControlResetCont_Type()
)
pmControlResetCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmControlResetCont.setStatus("current")
_PmEthTdList_ObjectIdentity = ObjectIdentity
pmEthTdList = _PmEthTdList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10)
)
_PmEthTdTable_Object = MibTable
pmEthTdTable = _PmEthTdTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1)
)
if mibBuilder.loadTexts:
    pmEthTdTable.setStatus("current")
_PmEthTdEntry_Object = MibTableRow
pmEthTdEntry = _PmEthTdEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1)
)
pmEthTdEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmEthTdIndex"),
)
if mibBuilder.loadTexts:
    pmEthTdEntry.setStatus("current")


class _PmEthTdIndex_Type(Unsigned32):
    """Custom type pmEthTdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmEthTdIndex_Type.__name__ = "Unsigned32"
_PmEthTdIndex_Object = MibTableColumn
pmEthTdIndex = _PmEthTdIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 1),
    _PmEthTdIndex_Type()
)
pmEthTdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdIndex.setStatus("current")
_PmEthTdName_Type = MgmtNameString
_PmEthTdName_Object = MibTableColumn
pmEthTdName = _PmEthTdName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 2),
    _PmEthTdName_Type()
)
pmEthTdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdName.setStatus("current")
_PmEthTdSubrack_Type = SubrackNumber
_PmEthTdSubrack_Object = MibTableColumn
pmEthTdSubrack = _PmEthTdSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 3),
    _PmEthTdSubrack_Type()
)
pmEthTdSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTdSubrack.setStatus("current")
_PmEthTdSlot_Type = SlotNumber
_PmEthTdSlot_Object = MibTableColumn
pmEthTdSlot = _PmEthTdSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 4),
    _PmEthTdSlot_Type()
)
pmEthTdSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTdSlot.setStatus("current")
_PmEthTdPort_Type = PortNumber
_PmEthTdPort_Object = MibTableColumn
pmEthTdPort = _PmEthTdPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 5),
    _PmEthTdPort_Type()
)
pmEthTdPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTdPort.setStatus("current")


class _PmEthTdPmReportMode_Type(Integer32):
    """Custom type pmEthTdPmReportMode based on Integer32"""
    defaultValue = 2

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


_PmEthTdPmReportMode_Type.__name__ = "Integer32"
_PmEthTdPmReportMode_Object = MibTableColumn
pmEthTdPmReportMode = _PmEthTdPmReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 6),
    _PmEthTdPmReportMode_Type()
)
pmEthTdPmReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdPmReportMode.setStatus("current")
_PmEthTdRxPort_Type = PortNumber
_PmEthTdRxPort_Object = MibTableColumn
pmEthTdRxPort = _PmEthTdRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 7),
    _PmEthTdRxPort_Type()
)
pmEthTdRxPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTdRxPort.setStatus("current")


class _PmEthTdReset15Min_Type(Integer32):
    """Custom type pmEthTdReset15Min based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthTdReset15Min_Type.__name__ = "Integer32"
_PmEthTdReset15Min_Object = MibTableColumn
pmEthTdReset15Min = _PmEthTdReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 8),
    _PmEthTdReset15Min_Type()
)
pmEthTdReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdReset15Min.setStatus("current")


class _PmEthTdReset24H_Type(Integer32):
    """Custom type pmEthTdReset24H based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthTdReset24H_Type.__name__ = "Integer32"
_PmEthTdReset24H_Object = MibTableColumn
pmEthTdReset24H = _PmEthTdReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 9),
    _PmEthTdReset24H_Type()
)
pmEthTdReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdReset24H.setStatus("current")


class _PmEthTdAdminStatus_Type(Integer32):
    """Custom type pmEthTdAdminStatus based on Integer32"""
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
        *(("down", 1),
          ("service", 2),
          ("up", 3))
    )


_PmEthTdAdminStatus_Type.__name__ = "Integer32"
_PmEthTdAdminStatus_Object = MibTableColumn
pmEthTdAdminStatus = _PmEthTdAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 10),
    _PmEthTdAdminStatus_Type()
)
pmEthTdAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdAdminStatus.setStatus("current")


class _PmEthTdOperStatus_Type(Integer32):
    """Custom type pmEthTdOperStatus based on Integer32"""
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
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_PmEthTdOperStatus_Type.__name__ = "Integer32"
_PmEthTdOperStatus_Object = MibTableColumn
pmEthTdOperStatus = _PmEthTdOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 11),
    _PmEthTdOperStatus_Type()
)
pmEthTdOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdOperStatus.setStatus("current")
_PmEthTdIsSuspect15Min_Type = TruthValue
_PmEthTdIsSuspect15Min_Object = MibTableColumn
pmEthTdIsSuspect15Min = _PmEthTdIsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 12),
    _PmEthTdIsSuspect15Min_Type()
)
pmEthTdIsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdIsSuspect15Min.setStatus("current")
_PmEthTdIsSuspect24h_Type = TruthValue
_PmEthTdIsSuspect24h_Object = MibTableColumn
pmEthTdIsSuspect24h = _PmEthTdIsSuspect24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 13),
    _PmEthTdIsSuspect24h_Type()
)
pmEthTdIsSuspect24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdIsSuspect24h.setStatus("current")
_PmEthTdCurrentRxUndersizedFrames_Type = Counter64
_PmEthTdCurrentRxUndersizedFrames_Object = MibTableColumn
pmEthTdCurrentRxUndersizedFrames = _PmEthTdCurrentRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 14),
    _PmEthTdCurrentRxUndersizedFrames_Type()
)
pmEthTdCurrentRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxUndersizedFrames.setStatus("current")
_PmEthTdCurrentRxOversizedFrames_Type = Counter64
_PmEthTdCurrentRxOversizedFrames_Object = MibTableColumn
pmEthTdCurrentRxOversizedFrames = _PmEthTdCurrentRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 15),
    _PmEthTdCurrentRxOversizedFrames_Type()
)
pmEthTdCurrentRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxOversizedFrames.setStatus("current")
_PmEthTdCurrentRxFragments_Type = Counter64
_PmEthTdCurrentRxFragments_Object = MibTableColumn
pmEthTdCurrentRxFragments = _PmEthTdCurrentRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 16),
    _PmEthTdCurrentRxFragments_Type()
)
pmEthTdCurrentRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxFragments.setStatus("current")
_PmEthTdCurrentRxFcsErrors_Type = Counter64
_PmEthTdCurrentRxFcsErrors_Object = MibTableColumn
pmEthTdCurrentRxFcsErrors = _PmEthTdCurrentRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 17),
    _PmEthTdCurrentRxFcsErrors_Type()
)
pmEthTdCurrentRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxFcsErrors.setStatus("current")
_PmEthTdCurrentRxInvalidCeVlanId_Type = Counter64
_PmEthTdCurrentRxInvalidCeVlanId_Object = MibTableColumn
pmEthTdCurrentRxInvalidCeVlanId = _PmEthTdCurrentRxInvalidCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 18),
    _PmEthTdCurrentRxInvalidCeVlanId_Type()
)
pmEthTdCurrentRxInvalidCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxInvalidCeVlanId.setStatus("current")
_PmEthTdCurrentTxOctets_Type = Counter64
_PmEthTdCurrentTxOctets_Object = MibTableColumn
pmEthTdCurrentTxOctets = _PmEthTdCurrentTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 19),
    _PmEthTdCurrentTxOctets_Type()
)
pmEthTdCurrentTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentTxOctets.setStatus("current")
_PmEthTdCurrentTxFrames_Type = Counter64
_PmEthTdCurrentTxFrames_Object = MibTableColumn
pmEthTdCurrentTxFrames = _PmEthTdCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 20),
    _PmEthTdCurrentTxFrames_Type()
)
pmEthTdCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentTxFrames.setStatus("current")
_PmEthTdCurrentTxUnicastFrames_Type = Counter64
_PmEthTdCurrentTxUnicastFrames_Object = MibTableColumn
pmEthTdCurrentTxUnicastFrames = _PmEthTdCurrentTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 21),
    _PmEthTdCurrentTxUnicastFrames_Type()
)
pmEthTdCurrentTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentTxUnicastFrames.setStatus("current")
_PmEthTdCurrentTxMulticastFrames_Type = Counter64
_PmEthTdCurrentTxMulticastFrames_Object = MibTableColumn
pmEthTdCurrentTxMulticastFrames = _PmEthTdCurrentTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 22),
    _PmEthTdCurrentTxMulticastFrames_Type()
)
pmEthTdCurrentTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentTxMulticastFrames.setStatus("current")
_PmEthTdCurrentTxBroadcastFrames_Type = Counter64
_PmEthTdCurrentTxBroadcastFrames_Object = MibTableColumn
pmEthTdCurrentTxBroadcastFrames = _PmEthTdCurrentTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 23),
    _PmEthTdCurrentTxBroadcastFrames_Type()
)
pmEthTdCurrentTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentTxBroadcastFrames.setStatus("current")
_PmEthTdCurrentRxOctets_Type = Counter64
_PmEthTdCurrentRxOctets_Object = MibTableColumn
pmEthTdCurrentRxOctets = _PmEthTdCurrentRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 24),
    _PmEthTdCurrentRxOctets_Type()
)
pmEthTdCurrentRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxOctets.setStatus("current")
_PmEthTdCurrentRxFrames_Type = Counter64
_PmEthTdCurrentRxFrames_Object = MibTableColumn
pmEthTdCurrentRxFrames = _PmEthTdCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 25),
    _PmEthTdCurrentRxFrames_Type()
)
pmEthTdCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxFrames.setStatus("current")
_PmEthTdCurrentRxUnicastFrames_Type = Counter64
_PmEthTdCurrentRxUnicastFrames_Object = MibTableColumn
pmEthTdCurrentRxUnicastFrames = _PmEthTdCurrentRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 26),
    _PmEthTdCurrentRxUnicastFrames_Type()
)
pmEthTdCurrentRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxUnicastFrames.setStatus("current")
_PmEthTdCurrentRxMulticastFrames_Type = Counter64
_PmEthTdCurrentRxMulticastFrames_Object = MibTableColumn
pmEthTdCurrentRxMulticastFrames = _PmEthTdCurrentRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 27),
    _PmEthTdCurrentRxMulticastFrames_Type()
)
pmEthTdCurrentRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxMulticastFrames.setStatus("current")
_PmEthTdCurrentRxBroadcastFrames_Type = Counter64
_PmEthTdCurrentRxBroadcastFrames_Object = MibTableColumn
pmEthTdCurrentRxBroadcastFrames = _PmEthTdCurrentRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 28),
    _PmEthTdCurrentRxBroadcastFrames_Type()
)
pmEthTdCurrentRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxBroadcastFrames.setStatus("current")
_PmEthTdCurrent24hRxUndersizedFrames_Type = Counter64
_PmEthTdCurrent24hRxUndersizedFrames_Object = MibTableColumn
pmEthTdCurrent24hRxUndersizedFrames = _PmEthTdCurrent24hRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 29),
    _PmEthTdCurrent24hRxUndersizedFrames_Type()
)
pmEthTdCurrent24hRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxUndersizedFrames.setStatus("current")
_PmEthTdCurrent24hRxOversizedFrames_Type = Counter64
_PmEthTdCurrent24hRxOversizedFrames_Object = MibTableColumn
pmEthTdCurrent24hRxOversizedFrames = _PmEthTdCurrent24hRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 30),
    _PmEthTdCurrent24hRxOversizedFrames_Type()
)
pmEthTdCurrent24hRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxOversizedFrames.setStatus("current")
_PmEthTdCurrent24hRxFragments_Type = Counter64
_PmEthTdCurrent24hRxFragments_Object = MibTableColumn
pmEthTdCurrent24hRxFragments = _PmEthTdCurrent24hRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 31),
    _PmEthTdCurrent24hRxFragments_Type()
)
pmEthTdCurrent24hRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxFragments.setStatus("current")
_PmEthTdCurrent24hRxFcsErrors_Type = Counter64
_PmEthTdCurrent24hRxFcsErrors_Object = MibTableColumn
pmEthTdCurrent24hRxFcsErrors = _PmEthTdCurrent24hRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 32),
    _PmEthTdCurrent24hRxFcsErrors_Type()
)
pmEthTdCurrent24hRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxFcsErrors.setStatus("current")
_PmEthTdCurrent24hRxInvalidCeVlanId_Type = Counter64
_PmEthTdCurrent24hRxInvalidCeVlanId_Object = MibTableColumn
pmEthTdCurrent24hRxInvalidCeVlanId = _PmEthTdCurrent24hRxInvalidCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 33),
    _PmEthTdCurrent24hRxInvalidCeVlanId_Type()
)
pmEthTdCurrent24hRxInvalidCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxInvalidCeVlanId.setStatus("current")
_PmEthTdCurrent24hTxOctets_Type = Counter64
_PmEthTdCurrent24hTxOctets_Object = MibTableColumn
pmEthTdCurrent24hTxOctets = _PmEthTdCurrent24hTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 34),
    _PmEthTdCurrent24hTxOctets_Type()
)
pmEthTdCurrent24hTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hTxOctets.setStatus("current")
_PmEthTdCurrent24hTxFrames_Type = Counter64
_PmEthTdCurrent24hTxFrames_Object = MibTableColumn
pmEthTdCurrent24hTxFrames = _PmEthTdCurrent24hTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 35),
    _PmEthTdCurrent24hTxFrames_Type()
)
pmEthTdCurrent24hTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hTxFrames.setStatus("current")
_PmEthTdCurrent24hTxUnicastFrames_Type = Counter64
_PmEthTdCurrent24hTxUnicastFrames_Object = MibTableColumn
pmEthTdCurrent24hTxUnicastFrames = _PmEthTdCurrent24hTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 36),
    _PmEthTdCurrent24hTxUnicastFrames_Type()
)
pmEthTdCurrent24hTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hTxUnicastFrames.setStatus("current")
_PmEthTdCurrent24hTxMulticastFrames_Type = Counter64
_PmEthTdCurrent24hTxMulticastFrames_Object = MibTableColumn
pmEthTdCurrent24hTxMulticastFrames = _PmEthTdCurrent24hTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 37),
    _PmEthTdCurrent24hTxMulticastFrames_Type()
)
pmEthTdCurrent24hTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hTxMulticastFrames.setStatus("current")
_PmEthTdCurrent24hTxBroadcastFrames_Type = Counter64
_PmEthTdCurrent24hTxBroadcastFrames_Object = MibTableColumn
pmEthTdCurrent24hTxBroadcastFrames = _PmEthTdCurrent24hTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 38),
    _PmEthTdCurrent24hTxBroadcastFrames_Type()
)
pmEthTdCurrent24hTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hTxBroadcastFrames.setStatus("current")
_PmEthTdCurrent24hRxOctets_Type = Counter64
_PmEthTdCurrent24hRxOctets_Object = MibTableColumn
pmEthTdCurrent24hRxOctets = _PmEthTdCurrent24hRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 39),
    _PmEthTdCurrent24hRxOctets_Type()
)
pmEthTdCurrent24hRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxOctets.setStatus("current")
_PmEthTdCurrent24hRxFrames_Type = Counter64
_PmEthTdCurrent24hRxFrames_Object = MibTableColumn
pmEthTdCurrent24hRxFrames = _PmEthTdCurrent24hRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 40),
    _PmEthTdCurrent24hRxFrames_Type()
)
pmEthTdCurrent24hRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxFrames.setStatus("current")
_PmEthTdCurrent24hRxUnicastFrames_Type = Counter64
_PmEthTdCurrent24hRxUnicastFrames_Object = MibTableColumn
pmEthTdCurrent24hRxUnicastFrames = _PmEthTdCurrent24hRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 41),
    _PmEthTdCurrent24hRxUnicastFrames_Type()
)
pmEthTdCurrent24hRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxUnicastFrames.setStatus("current")
_PmEthTdCurrent24hRxMulticastFrames_Type = Counter64
_PmEthTdCurrent24hRxMulticastFrames_Object = MibTableColumn
pmEthTdCurrent24hRxMulticastFrames = _PmEthTdCurrent24hRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 42),
    _PmEthTdCurrent24hRxMulticastFrames_Type()
)
pmEthTdCurrent24hRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxMulticastFrames.setStatus("current")
_PmEthTdCurrent24hRxBroadcastFrames_Type = Counter64
_PmEthTdCurrent24hRxBroadcastFrames_Object = MibTableColumn
pmEthTdCurrent24hRxBroadcastFrames = _PmEthTdCurrent24hRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 43),
    _PmEthTdCurrent24hRxBroadcastFrames_Type()
)
pmEthTdCurrent24hRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxBroadcastFrames.setStatus("current")
_PmEthTdObjectProperty_Type = ObjectProperty
_PmEthTdObjectProperty_Object = MibTableColumn
pmEthTdObjectProperty = _PmEthTdObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 44),
    _PmEthTdObjectProperty_Type()
)
pmEthTdObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdObjectProperty.setStatus("current")


class _PmEthTdRxUndersizedFramesThreshold_Type(Counter64):
    """Custom type pmEthTdRxUndersizedFramesThreshold based on Counter64"""
    defaultValue = 10


_PmEthTdRxUndersizedFramesThreshold_Type.__name__ = "Counter64"
_PmEthTdRxUndersizedFramesThreshold_Object = MibTableColumn
pmEthTdRxUndersizedFramesThreshold = _PmEthTdRxUndersizedFramesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 45),
    _PmEthTdRxUndersizedFramesThreshold_Type()
)
pmEthTdRxUndersizedFramesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdRxUndersizedFramesThreshold.setStatus("current")


class _PmEthTdRxOversizedFramesThreshold_Type(Counter64):
    """Custom type pmEthTdRxOversizedFramesThreshold based on Counter64"""
    defaultValue = 10


_PmEthTdRxOversizedFramesThreshold_Type.__name__ = "Counter64"
_PmEthTdRxOversizedFramesThreshold_Object = MibTableColumn
pmEthTdRxOversizedFramesThreshold = _PmEthTdRxOversizedFramesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 46),
    _PmEthTdRxOversizedFramesThreshold_Type()
)
pmEthTdRxOversizedFramesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdRxOversizedFramesThreshold.setStatus("current")


class _PmEthTdRxFragmentsThreshold_Type(Counter64):
    """Custom type pmEthTdRxFragmentsThreshold based on Counter64"""
    defaultValue = 10


_PmEthTdRxFragmentsThreshold_Type.__name__ = "Counter64"
_PmEthTdRxFragmentsThreshold_Object = MibTableColumn
pmEthTdRxFragmentsThreshold = _PmEthTdRxFragmentsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 47),
    _PmEthTdRxFragmentsThreshold_Type()
)
pmEthTdRxFragmentsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdRxFragmentsThreshold.setStatus("current")


class _PmEthTdRxFcsErrorsThreshold_Type(Counter64):
    """Custom type pmEthTdRxFcsErrorsThreshold based on Counter64"""
    defaultValue = 10


_PmEthTdRxFcsErrorsThreshold_Type.__name__ = "Counter64"
_PmEthTdRxFcsErrorsThreshold_Object = MibTableColumn
pmEthTdRxFcsErrorsThreshold = _PmEthTdRxFcsErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 48),
    _PmEthTdRxFcsErrorsThreshold_Type()
)
pmEthTdRxFcsErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdRxFcsErrorsThreshold.setStatus("current")


class _PmEthTdRxInvalidCeVlanIdThreshold_Type(Counter64):
    """Custom type pmEthTdRxInvalidCeVlanIdThreshold based on Counter64"""
    defaultValue = 10


_PmEthTdRxInvalidCeVlanIdThreshold_Type.__name__ = "Counter64"
_PmEthTdRxInvalidCeVlanIdThreshold_Object = MibTableColumn
pmEthTdRxInvalidCeVlanIdThreshold = _PmEthTdRxInvalidCeVlanIdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 49),
    _PmEthTdRxInvalidCeVlanIdThreshold_Type()
)
pmEthTdRxInvalidCeVlanIdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdRxInvalidCeVlanIdThreshold.setStatus("current")


class _PmEthTd24hRxUndersizedFramesThreshold_Type(Counter64):
    """Custom type pmEthTd24hRxUndersizedFramesThreshold based on Counter64"""
    defaultValue = 10


_PmEthTd24hRxUndersizedFramesThreshold_Type.__name__ = "Counter64"
_PmEthTd24hRxUndersizedFramesThreshold_Object = MibTableColumn
pmEthTd24hRxUndersizedFramesThreshold = _PmEthTd24hRxUndersizedFramesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 50),
    _PmEthTd24hRxUndersizedFramesThreshold_Type()
)
pmEthTd24hRxUndersizedFramesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTd24hRxUndersizedFramesThreshold.setStatus("current")


class _PmEthTd24hRxOversizedFramesThreshold_Type(Counter64):
    """Custom type pmEthTd24hRxOversizedFramesThreshold based on Counter64"""
    defaultValue = 10


_PmEthTd24hRxOversizedFramesThreshold_Type.__name__ = "Counter64"
_PmEthTd24hRxOversizedFramesThreshold_Object = MibTableColumn
pmEthTd24hRxOversizedFramesThreshold = _PmEthTd24hRxOversizedFramesThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 51),
    _PmEthTd24hRxOversizedFramesThreshold_Type()
)
pmEthTd24hRxOversizedFramesThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTd24hRxOversizedFramesThreshold.setStatus("current")


class _PmEthTd24hRxFragmentsThreshold_Type(Counter64):
    """Custom type pmEthTd24hRxFragmentsThreshold based on Counter64"""
    defaultValue = 10


_PmEthTd24hRxFragmentsThreshold_Type.__name__ = "Counter64"
_PmEthTd24hRxFragmentsThreshold_Object = MibTableColumn
pmEthTd24hRxFragmentsThreshold = _PmEthTd24hRxFragmentsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 52),
    _PmEthTd24hRxFragmentsThreshold_Type()
)
pmEthTd24hRxFragmentsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTd24hRxFragmentsThreshold.setStatus("current")


class _PmEthTd24hRxFcsErrorsThreshold_Type(Counter64):
    """Custom type pmEthTd24hRxFcsErrorsThreshold based on Counter64"""
    defaultValue = 10


_PmEthTd24hRxFcsErrorsThreshold_Type.__name__ = "Counter64"
_PmEthTd24hRxFcsErrorsThreshold_Object = MibTableColumn
pmEthTd24hRxFcsErrorsThreshold = _PmEthTd24hRxFcsErrorsThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 53),
    _PmEthTd24hRxFcsErrorsThreshold_Type()
)
pmEthTd24hRxFcsErrorsThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTd24hRxFcsErrorsThreshold.setStatus("current")


class _PmEthTd24hRxInvalidCeVlanIdThreshold_Type(Counter64):
    """Custom type pmEthTd24hRxInvalidCeVlanIdThreshold based on Counter64"""
    defaultValue = 10


_PmEthTd24hRxInvalidCeVlanIdThreshold_Type.__name__ = "Counter64"
_PmEthTd24hRxInvalidCeVlanIdThreshold_Object = MibTableColumn
pmEthTd24hRxInvalidCeVlanIdThreshold = _PmEthTd24hRxInvalidCeVlanIdThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 54),
    _PmEthTd24hRxInvalidCeVlanIdThreshold_Type()
)
pmEthTd24hRxInvalidCeVlanIdThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTd24hRxInvalidCeVlanIdThreshold.setStatus("current")
_PmEthTdRxUndersizedFrames_Type = FaultStatus
_PmEthTdRxUndersizedFrames_Object = MibTableColumn
pmEthTdRxUndersizedFrames = _PmEthTdRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 55),
    _PmEthTdRxUndersizedFrames_Type()
)
pmEthTdRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdRxUndersizedFrames.setStatus("current")
_PmEthTdRxOversizedFrames_Type = FaultStatus
_PmEthTdRxOversizedFrames_Object = MibTableColumn
pmEthTdRxOversizedFrames = _PmEthTdRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 56),
    _PmEthTdRxOversizedFrames_Type()
)
pmEthTdRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdRxOversizedFrames.setStatus("current")
_PmEthTdRxFragments_Type = FaultStatus
_PmEthTdRxFragments_Object = MibTableColumn
pmEthTdRxFragments = _PmEthTdRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 57),
    _PmEthTdRxFragments_Type()
)
pmEthTdRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdRxFragments.setStatus("current")
_PmEthTdRxFcsErrors_Type = FaultStatus
_PmEthTdRxFcsErrors_Object = MibTableColumn
pmEthTdRxFcsErrors = _PmEthTdRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 58),
    _PmEthTdRxFcsErrors_Type()
)
pmEthTdRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdRxFcsErrors.setStatus("current")
_PmEthTdRxInvalidCeVlanId_Type = FaultStatus
_PmEthTdRxInvalidCeVlanId_Object = MibTableColumn
pmEthTdRxInvalidCeVlanId = _PmEthTdRxInvalidCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 59),
    _PmEthTdRxInvalidCeVlanId_Type()
)
pmEthTdRxInvalidCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdRxInvalidCeVlanId.setStatus("current")
_PmEthTd24hRxUndersizedFrames_Type = FaultStatus
_PmEthTd24hRxUndersizedFrames_Object = MibTableColumn
pmEthTd24hRxUndersizedFrames = _PmEthTd24hRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 60),
    _PmEthTd24hRxUndersizedFrames_Type()
)
pmEthTd24hRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTd24hRxUndersizedFrames.setStatus("current")
_PmEthTd24hRxOversizedFrames_Type = FaultStatus
_PmEthTd24hRxOversizedFrames_Object = MibTableColumn
pmEthTd24hRxOversizedFrames = _PmEthTd24hRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 61),
    _PmEthTd24hRxOversizedFrames_Type()
)
pmEthTd24hRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTd24hRxOversizedFrames.setStatus("current")
_PmEthTd24hRxFragments_Type = FaultStatus
_PmEthTd24hRxFragments_Object = MibTableColumn
pmEthTd24hRxFragments = _PmEthTd24hRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 62),
    _PmEthTd24hRxFragments_Type()
)
pmEthTd24hRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTd24hRxFragments.setStatus("current")
_PmEthTd24hRxFcsErrors_Type = FaultStatus
_PmEthTd24hRxFcsErrors_Object = MibTableColumn
pmEthTd24hRxFcsErrors = _PmEthTd24hRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 63),
    _PmEthTd24hRxFcsErrors_Type()
)
pmEthTd24hRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTd24hRxFcsErrors.setStatus("current")
_PmEthTd24hRxInvalidCeVlanId_Type = FaultStatus
_PmEthTd24hRxInvalidCeVlanId_Object = MibTableColumn
pmEthTd24hRxInvalidCeVlanId = _PmEthTd24hRxInvalidCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 64),
    _PmEthTd24hRxInvalidCeVlanId_Type()
)
pmEthTd24hRxInvalidCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTd24hRxInvalidCeVlanId.setStatus("current")
_PmEthTdCurrentTxEthMaxUtilization_Type = Gauge32
_PmEthTdCurrentTxEthMaxUtilization_Object = MibTableColumn
pmEthTdCurrentTxEthMaxUtilization = _PmEthTdCurrentTxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 65),
    _PmEthTdCurrentTxEthMaxUtilization_Type()
)
pmEthTdCurrentTxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentTxEthMaxUtilization.setStatus("current")
_PmEthTdCurrentRxEthMaxUtilization_Type = Gauge32
_PmEthTdCurrentRxEthMaxUtilization_Object = MibTableColumn
pmEthTdCurrentRxEthMaxUtilization = _PmEthTdCurrentRxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 66),
    _PmEthTdCurrentRxEthMaxUtilization_Type()
)
pmEthTdCurrentRxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentRxEthMaxUtilization.setStatus("current")
_PmEthTdCurrent24hTxEthMaxUtilization_Type = Gauge32
_PmEthTdCurrent24hTxEthMaxUtilization_Object = MibTableColumn
pmEthTdCurrent24hTxEthMaxUtilization = _PmEthTdCurrent24hTxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 67),
    _PmEthTdCurrent24hTxEthMaxUtilization_Type()
)
pmEthTdCurrent24hTxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hTxEthMaxUtilization.setStatus("current")
_PmEthTdCurrent24hRxEthMaxUtilization_Type = Gauge32
_PmEthTdCurrent24hRxEthMaxUtilization_Object = MibTableColumn
pmEthTdCurrent24hRxEthMaxUtilization = _PmEthTdCurrent24hRxEthMaxUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 68),
    _PmEthTdCurrent24hRxEthMaxUtilization_Type()
)
pmEthTdCurrent24hRxEthMaxUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrent24hRxEthMaxUtilization.setStatus("current")


class _PmEthTdResetCont_Type(Integer32):
    """Custom type pmEthTdResetCont based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthTdResetCont_Type.__name__ = "Integer32"
_PmEthTdResetCont_Object = MibTableColumn
pmEthTdResetCont = _PmEthTdResetCont_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 69),
    _PmEthTdResetCont_Type()
)
pmEthTdResetCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTdResetCont.setStatus("current")
_PmEthTdCurrentContRxUndersizedFrames_Type = Counter64
_PmEthTdCurrentContRxUndersizedFrames_Object = MibTableColumn
pmEthTdCurrentContRxUndersizedFrames = _PmEthTdCurrentContRxUndersizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 70),
    _PmEthTdCurrentContRxUndersizedFrames_Type()
)
pmEthTdCurrentContRxUndersizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxUndersizedFrames.setStatus("current")
_PmEthTdCurrentContRxOversizedFrames_Type = Counter64
_PmEthTdCurrentContRxOversizedFrames_Object = MibTableColumn
pmEthTdCurrentContRxOversizedFrames = _PmEthTdCurrentContRxOversizedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 71),
    _PmEthTdCurrentContRxOversizedFrames_Type()
)
pmEthTdCurrentContRxOversizedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxOversizedFrames.setStatus("current")
_PmEthTdCurrentContRxFragments_Type = Counter64
_PmEthTdCurrentContRxFragments_Object = MibTableColumn
pmEthTdCurrentContRxFragments = _PmEthTdCurrentContRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 72),
    _PmEthTdCurrentContRxFragments_Type()
)
pmEthTdCurrentContRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxFragments.setStatus("current")
_PmEthTdCurrentContRxFcsErrors_Type = Counter64
_PmEthTdCurrentContRxFcsErrors_Object = MibTableColumn
pmEthTdCurrentContRxFcsErrors = _PmEthTdCurrentContRxFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 73),
    _PmEthTdCurrentContRxFcsErrors_Type()
)
pmEthTdCurrentContRxFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxFcsErrors.setStatus("current")
_PmEthTdCurrentContRxInvalidCeVlanId_Type = Counter64
_PmEthTdCurrentContRxInvalidCeVlanId_Object = MibTableColumn
pmEthTdCurrentContRxInvalidCeVlanId = _PmEthTdCurrentContRxInvalidCeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 74),
    _PmEthTdCurrentContRxInvalidCeVlanId_Type()
)
pmEthTdCurrentContRxInvalidCeVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxInvalidCeVlanId.setStatus("current")
_PmEthTdCurrentContTxOctets_Type = Counter64
_PmEthTdCurrentContTxOctets_Object = MibTableColumn
pmEthTdCurrentContTxOctets = _PmEthTdCurrentContTxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 75),
    _PmEthTdCurrentContTxOctets_Type()
)
pmEthTdCurrentContTxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContTxOctets.setStatus("current")
_PmEthTdCurrentContTxFrames_Type = Counter64
_PmEthTdCurrentContTxFrames_Object = MibTableColumn
pmEthTdCurrentContTxFrames = _PmEthTdCurrentContTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 76),
    _PmEthTdCurrentContTxFrames_Type()
)
pmEthTdCurrentContTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContTxFrames.setStatus("current")
_PmEthTdCurrentContTxUnicastFrames_Type = Counter64
_PmEthTdCurrentContTxUnicastFrames_Object = MibTableColumn
pmEthTdCurrentContTxUnicastFrames = _PmEthTdCurrentContTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 77),
    _PmEthTdCurrentContTxUnicastFrames_Type()
)
pmEthTdCurrentContTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContTxUnicastFrames.setStatus("current")
_PmEthTdCurrentContTxMulticastFrames_Type = Counter64
_PmEthTdCurrentContTxMulticastFrames_Object = MibTableColumn
pmEthTdCurrentContTxMulticastFrames = _PmEthTdCurrentContTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 78),
    _PmEthTdCurrentContTxMulticastFrames_Type()
)
pmEthTdCurrentContTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContTxMulticastFrames.setStatus("current")
_PmEthTdCurrentContTxBroadcastFrames_Type = Counter64
_PmEthTdCurrentContTxBroadcastFrames_Object = MibTableColumn
pmEthTdCurrentContTxBroadcastFrames = _PmEthTdCurrentContTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 79),
    _PmEthTdCurrentContTxBroadcastFrames_Type()
)
pmEthTdCurrentContTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContTxBroadcastFrames.setStatus("current")
_PmEthTdCurrentContRxOctets_Type = Counter64
_PmEthTdCurrentContRxOctets_Object = MibTableColumn
pmEthTdCurrentContRxOctets = _PmEthTdCurrentContRxOctets_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 80),
    _PmEthTdCurrentContRxOctets_Type()
)
pmEthTdCurrentContRxOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxOctets.setStatus("current")
_PmEthTdCurrentContRxFrames_Type = Counter64
_PmEthTdCurrentContRxFrames_Object = MibTableColumn
pmEthTdCurrentContRxFrames = _PmEthTdCurrentContRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 81),
    _PmEthTdCurrentContRxFrames_Type()
)
pmEthTdCurrentContRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxFrames.setStatus("current")
_PmEthTdCurrentContRxUnicastFrames_Type = Counter64
_PmEthTdCurrentContRxUnicastFrames_Object = MibTableColumn
pmEthTdCurrentContRxUnicastFrames = _PmEthTdCurrentContRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 82),
    _PmEthTdCurrentContRxUnicastFrames_Type()
)
pmEthTdCurrentContRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxUnicastFrames.setStatus("current")
_PmEthTdCurrentContRxMulticastFrames_Type = Counter64
_PmEthTdCurrentContRxMulticastFrames_Object = MibTableColumn
pmEthTdCurrentContRxMulticastFrames = _PmEthTdCurrentContRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 83),
    _PmEthTdCurrentContRxMulticastFrames_Type()
)
pmEthTdCurrentContRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxMulticastFrames.setStatus("current")
_PmEthTdCurrentContRxBroadcastFrames_Type = Counter64
_PmEthTdCurrentContRxBroadcastFrames_Object = MibTableColumn
pmEthTdCurrentContRxBroadcastFrames = _PmEthTdCurrentContRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 84),
    _PmEthTdCurrentContRxBroadcastFrames_Type()
)
pmEthTdCurrentContRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdCurrentContRxBroadcastFrames.setStatus("current")


class _PmEthTdVlanId_Type(Integer32):
    """Custom type pmEthTdVlanId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4094),
    )


_PmEthTdVlanId_Type.__name__ = "Integer32"
_PmEthTdVlanId_Object = MibTableColumn
pmEthTdVlanId = _PmEthTdVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 85),
    _PmEthTdVlanId_Type()
)
pmEthTdVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTdVlanId.setStatus("current")
_PmEthTdIfNo_Type = PortNumber
_PmEthTdIfNo_Object = MibTableColumn
pmEthTdIfNo = _PmEthTdIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 86),
    _PmEthTdIfNo_Type()
)
pmEthTdIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTdIfNo.setStatus("current")


class _PmEthTdUpPortId_Type(Integer32):
    """Custom type pmEthTdUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PmEthTdUpPortId_Type.__name__ = "Integer32"
_PmEthTdUpPortId_Object = MibTableColumn
pmEthTdUpPortId = _PmEthTdUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 10, 1, 1, 87),
    _PmEthTdUpPortId_Type()
)
pmEthTdUpPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTdUpPortId.setStatus("current")
_PmEthTmList_ObjectIdentity = ObjectIdentity
pmEthTmList = _PmEthTmList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11)
)
_PmEthTmTable_Object = MibTable
pmEthTmTable = _PmEthTmTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1)
)
if mibBuilder.loadTexts:
    pmEthTmTable.setStatus("obsolete")
_PmEthTmEntry_Object = MibTableRow
pmEthTmEntry = _PmEthTmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1)
)
pmEthTmEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmEthTmIndex"),
)
if mibBuilder.loadTexts:
    pmEthTmEntry.setStatus("current")


class _PmEthTmIndex_Type(Unsigned32):
    """Custom type pmEthTmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmEthTmIndex_Type.__name__ = "Unsigned32"
_PmEthTmIndex_Object = MibTableColumn
pmEthTmIndex = _PmEthTmIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 1),
    _PmEthTmIndex_Type()
)
pmEthTmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmIndex.setStatus("current")
_PmEthTmName_Type = MgmtNameString
_PmEthTmName_Object = MibTableColumn
pmEthTmName = _PmEthTmName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 2),
    _PmEthTmName_Type()
)
pmEthTmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmName.setStatus("current")
_PmEthTmSubrack_Type = SubrackNumber
_PmEthTmSubrack_Object = MibTableColumn
pmEthTmSubrack = _PmEthTmSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 3),
    _PmEthTmSubrack_Type()
)
pmEthTmSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmSubrack.setStatus("current")
_PmEthTmSlot_Type = SlotNumber
_PmEthTmSlot_Object = MibTableColumn
pmEthTmSlot = _PmEthTmSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 4),
    _PmEthTmSlot_Type()
)
pmEthTmSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmSlot.setStatus("current")
_PmEthTmPort_Type = PortNumber
_PmEthTmPort_Object = MibTableColumn
pmEthTmPort = _PmEthTmPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 5),
    _PmEthTmPort_Type()
)
pmEthTmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmPort.setStatus("current")


class _PmEthTmPmReportMode_Type(Integer32):
    """Custom type pmEthTmPmReportMode based on Integer32"""
    defaultValue = 2

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


_PmEthTmPmReportMode_Type.__name__ = "Integer32"
_PmEthTmPmReportMode_Object = MibTableColumn
pmEthTmPmReportMode = _PmEthTmPmReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 6),
    _PmEthTmPmReportMode_Type()
)
pmEthTmPmReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTmPmReportMode.setStatus("current")
_PmEthTmRxPort_Type = PortNumber
_PmEthTmRxPort_Object = MibTableColumn
pmEthTmRxPort = _PmEthTmRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 7),
    _PmEthTmRxPort_Type()
)
pmEthTmRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmRxPort.setStatus("current")


class _PmEthTmReset15Min_Type(Integer32):
    """Custom type pmEthTmReset15Min based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthTmReset15Min_Type.__name__ = "Integer32"
_PmEthTmReset15Min_Object = MibTableColumn
pmEthTmReset15Min = _PmEthTmReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 8),
    _PmEthTmReset15Min_Type()
)
pmEthTmReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTmReset15Min.setStatus("current")


class _PmEthTmReset24H_Type(Integer32):
    """Custom type pmEthTmReset24H based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthTmReset24H_Type.__name__ = "Integer32"
_PmEthTmReset24H_Object = MibTableColumn
pmEthTmReset24H = _PmEthTmReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 9),
    _PmEthTmReset24H_Type()
)
pmEthTmReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTmReset24H.setStatus("current")


class _PmEthTmAdminStatus_Type(Integer32):
    """Custom type pmEthTmAdminStatus based on Integer32"""
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
        *(("down", 1),
          ("service", 2),
          ("up", 3))
    )


_PmEthTmAdminStatus_Type.__name__ = "Integer32"
_PmEthTmAdminStatus_Object = MibTableColumn
pmEthTmAdminStatus = _PmEthTmAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 10),
    _PmEthTmAdminStatus_Type()
)
pmEthTmAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthTmAdminStatus.setStatus("current")


class _PmEthTmOperStatus_Type(Integer32):
    """Custom type pmEthTmOperStatus based on Integer32"""
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
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_PmEthTmOperStatus_Type.__name__ = "Integer32"
_PmEthTmOperStatus_Object = MibTableColumn
pmEthTmOperStatus = _PmEthTmOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 11),
    _PmEthTmOperStatus_Type()
)
pmEthTmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmOperStatus.setStatus("current")
_PmEthTmIsSuspect15Min_Type = TruthValue
_PmEthTmIsSuspect15Min_Object = MibTableColumn
pmEthTmIsSuspect15Min = _PmEthTmIsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 12),
    _PmEthTmIsSuspect15Min_Type()
)
pmEthTmIsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmIsSuspect15Min.setStatus("current")
_PmEthTmIsSuspect24h_Type = TruthValue
_PmEthTmIsSuspect24h_Object = MibTableColumn
pmEthTmIsSuspect24h = _PmEthTmIsSuspect24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 13),
    _PmEthTmIsSuspect24h_Type()
)
pmEthTmIsSuspect24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmIsSuspect24h.setStatus("current")
_PmEthTmCurrentIngressGreenFrameCount_Type = Counter64
_PmEthTmCurrentIngressGreenFrameCount_Object = MibTableColumn
pmEthTmCurrentIngressGreenFrameCount = _PmEthTmCurrentIngressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 14),
    _PmEthTmCurrentIngressGreenFrameCount_Type()
)
pmEthTmCurrentIngressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentIngressGreenFrameCount.setStatus("current")
_PmEthTmCurrentIngressYellowFrameCount_Type = Counter64
_PmEthTmCurrentIngressYellowFrameCount_Object = MibTableColumn
pmEthTmCurrentIngressYellowFrameCount = _PmEthTmCurrentIngressYellowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 15),
    _PmEthTmCurrentIngressYellowFrameCount_Type()
)
pmEthTmCurrentIngressYellowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentIngressYellowFrameCount.setStatus("current")
_PmEthTmCurrentIngressRedFrameCount_Type = Counter64
_PmEthTmCurrentIngressRedFrameCount_Object = MibTableColumn
pmEthTmCurrentIngressRedFrameCount = _PmEthTmCurrentIngressRedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 16),
    _PmEthTmCurrentIngressRedFrameCount_Type()
)
pmEthTmCurrentIngressRedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentIngressRedFrameCount.setStatus("current")
_PmEthTmCurrentIngressGreenOctetCount_Type = Counter64
_PmEthTmCurrentIngressGreenOctetCount_Object = MibTableColumn
pmEthTmCurrentIngressGreenOctetCount = _PmEthTmCurrentIngressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 17),
    _PmEthTmCurrentIngressGreenOctetCount_Type()
)
pmEthTmCurrentIngressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentIngressGreenOctetCount.setStatus("current")
_PmEthTmCurrentIngressYellowOctetCount_Type = Counter64
_PmEthTmCurrentIngressYellowOctetCount_Object = MibTableColumn
pmEthTmCurrentIngressYellowOctetCount = _PmEthTmCurrentIngressYellowOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 18),
    _PmEthTmCurrentIngressYellowOctetCount_Type()
)
pmEthTmCurrentIngressYellowOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentIngressYellowOctetCount.setStatus("current")
_PmEthTmCurrentIngressRedOctetCount_Type = Counter64
_PmEthTmCurrentIngressRedOctetCount_Object = MibTableColumn
pmEthTmCurrentIngressRedOctetCount = _PmEthTmCurrentIngressRedOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 19),
    _PmEthTmCurrentIngressRedOctetCount_Type()
)
pmEthTmCurrentIngressRedOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentIngressRedOctetCount.setStatus("current")
_PmEthTmCurrentEgressGreenFrameCount_Type = Counter64
_PmEthTmCurrentEgressGreenFrameCount_Object = MibTableColumn
pmEthTmCurrentEgressGreenFrameCount = _PmEthTmCurrentEgressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 20),
    _PmEthTmCurrentEgressGreenFrameCount_Type()
)
pmEthTmCurrentEgressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentEgressGreenFrameCount.setStatus("current")
_PmEthTmCurrentEgressGreenOctetCount_Type = Counter64
_PmEthTmCurrentEgressGreenOctetCount_Object = MibTableColumn
pmEthTmCurrentEgressGreenOctetCount = _PmEthTmCurrentEgressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 21),
    _PmEthTmCurrentEgressGreenOctetCount_Type()
)
pmEthTmCurrentEgressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentEgressGreenOctetCount.setStatus("current")
_PmEthTmCurrentGreenFrameDiscards_Type = Counter64
_PmEthTmCurrentGreenFrameDiscards_Object = MibTableColumn
pmEthTmCurrentGreenFrameDiscards = _PmEthTmCurrentGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 22),
    _PmEthTmCurrentGreenFrameDiscards_Type()
)
pmEthTmCurrentGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentGreenFrameDiscards.setStatus("current")
_PmEthTmCurrentYellowFrameDiscards_Type = Counter64
_PmEthTmCurrentYellowFrameDiscards_Object = MibTableColumn
pmEthTmCurrentYellowFrameDiscards = _PmEthTmCurrentYellowFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 23),
    _PmEthTmCurrentYellowFrameDiscards_Type()
)
pmEthTmCurrentYellowFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentYellowFrameDiscards.setStatus("current")
_PmEthTmCurrentGreenOctetDiscards_Type = Counter64
_PmEthTmCurrentGreenOctetDiscards_Object = MibTableColumn
pmEthTmCurrentGreenOctetDiscards = _PmEthTmCurrentGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 24),
    _PmEthTmCurrentGreenOctetDiscards_Type()
)
pmEthTmCurrentGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentGreenOctetDiscards.setStatus("current")
_PmEthTmCurrentYellowOctetDiscards_Type = Counter64
_PmEthTmCurrentYellowOctetDiscards_Object = MibTableColumn
pmEthTmCurrentYellowOctetDiscards = _PmEthTmCurrentYellowOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 25),
    _PmEthTmCurrentYellowOctetDiscards_Type()
)
pmEthTmCurrentYellowOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrentYellowOctetDiscards.setStatus("current")
_PmEthTmCurrent24hIngressGreenFrameCount_Type = Counter64
_PmEthTmCurrent24hIngressGreenFrameCount_Object = MibTableColumn
pmEthTmCurrent24hIngressGreenFrameCount = _PmEthTmCurrent24hIngressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 26),
    _PmEthTmCurrent24hIngressGreenFrameCount_Type()
)
pmEthTmCurrent24hIngressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hIngressGreenFrameCount.setStatus("current")
_PmEthTmCurrent24hIngressYellowFrameCount_Type = Counter64
_PmEthTmCurrent24hIngressYellowFrameCount_Object = MibTableColumn
pmEthTmCurrent24hIngressYellowFrameCount = _PmEthTmCurrent24hIngressYellowFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 27),
    _PmEthTmCurrent24hIngressYellowFrameCount_Type()
)
pmEthTmCurrent24hIngressYellowFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hIngressYellowFrameCount.setStatus("current")
_PmEthTmCurrent24hIngressRedFrameCount_Type = Counter64
_PmEthTmCurrent24hIngressRedFrameCount_Object = MibTableColumn
pmEthTmCurrent24hIngressRedFrameCount = _PmEthTmCurrent24hIngressRedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 28),
    _PmEthTmCurrent24hIngressRedFrameCount_Type()
)
pmEthTmCurrent24hIngressRedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hIngressRedFrameCount.setStatus("current")
_PmEthTmCurrent24hIngressGreenOctetCount_Type = Counter64
_PmEthTmCurrent24hIngressGreenOctetCount_Object = MibTableColumn
pmEthTmCurrent24hIngressGreenOctetCount = _PmEthTmCurrent24hIngressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 29),
    _PmEthTmCurrent24hIngressGreenOctetCount_Type()
)
pmEthTmCurrent24hIngressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hIngressGreenOctetCount.setStatus("current")
_PmEthTmCurrent24hIngressYellowOctetCount_Type = Counter64
_PmEthTmCurrent24hIngressYellowOctetCount_Object = MibTableColumn
pmEthTmCurrent24hIngressYellowOctetCount = _PmEthTmCurrent24hIngressYellowOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 30),
    _PmEthTmCurrent24hIngressYellowOctetCount_Type()
)
pmEthTmCurrent24hIngressYellowOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hIngressYellowOctetCount.setStatus("current")
_PmEthTmCurrent24hIngressRedOctetCount_Type = Counter64
_PmEthTmCurrent24hIngressRedOctetCount_Object = MibTableColumn
pmEthTmCurrent24hIngressRedOctetCount = _PmEthTmCurrent24hIngressRedOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 31),
    _PmEthTmCurrent24hIngressRedOctetCount_Type()
)
pmEthTmCurrent24hIngressRedOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hIngressRedOctetCount.setStatus("current")
_PmEthTmCurrent24hEgressGreenFrameCount_Type = Counter64
_PmEthTmCurrent24hEgressGreenFrameCount_Object = MibTableColumn
pmEthTmCurrent24hEgressGreenFrameCount = _PmEthTmCurrent24hEgressGreenFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 32),
    _PmEthTmCurrent24hEgressGreenFrameCount_Type()
)
pmEthTmCurrent24hEgressGreenFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hEgressGreenFrameCount.setStatus("current")
_PmEthTmCurrent24hEgressGreenOctetCount_Type = Counter64
_PmEthTmCurrent24hEgressGreenOctetCount_Object = MibTableColumn
pmEthTmCurrent24hEgressGreenOctetCount = _PmEthTmCurrent24hEgressGreenOctetCount_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 33),
    _PmEthTmCurrent24hEgressGreenOctetCount_Type()
)
pmEthTmCurrent24hEgressGreenOctetCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hEgressGreenOctetCount.setStatus("current")
_PmEthTmCurrent24hGreenFrameDiscards_Type = Counter64
_PmEthTmCurrent24hGreenFrameDiscards_Object = MibTableColumn
pmEthTmCurrent24hGreenFrameDiscards = _PmEthTmCurrent24hGreenFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 34),
    _PmEthTmCurrent24hGreenFrameDiscards_Type()
)
pmEthTmCurrent24hGreenFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hGreenFrameDiscards.setStatus("current")
_PmEthTmCurrent24hYellowFrameDiscards_Type = Counter64
_PmEthTmCurrent24hYellowFrameDiscards_Object = MibTableColumn
pmEthTmCurrent24hYellowFrameDiscards = _PmEthTmCurrent24hYellowFrameDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 35),
    _PmEthTmCurrent24hYellowFrameDiscards_Type()
)
pmEthTmCurrent24hYellowFrameDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hYellowFrameDiscards.setStatus("current")
_PmEthTmCurrent24hGreenOctetDiscards_Type = Counter64
_PmEthTmCurrent24hGreenOctetDiscards_Object = MibTableColumn
pmEthTmCurrent24hGreenOctetDiscards = _PmEthTmCurrent24hGreenOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 36),
    _PmEthTmCurrent24hGreenOctetDiscards_Type()
)
pmEthTmCurrent24hGreenOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hGreenOctetDiscards.setStatus("current")
_PmEthTmCurrent24hYellowOctetDiscards_Type = Counter64
_PmEthTmCurrent24hYellowOctetDiscards_Object = MibTableColumn
pmEthTmCurrent24hYellowOctetDiscards = _PmEthTmCurrent24hYellowOctetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 37),
    _PmEthTmCurrent24hYellowOctetDiscards_Type()
)
pmEthTmCurrent24hYellowOctetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmCurrent24hYellowOctetDiscards.setStatus("current")
_PmEthTmObjectProperty_Type = ObjectProperty
_PmEthTmObjectProperty_Object = MibTableColumn
pmEthTmObjectProperty = _PmEthTmObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 38),
    _PmEthTmObjectProperty_Type()
)
pmEthTmObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthTmObjectProperty.setStatus("current")


class _PmEthTmInternalReference_Type(Unsigned32):
    """Custom type pmEthTmInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PmEthTmInternalReference_Type.__name__ = "Unsigned32"
_PmEthTmInternalReference_Object = MibTableColumn
pmEthTmInternalReference = _PmEthTmInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 39),
    _PmEthTmInternalReference_Type()
)
pmEthTmInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTmInternalReference.setStatus("current")


class _PmEthTmIdentifier_Type(DisplayString):
    """Custom type pmEthTmIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_PmEthTmIdentifier_Type.__name__ = "DisplayString"
_PmEthTmIdentifier_Object = MibTableColumn
pmEthTmIdentifier = _PmEthTmIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 11, 1, 1, 40),
    _PmEthTmIdentifier_Type()
)
pmEthTmIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthTmIdentifier.setStatus("current")
_PmEthOamList_ObjectIdentity = ObjectIdentity
pmEthOamList = _PmEthOamList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12)
)
_PmEthOamTable_Object = MibTable
pmEthOamTable = _PmEthOamTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1)
)
if mibBuilder.loadTexts:
    pmEthOamTable.setStatus("obsolete")
_PmEthOamEntry_Object = MibTableRow
pmEthOamEntry = _PmEthOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1)
)
pmEthOamEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmEthOamIndex"),
)
if mibBuilder.loadTexts:
    pmEthOamEntry.setStatus("current")


class _PmEthOamIndex_Type(Unsigned32):
    """Custom type pmEthOamIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmEthOamIndex_Type.__name__ = "Unsigned32"
_PmEthOamIndex_Object = MibTableColumn
pmEthOamIndex = _PmEthOamIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 1),
    _PmEthOamIndex_Type()
)
pmEthOamIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamIndex.setStatus("current")
_PmEthOamName_Type = MgmtNameString
_PmEthOamName_Object = MibTableColumn
pmEthOamName = _PmEthOamName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 2),
    _PmEthOamName_Type()
)
pmEthOamName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamName.setStatus("current")
_PmEthOamSubrack_Type = SubrackNumber
_PmEthOamSubrack_Object = MibTableColumn
pmEthOamSubrack = _PmEthOamSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 3),
    _PmEthOamSubrack_Type()
)
pmEthOamSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamSubrack.setStatus("current")
_PmEthOamSlot_Type = SlotNumber
_PmEthOamSlot_Object = MibTableColumn
pmEthOamSlot = _PmEthOamSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 4),
    _PmEthOamSlot_Type()
)
pmEthOamSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamSlot.setStatus("current")
_PmEthOamPort_Type = PortNumber
_PmEthOamPort_Object = MibTableColumn
pmEthOamPort = _PmEthOamPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 5),
    _PmEthOamPort_Type()
)
pmEthOamPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamPort.setStatus("current")


class _PmEthOamPmReportMode_Type(Integer32):
    """Custom type pmEthOamPmReportMode based on Integer32"""
    defaultValue = 2

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


_PmEthOamPmReportMode_Type.__name__ = "Integer32"
_PmEthOamPmReportMode_Object = MibTableColumn
pmEthOamPmReportMode = _PmEthOamPmReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 6),
    _PmEthOamPmReportMode_Type()
)
pmEthOamPmReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthOamPmReportMode.setStatus("current")
_PmEthOamRxPort_Type = PortNumber
_PmEthOamRxPort_Object = MibTableColumn
pmEthOamRxPort = _PmEthOamRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 7),
    _PmEthOamRxPort_Type()
)
pmEthOamRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamRxPort.setStatus("current")


class _PmEthOamReset15Min_Type(Integer32):
    """Custom type pmEthOamReset15Min based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthOamReset15Min_Type.__name__ = "Integer32"
_PmEthOamReset15Min_Object = MibTableColumn
pmEthOamReset15Min = _PmEthOamReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 8),
    _PmEthOamReset15Min_Type()
)
pmEthOamReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthOamReset15Min.setStatus("current")


class _PmEthOamReset24H_Type(Integer32):
    """Custom type pmEthOamReset24H based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthOamReset24H_Type.__name__ = "Integer32"
_PmEthOamReset24H_Object = MibTableColumn
pmEthOamReset24H = _PmEthOamReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 9),
    _PmEthOamReset24H_Type()
)
pmEthOamReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthOamReset24H.setStatus("current")


class _PmEthOamAdminStatus_Type(Integer32):
    """Custom type pmEthOamAdminStatus based on Integer32"""
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
        *(("down", 1),
          ("service", 2),
          ("up", 3))
    )


_PmEthOamAdminStatus_Type.__name__ = "Integer32"
_PmEthOamAdminStatus_Object = MibTableColumn
pmEthOamAdminStatus = _PmEthOamAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 10),
    _PmEthOamAdminStatus_Type()
)
pmEthOamAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthOamAdminStatus.setStatus("current")


class _PmEthOamOperStatus_Type(Integer32):
    """Custom type pmEthOamOperStatus based on Integer32"""
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
        *(("notPresent", 1),
          ("down", 2),
          ("up", 3))
    )


_PmEthOamOperStatus_Type.__name__ = "Integer32"
_PmEthOamOperStatus_Object = MibTableColumn
pmEthOamOperStatus = _PmEthOamOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 11),
    _PmEthOamOperStatus_Type()
)
pmEthOamOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamOperStatus.setStatus("current")
_PmEthOamIsSuspect15Min_Type = TruthValue
_PmEthOamIsSuspect15Min_Object = MibTableColumn
pmEthOamIsSuspect15Min = _PmEthOamIsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 12),
    _PmEthOamIsSuspect15Min_Type()
)
pmEthOamIsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamIsSuspect15Min.setStatus("current")
_PmEthOamIsSuspect24h_Type = TruthValue
_PmEthOamIsSuspect24h_Object = MibTableColumn
pmEthOamIsSuspect24h = _PmEthOamIsSuspect24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 13),
    _PmEthOamIsSuspect24h_Type()
)
pmEthOamIsSuspect24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamIsSuspect24h.setStatus("current")
_PmEthOamCurrentTwoWayFrameDelay_Type = Gauge32
_PmEthOamCurrentTwoWayFrameDelay_Object = MibTableColumn
pmEthOamCurrentTwoWayFrameDelay = _PmEthOamCurrentTwoWayFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 14),
    _PmEthOamCurrentTwoWayFrameDelay_Type()
)
pmEthOamCurrentTwoWayFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrentTwoWayFrameDelay.setStatus("current")
_PmEthOamCurrentTwoWayFrameDelayVariation_Type = Gauge32
_PmEthOamCurrentTwoWayFrameDelayVariation_Object = MibTableColumn
pmEthOamCurrentTwoWayFrameDelayVariation = _PmEthOamCurrentTwoWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 15),
    _PmEthOamCurrentTwoWayFrameDelayVariation_Type()
)
pmEthOamCurrentTwoWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrentTwoWayFrameDelayVariation.setStatus("current")
_PmEthOamCurrentFrameLossRatioNearEnd_Type = Gauge32
_PmEthOamCurrentFrameLossRatioNearEnd_Object = MibTableColumn
pmEthOamCurrentFrameLossRatioNearEnd = _PmEthOamCurrentFrameLossRatioNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 16),
    _PmEthOamCurrentFrameLossRatioNearEnd_Type()
)
pmEthOamCurrentFrameLossRatioNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrentFrameLossRatioNearEnd.setStatus("current")
_PmEthOamCurrentFrameLossRatioFarEnd_Type = Gauge32
_PmEthOamCurrentFrameLossRatioFarEnd_Object = MibTableColumn
pmEthOamCurrentFrameLossRatioFarEnd = _PmEthOamCurrentFrameLossRatioFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 17),
    _PmEthOamCurrentFrameLossRatioFarEnd_Type()
)
pmEthOamCurrentFrameLossRatioFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrentFrameLossRatioFarEnd.setStatus("current")
_PmEthOamCurrentUnavailabilityNearEnd_Type = Gauge32
_PmEthOamCurrentUnavailabilityNearEnd_Object = MibTableColumn
pmEthOamCurrentUnavailabilityNearEnd = _PmEthOamCurrentUnavailabilityNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 18),
    _PmEthOamCurrentUnavailabilityNearEnd_Type()
)
pmEthOamCurrentUnavailabilityNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrentUnavailabilityNearEnd.setStatus("current")
_PmEthOamCurrentUnavailabilityFarEnd_Type = Gauge32
_PmEthOamCurrentUnavailabilityFarEnd_Object = MibTableColumn
pmEthOamCurrentUnavailabilityFarEnd = _PmEthOamCurrentUnavailabilityFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 19),
    _PmEthOamCurrentUnavailabilityFarEnd_Type()
)
pmEthOamCurrentUnavailabilityFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrentUnavailabilityFarEnd.setStatus("current")
_PmEthOamCurrent24hTwoWayFrameDelay_Type = Gauge32
_PmEthOamCurrent24hTwoWayFrameDelay_Object = MibTableColumn
pmEthOamCurrent24hTwoWayFrameDelay = _PmEthOamCurrent24hTwoWayFrameDelay_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 20),
    _PmEthOamCurrent24hTwoWayFrameDelay_Type()
)
pmEthOamCurrent24hTwoWayFrameDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrent24hTwoWayFrameDelay.setStatus("current")
_PmEthOamCurrent24hTwoWayFrameDelayVariation_Type = Gauge32
_PmEthOamCurrent24hTwoWayFrameDelayVariation_Object = MibTableColumn
pmEthOamCurrent24hTwoWayFrameDelayVariation = _PmEthOamCurrent24hTwoWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 21),
    _PmEthOamCurrent24hTwoWayFrameDelayVariation_Type()
)
pmEthOamCurrent24hTwoWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrent24hTwoWayFrameDelayVariation.setStatus("current")
_PmEthOamCurrent24hFrameLossRatioNearEnd_Type = Gauge32
_PmEthOamCurrent24hFrameLossRatioNearEnd_Object = MibTableColumn
pmEthOamCurrent24hFrameLossRatioNearEnd = _PmEthOamCurrent24hFrameLossRatioNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 22),
    _PmEthOamCurrent24hFrameLossRatioNearEnd_Type()
)
pmEthOamCurrent24hFrameLossRatioNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrent24hFrameLossRatioNearEnd.setStatus("current")
_PmEthOamCurrent24hFrameLossRatioFarEnd_Type = Gauge32
_PmEthOamCurrent24hFrameLossRatioFarEnd_Object = MibTableColumn
pmEthOamCurrent24hFrameLossRatioFarEnd = _PmEthOamCurrent24hFrameLossRatioFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 23),
    _PmEthOamCurrent24hFrameLossRatioFarEnd_Type()
)
pmEthOamCurrent24hFrameLossRatioFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrent24hFrameLossRatioFarEnd.setStatus("current")
_PmEthOamCurrent24hUnavailabilityNearEnd_Type = Gauge32
_PmEthOamCurrent24hUnavailabilityNearEnd_Object = MibTableColumn
pmEthOamCurrent24hUnavailabilityNearEnd = _PmEthOamCurrent24hUnavailabilityNearEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 24),
    _PmEthOamCurrent24hUnavailabilityNearEnd_Type()
)
pmEthOamCurrent24hUnavailabilityNearEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrent24hUnavailabilityNearEnd.setStatus("current")
_PmEthOamCurrent24hUnavailabilityFarEnd_Type = Gauge32
_PmEthOamCurrent24hUnavailabilityFarEnd_Object = MibTableColumn
pmEthOamCurrent24hUnavailabilityFarEnd = _PmEthOamCurrent24hUnavailabilityFarEnd_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 25),
    _PmEthOamCurrent24hUnavailabilityFarEnd_Type()
)
pmEthOamCurrent24hUnavailabilityFarEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrent24hUnavailabilityFarEnd.setStatus("current")
_PmEthOamObjectProperty_Type = ObjectProperty
_PmEthOamObjectProperty_Object = MibTableColumn
pmEthOamObjectProperty = _PmEthOamObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 26),
    _PmEthOamObjectProperty_Type()
)
pmEthOamObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamObjectProperty.setStatus("current")


class _PmEthOamInternalReference_Type(Unsigned32):
    """Custom type pmEthOamInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PmEthOamInternalReference_Type.__name__ = "Unsigned32"
_PmEthOamInternalReference_Object = MibTableColumn
pmEthOamInternalReference = _PmEthOamInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 27),
    _PmEthOamInternalReference_Type()
)
pmEthOamInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthOamInternalReference.setStatus("current")


class _PmEthOamIdentifier_Type(DisplayString):
    """Custom type pmEthOamIdentifier based on DisplayString"""
    defaultValue = OctetString("")


_PmEthOamIdentifier_Type.__name__ = "DisplayString"
_PmEthOamIdentifier_Object = MibTableColumn
pmEthOamIdentifier = _PmEthOamIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 28),
    _PmEthOamIdentifier_Type()
)
pmEthOamIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthOamIdentifier.setStatus("current")


class _PmEthOamUsedPercentOfFrames_Type(Unsigned32):
    """Custom type pmEthOamUsedPercentOfFrames based on Unsigned32"""
    defaultValue = 95

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_PmEthOamUsedPercentOfFrames_Type.__name__ = "Unsigned32"
_PmEthOamUsedPercentOfFrames_Object = MibTableColumn
pmEthOamUsedPercentOfFrames = _PmEthOamUsedPercentOfFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 29),
    _PmEthOamUsedPercentOfFrames_Type()
)
pmEthOamUsedPercentOfFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthOamUsedPercentOfFrames.setStatus("current")


class _PmEthOamFrameLossRatioUnavailableThreshold_Type(Unsigned32):
    """Custom type pmEthOamFrameLossRatioUnavailableThreshold based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_PmEthOamFrameLossRatioUnavailableThreshold_Type.__name__ = "Unsigned32"
_PmEthOamFrameLossRatioUnavailableThreshold_Object = MibTableColumn
pmEthOamFrameLossRatioUnavailableThreshold = _PmEthOamFrameLossRatioUnavailableThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 30),
    _PmEthOamFrameLossRatioUnavailableThreshold_Type()
)
pmEthOamFrameLossRatioUnavailableThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthOamFrameLossRatioUnavailableThreshold.setStatus("current")
_PmEthOamCurrentOneWayFrameDelayVariation_Type = Gauge32
_PmEthOamCurrentOneWayFrameDelayVariation_Object = MibTableColumn
pmEthOamCurrentOneWayFrameDelayVariation = _PmEthOamCurrentOneWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 31),
    _PmEthOamCurrentOneWayFrameDelayVariation_Type()
)
pmEthOamCurrentOneWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrentOneWayFrameDelayVariation.setStatus("current")
_PmEthOamCurrent24hOneWayFrameDelayVariation_Type = Gauge32
_PmEthOamCurrent24hOneWayFrameDelayVariation_Object = MibTableColumn
pmEthOamCurrent24hOneWayFrameDelayVariation = _PmEthOamCurrent24hOneWayFrameDelayVariation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 12, 1, 1, 32),
    _PmEthOamCurrent24hOneWayFrameDelayVariation_Type()
)
pmEthOamCurrent24hOneWayFrameDelayVariation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthOamCurrent24hOneWayFrameDelayVariation.setStatus("current")
_PmEthDropList_ObjectIdentity = ObjectIdentity
pmEthDropList = _PmEthDropList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13)
)
_PmEthDropTable_Object = MibTable
pmEthDropTable = _PmEthDropTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1)
)
if mibBuilder.loadTexts:
    pmEthDropTable.setStatus("current")
_PmEthDropEntry_Object = MibTableRow
pmEthDropEntry = _PmEthDropEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1)
)
pmEthDropEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmEthDropIndex"),
)
if mibBuilder.loadTexts:
    pmEthDropEntry.setStatus("current")


class _PmEthDropIndex_Type(Unsigned32):
    """Custom type pmEthDropIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmEthDropIndex_Type.__name__ = "Unsigned32"
_PmEthDropIndex_Object = MibTableColumn
pmEthDropIndex = _PmEthDropIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 1),
    _PmEthDropIndex_Type()
)
pmEthDropIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropIndex.setStatus("current")
_PmEthDropName_Type = MgmtNameString
_PmEthDropName_Object = MibTableColumn
pmEthDropName = _PmEthDropName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 2),
    _PmEthDropName_Type()
)
pmEthDropName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropName.setStatus("current")
_PmEthDropSubrack_Type = SubrackNumber
_PmEthDropSubrack_Object = MibTableColumn
pmEthDropSubrack = _PmEthDropSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 3),
    _PmEthDropSubrack_Type()
)
pmEthDropSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropSubrack.setStatus("current")
_PmEthDropSlot_Type = SlotNumber
_PmEthDropSlot_Object = MibTableColumn
pmEthDropSlot = _PmEthDropSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 4),
    _PmEthDropSlot_Type()
)
pmEthDropSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropSlot.setStatus("current")
_PmEthDropPort_Type = PortNumber
_PmEthDropPort_Object = MibTableColumn
pmEthDropPort = _PmEthDropPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 5),
    _PmEthDropPort_Type()
)
pmEthDropPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropPort.setStatus("current")
_PmEthDropRxPort_Type = PortNumber
_PmEthDropRxPort_Object = MibTableColumn
pmEthDropRxPort = _PmEthDropRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 6),
    _PmEthDropRxPort_Type()
)
pmEthDropRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropRxPort.setStatus("current")


class _PmEthDropResetCont_Type(Integer32):
    """Custom type pmEthDropResetCont based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthDropResetCont_Type.__name__ = "Integer32"
_PmEthDropResetCont_Object = MibTableColumn
pmEthDropResetCont = _PmEthDropResetCont_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 7),
    _PmEthDropResetCont_Type()
)
pmEthDropResetCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthDropResetCont.setStatus("current")
_PmEthDropFrames_Type = Counter64
_PmEthDropFrames_Object = MibTableColumn
pmEthDropFrames = _PmEthDropFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 8),
    _PmEthDropFrames_Type()
)
pmEthDropFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames.setStatus("current")
_PmEthDropBytes_Type = Counter64
_PmEthDropBytes_Object = MibTableColumn
pmEthDropBytes = _PmEthDropBytes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 9),
    _PmEthDropBytes_Type()
)
pmEthDropBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes.setStatus("current")
_PmEthDropYellowFrames_Type = Counter64
_PmEthDropYellowFrames_Object = MibTableColumn
pmEthDropYellowFrames = _PmEthDropYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 10),
    _PmEthDropYellowFrames_Type()
)
pmEthDropYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropYellowFrames.setStatus("current")
_PmEthDropRedFrames_Type = Counter64
_PmEthDropRedFrames_Object = MibTableColumn
pmEthDropRedFrames = _PmEthDropRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 11),
    _PmEthDropRedFrames_Type()
)
pmEthDropRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropRedFrames.setStatus("current")
_PmEthDropFramesQ1_Type = Counter64
_PmEthDropFramesQ1_Object = MibTableColumn
pmEthDropFramesQ1 = _PmEthDropFramesQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 12),
    _PmEthDropFramesQ1_Type()
)
pmEthDropFramesQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ1.setStatus("current")
_PmEthDropBytesQ1_Type = Counter64
_PmEthDropBytesQ1_Object = MibTableColumn
pmEthDropBytesQ1 = _PmEthDropBytesQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 13),
    _PmEthDropBytesQ1_Type()
)
pmEthDropBytesQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ1.setStatus("current")
_PmEthDropFramesQ2_Type = Counter64
_PmEthDropFramesQ2_Object = MibTableColumn
pmEthDropFramesQ2 = _PmEthDropFramesQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 14),
    _PmEthDropFramesQ2_Type()
)
pmEthDropFramesQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ2.setStatus("current")
_PmEthDropBytesQ2_Type = Counter64
_PmEthDropBytesQ2_Object = MibTableColumn
pmEthDropBytesQ2 = _PmEthDropBytesQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 15),
    _PmEthDropBytesQ2_Type()
)
pmEthDropBytesQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ2.setStatus("current")
_PmEthDropFramesQ3_Type = Counter64
_PmEthDropFramesQ3_Object = MibTableColumn
pmEthDropFramesQ3 = _PmEthDropFramesQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 16),
    _PmEthDropFramesQ3_Type()
)
pmEthDropFramesQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ3.setStatus("current")
_PmEthDropBytesQ3_Type = Counter64
_PmEthDropBytesQ3_Object = MibTableColumn
pmEthDropBytesQ3 = _PmEthDropBytesQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 17),
    _PmEthDropBytesQ3_Type()
)
pmEthDropBytesQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ3.setStatus("current")
_PmEthDropFramesQ4_Type = Counter64
_PmEthDropFramesQ4_Object = MibTableColumn
pmEthDropFramesQ4 = _PmEthDropFramesQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 18),
    _PmEthDropFramesQ4_Type()
)
pmEthDropFramesQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ4.setStatus("current")
_PmEthDropBytesQ4_Type = Counter64
_PmEthDropBytesQ4_Object = MibTableColumn
pmEthDropBytesQ4 = _PmEthDropBytesQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 19),
    _PmEthDropBytesQ4_Type()
)
pmEthDropBytesQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ4.setStatus("current")
_PmEthDropFramesQ5_Type = Counter64
_PmEthDropFramesQ5_Object = MibTableColumn
pmEthDropFramesQ5 = _PmEthDropFramesQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 20),
    _PmEthDropFramesQ5_Type()
)
pmEthDropFramesQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ5.setStatus("current")
_PmEthDropBytesQ5_Type = Counter64
_PmEthDropBytesQ5_Object = MibTableColumn
pmEthDropBytesQ5 = _PmEthDropBytesQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 21),
    _PmEthDropBytesQ5_Type()
)
pmEthDropBytesQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ5.setStatus("current")
_PmEthDropFramesQ6_Type = Counter64
_PmEthDropFramesQ6_Object = MibTableColumn
pmEthDropFramesQ6 = _PmEthDropFramesQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 22),
    _PmEthDropFramesQ6_Type()
)
pmEthDropFramesQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ6.setStatus("current")
_PmEthDropBytesQ6_Type = Counter64
_PmEthDropBytesQ6_Object = MibTableColumn
pmEthDropBytesQ6 = _PmEthDropBytesQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 23),
    _PmEthDropBytesQ6_Type()
)
pmEthDropBytesQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ6.setStatus("current")
_PmEthDropFramesQ7_Type = Counter64
_PmEthDropFramesQ7_Object = MibTableColumn
pmEthDropFramesQ7 = _PmEthDropFramesQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 24),
    _PmEthDropFramesQ7_Type()
)
pmEthDropFramesQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ7.setStatus("current")
_PmEthDropBytesQ7_Type = Counter64
_PmEthDropBytesQ7_Object = MibTableColumn
pmEthDropBytesQ7 = _PmEthDropBytesQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 25),
    _PmEthDropBytesQ7_Type()
)
pmEthDropBytesQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ7.setStatus("current")
_PmEthDropFramesQ8_Type = Counter64
_PmEthDropFramesQ8_Object = MibTableColumn
pmEthDropFramesQ8 = _PmEthDropFramesQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 26),
    _PmEthDropFramesQ8_Type()
)
pmEthDropFramesQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFramesQ8.setStatus("current")
_PmEthDropBytesQ8_Type = Counter64
_PmEthDropBytesQ8_Object = MibTableColumn
pmEthDropBytesQ8 = _PmEthDropBytesQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 27),
    _PmEthDropBytesQ8_Type()
)
pmEthDropBytesQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytesQ8.setStatus("current")
_PmEthDropIfNo_Type = PortNumber
_PmEthDropIfNo_Object = MibTableColumn
pmEthDropIfNo = _PmEthDropIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 28),
    _PmEthDropIfNo_Type()
)
pmEthDropIfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropIfNo.setStatus("current")


class _PmEthDropUpPortId_Type(Integer32):
    """Custom type pmEthDropUpPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PmEthDropUpPortId_Type.__name__ = "Integer32"
_PmEthDropUpPortId_Object = MibTableColumn
pmEthDropUpPortId = _PmEthDropUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 29),
    _PmEthDropUpPortId_Type()
)
pmEthDropUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropUpPortId.setStatus("current")
_PmEthDropFrames15m_Type = Counter64
_PmEthDropFrames15m_Object = MibTableColumn
pmEthDropFrames15m = _PmEthDropFrames15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 30),
    _PmEthDropFrames15m_Type()
)
pmEthDropFrames15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15m.setStatus("current")
_PmEthDropBytes15m_Type = Counter64
_PmEthDropBytes15m_Object = MibTableColumn
pmEthDropBytes15m = _PmEthDropBytes15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 31),
    _PmEthDropBytes15m_Type()
)
pmEthDropBytes15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15m.setStatus("current")
_PmEthDropYellowFrames15m_Type = Counter64
_PmEthDropYellowFrames15m_Object = MibTableColumn
pmEthDropYellowFrames15m = _PmEthDropYellowFrames15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 32),
    _PmEthDropYellowFrames15m_Type()
)
pmEthDropYellowFrames15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropYellowFrames15m.setStatus("current")
_PmEthDropRedFrames15m_Type = Counter64
_PmEthDropRedFrames15m_Object = MibTableColumn
pmEthDropRedFrames15m = _PmEthDropRedFrames15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 33),
    _PmEthDropRedFrames15m_Type()
)
pmEthDropRedFrames15m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropRedFrames15m.setStatus("current")
_PmEthDropFrames24h_Type = Counter64
_PmEthDropFrames24h_Object = MibTableColumn
pmEthDropFrames24h = _PmEthDropFrames24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 34),
    _PmEthDropFrames24h_Type()
)
pmEthDropFrames24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24h.setStatus("current")
_PmEthDropBytes24h_Type = Counter64
_PmEthDropBytes24h_Object = MibTableColumn
pmEthDropBytes24h = _PmEthDropBytes24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 35),
    _PmEthDropBytes24h_Type()
)
pmEthDropBytes24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24h.setStatus("current")
_PmEthDropYellowFrames24h_Type = Counter64
_PmEthDropYellowFrames24h_Object = MibTableColumn
pmEthDropYellowFrames24h = _PmEthDropYellowFrames24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 36),
    _PmEthDropYellowFrames24h_Type()
)
pmEthDropYellowFrames24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropYellowFrames24h.setStatus("current")
_PmEthDropRedFrames24h_Type = Counter64
_PmEthDropRedFrames24h_Object = MibTableColumn
pmEthDropRedFrames24h = _PmEthDropRedFrames24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 37),
    _PmEthDropRedFrames24h_Type()
)
pmEthDropRedFrames24h.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropRedFrames24h.setStatus("current")
_PmEthDropFrames15mQ1_Type = Counter64
_PmEthDropFrames15mQ1_Object = MibTableColumn
pmEthDropFrames15mQ1 = _PmEthDropFrames15mQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 38),
    _PmEthDropFrames15mQ1_Type()
)
pmEthDropFrames15mQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ1.setStatus("current")
_PmEthDropBytes15mQ1_Type = Counter64
_PmEthDropBytes15mQ1_Object = MibTableColumn
pmEthDropBytes15mQ1 = _PmEthDropBytes15mQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 39),
    _PmEthDropBytes15mQ1_Type()
)
pmEthDropBytes15mQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ1.setStatus("current")
_PmEthDropFrames24hQ1_Type = Counter64
_PmEthDropFrames24hQ1_Object = MibTableColumn
pmEthDropFrames24hQ1 = _PmEthDropFrames24hQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 40),
    _PmEthDropFrames24hQ1_Type()
)
pmEthDropFrames24hQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ1.setStatus("current")
_PmEthDropBytes24hQ1_Type = Counter64
_PmEthDropBytes24hQ1_Object = MibTableColumn
pmEthDropBytes24hQ1 = _PmEthDropBytes24hQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 41),
    _PmEthDropBytes24hQ1_Type()
)
pmEthDropBytes24hQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ1.setStatus("current")
_PmEthDropFrames15mQ2_Type = Counter64
_PmEthDropFrames15mQ2_Object = MibTableColumn
pmEthDropFrames15mQ2 = _PmEthDropFrames15mQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 42),
    _PmEthDropFrames15mQ2_Type()
)
pmEthDropFrames15mQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ2.setStatus("current")
_PmEthDropBytes15mQ2_Type = Counter64
_PmEthDropBytes15mQ2_Object = MibTableColumn
pmEthDropBytes15mQ2 = _PmEthDropBytes15mQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 43),
    _PmEthDropBytes15mQ2_Type()
)
pmEthDropBytes15mQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ2.setStatus("current")
_PmEthDropFrames24hQ2_Type = Counter64
_PmEthDropFrames24hQ2_Object = MibTableColumn
pmEthDropFrames24hQ2 = _PmEthDropFrames24hQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 44),
    _PmEthDropFrames24hQ2_Type()
)
pmEthDropFrames24hQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ2.setStatus("current")
_PmEthDropBytes24hQ2_Type = Counter64
_PmEthDropBytes24hQ2_Object = MibTableColumn
pmEthDropBytes24hQ2 = _PmEthDropBytes24hQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 45),
    _PmEthDropBytes24hQ2_Type()
)
pmEthDropBytes24hQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ2.setStatus("current")
_PmEthDropFrames15mQ3_Type = Counter64
_PmEthDropFrames15mQ3_Object = MibTableColumn
pmEthDropFrames15mQ3 = _PmEthDropFrames15mQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 46),
    _PmEthDropFrames15mQ3_Type()
)
pmEthDropFrames15mQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ3.setStatus("current")
_PmEthDropBytes15mQ3_Type = Counter64
_PmEthDropBytes15mQ3_Object = MibTableColumn
pmEthDropBytes15mQ3 = _PmEthDropBytes15mQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 47),
    _PmEthDropBytes15mQ3_Type()
)
pmEthDropBytes15mQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ3.setStatus("current")
_PmEthDropFrames24hQ3_Type = Counter64
_PmEthDropFrames24hQ3_Object = MibTableColumn
pmEthDropFrames24hQ3 = _PmEthDropFrames24hQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 48),
    _PmEthDropFrames24hQ3_Type()
)
pmEthDropFrames24hQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ3.setStatus("current")
_PmEthDropBytes24hQ3_Type = Counter64
_PmEthDropBytes24hQ3_Object = MibTableColumn
pmEthDropBytes24hQ3 = _PmEthDropBytes24hQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 49),
    _PmEthDropBytes24hQ3_Type()
)
pmEthDropBytes24hQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ3.setStatus("current")
_PmEthDropFrames15mQ4_Type = Counter64
_PmEthDropFrames15mQ4_Object = MibTableColumn
pmEthDropFrames15mQ4 = _PmEthDropFrames15mQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 50),
    _PmEthDropFrames15mQ4_Type()
)
pmEthDropFrames15mQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ4.setStatus("current")
_PmEthDropBytes15mQ4_Type = Counter64
_PmEthDropBytes15mQ4_Object = MibTableColumn
pmEthDropBytes15mQ4 = _PmEthDropBytes15mQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 51),
    _PmEthDropBytes15mQ4_Type()
)
pmEthDropBytes15mQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ4.setStatus("current")
_PmEthDropFrames24hQ4_Type = Counter64
_PmEthDropFrames24hQ4_Object = MibTableColumn
pmEthDropFrames24hQ4 = _PmEthDropFrames24hQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 52),
    _PmEthDropFrames24hQ4_Type()
)
pmEthDropFrames24hQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ4.setStatus("current")
_PmEthDropBytes24hQ4_Type = Counter64
_PmEthDropBytes24hQ4_Object = MibTableColumn
pmEthDropBytes24hQ4 = _PmEthDropBytes24hQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 53),
    _PmEthDropBytes24hQ4_Type()
)
pmEthDropBytes24hQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ4.setStatus("current")
_PmEthDropFrames15mQ5_Type = Counter64
_PmEthDropFrames15mQ5_Object = MibTableColumn
pmEthDropFrames15mQ5 = _PmEthDropFrames15mQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 54),
    _PmEthDropFrames15mQ5_Type()
)
pmEthDropFrames15mQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ5.setStatus("current")
_PmEthDropBytes15mQ5_Type = Counter64
_PmEthDropBytes15mQ5_Object = MibTableColumn
pmEthDropBytes15mQ5 = _PmEthDropBytes15mQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 55),
    _PmEthDropBytes15mQ5_Type()
)
pmEthDropBytes15mQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ5.setStatus("current")
_PmEthDropFrames24hQ5_Type = Counter64
_PmEthDropFrames24hQ5_Object = MibTableColumn
pmEthDropFrames24hQ5 = _PmEthDropFrames24hQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 56),
    _PmEthDropFrames24hQ5_Type()
)
pmEthDropFrames24hQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ5.setStatus("current")
_PmEthDropBytes24hQ5_Type = Counter64
_PmEthDropBytes24hQ5_Object = MibTableColumn
pmEthDropBytes24hQ5 = _PmEthDropBytes24hQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 57),
    _PmEthDropBytes24hQ5_Type()
)
pmEthDropBytes24hQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ5.setStatus("current")
_PmEthDropFrames15mQ6_Type = Counter64
_PmEthDropFrames15mQ6_Object = MibTableColumn
pmEthDropFrames15mQ6 = _PmEthDropFrames15mQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 58),
    _PmEthDropFrames15mQ6_Type()
)
pmEthDropFrames15mQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ6.setStatus("current")
_PmEthDropBytes15mQ6_Type = Counter64
_PmEthDropBytes15mQ6_Object = MibTableColumn
pmEthDropBytes15mQ6 = _PmEthDropBytes15mQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 59),
    _PmEthDropBytes15mQ6_Type()
)
pmEthDropBytes15mQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ6.setStatus("current")
_PmEthDropFrames24hQ6_Type = Counter64
_PmEthDropFrames24hQ6_Object = MibTableColumn
pmEthDropFrames24hQ6 = _PmEthDropFrames24hQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 60),
    _PmEthDropFrames24hQ6_Type()
)
pmEthDropFrames24hQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ6.setStatus("current")
_PmEthDropBytes24hQ6_Type = Counter64
_PmEthDropBytes24hQ6_Object = MibTableColumn
pmEthDropBytes24hQ6 = _PmEthDropBytes24hQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 61),
    _PmEthDropBytes24hQ6_Type()
)
pmEthDropBytes24hQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ6.setStatus("current")
_PmEthDropFrames15mQ7_Type = Counter64
_PmEthDropFrames15mQ7_Object = MibTableColumn
pmEthDropFrames15mQ7 = _PmEthDropFrames15mQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 62),
    _PmEthDropFrames15mQ7_Type()
)
pmEthDropFrames15mQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ7.setStatus("current")
_PmEthDropBytes15mQ7_Type = Counter64
_PmEthDropBytes15mQ7_Object = MibTableColumn
pmEthDropBytes15mQ7 = _PmEthDropBytes15mQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 63),
    _PmEthDropBytes15mQ7_Type()
)
pmEthDropBytes15mQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ7.setStatus("current")
_PmEthDropFrames24hQ7_Type = Counter64
_PmEthDropFrames24hQ7_Object = MibTableColumn
pmEthDropFrames24hQ7 = _PmEthDropFrames24hQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 64),
    _PmEthDropFrames24hQ7_Type()
)
pmEthDropFrames24hQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ7.setStatus("current")
_PmEthDropBytes24hQ7_Type = Counter64
_PmEthDropBytes24hQ7_Object = MibTableColumn
pmEthDropBytes24hQ7 = _PmEthDropBytes24hQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 65),
    _PmEthDropBytes24hQ7_Type()
)
pmEthDropBytes24hQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ7.setStatus("current")
_PmEthDropFrames15mQ8_Type = Counter64
_PmEthDropFrames15mQ8_Object = MibTableColumn
pmEthDropFrames15mQ8 = _PmEthDropFrames15mQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 66),
    _PmEthDropFrames15mQ8_Type()
)
pmEthDropFrames15mQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames15mQ8.setStatus("current")
_PmEthDropBytes15mQ8_Type = Counter64
_PmEthDropBytes15mQ8_Object = MibTableColumn
pmEthDropBytes15mQ8 = _PmEthDropBytes15mQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 67),
    _PmEthDropBytes15mQ8_Type()
)
pmEthDropBytes15mQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes15mQ8.setStatus("current")
_PmEthDropFrames24hQ8_Type = Counter64
_PmEthDropFrames24hQ8_Object = MibTableColumn
pmEthDropFrames24hQ8 = _PmEthDropFrames24hQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 68),
    _PmEthDropFrames24hQ8_Type()
)
pmEthDropFrames24hQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropFrames24hQ8.setStatus("current")
_PmEthDropBytes24hQ8_Type = Counter64
_PmEthDropBytes24hQ8_Object = MibTableColumn
pmEthDropBytes24hQ8 = _PmEthDropBytes24hQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 69),
    _PmEthDropBytes24hQ8_Type()
)
pmEthDropBytes24hQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropBytes24hQ8.setStatus("current")


class _PmEthDropReset15m_Type(Integer32):
    """Custom type pmEthDropReset15m based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthDropReset15m_Type.__name__ = "Integer32"
_PmEthDropReset15m_Object = MibTableColumn
pmEthDropReset15m = _PmEthDropReset15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 70),
    _PmEthDropReset15m_Type()
)
pmEthDropReset15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthDropReset15m.setStatus("current")


class _PmEthDropReset24h_Type(Integer32):
    """Custom type pmEthDropReset24h based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthDropReset24h_Type.__name__ = "Integer32"
_PmEthDropReset24h_Object = MibTableColumn
pmEthDropReset24h = _PmEthDropReset24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 71),
    _PmEthDropReset24h_Type()
)
pmEthDropReset24h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthDropReset24h.setStatus("current")


class _PmEthDropReportMode_Type(Integer32):
    """Custom type pmEthDropReportMode based on Integer32"""
    defaultValue = 2

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


_PmEthDropReportMode_Type.__name__ = "Integer32"
_PmEthDropReportMode_Object = MibTableColumn
pmEthDropReportMode = _PmEthDropReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 72),
    _PmEthDropReportMode_Type()
)
pmEthDropReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthDropReportMode.setStatus("current")
_PmEthDropIsSuspect15Min_Type = TruthValue
_PmEthDropIsSuspect15Min_Object = MibTableColumn
pmEthDropIsSuspect15Min = _PmEthDropIsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 73),
    _PmEthDropIsSuspect15Min_Type()
)
pmEthDropIsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropIsSuspect15Min.setStatus("current")
_PmEthDropIsSuspect24H_Type = TruthValue
_PmEthDropIsSuspect24H_Object = MibTableColumn
pmEthDropIsSuspect24H = _PmEthDropIsSuspect24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 13, 1, 1, 74),
    _PmEthDropIsSuspect24H_Type()
)
pmEthDropIsSuspect24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthDropIsSuspect24H.setStatus("current")
_PmEthClassificationList_ObjectIdentity = ObjectIdentity
pmEthClassificationList = _PmEthClassificationList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14)
)
_PmEthClassificationTable_Object = MibTable
pmEthClassificationTable = _PmEthClassificationTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1)
)
if mibBuilder.loadTexts:
    pmEthClassificationTable.setStatus("current")
_PmEthClassificationEntry_Object = MibTableRow
pmEthClassificationEntry = _PmEthClassificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1)
)
pmEthClassificationEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmEthClassificationIndex"),
)
if mibBuilder.loadTexts:
    pmEthClassificationEntry.setStatus("current")


class _PmEthClassificationIndex_Type(Unsigned32):
    """Custom type pmEthClassificationIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmEthClassificationIndex_Type.__name__ = "Unsigned32"
_PmEthClassificationIndex_Object = MibTableColumn
pmEthClassificationIndex = _PmEthClassificationIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 1),
    _PmEthClassificationIndex_Type()
)
pmEthClassificationIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationIndex.setStatus("current")
_PmEthClassificationName_Type = MgmtNameString
_PmEthClassificationName_Object = MibTableColumn
pmEthClassificationName = _PmEthClassificationName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 2),
    _PmEthClassificationName_Type()
)
pmEthClassificationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationName.setStatus("current")
_PmEthClassificationSubrack_Type = SubrackNumber
_PmEthClassificationSubrack_Object = MibTableColumn
pmEthClassificationSubrack = _PmEthClassificationSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 3),
    _PmEthClassificationSubrack_Type()
)
pmEthClassificationSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationSubrack.setStatus("current")
_PmEthClassificationSlot_Type = SlotNumber
_PmEthClassificationSlot_Object = MibTableColumn
pmEthClassificationSlot = _PmEthClassificationSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 4),
    _PmEthClassificationSlot_Type()
)
pmEthClassificationSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationSlot.setStatus("current")
_PmEthClassificationIdentifier_Type = DisplayString
_PmEthClassificationIdentifier_Object = MibTableColumn
pmEthClassificationIdentifier = _PmEthClassificationIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 5),
    _PmEthClassificationIdentifier_Type()
)
pmEthClassificationIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationIdentifier.setStatus("current")


class _PmEthClassificationResetCont_Type(Integer32):
    """Custom type pmEthClassificationResetCont based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthClassificationResetCont_Type.__name__ = "Integer32"
_PmEthClassificationResetCont_Object = MibTableColumn
pmEthClassificationResetCont = _PmEthClassificationResetCont_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 6),
    _PmEthClassificationResetCont_Type()
)
pmEthClassificationResetCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthClassificationResetCont.setStatus("current")


class _PmEthClassificationInternalReference_Type(Unsigned32):
    """Custom type pmEthClassificationInternalReference based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PmEthClassificationInternalReference_Type.__name__ = "Unsigned32"
_PmEthClassificationInternalReference_Object = MibTableColumn
pmEthClassificationInternalReference = _PmEthClassificationInternalReference_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 7),
    _PmEthClassificationInternalReference_Type()
)
pmEthClassificationInternalReference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmEthClassificationInternalReference.setStatus("current")
_PmEthClassificationCounter1_Type = Counter64
_PmEthClassificationCounter1_Object = MibTableColumn
pmEthClassificationCounter1 = _PmEthClassificationCounter1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 8),
    _PmEthClassificationCounter1_Type()
)
pmEthClassificationCounter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationCounter1.setStatus("current")
_PmEthClassificationCounter2_Type = Counter64
_PmEthClassificationCounter2_Object = MibTableColumn
pmEthClassificationCounter2 = _PmEthClassificationCounter2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 9),
    _PmEthClassificationCounter2_Type()
)
pmEthClassificationCounter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationCounter2.setStatus("current")
_PmEthClassificationCounter3_Type = Counter64
_PmEthClassificationCounter3_Object = MibTableColumn
pmEthClassificationCounter3 = _PmEthClassificationCounter3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 10),
    _PmEthClassificationCounter3_Type()
)
pmEthClassificationCounter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationCounter3.setStatus("current")
_PmEthClassificationCounter4_Type = Counter64
_PmEthClassificationCounter4_Object = MibTableColumn
pmEthClassificationCounter4 = _PmEthClassificationCounter4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 14, 1, 1, 11),
    _PmEthClassificationCounter4_Type()
)
pmEthClassificationCounter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthClassificationCounter4.setStatus("current")
_PmMpoLanesList_ObjectIdentity = ObjectIdentity
pmMpoLanesList = _PmMpoLanesList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15)
)
_PmMpoLanesTable_Object = MibTable
pmMpoLanesTable = _PmMpoLanesTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1)
)
if mibBuilder.loadTexts:
    pmMpoLanesTable.setStatus("current")
_PmMpoLanesEntry_Object = MibTableRow
pmMpoLanesEntry = _PmMpoLanesEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1)
)
pmMpoLanesEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmMpoLanesIndex"),
)
if mibBuilder.loadTexts:
    pmMpoLanesEntry.setStatus("current")


class _PmMpoLanesIndex_Type(Unsigned32):
    """Custom type pmMpoLanesIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmMpoLanesIndex_Type.__name__ = "Unsigned32"
_PmMpoLanesIndex_Object = MibTableColumn
pmMpoLanesIndex = _PmMpoLanesIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 1),
    _PmMpoLanesIndex_Type()
)
pmMpoLanesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesIndex.setStatus("current")
_PmMpoLanesName_Type = MgmtNameString
_PmMpoLanesName_Object = MibTableColumn
pmMpoLanesName = _PmMpoLanesName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 2),
    _PmMpoLanesName_Type()
)
pmMpoLanesName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesName.setStatus("current")
_PmMpoLanesSubrack_Type = SubrackNumber
_PmMpoLanesSubrack_Object = MibTableColumn
pmMpoLanesSubrack = _PmMpoLanesSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 3),
    _PmMpoLanesSubrack_Type()
)
pmMpoLanesSubrack.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmMpoLanesSubrack.setStatus("current")
_PmMpoLanesSlot_Type = SlotNumber
_PmMpoLanesSlot_Object = MibTableColumn
pmMpoLanesSlot = _PmMpoLanesSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 4),
    _PmMpoLanesSlot_Type()
)
pmMpoLanesSlot.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmMpoLanesSlot.setStatus("current")


class _PmMpoLanesLaneId_Type(Unsigned32):
    """Custom type pmMpoLanesLaneId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PmMpoLanesLaneId_Type.__name__ = "Unsigned32"
_PmMpoLanesLaneId_Object = MibTableColumn
pmMpoLanesLaneId = _PmMpoLanesLaneId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 5),
    _PmMpoLanesLaneId_Type()
)
pmMpoLanesLaneId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmMpoLanesLaneId.setStatus("current")


class _PmMpoLanesAdminStatus_Type(BoardOrInterfaceAdminStatus):
    """Custom type pmMpoLanesAdminStatus based on BoardOrInterfaceAdminStatus"""
    defaultValue = 3


_PmMpoLanesAdminStatus_Type.__name__ = "BoardOrInterfaceAdminStatus"
_PmMpoLanesAdminStatus_Object = MibTableColumn
pmMpoLanesAdminStatus = _PmMpoLanesAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 6),
    _PmMpoLanesAdminStatus_Type()
)
pmMpoLanesAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesAdminStatus.setStatus("current")


class _PmMpoLanesOperStatus_Type(BoardOrInterfaceOperStatus):
    """Custom type pmMpoLanesOperStatus based on BoardOrInterfaceOperStatus"""
    defaultValue = 1


_PmMpoLanesOperStatus_Type.__name__ = "BoardOrInterfaceOperStatus"
_PmMpoLanesOperStatus_Object = MibTableColumn
pmMpoLanesOperStatus = _PmMpoLanesOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 7),
    _PmMpoLanesOperStatus_Type()
)
pmMpoLanesOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesOperStatus.setStatus("current")


class _PmMpoLanesPmReportMode_Type(OnOff):
    """Custom type pmMpoLanesPmReportMode based on OnOff"""
    defaultValue = 2


_PmMpoLanesPmReportMode_Type.__name__ = "OnOff"
_PmMpoLanesPmReportMode_Object = MibTableColumn
pmMpoLanesPmReportMode = _PmMpoLanesPmReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 8),
    _PmMpoLanesPmReportMode_Type()
)
pmMpoLanesPmReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesPmReportMode.setStatus("current")
_PmMpoLanesIsSuspect15Min_Type = TruthValue
_PmMpoLanesIsSuspect15Min_Object = MibTableColumn
pmMpoLanesIsSuspect15Min = _PmMpoLanesIsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 9),
    _PmMpoLanesIsSuspect15Min_Type()
)
pmMpoLanesIsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesIsSuspect15Min.setStatus("current")
_PmMpoLanesIsSuspect24H_Type = TruthValue
_PmMpoLanesIsSuspect24H_Object = MibTableColumn
pmMpoLanesIsSuspect24H = _PmMpoLanesIsSuspect24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 10),
    _PmMpoLanesIsSuspect24H_Type()
)
pmMpoLanesIsSuspect24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesIsSuspect24H.setStatus("current")
_PmMpoLanesRxCurrentES_Type = Gauge32
_PmMpoLanesRxCurrentES_Object = MibTableColumn
pmMpoLanesRxCurrentES = _PmMpoLanesRxCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 11),
    _PmMpoLanesRxCurrentES_Type()
)
pmMpoLanesRxCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxCurrentES.setStatus("current")
_PmMpoLanesRxCurrentSES_Type = Gauge32
_PmMpoLanesRxCurrentSES_Object = MibTableColumn
pmMpoLanesRxCurrentSES = _PmMpoLanesRxCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 12),
    _PmMpoLanesRxCurrentSES_Type()
)
pmMpoLanesRxCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxCurrentSES.setStatus("current")
_PmMpoLanesRxCurrentBBE_Type = Gauge32
_PmMpoLanesRxCurrentBBE_Object = MibTableColumn
pmMpoLanesRxCurrentBBE = _PmMpoLanesRxCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 13),
    _PmMpoLanesRxCurrentBBE_Type()
)
pmMpoLanesRxCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxCurrentBBE.setStatus("current")
_PmMpoLanesRxCurrentUAS_Type = Gauge32
_PmMpoLanesRxCurrentUAS_Object = MibTableColumn
pmMpoLanesRxCurrentUAS = _PmMpoLanesRxCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 14),
    _PmMpoLanesRxCurrentUAS_Type()
)
pmMpoLanesRxCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxCurrentUAS.setStatus("current")
_PmMpoLanesTxCurrentES_Type = Gauge32
_PmMpoLanesTxCurrentES_Object = MibTableColumn
pmMpoLanesTxCurrentES = _PmMpoLanesTxCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 15),
    _PmMpoLanesTxCurrentES_Type()
)
pmMpoLanesTxCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxCurrentES.setStatus("current")
_PmMpoLanesTxCurrentSES_Type = Gauge32
_PmMpoLanesTxCurrentSES_Object = MibTableColumn
pmMpoLanesTxCurrentSES = _PmMpoLanesTxCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 16),
    _PmMpoLanesTxCurrentSES_Type()
)
pmMpoLanesTxCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxCurrentSES.setStatus("current")
_PmMpoLanesTxCurrentBBE_Type = Gauge32
_PmMpoLanesTxCurrentBBE_Object = MibTableColumn
pmMpoLanesTxCurrentBBE = _PmMpoLanesTxCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 17),
    _PmMpoLanesTxCurrentBBE_Type()
)
pmMpoLanesTxCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxCurrentBBE.setStatus("current")
_PmMpoLanesTxCurrentUAS_Type = Gauge32
_PmMpoLanesTxCurrentUAS_Object = MibTableColumn
pmMpoLanesTxCurrentUAS = _PmMpoLanesTxCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 18),
    _PmMpoLanesTxCurrentUAS_Type()
)
pmMpoLanesTxCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxCurrentUAS.setStatus("current")
_PmMpoLanesRx24hCurrentES_Type = Gauge32
_PmMpoLanesRx24hCurrentES_Object = MibTableColumn
pmMpoLanesRx24hCurrentES = _PmMpoLanesRx24hCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 19),
    _PmMpoLanesRx24hCurrentES_Type()
)
pmMpoLanesRx24hCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hCurrentES.setStatus("current")
_PmMpoLanesRx24hCurrentSES_Type = Gauge32
_PmMpoLanesRx24hCurrentSES_Object = MibTableColumn
pmMpoLanesRx24hCurrentSES = _PmMpoLanesRx24hCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 20),
    _PmMpoLanesRx24hCurrentSES_Type()
)
pmMpoLanesRx24hCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hCurrentSES.setStatus("current")
_PmMpoLanesRx24hCurrentBBE_Type = Gauge32
_PmMpoLanesRx24hCurrentBBE_Object = MibTableColumn
pmMpoLanesRx24hCurrentBBE = _PmMpoLanesRx24hCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 21),
    _PmMpoLanesRx24hCurrentBBE_Type()
)
pmMpoLanesRx24hCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hCurrentBBE.setStatus("current")
_PmMpoLanesRx24hCurrentUAS_Type = Gauge32
_PmMpoLanesRx24hCurrentUAS_Object = MibTableColumn
pmMpoLanesRx24hCurrentUAS = _PmMpoLanesRx24hCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 22),
    _PmMpoLanesRx24hCurrentUAS_Type()
)
pmMpoLanesRx24hCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hCurrentUAS.setStatus("current")
_PmMpoLanesTx24hCurrentES_Type = Gauge32
_PmMpoLanesTx24hCurrentES_Object = MibTableColumn
pmMpoLanesTx24hCurrentES = _PmMpoLanesTx24hCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 23),
    _PmMpoLanesTx24hCurrentES_Type()
)
pmMpoLanesTx24hCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hCurrentES.setStatus("current")
_PmMpoLanesTx24hCurrentSES_Type = Gauge32
_PmMpoLanesTx24hCurrentSES_Object = MibTableColumn
pmMpoLanesTx24hCurrentSES = _PmMpoLanesTx24hCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 24),
    _PmMpoLanesTx24hCurrentSES_Type()
)
pmMpoLanesTx24hCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hCurrentSES.setStatus("current")
_PmMpoLanesTx24hCurrentBBE_Type = Gauge32
_PmMpoLanesTx24hCurrentBBE_Object = MibTableColumn
pmMpoLanesTx24hCurrentBBE = _PmMpoLanesTx24hCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 25),
    _PmMpoLanesTx24hCurrentBBE_Type()
)
pmMpoLanesTx24hCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hCurrentBBE.setStatus("current")
_PmMpoLanesTx24hCurrentUAS_Type = Gauge32
_PmMpoLanesTx24hCurrentUAS_Object = MibTableColumn
pmMpoLanesTx24hCurrentUAS = _PmMpoLanesTx24hCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 26),
    _PmMpoLanesTx24hCurrentUAS_Type()
)
pmMpoLanesTx24hCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hCurrentUAS.setStatus("current")


class _PmMpoLanesRxESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRxESThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmMpoLanesRxESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRxESThreshold_Object = MibTableColumn
pmMpoLanesRxESThreshold = _PmMpoLanesRxESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 27),
    _PmMpoLanesRxESThreshold_Type()
)
pmMpoLanesRxESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRxESThreshold.setStatus("current")


class _PmMpoLanesRxSESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRxSESThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmMpoLanesRxSESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRxSESThreshold_Object = MibTableColumn
pmMpoLanesRxSESThreshold = _PmMpoLanesRxSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 28),
    _PmMpoLanesRxSESThreshold_Type()
)
pmMpoLanesRxSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRxSESThreshold.setStatus("current")


class _PmMpoLanesRxBBEThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRxBBEThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmMpoLanesRxBBEThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRxBBEThreshold_Object = MibTableColumn
pmMpoLanesRxBBEThreshold = _PmMpoLanesRxBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 29),
    _PmMpoLanesRxBBEThreshold_Type()
)
pmMpoLanesRxBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRxBBEThreshold.setStatus("current")


class _PmMpoLanesRxUASThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRxUASThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmMpoLanesRxUASThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRxUASThreshold_Object = MibTableColumn
pmMpoLanesRxUASThreshold = _PmMpoLanesRxUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 30),
    _PmMpoLanesRxUASThreshold_Type()
)
pmMpoLanesRxUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRxUASThreshold.setStatus("current")


class _PmMpoLanesTxESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTxESThreshold based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmMpoLanesTxESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTxESThreshold_Object = MibTableColumn
pmMpoLanesTxESThreshold = _PmMpoLanesTxESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 31),
    _PmMpoLanesTxESThreshold_Type()
)
pmMpoLanesTxESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTxESThreshold.setStatus("current")


class _PmMpoLanesTxSESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTxSESThreshold based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmMpoLanesTxSESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTxSESThreshold_Object = MibTableColumn
pmMpoLanesTxSESThreshold = _PmMpoLanesTxSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 32),
    _PmMpoLanesTxSESThreshold_Type()
)
pmMpoLanesTxSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTxSESThreshold.setStatus("current")


class _PmMpoLanesTxBBEThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTxBBEThreshold based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmMpoLanesTxBBEThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTxBBEThreshold_Object = MibTableColumn
pmMpoLanesTxBBEThreshold = _PmMpoLanesTxBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 33),
    _PmMpoLanesTxBBEThreshold_Type()
)
pmMpoLanesTxBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTxBBEThreshold.setStatus("current")


class _PmMpoLanesTxUASThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTxUASThreshold based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_PmMpoLanesTxUASThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTxUASThreshold_Object = MibTableColumn
pmMpoLanesTxUASThreshold = _PmMpoLanesTxUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 34),
    _PmMpoLanesTxUASThreshold_Type()
)
pmMpoLanesTxUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTxUASThreshold.setStatus("current")


class _PmMpoLanesRx24hESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRx24hESThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmMpoLanesRx24hESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRx24hESThreshold_Object = MibTableColumn
pmMpoLanesRx24hESThreshold = _PmMpoLanesRx24hESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 35),
    _PmMpoLanesRx24hESThreshold_Type()
)
pmMpoLanesRx24hESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hESThreshold.setStatus("current")


class _PmMpoLanesRx24hSESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRx24hSESThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmMpoLanesRx24hSESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRx24hSESThreshold_Object = MibTableColumn
pmMpoLanesRx24hSESThreshold = _PmMpoLanesRx24hSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 36),
    _PmMpoLanesRx24hSESThreshold_Type()
)
pmMpoLanesRx24hSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hSESThreshold.setStatus("current")


class _PmMpoLanesRx24hBBEThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRx24hBBEThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmMpoLanesRx24hBBEThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRx24hBBEThreshold_Object = MibTableColumn
pmMpoLanesRx24hBBEThreshold = _PmMpoLanesRx24hBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 37),
    _PmMpoLanesRx24hBBEThreshold_Type()
)
pmMpoLanesRx24hBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hBBEThreshold.setStatus("current")


class _PmMpoLanesRx24hUASThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesRx24hUASThreshold based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmMpoLanesRx24hUASThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesRx24hUASThreshold_Object = MibTableColumn
pmMpoLanesRx24hUASThreshold = _PmMpoLanesRx24hUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 38),
    _PmMpoLanesRx24hUASThreshold_Type()
)
pmMpoLanesRx24hUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hUASThreshold.setStatus("current")


class _PmMpoLanesTx24hESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTx24hESThreshold based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmMpoLanesTx24hESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTx24hESThreshold_Object = MibTableColumn
pmMpoLanesTx24hESThreshold = _PmMpoLanesTx24hESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 39),
    _PmMpoLanesTx24hESThreshold_Type()
)
pmMpoLanesTx24hESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hESThreshold.setStatus("current")


class _PmMpoLanesTx24hSESThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTx24hSESThreshold based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmMpoLanesTx24hSESThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTx24hSESThreshold_Object = MibTableColumn
pmMpoLanesTx24hSESThreshold = _PmMpoLanesTx24hSESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 40),
    _PmMpoLanesTx24hSESThreshold_Type()
)
pmMpoLanesTx24hSESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hSESThreshold.setStatus("current")


class _PmMpoLanesTx24hBBEThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTx24hBBEThreshold based on Unsigned32"""
    defaultValue = 1000000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_PmMpoLanesTx24hBBEThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTx24hBBEThreshold_Object = MibTableColumn
pmMpoLanesTx24hBBEThreshold = _PmMpoLanesTx24hBBEThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 41),
    _PmMpoLanesTx24hBBEThreshold_Type()
)
pmMpoLanesTx24hBBEThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hBBEThreshold.setStatus("current")


class _PmMpoLanesTx24hUASThreshold_Type(Unsigned32):
    """Custom type pmMpoLanesTx24hUASThreshold based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_PmMpoLanesTx24hUASThreshold_Type.__name__ = "Unsigned32"
_PmMpoLanesTx24hUASThreshold_Object = MibTableColumn
pmMpoLanesTx24hUASThreshold = _PmMpoLanesTx24hUASThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 42),
    _PmMpoLanesTx24hUASThreshold_Type()
)
pmMpoLanesTx24hUASThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hUASThreshold.setStatus("current")
_PmMpoLanesRxES_Type = FaultStatus
_PmMpoLanesRxES_Object = MibTableColumn
pmMpoLanesRxES = _PmMpoLanesRxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 43),
    _PmMpoLanesRxES_Type()
)
pmMpoLanesRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxES.setStatus("current")
_PmMpoLanesRxSES_Type = FaultStatus
_PmMpoLanesRxSES_Object = MibTableColumn
pmMpoLanesRxSES = _PmMpoLanesRxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 44),
    _PmMpoLanesRxSES_Type()
)
pmMpoLanesRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxSES.setStatus("current")
_PmMpoLanesRxBBE_Type = FaultStatus
_PmMpoLanesRxBBE_Object = MibTableColumn
pmMpoLanesRxBBE = _PmMpoLanesRxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 45),
    _PmMpoLanesRxBBE_Type()
)
pmMpoLanesRxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxBBE.setStatus("current")
_PmMpoLanesRxUAS_Type = FaultStatus
_PmMpoLanesRxUAS_Object = MibTableColumn
pmMpoLanesRxUAS = _PmMpoLanesRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 46),
    _PmMpoLanesRxUAS_Type()
)
pmMpoLanesRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxUAS.setStatus("current")
_PmMpoLanesTxES_Type = FaultStatus
_PmMpoLanesTxES_Object = MibTableColumn
pmMpoLanesTxES = _PmMpoLanesTxES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 47),
    _PmMpoLanesTxES_Type()
)
pmMpoLanesTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxES.setStatus("current")
_PmMpoLanesTxSES_Type = FaultStatus
_PmMpoLanesTxSES_Object = MibTableColumn
pmMpoLanesTxSES = _PmMpoLanesTxSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 48),
    _PmMpoLanesTxSES_Type()
)
pmMpoLanesTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxSES.setStatus("current")
_PmMpoLanesTxBBE_Type = FaultStatus
_PmMpoLanesTxBBE_Object = MibTableColumn
pmMpoLanesTxBBE = _PmMpoLanesTxBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 49),
    _PmMpoLanesTxBBE_Type()
)
pmMpoLanesTxBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxBBE.setStatus("current")
_PmMpoLanesTxUAS_Type = FaultStatus
_PmMpoLanesTxUAS_Object = MibTableColumn
pmMpoLanesTxUAS = _PmMpoLanesTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 50),
    _PmMpoLanesTxUAS_Type()
)
pmMpoLanesTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxUAS.setStatus("current")
_PmMpoLanesRx24hES_Type = FaultStatus
_PmMpoLanesRx24hES_Object = MibTableColumn
pmMpoLanesRx24hES = _PmMpoLanesRx24hES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 51),
    _PmMpoLanesRx24hES_Type()
)
pmMpoLanesRx24hES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hES.setStatus("current")
_PmMpoLanesRx24hSES_Type = FaultStatus
_PmMpoLanesRx24hSES_Object = MibTableColumn
pmMpoLanesRx24hSES = _PmMpoLanesRx24hSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 52),
    _PmMpoLanesRx24hSES_Type()
)
pmMpoLanesRx24hSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hSES.setStatus("current")
_PmMpoLanesRx24hBBE_Type = FaultStatus
_PmMpoLanesRx24hBBE_Object = MibTableColumn
pmMpoLanesRx24hBBE = _PmMpoLanesRx24hBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 53),
    _PmMpoLanesRx24hBBE_Type()
)
pmMpoLanesRx24hBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hBBE.setStatus("current")
_PmMpoLanesRx24hUAS_Type = FaultStatus
_PmMpoLanesRx24hUAS_Object = MibTableColumn
pmMpoLanesRx24hUAS = _PmMpoLanesRx24hUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 54),
    _PmMpoLanesRx24hUAS_Type()
)
pmMpoLanesRx24hUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRx24hUAS.setStatus("current")
_PmMpoLanesTx24hES_Type = FaultStatus
_PmMpoLanesTx24hES_Object = MibTableColumn
pmMpoLanesTx24hES = _PmMpoLanesTx24hES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 55),
    _PmMpoLanesTx24hES_Type()
)
pmMpoLanesTx24hES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hES.setStatus("current")
_PmMpoLanesTx24hSES_Type = FaultStatus
_PmMpoLanesTx24hSES_Object = MibTableColumn
pmMpoLanesTx24hSES = _PmMpoLanesTx24hSES_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 56),
    _PmMpoLanesTx24hSES_Type()
)
pmMpoLanesTx24hSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hSES.setStatus("current")
_PmMpoLanesTx24hBBE_Type = FaultStatus
_PmMpoLanesTx24hBBE_Object = MibTableColumn
pmMpoLanesTx24hBBE = _PmMpoLanesTx24hBBE_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 57),
    _PmMpoLanesTx24hBBE_Type()
)
pmMpoLanesTx24hBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hBBE.setStatus("current")
_PmMpoLanesTx24hUAS_Type = FaultStatus
_PmMpoLanesTx24hUAS_Object = MibTableColumn
pmMpoLanesTx24hUAS = _PmMpoLanesTx24hUAS_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 58),
    _PmMpoLanesTx24hUAS_Type()
)
pmMpoLanesTx24hUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTx24hUAS.setStatus("current")


class _PmMpoLanesReset15Min_Type(Integer32):
    """Custom type pmMpoLanesReset15Min based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmMpoLanesReset15Min_Type.__name__ = "Integer32"
_PmMpoLanesReset15Min_Object = MibTableColumn
pmMpoLanesReset15Min = _PmMpoLanesReset15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 59),
    _PmMpoLanesReset15Min_Type()
)
pmMpoLanesReset15Min.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesReset15Min.setStatus("current")


class _PmMpoLanesReset24H_Type(Integer32):
    """Custom type pmMpoLanesReset24H based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmMpoLanesReset24H_Type.__name__ = "Integer32"
_PmMpoLanesReset24H_Object = MibTableColumn
pmMpoLanesReset24H = _PmMpoLanesReset24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 60),
    _PmMpoLanesReset24H_Type()
)
pmMpoLanesReset24H.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmMpoLanesReset24H.setStatus("current")
_PmMpoLanesRxPowerLevel_Type = Integer32
_PmMpoLanesRxPowerLevel_Object = MibTableColumn
pmMpoLanesRxPowerLevel = _PmMpoLanesRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 61),
    _PmMpoLanesRxPowerLevel_Type()
)
pmMpoLanesRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesRxPowerLevel.setStatus("current")
_PmMpoLanesTxPowerLevel_Type = Integer32
_PmMpoLanesTxPowerLevel_Object = MibTableColumn
pmMpoLanesTxPowerLevel = _PmMpoLanesTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 62),
    _PmMpoLanesTxPowerLevel_Type()
)
pmMpoLanesTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesTxPowerLevel.setStatus("current")
_PmMpoLanesObjectProperty_Type = ObjectProperty
_PmMpoLanesObjectProperty_Object = MibTableColumn
pmMpoLanesObjectProperty = _PmMpoLanesObjectProperty_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 63),
    _PmMpoLanesObjectProperty_Type()
)
pmMpoLanesObjectProperty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmMpoLanesObjectProperty.setStatus("current")
_PmMpoLanesIfNo_Type = PortNumber
_PmMpoLanesIfNo_Object = MibTableColumn
pmMpoLanesIfNo = _PmMpoLanesIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 64),
    _PmMpoLanesIfNo_Type()
)
pmMpoLanesIfNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmMpoLanesIfNo.setStatus("current")


class _PmMpoLanesUpPortId_Type(Integer32):
    """Custom type pmMpoLanesUpPortId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PmMpoLanesUpPortId_Type.__name__ = "Integer32"
_PmMpoLanesUpPortId_Object = MibTableColumn
pmMpoLanesUpPortId = _PmMpoLanesUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 15, 1, 1, 65),
    _PmMpoLanesUpPortId_Type()
)
pmMpoLanesUpPortId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pmMpoLanesUpPortId.setStatus("current")
_PmEthEgressList_ObjectIdentity = ObjectIdentity
pmEthEgressList = _PmEthEgressList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16)
)
_PmEthEgressTable_Object = MibTable
pmEthEgressTable = _PmEthEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1)
)
if mibBuilder.loadTexts:
    pmEthEgressTable.setStatus("current")
_PmEthEgressEntry_Object = MibTableRow
pmEthEgressEntry = _PmEthEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1)
)
pmEthEgressEntry.setIndexNames(
    (0, "LUM-PM-MIB", "pmEthEgressIndex"),
)
if mibBuilder.loadTexts:
    pmEthEgressEntry.setStatus("current")


class _PmEthEgressIndex_Type(Unsigned32):
    """Custom type pmEthEgressIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PmEthEgressIndex_Type.__name__ = "Unsigned32"
_PmEthEgressIndex_Object = MibTableColumn
pmEthEgressIndex = _PmEthEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 1),
    _PmEthEgressIndex_Type()
)
pmEthEgressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressIndex.setStatus("current")
_PmEthEgressName_Type = MgmtNameString
_PmEthEgressName_Object = MibTableColumn
pmEthEgressName = _PmEthEgressName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 2),
    _PmEthEgressName_Type()
)
pmEthEgressName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressName.setStatus("current")
_PmEthEgressSubrack_Type = SubrackNumber
_PmEthEgressSubrack_Object = MibTableColumn
pmEthEgressSubrack = _PmEthEgressSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 3),
    _PmEthEgressSubrack_Type()
)
pmEthEgressSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressSubrack.setStatus("current")
_PmEthEgressSlot_Type = SlotNumber
_PmEthEgressSlot_Object = MibTableColumn
pmEthEgressSlot = _PmEthEgressSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 4),
    _PmEthEgressSlot_Type()
)
pmEthEgressSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressSlot.setStatus("current")
_PmEthEgressIfNo_Type = PortNumber
_PmEthEgressIfNo_Object = MibTableColumn
pmEthEgressIfNo = _PmEthEgressIfNo_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 5),
    _PmEthEgressIfNo_Type()
)
pmEthEgressIfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressIfNo.setStatus("current")
_PmEthEgressPort_Type = PortNumber
_PmEthEgressPort_Object = MibTableColumn
pmEthEgressPort = _PmEthEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 6),
    _PmEthEgressPort_Type()
)
pmEthEgressPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressPort.setStatus("current")
_PmEthEgressRxPort_Type = PortNumber
_PmEthEgressRxPort_Object = MibTableColumn
pmEthEgressRxPort = _PmEthEgressRxPort_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 7),
    _PmEthEgressRxPort_Type()
)
pmEthEgressRxPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressRxPort.setStatus("current")


class _PmEthEgressUpPortId_Type(Integer32):
    """Custom type pmEthEgressUpPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_PmEthEgressUpPortId_Type.__name__ = "Integer32"
_PmEthEgressUpPortId_Object = MibTableColumn
pmEthEgressUpPortId = _PmEthEgressUpPortId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 8),
    _PmEthEgressUpPortId_Type()
)
pmEthEgressUpPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressUpPortId.setStatus("current")


class _PmEthEgressResetCont_Type(Integer32):
    """Custom type pmEthEgressResetCont based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthEgressResetCont_Type.__name__ = "Integer32"
_PmEthEgressResetCont_Object = MibTableColumn
pmEthEgressResetCont = _PmEthEgressResetCont_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 9),
    _PmEthEgressResetCont_Type()
)
pmEthEgressResetCont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthEgressResetCont.setStatus("current")


class _PmEthEgressReset15m_Type(Integer32):
    """Custom type pmEthEgressReset15m based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthEgressReset15m_Type.__name__ = "Integer32"
_PmEthEgressReset15m_Object = MibTableColumn
pmEthEgressReset15m = _PmEthEgressReset15m_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 10),
    _PmEthEgressReset15m_Type()
)
pmEthEgressReset15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthEgressReset15m.setStatus("current")


class _PmEthEgressReset24h_Type(Integer32):
    """Custom type pmEthEgressReset24h based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_PmEthEgressReset24h_Type.__name__ = "Integer32"
_PmEthEgressReset24h_Object = MibTableColumn
pmEthEgressReset24h = _PmEthEgressReset24h_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 11),
    _PmEthEgressReset24h_Type()
)
pmEthEgressReset24h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthEgressReset24h.setStatus("current")
_PmEthEgressFramesQ1_Type = Counter64
_PmEthEgressFramesQ1_Object = MibTableColumn
pmEthEgressFramesQ1 = _PmEthEgressFramesQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 12),
    _PmEthEgressFramesQ1_Type()
)
pmEthEgressFramesQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ1.setStatus("current")
_PmEthEgressBytesQ1_Type = Counter64
_PmEthEgressBytesQ1_Object = MibTableColumn
pmEthEgressBytesQ1 = _PmEthEgressBytesQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 13),
    _PmEthEgressBytesQ1_Type()
)
pmEthEgressBytesQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ1.setStatus("current")
_PmEthEgressBandwidthQ1_Type = Counter64
_PmEthEgressBandwidthQ1_Object = MibTableColumn
pmEthEgressBandwidthQ1 = _PmEthEgressBandwidthQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 14),
    _PmEthEgressBandwidthQ1_Type()
)
pmEthEgressBandwidthQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ1.setStatus("current")
_PmEthEgressFrames15mQ1_Type = Counter64
_PmEthEgressFrames15mQ1_Object = MibTableColumn
pmEthEgressFrames15mQ1 = _PmEthEgressFrames15mQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 15),
    _PmEthEgressFrames15mQ1_Type()
)
pmEthEgressFrames15mQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ1.setStatus("current")
_PmEthEgressBytes15mQ1_Type = Counter64
_PmEthEgressBytes15mQ1_Object = MibTableColumn
pmEthEgressBytes15mQ1 = _PmEthEgressBytes15mQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 16),
    _PmEthEgressBytes15mQ1_Type()
)
pmEthEgressBytes15mQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ1.setStatus("current")
_PmEthEgressFrames24hQ1_Type = Counter64
_PmEthEgressFrames24hQ1_Object = MibTableColumn
pmEthEgressFrames24hQ1 = _PmEthEgressFrames24hQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 17),
    _PmEthEgressFrames24hQ1_Type()
)
pmEthEgressFrames24hQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ1.setStatus("current")
_PmEthEgressBytes24hQ1_Type = Counter64
_PmEthEgressBytes24hQ1_Object = MibTableColumn
pmEthEgressBytes24hQ1 = _PmEthEgressBytes24hQ1_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 18),
    _PmEthEgressBytes24hQ1_Type()
)
pmEthEgressBytes24hQ1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ1.setStatus("current")
_PmEthEgressFramesQ2_Type = Counter64
_PmEthEgressFramesQ2_Object = MibTableColumn
pmEthEgressFramesQ2 = _PmEthEgressFramesQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 19),
    _PmEthEgressFramesQ2_Type()
)
pmEthEgressFramesQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ2.setStatus("current")
_PmEthEgressBytesQ2_Type = Counter64
_PmEthEgressBytesQ2_Object = MibTableColumn
pmEthEgressBytesQ2 = _PmEthEgressBytesQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 20),
    _PmEthEgressBytesQ2_Type()
)
pmEthEgressBytesQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ2.setStatus("current")
_PmEthEgressBandwidthQ2_Type = Counter64
_PmEthEgressBandwidthQ2_Object = MibTableColumn
pmEthEgressBandwidthQ2 = _PmEthEgressBandwidthQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 21),
    _PmEthEgressBandwidthQ2_Type()
)
pmEthEgressBandwidthQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ2.setStatus("current")
_PmEthEgressFrames15mQ2_Type = Counter64
_PmEthEgressFrames15mQ2_Object = MibTableColumn
pmEthEgressFrames15mQ2 = _PmEthEgressFrames15mQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 22),
    _PmEthEgressFrames15mQ2_Type()
)
pmEthEgressFrames15mQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ2.setStatus("current")
_PmEthEgressBytes15mQ2_Type = Counter64
_PmEthEgressBytes15mQ2_Object = MibTableColumn
pmEthEgressBytes15mQ2 = _PmEthEgressBytes15mQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 23),
    _PmEthEgressBytes15mQ2_Type()
)
pmEthEgressBytes15mQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ2.setStatus("current")
_PmEthEgressFrames24hQ2_Type = Counter64
_PmEthEgressFrames24hQ2_Object = MibTableColumn
pmEthEgressFrames24hQ2 = _PmEthEgressFrames24hQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 24),
    _PmEthEgressFrames24hQ2_Type()
)
pmEthEgressFrames24hQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ2.setStatus("current")
_PmEthEgressBytes24hQ2_Type = Counter64
_PmEthEgressBytes24hQ2_Object = MibTableColumn
pmEthEgressBytes24hQ2 = _PmEthEgressBytes24hQ2_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 25),
    _PmEthEgressBytes24hQ2_Type()
)
pmEthEgressBytes24hQ2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ2.setStatus("current")
_PmEthEgressFramesQ3_Type = Counter64
_PmEthEgressFramesQ3_Object = MibTableColumn
pmEthEgressFramesQ3 = _PmEthEgressFramesQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 26),
    _PmEthEgressFramesQ3_Type()
)
pmEthEgressFramesQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ3.setStatus("current")
_PmEthEgressBytesQ3_Type = Counter64
_PmEthEgressBytesQ3_Object = MibTableColumn
pmEthEgressBytesQ3 = _PmEthEgressBytesQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 27),
    _PmEthEgressBytesQ3_Type()
)
pmEthEgressBytesQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ3.setStatus("current")
_PmEthEgressBandwidthQ3_Type = Counter64
_PmEthEgressBandwidthQ3_Object = MibTableColumn
pmEthEgressBandwidthQ3 = _PmEthEgressBandwidthQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 28),
    _PmEthEgressBandwidthQ3_Type()
)
pmEthEgressBandwidthQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ3.setStatus("current")
_PmEthEgressFrames15mQ3_Type = Counter64
_PmEthEgressFrames15mQ3_Object = MibTableColumn
pmEthEgressFrames15mQ3 = _PmEthEgressFrames15mQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 29),
    _PmEthEgressFrames15mQ3_Type()
)
pmEthEgressFrames15mQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ3.setStatus("current")
_PmEthEgressBytes15mQ3_Type = Counter64
_PmEthEgressBytes15mQ3_Object = MibTableColumn
pmEthEgressBytes15mQ3 = _PmEthEgressBytes15mQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 30),
    _PmEthEgressBytes15mQ3_Type()
)
pmEthEgressBytes15mQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ3.setStatus("current")
_PmEthEgressFrames24hQ3_Type = Counter64
_PmEthEgressFrames24hQ3_Object = MibTableColumn
pmEthEgressFrames24hQ3 = _PmEthEgressFrames24hQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 31),
    _PmEthEgressFrames24hQ3_Type()
)
pmEthEgressFrames24hQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ3.setStatus("current")
_PmEthEgressBytes24hQ3_Type = Counter64
_PmEthEgressBytes24hQ3_Object = MibTableColumn
pmEthEgressBytes24hQ3 = _PmEthEgressBytes24hQ3_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 32),
    _PmEthEgressBytes24hQ3_Type()
)
pmEthEgressBytes24hQ3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ3.setStatus("current")
_PmEthEgressFramesQ4_Type = Counter64
_PmEthEgressFramesQ4_Object = MibTableColumn
pmEthEgressFramesQ4 = _PmEthEgressFramesQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 33),
    _PmEthEgressFramesQ4_Type()
)
pmEthEgressFramesQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ4.setStatus("current")
_PmEthEgressBytesQ4_Type = Counter64
_PmEthEgressBytesQ4_Object = MibTableColumn
pmEthEgressBytesQ4 = _PmEthEgressBytesQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 34),
    _PmEthEgressBytesQ4_Type()
)
pmEthEgressBytesQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ4.setStatus("current")
_PmEthEgressBandwidthQ4_Type = Counter64
_PmEthEgressBandwidthQ4_Object = MibTableColumn
pmEthEgressBandwidthQ4 = _PmEthEgressBandwidthQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 35),
    _PmEthEgressBandwidthQ4_Type()
)
pmEthEgressBandwidthQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ4.setStatus("current")
_PmEthEgressFrames15mQ4_Type = Counter64
_PmEthEgressFrames15mQ4_Object = MibTableColumn
pmEthEgressFrames15mQ4 = _PmEthEgressFrames15mQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 36),
    _PmEthEgressFrames15mQ4_Type()
)
pmEthEgressFrames15mQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ4.setStatus("current")
_PmEthEgressBytes15mQ4_Type = Counter64
_PmEthEgressBytes15mQ4_Object = MibTableColumn
pmEthEgressBytes15mQ4 = _PmEthEgressBytes15mQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 37),
    _PmEthEgressBytes15mQ4_Type()
)
pmEthEgressBytes15mQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ4.setStatus("current")
_PmEthEgressFrames24hQ4_Type = Counter64
_PmEthEgressFrames24hQ4_Object = MibTableColumn
pmEthEgressFrames24hQ4 = _PmEthEgressFrames24hQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 38),
    _PmEthEgressFrames24hQ4_Type()
)
pmEthEgressFrames24hQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ4.setStatus("current")
_PmEthEgressBytes24hQ4_Type = Counter64
_PmEthEgressBytes24hQ4_Object = MibTableColumn
pmEthEgressBytes24hQ4 = _PmEthEgressBytes24hQ4_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 39),
    _PmEthEgressBytes24hQ4_Type()
)
pmEthEgressBytes24hQ4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ4.setStatus("current")
_PmEthEgressFramesQ5_Type = Counter64
_PmEthEgressFramesQ5_Object = MibTableColumn
pmEthEgressFramesQ5 = _PmEthEgressFramesQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 40),
    _PmEthEgressFramesQ5_Type()
)
pmEthEgressFramesQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ5.setStatus("current")
_PmEthEgressBytesQ5_Type = Counter64
_PmEthEgressBytesQ5_Object = MibTableColumn
pmEthEgressBytesQ5 = _PmEthEgressBytesQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 41),
    _PmEthEgressBytesQ5_Type()
)
pmEthEgressBytesQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ5.setStatus("current")
_PmEthEgressBandwidthQ5_Type = Counter64
_PmEthEgressBandwidthQ5_Object = MibTableColumn
pmEthEgressBandwidthQ5 = _PmEthEgressBandwidthQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 42),
    _PmEthEgressBandwidthQ5_Type()
)
pmEthEgressBandwidthQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ5.setStatus("current")
_PmEthEgressFrames15mQ5_Type = Counter64
_PmEthEgressFrames15mQ5_Object = MibTableColumn
pmEthEgressFrames15mQ5 = _PmEthEgressFrames15mQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 43),
    _PmEthEgressFrames15mQ5_Type()
)
pmEthEgressFrames15mQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ5.setStatus("current")
_PmEthEgressBytes15mQ5_Type = Counter64
_PmEthEgressBytes15mQ5_Object = MibTableColumn
pmEthEgressBytes15mQ5 = _PmEthEgressBytes15mQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 44),
    _PmEthEgressBytes15mQ5_Type()
)
pmEthEgressBytes15mQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ5.setStatus("current")
_PmEthEgressFrames24hQ5_Type = Counter64
_PmEthEgressFrames24hQ5_Object = MibTableColumn
pmEthEgressFrames24hQ5 = _PmEthEgressFrames24hQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 45),
    _PmEthEgressFrames24hQ5_Type()
)
pmEthEgressFrames24hQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ5.setStatus("current")
_PmEthEgressBytes24hQ5_Type = Counter64
_PmEthEgressBytes24hQ5_Object = MibTableColumn
pmEthEgressBytes24hQ5 = _PmEthEgressBytes24hQ5_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 46),
    _PmEthEgressBytes24hQ5_Type()
)
pmEthEgressBytes24hQ5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ5.setStatus("current")
_PmEthEgressFramesQ6_Type = Counter64
_PmEthEgressFramesQ6_Object = MibTableColumn
pmEthEgressFramesQ6 = _PmEthEgressFramesQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 47),
    _PmEthEgressFramesQ6_Type()
)
pmEthEgressFramesQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ6.setStatus("current")
_PmEthEgressBytesQ6_Type = Counter64
_PmEthEgressBytesQ6_Object = MibTableColumn
pmEthEgressBytesQ6 = _PmEthEgressBytesQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 48),
    _PmEthEgressBytesQ6_Type()
)
pmEthEgressBytesQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ6.setStatus("current")
_PmEthEgressBandwidthQ6_Type = Counter64
_PmEthEgressBandwidthQ6_Object = MibTableColumn
pmEthEgressBandwidthQ6 = _PmEthEgressBandwidthQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 49),
    _PmEthEgressBandwidthQ6_Type()
)
pmEthEgressBandwidthQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ6.setStatus("current")
_PmEthEgressFrames15mQ6_Type = Counter64
_PmEthEgressFrames15mQ6_Object = MibTableColumn
pmEthEgressFrames15mQ6 = _PmEthEgressFrames15mQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 50),
    _PmEthEgressFrames15mQ6_Type()
)
pmEthEgressFrames15mQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ6.setStatus("current")
_PmEthEgressBytes15mQ6_Type = Counter64
_PmEthEgressBytes15mQ6_Object = MibTableColumn
pmEthEgressBytes15mQ6 = _PmEthEgressBytes15mQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 51),
    _PmEthEgressBytes15mQ6_Type()
)
pmEthEgressBytes15mQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ6.setStatus("current")
_PmEthEgressFrames24hQ6_Type = Counter64
_PmEthEgressFrames24hQ6_Object = MibTableColumn
pmEthEgressFrames24hQ6 = _PmEthEgressFrames24hQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 52),
    _PmEthEgressFrames24hQ6_Type()
)
pmEthEgressFrames24hQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ6.setStatus("current")
_PmEthEgressBytes24hQ6_Type = Counter64
_PmEthEgressBytes24hQ6_Object = MibTableColumn
pmEthEgressBytes24hQ6 = _PmEthEgressBytes24hQ6_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 53),
    _PmEthEgressBytes24hQ6_Type()
)
pmEthEgressBytes24hQ6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ6.setStatus("current")
_PmEthEgressFramesQ7_Type = Counter64
_PmEthEgressFramesQ7_Object = MibTableColumn
pmEthEgressFramesQ7 = _PmEthEgressFramesQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 54),
    _PmEthEgressFramesQ7_Type()
)
pmEthEgressFramesQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ7.setStatus("current")
_PmEthEgressBytesQ7_Type = Counter64
_PmEthEgressBytesQ7_Object = MibTableColumn
pmEthEgressBytesQ7 = _PmEthEgressBytesQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 55),
    _PmEthEgressBytesQ7_Type()
)
pmEthEgressBytesQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ7.setStatus("current")
_PmEthEgressBandwidthQ7_Type = Counter64
_PmEthEgressBandwidthQ7_Object = MibTableColumn
pmEthEgressBandwidthQ7 = _PmEthEgressBandwidthQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 56),
    _PmEthEgressBandwidthQ7_Type()
)
pmEthEgressBandwidthQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ7.setStatus("current")
_PmEthEgressFrames15mQ7_Type = Counter64
_PmEthEgressFrames15mQ7_Object = MibTableColumn
pmEthEgressFrames15mQ7 = _PmEthEgressFrames15mQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 57),
    _PmEthEgressFrames15mQ7_Type()
)
pmEthEgressFrames15mQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ7.setStatus("current")
_PmEthEgressBytes15mQ7_Type = Counter64
_PmEthEgressBytes15mQ7_Object = MibTableColumn
pmEthEgressBytes15mQ7 = _PmEthEgressBytes15mQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 58),
    _PmEthEgressBytes15mQ7_Type()
)
pmEthEgressBytes15mQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ7.setStatus("current")
_PmEthEgressFrames24hQ7_Type = Counter64
_PmEthEgressFrames24hQ7_Object = MibTableColumn
pmEthEgressFrames24hQ7 = _PmEthEgressFrames24hQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 59),
    _PmEthEgressFrames24hQ7_Type()
)
pmEthEgressFrames24hQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ7.setStatus("current")
_PmEthEgressBytes24hQ7_Type = Counter64
_PmEthEgressBytes24hQ7_Object = MibTableColumn
pmEthEgressBytes24hQ7 = _PmEthEgressBytes24hQ7_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 60),
    _PmEthEgressBytes24hQ7_Type()
)
pmEthEgressBytes24hQ7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ7.setStatus("current")
_PmEthEgressFramesQ8_Type = Counter64
_PmEthEgressFramesQ8_Object = MibTableColumn
pmEthEgressFramesQ8 = _PmEthEgressFramesQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 61),
    _PmEthEgressFramesQ8_Type()
)
pmEthEgressFramesQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFramesQ8.setStatus("current")
_PmEthEgressBytesQ8_Type = Counter64
_PmEthEgressBytesQ8_Object = MibTableColumn
pmEthEgressBytesQ8 = _PmEthEgressBytesQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 62),
    _PmEthEgressBytesQ8_Type()
)
pmEthEgressBytesQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytesQ8.setStatus("current")
_PmEthEgressBandwidthQ8_Type = Counter64
_PmEthEgressBandwidthQ8_Object = MibTableColumn
pmEthEgressBandwidthQ8 = _PmEthEgressBandwidthQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 63),
    _PmEthEgressBandwidthQ8_Type()
)
pmEthEgressBandwidthQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBandwidthQ8.setStatus("current")
_PmEthEgressFrames15mQ8_Type = Counter64
_PmEthEgressFrames15mQ8_Object = MibTableColumn
pmEthEgressFrames15mQ8 = _PmEthEgressFrames15mQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 64),
    _PmEthEgressFrames15mQ8_Type()
)
pmEthEgressFrames15mQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames15mQ8.setStatus("current")
_PmEthEgressBytes15mQ8_Type = Counter64
_PmEthEgressBytes15mQ8_Object = MibTableColumn
pmEthEgressBytes15mQ8 = _PmEthEgressBytes15mQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 65),
    _PmEthEgressBytes15mQ8_Type()
)
pmEthEgressBytes15mQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes15mQ8.setStatus("current")
_PmEthEgressFrames24hQ8_Type = Counter64
_PmEthEgressFrames24hQ8_Object = MibTableColumn
pmEthEgressFrames24hQ8 = _PmEthEgressFrames24hQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 66),
    _PmEthEgressFrames24hQ8_Type()
)
pmEthEgressFrames24hQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressFrames24hQ8.setStatus("current")
_PmEthEgressBytes24hQ8_Type = Counter64
_PmEthEgressBytes24hQ8_Object = MibTableColumn
pmEthEgressBytes24hQ8 = _PmEthEgressBytes24hQ8_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 67),
    _PmEthEgressBytes24hQ8_Type()
)
pmEthEgressBytes24hQ8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressBytes24hQ8.setStatus("current")


class _PmEthEgressReportMode_Type(Integer32):
    """Custom type pmEthEgressReportMode based on Integer32"""
    defaultValue = 2

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


_PmEthEgressReportMode_Type.__name__ = "Integer32"
_PmEthEgressReportMode_Object = MibTableColumn
pmEthEgressReportMode = _PmEthEgressReportMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 68),
    _PmEthEgressReportMode_Type()
)
pmEthEgressReportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmEthEgressReportMode.setStatus("current")
_PmEthEgressIsSuspect15Min_Type = TruthValue
_PmEthEgressIsSuspect15Min_Object = MibTableColumn
pmEthEgressIsSuspect15Min = _PmEthEgressIsSuspect15Min_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 69),
    _PmEthEgressIsSuspect15Min_Type()
)
pmEthEgressIsSuspect15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressIsSuspect15Min.setStatus("current")
_PmEthEgressIsSuspect24H_Type = TruthValue
_PmEthEgressIsSuspect24H_Object = MibTableColumn
pmEthEgressIsSuspect24H = _PmEthEgressIsSuspect24H_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 16, 1, 1, 70),
    _PmEthEgressIsSuspect24H_Type()
)
pmEthEgressIsSuspect24H.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pmEthEgressIsSuspect24H.setStatus("current")

# Managed Objects groups

pmGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 1)
)
pmGeneralGroup.setObjects(
    ("LUM-PM-MIB", "pmGeneralLastChangeTime")
)
if mibBuilder.loadTexts:
    pmGeneralGroup.setStatus("deprecated")

pmIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 3)
)
pmIntervalGroup.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"))
)
if mibBuilder.loadTexts:
    pmIntervalGroup.setStatus("deprecated")

pmInterval24hGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 5)
)
pmInterval24hGroup.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroup.setStatus("deprecated")

pmIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 6)
)
pmIfGroup.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"))
)
if mibBuilder.loadTexts:
    pmIfGroup.setStatus("deprecated")

pmLogGeneralGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 7)
)
pmLogGeneralGroup.setObjects(
      *(("LUM-PM-MIB", "pmLogGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmLogGeneralSize"),
        ("LUM-PM-MIB", "pmLogGeneralSize24h"))
)
if mibBuilder.loadTexts:
    pmLogGeneralGroup.setStatus("deprecated")

pmFileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 8)
)
pmFileGroup.setObjects(
      *(("LUM-PM-MIB", "pmFileIndex"),
        ("LUM-PM-MIB", "pmFileName"),
        ("LUM-PM-MIB", "pmFileCreatedTime"))
)
if mibBuilder.loadTexts:
    pmFileGroup.setStatus("deprecated")

pmFile24hGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 9)
)
pmFile24hGroup.setObjects(
      *(("LUM-PM-MIB", "pmFile24hIndex"),
        ("LUM-PM-MIB", "pmFile24hName"),
        ("LUM-PM-MIB", "pmFile24hCreatedTime"))
)
if mibBuilder.loadTexts:
    pmFile24hGroup.setStatus("deprecated")

pmIfGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 11)
)
pmIfGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"))
)
if mibBuilder.loadTexts:
    pmIfGroupV2.setStatus("deprecated")

pmGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 12)
)
pmGeneralGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmGeneralStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    pmGeneralGroupV2.setStatus("deprecated")

pmControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 13)
)
pmControlGroup.setObjects(
      *(("LUM-PM-MIB", "pmControlReset15Min"),
        ("LUM-PM-MIB", "pmControlReset24H"))
)
if mibBuilder.loadTexts:
    pmControlGroup.setStatus("deprecated")

pmIfGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 14)
)
pmIfGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"))
)
if mibBuilder.loadTexts:
    pmIfGroupV3.setStatus("current")

pmFileGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 15)
)
pmFileGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmFileIndex"),
        ("LUM-PM-MIB", "pmFileName"),
        ("LUM-PM-MIB", "pmFileCreatedTime"),
        ("LUM-PM-MIB", "pmFileSeqNumber"))
)
if mibBuilder.loadTexts:
    pmFileGroupV2.setStatus("current")

pmFile24hGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 16)
)
pmFile24hGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmFile24hIndex"),
        ("LUM-PM-MIB", "pmFile24hName"),
        ("LUM-PM-MIB", "pmFile24hCreatedTime"),
        ("LUM-PM-MIB", "pmFile24hSeqNumber"))
)
if mibBuilder.loadTexts:
    pmFile24hGroupV2.setStatus("current")

pmIfGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 17)
)
pmIfGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"))
)
if mibBuilder.loadTexts:
    pmIfGroupV4.setStatus("deprecated")

pmIfGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 18)
)
pmIfGroupV5.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"))
)
if mibBuilder.loadTexts:
    pmIfGroupV5.setStatus("deprecated")

pmFileGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 19)
)
pmFileGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmFileIndex"),
        ("LUM-PM-MIB", "pmFileName"),
        ("LUM-PM-MIB", "pmFileCreatedTime"),
        ("LUM-PM-MIB", "pmFileSeqNumber"),
        ("LUM-PM-MIB", "pmFileStartTime"),
        ("LUM-PM-MIB", "pmFileStopTime"))
)
if mibBuilder.loadTexts:
    pmFileGroupV3.setStatus("deprecated")

pmFile24hGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 20)
)
pmFile24hGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmFile24hIndex"),
        ("LUM-PM-MIB", "pmFile24hName"),
        ("LUM-PM-MIB", "pmFile24hCreatedTime"),
        ("LUM-PM-MIB", "pmFile24hSeqNumber"),
        ("LUM-PM-MIB", "pmFile24hStartTime"),
        ("LUM-PM-MIB", "pmFile24hStopTime"))
)
if mibBuilder.loadTexts:
    pmFile24hGroupV3.setStatus("deprecated")

pmFileGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 21)
)
pmFileGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmFileIndex"),
        ("LUM-PM-MIB", "pmFileName"),
        ("LUM-PM-MIB", "pmFileCreatedTime"),
        ("LUM-PM-MIB", "pmFileSeqNumber"),
        ("LUM-PM-MIB", "pmFileStartTime"),
        ("LUM-PM-MIB", "pmFileStopTime"),
        ("LUM-PM-MIB", "pmFileUrl"))
)
if mibBuilder.loadTexts:
    pmFileGroupV4.setStatus("current")

pmFile24hGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 22)
)
pmFile24hGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmFile24hIndex"),
        ("LUM-PM-MIB", "pmFile24hName"),
        ("LUM-PM-MIB", "pmFile24hCreatedTime"),
        ("LUM-PM-MIB", "pmFile24hSeqNumber"),
        ("LUM-PM-MIB", "pmFile24hStartTime"),
        ("LUM-PM-MIB", "pmFile24hStopTime"),
        ("LUM-PM-MIB", "pmFile24hUrl"))
)
if mibBuilder.loadTexts:
    pmFile24hGroupV4.setStatus("current")

pmIntervalGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 23)
)
pmIntervalGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"),
        ("LUM-PM-MIB", "pmIntervalRxPowerLevel"))
)
if mibBuilder.loadTexts:
    pmIntervalGroupV2.setStatus("deprecated")

pmInterval24hGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 24)
)
pmInterval24hGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"),
        ("LUM-PM-MIB", "pmInterval24hRxPowerLevel"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroupV2.setStatus("deprecated")

pmIfGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 25)
)
pmIfGroupV6.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"),
        ("LUM-PM-MIB", "pmIfInstallCommand"),
        ("LUM-PM-MIB", "pmIfRxPowerLevel"),
        ("LUM-PM-MIB", "pmIfInitialPowerLevel"))
)
if mibBuilder.loadTexts:
    pmIfGroupV6.setStatus("deprecated")

pmLogGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 26)
)
pmLogGeneralGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmLogGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmLogGeneralSize"),
        ("LUM-PM-MIB", "pmLogGeneralSize24h"),
        ("LUM-PM-MIB", "pmLogGeneralFileTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralFile24hTableSize"))
)
if mibBuilder.loadTexts:
    pmLogGeneralGroupV2.setStatus("deprecated")

pmIntervalGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 27)
)
pmIntervalGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"),
        ("LUM-PM-MIB", "pmIntervalRxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalGbeMaxUtilization"))
)
if mibBuilder.loadTexts:
    pmIntervalGroupV3.setStatus("deprecated")

pmInterval24hGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 28)
)
pmInterval24hGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"),
        ("LUM-PM-MIB", "pmInterval24hRxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hGbeMaxUtilization"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroupV3.setStatus("deprecated")

pmIfGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 29)
)
pmIfGroupV7.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"),
        ("LUM-PM-MIB", "pmIfInstallCommand"),
        ("LUM-PM-MIB", "pmIfRxPowerLevel"),
        ("LUM-PM-MIB", "pmIfInitialPowerLevel"),
        ("LUM-PM-MIB", "pmIfRxGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfRx24hGbeMaxUtilization"))
)
if mibBuilder.loadTexts:
    pmIfGroupV7.setStatus("deprecated")

pmGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 30)
)
pmGeneralGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmGeneralStateLastChangeTime"),
        ("LUM-PM-MIB", "pmGeneralPmIfTableSize"))
)
if mibBuilder.loadTexts:
    pmGeneralGroupV3.setStatus("deprecated")

pmLogGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 31)
)
pmLogGeneralGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmLogGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmLogGeneralSize"),
        ("LUM-PM-MIB", "pmLogGeneralSize24h"),
        ("LUM-PM-MIB", "pmLogGeneralFileTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralFile24hTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralInterval15mTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralInterval24hTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralInterval15mShowNonZeroOnly"),
        ("LUM-PM-MIB", "pmLogGeneralInterval24hShowNonZeroOnly"))
)
if mibBuilder.loadTexts:
    pmLogGeneralGroupV3.setStatus("deprecated")

pmIntervalGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 32)
)
pmIntervalGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"),
        ("LUM-PM-MIB", "pmIntervalGbeMaxUtilization"))
)
if mibBuilder.loadTexts:
    pmIntervalGroupV4.setStatus("deprecated")

pmInterval24hGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 33)
)
pmInterval24hGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"),
        ("LUM-PM-MIB", "pmInterval24hGbeMaxUtilization"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroupV4.setStatus("deprecated")

pmIfGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 34)
)
pmIfGroupV8.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"),
        ("LUM-PM-MIB", "pmIfInstallCommand"),
        ("LUM-PM-MIB", "pmIfRxPowerLevel"),
        ("LUM-PM-MIB", "pmIfInitialPowerLevel"),
        ("LUM-PM-MIB", "pmIfRxGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfRx24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfTxPowerLevel"))
)
if mibBuilder.loadTexts:
    pmIfGroupV8.setStatus("deprecated")

pmIntervalGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 35)
)
pmIntervalGroupV5.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"),
        ("LUM-PM-MIB", "pmIntervalRxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIntervalTxPowerLevel"))
)
if mibBuilder.loadTexts:
    pmIntervalGroupV5.setStatus("deprecated")

pmInterval24hGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 36)
)
pmInterval24hGroupV5.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"),
        ("LUM-PM-MIB", "pmInterval24hRxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmInterval24hTxPowerLevel"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroupV5.setStatus("deprecated")

pmLogGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 37)
)
pmLogGeneralGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmLogGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmLogGeneralSize"),
        ("LUM-PM-MIB", "pmLogGeneralSize24h"),
        ("LUM-PM-MIB", "pmLogGeneralFileTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralFile24hTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralInterval15mTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralInterval24hTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralInterval15mShowNonZeroOnly"),
        ("LUM-PM-MIB", "pmLogGeneralInterval24hShowNonZeroOnly"),
        ("LUM-PM-MIB", "pmLogGeneralFile15mLastSeqNumber"),
        ("LUM-PM-MIB", "pmLogGeneralFile24hLastSeqNumber"))
)
if mibBuilder.loadTexts:
    pmLogGeneralGroupV4.setStatus("deprecated")

pmIfGroupV9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 38)
)
pmIfGroupV9.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"),
        ("LUM-PM-MIB", "pmIfInstallCommand"),
        ("LUM-PM-MIB", "pmIfRxPowerLevel"),
        ("LUM-PM-MIB", "pmIfInitialPowerLevel"),
        ("LUM-PM-MIB", "pmIfRxGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfRx24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfTxPowerLevel"),
        ("LUM-PM-MIB", "pmIfObjectProperty"))
)
if mibBuilder.loadTexts:
    pmIfGroupV9.setStatus("deprecated")

pmIntervalGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 39)
)
pmIntervalGroupV6.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"),
        ("LUM-PM-MIB", "pmIntervalRxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIntervalTxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmIntervalRxOversizedFrames"),
        ("LUM-PM-MIB", "pmIntervalRxFragments"),
        ("LUM-PM-MIB", "pmIntervalRxFcsErrors"),
        ("LUM-PM-MIB", "pmIntervalRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmIntervalTxOctets"),
        ("LUM-PM-MIB", "pmIntervalTxFrames"),
        ("LUM-PM-MIB", "pmIntervalTxUnicastFrames"),
        ("LUM-PM-MIB", "pmIntervalTxMulticastFrames"),
        ("LUM-PM-MIB", "pmIntervalTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmIntervalRxOctets"),
        ("LUM-PM-MIB", "pmIntervalRxFrames"),
        ("LUM-PM-MIB", "pmIntervalRxUnicastFrames"),
        ("LUM-PM-MIB", "pmIntervalRxMulticastFrames"),
        ("LUM-PM-MIB", "pmIntervalRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmIntervalIngressGreenFrameCount"),
        ("LUM-PM-MIB", "pmIntervalIngressYellowFrameCount"),
        ("LUM-PM-MIB", "pmIntervalIngressRedFrameCount"),
        ("LUM-PM-MIB", "pmIntervalIngressGreenOctetCount"),
        ("LUM-PM-MIB", "pmIntervalIngressYellowOctetCount"),
        ("LUM-PM-MIB", "pmIntervalIngressRedOctetCount"),
        ("LUM-PM-MIB", "pmIntervalEgressGreenFrameCount"),
        ("LUM-PM-MIB", "pmIntervalEgressGreenOctetCount"),
        ("LUM-PM-MIB", "pmIntervalGreenFrameDiscards"),
        ("LUM-PM-MIB", "pmIntervalYellowFrameDiscards"),
        ("LUM-PM-MIB", "pmIntervalGreenOctetDiscards"),
        ("LUM-PM-MIB", "pmIntervalYellowOctetDiscards"),
        ("LUM-PM-MIB", "pmIntervalTwoWayFrameDelay"),
        ("LUM-PM-MIB", "pmIntervalTwoWayFrameDelayVariation"),
        ("LUM-PM-MIB", "pmIntervalFrameLossRatioNearEnd"),
        ("LUM-PM-MIB", "pmIntervalFrameLossRatioFarEnd"),
        ("LUM-PM-MIB", "pmIntervalUnavailabilityNearEnd"),
        ("LUM-PM-MIB", "pmIntervalUnavailabilityFarEnd"),
        ("LUM-PM-MIB", "pmIntervalOneWayFrameDelayVariation"))
)
if mibBuilder.loadTexts:
    pmIntervalGroupV6.setStatus("deprecated")

pmInterval24hGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 40)
)
pmInterval24hGroupV6.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"),
        ("LUM-PM-MIB", "pmInterval24hRxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmInterval24hTxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmInterval24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmInterval24hRxFragments"),
        ("LUM-PM-MIB", "pmInterval24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmInterval24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmInterval24hTxOctets"),
        ("LUM-PM-MIB", "pmInterval24hTxFrames"),
        ("LUM-PM-MIB", "pmInterval24hTxUnicastFrames"),
        ("LUM-PM-MIB", "pmInterval24hTxMulticastFrames"),
        ("LUM-PM-MIB", "pmInterval24hTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmInterval24hRxOctets"),
        ("LUM-PM-MIB", "pmInterval24hRxFrames"),
        ("LUM-PM-MIB", "pmInterval24hRxUnicastFrames"),
        ("LUM-PM-MIB", "pmInterval24hRxMulticastFrames"),
        ("LUM-PM-MIB", "pmInterval24hRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmInterval24hIngressGreenFrameCount"),
        ("LUM-PM-MIB", "pmInterval24hIngressYellowFrameCount"),
        ("LUM-PM-MIB", "pmInterval24hIngressRedFrameCount"),
        ("LUM-PM-MIB", "pmInterval24hIngressGreenOctetCount"),
        ("LUM-PM-MIB", "pmInterval24hIngressYellowOctetCount"),
        ("LUM-PM-MIB", "pmInterval24hIngressRedOctetCount"),
        ("LUM-PM-MIB", "pmInterval24hEgressGreenFrameCount"),
        ("LUM-PM-MIB", "pmInterval24hEgressGreenOctetCount"),
        ("LUM-PM-MIB", "pmInterval24hGreenFrameDiscards"),
        ("LUM-PM-MIB", "pmInterval24hYellowFrameDiscards"),
        ("LUM-PM-MIB", "pmInterval24hGreenOctetDiscards"),
        ("LUM-PM-MIB", "pmInterval24hYellowOctetDiscards"),
        ("LUM-PM-MIB", "pmInterval24hTwoWayFrameDelay"),
        ("LUM-PM-MIB", "pmInterval24hTwoWayFrameDelayVariation"),
        ("LUM-PM-MIB", "pmInterval24hFrameLossRatioNearEnd"),
        ("LUM-PM-MIB", "pmInterval24hFrameLossRatioFarEnd"),
        ("LUM-PM-MIB", "pmInterval24hUnavailabilityNearEnd"),
        ("LUM-PM-MIB", "pmInterval24hUnavailabilityFarEnd"),
        ("LUM-PM-MIB", "pmInterval24hOneWayFrameDelayVariation"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroupV6.setStatus("deprecated")

pmEthTdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 41)
)
pmEthTdGroup.setObjects(
      *(("LUM-PM-MIB", "pmEthTdIndex"),
        ("LUM-PM-MIB", "pmEthTdName"),
        ("LUM-PM-MIB", "pmEthTdSubrack"),
        ("LUM-PM-MIB", "pmEthTdSlot"),
        ("LUM-PM-MIB", "pmEthTdPort"),
        ("LUM-PM-MIB", "pmEthTdPmReportMode"),
        ("LUM-PM-MIB", "pmEthTdRxPort"),
        ("LUM-PM-MIB", "pmEthTdReset15Min"),
        ("LUM-PM-MIB", "pmEthTdReset24H"),
        ("LUM-PM-MIB", "pmEthTdAdminStatus"),
        ("LUM-PM-MIB", "pmEthTdOperStatus"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect24h"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdObjectProperty"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxFragments"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanId"))
)
if mibBuilder.loadTexts:
    pmEthTdGroup.setStatus("deprecated")

pmEthTmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 42)
)
pmEthTmGroup.setObjects(
      *(("LUM-PM-MIB", "pmEthTmIndex"),
        ("LUM-PM-MIB", "pmEthTmName"),
        ("LUM-PM-MIB", "pmEthTmSubrack"),
        ("LUM-PM-MIB", "pmEthTmSlot"),
        ("LUM-PM-MIB", "pmEthTmPort"),
        ("LUM-PM-MIB", "pmEthTmPmReportMode"),
        ("LUM-PM-MIB", "pmEthTmRxPort"),
        ("LUM-PM-MIB", "pmEthTmReset15Min"),
        ("LUM-PM-MIB", "pmEthTmReset24H"),
        ("LUM-PM-MIB", "pmEthTmAdminStatus"),
        ("LUM-PM-MIB", "pmEthTmOperStatus"),
        ("LUM-PM-MIB", "pmEthTmIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthTmIsSuspect24h"),
        ("LUM-PM-MIB", "pmEthTmCurrentIngressGreenFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentIngressYellowFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentIngressRedFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentIngressGreenOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentIngressYellowOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentIngressRedOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentEgressGreenFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentEgressGreenOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrentGreenFrameDiscards"),
        ("LUM-PM-MIB", "pmEthTmCurrentYellowFrameDiscards"),
        ("LUM-PM-MIB", "pmEthTmCurrentGreenOctetDiscards"),
        ("LUM-PM-MIB", "pmEthTmCurrentYellowOctetDiscards"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hIngressGreenFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hIngressYellowFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hIngressRedFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hIngressGreenOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hIngressYellowOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hIngressRedOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hEgressGreenFrameCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hEgressGreenOctetCount"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hGreenFrameDiscards"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hYellowFrameDiscards"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hGreenOctetDiscards"),
        ("LUM-PM-MIB", "pmEthTmCurrent24hYellowOctetDiscards"),
        ("LUM-PM-MIB", "pmEthTmObjectProperty"),
        ("LUM-PM-MIB", "pmEthTmInternalReference"),
        ("LUM-PM-MIB", "pmEthTmIdentifier"))
)
if mibBuilder.loadTexts:
    pmEthTmGroup.setStatus("current")

pmEthOamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 43)
)
pmEthOamGroup.setObjects(
      *(("LUM-PM-MIB", "pmEthOamIndex"),
        ("LUM-PM-MIB", "pmEthOamName"),
        ("LUM-PM-MIB", "pmEthOamSubrack"),
        ("LUM-PM-MIB", "pmEthOamSlot"),
        ("LUM-PM-MIB", "pmEthOamPort"),
        ("LUM-PM-MIB", "pmEthOamPmReportMode"),
        ("LUM-PM-MIB", "pmEthOamRxPort"),
        ("LUM-PM-MIB", "pmEthOamReset15Min"),
        ("LUM-PM-MIB", "pmEthOamReset24H"),
        ("LUM-PM-MIB", "pmEthOamAdminStatus"),
        ("LUM-PM-MIB", "pmEthOamOperStatus"),
        ("LUM-PM-MIB", "pmEthOamIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthOamIsSuspect24h"),
        ("LUM-PM-MIB", "pmEthOamCurrentTwoWayFrameDelay"),
        ("LUM-PM-MIB", "pmEthOamCurrentTwoWayFrameDelayVariation"),
        ("LUM-PM-MIB", "pmEthOamCurrentFrameLossRatioNearEnd"),
        ("LUM-PM-MIB", "pmEthOamCurrentFrameLossRatioFarEnd"),
        ("LUM-PM-MIB", "pmEthOamCurrentUnavailabilityNearEnd"),
        ("LUM-PM-MIB", "pmEthOamCurrentUnavailabilityFarEnd"),
        ("LUM-PM-MIB", "pmEthOamCurrent24hTwoWayFrameDelay"),
        ("LUM-PM-MIB", "pmEthOamCurrent24hTwoWayFrameDelayVariation"),
        ("LUM-PM-MIB", "pmEthOamCurrent24hFrameLossRatioNearEnd"),
        ("LUM-PM-MIB", "pmEthOamCurrent24hFrameLossRatioFarEnd"),
        ("LUM-PM-MIB", "pmEthOamCurrent24hUnavailabilityNearEnd"),
        ("LUM-PM-MIB", "pmEthOamCurrent24hUnavailabilityFarEnd"),
        ("LUM-PM-MIB", "pmEthOamObjectProperty"),
        ("LUM-PM-MIB", "pmEthOamInternalReference"),
        ("LUM-PM-MIB", "pmEthOamIdentifier"),
        ("LUM-PM-MIB", "pmEthOamUsedPercentOfFrames"),
        ("LUM-PM-MIB", "pmEthOamFrameLossRatioUnavailableThreshold"),
        ("LUM-PM-MIB", "pmEthOamCurrentOneWayFrameDelayVariation"),
        ("LUM-PM-MIB", "pmEthOamCurrent24hOneWayFrameDelayVariation"))
)
if mibBuilder.loadTexts:
    pmEthOamGroup.setStatus("current")

pmGeneralGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 44)
)
pmGeneralGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmGeneralStateLastChangeTime"),
        ("LUM-PM-MIB", "pmGeneralPmIfTableSize"),
        ("LUM-PM-MIB", "pmGeneralPmEthTdTableSize"),
        ("LUM-PM-MIB", "pmGeneralPmEthTmTableSize"),
        ("LUM-PM-MIB", "pmGeneralPmEthOamTableSize"))
)
if mibBuilder.loadTexts:
    pmGeneralGroupV4.setStatus("deprecated")

pmEthTdGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 45)
)
pmEthTdGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmEthTdIndex"),
        ("LUM-PM-MIB", "pmEthTdName"),
        ("LUM-PM-MIB", "pmEthTdSubrack"),
        ("LUM-PM-MIB", "pmEthTdSlot"),
        ("LUM-PM-MIB", "pmEthTdPort"),
        ("LUM-PM-MIB", "pmEthTdPmReportMode"),
        ("LUM-PM-MIB", "pmEthTdRxPort"),
        ("LUM-PM-MIB", "pmEthTdReset15Min"),
        ("LUM-PM-MIB", "pmEthTdReset24H"),
        ("LUM-PM-MIB", "pmEthTdAdminStatus"),
        ("LUM-PM-MIB", "pmEthTdOperStatus"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect24h"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdObjectProperty"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxFragments"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanId"))
)
if mibBuilder.loadTexts:
    pmEthTdGroupV2.setStatus("deprecated")

pmIntervalGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 46)
)
pmIntervalGroupV7.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"),
        ("LUM-PM-MIB", "pmIntervalRxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIntervalTxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmIntervalRxEthMaxUtilization"))
)
if mibBuilder.loadTexts:
    pmIntervalGroupV7.setStatus("deprecated")

pmInterval24hGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 47)
)
pmInterval24hGroupV7.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"),
        ("LUM-PM-MIB", "pmInterval24hRxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmInterval24hTxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmInterval24hRxEthMaxUtilization"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroupV7.setStatus("deprecated")

pmIntervalGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 48)
)
pmIntervalGroupV8.setObjects(
      *(("LUM-PM-MIB", "pmIntervalSubrack"),
        ("LUM-PM-MIB", "pmIntervalSlot"),
        ("LUM-PM-MIB", "pmIntervalPort"),
        ("LUM-PM-MIB", "pmIntervalNumber"),
        ("LUM-PM-MIB", "pmIntervalIsSuspect"),
        ("LUM-PM-MIB", "pmIntervalRxES"),
        ("LUM-PM-MIB", "pmIntervalRxSES"),
        ("LUM-PM-MIB", "pmIntervalRxBBE"),
        ("LUM-PM-MIB", "pmIntervalRxUAS"),
        ("LUM-PM-MIB", "pmIntervalTxES"),
        ("LUM-PM-MIB", "pmIntervalTxSES"),
        ("LUM-PM-MIB", "pmIntervalTxBBE"),
        ("LUM-PM-MIB", "pmIntervalTxUAS"),
        ("LUM-PM-MIB", "pmIntervalName"),
        ("LUM-PM-MIB", "pmIntervalRxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIntervalTxPowerLevel"),
        ("LUM-PM-MIB", "pmIntervalTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmIntervalRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmIntervalStartTime"),
        ("LUM-PM-MIB", "pmIntervalStopTime"))
)
if mibBuilder.loadTexts:
    pmIntervalGroupV8.setStatus("deprecated")

pmInterval24hGroupV8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 49)
)
pmInterval24hGroupV8.setObjects(
      *(("LUM-PM-MIB", "pmInterval24hSubrack"),
        ("LUM-PM-MIB", "pmInterval24hSlot"),
        ("LUM-PM-MIB", "pmInterval24hPort"),
        ("LUM-PM-MIB", "pmInterval24hNumber"),
        ("LUM-PM-MIB", "pmInterval24hIsSuspect"),
        ("LUM-PM-MIB", "pmInterval24hRxES"),
        ("LUM-PM-MIB", "pmInterval24hRxSES"),
        ("LUM-PM-MIB", "pmInterval24hRxBBE"),
        ("LUM-PM-MIB", "pmInterval24hRxUAS"),
        ("LUM-PM-MIB", "pmInterval24hTxES"),
        ("LUM-PM-MIB", "pmInterval24hTxSES"),
        ("LUM-PM-MIB", "pmInterval24hTxBBE"),
        ("LUM-PM-MIB", "pmInterval24hTxUAS"),
        ("LUM-PM-MIB", "pmInterval24hName"),
        ("LUM-PM-MIB", "pmInterval24hRxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmInterval24hTxPowerLevel"),
        ("LUM-PM-MIB", "pmInterval24hTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmInterval24hRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmInterval24hStartTime"),
        ("LUM-PM-MIB", "pmInterval24hStopTime"))
)
if mibBuilder.loadTexts:
    pmInterval24hGroupV8.setStatus("deprecated")

pmIfGroupV10 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 50)
)
pmIfGroupV10.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"),
        ("LUM-PM-MIB", "pmIfInstallCommand"),
        ("LUM-PM-MIB", "pmIfRxPowerLevel"),
        ("LUM-PM-MIB", "pmIfInitialPowerLevel"),
        ("LUM-PM-MIB", "pmIfRxGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfRx24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfTxPowerLevel"),
        ("LUM-PM-MIB", "pmIfObjectProperty"),
        ("LUM-PM-MIB", "pmIfDelay"))
)
if mibBuilder.loadTexts:
    pmIfGroupV10.setStatus("deprecated")

pmIfGroupV11 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 51)
)
pmIfGroupV11.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"),
        ("LUM-PM-MIB", "pmIfInstallCommand"),
        ("LUM-PM-MIB", "pmIfRxPowerLevel"),
        ("LUM-PM-MIB", "pmIfInitialPowerLevel"),
        ("LUM-PM-MIB", "pmIfRxGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfRx24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfTxPowerLevel"),
        ("LUM-PM-MIB", "pmIfObjectProperty"),
        ("LUM-PM-MIB", "pmIfDelay"),
        ("LUM-PM-MIB", "pmIfRxBEREstimation"))
)
if mibBuilder.loadTexts:
    pmIfGroupV11.setStatus("deprecated")

pmEthTdGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 52)
)
pmEthTdGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmEthTdIndex"),
        ("LUM-PM-MIB", "pmEthTdName"),
        ("LUM-PM-MIB", "pmEthTdSubrack"),
        ("LUM-PM-MIB", "pmEthTdSlot"),
        ("LUM-PM-MIB", "pmEthTdPort"),
        ("LUM-PM-MIB", "pmEthTdPmReportMode"),
        ("LUM-PM-MIB", "pmEthTdRxPort"),
        ("LUM-PM-MIB", "pmEthTdReset15Min"),
        ("LUM-PM-MIB", "pmEthTdReset24H"),
        ("LUM-PM-MIB", "pmEthTdAdminStatus"),
        ("LUM-PM-MIB", "pmEthTdOperStatus"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect24h"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdObjectProperty"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxFragments"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdResetCont"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxBroadcastFrames"))
)
if mibBuilder.loadTexts:
    pmEthTdGroupV3.setStatus("deprecated")

pmControlGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 53)
)
pmControlGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmControlReset15Min"),
        ("LUM-PM-MIB", "pmControlReset24H"),
        ("LUM-PM-MIB", "pmControlResetCont"))
)
if mibBuilder.loadTexts:
    pmControlGroupV2.setStatus("current")

pmEthDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 54)
)
pmEthDropGroup.setObjects(
      *(("LUM-PM-MIB", "pmEthDropIndex"),
        ("LUM-PM-MIB", "pmEthDropName"),
        ("LUM-PM-MIB", "pmEthDropSubrack"),
        ("LUM-PM-MIB", "pmEthDropSlot"),
        ("LUM-PM-MIB", "pmEthDropPort"),
        ("LUM-PM-MIB", "pmEthDropRxPort"),
        ("LUM-PM-MIB", "pmEthDropResetCont"),
        ("LUM-PM-MIB", "pmEthDropFrames"),
        ("LUM-PM-MIB", "pmEthDropBytes"),
        ("LUM-PM-MIB", "pmEthDropYellowFrames"),
        ("LUM-PM-MIB", "pmEthDropRedFrames"),
        ("LUM-PM-MIB", "pmEthDropFramesQ1"),
        ("LUM-PM-MIB", "pmEthDropBytesQ1"),
        ("LUM-PM-MIB", "pmEthDropFramesQ2"),
        ("LUM-PM-MIB", "pmEthDropBytesQ2"),
        ("LUM-PM-MIB", "pmEthDropFramesQ3"),
        ("LUM-PM-MIB", "pmEthDropBytesQ3"),
        ("LUM-PM-MIB", "pmEthDropFramesQ4"),
        ("LUM-PM-MIB", "pmEthDropBytesQ4"),
        ("LUM-PM-MIB", "pmEthDropFramesQ5"),
        ("LUM-PM-MIB", "pmEthDropBytesQ5"),
        ("LUM-PM-MIB", "pmEthDropFramesQ6"),
        ("LUM-PM-MIB", "pmEthDropBytesQ6"),
        ("LUM-PM-MIB", "pmEthDropFramesQ7"),
        ("LUM-PM-MIB", "pmEthDropBytesQ7"),
        ("LUM-PM-MIB", "pmEthDropFramesQ8"),
        ("LUM-PM-MIB", "pmEthDropBytesQ8"))
)
if mibBuilder.loadTexts:
    pmEthDropGroup.setStatus("deprecated")

pmEthClassificationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 55)
)
pmEthClassificationGroup.setObjects(
      *(("LUM-PM-MIB", "pmEthClassificationIndex"),
        ("LUM-PM-MIB", "pmEthClassificationName"),
        ("LUM-PM-MIB", "pmEthClassificationSubrack"),
        ("LUM-PM-MIB", "pmEthClassificationSlot"),
        ("LUM-PM-MIB", "pmEthClassificationIdentifier"),
        ("LUM-PM-MIB", "pmEthClassificationResetCont"),
        ("LUM-PM-MIB", "pmEthClassificationInternalReference"),
        ("LUM-PM-MIB", "pmEthClassificationCounter1"),
        ("LUM-PM-MIB", "pmEthClassificationCounter2"))
)
if mibBuilder.loadTexts:
    pmEthClassificationGroup.setStatus("current")

pmLogGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 56)
)
pmLogGeneralGroupV5.setObjects(
      *(("LUM-PM-MIB", "pmLogGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmLogGeneralSize"),
        ("LUM-PM-MIB", "pmLogGeneralSize24h"),
        ("LUM-PM-MIB", "pmLogGeneralFileTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralFile24hTableSize"),
        ("LUM-PM-MIB", "pmLogGeneralFile15mLastSeqNumber"),
        ("LUM-PM-MIB", "pmLogGeneralFile24hLastSeqNumber"))
)
if mibBuilder.loadTexts:
    pmLogGeneralGroupV5.setStatus("current")

pmEthClassificationGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 57)
)
pmEthClassificationGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmEthClassificationIndex"),
        ("LUM-PM-MIB", "pmEthClassificationName"),
        ("LUM-PM-MIB", "pmEthClassificationSubrack"),
        ("LUM-PM-MIB", "pmEthClassificationSlot"),
        ("LUM-PM-MIB", "pmEthClassificationIdentifier"),
        ("LUM-PM-MIB", "pmEthClassificationResetCont"),
        ("LUM-PM-MIB", "pmEthClassificationInternalReference"),
        ("LUM-PM-MIB", "pmEthClassificationCounter1"),
        ("LUM-PM-MIB", "pmEthClassificationCounter2"),
        ("LUM-PM-MIB", "pmEthClassificationCounter3"),
        ("LUM-PM-MIB", "pmEthClassificationCounter4"))
)
if mibBuilder.loadTexts:
    pmEthClassificationGroupV2.setStatus("current")

pmEthTdGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 58)
)
pmEthTdGroupV4.setObjects(
      *(("LUM-PM-MIB", "pmEthTdIndex"),
        ("LUM-PM-MIB", "pmEthTdName"),
        ("LUM-PM-MIB", "pmEthTdSubrack"),
        ("LUM-PM-MIB", "pmEthTdSlot"),
        ("LUM-PM-MIB", "pmEthTdPort"),
        ("LUM-PM-MIB", "pmEthTdPmReportMode"),
        ("LUM-PM-MIB", "pmEthTdRxPort"),
        ("LUM-PM-MIB", "pmEthTdReset15Min"),
        ("LUM-PM-MIB", "pmEthTdReset24H"),
        ("LUM-PM-MIB", "pmEthTdAdminStatus"),
        ("LUM-PM-MIB", "pmEthTdOperStatus"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect24h"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdObjectProperty"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxFragments"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdResetCont"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdVlanId"))
)
if mibBuilder.loadTexts:
    pmEthTdGroupV4.setStatus("deprecated")

pmEthTdGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 59)
)
pmEthTdGroupV5.setObjects(
      *(("LUM-PM-MIB", "pmEthTdIndex"),
        ("LUM-PM-MIB", "pmEthTdName"),
        ("LUM-PM-MIB", "pmEthTdSubrack"),
        ("LUM-PM-MIB", "pmEthTdSlot"),
        ("LUM-PM-MIB", "pmEthTdPort"),
        ("LUM-PM-MIB", "pmEthTdPmReportMode"),
        ("LUM-PM-MIB", "pmEthTdRxPort"),
        ("LUM-PM-MIB", "pmEthTdReset15Min"),
        ("LUM-PM-MIB", "pmEthTdReset24H"),
        ("LUM-PM-MIB", "pmEthTdAdminStatus"),
        ("LUM-PM-MIB", "pmEthTdOperStatus"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthTdIsSuspect24h"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrentRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hTxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdCurrent24hRxEthMaxUtilization"),
        ("LUM-PM-MIB", "pmEthTdObjectProperty"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFramesThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragmentsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrorsThreshold"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanIdThreshold"),
        ("LUM-PM-MIB", "pmEthTdRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdRxFragments"),
        ("LUM-PM-MIB", "pmEthTdRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTd24hRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTd24hRxFragments"),
        ("LUM-PM-MIB", "pmEthTd24hRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTd24hRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdResetCont"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxUndersizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxOversizedFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFragments"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFcsErrors"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxInvalidCeVlanId"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContTxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxOctets"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxUnicastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxMulticastFrames"),
        ("LUM-PM-MIB", "pmEthTdCurrentContRxBroadcastFrames"),
        ("LUM-PM-MIB", "pmEthTdVlanId"),
        ("LUM-PM-MIB", "pmEthTdIfNo"),
        ("LUM-PM-MIB", "pmEthTdUpPortId"))
)
if mibBuilder.loadTexts:
    pmEthTdGroupV5.setStatus("current")

pmIfGroupV12 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 60)
)
pmIfGroupV12.setObjects(
      *(("LUM-PM-MIB", "pmIfIndex"),
        ("LUM-PM-MIB", "pmIfName"),
        ("LUM-PM-MIB", "pmIfSubrack"),
        ("LUM-PM-MIB", "pmIfSlot"),
        ("LUM-PM-MIB", "pmIfPort"),
        ("LUM-PM-MIB", "pmIfPmReportMode"),
        ("LUM-PM-MIB", "pmIfRxCurrentES"),
        ("LUM-PM-MIB", "pmIfRxCurrentSES"),
        ("LUM-PM-MIB", "pmIfRxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTxCurrentES"),
        ("LUM-PM-MIB", "pmIfTxCurrentSES"),
        ("LUM-PM-MIB", "pmIfTxCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTxCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfRx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentSES"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentBBE"),
        ("LUM-PM-MIB", "pmIfTx24hCurrentUAS"),
        ("LUM-PM-MIB", "pmIfRxESThreshold"),
        ("LUM-PM-MIB", "pmIfRxSESThreshold"),
        ("LUM-PM-MIB", "pmIfRxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRxUASThreshold"),
        ("LUM-PM-MIB", "pmIfTxESThreshold"),
        ("LUM-PM-MIB", "pmIfTxSESThreshold"),
        ("LUM-PM-MIB", "pmIfTxBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTxUASThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfRx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hSESThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hBBEThreshold"),
        ("LUM-PM-MIB", "pmIfTx24hUASThreshold"),
        ("LUM-PM-MIB", "pmIfRxES"),
        ("LUM-PM-MIB", "pmIfRxSES"),
        ("LUM-PM-MIB", "pmIfRxBBE"),
        ("LUM-PM-MIB", "pmIfRxUAS"),
        ("LUM-PM-MIB", "pmIfTxES"),
        ("LUM-PM-MIB", "pmIfTxSES"),
        ("LUM-PM-MIB", "pmIfTxBBE"),
        ("LUM-PM-MIB", "pmIfTxUAS"),
        ("LUM-PM-MIB", "pmIfRx24hES"),
        ("LUM-PM-MIB", "pmIfRx24hSES"),
        ("LUM-PM-MIB", "pmIfRx24hBBE"),
        ("LUM-PM-MIB", "pmIfRx24hUAS"),
        ("LUM-PM-MIB", "pmIfTx24hES"),
        ("LUM-PM-MIB", "pmIfTx24hSES"),
        ("LUM-PM-MIB", "pmIfTx24hBBE"),
        ("LUM-PM-MIB", "pmIfTx24hUAS"),
        ("LUM-PM-MIB", "pmIfRxPort"),
        ("LUM-PM-MIB", "pmIfReset15Min"),
        ("LUM-PM-MIB", "pmIfReset24H"),
        ("LUM-PM-MIB", "pmIfAdminStatus"),
        ("LUM-PM-MIB", "pmIfOperStatus"),
        ("LUM-PM-MIB", "pmIfIsSuspect15Min"),
        ("LUM-PM-MIB", "pmIfIsSuspect24H"),
        ("LUM-PM-MIB", "pmIfInstallCommand"),
        ("LUM-PM-MIB", "pmIfRxPowerLevel"),
        ("LUM-PM-MIB", "pmIfInitialPowerLevel"),
        ("LUM-PM-MIB", "pmIfRxGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfRx24hGbeMaxUtilization"),
        ("LUM-PM-MIB", "pmIfTxPowerLevel"),
        ("LUM-PM-MIB", "pmIfObjectProperty"),
        ("LUM-PM-MIB", "pmIfDelay"),
        ("LUM-PM-MIB", "pmIfRxBEREstimation"),
        ("LUM-PM-MIB", "pmIfIfNo"),
        ("LUM-PM-MIB", "pmIfUpPortId"))
)
if mibBuilder.loadTexts:
    pmIfGroupV12.setStatus("current")

pmGeneralGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 61)
)
pmGeneralGroupV5.setObjects(
      *(("LUM-PM-MIB", "pmGeneralLastChangeTime"),
        ("LUM-PM-MIB", "pmGeneralStateLastChangeTime"),
        ("LUM-PM-MIB", "pmGeneralPmIfTableSize"),
        ("LUM-PM-MIB", "pmGeneralPmEthTdTableSize"),
        ("LUM-PM-MIB", "pmGeneralPmEthTmTableSize"),
        ("LUM-PM-MIB", "pmGeneralPmEthOamTableSize"),
        ("LUM-PM-MIB", "pmGeneralPmMpoLanesTableSize"))
)
if mibBuilder.loadTexts:
    pmGeneralGroupV5.setStatus("current")

pmEthDropGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 62)
)
pmEthDropGroupV2.setObjects(
      *(("LUM-PM-MIB", "pmEthDropIndex"),
        ("LUM-PM-MIB", "pmEthDropName"),
        ("LUM-PM-MIB", "pmEthDropSubrack"),
        ("LUM-PM-MIB", "pmEthDropSlot"),
        ("LUM-PM-MIB", "pmEthDropPort"),
        ("LUM-PM-MIB", "pmEthDropRxPort"),
        ("LUM-PM-MIB", "pmEthDropResetCont"),
        ("LUM-PM-MIB", "pmEthDropFrames"),
        ("LUM-PM-MIB", "pmEthDropBytes"),
        ("LUM-PM-MIB", "pmEthDropYellowFrames"),
        ("LUM-PM-MIB", "pmEthDropRedFrames"),
        ("LUM-PM-MIB", "pmEthDropFramesQ1"),
        ("LUM-PM-MIB", "pmEthDropBytesQ1"),
        ("LUM-PM-MIB", "pmEthDropFramesQ2"),
        ("LUM-PM-MIB", "pmEthDropBytesQ2"),
        ("LUM-PM-MIB", "pmEthDropFramesQ3"),
        ("LUM-PM-MIB", "pmEthDropBytesQ3"),
        ("LUM-PM-MIB", "pmEthDropFramesQ4"),
        ("LUM-PM-MIB", "pmEthDropBytesQ4"),
        ("LUM-PM-MIB", "pmEthDropFramesQ5"),
        ("LUM-PM-MIB", "pmEthDropBytesQ5"),
        ("LUM-PM-MIB", "pmEthDropFramesQ6"),
        ("LUM-PM-MIB", "pmEthDropBytesQ6"),
        ("LUM-PM-MIB", "pmEthDropFramesQ7"),
        ("LUM-PM-MIB", "pmEthDropBytesQ7"),
        ("LUM-PM-MIB", "pmEthDropFramesQ8"),
        ("LUM-PM-MIB", "pmEthDropBytesQ8"),
        ("LUM-PM-MIB", "pmEthDropIfNo"),
        ("LUM-PM-MIB", "pmEthDropUpPortId"))
)
if mibBuilder.loadTexts:
    pmEthDropGroupV2.setStatus("deprecated")

pmEthDropGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 63)
)
pmEthDropGroupV3.setObjects(
      *(("LUM-PM-MIB", "pmEthDropIndex"),
        ("LUM-PM-MIB", "pmEthDropName"),
        ("LUM-PM-MIB", "pmEthDropSubrack"),
        ("LUM-PM-MIB", "pmEthDropSlot"),
        ("LUM-PM-MIB", "pmEthDropPort"),
        ("LUM-PM-MIB", "pmEthDropRxPort"),
        ("LUM-PM-MIB", "pmEthDropResetCont"),
        ("LUM-PM-MIB", "pmEthDropFrames"),
        ("LUM-PM-MIB", "pmEthDropBytes"),
        ("LUM-PM-MIB", "pmEthDropYellowFrames"),
        ("LUM-PM-MIB", "pmEthDropRedFrames"),
        ("LUM-PM-MIB", "pmEthDropFramesQ1"),
        ("LUM-PM-MIB", "pmEthDropBytesQ1"),
        ("LUM-PM-MIB", "pmEthDropFramesQ2"),
        ("LUM-PM-MIB", "pmEthDropBytesQ2"),
        ("LUM-PM-MIB", "pmEthDropFramesQ3"),
        ("LUM-PM-MIB", "pmEthDropBytesQ3"),
        ("LUM-PM-MIB", "pmEthDropFramesQ4"),
        ("LUM-PM-MIB", "pmEthDropBytesQ4"),
        ("LUM-PM-MIB", "pmEthDropFramesQ5"),
        ("LUM-PM-MIB", "pmEthDropBytesQ5"),
        ("LUM-PM-MIB", "pmEthDropFramesQ6"),
        ("LUM-PM-MIB", "pmEthDropBytesQ6"),
        ("LUM-PM-MIB", "pmEthDropFramesQ7"),
        ("LUM-PM-MIB", "pmEthDropBytesQ7"),
        ("LUM-PM-MIB", "pmEthDropFramesQ8"),
        ("LUM-PM-MIB", "pmEthDropBytesQ8"),
        ("LUM-PM-MIB", "pmEthDropIfNo"),
        ("LUM-PM-MIB", "pmEthDropUpPortId"),
        ("LUM-PM-MIB", "pmEthDropReset15m"),
        ("LUM-PM-MIB", "pmEthDropReset24h"),
        ("LUM-PM-MIB", "pmEthDropReportMode"),
        ("LUM-PM-MIB", "pmEthDropIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthDropIsSuspect24H"))
)
if mibBuilder.loadTexts:
    pmEthDropGroupV3.setStatus("current")

pmEthEgressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 64)
)
pmEthEgressGroup.setObjects(
      *(("LUM-PM-MIB", "pmEthEgressIndex"),
        ("LUM-PM-MIB", "pmEthEgressName"),
        ("LUM-PM-MIB", "pmEthEgressSubrack"),
        ("LUM-PM-MIB", "pmEthEgressSlot"),
        ("LUM-PM-MIB", "pmEthEgressPort"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ1"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ1"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ1"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ1"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ1"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ1"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ1"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ2"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ2"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ2"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ2"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ2"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ2"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ2"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ3"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ3"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ3"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ3"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ3"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ3"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ3"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ4"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ4"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ4"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ4"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ4"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ4"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ4"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ5"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ5"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ5"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ5"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ5"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ5"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ5"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ6"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ6"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ6"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ6"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ6"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ6"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ6"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ7"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ7"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ7"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ7"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ7"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ7"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ7"),
        ("LUM-PM-MIB", "pmEthEgressFramesQ8"),
        ("LUM-PM-MIB", "pmEthEgressBytesQ8"),
        ("LUM-PM-MIB", "pmEthEgressBandwidthQ8"),
        ("LUM-PM-MIB", "pmEthEgressFrames15mQ8"),
        ("LUM-PM-MIB", "pmEthEgressBytes15mQ8"),
        ("LUM-PM-MIB", "pmEthEgressFrames24hQ8"),
        ("LUM-PM-MIB", "pmEthEgressBytes24hQ8"),
        ("LUM-PM-MIB", "pmEthEgressResetCont"),
        ("LUM-PM-MIB", "pmEthEgressReset15m"),
        ("LUM-PM-MIB", "pmEthEgressReset24h"),
        ("LUM-PM-MIB", "pmEthEgressReportMode"),
        ("LUM-PM-MIB", "pmEthEgressIsSuspect15Min"),
        ("LUM-PM-MIB", "pmEthEgressIsSuspect24H"))
)
if mibBuilder.loadTexts:
    pmEthEgressGroup.setStatus("current")


# Notification objects

pmFileAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 4, 0, 1)
)
pmFileAdded.setObjects(
      *(("LUM-PM-MIB", "pmFileIndex"),
        ("LUM-PM-MIB", "pmFileName"),
        ("LUM-PM-MIB", "pmFileCreatedTime"),
        ("LUM-PM-MIB", "pmFileSeqNumber"))
)
if mibBuilder.loadTexts:
    pmFileAdded.setStatus(
        "current"
    )

pmFile24hAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 2, 4, 0, 2)
)
pmFile24hAdded.setObjects(
      *(("LUM-PM-MIB", "pmFile24hIndex"),
        ("LUM-PM-MIB", "pmFile24hName"),
        ("LUM-PM-MIB", "pmFile24hCreatedTime"),
        ("LUM-PM-MIB", "pmFile24hSeqNumber"))
)
if mibBuilder.loadTexts:
    pmFile24hAdded.setStatus(
        "current"
    )


# Notifications groups

pmNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 1, 10)
)
pmNotificationGroup.setObjects(
      *(("LUM-PM-MIB", "pmFileAdded"),
        ("LUM-PM-MIB", "pmFile24hAdded"))
)
if mibBuilder.loadTexts:
    pmNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

lumPmBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 1)
)
lumPmBasicComplV1.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroup"),
        ("LUM-PM-MIB", "pmIfGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV1.setStatus(
        "deprecated"
    )

lumPmBasicComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 2)
)
lumPmBasicComplV2.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroup"),
        ("LUM-PM-MIB", "pmIfGroupV2"),
        ("LUM-PM-MIB", "pmIntervalGroup"),
        ("LUM-PM-MIB", "pmInterval24hGroup"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroup"),
        ("LUM-PM-MIB", "pmFile24hGroup"),
        ("LUM-PM-MIB", "pmNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV2.setStatus(
        "deprecated"
    )

lumPmBasicComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 3)
)
lumPmBasicComplV3.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV2"),
        ("LUM-PM-MIB", "pmIfGroupV2"),
        ("LUM-PM-MIB", "pmIntervalGroup"),
        ("LUM-PM-MIB", "pmInterval24hGroup"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroup"),
        ("LUM-PM-MIB", "pmFile24hGroup"),
        ("LUM-PM-MIB", "pmNotificationGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV3.setStatus(
        "deprecated"
    )

lumPmBasicComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 4)
)
lumPmBasicComplV4.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV2"),
        ("LUM-PM-MIB", "pmIfGroupV3"),
        ("LUM-PM-MIB", "pmIntervalGroup"),
        ("LUM-PM-MIB", "pmInterval24hGroup"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroup"),
        ("LUM-PM-MIB", "pmFile24hGroup"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV4.setStatus(
        "deprecated"
    )

lumPmBasicComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 5)
)
lumPmBasicComplV5.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV2"),
        ("LUM-PM-MIB", "pmIfGroupV3"),
        ("LUM-PM-MIB", "pmIntervalGroup"),
        ("LUM-PM-MIB", "pmInterval24hGroup"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroupV2"),
        ("LUM-PM-MIB", "pmFile24hGroupV2"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV5.setStatus(
        "deprecated"
    )

lumPmBasicComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 6)
)
lumPmBasicComplV6.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV2"),
        ("LUM-PM-MIB", "pmIfGroupV4"),
        ("LUM-PM-MIB", "pmIntervalGroup"),
        ("LUM-PM-MIB", "pmInterval24hGroup"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroupV2"),
        ("LUM-PM-MIB", "pmFile24hGroupV2"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV6.setStatus(
        "deprecated"
    )

lumPmBasicComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 7)
)
lumPmBasicComplV7.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV2"),
        ("LUM-PM-MIB", "pmIfGroupV5"),
        ("LUM-PM-MIB", "pmIntervalGroup"),
        ("LUM-PM-MIB", "pmInterval24hGroup"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroupV3"),
        ("LUM-PM-MIB", "pmFile24hGroupV3"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV7.setStatus(
        "deprecated"
    )

lumPmBasicComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 8)
)
lumPmBasicComplV8.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV2"),
        ("LUM-PM-MIB", "pmIfGroupV5"),
        ("LUM-PM-MIB", "pmIntervalGroup"),
        ("LUM-PM-MIB", "pmInterval24hGroup"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV8.setStatus(
        "deprecated"
    )

lumPmBasicComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 9)
)
lumPmBasicComplV9.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV2"),
        ("LUM-PM-MIB", "pmIfGroupV6"),
        ("LUM-PM-MIB", "pmIntervalGroupV2"),
        ("LUM-PM-MIB", "pmInterval24hGroupV2"),
        ("LUM-PM-MIB", "pmLogGeneralGroup"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV9.setStatus(
        "deprecated"
    )

lumPmBasicComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 10)
)
lumPmBasicComplV10.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV3"),
        ("LUM-PM-MIB", "pmIfGroupV7"),
        ("LUM-PM-MIB", "pmIntervalGroupV3"),
        ("LUM-PM-MIB", "pmInterval24hGroupV3"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV2"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV10.setStatus(
        "deprecated"
    )

lumPmBasicComplV11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 11)
)
lumPmBasicComplV11.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV3"),
        ("LUM-PM-MIB", "pmIfGroupV7"),
        ("LUM-PM-MIB", "pmIntervalGroupV4"),
        ("LUM-PM-MIB", "pmInterval24hGroupV4"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV3"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV11.setStatus(
        "deprecated"
    )

lumPmBasicComplV12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 12)
)
lumPmBasicComplV12.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV3"),
        ("LUM-PM-MIB", "pmIfGroupV8"),
        ("LUM-PM-MIB", "pmIntervalGroupV5"),
        ("LUM-PM-MIB", "pmInterval24hGroupV5"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV3"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV12.setStatus(
        "deprecated"
    )

lumPmBasicComplV13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 13)
)
lumPmBasicComplV13.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV3"),
        ("LUM-PM-MIB", "pmIfGroupV8"),
        ("LUM-PM-MIB", "pmIntervalGroupV5"),
        ("LUM-PM-MIB", "pmInterval24hGroupV5"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV4"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV13.setStatus(
        "deprecated"
    )

lumPmBasicComplV14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 14)
)
lumPmBasicComplV14.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV9"),
        ("LUM-PM-MIB", "pmEthTdGroup"),
        ("LUM-PM-MIB", "pmEthTmGroup"),
        ("LUM-PM-MIB", "pmEthOamGroup"),
        ("LUM-PM-MIB", "pmIntervalGroupV5"),
        ("LUM-PM-MIB", "pmInterval24hGroupV5"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV4"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV14.setStatus(
        "deprecated"
    )

lumPmBasicComplV15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 15)
)
lumPmBasicComplV15.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV9"),
        ("LUM-PM-MIB", "pmEthTdGroupV2"),
        ("LUM-PM-MIB", "pmEthTmGroup"),
        ("LUM-PM-MIB", "pmEthOamGroup"),
        ("LUM-PM-MIB", "pmIntervalGroupV7"),
        ("LUM-PM-MIB", "pmInterval24hGroupV7"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV4"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV15.setStatus(
        "deprecated"
    )

lumPmBasicComplV16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 16)
)
lumPmBasicComplV16.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV10"),
        ("LUM-PM-MIB", "pmEthTdGroupV2"),
        ("LUM-PM-MIB", "pmEthTmGroup"),
        ("LUM-PM-MIB", "pmEthOamGroup"),
        ("LUM-PM-MIB", "pmIntervalGroupV7"),
        ("LUM-PM-MIB", "pmInterval24hGroupV7"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV4"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV16.setStatus(
        "deprecated"
    )

lumPmBasicComplV17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 17)
)
lumPmBasicComplV17.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV3"),
        ("LUM-PM-MIB", "pmEthTmGroup"),
        ("LUM-PM-MIB", "pmEthOamGroup"),
        ("LUM-PM-MIB", "pmIntervalGroupV8"),
        ("LUM-PM-MIB", "pmInterval24hGroupV8"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV4"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroup"),
        ("LUM-PM-MIB", "pmEthClassificationGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV17.setStatus(
        "deprecated"
    )

lumPmBasicComplV18 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 18)
)
lumPmBasicComplV18.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV3"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV4"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroup"),
        ("LUM-PM-MIB", "pmEthClassificationGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV18.setStatus(
        "deprecated"
    )

lumPmBasicComplV19 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 19)
)
lumPmBasicComplV19.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV3"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV5"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroup"),
        ("LUM-PM-MIB", "pmEthClassificationGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV19.setStatus(
        "deprecated"
    )

lumPmBasicComplV20 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 20)
)
lumPmBasicComplV20.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV3"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV5"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroup"),
        ("LUM-PM-MIB", "pmEthClassificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV20.setStatus(
        "deprecated"
    )

lumPmBasicComplV21 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 21)
)
lumPmBasicComplV21.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV4"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV5"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroup"),
        ("LUM-PM-MIB", "pmEthClassificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV21.setStatus(
        "deprecated"
    )

lumPmBasicComplV22 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 22)
)
lumPmBasicComplV22.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV4"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV5"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV5"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroup"),
        ("LUM-PM-MIB", "pmEthClassificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV22.setStatus(
        "deprecated"
    )

lumPmBasicComplV23 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 23)
)
lumPmBasicComplV23.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV5"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV5"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV5"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroupV2"),
        ("LUM-PM-MIB", "pmEthClassificationGroupV2"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV23.setStatus(
        "deprecated"
    )

lumPmBasicComplV24 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 15, 1, 2, 24)
)
lumPmBasicComplV24.setObjects(
      *(("LUM-PM-MIB", "pmGeneralGroupV5"),
        ("LUM-PM-MIB", "pmIfGroupV11"),
        ("LUM-PM-MIB", "pmEthTdGroupV5"),
        ("LUM-PM-MIB", "pmLogGeneralGroupV5"),
        ("LUM-PM-MIB", "pmFileGroupV4"),
        ("LUM-PM-MIB", "pmFile24hGroupV4"),
        ("LUM-PM-MIB", "pmNotificationGroup"),
        ("LUM-PM-MIB", "pmControlGroupV2"),
        ("LUM-PM-MIB", "pmEthDropGroupV3"),
        ("LUM-PM-MIB", "pmEthClassificationGroupV2"),
        ("LUM-PM-MIB", "pmEthEgressGroup"))
)
if mibBuilder.loadTexts:
    lumPmBasicComplV24.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-PM-MIB",
    **{"PmInterval15mNumber": PmInterval15mNumber,
       "PmInterval24hNumber": PmInterval24hNumber,
       "lumPmMIBModule": lumPmMIBModule,
       "lumPmConfs": lumPmConfs,
       "lumPmGroups": lumPmGroups,
       "pmGeneralGroup": pmGeneralGroup,
       "pmIntervalGroup": pmIntervalGroup,
       "pmInterval24hGroup": pmInterval24hGroup,
       "pmIfGroup": pmIfGroup,
       "pmLogGeneralGroup": pmLogGeneralGroup,
       "pmFileGroup": pmFileGroup,
       "pmFile24hGroup": pmFile24hGroup,
       "pmNotificationGroup": pmNotificationGroup,
       "pmIfGroupV2": pmIfGroupV2,
       "pmGeneralGroupV2": pmGeneralGroupV2,
       "pmControlGroup": pmControlGroup,
       "pmIfGroupV3": pmIfGroupV3,
       "pmFileGroupV2": pmFileGroupV2,
       "pmFile24hGroupV2": pmFile24hGroupV2,
       "pmIfGroupV4": pmIfGroupV4,
       "pmIfGroupV5": pmIfGroupV5,
       "pmFileGroupV3": pmFileGroupV3,
       "pmFile24hGroupV3": pmFile24hGroupV3,
       "pmFileGroupV4": pmFileGroupV4,
       "pmFile24hGroupV4": pmFile24hGroupV4,
       "pmIntervalGroupV2": pmIntervalGroupV2,
       "pmInterval24hGroupV2": pmInterval24hGroupV2,
       "pmIfGroupV6": pmIfGroupV6,
       "pmLogGeneralGroupV2": pmLogGeneralGroupV2,
       "pmIntervalGroupV3": pmIntervalGroupV3,
       "pmInterval24hGroupV3": pmInterval24hGroupV3,
       "pmIfGroupV7": pmIfGroupV7,
       "pmGeneralGroupV3": pmGeneralGroupV3,
       "pmLogGeneralGroupV3": pmLogGeneralGroupV3,
       "pmIntervalGroupV4": pmIntervalGroupV4,
       "pmInterval24hGroupV4": pmInterval24hGroupV4,
       "pmIfGroupV8": pmIfGroupV8,
       "pmIntervalGroupV5": pmIntervalGroupV5,
       "pmInterval24hGroupV5": pmInterval24hGroupV5,
       "pmLogGeneralGroupV4": pmLogGeneralGroupV4,
       "pmIfGroupV9": pmIfGroupV9,
       "pmIntervalGroupV6": pmIntervalGroupV6,
       "pmInterval24hGroupV6": pmInterval24hGroupV6,
       "pmEthTdGroup": pmEthTdGroup,
       "pmEthTmGroup": pmEthTmGroup,
       "pmEthOamGroup": pmEthOamGroup,
       "pmGeneralGroupV4": pmGeneralGroupV4,
       "pmEthTdGroupV2": pmEthTdGroupV2,
       "pmIntervalGroupV7": pmIntervalGroupV7,
       "pmInterval24hGroupV7": pmInterval24hGroupV7,
       "pmIntervalGroupV8": pmIntervalGroupV8,
       "pmInterval24hGroupV8": pmInterval24hGroupV8,
       "pmIfGroupV10": pmIfGroupV10,
       "pmIfGroupV11": pmIfGroupV11,
       "pmEthTdGroupV3": pmEthTdGroupV3,
       "pmControlGroupV2": pmControlGroupV2,
       "pmEthDropGroup": pmEthDropGroup,
       "pmEthClassificationGroup": pmEthClassificationGroup,
       "pmLogGeneralGroupV5": pmLogGeneralGroupV5,
       "pmEthClassificationGroupV2": pmEthClassificationGroupV2,
       "pmEthTdGroupV4": pmEthTdGroupV4,
       "pmEthTdGroupV5": pmEthTdGroupV5,
       "pmIfGroupV12": pmIfGroupV12,
       "pmGeneralGroupV5": pmGeneralGroupV5,
       "pmEthDropGroupV2": pmEthDropGroupV2,
       "pmEthDropGroupV3": pmEthDropGroupV3,
       "pmEthEgressGroup": pmEthEgressGroup,
       "lumPmCompl": lumPmCompl,
       "lumPmBasicComplV1": lumPmBasicComplV1,
       "lumPmBasicComplV2": lumPmBasicComplV2,
       "lumPmBasicComplV3": lumPmBasicComplV3,
       "lumPmBasicComplV4": lumPmBasicComplV4,
       "lumPmBasicComplV5": lumPmBasicComplV5,
       "lumPmBasicComplV6": lumPmBasicComplV6,
       "lumPmBasicComplV7": lumPmBasicComplV7,
       "lumPmBasicComplV8": lumPmBasicComplV8,
       "lumPmBasicComplV9": lumPmBasicComplV9,
       "lumPmBasicComplV10": lumPmBasicComplV10,
       "lumPmBasicComplV11": lumPmBasicComplV11,
       "lumPmBasicComplV12": lumPmBasicComplV12,
       "lumPmBasicComplV13": lumPmBasicComplV13,
       "lumPmBasicComplV14": lumPmBasicComplV14,
       "lumPmBasicComplV15": lumPmBasicComplV15,
       "lumPmBasicComplV16": lumPmBasicComplV16,
       "lumPmBasicComplV17": lumPmBasicComplV17,
       "lumPmBasicComplV18": lumPmBasicComplV18,
       "lumPmBasicComplV19": lumPmBasicComplV19,
       "lumPmBasicComplV20": lumPmBasicComplV20,
       "lumPmBasicComplV21": lumPmBasicComplV21,
       "lumPmBasicComplV22": lumPmBasicComplV22,
       "lumPmBasicComplV23": lumPmBasicComplV23,
       "lumPmBasicComplV24": lumPmBasicComplV24,
       "lumPmMIBObjects": lumPmMIBObjects,
       "pmGeneral": pmGeneral,
       "pmGeneralLastChangeTime": pmGeneralLastChangeTime,
       "pmGeneralStateLastChangeTime": pmGeneralStateLastChangeTime,
       "pmGeneralPmIfTableSize": pmGeneralPmIfTableSize,
       "pmGeneralPmEthTdTableSize": pmGeneralPmEthTdTableSize,
       "pmGeneralPmEthTmTableSize": pmGeneralPmEthTmTableSize,
       "pmGeneralPmEthOamTableSize": pmGeneralPmEthOamTableSize,
       "pmGeneralPmEthDropTableSize": pmGeneralPmEthDropTableSize,
       "pmGeneralPmEthClassificationTableSize": pmGeneralPmEthClassificationTableSize,
       "pmGeneralPmMpoLanesTableSize": pmGeneralPmMpoLanesTableSize,
       "pmInterval": pmInterval,
       "pmIntervalTable": pmIntervalTable,
       "pmIntervalEntry": pmIntervalEntry,
       "pmIntervalSubrack": pmIntervalSubrack,
       "pmIntervalSlot": pmIntervalSlot,
       "pmIntervalPort": pmIntervalPort,
       "pmIntervalNumber": pmIntervalNumber,
       "pmIntervalIsSuspect": pmIntervalIsSuspect,
       "pmIntervalRxES": pmIntervalRxES,
       "pmIntervalRxSES": pmIntervalRxSES,
       "pmIntervalRxBBE": pmIntervalRxBBE,
       "pmIntervalRxUAS": pmIntervalRxUAS,
       "pmIntervalTxES": pmIntervalTxES,
       "pmIntervalTxSES": pmIntervalTxSES,
       "pmIntervalTxBBE": pmIntervalTxBBE,
       "pmIntervalTxUAS": pmIntervalTxUAS,
       "pmIntervalName": pmIntervalName,
       "pmIntervalRxPowerLevel": pmIntervalRxPowerLevel,
       "pmIntervalGbeMaxUtilization": pmIntervalGbeMaxUtilization,
       "pmIntervalTxPowerLevel": pmIntervalTxPowerLevel,
       "pmIntervalRxUndersizedFrames": pmIntervalRxUndersizedFrames,
       "pmIntervalRxOversizedFrames": pmIntervalRxOversizedFrames,
       "pmIntervalRxFragments": pmIntervalRxFragments,
       "pmIntervalRxFcsErrors": pmIntervalRxFcsErrors,
       "pmIntervalRxInvalidCeVlanId": pmIntervalRxInvalidCeVlanId,
       "pmIntervalTxOctets": pmIntervalTxOctets,
       "pmIntervalTxFrames": pmIntervalTxFrames,
       "pmIntervalTxUnicastFrames": pmIntervalTxUnicastFrames,
       "pmIntervalTxMulticastFrames": pmIntervalTxMulticastFrames,
       "pmIntervalTxBroadcastFrames": pmIntervalTxBroadcastFrames,
       "pmIntervalRxOctets": pmIntervalRxOctets,
       "pmIntervalRxFrames": pmIntervalRxFrames,
       "pmIntervalRxUnicastFrames": pmIntervalRxUnicastFrames,
       "pmIntervalRxMulticastFrames": pmIntervalRxMulticastFrames,
       "pmIntervalRxBroadcastFrames": pmIntervalRxBroadcastFrames,
       "pmIntervalIngressGreenFrameCount": pmIntervalIngressGreenFrameCount,
       "pmIntervalIngressYellowFrameCount": pmIntervalIngressYellowFrameCount,
       "pmIntervalIngressRedFrameCount": pmIntervalIngressRedFrameCount,
       "pmIntervalIngressGreenOctetCount": pmIntervalIngressGreenOctetCount,
       "pmIntervalIngressYellowOctetCount": pmIntervalIngressYellowOctetCount,
       "pmIntervalIngressRedOctetCount": pmIntervalIngressRedOctetCount,
       "pmIntervalEgressGreenFrameCount": pmIntervalEgressGreenFrameCount,
       "pmIntervalEgressGreenOctetCount": pmIntervalEgressGreenOctetCount,
       "pmIntervalGreenFrameDiscards": pmIntervalGreenFrameDiscards,
       "pmIntervalYellowFrameDiscards": pmIntervalYellowFrameDiscards,
       "pmIntervalGreenOctetDiscards": pmIntervalGreenOctetDiscards,
       "pmIntervalYellowOctetDiscards": pmIntervalYellowOctetDiscards,
       "pmIntervalTwoWayFrameDelay": pmIntervalTwoWayFrameDelay,
       "pmIntervalTwoWayFrameDelayVariation": pmIntervalTwoWayFrameDelayVariation,
       "pmIntervalFrameLossRatioNearEnd": pmIntervalFrameLossRatioNearEnd,
       "pmIntervalFrameLossRatioFarEnd": pmIntervalFrameLossRatioFarEnd,
       "pmIntervalUnavailabilityNearEnd": pmIntervalUnavailabilityNearEnd,
       "pmIntervalUnavailabilityFarEnd": pmIntervalUnavailabilityFarEnd,
       "pmIntervalOneWayFrameDelayVariation": pmIntervalOneWayFrameDelayVariation,
       "pmIntervalTxEthMaxUtilization": pmIntervalTxEthMaxUtilization,
       "pmIntervalRxEthMaxUtilization": pmIntervalRxEthMaxUtilization,
       "pmIntervalStartTime": pmIntervalStartTime,
       "pmIntervalStopTime": pmIntervalStopTime,
       "pmInterval24h": pmInterval24h,
       "pmInterval24hTable": pmInterval24hTable,
       "pmInterval24hEntry": pmInterval24hEntry,
       "pmInterval24hSubrack": pmInterval24hSubrack,
       "pmInterval24hSlot": pmInterval24hSlot,
       "pmInterval24hPort": pmInterval24hPort,
       "pmInterval24hNumber": pmInterval24hNumber,
       "pmInterval24hIsSuspect": pmInterval24hIsSuspect,
       "pmInterval24hRxES": pmInterval24hRxES,
       "pmInterval24hRxSES": pmInterval24hRxSES,
       "pmInterval24hRxBBE": pmInterval24hRxBBE,
       "pmInterval24hRxUAS": pmInterval24hRxUAS,
       "pmInterval24hTxES": pmInterval24hTxES,
       "pmInterval24hTxSES": pmInterval24hTxSES,
       "pmInterval24hTxBBE": pmInterval24hTxBBE,
       "pmInterval24hTxUAS": pmInterval24hTxUAS,
       "pmInterval24hName": pmInterval24hName,
       "pmInterval24hRxPowerLevel": pmInterval24hRxPowerLevel,
       "pmInterval24hGbeMaxUtilization": pmInterval24hGbeMaxUtilization,
       "pmInterval24hTxPowerLevel": pmInterval24hTxPowerLevel,
       "pmInterval24hRxUndersizedFrames": pmInterval24hRxUndersizedFrames,
       "pmInterval24hRxOversizedFrames": pmInterval24hRxOversizedFrames,
       "pmInterval24hRxFragments": pmInterval24hRxFragments,
       "pmInterval24hRxFcsErrors": pmInterval24hRxFcsErrors,
       "pmInterval24hRxInvalidCeVlanId": pmInterval24hRxInvalidCeVlanId,
       "pmInterval24hTxOctets": pmInterval24hTxOctets,
       "pmInterval24hTxFrames": pmInterval24hTxFrames,
       "pmInterval24hTxUnicastFrames": pmInterval24hTxUnicastFrames,
       "pmInterval24hTxMulticastFrames": pmInterval24hTxMulticastFrames,
       "pmInterval24hTxBroadcastFrames": pmInterval24hTxBroadcastFrames,
       "pmInterval24hRxOctets": pmInterval24hRxOctets,
       "pmInterval24hRxFrames": pmInterval24hRxFrames,
       "pmInterval24hRxUnicastFrames": pmInterval24hRxUnicastFrames,
       "pmInterval24hRxMulticastFrames": pmInterval24hRxMulticastFrames,
       "pmInterval24hRxBroadcastFrames": pmInterval24hRxBroadcastFrames,
       "pmInterval24hIngressGreenFrameCount": pmInterval24hIngressGreenFrameCount,
       "pmInterval24hIngressYellowFrameCount": pmInterval24hIngressYellowFrameCount,
       "pmInterval24hIngressRedFrameCount": pmInterval24hIngressRedFrameCount,
       "pmInterval24hIngressGreenOctetCount": pmInterval24hIngressGreenOctetCount,
       "pmInterval24hIngressYellowOctetCount": pmInterval24hIngressYellowOctetCount,
       "pmInterval24hIngressRedOctetCount": pmInterval24hIngressRedOctetCount,
       "pmInterval24hEgressGreenFrameCount": pmInterval24hEgressGreenFrameCount,
       "pmInterval24hEgressGreenOctetCount": pmInterval24hEgressGreenOctetCount,
       "pmInterval24hGreenFrameDiscards": pmInterval24hGreenFrameDiscards,
       "pmInterval24hYellowFrameDiscards": pmInterval24hYellowFrameDiscards,
       "pmInterval24hGreenOctetDiscards": pmInterval24hGreenOctetDiscards,
       "pmInterval24hYellowOctetDiscards": pmInterval24hYellowOctetDiscards,
       "pmInterval24hTwoWayFrameDelay": pmInterval24hTwoWayFrameDelay,
       "pmInterval24hTwoWayFrameDelayVariation": pmInterval24hTwoWayFrameDelayVariation,
       "pmInterval24hFrameLossRatioNearEnd": pmInterval24hFrameLossRatioNearEnd,
       "pmInterval24hFrameLossRatioFarEnd": pmInterval24hFrameLossRatioFarEnd,
       "pmInterval24hUnavailabilityNearEnd": pmInterval24hUnavailabilityNearEnd,
       "pmInterval24hUnavailabilityFarEnd": pmInterval24hUnavailabilityFarEnd,
       "pmInterval24hOneWayFrameDelayVariation": pmInterval24hOneWayFrameDelayVariation,
       "pmInterval24hTxEthMaxUtilization": pmInterval24hTxEthMaxUtilization,
       "pmInterval24hRxEthMaxUtilization": pmInterval24hRxEthMaxUtilization,
       "pmInterval24hStartTime": pmInterval24hStartTime,
       "pmInterval24hStopTime": pmInterval24hStopTime,
       "lumentisPmNotifications": lumentisPmNotifications,
       "pmNotifyPrefix": pmNotifyPrefix,
       "pmFileAdded": pmFileAdded,
       "pmFile24hAdded": pmFile24hAdded,
       "pmFile": pmFile,
       "pmFileTable": pmFileTable,
       "pmFileEntry": pmFileEntry,
       "pmFileIndex": pmFileIndex,
       "pmFileName": pmFileName,
       "pmFileCreatedTime": pmFileCreatedTime,
       "pmFileSeqNumber": pmFileSeqNumber,
       "pmFileStartTime": pmFileStartTime,
       "pmFileStopTime": pmFileStopTime,
       "pmFileUrl": pmFileUrl,
       "pmIfList": pmIfList,
       "pmIfTable": pmIfTable,
       "pmIfEntry": pmIfEntry,
       "pmIfIndex": pmIfIndex,
       "pmIfName": pmIfName,
       "pmIfSubrack": pmIfSubrack,
       "pmIfSlot": pmIfSlot,
       "pmIfPort": pmIfPort,
       "pmIfPmReportMode": pmIfPmReportMode,
       "pmIfRxCurrentES": pmIfRxCurrentES,
       "pmIfRxCurrentSES": pmIfRxCurrentSES,
       "pmIfRxCurrentBBE": pmIfRxCurrentBBE,
       "pmIfRxCurrentUAS": pmIfRxCurrentUAS,
       "pmIfTxCurrentES": pmIfTxCurrentES,
       "pmIfTxCurrentSES": pmIfTxCurrentSES,
       "pmIfTxCurrentBBE": pmIfTxCurrentBBE,
       "pmIfTxCurrentUAS": pmIfTxCurrentUAS,
       "pmIfRx24hCurrentES": pmIfRx24hCurrentES,
       "pmIfRx24hCurrentSES": pmIfRx24hCurrentSES,
       "pmIfRx24hCurrentBBE": pmIfRx24hCurrentBBE,
       "pmIfRx24hCurrentUAS": pmIfRx24hCurrentUAS,
       "pmIfTx24hCurrentES": pmIfTx24hCurrentES,
       "pmIfTx24hCurrentSES": pmIfTx24hCurrentSES,
       "pmIfTx24hCurrentBBE": pmIfTx24hCurrentBBE,
       "pmIfTx24hCurrentUAS": pmIfTx24hCurrentUAS,
       "pmIfRxESThreshold": pmIfRxESThreshold,
       "pmIfRxSESThreshold": pmIfRxSESThreshold,
       "pmIfRxBBEThreshold": pmIfRxBBEThreshold,
       "pmIfRxUASThreshold": pmIfRxUASThreshold,
       "pmIfTxESThreshold": pmIfTxESThreshold,
       "pmIfTxSESThreshold": pmIfTxSESThreshold,
       "pmIfTxBBEThreshold": pmIfTxBBEThreshold,
       "pmIfTxUASThreshold": pmIfTxUASThreshold,
       "pmIfRx24hESThreshold": pmIfRx24hESThreshold,
       "pmIfRx24hSESThreshold": pmIfRx24hSESThreshold,
       "pmIfRx24hBBEThreshold": pmIfRx24hBBEThreshold,
       "pmIfRx24hUASThreshold": pmIfRx24hUASThreshold,
       "pmIfTx24hESThreshold": pmIfTx24hESThreshold,
       "pmIfTx24hSESThreshold": pmIfTx24hSESThreshold,
       "pmIfTx24hBBEThreshold": pmIfTx24hBBEThreshold,
       "pmIfTx24hUASThreshold": pmIfTx24hUASThreshold,
       "pmIfRxES": pmIfRxES,
       "pmIfRxSES": pmIfRxSES,
       "pmIfRxBBE": pmIfRxBBE,
       "pmIfRxUAS": pmIfRxUAS,
       "pmIfTxES": pmIfTxES,
       "pmIfTxSES": pmIfTxSES,
       "pmIfTxBBE": pmIfTxBBE,
       "pmIfTxUAS": pmIfTxUAS,
       "pmIfRx24hES": pmIfRx24hES,
       "pmIfRx24hSES": pmIfRx24hSES,
       "pmIfRx24hBBE": pmIfRx24hBBE,
       "pmIfRx24hUAS": pmIfRx24hUAS,
       "pmIfTx24hES": pmIfTx24hES,
       "pmIfTx24hSES": pmIfTx24hSES,
       "pmIfTx24hBBE": pmIfTx24hBBE,
       "pmIfTx24hUAS": pmIfTx24hUAS,
       "pmIfRxPort": pmIfRxPort,
       "pmIfReset15Min": pmIfReset15Min,
       "pmIfReset24H": pmIfReset24H,
       "pmIfAdminStatus": pmIfAdminStatus,
       "pmIfOperStatus": pmIfOperStatus,
       "pmIfIsSuspect15Min": pmIfIsSuspect15Min,
       "pmIfIsSuspect24H": pmIfIsSuspect24H,
       "pmIfInstallCommand": pmIfInstallCommand,
       "pmIfRxPowerLevel": pmIfRxPowerLevel,
       "pmIfInitialPowerLevel": pmIfInitialPowerLevel,
       "pmIfRxGbeMaxUtilization": pmIfRxGbeMaxUtilization,
       "pmIfRx24hGbeMaxUtilization": pmIfRx24hGbeMaxUtilization,
       "pmIfTxPowerLevel": pmIfTxPowerLevel,
       "pmIfObjectProperty": pmIfObjectProperty,
       "pmIfDelay": pmIfDelay,
       "pmIfRxBEREstimation": pmIfRxBEREstimation,
       "pmIfIfNo": pmIfIfNo,
       "pmIfUpPortId": pmIfUpPortId,
       "pmLogGeneral": pmLogGeneral,
       "pmLogGeneralLastChangeTime": pmLogGeneralLastChangeTime,
       "pmLogGeneralSize": pmLogGeneralSize,
       "pmLogGeneralSize24h": pmLogGeneralSize24h,
       "pmLogGeneralFileTableSize": pmLogGeneralFileTableSize,
       "pmLogGeneralFile24hTableSize": pmLogGeneralFile24hTableSize,
       "pmLogGeneralInterval15mTableSize": pmLogGeneralInterval15mTableSize,
       "pmLogGeneralInterval24hTableSize": pmLogGeneralInterval24hTableSize,
       "pmLogGeneralInterval15mShowNonZeroOnly": pmLogGeneralInterval15mShowNonZeroOnly,
       "pmLogGeneralInterval24hShowNonZeroOnly": pmLogGeneralInterval24hShowNonZeroOnly,
       "pmLogGeneralFile15mLastSeqNumber": pmLogGeneralFile15mLastSeqNumber,
       "pmLogGeneralFile24hLastSeqNumber": pmLogGeneralFile24hLastSeqNumber,
       "pmFile24h": pmFile24h,
       "pmFile24hTable": pmFile24hTable,
       "pmFile24hEntry": pmFile24hEntry,
       "pmFile24hIndex": pmFile24hIndex,
       "pmFile24hName": pmFile24hName,
       "pmFile24hCreatedTime": pmFile24hCreatedTime,
       "pmFile24hSeqNumber": pmFile24hSeqNumber,
       "pmFile24hStartTime": pmFile24hStartTime,
       "pmFile24hStopTime": pmFile24hStopTime,
       "pmFile24hUrl": pmFile24hUrl,
       "pmControl": pmControl,
       "pmControlReset15Min": pmControlReset15Min,
       "pmControlReset24H": pmControlReset24H,
       "pmControlResetCont": pmControlResetCont,
       "pmEthTdList": pmEthTdList,
       "pmEthTdTable": pmEthTdTable,
       "pmEthTdEntry": pmEthTdEntry,
       "pmEthTdIndex": pmEthTdIndex,
       "pmEthTdName": pmEthTdName,
       "pmEthTdSubrack": pmEthTdSubrack,
       "pmEthTdSlot": pmEthTdSlot,
       "pmEthTdPort": pmEthTdPort,
       "pmEthTdPmReportMode": pmEthTdPmReportMode,
       "pmEthTdRxPort": pmEthTdRxPort,
       "pmEthTdReset15Min": pmEthTdReset15Min,
       "pmEthTdReset24H": pmEthTdReset24H,
       "pmEthTdAdminStatus": pmEthTdAdminStatus,
       "pmEthTdOperStatus": pmEthTdOperStatus,
       "pmEthTdIsSuspect15Min": pmEthTdIsSuspect15Min,
       "pmEthTdIsSuspect24h": pmEthTdIsSuspect24h,
       "pmEthTdCurrentRxUndersizedFrames": pmEthTdCurrentRxUndersizedFrames,
       "pmEthTdCurrentRxOversizedFrames": pmEthTdCurrentRxOversizedFrames,
       "pmEthTdCurrentRxFragments": pmEthTdCurrentRxFragments,
       "pmEthTdCurrentRxFcsErrors": pmEthTdCurrentRxFcsErrors,
       "pmEthTdCurrentRxInvalidCeVlanId": pmEthTdCurrentRxInvalidCeVlanId,
       "pmEthTdCurrentTxOctets": pmEthTdCurrentTxOctets,
       "pmEthTdCurrentTxFrames": pmEthTdCurrentTxFrames,
       "pmEthTdCurrentTxUnicastFrames": pmEthTdCurrentTxUnicastFrames,
       "pmEthTdCurrentTxMulticastFrames": pmEthTdCurrentTxMulticastFrames,
       "pmEthTdCurrentTxBroadcastFrames": pmEthTdCurrentTxBroadcastFrames,
       "pmEthTdCurrentRxOctets": pmEthTdCurrentRxOctets,
       "pmEthTdCurrentRxFrames": pmEthTdCurrentRxFrames,
       "pmEthTdCurrentRxUnicastFrames": pmEthTdCurrentRxUnicastFrames,
       "pmEthTdCurrentRxMulticastFrames": pmEthTdCurrentRxMulticastFrames,
       "pmEthTdCurrentRxBroadcastFrames": pmEthTdCurrentRxBroadcastFrames,
       "pmEthTdCurrent24hRxUndersizedFrames": pmEthTdCurrent24hRxUndersizedFrames,
       "pmEthTdCurrent24hRxOversizedFrames": pmEthTdCurrent24hRxOversizedFrames,
       "pmEthTdCurrent24hRxFragments": pmEthTdCurrent24hRxFragments,
       "pmEthTdCurrent24hRxFcsErrors": pmEthTdCurrent24hRxFcsErrors,
       "pmEthTdCurrent24hRxInvalidCeVlanId": pmEthTdCurrent24hRxInvalidCeVlanId,
       "pmEthTdCurrent24hTxOctets": pmEthTdCurrent24hTxOctets,
       "pmEthTdCurrent24hTxFrames": pmEthTdCurrent24hTxFrames,
       "pmEthTdCurrent24hTxUnicastFrames": pmEthTdCurrent24hTxUnicastFrames,
       "pmEthTdCurrent24hTxMulticastFrames": pmEthTdCurrent24hTxMulticastFrames,
       "pmEthTdCurrent24hTxBroadcastFrames": pmEthTdCurrent24hTxBroadcastFrames,
       "pmEthTdCurrent24hRxOctets": pmEthTdCurrent24hRxOctets,
       "pmEthTdCurrent24hRxFrames": pmEthTdCurrent24hRxFrames,
       "pmEthTdCurrent24hRxUnicastFrames": pmEthTdCurrent24hRxUnicastFrames,
       "pmEthTdCurrent24hRxMulticastFrames": pmEthTdCurrent24hRxMulticastFrames,
       "pmEthTdCurrent24hRxBroadcastFrames": pmEthTdCurrent24hRxBroadcastFrames,
       "pmEthTdObjectProperty": pmEthTdObjectProperty,
       "pmEthTdRxUndersizedFramesThreshold": pmEthTdRxUndersizedFramesThreshold,
       "pmEthTdRxOversizedFramesThreshold": pmEthTdRxOversizedFramesThreshold,
       "pmEthTdRxFragmentsThreshold": pmEthTdRxFragmentsThreshold,
       "pmEthTdRxFcsErrorsThreshold": pmEthTdRxFcsErrorsThreshold,
       "pmEthTdRxInvalidCeVlanIdThreshold": pmEthTdRxInvalidCeVlanIdThreshold,
       "pmEthTd24hRxUndersizedFramesThreshold": pmEthTd24hRxUndersizedFramesThreshold,
       "pmEthTd24hRxOversizedFramesThreshold": pmEthTd24hRxOversizedFramesThreshold,
       "pmEthTd24hRxFragmentsThreshold": pmEthTd24hRxFragmentsThreshold,
       "pmEthTd24hRxFcsErrorsThreshold": pmEthTd24hRxFcsErrorsThreshold,
       "pmEthTd24hRxInvalidCeVlanIdThreshold": pmEthTd24hRxInvalidCeVlanIdThreshold,
       "pmEthTdRxUndersizedFrames": pmEthTdRxUndersizedFrames,
       "pmEthTdRxOversizedFrames": pmEthTdRxOversizedFrames,
       "pmEthTdRxFragments": pmEthTdRxFragments,
       "pmEthTdRxFcsErrors": pmEthTdRxFcsErrors,
       "pmEthTdRxInvalidCeVlanId": pmEthTdRxInvalidCeVlanId,
       "pmEthTd24hRxUndersizedFrames": pmEthTd24hRxUndersizedFrames,
       "pmEthTd24hRxOversizedFrames": pmEthTd24hRxOversizedFrames,
       "pmEthTd24hRxFragments": pmEthTd24hRxFragments,
       "pmEthTd24hRxFcsErrors": pmEthTd24hRxFcsErrors,
       "pmEthTd24hRxInvalidCeVlanId": pmEthTd24hRxInvalidCeVlanId,
       "pmEthTdCurrentTxEthMaxUtilization": pmEthTdCurrentTxEthMaxUtilization,
       "pmEthTdCurrentRxEthMaxUtilization": pmEthTdCurrentRxEthMaxUtilization,
       "pmEthTdCurrent24hTxEthMaxUtilization": pmEthTdCurrent24hTxEthMaxUtilization,
       "pmEthTdCurrent24hRxEthMaxUtilization": pmEthTdCurrent24hRxEthMaxUtilization,
       "pmEthTdResetCont": pmEthTdResetCont,
       "pmEthTdCurrentContRxUndersizedFrames": pmEthTdCurrentContRxUndersizedFrames,
       "pmEthTdCurrentContRxOversizedFrames": pmEthTdCurrentContRxOversizedFrames,
       "pmEthTdCurrentContRxFragments": pmEthTdCurrentContRxFragments,
       "pmEthTdCurrentContRxFcsErrors": pmEthTdCurrentContRxFcsErrors,
       "pmEthTdCurrentContRxInvalidCeVlanId": pmEthTdCurrentContRxInvalidCeVlanId,
       "pmEthTdCurrentContTxOctets": pmEthTdCurrentContTxOctets,
       "pmEthTdCurrentContTxFrames": pmEthTdCurrentContTxFrames,
       "pmEthTdCurrentContTxUnicastFrames": pmEthTdCurrentContTxUnicastFrames,
       "pmEthTdCurrentContTxMulticastFrames": pmEthTdCurrentContTxMulticastFrames,
       "pmEthTdCurrentContTxBroadcastFrames": pmEthTdCurrentContTxBroadcastFrames,
       "pmEthTdCurrentContRxOctets": pmEthTdCurrentContRxOctets,
       "pmEthTdCurrentContRxFrames": pmEthTdCurrentContRxFrames,
       "pmEthTdCurrentContRxUnicastFrames": pmEthTdCurrentContRxUnicastFrames,
       "pmEthTdCurrentContRxMulticastFrames": pmEthTdCurrentContRxMulticastFrames,
       "pmEthTdCurrentContRxBroadcastFrames": pmEthTdCurrentContRxBroadcastFrames,
       "pmEthTdVlanId": pmEthTdVlanId,
       "pmEthTdIfNo": pmEthTdIfNo,
       "pmEthTdUpPortId": pmEthTdUpPortId,
       "pmEthTmList": pmEthTmList,
       "pmEthTmTable": pmEthTmTable,
       "pmEthTmEntry": pmEthTmEntry,
       "pmEthTmIndex": pmEthTmIndex,
       "pmEthTmName": pmEthTmName,
       "pmEthTmSubrack": pmEthTmSubrack,
       "pmEthTmSlot": pmEthTmSlot,
       "pmEthTmPort": pmEthTmPort,
       "pmEthTmPmReportMode": pmEthTmPmReportMode,
       "pmEthTmRxPort": pmEthTmRxPort,
       "pmEthTmReset15Min": pmEthTmReset15Min,
       "pmEthTmReset24H": pmEthTmReset24H,
       "pmEthTmAdminStatus": pmEthTmAdminStatus,
       "pmEthTmOperStatus": pmEthTmOperStatus,
       "pmEthTmIsSuspect15Min": pmEthTmIsSuspect15Min,
       "pmEthTmIsSuspect24h": pmEthTmIsSuspect24h,
       "pmEthTmCurrentIngressGreenFrameCount": pmEthTmCurrentIngressGreenFrameCount,
       "pmEthTmCurrentIngressYellowFrameCount": pmEthTmCurrentIngressYellowFrameCount,
       "pmEthTmCurrentIngressRedFrameCount": pmEthTmCurrentIngressRedFrameCount,
       "pmEthTmCurrentIngressGreenOctetCount": pmEthTmCurrentIngressGreenOctetCount,
       "pmEthTmCurrentIngressYellowOctetCount": pmEthTmCurrentIngressYellowOctetCount,
       "pmEthTmCurrentIngressRedOctetCount": pmEthTmCurrentIngressRedOctetCount,
       "pmEthTmCurrentEgressGreenFrameCount": pmEthTmCurrentEgressGreenFrameCount,
       "pmEthTmCurrentEgressGreenOctetCount": pmEthTmCurrentEgressGreenOctetCount,
       "pmEthTmCurrentGreenFrameDiscards": pmEthTmCurrentGreenFrameDiscards,
       "pmEthTmCurrentYellowFrameDiscards": pmEthTmCurrentYellowFrameDiscards,
       "pmEthTmCurrentGreenOctetDiscards": pmEthTmCurrentGreenOctetDiscards,
       "pmEthTmCurrentYellowOctetDiscards": pmEthTmCurrentYellowOctetDiscards,
       "pmEthTmCurrent24hIngressGreenFrameCount": pmEthTmCurrent24hIngressGreenFrameCount,
       "pmEthTmCurrent24hIngressYellowFrameCount": pmEthTmCurrent24hIngressYellowFrameCount,
       "pmEthTmCurrent24hIngressRedFrameCount": pmEthTmCurrent24hIngressRedFrameCount,
       "pmEthTmCurrent24hIngressGreenOctetCount": pmEthTmCurrent24hIngressGreenOctetCount,
       "pmEthTmCurrent24hIngressYellowOctetCount": pmEthTmCurrent24hIngressYellowOctetCount,
       "pmEthTmCurrent24hIngressRedOctetCount": pmEthTmCurrent24hIngressRedOctetCount,
       "pmEthTmCurrent24hEgressGreenFrameCount": pmEthTmCurrent24hEgressGreenFrameCount,
       "pmEthTmCurrent24hEgressGreenOctetCount": pmEthTmCurrent24hEgressGreenOctetCount,
       "pmEthTmCurrent24hGreenFrameDiscards": pmEthTmCurrent24hGreenFrameDiscards,
       "pmEthTmCurrent24hYellowFrameDiscards": pmEthTmCurrent24hYellowFrameDiscards,
       "pmEthTmCurrent24hGreenOctetDiscards": pmEthTmCurrent24hGreenOctetDiscards,
       "pmEthTmCurrent24hYellowOctetDiscards": pmEthTmCurrent24hYellowOctetDiscards,
       "pmEthTmObjectProperty": pmEthTmObjectProperty,
       "pmEthTmInternalReference": pmEthTmInternalReference,
       "pmEthTmIdentifier": pmEthTmIdentifier,
       "pmEthOamList": pmEthOamList,
       "pmEthOamTable": pmEthOamTable,
       "pmEthOamEntry": pmEthOamEntry,
       "pmEthOamIndex": pmEthOamIndex,
       "pmEthOamName": pmEthOamName,
       "pmEthOamSubrack": pmEthOamSubrack,
       "pmEthOamSlot": pmEthOamSlot,
       "pmEthOamPort": pmEthOamPort,
       "pmEthOamPmReportMode": pmEthOamPmReportMode,
       "pmEthOamRxPort": pmEthOamRxPort,
       "pmEthOamReset15Min": pmEthOamReset15Min,
       "pmEthOamReset24H": pmEthOamReset24H,
       "pmEthOamAdminStatus": pmEthOamAdminStatus,
       "pmEthOamOperStatus": pmEthOamOperStatus,
       "pmEthOamIsSuspect15Min": pmEthOamIsSuspect15Min,
       "pmEthOamIsSuspect24h": pmEthOamIsSuspect24h,
       "pmEthOamCurrentTwoWayFrameDelay": pmEthOamCurrentTwoWayFrameDelay,
       "pmEthOamCurrentTwoWayFrameDelayVariation": pmEthOamCurrentTwoWayFrameDelayVariation,
       "pmEthOamCurrentFrameLossRatioNearEnd": pmEthOamCurrentFrameLossRatioNearEnd,
       "pmEthOamCurrentFrameLossRatioFarEnd": pmEthOamCurrentFrameLossRatioFarEnd,
       "pmEthOamCurrentUnavailabilityNearEnd": pmEthOamCurrentUnavailabilityNearEnd,
       "pmEthOamCurrentUnavailabilityFarEnd": pmEthOamCurrentUnavailabilityFarEnd,
       "pmEthOamCurrent24hTwoWayFrameDelay": pmEthOamCurrent24hTwoWayFrameDelay,
       "pmEthOamCurrent24hTwoWayFrameDelayVariation": pmEthOamCurrent24hTwoWayFrameDelayVariation,
       "pmEthOamCurrent24hFrameLossRatioNearEnd": pmEthOamCurrent24hFrameLossRatioNearEnd,
       "pmEthOamCurrent24hFrameLossRatioFarEnd": pmEthOamCurrent24hFrameLossRatioFarEnd,
       "pmEthOamCurrent24hUnavailabilityNearEnd": pmEthOamCurrent24hUnavailabilityNearEnd,
       "pmEthOamCurrent24hUnavailabilityFarEnd": pmEthOamCurrent24hUnavailabilityFarEnd,
       "pmEthOamObjectProperty": pmEthOamObjectProperty,
       "pmEthOamInternalReference": pmEthOamInternalReference,
       "pmEthOamIdentifier": pmEthOamIdentifier,
       "pmEthOamUsedPercentOfFrames": pmEthOamUsedPercentOfFrames,
       "pmEthOamFrameLossRatioUnavailableThreshold": pmEthOamFrameLossRatioUnavailableThreshold,
       "pmEthOamCurrentOneWayFrameDelayVariation": pmEthOamCurrentOneWayFrameDelayVariation,
       "pmEthOamCurrent24hOneWayFrameDelayVariation": pmEthOamCurrent24hOneWayFrameDelayVariation,
       "pmEthDropList": pmEthDropList,
       "pmEthDropTable": pmEthDropTable,
       "pmEthDropEntry": pmEthDropEntry,
       "pmEthDropIndex": pmEthDropIndex,
       "pmEthDropName": pmEthDropName,
       "pmEthDropSubrack": pmEthDropSubrack,
       "pmEthDropSlot": pmEthDropSlot,
       "pmEthDropPort": pmEthDropPort,
       "pmEthDropRxPort": pmEthDropRxPort,
       "pmEthDropResetCont": pmEthDropResetCont,
       "pmEthDropFrames": pmEthDropFrames,
       "pmEthDropBytes": pmEthDropBytes,
       "pmEthDropYellowFrames": pmEthDropYellowFrames,
       "pmEthDropRedFrames": pmEthDropRedFrames,
       "pmEthDropFramesQ1": pmEthDropFramesQ1,
       "pmEthDropBytesQ1": pmEthDropBytesQ1,
       "pmEthDropFramesQ2": pmEthDropFramesQ2,
       "pmEthDropBytesQ2": pmEthDropBytesQ2,
       "pmEthDropFramesQ3": pmEthDropFramesQ3,
       "pmEthDropBytesQ3": pmEthDropBytesQ3,
       "pmEthDropFramesQ4": pmEthDropFramesQ4,
       "pmEthDropBytesQ4": pmEthDropBytesQ4,
       "pmEthDropFramesQ5": pmEthDropFramesQ5,
       "pmEthDropBytesQ5": pmEthDropBytesQ5,
       "pmEthDropFramesQ6": pmEthDropFramesQ6,
       "pmEthDropBytesQ6": pmEthDropBytesQ6,
       "pmEthDropFramesQ7": pmEthDropFramesQ7,
       "pmEthDropBytesQ7": pmEthDropBytesQ7,
       "pmEthDropFramesQ8": pmEthDropFramesQ8,
       "pmEthDropBytesQ8": pmEthDropBytesQ8,
       "pmEthDropIfNo": pmEthDropIfNo,
       "pmEthDropUpPortId": pmEthDropUpPortId,
       "pmEthDropFrames15m": pmEthDropFrames15m,
       "pmEthDropBytes15m": pmEthDropBytes15m,
       "pmEthDropYellowFrames15m": pmEthDropYellowFrames15m,
       "pmEthDropRedFrames15m": pmEthDropRedFrames15m,
       "pmEthDropFrames24h": pmEthDropFrames24h,
       "pmEthDropBytes24h": pmEthDropBytes24h,
       "pmEthDropYellowFrames24h": pmEthDropYellowFrames24h,
       "pmEthDropRedFrames24h": pmEthDropRedFrames24h,
       "pmEthDropFrames15mQ1": pmEthDropFrames15mQ1,
       "pmEthDropBytes15mQ1": pmEthDropBytes15mQ1,
       "pmEthDropFrames24hQ1": pmEthDropFrames24hQ1,
       "pmEthDropBytes24hQ1": pmEthDropBytes24hQ1,
       "pmEthDropFrames15mQ2": pmEthDropFrames15mQ2,
       "pmEthDropBytes15mQ2": pmEthDropBytes15mQ2,
       "pmEthDropFrames24hQ2": pmEthDropFrames24hQ2,
       "pmEthDropBytes24hQ2": pmEthDropBytes24hQ2,
       "pmEthDropFrames15mQ3": pmEthDropFrames15mQ3,
       "pmEthDropBytes15mQ3": pmEthDropBytes15mQ3,
       "pmEthDropFrames24hQ3": pmEthDropFrames24hQ3,
       "pmEthDropBytes24hQ3": pmEthDropBytes24hQ3,
       "pmEthDropFrames15mQ4": pmEthDropFrames15mQ4,
       "pmEthDropBytes15mQ4": pmEthDropBytes15mQ4,
       "pmEthDropFrames24hQ4": pmEthDropFrames24hQ4,
       "pmEthDropBytes24hQ4": pmEthDropBytes24hQ4,
       "pmEthDropFrames15mQ5": pmEthDropFrames15mQ5,
       "pmEthDropBytes15mQ5": pmEthDropBytes15mQ5,
       "pmEthDropFrames24hQ5": pmEthDropFrames24hQ5,
       "pmEthDropBytes24hQ5": pmEthDropBytes24hQ5,
       "pmEthDropFrames15mQ6": pmEthDropFrames15mQ6,
       "pmEthDropBytes15mQ6": pmEthDropBytes15mQ6,
       "pmEthDropFrames24hQ6": pmEthDropFrames24hQ6,
       "pmEthDropBytes24hQ6": pmEthDropBytes24hQ6,
       "pmEthDropFrames15mQ7": pmEthDropFrames15mQ7,
       "pmEthDropBytes15mQ7": pmEthDropBytes15mQ7,
       "pmEthDropFrames24hQ7": pmEthDropFrames24hQ7,
       "pmEthDropBytes24hQ7": pmEthDropBytes24hQ7,
       "pmEthDropFrames15mQ8": pmEthDropFrames15mQ8,
       "pmEthDropBytes15mQ8": pmEthDropBytes15mQ8,
       "pmEthDropFrames24hQ8": pmEthDropFrames24hQ8,
       "pmEthDropBytes24hQ8": pmEthDropBytes24hQ8,
       "pmEthDropReset15m": pmEthDropReset15m,
       "pmEthDropReset24h": pmEthDropReset24h,
       "pmEthDropReportMode": pmEthDropReportMode,
       "pmEthDropIsSuspect15Min": pmEthDropIsSuspect15Min,
       "pmEthDropIsSuspect24H": pmEthDropIsSuspect24H,
       "pmEthClassificationList": pmEthClassificationList,
       "pmEthClassificationTable": pmEthClassificationTable,
       "pmEthClassificationEntry": pmEthClassificationEntry,
       "pmEthClassificationIndex": pmEthClassificationIndex,
       "pmEthClassificationName": pmEthClassificationName,
       "pmEthClassificationSubrack": pmEthClassificationSubrack,
       "pmEthClassificationSlot": pmEthClassificationSlot,
       "pmEthClassificationIdentifier": pmEthClassificationIdentifier,
       "pmEthClassificationResetCont": pmEthClassificationResetCont,
       "pmEthClassificationInternalReference": pmEthClassificationInternalReference,
       "pmEthClassificationCounter1": pmEthClassificationCounter1,
       "pmEthClassificationCounter2": pmEthClassificationCounter2,
       "pmEthClassificationCounter3": pmEthClassificationCounter3,
       "pmEthClassificationCounter4": pmEthClassificationCounter4,
       "pmMpoLanesList": pmMpoLanesList,
       "pmMpoLanesTable": pmMpoLanesTable,
       "pmMpoLanesEntry": pmMpoLanesEntry,
       "pmMpoLanesIndex": pmMpoLanesIndex,
       "pmMpoLanesName": pmMpoLanesName,
       "pmMpoLanesSubrack": pmMpoLanesSubrack,
       "pmMpoLanesSlot": pmMpoLanesSlot,
       "pmMpoLanesLaneId": pmMpoLanesLaneId,
       "pmMpoLanesAdminStatus": pmMpoLanesAdminStatus,
       "pmMpoLanesOperStatus": pmMpoLanesOperStatus,
       "pmMpoLanesPmReportMode": pmMpoLanesPmReportMode,
       "pmMpoLanesIsSuspect15Min": pmMpoLanesIsSuspect15Min,
       "pmMpoLanesIsSuspect24H": pmMpoLanesIsSuspect24H,
       "pmMpoLanesRxCurrentES": pmMpoLanesRxCurrentES,
       "pmMpoLanesRxCurrentSES": pmMpoLanesRxCurrentSES,
       "pmMpoLanesRxCurrentBBE": pmMpoLanesRxCurrentBBE,
       "pmMpoLanesRxCurrentUAS": pmMpoLanesRxCurrentUAS,
       "pmMpoLanesTxCurrentES": pmMpoLanesTxCurrentES,
       "pmMpoLanesTxCurrentSES": pmMpoLanesTxCurrentSES,
       "pmMpoLanesTxCurrentBBE": pmMpoLanesTxCurrentBBE,
       "pmMpoLanesTxCurrentUAS": pmMpoLanesTxCurrentUAS,
       "pmMpoLanesRx24hCurrentES": pmMpoLanesRx24hCurrentES,
       "pmMpoLanesRx24hCurrentSES": pmMpoLanesRx24hCurrentSES,
       "pmMpoLanesRx24hCurrentBBE": pmMpoLanesRx24hCurrentBBE,
       "pmMpoLanesRx24hCurrentUAS": pmMpoLanesRx24hCurrentUAS,
       "pmMpoLanesTx24hCurrentES": pmMpoLanesTx24hCurrentES,
       "pmMpoLanesTx24hCurrentSES": pmMpoLanesTx24hCurrentSES,
       "pmMpoLanesTx24hCurrentBBE": pmMpoLanesTx24hCurrentBBE,
       "pmMpoLanesTx24hCurrentUAS": pmMpoLanesTx24hCurrentUAS,
       "pmMpoLanesRxESThreshold": pmMpoLanesRxESThreshold,
       "pmMpoLanesRxSESThreshold": pmMpoLanesRxSESThreshold,
       "pmMpoLanesRxBBEThreshold": pmMpoLanesRxBBEThreshold,
       "pmMpoLanesRxUASThreshold": pmMpoLanesRxUASThreshold,
       "pmMpoLanesTxESThreshold": pmMpoLanesTxESThreshold,
       "pmMpoLanesTxSESThreshold": pmMpoLanesTxSESThreshold,
       "pmMpoLanesTxBBEThreshold": pmMpoLanesTxBBEThreshold,
       "pmMpoLanesTxUASThreshold": pmMpoLanesTxUASThreshold,
       "pmMpoLanesRx24hESThreshold": pmMpoLanesRx24hESThreshold,
       "pmMpoLanesRx24hSESThreshold": pmMpoLanesRx24hSESThreshold,
       "pmMpoLanesRx24hBBEThreshold": pmMpoLanesRx24hBBEThreshold,
       "pmMpoLanesRx24hUASThreshold": pmMpoLanesRx24hUASThreshold,
       "pmMpoLanesTx24hESThreshold": pmMpoLanesTx24hESThreshold,
       "pmMpoLanesTx24hSESThreshold": pmMpoLanesTx24hSESThreshold,
       "pmMpoLanesTx24hBBEThreshold": pmMpoLanesTx24hBBEThreshold,
       "pmMpoLanesTx24hUASThreshold": pmMpoLanesTx24hUASThreshold,
       "pmMpoLanesRxES": pmMpoLanesRxES,
       "pmMpoLanesRxSES": pmMpoLanesRxSES,
       "pmMpoLanesRxBBE": pmMpoLanesRxBBE,
       "pmMpoLanesRxUAS": pmMpoLanesRxUAS,
       "pmMpoLanesTxES": pmMpoLanesTxES,
       "pmMpoLanesTxSES": pmMpoLanesTxSES,
       "pmMpoLanesTxBBE": pmMpoLanesTxBBE,
       "pmMpoLanesTxUAS": pmMpoLanesTxUAS,
       "pmMpoLanesRx24hES": pmMpoLanesRx24hES,
       "pmMpoLanesRx24hSES": pmMpoLanesRx24hSES,
       "pmMpoLanesRx24hBBE": pmMpoLanesRx24hBBE,
       "pmMpoLanesRx24hUAS": pmMpoLanesRx24hUAS,
       "pmMpoLanesTx24hES": pmMpoLanesTx24hES,
       "pmMpoLanesTx24hSES": pmMpoLanesTx24hSES,
       "pmMpoLanesTx24hBBE": pmMpoLanesTx24hBBE,
       "pmMpoLanesTx24hUAS": pmMpoLanesTx24hUAS,
       "pmMpoLanesReset15Min": pmMpoLanesReset15Min,
       "pmMpoLanesReset24H": pmMpoLanesReset24H,
       "pmMpoLanesRxPowerLevel": pmMpoLanesRxPowerLevel,
       "pmMpoLanesTxPowerLevel": pmMpoLanesTxPowerLevel,
       "pmMpoLanesObjectProperty": pmMpoLanesObjectProperty,
       "pmMpoLanesIfNo": pmMpoLanesIfNo,
       "pmMpoLanesUpPortId": pmMpoLanesUpPortId,
       "pmEthEgressList": pmEthEgressList,
       "pmEthEgressTable": pmEthEgressTable,
       "pmEthEgressEntry": pmEthEgressEntry,
       "pmEthEgressIndex": pmEthEgressIndex,
       "pmEthEgressName": pmEthEgressName,
       "pmEthEgressSubrack": pmEthEgressSubrack,
       "pmEthEgressSlot": pmEthEgressSlot,
       "pmEthEgressIfNo": pmEthEgressIfNo,
       "pmEthEgressPort": pmEthEgressPort,
       "pmEthEgressRxPort": pmEthEgressRxPort,
       "pmEthEgressUpPortId": pmEthEgressUpPortId,
       "pmEthEgressResetCont": pmEthEgressResetCont,
       "pmEthEgressReset15m": pmEthEgressReset15m,
       "pmEthEgressReset24h": pmEthEgressReset24h,
       "pmEthEgressFramesQ1": pmEthEgressFramesQ1,
       "pmEthEgressBytesQ1": pmEthEgressBytesQ1,
       "pmEthEgressBandwidthQ1": pmEthEgressBandwidthQ1,
       "pmEthEgressFrames15mQ1": pmEthEgressFrames15mQ1,
       "pmEthEgressBytes15mQ1": pmEthEgressBytes15mQ1,
       "pmEthEgressFrames24hQ1": pmEthEgressFrames24hQ1,
       "pmEthEgressBytes24hQ1": pmEthEgressBytes24hQ1,
       "pmEthEgressFramesQ2": pmEthEgressFramesQ2,
       "pmEthEgressBytesQ2": pmEthEgressBytesQ2,
       "pmEthEgressBandwidthQ2": pmEthEgressBandwidthQ2,
       "pmEthEgressFrames15mQ2": pmEthEgressFrames15mQ2,
       "pmEthEgressBytes15mQ2": pmEthEgressBytes15mQ2,
       "pmEthEgressFrames24hQ2": pmEthEgressFrames24hQ2,
       "pmEthEgressBytes24hQ2": pmEthEgressBytes24hQ2,
       "pmEthEgressFramesQ3": pmEthEgressFramesQ3,
       "pmEthEgressBytesQ3": pmEthEgressBytesQ3,
       "pmEthEgressBandwidthQ3": pmEthEgressBandwidthQ3,
       "pmEthEgressFrames15mQ3": pmEthEgressFrames15mQ3,
       "pmEthEgressBytes15mQ3": pmEthEgressBytes15mQ3,
       "pmEthEgressFrames24hQ3": pmEthEgressFrames24hQ3,
       "pmEthEgressBytes24hQ3": pmEthEgressBytes24hQ3,
       "pmEthEgressFramesQ4": pmEthEgressFramesQ4,
       "pmEthEgressBytesQ4": pmEthEgressBytesQ4,
       "pmEthEgressBandwidthQ4": pmEthEgressBandwidthQ4,
       "pmEthEgressFrames15mQ4": pmEthEgressFrames15mQ4,
       "pmEthEgressBytes15mQ4": pmEthEgressBytes15mQ4,
       "pmEthEgressFrames24hQ4": pmEthEgressFrames24hQ4,
       "pmEthEgressBytes24hQ4": pmEthEgressBytes24hQ4,
       "pmEthEgressFramesQ5": pmEthEgressFramesQ5,
       "pmEthEgressBytesQ5": pmEthEgressBytesQ5,
       "pmEthEgressBandwidthQ5": pmEthEgressBandwidthQ5,
       "pmEthEgressFrames15mQ5": pmEthEgressFrames15mQ5,
       "pmEthEgressBytes15mQ5": pmEthEgressBytes15mQ5,
       "pmEthEgressFrames24hQ5": pmEthEgressFrames24hQ5,
       "pmEthEgressBytes24hQ5": pmEthEgressBytes24hQ5,
       "pmEthEgressFramesQ6": pmEthEgressFramesQ6,
       "pmEthEgressBytesQ6": pmEthEgressBytesQ6,
       "pmEthEgressBandwidthQ6": pmEthEgressBandwidthQ6,
       "pmEthEgressFrames15mQ6": pmEthEgressFrames15mQ6,
       "pmEthEgressBytes15mQ6": pmEthEgressBytes15mQ6,
       "pmEthEgressFrames24hQ6": pmEthEgressFrames24hQ6,
       "pmEthEgressBytes24hQ6": pmEthEgressBytes24hQ6,
       "pmEthEgressFramesQ7": pmEthEgressFramesQ7,
       "pmEthEgressBytesQ7": pmEthEgressBytesQ7,
       "pmEthEgressBandwidthQ7": pmEthEgressBandwidthQ7,
       "pmEthEgressFrames15mQ7": pmEthEgressFrames15mQ7,
       "pmEthEgressBytes15mQ7": pmEthEgressBytes15mQ7,
       "pmEthEgressFrames24hQ7": pmEthEgressFrames24hQ7,
       "pmEthEgressBytes24hQ7": pmEthEgressBytes24hQ7,
       "pmEthEgressFramesQ8": pmEthEgressFramesQ8,
       "pmEthEgressBytesQ8": pmEthEgressBytesQ8,
       "pmEthEgressBandwidthQ8": pmEthEgressBandwidthQ8,
       "pmEthEgressFrames15mQ8": pmEthEgressFrames15mQ8,
       "pmEthEgressBytes15mQ8": pmEthEgressBytes15mQ8,
       "pmEthEgressFrames24hQ8": pmEthEgressFrames24hQ8,
       "pmEthEgressBytes24hQ8": pmEthEgressBytes24hQ8,
       "pmEthEgressReportMode": pmEthEgressReportMode,
       "pmEthEgressIsSuspect15Min": pmEthEgressIsSuspect15Min,
       "pmEthEgressIsSuspect24H": pmEthEgressIsSuspect24H}
)
