# SNMP MIB module (KYOCERA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/kyocera/KYOCERA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:50 2025
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

(hrDeviceIndex,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "hrDeviceIndex")

(PresentOnOff,
 prtMarkerIndex) = mibBuilder.importSymbols(
    "Printer-MIB",
    "PresentOnOff",
    "prtMarkerIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Kyocera_ObjectIdentity = ObjectIdentity
kyocera = _Kyocera_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347)
)
_KcPrinter_ObjectIdentity = ObjectIdentity
kcPrinter = _KcPrinter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43)
)
_KcprtGeneral_ObjectIdentity = ObjectIdentity
kcprtGeneral = _KcprtGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5)
)
_KcprtGeneralTable_Object = MibTable
kcprtGeneralTable = _KcprtGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1)
)
if mibBuilder.loadTexts:
    kcprtGeneralTable.setStatus("mandatory")
_KcprtGeneralEntry_Object = MibTableRow
kcprtGeneralEntry = _KcprtGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1)
)
kcprtGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kcprtGeneralEntry.setStatus("mandatory")


class _KcprtGeneralModelName_Type(DisplayString):
    """Custom type kcprtGeneralModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KcprtGeneralModelName_Type.__name__ = "DisplayString"
_KcprtGeneralModelName_Object = MibTableColumn
kcprtGeneralModelName = _KcprtGeneralModelName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 1),
    _KcprtGeneralModelName_Type()
)
kcprtGeneralModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtGeneralModelName.setStatus("mandatory")


class _KcprtOptionVersion_Type(DisplayString):
    """Custom type kcprtOptionVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_KcprtOptionVersion_Type.__name__ = "DisplayString"
_KcprtOptionVersion_Object = MibTableColumn
kcprtOptionVersion = _KcprtOptionVersion_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 2),
    _KcprtOptionVersion_Type()
)
kcprtOptionVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOptionVersion.setStatus("mandatory")


class _KcprtKpdlLevel_Type(Integer32):
    """Custom type kcprtKpdlLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_KcprtKpdlLevel_Type.__name__ = "Integer32"
_KcprtKpdlLevel_Object = MibTableColumn
kcprtKpdlLevel = _KcprtKpdlLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 3),
    _KcprtKpdlLevel_Type()
)
kcprtKpdlLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtKpdlLevel.setStatus("mandatory")


class _KcprtSystemUpTime_Type(Integer32):
    """Custom type kcprtSystemUpTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtSystemUpTime_Type.__name__ = "Integer32"
_KcprtSystemUpTime_Object = MibTableColumn
kcprtSystemUpTime = _KcprtSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 4),
    _KcprtSystemUpTime_Type()
)
kcprtSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSystemUpTime.setStatus("mandatory")


class _KcprtBinNumber_Type(Integer32):
    """Custom type kcprtBinNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtBinNumber_Type.__name__ = "Integer32"
_KcprtBinNumber_Object = MibTableColumn
kcprtBinNumber = _KcprtBinNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 5),
    _KcprtBinNumber_Type()
)
kcprtBinNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtBinNumber.setStatus("mandatory")


class _KcprtCardSlotCapacity_Type(Integer32):
    """Custom type kcprtCardSlotCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtCardSlotCapacity_Type.__name__ = "Integer32"
_KcprtCardSlotCapacity_Object = MibTableColumn
kcprtCardSlotCapacity = _KcprtCardSlotCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 6),
    _KcprtCardSlotCapacity_Type()
)
kcprtCardSlotCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCardSlotCapacity.setStatus("mandatory")


class _KcprtRomSlotNumber_Type(Integer32):
    """Custom type kcprtRomSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtRomSlotNumber_Type.__name__ = "Integer32"
_KcprtRomSlotNumber_Object = MibTableColumn
kcprtRomSlotNumber = _KcprtRomSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 7),
    _KcprtRomSlotNumber_Type()
)
kcprtRomSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtRomSlotNumber.setStatus("mandatory")


class _KcprtSimmSlotCapacity_Type(Integer32):
    """Custom type kcprtSimmSlotCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtSimmSlotCapacity_Type.__name__ = "Integer32"
_KcprtSimmSlotCapacity_Object = MibTableColumn
kcprtSimmSlotCapacity = _KcprtSimmSlotCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 8),
    _KcprtSimmSlotCapacity_Type()
)
kcprtSimmSlotCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSimmSlotCapacity.setStatus("mandatory")


class _KcprtSimmSlotUsed_Type(Integer32):
    """Custom type kcprtSimmSlotUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtSimmSlotUsed_Type.__name__ = "Integer32"
_KcprtSimmSlotUsed_Object = MibTableColumn
kcprtSimmSlotUsed = _KcprtSimmSlotUsed_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 9),
    _KcprtSimmSlotUsed_Type()
)
kcprtSimmSlotUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSimmSlotUsed.setStatus("mandatory")


class _KcprtOriginalMemorySize_Type(Integer32):
    """Custom type kcprtOriginalMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtOriginalMemorySize_Type.__name__ = "Integer32"
_KcprtOriginalMemorySize_Object = MibTableColumn
kcprtOriginalMemorySize = _KcprtOriginalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 10),
    _KcprtOriginalMemorySize_Type()
)
kcprtOriginalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOriginalMemorySize.setStatus("mandatory")


class _KcprtTotalMemorySize_Type(Integer32):
    """Custom type kcprtTotalMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtTotalMemorySize_Type.__name__ = "Integer32"
_KcprtTotalMemorySize_Object = MibTableColumn
kcprtTotalMemorySize = _KcprtTotalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 11),
    _KcprtTotalMemorySize_Type()
)
kcprtTotalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTotalMemorySize.setStatus("mandatory")


class _KcprtUserMemorySize_Type(Integer32):
    """Custom type kcprtUserMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtUserMemorySize_Type.__name__ = "Integer32"
_KcprtUserMemorySize_Object = MibTableColumn
kcprtUserMemorySize = _KcprtUserMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 12),
    _KcprtUserMemorySize_Type()
)
kcprtUserMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtUserMemorySize.setStatus("mandatory")


class _KcprtVirtualMemory_Type(Integer32):
    """Custom type kcprtVirtualMemory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 0),
          ("support", 1))
    )


_KcprtVirtualMemory_Type.__name__ = "Integer32"
_KcprtVirtualMemory_Object = MibTableColumn
kcprtVirtualMemory = _KcprtVirtualMemory_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 13),
    _KcprtVirtualMemory_Type()
)
kcprtVirtualMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtVirtualMemory.setStatus("mandatory")


class _KcprtPageMemorySize_Type(Integer32):
    """Custom type kcprtPageMemorySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("mem128KB", 1),
          ("mem256KB", 2),
          ("mem512KB", 3),
          ("memA4orLetter", 4),
          ("memLegal", 5),
          ("memwLetter", 6),
          ("memwLegal", 7))
    )


_KcprtPageMemorySize_Type.__name__ = "Integer32"
_KcprtPageMemorySize_Object = MibTableColumn
kcprtPageMemorySize = _KcprtPageMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 14),
    _KcprtPageMemorySize_Type()
)
kcprtPageMemorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtPageMemorySize.setStatus("mandatory")


class _KcprtHostBufferSize_Type(Integer32):
    """Custom type kcprtHostBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtHostBufferSize_Type.__name__ = "Integer32"
_KcprtHostBufferSize_Object = MibTableColumn
kcprtHostBufferSize = _KcprtHostBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 15),
    _KcprtHostBufferSize_Type()
)
kcprtHostBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBufferSize.setStatus("mandatory")


class _KcprtHostBuffer1stRate_Type(Integer32):
    """Custom type kcprtHostBuffer1stRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_KcprtHostBuffer1stRate_Type.__name__ = "Integer32"
_KcprtHostBuffer1stRate_Object = MibTableColumn
kcprtHostBuffer1stRate = _KcprtHostBuffer1stRate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 16),
    _KcprtHostBuffer1stRate_Type()
)
kcprtHostBuffer1stRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBuffer1stRate.setStatus("mandatory")


class _KcprtHostBuffer2ndRate_Type(Integer32):
    """Custom type kcprtHostBuffer2ndRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_KcprtHostBuffer2ndRate_Type.__name__ = "Integer32"
_KcprtHostBuffer2ndRate_Object = MibTableColumn
kcprtHostBuffer2ndRate = _KcprtHostBuffer2ndRate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 17),
    _KcprtHostBuffer2ndRate_Type()
)
kcprtHostBuffer2ndRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBuffer2ndRate.setStatus("mandatory")


class _KcprtHostBuffer3rdRate_Type(Integer32):
    """Custom type kcprtHostBuffer3rdRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_KcprtHostBuffer3rdRate_Type.__name__ = "Integer32"
_KcprtHostBuffer3rdRate_Object = MibTableColumn
kcprtHostBuffer3rdRate = _KcprtHostBuffer3rdRate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 18),
    _KcprtHostBuffer3rdRate_Type()
)
kcprtHostBuffer3rdRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBuffer3rdRate.setStatus("mandatory")


class _KcprtHostBufferOption_Type(Integer32):
    """Custom type kcprtHostBufferOption based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("fixed", 1))
    )


_KcprtHostBufferOption_Type.__name__ = "Integer32"
_KcprtHostBufferOption_Object = MibTableColumn
kcprtHostBufferOption = _KcprtHostBufferOption_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 19),
    _KcprtHostBufferOption_Type()
)
kcprtHostBufferOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBufferOption.setStatus("mandatory")


class _KcprtBufferXoffLevel_Type(Integer32):
    """Custom type kcprtBufferXoffLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtBufferXoffLevel_Type.__name__ = "Integer32"
_KcprtBufferXoffLevel_Object = MibTableColumn
kcprtBufferXoffLevel = _KcprtBufferXoffLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 20),
    _KcprtBufferXoffLevel_Type()
)
kcprtBufferXoffLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtBufferXoffLevel.setStatus("mandatory")


class _KcprtBufferXonLevel_Type(Integer32):
    """Custom type kcprtBufferXonLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtBufferXonLevel_Type.__name__ = "Integer32"
_KcprtBufferXonLevel_Object = MibTableColumn
kcprtBufferXonLevel = _KcprtBufferXonLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 21),
    _KcprtBufferXonLevel_Type()
)
kcprtBufferXonLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtBufferXonLevel.setStatus("mandatory")


class _KcprtFFTimeout_Type(Integer32):
    """Custom type kcprtFFTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtFFTimeout_Type.__name__ = "Integer32"
_KcprtFFTimeout_Object = MibTableColumn
kcprtFFTimeout = _KcprtFFTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 22),
    _KcprtFFTimeout_Type()
)
kcprtFFTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtFFTimeout.setStatus("mandatory")


class _KcprtSleepTimer_Type(Integer32):
    """Custom type kcprtSleepTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_KcprtSleepTimer_Type.__name__ = "Integer32"
_KcprtSleepTimer_Object = MibTableColumn
kcprtSleepTimer = _KcprtSleepTimer_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 23),
    _KcprtSleepTimer_Type()
)
kcprtSleepTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtSleepTimer.setStatus("mandatory")


class _KcprtWakeupStatusPage_Type(Integer32):
    """Custom type kcprtWakeupStatusPage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_KcprtWakeupStatusPage_Type.__name__ = "Integer32"
_KcprtWakeupStatusPage_Object = MibTableColumn
kcprtWakeupStatusPage = _KcprtWakeupStatusPage_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 24),
    _KcprtWakeupStatusPage_Type()
)
kcprtWakeupStatusPage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtWakeupStatusPage.setStatus("mandatory")


class _KcprtOnlineControl_Type(Integer32):
    """Custom type kcprtOnlineControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("offLine", 0),
          ("onLine", 1))
    )


_KcprtOnlineControl_Type.__name__ = "Integer32"
_KcprtOnlineControl_Object = MibTableColumn
kcprtOnlineControl = _KcprtOnlineControl_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 25),
    _KcprtOnlineControl_Type()
)
kcprtOnlineControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOnlineControl.setStatus("mandatory")


class _KcprtCopyCount_Type(Integer32):
    """Custom type kcprtCopyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_KcprtCopyCount_Type.__name__ = "Integer32"
_KcprtCopyCount_Object = MibTableColumn
kcprtCopyCount = _KcprtCopyCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 26),
    _KcprtCopyCount_Type()
)
kcprtCopyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtCopyCount.setStatus("mandatory")


class _KcprtContinueKey_Type(Integer32):
    """Custom type kcprtContinueKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("continue", 1))
    )


_KcprtContinueKey_Type.__name__ = "Integer32"
_KcprtContinueKey_Object = MibTableColumn
kcprtContinueKey = _KcprtContinueKey_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 27),
    _KcprtContinueKey_Type()
)
kcprtContinueKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtContinueKey.setStatus("mandatory")


class _KcprtSerialNumber_Type(DisplayString):
    """Custom type kcprtSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_KcprtSerialNumber_Type.__name__ = "DisplayString"
_KcprtSerialNumber_Object = MibTableColumn
kcprtSerialNumber = _KcprtSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 28),
    _KcprtSerialNumber_Type()
)
kcprtSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSerialNumber.setStatus("mandatory")


class _KcprtAssetNumber_Type(DisplayString):
    """Custom type kcprtAssetNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KcprtAssetNumber_Type.__name__ = "DisplayString"
_KcprtAssetNumber_Object = MibTableColumn
kcprtAssetNumber = _KcprtAssetNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 29),
    _KcprtAssetNumber_Type()
)
kcprtAssetNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtAssetNumber.setStatus("mandatory")


class _KcprtSignature_Type(OctetString):
    """Custom type kcprtSignature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KcprtSignature_Type.__name__ = "OctetString"
_KcprtSignature_Object = MibTableColumn
kcprtSignature = _KcprtSignature_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 30),
    _KcprtSignature_Type()
)
kcprtSignature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtSignature.setStatus("mandatory")


class _KcprtFirmParamCurrentRegister_Type(OctetString):
    """Custom type kcprtFirmParamCurrentRegister based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_KcprtFirmParamCurrentRegister_Type.__name__ = "OctetString"
_KcprtFirmParamCurrentRegister_Object = MibTableColumn
kcprtFirmParamCurrentRegister = _KcprtFirmParamCurrentRegister_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 31),
    _KcprtFirmParamCurrentRegister_Type()
)
kcprtFirmParamCurrentRegister.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtFirmParamCurrentRegister.setStatus("mandatory")


class _KcprtFirmParamCurrentValue_Type(OctetString):
    """Custom type kcprtFirmParamCurrentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtFirmParamCurrentValue_Type.__name__ = "OctetString"
_KcprtFirmParamCurrentValue_Object = MibTableColumn
kcprtFirmParamCurrentValue = _KcprtFirmParamCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 32),
    _KcprtFirmParamCurrentValue_Type()
)
kcprtFirmParamCurrentValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtFirmParamCurrentValue.setStatus("mandatory")


class _KcprtSleepMode_Type(Integer32):
    """Custom type kcprtSleepMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_KcprtSleepMode_Type.__name__ = "Integer32"
_KcprtSleepMode_Object = MibTableColumn
kcprtSleepMode = _KcprtSleepMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 33),
    _KcprtSleepMode_Type()
)
kcprtSleepMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtSleepMode.setStatus("mandatory")


class _KcprtAutoContinueMode_Type(Integer32):
    """Custom type kcprtAutoContinueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_KcprtAutoContinueMode_Type.__name__ = "Integer32"
_KcprtAutoContinueMode_Object = MibTableColumn
kcprtAutoContinueMode = _KcprtAutoContinueMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 34),
    _KcprtAutoContinueMode_Type()
)
kcprtAutoContinueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtAutoContinueMode.setStatus("mandatory")


class _KcprtAutoContinueTimer_Type(Integer32):
    """Custom type kcprtAutoContinueTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_KcprtAutoContinueTimer_Type.__name__ = "Integer32"
_KcprtAutoContinueTimer_Object = MibTableColumn
kcprtAutoContinueTimer = _KcprtAutoContinueTimer_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 35),
    _KcprtAutoContinueTimer_Type()
)
kcprtAutoContinueTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtAutoContinueTimer.setStatus("mandatory")


class _KcprtAbsoluteModelName_Type(DisplayString):
    """Custom type kcprtAbsoluteModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KcprtAbsoluteModelName_Type.__name__ = "DisplayString"
_KcprtAbsoluteModelName_Object = MibTableColumn
kcprtAbsoluteModelName = _KcprtAbsoluteModelName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 36),
    _KcprtAbsoluteModelName_Type()
)
kcprtAbsoluteModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAbsoluteModelName.setStatus("mandatory")


class _KcprtEquipmentID_Type(DisplayString):
    """Custom type kcprtEquipmentID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KcprtEquipmentID_Type.__name__ = "DisplayString"
_KcprtEquipmentID_Object = MibTableColumn
kcprtEquipmentID = _KcprtEquipmentID_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 37),
    _KcprtEquipmentID_Type()
)
kcprtEquipmentID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtEquipmentID.setStatus("mandatory")
_KcprtMaxCopyCount_Type = Integer32
_KcprtMaxCopyCount_Object = MibTableColumn
kcprtMaxCopyCount = _KcprtMaxCopyCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 1, 1, 38),
    _KcprtMaxCopyCount_Type()
)
kcprtMaxCopyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMaxCopyCount.setStatus("mandatory")
_KcprtCpuTable_Object = MibTable
kcprtCpuTable = _KcprtCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4)
)
if mibBuilder.loadTexts:
    kcprtCpuTable.setStatus("mandatory")
_KcprtCpuEntry_Object = MibTableRow
kcprtCpuEntry = _KcprtCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1)
)
kcprtCpuEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtCpuIndex"),
)
if mibBuilder.loadTexts:
    kcprtCpuEntry.setStatus("mandatory")
_KcprtCpuIndex_Type = Integer32
_KcprtCpuIndex_Object = MibTableColumn
kcprtCpuIndex = _KcprtCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 1),
    _KcprtCpuIndex_Type()
)
kcprtCpuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtCpuIndex.setStatus("mandatory")


class _KcprtCpuName_Type(DisplayString):
    """Custom type kcprtCpuName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtCpuName_Type.__name__ = "DisplayString"
_KcprtCpuName_Object = MibTableColumn
kcprtCpuName = _KcprtCpuName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 2),
    _KcprtCpuName_Type()
)
kcprtCpuName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCpuName.setStatus("mandatory")
_KcprtCpuClock_Type = Integer32
_KcprtCpuClock_Object = MibTableColumn
kcprtCpuClock = _KcprtCpuClock_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 3),
    _KcprtCpuClock_Type()
)
kcprtCpuClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCpuClock.setStatus("mandatory")


