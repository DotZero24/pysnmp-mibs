# SNMP MIB module (ADTRAN-GEN-ETH-IFC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-ETH-IFC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:44 2025
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

(adGenEthIfc,
 adGenEthIfcID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenEthIfc",
    "adGenEthIfcID")

(GenSystemInterfaceType,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "GenSystemInterfaceType")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(Unsigned64TC,) = mibBuilder.importSymbols(
    "APPLICATION-MIB",
    "Unsigned64TC")

(InterfaceIndex,
 ifDescr,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

adGenEthMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 15, 1)
)
if mibBuilder.loadTexts:
    adGenEthMIB.setRevisions(
        ("2020-07-21 00:00",
         "2020-03-26 00:00",
         "2019-09-03 00:00",
         "2019-04-23 00:00",
         "2016-05-26 00:00",
         "2016-03-07 00:00",
         "2013-10-25 00:00",
         "2013-06-14 00:00",
         "2013-03-22 00:00",
         "2013-02-08 00:00",
         "2012-09-11 00:00",
         "2012-03-14 00:00",
         "2012-02-21 00:00",
         "2012-02-13 00:00",
         "2012-02-02 00:00",
         "2012-01-11 00:00",
         "2011-11-28 16:40",
         "2011-10-10 13:46",
         "2011-09-15 00:00",
         "2011-04-27 19:59",
         "2010-04-23 00:00",
         "2009-02-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEthIfcEvents_ObjectIdentity = ObjectIdentity
adGenEthIfcEvents = _AdGenEthIfcEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0)
)
_AdGenEthIfcProvisioning_ObjectIdentity = ObjectIdentity
adGenEthIfcProvisioning = _AdGenEthIfcProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1)
)
_AdGenEthProvTable_Object = MibTable
adGenEthProvTable = _AdGenEthProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEthProvTable.setStatus("current")
_AdGenEthProvEntry_Object = MibTableRow
adGenEthProvEntry = _AdGenEthProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1)
)
adGenEthProvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthProvEntry.setStatus("current")


class _AdGenEthPortSpeed_Type(Integer32):
    """Custom type adGenEthPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("auto", 1),
          ("speed10Mbps", 2),
          ("speed100Mbps", 3),
          ("speed1000Mbps", 4),
          ("speed2500Mbps", 5),
          ("speed10Gbps", 6),
          ("speedScan", 7),
          ("speed40Gbps", 8),
          ("speed100Gbps", 9))
    )


_AdGenEthPortSpeed_Type.__name__ = "Integer32"
_AdGenEthPortSpeed_Object = MibTableColumn
adGenEthPortSpeed = _AdGenEthPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 1),
    _AdGenEthPortSpeed_Type()
)
adGenEthPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthPortSpeed.setStatus("deprecated")


class _AdGenEthPortDuplex_Type(Integer32):
    """Custom type adGenEthPortDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_AdGenEthPortDuplex_Type.__name__ = "Integer32"
_AdGenEthPortDuplex_Object = MibTableColumn
adGenEthPortDuplex = _AdGenEthPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 2),
    _AdGenEthPortDuplex_Type()
)
adGenEthPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthPortDuplex.setStatus("deprecated")


class _AdGenEthLinkUpDownTrapEnable_Type(Integer32):
    """Custom type adGenEthLinkUpDownTrapEnable based on Integer32"""
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


_AdGenEthLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_AdGenEthLinkUpDownTrapEnable_Object = MibTableColumn
adGenEthLinkUpDownTrapEnable = _AdGenEthLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 3),
    _AdGenEthLinkUpDownTrapEnable_Type()
)
adGenEthLinkUpDownTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthLinkUpDownTrapEnable.setStatus("current")


class _AdGenEthPortFixedSpeed_Type(Integer32):
    """Custom type adGenEthPortFixedSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
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
        *(("fixedSpeed10Mbps", 2),
          ("fixedSpeed100Mbps", 3),
          ("fixedSpeed1000Mbps", 4),
          ("fixedSpeed2500Mbps", 5),
          ("fixedSpeed10Gbps", 6),
          ("fixedSpeedScan", 7),
          ("fixedSpeed40Gbps", 8),
          ("fixedSpeed100Gbps", 9))
    )


_AdGenEthPortFixedSpeed_Type.__name__ = "Integer32"
_AdGenEthPortFixedSpeed_Object = MibTableColumn
adGenEthPortFixedSpeed = _AdGenEthPortFixedSpeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 4),
    _AdGenEthPortFixedSpeed_Type()
)
adGenEthPortFixedSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthPortFixedSpeed.setStatus("current")


class _AdGenEthPortFixedDuplex_Type(Integer32):
    """Custom type adGenEthPortFixedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fixedHalfDuplex", 2),
          ("fixedFullDuplex", 3))
    )


_AdGenEthPortFixedDuplex_Type.__name__ = "Integer32"
_AdGenEthPortFixedDuplex_Object = MibTableColumn
adGenEthPortFixedDuplex = _AdGenEthPortFixedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 5),
    _AdGenEthPortFixedDuplex_Type()
)
adGenEthPortFixedDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthPortFixedDuplex.setStatus("current")
_AdGenEthAutoNegotiateCu_Type = TruthValue
_AdGenEthAutoNegotiateCu_Object = MibTableColumn
adGenEthAutoNegotiateCu = _AdGenEthAutoNegotiateCu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 6),
    _AdGenEthAutoNegotiateCu_Type()
)
adGenEthAutoNegotiateCu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthAutoNegotiateCu.setStatus("current")


class _AdGenEthAdvertisedSpeedAndDuplexCu_Type(Bits):
    """Custom type adGenEthAdvertisedSpeedAndDuplexCu based on Bits"""
    namedValues = NamedValues(
        *(("cuSpeed1000FullDuplex", 0),
          ("cuSpeed100FullDuplex", 1),
          ("cuSpeed100HalfDuplex", 2),
          ("cuSpeed10FullDuplex", 3),
          ("cuSpeed10HalfDuplex", 4))
    )

_AdGenEthAdvertisedSpeedAndDuplexCu_Type.__name__ = "Bits"
_AdGenEthAdvertisedSpeedAndDuplexCu_Object = MibTableColumn
adGenEthAdvertisedSpeedAndDuplexCu = _AdGenEthAdvertisedSpeedAndDuplexCu_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 8),
    _AdGenEthAdvertisedSpeedAndDuplexCu_Type()
)
adGenEthAdvertisedSpeedAndDuplexCu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthAdvertisedSpeedAndDuplexCu.setStatus("current")
_AdGenEthAutoNegotiateFiber_Type = TruthValue
_AdGenEthAutoNegotiateFiber_Object = MibTableColumn
adGenEthAutoNegotiateFiber = _AdGenEthAutoNegotiateFiber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 9),
    _AdGenEthAutoNegotiateFiber_Type()
)
adGenEthAutoNegotiateFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthAutoNegotiateFiber.setStatus("current")


class _AdGenEthAdvertisedDuplexFiber_Type(Bits):
    """Custom type adGenEthAdvertisedDuplexFiber based on Bits"""
    namedValues = NamedValues(
        *(("fiberFullDuplex", 0),
          ("fiberHalfDuplex", 1))
    )

_AdGenEthAdvertisedDuplexFiber_Type.__name__ = "Bits"
_AdGenEthAdvertisedDuplexFiber_Object = MibTableColumn
adGenEthAdvertisedDuplexFiber = _AdGenEthAdvertisedDuplexFiber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 11),
    _AdGenEthAdvertisedDuplexFiber_Type()
)
adGenEthAdvertisedDuplexFiber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthAdvertisedDuplexFiber.setStatus("current")
_AdGenEthPortYCableEnable_Type = TruthValue
_AdGenEthPortYCableEnable_Object = MibTableColumn
adGenEthPortYCableEnable = _AdGenEthPortYCableEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 12),
    _AdGenEthPortYCableEnable_Type()
)
adGenEthPortYCableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthPortYCableEnable.setStatus("current")


class _AdGenEthSpeedScanAlarmEnable_Type(TruthValue):
    """Custom type adGenEthSpeedScanAlarmEnable based on TruthValue"""
    defaultValue = 1


_AdGenEthSpeedScanAlarmEnable_Type.__name__ = "TruthValue"
_AdGenEthSpeedScanAlarmEnable_Object = MibTableColumn
adGenEthSpeedScanAlarmEnable = _AdGenEthSpeedScanAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 13),
    _AdGenEthSpeedScanAlarmEnable_Type()
)
adGenEthSpeedScanAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthSpeedScanAlarmEnable.setStatus("current")


class _AdGenEthSpeedScanAlarmSeverityLevel_Type(Integer32):
    """Custom type adGenEthSpeedScanAlarmSeverityLevel based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenEthSpeedScanAlarmSeverityLevel_Type.__name__ = "Integer32"
_AdGenEthSpeedScanAlarmSeverityLevel_Object = MibTableColumn
adGenEthSpeedScanAlarmSeverityLevel = _AdGenEthSpeedScanAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 14),
    _AdGenEthSpeedScanAlarmSeverityLevel_Type()
)
adGenEthSpeedScanAlarmSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthSpeedScanAlarmSeverityLevel.setStatus("current")


class _AdGenEthPortBreakoutMode_Type(Integer32):
    """Custom type adGenEthPortBreakoutMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("fourBy10Gig", 2))
    )


_AdGenEthPortBreakoutMode_Type.__name__ = "Integer32"
_AdGenEthPortBreakoutMode_Object = MibTableColumn
adGenEthPortBreakoutMode = _AdGenEthPortBreakoutMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 15),
    _AdGenEthPortBreakoutMode_Type()
)
adGenEthPortBreakoutMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthPortBreakoutMode.setStatus("current")


class _AdGenEthPortBreakoutModesSupported_Type(Bits):
    """Custom type adGenEthPortBreakoutModesSupported based on Bits"""
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("oneBy40Gig", 1),
          ("fourBy10Gig", 2))
    )

_AdGenEthPortBreakoutModesSupported_Type.__name__ = "Bits"
_AdGenEthPortBreakoutModesSupported_Object = MibTableColumn
adGenEthPortBreakoutModesSupported = _AdGenEthPortBreakoutModesSupported_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 16),
    _AdGenEthPortBreakoutModesSupported_Type()
)
adGenEthPortBreakoutModesSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthPortBreakoutModesSupported.setStatus("current")
_AdGenEthForwardErrorCorrection_Type = TruthValue
_AdGenEthForwardErrorCorrection_Object = MibTableColumn
adGenEthForwardErrorCorrection = _AdGenEthForwardErrorCorrection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 17),
    _AdGenEthForwardErrorCorrection_Type()
)
adGenEthForwardErrorCorrection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthForwardErrorCorrection.setStatus("current")


class _AdGenEthPortBreakoutModeStatus_Type(Integer32):
    """Custom type adGenEthPortBreakoutModeStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-6,
              -5,
              -4,
              -3,
              -2,
              -1,
              0)
        )
    )
    namedValues = NamedValues(
        *(("notDone", -6),
          ("internalError", -5),
          ("invalidPort", -4),
          ("portNotDisabled", -3),
          ("modeNotSupported", -2),
          ("breakoutNotSupported", -1),
          ("success", 0))
    )


_AdGenEthPortBreakoutModeStatus_Type.__name__ = "Integer32"
_AdGenEthPortBreakoutModeStatus_Object = MibTableColumn
adGenEthPortBreakoutModeStatus = _AdGenEthPortBreakoutModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 1, 1, 18),
    _AdGenEthPortBreakoutModeStatus_Type()
)
adGenEthPortBreakoutModeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthPortBreakoutModeStatus.setStatus("current")
_AdGenEthProvEVCAdvertisementTable_Object = MibTable
adGenEthProvEVCAdvertisementTable = _AdGenEthProvEVCAdvertisementTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 2)
)
if mibBuilder.loadTexts:
    adGenEthProvEVCAdvertisementTable.setStatus("current")
_AdGenEthProvEVCAdvertisementEntry_Object = MibTableRow
adGenEthProvEVCAdvertisementEntry = _AdGenEthProvEVCAdvertisementEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 2, 1)
)
adGenEthProvEVCAdvertisementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthProvEVCAdvertisementEntry.setStatus("current")


class _AdGenEthProvEVCAdvertisementState_Type(Integer32):
    """Custom type adGenEthProvEVCAdvertisementState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenEthProvEVCAdvertisementState_Type.__name__ = "Integer32"
_AdGenEthProvEVCAdvertisementState_Object = MibTableColumn
adGenEthProvEVCAdvertisementState = _AdGenEthProvEVCAdvertisementState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 2, 1, 1),
    _AdGenEthProvEVCAdvertisementState_Type()
)
adGenEthProvEVCAdvertisementState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthProvEVCAdvertisementState.setStatus("current")
_AdGenEthAlarmSlotProvTable_Object = MibTable
adGenEthAlarmSlotProvTable = _AdGenEthAlarmSlotProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 3)
)
if mibBuilder.loadTexts:
    adGenEthAlarmSlotProvTable.setStatus("current")
_AdGenEthAlarmSlotProvEntry_Object = MibTableRow
adGenEthAlarmSlotProvEntry = _AdGenEthAlarmSlotProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 3, 1)
)
adGenEthAlarmSlotProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthAlarmSlotProvEntry.setStatus("current")


class _AdGenEthAlarmSlotIfcLinkDownSeverityLevel_Type(Integer32):
    """Custom type adGenEthAlarmSlotIfcLinkDownSeverityLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenEthAlarmSlotIfcLinkDownSeverityLevel_Type.__name__ = "Integer32"
_AdGenEthAlarmSlotIfcLinkDownSeverityLevel_Object = MibTableColumn
adGenEthAlarmSlotIfcLinkDownSeverityLevel = _AdGenEthAlarmSlotIfcLinkDownSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 3, 1, 1),
    _AdGenEthAlarmSlotIfcLinkDownSeverityLevel_Type()
)
adGenEthAlarmSlotIfcLinkDownSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthAlarmSlotIfcLinkDownSeverityLevel.setStatus("current")


class _AdGenEthAlarmSlotLinkDownSeverityLevel_Type(Integer32):
    """Custom type adGenEthAlarmSlotLinkDownSeverityLevel based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenEthAlarmSlotLinkDownSeverityLevel_Type.__name__ = "Integer32"
_AdGenEthAlarmSlotLinkDownSeverityLevel_Object = MibTableColumn
adGenEthAlarmSlotLinkDownSeverityLevel = _AdGenEthAlarmSlotLinkDownSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 1, 3, 1, 2),
    _AdGenEthAlarmSlotLinkDownSeverityLevel_Type()
)
adGenEthAlarmSlotLinkDownSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthAlarmSlotLinkDownSeverityLevel.setStatus("current")
_AdGenEthIfcStatus_ObjectIdentity = ObjectIdentity
adGenEthIfcStatus = _AdGenEthIfcStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2)
)
_AdGenEthStatusTable_Object = MibTable
adGenEthStatusTable = _AdGenEthStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1)
)
if mibBuilder.loadTexts:
    adGenEthStatusTable.setStatus("current")
_AdGenEthStatusEntry_Object = MibTableRow
adGenEthStatusEntry = _AdGenEthStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1)
)
adGenEthStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthStatusEntry.setStatus("current")


class _AdGenEthCurrentSpeed_Type(Integer32):
    """Custom type adGenEthCurrentSpeed based on Integer32"""
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
        *(("unknown", 1),
          ("speed10Mbps", 2),
          ("speed100Mbps", 3),
          ("speed1000Mbps", 4),
          ("speed2500Mbps", 5),
          ("speed10Gbps", 6))
    )


_AdGenEthCurrentSpeed_Type.__name__ = "Integer32"
_AdGenEthCurrentSpeed_Object = MibTableColumn
adGenEthCurrentSpeed = _AdGenEthCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 1),
    _AdGenEthCurrentSpeed_Type()
)
adGenEthCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCurrentSpeed.setStatus("current")


class _AdGenEthCurrentDuplex_Type(Integer32):
    """Custom type adGenEthCurrentDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halfDuplex", 2),
          ("fullDuplex", 3))
    )


_AdGenEthCurrentDuplex_Type.__name__ = "Integer32"
_AdGenEthCurrentDuplex_Object = MibTableColumn
adGenEthCurrentDuplex = _AdGenEthCurrentDuplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 2),
    _AdGenEthCurrentDuplex_Type()
)
adGenEthCurrentDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCurrentDuplex.setStatus("current")


class _AdGenEthCurrentAutoNeg_Type(Integer32):
    """Custom type adGenEthCurrentAutoNeg based on Integer32"""
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


_AdGenEthCurrentAutoNeg_Type.__name__ = "Integer32"
_AdGenEthCurrentAutoNeg_Object = MibTableColumn
adGenEthCurrentAutoNeg = _AdGenEthCurrentAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 3),
    _AdGenEthCurrentAutoNeg_Type()
)
adGenEthCurrentAutoNeg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCurrentAutoNeg.setStatus("current")


class _AdGenEthCurrentAutoNegStatus_Type(Integer32):
    """Custom type adGenEthCurrentAutoNegStatus based on Integer32"""
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
          ("incomplete", 2),
          ("complete", 3))
    )


_AdGenEthCurrentAutoNegStatus_Type.__name__ = "Integer32"
_AdGenEthCurrentAutoNegStatus_Object = MibTableColumn
adGenEthCurrentAutoNegStatus = _AdGenEthCurrentAutoNegStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 4),
    _AdGenEthCurrentAutoNegStatus_Type()
)
adGenEthCurrentAutoNegStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCurrentAutoNegStatus.setStatus("current")
_AdGenEthCurrentInterfaceType_Type = GenSystemInterfaceType
_AdGenEthCurrentInterfaceType_Object = MibTableColumn
adGenEthCurrentInterfaceType = _AdGenEthCurrentInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 5),
    _AdGenEthCurrentInterfaceType_Type()
)
adGenEthCurrentInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCurrentInterfaceType.setStatus("current")


class _AdGenEthInterfaceCuOrFiber_Type(Integer32):
    """Custom type adGenEthInterfaceCuOrFiber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_AdGenEthInterfaceCuOrFiber_Type.__name__ = "Integer32"
_AdGenEthInterfaceCuOrFiber_Object = MibTableColumn
adGenEthInterfaceCuOrFiber = _AdGenEthInterfaceCuOrFiber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 6),
    _AdGenEthInterfaceCuOrFiber_Type()
)
adGenEthInterfaceCuOrFiber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInterfaceCuOrFiber.setStatus("current")


class _AdGenEthInterfaceFixedOrPluggable_Type(Integer32):
    """Custom type adGenEthInterfaceFixedOrPluggable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixedPort", 1),
          ("pluggablePort", 2))
    )


_AdGenEthInterfaceFixedOrPluggable_Type.__name__ = "Integer32"
_AdGenEthInterfaceFixedOrPluggable_Object = MibTableColumn
adGenEthInterfaceFixedOrPluggable = _AdGenEthInterfaceFixedOrPluggable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 7),
    _AdGenEthInterfaceFixedOrPluggable_Type()
)
adGenEthInterfaceFixedOrPluggable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInterfaceFixedOrPluggable.setStatus("current")


class _AdGenEthValid15MinIntervals_Type(Integer32):
    """Custom type adGenEthValid15MinIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_AdGenEthValid15MinIntervals_Type.__name__ = "Integer32"
_AdGenEthValid15MinIntervals_Object = MibTableColumn
adGenEthValid15MinIntervals = _AdGenEthValid15MinIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 8),
    _AdGenEthValid15MinIntervals_Type()
)
adGenEthValid15MinIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthValid15MinIntervals.setStatus("current")


class _AdGenEthValid24HrIntervals_Type(Integer32):
    """Custom type adGenEthValid24HrIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenEthValid24HrIntervals_Type.__name__ = "Integer32"
_AdGenEthValid24HrIntervals_Object = MibTableColumn
adGenEthValid24HrIntervals = _AdGenEthValid24HrIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 9),
    _AdGenEthValid24HrIntervals_Type()
)
adGenEthValid24HrIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthValid24HrIntervals.setStatus("current")


class _AdGenEthAlarmStatus_Type(Bits):
    """Custom type adGenEthAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("noAlarm", 0),
          ("lossOfSignal", 1),
          ("lossOfBlockSync", 2),
          ("highBERT", 3),
          ("localFault", 4),
          ("remoteFault", 5))
    )

_AdGenEthAlarmStatus_Type.__name__ = "Bits"
_AdGenEthAlarmStatus_Object = MibTableColumn
adGenEthAlarmStatus = _AdGenEthAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 10),
    _AdGenEthAlarmStatus_Type()
)
adGenEthAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthAlarmStatus.setStatus("current")
_AdGenEthLastError_Type = DisplayString
_AdGenEthLastError_Object = MibTableColumn
adGenEthLastError = _AdGenEthLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 1, 1, 11),
    _AdGenEthLastError_Type()
)
adGenEthLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthLastError.setStatus("current")
_AdGenEthStatEVCAdvertisementTable_Object = MibTable
adGenEthStatEVCAdvertisementTable = _AdGenEthStatEVCAdvertisementTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 2)
)
if mibBuilder.loadTexts:
    adGenEthStatEVCAdvertisementTable.setStatus("current")
_AdGenEthStatEVCAdvertisementEntry_Object = MibTableRow
adGenEthStatEVCAdvertisementEntry = _AdGenEthStatEVCAdvertisementEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 2, 1)
)
adGenEthStatEVCAdvertisementEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-ETH-IFC-MIB", "adGenEthStatEVCAdvertisementVLANID"),
)
if mibBuilder.loadTexts:
    adGenEthStatEVCAdvertisementEntry.setStatus("current")


class _AdGenEthStatEVCAdvertisementVLANID_Type(Unsigned32):
    """Custom type adGenEthStatEVCAdvertisementVLANID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AdGenEthStatEVCAdvertisementVLANID_Type.__name__ = "Unsigned32"
_AdGenEthStatEVCAdvertisementVLANID_Object = MibTableColumn
adGenEthStatEVCAdvertisementVLANID = _AdGenEthStatEVCAdvertisementVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 2, 1, 1),
    _AdGenEthStatEVCAdvertisementVLANID_Type()
)
adGenEthStatEVCAdvertisementVLANID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthStatEVCAdvertisementVLANID.setStatus("current")


class _AdGenEthStatEVCAdvertisementStatus_Type(Integer32):
    """Custom type adGenEthStatEVCAdvertisementStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("localAdvertisedOnly", 1),
          ("peerAdvertisedOnly", 2),
          ("localAndPeerAdvertised", 3))
    )


_AdGenEthStatEVCAdvertisementStatus_Type.__name__ = "Integer32"
_AdGenEthStatEVCAdvertisementStatus_Object = MibTableColumn
adGenEthStatEVCAdvertisementStatus = _AdGenEthStatEVCAdvertisementStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 2, 2, 1, 2),
    _AdGenEthStatEVCAdvertisementStatus_Type()
)
adGenEthStatEVCAdvertisementStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthStatEVCAdvertisementStatus.setStatus("current")
_AdGenEthIfcPerformance_ObjectIdentity = ObjectIdentity
adGenEthIfcPerformance = _AdGenEthIfcPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3)
)
_AdGenEthPerformanceScalars_ObjectIdentity = ObjectIdentity
adGenEthPerformanceScalars = _AdGenEthPerformanceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 1)
)


class _AdGenEthRstCurrentIntervals_Type(Integer32):
    """Custom type adGenEthRstCurrentIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rstAllCurrentIntervals", 1)
    )


_AdGenEthRstCurrentIntervals_Type.__name__ = "Integer32"
_AdGenEthRstCurrentIntervals_Object = MibScalar
adGenEthRstCurrentIntervals = _AdGenEthRstCurrentIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 1, 1),
    _AdGenEthRstCurrentIntervals_Type()
)
adGenEthRstCurrentIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthRstCurrentIntervals.setStatus("current")


class _AdGenEthRstAll_Type(Integer32):
    """Custom type adGenEthRstAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rstAllIntervals", 1)
    )


_AdGenEthRstAll_Type.__name__ = "Integer32"
_AdGenEthRstAll_Object = MibScalar
adGenEthRstAll = _AdGenEthRstAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 1, 2),
    _AdGenEthRstAll_Type()
)
adGenEthRstAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthRstAll.setStatus("current")
_AdGenEth15MinCurrentTable_Object = MibTable
adGenEth15MinCurrentTable = _AdGenEth15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2)
)
if mibBuilder.loadTexts:
    adGenEth15MinCurrentTable.setStatus("current")
