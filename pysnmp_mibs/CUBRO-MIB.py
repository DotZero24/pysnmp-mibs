# SNMP MIB module (CUBRO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cubro/CUBRO-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:47:50 2025
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

cubro_MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 32182)
)
if mibBuilder.loadTexts:
    cubro_MIB.setRevisions(
        ("2016-10-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EXPSUIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EXTEMPIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EXFANIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



class EXTransceiverIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )



# MIB Managed Objects in the order of their OIDs

_PacketmasterEX_ObjectIdentity = ObjectIdentity
packetmasterEX = _PacketmasterEX_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1)
)
_Environment_ObjectIdentity = ObjectIdentity
environment = _Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1)
)
_Psu_ObjectIdentity = ObjectIdentity
psu = _Psu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1)
)
_PsuNumber_Type = Integer32
_PsuNumber_Object = MibScalar
psuNumber = _PsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 1),
    _PsuNumber_Type()
)
psuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuNumber.setStatus("current")
_PsuTable_Object = MibTable
psuTable = _PsuTable_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    psuTable.setStatus("current")
_PsuEntry_Object = MibTableRow
psuEntry = _PsuEntry_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1)
)
psuEntry.setIndexNames(
    (0, "CUBRO-MIB", "psuIndex"),
)
if mibBuilder.loadTexts:
    psuEntry.setStatus("current")
_PsuIndex_Type = EXPSUIndex
_PsuIndex_Object = MibTableColumn
psuIndex = _PsuIndex_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 1),
    _PsuIndex_Type()
)
psuIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    psuIndex.setStatus("current")


class _PsuPresent_Type(DisplayString):
    """Custom type psuPresent based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuPresent_Type.__name__ = "DisplayString"
_PsuPresent_Object = MibTableColumn
psuPresent = _PsuPresent_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 2),
    _PsuPresent_Type()
)
psuPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuPresent.setStatus("current")


class _PsuPower_Type(DisplayString):
    """Custom type psuPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuPower_Type.__name__ = "DisplayString"
_PsuPower_Object = MibTableColumn
psuPower = _PsuPower_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 3),
    _PsuPower_Type()
)
psuPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuPower.setStatus("current")


class _PsuType_Type(DisplayString):
    """Custom type psuType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuType_Type.__name__ = "DisplayString"
_PsuType_Object = MibTableColumn
psuType = _PsuType_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 4),
    _PsuType_Type()
)
psuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuType.setStatus("current")


class _PsuAlert_Type(DisplayString):
    """Custom type psuAlert based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PsuAlert_Type.__name__ = "DisplayString"
_PsuAlert_Object = MibTableColumn
psuAlert = _PsuAlert_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 1, 2, 1, 5),
    _PsuAlert_Type()
)
psuAlert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    psuAlert.setStatus("current")
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2)
)
_TempNumber_Type = Integer32
_TempNumber_Object = MibScalar
tempNumber = _TempNumber_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 1),
    _TempNumber_Type()
)
tempNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempNumber.setStatus("current")
_TempTable_Object = MibTable
tempTable = _TempTable_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tempTable.setStatus("current")
_TempEntry_Object = MibTableRow
tempEntry = _TempEntry_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1)
)
tempEntry.setIndexNames(
    (0, "CUBRO-MIB", "tempIndex"),
)
if mibBuilder.loadTexts:
    tempEntry.setStatus("current")
_TempIndex_Type = EXTEMPIndex
_TempIndex_Object = MibTableColumn
tempIndex = _TempIndex_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 1),
    _TempIndex_Type()
)
tempIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tempIndex.setStatus("current")
_TempTemp_Type = Integer32
_TempTemp_Object = MibTableColumn
tempTemp = _TempTemp_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 2),
    _TempTemp_Type()
)
tempTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempTemp.setStatus("current")
_TempLowerAlarm_Type = Integer32
_TempLowerAlarm_Object = MibTableColumn
tempLowerAlarm = _TempLowerAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 3),
    _TempLowerAlarm_Type()
)
tempLowerAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempLowerAlarm.setStatus("current")
_TempHighAlarm_Type = Integer32
_TempHighAlarm_Object = MibTableColumn
tempHighAlarm = _TempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 4),
    _TempHighAlarm_Type()
)
tempHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempHighAlarm.setStatus("current")
_TempCriticalLimit_Type = Integer32
_TempCriticalLimit_Object = MibTableColumn
tempCriticalLimit = _TempCriticalLimit_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 5),
    _TempCriticalLimit_Type()
)
tempCriticalLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempCriticalLimit.setStatus("current")