class _KcprtCpuRole_Type(Integer32):
    """Custom type kcprtCpuRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("engine", 0),
          ("controller", 1))
    )


_KcprtCpuRole_Type.__name__ = "Integer32"
_KcprtCpuRole_Object = MibTableColumn
kcprtCpuRole = _KcprtCpuRole_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 4),
    _KcprtCpuRole_Type()
)
kcprtCpuRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCpuRole.setStatus("mandatory")


class _KcprtFirmwareVersion_Type(DisplayString):
    """Custom type kcprtFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtFirmwareVersion_Type.__name__ = "DisplayString"
_KcprtFirmwareVersion_Object = MibTableColumn
kcprtFirmwareVersion = _KcprtFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 5),
    _KcprtFirmwareVersion_Type()
)
kcprtFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFirmwareVersion.setStatus("mandatory")


class _KcprtFirmwareUpdate_Type(Integer32):
    """Custom type kcprtFirmwareUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 3),
          ("disabled", 4))
    )


_KcprtFirmwareUpdate_Type.__name__ = "Integer32"
_KcprtFirmwareUpdate_Object = MibTableColumn
kcprtFirmwareUpdate = _KcprtFirmwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 5, 4, 1, 6),
    _KcprtFirmwareUpdate_Type()
)
kcprtFirmwareUpdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFirmwareUpdate.setStatus("mandatory")
_KcprtInput_ObjectIdentity = ObjectIdentity
kcprtInput = _KcprtInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8)
)
_KcprtInputTable_Object = MibTable
kcprtInputTable = _KcprtInputTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1)
)
if mibBuilder.loadTexts:
    kcprtInputTable.setStatus("mandatory")
_KcprtInputEntry_Object = MibTableRow
kcprtInputEntry = _KcprtInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1)
)
kcprtInputEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtInputIndex"),
)
if mibBuilder.loadTexts:
    kcprtInputEntry.setStatus("mandatory")
_KcprtInputIndex_Type = Integer32
_KcprtInputIndex_Object = MibTableColumn
kcprtInputIndex = _KcprtInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 1),
    _KcprtInputIndex_Type()
)
kcprtInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtInputIndex.setStatus("mandatory")


class _KcprtInputMPtrayMode_Type(Integer32):
    """Custom type kcprtInputMPtrayMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("cassette", 0),
          ("manual", 1),
          ("first", 2),
          ("notPresent", 5))
    )


_KcprtInputMPtrayMode_Type.__name__ = "Integer32"
_KcprtInputMPtrayMode_Object = MibTableColumn
kcprtInputMPtrayMode = _KcprtInputMPtrayMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 2),
    _KcprtInputMPtrayMode_Type()
)
kcprtInputMPtrayMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtInputMPtrayMode.setStatus("mandatory")


class _KcprtInputGroupMember_Type(Integer32):
    """Custom type kcprtInputGroupMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("member", 3),
          ("notMember", 4),
          ("alone", 5))
    )


_KcprtInputGroupMember_Type.__name__ = "Integer32"
_KcprtInputGroupMember_Object = MibTableColumn
kcprtInputGroupMember = _KcprtInputGroupMember_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 3),
    _KcprtInputGroupMember_Type()
)
kcprtInputGroupMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtInputGroupMember.setStatus("mandatory")
_KcprtInputMediaListIndex_Type = Integer32
_KcprtInputMediaListIndex_Object = MibTableColumn
kcprtInputMediaListIndex = _KcprtInputMediaListIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 4),
    _KcprtInputMediaListIndex_Type()
)
kcprtInputMediaListIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtInputMediaListIndex.setStatus("mandatory")


class _KcprtInputStatus_Type(Integer32):
    """Custom type kcprtInputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("down", 1))
    )


_KcprtInputStatus_Type.__name__ = "Integer32"
_KcprtInputStatus_Object = MibTableColumn
kcprtInputStatus = _KcprtInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 5),
    _KcprtInputStatus_Type()
)
kcprtInputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtInputStatus.setStatus("mandatory")
_KcprtInputDialPaperSize_Type = Integer32
_KcprtInputDialPaperSize_Object = MibTableColumn
kcprtInputDialPaperSize = _KcprtInputDialPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 6),
    _KcprtInputDialPaperSize_Type()
)
kcprtInputDialPaperSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtInputDialPaperSize.setStatus("mandatory")
_KcprtInputOtherPaperSize_Type = Integer32
_KcprtInputOtherPaperSize_Object = MibTableColumn
kcprtInputOtherPaperSize = _KcprtInputOtherPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 7),
    _KcprtInputOtherPaperSize_Type()
)
kcprtInputOtherPaperSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtInputOtherPaperSize.setStatus("mandatory")


class _PrtInputCustomDimFeedDirDeclared_Type(Integer32):
    """Custom type prtInputCustomDimFeedDirDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PrtInputCustomDimFeedDirDeclared_Type.__name__ = "Integer32"
_PrtInputCustomDimFeedDirDeclared_Object = MibTableColumn
prtInputCustomDimFeedDirDeclared = _PrtInputCustomDimFeedDirDeclared_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 8),
    _PrtInputCustomDimFeedDirDeclared_Type()
)
prtInputCustomDimFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputCustomDimFeedDirDeclared.setStatus("mandatory")


class _PrtInputCustomDimXFeedDirDeclared_Type(Integer32):
    """Custom type prtInputCustomDimXFeedDirDeclared based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_PrtInputCustomDimXFeedDirDeclared_Type.__name__ = "Integer32"
_PrtInputCustomDimXFeedDirDeclared_Object = MibTableColumn
prtInputCustomDimXFeedDirDeclared = _PrtInputCustomDimXFeedDirDeclared_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 9),
    _PrtInputCustomDimXFeedDirDeclared_Type()
)
prtInputCustomDimXFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prtInputCustomDimXFeedDirDeclared.setStatus("mandatory")
_KcprnInputMediaMatrix_Type = DisplayString
_KcprnInputMediaMatrix_Object = MibTableColumn
kcprnInputMediaMatrix = _KcprnInputMediaMatrix_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 10),
    _KcprnInputMediaMatrix_Type()
)
kcprnInputMediaMatrix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprnInputMediaMatrix.setStatus("mandatory")
_KcprnInputPaperSizeIndex_Type = Integer32
_KcprnInputPaperSizeIndex_Object = MibTableColumn
kcprnInputPaperSizeIndex = _KcprnInputPaperSizeIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 1, 1, 11),
    _KcprnInputPaperSizeIndex_Type()
)
kcprnInputPaperSizeIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprnInputPaperSizeIndex.setStatus("mandatory")
_KcprtInputGroupTable_Object = MibTable
kcprtInputGroupTable = _KcprtInputGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 2)
)
if mibBuilder.loadTexts:
    kcprtInputGroupTable.setStatus("mandatory")
_KcprtInputGroupEntry_Object = MibTableRow
kcprtInputGroupEntry = _KcprtInputGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 2, 1)
)
kcprtInputGroupEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtInputGroupIndex"),
)
if mibBuilder.loadTexts:
    kcprtInputGroupEntry.setStatus("mandatory")
_KcprtInputGroupIndex_Type = Integer32
_KcprtInputGroupIndex_Object = MibTableColumn
kcprtInputGroupIndex = _KcprtInputGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 2, 1, 1),
    _KcprtInputGroupIndex_Type()
)
kcprtInputGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtInputGroupIndex.setStatus("mandatory")


class _KcprtInputGroupMode_Type(Integer32):
    """Custom type kcprtInputGroupMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("group", 1),
          ("size", 2),
          ("all", 3))
    )


_KcprtInputGroupMode_Type.__name__ = "Integer32"
_KcprtInputGroupMode_Object = MibTableColumn
kcprtInputGroupMode = _KcprtInputGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 8, 2, 1, 2),
    _KcprtInputGroupMode_Type()
)
kcprtInputGroupMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtInputGroupMode.setStatus("mandatory")
_KcprtOutput_ObjectIdentity = ObjectIdentity
kcprtOutput = _KcprtOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9)
)
_KcprtOutputTable_Object = MibTable
kcprtOutputTable = _KcprtOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1)
)
if mibBuilder.loadTexts:
    kcprtOutputTable.setStatus("mandatory")
_KcprtOutputEntry_Object = MibTableRow
kcprtOutputEntry = _KcprtOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1)
)
kcprtOutputEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtOutputIndex"),
)
if mibBuilder.loadTexts:
    kcprtOutputEntry.setStatus("mandatory")
_KcprtOutputIndex_Type = Integer32
_KcprtOutputIndex_Object = MibTableColumn
kcprtOutputIndex = _KcprtOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 1),
    _KcprtOutputIndex_Type()
)
kcprtOutputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtOutputIndex.setStatus("mandatory")


class _KcprtOutputMode_Type(Integer32):
    """Custom type kcprtOutputMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sorter", 0),
          ("collator", 1),
          ("stacker", 2),
          ("mailbox", 3))
    )


_KcprtOutputMode_Type.__name__ = "Integer32"
_KcprtOutputMode_Object = MibTableColumn
kcprtOutputMode = _KcprtOutputMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 2),
    _KcprtOutputMode_Type()
)
kcprtOutputMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputMode.setStatus("mandatory")


class _KcprtOutputMultiMode_Type(Integer32):
    """Custom type kcprtOutputMultiMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("id-specific", 1),
          ("if-specific", 2))
    )


_KcprtOutputMultiMode_Type.__name__ = "Integer32"
_KcprtOutputMultiMode_Object = MibTableColumn
kcprtOutputMultiMode = _KcprtOutputMultiMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 3),
    _KcprtOutputMultiMode_Type()
)
kcprtOutputMultiMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputMultiMode.setStatus("mandatory")
_KcprtOutputGroupNumber_Type = Integer32
_KcprtOutputGroupNumber_Object = MibTableColumn
kcprtOutputGroupNumber = _KcprtOutputGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 4),
    _KcprtOutputGroupNumber_Type()
)
kcprtOutputGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputGroupNumber.setStatus("mandatory")
_KcprtOutputDefaultGroup_Type = Integer32
_KcprtOutputDefaultGroup_Object = MibTableColumn
kcprtOutputDefaultGroup = _KcprtOutputDefaultGroup_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 5),
    _KcprtOutputDefaultGroup_Type()
)
kcprtOutputDefaultGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputDefaultGroup.setStatus("mandatory")


class _KcprtOutputBulkStatus_Type(Integer32):
    """Custom type kcprtOutputBulkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notFull", 0),
          ("full", 1))
    )


_KcprtOutputBulkStatus_Type.__name__ = "Integer32"
_KcprtOutputBulkStatus_Object = MibTableColumn
kcprtOutputBulkStatus = _KcprtOutputBulkStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 6),
    _KcprtOutputBulkStatus_Type()
)
kcprtOutputBulkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputBulkStatus.setStatus("mandatory")
_KcprtOutputTrayMaxCapacity_Type = Integer32
_KcprtOutputTrayMaxCapacity_Object = MibTableColumn
kcprtOutputTrayMaxCapacity = _KcprtOutputTrayMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 7),
    _KcprtOutputTrayMaxCapacity_Type()
)
kcprtOutputTrayMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayMaxCapacity.setStatus("mandatory")
_KcprtStapler_Type = PresentOnOff
_KcprtStapler_Object = MibTableColumn
kcprtStapler = _KcprtStapler_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 8),
    _KcprtStapler_Type()
)
kcprtStapler.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtStapler.setStatus("mandatory")
_KcprtStaplerConsumableState_Type = Integer32
_KcprtStaplerConsumableState_Object = MibTableColumn
kcprtStaplerConsumableState = _KcprtStaplerConsumableState_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 9),
    _KcprtStaplerConsumableState_Type()
)
kcprtStaplerConsumableState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtStaplerConsumableState.setStatus("mandatory")


class _KcprtOutputActionOnFull_Type(Integer32):
    """Custom type kcprtOutputActionOnFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("printStoppedWithMessage", 0),
          ("printContinue", 1))
    )


_KcprtOutputActionOnFull_Type.__name__ = "Integer32"
_KcprtOutputActionOnFull_Object = MibTableColumn
kcprtOutputActionOnFull = _KcprtOutputActionOnFull_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 10),
    _KcprtOutputActionOnFull_Type()
)
kcprtOutputActionOnFull.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputActionOnFull.setStatus("mandatory")


class _KcprtOutputPunchStatus_Type(Integer32):
    """Custom type kcprtOutputPunchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enabled", 1))
    )


_KcprtOutputPunchStatus_Type.__name__ = "Integer32"
_KcprtOutputPunchStatus_Object = MibTableColumn
kcprtOutputPunchStatus = _KcprtOutputPunchStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 11),
    _KcprtOutputPunchStatus_Type()
)
kcprtOutputPunchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputPunchStatus.setStatus("mandatory")


class _KcprtOutputStatus_Type(Integer32):
    """Custom type kcprtOutputStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("ready", 0),
          ("down", 1))
    )


_KcprtOutputStatus_Type.__name__ = "Integer32"
_KcprtOutputStatus_Object = MibTableColumn
kcprtOutputStatus = _KcprtOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 1, 1, 12),
    _KcprtOutputStatus_Type()
)
kcprtOutputStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputStatus.setStatus("mandatory")
_KcprtTrayGroupTable_Object = MibTable
kcprtTrayGroupTable = _KcprtTrayGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2)
)
if mibBuilder.loadTexts:
    kcprtTrayGroupTable.setStatus("mandatory")
_KcprtTrayGroupEntry_Object = MibTableRow
kcprtTrayGroupEntry = _KcprtTrayGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1)
)
kcprtTrayGroupEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtOutputIndex"),
    (0, "KYOCERA-MIB", "kcprtTrayGroupIndex"),
)
if mibBuilder.loadTexts:
    kcprtTrayGroupEntry.setStatus("mandatory")
_KcprtTrayGroupIndex_Type = Integer32
_KcprtTrayGroupIndex_Object = MibTableColumn
kcprtTrayGroupIndex = _KcprtTrayGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1, 1),
    _KcprtTrayGroupIndex_Type()
)
kcprtTrayGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtTrayGroupIndex.setStatus("mandatory")
_KcprtTrayGroupBeginIndex_Type = Integer32
_KcprtTrayGroupBeginIndex_Object = MibTableColumn
kcprtTrayGroupBeginIndex = _KcprtTrayGroupBeginIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1, 2),
    _KcprtTrayGroupBeginIndex_Type()
)
kcprtTrayGroupBeginIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayGroupBeginIndex.setStatus("mandatory")
_KcprtTrayGroupEndIndex_Type = Integer32
_KcprtTrayGroupEndIndex_Object = MibTableColumn
kcprtTrayGroupEndIndex = _KcprtTrayGroupEndIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 2, 1, 3),
    _KcprtTrayGroupEndIndex_Type()
)
kcprtTrayGroupEndIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayGroupEndIndex.setStatus("mandatory")
_KcprtOutputTrayTable_Object = MibTable
kcprtOutputTrayTable = _KcprtOutputTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3)
)
if mibBuilder.loadTexts:
    kcprtOutputTrayTable.setStatus("mandatory")
_KcprtOutputTrayEntry_Object = MibTableRow
kcprtOutputTrayEntry = _KcprtOutputTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1)
)
kcprtOutputTrayEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtOutputIndex"),
    (0, "KYOCERA-MIB", "kcprtOutputTrayIndex"),
)
if mibBuilder.loadTexts:
    kcprtOutputTrayEntry.setStatus("mandatory")
_KcprtOutputTrayIndex_Type = Integer32
_KcprtOutputTrayIndex_Object = MibTableColumn
kcprtOutputTrayIndex = _KcprtOutputTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 1),
    _KcprtOutputTrayIndex_Type()
)
kcprtOutputTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtOutputTrayIndex.setStatus("mandatory")
_KcprtOutputTrayOrder_Type = Integer32
_KcprtOutputTrayOrder_Object = MibTableColumn
kcprtOutputTrayOrder = _KcprtOutputTrayOrder_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 2),
    _KcprtOutputTrayOrder_Type()
)
kcprtOutputTrayOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayOrder.setStatus("mandatory")
_KcprtOutputTrayGroup_Type = Integer32
_KcprtOutputTrayGroup_Object = MibTableColumn
kcprtOutputTrayGroup = _KcprtOutputTrayGroup_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 3),
    _KcprtOutputTrayGroup_Type()
)
kcprtOutputTrayGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayGroup.setStatus("mandatory")
_KcprtOutputTrayCount_Type = Integer32
_KcprtOutputTrayCount_Object = MibTableColumn
kcprtOutputTrayCount = _KcprtOutputTrayCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 4),
    _KcprtOutputTrayCount_Type()
)
kcprtOutputTrayCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtOutputTrayCount.setStatus("mandatory")


class _KcprtOutputTrayName_Type(DisplayString):
    """Custom type kcprtOutputTrayName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KcprtOutputTrayName_Type.__name__ = "DisplayString"
_KcprtOutputTrayName_Object = MibTableColumn
kcprtOutputTrayName = _KcprtOutputTrayName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 3, 1, 5),
    _KcprtOutputTrayName_Type()
)
kcprtOutputTrayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtOutputTrayName.setStatus("mandatory")
_KcprtPunchGroupTable_Object = MibTable
kcprtPunchGroupTable = _KcprtPunchGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 4)
)
if mibBuilder.loadTexts:
    kcprtPunchGroupTable.setStatus("mandatory")
_KcprtPunchGroupEntry_Object = MibTableRow
kcprtPunchGroupEntry = _KcprtPunchGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 4, 1)
)
kcprtPunchGroupEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtPunchGroupIndex"),
)
if mibBuilder.loadTexts:
    kcprtPunchGroupEntry.setStatus("mandatory")
_KcprtPunchGroupIndex_Type = Integer32
_KcprtPunchGroupIndex_Object = MibTableColumn
kcprtPunchGroupIndex = _KcprtPunchGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 4, 1, 1),
    _KcprtPunchGroupIndex_Type()
)
kcprtPunchGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtPunchGroupIndex.setStatus("mandatory")