_AdGenEth15MinCurrentEntry_Object = MibTableRow
adGenEth15MinCurrentEntry = _AdGenEth15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1)
)
adGenEth15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEth15MinCurrentEntry.setStatus("current")
_AdGenEth15MinCurrentOutOctets_Type = Gauge32
_AdGenEth15MinCurrentOutOctets_Object = MibTableColumn
adGenEth15MinCurrentOutOctets = _AdGenEth15MinCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 1),
    _AdGenEth15MinCurrentOutOctets_Type()
)
adGenEth15MinCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutOctets.setStatus("current")
_AdGenEth15MinCurrentOutPkts_Type = Gauge32
_AdGenEth15MinCurrentOutPkts_Object = MibTableColumn
adGenEth15MinCurrentOutPkts = _AdGenEth15MinCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 2),
    _AdGenEth15MinCurrentOutPkts_Type()
)
adGenEth15MinCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutPkts.setStatus("current")
_AdGenEth15MinCurrentInOctets_Type = Gauge32
_AdGenEth15MinCurrentInOctets_Object = MibTableColumn
adGenEth15MinCurrentInOctets = _AdGenEth15MinCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 3),
    _AdGenEth15MinCurrentInOctets_Type()
)
adGenEth15MinCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInOctets.setStatus("current")
_AdGenEth15MinCurrentInPkts_Type = Gauge32
_AdGenEth15MinCurrentInPkts_Object = MibTableColumn
adGenEth15MinCurrentInPkts = _AdGenEth15MinCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 4),
    _AdGenEth15MinCurrentInPkts_Type()
)
adGenEth15MinCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInPkts.setStatus("current")
_AdGenEth15MinCurrentInGoodOctets_Type = Gauge32
_AdGenEth15MinCurrentInGoodOctets_Object = MibTableColumn
adGenEth15MinCurrentInGoodOctets = _AdGenEth15MinCurrentInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 5),
    _AdGenEth15MinCurrentInGoodOctets_Type()
)
adGenEth15MinCurrentInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInGoodOctets.setStatus("current")
_AdGenEth15MinCurrentInGoodPkts_Type = Gauge32
_AdGenEth15MinCurrentInGoodPkts_Object = MibTableColumn
adGenEth15MinCurrentInGoodPkts = _AdGenEth15MinCurrentInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 6),
    _AdGenEth15MinCurrentInGoodPkts_Type()
)
adGenEth15MinCurrentInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInGoodPkts.setStatus("current")
_AdGenEth15MinCurrentInErrors_Type = Gauge32
_AdGenEth15MinCurrentInErrors_Object = MibTableColumn
adGenEth15MinCurrentInErrors = _AdGenEth15MinCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 7),
    _AdGenEth15MinCurrentInErrors_Type()
)
adGenEth15MinCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInErrors.setStatus("current")
_AdGenEth15MinCurrentInDiscards_Type = Gauge32
_AdGenEth15MinCurrentInDiscards_Object = MibTableColumn
adGenEth15MinCurrentInDiscards = _AdGenEth15MinCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 8),
    _AdGenEth15MinCurrentInDiscards_Type()
)
adGenEth15MinCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInDiscards.setStatus("current")
_AdGenEth15MinCurrentInGiants_Type = Gauge32
_AdGenEth15MinCurrentInGiants_Object = MibTableColumn
adGenEth15MinCurrentInGiants = _AdGenEth15MinCurrentInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 9),
    _AdGenEth15MinCurrentInGiants_Type()
)
adGenEth15MinCurrentInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInGiants.setStatus("current")
_AdGenEth15MinCurrentInRunts_Type = Gauge32
_AdGenEth15MinCurrentInRunts_Object = MibTableColumn
adGenEth15MinCurrentInRunts = _AdGenEth15MinCurrentInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 10),
    _AdGenEth15MinCurrentInRunts_Type()
)
adGenEth15MinCurrentInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInRunts.setStatus("current")
_AdGenEth15MinCurrentInMulticastPkts_Type = Gauge32
_AdGenEth15MinCurrentInMulticastPkts_Object = MibTableColumn
adGenEth15MinCurrentInMulticastPkts = _AdGenEth15MinCurrentInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 11),
    _AdGenEth15MinCurrentInMulticastPkts_Type()
)
adGenEth15MinCurrentInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInMulticastPkts.setStatus("current")
_AdGenEth15MinCurrentInBroadcastPkts_Type = Gauge32
_AdGenEth15MinCurrentInBroadcastPkts_Object = MibTableColumn
adGenEth15MinCurrentInBroadcastPkts = _AdGenEth15MinCurrentInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 12),
    _AdGenEth15MinCurrentInBroadcastPkts_Type()
)
adGenEth15MinCurrentInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInBroadcastPkts.setStatus("current")
_AdGenEth15MinCurrentInUnicastPkts_Type = Gauge32
_AdGenEth15MinCurrentInUnicastPkts_Object = MibTableColumn
adGenEth15MinCurrentInUnicastPkts = _AdGenEth15MinCurrentInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 13),
    _AdGenEth15MinCurrentInUnicastPkts_Type()
)
adGenEth15MinCurrentInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInUnicastPkts.setStatus("current")
_AdGenEth15MinCurrentOutMulticastPkts_Type = Gauge32
_AdGenEth15MinCurrentOutMulticastPkts_Object = MibTableColumn
adGenEth15MinCurrentOutMulticastPkts = _AdGenEth15MinCurrentOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 14),
    _AdGenEth15MinCurrentOutMulticastPkts_Type()
)
adGenEth15MinCurrentOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutMulticastPkts.setStatus("current")
_AdGenEth15MinCurrentOutBroadcastPkts_Type = Gauge32
_AdGenEth15MinCurrentOutBroadcastPkts_Object = MibTableColumn
adGenEth15MinCurrentOutBroadcastPkts = _AdGenEth15MinCurrentOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 15),
    _AdGenEth15MinCurrentOutBroadcastPkts_Type()
)
adGenEth15MinCurrentOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutBroadcastPkts.setStatus("current")
_AdGenEth15MinCurrentOutUnicastPkts_Type = Gauge32
_AdGenEth15MinCurrentOutUnicastPkts_Object = MibTableColumn
adGenEth15MinCurrentOutUnicastPkts = _AdGenEth15MinCurrentOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 16),
    _AdGenEth15MinCurrentOutUnicastPkts_Type()
)
adGenEth15MinCurrentOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutUnicastPkts.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue0_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue0_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue0 = _AdGenEth15MinCurrentDroppedPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 17),
    _AdGenEth15MinCurrentDroppedPktsQueue0_Type()
)
adGenEth15MinCurrentDroppedPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue0.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue1_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue1_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue1 = _AdGenEth15MinCurrentDroppedPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 18),
    _AdGenEth15MinCurrentDroppedPktsQueue1_Type()
)
adGenEth15MinCurrentDroppedPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue1.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue2_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue2_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue2 = _AdGenEth15MinCurrentDroppedPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 19),
    _AdGenEth15MinCurrentDroppedPktsQueue2_Type()
)
adGenEth15MinCurrentDroppedPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue2.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue3_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue3_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue3 = _AdGenEth15MinCurrentDroppedPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 20),
    _AdGenEth15MinCurrentDroppedPktsQueue3_Type()
)
adGenEth15MinCurrentDroppedPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue3.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue4_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue4_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue4 = _AdGenEth15MinCurrentDroppedPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 21),
    _AdGenEth15MinCurrentDroppedPktsQueue4_Type()
)
adGenEth15MinCurrentDroppedPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue4.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue5_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue5_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue5 = _AdGenEth15MinCurrentDroppedPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 22),
    _AdGenEth15MinCurrentDroppedPktsQueue5_Type()
)
adGenEth15MinCurrentDroppedPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue5.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue6_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue6_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue6 = _AdGenEth15MinCurrentDroppedPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 23),
    _AdGenEth15MinCurrentDroppedPktsQueue6_Type()
)
adGenEth15MinCurrentDroppedPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue6.setStatus("current")
_AdGenEth15MinCurrentDroppedPktsQueue7_Type = Gauge32
_AdGenEth15MinCurrentDroppedPktsQueue7_Object = MibTableColumn
adGenEth15MinCurrentDroppedPktsQueue7 = _AdGenEth15MinCurrentDroppedPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 24),
    _AdGenEth15MinCurrentDroppedPktsQueue7_Type()
)
adGenEth15MinCurrentDroppedPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentDroppedPktsQueue7.setStatus("current")
_AdGenEth15MinCurrentOutDiscards_Type = Gauge32
_AdGenEth15MinCurrentOutDiscards_Object = MibTableColumn
adGenEth15MinCurrentOutDiscards = _AdGenEth15MinCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 25),
    _AdGenEth15MinCurrentOutDiscards_Type()
)
adGenEth15MinCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutDiscards.setStatus("current")
_AdGenEth15MinCurrentInCRCErrors_Type = Gauge32
_AdGenEth15MinCurrentInCRCErrors_Object = MibTableColumn
adGenEth15MinCurrentInCRCErrors = _AdGenEth15MinCurrentInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 26),
    _AdGenEth15MinCurrentInCRCErrors_Type()
)
adGenEth15MinCurrentInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInCRCErrors.setStatus("current")
_AdGenEth15MinCurrentInFrameErrors_Type = Gauge32
_AdGenEth15MinCurrentInFrameErrors_Object = MibTableColumn
adGenEth15MinCurrentInFrameErrors = _AdGenEth15MinCurrentInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 27),
    _AdGenEth15MinCurrentInFrameErrors_Type()
)
adGenEth15MinCurrentInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInFrameErrors.setStatus("current")
_AdGenEth15MinCurrentOutErrors_Type = Gauge32
_AdGenEth15MinCurrentOutErrors_Object = MibTableColumn
adGenEth15MinCurrentOutErrors = _AdGenEth15MinCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 28),
    _AdGenEth15MinCurrentOutErrors_Type()
)
adGenEth15MinCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutErrors.setStatus("current")
_AdGenEth15MinCurrentInPeakUtilization_Type = Gauge32
_AdGenEth15MinCurrentInPeakUtilization_Object = MibTableColumn
adGenEth15MinCurrentInPeakUtilization = _AdGenEth15MinCurrentInPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 29),
    _AdGenEth15MinCurrentInPeakUtilization_Type()
)
adGenEth15MinCurrentInPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInPeakUtilization.setStatus("current")
_AdGenEth15MinCurrentInAvgUtilization_Type = Gauge32
_AdGenEth15MinCurrentInAvgUtilization_Object = MibTableColumn
adGenEth15MinCurrentInAvgUtilization = _AdGenEth15MinCurrentInAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 30),
    _AdGenEth15MinCurrentInAvgUtilization_Type()
)
adGenEth15MinCurrentInAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentInAvgUtilization.setStatus("current")
_AdGenEth15MinCurrentOutPeakUtilization_Type = Gauge32
_AdGenEth15MinCurrentOutPeakUtilization_Object = MibTableColumn
adGenEth15MinCurrentOutPeakUtilization = _AdGenEth15MinCurrentOutPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 31),
    _AdGenEth15MinCurrentOutPeakUtilization_Type()
)
adGenEth15MinCurrentOutPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutPeakUtilization.setStatus("current")
_AdGenEth15MinCurrentOutAvgUtilization_Type = Gauge32
_AdGenEth15MinCurrentOutAvgUtilization_Object = MibTableColumn
adGenEth15MinCurrentOutAvgUtilization = _AdGenEth15MinCurrentOutAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 2, 1, 32),
    _AdGenEth15MinCurrentOutAvgUtilization_Type()
)
adGenEth15MinCurrentOutAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentOutAvgUtilization.setStatus("current")
_AdGenEth15MinCurrentHCTable_Object = MibTable
adGenEth15MinCurrentHCTable = _AdGenEth15MinCurrentHCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3)
)
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTable.setStatus("current")
_AdGenEth15MinCurrentHCEntry_Object = MibTableRow
adGenEth15MinCurrentHCEntry = _AdGenEth15MinCurrentHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1)
)
adGenEth15MinCurrentHCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCEntry.setStatus("current")
_AdGenEth15MinCurrentHCOutOctets_Type = Counter64
_AdGenEth15MinCurrentHCOutOctets_Object = MibTableColumn
adGenEth15MinCurrentHCOutOctets = _AdGenEth15MinCurrentHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 1),
    _AdGenEth15MinCurrentHCOutOctets_Type()
)
adGenEth15MinCurrentHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCOutOctets.setStatus("current")
_AdGenEth15MinCurrentHCInOctets_Type = Counter64
_AdGenEth15MinCurrentHCInOctets_Object = MibTableColumn
adGenEth15MinCurrentHCInOctets = _AdGenEth15MinCurrentHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 2),
    _AdGenEth15MinCurrentHCInOctets_Type()
)
adGenEth15MinCurrentHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCInOctets.setStatus("current")
_AdGenEth15MinCurrentHCInMulticastPkts_Type = Counter64
_AdGenEth15MinCurrentHCInMulticastPkts_Object = MibTableColumn
adGenEth15MinCurrentHCInMulticastPkts = _AdGenEth15MinCurrentHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 3),
    _AdGenEth15MinCurrentHCInMulticastPkts_Type()
)
adGenEth15MinCurrentHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCInMulticastPkts.setStatus("current")
_AdGenEth15MinCurrentHCInBroadcastPkts_Type = Counter64
_AdGenEth15MinCurrentHCInBroadcastPkts_Object = MibTableColumn
adGenEth15MinCurrentHCInBroadcastPkts = _AdGenEth15MinCurrentHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 4),
    _AdGenEth15MinCurrentHCInBroadcastPkts_Type()
)
adGenEth15MinCurrentHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCInBroadcastPkts.setStatus("current")
_AdGenEth15MinCurrentHCInUnicastPkts_Type = Counter64
_AdGenEth15MinCurrentHCInUnicastPkts_Object = MibTableColumn
adGenEth15MinCurrentHCInUnicastPkts = _AdGenEth15MinCurrentHCInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 5),
    _AdGenEth15MinCurrentHCInUnicastPkts_Type()
)
adGenEth15MinCurrentHCInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCInUnicastPkts.setStatus("current")
_AdGenEth15MinCurrentHCOutMulticastPkts_Type = Counter64
_AdGenEth15MinCurrentHCOutMulticastPkts_Object = MibTableColumn
adGenEth15MinCurrentHCOutMulticastPkts = _AdGenEth15MinCurrentHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 6),
    _AdGenEth15MinCurrentHCOutMulticastPkts_Type()
)
adGenEth15MinCurrentHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCOutMulticastPkts.setStatus("current")
_AdGenEth15MinCurrentHCOutBroadcastPkts_Type = Counter64
_AdGenEth15MinCurrentHCOutBroadcastPkts_Object = MibTableColumn
adGenEth15MinCurrentHCOutBroadcastPkts = _AdGenEth15MinCurrentHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 7),
    _AdGenEth15MinCurrentHCOutBroadcastPkts_Type()
)
adGenEth15MinCurrentHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCOutBroadcastPkts.setStatus("current")
_AdGenEth15MinCurrentHCOutUnicastPkts_Type = Counter64
_AdGenEth15MinCurrentHCOutUnicastPkts_Object = MibTableColumn
adGenEth15MinCurrentHCOutUnicastPkts = _AdGenEth15MinCurrentHCOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 8),
    _AdGenEth15MinCurrentHCOutUnicastPkts_Type()
)
adGenEth15MinCurrentHCOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCOutUnicastPkts.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue0_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue0_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue0 = _AdGenEth15MinCurrentHCTotalPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 9),
    _AdGenEth15MinCurrentHCTotalPktsQueue0_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue0.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue1_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue1_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue1 = _AdGenEth15MinCurrentHCTotalPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 10),
    _AdGenEth15MinCurrentHCTotalPktsQueue1_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue1.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue2_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue2_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue2 = _AdGenEth15MinCurrentHCTotalPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 11),
    _AdGenEth15MinCurrentHCTotalPktsQueue2_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue2.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue3_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue3_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue3 = _AdGenEth15MinCurrentHCTotalPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 12),
    _AdGenEth15MinCurrentHCTotalPktsQueue3_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue3.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue4_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue4_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue4 = _AdGenEth15MinCurrentHCTotalPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 13),
    _AdGenEth15MinCurrentHCTotalPktsQueue4_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue4.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue5_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue5_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue5 = _AdGenEth15MinCurrentHCTotalPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 14),
    _AdGenEth15MinCurrentHCTotalPktsQueue5_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue5.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue6_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue6_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue6 = _AdGenEth15MinCurrentHCTotalPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 15),
    _AdGenEth15MinCurrentHCTotalPktsQueue6_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue6.setStatus("current")
_AdGenEth15MinCurrentHCTotalPktsQueue7_Type = Counter64
_AdGenEth15MinCurrentHCTotalPktsQueue7_Object = MibTableColumn
adGenEth15MinCurrentHCTotalPktsQueue7 = _AdGenEth15MinCurrentHCTotalPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 16),
    _AdGenEth15MinCurrentHCTotalPktsQueue7_Type()
)
adGenEth15MinCurrentHCTotalPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCTotalPktsQueue7.setStatus("current")
_AdGenEth15MinCurrentHCOutLcv_Type = Counter64
_AdGenEth15MinCurrentHCOutLcv_Object = MibTableColumn
adGenEth15MinCurrentHCOutLcv = _AdGenEth15MinCurrentHCOutLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 17),
    _AdGenEth15MinCurrentHCOutLcv_Type()
)
adGenEth15MinCurrentHCOutLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCOutLcv.setStatus("current")
_AdGenEth15MinCurrentHCInLcv_Type = Counter64
_AdGenEth15MinCurrentHCInLcv_Object = MibTableColumn
adGenEth15MinCurrentHCInLcv = _AdGenEth15MinCurrentHCInLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 18),
    _AdGenEth15MinCurrentHCInLcv_Type()
)
adGenEth15MinCurrentHCInLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCInLcv.setStatus("current")
_AdGenEth15MinCurrentHCInAvgBitsPerSec_Type = Counter64
_AdGenEth15MinCurrentHCInAvgBitsPerSec_Object = MibTableColumn
adGenEth15MinCurrentHCInAvgBitsPerSec = _AdGenEth15MinCurrentHCInAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 19),
    _AdGenEth15MinCurrentHCInAvgBitsPerSec_Type()
)
adGenEth15MinCurrentHCInAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCInAvgBitsPerSec.setStatus("current")
_AdGenEth15MinCurrentHCInAvgPktsPerSec_Type = Counter64
_AdGenEth15MinCurrentHCInAvgPktsPerSec_Object = MibTableColumn
adGenEth15MinCurrentHCInAvgPktsPerSec = _AdGenEth15MinCurrentHCInAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 20),
    _AdGenEth15MinCurrentHCInAvgPktsPerSec_Type()
)
adGenEth15MinCurrentHCInAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCInAvgPktsPerSec.setStatus("current")
_AdGenEth15MinCurrentHCOutAvgBitsPerSec_Type = Counter64
_AdGenEth15MinCurrentHCOutAvgBitsPerSec_Object = MibTableColumn
adGenEth15MinCurrentHCOutAvgBitsPerSec = _AdGenEth15MinCurrentHCOutAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 21),
    _AdGenEth15MinCurrentHCOutAvgBitsPerSec_Type()
)
adGenEth15MinCurrentHCOutAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCOutAvgBitsPerSec.setStatus("current")
_AdGenEth15MinCurrentHCOutAvgPktsPerSec_Type = Counter64
_AdGenEth15MinCurrentHCOutAvgPktsPerSec_Object = MibTableColumn
adGenEth15MinCurrentHCOutAvgPktsPerSec = _AdGenEth15MinCurrentHCOutAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 3, 1, 22),
    _AdGenEth15MinCurrentHCOutAvgPktsPerSec_Type()
)
adGenEth15MinCurrentHCOutAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinCurrentHCOutAvgPktsPerSec.setStatus("current")
_AdGenEth15MinIntervalTable_Object = MibTable
adGenEth15MinIntervalTable = _AdGenEth15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4)
)
if mibBuilder.loadTexts:
    adGenEth15MinIntervalTable.setStatus("current")