class _TempPosition_Type(DisplayString):
    """Custom type tempPosition based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TempPosition_Type.__name__ = "DisplayString"
_TempPosition_Object = MibTableColumn
tempPosition = _TempPosition_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 2, 2, 1, 6),
    _TempPosition_Type()
)
tempPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempPosition.setStatus("current")
_Fan_ObjectIdentity = ObjectIdentity
fan = _Fan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3)
)
_FanNumber_Type = Integer32
_FanNumber_Object = MibScalar
fanNumber = _FanNumber_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 1),
    _FanNumber_Type()
)
fanNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanNumber.setStatus("current")
_FanTable_Object = MibTable
fanTable = _FanTable_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    fanTable.setStatus("current")
_FanEntry_Object = MibTableRow
fanEntry = _FanEntry_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1)
)
fanEntry.setIndexNames(
    (0, "CUBRO-MIB", "fanIndex"),
)
if mibBuilder.loadTexts:
    fanEntry.setStatus("current")
_FanIndex_Type = EXFANIndex
_FanIndex_Object = MibTableColumn
fanIndex = _FanIndex_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 1),
    _FanIndex_Type()
)
fanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanIndex.setStatus("current")


class _FanStatus_Type(DisplayString):
    """Custom type fanStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanStatus_Type.__name__ = "DisplayString"
_FanStatus_Object = MibTableColumn
fanStatus = _FanStatus_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 2),
    _FanStatus_Type()
)
fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanStatus.setStatus("current")


class _FanSpeedRate_Type(Gauge32):
    """Custom type fanSpeedRate based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_FanSpeedRate_Type.__name__ = "Gauge32"
_FanSpeedRate_Object = MibTableColumn
fanSpeedRate = _FanSpeedRate_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 3),
    _FanSpeedRate_Type()
)
fanSpeedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanSpeedRate.setStatus("current")


class _FanMode_Type(DisplayString):
    """Custom type fanMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FanMode_Type.__name__ = "DisplayString"
_FanMode_Object = MibTableColumn
fanMode = _FanMode_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 3, 2, 1, 4),
    _FanMode_Type()
)
fanMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanMode.setStatus("current")
_Transceiver_ObjectIdentity = ObjectIdentity
transceiver = _Transceiver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4)
)
_TransceiverNumber_Type = Integer32
_TransceiverNumber_Object = MibScalar
transceiverNumber = _TransceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 1),
    _TransceiverNumber_Type()
)
transceiverNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transceiverNumber.setStatus("current")
_TransceiverTable_Object = MibTable
transceiverTable = _TransceiverTable_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    transceiverTable.setStatus("current")
_TransceiverEntry_Object = MibTableRow
transceiverEntry = _TransceiverEntry_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1)
)
transceiverEntry.setIndexNames(
    (0, "CUBRO-MIB", "transIndex"),
)
if mibBuilder.loadTexts:
    transceiverEntry.setStatus("current")
_TransIndex_Type = EXTransceiverIndex
_TransIndex_Object = MibTableColumn
transIndex = _TransIndex_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 1),
    _TransIndex_Type()
)
transIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    transIndex.setStatus("current")


class _TransName_Type(DisplayString):
    """Custom type transName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransName_Type.__name__ = "DisplayString"
_TransName_Object = MibTableColumn
transName = _TransName_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 2),
    _TransName_Type()
)
transName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transName.setStatus("current")


class _TransDiagnosticImplemented_Type(Integer32):
    """Custom type transDiagnosticImplemented based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_TransDiagnosticImplemented_Type.__name__ = "Integer32"
_TransDiagnosticImplemented_Object = MibTableColumn
transDiagnosticImplemented = _TransDiagnosticImplemented_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 3),
    _TransDiagnosticImplemented_Type()
)
transDiagnosticImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transDiagnosticImplemented.setStatus("current")


class _TransOpticalTransmitPower_Type(DisplayString):
    """Custom type transOpticalTransmitPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalTransmitPower_Type.__name__ = "DisplayString"
_TransOpticalTransmitPower_Object = MibTableColumn
transOpticalTransmitPower = _TransOpticalTransmitPower_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 4),
    _TransOpticalTransmitPower_Type()
)
transOpticalTransmitPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalTransmitPower.setStatus("current")


class _TransOpticalTransmitHighAlarm_Type(DisplayString):
    """Custom type transOpticalTransmitHighAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalTransmitHighAlarm_Type.__name__ = "DisplayString"
_TransOpticalTransmitHighAlarm_Object = MibTableColumn
transOpticalTransmitHighAlarm = _TransOpticalTransmitHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 5),
    _TransOpticalTransmitHighAlarm_Type()
)
transOpticalTransmitHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalTransmitHighAlarm.setStatus("current")