class _KcprtPunchGroupName_Type(DisplayString):
    """Custom type kcprtPunchGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KcprtPunchGroupName_Type.__name__ = "DisplayString"
_KcprtPunchGroupName_Object = MibTableColumn
kcprtPunchGroupName = _KcprtPunchGroupName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 4, 1, 2),
    _KcprtPunchGroupName_Type()
)
kcprtPunchGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPunchGroupName.setStatus("mandatory")
_KcprtPunchGroupHoleNumber_Type = Integer32
_KcprtPunchGroupHoleNumber_Object = MibTableColumn
kcprtPunchGroupHoleNumber = _KcprtPunchGroupHoleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 4, 1, 3),
    _KcprtPunchGroupHoleNumber_Type()
)
kcprtPunchGroupHoleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPunchGroupHoleNumber.setStatus("mandatory")


class _KcprtPunchGroupType_Type(DisplayString):
    """Custom type kcprtPunchGroupType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_KcprtPunchGroupType_Type.__name__ = "DisplayString"
_KcprtPunchGroupType_Object = MibTableColumn
kcprtPunchGroupType = _KcprtPunchGroupType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 9, 4, 1, 4),
    _KcprtPunchGroupType_Type()
)
kcprtPunchGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPunchGroupType.setStatus("mandatory")
_KcprtMarker_ObjectIdentity = ObjectIdentity
kcprtMarker = _KcprtMarker_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10)
)
_KcprtMarkerTable_Object = MibTable
kcprtMarkerTable = _KcprtMarkerTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1)
)
if mibBuilder.loadTexts:
    kcprtMarkerTable.setStatus("mandatory")
_KcprtMarkerEntry_Object = MibTableRow
kcprtMarkerEntry = _KcprtMarkerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1)
)
kcprtMarkerEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "Printer-MIB", "prtMarkerIndex"),
)
if mibBuilder.loadTexts:
    kcprtMarkerEntry.setStatus("mandatory")
_KcprtMarkerIndex_Type = Integer32
_KcprtMarkerIndex_Object = MibTableColumn
kcprtMarkerIndex = _KcprtMarkerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 1),
    _KcprtMarkerIndex_Type()
)
kcprtMarkerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMarkerIndex.setStatus("mandatory")


class _KcprtMarkerKirLevel_Type(Integer32):
    """Custom type kcprtMarkerKirLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offOrNotSupport", 0),
          ("light", 1),
          ("medium", 2),
          ("dark", 3))
    )


_KcprtMarkerKirLevel_Type.__name__ = "Integer32"
_KcprtMarkerKirLevel_Object = MibTableColumn
kcprtMarkerKirLevel = _KcprtMarkerKirLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 2),
    _KcprtMarkerKirLevel_Type()
)
kcprtMarkerKirLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerKirLevel.setStatus("mandatory")


class _KcprtMarkerEcoprintLevel_Type(Integer32):
    """Custom type kcprtMarkerEcoprintLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("offOrNotSupport", 0),
          ("light", 1),
          ("medium", 2),
          ("dark", 3))
    )


_KcprtMarkerEcoprintLevel_Type.__name__ = "Integer32"
_KcprtMarkerEcoprintLevel_Object = MibTableColumn
kcprtMarkerEcoprintLevel = _KcprtMarkerEcoprintLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 3),
    _KcprtMarkerEcoprintLevel_Type()
)
kcprtMarkerEcoprintLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerEcoprintLevel.setStatus("mandatory")
_KcprtMarkerAddressabilityFeedDirDeclared_Type = Integer32
_KcprtMarkerAddressabilityFeedDirDeclared_Object = MibTableColumn
kcprtMarkerAddressabilityFeedDirDeclared = _KcprtMarkerAddressabilityFeedDirDeclared_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 4),
    _KcprtMarkerAddressabilityFeedDirDeclared_Type()
)
kcprtMarkerAddressabilityFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerAddressabilityFeedDirDeclared.setStatus("mandatory")
_KcprtMarkerAddressabilityXFeedDirDeclared_Type = Integer32
_KcprtMarkerAddressabilityXFeedDirDeclared_Object = MibTableColumn
kcprtMarkerAddressabilityXFeedDirDeclared = _KcprtMarkerAddressabilityXFeedDirDeclared_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 5),
    _KcprtMarkerAddressabilityXFeedDirDeclared_Type()
)
kcprtMarkerAddressabilityXFeedDirDeclared.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerAddressabilityXFeedDirDeclared.setStatus("mandatory")
_KcprtMarkerAddressabilityFeedDirChosen_Type = Integer32
_KcprtMarkerAddressabilityFeedDirChosen_Object = MibTableColumn
kcprtMarkerAddressabilityFeedDirChosen = _KcprtMarkerAddressabilityFeedDirChosen_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 6),
    _KcprtMarkerAddressabilityFeedDirChosen_Type()
)
kcprtMarkerAddressabilityFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMarkerAddressabilityFeedDirChosen.setStatus("mandatory")
_KcprtMarkerAddressabilityXFeedDirChosen_Type = Integer32
_KcprtMarkerAddressabilityXFeedDirChosen_Object = MibTableColumn
kcprtMarkerAddressabilityXFeedDirChosen = _KcprtMarkerAddressabilityXFeedDirChosen_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 7),
    _KcprtMarkerAddressabilityXFeedDirChosen_Type()
)
kcprtMarkerAddressabilityXFeedDirChosen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMarkerAddressabilityXFeedDirChosen.setStatus("mandatory")
_KcprtMarkerDrumCounter_Type = Integer32
_KcprtMarkerDrumCounter_Object = MibTableColumn
kcprtMarkerDrumCounter = _KcprtMarkerDrumCounter_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 8),
    _KcprtMarkerDrumCounter_Type()
)
kcprtMarkerDrumCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMarkerDrumCounter.setStatus("mandatory")


class _KcprtMarkerColorMode_Type(Integer32):
    """Custom type kcprtMarkerColorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("monochrome", 1),
          ("color", 4))
    )


_KcprtMarkerColorMode_Type.__name__ = "Integer32"
_KcprtMarkerColorMode_Object = MibTableColumn
kcprtMarkerColorMode = _KcprtMarkerColorMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 9),
    _KcprtMarkerColorMode_Type()
)
kcprtMarkerColorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerColorMode.setStatus("mandatory")
_KcprtMarkerBitsPerPixel_Type = Integer32
_KcprtMarkerBitsPerPixel_Object = MibTableColumn
kcprtMarkerBitsPerPixel = _KcprtMarkerBitsPerPixel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 10),
    _KcprtMarkerBitsPerPixel_Type()
)
kcprtMarkerBitsPerPixel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerBitsPerPixel.setStatus("mandatory")


class _KcprtMarkerGlossMode_Type(Integer32):
    """Custom type kcprtMarkerGlossMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("low", 0),
          ("high", 1))
    )


_KcprtMarkerGlossMode_Type.__name__ = "Integer32"
_KcprtMarkerGlossMode_Object = MibTableColumn
kcprtMarkerGlossMode = _KcprtMarkerGlossMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 11),
    _KcprtMarkerGlossMode_Type()
)
kcprtMarkerGlossMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMarkerGlossMode.setStatus("mandatory")
_KcprtMarkerServiceCount_Type = Integer32
_KcprtMarkerServiceCount_Object = MibTableColumn
kcprtMarkerServiceCount = _KcprtMarkerServiceCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 10, 1, 1, 12),
    _KcprtMarkerServiceCount_Type()
)
kcprtMarkerServiceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMarkerServiceCount.setStatus("mandatory")
_KcprtColorant_ObjectIdentity = ObjectIdentity
kcprtColorant = _KcprtColorant_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12)
)
_KcprtColorantGeneralTable_Object = MibTable
kcprtColorantGeneralTable = _KcprtColorantGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12, 1)
)
if mibBuilder.loadTexts:
    kcprtColorantGeneralTable.setStatus("mandatory")
_KcprtColorantGeneralEntry_Object = MibTableRow
kcprtColorantGeneralEntry = _KcprtColorantGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12, 1, 1)
)
kcprtColorantGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kcprtColorantGeneralEntry.setStatus("mandatory")


class _KcprtColorQuality_Type(Integer32):
    """Custom type kcprtColorQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("quick", 1),
          ("fine", 2),
          ("presentation", 3))
    )


_KcprtColorQuality_Type.__name__ = "Integer32"
_KcprtColorQuality_Object = MibTableColumn
kcprtColorQuality = _KcprtColorQuality_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12, 1, 1, 1),
    _KcprtColorQuality_Type()
)
kcprtColorQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtColorQuality.setStatus("optional")


class _KcprtColorMatching_Type(Integer32):
    """Custom type kcprtColorMatching based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("auto", 1),
          ("vivid", 2),
          ("display", 3))
    )


_KcprtColorMatching_Type.__name__ = "Integer32"
_KcprtColorMatching_Object = MibTableColumn
kcprtColorMatching = _KcprtColorMatching_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12, 1, 1, 2),
    _KcprtColorMatching_Type()
)
kcprtColorMatching.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtColorMatching.setStatus("optional")


class _KcprtColorantIdentifier_Type(OctetString):
    """Custom type kcprtColorantIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_KcprtColorantIdentifier_Type.__name__ = "OctetString"
_KcprtColorantIdentifier_Object = MibTableColumn
kcprtColorantIdentifier = _KcprtColorantIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12, 1, 1, 3),
    _KcprtColorantIdentifier_Type()
)
kcprtColorantIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtColorantIdentifier.setStatus("optional")


class _KcprtRGBSimulation_Type(Integer32):
    """Custom type kcprtRGBSimulation based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("smtpe240m", 1),
          ("hdtv", 2),
          ("trinitron", 3),
          ("applergb", 4),
          ("ntsc", 5),
          ("kcrgb", 6),
          ("custom", 7))
    )


_KcprtRGBSimulation_Type.__name__ = "Integer32"
_KcprtRGBSimulation_Object = MibTableColumn
kcprtRGBSimulation = _KcprtRGBSimulation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12, 1, 1, 4),
    _KcprtRGBSimulation_Type()
)
kcprtRGBSimulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtRGBSimulation.setStatus("optional")


class _KcprtCMYKSimulation_Type(Integer32):
    """Custom type kcprtCMYKSimulation based on Integer32"""
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
        *(("normal", 0),
          ("none", 1),
          ("swop", 2),
          ("euroscale", 3),
          ("toyo", 4),
          ("dic", 5))
    )


_KcprtCMYKSimulation_Type.__name__ = "Integer32"
_KcprtCMYKSimulation_Object = MibTableColumn
kcprtCMYKSimulation = _KcprtCMYKSimulation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 12, 1, 1, 5),
    _KcprtCMYKSimulation_Type()
)
kcprtCMYKSimulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtCMYKSimulation.setStatus("optional")
_KcprtChannel_ObjectIdentity = ObjectIdentity
kcprtChannel = _KcprtChannel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14)
)
_KcprtChannelTable_Object = MibTable
kcprtChannelTable = _KcprtChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1)
)
if mibBuilder.loadTexts:
    kcprtChannelTable.setStatus("mandatory")
_KcprtChannelEntry_Object = MibTableRow
kcprtChannelEntry = _KcprtChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1)
)
kcprtChannelEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtChannelIndex"),
)
if mibBuilder.loadTexts:
    kcprtChannelEntry.setStatus("mandatory")
_KcprtChannelIndex_Type = Integer32
_KcprtChannelIndex_Object = MibTableColumn
kcprtChannelIndex = _KcprtChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 1),
    _KcprtChannelIndex_Type()
)
kcprtChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtChannelIndex.setStatus("mandatory")


class _KcprtChannelMode_Type(Integer32):
    """Custom type kcprtChannelMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("through", 0),
          ("hexDump", 1))
    )


_KcprtChannelMode_Type.__name__ = "Integer32"
_KcprtChannelMode_Object = MibTableColumn
kcprtChannelMode = _KcprtChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 2),
    _KcprtChannelMode_Type()
)
kcprtChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtChannelMode.setStatus("mandatory")


class _KcprtChannelCopyCount_Type(Integer32):
    """Custom type kcprtChannelCopyCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_KcprtChannelCopyCount_Type.__name__ = "Integer32"
_KcprtChannelCopyCount_Object = MibTableColumn
kcprtChannelCopyCount = _KcprtChannelCopyCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 3),
    _KcprtChannelCopyCount_Type()
)
kcprtChannelCopyCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtChannelCopyCount.setStatus("mandatory")
_KcprtChannelResolution_Type = Integer32
_KcprtChannelResolution_Object = MibTableColumn
kcprtChannelResolution = _KcprtChannelResolution_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 4),
    _KcprtChannelResolution_Type()
)
kcprtChannelResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtChannelResolution.setStatus("mandatory")
_KcprtChannelPaperSize_Type = Integer32
_KcprtChannelPaperSize_Object = MibTableColumn
kcprtChannelPaperSize = _KcprtChannelPaperSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 5),
    _KcprtChannelPaperSize_Type()
)
kcprtChannelPaperSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtChannelPaperSize.setStatus("mandatory")
_KcprtHostBufferRatio_Type = Integer32
_KcprtHostBufferRatio_Object = MibTableColumn
kcprtHostBufferRatio = _KcprtHostBufferRatio_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 6),
    _KcprtHostBufferRatio_Type()
)
kcprtHostBufferRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtHostBufferRatio.setStatus("optional")


class _KcprtChannelErrorCounter_Type(Integer32):
    """Custom type kcprtChannelErrorCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtChannelErrorCounter_Type.__name__ = "Integer32"
_KcprtChannelErrorCounter_Object = MibTableColumn
kcprtChannelErrorCounter = _KcprtChannelErrorCounter_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 14, 1, 1, 7),
    _KcprtChannelErrorCounter_Type()
)
kcprtChannelErrorCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtChannelErrorCounter.setStatus("optional")
_KcprtBuzzer_ObjectIdentity = ObjectIdentity
kcprtBuzzer = _KcprtBuzzer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17)
)
_KcprtBuzzerTable_Object = MibTable
kcprtBuzzerTable = _KcprtBuzzerTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17, 1)
)
if mibBuilder.loadTexts:
    kcprtBuzzerTable.setStatus("mandatory")
_KcprtBuzzerEntry_Object = MibTableRow
kcprtBuzzerEntry = _KcprtBuzzerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17, 1, 1)
)
kcprtBuzzerEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtBuzzerIndex"),
)
if mibBuilder.loadTexts:
    kcprtBuzzerEntry.setStatus("mandatory")
_KcprtBuzzerIndex_Type = Integer32
_KcprtBuzzerIndex_Object = MibTableColumn
kcprtBuzzerIndex = _KcprtBuzzerIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17, 1, 1, 1),
    _KcprtBuzzerIndex_Type()
)
kcprtBuzzerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtBuzzerIndex.setStatus("mandatory")


class _KcprtBuzzerOnTime_Type(Integer32):
    """Custom type kcprtBuzzerOnTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_KcprtBuzzerOnTime_Type.__name__ = "Integer32"
_KcprtBuzzerOnTime_Object = MibTableColumn
kcprtBuzzerOnTime = _KcprtBuzzerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17, 1, 1, 2),
    _KcprtBuzzerOnTime_Type()
)
kcprtBuzzerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtBuzzerOnTime.setStatus("mandatory")


class _KcprtBuzzerOffTime_Type(Integer32):
    """Custom type kcprtBuzzerOffTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )


_KcprtBuzzerOffTime_Type.__name__ = "Integer32"
_KcprtBuzzerOffTime_Object = MibTableColumn
kcprtBuzzerOffTime = _KcprtBuzzerOffTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17, 1, 1, 3),
    _KcprtBuzzerOffTime_Type()
)
kcprtBuzzerOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtBuzzerOffTime.setStatus("mandatory")


class _KcprtBuzzerMode_Type(Integer32):
    """Custom type kcprtBuzzerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_KcprtBuzzerMode_Type.__name__ = "Integer32"
_KcprtBuzzerMode_Object = MibTableColumn
kcprtBuzzerMode = _KcprtBuzzerMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17, 1, 1, 4),
    _KcprtBuzzerMode_Type()
)
kcprtBuzzerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtBuzzerMode.setStatus("mandatory")


class _KcprtBuzzerTone_Type(Integer32):
    """Custom type kcprtBuzzerTone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30000),
    )


_KcprtBuzzerTone_Type.__name__ = "Integer32"
_KcprtBuzzerTone_Object = MibTableColumn
kcprtBuzzerTone = _KcprtBuzzerTone_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 17, 1, 1, 5),
    _KcprtBuzzerTone_Type()
)
kcprtBuzzerTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtBuzzerTone.setStatus("mandatory")
_KcprtAlert_ObjectIdentity = ObjectIdentity
kcprtAlert = _KcprtAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18)
)
_KcprtAlertTable_Object = MibTable
kcprtAlertTable = _KcprtAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 1)
)
if mibBuilder.loadTexts:
    kcprtAlertTable.setStatus("mandatory")
_KcprtAlertEntry_Object = MibTableRow
kcprtAlertEntry = _KcprtAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 1, 1)
)
kcprtAlertEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtAlertIndex"),
)
if mibBuilder.loadTexts:
    kcprtAlertEntry.setStatus("mandatory")
_KcprtAlertIndex_Type = Integer32
_KcprtAlertIndex_Object = MibTableColumn
kcprtAlertIndex = _KcprtAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 1, 1, 1),
    _KcprtAlertIndex_Type()
)
kcprtAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtAlertIndex.setStatus("mandatory")


class _KcprtAlertInformation_Type(OctetString):
    """Custom type kcprtAlertInformation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_KcprtAlertInformation_Type.__name__ = "OctetString"
_KcprtAlertInformation_Object = MibTableColumn
kcprtAlertInformation = _KcprtAlertInformation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 1, 1, 2),
    _KcprtAlertInformation_Type()
)
kcprtAlertInformation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertInformation.setStatus("mandatory")
_KcprtAlertStateTable_Object = MibTable
kcprtAlertStateTable = _KcprtAlertStateTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 2)
)
if mibBuilder.loadTexts:
    kcprtAlertStateTable.setStatus("mandatory")
_KcprtAlertStateEntry_Object = MibTableRow
kcprtAlertStateEntry = _KcprtAlertStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 2, 1)
)
kcprtAlertStateEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtAlertStateDisplayIndex"),
)
if mibBuilder.loadTexts:
    kcprtAlertStateEntry.setStatus("mandatory")
_KcprtAlertStateDisplayIndex_Type = Integer32
_KcprtAlertStateDisplayIndex_Object = MibTableColumn
kcprtAlertStateDisplayIndex = _KcprtAlertStateDisplayIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 2, 1, 1),
    _KcprtAlertStateDisplayIndex_Type()
)
kcprtAlertStateDisplayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtAlertStateDisplayIndex.setStatus("mandatory")