_AdGenEth15MinIntervalEntry_Object = MibTableRow
adGenEth15MinIntervalEntry = _AdGenEth15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1)
)
adGenEth15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-ETH-IFC-MIB", "adGenEth15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenEth15MinIntervalEntry.setStatus("current")
_AdGenEth15MinIntervalNumber_Type = Integer32
_AdGenEth15MinIntervalNumber_Object = MibTableColumn
adGenEth15MinIntervalNumber = _AdGenEth15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 1),
    _AdGenEth15MinIntervalNumber_Type()
)
adGenEth15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalNumber.setStatus("current")
_AdGenEth15MinIntervalOutOctets_Type = Gauge32
_AdGenEth15MinIntervalOutOctets_Object = MibTableColumn
adGenEth15MinIntervalOutOctets = _AdGenEth15MinIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 2),
    _AdGenEth15MinIntervalOutOctets_Type()
)
adGenEth15MinIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutOctets.setStatus("current")
_AdGenEth15MinIntervalOutPkts_Type = Gauge32
_AdGenEth15MinIntervalOutPkts_Object = MibTableColumn
adGenEth15MinIntervalOutPkts = _AdGenEth15MinIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 3),
    _AdGenEth15MinIntervalOutPkts_Type()
)
adGenEth15MinIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutPkts.setStatus("current")
_AdGenEth15MinIntervalInOctets_Type = Gauge32
_AdGenEth15MinIntervalInOctets_Object = MibTableColumn
adGenEth15MinIntervalInOctets = _AdGenEth15MinIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 4),
    _AdGenEth15MinIntervalInOctets_Type()
)
adGenEth15MinIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInOctets.setStatus("current")
_AdGenEth15MinIntervalInPkts_Type = Gauge32
_AdGenEth15MinIntervalInPkts_Object = MibTableColumn
adGenEth15MinIntervalInPkts = _AdGenEth15MinIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 5),
    _AdGenEth15MinIntervalInPkts_Type()
)
adGenEth15MinIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInPkts.setStatus("current")
_AdGenEth15MinIntervalInGoodOctets_Type = Gauge32
_AdGenEth15MinIntervalInGoodOctets_Object = MibTableColumn
adGenEth15MinIntervalInGoodOctets = _AdGenEth15MinIntervalInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 6),
    _AdGenEth15MinIntervalInGoodOctets_Type()
)
adGenEth15MinIntervalInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInGoodOctets.setStatus("current")
_AdGenEth15MinIntervalInGoodPkts_Type = Gauge32
_AdGenEth15MinIntervalInGoodPkts_Object = MibTableColumn
adGenEth15MinIntervalInGoodPkts = _AdGenEth15MinIntervalInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 7),
    _AdGenEth15MinIntervalInGoodPkts_Type()
)
adGenEth15MinIntervalInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInGoodPkts.setStatus("current")
_AdGenEth15MinIntervalInErrors_Type = Gauge32
_AdGenEth15MinIntervalInErrors_Object = MibTableColumn
adGenEth15MinIntervalInErrors = _AdGenEth15MinIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 8),
    _AdGenEth15MinIntervalInErrors_Type()
)
adGenEth15MinIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInErrors.setStatus("current")
_AdGenEth15MinIntervalInDiscards_Type = Gauge32
_AdGenEth15MinIntervalInDiscards_Object = MibTableColumn
adGenEth15MinIntervalInDiscards = _AdGenEth15MinIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 9),
    _AdGenEth15MinIntervalInDiscards_Type()
)
adGenEth15MinIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInDiscards.setStatus("current")
_AdGenEth15MinIntervalInGiants_Type = Gauge32
_AdGenEth15MinIntervalInGiants_Object = MibTableColumn
adGenEth15MinIntervalInGiants = _AdGenEth15MinIntervalInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 10),
    _AdGenEth15MinIntervalInGiants_Type()
)
adGenEth15MinIntervalInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInGiants.setStatus("current")
_AdGenEth15MinIntervalInRunts_Type = Gauge32
_AdGenEth15MinIntervalInRunts_Object = MibTableColumn
adGenEth15MinIntervalInRunts = _AdGenEth15MinIntervalInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 11),
    _AdGenEth15MinIntervalInRunts_Type()
)
adGenEth15MinIntervalInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInRunts.setStatus("current")
_AdGenEth15MinIntervalInMulticastPkts_Type = Gauge32
_AdGenEth15MinIntervalInMulticastPkts_Object = MibTableColumn
adGenEth15MinIntervalInMulticastPkts = _AdGenEth15MinIntervalInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 12),
    _AdGenEth15MinIntervalInMulticastPkts_Type()
)
adGenEth15MinIntervalInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInMulticastPkts.setStatus("current")
_AdGenEth15MinIntervalInBroadcastPkts_Type = Gauge32
_AdGenEth15MinIntervalInBroadcastPkts_Object = MibTableColumn
adGenEth15MinIntervalInBroadcastPkts = _AdGenEth15MinIntervalInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 13),
    _AdGenEth15MinIntervalInBroadcastPkts_Type()
)
adGenEth15MinIntervalInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInBroadcastPkts.setStatus("current")
_AdGenEth15MinIntervalInUnicastPkts_Type = Gauge32
_AdGenEth15MinIntervalInUnicastPkts_Object = MibTableColumn
adGenEth15MinIntervalInUnicastPkts = _AdGenEth15MinIntervalInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 14),
    _AdGenEth15MinIntervalInUnicastPkts_Type()
)
adGenEth15MinIntervalInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInUnicastPkts.setStatus("current")
_AdGenEth15MinIntervalOutMulticastPkts_Type = Gauge32
_AdGenEth15MinIntervalOutMulticastPkts_Object = MibTableColumn
adGenEth15MinIntervalOutMulticastPkts = _AdGenEth15MinIntervalOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 15),
    _AdGenEth15MinIntervalOutMulticastPkts_Type()
)
adGenEth15MinIntervalOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutMulticastPkts.setStatus("current")
_AdGenEth15MinIntervalOutBroadcastPkts_Type = Gauge32
_AdGenEth15MinIntervalOutBroadcastPkts_Object = MibTableColumn
adGenEth15MinIntervalOutBroadcastPkts = _AdGenEth15MinIntervalOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 16),
    _AdGenEth15MinIntervalOutBroadcastPkts_Type()
)
adGenEth15MinIntervalOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutBroadcastPkts.setStatus("current")
_AdGenEth15MinIntervalOutUnicastPkts_Type = Gauge32
_AdGenEth15MinIntervalOutUnicastPkts_Object = MibTableColumn
adGenEth15MinIntervalOutUnicastPkts = _AdGenEth15MinIntervalOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 17),
    _AdGenEth15MinIntervalOutUnicastPkts_Type()
)
adGenEth15MinIntervalOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutUnicastPkts.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue0_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue0_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue0 = _AdGenEth15MinIntervalDroppedPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 18),
    _AdGenEth15MinIntervalDroppedPktsQueue0_Type()
)
adGenEth15MinIntervalDroppedPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue0.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue1_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue1_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue1 = _AdGenEth15MinIntervalDroppedPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 19),
    _AdGenEth15MinIntervalDroppedPktsQueue1_Type()
)
adGenEth15MinIntervalDroppedPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue1.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue2_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue2_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue2 = _AdGenEth15MinIntervalDroppedPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 20),
    _AdGenEth15MinIntervalDroppedPktsQueue2_Type()
)
adGenEth15MinIntervalDroppedPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue2.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue3_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue3_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue3 = _AdGenEth15MinIntervalDroppedPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 21),
    _AdGenEth15MinIntervalDroppedPktsQueue3_Type()
)
adGenEth15MinIntervalDroppedPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue3.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue4_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue4_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue4 = _AdGenEth15MinIntervalDroppedPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 22),
    _AdGenEth15MinIntervalDroppedPktsQueue4_Type()
)
adGenEth15MinIntervalDroppedPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue4.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue5_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue5_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue5 = _AdGenEth15MinIntervalDroppedPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 23),
    _AdGenEth15MinIntervalDroppedPktsQueue5_Type()
)
adGenEth15MinIntervalDroppedPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue5.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue6_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue6_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue6 = _AdGenEth15MinIntervalDroppedPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 24),
    _AdGenEth15MinIntervalDroppedPktsQueue6_Type()
)
adGenEth15MinIntervalDroppedPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue6.setStatus("current")
_AdGenEth15MinIntervalDroppedPktsQueue7_Type = Gauge32
_AdGenEth15MinIntervalDroppedPktsQueue7_Object = MibTableColumn
adGenEth15MinIntervalDroppedPktsQueue7 = _AdGenEth15MinIntervalDroppedPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 25),
    _AdGenEth15MinIntervalDroppedPktsQueue7_Type()
)
adGenEth15MinIntervalDroppedPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalDroppedPktsQueue7.setStatus("current")
_AdGenEth15MinIntervalOutDiscards_Type = Gauge32
_AdGenEth15MinIntervalOutDiscards_Object = MibTableColumn
adGenEth15MinIntervalOutDiscards = _AdGenEth15MinIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 26),
    _AdGenEth15MinIntervalOutDiscards_Type()
)
adGenEth15MinIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutDiscards.setStatus("current")
_AdGenEth15MinIntervalInCRCErrors_Type = Gauge32
_AdGenEth15MinIntervalInCRCErrors_Object = MibTableColumn
adGenEth15MinIntervalInCRCErrors = _AdGenEth15MinIntervalInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 27),
    _AdGenEth15MinIntervalInCRCErrors_Type()
)
adGenEth15MinIntervalInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInCRCErrors.setStatus("current")
_AdGenEth15MinIntervalInFrameErrors_Type = Gauge32
_AdGenEth15MinIntervalInFrameErrors_Object = MibTableColumn
adGenEth15MinIntervalInFrameErrors = _AdGenEth15MinIntervalInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 28),
    _AdGenEth15MinIntervalInFrameErrors_Type()
)
adGenEth15MinIntervalInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInFrameErrors.setStatus("current")
_AdGenEth15MinIntervalOutErrors_Type = Gauge32
_AdGenEth15MinIntervalOutErrors_Object = MibTableColumn
adGenEth15MinIntervalOutErrors = _AdGenEth15MinIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 29),
    _AdGenEth15MinIntervalOutErrors_Type()
)
adGenEth15MinIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutErrors.setStatus("current")
_AdGenEth15MinIntervalInPeakUtilization_Type = Gauge32
_AdGenEth15MinIntervalInPeakUtilization_Object = MibTableColumn
adGenEth15MinIntervalInPeakUtilization = _AdGenEth15MinIntervalInPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 30),
    _AdGenEth15MinIntervalInPeakUtilization_Type()
)
adGenEth15MinIntervalInPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInPeakUtilization.setStatus("current")
_AdGenEth15MinIntervalInAvgUtilization_Type = Gauge32
_AdGenEth15MinIntervalInAvgUtilization_Object = MibTableColumn
adGenEth15MinIntervalInAvgUtilization = _AdGenEth15MinIntervalInAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 31),
    _AdGenEth15MinIntervalInAvgUtilization_Type()
)
adGenEth15MinIntervalInAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalInAvgUtilization.setStatus("current")
_AdGenEth15MinIntervalOutPeakUtilization_Type = Gauge32
_AdGenEth15MinIntervalOutPeakUtilization_Object = MibTableColumn
adGenEth15MinIntervalOutPeakUtilization = _AdGenEth15MinIntervalOutPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 32),
    _AdGenEth15MinIntervalOutPeakUtilization_Type()
)
adGenEth15MinIntervalOutPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutPeakUtilization.setStatus("current")
_AdGenEth15MinIntervalOutAvgUtilization_Type = Gauge32
_AdGenEth15MinIntervalOutAvgUtilization_Object = MibTableColumn
adGenEth15MinIntervalOutAvgUtilization = _AdGenEth15MinIntervalOutAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 4, 1, 33),
    _AdGenEth15MinIntervalOutAvgUtilization_Type()
)
adGenEth15MinIntervalOutAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalOutAvgUtilization.setStatus("current")
_AdGenEth15MinIntervalHCTable_Object = MibTable
adGenEth15MinIntervalHCTable = _AdGenEth15MinIntervalHCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5)
)
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTable.setStatus("current")
_AdGenEth15MinIntervalHCEntry_Object = MibTableRow
adGenEth15MinIntervalHCEntry = _AdGenEth15MinIntervalHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1)
)
adGenEth15MinIntervalHCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-ETH-IFC-MIB", "adGenEth15MinIntervalHCNumber"),
)
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCEntry.setStatus("current")
_AdGenEth15MinIntervalHCNumber_Type = Integer32
_AdGenEth15MinIntervalHCNumber_Object = MibTableColumn
adGenEth15MinIntervalHCNumber = _AdGenEth15MinIntervalHCNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 1),
    _AdGenEth15MinIntervalHCNumber_Type()
)
adGenEth15MinIntervalHCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCNumber.setStatus("current")
_AdGenEth15MinIntervalHCOutOctets_Type = Counter64
_AdGenEth15MinIntervalHCOutOctets_Object = MibTableColumn
adGenEth15MinIntervalHCOutOctets = _AdGenEth15MinIntervalHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 2),
    _AdGenEth15MinIntervalHCOutOctets_Type()
)
adGenEth15MinIntervalHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCOutOctets.setStatus("current")
_AdGenEth15MinIntervalHCInOctets_Type = Counter64
_AdGenEth15MinIntervalHCInOctets_Object = MibTableColumn
adGenEth15MinIntervalHCInOctets = _AdGenEth15MinIntervalHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 3),
    _AdGenEth15MinIntervalHCInOctets_Type()
)
adGenEth15MinIntervalHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCInOctets.setStatus("current")
_AdGenEth15MinIntervalHCInMulticastPkts_Type = Counter64
_AdGenEth15MinIntervalHCInMulticastPkts_Object = MibTableColumn
adGenEth15MinIntervalHCInMulticastPkts = _AdGenEth15MinIntervalHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 4),
    _AdGenEth15MinIntervalHCInMulticastPkts_Type()
)
adGenEth15MinIntervalHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCInMulticastPkts.setStatus("current")
_AdGenEth15MinIntervalHCInBroadcastPkts_Type = Counter64
_AdGenEth15MinIntervalHCInBroadcastPkts_Object = MibTableColumn
adGenEth15MinIntervalHCInBroadcastPkts = _AdGenEth15MinIntervalHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 5),
    _AdGenEth15MinIntervalHCInBroadcastPkts_Type()
)
adGenEth15MinIntervalHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCInBroadcastPkts.setStatus("current")
_AdGenEth15MinIntervalHCInUnicastPkts_Type = Counter64
_AdGenEth15MinIntervalHCInUnicastPkts_Object = MibTableColumn
adGenEth15MinIntervalHCInUnicastPkts = _AdGenEth15MinIntervalHCInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 6),
    _AdGenEth15MinIntervalHCInUnicastPkts_Type()
)
adGenEth15MinIntervalHCInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCInUnicastPkts.setStatus("current")
_AdGenEth15MinIntervalHCOutMulticastPkts_Type = Counter64
_AdGenEth15MinIntervalHCOutMulticastPkts_Object = MibTableColumn
adGenEth15MinIntervalHCOutMulticastPkts = _AdGenEth15MinIntervalHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 7),
    _AdGenEth15MinIntervalHCOutMulticastPkts_Type()
)
adGenEth15MinIntervalHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCOutMulticastPkts.setStatus("current")
_AdGenEth15MinIntervalHCOutBroadcastPkts_Type = Counter64
_AdGenEth15MinIntervalHCOutBroadcastPkts_Object = MibTableColumn
adGenEth15MinIntervalHCOutBroadcastPkts = _AdGenEth15MinIntervalHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 8),
    _AdGenEth15MinIntervalHCOutBroadcastPkts_Type()
)
adGenEth15MinIntervalHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCOutBroadcastPkts.setStatus("current")
_AdGenEth15MinIntervalHCOutUnicastPkts_Type = Counter64
_AdGenEth15MinIntervalHCOutUnicastPkts_Object = MibTableColumn
adGenEth15MinIntervalHCOutUnicastPkts = _AdGenEth15MinIntervalHCOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 9),
    _AdGenEth15MinIntervalHCOutUnicastPkts_Type()
)
adGenEth15MinIntervalHCOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCOutUnicastPkts.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue0_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue0_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue0 = _AdGenEth15MinIntervalHCTotalPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 10),
    _AdGenEth15MinIntervalHCTotalPktsQueue0_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue0.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue1_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue1_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue1 = _AdGenEth15MinIntervalHCTotalPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 11),
    _AdGenEth15MinIntervalHCTotalPktsQueue1_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue1.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue2_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue2_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue2 = _AdGenEth15MinIntervalHCTotalPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 12),
    _AdGenEth15MinIntervalHCTotalPktsQueue2_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue2.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue3_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue3_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue3 = _AdGenEth15MinIntervalHCTotalPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 13),
    _AdGenEth15MinIntervalHCTotalPktsQueue3_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue3.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue4_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue4_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue4 = _AdGenEth15MinIntervalHCTotalPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 14),
    _AdGenEth15MinIntervalHCTotalPktsQueue4_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue4.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue5_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue5_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue5 = _AdGenEth15MinIntervalHCTotalPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 15),
    _AdGenEth15MinIntervalHCTotalPktsQueue5_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue5.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue6_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue6_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue6 = _AdGenEth15MinIntervalHCTotalPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 16),
    _AdGenEth15MinIntervalHCTotalPktsQueue6_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue6.setStatus("current")
_AdGenEth15MinIntervalHCTotalPktsQueue7_Type = Counter64
_AdGenEth15MinIntervalHCTotalPktsQueue7_Object = MibTableColumn
adGenEth15MinIntervalHCTotalPktsQueue7 = _AdGenEth15MinIntervalHCTotalPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 17),
    _AdGenEth15MinIntervalHCTotalPktsQueue7_Type()
)
adGenEth15MinIntervalHCTotalPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCTotalPktsQueue7.setStatus("current")
_AdGenEth15MinIntervalHCOutLcv_Type = Counter64
_AdGenEth15MinIntervalHCOutLcv_Object = MibTableColumn
adGenEth15MinIntervalHCOutLcv = _AdGenEth15MinIntervalHCOutLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 18),
    _AdGenEth15MinIntervalHCOutLcv_Type()
)
adGenEth15MinIntervalHCOutLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCOutLcv.setStatus("current")
_AdGenEth15MinIntervalHCInLcv_Type = Counter64
_AdGenEth15MinIntervalHCInLcv_Object = MibTableColumn
adGenEth15MinIntervalHCInLcv = _AdGenEth15MinIntervalHCInLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 19),
    _AdGenEth15MinIntervalHCInLcv_Type()
)
adGenEth15MinIntervalHCInLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCInLcv.setStatus("current")
_AdGenEth15MinIntervalHCValidData_Type = TruthValue
_AdGenEth15MinIntervalHCValidData_Object = MibTableColumn
adGenEth15MinIntervalHCValidData = _AdGenEth15MinIntervalHCValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 20),
    _AdGenEth15MinIntervalHCValidData_Type()
)
adGenEth15MinIntervalHCValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCValidData.setStatus("current")
_AdGenEth15MinIntervalHCInAvgBitsPerSec_Type = Counter64
_AdGenEth15MinIntervalHCInAvgBitsPerSec_Object = MibTableColumn
adGenEth15MinIntervalHCInAvgBitsPerSec = _AdGenEth15MinIntervalHCInAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 21),
    _AdGenEth15MinIntervalHCInAvgBitsPerSec_Type()
)
adGenEth15MinIntervalHCInAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCInAvgBitsPerSec.setStatus("current")
_AdGenEth15MinIntervalHCInAvgPktsPerSec_Type = Counter64
_AdGenEth15MinIntervalHCInAvgPktsPerSec_Object = MibTableColumn
adGenEth15MinIntervalHCInAvgPktsPerSec = _AdGenEth15MinIntervalHCInAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 22),
    _AdGenEth15MinIntervalHCInAvgPktsPerSec_Type()
)
adGenEth15MinIntervalHCInAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCInAvgPktsPerSec.setStatus("current")
_AdGenEth15MinIntervalHCOutAvgBitsPerSec_Type = Counter64
_AdGenEth15MinIntervalHCOutAvgBitsPerSec_Object = MibTableColumn
adGenEth15MinIntervalHCOutAvgBitsPerSec = _AdGenEth15MinIntervalHCOutAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 23),
    _AdGenEth15MinIntervalHCOutAvgBitsPerSec_Type()
)
adGenEth15MinIntervalHCOutAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCOutAvgBitsPerSec.setStatus("current")
_AdGenEth15MinIntervalHCOutAvgPktsPerSec_Type = Counter64
_AdGenEth15MinIntervalHCOutAvgPktsPerSec_Object = MibTableColumn
adGenEth15MinIntervalHCOutAvgPktsPerSec = _AdGenEth15MinIntervalHCOutAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 5, 1, 24),
    _AdGenEth15MinIntervalHCOutAvgPktsPerSec_Type()
)
adGenEth15MinIntervalHCOutAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth15MinIntervalHCOutAvgPktsPerSec.setStatus("current")
_AdGenEth24HrCurrentTable_Object = MibTable
adGenEth24HrCurrentTable = _AdGenEth24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6)
)
if mibBuilder.loadTexts:
    adGenEth24HrCurrentTable.setStatus("current")
_AdGenEth24HrCurrentEntry_Object = MibTableRow
adGenEth24HrCurrentEntry = _AdGenEth24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1)
)
adGenEth24HrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEth24HrCurrentEntry.setStatus("current")
_AdGenEth24HrCurrentOutOctets_Type = Gauge32
_AdGenEth24HrCurrentOutOctets_Object = MibTableColumn
adGenEth24HrCurrentOutOctets = _AdGenEth24HrCurrentOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 1),
    _AdGenEth24HrCurrentOutOctets_Type()
)
adGenEth24HrCurrentOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutOctets.setStatus("current")
_AdGenEth24HrCurrentOutPkts_Type = Gauge32
_AdGenEth24HrCurrentOutPkts_Object = MibTableColumn
adGenEth24HrCurrentOutPkts = _AdGenEth24HrCurrentOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 2),
    _AdGenEth24HrCurrentOutPkts_Type()
)
adGenEth24HrCurrentOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutPkts.setStatus("current")
_AdGenEth24HrCurrentInOctets_Type = Gauge32
_AdGenEth24HrCurrentInOctets_Object = MibTableColumn
adGenEth24HrCurrentInOctets = _AdGenEth24HrCurrentInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 3),
    _AdGenEth24HrCurrentInOctets_Type()
)
adGenEth24HrCurrentInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInOctets.setStatus("current")
_AdGenEth24HrCurrentInPkts_Type = Gauge32
_AdGenEth24HrCurrentInPkts_Object = MibTableColumn
adGenEth24HrCurrentInPkts = _AdGenEth24HrCurrentInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 4),
    _AdGenEth24HrCurrentInPkts_Type()
)
adGenEth24HrCurrentInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInPkts.setStatus("current")
_AdGenEth24HrCurrentInGoodOctets_Type = Gauge32
_AdGenEth24HrCurrentInGoodOctets_Object = MibTableColumn
adGenEth24HrCurrentInGoodOctets = _AdGenEth24HrCurrentInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 5),
    _AdGenEth24HrCurrentInGoodOctets_Type()
)
adGenEth24HrCurrentInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInGoodOctets.setStatus("current")
_AdGenEth24HrCurrentInGoodPkts_Type = Gauge32
_AdGenEth24HrCurrentInGoodPkts_Object = MibTableColumn
adGenEth24HrCurrentInGoodPkts = _AdGenEth24HrCurrentInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 6),
    _AdGenEth24HrCurrentInGoodPkts_Type()
)
adGenEth24HrCurrentInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInGoodPkts.setStatus("current")
_AdGenEth24HrCurrentInErrors_Type = Gauge32
_AdGenEth24HrCurrentInErrors_Object = MibTableColumn
adGenEth24HrCurrentInErrors = _AdGenEth24HrCurrentInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 7),
    _AdGenEth24HrCurrentInErrors_Type()
)
adGenEth24HrCurrentInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInErrors.setStatus("current")
_AdGenEth24HrCurrentInDiscards_Type = Gauge32
_AdGenEth24HrCurrentInDiscards_Object = MibTableColumn
adGenEth24HrCurrentInDiscards = _AdGenEth24HrCurrentInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 8),
    _AdGenEth24HrCurrentInDiscards_Type()
)
adGenEth24HrCurrentInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInDiscards.setStatus("current")
_AdGenEth24HrCurrentInGiants_Type = Gauge32
_AdGenEth24HrCurrentInGiants_Object = MibTableColumn
adGenEth24HrCurrentInGiants = _AdGenEth24HrCurrentInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 9),
    _AdGenEth24HrCurrentInGiants_Type()
)
adGenEth24HrCurrentInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInGiants.setStatus("current")
_AdGenEth24HrCurrentInRunts_Type = Gauge32
_AdGenEth24HrCurrentInRunts_Object = MibTableColumn
adGenEth24HrCurrentInRunts = _AdGenEth24HrCurrentInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 10),
    _AdGenEth24HrCurrentInRunts_Type()
)
adGenEth24HrCurrentInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInRunts.setStatus("current")
_AdGenEth24HrCurrentInMulticastPkts_Type = Gauge32
_AdGenEth24HrCurrentInMulticastPkts_Object = MibTableColumn
adGenEth24HrCurrentInMulticastPkts = _AdGenEth24HrCurrentInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 11),
    _AdGenEth24HrCurrentInMulticastPkts_Type()
)
adGenEth24HrCurrentInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInMulticastPkts.setStatus("current")
_AdGenEth24HrCurrentInBroadcastPkts_Type = Gauge32
_AdGenEth24HrCurrentInBroadcastPkts_Object = MibTableColumn
adGenEth24HrCurrentInBroadcastPkts = _AdGenEth24HrCurrentInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 12),
    _AdGenEth24HrCurrentInBroadcastPkts_Type()
)
adGenEth24HrCurrentInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInBroadcastPkts.setStatus("current")
_AdGenEth24HrCurrentInUnicastPkts_Type = Gauge32
_AdGenEth24HrCurrentInUnicastPkts_Object = MibTableColumn
adGenEth24HrCurrentInUnicastPkts = _AdGenEth24HrCurrentInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 13),
    _AdGenEth24HrCurrentInUnicastPkts_Type()
)
adGenEth24HrCurrentInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInUnicastPkts.setStatus("current")
_AdGenEth24HrCurrentOutMulticastPkts_Type = Gauge32
_AdGenEth24HrCurrentOutMulticastPkts_Object = MibTableColumn
adGenEth24HrCurrentOutMulticastPkts = _AdGenEth24HrCurrentOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 14),
    _AdGenEth24HrCurrentOutMulticastPkts_Type()
)
adGenEth24HrCurrentOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutMulticastPkts.setStatus("current")
_AdGenEth24HrCurrentOutBroadcastPkts_Type = Gauge32
_AdGenEth24HrCurrentOutBroadcastPkts_Object = MibTableColumn
adGenEth24HrCurrentOutBroadcastPkts = _AdGenEth24HrCurrentOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 15),
    _AdGenEth24HrCurrentOutBroadcastPkts_Type()
)
adGenEth24HrCurrentOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutBroadcastPkts.setStatus("current")
_AdGenEth24HrCurrentOutUnicastPkts_Type = Gauge32
_AdGenEth24HrCurrentOutUnicastPkts_Object = MibTableColumn
adGenEth24HrCurrentOutUnicastPkts = _AdGenEth24HrCurrentOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 16),
    _AdGenEth24HrCurrentOutUnicastPkts_Type()
)
adGenEth24HrCurrentOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutUnicastPkts.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue0_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue0_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue0 = _AdGenEth24HrCurrentDroppedPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 17),
    _AdGenEth24HrCurrentDroppedPktsQueue0_Type()
)
adGenEth24HrCurrentDroppedPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue0.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue1_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue1_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue1 = _AdGenEth24HrCurrentDroppedPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 18),
    _AdGenEth24HrCurrentDroppedPktsQueue1_Type()
)
adGenEth24HrCurrentDroppedPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue1.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue2_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue2_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue2 = _AdGenEth24HrCurrentDroppedPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 19),
    _AdGenEth24HrCurrentDroppedPktsQueue2_Type()
)
adGenEth24HrCurrentDroppedPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue2.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue3_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue3_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue3 = _AdGenEth24HrCurrentDroppedPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 20),
    _AdGenEth24HrCurrentDroppedPktsQueue3_Type()
)
adGenEth24HrCurrentDroppedPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue3.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue4_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue4_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue4 = _AdGenEth24HrCurrentDroppedPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 21),
    _AdGenEth24HrCurrentDroppedPktsQueue4_Type()
)
adGenEth24HrCurrentDroppedPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue4.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue5_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue5_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue5 = _AdGenEth24HrCurrentDroppedPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 22),
    _AdGenEth24HrCurrentDroppedPktsQueue5_Type()
)
adGenEth24HrCurrentDroppedPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue5.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue6_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue6_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue6 = _AdGenEth24HrCurrentDroppedPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 23),
    _AdGenEth24HrCurrentDroppedPktsQueue6_Type()
)
adGenEth24HrCurrentDroppedPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue6.setStatus("current")
_AdGenEth24HrCurrentDroppedPktsQueue7_Type = Gauge32
_AdGenEth24HrCurrentDroppedPktsQueue7_Object = MibTableColumn
adGenEth24HrCurrentDroppedPktsQueue7 = _AdGenEth24HrCurrentDroppedPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 24),
    _AdGenEth24HrCurrentDroppedPktsQueue7_Type()
)
adGenEth24HrCurrentDroppedPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentDroppedPktsQueue7.setStatus("current")
_AdGenEth24HrCurrentOutDiscards_Type = Gauge32
_AdGenEth24HrCurrentOutDiscards_Object = MibTableColumn
adGenEth24HrCurrentOutDiscards = _AdGenEth24HrCurrentOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 25),
    _AdGenEth24HrCurrentOutDiscards_Type()
)
adGenEth24HrCurrentOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutDiscards.setStatus("current")
_AdGenEth24HrCurrentInCRCErrors_Type = Gauge32
_AdGenEth24HrCurrentInCRCErrors_Object = MibTableColumn
adGenEth24HrCurrentInCRCErrors = _AdGenEth24HrCurrentInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 26),
    _AdGenEth24HrCurrentInCRCErrors_Type()
)
adGenEth24HrCurrentInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInCRCErrors.setStatus("current")
_AdGenEth24HrCurrentInFrameErrors_Type = Gauge32
_AdGenEth24HrCurrentInFrameErrors_Object = MibTableColumn
adGenEth24HrCurrentInFrameErrors = _AdGenEth24HrCurrentInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 27),
    _AdGenEth24HrCurrentInFrameErrors_Type()
)
adGenEth24HrCurrentInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInFrameErrors.setStatus("current")
_AdGenEth24HrCurrentOutErrors_Type = Gauge32
_AdGenEth24HrCurrentOutErrors_Object = MibTableColumn
adGenEth24HrCurrentOutErrors = _AdGenEth24HrCurrentOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 28),
    _AdGenEth24HrCurrentOutErrors_Type()
)
adGenEth24HrCurrentOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutErrors.setStatus("current")
_AdGenEth24HrCurrentInPeakUtilization_Type = Gauge32
_AdGenEth24HrCurrentInPeakUtilization_Object = MibTableColumn
adGenEth24HrCurrentInPeakUtilization = _AdGenEth24HrCurrentInPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 29),
    _AdGenEth24HrCurrentInPeakUtilization_Type()
)
adGenEth24HrCurrentInPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInPeakUtilization.setStatus("current")
_AdGenEth24HrCurrentInAvgUtilization_Type = Gauge32
_AdGenEth24HrCurrentInAvgUtilization_Object = MibTableColumn
adGenEth24HrCurrentInAvgUtilization = _AdGenEth24HrCurrentInAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 30),
    _AdGenEth24HrCurrentInAvgUtilization_Type()
)
adGenEth24HrCurrentInAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentInAvgUtilization.setStatus("current")
_AdGenEth24HrCurrentOutPeakUtilization_Type = Gauge32
_AdGenEth24HrCurrentOutPeakUtilization_Object = MibTableColumn
adGenEth24HrCurrentOutPeakUtilization = _AdGenEth24HrCurrentOutPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 31),
    _AdGenEth24HrCurrentOutPeakUtilization_Type()
)
adGenEth24HrCurrentOutPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutPeakUtilization.setStatus("current")
_AdGenEth24HrCurrentOutAvgUtilization_Type = Gauge32
_AdGenEth24HrCurrentOutAvgUtilization_Object = MibTableColumn
adGenEth24HrCurrentOutAvgUtilization = _AdGenEth24HrCurrentOutAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 6, 1, 32),
    _AdGenEth24HrCurrentOutAvgUtilization_Type()
)
adGenEth24HrCurrentOutAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentOutAvgUtilization.setStatus("current")
_AdGenEth24HrCurrentHCTable_Object = MibTable
adGenEth24HrCurrentHCTable = _AdGenEth24HrCurrentHCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7)
)
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTable.setStatus("current")
_AdGenEth24HrCurrentHCEntry_Object = MibTableRow
adGenEth24HrCurrentHCEntry = _AdGenEth24HrCurrentHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1)
)
adGenEth24HrCurrentHCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCEntry.setStatus("current")
_AdGenEth24HrCurrentHCOutOctets_Type = Counter64
_AdGenEth24HrCurrentHCOutOctets_Object = MibTableColumn
adGenEth24HrCurrentHCOutOctets = _AdGenEth24HrCurrentHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 1),
    _AdGenEth24HrCurrentHCOutOctets_Type()
)
adGenEth24HrCurrentHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCOutOctets.setStatus("current")
_AdGenEth24HrCurrentHCInOctets_Type = Counter64
_AdGenEth24HrCurrentHCInOctets_Object = MibTableColumn
adGenEth24HrCurrentHCInOctets = _AdGenEth24HrCurrentHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 2),
    _AdGenEth24HrCurrentHCInOctets_Type()
)
adGenEth24HrCurrentHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCInOctets.setStatus("current")
_AdGenEth24HrCurrentHCInMulticastPkts_Type = Counter64
_AdGenEth24HrCurrentHCInMulticastPkts_Object = MibTableColumn
adGenEth24HrCurrentHCInMulticastPkts = _AdGenEth24HrCurrentHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 3),
    _AdGenEth24HrCurrentHCInMulticastPkts_Type()
)
adGenEth24HrCurrentHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCInMulticastPkts.setStatus("current")
_AdGenEth24HrCurrentHCInBroadcastPkts_Type = Counter64
_AdGenEth24HrCurrentHCInBroadcastPkts_Object = MibTableColumn
adGenEth24HrCurrentHCInBroadcastPkts = _AdGenEth24HrCurrentHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 4),
    _AdGenEth24HrCurrentHCInBroadcastPkts_Type()
)
adGenEth24HrCurrentHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCInBroadcastPkts.setStatus("current")
_AdGenEth24HrCurrentHCInUnicastPkts_Type = Counter64
_AdGenEth24HrCurrentHCInUnicastPkts_Object = MibTableColumn
adGenEth24HrCurrentHCInUnicastPkts = _AdGenEth24HrCurrentHCInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 5),
    _AdGenEth24HrCurrentHCInUnicastPkts_Type()
)
adGenEth24HrCurrentHCInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCInUnicastPkts.setStatus("current")
_AdGenEth24HrCurrentHCOutMulticastPkts_Type = Counter64
_AdGenEth24HrCurrentHCOutMulticastPkts_Object = MibTableColumn
adGenEth24HrCurrentHCOutMulticastPkts = _AdGenEth24HrCurrentHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 6),
    _AdGenEth24HrCurrentHCOutMulticastPkts_Type()
)
adGenEth24HrCurrentHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCOutMulticastPkts.setStatus("current")
_AdGenEth24HrCurrentHCOutBroadcastPkts_Type = Counter64
_AdGenEth24HrCurrentHCOutBroadcastPkts_Object = MibTableColumn
adGenEth24HrCurrentHCOutBroadcastPkts = _AdGenEth24HrCurrentHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 7),
    _AdGenEth24HrCurrentHCOutBroadcastPkts_Type()
)
adGenEth24HrCurrentHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCOutBroadcastPkts.setStatus("current")
_AdGenEth24HrCurrentHCOutUnicastPkts_Type = Counter64
_AdGenEth24HrCurrentHCOutUnicastPkts_Object = MibTableColumn
adGenEth24HrCurrentHCOutUnicastPkts = _AdGenEth24HrCurrentHCOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 8),
    _AdGenEth24HrCurrentHCOutUnicastPkts_Type()
)
adGenEth24HrCurrentHCOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCOutUnicastPkts.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue0_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue0_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue0 = _AdGenEth24HrCurrentHCTotalPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 9),
    _AdGenEth24HrCurrentHCTotalPktsQueue0_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue0.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue1_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue1_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue1 = _AdGenEth24HrCurrentHCTotalPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 10),
    _AdGenEth24HrCurrentHCTotalPktsQueue1_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue1.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue2_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue2_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue2 = _AdGenEth24HrCurrentHCTotalPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 11),
    _AdGenEth24HrCurrentHCTotalPktsQueue2_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue2.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue3_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue3_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue3 = _AdGenEth24HrCurrentHCTotalPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 12),
    _AdGenEth24HrCurrentHCTotalPktsQueue3_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue3.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue4_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue4_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue4 = _AdGenEth24HrCurrentHCTotalPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 13),
    _AdGenEth24HrCurrentHCTotalPktsQueue4_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue4.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue5_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue5_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue5 = _AdGenEth24HrCurrentHCTotalPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 14),
    _AdGenEth24HrCurrentHCTotalPktsQueue5_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue5.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue6_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue6_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue6 = _AdGenEth24HrCurrentHCTotalPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 15),
    _AdGenEth24HrCurrentHCTotalPktsQueue6_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue6.setStatus("current")