class _TransOpticalTransmitHighWarn_Type(DisplayString):
    """Custom type transOpticalTransmitHighWarn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalTransmitHighWarn_Type.__name__ = "DisplayString"
_TransOpticalTransmitHighWarn_Object = MibTableColumn
transOpticalTransmitHighWarn = _TransOpticalTransmitHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 6),
    _TransOpticalTransmitHighWarn_Type()
)
transOpticalTransmitHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalTransmitHighWarn.setStatus("current")


class _TransOpticalTransmitLowWarn_Type(DisplayString):
    """Custom type transOpticalTransmitLowWarn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalTransmitLowWarn_Type.__name__ = "DisplayString"
_TransOpticalTransmitLowWarn_Object = MibTableColumn
transOpticalTransmitLowWarn = _TransOpticalTransmitLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 7),
    _TransOpticalTransmitLowWarn_Type()
)
transOpticalTransmitLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalTransmitLowWarn.setStatus("current")


class _TransOpticalTransmitLowAlarm_Type(DisplayString):
    """Custom type transOpticalTransmitLowAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalTransmitLowAlarm_Type.__name__ = "DisplayString"
_TransOpticalTransmitLowAlarm_Object = MibTableColumn
transOpticalTransmitLowAlarm = _TransOpticalTransmitLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 8),
    _TransOpticalTransmitLowAlarm_Type()
)
transOpticalTransmitLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalTransmitLowAlarm.setStatus("current")


class _TransOpticalReceivePower_Type(DisplayString):
    """Custom type transOpticalReceivePower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalReceivePower_Type.__name__ = "DisplayString"
_TransOpticalReceivePower_Object = MibTableColumn
transOpticalReceivePower = _TransOpticalReceivePower_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 9),
    _TransOpticalReceivePower_Type()
)
transOpticalReceivePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalReceivePower.setStatus("current")


class _TransOpticalReceiveHighAlarm_Type(DisplayString):
    """Custom type transOpticalReceiveHighAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalReceiveHighAlarm_Type.__name__ = "DisplayString"
_TransOpticalReceiveHighAlarm_Object = MibTableColumn
transOpticalReceiveHighAlarm = _TransOpticalReceiveHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 10),
    _TransOpticalReceiveHighAlarm_Type()
)
transOpticalReceiveHighAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalReceiveHighAlarm.setStatus("current")


class _TransOpticalReceiveHighWarn_Type(DisplayString):
    """Custom type transOpticalReceiveHighWarn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalReceiveHighWarn_Type.__name__ = "DisplayString"
_TransOpticalReceiveHighWarn_Object = MibTableColumn
transOpticalReceiveHighWarn = _TransOpticalReceiveHighWarn_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 11),
    _TransOpticalReceiveHighWarn_Type()
)
transOpticalReceiveHighWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalReceiveHighWarn.setStatus("current")


class _TransOpticalReceiveLowWarn_Type(DisplayString):
    """Custom type transOpticalReceiveLowWarn based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalReceiveLowWarn_Type.__name__ = "DisplayString"
_TransOpticalReceiveLowWarn_Object = MibTableColumn
transOpticalReceiveLowWarn = _TransOpticalReceiveLowWarn_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 12),
    _TransOpticalReceiveLowWarn_Type()
)
transOpticalReceiveLowWarn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalReceiveLowWarn.setStatus("current")


class _TransOpticalReceiveLowAlarm_Type(DisplayString):
    """Custom type transOpticalReceiveLowAlarm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TransOpticalReceiveLowAlarm_Type.__name__ = "DisplayString"
_TransOpticalReceiveLowAlarm_Object = MibTableColumn
transOpticalReceiveLowAlarm = _TransOpticalReceiveLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 4, 2, 1, 13),
    _TransOpticalReceiveLowAlarm_Type()
)
transOpticalReceiveLowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    transOpticalReceiveLowAlarm.setStatus("current")
_EnvConformance_ObjectIdentity = ObjectIdentity
envConformance = _EnvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10)
)
_EnvGroups_ObjectIdentity = ObjectIdentity
envGroups = _EnvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1)
)
_EnvCompliances_ObjectIdentity = ObjectIdentity
envCompliances = _EnvCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 2)
)

# Managed Objects groups

envPSUGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 1)
)
envPSUGroup.setObjects(
      *(("CUBRO-MIB", "psuNumber"),
        ("CUBRO-MIB", "psuPresent"),
        ("CUBRO-MIB", "psuPower"),
        ("CUBRO-MIB", "psuType"),
        ("CUBRO-MIB", "psuAlert"))
)
if mibBuilder.loadTexts:
    envPSUGroup.setStatus("current")

envTempGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 2)
)
envTempGroup.setObjects(
      *(("CUBRO-MIB", "tempNumber"),
        ("CUBRO-MIB", "tempTemp"),
        ("CUBRO-MIB", "tempLowerAlarm"),
        ("CUBRO-MIB", "tempHighAlarm"),
        ("CUBRO-MIB", "tempCriticalLimit"),
        ("CUBRO-MIB", "tempPosition"))
)
if mibBuilder.loadTexts:
    envTempGroup.setStatus("current")

envFanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 3)
)
envFanGroup.setObjects(
      *(("CUBRO-MIB", "fanNumber"),
        ("CUBRO-MIB", "fanStatus"),
        ("CUBRO-MIB", "fanSpeedRate"),
        ("CUBRO-MIB", "fanMode"))
)
if mibBuilder.loadTexts:
    envFanGroup.setStatus("current")

transmitterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 1, 4)
)
transmitterGroup.setObjects(
      *(("CUBRO-MIB", "transceiverNumber"),
        ("CUBRO-MIB", "transName"),
        ("CUBRO-MIB", "transDiagnosticImplemented"),
        ("CUBRO-MIB", "transOpticalTransmitPower"),
        ("CUBRO-MIB", "transOpticalTransmitHighAlarm"),
        ("CUBRO-MIB", "transOpticalTransmitHighWarn"),
        ("CUBRO-MIB", "transOpticalTransmitLowWarn"),
        ("CUBRO-MIB", "transOpticalTransmitLowAlarm"),
        ("CUBRO-MIB", "transOpticalReceivePower"),
        ("CUBRO-MIB", "transOpticalReceiveHighAlarm"),
        ("CUBRO-MIB", "transOpticalReceiveHighWarn"),
        ("CUBRO-MIB", "transOpticalReceiveLowWarn"),
        ("CUBRO-MIB", "transOpticalReceiveLowAlarm"))
)
if mibBuilder.loadTexts:
    transmitterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

envCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 32182, 1, 1, 10, 2, 1)
)
envCompliance.setObjects(
      *(("CUBRO-MIB", "envTempGroup"),
        ("CUBRO-MIB", "envPSUGroup"),
        ("CUBRO-MIB", "envTempGroup"),
        ("CUBRO-MIB", "envFanGroup"),
        ("CUBRO-MIB", "transmitterGroup"))
)
if mibBuilder.loadTexts:
    envCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CUBRO-MIB",
    **{"EXPSUIndex": EXPSUIndex,
       "EXTEMPIndex": EXTEMPIndex,
       "EXFANIndex": EXFANIndex,
       "EXTransceiverIndex": EXTransceiverIndex,
       "cubro-MIB": cubro_MIB,
       "packetmasterEX": packetmasterEX,
       "environment": environment,
       "psu": psu,
       "psuNumber": psuNumber,
       "psuTable": psuTable,
       "psuEntry": psuEntry,
       "psuIndex": psuIndex,
       "psuPresent": psuPresent,
       "psuPower": psuPower,
       "psuType": psuType,
       "psuAlert": psuAlert,
       "temperature": temperature,
       "tempNumber": tempNumber,
       "tempTable": tempTable,
       "tempEntry": tempEntry,
       "tempIndex": tempIndex,
       "tempTemp": tempTemp,
       "tempLowerAlarm": tempLowerAlarm,
       "tempHighAlarm": tempHighAlarm,
       "tempCriticalLimit": tempCriticalLimit,
       "tempPosition": tempPosition,
       "fan": fan,
       "fanNumber": fanNumber,
       "fanTable": fanTable,
       "fanEntry": fanEntry,
       "fanIndex": fanIndex,
       "fanStatus": fanStatus,
       "fanSpeedRate": fanSpeedRate,
       "fanMode": fanMode,
       "transceiver": transceiver,
       "transceiverNumber": transceiverNumber,
       "transceiverTable": transceiverTable,
       "transceiverEntry": transceiverEntry,
       "transIndex": transIndex,
       "transName": transName,
       "transDiagnosticImplemented": transDiagnosticImplemented,
       "transOpticalTransmitPower": transOpticalTransmitPower,
       "transOpticalTransmitHighAlarm": transOpticalTransmitHighAlarm,
       "transOpticalTransmitHighWarn": transOpticalTransmitHighWarn,
       "transOpticalTransmitLowWarn": transOpticalTransmitLowWarn,
       "transOpticalTransmitLowAlarm": transOpticalTransmitLowAlarm,
       "transOpticalReceivePower": transOpticalReceivePower,
       "transOpticalReceiveHighAlarm": transOpticalReceiveHighAlarm,
       "transOpticalReceiveHighWarn": transOpticalReceiveHighWarn,
       "transOpticalReceiveLowWarn": transOpticalReceiveLowWarn,
       "transOpticalReceiveLowAlarm": transOpticalReceiveLowAlarm,
       "envConformance": envConformance,
       "envGroups": envGroups,
       "envPSUGroup": envPSUGroup,
       "envTempGroup": envTempGroup,
       "envFanGroup": envFanGroup,
       "transmitterGroup": transmitterGroup,
       "envCompliances": envCompliances,
       "envCompliance": envCompliance}
)