class _KcprtAlertStateDisplay_Type(DisplayString):
    """Custom type kcprtAlertStateDisplay based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtAlertStateDisplay_Type.__name__ = "DisplayString"
_KcprtAlertStateDisplay_Object = MibTableColumn
kcprtAlertStateDisplay = _KcprtAlertStateDisplay_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 2, 1, 2),
    _KcprtAlertStateDisplay_Type()
)
kcprtAlertStateDisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertStateDisplay.setStatus("mandatory")
_KcprtAlertStateCode_Type = Integer32
_KcprtAlertStateCode_Object = MibTableColumn
kcprtAlertStateCode = _KcprtAlertStateCode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 2, 1, 3),
    _KcprtAlertStateCode_Type()
)
kcprtAlertStateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertStateCode.setStatus("mandatory")
_KcprtAlertJamLogTable_Object = MibTable
kcprtAlertJamLogTable = _KcprtAlertJamLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3)
)
if mibBuilder.loadTexts:
    kcprtAlertJamLogTable.setStatus("mandatory")
_KcprtAlertJamLogEntry_Object = MibTableRow
kcprtAlertJamLogEntry = _KcprtAlertJamLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1)
)
kcprtAlertJamLogEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtAlertJamLogIndex"),
)
if mibBuilder.loadTexts:
    kcprtAlertJamLogEntry.setStatus("mandatory")
_KcprtAlertJamLogIndex_Type = Integer32
_KcprtAlertJamLogIndex_Object = MibTableColumn
kcprtAlertJamLogIndex = _KcprtAlertJamLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 1),
    _KcprtAlertJamLogIndex_Type()
)
kcprtAlertJamLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtAlertJamLogIndex.setStatus("mandatory")
_KcprtAlertJamLogStamp_Type = Integer32
_KcprtAlertJamLogStamp_Object = MibTableColumn
kcprtAlertJamLogStamp = _KcprtAlertJamLogStamp_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 2),
    _KcprtAlertJamLogStamp_Type()
)
kcprtAlertJamLogStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertJamLogStamp.setStatus("mandatory")
_KcprtAlertJamLogFactor_Type = DisplayString
_KcprtAlertJamLogFactor_Object = MibTableColumn
kcprtAlertJamLogFactor = _KcprtAlertJamLogFactor_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 3),
    _KcprtAlertJamLogFactor_Type()
)
kcprtAlertJamLogFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertJamLogFactor.setStatus("mandatory")
_KcprtAlertJamLogPosition_Type = DisplayString
_KcprtAlertJamLogPosition_Object = MibTableColumn
kcprtAlertJamLogPosition = _KcprtAlertJamLogPosition_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 4),
    _KcprtAlertJamLogPosition_Type()
)
kcprtAlertJamLogPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertJamLogPosition.setStatus("mandatory")
_KcprtAlertJamLogInput_Type = Integer32
_KcprtAlertJamLogInput_Object = MibTableColumn
kcprtAlertJamLogInput = _KcprtAlertJamLogInput_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 5),
    _KcprtAlertJamLogInput_Type()
)
kcprtAlertJamLogInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertJamLogInput.setStatus("mandatory")
_KcprtAlertJamLogPaper_Type = Integer32
_KcprtAlertJamLogPaper_Object = MibTableColumn
kcprtAlertJamLogPaper = _KcprtAlertJamLogPaper_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 6),
    _KcprtAlertJamLogPaper_Type()
)
kcprtAlertJamLogPaper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertJamLogPaper.setStatus("mandatory")
_KcprtAlertJamLogMedia_Type = Integer32
_KcprtAlertJamLogMedia_Object = MibTableColumn
kcprtAlertJamLogMedia = _KcprtAlertJamLogMedia_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 7),
    _KcprtAlertJamLogMedia_Type()
)
kcprtAlertJamLogMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertJamLogMedia.setStatus("mandatory")
_KcprtAlertJamLogOutput_Type = Integer32
_KcprtAlertJamLogOutput_Object = MibTableColumn
kcprtAlertJamLogOutput = _KcprtAlertJamLogOutput_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 3, 1, 8),
    _KcprtAlertJamLogOutput_Type()
)
kcprtAlertJamLogOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertJamLogOutput.setStatus("mandatory")
_KcprtAlertCallLogTable_Object = MibTable
kcprtAlertCallLogTable = _KcprtAlertCallLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 4)
)
if mibBuilder.loadTexts:
    kcprtAlertCallLogTable.setStatus("mandatory")
_KcprtAlertCallLogEntry_Object = MibTableRow
kcprtAlertCallLogEntry = _KcprtAlertCallLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 4, 1)
)
kcprtAlertCallLogEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtAlertCallLogIndex"),
)
if mibBuilder.loadTexts:
    kcprtAlertCallLogEntry.setStatus("mandatory")
_KcprtAlertCallLogIndex_Type = Integer32
_KcprtAlertCallLogIndex_Object = MibTableColumn
kcprtAlertCallLogIndex = _KcprtAlertCallLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 4, 1, 1),
    _KcprtAlertCallLogIndex_Type()
)
kcprtAlertCallLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtAlertCallLogIndex.setStatus("mandatory")
_KcprtAlertCallLogStamp_Type = Integer32
_KcprtAlertCallLogStamp_Object = MibTableColumn
kcprtAlertCallLogStamp = _KcprtAlertCallLogStamp_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 4, 1, 2),
    _KcprtAlertCallLogStamp_Type()
)
kcprtAlertCallLogStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertCallLogStamp.setStatus("mandatory")
_KcprtAlertCallLogFactor_Type = DisplayString
_KcprtAlertCallLogFactor_Object = MibTableColumn
kcprtAlertCallLogFactor = _KcprtAlertCallLogFactor_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 4, 1, 3),
    _KcprtAlertCallLogFactor_Type()
)
kcprtAlertCallLogFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertCallLogFactor.setStatus("mandatory")
_KcprtAlertChangeLogTable_Object = MibTable
kcprtAlertChangeLogTable = _KcprtAlertChangeLogTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 5)
)
if mibBuilder.loadTexts:
    kcprtAlertChangeLogTable.setStatus("mandatory")
_KcprtAlertChangeLogEntry_Object = MibTableRow
kcprtAlertChangeLogEntry = _KcprtAlertChangeLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 5, 1)
)
kcprtAlertChangeLogEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtAlertChangeLogIndex"),
)
if mibBuilder.loadTexts:
    kcprtAlertChangeLogEntry.setStatus("mandatory")
_KcprtAlertChangeLogIndex_Type = Integer32
_KcprtAlertChangeLogIndex_Object = MibTableColumn
kcprtAlertChangeLogIndex = _KcprtAlertChangeLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 5, 1, 1),
    _KcprtAlertChangeLogIndex_Type()
)
kcprtAlertChangeLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtAlertChangeLogIndex.setStatus("mandatory")
_KcprtAlertChangeLogStamp_Type = Integer32
_KcprtAlertChangeLogStamp_Object = MibTableColumn
kcprtAlertChangeLogStamp = _KcprtAlertChangeLogStamp_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 5, 1, 2),
    _KcprtAlertChangeLogStamp_Type()
)
kcprtAlertChangeLogStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertChangeLogStamp.setStatus("mandatory")
_KcprtAlertChangeLogKind_Type = DisplayString
_KcprtAlertChangeLogKind_Object = MibTableColumn
kcprtAlertChangeLogKind = _KcprtAlertChangeLogKind_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 5, 1, 3),
    _KcprtAlertChangeLogKind_Type()
)
kcprtAlertChangeLogKind.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertChangeLogKind.setStatus("mandatory")
_KcprtAlertEventCountTable_Object = MibTable
kcprtAlertEventCountTable = _KcprtAlertEventCountTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 6)
)
if mibBuilder.loadTexts:
    kcprtAlertEventCountTable.setStatus("mandatory")
_KcprtAlertEventCountEntry_Object = MibTableRow
kcprtAlertEventCountEntry = _KcprtAlertEventCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 6, 1)
)
kcprtAlertEventCountEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtAlertEventCountIndex"),
)
if mibBuilder.loadTexts:
    kcprtAlertEventCountEntry.setStatus("mandatory")
_KcprtAlertEventCountIndex_Type = Integer32
_KcprtAlertEventCountIndex_Object = MibTableColumn
kcprtAlertEventCountIndex = _KcprtAlertEventCountIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 6, 1, 1),
    _KcprtAlertEventCountIndex_Type()
)
kcprtAlertEventCountIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtAlertEventCountIndex.setStatus("mandatory")
_KcprtAlertEventCountFactor_Type = DisplayString
_KcprtAlertEventCountFactor_Object = MibTableColumn
kcprtAlertEventCountFactor = _KcprtAlertEventCountFactor_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 6, 1, 2),
    _KcprtAlertEventCountFactor_Type()
)
kcprtAlertEventCountFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertEventCountFactor.setStatus("mandatory")
_KcprtAlertEventCountValue_Type = Integer32
_KcprtAlertEventCountValue_Object = MibTableColumn
kcprtAlertEventCountValue = _KcprtAlertEventCountValue_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 18, 6, 1, 3),
    _KcprtAlertEventCountValue_Type()
)
kcprtAlertEventCountValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtAlertEventCountValue.setStatus("mandatory")
_KcprtMemoryResource_ObjectIdentity = ObjectIdentity
kcprtMemoryResource = _KcprtMemoryResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20)
)
_KcprtMemoryDeviceTable_Object = MibTable
kcprtMemoryDeviceTable = _KcprtMemoryDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1)
)
if mibBuilder.loadTexts:
    kcprtMemoryDeviceTable.setStatus("mandatory")
_KcprtMemoryDeviceEntry_Object = MibTableRow
kcprtMemoryDeviceEntry = _KcprtMemoryDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1)
)
kcprtMemoryDeviceEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtMemoryDeviceIndex"),
)
if mibBuilder.loadTexts:
    kcprtMemoryDeviceEntry.setStatus("mandatory")
_KcprtMemoryDeviceIndex_Type = Integer32
_KcprtMemoryDeviceIndex_Object = MibTableColumn
kcprtMemoryDeviceIndex = _KcprtMemoryDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 1),
    _KcprtMemoryDeviceIndex_Type()
)
kcprtMemoryDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceIndex.setStatus("mandatory")


class _KcprtMemoryDeviceLocation_Type(Integer32):
    """Custom type kcprtMemoryDeviceLocation based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("pcCard-A", 0),
          ("pcCard-B", 1),
          ("optionROMsocket", 2),
          ("residentFont", 3),
          ("downloadArea", 4),
          ("hardDisk", 5),
          ("memoryCard", 6),
          ("others", 255))
    )


_KcprtMemoryDeviceLocation_Type.__name__ = "Integer32"
_KcprtMemoryDeviceLocation_Object = MibTableColumn
kcprtMemoryDeviceLocation = _KcprtMemoryDeviceLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 2),
    _KcprtMemoryDeviceLocation_Type()
)
kcprtMemoryDeviceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceLocation.setStatus("mandatory")


class _KcprtMemoryDeviceType_Type(Integer32):
    """Custom type kcprtMemoryDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("rom", 0),
          ("flash", 1),
          ("sram", 2),
          ("dram", 3),
          ("strage", 4),
          ("others", 255))
    )


_KcprtMemoryDeviceType_Type.__name__ = "Integer32"
_KcprtMemoryDeviceType_Object = MibTableColumn
kcprtMemoryDeviceType = _KcprtMemoryDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 3),
    _KcprtMemoryDeviceType_Type()
)
kcprtMemoryDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceType.setStatus("mandatory")
_KcprtMemoryDeviceTotalSize_Type = Integer32
_KcprtMemoryDeviceTotalSize_Object = MibTableColumn
kcprtMemoryDeviceTotalSize = _KcprtMemoryDeviceTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 4),
    _KcprtMemoryDeviceTotalSize_Type()
)
kcprtMemoryDeviceTotalSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceTotalSize.setStatus("mandatory")
_KcprtMemoryDeviceUsedSize_Type = Integer32
_KcprtMemoryDeviceUsedSize_Object = MibTableColumn
kcprtMemoryDeviceUsedSize = _KcprtMemoryDeviceUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 5),
    _KcprtMemoryDeviceUsedSize_Type()
)
kcprtMemoryDeviceUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceUsedSize.setStatus("mandatory")


class _KcprtMemoryDeviceStatus_Type(Integer32):
    """Custom type kcprtMemoryDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4)
        )
    )
    namedValues = NamedValues(
        *(("readyReadWrite", 0),
          ("readyReadOnly", 1),
          ("notAccessible", 2),
          ("lowBattery", 4))
    )


_KcprtMemoryDeviceStatus_Type.__name__ = "Integer32"
_KcprtMemoryDeviceStatus_Object = MibTableColumn
kcprtMemoryDeviceStatus = _KcprtMemoryDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 6),
    _KcprtMemoryDeviceStatus_Type()
)
kcprtMemoryDeviceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceStatus.setStatus("mandatory")
_KcprtMemoryDeviceUnit_Type = Integer32
_KcprtMemoryDeviceUnit_Object = MibTableColumn
kcprtMemoryDeviceUnit = _KcprtMemoryDeviceUnit_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 1, 1, 7),
    _KcprtMemoryDeviceUnit_Type()
)
kcprtMemoryDeviceUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMemoryDeviceUnit.setStatus("mandatory")
_KcprtPartitionTable_Object = MibTable
kcprtPartitionTable = _KcprtPartitionTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2)
)
if mibBuilder.loadTexts:
    kcprtPartitionTable.setStatus("mandatory")
_KcprtPartitionEntry_Object = MibTableRow
kcprtPartitionEntry = _KcprtPartitionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1)
)
kcprtPartitionEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtPartitionIndex"),
)
if mibBuilder.loadTexts:
    kcprtPartitionEntry.setStatus("mandatory")
_KcprtPartitionIndex_Type = Integer32
_KcprtPartitionIndex_Object = MibTableColumn
kcprtPartitionIndex = _KcprtPartitionIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 1),
    _KcprtPartitionIndex_Type()
)
kcprtPartitionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtPartitionIndex.setStatus("mandatory")
_KcprtPartitionSize_Type = Integer32
_KcprtPartitionSize_Object = MibTableColumn
kcprtPartitionSize = _KcprtPartitionSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 2),
    _KcprtPartitionSize_Type()
)
kcprtPartitionSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionSize.setStatus("mandatory")
_KcprtPartitionLocation_Type = Integer32
_KcprtPartitionLocation_Object = MibTableColumn
kcprtPartitionLocation = _KcprtPartitionLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 3),
    _KcprtPartitionLocation_Type()
)
kcprtPartitionLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionLocation.setStatus("mandatory")


class _KcprtPartitionResourceType_Type(Integer32):
    """Custom type kcprtPartitionResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("void", 0),
          ("macro", 3),
          ("hostData", 4),
          ("programData", 5),
          ("messageData", 6),
          ("fontData", 7))
    )


_KcprtPartitionResourceType_Type.__name__ = "Integer32"
_KcprtPartitionResourceType_Object = MibTableColumn
kcprtPartitionResourceType = _KcprtPartitionResourceType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 4),
    _KcprtPartitionResourceType_Type()
)
kcprtPartitionResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionResourceType.setStatus("mandatory")


class _KcprtPartitionName_Type(DisplayString):
    """Custom type kcprtPartitionName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtPartitionName_Type.__name__ = "DisplayString"
_KcprtPartitionName_Object = MibTableColumn
kcprtPartitionName = _KcprtPartitionName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 5),
    _KcprtPartitionName_Type()
)
kcprtPartitionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionName.setStatus("mandatory")


class _KcprtPartitionLoad_Type(Integer32):
    """Custom type kcprtPartitionLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notLoaded", 0),
          ("loaded", 1))
    )


_KcprtPartitionLoad_Type.__name__ = "Integer32"
_KcprtPartitionLoad_Object = MibTableColumn
kcprtPartitionLoad = _KcprtPartitionLoad_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 2, 1, 6),
    _KcprtPartitionLoad_Type()
)
kcprtPartitionLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtPartitionLoad.setStatus("mandatory")
_KcprtMacroDataTable_Object = MibTable
kcprtMacroDataTable = _KcprtMacroDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3)
)
if mibBuilder.loadTexts:
    kcprtMacroDataTable.setStatus("mandatory")
_KcprtMacroDataEntry_Object = MibTableRow
kcprtMacroDataEntry = _KcprtMacroDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1)
)
kcprtMacroDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtMacroDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtMacroDataEntry.setStatus("mandatory")
_KcprtMacroDataIndex_Type = Integer32
_KcprtMacroDataIndex_Object = MibTableColumn
kcprtMacroDataIndex = _KcprtMacroDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 1),
    _KcprtMacroDataIndex_Type()
)
kcprtMacroDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMacroDataIndex.setStatus("mandatory")


class _KcprtMacroDataName_Type(DisplayString):
    """Custom type kcprtMacroDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4),
    )


_KcprtMacroDataName_Type.__name__ = "DisplayString"
_KcprtMacroDataName_Object = MibTableColumn
kcprtMacroDataName = _KcprtMacroDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 2),
    _KcprtMacroDataName_Type()
)
kcprtMacroDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataName.setStatus("mandatory")
_KcprtMacroDataID_Type = Integer32
_KcprtMacroDataID_Object = MibTableColumn
kcprtMacroDataID = _KcprtMacroDataID_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 3),
    _KcprtMacroDataID_Type()
)
kcprtMacroDataID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataID.setStatus("mandatory")


class _KcprtMacroDataType_Type(Integer32):
    """Custom type kcprtMacroDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("prescribe", 1),
          ("pcl", 2),
          ("others", 255))
    )


_KcprtMacroDataType_Type.__name__ = "Integer32"
_KcprtMacroDataType_Object = MibTableColumn
kcprtMacroDataType = _KcprtMacroDataType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 4),
    _KcprtMacroDataType_Type()
)
kcprtMacroDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataType.setStatus("mandatory")


class _KcprtMacroDataAutoLoad_Type(Integer32):
    """Custom type kcprtMacroDataAutoLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("onWithInitialize", 1),
          ("onWithoutInitialize", 2))
    )


_KcprtMacroDataAutoLoad_Type.__name__ = "Integer32"
_KcprtMacroDataAutoLoad_Object = MibTableColumn
kcprtMacroDataAutoLoad = _KcprtMacroDataAutoLoad_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 5),
    _KcprtMacroDataAutoLoad_Type()
)
kcprtMacroDataAutoLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataAutoLoad.setStatus("mandatory")
_KcprtMacroDataLocation_Type = Integer32
_KcprtMacroDataLocation_Object = MibTableColumn
kcprtMacroDataLocation = _KcprtMacroDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 6),
    _KcprtMacroDataLocation_Type()
)
kcprtMacroDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataLocation.setStatus("mandatory")