_AdGenEth24HrCurrentHCTotalPktsQueue7_Type = Counter64
_AdGenEth24HrCurrentHCTotalPktsQueue7_Object = MibTableColumn
adGenEth24HrCurrentHCTotalPktsQueue7 = _AdGenEth24HrCurrentHCTotalPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 16),
    _AdGenEth24HrCurrentHCTotalPktsQueue7_Type()
)
adGenEth24HrCurrentHCTotalPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCTotalPktsQueue7.setStatus("current")
_AdGenEth24HrCurrentHCOutLcv_Type = Counter64
_AdGenEth24HrCurrentHCOutLcv_Object = MibTableColumn
adGenEth24HrCurrentHCOutLcv = _AdGenEth24HrCurrentHCOutLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 17),
    _AdGenEth24HrCurrentHCOutLcv_Type()
)
adGenEth24HrCurrentHCOutLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCOutLcv.setStatus("current")
_AdGenEth24HrCurrentHCInLcv_Type = Counter64
_AdGenEth24HrCurrentHCInLcv_Object = MibTableColumn
adGenEth24HrCurrentHCInLcv = _AdGenEth24HrCurrentHCInLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 18),
    _AdGenEth24HrCurrentHCInLcv_Type()
)
adGenEth24HrCurrentHCInLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCInLcv.setStatus("current")
_AdGenEth24HrCurrentHCInAvgBitsPerSec_Type = Counter64
_AdGenEth24HrCurrentHCInAvgBitsPerSec_Object = MibTableColumn
adGenEth24HrCurrentHCInAvgBitsPerSec = _AdGenEth24HrCurrentHCInAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 19),
    _AdGenEth24HrCurrentHCInAvgBitsPerSec_Type()
)
adGenEth24HrCurrentHCInAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCInAvgBitsPerSec.setStatus("current")
_AdGenEth24HrCurrentHCInAvgPktsPerSec_Type = Counter64
_AdGenEth24HrCurrentHCInAvgPktsPerSec_Object = MibTableColumn
adGenEth24HrCurrentHCInAvgPktsPerSec = _AdGenEth24HrCurrentHCInAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 20),
    _AdGenEth24HrCurrentHCInAvgPktsPerSec_Type()
)
adGenEth24HrCurrentHCInAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCInAvgPktsPerSec.setStatus("current")
_AdGenEth24HrCurrentHCOutAvgBitsPerSec_Type = Counter64
_AdGenEth24HrCurrentHCOutAvgBitsPerSec_Object = MibTableColumn
adGenEth24HrCurrentHCOutAvgBitsPerSec = _AdGenEth24HrCurrentHCOutAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 21),
    _AdGenEth24HrCurrentHCOutAvgBitsPerSec_Type()
)
adGenEth24HrCurrentHCOutAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCOutAvgBitsPerSec.setStatus("current")
_AdGenEth24HrCurrentHCOutAvgPktsPerSec_Type = Counter64
_AdGenEth24HrCurrentHCOutAvgPktsPerSec_Object = MibTableColumn
adGenEth24HrCurrentHCOutAvgPktsPerSec = _AdGenEth24HrCurrentHCOutAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 7, 1, 22),
    _AdGenEth24HrCurrentHCOutAvgPktsPerSec_Type()
)
adGenEth24HrCurrentHCOutAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrCurrentHCOutAvgPktsPerSec.setStatus("current")
_AdGenEth24HrIntervalTable_Object = MibTable
adGenEth24HrIntervalTable = _AdGenEth24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8)
)
if mibBuilder.loadTexts:
    adGenEth24HrIntervalTable.setStatus("current")
_AdGenEth24HrIntervalEntry_Object = MibTableRow
adGenEth24HrIntervalEntry = _AdGenEth24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1)
)
adGenEth24HrIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-ETH-IFC-MIB", "adGenEth24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenEth24HrIntervalEntry.setStatus("current")
_AdGenEth24HrIntervalNumber_Type = Integer32
_AdGenEth24HrIntervalNumber_Object = MibTableColumn
adGenEth24HrIntervalNumber = _AdGenEth24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 1),
    _AdGenEth24HrIntervalNumber_Type()
)
adGenEth24HrIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalNumber.setStatus("current")
_AdGenEth24HrIntervalOutOctets_Type = Gauge32
_AdGenEth24HrIntervalOutOctets_Object = MibTableColumn
adGenEth24HrIntervalOutOctets = _AdGenEth24HrIntervalOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 2),
    _AdGenEth24HrIntervalOutOctets_Type()
)
adGenEth24HrIntervalOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutOctets.setStatus("current")
_AdGenEth24HrIntervalOutPkts_Type = Gauge32
_AdGenEth24HrIntervalOutPkts_Object = MibTableColumn
adGenEth24HrIntervalOutPkts = _AdGenEth24HrIntervalOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 3),
    _AdGenEth24HrIntervalOutPkts_Type()
)
adGenEth24HrIntervalOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutPkts.setStatus("current")
_AdGenEth24HrIntervalInOctets_Type = Gauge32
_AdGenEth24HrIntervalInOctets_Object = MibTableColumn
adGenEth24HrIntervalInOctets = _AdGenEth24HrIntervalInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 4),
    _AdGenEth24HrIntervalInOctets_Type()
)
adGenEth24HrIntervalInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInOctets.setStatus("current")
_AdGenEth24HrIntervalInPkts_Type = Gauge32
_AdGenEth24HrIntervalInPkts_Object = MibTableColumn
adGenEth24HrIntervalInPkts = _AdGenEth24HrIntervalInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 5),
    _AdGenEth24HrIntervalInPkts_Type()
)
adGenEth24HrIntervalInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInPkts.setStatus("current")
_AdGenEth24HrIntervalInGoodOctets_Type = Gauge32
_AdGenEth24HrIntervalInGoodOctets_Object = MibTableColumn
adGenEth24HrIntervalInGoodOctets = _AdGenEth24HrIntervalInGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 6),
    _AdGenEth24HrIntervalInGoodOctets_Type()
)
adGenEth24HrIntervalInGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInGoodOctets.setStatus("current")
_AdGenEth24HrIntervalInGoodPkts_Type = Gauge32
_AdGenEth24HrIntervalInGoodPkts_Object = MibTableColumn
adGenEth24HrIntervalInGoodPkts = _AdGenEth24HrIntervalInGoodPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 7),
    _AdGenEth24HrIntervalInGoodPkts_Type()
)
adGenEth24HrIntervalInGoodPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInGoodPkts.setStatus("current")
_AdGenEth24HrIntervalInErrors_Type = Gauge32
_AdGenEth24HrIntervalInErrors_Object = MibTableColumn
adGenEth24HrIntervalInErrors = _AdGenEth24HrIntervalInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 8),
    _AdGenEth24HrIntervalInErrors_Type()
)
adGenEth24HrIntervalInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInErrors.setStatus("current")
_AdGenEth24HrIntervalInDiscards_Type = Gauge32
_AdGenEth24HrIntervalInDiscards_Object = MibTableColumn
adGenEth24HrIntervalInDiscards = _AdGenEth24HrIntervalInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 9),
    _AdGenEth24HrIntervalInDiscards_Type()
)
adGenEth24HrIntervalInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInDiscards.setStatus("current")
_AdGenEth24HrIntervalInGiants_Type = Gauge32
_AdGenEth24HrIntervalInGiants_Object = MibTableColumn
adGenEth24HrIntervalInGiants = _AdGenEth24HrIntervalInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 10),
    _AdGenEth24HrIntervalInGiants_Type()
)
adGenEth24HrIntervalInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInGiants.setStatus("current")
_AdGenEth24HrIntervalInRunts_Type = Gauge32
_AdGenEth24HrIntervalInRunts_Object = MibTableColumn
adGenEth24HrIntervalInRunts = _AdGenEth24HrIntervalInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 11),
    _AdGenEth24HrIntervalInRunts_Type()
)
adGenEth24HrIntervalInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInRunts.setStatus("current")
_AdGenEth24HrIntervalInMulticastPkts_Type = Gauge32
_AdGenEth24HrIntervalInMulticastPkts_Object = MibTableColumn
adGenEth24HrIntervalInMulticastPkts = _AdGenEth24HrIntervalInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 12),
    _AdGenEth24HrIntervalInMulticastPkts_Type()
)
adGenEth24HrIntervalInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInMulticastPkts.setStatus("current")
_AdGenEth24HrIntervalInBroadcastPkts_Type = Gauge32
_AdGenEth24HrIntervalInBroadcastPkts_Object = MibTableColumn
adGenEth24HrIntervalInBroadcastPkts = _AdGenEth24HrIntervalInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 13),
    _AdGenEth24HrIntervalInBroadcastPkts_Type()
)
adGenEth24HrIntervalInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInBroadcastPkts.setStatus("current")
_AdGenEth24HrIntervalInUnicastPkts_Type = Gauge32
_AdGenEth24HrIntervalInUnicastPkts_Object = MibTableColumn
adGenEth24HrIntervalInUnicastPkts = _AdGenEth24HrIntervalInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 14),
    _AdGenEth24HrIntervalInUnicastPkts_Type()
)
adGenEth24HrIntervalInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInUnicastPkts.setStatus("current")
_AdGenEth24HrIntervalOutMulticastPkts_Type = Gauge32
_AdGenEth24HrIntervalOutMulticastPkts_Object = MibTableColumn
adGenEth24HrIntervalOutMulticastPkts = _AdGenEth24HrIntervalOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 15),
    _AdGenEth24HrIntervalOutMulticastPkts_Type()
)
adGenEth24HrIntervalOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutMulticastPkts.setStatus("current")
_AdGenEth24HrIntervalOutBroadcastPkts_Type = Gauge32
_AdGenEth24HrIntervalOutBroadcastPkts_Object = MibTableColumn
adGenEth24HrIntervalOutBroadcastPkts = _AdGenEth24HrIntervalOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 16),
    _AdGenEth24HrIntervalOutBroadcastPkts_Type()
)
adGenEth24HrIntervalOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutBroadcastPkts.setStatus("current")
_AdGenEth24HrIntervalOutUnicastPkts_Type = Gauge32
_AdGenEth24HrIntervalOutUnicastPkts_Object = MibTableColumn
adGenEth24HrIntervalOutUnicastPkts = _AdGenEth24HrIntervalOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 17),
    _AdGenEth24HrIntervalOutUnicastPkts_Type()
)
adGenEth24HrIntervalOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutUnicastPkts.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue0_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue0_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue0 = _AdGenEth24HrIntervalDroppedPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 18),
    _AdGenEth24HrIntervalDroppedPktsQueue0_Type()
)
adGenEth24HrIntervalDroppedPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue0.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue1_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue1_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue1 = _AdGenEth24HrIntervalDroppedPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 19),
    _AdGenEth24HrIntervalDroppedPktsQueue1_Type()
)
adGenEth24HrIntervalDroppedPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue1.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue2_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue2_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue2 = _AdGenEth24HrIntervalDroppedPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 20),
    _AdGenEth24HrIntervalDroppedPktsQueue2_Type()
)
adGenEth24HrIntervalDroppedPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue2.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue3_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue3_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue3 = _AdGenEth24HrIntervalDroppedPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 21),
    _AdGenEth24HrIntervalDroppedPktsQueue3_Type()
)
adGenEth24HrIntervalDroppedPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue3.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue4_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue4_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue4 = _AdGenEth24HrIntervalDroppedPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 22),
    _AdGenEth24HrIntervalDroppedPktsQueue4_Type()
)
adGenEth24HrIntervalDroppedPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue4.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue5_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue5_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue5 = _AdGenEth24HrIntervalDroppedPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 23),
    _AdGenEth24HrIntervalDroppedPktsQueue5_Type()
)
adGenEth24HrIntervalDroppedPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue5.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue6_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue6_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue6 = _AdGenEth24HrIntervalDroppedPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 24),
    _AdGenEth24HrIntervalDroppedPktsQueue6_Type()
)
adGenEth24HrIntervalDroppedPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue6.setStatus("current")
_AdGenEth24HrIntervalDroppedPktsQueue7_Type = Gauge32
_AdGenEth24HrIntervalDroppedPktsQueue7_Object = MibTableColumn
adGenEth24HrIntervalDroppedPktsQueue7 = _AdGenEth24HrIntervalDroppedPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 25),
    _AdGenEth24HrIntervalDroppedPktsQueue7_Type()
)
adGenEth24HrIntervalDroppedPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalDroppedPktsQueue7.setStatus("current")
_AdGenEth24HrIntervalOutDiscards_Type = Gauge32
_AdGenEth24HrIntervalOutDiscards_Object = MibTableColumn
adGenEth24HrIntervalOutDiscards = _AdGenEth24HrIntervalOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 26),
    _AdGenEth24HrIntervalOutDiscards_Type()
)
adGenEth24HrIntervalOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutDiscards.setStatus("current")
_AdGenEth24HrIntervalInCRCErrors_Type = Gauge32
_AdGenEth24HrIntervalInCRCErrors_Object = MibTableColumn
adGenEth24HrIntervalInCRCErrors = _AdGenEth24HrIntervalInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 27),
    _AdGenEth24HrIntervalInCRCErrors_Type()
)
adGenEth24HrIntervalInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInCRCErrors.setStatus("current")
_AdGenEth24HrIntervalInFrameErrors_Type = Gauge32
_AdGenEth24HrIntervalInFrameErrors_Object = MibTableColumn
adGenEth24HrIntervalInFrameErrors = _AdGenEth24HrIntervalInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 28),
    _AdGenEth24HrIntervalInFrameErrors_Type()
)
adGenEth24HrIntervalInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInFrameErrors.setStatus("current")
_AdGenEth24HrIntervalOutErrors_Type = Gauge32
_AdGenEth24HrIntervalOutErrors_Object = MibTableColumn
adGenEth24HrIntervalOutErrors = _AdGenEth24HrIntervalOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 29),
    _AdGenEth24HrIntervalOutErrors_Type()
)
adGenEth24HrIntervalOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutErrors.setStatus("current")
_AdGenEth24HrIntervalInPeakUtilization_Type = Gauge32
_AdGenEth24HrIntervalInPeakUtilization_Object = MibTableColumn
adGenEth24HrIntervalInPeakUtilization = _AdGenEth24HrIntervalInPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 30),
    _AdGenEth24HrIntervalInPeakUtilization_Type()
)
adGenEth24HrIntervalInPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInPeakUtilization.setStatus("current")
_AdGenEth24HrIntervalInAvgUtilization_Type = Gauge32
_AdGenEth24HrIntervalInAvgUtilization_Object = MibTableColumn
adGenEth24HrIntervalInAvgUtilization = _AdGenEth24HrIntervalInAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 31),
    _AdGenEth24HrIntervalInAvgUtilization_Type()
)
adGenEth24HrIntervalInAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalInAvgUtilization.setStatus("current")
_AdGenEth24HrIntervalOutPeakUtilization_Type = Gauge32
_AdGenEth24HrIntervalOutPeakUtilization_Object = MibTableColumn
adGenEth24HrIntervalOutPeakUtilization = _AdGenEth24HrIntervalOutPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 32),
    _AdGenEth24HrIntervalOutPeakUtilization_Type()
)
adGenEth24HrIntervalOutPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutPeakUtilization.setStatus("current")
_AdGenEth24HrIntervalOutAvgUtilization_Type = Gauge32
_AdGenEth24HrIntervalOutAvgUtilization_Object = MibTableColumn
adGenEth24HrIntervalOutAvgUtilization = _AdGenEth24HrIntervalOutAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 8, 1, 33),
    _AdGenEth24HrIntervalOutAvgUtilization_Type()
)
adGenEth24HrIntervalOutAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalOutAvgUtilization.setStatus("current")
_AdGenEth24HrIntervalHCTable_Object = MibTable
adGenEth24HrIntervalHCTable = _AdGenEth24HrIntervalHCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9)
)
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTable.setStatus("current")
_AdGenEth24HrIntervalHCEntry_Object = MibTableRow
adGenEth24HrIntervalHCEntry = _AdGenEth24HrIntervalHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1)
)
adGenEth24HrIntervalHCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-ETH-IFC-MIB", "adGenEth24HrIntervalHCNumber"),
)
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCEntry.setStatus("current")
_AdGenEth24HrIntervalHCNumber_Type = Integer32
_AdGenEth24HrIntervalHCNumber_Object = MibTableColumn
adGenEth24HrIntervalHCNumber = _AdGenEth24HrIntervalHCNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 1),
    _AdGenEth24HrIntervalHCNumber_Type()
)
adGenEth24HrIntervalHCNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCNumber.setStatus("current")
_AdGenEth24HrIntervalHCOutOctets_Type = Counter64
_AdGenEth24HrIntervalHCOutOctets_Object = MibTableColumn
adGenEth24HrIntervalHCOutOctets = _AdGenEth24HrIntervalHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 2),
    _AdGenEth24HrIntervalHCOutOctets_Type()
)
adGenEth24HrIntervalHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCOutOctets.setStatus("current")
_AdGenEth24HrIntervalHCInOctets_Type = Counter64
_AdGenEth24HrIntervalHCInOctets_Object = MibTableColumn
adGenEth24HrIntervalHCInOctets = _AdGenEth24HrIntervalHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 3),
    _AdGenEth24HrIntervalHCInOctets_Type()
)
adGenEth24HrIntervalHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCInOctets.setStatus("current")
_AdGenEth24HrIntervalHCInMulticastPkts_Type = Counter64
_AdGenEth24HrIntervalHCInMulticastPkts_Object = MibTableColumn
adGenEth24HrIntervalHCInMulticastPkts = _AdGenEth24HrIntervalHCInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 4),
    _AdGenEth24HrIntervalHCInMulticastPkts_Type()
)
adGenEth24HrIntervalHCInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCInMulticastPkts.setStatus("current")
_AdGenEth24HrIntervalHCInBroadcastPkts_Type = Counter64
_AdGenEth24HrIntervalHCInBroadcastPkts_Object = MibTableColumn
adGenEth24HrIntervalHCInBroadcastPkts = _AdGenEth24HrIntervalHCInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 5),
    _AdGenEth24HrIntervalHCInBroadcastPkts_Type()
)
adGenEth24HrIntervalHCInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCInBroadcastPkts.setStatus("current")
_AdGenEth24HrIntervalHCInUnicastPkts_Type = Counter64
_AdGenEth24HrIntervalHCInUnicastPkts_Object = MibTableColumn
adGenEth24HrIntervalHCInUnicastPkts = _AdGenEth24HrIntervalHCInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 6),
    _AdGenEth24HrIntervalHCInUnicastPkts_Type()
)
adGenEth24HrIntervalHCInUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCInUnicastPkts.setStatus("current")
_AdGenEth24HrIntervalHCOutMulticastPkts_Type = Counter64
_AdGenEth24HrIntervalHCOutMulticastPkts_Object = MibTableColumn
adGenEth24HrIntervalHCOutMulticastPkts = _AdGenEth24HrIntervalHCOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 7),
    _AdGenEth24HrIntervalHCOutMulticastPkts_Type()
)
adGenEth24HrIntervalHCOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCOutMulticastPkts.setStatus("current")
_AdGenEth24HrIntervalHCOutBroadcastPkts_Type = Counter64
_AdGenEth24HrIntervalHCOutBroadcastPkts_Object = MibTableColumn
adGenEth24HrIntervalHCOutBroadcastPkts = _AdGenEth24HrIntervalHCOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 8),
    _AdGenEth24HrIntervalHCOutBroadcastPkts_Type()
)
adGenEth24HrIntervalHCOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCOutBroadcastPkts.setStatus("current")
_AdGenEth24HrIntervalHCOutUnicastPkts_Type = Counter64
_AdGenEth24HrIntervalHCOutUnicastPkts_Object = MibTableColumn
adGenEth24HrIntervalHCOutUnicastPkts = _AdGenEth24HrIntervalHCOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 9),
    _AdGenEth24HrIntervalHCOutUnicastPkts_Type()
)
adGenEth24HrIntervalHCOutUnicastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCOutUnicastPkts.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue0_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue0_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue0 = _AdGenEth24HrIntervalHCTotalPktsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 10),
    _AdGenEth24HrIntervalHCTotalPktsQueue0_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue0.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue1_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue1_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue1 = _AdGenEth24HrIntervalHCTotalPktsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 11),
    _AdGenEth24HrIntervalHCTotalPktsQueue1_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue1.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue2_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue2_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue2 = _AdGenEth24HrIntervalHCTotalPktsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 12),
    _AdGenEth24HrIntervalHCTotalPktsQueue2_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue2.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue3_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue3_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue3 = _AdGenEth24HrIntervalHCTotalPktsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 13),
    _AdGenEth24HrIntervalHCTotalPktsQueue3_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue3.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue4_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue4_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue4 = _AdGenEth24HrIntervalHCTotalPktsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 14),
    _AdGenEth24HrIntervalHCTotalPktsQueue4_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue4.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue5_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue5_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue5 = _AdGenEth24HrIntervalHCTotalPktsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 15),
    _AdGenEth24HrIntervalHCTotalPktsQueue5_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue5.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue6_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue6_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue6 = _AdGenEth24HrIntervalHCTotalPktsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 16),
    _AdGenEth24HrIntervalHCTotalPktsQueue6_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue6.setStatus("current")