class _KcprtMacroDataAttribute_Type(Integer32):
    """Custom type kcprtMacroDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtMacroDataAttribute_Type.__name__ = "Integer32"
_KcprtMacroDataAttribute_Object = MibTableColumn
kcprtMacroDataAttribute = _KcprtMacroDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 3, 1, 7),
    _KcprtMacroDataAttribute_Type()
)
kcprtMacroDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMacroDataAttribute.setStatus("mandatory")
_KcprtHostDataTable_Object = MibTable
kcprtHostDataTable = _KcprtHostDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4)
)
if mibBuilder.loadTexts:
    kcprtHostDataTable.setStatus("mandatory")
_KcprtHostDataEntry_Object = MibTableRow
kcprtHostDataEntry = _KcprtHostDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1)
)
kcprtHostDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtHostDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtHostDataEntry.setStatus("mandatory")
_KcprtHostDataIndex_Type = Integer32
_KcprtHostDataIndex_Object = MibTableColumn
kcprtHostDataIndex = _KcprtHostDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 1),
    _KcprtHostDataIndex_Type()
)
kcprtHostDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtHostDataIndex.setStatus("mandatory")


class _KcprtHostDataName_Type(DisplayString):
    """Custom type kcprtHostDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtHostDataName_Type.__name__ = "DisplayString"
_KcprtHostDataName_Object = MibTableColumn
kcprtHostDataName = _KcprtHostDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 2),
    _KcprtHostDataName_Type()
)
kcprtHostDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtHostDataName.setStatus("mandatory")
_KcprtHostDataLocation_Type = Integer32
_KcprtHostDataLocation_Object = MibTableColumn
kcprtHostDataLocation = _KcprtHostDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 3),
    _KcprtHostDataLocation_Type()
)
kcprtHostDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtHostDataLocation.setStatus("mandatory")


class _KcprtHostDataAttribute_Type(Integer32):
    """Custom type kcprtHostDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtHostDataAttribute_Type.__name__ = "Integer32"
_KcprtHostDataAttribute_Object = MibTableColumn
kcprtHostDataAttribute = _KcprtHostDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 4, 1, 4),
    _KcprtHostDataAttribute_Type()
)
kcprtHostDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtHostDataAttribute.setStatus("mandatory")
_KcprtProgramDataTable_Object = MibTable
kcprtProgramDataTable = _KcprtProgramDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5)
)
if mibBuilder.loadTexts:
    kcprtProgramDataTable.setStatus("mandatory")
_KcprtProgramDataEntry_Object = MibTableRow
kcprtProgramDataEntry = _KcprtProgramDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1)
)
kcprtProgramDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtProgramDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtProgramDataEntry.setStatus("mandatory")
_KcprtProgramDataIndex_Type = Integer32
_KcprtProgramDataIndex_Object = MibTableColumn
kcprtProgramDataIndex = _KcprtProgramDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 1),
    _KcprtProgramDataIndex_Type()
)
kcprtProgramDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtProgramDataIndex.setStatus("mandatory")


class _KcprtProgramDataName_Type(DisplayString):
    """Custom type kcprtProgramDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtProgramDataName_Type.__name__ = "DisplayString"
_KcprtProgramDataName_Object = MibTableColumn
kcprtProgramDataName = _KcprtProgramDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 2),
    _KcprtProgramDataName_Type()
)
kcprtProgramDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataName.setStatus("mandatory")


class _KcprtProgramDataType_Type(Integer32):
    """Custom type kcprtProgramDataType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("emulation", 0),
          ("prescribe", 1),
          ("panel", 2),
          ("others", 255))
    )


_KcprtProgramDataType_Type.__name__ = "Integer32"
_KcprtProgramDataType_Object = MibTableColumn
kcprtProgramDataType = _KcprtProgramDataType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 3),
    _KcprtProgramDataType_Type()
)
kcprtProgramDataType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataType.setStatus("mandatory")
_KcprtProgramDataLocation_Type = Integer32
_KcprtProgramDataLocation_Object = MibTableColumn
kcprtProgramDataLocation = _KcprtProgramDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 4),
    _KcprtProgramDataLocation_Type()
)
kcprtProgramDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataLocation.setStatus("mandatory")


class _KcprtProgramDataAttribute_Type(Integer32):
    """Custom type kcprtProgramDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1),
          ("running", 2))
    )


_KcprtProgramDataAttribute_Type.__name__ = "Integer32"
_KcprtProgramDataAttribute_Object = MibTableColumn
kcprtProgramDataAttribute = _KcprtProgramDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 5, 1, 5),
    _KcprtProgramDataAttribute_Type()
)
kcprtProgramDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtProgramDataAttribute.setStatus("mandatory")
_KcprtMessageDataTable_Object = MibTable
kcprtMessageDataTable = _KcprtMessageDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6)
)
if mibBuilder.loadTexts:
    kcprtMessageDataTable.setStatus("mandatory")
_KcprtMessageDataEntry_Object = MibTableRow
kcprtMessageDataEntry = _KcprtMessageDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1)
)
kcprtMessageDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtMessageDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtMessageDataEntry.setStatus("mandatory")
_KcprtMessageDataIndex_Type = Integer32
_KcprtMessageDataIndex_Object = MibTableColumn
kcprtMessageDataIndex = _KcprtMessageDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 1),
    _KcprtMessageDataIndex_Type()
)
kcprtMessageDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMessageDataIndex.setStatus("mandatory")


class _KcprtMessageDataName_Type(DisplayString):
    """Custom type kcprtMessageDataName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_KcprtMessageDataName_Type.__name__ = "DisplayString"
_KcprtMessageDataName_Object = MibTableColumn
kcprtMessageDataName = _KcprtMessageDataName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 2),
    _KcprtMessageDataName_Type()
)
kcprtMessageDataName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMessageDataName.setStatus("mandatory")
_KcprtMessageDataLocation_Type = Integer32
_KcprtMessageDataLocation_Object = MibTableColumn
kcprtMessageDataLocation = _KcprtMessageDataLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 3),
    _KcprtMessageDataLocation_Type()
)
kcprtMessageDataLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMessageDataLocation.setStatus("mandatory")


class _KcprtMessageDataAttribute_Type(Integer32):
    """Custom type kcprtMessageDataAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtMessageDataAttribute_Type.__name__ = "Integer32"
_KcprtMessageDataAttribute_Object = MibTableColumn
kcprtMessageDataAttribute = _KcprtMessageDataAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 6, 1, 4),
    _KcprtMessageDataAttribute_Type()
)
kcprtMessageDataAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMessageDataAttribute.setStatus("mandatory")
_KcprtFontDataTable_Object = MibTable
kcprtFontDataTable = _KcprtFontDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7)
)
if mibBuilder.loadTexts:
    kcprtFontDataTable.setStatus("mandatory")
_KcprtFontDataEntry_Object = MibTableRow
kcprtFontDataEntry = _KcprtFontDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1)
)
kcprtFontDataEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtFontDataIndex"),
)
if mibBuilder.loadTexts:
    kcprtFontDataEntry.setStatus("mandatory")
_KcprtFontDataIndex_Type = Integer32
_KcprtFontDataIndex_Object = MibTableColumn
kcprtFontDataIndex = _KcprtFontDataIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 1),
    _KcprtFontDataIndex_Type()
)
kcprtFontDataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtFontDataIndex.setStatus("mandatory")


class _KcprtTypeFaceName_Type(DisplayString):
    """Custom type kcprtTypeFaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtTypeFaceName_Type.__name__ = "DisplayString"
_KcprtTypeFaceName_Object = MibTableColumn
kcprtTypeFaceName = _KcprtTypeFaceName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 2),
    _KcprtTypeFaceName_Type()
)
kcprtTypeFaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTypeFaceName.setStatus("mandatory")
_KcprtFontID_Type = Integer32
_KcprtFontID_Object = MibTableColumn
kcprtFontID = _KcprtFontID_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 3),
    _KcprtFontID_Type()
)
kcprtFontID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontID.setStatus("mandatory")


class _KcprtFontType_Type(Integer32):
    """Custom type kcprtFontType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("bitmap", 0),
          ("scalable", 1),
          ("others", 255))
    )


_KcprtFontType_Type.__name__ = "Integer32"
_KcprtFontType_Object = MibTableColumn
kcprtFontType = _KcprtFontType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 4),
    _KcprtFontType_Type()
)
kcprtFontType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontType.setStatus("mandatory")
_KcprtFontLocation_Type = Integer32
_KcprtFontLocation_Object = MibTableColumn
kcprtFontLocation = _KcprtFontLocation_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 5),
    _KcprtFontLocation_Type()
)
kcprtFontLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontLocation.setStatus("mandatory")


class _KcprtFontAttribute_Type(Integer32):
    """Custom type kcprtFontAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 0),
          ("registered", 1))
    )


_KcprtFontAttribute_Type.__name__ = "Integer32"
_KcprtFontAttribute_Object = MibTableColumn
kcprtFontAttribute = _KcprtFontAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 7, 1, 6),
    _KcprtFontAttribute_Type()
)
kcprtFontAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFontAttribute.setStatus("mandatory")
_KcprtFileStorageTable_Object = MibTable
kcprtFileStorageTable = _KcprtFileStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 8)
)
if mibBuilder.loadTexts:
    kcprtFileStorageTable.setStatus("mandatory")
_KcprtFileStorageEntry_Object = MibTableRow
kcprtFileStorageEntry = _KcprtFileStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 8, 1)
)
kcprtFileStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtFileStorageIndex"),
)
if mibBuilder.loadTexts:
    kcprtFileStorageEntry.setStatus("mandatory")
_KcprtFileStorageIndex_Type = Integer32
_KcprtFileStorageIndex_Object = MibTableColumn
kcprtFileStorageIndex = _KcprtFileStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 8, 1, 1),
    _KcprtFileStorageIndex_Type()
)
kcprtFileStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtFileStorageIndex.setStatus("mandatory")
_KcprtFileStorageLimitSize_Type = Integer32
_KcprtFileStorageLimitSize_Object = MibTableColumn
kcprtFileStorageLimitSize = _KcprtFileStorageLimitSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 8, 1, 2),
    _KcprtFileStorageLimitSize_Type()
)
kcprtFileStorageLimitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFileStorageLimitSize.setStatus("mandatory")
_KcprtFileStorageUsedSize_Type = Integer32
_KcprtFileStorageUsedSize_Object = MibTableColumn
kcprtFileStorageUsedSize = _KcprtFileStorageUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 8, 1, 3),
    _KcprtFileStorageUsedSize_Type()
)
kcprtFileStorageUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFileStorageUsedSize.setStatus("mandatory")
_KcprtFileStorageUnit_Type = Integer32
_KcprtFileStorageUnit_Object = MibTableColumn
kcprtFileStorageUnit = _KcprtFileStorageUnit_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 8, 1, 4),
    _KcprtFileStorageUnit_Type()
)
kcprtFileStorageUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFileStorageUnit.setStatus("mandatory")


class _KcprtFileStorageCounter_Type(Integer32):
    """Custom type kcprtFileStorageCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtFileStorageCounter_Type.__name__ = "Integer32"
_KcprtFileStorageCounter_Object = MibTableColumn
kcprtFileStorageCounter = _KcprtFileStorageCounter_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 8, 1, 5),
    _KcprtFileStorageCounter_Type()
)
kcprtFileStorageCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFileStorageCounter.setStatus("mandatory")
_KcprtFileTable_Object = MibTable
kcprtFileTable = _KcprtFileTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 9)
)
if mibBuilder.loadTexts:
    kcprtFileTable.setStatus("mandatory")
_KcprtFileEntry_Object = MibTableRow
kcprtFileEntry = _KcprtFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 9, 1)
)
kcprtFileEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtFileIndex"),
)
if mibBuilder.loadTexts:
    kcprtFileEntry.setStatus("mandatory")
_KcprtFileIndex_Type = Integer32
_KcprtFileIndex_Object = MibTableColumn
kcprtFileIndex = _KcprtFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 9, 1, 1),
    _KcprtFileIndex_Type()
)
kcprtFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFileIndex.setStatus("mandatory")


class _KcprtFileName_Type(OctetString):
    """Custom type kcprtFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_KcprtFileName_Type.__name__ = "OctetString"
_KcprtFileName_Object = MibTableColumn
kcprtFileName = _KcprtFileName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 9, 1, 2),
    _KcprtFileName_Type()
)
kcprtFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFileName.setStatus("mandatory")
_KcprtFileSize_Type = Integer32
_KcprtFileSize_Object = MibTableColumn
kcprtFileSize = _KcprtFileSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 9, 1, 3),
    _KcprtFileSize_Type()
)
kcprtFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtFileSize.setStatus("mandatory")
_KcprtSJobStorageTable_Object = MibTable
kcprtSJobStorageTable = _KcprtSJobStorageTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10)
)
if mibBuilder.loadTexts:
    kcprtSJobStorageTable.setStatus("mandatory")
_KcprtSJobStorageEntry_Object = MibTableRow
kcprtSJobStorageEntry = _KcprtSJobStorageEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10, 1)
)
kcprtSJobStorageEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtSJobStorageIndex"),
)
if mibBuilder.loadTexts:
    kcprtSJobStorageEntry.setStatus("mandatory")
_KcprtSJobStorageIndex_Type = Integer32
_KcprtSJobStorageIndex_Object = MibTableColumn
kcprtSJobStorageIndex = _KcprtSJobStorageIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10, 1, 1),
    _KcprtSJobStorageIndex_Type()
)
kcprtSJobStorageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtSJobStorageIndex.setStatus("mandatory")
_KcprtSJobStorageLimitSize_Type = Integer32
_KcprtSJobStorageLimitSize_Object = MibTableColumn
kcprtSJobStorageLimitSize = _KcprtSJobStorageLimitSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10, 1, 2),
    _KcprtSJobStorageLimitSize_Type()
)
kcprtSJobStorageLimitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStorageLimitSize.setStatus("mandatory")
_KcprtSJobStorageUsedSize_Type = Integer32
_KcprtSJobStorageUsedSize_Object = MibTableColumn
kcprtSJobStorageUsedSize = _KcprtSJobStorageUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10, 1, 3),
    _KcprtSJobStorageUsedSize_Type()
)
kcprtSJobStorageUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStorageUsedSize.setStatus("mandatory")
_KcprtSJobStorageUnit_Type = Integer32
_KcprtSJobStorageUnit_Object = MibTableColumn
kcprtSJobStorageUnit = _KcprtSJobStorageUnit_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10, 1, 4),
    _KcprtSJobStorageUnit_Type()
)
kcprtSJobStorageUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStorageUnit.setStatus("mandatory")


class _KcprtSJobStorageStateCounter_Type(Integer32):
    """Custom type kcprtSJobStorageStateCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtSJobStorageStateCounter_Type.__name__ = "Integer32"
_KcprtSJobStorageStateCounter_Object = MibTableColumn
kcprtSJobStorageStateCounter = _KcprtSJobStorageStateCounter_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10, 1, 5),
    _KcprtSJobStorageStateCounter_Type()
)
kcprtSJobStorageStateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStorageStateCounter.setStatus("mandatory")


class _KcprtSJobStorageAttribute_Type(Integer32):
    """Custom type kcprtSJobStorageAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              255)
        )
    )
    namedValues = NamedValues(
        *(("volatile", 1),
          ("nonVolatile", 2),
          ("unknown", 255))
    )


_KcprtSJobStorageAttribute_Type.__name__ = "Integer32"
_KcprtSJobStorageAttribute_Object = MibTableColumn
kcprtSJobStorageAttribute = _KcprtSJobStorageAttribute_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 10, 1, 6),
    _KcprtSJobStorageAttribute_Type()
)
kcprtSJobStorageAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStorageAttribute.setStatus("mandatory")
_KcprtSJobTable_Object = MibTable
kcprtSJobTable = _KcprtSJobTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11)
)
if mibBuilder.loadTexts:
    kcprtSJobTable.setStatus("mandatory")
_KcprtSJobEntry_Object = MibTableRow
kcprtSJobEntry = _KcprtSJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1)
)
kcprtSJobEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtSJobIndex"),
)
if mibBuilder.loadTexts:
    kcprtSJobEntry.setStatus("mandatory")
_KcprtSJobIndex_Type = Integer32
_KcprtSJobIndex_Object = MibTableColumn
kcprtSJobIndex = _KcprtSJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 1),
    _KcprtSJobIndex_Type()
)
kcprtSJobIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtSJobIndex.setStatus("mandatory")


class _KcprtSjobID_Type(DisplayString):
    """Custom type kcprtSjobID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_KcprtSjobID_Type.__name__ = "DisplayString"
_KcprtSjobID_Object = MibTableColumn
kcprtSjobID = _KcprtSjobID_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 2),
    _KcprtSjobID_Type()
)
kcprtSjobID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSjobID.setStatus("mandatory")


class _KcprtSJobName_Type(DisplayString):
    """Custom type kcprtSJobName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtSJobName_Type.__name__ = "DisplayString"
_KcprtSJobName_Object = MibTableColumn
kcprtSJobName = _KcprtSJobName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 3),
    _KcprtSJobName_Type()
)
kcprtSJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobName.setStatus("mandatory")


class _KcprtSJobOwner_Type(DisplayString):
    """Custom type kcprtSJobOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtSJobOwner_Type.__name__ = "DisplayString"
_KcprtSJobOwner_Object = MibTableColumn
kcprtSJobOwner = _KcprtSJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 4),
    _KcprtSJobOwner_Type()
)
kcprtSJobOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobOwner.setStatus("mandatory")


class _KcprtSJobTime_Type(DisplayString):
    """Custom type kcprtSJobTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtSJobTime_Type.__name__ = "DisplayString"
_KcprtSJobTime_Object = MibTableColumn
kcprtSJobTime = _KcprtSJobTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 5),
    _KcprtSJobTime_Type()
)
kcprtSJobTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobTime.setStatus("mandatory")
_KcprtSJobPageNumber_Type = Integer32
_KcprtSJobPageNumber_Object = MibTableColumn
kcprtSJobPageNumber = _KcprtSJobPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 6),
    _KcprtSJobPageNumber_Type()
)
kcprtSJobPageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobPageNumber.setStatus("mandatory")


class _KcprtSJobSize_Type(Integer32):
    """Custom type kcprtSJobSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtSJobSize_Type.__name__ = "Integer32"