_AdGenEth24HrIntervalHCTotalPktsQueue7_Type = Counter64
_AdGenEth24HrIntervalHCTotalPktsQueue7_Object = MibTableColumn
adGenEth24HrIntervalHCTotalPktsQueue7 = _AdGenEth24HrIntervalHCTotalPktsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 17),
    _AdGenEth24HrIntervalHCTotalPktsQueue7_Type()
)
adGenEth24HrIntervalHCTotalPktsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCTotalPktsQueue7.setStatus("current")
_AdGenEth24HrIntervalHCOutLcv_Type = Counter64
_AdGenEth24HrIntervalHCOutLcv_Object = MibTableColumn
adGenEth24HrIntervalHCOutLcv = _AdGenEth24HrIntervalHCOutLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 18),
    _AdGenEth24HrIntervalHCOutLcv_Type()
)
adGenEth24HrIntervalHCOutLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCOutLcv.setStatus("current")
_AdGenEth24HrIntervalHCInLcv_Type = Counter64
_AdGenEth24HrIntervalHCInLcv_Object = MibTableColumn
adGenEth24HrIntervalHCInLcv = _AdGenEth24HrIntervalHCInLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 19),
    _AdGenEth24HrIntervalHCInLcv_Type()
)
adGenEth24HrIntervalHCInLcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCInLcv.setStatus("current")
_AdGenEth24HrIntervalHCValidData_Type = TruthValue
_AdGenEth24HrIntervalHCValidData_Object = MibTableColumn
adGenEth24HrIntervalHCValidData = _AdGenEth24HrIntervalHCValidData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 20),
    _AdGenEth24HrIntervalHCValidData_Type()
)
adGenEth24HrIntervalHCValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCValidData.setStatus("current")
_AdGenEth24HrIntervalHCInAvgBitsPerSec_Type = Counter64
_AdGenEth24HrIntervalHCInAvgBitsPerSec_Object = MibTableColumn
adGenEth24HrIntervalHCInAvgBitsPerSec = _AdGenEth24HrIntervalHCInAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 21),
    _AdGenEth24HrIntervalHCInAvgBitsPerSec_Type()
)
adGenEth24HrIntervalHCInAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCInAvgBitsPerSec.setStatus("current")
_AdGenEth24HrIntervalHCInAvgPktsPerSec_Type = Counter64
_AdGenEth24HrIntervalHCInAvgPktsPerSec_Object = MibTableColumn
adGenEth24HrIntervalHCInAvgPktsPerSec = _AdGenEth24HrIntervalHCInAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 22),
    _AdGenEth24HrIntervalHCInAvgPktsPerSec_Type()
)
adGenEth24HrIntervalHCInAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCInAvgPktsPerSec.setStatus("current")
_AdGenEth24HrIntervalHCOutAvgBitsPerSec_Type = Counter64
_AdGenEth24HrIntervalHCOutAvgBitsPerSec_Object = MibTableColumn
adGenEth24HrIntervalHCOutAvgBitsPerSec = _AdGenEth24HrIntervalHCOutAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 23),
    _AdGenEth24HrIntervalHCOutAvgBitsPerSec_Type()
)
adGenEth24HrIntervalHCOutAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCOutAvgBitsPerSec.setStatus("current")
_AdGenEth24HrIntervalHCOutAvgPktsPerSec_Type = Counter64
_AdGenEth24HrIntervalHCOutAvgPktsPerSec_Object = MibTableColumn
adGenEth24HrIntervalHCOutAvgPktsPerSec = _AdGenEth24HrIntervalHCOutAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 9, 1, 24),
    _AdGenEth24HrIntervalHCOutAvgPktsPerSec_Type()
)
adGenEth24HrIntervalHCOutAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEth24HrIntervalHCOutAvgPktsPerSec.setStatus("current")
_AdGenEthPerfResetTable_Object = MibTable
adGenEthPerfResetTable = _AdGenEthPerfResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 10)
)
if mibBuilder.loadTexts:
    adGenEthPerfResetTable.setStatus("current")
_AdGenEthPerfResetEntry_Object = MibTableRow
adGenEthPerfResetEntry = _AdGenEthPerfResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 10, 1)
)
adGenEthPerfResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthPerfResetEntry.setStatus("current")


class _AdGenEthPerfReset_Type(Integer32):
    """Custom type adGenEthPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethPerfRst", 1)
    )


_AdGenEthPerfReset_Type.__name__ = "Integer32"
_AdGenEthPerfReset_Object = MibTableColumn
adGenEthPerfReset = _AdGenEthPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 10, 1, 1),
    _AdGenEthPerfReset_Type()
)
adGenEthPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthPerfReset.setStatus("current")
_AdGenEthPerfThresholds_ObjectIdentity = ObjectIdentity
adGenEthPerfThresholds = _AdGenEthPerfThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11)
)
_AdGenEth15MinThreshTable_Object = MibTable
adGenEth15MinThreshTable = _AdGenEth15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1)
)
if mibBuilder.loadTexts:
    adGenEth15MinThreshTable.setStatus("current")
_AdGenEth15MinThreshEntry_Object = MibTableRow
adGenEth15MinThreshEntry = _AdGenEth15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1)
)
adGenEth15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEth15MinThreshEntry.setStatus("current")
_AdGenEth15MinThreshInErrors_Type = Unsigned32
_AdGenEth15MinThreshInErrors_Object = MibTableColumn
adGenEth15MinThreshInErrors = _AdGenEth15MinThreshInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 1),
    _AdGenEth15MinThreshInErrors_Type()
)
adGenEth15MinThreshInErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInErrors.setStatus("current")
_AdGenEth15MinThreshInDiscards_Type = Unsigned32
_AdGenEth15MinThreshInDiscards_Object = MibTableColumn
adGenEth15MinThreshInDiscards = _AdGenEth15MinThreshInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 2),
    _AdGenEth15MinThreshInDiscards_Type()
)
adGenEth15MinThreshInDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInDiscards.setStatus("current")
_AdGenEth15MinThreshInGiants_Type = Unsigned32
_AdGenEth15MinThreshInGiants_Object = MibTableColumn
adGenEth15MinThreshInGiants = _AdGenEth15MinThreshInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 3),
    _AdGenEth15MinThreshInGiants_Type()
)
adGenEth15MinThreshInGiants.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInGiants.setStatus("current")
_AdGenEth15MinThreshInRunts_Type = Unsigned32
_AdGenEth15MinThreshInRunts_Object = MibTableColumn
adGenEth15MinThreshInRunts = _AdGenEth15MinThreshInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 4),
    _AdGenEth15MinThreshInRunts_Type()
)
adGenEth15MinThreshInRunts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInRunts.setStatus("current")
_AdGenEth15MinThreshInMulticastPkts_Type = Unsigned32
_AdGenEth15MinThreshInMulticastPkts_Object = MibTableColumn
adGenEth15MinThreshInMulticastPkts = _AdGenEth15MinThreshInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 5),
    _AdGenEth15MinThreshInMulticastPkts_Type()
)
adGenEth15MinThreshInMulticastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInMulticastPkts.setStatus("current")
_AdGenEth15MinThreshInBroadcastPkts_Type = Unsigned32
_AdGenEth15MinThreshInBroadcastPkts_Object = MibTableColumn
adGenEth15MinThreshInBroadcastPkts = _AdGenEth15MinThreshInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 6),
    _AdGenEth15MinThreshInBroadcastPkts_Type()
)
adGenEth15MinThreshInBroadcastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInBroadcastPkts.setStatus("current")
_AdGenEth15MinThreshInUnicastPkts_Type = Unsigned32
_AdGenEth15MinThreshInUnicastPkts_Object = MibTableColumn
adGenEth15MinThreshInUnicastPkts = _AdGenEth15MinThreshInUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 7),
    _AdGenEth15MinThreshInUnicastPkts_Type()
)
adGenEth15MinThreshInUnicastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInUnicastPkts.setStatus("current")
_AdGenEth15MinThreshInUnknownProtocols_Type = Unsigned32
_AdGenEth15MinThreshInUnknownProtocols_Object = MibTableColumn
adGenEth15MinThreshInUnknownProtocols = _AdGenEth15MinThreshInUnknownProtocols_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 8),
    _AdGenEth15MinThreshInUnknownProtocols_Type()
)
adGenEth15MinThreshInUnknownProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInUnknownProtocols.setStatus("current")
_AdGenEth15MinThreshInOctets_Type = Unsigned64TC
_AdGenEth15MinThreshInOctets_Object = MibTableColumn
adGenEth15MinThreshInOctets = _AdGenEth15MinThreshInOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 9),
    _AdGenEth15MinThreshInOctets_Type()
)
adGenEth15MinThreshInOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInOctets.setStatus("current")
_AdGenEth15MinThreshInPkts_Type = Unsigned32
_AdGenEth15MinThreshInPkts_Object = MibTableColumn
adGenEth15MinThreshInPkts = _AdGenEth15MinThreshInPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 10),
    _AdGenEth15MinThreshInPkts_Type()
)
adGenEth15MinThreshInPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInPkts.setStatus("current")
_AdGenEth15MinThreshInPkts64Octets_Type = Unsigned32
_AdGenEth15MinThreshInPkts64Octets_Object = MibTableColumn
adGenEth15MinThreshInPkts64Octets = _AdGenEth15MinThreshInPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 11),
    _AdGenEth15MinThreshInPkts64Octets_Type()
)
adGenEth15MinThreshInPkts64Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInPkts64Octets.setStatus("current")
_AdGenEth15MinThreshInPkts65to127Octets_Type = Unsigned32
_AdGenEth15MinThreshInPkts65to127Octets_Object = MibTableColumn
adGenEth15MinThreshInPkts65to127Octets = _AdGenEth15MinThreshInPkts65to127Octets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 12),
    _AdGenEth15MinThreshInPkts65to127Octets_Type()
)
adGenEth15MinThreshInPkts65to127Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInPkts65to127Octets.setStatus("current")
_AdGenEth15MinThreshInPkts128to255Octets_Type = Unsigned32
_AdGenEth15MinThreshInPkts128to255Octets_Object = MibTableColumn
adGenEth15MinThreshInPkts128to255Octets = _AdGenEth15MinThreshInPkts128to255Octets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 13),
    _AdGenEth15MinThreshInPkts128to255Octets_Type()
)
adGenEth15MinThreshInPkts128to255Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInPkts128to255Octets.setStatus("current")
_AdGenEth15MinThreshInPkts256to511Octets_Type = Unsigned32
_AdGenEth15MinThreshInPkts256to511Octets_Object = MibTableColumn
adGenEth15MinThreshInPkts256to511Octets = _AdGenEth15MinThreshInPkts256to511Octets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 14),
    _AdGenEth15MinThreshInPkts256to511Octets_Type()
)
adGenEth15MinThreshInPkts256to511Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInPkts256to511Octets.setStatus("current")
_AdGenEth15MinThreshInPkts512to1023Octets_Type = Unsigned32
_AdGenEth15MinThreshInPkts512to1023Octets_Object = MibTableColumn
adGenEth15MinThreshInPkts512to1023Octets = _AdGenEth15MinThreshInPkts512to1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 15),
    _AdGenEth15MinThreshInPkts512to1023Octets_Type()
)
adGenEth15MinThreshInPkts512to1023Octets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInPkts512to1023Octets.setStatus("current")
_AdGenEth15MinThreshInPkts1024toMaxOctets_Type = Unsigned32
_AdGenEth15MinThreshInPkts1024toMaxOctets_Object = MibTableColumn
adGenEth15MinThreshInPkts1024toMaxOctets = _AdGenEth15MinThreshInPkts1024toMaxOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 16),
    _AdGenEth15MinThreshInPkts1024toMaxOctets_Type()
)
adGenEth15MinThreshInPkts1024toMaxOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInPkts1024toMaxOctets.setStatus("current")
_AdGenEth15MinThreshOutErrors_Type = Unsigned32
_AdGenEth15MinThreshOutErrors_Object = MibTableColumn
adGenEth15MinThreshOutErrors = _AdGenEth15MinThreshOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 17),
    _AdGenEth15MinThreshOutErrors_Type()
)
adGenEth15MinThreshOutErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutErrors.setStatus("current")
_AdGenEth15MinThreshOutDiscards_Type = Unsigned32
_AdGenEth15MinThreshOutDiscards_Object = MibTableColumn
adGenEth15MinThreshOutDiscards = _AdGenEth15MinThreshOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 18),
    _AdGenEth15MinThreshOutDiscards_Type()
)
adGenEth15MinThreshOutDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutDiscards.setStatus("current")
_AdGenEth15MinThreshOutMulticastPkts_Type = Unsigned32
_AdGenEth15MinThreshOutMulticastPkts_Object = MibTableColumn
adGenEth15MinThreshOutMulticastPkts = _AdGenEth15MinThreshOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 19),
    _AdGenEth15MinThreshOutMulticastPkts_Type()
)
adGenEth15MinThreshOutMulticastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutMulticastPkts.setStatus("current")
_AdGenEth15MinThreshOutBroadcastPkts_Type = Unsigned32
_AdGenEth15MinThreshOutBroadcastPkts_Object = MibTableColumn
adGenEth15MinThreshOutBroadcastPkts = _AdGenEth15MinThreshOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 20),
    _AdGenEth15MinThreshOutBroadcastPkts_Type()
)
adGenEth15MinThreshOutBroadcastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutBroadcastPkts.setStatus("current")
_AdGenEth15MinThreshOutUnicastPkts_Type = Unsigned32
_AdGenEth15MinThreshOutUnicastPkts_Object = MibTableColumn
adGenEth15MinThreshOutUnicastPkts = _AdGenEth15MinThreshOutUnicastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 21),
    _AdGenEth15MinThreshOutUnicastPkts_Type()
)
adGenEth15MinThreshOutUnicastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutUnicastPkts.setStatus("current")
_AdGenEth15MinThreshOutOctets_Type = Unsigned64TC
_AdGenEth15MinThreshOutOctets_Object = MibTableColumn
adGenEth15MinThreshOutOctets = _AdGenEth15MinThreshOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 22),
    _AdGenEth15MinThreshOutOctets_Type()
)
adGenEth15MinThreshOutOctets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutOctets.setStatus("current")
_AdGenEth15MinThreshOutPkts_Type = Unsigned32
_AdGenEth15MinThreshOutPkts_Object = MibTableColumn
adGenEth15MinThreshOutPkts = _AdGenEth15MinThreshOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 23),
    _AdGenEth15MinThreshOutPkts_Type()
)
adGenEth15MinThreshOutPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutPkts.setStatus("current")
_AdGenEth15MinThreshES_Type = Unsigned32
_AdGenEth15MinThreshES_Object = MibTableColumn
adGenEth15MinThreshES = _AdGenEth15MinThreshES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 24),
    _AdGenEth15MinThreshES_Type()
)
adGenEth15MinThreshES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshES.setStatus("current")
_AdGenEth15MinThreshLOSS_Type = Unsigned32
_AdGenEth15MinThreshLOSS_Object = MibTableColumn
adGenEth15MinThreshLOSS = _AdGenEth15MinThreshLOSS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 25),
    _AdGenEth15MinThreshLOSS_Type()
)
adGenEth15MinThreshLOSS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshLOSS.setStatus("current")
_AdGenEth15MinThreshSEFS_Type = Unsigned32
_AdGenEth15MinThreshSEFS_Object = MibTableColumn
adGenEth15MinThreshSEFS = _AdGenEth15MinThreshSEFS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 26),
    _AdGenEth15MinThreshSEFS_Type()
)
adGenEth15MinThreshSEFS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshSEFS.setStatus("current")
_AdGenEth15MinThreshSES_Type = Unsigned32
_AdGenEth15MinThreshSES_Object = MibTableColumn
adGenEth15MinThreshSES = _AdGenEth15MinThreshSES_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 27),
    _AdGenEth15MinThreshSES_Type()
)
adGenEth15MinThreshSES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshSES.setStatus("current")
_AdGenEth15MinThreshUAS_Type = Unsigned32
_AdGenEth15MinThreshUAS_Object = MibTableColumn
adGenEth15MinThreshUAS = _AdGenEth15MinThreshUAS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 28),
    _AdGenEth15MinThreshUAS_Type()
)
adGenEth15MinThreshUAS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshUAS.setStatus("current")
_AdGenEth15MinThreshOutLcv_Type = Unsigned64TC
_AdGenEth15MinThreshOutLcv_Object = MibTableColumn
adGenEth15MinThreshOutLcv = _AdGenEth15MinThreshOutLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 29),
    _AdGenEth15MinThreshOutLcv_Type()
)
adGenEth15MinThreshOutLcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshOutLcv.setStatus("current")
_AdGenEth15MinThreshInLcv_Type = Unsigned64TC
_AdGenEth15MinThreshInLcv_Object = MibTableColumn
adGenEth15MinThreshInLcv = _AdGenEth15MinThreshInLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 1, 1, 30),
    _AdGenEth15MinThreshInLcv_Type()
)
adGenEth15MinThreshInLcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth15MinThreshInLcv.setStatus("current")
_AdGenEth24HrThreshTable_Object = MibTable
adGenEth24HrThreshTable = _AdGenEth24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2)
)
if mibBuilder.loadTexts:
    adGenEth24HrThreshTable.setStatus("current")
_AdGenEth24HrThreshEntry_Object = MibTableRow
adGenEth24HrThreshEntry = _AdGenEth24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1)
)
adGenEth24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEth24HrThreshEntry.setStatus("current")
_AdGenEth24HrThreshInErrors_Type = Unsigned32
_AdGenEth24HrThreshInErrors_Object = MibTableColumn
adGenEth24HrThreshInErrors = _AdGenEth24HrThreshInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 1),
    _AdGenEth24HrThreshInErrors_Type()
)
adGenEth24HrThreshInErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshInErrors.setStatus("current")
_AdGenEth24HrThreshInDiscards_Type = Unsigned32
_AdGenEth24HrThreshInDiscards_Object = MibTableColumn
adGenEth24HrThreshInDiscards = _AdGenEth24HrThreshInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 2),
    _AdGenEth24HrThreshInDiscards_Type()
)
adGenEth24HrThreshInDiscards.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshInDiscards.setStatus("current")
_AdGenEth24HrThreshInGiants_Type = Unsigned32
_AdGenEth24HrThreshInGiants_Object = MibTableColumn
adGenEth24HrThreshInGiants = _AdGenEth24HrThreshInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 3),
    _AdGenEth24HrThreshInGiants_Type()
)
adGenEth24HrThreshInGiants.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshInGiants.setStatus("current")
_AdGenEth24HrThreshInRunts_Type = Unsigned32
_AdGenEth24HrThreshInRunts_Object = MibTableColumn
adGenEth24HrThreshInRunts = _AdGenEth24HrThreshInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 4),
    _AdGenEth24HrThreshInRunts_Type()
)
adGenEth24HrThreshInRunts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshInRunts.setStatus("current")
_AdGenEth24HrThreshInMulticastPkts_Type = Unsigned32
_AdGenEth24HrThreshInMulticastPkts_Object = MibTableColumn
adGenEth24HrThreshInMulticastPkts = _AdGenEth24HrThreshInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 5),
    _AdGenEth24HrThreshInMulticastPkts_Type()
)
adGenEth24HrThreshInMulticastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshInMulticastPkts.setStatus("current")
_AdGenEth24HrThreshInBroadcastPkts_Type = Unsigned32
_AdGenEth24HrThreshInBroadcastPkts_Object = MibTableColumn
adGenEth24HrThreshInBroadcastPkts = _AdGenEth24HrThreshInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 6),
    _AdGenEth24HrThreshInBroadcastPkts_Type()
)
adGenEth24HrThreshInBroadcastPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshInBroadcastPkts.setStatus("current")
_AdGenEth24HrThreshOutLcv_Type = Unsigned64TC
_AdGenEth24HrThreshOutLcv_Object = MibTableColumn
adGenEth24HrThreshOutLcv = _AdGenEth24HrThreshOutLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 7),
    _AdGenEth24HrThreshOutLcv_Type()
)
adGenEth24HrThreshOutLcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshOutLcv.setStatus("current")
_AdGenEth24HrThreshInLcv_Type = Unsigned64TC
_AdGenEth24HrThreshInLcv_Object = MibTableColumn
adGenEth24HrThreshInLcv = _AdGenEth24HrThreshInLcv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 11, 2, 1, 8),
    _AdGenEth24HrThreshInLcv_Type()
)
adGenEth24HrThreshInLcv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEth24HrThreshInLcv.setStatus("current")
_AdGenEthPerformanceCountersTable_Object = MibTable
adGenEthPerformanceCountersTable = _AdGenEthPerformanceCountersTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12)
)
if mibBuilder.loadTexts:
    adGenEthPerformanceCountersTable.setStatus("current")
_AdGenEthPerformanceCountersEntry_Object = MibTableRow
adGenEthPerformanceCountersEntry = _AdGenEthPerformanceCountersEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1)
)
adGenEthPerformanceCountersEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthPerformanceCountersEntry.setStatus("current")
_AdGenEthInPackets_Type = Counter32
_AdGenEthInPackets_Object = MibTableColumn
adGenEthInPackets = _AdGenEthInPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 1),
    _AdGenEthInPackets_Type()
)
adGenEthInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInPackets.setStatus("current")
_AdGenEthOutPackets_Type = Counter32
_AdGenEthOutPackets_Object = MibTableColumn
adGenEthOutPackets = _AdGenEthOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 2),
    _AdGenEthOutPackets_Type()
)
adGenEthOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthOutPackets.setStatus("current")
_AdGenEthInRunts_Type = Counter32
_AdGenEthInRunts_Object = MibTableColumn
adGenEthInRunts = _AdGenEthInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 3),
    _AdGenEthInRunts_Type()
)
adGenEthInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInRunts.setStatus("current")
_AdGenEthInGiants_Type = Counter32
_AdGenEthInGiants_Object = MibTableColumn
adGenEthInGiants = _AdGenEthInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 4),
    _AdGenEthInGiants_Type()
)
adGenEthInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInGiants.setStatus("current")
_AdGenEthInFrameErrors_Type = Counter32
_AdGenEthInFrameErrors_Object = MibTableColumn
adGenEthInFrameErrors = _AdGenEthInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 5),
    _AdGenEthInFrameErrors_Type()
)
adGenEthInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInFrameErrors.setStatus("current")
_AdGenEthInFCSErrors_Type = Counter32
_AdGenEthInFCSErrors_Object = MibTableColumn
adGenEthInFCSErrors = _AdGenEthInFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 6),
    _AdGenEthInFCSErrors_Type()
)
adGenEthInFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInFCSErrors.setStatus("current")
_AdGenEthInAvgPktsPerSec_Type = Counter32
_AdGenEthInAvgPktsPerSec_Object = MibTableColumn
adGenEthInAvgPktsPerSec = _AdGenEthInAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 7),
    _AdGenEthInAvgPktsPerSec_Type()
)
adGenEthInAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInAvgPktsPerSec.setStatus("current")
_AdGenEthOutAvgPktsPerSec_Type = Counter32
_AdGenEthOutAvgPktsPerSec_Object = MibTableColumn
adGenEthOutAvgPktsPerSec = _AdGenEthOutAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 8),
    _AdGenEthOutAvgPktsPerSec_Type()
)
adGenEthOutAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthOutAvgPktsPerSec.setStatus("current")
_AdGenEthInAvgBitsPerSec_Type = Counter32
_AdGenEthInAvgBitsPerSec_Object = MibTableColumn
adGenEthInAvgBitsPerSec = _AdGenEthInAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 9),
    _AdGenEthInAvgBitsPerSec_Type()
)
adGenEthInAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInAvgBitsPerSec.setStatus("current")
_AdGenEthOutAvgBitsPerSec_Type = Counter32
_AdGenEthOutAvgBitsPerSec_Object = MibTableColumn
adGenEthOutAvgBitsPerSec = _AdGenEthOutAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 10),
    _AdGenEthOutAvgBitsPerSec_Type()
)
adGenEthOutAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthOutAvgBitsPerSec.setStatus("current")
_AdGenEthTotalTxPacketsQueue0_Type = Counter64
_AdGenEthTotalTxPacketsQueue0_Object = MibTableColumn
adGenEthTotalTxPacketsQueue0 = _AdGenEthTotalTxPacketsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 11),
    _AdGenEthTotalTxPacketsQueue0_Type()
)
adGenEthTotalTxPacketsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue0.setStatus("current")
_AdGenEthTotalTxPacketsQueue1_Type = Counter64
_AdGenEthTotalTxPacketsQueue1_Object = MibTableColumn
adGenEthTotalTxPacketsQueue1 = _AdGenEthTotalTxPacketsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 12),
    _AdGenEthTotalTxPacketsQueue1_Type()
)
adGenEthTotalTxPacketsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue1.setStatus("current")
_AdGenEthTotalTxPacketsQueue2_Type = Counter64
_AdGenEthTotalTxPacketsQueue2_Object = MibTableColumn
adGenEthTotalTxPacketsQueue2 = _AdGenEthTotalTxPacketsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 13),
    _AdGenEthTotalTxPacketsQueue2_Type()
)
adGenEthTotalTxPacketsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue2.setStatus("current")
_AdGenEthTotalTxPacketsQueue3_Type = Counter64
_AdGenEthTotalTxPacketsQueue3_Object = MibTableColumn
adGenEthTotalTxPacketsQueue3 = _AdGenEthTotalTxPacketsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 14),
    _AdGenEthTotalTxPacketsQueue3_Type()
)
adGenEthTotalTxPacketsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue3.setStatus("current")
_AdGenEthTotalTxPacketsQueue4_Type = Counter64
_AdGenEthTotalTxPacketsQueue4_Object = MibTableColumn
adGenEthTotalTxPacketsQueue4 = _AdGenEthTotalTxPacketsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 15),
    _AdGenEthTotalTxPacketsQueue4_Type()
)
adGenEthTotalTxPacketsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue4.setStatus("current")
_AdGenEthTotalTxPacketsQueue5_Type = Counter64
_AdGenEthTotalTxPacketsQueue5_Object = MibTableColumn
adGenEthTotalTxPacketsQueue5 = _AdGenEthTotalTxPacketsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 16),
    _AdGenEthTotalTxPacketsQueue5_Type()
)
adGenEthTotalTxPacketsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue5.setStatus("current")
_AdGenEthTotalTxPacketsQueue6_Type = Counter64
_AdGenEthTotalTxPacketsQueue6_Object = MibTableColumn
adGenEthTotalTxPacketsQueue6 = _AdGenEthTotalTxPacketsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 17),
    _AdGenEthTotalTxPacketsQueue6_Type()
)
adGenEthTotalTxPacketsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue6.setStatus("current")
_AdGenEthTotalTxPacketsQueue7_Type = Counter64
_AdGenEthTotalTxPacketsQueue7_Object = MibTableColumn
adGenEthTotalTxPacketsQueue7 = _AdGenEthTotalTxPacketsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 18),
    _AdGenEthTotalTxPacketsQueue7_Type()
)
adGenEthTotalTxPacketsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthTotalTxPacketsQueue7.setStatus("current")
_AdGenEthDroppedPacketsQueue0_Type = Counter32
_AdGenEthDroppedPacketsQueue0_Object = MibTableColumn
adGenEthDroppedPacketsQueue0 = _AdGenEthDroppedPacketsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 19),
    _AdGenEthDroppedPacketsQueue0_Type()
)
adGenEthDroppedPacketsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue0.setStatus("current")
_AdGenEthDroppedPacketsQueue1_Type = Counter32
_AdGenEthDroppedPacketsQueue1_Object = MibTableColumn
adGenEthDroppedPacketsQueue1 = _AdGenEthDroppedPacketsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 20),
    _AdGenEthDroppedPacketsQueue1_Type()
)
adGenEthDroppedPacketsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue1.setStatus("current")
_AdGenEthDroppedPacketsQueue2_Type = Counter32
_AdGenEthDroppedPacketsQueue2_Object = MibTableColumn
adGenEthDroppedPacketsQueue2 = _AdGenEthDroppedPacketsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 21),
    _AdGenEthDroppedPacketsQueue2_Type()
)
adGenEthDroppedPacketsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue2.setStatus("current")
_AdGenEthDroppedPacketsQueue3_Type = Counter32
_AdGenEthDroppedPacketsQueue3_Object = MibTableColumn
adGenEthDroppedPacketsQueue3 = _AdGenEthDroppedPacketsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 22),
    _AdGenEthDroppedPacketsQueue3_Type()
)
adGenEthDroppedPacketsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue3.setStatus("current")
_AdGenEthDroppedPacketsQueue4_Type = Counter32
_AdGenEthDroppedPacketsQueue4_Object = MibTableColumn
adGenEthDroppedPacketsQueue4 = _AdGenEthDroppedPacketsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 23),
    _AdGenEthDroppedPacketsQueue4_Type()
)
adGenEthDroppedPacketsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue4.setStatus("current")
_AdGenEthDroppedPacketsQueue5_Type = Counter32
_AdGenEthDroppedPacketsQueue5_Object = MibTableColumn
adGenEthDroppedPacketsQueue5 = _AdGenEthDroppedPacketsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 24),
    _AdGenEthDroppedPacketsQueue5_Type()
)
adGenEthDroppedPacketsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue5.setStatus("current")
_AdGenEthDroppedPacketsQueue6_Type = Counter32
_AdGenEthDroppedPacketsQueue6_Object = MibTableColumn
adGenEthDroppedPacketsQueue6 = _AdGenEthDroppedPacketsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 25),
    _AdGenEthDroppedPacketsQueue6_Type()
)
adGenEthDroppedPacketsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue6.setStatus("current")
_AdGenEthDroppedPacketsQueue7_Type = Counter32
_AdGenEthDroppedPacketsQueue7_Object = MibTableColumn
adGenEthDroppedPacketsQueue7 = _AdGenEthDroppedPacketsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 26),
    _AdGenEthDroppedPacketsQueue7_Type()
)
adGenEthDroppedPacketsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDroppedPacketsQueue7.setStatus("current")
_AdGenEthInPeakUtilization_Type = Gauge32
_AdGenEthInPeakUtilization_Object = MibTableColumn
adGenEthInPeakUtilization = _AdGenEthInPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 27),
    _AdGenEthInPeakUtilization_Type()
)
adGenEthInPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInPeakUtilization.setStatus("current")
_AdGenEthInAvgUtilization_Type = Gauge32
_AdGenEthInAvgUtilization_Object = MibTableColumn
adGenEthInAvgUtilization = _AdGenEthInAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 28),
    _AdGenEthInAvgUtilization_Type()
)
adGenEthInAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthInAvgUtilization.setStatus("current")
_AdGenEthOutPeakUtilization_Type = Gauge32
_AdGenEthOutPeakUtilization_Object = MibTableColumn
adGenEthOutPeakUtilization = _AdGenEthOutPeakUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 29),
    _AdGenEthOutPeakUtilization_Type()
)
adGenEthOutPeakUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthOutPeakUtilization.setStatus("current")
_AdGenEthOutAvgUtilization_Type = Gauge32
_AdGenEthOutAvgUtilization_Object = MibTableColumn
adGenEthOutAvgUtilization = _AdGenEthOutAvgUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 30),
    _AdGenEthOutAvgUtilization_Type()
)
adGenEthOutAvgUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthOutAvgUtilization.setStatus("current")
_AdGenEthDepthPacketsQueue0_Type = Gauge32
_AdGenEthDepthPacketsQueue0_Object = MibTableColumn
adGenEthDepthPacketsQueue0 = _AdGenEthDepthPacketsQueue0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 31),
    _AdGenEthDepthPacketsQueue0_Type()
)
adGenEthDepthPacketsQueue0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue0.setStatus("current")
_AdGenEthDepthPacketsQueue1_Type = Gauge32
_AdGenEthDepthPacketsQueue1_Object = MibTableColumn
adGenEthDepthPacketsQueue1 = _AdGenEthDepthPacketsQueue1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 32),
    _AdGenEthDepthPacketsQueue1_Type()
)
adGenEthDepthPacketsQueue1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue1.setStatus("current")
_AdGenEthDepthPacketsQueue2_Type = Gauge32
_AdGenEthDepthPacketsQueue2_Object = MibTableColumn
adGenEthDepthPacketsQueue2 = _AdGenEthDepthPacketsQueue2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 33),
    _AdGenEthDepthPacketsQueue2_Type()
)
adGenEthDepthPacketsQueue2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue2.setStatus("current")
_AdGenEthDepthPacketsQueue3_Type = Gauge32
_AdGenEthDepthPacketsQueue3_Object = MibTableColumn
adGenEthDepthPacketsQueue3 = _AdGenEthDepthPacketsQueue3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 34),
    _AdGenEthDepthPacketsQueue3_Type()
)
adGenEthDepthPacketsQueue3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue3.setStatus("current")
_AdGenEthDepthPacketsQueue4_Type = Gauge32
_AdGenEthDepthPacketsQueue4_Object = MibTableColumn
adGenEthDepthPacketsQueue4 = _AdGenEthDepthPacketsQueue4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 35),
    _AdGenEthDepthPacketsQueue4_Type()
)
adGenEthDepthPacketsQueue4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue4.setStatus("current")
_AdGenEthDepthPacketsQueue5_Type = Gauge32
_AdGenEthDepthPacketsQueue5_Object = MibTableColumn
adGenEthDepthPacketsQueue5 = _AdGenEthDepthPacketsQueue5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 36),
    _AdGenEthDepthPacketsQueue5_Type()
)
adGenEthDepthPacketsQueue5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue5.setStatus("current")
_AdGenEthDepthPacketsQueue6_Type = Gauge32
_AdGenEthDepthPacketsQueue6_Object = MibTableColumn
adGenEthDepthPacketsQueue6 = _AdGenEthDepthPacketsQueue6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 37),
    _AdGenEthDepthPacketsQueue6_Type()
)
adGenEthDepthPacketsQueue6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue6.setStatus("current")
_AdGenEthDepthPacketsQueue7_Type = Gauge32
_AdGenEthDepthPacketsQueue7_Object = MibTableColumn
adGenEthDepthPacketsQueue7 = _AdGenEthDepthPacketsQueue7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 38),
    _AdGenEthDepthPacketsQueue7_Type()
)
adGenEthDepthPacketsQueue7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthDepthPacketsQueue7.setStatus("current")
_AdGenEthHCInAvgPktsPerSec_Type = Counter64
_AdGenEthHCInAvgPktsPerSec_Object = MibTableColumn
adGenEthHCInAvgPktsPerSec = _AdGenEthHCInAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 39),
    _AdGenEthHCInAvgPktsPerSec_Type()
)
adGenEthHCInAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthHCInAvgPktsPerSec.setStatus("current")
_AdGenEthHCOutAvgPktsPerSec_Type = Counter64
_AdGenEthHCOutAvgPktsPerSec_Object = MibTableColumn
adGenEthHCOutAvgPktsPerSec = _AdGenEthHCOutAvgPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 40),
    _AdGenEthHCOutAvgPktsPerSec_Type()
)
adGenEthHCOutAvgPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthHCOutAvgPktsPerSec.setStatus("current")
_AdGenEthHCInAvgBitsPerSec_Type = Counter64
_AdGenEthHCInAvgBitsPerSec_Object = MibTableColumn
adGenEthHCInAvgBitsPerSec = _AdGenEthHCInAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 41),
    _AdGenEthHCInAvgBitsPerSec_Type()
)
adGenEthHCInAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthHCInAvgBitsPerSec.setStatus("current")
_AdGenEthHCOutAvgBitsPerSec_Type = Counter64
_AdGenEthHCOutAvgBitsPerSec_Object = MibTableColumn
adGenEthHCOutAvgBitsPerSec = _AdGenEthHCOutAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 12, 1, 42),
    _AdGenEthHCOutAvgBitsPerSec_Type()
)
adGenEthHCOutAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthHCOutAvgBitsPerSec.setStatus("current")
_AdGenEthPerformanceCountersHCTable_Object = MibTable
adGenEthPerformanceCountersHCTable = _AdGenEthPerformanceCountersHCTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13)
)
if mibBuilder.loadTexts:
    adGenEthPerformanceCountersHCTable.setStatus("current")
_AdGenEthPerformanceCountersHCEntry_Object = MibTableRow
adGenEthPerformanceCountersHCEntry = _AdGenEthPerformanceCountersHCEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1)
)
adGenEthPerformanceCountersHCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthPerformanceCountersHCEntry.setStatus("current")
_AdGenEthCounterHCInPackets_Type = Counter64
_AdGenEthCounterHCInPackets_Object = MibTableColumn
adGenEthCounterHCInPackets = _AdGenEthCounterHCInPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 1),
    _AdGenEthCounterHCInPackets_Type()
)
adGenEthCounterHCInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInPackets.setStatus("current")
_AdGenEthCounterHCOutPackets_Type = Counter64
_AdGenEthCounterHCOutPackets_Object = MibTableColumn
adGenEthCounterHCOutPackets = _AdGenEthCounterHCOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 2),
    _AdGenEthCounterHCOutPackets_Type()
)
adGenEthCounterHCOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutPackets.setStatus("current")
_AdGenEthCounterHCInBytes_Type = Counter64
_AdGenEthCounterHCInBytes_Object = MibTableColumn
adGenEthCounterHCInBytes = _AdGenEthCounterHCInBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 3),
    _AdGenEthCounterHCInBytes_Type()
)
adGenEthCounterHCInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInBytes.setStatus("current")
_AdGenEthCounterHCOutBytes_Type = Counter64
_AdGenEthCounterHCOutBytes_Object = MibTableColumn
adGenEthCounterHCOutBytes = _AdGenEthCounterHCOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 4),
    _AdGenEthCounterHCOutBytes_Type()
)
adGenEthCounterHCOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutBytes.setStatus("current")
_AdGenEthCounterHCInUnicasts_Type = Counter64
_AdGenEthCounterHCInUnicasts_Object = MibTableColumn
adGenEthCounterHCInUnicasts = _AdGenEthCounterHCInUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 5),
    _AdGenEthCounterHCInUnicasts_Type()
)
adGenEthCounterHCInUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInUnicasts.setStatus("current")
_AdGenEthCounterHCOutUnicasts_Type = Counter64
_AdGenEthCounterHCOutUnicasts_Object = MibTableColumn
adGenEthCounterHCOutUnicasts = _AdGenEthCounterHCOutUnicasts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 6),
    _AdGenEthCounterHCOutUnicasts_Type()
)
adGenEthCounterHCOutUnicasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutUnicasts.setStatus("current")
_AdGenEthCounterHCInBroadcasts_Type = Counter64
_AdGenEthCounterHCInBroadcasts_Object = MibTableColumn
adGenEthCounterHCInBroadcasts = _AdGenEthCounterHCInBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 7),
    _AdGenEthCounterHCInBroadcasts_Type()
)
adGenEthCounterHCInBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInBroadcasts.setStatus("current")
_AdGenEthCounterHCOutBroadcasts_Type = Counter64
_AdGenEthCounterHCOutBroadcasts_Object = MibTableColumn
adGenEthCounterHCOutBroadcasts = _AdGenEthCounterHCOutBroadcasts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 8),
    _AdGenEthCounterHCOutBroadcasts_Type()
)
adGenEthCounterHCOutBroadcasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutBroadcasts.setStatus("current")
_AdGenEthCounterHCInMulticasts_Type = Counter64
_AdGenEthCounterHCInMulticasts_Object = MibTableColumn
adGenEthCounterHCInMulticasts = _AdGenEthCounterHCInMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 9),
    _AdGenEthCounterHCInMulticasts_Type()
)
adGenEthCounterHCInMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInMulticasts.setStatus("current")
_AdGenEthCounterHCOutMulticasts_Type = Counter64
_AdGenEthCounterHCOutMulticasts_Object = MibTableColumn
adGenEthCounterHCOutMulticasts = _AdGenEthCounterHCOutMulticasts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 10),
    _AdGenEthCounterHCOutMulticasts_Type()
)
adGenEthCounterHCOutMulticasts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutMulticasts.setStatus("current")
_AdGenEthCounterHCInErrors_Type = Counter64
_AdGenEthCounterHCInErrors_Object = MibTableColumn
adGenEthCounterHCInErrors = _AdGenEthCounterHCInErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 11),
    _AdGenEthCounterHCInErrors_Type()
)
adGenEthCounterHCInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInErrors.setStatus("current")
_AdGenEthCounterHCOutErrors_Type = Counter64
_AdGenEthCounterHCOutErrors_Object = MibTableColumn
adGenEthCounterHCOutErrors = _AdGenEthCounterHCOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 12),
    _AdGenEthCounterHCOutErrors_Type()
)
adGenEthCounterHCOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutErrors.setStatus("current")
_AdGenEthCounterHCInDiscards_Type = Counter64
_AdGenEthCounterHCInDiscards_Object = MibTableColumn
adGenEthCounterHCInDiscards = _AdGenEthCounterHCInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 13),
    _AdGenEthCounterHCInDiscards_Type()
)
adGenEthCounterHCInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInDiscards.setStatus("current")
_AdGenEthCounterHCOutDiscards_Type = Counter64
_AdGenEthCounterHCOutDiscards_Object = MibTableColumn
adGenEthCounterHCOutDiscards = _AdGenEthCounterHCOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 14),
    _AdGenEthCounterHCOutDiscards_Type()
)
adGenEthCounterHCOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutDiscards.setStatus("current")
_AdGenEthCounterHCInLCVs_Type = Counter64
_AdGenEthCounterHCInLCVs_Object = MibTableColumn
adGenEthCounterHCInLCVs = _AdGenEthCounterHCInLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 15),
    _AdGenEthCounterHCInLCVs_Type()
)
adGenEthCounterHCInLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInLCVs.setStatus("current")
_AdGenEthCounterHCOutLCVs_Type = Counter64
_AdGenEthCounterHCOutLCVs_Object = MibTableColumn
adGenEthCounterHCOutLCVs = _AdGenEthCounterHCOutLCVs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 16),
    _AdGenEthCounterHCOutLCVs_Type()
)
adGenEthCounterHCOutLCVs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCOutLCVs.setStatus("current")
_AdGenEthCounterHCInRunts_Type = Counter64
_AdGenEthCounterHCInRunts_Object = MibTableColumn
adGenEthCounterHCInRunts = _AdGenEthCounterHCInRunts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 17),
    _AdGenEthCounterHCInRunts_Type()
)
adGenEthCounterHCInRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInRunts.setStatus("current")
_AdGenEthCounterHCInGiants_Type = Counter64
_AdGenEthCounterHCInGiants_Object = MibTableColumn
adGenEthCounterHCInGiants = _AdGenEthCounterHCInGiants_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 18),
    _AdGenEthCounterHCInGiants_Type()
)
adGenEthCounterHCInGiants.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInGiants.setStatus("current")
_AdGenEthCounterHCInFrameErrors_Type = Counter64
_AdGenEthCounterHCInFrameErrors_Object = MibTableColumn
adGenEthCounterHCInFrameErrors = _AdGenEthCounterHCInFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 19),
    _AdGenEthCounterHCInFrameErrors_Type()
)
adGenEthCounterHCInFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInFrameErrors.setStatus("current")
_AdGenEthCounterHCInCRCErrors_Type = Counter64
_AdGenEthCounterHCInCRCErrors_Object = MibTableColumn
adGenEthCounterHCInCRCErrors = _AdGenEthCounterHCInCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 3, 13, 1, 20),
    _AdGenEthCounterHCInCRCErrors_Type()
)
adGenEthCounterHCInCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthCounterHCInCRCErrors.setStatus("current")

# Managed Objects groups


# Notification objects

adGenEthSet15MinInErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 1)
)
adGenEthSet15MinInErrors.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInErrors.setStatus(
        "current"
    )

adGenEthSet15MinInDiscards = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 2)
)
adGenEthSet15MinInDiscards.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInDiscards.setStatus(
        "current"
    )

adGenEthSet15MinInGiants = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 3)
)
adGenEthSet15MinInGiants.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInGiants.setStatus(
        "current"
    )

adGenEthSet15MinInRunts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 4)
)
adGenEthSet15MinInRunts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInRunts.setStatus(
        "current"
    )

adGenEthSet15MinInMulticastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 5)
)
adGenEthSet15MinInMulticastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInMulticastPkts.setStatus(
        "current"
    )

adGenEthSet15MinInBroadcastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 6)
)
adGenEthSet15MinInBroadcastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInBroadcastPkts.setStatus(
        "current"
    )

adGenEthSet24HrInErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 7)
)
adGenEthSet24HrInErrors.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrInErrors.setStatus(
        "current"
    )

adGenEthSet24HrInDiscards = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 8)
)
adGenEthSet24HrInDiscards.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrInDiscards.setStatus(
        "current"
    )

adGenEthSet24HrInGiants = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 9)
)
adGenEthSet24HrInGiants.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrInGiants.setStatus(
        "current"
    )

adGenEthSet24HrInRunts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 10)
)
adGenEthSet24HrInRunts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrInRunts.setStatus(
        "current"
    )

adGenEthSet24HrInMulticastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 11)
)
adGenEthSet24HrInMulticastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrInMulticastPkts.setStatus(
        "current"
    )

adGenEthSet24HrInBroadcastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 12)
)
adGenEthSet24HrInBroadcastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrInBroadcastPkts.setStatus(
        "current"
    )

adGenEthIfcLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 14)
)
adGenEthIfcLinkUp.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLinkUp.setStatus(
        "current"
    )

adGenEthIfcLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 15)
)
adGenEthIfcLinkDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLinkDown.setStatus(
        "current"
    )

adGenEthSet15MinInUnicastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 21)
)
adGenEthSet15MinInUnicastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInUnicastPkts.setStatus(
        "current"
    )

adGenEthSet15MinInUnknownProtocols = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 22)
)
adGenEthSet15MinInUnknownProtocols.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInUnknownProtocols.setStatus(
        "current"
    )

adGenEthSet15MinInOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 23)
)
adGenEthSet15MinInOctets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInOctets.setStatus(
        "current"
    )

adGenEthSet15MinInPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 24)
)
adGenEthSet15MinInPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInPkts.setStatus(
        "current"
    )

adGenEthSet15MinInPkts64Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 25)
)
adGenEthSet15MinInPkts64Octets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInPkts64Octets.setStatus(
        "current"
    )

adGenEthSet15MinInPkts65to127Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 27)
)
adGenEthSet15MinInPkts65to127Octets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInPkts65to127Octets.setStatus(
        "current"
    )

adGenEthSet15MinInPkts128to255Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 28)
)
adGenEthSet15MinInPkts128to255Octets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInPkts128to255Octets.setStatus(
        "current"
    )

adGenEthSet15MinInPkts256to511Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 29)
)
adGenEthSet15MinInPkts256to511Octets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInPkts256to511Octets.setStatus(
        "current"
    )

adGenEthSet15MinInPkts512to1023Octets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 30)
)
adGenEthSet15MinInPkts512to1023Octets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInPkts512to1023Octets.setStatus(
        "current"
    )

adGenEthSet15MinInPkts1024toMaxOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 31)
)
adGenEthSet15MinInPkts1024toMaxOctets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInPkts1024toMaxOctets.setStatus(
        "current"
    )

adGenEthSet15MinOutErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 32)
)
adGenEthSet15MinOutErrors.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutErrors.setStatus(
        "current"
    )

adGenEthSet15MinOutDiscards = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 33)
)
adGenEthSet15MinOutDiscards.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutDiscards.setStatus(
        "current"
    )

adGenEthSet15MinOutMulticastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 34)
)
adGenEthSet15MinOutMulticastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutMulticastPkts.setStatus(
        "current"
    )

adGenEthSet15MinOutBroadcastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 35)
)
adGenEthSet15MinOutBroadcastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutBroadcastPkts.setStatus(
        "current"
    )

adGenEthSet15MinOutUnicastPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 36)
)
adGenEthSet15MinOutUnicastPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutUnicastPkts.setStatus(
        "current"
    )

adGenEthSet15MinOutOctets = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 37)
)
adGenEthSet15MinOutOctets.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutOctets.setStatus(
        "current"
    )

adGenEthSet15MinOutPkts = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 38)
)
adGenEthSet15MinOutPkts.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutPkts.setStatus(
        "current"
    )

adGenEthSet15MinES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 39)
)
adGenEthSet15MinES.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinES.setStatus(
        "current"
    )

adGenEthSet15MinLOSS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 40)
)
adGenEthSet15MinLOSS.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinLOSS.setStatus(
        "current"
    )

adGenEthSet15MinSEFS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 41)
)
adGenEthSet15MinSEFS.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinSEFS.setStatus(
        "current"
    )

adGenEthSet15MinSES = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 42)
)
adGenEthSet15MinSES.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinSES.setStatus(
        "current"
    )

adGenEthSet15MinUAS = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 43)
)
adGenEthSet15MinUAS.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinUAS.setStatus(
        "current"
    )

adGenEthSet15MinOutLcvAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 44)
)
adGenEthSet15MinOutLcvAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GEN-ETH-IFC-MIB", "adGenEth15MinThreshOutLcv"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinOutLcvAlm.setStatus(
        "current"
    )

adGenEthSet15MinInLcvAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 45)
)
adGenEthSet15MinInLcvAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GEN-ETH-IFC-MIB", "adGenEth15MinThreshInLcv"))
)
if mibBuilder.loadTexts:
    adGenEthSet15MinInLcvAlm.setStatus(
        "current"
    )

adGenEthSet24HrOutLcvAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 46)
)
adGenEthSet24HrOutLcvAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GEN-ETH-IFC-MIB", "adGenEth24HrThreshOutLcv"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrOutLcvAlm.setStatus(
        "current"
    )

adGenEthSet24HrInLcvAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 47)
)
adGenEthSet24HrInLcvAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GEN-ETH-IFC-MIB", "adGenEth24HrThreshInLcv"))
)
if mibBuilder.loadTexts:
    adGenEthSet24HrInLcvAlm.setStatus(
        "current"
    )

adGenEthIfcLOSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 49)
)
adGenEthIfcLOSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLOSClear.setStatus(
        "current"
    )

adGenEthIfcLOSSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 50)
)
adGenEthIfcLOSSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLOSSet.setStatus(
        "current"
    )

adGenEthIfcLOBSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 51)
)
adGenEthIfcLOBSClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLOBSClear.setStatus(
        "current"
    )

adGenEthIfcLOBSSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 52)
)
adGenEthIfcLOBSSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLOBSSet.setStatus(
        "current"
    )

adGenEthIfcHIBERClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 53)
)
adGenEthIfcHIBERClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcHIBERClear.setStatus(
        "current"
    )

adGenEthIfcHIBERSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 54)
)
adGenEthIfcHIBERSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcHIBERSet.setStatus(
        "current"
    )

adGenEthIfcLocalFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 55)
)
adGenEthIfcLocalFaultClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLocalFaultClear.setStatus(
        "current"
    )

adGenEthIfcLocalFaultSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 56)
)
adGenEthIfcLocalFaultSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcLocalFaultSet.setStatus(
        "current"
    )

adGenEthIfcRemoteFaultClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 57)
)
adGenEthIfcRemoteFaultClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcRemoteFaultClear.setStatus(
        "current"
    )

adGenEthIfcRemoteFaultSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 58)
)
adGenEthIfcRemoteFaultSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthIfcRemoteFaultSet.setStatus(
        "current"
    )

adGenEthPortYCableCfgAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 59)
)
adGenEthPortYCableCfgAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthPortYCableCfgAlarmClear.setStatus(
        "current"
    )

adGenEthPortYCableCfgAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 60)
)
adGenEthPortYCableCfgAlarmSet.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenEthPortYCableCfgAlarmSet.setStatus(
        "current"
    )

adGenEthSpeedScanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 61)
)
adGenEthSpeedScanAlarm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenEthSpeedScanAlarm.setStatus(
        "current"
    )

adGenEthSpeedScanAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 15, 0, 62)
)
adGenEthSpeedScanAlarmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("IF-MIB", "ifDescr"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenEthSpeedScanAlarmClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-ETH-IFC-MIB",
    **{"adGenEthIfcEvents": adGenEthIfcEvents,
       "adGenEthSet15MinInErrors": adGenEthSet15MinInErrors,
       "adGenEthSet15MinInDiscards": adGenEthSet15MinInDiscards,
       "adGenEthSet15MinInGiants": adGenEthSet15MinInGiants,
       "adGenEthSet15MinInRunts": adGenEthSet15MinInRunts,
       "adGenEthSet15MinInMulticastPkts": adGenEthSet15MinInMulticastPkts,
       "adGenEthSet15MinInBroadcastPkts": adGenEthSet15MinInBroadcastPkts,
       "adGenEthSet24HrInErrors": adGenEthSet24HrInErrors,
       "adGenEthSet24HrInDiscards": adGenEthSet24HrInDiscards,
       "adGenEthSet24HrInGiants": adGenEthSet24HrInGiants,
       "adGenEthSet24HrInRunts": adGenEthSet24HrInRunts,
       "adGenEthSet24HrInMulticastPkts": adGenEthSet24HrInMulticastPkts,
       "adGenEthSet24HrInBroadcastPkts": adGenEthSet24HrInBroadcastPkts,
       "adGenEthIfcLinkUp": adGenEthIfcLinkUp,
       "adGenEthIfcLinkDown": adGenEthIfcLinkDown,
       "adGenEthSet15MinInUnicastPkts": adGenEthSet15MinInUnicastPkts,
       "adGenEthSet15MinInUnknownProtocols": adGenEthSet15MinInUnknownProtocols,
       "adGenEthSet15MinInOctets": adGenEthSet15MinInOctets,
       "adGenEthSet15MinInPkts": adGenEthSet15MinInPkts,
       "adGenEthSet15MinInPkts64Octets": adGenEthSet15MinInPkts64Octets,
       "adGenEthSet15MinInPkts65to127Octets": adGenEthSet15MinInPkts65to127Octets,
       "adGenEthSet15MinInPkts128to255Octets": adGenEthSet15MinInPkts128to255Octets,
       "adGenEthSet15MinInPkts256to511Octets": adGenEthSet15MinInPkts256to511Octets,
       "adGenEthSet15MinInPkts512to1023Octets": adGenEthSet15MinInPkts512to1023Octets,
       "adGenEthSet15MinInPkts1024toMaxOctets": adGenEthSet15MinInPkts1024toMaxOctets,
       "adGenEthSet15MinOutErrors": adGenEthSet15MinOutErrors,
       "adGenEthSet15MinOutDiscards": adGenEthSet15MinOutDiscards,
       "adGenEthSet15MinOutMulticastPkts": adGenEthSet15MinOutMulticastPkts,
       "adGenEthSet15MinOutBroadcastPkts": adGenEthSet15MinOutBroadcastPkts,
       "adGenEthSet15MinOutUnicastPkts": adGenEthSet15MinOutUnicastPkts,
       "adGenEthSet15MinOutOctets": adGenEthSet15MinOutOctets,
       "adGenEthSet15MinOutPkts": adGenEthSet15MinOutPkts,
       "adGenEthSet15MinES": adGenEthSet15MinES,
       "adGenEthSet15MinLOSS": adGenEthSet15MinLOSS,
       "adGenEthSet15MinSEFS": adGenEthSet15MinSEFS,
       "adGenEthSet15MinSES": adGenEthSet15MinSES,
       "adGenEthSet15MinUAS": adGenEthSet15MinUAS,
       "adGenEthSet15MinOutLcvAlm": adGenEthSet15MinOutLcvAlm,
       "adGenEthSet15MinInLcvAlm": adGenEthSet15MinInLcvAlm,
       "adGenEthSet24HrOutLcvAlm": adGenEthSet24HrOutLcvAlm,
       "adGenEthSet24HrInLcvAlm": adGenEthSet24HrInLcvAlm,
       "adGenEthIfcLOSClear": adGenEthIfcLOSClear,
       "adGenEthIfcLOSSet": adGenEthIfcLOSSet,
       "adGenEthIfcLOBSClear": adGenEthIfcLOBSClear,
       "adGenEthIfcLOBSSet": adGenEthIfcLOBSSet,
       "adGenEthIfcHIBERClear": adGenEthIfcHIBERClear,
       "adGenEthIfcHIBERSet": adGenEthIfcHIBERSet,
       "adGenEthIfcLocalFaultClear": adGenEthIfcLocalFaultClear,
       "adGenEthIfcLocalFaultSet": adGenEthIfcLocalFaultSet,
       "adGenEthIfcRemoteFaultClear": adGenEthIfcRemoteFaultClear,
       "adGenEthIfcRemoteFaultSet": adGenEthIfcRemoteFaultSet,
       "adGenEthPortYCableCfgAlarmClear": adGenEthPortYCableCfgAlarmClear,
       "adGenEthPortYCableCfgAlarmSet": adGenEthPortYCableCfgAlarmSet,
       "adGenEthSpeedScanAlarm": adGenEthSpeedScanAlarm,
       "adGenEthSpeedScanAlarmClear": adGenEthSpeedScanAlarmClear,
       "adGenEthIfcProvisioning": adGenEthIfcProvisioning,
       "adGenEthProvTable": adGenEthProvTable,
       "adGenEthProvEntry": adGenEthProvEntry,
       "adGenEthPortSpeed": adGenEthPortSpeed,
       "adGenEthPortDuplex": adGenEthPortDuplex,
       "adGenEthLinkUpDownTrapEnable": adGenEthLinkUpDownTrapEnable,
       "adGenEthPortFixedSpeed": adGenEthPortFixedSpeed,
       "adGenEthPortFixedDuplex": adGenEthPortFixedDuplex,
       "adGenEthAutoNegotiateCu": adGenEthAutoNegotiateCu,
       "adGenEthAdvertisedSpeedAndDuplexCu": adGenEthAdvertisedSpeedAndDuplexCu,
       "adGenEthAutoNegotiateFiber": adGenEthAutoNegotiateFiber,
       "adGenEthAdvertisedDuplexFiber": adGenEthAdvertisedDuplexFiber,
       "adGenEthPortYCableEnable": adGenEthPortYCableEnable,
       "adGenEthSpeedScanAlarmEnable": adGenEthSpeedScanAlarmEnable,
       "adGenEthSpeedScanAlarmSeverityLevel": adGenEthSpeedScanAlarmSeverityLevel,
       "adGenEthPortBreakoutMode": adGenEthPortBreakoutMode,
       "adGenEthPortBreakoutModesSupported": adGenEthPortBreakoutModesSupported,
       "adGenEthForwardErrorCorrection": adGenEthForwardErrorCorrection,
       "adGenEthPortBreakoutModeStatus": adGenEthPortBreakoutModeStatus,
       "adGenEthProvEVCAdvertisementTable": adGenEthProvEVCAdvertisementTable,
       "adGenEthProvEVCAdvertisementEntry": adGenEthProvEVCAdvertisementEntry,
       "adGenEthProvEVCAdvertisementState": adGenEthProvEVCAdvertisementState,
       "adGenEthAlarmSlotProvTable": adGenEthAlarmSlotProvTable,
       "adGenEthAlarmSlotProvEntry": adGenEthAlarmSlotProvEntry,
       "adGenEthAlarmSlotIfcLinkDownSeverityLevel": adGenEthAlarmSlotIfcLinkDownSeverityLevel,
       "adGenEthAlarmSlotLinkDownSeverityLevel": adGenEthAlarmSlotLinkDownSeverityLevel,
       "adGenEthIfcStatus": adGenEthIfcStatus,
       "adGenEthStatusTable": adGenEthStatusTable,
       "adGenEthStatusEntry": adGenEthStatusEntry,
       "adGenEthCurrentSpeed": adGenEthCurrentSpeed,
       "adGenEthCurrentDuplex": adGenEthCurrentDuplex,
       "adGenEthCurrentAutoNeg": adGenEthCurrentAutoNeg,
       "adGenEthCurrentAutoNegStatus": adGenEthCurrentAutoNegStatus,
       "adGenEthCurrentInterfaceType": adGenEthCurrentInterfaceType,
       "adGenEthInterfaceCuOrFiber": adGenEthInterfaceCuOrFiber,
       "adGenEthInterfaceFixedOrPluggable": adGenEthInterfaceFixedOrPluggable,
       "adGenEthValid15MinIntervals": adGenEthValid15MinIntervals,
       "adGenEthValid24HrIntervals": adGenEthValid24HrIntervals,
       "adGenEthAlarmStatus": adGenEthAlarmStatus,
       "adGenEthLastError": adGenEthLastError,
       "adGenEthStatEVCAdvertisementTable": adGenEthStatEVCAdvertisementTable,
       "adGenEthStatEVCAdvertisementEntry": adGenEthStatEVCAdvertisementEntry,
       "adGenEthStatEVCAdvertisementVLANID": adGenEthStatEVCAdvertisementVLANID,
       "adGenEthStatEVCAdvertisementStatus": adGenEthStatEVCAdvertisementStatus,
       "adGenEthIfcPerformance": adGenEthIfcPerformance,
       "adGenEthPerformanceScalars": adGenEthPerformanceScalars,
       "adGenEthRstCurrentIntervals": adGenEthRstCurrentIntervals,
       "adGenEthRstAll": adGenEthRstAll,
       "adGenEth15MinCurrentTable": adGenEth15MinCurrentTable,
       "adGenEth15MinCurrentEntry": adGenEth15MinCurrentEntry,
       "adGenEth15MinCurrentOutOctets": adGenEth15MinCurrentOutOctets,
       "adGenEth15MinCurrentOutPkts": adGenEth15MinCurrentOutPkts,
       "adGenEth15MinCurrentInOctets": adGenEth15MinCurrentInOctets,
       "adGenEth15MinCurrentInPkts": adGenEth15MinCurrentInPkts,
       "adGenEth15MinCurrentInGoodOctets": adGenEth15MinCurrentInGoodOctets,
       "adGenEth15MinCurrentInGoodPkts": adGenEth15MinCurrentInGoodPkts,
       "adGenEth15MinCurrentInErrors": adGenEth15MinCurrentInErrors,
       "adGenEth15MinCurrentInDiscards": adGenEth15MinCurrentInDiscards,
       "adGenEth15MinCurrentInGiants": adGenEth15MinCurrentInGiants,
       "adGenEth15MinCurrentInRunts": adGenEth15MinCurrentInRunts,
       "adGenEth15MinCurrentInMulticastPkts": adGenEth15MinCurrentInMulticastPkts,
       "adGenEth15MinCurrentInBroadcastPkts": adGenEth15MinCurrentInBroadcastPkts,
       "adGenEth15MinCurrentInUnicastPkts": adGenEth15MinCurrentInUnicastPkts,
       "adGenEth15MinCurrentOutMulticastPkts": adGenEth15MinCurrentOutMulticastPkts,
       "adGenEth15MinCurrentOutBroadcastPkts": adGenEth15MinCurrentOutBroadcastPkts,
       "adGenEth15MinCurrentOutUnicastPkts": adGenEth15MinCurrentOutUnicastPkts,
       "adGenEth15MinCurrentDroppedPktsQueue0": adGenEth15MinCurrentDroppedPktsQueue0,
       "adGenEth15MinCurrentDroppedPktsQueue1": adGenEth15MinCurrentDroppedPktsQueue1,
       "adGenEth15MinCurrentDroppedPktsQueue2": adGenEth15MinCurrentDroppedPktsQueue2,
       "adGenEth15MinCurrentDroppedPktsQueue3": adGenEth15MinCurrentDroppedPktsQueue3,
       "adGenEth15MinCurrentDroppedPktsQueue4": adGenEth15MinCurrentDroppedPktsQueue4,
       "adGenEth15MinCurrentDroppedPktsQueue5": adGenEth15MinCurrentDroppedPktsQueue5,
       "adGenEth15MinCurrentDroppedPktsQueue6": adGenEth15MinCurrentDroppedPktsQueue6,
       "adGenEth15MinCurrentDroppedPktsQueue7": adGenEth15MinCurrentDroppedPktsQueue7,
       "adGenEth15MinCurrentOutDiscards": adGenEth15MinCurrentOutDiscards,
       "adGenEth15MinCurrentInCRCErrors": adGenEth15MinCurrentInCRCErrors,
       "adGenEth15MinCurrentInFrameErrors": adGenEth15MinCurrentInFrameErrors,
       "adGenEth15MinCurrentOutErrors": adGenEth15MinCurrentOutErrors,
       "adGenEth15MinCurrentInPeakUtilization": adGenEth15MinCurrentInPeakUtilization,
       "adGenEth15MinCurrentInAvgUtilization": adGenEth15MinCurrentInAvgUtilization,
       "adGenEth15MinCurrentOutPeakUtilization": adGenEth15MinCurrentOutPeakUtilization,
       "adGenEth15MinCurrentOutAvgUtilization": adGenEth15MinCurrentOutAvgUtilization,
       "adGenEth15MinCurrentHCTable": adGenEth15MinCurrentHCTable,
       "adGenEth15MinCurrentHCEntry": adGenEth15MinCurrentHCEntry,
       "adGenEth15MinCurrentHCOutOctets": adGenEth15MinCurrentHCOutOctets,
       "adGenEth15MinCurrentHCInOctets": adGenEth15MinCurrentHCInOctets,
       "adGenEth15MinCurrentHCInMulticastPkts": adGenEth15MinCurrentHCInMulticastPkts,
       "adGenEth15MinCurrentHCInBroadcastPkts": adGenEth15MinCurrentHCInBroadcastPkts,
       "adGenEth15MinCurrentHCInUnicastPkts": adGenEth15MinCurrentHCInUnicastPkts,
       "adGenEth15MinCurrentHCOutMulticastPkts": adGenEth15MinCurrentHCOutMulticastPkts,
       "adGenEth15MinCurrentHCOutBroadcastPkts": adGenEth15MinCurrentHCOutBroadcastPkts,
       "adGenEth15MinCurrentHCOutUnicastPkts": adGenEth15MinCurrentHCOutUnicastPkts,
       "adGenEth15MinCurrentHCTotalPktsQueue0": adGenEth15MinCurrentHCTotalPktsQueue0,
       "adGenEth15MinCurrentHCTotalPktsQueue1": adGenEth15MinCurrentHCTotalPktsQueue1,
       "adGenEth15MinCurrentHCTotalPktsQueue2": adGenEth15MinCurrentHCTotalPktsQueue2,
       "adGenEth15MinCurrentHCTotalPktsQueue3": adGenEth15MinCurrentHCTotalPktsQueue3,
       "adGenEth15MinCurrentHCTotalPktsQueue4": adGenEth15MinCurrentHCTotalPktsQueue4,
       "adGenEth15MinCurrentHCTotalPktsQueue5": adGenEth15MinCurrentHCTotalPktsQueue5,
       "adGenEth15MinCurrentHCTotalPktsQueue6": adGenEth15MinCurrentHCTotalPktsQueue6,
       "adGenEth15MinCurrentHCTotalPktsQueue7": adGenEth15MinCurrentHCTotalPktsQueue7,
       "adGenEth15MinCurrentHCOutLcv": adGenEth15MinCurrentHCOutLcv,
       "adGenEth15MinCurrentHCInLcv": adGenEth15MinCurrentHCInLcv,
       "adGenEth15MinCurrentHCInAvgBitsPerSec": adGenEth15MinCurrentHCInAvgBitsPerSec,
       "adGenEth15MinCurrentHCInAvgPktsPerSec": adGenEth15MinCurrentHCInAvgPktsPerSec,
       "adGenEth15MinCurrentHCOutAvgBitsPerSec": adGenEth15MinCurrentHCOutAvgBitsPerSec,
       "adGenEth15MinCurrentHCOutAvgPktsPerSec": adGenEth15MinCurrentHCOutAvgPktsPerSec,
       "adGenEth15MinIntervalTable": adGenEth15MinIntervalTable,
       "adGenEth15MinIntervalEntry": adGenEth15MinIntervalEntry,
       "adGenEth15MinIntervalNumber": adGenEth15MinIntervalNumber,
       "adGenEth15MinIntervalOutOctets": adGenEth15MinIntervalOutOctets,
       "adGenEth15MinIntervalOutPkts": adGenEth15MinIntervalOutPkts,
       "adGenEth15MinIntervalInOctets": adGenEth15MinIntervalInOctets,
       "adGenEth15MinIntervalInPkts": adGenEth15MinIntervalInPkts,
       "adGenEth15MinIntervalInGoodOctets": adGenEth15MinIntervalInGoodOctets,
       "adGenEth15MinIntervalInGoodPkts": adGenEth15MinIntervalInGoodPkts,
       "adGenEth15MinIntervalInErrors": adGenEth15MinIntervalInErrors,
       "adGenEth15MinIntervalInDiscards": adGenEth15MinIntervalInDiscards,
       "adGenEth15MinIntervalInGiants": adGenEth15MinIntervalInGiants,
       "adGenEth15MinIntervalInRunts": adGenEth15MinIntervalInRunts,
       "adGenEth15MinIntervalInMulticastPkts": adGenEth15MinIntervalInMulticastPkts,
       "adGenEth15MinIntervalInBroadcastPkts": adGenEth15MinIntervalInBroadcastPkts,
       "adGenEth15MinIntervalInUnicastPkts": adGenEth15MinIntervalInUnicastPkts,
       "adGenEth15MinIntervalOutMulticastPkts": adGenEth15MinIntervalOutMulticastPkts,
       "adGenEth15MinIntervalOutBroadcastPkts": adGenEth15MinIntervalOutBroadcastPkts,
       "adGenEth15MinIntervalOutUnicastPkts": adGenEth15MinIntervalOutUnicastPkts,
       "adGenEth15MinIntervalDroppedPktsQueue0": adGenEth15MinIntervalDroppedPktsQueue0,
       "adGenEth15MinIntervalDroppedPktsQueue1": adGenEth15MinIntervalDroppedPktsQueue1,
       "adGenEth15MinIntervalDroppedPktsQueue2": adGenEth15MinIntervalDroppedPktsQueue2,
       "adGenEth15MinIntervalDroppedPktsQueue3": adGenEth15MinIntervalDroppedPktsQueue3,
       "adGenEth15MinIntervalDroppedPktsQueue4": adGenEth15MinIntervalDroppedPktsQueue4,
       "adGenEth15MinIntervalDroppedPktsQueue5": adGenEth15MinIntervalDroppedPktsQueue5,
       "adGenEth15MinIntervalDroppedPktsQueue6": adGenEth15MinIntervalDroppedPktsQueue6,
       "adGenEth15MinIntervalDroppedPktsQueue7": adGenEth15MinIntervalDroppedPktsQueue7,
       "adGenEth15MinIntervalOutDiscards": adGenEth15MinIntervalOutDiscards,
       "adGenEth15MinIntervalInCRCErrors": adGenEth15MinIntervalInCRCErrors,
       "adGenEth15MinIntervalInFrameErrors": adGenEth15MinIntervalInFrameErrors,
       "adGenEth15MinIntervalOutErrors": adGenEth15MinIntervalOutErrors,
       "adGenEth15MinIntervalInPeakUtilization": adGenEth15MinIntervalInPeakUtilization,
       "adGenEth15MinIntervalInAvgUtilization": adGenEth15MinIntervalInAvgUtilization,
       "adGenEth15MinIntervalOutPeakUtilization": adGenEth15MinIntervalOutPeakUtilization,
       "adGenEth15MinIntervalOutAvgUtilization": adGenEth15MinIntervalOutAvgUtilization,
       "adGenEth15MinIntervalHCTable": adGenEth15MinIntervalHCTable,
       "adGenEth15MinIntervalHCEntry": adGenEth15MinIntervalHCEntry,
       "adGenEth15MinIntervalHCNumber": adGenEth15MinIntervalHCNumber,
       "adGenEth15MinIntervalHCOutOctets": adGenEth15MinIntervalHCOutOctets,
       "adGenEth15MinIntervalHCInOctets": adGenEth15MinIntervalHCInOctets,
       "adGenEth15MinIntervalHCInMulticastPkts": adGenEth15MinIntervalHCInMulticastPkts,
       "adGenEth15MinIntervalHCInBroadcastPkts": adGenEth15MinIntervalHCInBroadcastPkts,
       "adGenEth15MinIntervalHCInUnicastPkts": adGenEth15MinIntervalHCInUnicastPkts,
       "adGenEth15MinIntervalHCOutMulticastPkts": adGenEth15MinIntervalHCOutMulticastPkts,
       "adGenEth15MinIntervalHCOutBroadcastPkts": adGenEth15MinIntervalHCOutBroadcastPkts,
       "adGenEth15MinIntervalHCOutUnicastPkts": adGenEth15MinIntervalHCOutUnicastPkts,
       "adGenEth15MinIntervalHCTotalPktsQueue0": adGenEth15MinIntervalHCTotalPktsQueue0,
       "adGenEth15MinIntervalHCTotalPktsQueue1": adGenEth15MinIntervalHCTotalPktsQueue1,
       "adGenEth15MinIntervalHCTotalPktsQueue2": adGenEth15MinIntervalHCTotalPktsQueue2,
       "adGenEth15MinIntervalHCTotalPktsQueue3": adGenEth15MinIntervalHCTotalPktsQueue3,
       "adGenEth15MinIntervalHCTotalPktsQueue4": adGenEth15MinIntervalHCTotalPktsQueue4,
       "adGenEth15MinIntervalHCTotalPktsQueue5": adGenEth15MinIntervalHCTotalPktsQueue5,
       "adGenEth15MinIntervalHCTotalPktsQueue6": adGenEth15MinIntervalHCTotalPktsQueue6,
       "adGenEth15MinIntervalHCTotalPktsQueue7": adGenEth15MinIntervalHCTotalPktsQueue7,
       "adGenEth15MinIntervalHCOutLcv": adGenEth15MinIntervalHCOutLcv,
       "adGenEth15MinIntervalHCInLcv": adGenEth15MinIntervalHCInLcv,
       "adGenEth15MinIntervalHCValidData": adGenEth15MinIntervalHCValidData,
       "adGenEth15MinIntervalHCInAvgBitsPerSec": adGenEth15MinIntervalHCInAvgBitsPerSec,
       "adGenEth15MinIntervalHCInAvgPktsPerSec": adGenEth15MinIntervalHCInAvgPktsPerSec,
       "adGenEth15MinIntervalHCOutAvgBitsPerSec": adGenEth15MinIntervalHCOutAvgBitsPerSec,
       "adGenEth15MinIntervalHCOutAvgPktsPerSec": adGenEth15MinIntervalHCOutAvgPktsPerSec,
       "adGenEth24HrCurrentTable": adGenEth24HrCurrentTable,
       "adGenEth24HrCurrentEntry": adGenEth24HrCurrentEntry,
       "adGenEth24HrCurrentOutOctets": adGenEth24HrCurrentOutOctets,
       "adGenEth24HrCurrentOutPkts": adGenEth24HrCurrentOutPkts,
       "adGenEth24HrCurrentInOctets": adGenEth24HrCurrentInOctets,
       "adGenEth24HrCurrentInPkts": adGenEth24HrCurrentInPkts,
       "adGenEth24HrCurrentInGoodOctets": adGenEth24HrCurrentInGoodOctets,
       "adGenEth24HrCurrentInGoodPkts": adGenEth24HrCurrentInGoodPkts,
       "adGenEth24HrCurrentInErrors": adGenEth24HrCurrentInErrors,
       "adGenEth24HrCurrentInDiscards": adGenEth24HrCurrentInDiscards,
       "adGenEth24HrCurrentInGiants": adGenEth24HrCurrentInGiants,
       "adGenEth24HrCurrentInRunts": adGenEth24HrCurrentInRunts,
       "adGenEth24HrCurrentInMulticastPkts": adGenEth24HrCurrentInMulticastPkts,
       "adGenEth24HrCurrentInBroadcastPkts": adGenEth24HrCurrentInBroadcastPkts,
       "adGenEth24HrCurrentInUnicastPkts": adGenEth24HrCurrentInUnicastPkts,
       "adGenEth24HrCurrentOutMulticastPkts": adGenEth24HrCurrentOutMulticastPkts,
       "adGenEth24HrCurrentOutBroadcastPkts": adGenEth24HrCurrentOutBroadcastPkts,
       "adGenEth24HrCurrentOutUnicastPkts": adGenEth24HrCurrentOutUnicastPkts,
       "adGenEth24HrCurrentDroppedPktsQueue0": adGenEth24HrCurrentDroppedPktsQueue0,
       "adGenEth24HrCurrentDroppedPktsQueue1": adGenEth24HrCurrentDroppedPktsQueue1,
       "adGenEth24HrCurrentDroppedPktsQueue2": adGenEth24HrCurrentDroppedPktsQueue2,
       "adGenEth24HrCurrentDroppedPktsQueue3": adGenEth24HrCurrentDroppedPktsQueue3,
       "adGenEth24HrCurrentDroppedPktsQueue4": adGenEth24HrCurrentDroppedPktsQueue4,
       "adGenEth24HrCurrentDroppedPktsQueue5": adGenEth24HrCurrentDroppedPktsQueue5,
       "adGenEth24HrCurrentDroppedPktsQueue6": adGenEth24HrCurrentDroppedPktsQueue6,
       "adGenEth24HrCurrentDroppedPktsQueue7": adGenEth24HrCurrentDroppedPktsQueue7,
       "adGenEth24HrCurrentOutDiscards": adGenEth24HrCurrentOutDiscards,
       "adGenEth24HrCurrentInCRCErrors": adGenEth24HrCurrentInCRCErrors,
       "adGenEth24HrCurrentInFrameErrors": adGenEth24HrCurrentInFrameErrors,
       "adGenEth24HrCurrentOutErrors": adGenEth24HrCurrentOutErrors,
       "adGenEth24HrCurrentInPeakUtilization": adGenEth24HrCurrentInPeakUtilization,
       "adGenEth24HrCurrentInAvgUtilization": adGenEth24HrCurrentInAvgUtilization,
       "adGenEth24HrCurrentOutPeakUtilization": adGenEth24HrCurrentOutPeakUtilization,
       "adGenEth24HrCurrentOutAvgUtilization": adGenEth24HrCurrentOutAvgUtilization,
       "adGenEth24HrCurrentHCTable": adGenEth24HrCurrentHCTable,
       "adGenEth24HrCurrentHCEntry": adGenEth24HrCurrentHCEntry,
       "adGenEth24HrCurrentHCOutOctets": adGenEth24HrCurrentHCOutOctets,
       "adGenEth24HrCurrentHCInOctets": adGenEth24HrCurrentHCInOctets,
       "adGenEth24HrCurrentHCInMulticastPkts": adGenEth24HrCurrentHCInMulticastPkts,
       "adGenEth24HrCurrentHCInBroadcastPkts": adGenEth24HrCurrentHCInBroadcastPkts,
       "adGenEth24HrCurrentHCInUnicastPkts": adGenEth24HrCurrentHCInUnicastPkts,
       "adGenEth24HrCurrentHCOutMulticastPkts": adGenEth24HrCurrentHCOutMulticastPkts,
       "adGenEth24HrCurrentHCOutBroadcastPkts": adGenEth24HrCurrentHCOutBroadcastPkts,
       "adGenEth24HrCurrentHCOutUnicastPkts": adGenEth24HrCurrentHCOutUnicastPkts,
       "adGenEth24HrCurrentHCTotalPktsQueue0": adGenEth24HrCurrentHCTotalPktsQueue0,
       "adGenEth24HrCurrentHCTotalPktsQueue1": adGenEth24HrCurrentHCTotalPktsQueue1,
       "adGenEth24HrCurrentHCTotalPktsQueue2": adGenEth24HrCurrentHCTotalPktsQueue2,
       "adGenEth24HrCurrentHCTotalPktsQueue3": adGenEth24HrCurrentHCTotalPktsQueue3,
       "adGenEth24HrCurrentHCTotalPktsQueue4": adGenEth24HrCurrentHCTotalPktsQueue4,
       "adGenEth24HrCurrentHCTotalPktsQueue5": adGenEth24HrCurrentHCTotalPktsQueue5,
       "adGenEth24HrCurrentHCTotalPktsQueue6": adGenEth24HrCurrentHCTotalPktsQueue6,
       "adGenEth24HrCurrentHCTotalPktsQueue7": adGenEth24HrCurrentHCTotalPktsQueue7,
       "adGenEth24HrCurrentHCOutLcv": adGenEth24HrCurrentHCOutLcv,
       "adGenEth24HrCurrentHCInLcv": adGenEth24HrCurrentHCInLcv,
       "adGenEth24HrCurrentHCInAvgBitsPerSec": adGenEth24HrCurrentHCInAvgBitsPerSec,
       "adGenEth24HrCurrentHCInAvgPktsPerSec": adGenEth24HrCurrentHCInAvgPktsPerSec,
       "adGenEth24HrCurrentHCOutAvgBitsPerSec": adGenEth24HrCurrentHCOutAvgBitsPerSec,
       "adGenEth24HrCurrentHCOutAvgPktsPerSec": adGenEth24HrCurrentHCOutAvgPktsPerSec,
       "adGenEth24HrIntervalTable": adGenEth24HrIntervalTable,
       "adGenEth24HrIntervalEntry": adGenEth24HrIntervalEntry,
       "adGenEth24HrIntervalNumber": adGenEth24HrIntervalNumber,
       "adGenEth24HrIntervalOutOctets": adGenEth24HrIntervalOutOctets,
       "adGenEth24HrIntervalOutPkts": adGenEth24HrIntervalOutPkts,
       "adGenEth24HrIntervalInOctets": adGenEth24HrIntervalInOctets,
       "adGenEth24HrIntervalInPkts": adGenEth24HrIntervalInPkts,
       "adGenEth24HrIntervalInGoodOctets": adGenEth24HrIntervalInGoodOctets,
       "adGenEth24HrIntervalInGoodPkts": adGenEth24HrIntervalInGoodPkts,
       "adGenEth24HrIntervalInErrors": adGenEth24HrIntervalInErrors,
       "adGenEth24HrIntervalInDiscards": adGenEth24HrIntervalInDiscards,
       "adGenEth24HrIntervalInGiants": adGenEth24HrIntervalInGiants,
       "adGenEth24HrIntervalInRunts": adGenEth24HrIntervalInRunts,
       "adGenEth24HrIntervalInMulticastPkts": adGenEth24HrIntervalInMulticastPkts,
       "adGenEth24HrIntervalInBroadcastPkts": adGenEth24HrIntervalInBroadcastPkts,
       "adGenEth24HrIntervalInUnicastPkts": adGenEth24HrIntervalInUnicastPkts,
       "adGenEth24HrIntervalOutMulticastPkts": adGenEth24HrIntervalOutMulticastPkts,
       "adGenEth24HrIntervalOutBroadcastPkts": adGenEth24HrIntervalOutBroadcastPkts,
       "adGenEth24HrIntervalOutUnicastPkts": adGenEth24HrIntervalOutUnicastPkts,
       "adGenEth24HrIntervalDroppedPktsQueue0": adGenEth24HrIntervalDroppedPktsQueue0,
       "adGenEth24HrIntervalDroppedPktsQueue1": adGenEth24HrIntervalDroppedPktsQueue1,
       "adGenEth24HrIntervalDroppedPktsQueue2": adGenEth24HrIntervalDroppedPktsQueue2,
       "adGenEth24HrIntervalDroppedPktsQueue3": adGenEth24HrIntervalDroppedPktsQueue3,
       "adGenEth24HrIntervalDroppedPktsQueue4": adGenEth24HrIntervalDroppedPktsQueue4,
       "adGenEth24HrIntervalDroppedPktsQueue5": adGenEth24HrIntervalDroppedPktsQueue5,
       "adGenEth24HrIntervalDroppedPktsQueue6": adGenEth24HrIntervalDroppedPktsQueue6,
       "adGenEth24HrIntervalDroppedPktsQueue7": adGenEth24HrIntervalDroppedPktsQueue7,
       "adGenEth24HrIntervalOutDiscards": adGenEth24HrIntervalOutDiscards,
       "adGenEth24HrIntervalInCRCErrors": adGenEth24HrIntervalInCRCErrors,
       "adGenEth24HrIntervalInFrameErrors": adGenEth24HrIntervalInFrameErrors,
       "adGenEth24HrIntervalOutErrors": adGenEth24HrIntervalOutErrors,
       "adGenEth24HrIntervalInPeakUtilization": adGenEth24HrIntervalInPeakUtilization,
       "adGenEth24HrIntervalInAvgUtilization": adGenEth24HrIntervalInAvgUtilization,
       "adGenEth24HrIntervalOutPeakUtilization": adGenEth24HrIntervalOutPeakUtilization,
       "adGenEth24HrIntervalOutAvgUtilization": adGenEth24HrIntervalOutAvgUtilization,
       "adGenEth24HrIntervalHCTable": adGenEth24HrIntervalHCTable,
       "adGenEth24HrIntervalHCEntry": adGenEth24HrIntervalHCEntry,
       "adGenEth24HrIntervalHCNumber": adGenEth24HrIntervalHCNumber,
       "adGenEth24HrIntervalHCOutOctets": adGenEth24HrIntervalHCOutOctets,
       "adGenEth24HrIntervalHCInOctets": adGenEth24HrIntervalHCInOctets,
       "adGenEth24HrIntervalHCInMulticastPkts": adGenEth24HrIntervalHCInMulticastPkts,
       "adGenEth24HrIntervalHCInBroadcastPkts": adGenEth24HrIntervalHCInBroadcastPkts,
       "adGenEth24HrIntervalHCInUnicastPkts": adGenEth24HrIntervalHCInUnicastPkts,
       "adGenEth24HrIntervalHCOutMulticastPkts": adGenEth24HrIntervalHCOutMulticastPkts,
       "adGenEth24HrIntervalHCOutBroadcastPkts": adGenEth24HrIntervalHCOutBroadcastPkts,
       "adGenEth24HrIntervalHCOutUnicastPkts": adGenEth24HrIntervalHCOutUnicastPkts,
       "adGenEth24HrIntervalHCTotalPktsQueue0": adGenEth24HrIntervalHCTotalPktsQueue0,
       "adGenEth24HrIntervalHCTotalPktsQueue1": adGenEth24HrIntervalHCTotalPktsQueue1,
       "adGenEth24HrIntervalHCTotalPktsQueue2": adGenEth24HrIntervalHCTotalPktsQueue2,
       "adGenEth24HrIntervalHCTotalPktsQueue3": adGenEth24HrIntervalHCTotalPktsQueue3,
       "adGenEth24HrIntervalHCTotalPktsQueue4": adGenEth24HrIntervalHCTotalPktsQueue4,
       "adGenEth24HrIntervalHCTotalPktsQueue5": adGenEth24HrIntervalHCTotalPktsQueue5,
       "adGenEth24HrIntervalHCTotalPktsQueue6": adGenEth24HrIntervalHCTotalPktsQueue6,
       "adGenEth24HrIntervalHCTotalPktsQueue7": adGenEth24HrIntervalHCTotalPktsQueue7,
       "adGenEth24HrIntervalHCOutLcv": adGenEth24HrIntervalHCOutLcv,
       "adGenEth24HrIntervalHCInLcv": adGenEth24HrIntervalHCInLcv,
       "adGenEth24HrIntervalHCValidData": adGenEth24HrIntervalHCValidData,
       "adGenEth24HrIntervalHCInAvgBitsPerSec": adGenEth24HrIntervalHCInAvgBitsPerSec,
       "adGenEth24HrIntervalHCInAvgPktsPerSec": adGenEth24HrIntervalHCInAvgPktsPerSec,
       "adGenEth24HrIntervalHCOutAvgBitsPerSec": adGenEth24HrIntervalHCOutAvgBitsPerSec,
       "adGenEth24HrIntervalHCOutAvgPktsPerSec": adGenEth24HrIntervalHCOutAvgPktsPerSec,
       "adGenEthPerfResetTable": adGenEthPerfResetTable,
       "adGenEthPerfResetEntry": adGenEthPerfResetEntry,
       "adGenEthPerfReset": adGenEthPerfReset,
       "adGenEthPerfThresholds": adGenEthPerfThresholds,
       "adGenEth15MinThreshTable": adGenEth15MinThreshTable,
       "adGenEth15MinThreshEntry": adGenEth15MinThreshEntry,
       "adGenEth15MinThreshInErrors": adGenEth15MinThreshInErrors,
       "adGenEth15MinThreshInDiscards": adGenEth15MinThreshInDiscards,
       "adGenEth15MinThreshInGiants": adGenEth15MinThreshInGiants,
       "adGenEth15MinThreshInRunts": adGenEth15MinThreshInRunts,
       "adGenEth15MinThreshInMulticastPkts": adGenEth15MinThreshInMulticastPkts,
       "adGenEth15MinThreshInBroadcastPkts": adGenEth15MinThreshInBroadcastPkts,
       "adGenEth15MinThreshInUnicastPkts": adGenEth15MinThreshInUnicastPkts,
       "adGenEth15MinThreshInUnknownProtocols": adGenEth15MinThreshInUnknownProtocols,
       "adGenEth15MinThreshInOctets": adGenEth15MinThreshInOctets,
       "adGenEth15MinThreshInPkts": adGenEth15MinThreshInPkts,
       "adGenEth15MinThreshInPkts64Octets": adGenEth15MinThreshInPkts64Octets,
       "adGenEth15MinThreshInPkts65to127Octets": adGenEth15MinThreshInPkts65to127Octets,
       "adGenEth15MinThreshInPkts128to255Octets": adGenEth15MinThreshInPkts128to255Octets,
       "adGenEth15MinThreshInPkts256to511Octets": adGenEth15MinThreshInPkts256to511Octets,
       "adGenEth15MinThreshInPkts512to1023Octets": adGenEth15MinThreshInPkts512to1023Octets,
       "adGenEth15MinThreshInPkts1024toMaxOctets": adGenEth15MinThreshInPkts1024toMaxOctets,
       "adGenEth15MinThreshOutErrors": adGenEth15MinThreshOutErrors,
       "adGenEth15MinThreshOutDiscards": adGenEth15MinThreshOutDiscards,
       "adGenEth15MinThreshOutMulticastPkts": adGenEth15MinThreshOutMulticastPkts,
       "adGenEth15MinThreshOutBroadcastPkts": adGenEth15MinThreshOutBroadcastPkts,
       "adGenEth15MinThreshOutUnicastPkts": adGenEth15MinThreshOutUnicastPkts,
       "adGenEth15MinThreshOutOctets": adGenEth15MinThreshOutOctets,
       "adGenEth15MinThreshOutPkts": adGenEth15MinThreshOutPkts,
       "adGenEth15MinThreshES": adGenEth15MinThreshES,
       "adGenEth15MinThreshLOSS": adGenEth15MinThreshLOSS,
       "adGenEth15MinThreshSEFS": adGenEth15MinThreshSEFS,
       "adGenEth15MinThreshSES": adGenEth15MinThreshSES,
       "adGenEth15MinThreshUAS": adGenEth15MinThreshUAS,
       "adGenEth15MinThreshOutLcv": adGenEth15MinThreshOutLcv,
       "adGenEth15MinThreshInLcv": adGenEth15MinThreshInLcv,
       "adGenEth24HrThreshTable": adGenEth24HrThreshTable,
       "adGenEth24HrThreshEntry": adGenEth24HrThreshEntry,
       "adGenEth24HrThreshInErrors": adGenEth24HrThreshInErrors,
       "adGenEth24HrThreshInDiscards": adGenEth24HrThreshInDiscards,
       "adGenEth24HrThreshInGiants": adGenEth24HrThreshInGiants,
       "adGenEth24HrThreshInRunts": adGenEth24HrThreshInRunts,
       "adGenEth24HrThreshInMulticastPkts": adGenEth24HrThreshInMulticastPkts,
       "adGenEth24HrThreshInBroadcastPkts": adGenEth24HrThreshInBroadcastPkts,
       "adGenEth24HrThreshOutLcv": adGenEth24HrThreshOutLcv,
       "adGenEth24HrThreshInLcv": adGenEth24HrThreshInLcv,
       "adGenEthPerformanceCountersTable": adGenEthPerformanceCountersTable,
       "adGenEthPerformanceCountersEntry": adGenEthPerformanceCountersEntry,
       "adGenEthInPackets": adGenEthInPackets,
       "adGenEthOutPackets": adGenEthOutPackets,
       "adGenEthInRunts": adGenEthInRunts,
       "adGenEthInGiants": adGenEthInGiants,
       "adGenEthInFrameErrors": adGenEthInFrameErrors,
       "adGenEthInFCSErrors": adGenEthInFCSErrors,
       "adGenEthInAvgPktsPerSec": adGenEthInAvgPktsPerSec,
       "adGenEthOutAvgPktsPerSec": adGenEthOutAvgPktsPerSec,
       "adGenEthInAvgBitsPerSec": adGenEthInAvgBitsPerSec,
       "adGenEthOutAvgBitsPerSec": adGenEthOutAvgBitsPerSec,
       "adGenEthTotalTxPacketsQueue0": adGenEthTotalTxPacketsQueue0,
       "adGenEthTotalTxPacketsQueue1": adGenEthTotalTxPacketsQueue1,
       "adGenEthTotalTxPacketsQueue2": adGenEthTotalTxPacketsQueue2,
       "adGenEthTotalTxPacketsQueue3": adGenEthTotalTxPacketsQueue3,
       "adGenEthTotalTxPacketsQueue4": adGenEthTotalTxPacketsQueue4,
       "adGenEthTotalTxPacketsQueue5": adGenEthTotalTxPacketsQueue5,
       "adGenEthTotalTxPacketsQueue6": adGenEthTotalTxPacketsQueue6,
       "adGenEthTotalTxPacketsQueue7": adGenEthTotalTxPacketsQueue7,
       "adGenEthDroppedPacketsQueue0": adGenEthDroppedPacketsQueue0,
       "adGenEthDroppedPacketsQueue1": adGenEthDroppedPacketsQueue1,
       "adGenEthDroppedPacketsQueue2": adGenEthDroppedPacketsQueue2,
       "adGenEthDroppedPacketsQueue3": adGenEthDroppedPacketsQueue3,
       "adGenEthDroppedPacketsQueue4": adGenEthDroppedPacketsQueue4,
       "adGenEthDroppedPacketsQueue5": adGenEthDroppedPacketsQueue5,
       "adGenEthDroppedPacketsQueue6": adGenEthDroppedPacketsQueue6,
       "adGenEthDroppedPacketsQueue7": adGenEthDroppedPacketsQueue7,
       "adGenEthInPeakUtilization": adGenEthInPeakUtilization,
       "adGenEthInAvgUtilization": adGenEthInAvgUtilization,
       "adGenEthOutPeakUtilization": adGenEthOutPeakUtilization,
       "adGenEthOutAvgUtilization": adGenEthOutAvgUtilization,
       "adGenEthDepthPacketsQueue0": adGenEthDepthPacketsQueue0,
       "adGenEthDepthPacketsQueue1": adGenEthDepthPacketsQueue1,
       "adGenEthDepthPacketsQueue2": adGenEthDepthPacketsQueue2,
       "adGenEthDepthPacketsQueue3": adGenEthDepthPacketsQueue3,
       "adGenEthDepthPacketsQueue4": adGenEthDepthPacketsQueue4,
       "adGenEthDepthPacketsQueue5": adGenEthDepthPacketsQueue5,
       "adGenEthDepthPacketsQueue6": adGenEthDepthPacketsQueue6,
       "adGenEthDepthPacketsQueue7": adGenEthDepthPacketsQueue7,
       "adGenEthHCInAvgPktsPerSec": adGenEthHCInAvgPktsPerSec,
       "adGenEthHCOutAvgPktsPerSec": adGenEthHCOutAvgPktsPerSec,
       "adGenEthHCInAvgBitsPerSec": adGenEthHCInAvgBitsPerSec,
       "adGenEthHCOutAvgBitsPerSec": adGenEthHCOutAvgBitsPerSec,
       "adGenEthPerformanceCountersHCTable": adGenEthPerformanceCountersHCTable,
       "adGenEthPerformanceCountersHCEntry": adGenEthPerformanceCountersHCEntry,
       "adGenEthCounterHCInPackets": adGenEthCounterHCInPackets,
       "adGenEthCounterHCOutPackets": adGenEthCounterHCOutPackets,
       "adGenEthCounterHCInBytes": adGenEthCounterHCInBytes,
       "adGenEthCounterHCOutBytes": adGenEthCounterHCOutBytes,
       "adGenEthCounterHCInUnicasts": adGenEthCounterHCInUnicasts,
       "adGenEthCounterHCOutUnicasts": adGenEthCounterHCOutUnicasts,
       "adGenEthCounterHCInBroadcasts": adGenEthCounterHCInBroadcasts,
       "adGenEthCounterHCOutBroadcasts": adGenEthCounterHCOutBroadcasts,
       "adGenEthCounterHCInMulticasts": adGenEthCounterHCInMulticasts,
       "adGenEthCounterHCOutMulticasts": adGenEthCounterHCOutMulticasts,
       "adGenEthCounterHCInErrors": adGenEthCounterHCInErrors,
       "adGenEthCounterHCOutErrors": adGenEthCounterHCOutErrors,
       "adGenEthCounterHCInDiscards": adGenEthCounterHCInDiscards,
       "adGenEthCounterHCOutDiscards": adGenEthCounterHCOutDiscards,
       "adGenEthCounterHCInLCVs": adGenEthCounterHCInLCVs,
       "adGenEthCounterHCOutLCVs": adGenEthCounterHCOutLCVs,
       "adGenEthCounterHCInRunts": adGenEthCounterHCInRunts,
       "adGenEthCounterHCInGiants": adGenEthCounterHCInGiants,
       "adGenEthCounterHCInFrameErrors": adGenEthCounterHCInFrameErrors,
       "adGenEthCounterHCInCRCErrors": adGenEthCounterHCInCRCErrors,
       "adGenEthMIB": adGenEthMIB}
)