_KcprtSJobSize_Object = MibTableColumn
kcprtSJobSize = _KcprtSJobSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 7),
    _KcprtSJobSize_Type()
)
kcprtSJobSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobSize.setStatus("mandatory")
_KcprtSJobStorageRef_Type = Integer32
_KcprtSJobStorageRef_Object = MibTableColumn
kcprtSJobStorageRef = _KcprtSJobStorageRef_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 8),
    _KcprtSJobStorageRef_Type()
)
kcprtSJobStorageRef.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStorageRef.setStatus("mandatory")
_KcprtSJobCopyCount_Type = Integer32
_KcprtSJobCopyCount_Object = MibTableColumn
kcprtSJobCopyCount = _KcprtSJobCopyCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 9),
    _KcprtSJobCopyCount_Type()
)
kcprtSJobCopyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobCopyCount.setStatus("mandatory")


class _KcprtSJobBarcodePrintExistence_Type(Integer32):
    """Custom type kcprtSJobBarcodePrintExistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notPrinting", 0),
          ("firstPagePrinting", 1),
          ("allPagePrinting", 2))
    )


_KcprtSJobBarcodePrintExistence_Type.__name__ = "Integer32"
_KcprtSJobBarcodePrintExistence_Object = MibTableColumn
kcprtSJobBarcodePrintExistence = _KcprtSJobBarcodePrintExistence_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 10),
    _KcprtSJobBarcodePrintExistence_Type()
)
kcprtSJobBarcodePrintExistence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobBarcodePrintExistence.setStatus("mandatory")


class _KcprtSJobDuplexMode_Type(Integer32):
    """Custom type kcprtSJobDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("shortEdgeBindingDuplex", 3),
          ("longEdgeBindingDuplex", 4),
          ("simplex", 5))
    )


_KcprtSJobDuplexMode_Type.__name__ = "Integer32"
_KcprtSJobDuplexMode_Object = MibTableColumn
kcprtSJobDuplexMode = _KcprtSJobDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 11),
    _KcprtSJobDuplexMode_Type()
)
kcprtSJobDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobDuplexMode.setStatus("mandatory")
_KcprtSJobOutputIndex_Type = Integer32
_KcprtSJobOutputIndex_Object = MibTableColumn
kcprtSJobOutputIndex = _KcprtSJobOutputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 12),
    _KcprtSJobOutputIndex_Type()
)
kcprtSJobOutputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobOutputIndex.setStatus("mandatory")


class _KcprtSJobStaplePosition_Type(Integer32):
    """Custom type kcprtSJobStaplePosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("oneFrontLocation", 1),
          ("oneRearLocation", 2),
          ("twoCentralLocation", 3))
    )


_KcprtSJobStaplePosition_Type.__name__ = "Integer32"
_KcprtSJobStaplePosition_Object = MibTableColumn
kcprtSJobStaplePosition = _KcprtSJobStaplePosition_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 13),
    _KcprtSJobStaplePosition_Type()
)
kcprtSJobStaplePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStaplePosition.setStatus("mandatory")
_KcprtSJobBarcodePosition_Type = Integer32
_KcprtSJobBarcodePosition_Object = MibTableColumn
kcprtSJobBarcodePosition = _KcprtSJobBarcodePosition_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 14),
    _KcprtSJobBarcodePosition_Type()
)
kcprtSJobBarcodePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobBarcodePosition.setStatus("mandatory")
_KcprtSJobStapleAndFoldCount_Type = Integer32
_KcprtSJobStapleAndFoldCount_Object = MibTableColumn
kcprtSJobStapleAndFoldCount = _KcprtSJobStapleAndFoldCount_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 15),
    _KcprtSJobStapleAndFoldCount_Type()
)
kcprtSJobStapleAndFoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobStapleAndFoldCount.setStatus("mandatory")


class _KcprtSJobFoldMode_Type(Integer32):
    """Custom type kcprtSJobFoldMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("foldandStaple", 1))
    )


_KcprtSJobFoldMode_Type.__name__ = "Integer32"
_KcprtSJobFoldMode_Object = MibTableColumn
kcprtSJobFoldMode = _KcprtSJobFoldMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 16),
    _KcprtSJobFoldMode_Type()
)
kcprtSJobFoldMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobFoldMode.setStatus("mandatory")


class _KcprtSJobPunchMode_Type(Integer32):
    """Custom type kcprtSJobPunchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("main", 1),
          ("sub", 2))
    )


_KcprtSJobPunchMode_Type.__name__ = "Integer32"
_KcprtSJobPunchMode_Object = MibTableColumn
kcprtSJobPunchMode = _KcprtSJobPunchMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 17),
    _KcprtSJobPunchMode_Type()
)
kcprtSJobPunchMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobPunchMode.setStatus("mandatory")


class _KcprtSJobTransparencySeparationMode_Type(Integer32):
    """Custom type kcprtSJobTransparencySeparationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("blankPaperIjnterReef", 1),
          ("copySheetInterReef", 2))
    )


_KcprtSJobTransparencySeparationMode_Type.__name__ = "Integer32"
_KcprtSJobTransparencySeparationMode_Object = MibTableColumn
kcprtSJobTransparencySeparationMode = _KcprtSJobTransparencySeparationMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 18),
    _KcprtSJobTransparencySeparationMode_Type()
)
kcprtSJobTransparencySeparationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobTransparencySeparationMode.setStatus("mandatory")
_KcprtSJobTransparencySeparationInputIndex_Type = Integer32
_KcprtSJobTransparencySeparationInputIndex_Object = MibTableColumn
kcprtSJobTransparencySeparationInputIndex = _KcprtSJobTransparencySeparationInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 19),
    _KcprtSJobTransparencySeparationInputIndex_Type()
)
kcprtSJobTransparencySeparationInputIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobTransparencySeparationInputIndex.setStatus("mandatory")


class _KcprtSJobRotatedCollationMode_Type(Integer32):
    """Custom type kcprtSJobRotatedCollationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_KcprtSJobRotatedCollationMode_Type.__name__ = "Integer32"
_KcprtSJobRotatedCollationMode_Object = MibTableColumn
kcprtSJobRotatedCollationMode = _KcprtSJobRotatedCollationMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 20),
    _KcprtSJobRotatedCollationMode_Type()
)
kcprtSJobRotatedCollationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobRotatedCollationMode.setStatus("mandatory")


class _KcprtSJobBookletMode_Type(Integer32):
    """Custom type kcprtSJobBookletMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("leftBinding", 1),
          ("rightBinding", 2))
    )


_KcprtSJobBookletMode_Type.__name__ = "Integer32"
_KcprtSJobBookletMode_Object = MibTableColumn
kcprtSJobBookletMode = _KcprtSJobBookletMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 21),
    _KcprtSJobBookletMode_Type()
)
kcprtSJobBookletMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobBookletMode.setStatus("mandatory")


class _KcprtSJobJobOffsetMode_Type(Integer32):
    """Custom type kcprtSJobJobOffsetMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_KcprtSJobJobOffsetMode_Type.__name__ = "Integer32"
_KcprtSJobJobOffsetMode_Object = MibTableColumn
kcprtSJobJobOffsetMode = _KcprtSJobJobOffsetMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 20, 11, 1, 22),
    _KcprtSJobJobOffsetMode_Type()
)
kcprtSJobJobOffsetMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSJobJobOffsetMode.setStatus("mandatory")
_KcprtMediaList_ObjectIdentity = ObjectIdentity
kcprtMediaList = _KcprtMediaList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21)
)
_KcprtMediaTable_Object = MibTable
kcprtMediaTable = _KcprtMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1)
)
if mibBuilder.loadTexts:
    kcprtMediaTable.setStatus("mandatory")
_KcprtMediaEntry_Object = MibTableRow
kcprtMediaEntry = _KcprtMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1)
)
kcprtMediaEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtMediaIndex"),
)
if mibBuilder.loadTexts:
    kcprtMediaEntry.setStatus("mandatory")
_KcprtMediaIndex_Type = Integer32
_KcprtMediaIndex_Object = MibTableColumn
kcprtMediaIndex = _KcprtMediaIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1, 1),
    _KcprtMediaIndex_Type()
)
kcprtMediaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMediaIndex.setStatus("mandatory")


class _KcprtMediaName_Type(DisplayString):
    """Custom type kcprtMediaName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_KcprtMediaName_Type.__name__ = "DisplayString"
_KcprtMediaName_Object = MibTableColumn
kcprtMediaName = _KcprtMediaName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1, 2),
    _KcprtMediaName_Type()
)
kcprtMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMediaName.setStatus("mandatory")


class _KcprtMediaWeight_Type(Integer32):
    """Custom type kcprtMediaWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("heavy", 1),
          ("light", 2),
          ("extraheavy", 3))
    )


_KcprtMediaWeight_Type.__name__ = "Integer32"
_KcprtMediaWeight_Object = MibTableColumn
kcprtMediaWeight = _KcprtMediaWeight_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1, 3),
    _KcprtMediaWeight_Type()
)
kcprtMediaWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMediaWeight.setStatus("mandatory")


class _KcprtMediaFuserMode_Type(Integer32):
    """Custom type kcprtMediaFuserMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 0),
          ("middle", 1),
          ("low", 2),
          ("vellum", 3))
    )


_KcprtMediaFuserMode_Type.__name__ = "Integer32"
_KcprtMediaFuserMode_Object = MibTableColumn
kcprtMediaFuserMode = _KcprtMediaFuserMode_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1, 4),
    _KcprtMediaFuserMode_Type()
)
kcprtMediaFuserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMediaFuserMode.setStatus("mandatory")


class _KcprtMediaPathType_Type(Integer32):
    """Custom type kcprtMediaPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enable", 0),
          ("disable", 1))
    )


_KcprtMediaPathType_Type.__name__ = "Integer32"
_KcprtMediaPathType_Object = MibTableColumn
kcprtMediaPathType = _KcprtMediaPathType_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1, 5),
    _KcprtMediaPathType_Type()
)
kcprtMediaPathType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMediaPathType.setStatus("mandatory")
_KcprtMediaDensity_Type = Integer32
_KcprtMediaDensity_Object = MibTableColumn
kcprtMediaDensity = _KcprtMediaDensity_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1, 6),
    _KcprtMediaDensity_Type()
)
kcprtMediaDensity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMediaDensity.setStatus("mandatory")


class _KcprtMediaManageLevel_Type(Integer32):
    """Custom type kcprtMediaManageLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              15)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 15))
    )


_KcprtMediaManageLevel_Type.__name__ = "Integer32"
_KcprtMediaManageLevel_Object = MibTableColumn
kcprtMediaManageLevel = _KcprtMediaManageLevel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 21, 1, 1, 7),
    _KcprtMediaManageLevel_Type()
)
kcprtMediaManageLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMediaManageLevel.setStatus("mandatory")
_KcprtMailBox_ObjectIdentity = ObjectIdentity
kcprtMailBox = _KcprtMailBox_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22)
)
_KcprtMailBoxTable_Object = MibTable
kcprtMailBoxTable = _KcprtMailBoxTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1)
)
if mibBuilder.loadTexts:
    kcprtMailBoxTable.setStatus("mandatory")
_KcprtMailBoxEntry_Object = MibTableRow
kcprtMailBoxEntry = _KcprtMailBoxEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1)
)
kcprtMailBoxEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtMailBoxIndex"),
)
if mibBuilder.loadTexts:
    kcprtMailBoxEntry.setStatus("mandatory")
_KcprtMailBoxIndex_Type = Integer32
_KcprtMailBoxIndex_Object = MibTableColumn
kcprtMailBoxIndex = _KcprtMailBoxIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 1),
    _KcprtMailBoxIndex_Type()
)
kcprtMailBoxIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMailBoxIndex.setStatus("mandatory")
_KcprtMailBoxDeviceIndex_Type = Integer32
_KcprtMailBoxDeviceIndex_Object = MibTableColumn
kcprtMailBoxDeviceIndex = _KcprtMailBoxDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 2),
    _KcprtMailBoxDeviceIndex_Type()
)
kcprtMailBoxDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxDeviceIndex.setStatus("mandatory")


class _KcprtMailBoxStateCounter_Type(Integer32):
    """Custom type kcprtMailBoxStateCounter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxStateCounter_Type.__name__ = "Integer32"
_KcprtMailBoxStateCounter_Object = MibTableColumn
kcprtMailBoxStateCounter = _KcprtMailBoxStateCounter_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 3),
    _KcprtMailBoxStateCounter_Type()
)
kcprtMailBoxStateCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxStateCounter.setStatus("mandatory")


class _KcprtMailBoxUsedTrays_Type(Integer32):
    """Custom type kcprtMailBoxUsedTrays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_KcprtMailBoxUsedTrays_Type.__name__ = "Integer32"
_KcprtMailBoxUsedTrays_Object = MibTableColumn
kcprtMailBoxUsedTrays = _KcprtMailBoxUsedTrays_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 4),
    _KcprtMailBoxUsedTrays_Type()
)
kcprtMailBoxUsedTrays.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxUsedTrays.setStatus("mandatory")


class _KcprtMailBoxDocumentsNumber_Type(Integer32):
    """Custom type kcprtMailBoxDocumentsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxDocumentsNumber_Type.__name__ = "Integer32"
_KcprtMailBoxDocumentsNumber_Object = MibTableColumn
kcprtMailBoxDocumentsNumber = _KcprtMailBoxDocumentsNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 5),
    _KcprtMailBoxDocumentsNumber_Type()
)
kcprtMailBoxDocumentsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxDocumentsNumber.setStatus("mandatory")


class _KcprtMailBoxPageNumber_Type(Integer32):
    """Custom type kcprtMailBoxPageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxPageNumber_Type.__name__ = "Integer32"
_KcprtMailBoxPageNumber_Object = MibTableColumn
kcprtMailBoxPageNumber = _KcprtMailBoxPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 6),
    _KcprtMailBoxPageNumber_Type()
)
kcprtMailBoxPageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxPageNumber.setStatus("mandatory")


class _KcprtMailBoxUsedSize_Type(Integer32):
    """Custom type kcprtMailBoxUsedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxUsedSize_Type.__name__ = "Integer32"
_KcprtMailBoxUsedSize_Object = MibTableColumn
kcprtMailBoxUsedSize = _KcprtMailBoxUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 7),
    _KcprtMailBoxUsedSize_Type()
)
kcprtMailBoxUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxUsedSize.setStatus("mandatory")


class _KcprtMailBoxLimitSize_Type(Integer32):
    """Custom type kcprtMailBoxLimitSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxLimitSize_Type.__name__ = "Integer32"
_KcprtMailBoxLimitSize_Object = MibTableColumn
kcprtMailBoxLimitSize = _KcprtMailBoxLimitSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 8),
    _KcprtMailBoxLimitSize_Type()
)
kcprtMailBoxLimitSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMailBoxLimitSize.setStatus("mandatory")


class _KcprtMailBoxMaxLimitSize_Type(Integer32):
    """Custom type kcprtMailBoxMaxLimitSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxMaxLimitSize_Type.__name__ = "Integer32"
_KcprtMailBoxMaxLimitSize_Object = MibTableColumn
kcprtMailBoxMaxLimitSize = _KcprtMailBoxMaxLimitSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 9),
    _KcprtMailBoxMaxLimitSize_Type()
)
kcprtMailBoxMaxLimitSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxMaxLimitSize.setStatus("mandatory")
_KcprtMailBoxUnit_Type = Integer32
_KcprtMailBoxUnit_Object = MibTableColumn
kcprtMailBoxUnit = _KcprtMailBoxUnit_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 10),
    _KcprtMailBoxUnit_Type()
)
kcprtMailBoxUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxUnit.setStatus("mandatory")


class _KcprtMailBoxAliasCheck_Type(DisplayString):
    """Custom type kcprtMailBoxAliasCheck based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtMailBoxAliasCheck_Type.__name__ = "DisplayString"
_KcprtMailBoxAliasCheck_Object = MibTableColumn
kcprtMailBoxAliasCheck = _KcprtMailBoxAliasCheck_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 1, 1, 11),
    _KcprtMailBoxAliasCheck_Type()
)
kcprtMailBoxAliasCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMailBoxAliasCheck.setStatus("mandatory")
_KcprtMailBoxTrayTable_Object = MibTable
kcprtMailBoxTrayTable = _KcprtMailBoxTrayTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2)
)
if mibBuilder.loadTexts:
    kcprtMailBoxTrayTable.setStatus("mandatory")
_KcprtMailBoxTrayEntry_Object = MibTableRow
kcprtMailBoxTrayEntry = _KcprtMailBoxTrayEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1)
)
kcprtMailBoxTrayEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtMailBoxIndex"),
    (0, "KYOCERA-MIB", "kcprtMailBoxTrayIndex"),
)
if mibBuilder.loadTexts:
    kcprtMailBoxTrayEntry.setStatus("mandatory")
_KcprtMailBoxTrayIndex_Type = Integer32
_KcprtMailBoxTrayIndex_Object = MibTableColumn
kcprtMailBoxTrayIndex = _KcprtMailBoxTrayIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 1),
    _KcprtMailBoxTrayIndex_Type()
)
kcprtMailBoxTrayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayIndex.setStatus("mandatory")


class _KcprtMailBoxTrayUsedFlag_Type(Integer32):
    """Custom type kcprtMailBoxTrayUsedFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("notUsed", 0),
          ("used", 1),
          ("unknown", 255))
    )


_KcprtMailBoxTrayUsedFlag_Type.__name__ = "Integer32"
_KcprtMailBoxTrayUsedFlag_Object = MibTableColumn
kcprtMailBoxTrayUsedFlag = _KcprtMailBoxTrayUsedFlag_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 2),
    _KcprtMailBoxTrayUsedFlag_Type()
)
kcprtMailBoxTrayUsedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayUsedFlag.setStatus("mandatory")


class _KcprtMailBoxTrayLabel_Type(DisplayString):
    """Custom type kcprtMailBoxTrayLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtMailBoxTrayLabel_Type.__name__ = "DisplayString"
_KcprtMailBoxTrayLabel_Object = MibTableColumn
kcprtMailBoxTrayLabel = _KcprtMailBoxTrayLabel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 3),
    _KcprtMailBoxTrayLabel_Type()
)
kcprtMailBoxTrayLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayLabel.setStatus("mandatory")


class _KcprtMailBoxTrayLock_Type(Integer32):
    """Custom type kcprtMailBoxTrayLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 0),
          ("lock", 1),
          ("unknown", 255))
    )


_KcprtMailBoxTrayLock_Type.__name__ = "Integer32"
_KcprtMailBoxTrayLock_Object = MibTableColumn
kcprtMailBoxTrayLock = _KcprtMailBoxTrayLock_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 4),
    _KcprtMailBoxTrayLock_Type()
)
kcprtMailBoxTrayLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayLock.setStatus("mandatory")


class _KcprtMailBoxTrayDocumentsNumber_Type(Integer32):
    """Custom type kcprtMailBoxTrayDocumentsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxTrayDocumentsNumber_Type.__name__ = "Integer32"
_KcprtMailBoxTrayDocumentsNumber_Object = MibTableColumn
kcprtMailBoxTrayDocumentsNumber = _KcprtMailBoxTrayDocumentsNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 5),
    _KcprtMailBoxTrayDocumentsNumber_Type()
)
kcprtMailBoxTrayDocumentsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayDocumentsNumber.setStatus("mandatory")


class _KcprtMailBoxTrayPageNumber_Type(Integer32):
    """Custom type kcprtMailBoxTrayPageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxTrayPageNumber_Type.__name__ = "Integer32"
_KcprtMailBoxTrayPageNumber_Object = MibTableColumn
kcprtMailBoxTrayPageNumber = _KcprtMailBoxTrayPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 6),
    _KcprtMailBoxTrayPageNumber_Type()
)
kcprtMailBoxTrayPageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayPageNumber.setStatus("mandatory")


class _KcprtMailBoxTrayOccupiedSize_Type(Integer32):
    """Custom type kcprtMailBoxTrayOccupiedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxTrayOccupiedSize_Type.__name__ = "Integer32"
_KcprtMailBoxTrayOccupiedSize_Object = MibTableColumn
kcprtMailBoxTrayOccupiedSize = _KcprtMailBoxTrayOccupiedSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 7),
    _KcprtMailBoxTrayOccupiedSize_Type()
)
kcprtMailBoxTrayOccupiedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayOccupiedSize.setStatus("mandatory")


class _KcprtMailBoxTraySharedSize_Type(Integer32):
    """Custom type kcprtMailBoxTraySharedSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxTraySharedSize_Type.__name__ = "Integer32"
_KcprtMailBoxTraySharedSize_Object = MibTableColumn
kcprtMailBoxTraySharedSize = _KcprtMailBoxTraySharedSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 8),
    _KcprtMailBoxTraySharedSize_Type()
)
kcprtMailBoxTraySharedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxTraySharedSize.setStatus("mandatory")


class _KcprtMailBoxTrayErrorLogNumber_Type(Integer32):
    """Custom type kcprtMailBoxTrayErrorLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxTrayErrorLogNumber_Type.__name__ = "Integer32"
_KcprtMailBoxTrayErrorLogNumber_Object = MibTableColumn
kcprtMailBoxTrayErrorLogNumber = _KcprtMailBoxTrayErrorLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 9),
    _KcprtMailBoxTrayErrorLogNumber_Type()
)
kcprtMailBoxTrayErrorLogNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayErrorLogNumber.setStatus("mandatory")


class _KcprtMailBoxTrayPurgeDocuments_Type(Integer32):
    """Custom type kcprtMailBoxTrayPurgeDocuments based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxTrayPurgeDocuments_Type.__name__ = "Integer32"
_KcprtMailBoxTrayPurgeDocuments_Object = MibTableColumn
kcprtMailBoxTrayPurgeDocuments = _KcprtMailBoxTrayPurgeDocuments_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 10),
    _KcprtMailBoxTrayPurgeDocuments_Type()
)
kcprtMailBoxTrayPurgeDocuments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayPurgeDocuments.setStatus("mandatory")


class _KcprtMailBoxTrayReset_Type(Integer32):
    """Custom type kcprtMailBoxTrayReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtMailBoxTrayReset_Type.__name__ = "Integer32"
_KcprtMailBoxTrayReset_Object = MibTableColumn
kcprtMailBoxTrayReset = _KcprtMailBoxTrayReset_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 2, 1, 11),
    _KcprtMailBoxTrayReset_Type()
)
kcprtMailBoxTrayReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    kcprtMailBoxTrayReset.setStatus("mandatory")
_KcprtTrayJobTable_Object = MibTable
kcprtTrayJobTable = _KcprtTrayJobTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3)
)
if mibBuilder.loadTexts:
    kcprtTrayJobTable.setStatus("mandatory")
_KcprtTrayJobEntry_Object = MibTableRow
kcprtTrayJobEntry = _KcprtTrayJobEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1)
)
kcprtTrayJobEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtMailBoxIndex"),
    (0, "KYOCERA-MIB", "kcprtMailBoxTrayIndex"),
    (0, "KYOCERA-MIB", "kcprtTrayJobIndex"),
)
if mibBuilder.loadTexts:
    kcprtTrayJobEntry.setStatus("mandatory")
_KcprtTrayJobIndex_Type = Integer32
_KcprtTrayJobIndex_Object = MibTableColumn
kcprtTrayJobIndex = _KcprtTrayJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 1),
    _KcprtTrayJobIndex_Type()
)
kcprtTrayJobIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtTrayJobIndex.setStatus("mandatory")


class _KcprtTrayJobID_Type(DisplayString):
    """Custom type kcprtTrayJobID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtTrayJobID_Type.__name__ = "DisplayString"
_KcprtTrayJobID_Object = MibTableColumn
kcprtTrayJobID = _KcprtTrayJobID_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 2),
    _KcprtTrayJobID_Type()
)
kcprtTrayJobID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayJobID.setStatus("mandatory")


class _KcprtTrayJobName_Type(DisplayString):
    """Custom type kcprtTrayJobName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtTrayJobName_Type.__name__ = "DisplayString"
_KcprtTrayJobName_Object = MibTableColumn
kcprtTrayJobName = _KcprtTrayJobName_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 3),
    _KcprtTrayJobName_Type()
)
kcprtTrayJobName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayJobName.setStatus("mandatory")


class _KcprtTrayJobOwner_Type(DisplayString):
    """Custom type kcprtTrayJobOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtTrayJobOwner_Type.__name__ = "DisplayString"
_KcprtTrayJobOwner_Object = MibTableColumn
kcprtTrayJobOwner = _KcprtTrayJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 4),
    _KcprtTrayJobOwner_Type()
)
kcprtTrayJobOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayJobOwner.setStatus("mandatory")


class _KcprtTrayJobTime_Type(DisplayString):
    """Custom type kcprtTrayJobTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtTrayJobTime_Type.__name__ = "DisplayString"
_KcprtTrayJobTime_Object = MibTableColumn
kcprtTrayJobTime = _KcprtTrayJobTime_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 5),
    _KcprtTrayJobTime_Type()
)
kcprtTrayJobTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayJobTime.setStatus("mandatory")


class _KcprtTrayJobPageNumber_Type(Integer32):
    """Custom type kcprtTrayJobPageNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtTrayJobPageNumber_Type.__name__ = "Integer32"
_KcprtTrayJobPageNumber_Object = MibTableColumn
kcprtTrayJobPageNumber = _KcprtTrayJobPageNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 6),
    _KcprtTrayJobPageNumber_Type()
)
kcprtTrayJobPageNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayJobPageNumber.setStatus("mandatory")


class _KcprtTrayJobSize_Type(Integer32):
    """Custom type kcprtTrayJobSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_KcprtTrayJobSize_Type.__name__ = "Integer32"
_KcprtTrayJobSize_Object = MibTableColumn
kcprtTrayJobSize = _KcprtTrayJobSize_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 7),
    _KcprtTrayJobSize_Type()
)
kcprtTrayJobSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayJobSize.setStatus("mandatory")


class _KcprtTrayJobStorageResult_Type(Integer32):
    """Custom type kcprtTrayJobStorageResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              255)
        )
    )
    namedValues = NamedValues(
        *(("noError", 0),
          ("error", 1),
          ("unknown", 255))
    )


_KcprtTrayJobStorageResult_Type.__name__ = "Integer32"
_KcprtTrayJobStorageResult_Object = MibTableColumn
kcprtTrayJobStorageResult = _KcprtTrayJobStorageResult_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 22, 3, 1, 8),
    _KcprtTrayJobStorageResult_Type()
)
kcprtTrayJobStorageResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtTrayJobStorageResult.setStatus("mandatory")
_KcprtSubUnit_ObjectIdentity = ObjectIdentity
kcprtSubUnit = _KcprtSubUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23)
)
_KcprtSubUnitTable_Object = MibTable
kcprtSubUnitTable = _KcprtSubUnitTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23, 1)
)
if mibBuilder.loadTexts:
    kcprtSubUnitTable.setStatus("mandatory")
_KcprtSubUnitEntry_Object = MibTableRow
kcprtSubUnitEntry = _KcprtSubUnitEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23, 1, 1)
)
kcprtSubUnitEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
    (0, "KYOCERA-MIB", "kcprtSubUnitIndex"),
)
if mibBuilder.loadTexts:
    kcprtSubUnitEntry.setStatus("mandatory")
_KcprtSubUnitIndex_Type = Integer32
_KcprtSubUnitIndex_Object = MibTableColumn
kcprtSubUnitIndex = _KcprtSubUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23, 1, 1, 1),
    _KcprtSubUnitIndex_Type()
)
kcprtSubUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    kcprtSubUnitIndex.setStatus("mandatory")


class _KcprtSubUnitModel_Type(DisplayString):
    """Custom type kcprtSubUnitModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtSubUnitModel_Type.__name__ = "DisplayString"
_KcprtSubUnitModel_Object = MibTableColumn
kcprtSubUnitModel = _KcprtSubUnitModel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23, 1, 1, 2),
    _KcprtSubUnitModel_Type()
)
kcprtSubUnitModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSubUnitModel.setStatus("mandatory")


class _KcprtSubUnitAbsoluteModel_Type(DisplayString):
    """Custom type kcprtSubUnitAbsoluteModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_KcprtSubUnitAbsoluteModel_Type.__name__ = "DisplayString"
_KcprtSubUnitAbsoluteModel_Object = MibTableColumn
kcprtSubUnitAbsoluteModel = _KcprtSubUnitAbsoluteModel_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23, 1, 1, 3),
    _KcprtSubUnitAbsoluteModel_Type()
)
kcprtSubUnitAbsoluteModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSubUnitAbsoluteModel.setStatus("mandatory")
_KcprtSubUnitTableIndex_Type = Integer32
_KcprtSubUnitTableIndex_Object = MibTableColumn
kcprtSubUnitTableIndex = _KcprtSubUnitTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23, 1, 1, 4),
    _KcprtSubUnitTableIndex_Type()
)
kcprtSubUnitTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSubUnitTableIndex.setStatus("mandatory")
_KcprtSubUnitObjectIndex_Type = Integer32
_KcprtSubUnitObjectIndex_Object = MibTableColumn
kcprtSubUnitObjectIndex = _KcprtSubUnitObjectIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 23, 1, 1, 5),
    _KcprtSubUnitObjectIndex_Type()
)
kcprtSubUnitObjectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtSubUnitObjectIndex.setStatus("mandatory")
_KcprtJob_ObjectIdentity = ObjectIdentity
kcprtJob = _KcprtJob_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1347, 43, 24)
)
_KcprtJobGeneralTable_Object = MibTable
kcprtJobGeneralTable = _KcprtJobGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 24, 1)
)
if mibBuilder.loadTexts:
    kcprtJobGeneralTable.setStatus("mandatory")
_KcprtJobGeneralEntry_Object = MibTableRow
kcprtJobGeneralEntry = _KcprtJobGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 24, 1, 1)
)
kcprtJobGeneralEntry.setIndexNames(
    (0, "HOST-RESOURCES-MIB", "hrDeviceIndex"),
)
if mibBuilder.loadTexts:
    kcprtJobGeneralEntry.setStatus("mandatory")
_KcprtJobMaxEntryNumber_Type = Integer32
_KcprtJobMaxEntryNumber_Object = MibTableColumn
kcprtJobMaxEntryNumber = _KcprtJobMaxEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 24, 1, 1, 1),
    _KcprtJobMaxEntryNumber_Type()
)
kcprtJobMaxEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtJobMaxEntryNumber.setStatus("mandatory")
_KcprtJobNewestJobIndex_Type = Integer32
_KcprtJobNewestJobIndex_Object = MibTableColumn
kcprtJobNewestJobIndex = _KcprtJobNewestJobIndex_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 24, 1, 1, 2),
    _KcprtJobNewestJobIndex_Type()
)
kcprtJobNewestJobIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    kcprtJobNewestJobIndex.setStatus("mandatory")


class _KcprtJobCancelByJobOwner_Type(DisplayString):
    """Custom type kcprtJobCancelByJobOwner based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_KcprtJobCancelByJobOwner_Type.__name__ = "DisplayString"
_KcprtJobCancelByJobOwner_Object = MibTableColumn
kcprtJobCancelByJobOwner = _KcprtJobCancelByJobOwner_Object(
    (1, 3, 6, 1, 4, 1, 1347, 43, 24, 1, 1, 3),
    _KcprtJobCancelByJobOwner_Type()
)
kcprtJobCancelByJobOwner.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    kcprtJobCancelByJobOwner.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KYOCERA-MIB",
    **{"kyocera": kyocera,
       "kcPrinter": kcPrinter,
       "kcprtGeneral": kcprtGeneral,
       "kcprtGeneralTable": kcprtGeneralTable,
       "kcprtGeneralEntry": kcprtGeneralEntry,
       "kcprtGeneralModelName": kcprtGeneralModelName,
       "kcprtOptionVersion": kcprtOptionVersion,
       "kcprtKpdlLevel": kcprtKpdlLevel,
       "kcprtSystemUpTime": kcprtSystemUpTime,
       "kcprtBinNumber": kcprtBinNumber,
       "kcprtCardSlotCapacity": kcprtCardSlotCapacity,
       "kcprtRomSlotNumber": kcprtRomSlotNumber,
       "kcprtSimmSlotCapacity": kcprtSimmSlotCapacity,
       "kcprtSimmSlotUsed": kcprtSimmSlotUsed,
       "kcprtOriginalMemorySize": kcprtOriginalMemorySize,
       "kcprtTotalMemorySize": kcprtTotalMemorySize,
       "kcprtUserMemorySize": kcprtUserMemorySize,
       "kcprtVirtualMemory": kcprtVirtualMemory,
       "kcprtPageMemorySize": kcprtPageMemorySize,
       "kcprtHostBufferSize": kcprtHostBufferSize,
       "kcprtHostBuffer1stRate": kcprtHostBuffer1stRate,
       "kcprtHostBuffer2ndRate": kcprtHostBuffer2ndRate,
       "kcprtHostBuffer3rdRate": kcprtHostBuffer3rdRate,
       "kcprtHostBufferOption": kcprtHostBufferOption,
       "kcprtBufferXoffLevel": kcprtBufferXoffLevel,
       "kcprtBufferXonLevel": kcprtBufferXonLevel,
       "kcprtFFTimeout": kcprtFFTimeout,
       "kcprtSleepTimer": kcprtSleepTimer,
       "kcprtWakeupStatusPage": kcprtWakeupStatusPage,
       "kcprtOnlineControl": kcprtOnlineControl,
       "kcprtCopyCount": kcprtCopyCount,
       "kcprtContinueKey": kcprtContinueKey,
       "kcprtSerialNumber": kcprtSerialNumber,
       "kcprtAssetNumber": kcprtAssetNumber,
       "kcprtSignature": kcprtSignature,
       "kcprtFirmParamCurrentRegister": kcprtFirmParamCurrentRegister,
       "kcprtFirmParamCurrentValue": kcprtFirmParamCurrentValue,
       "kcprtSleepMode": kcprtSleepMode,
       "kcprtAutoContinueMode": kcprtAutoContinueMode,
       "kcprtAutoContinueTimer": kcprtAutoContinueTimer,
       "kcprtAbsoluteModelName": kcprtAbsoluteModelName,
       "kcprtEquipmentID": kcprtEquipmentID,
       "kcprtMaxCopyCount": kcprtMaxCopyCount,
       "kcprtCpuTable": kcprtCpuTable,
       "kcprtCpuEntry": kcprtCpuEntry,
       "kcprtCpuIndex": kcprtCpuIndex,
       "kcprtCpuName": kcprtCpuName,
       "kcprtCpuClock": kcprtCpuClock,
       "kcprtCpuRole": kcprtCpuRole,
       "kcprtFirmwareVersion": kcprtFirmwareVersion,
       "kcprtFirmwareUpdate": kcprtFirmwareUpdate,
       "kcprtInput": kcprtInput,
       "kcprtInputTable": kcprtInputTable,
       "kcprtInputEntry": kcprtInputEntry,
       "kcprtInputIndex": kcprtInputIndex,
       "kcprtInputMPtrayMode": kcprtInputMPtrayMode,
       "kcprtInputGroupMember": kcprtInputGroupMember,
       "kcprtInputMediaListIndex": kcprtInputMediaListIndex,
       "kcprtInputStatus": kcprtInputStatus,
       "kcprtInputDialPaperSize": kcprtInputDialPaperSize,
       "kcprtInputOtherPaperSize": kcprtInputOtherPaperSize,
       "prtInputCustomDimFeedDirDeclared": prtInputCustomDimFeedDirDeclared,
       "prtInputCustomDimXFeedDirDeclared": prtInputCustomDimXFeedDirDeclared,
       "kcprnInputMediaMatrix": kcprnInputMediaMatrix,
       "kcprnInputPaperSizeIndex": kcprnInputPaperSizeIndex,
       "kcprtInputGroupTable": kcprtInputGroupTable,
       "kcprtInputGroupEntry": kcprtInputGroupEntry,
       "kcprtInputGroupIndex": kcprtInputGroupIndex,
       "kcprtInputGroupMode": kcprtInputGroupMode,
       "kcprtOutput": kcprtOutput,
       "kcprtOutputTable": kcprtOutputTable,
       "kcprtOutputEntry": kcprtOutputEntry,
       "kcprtOutputIndex": kcprtOutputIndex,
       "kcprtOutputMode": kcprtOutputMode,
       "kcprtOutputMultiMode": kcprtOutputMultiMode,
       "kcprtOutputGroupNumber": kcprtOutputGroupNumber,
       "kcprtOutputDefaultGroup": kcprtOutputDefaultGroup,
       "kcprtOutputBulkStatus": kcprtOutputBulkStatus,
       "kcprtOutputTrayMaxCapacity": kcprtOutputTrayMaxCapacity,
       "kcprtStapler": kcprtStapler,
       "kcprtStaplerConsumableState": kcprtStaplerConsumableState,
       "kcprtOutputActionOnFull": kcprtOutputActionOnFull,
       "kcprtOutputPunchStatus": kcprtOutputPunchStatus,
       "kcprtOutputStatus": kcprtOutputStatus,
       "kcprtTrayGroupTable": kcprtTrayGroupTable,
       "kcprtTrayGroupEntry": kcprtTrayGroupEntry,
       "kcprtTrayGroupIndex": kcprtTrayGroupIndex,
       "kcprtTrayGroupBeginIndex": kcprtTrayGroupBeginIndex,
       "kcprtTrayGroupEndIndex": kcprtTrayGroupEndIndex,
       "kcprtOutputTrayTable": kcprtOutputTrayTable,
       "kcprtOutputTrayEntry": kcprtOutputTrayEntry,
       "kcprtOutputTrayIndex": kcprtOutputTrayIndex,
       "kcprtOutputTrayOrder": kcprtOutputTrayOrder,
       "kcprtOutputTrayGroup": kcprtOutputTrayGroup,
       "kcprtOutputTrayCount": kcprtOutputTrayCount,
       "kcprtOutputTrayName": kcprtOutputTrayName,
       "kcprtPunchGroupTable": kcprtPunchGroupTable,
       "kcprtPunchGroupEntry": kcprtPunchGroupEntry,
       "kcprtPunchGroupIndex": kcprtPunchGroupIndex,
       "kcprtPunchGroupName": kcprtPunchGroupName,
       "kcprtPunchGroupHoleNumber": kcprtPunchGroupHoleNumber,
       "kcprtPunchGroupType": kcprtPunchGroupType,
       "kcprtMarker": kcprtMarker,
       "kcprtMarkerTable": kcprtMarkerTable,
       "kcprtMarkerEntry": kcprtMarkerEntry,
       "kcprtMarkerIndex": kcprtMarkerIndex,
       "kcprtMarkerKirLevel": kcprtMarkerKirLevel,
       "kcprtMarkerEcoprintLevel": kcprtMarkerEcoprintLevel,
       "kcprtMarkerAddressabilityFeedDirDeclared": kcprtMarkerAddressabilityFeedDirDeclared,
       "kcprtMarkerAddressabilityXFeedDirDeclared": kcprtMarkerAddressabilityXFeedDirDeclared,
       "kcprtMarkerAddressabilityFeedDirChosen": kcprtMarkerAddressabilityFeedDirChosen,
       "kcprtMarkerAddressabilityXFeedDirChosen": kcprtMarkerAddressabilityXFeedDirChosen,
       "kcprtMarkerDrumCounter": kcprtMarkerDrumCounter,
       "kcprtMarkerColorMode": kcprtMarkerColorMode,
       "kcprtMarkerBitsPerPixel": kcprtMarkerBitsPerPixel,
       "kcprtMarkerGlossMode": kcprtMarkerGlossMode,
       "kcprtMarkerServiceCount": kcprtMarkerServiceCount,
       "kcprtColorant": kcprtColorant,
       "kcprtColorantGeneralTable": kcprtColorantGeneralTable,
       "kcprtColorantGeneralEntry": kcprtColorantGeneralEntry,
       "kcprtColorQuality": kcprtColorQuality,
       "kcprtColorMatching": kcprtColorMatching,
       "kcprtColorantIdentifier": kcprtColorantIdentifier,
       "kcprtRGBSimulation": kcprtRGBSimulation,
       "kcprtCMYKSimulation": kcprtCMYKSimulation,
       "kcprtChannel": kcprtChannel,
       "kcprtChannelTable": kcprtChannelTable,
       "kcprtChannelEntry": kcprtChannelEntry,
       "kcprtChannelIndex": kcprtChannelIndex,
       "kcprtChannelMode": kcprtChannelMode,
       "kcprtChannelCopyCount": kcprtChannelCopyCount,
       "kcprtChannelResolution": kcprtChannelResolution,
       "kcprtChannelPaperSize": kcprtChannelPaperSize,
       "kcprtHostBufferRatio": kcprtHostBufferRatio,
       "kcprtChannelErrorCounter": kcprtChannelErrorCounter,
       "kcprtBuzzer": kcprtBuzzer,
       "kcprtBuzzerTable": kcprtBuzzerTable,
       "kcprtBuzzerEntry": kcprtBuzzerEntry,
       "kcprtBuzzerIndex": kcprtBuzzerIndex,
       "kcprtBuzzerOnTime": kcprtBuzzerOnTime,
       "kcprtBuzzerOffTime": kcprtBuzzerOffTime,
       "kcprtBuzzerMode": kcprtBuzzerMode,
       "kcprtBuzzerTone": kcprtBuzzerTone,
       "kcprtAlert": kcprtAlert,
       "kcprtAlertTable": kcprtAlertTable,
       "kcprtAlertEntry": kcprtAlertEntry,
       "kcprtAlertIndex": kcprtAlertIndex,
       "kcprtAlertInformation": kcprtAlertInformation,
       "kcprtAlertStateTable": kcprtAlertStateTable,
       "kcprtAlertStateEntry": kcprtAlertStateEntry,
       "kcprtAlertStateDisplayIndex": kcprtAlertStateDisplayIndex,
       "kcprtAlertStateDisplay": kcprtAlertStateDisplay,
       "kcprtAlertStateCode": kcprtAlertStateCode,
       "kcprtAlertJamLogTable": kcprtAlertJamLogTable,
       "kcprtAlertJamLogEntry": kcprtAlertJamLogEntry,
       "kcprtAlertJamLogIndex": kcprtAlertJamLogIndex,
       "kcprtAlertJamLogStamp": kcprtAlertJamLogStamp,
       "kcprtAlertJamLogFactor": kcprtAlertJamLogFactor,
       "kcprtAlertJamLogPosition": kcprtAlertJamLogPosition,
       "kcprtAlertJamLogInput": kcprtAlertJamLogInput,
       "kcprtAlertJamLogPaper": kcprtAlertJamLogPaper,
       "kcprtAlertJamLogMedia": kcprtAlertJamLogMedia,
       "kcprtAlertJamLogOutput": kcprtAlertJamLogOutput,
       "kcprtAlertCallLogTable": kcprtAlertCallLogTable,
       "kcprtAlertCallLogEntry": kcprtAlertCallLogEntry,
       "kcprtAlertCallLogIndex": kcprtAlertCallLogIndex,
       "kcprtAlertCallLogStamp": kcprtAlertCallLogStamp,
       "kcprtAlertCallLogFactor": kcprtAlertCallLogFactor,
       "kcprtAlertChangeLogTable": kcprtAlertChangeLogTable,
       "kcprtAlertChangeLogEntry": kcprtAlertChangeLogEntry,
       "kcprtAlertChangeLogIndex": kcprtAlertChangeLogIndex,
       "kcprtAlertChangeLogStamp": kcprtAlertChangeLogStamp,
       "kcprtAlertChangeLogKind": kcprtAlertChangeLogKind,
       "kcprtAlertEventCountTable": kcprtAlertEventCountTable,
       "kcprtAlertEventCountEntry": kcprtAlertEventCountEntry,
       "kcprtAlertEventCountIndex": kcprtAlertEventCountIndex,
       "kcprtAlertEventCountFactor": kcprtAlertEventCountFactor,
       "kcprtAlertEventCountValue": kcprtAlertEventCountValue,
       "kcprtMemoryResource": kcprtMemoryResource,
       "kcprtMemoryDeviceTable": kcprtMemoryDeviceTable,
       "kcprtMemoryDeviceEntry": kcprtMemoryDeviceEntry,
       "kcprtMemoryDeviceIndex": kcprtMemoryDeviceIndex,
       "kcprtMemoryDeviceLocation": kcprtMemoryDeviceLocation,
       "kcprtMemoryDeviceType": kcprtMemoryDeviceType,
       "kcprtMemoryDeviceTotalSize": kcprtMemoryDeviceTotalSize,
       "kcprtMemoryDeviceUsedSize": kcprtMemoryDeviceUsedSize,
       "kcprtMemoryDeviceStatus": kcprtMemoryDeviceStatus,
       "kcprtMemoryDeviceUnit": kcprtMemoryDeviceUnit,
       "kcprtPartitionTable": kcprtPartitionTable,
       "kcprtPartitionEntry": kcprtPartitionEntry,
       "kcprtPartitionIndex": kcprtPartitionIndex,
       "kcprtPartitionSize": kcprtPartitionSize,
       "kcprtPartitionLocation": kcprtPartitionLocation,
       "kcprtPartitionResourceType": kcprtPartitionResourceType,
       "kcprtPartitionName": kcprtPartitionName,
       "kcprtPartitionLoad": kcprtPartitionLoad,
       "kcprtMacroDataTable": kcprtMacroDataTable,
       "kcprtMacroDataEntry": kcprtMacroDataEntry,
       "kcprtMacroDataIndex": kcprtMacroDataIndex,
       "kcprtMacroDataName": kcprtMacroDataName,
       "kcprtMacroDataID": kcprtMacroDataID,
       "kcprtMacroDataType": kcprtMacroDataType,
       "kcprtMacroDataAutoLoad": kcprtMacroDataAutoLoad,
       "kcprtMacroDataLocation": kcprtMacroDataLocation,
       "kcprtMacroDataAttribute": kcprtMacroDataAttribute,
       "kcprtHostDataTable": kcprtHostDataTable,
       "kcprtHostDataEntry": kcprtHostDataEntry,
       "kcprtHostDataIndex": kcprtHostDataIndex,
       "kcprtHostDataName": kcprtHostDataName,
       "kcprtHostDataLocation": kcprtHostDataLocation,
       "kcprtHostDataAttribute": kcprtHostDataAttribute,
       "kcprtProgramDataTable": kcprtProgramDataTable,
       "kcprtProgramDataEntry": kcprtProgramDataEntry,
       "kcprtProgramDataIndex": kcprtProgramDataIndex,
       "kcprtProgramDataName": kcprtProgramDataName,
       "kcprtProgramDataType": kcprtProgramDataType,
       "kcprtProgramDataLocation": kcprtProgramDataLocation,
       "kcprtProgramDataAttribute": kcprtProgramDataAttribute,
       "kcprtMessageDataTable": kcprtMessageDataTable,
       "kcprtMessageDataEntry": kcprtMessageDataEntry,
       "kcprtMessageDataIndex": kcprtMessageDataIndex,
       "kcprtMessageDataName": kcprtMessageDataName,
       "kcprtMessageDataLocation": kcprtMessageDataLocation,
       "kcprtMessageDataAttribute": kcprtMessageDataAttribute,
       "kcprtFontDataTable": kcprtFontDataTable,
       "kcprtFontDataEntry": kcprtFontDataEntry,
       "kcprtFontDataIndex": kcprtFontDataIndex,
       "kcprtTypeFaceName": kcprtTypeFaceName,
       "kcprtFontID": kcprtFontID,
       "kcprtFontType": kcprtFontType,
       "kcprtFontLocation": kcprtFontLocation,
       "kcprtFontAttribute": kcprtFontAttribute,
       "kcprtFileStorageTable": kcprtFileStorageTable,
       "kcprtFileStorageEntry": kcprtFileStorageEntry,
       "kcprtFileStorageIndex": kcprtFileStorageIndex,
       "kcprtFileStorageLimitSize": kcprtFileStorageLimitSize,
       "kcprtFileStorageUsedSize": kcprtFileStorageUsedSize,
       "kcprtFileStorageUnit": kcprtFileStorageUnit,
       "kcprtFileStorageCounter": kcprtFileStorageCounter,
       "kcprtFileTable": kcprtFileTable,
       "kcprtFileEntry": kcprtFileEntry,
       "kcprtFileIndex": kcprtFileIndex,
       "kcprtFileName": kcprtFileName,
       "kcprtFileSize": kcprtFileSize,
       "kcprtSJobStorageTable": kcprtSJobStorageTable,
       "kcprtSJobStorageEntry": kcprtSJobStorageEntry,
       "kcprtSJobStorageIndex": kcprtSJobStorageIndex,
       "kcprtSJobStorageLimitSize": kcprtSJobStorageLimitSize,
       "kcprtSJobStorageUsedSize": kcprtSJobStorageUsedSize,
       "kcprtSJobStorageUnit": kcprtSJobStorageUnit,
       "kcprtSJobStorageStateCounter": kcprtSJobStorageStateCounter,
       "kcprtSJobStorageAttribute": kcprtSJobStorageAttribute,
       "kcprtSJobTable": kcprtSJobTable,
       "kcprtSJobEntry": kcprtSJobEntry,
       "kcprtSJobIndex": kcprtSJobIndex,
       "kcprtSjobID": kcprtSjobID,
       "kcprtSJobName": kcprtSJobName,
       "kcprtSJobOwner": kcprtSJobOwner,
       "kcprtSJobTime": kcprtSJobTime,
       "kcprtSJobPageNumber": kcprtSJobPageNumber,
       "kcprtSJobSize": kcprtSJobSize,
       "kcprtSJobStorageRef": kcprtSJobStorageRef,
       "kcprtSJobCopyCount": kcprtSJobCopyCount,
       "kcprtSJobBarcodePrintExistence": kcprtSJobBarcodePrintExistence,
       "kcprtSJobDuplexMode": kcprtSJobDuplexMode,
       "kcprtSJobOutputIndex": kcprtSJobOutputIndex,
       "kcprtSJobStaplePosition": kcprtSJobStaplePosition,
       "kcprtSJobBarcodePosition": kcprtSJobBarcodePosition,
       "kcprtSJobStapleAndFoldCount": kcprtSJobStapleAndFoldCount,
       "kcprtSJobFoldMode": kcprtSJobFoldMode,
       "kcprtSJobPunchMode": kcprtSJobPunchMode,
       "kcprtSJobTransparencySeparationMode": kcprtSJobTransparencySeparationMode,
       "kcprtSJobTransparencySeparationInputIndex": kcprtSJobTransparencySeparationInputIndex,
       "kcprtSJobRotatedCollationMode": kcprtSJobRotatedCollationMode,
       "kcprtSJobBookletMode": kcprtSJobBookletMode,
       "kcprtSJobJobOffsetMode": kcprtSJobJobOffsetMode,
       "kcprtMediaList": kcprtMediaList,
       "kcprtMediaTable": kcprtMediaTable,
       "kcprtMediaEntry": kcprtMediaEntry,
       "kcprtMediaIndex": kcprtMediaIndex,
       "kcprtMediaName": kcprtMediaName,
       "kcprtMediaWeight": kcprtMediaWeight,
       "kcprtMediaFuserMode": kcprtMediaFuserMode,
       "kcprtMediaPathType": kcprtMediaPathType,
       "kcprtMediaDensity": kcprtMediaDensity,
       "kcprtMediaManageLevel": kcprtMediaManageLevel,
       "kcprtMailBox": kcprtMailBox,
       "kcprtMailBoxTable": kcprtMailBoxTable,
       "kcprtMailBoxEntry": kcprtMailBoxEntry,
       "kcprtMailBoxIndex": kcprtMailBoxIndex,
       "kcprtMailBoxDeviceIndex": kcprtMailBoxDeviceIndex,
       "kcprtMailBoxStateCounter": kcprtMailBoxStateCounter,
       "kcprtMailBoxUsedTrays": kcprtMailBoxUsedTrays,
       "kcprtMailBoxDocumentsNumber": kcprtMailBoxDocumentsNumber,
       "kcprtMailBoxPageNumber": kcprtMailBoxPageNumber,
       "kcprtMailBoxUsedSize": kcprtMailBoxUsedSize,
       "kcprtMailBoxLimitSize": kcprtMailBoxLimitSize,
       "kcprtMailBoxMaxLimitSize": kcprtMailBoxMaxLimitSize,
       "kcprtMailBoxUnit": kcprtMailBoxUnit,
       "kcprtMailBoxAliasCheck": kcprtMailBoxAliasCheck,
       "kcprtMailBoxTrayTable": kcprtMailBoxTrayTable,
       "kcprtMailBoxTrayEntry": kcprtMailBoxTrayEntry,
       "kcprtMailBoxTrayIndex": kcprtMailBoxTrayIndex,
       "kcprtMailBoxTrayUsedFlag": kcprtMailBoxTrayUsedFlag,
       "kcprtMailBoxTrayLabel": kcprtMailBoxTrayLabel,
       "kcprtMailBoxTrayLock": kcprtMailBoxTrayLock,
       "kcprtMailBoxTrayDocumentsNumber": kcprtMailBoxTrayDocumentsNumber,
       "kcprtMailBoxTrayPageNumber": kcprtMailBoxTrayPageNumber,
       "kcprtMailBoxTrayOccupiedSize": kcprtMailBoxTrayOccupiedSize,
       "kcprtMailBoxTraySharedSize": kcprtMailBoxTraySharedSize,
       "kcprtMailBoxTrayErrorLogNumber": kcprtMailBoxTrayErrorLogNumber,
       "kcprtMailBoxTrayPurgeDocuments": kcprtMailBoxTrayPurgeDocuments,
       "kcprtMailBoxTrayReset": kcprtMailBoxTrayReset,
       "kcprtTrayJobTable": kcprtTrayJobTable,
       "kcprtTrayJobEntry": kcprtTrayJobEntry,
       "kcprtTrayJobIndex": kcprtTrayJobIndex,
       "kcprtTrayJobID": kcprtTrayJobID,
       "kcprtTrayJobName": kcprtTrayJobName,
       "kcprtTrayJobOwner": kcprtTrayJobOwner,
       "kcprtTrayJobTime": kcprtTrayJobTime,
       "kcprtTrayJobPageNumber": kcprtTrayJobPageNumber,
       "kcprtTrayJobSize": kcprtTrayJobSize,
       "kcprtTrayJobStorageResult": kcprtTrayJobStorageResult,
       "kcprtSubUnit": kcprtSubUnit,
       "kcprtSubUnitTable": kcprtSubUnitTable,
       "kcprtSubUnitEntry": kcprtSubUnitEntry,
       "kcprtSubUnitIndex": kcprtSubUnitIndex,
       "kcprtSubUnitModel": kcprtSubUnitModel,
       "kcprtSubUnitAbsoluteModel": kcprtSubUnitAbsoluteModel,
       "kcprtSubUnitTableIndex": kcprtSubUnitTableIndex,
       "kcprtSubUnitObjectIndex": kcprtSubUnitObjectIndex,
       "kcprtJob": kcprtJob,
       "kcprtJobGeneralTable": kcprtJobGeneralTable,
       "kcprtJobGeneralEntry": kcprtJobGeneralEntry,
       "kcprtJobMaxEntryNumber": kcprtJobMaxEntryNumber,
       "kcprtJobNewestJobIndex": kcprtJobNewestJobIndex,
       "kcprtJobCancelByJobOwner": kcprtJobCancelByJobOwner}
)
