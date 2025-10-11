# SNMP MIB module (RAINBOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alvarion/RAINBOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:07:14 2025
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

(products,) = mibBuilder.importSymbols(
    "ALVARION-TOP-MIB",
    "products")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rainbow = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2)
)
if mibBuilder.loadTexts:
    rainbow.setRevisions(
        ("2006-06-06 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TrapSeverity(TextualConvention, Integer32):
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
          ("critical", 1),
          ("major", 2),
          ("minor", 3),
          ("warning", 4),
          ("info", 5))
    )



class Modulation(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("rBpsk12", 1),
          ("rBpsk34", 2),
          ("rQpsk12", 3),
          ("rQpsk34", 4),
          ("r16Qam12", 5),
          ("r16Qam34", 6),
          ("r64Qam23", 7),
          ("r64Qam34", 8))
    )



class LinkSpeedAndDuplex(TextualConvention, Integer32):
    status = "current"
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
        *(("unknown", 1),
          ("fullDuplex100Mbps", 2),
          ("halfDuplex100Mbps", 3),
          ("fullDuplex10Mbps", 4),
          ("halfDuplex10Mbps", 5),
          ("fullDuplex1Gbps", 6),
          ("halfDuplex1Gbps", 7))
    )



class TenthdB(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"


# MIB Managed Objects in the order of their OIDs

_RbSysConfig_ObjectIdentity = ObjectIdentity
rbSysConfig = _RbSysConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 1)
)
_RbSysGeneral_ObjectIdentity = ObjectIdentity
rbSysGeneral = _RbSysGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 1, 1)
)


class _RbSysFaultStatus_Type(Integer32):
    """Custom type rbSysFaultStatus based on Integer32"""
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
        *(("noFaults", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_RbSysFaultStatus_Type.__name__ = "Integer32"
_RbSysFaultStatus_Object = MibScalar
rbSysFaultStatus = _RbSysFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 1, 1, 1),
    _RbSysFaultStatus_Type()
)
rbSysFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysFaultStatus.setStatus("current")
_RbSysLastTrapSeqNumber_Type = Unsigned32
_RbSysLastTrapSeqNumber_Object = MibScalar
rbSysLastTrapSeqNumber = _RbSysLastTrapSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 1, 1, 2),
    _RbSysLastTrapSeqNumber_Type()
)
rbSysLastTrapSeqNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSysLastTrapSeqNumber.setStatus("current")
_RbChassisConfig_ObjectIdentity = ObjectIdentity
rbChassisConfig = _RbChassisConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2)
)
_RbSlotConfigTable_Object = MibTable
rbSlotConfigTable = _RbSlotConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbSlotConfigTable.setStatus("current")
_RbSlotConfigEntry_Object = MibTableRow
rbSlotConfigEntry = _RbSlotConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1)
)
rbSlotConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSlotNumber"),
)
if mibBuilder.loadTexts:
    rbSlotConfigEntry.setStatus("current")


class _RbSlotNumber_Type(Integer32):
    """Custom type rbSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_RbSlotNumber_Type.__name__ = "Integer32"
_RbSlotNumber_Object = MibTableColumn
rbSlotNumber = _RbSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1, 1),
    _RbSlotNumber_Type()
)
rbSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSlotNumber.setStatus("current")


class _RbSlotDetectedCard_Type(Integer32):
    """Custom type rbSlotDetectedCard based on Integer32"""
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
        *(("notInstalled", 1),
          ("unknown", 2),
          ("au", 3),
          ("npu", 4))
    )


_RbSlotDetectedCard_Type.__name__ = "Integer32"
_RbSlotDetectedCard_Object = MibTableColumn
rbSlotDetectedCard = _RbSlotDetectedCard_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1, 2),
    _RbSlotDetectedCard_Type()
)
rbSlotDetectedCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSlotDetectedCard.setStatus("current")


class _RbSlotConfiguredCard_Type(Integer32):
    """Custom type rbSlotConfiguredCard based on Integer32"""
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
        *(("notInstalled", 1),
          ("unknown", 2),
          ("au", 3),
          ("npu", 4))
    )


_RbSlotConfiguredCard_Type.__name__ = "Integer32"
_RbSlotConfiguredCard_Object = MibTableColumn
rbSlotConfiguredCard = _RbSlotConfiguredCard_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1, 3),
    _RbSlotConfiguredCard_Type()
)
rbSlotConfiguredCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSlotConfiguredCard.setStatus("current")


class _RbSlotAllowedCard_Type(Integer32):
    """Custom type rbSlotAllowedCard based on Integer32"""
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
        *(("notInstalled", 1),
          ("unknown", 2),
          ("au", 3),
          ("npu", 4))
    )


_RbSlotAllowedCard_Type.__name__ = "Integer32"
_RbSlotAllowedCard_Object = MibTableColumn
rbSlotAllowedCard = _RbSlotAllowedCard_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1, 4),
    _RbSlotAllowedCard_Type()
)
rbSlotAllowedCard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSlotAllowedCard.setStatus("current")
_RbSlotLedStatus_Type = OctetString
_RbSlotLedStatus_Object = MibTableColumn
rbSlotLedStatus = _RbSlotLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1, 5),
    _RbSlotLedStatus_Type()
)
rbSlotLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSlotLedStatus.setStatus("current")


class _RbSlotFaultStatus_Type(Integer32):
    """Custom type rbSlotFaultStatus based on Integer32"""
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
        *(("noFaults", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4),
          ("disconnected", 5))
    )


_RbSlotFaultStatus_Type.__name__ = "Integer32"
_RbSlotFaultStatus_Object = MibTableColumn
rbSlotFaultStatus = _RbSlotFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1, 6),
    _RbSlotFaultStatus_Type()
)
rbSlotFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSlotFaultStatus.setStatus("current")


class _RbSlotExtractorState_Type(Integer32):
    """Custom type rbSlotExtractorState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("opened", 2),
          ("unknown", 3))
    )


_RbSlotExtractorState_Type.__name__ = "Integer32"
_RbSlotExtractorState_Object = MibTableColumn
rbSlotExtractorState = _RbSlotExtractorState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 1, 1, 7),
    _RbSlotExtractorState_Type()
)
rbSlotExtractorState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSlotExtractorState.setStatus("current")
_RbNpuConfiguration_ObjectIdentity = ObjectIdentity
rbNpuConfiguration = _RbNpuConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2)
)
_RbNpuConfigTable_Object = MibTable
rbNpuConfigTable = _RbNpuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbNpuConfigTable.setStatus("current")
_RbNpuConfigEntry_Object = MibTableRow
rbNpuConfigEntry = _RbNpuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1)
)
rbNpuConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSlotNumber"),
)
if mibBuilder.loadTexts:
    rbNpuConfigEntry.setStatus("current")
_RbNpuSerialNo_Type = DisplayString
_RbNpuSerialNo_Object = MibTableColumn
rbNpuSerialNo = _RbNpuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 1),
    _RbNpuSerialNo_Type()
)
rbNpuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuSerialNo.setStatus("current")


class _RbNpuSysName_Type(DisplayString):
    """Custom type rbNpuSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbNpuSysName_Type.__name__ = "DisplayString"
_RbNpuSysName_Object = MibTableColumn
rbNpuSysName = _RbNpuSysName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 2),
    _RbNpuSysName_Type()
)
rbNpuSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuSysName.setStatus("current")


class _RbNpuFaultStatus_Type(Integer32):
    """Custom type rbNpuFaultStatus based on Integer32"""
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
        *(("noFaults", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4),
          ("disconnected", 5))
    )


_RbNpuFaultStatus_Type.__name__ = "Integer32"
_RbNpuFaultStatus_Object = MibTableColumn
rbNpuFaultStatus = _RbNpuFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 3),
    _RbNpuFaultStatus_Type()
)
rbNpuFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuFaultStatus.setStatus("current")
_RbNpuHwRevision_Type = DisplayString
_RbNpuHwRevision_Object = MibTableColumn
rbNpuHwRevision = _RbNpuHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 4),
    _RbNpuHwRevision_Type()
)
rbNpuHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuHwRevision.setStatus("current")


class _RbNpuOperSwFileName_Type(DisplayString):
    """Custom type rbNpuOperSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbNpuOperSwFileName_Type.__name__ = "DisplayString"
_RbNpuOperSwFileName_Object = MibTableColumn
rbNpuOperSwFileName = _RbNpuOperSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 5),
    _RbNpuOperSwFileName_Type()
)
rbNpuOperSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuOperSwFileName.setStatus("current")


class _RbNpuOperSwVersion_Type(DisplayString):
    """Custom type rbNpuOperSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbNpuOperSwVersion_Type.__name__ = "DisplayString"
_RbNpuOperSwVersion_Object = MibTableColumn
rbNpuOperSwVersion = _RbNpuOperSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 6),
    _RbNpuOperSwVersion_Type()
)
rbNpuOperSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuOperSwVersion.setStatus("current")


class _RbNpuShadowSwFileName_Type(DisplayString):
    """Custom type rbNpuShadowSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbNpuShadowSwFileName_Type.__name__ = "DisplayString"
_RbNpuShadowSwFileName_Object = MibTableColumn
rbNpuShadowSwFileName = _RbNpuShadowSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 7),
    _RbNpuShadowSwFileName_Type()
)
rbNpuShadowSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuShadowSwFileName.setStatus("current")


class _RbNpuShadowSwVersion_Type(DisplayString):
    """Custom type rbNpuShadowSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbNpuShadowSwVersion_Type.__name__ = "DisplayString"
_RbNpuShadowSwVersion_Object = MibTableColumn
rbNpuShadowSwVersion = _RbNpuShadowSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 8),
    _RbNpuShadowSwVersion_Type()
)
rbNpuShadowSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuShadowSwVersion.setStatus("current")


class _RbNpuRunningSoftware_Type(Integer32):
    """Custom type rbNpuRunningSoftware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("shadow", 2))
    )


_RbNpuRunningSoftware_Type.__name__ = "Integer32"
_RbNpuRunningSoftware_Object = MibTableColumn
rbNpuRunningSoftware = _RbNpuRunningSoftware_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 9),
    _RbNpuRunningSoftware_Type()
)
rbNpuRunningSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuRunningSoftware.setStatus("current")


class _RbNpuOperVersionValidity_Type(Integer32):
    """Custom type rbNpuOperVersionValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("corrupted", 1),
          ("valid", 2),
          ("unknown", 3))
    )


_RbNpuOperVersionValidity_Type.__name__ = "Integer32"
_RbNpuOperVersionValidity_Object = MibTableColumn
rbNpuOperVersionValidity = _RbNpuOperVersionValidity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 10),
    _RbNpuOperVersionValidity_Type()
)
rbNpuOperVersionValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuOperVersionValidity.setStatus("current")


class _RbNpuShadowVersionValidity_Type(Integer32):
    """Custom type rbNpuShadowVersionValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("corrupted", 1),
          ("valid", 2),
          ("unknown", 3))
    )


_RbNpuShadowVersionValidity_Type.__name__ = "Integer32"
_RbNpuShadowVersionValidity_Object = MibTableColumn
rbNpuShadowVersionValidity = _RbNpuShadowVersionValidity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 11),
    _RbNpuShadowVersionValidity_Type()
)
rbNpuShadowVersionValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuShadowVersionValidity.setStatus("current")


class _RbNpuRedundancyStatus_Type(Integer32):
    """Custom type rbNpuRedundancyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2))
    )


_RbNpuRedundancyStatus_Type.__name__ = "Integer32"
_RbNpuRedundancyStatus_Object = MibTableColumn
rbNpuRedundancyStatus = _RbNpuRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 12),
    _RbNpuRedundancyStatus_Type()
)
rbNpuRedundancyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuRedundancyStatus.setStatus("current")


class _RbNpuUnitControl_Type(Integer32):
    """Custom type rbNpuUnitControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("reset", 2),
          ("resetAndRunFromShadow", 4),
          ("makeRunningVersionOperational", 5))
    )


_RbNpuUnitControl_Type.__name__ = "Integer32"
_RbNpuUnitControl_Object = MibTableColumn
rbNpuUnitControl = _RbNpuUnitControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 13),
    _RbNpuUnitControl_Type()
)
rbNpuUnitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuUnitControl.setStatus("current")


class _RbNpuSetDefaults_Type(Integer32):
    """Custom type rbNpuSetDefaults based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("factoryDefault", 2),
          ("partialDefault", 3),
          ("customerDefault", 4),
          ("partialCustomerDefault", 5))
    )


_RbNpuSetDefaults_Type.__name__ = "Integer32"
_RbNpuSetDefaults_Object = MibTableColumn
rbNpuSetDefaults = _RbNpuSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 14),
    _RbNpuSetDefaults_Type()
)
rbNpuSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuSetDefaults.setStatus("current")


class _RbNpuHwConfigDescription_Type(DisplayString):
    """Custom type rbNpuHwConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbNpuHwConfigDescription_Type.__name__ = "DisplayString"
_RbNpuHwConfigDescription_Object = MibTableColumn
rbNpuHwConfigDescription = _RbNpuHwConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 15),
    _RbNpuHwConfigDescription_Type()
)
rbNpuHwConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuHwConfigDescription.setStatus("current")


class _RbNpuManagementInterface_Type(Integer32):
    """Custom type rbNpuManagementInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("managementPort", 1),
          ("managementAndDataPort", 2))
    )


_RbNpuManagementInterface_Type.__name__ = "Integer32"
_RbNpuManagementInterface_Object = MibTableColumn
rbNpuManagementInterface = _RbNpuManagementInterface_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 16),
    _RbNpuManagementInterface_Type()
)
rbNpuManagementInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuManagementInterface.setStatus("current")


class _RbNpuCreateConfigFile_Type(DisplayString):
    """Custom type rbNpuCreateConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RbNpuCreateConfigFile_Type.__name__ = "DisplayString"
_RbNpuCreateConfigFile_Object = MibTableColumn
rbNpuCreateConfigFile = _RbNpuCreateConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 17),
    _RbNpuCreateConfigFile_Type()
)
rbNpuCreateConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuCreateConfigFile.setStatus("current")


class _RbNpuCreateBackupConfigFile_Type(Integer32):
    """Custom type rbNpuCreateBackupConfigFile based on Integer32"""
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
        *(("cfgFileNone", 0),
          ("cfgFileFull", 1),
          ("cfgFileProfiles", 2),
          ("cfgFileProfilesServices", 3),
          ("cfgFileFiltering", 4),
          ("cfgFileTraps", 5),
          ("cfgFileNmsSync", 6),
          ("cfgFileSUSync", 7))
    )


_RbNpuCreateBackupConfigFile_Type.__name__ = "Integer32"
_RbNpuCreateBackupConfigFile_Object = MibTableColumn
rbNpuCreateBackupConfigFile = _RbNpuCreateBackupConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 18),
    _RbNpuCreateBackupConfigFile_Type()
)
rbNpuCreateBackupConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuCreateBackupConfigFile.setStatus("current")
_RbNpuCumulativePowerOnTime_Type = Unsigned32
_RbNpuCumulativePowerOnTime_Object = MibTableColumn
rbNpuCumulativePowerOnTime = _RbNpuCumulativePowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 19),
    _RbNpuCumulativePowerOnTime_Type()
)
rbNpuCumulativePowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuCumulativePowerOnTime.setStatus("current")


class _RbNpuBootSwVersion_Type(DisplayString):
    """Custom type rbNpuBootSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbNpuBootSwVersion_Type.__name__ = "DisplayString"
_RbNpuBootSwVersion_Object = MibTableColumn
rbNpuBootSwVersion = _RbNpuBootSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 20),
    _RbNpuBootSwVersion_Type()
)
rbNpuBootSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuBootSwVersion.setStatus("current")
_RbNpuTemperature_Type = Integer32
_RbNpuTemperature_Object = MibTableColumn
rbNpuTemperature = _RbNpuTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 21),
    _RbNpuTemperature_Type()
)
rbNpuTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuTemperature.setStatus("current")


class _RbNpuDrapTtlRetries_Type(Integer32):
    """Custom type rbNpuDrapTtlRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_RbNpuDrapTtlRetries_Type.__name__ = "Integer32"
_RbNpuDrapTtlRetries_Object = MibTableColumn
rbNpuDrapTtlRetries = _RbNpuDrapTtlRetries_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 22),
    _RbNpuDrapTtlRetries_Type()
)
rbNpuDrapTtlRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuDrapTtlRetries.setStatus("current")


class _RbNpuRedundantCPLDVersion_Type(Integer32):
    """Custom type rbNpuRedundantCPLDVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RbNpuRedundantCPLDVersion_Type.__name__ = "Integer32"
_RbNpuRedundantCPLDVersion_Object = MibTableColumn
rbNpuRedundantCPLDVersion = _RbNpuRedundantCPLDVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 1, 1, 23),
    _RbNpuRedundantCPLDVersion_Type()
)
rbNpuRedundantCPLDVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNpuRedundantCPLDVersion.setStatus("current")
_RbNpuBridgingParameters_ObjectIdentity = ObjectIdentity
rbNpuBridgingParameters = _RbNpuBridgingParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 2)
)


class _RbNpuBridgeAgingTime_Type(Integer32):
    """Custom type rbNpuBridgeAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_RbNpuBridgeAgingTime_Type.__name__ = "Integer32"
_RbNpuBridgeAgingTime_Object = MibScalar
rbNpuBridgeAgingTime = _RbNpuBridgeAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 2, 1),
    _RbNpuBridgeAgingTime_Type()
)
rbNpuBridgeAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbNpuBridgeAgingTime.setStatus("current")
_RbNpuFrequencyBandsParameters_ObjectIdentity = ObjectIdentity
rbNpuFrequencyBandsParameters = _RbNpuFrequencyBandsParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3)
)
_RbFrequencyBandsFileVersion_Type = Unsigned32
_RbFrequencyBandsFileVersion_Object = MibScalar
rbFrequencyBandsFileVersion = _RbFrequencyBandsFileVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 1),
    _RbFrequencyBandsFileVersion_Type()
)
rbFrequencyBandsFileVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandsFileVersion.setStatus("current")
_RbFrequencyBandsTable_Object = MibTable
rbFrequencyBandsTable = _RbFrequencyBandsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    rbFrequencyBandsTable.setStatus("current")
_RbFrequencyBandsEntry_Object = MibTableRow
rbFrequencyBandsEntry = _RbFrequencyBandsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1)
)
rbFrequencyBandsEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbFrequencyBandId"),
)
if mibBuilder.loadTexts:
    rbFrequencyBandsEntry.setStatus("current")
_RbFrequencyBandId_Type = Unsigned32
_RbFrequencyBandId_Object = MibTableColumn
rbFrequencyBandId = _RbFrequencyBandId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 1),
    _RbFrequencyBandId_Type()
)
rbFrequencyBandId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandId.setStatus("current")


class _RbFrequencyBandName_Type(DisplayString):
    """Custom type rbFrequencyBandName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RbFrequencyBandName_Type.__name__ = "DisplayString"
_RbFrequencyBandName_Object = MibTableColumn
rbFrequencyBandName = _RbFrequencyBandName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 2),
    _RbFrequencyBandName_Type()
)
rbFrequencyBandName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandName.setStatus("current")


class _RbFrequencyBandRevision_Type(DisplayString):
    """Custom type rbFrequencyBandRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbFrequencyBandRevision_Type.__name__ = "DisplayString"
_RbFrequencyBandRevision_Object = MibTableColumn
rbFrequencyBandRevision = _RbFrequencyBandRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 3),
    _RbFrequencyBandRevision_Type()
)
rbFrequencyBandRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandRevision.setStatus("current")
_RbFrequencyBandGroupId_Type = Unsigned32
_RbFrequencyBandGroupId_Object = MibTableColumn
rbFrequencyBandGroupId = _RbFrequencyBandGroupId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 4),
    _RbFrequencyBandGroupId_Type()
)
rbFrequencyBandGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandGroupId.setStatus("current")
_RbFrequencyBandStartFrequency_Type = Unsigned32
_RbFrequencyBandStartFrequency_Object = MibTableColumn
rbFrequencyBandStartFrequency = _RbFrequencyBandStartFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 5),
    _RbFrequencyBandStartFrequency_Type()
)
rbFrequencyBandStartFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandStartFrequency.setStatus("current")
_RbFrequencyBandStopFrequency_Type = Unsigned32
_RbFrequencyBandStopFrequency_Object = MibTableColumn
rbFrequencyBandStopFrequency = _RbFrequencyBandStopFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 6),
    _RbFrequencyBandStopFrequency_Type()
)
rbFrequencyBandStopFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandStopFrequency.setStatus("current")
_RbFrequencyBandStep_Type = Unsigned32
_RbFrequencyBandStep_Object = MibTableColumn
rbFrequencyBandStep = _RbFrequencyBandStep_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 7),
    _RbFrequencyBandStep_Type()
)
rbFrequencyBandStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandStep.setStatus("current")
_RbFrequencyBandDuplexSeparation_Type = Integer32
_RbFrequencyBandDuplexSeparation_Object = MibTableColumn
rbFrequencyBandDuplexSeparation = _RbFrequencyBandDuplexSeparation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 2, 3, 2, 1, 8),
    _RbFrequencyBandDuplexSeparation_Type()
)
rbFrequencyBandDuplexSeparation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbFrequencyBandDuplexSeparation.setStatus("current")
_RbAuConfigTable_Object = MibTable
rbAuConfigTable = _RbAuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    rbAuConfigTable.setStatus("current")
_RbAuConfigEntry_Object = MibTableRow
rbAuConfigEntry = _RbAuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1)
)
rbAuConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSlotNumber"),
)
if mibBuilder.loadTexts:
    rbAuConfigEntry.setStatus("current")
_RbAuSerialNo_Type = DisplayString
_RbAuSerialNo_Object = MibTableColumn
rbAuSerialNo = _RbAuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 1),
    _RbAuSerialNo_Type()
)
rbAuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuSerialNo.setStatus("current")


class _RbAuSysName_Type(DisplayString):
    """Custom type rbAuSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbAuSysName_Type.__name__ = "DisplayString"
_RbAuSysName_Object = MibTableColumn
rbAuSysName = _RbAuSysName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 2),
    _RbAuSysName_Type()
)
rbAuSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuSysName.setStatus("current")


class _RbAuFaultStatus_Type(Integer32):
    """Custom type rbAuFaultStatus based on Integer32"""
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
        *(("noFaults", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4),
          ("disconnected", 5))
    )


_RbAuFaultStatus_Type.__name__ = "Integer32"
_RbAuFaultStatus_Object = MibTableColumn
rbAuFaultStatus = _RbAuFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 3),
    _RbAuFaultStatus_Type()
)
rbAuFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuFaultStatus.setStatus("current")
_RbAuIduTemperature_Type = Integer32
_RbAuIduTemperature_Object = MibTableColumn
rbAuIduTemperature = _RbAuIduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 4),
    _RbAuIduTemperature_Type()
)
rbAuIduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuIduTemperature.setStatus("current")
_RbAuIduHwRevision_Type = DisplayString
_RbAuIduHwRevision_Object = MibTableColumn
rbAuIduHwRevision = _RbAuIduHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 5),
    _RbAuIduHwRevision_Type()
)
rbAuIduHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuIduHwRevision.setStatus("current")


class _RbAuOperSwFileName_Type(DisplayString):
    """Custom type rbAuOperSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbAuOperSwFileName_Type.__name__ = "DisplayString"
_RbAuOperSwFileName_Object = MibTableColumn
rbAuOperSwFileName = _RbAuOperSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 6),
    _RbAuOperSwFileName_Type()
)
rbAuOperSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOperSwFileName.setStatus("current")


class _RbAuOperSwVersion_Type(DisplayString):
    """Custom type rbAuOperSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbAuOperSwVersion_Type.__name__ = "DisplayString"
_RbAuOperSwVersion_Object = MibTableColumn
rbAuOperSwVersion = _RbAuOperSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 7),
    _RbAuOperSwVersion_Type()
)
rbAuOperSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOperSwVersion.setStatus("current")


class _RbAuShadowSwFileName_Type(DisplayString):
    """Custom type rbAuShadowSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbAuShadowSwFileName_Type.__name__ = "DisplayString"
_RbAuShadowSwFileName_Object = MibTableColumn
rbAuShadowSwFileName = _RbAuShadowSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 8),
    _RbAuShadowSwFileName_Type()
)
rbAuShadowSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuShadowSwFileName.setStatus("current")


class _RbAuShadowSwVersion_Type(DisplayString):
    """Custom type rbAuShadowSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbAuShadowSwVersion_Type.__name__ = "DisplayString"
_RbAuShadowSwVersion_Object = MibTableColumn
rbAuShadowSwVersion = _RbAuShadowSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 9),
    _RbAuShadowSwVersion_Type()
)
rbAuShadowSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuShadowSwVersion.setStatus("current")


class _RbAuRunningSoftware_Type(Integer32):
    """Custom type rbAuRunningSoftware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("shadow", 2),
          ("unknown", 3))
    )


_RbAuRunningSoftware_Type.__name__ = "Integer32"
_RbAuRunningSoftware_Object = MibTableColumn
rbAuRunningSoftware = _RbAuRunningSoftware_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 10),
    _RbAuRunningSoftware_Type()
)
rbAuRunningSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuRunningSoftware.setStatus("current")


class _RbAuUnitControl_Type(Integer32):
    """Custom type rbAuUnitControl based on Integer32"""
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
        *(("none", 1),
          ("reset", 2),
          ("putToShadow", 3),
          ("resetAndRunFromShadow", 4),
          ("makeRunningVersionOperational", 5))
    )


_RbAuUnitControl_Type.__name__ = "Integer32"
_RbAuUnitControl_Object = MibTableColumn
rbAuUnitControl = _RbAuUnitControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 11),
    _RbAuUnitControl_Type()
)
rbAuUnitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuUnitControl.setStatus("current")


class _RbAuOperVersionValidity_Type(Integer32):
    """Custom type rbAuOperVersionValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("corrupted", 1),
          ("valid", 2),
          ("unknown", 3))
    )


_RbAuOperVersionValidity_Type.__name__ = "Integer32"
_RbAuOperVersionValidity_Object = MibTableColumn
rbAuOperVersionValidity = _RbAuOperVersionValidity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 12),
    _RbAuOperVersionValidity_Type()
)
rbAuOperVersionValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOperVersionValidity.setStatus("current")


class _RbAuShadowVersionValidity_Type(Integer32):
    """Custom type rbAuShadowVersionValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("corrupted", 1),
          ("valid", 2),
          ("unknown", 3))
    )


_RbAuShadowVersionValidity_Type.__name__ = "Integer32"
_RbAuShadowVersionValidity_Object = MibTableColumn
rbAuShadowVersionValidity = _RbAuShadowVersionValidity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 13),
    _RbAuShadowVersionValidity_Type()
)
rbAuShadowVersionValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuShadowVersionValidity.setStatus("current")


class _RbAuSetDefaults_Type(Integer32):
    """Custom type rbAuSetDefaults based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("factoryDefault", 2),
          ("partialDefault", 3),
          ("customerDefault", 4),
          ("partialCustomerDefault", 5))
    )


_RbAuSetDefaults_Type.__name__ = "Integer32"
_RbAuSetDefaults_Object = MibTableColumn
rbAuSetDefaults = _RbAuSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 14),
    _RbAuSetDefaults_Type()
)
rbAuSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuSetDefaults.setStatus("current")


class _RbAuIduHwConfigDescription_Type(DisplayString):
    """Custom type rbAuIduHwConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbAuIduHwConfigDescription_Type.__name__ = "DisplayString"
_RbAuIduHwConfigDescription_Object = MibTableColumn
rbAuIduHwConfigDescription = _RbAuIduHwConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 15),
    _RbAuIduHwConfigDescription_Type()
)
rbAuIduHwConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuIduHwConfigDescription.setStatus("current")


class _RbAuOduHwConfigDescription_Type(DisplayString):
    """Custom type rbAuOduHwConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbAuOduHwConfigDescription_Type.__name__ = "DisplayString"
_RbAuOduHwConfigDescription_Object = MibTableColumn
rbAuOduHwConfigDescription = _RbAuOduHwConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 16),
    _RbAuOduHwConfigDescription_Type()
)
rbAuOduHwConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOduHwConfigDescription.setStatus("current")


class _RbAuUpgradeSwFileName_Type(DisplayString):
    """Custom type rbAuUpgradeSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbAuUpgradeSwFileName_Type.__name__ = "DisplayString"
_RbAuUpgradeSwFileName_Object = MibTableColumn
rbAuUpgradeSwFileName = _RbAuUpgradeSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 17),
    _RbAuUpgradeSwFileName_Type()
)
rbAuUpgradeSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuUpgradeSwFileName.setStatus("current")


class _RbAuOduHwRevision_Type(DisplayString):
    """Custom type rbAuOduHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbAuOduHwRevision_Type.__name__ = "DisplayString"
_RbAuOduHwRevision_Object = MibTableColumn
rbAuOduHwRevision = _RbAuOduHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 18),
    _RbAuOduHwRevision_Type()
)
rbAuOduHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOduHwRevision.setStatus("current")


class _RbAuMaxNumberOfCalls_Type(Integer32):
    """Custom type rbAuMaxNumberOfCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_RbAuMaxNumberOfCalls_Type.__name__ = "Integer32"
_RbAuMaxNumberOfCalls_Object = MibTableColumn
rbAuMaxNumberOfCalls = _RbAuMaxNumberOfCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 19),
    _RbAuMaxNumberOfCalls_Type()
)
rbAuMaxNumberOfCalls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuMaxNumberOfCalls.setStatus("current")
_RbAuNumberOfRegisteredSUs_Type = Integer32
_RbAuNumberOfRegisteredSUs_Object = MibTableColumn
rbAuNumberOfRegisteredSUs = _RbAuNumberOfRegisteredSUs_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 20),
    _RbAuNumberOfRegisteredSUs_Type()
)
rbAuNumberOfRegisteredSUs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuNumberOfRegisteredSUs.setStatus("current")


class _RbAuAirInterfaceType_Type(Integer32):
    """Custom type rbAuAirInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("typeA", 1),
          ("typeSi", 2))
    )


_RbAuAirInterfaceType_Type.__name__ = "Integer32"
_RbAuAirInterfaceType_Object = MibTableColumn
rbAuAirInterfaceType = _RbAuAirInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 21),
    _RbAuAirInterfaceType_Type()
)
rbAuAirInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuAirInterfaceType.setStatus("current")
_RbAuCumulativePowerOnTime_Type = Unsigned32
_RbAuCumulativePowerOnTime_Object = MibTableColumn
rbAuCumulativePowerOnTime = _RbAuCumulativePowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 22),
    _RbAuCumulativePowerOnTime_Type()
)
rbAuCumulativePowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuCumulativePowerOnTime.setStatus("current")


class _RbAuBeStarvationProtectLevelCurrent_Type(Integer32):
    """Custom type rbAuBeStarvationProtectLevelCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_RbAuBeStarvationProtectLevelCurrent_Type.__name__ = "Integer32"
_RbAuBeStarvationProtectLevelCurrent_Object = MibTableColumn
rbAuBeStarvationProtectLevelCurrent = _RbAuBeStarvationProtectLevelCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 23),
    _RbAuBeStarvationProtectLevelCurrent_Type()
)
rbAuBeStarvationProtectLevelCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuBeStarvationProtectLevelCurrent.setStatus("deprecated")


class _RbAuBeStarvationProtectLevelConfig_Type(Integer32):
    """Custom type rbAuBeStarvationProtectLevelConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 250),
    )


_RbAuBeStarvationProtectLevelConfig_Type.__name__ = "Integer32"
_RbAuBeStarvationProtectLevelConfig_Object = MibTableColumn
rbAuBeStarvationProtectLevelConfig = _RbAuBeStarvationProtectLevelConfig_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 24),
    _RbAuBeStarvationProtectLevelConfig_Type()
)
rbAuBeStarvationProtectLevelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuBeStarvationProtectLevelConfig.setStatus("deprecated")


class _RbAuNrtStarvationProtectLevelCurrent_Type(Integer32):
    """Custom type rbAuNrtStarvationProtectLevelCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RbAuNrtStarvationProtectLevelCurrent_Type.__name__ = "Integer32"
_RbAuNrtStarvationProtectLevelCurrent_Object = MibTableColumn
rbAuNrtStarvationProtectLevelCurrent = _RbAuNrtStarvationProtectLevelCurrent_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 25),
    _RbAuNrtStarvationProtectLevelCurrent_Type()
)
rbAuNrtStarvationProtectLevelCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuNrtStarvationProtectLevelCurrent.setStatus("deprecated")


class _RbAuNrtStarvationProtectLevelConfig_Type(Integer32):
    """Custom type rbAuNrtStarvationProtectLevelConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RbAuNrtStarvationProtectLevelConfig_Type.__name__ = "Integer32"
_RbAuNrtStarvationProtectLevelConfig_Object = MibTableColumn
rbAuNrtStarvationProtectLevelConfig = _RbAuNrtStarvationProtectLevelConfig_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 26),
    _RbAuNrtStarvationProtectLevelConfig_Type()
)
rbAuNrtStarvationProtectLevelConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuNrtStarvationProtectLevelConfig.setStatus("deprecated")


class _RbAuActiveVoiceCalls_Type(Integer32):
    """Custom type rbAuActiveVoiceCalls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_RbAuActiveVoiceCalls_Type.__name__ = "Integer32"
_RbAuActiveVoiceCalls_Object = MibTableColumn
rbAuActiveVoiceCalls = _RbAuActiveVoiceCalls_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 27),
    _RbAuActiveVoiceCalls_Type()
)
rbAuActiveVoiceCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuActiveVoiceCalls.setStatus("current")


class _RbAuSuUpgradeSwFileName_Type(DisplayString):
    """Custom type rbAuSuUpgradeSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbAuSuUpgradeSwFileName_Type.__name__ = "DisplayString"
_RbAuSuUpgradeSwFileName_Object = MibTableColumn
rbAuSuUpgradeSwFileName = _RbAuSuUpgradeSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 28),
    _RbAuSuUpgradeSwFileName_Type()
)
rbAuSuUpgradeSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuSuUpgradeSwFileName.setStatus("current")


class _RbAuSuUpgradeSwAction_Type(Integer32):
    """Custom type rbAuSuUpgradeSwAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("putToShadow", 3),
          ("runFromShadow", 4),
          ("makeShadowOperational", 5))
    )


_RbAuSuUpgradeSwAction_Type.__name__ = "Integer32"
_RbAuSuUpgradeSwAction_Object = MibTableColumn
rbAuSuUpgradeSwAction = _RbAuSuUpgradeSwAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 29),
    _RbAuSuUpgradeSwAction_Type()
)
rbAuSuUpgradeSwAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuSuUpgradeSwAction.setStatus("current")


class _RbAuClearAllSuSwUpgradeParams_Type(Integer32):
    """Custom type rbAuClearAllSuSwUpgradeParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clearAllSuSwUpgradeParams", 2))
    )


_RbAuClearAllSuSwUpgradeParams_Type.__name__ = "Integer32"
_RbAuClearAllSuSwUpgradeParams_Object = MibTableColumn
rbAuClearAllSuSwUpgradeParams = _RbAuClearAllSuSwUpgradeParams_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 30),
    _RbAuClearAllSuSwUpgradeParams_Type()
)
rbAuClearAllSuSwUpgradeParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuClearAllSuSwUpgradeParams.setStatus("current")


class _RbAuDiversityMode_Type(Integer32):
    """Custom type rbAuDiversityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noDiversity", 1),
          ("secondOrder", 2),
          ("fourthOrder", 3))
    )


_RbAuDiversityMode_Type.__name__ = "Integer32"
_RbAuDiversityMode_Object = MibTableColumn
rbAuDiversityMode = _RbAuDiversityMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 3, 1, 31),
    _RbAuDiversityMode_Type()
)
rbAuDiversityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuDiversityMode.setStatus("current")
_RbAcuConfiguration_ObjectIdentity = ObjectIdentity
rbAcuConfiguration = _RbAcuConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 6)
)


class _RbAcuOperStatus_Type(Integer32):
    """Custom type rbAcuOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failed", 2),
          ("notInstalled", 3))
    )


_RbAcuOperStatus_Type.__name__ = "Integer32"
_RbAcuOperStatus_Object = MibScalar
rbAcuOperStatus = _RbAcuOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 6, 1),
    _RbAcuOperStatus_Type()
)
rbAcuOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAcuOperStatus.setStatus("current")


class _RbAcuFaultStatus_Type(OctetString):
    """Custom type rbAcuFaultStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10


_RbAcuFaultStatus_Type.__name__ = "OctetString"
_RbAcuFaultStatus_Object = MibScalar
rbAcuFaultStatus = _RbAcuFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 6, 2),
    _RbAcuFaultStatus_Type()
)
rbAcuFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAcuFaultStatus.setStatus("current")
_RbAcuLedStatus_Type = OctetString
_RbAcuLedStatus_Object = MibScalar
rbAcuLedStatus = _RbAcuLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 6, 3),
    _RbAcuLedStatus_Type()
)
rbAcuLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAcuLedStatus.setStatus("current")
_RbPsuConfigTable_Object = MibTable
rbPsuConfigTable = _RbPsuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 7)
)
if mibBuilder.loadTexts:
    rbPsuConfigTable.setStatus("current")
_RbPsuConfigEntry_Object = MibTableRow
rbPsuConfigEntry = _RbPsuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 7, 1)
)
rbPsuConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbPsuNumber"),
)
if mibBuilder.loadTexts:
    rbPsuConfigEntry.setStatus("current")


class _RbPsuNumber_Type(Integer32):
    """Custom type rbPsuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RbPsuNumber_Type.__name__ = "Integer32"
_RbPsuNumber_Object = MibTableColumn
rbPsuNumber = _RbPsuNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 7, 1, 1),
    _RbPsuNumber_Type()
)
rbPsuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPsuNumber.setStatus("current")


class _RbPsuStatus_Type(Integer32):
    """Custom type rbPsuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2),
          ("notInstalled", 3))
    )


_RbPsuStatus_Type.__name__ = "Integer32"
_RbPsuStatus_Object = MibTableColumn
rbPsuStatus = _RbPsuStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 7, 1, 2),
    _RbPsuStatus_Type()
)
rbPsuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPsuStatus.setStatus("current")
_RbPiuConfigTable_Object = MibTable
rbPiuConfigTable = _RbPiuConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 8)
)
if mibBuilder.loadTexts:
    rbPiuConfigTable.setStatus("current")
_RbPiuConfigEntry_Object = MibTableRow
rbPiuConfigEntry = _RbPiuConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 8, 1)
)
rbPiuConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbPiuNumber"),
)
if mibBuilder.loadTexts:
    rbPiuConfigEntry.setStatus("current")


class _RbPiuNumber_Type(Integer32):
    """Custom type rbPiuNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_RbPiuNumber_Type.__name__ = "Integer32"
_RbPiuNumber_Object = MibTableColumn
rbPiuNumber = _RbPiuNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 8, 1, 1),
    _RbPiuNumber_Type()
)
rbPiuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPiuNumber.setStatus("current")


class _RbPiuStatus_Type(Integer32):
    """Custom type rbPiuStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fault", 2),
          ("unknown", 3))
    )


_RbPiuStatus_Type.__name__ = "Integer32"
_RbPiuStatus_Object = MibTableColumn
rbPiuStatus = _RbPiuStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 8, 1, 2),
    _RbPiuStatus_Type()
)
rbPiuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPiuStatus.setStatus("current")


class _RbPiuMode_Type(Integer32):
    """Custom type rbPiuMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("redundant", 2),
          ("notInstalled", 3))
    )


_RbPiuMode_Type.__name__ = "Integer32"
_RbPiuMode_Object = MibTableColumn
rbPiuMode = _RbPiuMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 8, 1, 3),
    _RbPiuMode_Type()
)
rbPiuMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbPiuMode.setStatus("current")
_RbAuHwComponentsInfoTable_Object = MibTable
rbAuHwComponentsInfoTable = _RbAuHwComponentsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9)
)
if mibBuilder.loadTexts:
    rbAuHwComponentsInfoTable.setStatus("current")
_RbAuHwComponentsInfoEntry_Object = MibTableRow
rbAuHwComponentsInfoEntry = _RbAuHwComponentsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1)
)
rbAuHwComponentsInfoEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSlotNumber"),
)
if mibBuilder.loadTexts:
    rbAuHwComponentsInfoEntry.setStatus("current")
_RbAuIduIfCardRevision_Type = DisplayString
_RbAuIduIfCardRevision_Object = MibTableColumn
rbAuIduIfCardRevision = _RbAuIduIfCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1, 1),
    _RbAuIduIfCardRevision_Type()
)
rbAuIduIfCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuIduIfCardRevision.setStatus("current")
_RbAuIduIfCardConfiguration_Type = DisplayString
_RbAuIduIfCardConfiguration_Object = MibTableColumn
rbAuIduIfCardConfiguration = _RbAuIduIfCardConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1, 2),
    _RbAuIduIfCardConfiguration_Type()
)
rbAuIduIfCardConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuIduIfCardConfiguration.setStatus("current")
_RbAuIduBootVersion_Type = DisplayString
_RbAuIduBootVersion_Object = MibTableColumn
rbAuIduBootVersion = _RbAuIduBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1, 3),
    _RbAuIduBootVersion_Type()
)
rbAuIduBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuIduBootVersion.setStatus("current")
_RbAuOduHC08Version_Type = DisplayString
_RbAuOduHC08Version_Object = MibTableColumn
rbAuOduHC08Version = _RbAuOduHC08Version_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1, 4),
    _RbAuOduHC08Version_Type()
)
rbAuOduHC08Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOduHC08Version.setStatus("current")
_RbAuOduCpldVersion_Type = DisplayString
_RbAuOduCpldVersion_Object = MibTableColumn
rbAuOduCpldVersion = _RbAuOduCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1, 5),
    _RbAuOduCpldVersion_Type()
)
rbAuOduCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOduCpldVersion.setStatus("current")
_RbAuOduCardSerialNumber_Type = DisplayString
_RbAuOduCardSerialNumber_Object = MibTableColumn
rbAuOduCardSerialNumber = _RbAuOduCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1, 6),
    _RbAuOduCardSerialNumber_Type()
)
rbAuOduCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuOduCardSerialNumber.setStatus("current")


class _RbAuIduType_Type(Integer32):
    """Custom type rbAuIduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("twoChannels", 1),
          ("fourChannels", 2),
          ("twoChannels-HP", 3),
          ("fourChannels-HP", 4))
    )


_RbAuIduType_Type.__name__ = "Integer32"
_RbAuIduType_Object = MibTableColumn
rbAuIduType = _RbAuIduType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 9, 1, 7),
    _RbAuIduType_Type()
)
rbAuIduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuIduType.setStatus("current")
_RbChannelConfigTable_Object = MibTable
rbChannelConfigTable = _RbChannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11)
)
if mibBuilder.loadTexts:
    rbChannelConfigTable.setStatus("current")
_RbChannelConfigEntry_Object = MibTableRow
rbChannelConfigEntry = _RbChannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1)
)
rbChannelConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSlotNumber"),
    (0, "RAINBOW-MIB", "rbChannelId"),
)
if mibBuilder.loadTexts:
    rbChannelConfigEntry.setStatus("current")


class _RbChannelId_Type(Integer32):
    """Custom type rbChannelId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RbChannelId_Type.__name__ = "Integer32"
_RbChannelId_Object = MibTableColumn
rbChannelId = _RbChannelId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 1),
    _RbChannelId_Type()
)
rbChannelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbChannelId.setStatus("current")


class _RbChannelAssociatedRadioClusterId_Type(Integer32):
    """Custom type rbChannelAssociatedRadioClusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_RbChannelAssociatedRadioClusterId_Type.__name__ = "Integer32"
_RbChannelAssociatedRadioClusterId_Object = MibTableColumn
rbChannelAssociatedRadioClusterId = _RbChannelAssociatedRadioClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 2),
    _RbChannelAssociatedRadioClusterId_Type()
)
rbChannelAssociatedRadioClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbChannelAssociatedRadioClusterId.setStatus("current")


class _RbChannelAssociatedOduId_Type(Integer32):
    """Custom type rbChannelAssociatedOduId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_RbChannelAssociatedOduId_Type.__name__ = "Integer32"
_RbChannelAssociatedOduId_Object = MibTableColumn
rbChannelAssociatedOduId = _RbChannelAssociatedOduId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 3),
    _RbChannelAssociatedOduId_Type()
)
rbChannelAssociatedOduId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbChannelAssociatedOduId.setStatus("current")
_RbChannelTxFrequency_Type = DisplayString
_RbChannelTxFrequency_Object = MibTableColumn
rbChannelTxFrequency = _RbChannelTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 4),
    _RbChannelTxFrequency_Type()
)
rbChannelTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbChannelTxFrequency.setStatus("current")
_RbChannelRxFrequency_Type = DisplayString
_RbChannelRxFrequency_Object = MibTableColumn
rbChannelRxFrequency = _RbChannelRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 5),
    _RbChannelRxFrequency_Type()
)
rbChannelRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbChannelRxFrequency.setStatus("current")


class _RbChannelAdminStatus_Type(Integer32):
    """Custom type rbChannelAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RbChannelAdminStatus_Type.__name__ = "Integer32"
_RbChannelAdminStatus_Object = MibTableColumn
rbChannelAdminStatus = _RbChannelAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 6),
    _RbChannelAdminStatus_Type()
)
rbChannelAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbChannelAdminStatus.setStatus("current")
_RbChannelConfiguredTxFrequency_Type = DisplayString
_RbChannelConfiguredTxFrequency_Object = MibTableColumn
rbChannelConfiguredTxFrequency = _RbChannelConfiguredTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 7),
    _RbChannelConfiguredTxFrequency_Type()
)
rbChannelConfiguredTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbChannelConfiguredTxFrequency.setStatus("current")
_RbChannelOduActualFrequencyBand_Type = Integer32
_RbChannelOduActualFrequencyBand_Object = MibTableColumn
rbChannelOduActualFrequencyBand = _RbChannelOduActualFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 8),
    _RbChannelOduActualFrequencyBand_Type()
)
rbChannelOduActualFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbChannelOduActualFrequencyBand.setStatus("current")


class _RbChannelOperStatus_Type(Integer32):
    """Custom type rbChannelOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("up", 1),
          ("down", 2))
    )


_RbChannelOperStatus_Type.__name__ = "Integer32"
_RbChannelOperStatus_Object = MibTableColumn
rbChannelOperStatus = _RbChannelOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 2, 11, 1, 9),
    _RbChannelOperStatus_Type()
)
rbChannelOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbChannelOperStatus.setStatus("current")
_RbSubcriberUnitConfig_ObjectIdentity = ObjectIdentity
rbSubcriberUnitConfig = _RbSubcriberUnitConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5)
)
_RbRegisteredSuTable_Object = MibTable
rbRegisteredSuTable = _RbRegisteredSuTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    rbRegisteredSuTable.setStatus("current")
_RbRegisteredSuEntry_Object = MibTableRow
rbRegisteredSuEntry = _RbRegisteredSuEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1)
)
rbRegisteredSuEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
)
if mibBuilder.loadTexts:
    rbRegisteredSuEntry.setStatus("current")
_RbAuId_Type = Integer32
_RbAuId_Object = MibTableColumn
rbAuId = _RbAuId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 1),
    _RbAuId_Type()
)
rbAuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuId.setStatus("current")
_RbSuMacAddr_Type = MacAddress
_RbSuMacAddr_Object = MibTableColumn
rbSuMacAddr = _RbSuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 2),
    _RbSuMacAddr_Type()
)
rbSuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuMacAddr.setStatus("current")
_RbSuID_Type = Integer32
_RbSuID_Object = MibTableColumn
rbSuID = _RbSuID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 3),
    _RbSuID_Type()
)
rbSuID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuID.setStatus("current")


class _RbSuRegistrationState_Type(Integer32):
    """Custom type rbSuRegistrationState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRegistered", 1),
          ("registered", 2),
          ("authenticated", 3))
    )


_RbSuRegistrationState_Type.__name__ = "Integer32"
_RbSuRegistrationState_Object = MibTableColumn
rbSuRegistrationState = _RbSuRegistrationState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 4),
    _RbSuRegistrationState_Type()
)
rbSuRegistrationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuRegistrationState.setStatus("current")


class _RbSuPersistence_Type(Integer32):
    """Custom type rbSuPersistence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("temporary", 1),
          ("permanent", 2))
    )


_RbSuPersistence_Type.__name__ = "Integer32"
_RbSuPersistence_Object = MibTableColumn
rbSuPersistence = _RbSuPersistence_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 5),
    _RbSuPersistence_Type()
)
rbSuPersistence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuPersistence.setStatus("current")
_RbSuSerialNo_Type = DisplayString
_RbSuSerialNo_Object = MibTableColumn
rbSuSerialNo = _RbSuSerialNo_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 6),
    _RbSuSerialNo_Type()
)
rbSuSerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuSerialNo.setStatus("current")


class _RbSuSysName_Type(DisplayString):
    """Custom type rbSuSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbSuSysName_Type.__name__ = "DisplayString"
_RbSuSysName_Object = MibTableColumn
rbSuSysName = _RbSuSysName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 7),
    _RbSuSysName_Type()
)
rbSuSysName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuSysName.setStatus("current")


class _RbSuFaultStatus_Type(Integer32):
    """Custom type rbSuFaultStatus based on Integer32"""
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
        *(("noFaults", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4),
          ("disconnected", 5))
    )


_RbSuFaultStatus_Type.__name__ = "Integer32"
_RbSuFaultStatus_Object = MibTableColumn
rbSuFaultStatus = _RbSuFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 8),
    _RbSuFaultStatus_Type()
)
rbSuFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuFaultStatus.setStatus("current")
_RbSuHwRevision_Type = DisplayString
_RbSuHwRevision_Object = MibTableColumn
rbSuHwRevision = _RbSuHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 9),
    _RbSuHwRevision_Type()
)
rbSuHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuHwRevision.setStatus("current")


class _RbSuOperSwFileName_Type(DisplayString):
    """Custom type rbSuOperSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbSuOperSwFileName_Type.__name__ = "DisplayString"
_RbSuOperSwFileName_Object = MibTableColumn
rbSuOperSwFileName = _RbSuOperSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 10),
    _RbSuOperSwFileName_Type()
)
rbSuOperSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuOperSwFileName.setStatus("current")


class _RbSuOperSwVersion_Type(DisplayString):
    """Custom type rbSuOperSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbSuOperSwVersion_Type.__name__ = "DisplayString"
_RbSuOperSwVersion_Object = MibTableColumn
rbSuOperSwVersion = _RbSuOperSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 11),
    _RbSuOperSwVersion_Type()
)
rbSuOperSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuOperSwVersion.setStatus("current")


class _RbSuShadowSwFileName_Type(DisplayString):
    """Custom type rbSuShadowSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_RbSuShadowSwFileName_Type.__name__ = "DisplayString"
_RbSuShadowSwFileName_Object = MibTableColumn
rbSuShadowSwFileName = _RbSuShadowSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 12),
    _RbSuShadowSwFileName_Type()
)
rbSuShadowSwFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuShadowSwFileName.setStatus("current")


class _RbSuShadowSwVersion_Type(DisplayString):
    """Custom type rbSuShadowSwVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_RbSuShadowSwVersion_Type.__name__ = "DisplayString"
_RbSuShadowSwVersion_Object = MibTableColumn
rbSuShadowSwVersion = _RbSuShadowSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 13),
    _RbSuShadowSwVersion_Type()
)
rbSuShadowSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuShadowSwVersion.setStatus("current")


class _RbSuRunningSoftware_Type(Integer32):
    """Custom type rbSuRunningSoftware based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("operational", 1),
          ("shadow", 2),
          ("unknown", 3))
    )


_RbSuRunningSoftware_Type.__name__ = "Integer32"
_RbSuRunningSoftware_Object = MibTableColumn
rbSuRunningSoftware = _RbSuRunningSoftware_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 14),
    _RbSuRunningSoftware_Type()
)
rbSuRunningSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuRunningSoftware.setStatus("current")


class _RbSuOperVersionValidity_Type(Integer32):
    """Custom type rbSuOperVersionValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("corrupted", 1),
          ("valid", 2),
          ("unknown", 3))
    )


_RbSuOperVersionValidity_Type.__name__ = "Integer32"
_RbSuOperVersionValidity_Object = MibTableColumn
rbSuOperVersionValidity = _RbSuOperVersionValidity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 15),
    _RbSuOperVersionValidity_Type()
)
rbSuOperVersionValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuOperVersionValidity.setStatus("current")


class _RbSuShadowVersionValidity_Type(Integer32):
    """Custom type rbSuShadowVersionValidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("corrupted", 1),
          ("valid", 2),
          ("unknown", 3))
    )


_RbSuShadowVersionValidity_Type.__name__ = "Integer32"
_RbSuShadowVersionValidity_Object = MibTableColumn
rbSuShadowVersionValidity = _RbSuShadowVersionValidity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 16),
    _RbSuShadowVersionValidity_Type()
)
rbSuShadowVersionValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuShadowVersionValidity.setStatus("current")


class _RbSuUnitControl_Type(Integer32):
    """Custom type rbSuUnitControl based on Integer32"""
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
        *(("none", 1),
          ("reset", 2),
          ("putToShadow", 3),
          ("resetAndRunFromShadow", 4),
          ("makeRunningVersionOperational", 5))
    )


_RbSuUnitControl_Type.__name__ = "Integer32"
_RbSuUnitControl_Object = MibTableColumn
rbSuUnitControl = _RbSuUnitControl_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 17),
    _RbSuUnitControl_Type()
)
rbSuUnitControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuUnitControl.setStatus("current")


class _RbSuSetDefaults_Type(Integer32):
    """Custom type rbSuSetDefaults based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("factoryDefault", 2),
          ("partialDefault", 3),
          ("customerDefault", 4),
          ("partialCustomerDefault", 5))
    )


_RbSuSetDefaults_Type.__name__ = "Integer32"
_RbSuSetDefaults_Object = MibTableColumn
rbSuSetDefaults = _RbSuSetDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 18),
    _RbSuSetDefaults_Type()
)
rbSuSetDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuSetDefaults.setStatus("current")


class _RbSuAllowedUsersType_Type(Integer32):
    """Custom type rbSuAllowedUsersType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("residentional", 1),
          ("unknown", 2))
    )


_RbSuAllowedUsersType_Type.__name__ = "Integer32"
_RbSuAllowedUsersType_Object = MibTableColumn
rbSuAllowedUsersType = _RbSuAllowedUsersType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 19),
    _RbSuAllowedUsersType_Type()
)
rbSuAllowedUsersType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuAllowedUsersType.setStatus("deprecated")


class _RbSuAllowedQoS_Type(Integer32):
    """Custom type rbSuAllowedQoS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("residentional", 1),
          ("unknown", 2))
    )


_RbSuAllowedQoS_Type.__name__ = "Integer32"
_RbSuAllowedQoS_Object = MibTableColumn
rbSuAllowedQoS = _RbSuAllowedQoS_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 20),
    _RbSuAllowedQoS_Type()
)
rbSuAllowedQoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuAllowedQoS.setStatus("deprecated")
_RbSuAllowedService_Type = OctetString
_RbSuAllowedService_Object = MibTableColumn
rbSuAllowedService = _RbSuAllowedService_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 21),
    _RbSuAllowedService_Type()
)
rbSuAllowedService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuAllowedService.setStatus("deprecated")
_RbSuRowStatus_Type = RowStatus
_RbSuRowStatus_Object = MibTableColumn
rbSuRowStatus = _RbSuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 22),
    _RbSuRowStatus_Type()
)
rbSuRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuRowStatus.setStatus("current")


class _RbSuInstallerPassword_Type(DisplayString):
    """Custom type rbSuInstallerPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RbSuInstallerPassword_Type.__name__ = "DisplayString"
_RbSuInstallerPassword_Object = MibTableColumn
rbSuInstallerPassword = _RbSuInstallerPassword_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 23),
    _RbSuInstallerPassword_Type()
)
rbSuInstallerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuInstallerPassword.setStatus("current")


class _RbSuHwConfigDescription_Type(DisplayString):
    """Custom type rbSuHwConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuHwConfigDescription_Type.__name__ = "DisplayString"
_RbSuHwConfigDescription_Object = MibTableColumn
rbSuHwConfigDescription = _RbSuHwConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 24),
    _RbSuHwConfigDescription_Type()
)
rbSuHwConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuHwConfigDescription.setStatus("current")


class _RbSuUpgradeSwFileName_Type(DisplayString):
    """Custom type rbSuUpgradeSwFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbSuUpgradeSwFileName_Type.__name__ = "DisplayString"
_RbSuUpgradeSwFileName_Object = MibTableColumn
rbSuUpgradeSwFileName = _RbSuUpgradeSwFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 25),
    _RbSuUpgradeSwFileName_Type()
)
rbSuUpgradeSwFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuUpgradeSwFileName.setStatus("current")


class _RbSuServiceType_Type(Integer32):
    """Custom type rbSuServiceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("suData", 1),
          ("suVoice", 2))
    )


_RbSuServiceType_Type.__name__ = "Integer32"
_RbSuServiceType_Object = MibTableColumn
rbSuServiceType = _RbSuServiceType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 26),
    _RbSuServiceType_Type()
)
rbSuServiceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuServiceType.setStatus("deprecated")


class _RbSuIduType_Type(Integer32):
    """Custom type rbSuIduType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              11)
        )
    )
    namedValues = NamedValues(
        *(("basic", 0),
          ("vgData4Voice2", 6),
          ("ngData4Wireless", 11))
    )


_RbSuIduType_Type.__name__ = "Integer32"
_RbSuIduType_Object = MibTableColumn
rbSuIduType = _RbSuIduType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 27),
    _RbSuIduType_Type()
)
rbSuIduType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuIduType.setStatus("current")
_RbSuExternalDevNumber_Type = Integer32
_RbSuExternalDevNumber_Object = MibTableColumn
rbSuExternalDevNumber = _RbSuExternalDevNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 28),
    _RbSuExternalDevNumber_Type()
)
rbSuExternalDevNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuExternalDevNumber.setStatus("current")


class _RbSuServiceFaultBitMap_Type(OctetString):
    """Custom type rbSuServiceFaultBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_RbSuServiceFaultBitMap_Type.__name__ = "OctetString"
_RbSuServiceFaultBitMap_Object = MibTableColumn
rbSuServiceFaultBitMap = _RbSuServiceFaultBitMap_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 29),
    _RbSuServiceFaultBitMap_Type()
)
rbSuServiceFaultBitMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuServiceFaultBitMap.setStatus("current")
_RbSuCumulativePowerOnTime_Type = Unsigned32
_RbSuCumulativePowerOnTime_Object = MibTableColumn
rbSuCumulativePowerOnTime = _RbSuCumulativePowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 30),
    _RbSuCumulativePowerOnTime_Type()
)
rbSuCumulativePowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCumulativePowerOnTime.setStatus("current")


class _RbSuOrganizationName_Type(DisplayString):
    """Custom type rbSuOrganizationName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbSuOrganizationName_Type.__name__ = "DisplayString"
_RbSuOrganizationName_Object = MibTableColumn
rbSuOrganizationName = _RbSuOrganizationName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 31),
    _RbSuOrganizationName_Type()
)
rbSuOrganizationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuOrganizationName.setStatus("current")


class _RbSuAddress_Type(DisplayString):
    """Custom type rbSuAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbSuAddress_Type.__name__ = "DisplayString"
_RbSuAddress_Object = MibTableColumn
rbSuAddress = _RbSuAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 32),
    _RbSuAddress_Type()
)
rbSuAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuAddress.setStatus("current")


class _RbSuCountry_Type(DisplayString):
    """Custom type rbSuCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_RbSuCountry_Type.__name__ = "DisplayString"
_RbSuCountry_Object = MibTableColumn
rbSuCountry = _RbSuCountry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 33),
    _RbSuCountry_Type()
)
rbSuCountry.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCountry.setStatus("current")
_RbSuMACControlNumber_Type = Integer32
_RbSuMACControlNumber_Object = MibTableColumn
rbSuMACControlNumber = _RbSuMACControlNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 34),
    _RbSuMACControlNumber_Type()
)
rbSuMACControlNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuMACControlNumber.setStatus("current")


class _RbSuAirInterfaceType_Type(Integer32):
    """Custom type rbSuAirInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("typeA", 1),
          ("typeSi", 2))
    )


_RbSuAirInterfaceType_Type.__name__ = "Integer32"
_RbSuAirInterfaceType_Object = MibTableColumn
rbSuAirInterfaceType = _RbSuAirInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 1, 1, 35),
    _RbSuAirInterfaceType_Type()
)
rbSuAirInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuAirInterfaceType.setStatus("current")
_RbSuSubDevicesTable_Object = MibTable
rbSuSubDevicesTable = _RbSuSubDevicesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 2)
)
if mibBuilder.loadTexts:
    rbSuSubDevicesTable.setStatus("current")
_RbSuSubDevicesEntry_Object = MibTableRow
rbSuSubDevicesEntry = _RbSuSubDevicesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 2, 1)
)
rbSuSubDevicesEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSubDeviceIpAddress"),
)
if mibBuilder.loadTexts:
    rbSuSubDevicesEntry.setStatus("current")
_RbSubDeviceIpAddress_Type = IpAddress
_RbSubDeviceIpAddress_Object = MibTableColumn
rbSubDeviceIpAddress = _RbSubDeviceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 2, 1, 1),
    _RbSubDeviceIpAddress_Type()
)
rbSubDeviceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSubDeviceIpAddress.setStatus("current")
_RbSuMacAddress_Type = MacAddress
_RbSuMacAddress_Object = MibTableColumn
rbSuMacAddress = _RbSuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 2, 1, 2),
    _RbSuMacAddress_Type()
)
rbSuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuMacAddress.setStatus("current")


class _RbSubDeviceType_Type(Integer32):
    """Custom type rbSubDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              5,
              6,
              7,
              11,
              23)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("vgDataVoice", 4),
          ("vgData1Voice1", 5),
          ("vgData4Voice2", 6),
          ("vgDataVoice2", 7),
          ("ngData4Wireless", 11),
          ("winetworksMSG", 23))
    )


_RbSubDeviceType_Type.__name__ = "Integer32"
_RbSubDeviceType_Object = MibTableColumn
rbSubDeviceType = _RbSubDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 2, 1, 3),
    _RbSubDeviceType_Type()
)
rbSubDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSubDeviceType.setStatus("current")
_RbSubDeviceVlanID_Type = Integer32
_RbSubDeviceVlanID_Object = MibTableColumn
rbSubDeviceVlanID = _RbSubDeviceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 2, 1, 4),
    _RbSubDeviceVlanID_Type()
)
rbSubDeviceVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSubDeviceVlanID.setStatus("current")
_RbSuHwComponentsInfoTable_Object = MibTable
rbSuHwComponentsInfoTable = _RbSuHwComponentsInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 3)
)
if mibBuilder.loadTexts:
    rbSuHwComponentsInfoTable.setStatus("current")
_RbSuHwComponentsInfoEntry_Object = MibTableRow
rbSuHwComponentsInfoEntry = _RbSuHwComponentsInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 3, 1)
)
rbSuHwComponentsInfoEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
)
if mibBuilder.loadTexts:
    rbSuHwComponentsInfoEntry.setStatus("current")
_RbSuRfCardRevision_Type = DisplayString
_RbSuRfCardRevision_Object = MibTableColumn
rbSuRfCardRevision = _RbSuRfCardRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 3, 1, 1),
    _RbSuRfCardRevision_Type()
)
rbSuRfCardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuRfCardRevision.setStatus("current")
_RbSuRfCardConfiguration_Type = DisplayString
_RbSuRfCardConfiguration_Object = MibTableColumn
rbSuRfCardConfiguration = _RbSuRfCardConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 3, 1, 2),
    _RbSuRfCardConfiguration_Type()
)
rbSuRfCardConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuRfCardConfiguration.setStatus("deprecated")
_RbSuBootVersion_Type = DisplayString
_RbSuBootVersion_Object = MibTableColumn
rbSuBootVersion = _RbSuBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 3, 1, 3),
    _RbSuBootVersion_Type()
)
rbSuBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuBootVersion.setStatus("current")


class _RbSuType_Type(Integer32):
    """Custom type rbSuType based on Integer32"""
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
        *(("unknown", 0),
          ("cpe", 1),
          ("cpePro", 2),
          ("cpeSi", 3),
          ("cpeProL", 4),
          ("cpeSiL", 5),
          ("cpe2Pro", 6),
          ("cpe2Si", 7),
          ("cpe2ProL", 8),
          ("cpe2SiL", 9))
    )


_RbSuType_Type.__name__ = "Integer32"
_RbSuType_Object = MibTableColumn
rbSuType = _RbSuType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 3, 1, 4),
    _RbSuType_Type()
)
rbSuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuType.setStatus("current")
_SuBridgingParameters_ObjectIdentity = ObjectIdentity
suBridgingParameters = _SuBridgingParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 4)
)


class _RbSuSupportDevicesLimit_Type(Integer32):
    """Custom type rbSuSupportDevicesLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("unknown", 3))
    )


_RbSuSupportDevicesLimit_Type.__name__ = "Integer32"
_RbSuSupportDevicesLimit_Object = MibScalar
rbSuSupportDevicesLimit = _RbSuSupportDevicesLimit_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 4, 1),
    _RbSuSupportDevicesLimit_Type()
)
rbSuSupportDevicesLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuSupportDevicesLimit.setStatus("current")


class _RbSuMaxNumberOfSupportedDevices_Type(Integer32):
    """Custom type rbSuMaxNumberOfSupportedDevices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 512),
    )


_RbSuMaxNumberOfSupportedDevices_Type.__name__ = "Integer32"
_RbSuMaxNumberOfSupportedDevices_Object = MibScalar
rbSuMaxNumberOfSupportedDevices = _RbSuMaxNumberOfSupportedDevices_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 4, 2),
    _RbSuMaxNumberOfSupportedDevices_Type()
)
rbSuMaxNumberOfSupportedDevices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuMaxNumberOfSupportedDevices.setStatus("current")


class _RbSuBridgeAgingTime_Type(Integer32):
    """Custom type rbSuBridgeAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_RbSuBridgeAgingTime_Type.__name__ = "Integer32"
_RbSuBridgeAgingTime_Object = MibScalar
rbSuBridgeAgingTime = _RbSuBridgeAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 4, 3),
    _RbSuBridgeAgingTime_Type()
)
rbSuBridgeAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuBridgeAgingTime.setStatus("current")
_RbMACBehindSUList_ObjectIdentity = ObjectIdentity
rbMACBehindSUList = _RbMACBehindSUList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 5)
)
_RbMACBehindSUListTable_Object = MibTable
rbMACBehindSUListTable = _RbMACBehindSUListTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 5, 1)
)
if mibBuilder.loadTexts:
    rbMACBehindSUListTable.setStatus("current")
_RbMACBehindSUListEntry_Object = MibTableRow
rbMACBehindSUListEntry = _RbMACBehindSUListEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 5, 1, 1)
)
rbMACBehindSUListEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
    (0, "RAINBOW-MIB", "rbMacBehindSuAddr"),
)
if mibBuilder.loadTexts:
    rbMACBehindSUListEntry.setStatus("current")
_RbMacBehindSuAddr_Type = MacAddress
_RbMacBehindSuAddr_Object = MibTableColumn
rbMacBehindSuAddr = _RbMacBehindSuAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 5, 1, 1, 1),
    _RbMacBehindSuAddr_Type()
)
rbMacBehindSuAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMacBehindSuAddr.setStatus("current")
_RbMacBehindSuVlan_Type = Integer32
_RbMacBehindSuVlan_Object = MibTableColumn
rbMacBehindSuVlan = _RbMacBehindSuVlan_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 5, 1, 1, 2),
    _RbMacBehindSuVlan_Type()
)
rbMacBehindSuVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbMacBehindSuVlan.setStatus("current")
_RbSiSuInfo_ObjectIdentity = ObjectIdentity
rbSiSuInfo = _RbSiSuInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 6)
)
_RbSiSuInfoTable_Object = MibTable
rbSiSuInfoTable = _RbSiSuInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 6, 1)
)
if mibBuilder.loadTexts:
    rbSiSuInfoTable.setStatus("current")
_RbSiSuInfoEntry_Object = MibTableRow
rbSiSuInfoEntry = _RbSiSuInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 6, 1, 1)
)
rbSiSuInfoEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
)
if mibBuilder.loadTexts:
    rbSiSuInfoEntry.setStatus("current")


class _RbSiSuAntennaSelection_Type(Integer32):
    """Custom type rbSiSuAntennaSelection based on Integer32"""
    defaultValue = 3

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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("internal1", 1),
          ("internal2", 2),
          ("internal3", 3),
          ("internal4", 4),
          ("internal5", 5),
          ("internal6", 6),
          ("external", 7),
          ("automatic", 8))
    )


_RbSiSuAntennaSelection_Type.__name__ = "Integer32"
_RbSiSuAntennaSelection_Object = MibTableColumn
rbSiSuAntennaSelection = _RbSiSuAntennaSelection_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 6, 1, 1, 1),
    _RbSiSuAntennaSelection_Type()
)
rbSiSuAntennaSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSiSuAntennaSelection.setStatus("current")


class _RbSiSuSmartCardStatus_Type(Integer32):
    """Custom type rbSiSuSmartCardStatus based on Integer32"""
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
        *(("unknown", 0),
          ("installed", 1),
          ("notInstalled", 2),
          ("fault", 3))
    )


_RbSiSuSmartCardStatus_Type.__name__ = "Integer32"
_RbSiSuSmartCardStatus_Object = MibTableColumn
rbSiSuSmartCardStatus = _RbSiSuSmartCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 6, 1, 1, 2),
    _RbSiSuSmartCardStatus_Type()
)
rbSiSuSmartCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSiSuSmartCardStatus.setStatus("current")


class _RbSiSuInterfaceType_Type(Integer32):
    """Custom type rbSiSuInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("ethernet", 1),
          ("usb", 2))
    )


_RbSiSuInterfaceType_Type.__name__ = "Integer32"
_RbSiSuInterfaceType_Object = MibTableColumn
rbSiSuInterfaceType = _RbSiSuInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 6, 1, 1, 3),
    _RbSiSuInterfaceType_Type()
)
rbSiSuInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSiSuInterfaceType.setStatus("current")
_RbSuLicenses_ObjectIdentity = ObjectIdentity
rbSuLicenses = _RbSuLicenses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 7)
)
_RbSuLicensesTable_Object = MibTable
rbSuLicensesTable = _RbSuLicensesTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 7, 1)
)
if mibBuilder.loadTexts:
    rbSuLicensesTable.setStatus("current")
_RbSuLicensesEntry_Object = MibTableRow
rbSuLicensesEntry = _RbSuLicensesEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 7, 1, 1)
)
rbSuLicensesEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
    (0, "RAINBOW-MIB", "rbSuLicenseIdx"),
)
if mibBuilder.loadTexts:
    rbSuLicensesEntry.setStatus("current")


class _RbSuLicenseIdx_Type(Integer32):
    """Custom type rbSuLicenseIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_RbSuLicenseIdx_Type.__name__ = "Integer32"
_RbSuLicenseIdx_Object = MibTableColumn
rbSuLicenseIdx = _RbSuLicenseIdx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 7, 1, 1, 1),
    _RbSuLicenseIdx_Type()
)
rbSuLicenseIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuLicenseIdx.setStatus("current")


class _RbSuLicenseId_Type(Integer32):
    """Custom type rbSuLicenseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bandwidth", 1)
    )


_RbSuLicenseId_Type.__name__ = "Integer32"
_RbSuLicenseId_Object = MibTableColumn
rbSuLicenseId = _RbSuLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 7, 1, 1, 2),
    _RbSuLicenseId_Type()
)
rbSuLicenseId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuLicenseId.setStatus("current")
_RbSuLicenseValue_Type = Unsigned32
_RbSuLicenseValue_Object = MibTableColumn
rbSuLicenseValue = _RbSuLicenseValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 5, 7, 1, 1, 3),
    _RbSuLicenseValue_Type()
)
rbSuLicenseValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuLicenseValue.setStatus("current")
_RbAuthorizationAndTraps_ObjectIdentity = ObjectIdentity
rbAuthorizationAndTraps = _RbAuthorizationAndTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6)
)
_RbAuthorizedManagersTable_Object = MibTable
rbAuthorizedManagersTable = _RbAuthorizedManagersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    rbAuthorizedManagersTable.setStatus("current")
_RbAuthorizedManagersEntry_Object = MibTableRow
rbAuthorizedManagersEntry = _RbAuthorizedManagersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 1, 1)
)
rbAuthorizedManagersEntry.setIndexNames(
    (0, "RAINBOW-MIB", "authMngrIpAddr"),
)
if mibBuilder.loadTexts:
    rbAuthorizedManagersEntry.setStatus("current")
_AuthMngrIpAddr_Type = IpAddress
_AuthMngrIpAddr_Object = MibTableColumn
authMngrIpAddr = _AuthMngrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 1, 1, 1),
    _AuthMngrIpAddr_Type()
)
authMngrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMngrIpAddr.setStatus("current")


class _AuthMngrReadCommunity_Type(DisplayString):
    """Custom type authMngrReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_AuthMngrReadCommunity_Type.__name__ = "DisplayString"
_AuthMngrReadCommunity_Object = MibTableColumn
authMngrReadCommunity = _AuthMngrReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 1, 1, 2),
    _AuthMngrReadCommunity_Type()
)
authMngrReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMngrReadCommunity.setStatus("current")


class _AuthMngrWriteCommunity_Type(DisplayString):
    """Custom type authMngrWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 23),
    )


_AuthMngrWriteCommunity_Type.__name__ = "DisplayString"
_AuthMngrWriteCommunity_Object = MibTableColumn
authMngrWriteCommunity = _AuthMngrWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 1, 1, 3),
    _AuthMngrWriteCommunity_Type()
)
authMngrWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMngrWriteCommunity.setStatus("current")


class _AuthMngrTrapEnable_Type(Integer32):
    """Custom type authMngrTrapEnable based on Integer32"""
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


_AuthMngrTrapEnable_Type.__name__ = "Integer32"
_AuthMngrTrapEnable_Object = MibTableColumn
authMngrTrapEnable = _AuthMngrTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 1, 1, 4),
    _AuthMngrTrapEnable_Type()
)
authMngrTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMngrTrapEnable.setStatus("current")
_AuthMngrRowStatus_Type = RowStatus
_AuthMngrRowStatus_Object = MibTableColumn
authMngrRowStatus = _AuthMngrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 1, 1, 5),
    _AuthMngrRowStatus_Type()
)
authMngrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    authMngrRowStatus.setStatus("current")
_RbTrapConfigTable_Object = MibTable
rbTrapConfigTable = _RbTrapConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 2)
)
if mibBuilder.loadTexts:
    rbTrapConfigTable.setStatus("current")
_RbTrapConfigEntry_Object = MibTableRow
rbTrapConfigEntry = _RbTrapConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 2, 1)
)
rbTrapConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "trapEnterprizeId"),
    (0, "RAINBOW-MIB", "trapId"),
)
if mibBuilder.loadTexts:
    rbTrapConfigEntry.setStatus("current")


class _TrapEnterprizeId_Type(Integer32):
    """Custom type trapEnterprizeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmp", 1),
          ("rainbow", 2),
          ("other", 3))
    )


_TrapEnterprizeId_Type.__name__ = "Integer32"
_TrapEnterprizeId_Object = MibTableColumn
trapEnterprizeId = _TrapEnterprizeId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 2, 1, 1),
    _TrapEnterprizeId_Type()
)
trapEnterprizeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEnterprizeId.setStatus("current")


class _TrapId_Type(Integer32):
    """Custom type trapId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_TrapId_Type.__name__ = "Integer32"
_TrapId_Object = MibTableColumn
trapId = _TrapId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 2, 1, 2),
    _TrapId_Type()
)
trapId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapId.setStatus("current")


class _TrapEnable_Type(Integer32):
    """Custom type trapEnable based on Integer32"""
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


_TrapEnable_Type.__name__ = "Integer32"
_TrapEnable_Object = MibTableColumn
trapEnable = _TrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 2, 1, 3),
    _TrapEnable_Type()
)
trapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnable.setStatus("current")
_TrapSeverity_Type = TrapSeverity
_TrapSeverity_Object = MibTableColumn
trapSeverity = _TrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 2, 1, 4),
    _TrapSeverity_Type()
)
trapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSeverity.setStatus("current")


class _TrapSuppressionInterval_Type(Integer32):
    """Custom type trapSuppressionInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_TrapSuppressionInterval_Type.__name__ = "Integer32"
_TrapSuppressionInterval_Object = MibTableColumn
trapSuppressionInterval = _TrapSuppressionInterval_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 2, 1, 5),
    _TrapSuppressionInterval_Type()
)
trapSuppressionInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapSuppressionInterval.setStatus("current")


class _RbTrapGetActive_Type(Integer32):
    """Custom type rbTrapGetActive based on Integer32"""
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


_RbTrapGetActive_Type.__name__ = "Integer32"
_RbTrapGetActive_Object = MibScalar
rbTrapGetActive = _RbTrapGetActive_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 3),
    _RbTrapGetActive_Type()
)
rbTrapGetActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbTrapGetActive.setStatus("current")
_RbTrapSeqNumber_Type = Unsigned32
_RbTrapSeqNumber_Object = MibScalar
rbTrapSeqNumber = _RbTrapSeqNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 4),
    _RbTrapSeqNumber_Type()
)
rbTrapSeqNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbTrapSeqNumber.setStatus("current")
_RbTrapSeverity_Type = TrapSeverity
_RbTrapSeverity_Object = MibScalar
rbTrapSeverity = _RbTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 5),
    _RbTrapSeverity_Type()
)
rbTrapSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapSeverity.setStatus("current")
_RbTrapSource_Type = DisplayString
_RbTrapSource_Object = MibScalar
rbTrapSource = _RbTrapSource_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 6),
    _RbTrapSource_Type()
)
rbTrapSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapSource.setStatus("current")


class _RbTrapAdditionalInfo_Type(Integer32):
    """Custom type rbTrapAdditionalInfo based on Integer32"""
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
              10,
              23,
              24,
              25,
              26,
              27,
              30,
              31,
              32,
              33,
              53,
              54,
              55,
              73,
              74,
              75,
              76,
              100,
              101,
              102,
              103,
              104,
              105,
              111,
              112,
              113,
              114,
              115,
              116,
              117,
              118,
              119,
              120,
              121,
              122,
              127,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              140,
              141,
              142,
              143,
              144,
              145,
              146,
              147,
              148,
              149,
              150,
              151,
              152,
              153,
              154,
              155,
              156,
              157,
              158,
              159,
              160,
              161,
              162,
              163,
              164,
              165,
              166,
              167,
              168,
              169,
              170,
              171,
              172,
              173,
              174,
              175,
              176,
              177,
              178,
              179,
              180,
              181,
              182,
              183,
              184,
              185,
              186,
              187,
              188,
              189,
              190,
              191,
              200,
              201,
              202,
              203,
              204,
              205,
              206,
              207,
              208,
              209,
              210,
              211,
              212,
              213,
              214,
              220,
              221,
              222,
              223,
              224,
              225,
              226,
              227,
              228)
        )
    )
    namedValues = NamedValues(
        *(("noInfo", 0),
          ("externalReset", 1),
          ("internalFaultReset", 2),
          ("mantaPllNotLockedOnInit", 3),
          ("mantaPllNotLockedOnSteadyState", 4),
          ("mantaSWDownloadError", 5),
          ("radioPLLNotLockedAfterPowerUP", 6),
          ("radioPLLNotLockedOnSteadyState", 7),
          ("bitTestFailed", 8),
          ("suEthernetPortLoop", 10),
          ("powerExPmaxTimeTooLong", 23),
          ("phyIDUburnFailed", 24),
          ("ifFailLock", 25),
          ("oduTableDnldError", 26),
          ("oduConnLost", 27),
          ("configElementAdded", 30),
          ("configElementDeleted", 31),
          ("configElementUpdated", 32),
          ("managementPortConfig", 33),
          ("powerSupplyFault", 53),
          ("powerInterfaceUnitsFault", 54),
          ("acuFault", 55),
          ("dryContactsFault", 73),
          ("npuTemperatureFault", 74),
          ("auIduTemperatureFault", 75),
          ("auOduTemperatureFault", 76),
          ("sdlBadVersion", 100),
          ("sdlVerNotAvailable", 101),
          ("sdlFailed", 102),
          ("noDiskSpace", 103),
          ("actionRunFromShadow", 104),
          ("actionMakeRunningVerOperational", 105),
          ("maxSubscribers", 111),
          ("maxServPipes", 112),
          ("maxServProfiles", 113),
          ("maxForwRules", 114),
          ("maxPolicyRules", 115),
          ("maxQoSProfiles", 116),
          ("maxNumOfCalls", 117),
          ("noBWforVOIP", 118),
          ("serviceAdminStatusChanged", 119),
          ("serviceSuMacChanged", 120),
          ("serviceVlanListChanged", 121),
          ("serviceProfileChanged", 122),
          ("mainBackbonePort", 127),
          ("managementPort", 128),
          ("connection2AU", 129),
          ("radioLinkAU", 130),
          ("radioLinkAU2SU", 131),
          ("authenticationProcessFailed", 132),
          ("registrationProcessFailed", 133),
          ("registrationProcessSucceed", 134),
          ("auDhcpProcessFailed", 135),
          ("auConfigurationDownloadFailed", 136),
          ("auSetParametersFailed", 137),
          ("auFirmwareDownloadFailed", 138),
          ("auInService", 139),
          ("lciConnection", 140),
          ("telnetConnection", 141),
          ("telnetAuthenticationFailure", 142),
          ("lciAuthenticationFailure", 143),
          ("diversityModeMismatch", 144),
          ("wrongBandwidth", 145),
          ("wrongFDDConfig", 146),
          ("wrongTDDConfig", 147),
          ("wrongMaxCellRadius", 148),
          ("wrongMinCellRadius", 149),
          ("downloadAborted", 150),
          ("incompatibleHWRevisionDetected", 151),
          ("incompatibleHWConfigurationDetected", 152),
          ("createFileFailed", 153),
          ("openFileFailed", 154),
          ("fstatFailed", 155),
          ("readFileFailed", 156),
          ("writeFileFailed", 157),
          ("writeInfoFailed", 158),
          ("flashAccessFailed", 159),
          ("shadowFileAccessFailed", 160),
          ("wrongSignature", 161),
          ("fileWithoutHeader", 162),
          ("headerTooLong", 163),
          ("mismatchInHeader", 164),
          ("invalidUnitType", 165),
          ("noRFVersionInHeader", 166),
          ("incompatibleRFRevision", 167),
          ("calcCRCFailed", 168),
          ("wrongCRC", 169),
          ("wrongFileSize", 170),
          ("tFTPStartFailed", 171),
          ("errorDuringTFTP", 172),
          ("readSocketError", 173),
          ("noReadBytes", 174),
          ("inProcess", 175),
          ("noFilename", 176),
          ("fileSizeTooBig", 177),
          ("wrongFileExt", 178),
          ("fileIsMain", 179),
          ("fileNotAvailable", 180),
          ("timeout", 181),
          ("tempGracePeriodStarted", 182),
          ("tempGracePeriodStopped", 183),
          ("gracePeriodStarted", 184),
          ("gracePeriodExpired", 185),
          ("gracePeriodExpiresIn3days", 186),
          ("macInLicenseFileConflict", 187),
          ("wrongFileSignature", 188),
          ("wrongFileSyntax", 189),
          ("wrongFileCPEsNumber", 190),
          ("fileExists", 191),
          ("serviceProfileDoesNotExist", 200),
          ("tooManyVlansPerService", 201),
          ("tooManyVlansPerSU", 202),
          ("wrongVlanID", 203),
          ("transparentVlanAndVplMismatch", 204),
          ("vlanMismatch", 205),
          ("sameServiceTypeOnVlan", 206),
          ("oneVlanPermittedForVlanClassMode", 207),
          ("accessVlanMismatch", 208),
          ("accessVlanDuplicate", 209),
          ("oneAccessVlanPerSU", 210),
          ("userAuthTimeOut", 211),
          ("userAccStartTimeOut", 212),
          ("userAccStopTimeOut", 213),
          ("tableIsFull", 214),
          ("fileDownloadStarted", 220),
          ("fileDownloadCompleted", 221),
          ("fileMD5Failure", 222),
          ("fileParsingFailure", 223),
          ("fileDownloadFailure", 224),
          ("overCurrent", 225),
          ("synthesizerUnlock", 226),
          ("highReflectedPower", 227),
          ("overTemperature", 228))
    )


_RbTrapAdditionalInfo_Type.__name__ = "Integer32"
_RbTrapAdditionalInfo_Object = MibScalar
rbTrapAdditionalInfo = _RbTrapAdditionalInfo_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 7),
    _RbTrapAdditionalInfo_Type()
)
rbTrapAdditionalInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapAdditionalInfo.setStatus("current")


class _RbTrapCategory_Type(Integer32):
    """Custom type rbTrapCategory based on Integer32"""
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
          ("communications", 1),
          ("qualityOfService", 2),
          ("processingError", 3),
          ("equipment", 4),
          ("environmental", 5))
    )


_RbTrapCategory_Type.__name__ = "Integer32"
_RbTrapCategory_Object = MibScalar
rbTrapCategory = _RbTrapCategory_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 8),
    _RbTrapCategory_Type()
)
rbTrapCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapCategory.setStatus("current")
_RbTrapMinSeverity_Type = TrapSeverity
_RbTrapMinSeverity_Object = MibScalar
rbTrapMinSeverity = _RbTrapMinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 9),
    _RbTrapMinSeverity_Type()
)
rbTrapMinSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapMinSeverity.setStatus("current")
_RbTrapLedStatus_Type = OctetString
_RbTrapLedStatus_Object = MibScalar
rbTrapLedStatus = _RbTrapLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 10),
    _RbTrapLedStatus_Type()
)
rbTrapLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapLedStatus.setStatus("current")
_RbTrapIpAddress_Type = IpAddress
_RbTrapIpAddress_Object = MibScalar
rbTrapIpAddress = _RbTrapIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 11),
    _RbTrapIpAddress_Type()
)
rbTrapIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapIpAddress.setStatus("current")


class _RbTrapSetFailureReason_Type(Integer32):
    """Custom type rbTrapSetFailureReason based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("generalError", 1),
          ("updateCRCFailed", 2),
          ("wrongDefaultsValue", 3),
          ("setDefaultsFailed", 4),
          ("logPreffixTooLong", 5),
          ("setLogPreffixFailed", 6),
          ("invalidCellRadius", 7),
          ("setCellRadiusFailed", 8),
          ("setBsIDFailed", 9),
          ("setBsMaskFailed", 10),
          ("setArqModeFailed", 11),
          ("setBandTypeFailed", 12),
          ("txFrequencyOutOfLimitedRange", 13),
          ("invalidTxFrequency", 14),
          ("txFrequencyOutOfRange", 15),
          ("setTxFrequencyFailed", 16),
          ("invalidTxPower", 17),
          ("setTxPowerFailed", 18),
          ("invalidUplinkBasicRate", 19),
          ("setUplinkBasicRateFailed", 20),
          ("invalidDownlinkBasicRate", 21),
          ("setDownlinkBasicRateFailed", 22),
          ("setSuRateWhileMrtEnabled", 23),
          ("invalidDownLinkRate", 24),
          ("invalidUplinkRate", 25),
          ("invalidOptimalRSSI", 26),
          ("setOptimalRSSIFailed", 27),
          ("berTestDataSizeUnderMin", 28),
          ("berTestDataSizeOverMax", 29),
          ("berTestIsAlreadyRunning", 30),
          ("invalidBerTestRate", 31),
          ("invalidBerTestSLA", 32),
          ("setBerTestSlaFailed", 33),
          ("invalidBerTestMaxPacketSize", 34),
          ("setBerTestMaxPacketSizeFailed", 35),
          ("berTestCreateConnectionFailed", 36),
          ("telnetDisconnectFailed", 37),
          ("invalidEthernetMode", 38),
          ("setEthernetModeFailed", 39),
          ("installerPasswordTooLong", 40),
          ("setInstallerPasswordFailed", 41),
          ("invalidBand", 42),
          ("invalidAgingTime", 43),
          ("invalidLimitDevicesNum", 44),
          ("invalidLimitMaxDevicesEnable", 45),
          ("maxCellRadiusConflict", 46))
    )


_RbTrapSetFailureReason_Type.__name__ = "Integer32"
_RbTrapSetFailureReason_Object = MibScalar
rbTrapSetFailureReason = _RbTrapSetFailureReason_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 12),
    _RbTrapSetFailureReason_Type()
)
rbTrapSetFailureReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbTrapSetFailureReason.setStatus("current")


class _RbTrapRestoreDefaults_Type(Integer32):
    """Custom type rbTrapRestoreDefaults based on Integer32"""
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
        *(("noAction", 0),
          ("restoreTrapEnable", 1),
          ("restoreTrapSeverity", 2),
          ("restoreTrapSuppressionInterval", 3))
    )


_RbTrapRestoreDefaults_Type.__name__ = "Integer32"
_RbTrapRestoreDefaults_Object = MibScalar
rbTrapRestoreDefaults = _RbTrapRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 13),
    _RbTrapRestoreDefaults_Type()
)
rbTrapRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbTrapRestoreDefaults.setStatus("current")
_RbTrapThresholdsTable_Object = MibTable
rbTrapThresholdsTable = _RbTrapThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 20)
)
if mibBuilder.loadTexts:
    rbTrapThresholdsTable.setStatus("current")
_RbTrapThresholdsEntry_Object = MibTableRow
rbTrapThresholdsEntry = _RbTrapThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 20, 1)
)
rbTrapThresholdsEntry.setIndexNames(
    (0, "RAINBOW-MIB", "counterId"),
)
if mibBuilder.loadTexts:
    rbTrapThresholdsEntry.setStatus("current")


class _CounterId_Type(Integer32):
    """Custom type counterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CounterId_Type.__name__ = "Integer32"
_CounterId_Object = MibTableColumn
counterId = _CounterId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 20, 1, 1),
    _CounterId_Type()
)
counterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterId.setStatus("current")
_CounterName_Type = DisplayString
_CounterName_Object = MibTableColumn
counterName = _CounterName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 20, 1, 2),
    _CounterName_Type()
)
counterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterName.setStatus("current")


class _CounterType_Type(Integer32):
    """Custom type counterType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("integer", 1),
          ("string", 2))
    )


_CounterType_Type.__name__ = "Integer32"
_CounterType_Object = MibTableColumn
counterType = _CounterType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 20, 1, 3),
    _CounterType_Type()
)
counterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterType.setStatus("current")
_CounterIntValue_Type = Integer32
_CounterIntValue_Object = MibTableColumn
counterIntValue = _CounterIntValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 20, 1, 4),
    _CounterIntValue_Type()
)
counterIntValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterIntValue.setStatus("current")
_CounterStringValue_Type = DisplayString
_CounterStringValue_Object = MibTableColumn
counterStringValue = _CounterStringValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 20, 1, 5),
    _CounterStringValue_Type()
)
counterStringValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    counterStringValue.setStatus("current")
_RbTrapEventLogTable_Object = MibTable
rbTrapEventLogTable = _RbTrapEventLogTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21)
)
if mibBuilder.loadTexts:
    rbTrapEventLogTable.setStatus("current")
_RbTrapEventLogEntry_Object = MibTableRow
rbTrapEventLogEntry = _RbTrapEventLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1)
)
rbTrapEventLogEntry.setIndexNames(
    (0, "RAINBOW-MIB", "trapEventLogSeqNum"),
)
if mibBuilder.loadTexts:
    rbTrapEventLogEntry.setStatus("current")
_TrapEventLogSeqNum_Type = Unsigned32
_TrapEventLogSeqNum_Object = MibTableColumn
trapEventLogSeqNum = _TrapEventLogSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 1),
    _TrapEventLogSeqNum_Type()
)
trapEventLogSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogSeqNum.setStatus("current")
_TrapEventLogId_Type = Integer32
_TrapEventLogId_Object = MibTableColumn
trapEventLogId = _TrapEventLogId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 2),
    _TrapEventLogId_Type()
)
trapEventLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogId.setStatus("current")
_TrapEventLogSeverity_Type = TrapSeverity
_TrapEventLogSeverity_Object = MibTableColumn
trapEventLogSeverity = _TrapEventLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 3),
    _TrapEventLogSeverity_Type()
)
trapEventLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogSeverity.setStatus("current")


class _TrapEventLogType_Type(Integer32):
    """Custom type trapEventLogType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("coldStart", 0),
          ("warmStart", 1),
          ("linkDown", 2),
          ("linkUp", 3),
          ("authenticationFailure", 4),
          ("egpNeighborLoss", 5),
          ("enterpriseSpecific", 6))
    )


_TrapEventLogType_Type.__name__ = "Integer32"
_TrapEventLogType_Object = MibTableColumn
trapEventLogType = _TrapEventLogType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 4),
    _TrapEventLogType_Type()
)
trapEventLogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogType.setStatus("current")


class _TrapEventLogCategory_Type(Integer32):
    """Custom type trapEventLogCategory based on Integer32"""
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
          ("communications", 1),
          ("qualityOfService", 2),
          ("processingError", 3),
          ("equipment", 4),
          ("environmental", 5))
    )


_TrapEventLogCategory_Type.__name__ = "Integer32"
_TrapEventLogCategory_Object = MibTableColumn
trapEventLogCategory = _TrapEventLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 5),
    _TrapEventLogCategory_Type()
)
trapEventLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogCategory.setStatus("current")
_TrapEventLogSource_Type = DisplayString
_TrapEventLogSource_Object = MibTableColumn
trapEventLogSource = _TrapEventLogSource_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 6),
    _TrapEventLogSource_Type()
)
trapEventLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogSource.setStatus("current")
_TrapEventLogVarBindNumber_Type = Integer32
_TrapEventLogVarBindNumber_Object = MibTableColumn
trapEventLogVarBindNumber = _TrapEventLogVarBindNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 7),
    _TrapEventLogVarBindNumber_Type()
)
trapEventLogVarBindNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogVarBindNumber.setStatus("current")
_TrapEventLogVarBindSize_Type = Integer32
_TrapEventLogVarBindSize_Object = MibTableColumn
trapEventLogVarBindSize = _TrapEventLogVarBindSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 8),
    _TrapEventLogVarBindSize_Type()
)
trapEventLogVarBindSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogVarBindSize.setStatus("current")
_TrapEventLogAddVarAttributes_Type = DisplayString
_TrapEventLogAddVarAttributes_Object = MibTableColumn
trapEventLogAddVarAttributes = _TrapEventLogAddVarAttributes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 9),
    _TrapEventLogAddVarAttributes_Type()
)
trapEventLogAddVarAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogAddVarAttributes.setStatus("current")
_TrapEventLogDateAndTime_Type = DisplayString
_TrapEventLogDateAndTime_Object = MibTableColumn
trapEventLogDateAndTime = _TrapEventLogDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 21, 1, 10),
    _TrapEventLogDateAndTime_Type()
)
trapEventLogDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventLogDateAndTime.setStatus("current")
_RbTrapAlarmLogTable_Object = MibTable
rbTrapAlarmLogTable = _RbTrapAlarmLogTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22)
)
if mibBuilder.loadTexts:
    rbTrapAlarmLogTable.setStatus("current")
_RbTrapAlarmLogEntry_Object = MibTableRow
rbTrapAlarmLogEntry = _RbTrapAlarmLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1)
)
rbTrapAlarmLogEntry.setIndexNames(
    (0, "RAINBOW-MIB", "trapAlarmLogAlarmId"),
    (0, "RAINBOW-MIB", "trapAlarmLogSource"),
    (0, "RAINBOW-MIB", "trapAlarmLogSlotId"),
)
if mibBuilder.loadTexts:
    rbTrapAlarmLogEntry.setStatus("current")


class _TrapAlarmLogAlarmId_Type(Integer32):
    """Custom type trapAlarmLogAlarmId based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("npuEthConn", 1),
          ("npuMngConn", 2),
          ("npuAuConn", 3),
          ("auRlinkLoss", 4),
          ("npuLciUnauthAcc", 5),
          ("npuTelnetUnauthAcc", 6),
          ("bitFailed", 7),
          ("npuLciAccess", 8),
          ("npuTelnetAccess", 9),
          ("npuReset", 10),
          ("swDnl", 11),
          ("swDnlFail", 12),
          ("swDnlSwitch", 13),
          ("bstCard", 14),
          ("bstPerFault", 15),
          ("bstEnvFault", 16),
          ("service", 17),
          ("bstExt1PPSFault", 18),
          ("bstInt1PPSFault", 19),
          ("bstExt16MHzFault", 20),
          ("bstInt16MHzFault", 21),
          ("bstGpsComFault", 22),
          ("bstGpsHealthFault", 23),
          ("bstGpsNumSatsFault", 24),
          ("authSrvKeepAliveFault", 25),
          ("acctSrvKeepAliveFault", 26),
          ("auModeConflict", 27),
          ("auOduComError", 28),
          ("auOduBandMismatch", 29),
          ("auExt1PPSFault", 30),
          ("auHoldOverEntered", 31),
          ("auHoldOverTOPassed", 32))
    )


_TrapAlarmLogAlarmId_Type.__name__ = "Integer32"
_TrapAlarmLogAlarmId_Object = MibTableColumn
trapAlarmLogAlarmId = _TrapAlarmLogAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 1),
    _TrapAlarmLogAlarmId_Type()
)
trapAlarmLogAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogAlarmId.setStatus("current")


class _TrapAlarmLogSource_Type(Integer32):
    """Custom type trapAlarmLogSource based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("npu", 1),
          ("au", 2),
          ("su", 3),
          ("bs", 4),
          ("psu", 5),
          ("piu", 6),
          ("acu", 7),
          ("service", 8))
    )


_TrapAlarmLogSource_Type.__name__ = "Integer32"
_TrapAlarmLogSource_Object = MibTableColumn
trapAlarmLogSource = _TrapAlarmLogSource_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 2),
    _TrapAlarmLogSource_Type()
)
trapAlarmLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogSource.setStatus("current")


class _TrapAlarmLogSlotId_Type(Integer32):
    """Custom type trapAlarmLogSlotId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_TrapAlarmLogSlotId_Type.__name__ = "Integer32"
_TrapAlarmLogSlotId_Object = MibTableColumn
trapAlarmLogSlotId = _TrapAlarmLogSlotId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 3),
    _TrapAlarmLogSlotId_Type()
)
trapAlarmLogSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogSlotId.setStatus("current")
_TrapAlarmLogEventId_Type = Integer32
_TrapAlarmLogEventId_Object = MibTableColumn
trapAlarmLogEventId = _TrapAlarmLogEventId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 4),
    _TrapAlarmLogEventId_Type()
)
trapAlarmLogEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogEventId.setStatus("current")
_TrapAlarmLogName_Type = DisplayString
_TrapAlarmLogName_Object = MibTableColumn
trapAlarmLogName = _TrapAlarmLogName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 5),
    _TrapAlarmLogName_Type()
)
trapAlarmLogName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogName.setStatus("current")
_TrapAlarmLogSeverity_Type = TrapSeverity
_TrapAlarmLogSeverity_Object = MibTableColumn
trapAlarmLogSeverity = _TrapAlarmLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 6),
    _TrapAlarmLogSeverity_Type()
)
trapAlarmLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogSeverity.setStatus("current")


class _TrapAlarmLogCategory_Type(Integer32):
    """Custom type trapAlarmLogCategory based on Integer32"""
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
          ("communications", 1),
          ("qualityOfService", 2),
          ("processingError", 3),
          ("equipment", 4),
          ("environmental", 5))
    )


_TrapAlarmLogCategory_Type.__name__ = "Integer32"
_TrapAlarmLogCategory_Object = MibTableColumn
trapAlarmLogCategory = _TrapAlarmLogCategory_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 7),
    _TrapAlarmLogCategory_Type()
)
trapAlarmLogCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogCategory.setStatus("current")
_TrapAlarmLogStrOn_Type = DisplayString
_TrapAlarmLogStrOn_Object = MibTableColumn
trapAlarmLogStrOn = _TrapAlarmLogStrOn_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 8),
    _TrapAlarmLogStrOn_Type()
)
trapAlarmLogStrOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogStrOn.setStatus("current")
_TrapAlarmLogVarBindNumber_Type = Integer32
_TrapAlarmLogVarBindNumber_Object = MibTableColumn
trapAlarmLogVarBindNumber = _TrapAlarmLogVarBindNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 9),
    _TrapAlarmLogVarBindNumber_Type()
)
trapAlarmLogVarBindNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogVarBindNumber.setStatus("current")
_TrapAlarmLogVarBindSize_Type = Integer32
_TrapAlarmLogVarBindSize_Object = MibTableColumn
trapAlarmLogVarBindSize = _TrapAlarmLogVarBindSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 10),
    _TrapAlarmLogVarBindSize_Type()
)
trapAlarmLogVarBindSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogVarBindSize.setStatus("current")
_TrapAlarmLogAddVarAttributes_Type = DisplayString
_TrapAlarmLogAddVarAttributes_Object = MibTableColumn
trapAlarmLogAddVarAttributes = _TrapAlarmLogAddVarAttributes_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 11),
    _TrapAlarmLogAddVarAttributes_Type()
)
trapAlarmLogAddVarAttributes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogAddVarAttributes.setStatus("current")


class _TrapAlarmLogLed_Type(Integer32):
    """Custom type trapAlarmLogLed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("led", 1),
          ("ledBst", 2))
    )


_TrapAlarmLogLed_Type.__name__ = "Integer32"
_TrapAlarmLogLed_Object = MibTableColumn
trapAlarmLogLed = _TrapAlarmLogLed_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 6, 22, 1, 12),
    _TrapAlarmLogLed_Type()
)
trapAlarmLogLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapAlarmLogLed.setStatus("current")
_RbInterfaces_ObjectIdentity = ObjectIdentity
rbInterfaces = _RbInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7)
)
_RbEthernetInterface_ObjectIdentity = ObjectIdentity
rbEthernetInterface = _RbEthernetInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1)
)
_RbEthIfConfigTable_Object = MibTable
rbEthIfConfigTable = _RbEthIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rbEthIfConfigTable.setStatus("current")
_RbEthIfConfigEntry_Object = MibTableRow
rbEthIfConfigEntry = _RbEthIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1, 1, 1)
)
rbEthIfConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "ethConfigIfIndex"),
)
if mibBuilder.loadTexts:
    rbEthIfConfigEntry.setStatus("current")


class _EthConfigIfIndex_Type(Integer32):
    """Custom type ethConfigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_EthConfigIfIndex_Type.__name__ = "Integer32"
_EthConfigIfIndex_Object = MibTableColumn
ethConfigIfIndex = _EthConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1, 1, 1, 1),
    _EthConfigIfIndex_Type()
)
ethConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethConfigIfIndex.setStatus("current")


class _EthConfigAutoNegotiation_Type(Integer32):
    """Custom type ethConfigAutoNegotiation based on Integer32"""
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


_EthConfigAutoNegotiation_Type.__name__ = "Integer32"
_EthConfigAutoNegotiation_Object = MibTableColumn
ethConfigAutoNegotiation = _EthConfigAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1, 1, 1, 2),
    _EthConfigAutoNegotiation_Type()
)
ethConfigAutoNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethConfigAutoNegotiation.setStatus("current")
_EthConfigLinkSpeedAndDuplex_Type = LinkSpeedAndDuplex
_EthConfigLinkSpeedAndDuplex_Object = MibTableColumn
ethConfigLinkSpeedAndDuplex = _EthConfigLinkSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1, 1, 1, 3),
    _EthConfigLinkSpeedAndDuplex_Type()
)
ethConfigLinkSpeedAndDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethConfigLinkSpeedAndDuplex.setStatus("current")


class _EthConfigCurrentdAutoNegotiation_Type(Integer32):
    """Custom type ethConfigCurrentdAutoNegotiation based on Integer32"""
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


_EthConfigCurrentdAutoNegotiation_Type.__name__ = "Integer32"
_EthConfigCurrentdAutoNegotiation_Object = MibTableColumn
ethConfigCurrentdAutoNegotiation = _EthConfigCurrentdAutoNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1, 1, 1, 4),
    _EthConfigCurrentdAutoNegotiation_Type()
)
ethConfigCurrentdAutoNegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethConfigCurrentdAutoNegotiation.setStatus("current")
_EthConfigCurrentLinkSpeedAndDuplex_Type = LinkSpeedAndDuplex
_EthConfigCurrentLinkSpeedAndDuplex_Object = MibTableColumn
ethConfigCurrentLinkSpeedAndDuplex = _EthConfigCurrentLinkSpeedAndDuplex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 1, 1, 1, 5),
    _EthConfigCurrentLinkSpeedAndDuplex_Type()
)
ethConfigCurrentLinkSpeedAndDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethConfigCurrentLinkSpeedAndDuplex.setStatus("current")
_RbAirInterface_ObjectIdentity = ObjectIdentity
rbAirInterface = _RbAirInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2)
)
_RbAuMacParameters_ObjectIdentity = ObjectIdentity
rbAuMacParameters = _RbAuMacParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1)
)


class _RbAuBaseStationId_Type(OctetString):
    """Custom type rbAuBaseStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbAuBaseStationId_Type.__name__ = "OctetString"
_RbAuBaseStationId_Object = MibScalar
rbAuBaseStationId = _RbAuBaseStationId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1, 1),
    _RbAuBaseStationId_Type()
)
rbAuBaseStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuBaseStationId.setStatus("current")


class _RbAuMaxCellRadius_Type(Integer32):
    """Custom type rbAuMaxCellRadius based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 110),
    )


_RbAuMaxCellRadius_Type.__name__ = "Integer32"
_RbAuMaxCellRadius_Object = MibScalar
rbAuMaxCellRadius = _RbAuMaxCellRadius_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1, 2),
    _RbAuMaxCellRadius_Type()
)
rbAuMaxCellRadius.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuMaxCellRadius.setStatus("current")


class _RbAuConfiguredBaseStationId_Type(OctetString):
    """Custom type rbAuConfiguredBaseStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbAuConfiguredBaseStationId_Type.__name__ = "OctetString"
_RbAuConfiguredBaseStationId_Object = MibScalar
rbAuConfiguredBaseStationId = _RbAuConfiguredBaseStationId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1, 3),
    _RbAuConfiguredBaseStationId_Type()
)
rbAuConfiguredBaseStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuConfiguredBaseStationId.setStatus("current")


class _RbAuARQState_Type(Integer32):
    """Custom type rbAuARQState based on Integer32"""
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


_RbAuARQState_Type.__name__ = "Integer32"
_RbAuARQState_Object = MibScalar
rbAuARQState = _RbAuARQState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1, 4),
    _RbAuARQState_Type()
)
rbAuARQState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuARQState.setStatus("current")


class _RbAuConfiguredARQState_Type(Integer32):
    """Custom type rbAuConfiguredARQState based on Integer32"""
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


_RbAuConfiguredARQState_Type.__name__ = "Integer32"
_RbAuConfiguredARQState_Object = MibScalar
rbAuConfiguredARQState = _RbAuConfiguredARQState_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1, 5),
    _RbAuConfiguredARQState_Type()
)
rbAuConfiguredARQState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuConfiguredARQState.setStatus("current")


class _RbAuConfiguredSectorId_Type(OctetString):
    """Custom type rbAuConfiguredSectorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RbAuConfiguredSectorId_Type.__name__ = "OctetString"
_RbAuConfiguredSectorId_Object = MibScalar
rbAuConfiguredSectorId = _RbAuConfiguredSectorId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1, 6),
    _RbAuConfiguredSectorId_Type()
)
rbAuConfiguredSectorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuConfiguredSectorId.setStatus("current")


class _RbAuCurrentMaxCellRadius_Type(Integer32):
    """Custom type rbAuCurrentMaxCellRadius based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 110),
    )


_RbAuCurrentMaxCellRadius_Type.__name__ = "Integer32"
_RbAuCurrentMaxCellRadius_Object = MibScalar
rbAuCurrentMaxCellRadius = _RbAuCurrentMaxCellRadius_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 1, 7),
    _RbAuCurrentMaxCellRadius_Type()
)
rbAuCurrentMaxCellRadius.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuCurrentMaxCellRadius.setStatus("current")
_RbSuMacParameters_ObjectIdentity = ObjectIdentity
rbSuMacParameters = _RbSuMacParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 2)
)


class _RbSuBaseStationId_Type(OctetString):
    """Custom type rbSuBaseStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuBaseStationId_Type.__name__ = "OctetString"
_RbSuBaseStationId_Object = MibScalar
rbSuBaseStationId = _RbSuBaseStationId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 2, 1),
    _RbSuBaseStationId_Type()
)
rbSuBaseStationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuBaseStationId.setStatus("current")


class _RbSuBaseStationIdMask_Type(OctetString):
    """Custom type rbSuBaseStationIdMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuBaseStationIdMask_Type.__name__ = "OctetString"
_RbSuBaseStationIdMask_Object = MibScalar
rbSuBaseStationIdMask = _RbSuBaseStationIdMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 2, 2),
    _RbSuBaseStationIdMask_Type()
)
rbSuBaseStationIdMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuBaseStationIdMask.setStatus("current")


class _RbSuConfiguredBaseStationId_Type(OctetString):
    """Custom type rbSuConfiguredBaseStationId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuConfiguredBaseStationId_Type.__name__ = "OctetString"
_RbSuConfiguredBaseStationId_Object = MibScalar
rbSuConfiguredBaseStationId = _RbSuConfiguredBaseStationId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 2, 3),
    _RbSuConfiguredBaseStationId_Type()
)
rbSuConfiguredBaseStationId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredBaseStationId.setStatus("current")


class _RbSuConfiguredBaseStationIdMask_Type(OctetString):
    """Custom type rbSuConfiguredBaseStationIdMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuConfiguredBaseStationIdMask_Type.__name__ = "OctetString"
_RbSuConfiguredBaseStationIdMask_Object = MibScalar
rbSuConfiguredBaseStationIdMask = _RbSuConfiguredBaseStationIdMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 2, 4),
    _RbSuConfiguredBaseStationIdMask_Type()
)
rbSuConfiguredBaseStationIdMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredBaseStationIdMask.setStatus("current")
_RbAuMultirateParameters_ObjectIdentity = ObjectIdentity
rbAuMultirateParameters = _RbAuMultirateParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 3)
)


class _RbAuMultirateSupport_Type(Integer32):
    """Custom type rbAuMultirateSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notDefined", 3))
    )


_RbAuMultirateSupport_Type.__name__ = "Integer32"
_RbAuMultirateSupport_Object = MibScalar
rbAuMultirateSupport = _RbAuMultirateSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 3, 1),
    _RbAuMultirateSupport_Type()
)
rbAuMultirateSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuMultirateSupport.setStatus("current")


class _RbAuUlBasicRate_Type(Modulation):
    """Custom type rbAuUlBasicRate based on Modulation"""
    defaultValue = 1


_RbAuUlBasicRate_Type.__name__ = "Modulation"
_RbAuUlBasicRate_Object = MibScalar
rbAuUlBasicRate = _RbAuUlBasicRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 3, 2),
    _RbAuUlBasicRate_Type()
)
rbAuUlBasicRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuUlBasicRate.setStatus("current")


class _RbAuDlBasicRate_Type(Modulation):
    """Custom type rbAuDlBasicRate based on Modulation"""
    defaultValue = 1


_RbAuDlBasicRate_Type.__name__ = "Modulation"
_RbAuDlBasicRate_Object = MibScalar
rbAuDlBasicRate = _RbAuDlBasicRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 3, 3),
    _RbAuDlBasicRate_Type()
)
rbAuDlBasicRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuDlBasicRate.setStatus("current")


class _RbAuUlMinNoOfSubChannels_Type(Integer32):
    """Custom type rbAuUlMinNoOfSubChannels based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_RbAuUlMinNoOfSubChannels_Type.__name__ = "Integer32"
_RbAuUlMinNoOfSubChannels_Object = MibScalar
rbAuUlMinNoOfSubChannels = _RbAuUlMinNoOfSubChannels_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 3, 4),
    _RbAuUlMinNoOfSubChannels_Type()
)
rbAuUlMinNoOfSubChannels.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuUlMinNoOfSubChannels.setStatus("current")
_RbAuATPCParameters_ObjectIdentity = ObjectIdentity
rbAuATPCParameters = _RbAuATPCParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 4)
)


class _RbAuATPCSupport_Type(Integer32):
    """Custom type rbAuATPCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notDefined", 3))
    )


_RbAuATPCSupport_Type.__name__ = "Integer32"
_RbAuATPCSupport_Object = MibScalar
rbAuATPCSupport = _RbAuATPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 4, 1),
    _RbAuATPCSupport_Type()
)
rbAuATPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuATPCSupport.setStatus("current")


class _RbAuOptimalRSSI_Type(Integer32):
    """Custom type rbAuOptimalRSSI based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RbAuOptimalRSSI_Type.__name__ = "Integer32"
_RbAuOptimalRSSI_Object = MibScalar
rbAuOptimalRSSI = _RbAuOptimalRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 4, 2),
    _RbAuOptimalRSSI_Type()
)
rbAuOptimalRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuOptimalRSSI.setStatus("current")
_RbSuMultirateParameters_ObjectIdentity = ObjectIdentity
rbSuMultirateParameters = _RbSuMultirateParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5)
)
_RbSuTxPower_Type = DisplayString
_RbSuTxPower_Object = MibScalar
rbSuTxPower = _RbSuTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 1),
    _RbSuTxPower_Type()
)
rbSuTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuTxPower.setStatus("current")
_RbSuUlSNR_Type = DisplayString
_RbSuUlSNR_Object = MibScalar
rbSuUlSNR = _RbSuUlSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 3),
    _RbSuUlSNR_Type()
)
rbSuUlSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuUlSNR.setStatus("current")
_RbSuUlRSSI_Type = DisplayString
_RbSuUlRSSI_Object = MibScalar
rbSuUlRSSI = _RbSuUlRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 4),
    _RbSuUlRSSI_Type()
)
rbSuUlRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuUlRSSI.setStatus("current")
_RbSuUlCurrentRate_Type = Modulation
_RbSuUlCurrentRate_Object = MibScalar
rbSuUlCurrentRate = _RbSuUlCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 5),
    _RbSuUlCurrentRate_Type()
)
rbSuUlCurrentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuUlCurrentRate.setStatus("current")
_RbSuDlSNR_Type = DisplayString
_RbSuDlSNR_Object = MibScalar
rbSuDlSNR = _RbSuDlSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 6),
    _RbSuDlSNR_Type()
)
rbSuDlSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDlSNR.setStatus("current")
_RbSuDlRSSI_Type = DisplayString
_RbSuDlRSSI_Object = MibScalar
rbSuDlRSSI = _RbSuDlRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 7),
    _RbSuDlRSSI_Type()
)
rbSuDlRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDlRSSI.setStatus("current")
_RbSuDlCurrentRate_Type = Modulation
_RbSuDlCurrentRate_Object = MibScalar
rbSuDlCurrentRate = _RbSuDlCurrentRate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 8),
    _RbSuDlCurrentRate_Type()
)
rbSuDlCurrentRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuDlCurrentRate.setStatus("current")


class _RbSuMultirateSupport_Type(Integer32):
    """Custom type rbSuMultirateSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notDefined", 3))
    )


_RbSuMultirateSupport_Type.__name__ = "Integer32"
_RbSuMultirateSupport_Object = MibScalar
rbSuMultirateSupport = _RbSuMultirateSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 9),
    _RbSuMultirateSupport_Type()
)
rbSuMultirateSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuMultirateSupport.setStatus("current")
_RbSuEstDistance_Type = Unsigned32
_RbSuEstDistance_Object = MibScalar
rbSuEstDistance = _RbSuEstDistance_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 10),
    _RbSuEstDistance_Type()
)
rbSuEstDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuEstDistance.setStatus("current")
_RbSuUlSNRValue_Type = TenthdB
_RbSuUlSNRValue_Object = MibScalar
rbSuUlSNRValue = _RbSuUlSNRValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 11),
    _RbSuUlSNRValue_Type()
)
rbSuUlSNRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuUlSNRValue.setStatus("current")
_RbSuUlRSSIValue_Type = TenthdB
_RbSuUlRSSIValue_Object = MibScalar
rbSuUlRSSIValue = _RbSuUlRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 12),
    _RbSuUlRSSIValue_Type()
)
rbSuUlRSSIValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuUlRSSIValue.setStatus("current")
_RbSuDlSNRValue_Type = TenthdB
_RbSuDlSNRValue_Object = MibScalar
rbSuDlSNRValue = _RbSuDlSNRValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 13),
    _RbSuDlSNRValue_Type()
)
rbSuDlSNRValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDlSNRValue.setStatus("current")
_RbSuDlRSSIValue_Type = TenthdB
_RbSuDlRSSIValue_Object = MibScalar
rbSuDlRSSIValue = _RbSuDlRSSIValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 5, 14),
    _RbSuDlRSSIValue_Type()
)
rbSuDlRSSIValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDlRSSIValue.setStatus("current")
_RbSuATPCParameters_ObjectIdentity = ObjectIdentity
rbSuATPCParameters = _RbSuATPCParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 6)
)


class _RbSuATPCSupport_Type(Integer32):
    """Custom type rbSuATPCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notDefined", 3))
    )


_RbSuATPCSupport_Type.__name__ = "Integer32"
_RbSuATPCSupport_Object = MibScalar
rbSuATPCSupport = _RbSuATPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 6, 1),
    _RbSuATPCSupport_Type()
)
rbSuATPCSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuATPCSupport.setStatus("current")
_RbAuPhyParameters_ObjectIdentity = ObjectIdentity
rbAuPhyParameters = _RbAuPhyParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 7)
)


class _RbAuCurrentPhyBandwidth_Type(Integer32):
    """Custom type rbAuCurrentPhyBandwidth based on Integer32"""
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
        *(("b175", 1),
          ("b35", 2),
          ("b50", 3),
          ("b70", 4),
          ("b100", 5))
    )


_RbAuCurrentPhyBandwidth_Type.__name__ = "Integer32"
_RbAuCurrentPhyBandwidth_Object = MibScalar
rbAuCurrentPhyBandwidth = _RbAuCurrentPhyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 7, 1),
    _RbAuCurrentPhyBandwidth_Type()
)
rbAuCurrentPhyBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuCurrentPhyBandwidth.setStatus("current")
_RbAuPhyTxFrequencyChannel_Type = DisplayString
_RbAuPhyTxFrequencyChannel_Object = MibScalar
rbAuPhyTxFrequencyChannel = _RbAuPhyTxFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 7, 2),
    _RbAuPhyTxFrequencyChannel_Type()
)
rbAuPhyTxFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbAuPhyTxFrequencyChannel.setStatus("current")
_RbAuPhyTxConfiguredFrequencyChannel_Type = DisplayString
_RbAuPhyTxConfiguredFrequencyChannel_Object = MibScalar
rbAuPhyTxConfiguredFrequencyChannel = _RbAuPhyTxConfiguredFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 7, 3),
    _RbAuPhyTxConfiguredFrequencyChannel_Type()
)
rbAuPhyTxConfiguredFrequencyChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuPhyTxConfiguredFrequencyChannel.setStatus("current")


class _RbAuConfiguredPhyBandwidth_Type(Integer32):
    """Custom type rbAuConfiguredPhyBandwidth based on Integer32"""
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
        *(("b175", 1),
          ("b35", 2),
          ("b50", 3),
          ("b70", 4),
          ("b100", 5))
    )


_RbAuConfiguredPhyBandwidth_Type.__name__ = "Integer32"
_RbAuConfiguredPhyBandwidth_Object = MibScalar
rbAuConfiguredPhyBandwidth = _RbAuConfiguredPhyBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 7, 4),
    _RbAuConfiguredPhyBandwidth_Type()
)
rbAuConfiguredPhyBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbAuConfiguredPhyBandwidth.setStatus("current")
_RbAuOutdoorConfigTable_Object = MibTable
rbAuOutdoorConfigTable = _RbAuOutdoorConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 8)
)
if mibBuilder.loadTexts:
    rbAuOutdoorConfigTable.setStatus("deprecated")
_RbAuOutdoorConfigEntry_Object = MibTableRow
rbAuOutdoorConfigEntry = _RbAuOutdoorConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 8, 1)
)
rbAuOutdoorConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "auOutdoorUnitIndex"),
)
if mibBuilder.loadTexts:
    rbAuOutdoorConfigEntry.setStatus("deprecated")


class _AuOutdoorUnitIndex_Type(Integer32):
    """Custom type auOutdoorUnitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_AuOutdoorUnitIndex_Type.__name__ = "Integer32"
_AuOutdoorUnitIndex_Object = MibTableColumn
auOutdoorUnitIndex = _AuOutdoorUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 8, 1, 1),
    _AuOutdoorUnitIndex_Type()
)
auOutdoorUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auOutdoorUnitIndex.setStatus("deprecated")


class _AuFrequencyBand_Type(Integer32):
    """Custom type auFrequencyBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("bandA1", 1),
          ("bandB", 2),
          ("bandF", 3),
          ("bandD", 4),
          ("bandE", 5),
          ("band23", 12),
          ("band25A", 13),
          ("band25B", 14))
    )


_AuFrequencyBand_Type.__name__ = "Integer32"
_AuFrequencyBand_Object = MibTableColumn
auFrequencyBand = _AuFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 8, 1, 2),
    _AuFrequencyBand_Type()
)
auFrequencyBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    auFrequencyBand.setStatus("deprecated")
_AuTxPower_Type = DisplayString
_AuTxPower_Object = MibTableColumn
auTxPower = _AuTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 8, 1, 3),
    _AuTxPower_Type()
)
auTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auTxPower.setStatus("deprecated")
_RbSuPhyParameters_ObjectIdentity = ObjectIdentity
rbSuPhyParameters = _RbSuPhyParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 9)
)


class _SuPhyCurrentBandwidth_Type(Integer32):
    """Custom type suPhyCurrentBandwidth based on Integer32"""
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
        *(("b175", 1),
          ("b35", 2),
          ("b50", 3),
          ("b70", 4),
          ("b100", 5))
    )


_SuPhyCurrentBandwidth_Type.__name__ = "Integer32"
_SuPhyCurrentBandwidth_Object = MibScalar
suPhyCurrentBandwidth = _SuPhyCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 9, 1),
    _SuPhyCurrentBandwidth_Type()
)
suPhyCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suPhyCurrentBandwidth.setStatus("current")
_SuPhyCurrentTxFrequencyChannel_Type = DisplayString
_SuPhyCurrentTxFrequencyChannel_Object = MibScalar
suPhyCurrentTxFrequencyChannel = _SuPhyCurrentTxFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 9, 2),
    _SuPhyCurrentTxFrequencyChannel_Type()
)
suPhyCurrentTxFrequencyChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    suPhyCurrentTxFrequencyChannel.setStatus("current")


class _SuPhyConfiguredBandwidth_Type(Integer32):
    """Custom type suPhyConfiguredBandwidth based on Integer32"""
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
        *(("b175", 1),
          ("b35", 2),
          ("b50", 3),
          ("b70", 4),
          ("b100", 5))
    )


_SuPhyConfiguredBandwidth_Type.__name__ = "Integer32"
_SuPhyConfiguredBandwidth_Object = MibScalar
suPhyConfiguredBandwidth = _SuPhyConfiguredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 9, 3),
    _SuPhyConfiguredBandwidth_Type()
)
suPhyConfiguredBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suPhyConfiguredBandwidth.setStatus("current")
_SuPhyConfiguredTxFrequencyChannel_Type = DisplayString
_SuPhyConfiguredTxFrequencyChannel_Object = MibScalar
suPhyConfiguredTxFrequencyChannel = _SuPhyConfiguredTxFrequencyChannel_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 9, 4),
    _SuPhyConfiguredTxFrequencyChannel_Type()
)
suPhyConfiguredTxFrequencyChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    suPhyConfiguredTxFrequencyChannel.setStatus("current")
_RbSuBestBstAuParams_ObjectIdentity = ObjectIdentity
rbSuBestBstAuParams = _RbSuBestBstAuParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10)
)
_RbSuBestBstAuParamsTable_Object = MibTable
rbSuBestBstAuParamsTable = _RbSuBestBstAuParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1)
)
if mibBuilder.loadTexts:
    rbSuBestBstAuParamsTable.setStatus("current")
_RbSuBestBstAuParamsEntry_Object = MibTableRow
rbSuBestBstAuParamsEntry = _RbSuBestBstAuParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1)
)
rbSuBestBstAuParamsEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
)
if mibBuilder.loadTexts:
    rbSuBestBstAuParamsEntry.setStatus("current")


class _RbSuCurrentBestBstAuSupport_Type(Integer32):
    """Custom type rbSuCurrentBestBstAuSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RbSuCurrentBestBstAuSupport_Type.__name__ = "Integer32"
_RbSuCurrentBestBstAuSupport_Object = MibTableColumn
rbSuCurrentBestBstAuSupport = _RbSuCurrentBestBstAuSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 1),
    _RbSuCurrentBestBstAuSupport_Type()
)
rbSuCurrentBestBstAuSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentBestBstAuSupport.setStatus("current")


class _RbSuConfiguredBestBstAuSupport_Type(Integer32):
    """Custom type rbSuConfiguredBestBstAuSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("enable", 1),
          ("disable", 2))
    )


_RbSuConfiguredBestBstAuSupport_Type.__name__ = "Integer32"
_RbSuConfiguredBestBstAuSupport_Object = MibTableColumn
rbSuConfiguredBestBstAuSupport = _RbSuConfiguredBestBstAuSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 2),
    _RbSuConfiguredBestBstAuSupport_Type()
)
rbSuConfiguredBestBstAuSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredBestBstAuSupport.setStatus("current")


class _RbSuCurrentPreferredBstAuId_Type(OctetString):
    """Custom type rbSuCurrentPreferredBstAuId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuCurrentPreferredBstAuId_Type.__name__ = "OctetString"
_RbSuCurrentPreferredBstAuId_Object = MibTableColumn
rbSuCurrentPreferredBstAuId = _RbSuCurrentPreferredBstAuId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 3),
    _RbSuCurrentPreferredBstAuId_Type()
)
rbSuCurrentPreferredBstAuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentPreferredBstAuId.setStatus("current")


class _RbSuConfiguredPreferredBstAuId_Type(OctetString):
    """Custom type rbSuConfiguredPreferredBstAuId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuConfiguredPreferredBstAuId_Type.__name__ = "OctetString"
_RbSuConfiguredPreferredBstAuId_Object = MibTableColumn
rbSuConfiguredPreferredBstAuId = _RbSuConfiguredPreferredBstAuId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 4),
    _RbSuConfiguredPreferredBstAuId_Type()
)
rbSuConfiguredPreferredBstAuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredPreferredBstAuId.setStatus("current")


class _RbSuCurrentPreferredBstAuMask_Type(OctetString):
    """Custom type rbSuCurrentPreferredBstAuMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuCurrentPreferredBstAuMask_Type.__name__ = "OctetString"
_RbSuCurrentPreferredBstAuMask_Object = MibTableColumn
rbSuCurrentPreferredBstAuMask = _RbSuCurrentPreferredBstAuMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 5),
    _RbSuCurrentPreferredBstAuMask_Type()
)
rbSuCurrentPreferredBstAuMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentPreferredBstAuMask.setStatus("current")


class _RbSuConfiguredPreferredBstAuMask_Type(OctetString):
    """Custom type rbSuConfiguredPreferredBstAuMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuConfiguredPreferredBstAuMask_Type.__name__ = "OctetString"
_RbSuConfiguredPreferredBstAuMask_Object = MibTableColumn
rbSuConfiguredPreferredBstAuMask = _RbSuConfiguredPreferredBstAuMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 6),
    _RbSuConfiguredPreferredBstAuMask_Type()
)
rbSuConfiguredPreferredBstAuMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredPreferredBstAuMask.setStatus("current")


class _RbSuSelectedBstAu_Type(OctetString):
    """Custom type rbSuSelectedBstAu based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuSelectedBstAu_Type.__name__ = "OctetString"
_RbSuSelectedBstAu_Object = MibTableColumn
rbSuSelectedBstAu = _RbSuSelectedBstAu_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 7),
    _RbSuSelectedBstAu_Type()
)
rbSuSelectedBstAu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuSelectedBstAu.setStatus("current")
_RbSuSelectedRxFrequency_Type = DisplayString
_RbSuSelectedRxFrequency_Object = MibTableColumn
rbSuSelectedRxFrequency = _RbSuSelectedRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 8),
    _RbSuSelectedRxFrequency_Type()
)
rbSuSelectedRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuSelectedRxFrequency.setStatus("current")
_RbSuSelectedTxFrequency_Type = DisplayString
_RbSuSelectedTxFrequency_Object = MibTableColumn
rbSuSelectedTxFrequency = _RbSuSelectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 9),
    _RbSuSelectedTxFrequency_Type()
)
rbSuSelectedTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuSelectedTxFrequency.setStatus("current")


class _RbSuCurrentBstAuId_Type(OctetString):
    """Custom type rbSuCurrentBstAuId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuCurrentBstAuId_Type.__name__ = "OctetString"
_RbSuCurrentBstAuId_Object = MibTableColumn
rbSuCurrentBstAuId = _RbSuCurrentBstAuId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 10),
    _RbSuCurrentBstAuId_Type()
)
rbSuCurrentBstAuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentBstAuId.setStatus("current")


class _RbSuConfiguredBstAuId_Type(OctetString):
    """Custom type rbSuConfiguredBstAuId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuConfiguredBstAuId_Type.__name__ = "OctetString"
_RbSuConfiguredBstAuId_Object = MibTableColumn
rbSuConfiguredBstAuId = _RbSuConfiguredBstAuId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 11),
    _RbSuConfiguredBstAuId_Type()
)
rbSuConfiguredBstAuId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredBstAuId.setStatus("current")


class _RbSuCurrentBstAuMask_Type(OctetString):
    """Custom type rbSuCurrentBstAuMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuCurrentBstAuMask_Type.__name__ = "OctetString"
_RbSuCurrentBstAuMask_Object = MibTableColumn
rbSuCurrentBstAuMask = _RbSuCurrentBstAuMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 12),
    _RbSuCurrentBstAuMask_Type()
)
rbSuCurrentBstAuMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentBstAuMask.setStatus("current")


class _RbSuConfiguredBstAuMask_Type(OctetString):
    """Custom type rbSuConfiguredBstAuMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbSuConfiguredBstAuMask_Type.__name__ = "OctetString"
_RbSuConfiguredBstAuMask_Object = MibTableColumn
rbSuConfiguredBstAuMask = _RbSuConfiguredBstAuMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 1, 1, 13),
    _RbSuConfiguredBstAuMask_Type()
)
rbSuConfiguredBstAuMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredBstAuMask.setStatus("current")
_RbSuBestBstAuDataTable_Object = MibTable
rbSuBestBstAuDataTable = _RbSuBestBstAuDataTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 2)
)
if mibBuilder.loadTexts:
    rbSuBestBstAuDataTable.setStatus("current")
_RbSuBestBstAuDataEntry_Object = MibTableRow
rbSuBestBstAuDataEntry = _RbSuBestBstAuDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 2, 1)
)
rbSuBestBstAuDataEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
    (0, "RAINBOW-MIB", "rbBstAuIndx"),
)
if mibBuilder.loadTexts:
    rbSuBestBstAuDataEntry.setStatus("current")


class _RbBstAuIndx_Type(Integer32):
    """Custom type rbBstAuIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RbBstAuIndx_Type.__name__ = "Integer32"
_RbBstAuIndx_Object = MibTableColumn
rbBstAuIndx = _RbBstAuIndx_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 2, 1, 1),
    _RbBstAuIndx_Type()
)
rbBstAuIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstAuIndx.setStatus("current")


class _RbBstAuId_Type(OctetString):
    """Custom type rbBstAuId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbBstAuId_Type.__name__ = "OctetString"
_RbBstAuId_Object = MibTableColumn
rbBstAuId = _RbBstAuId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 2, 1, 2),
    _RbBstAuId_Type()
)
rbBstAuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstAuId.setStatus("current")
_RbBstAuRxFrequency_Type = DisplayString
_RbBstAuRxFrequency_Object = MibTableColumn
rbBstAuRxFrequency = _RbBstAuRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 2, 1, 3),
    _RbBstAuRxFrequency_Type()
)
rbBstAuRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstAuRxFrequency.setStatus("current")
_RbBstAuSNR_Type = TenthdB
_RbBstAuSNR_Object = MibTableColumn
rbBstAuSNR = _RbBstAuSNR_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 2, 1, 4),
    _RbBstAuSNR_Type()
)
rbBstAuSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstAuSNR.setStatus("current")


class _RbBstAuRxAntennaNumber_Type(Integer32):
    """Custom type rbBstAuRxAntennaNumber based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("internal1", 1),
          ("internal2", 2),
          ("internal3", 3),
          ("internal4", 4),
          ("internal5", 5),
          ("internal6", 6),
          ("external", 7),
          ("automatic", 8))
    )


_RbBstAuRxAntennaNumber_Type.__name__ = "Integer32"
_RbBstAuRxAntennaNumber_Object = MibTableColumn
rbBstAuRxAntennaNumber = _RbBstAuRxAntennaNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 10, 2, 1, 5),
    _RbBstAuRxAntennaNumber_Type()
)
rbBstAuRxAntennaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstAuRxAntennaNumber.setStatus("current")
_RbSuRadioParameters_ObjectIdentity = ObjectIdentity
rbSuRadioParameters = _RbSuRadioParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11)
)
_RbSuRadioParametersTable_Object = MibTable
rbSuRadioParametersTable = _RbSuRadioParametersTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1)
)
if mibBuilder.loadTexts:
    rbSuRadioParametersTable.setStatus("current")
_RbSuRadioParametersEntry_Object = MibTableRow
rbSuRadioParametersEntry = _RbSuRadioParametersEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1)
)
rbSuRadioParametersEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSuMacAddr"),
)
if mibBuilder.loadTexts:
    rbSuRadioParametersEntry.setStatus("current")


class _RbSuCurrentScanStartFreq_Type(DisplayString):
    """Custom type rbSuCurrentScanStartFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuCurrentScanStartFreq_Type.__name__ = "DisplayString"
_RbSuCurrentScanStartFreq_Object = MibTableColumn
rbSuCurrentScanStartFreq = _RbSuCurrentScanStartFreq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 1),
    _RbSuCurrentScanStartFreq_Type()
)
rbSuCurrentScanStartFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentScanStartFreq.setStatus("current")


class _RbSuConfiguredScanStartFreq_Type(DisplayString):
    """Custom type rbSuConfiguredScanStartFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuConfiguredScanStartFreq_Type.__name__ = "DisplayString"
_RbSuConfiguredScanStartFreq_Object = MibTableColumn
rbSuConfiguredScanStartFreq = _RbSuConfiguredScanStartFreq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 2),
    _RbSuConfiguredScanStartFreq_Type()
)
rbSuConfiguredScanStartFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredScanStartFreq.setStatus("current")


class _RbSuCurrentScanEndFreq_Type(DisplayString):
    """Custom type rbSuCurrentScanEndFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuCurrentScanEndFreq_Type.__name__ = "DisplayString"
_RbSuCurrentScanEndFreq_Object = MibTableColumn
rbSuCurrentScanEndFreq = _RbSuCurrentScanEndFreq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 3),
    _RbSuCurrentScanEndFreq_Type()
)
rbSuCurrentScanEndFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentScanEndFreq.setStatus("current")


class _RbSuConfiguredScanEndFreq_Type(DisplayString):
    """Custom type rbSuConfiguredScanEndFreq based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuConfiguredScanEndFreq_Type.__name__ = "DisplayString"
_RbSuConfiguredScanEndFreq_Object = MibTableColumn
rbSuConfiguredScanEndFreq = _RbSuConfiguredScanEndFreq_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 4),
    _RbSuConfiguredScanEndFreq_Type()
)
rbSuConfiguredScanEndFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredScanEndFreq.setStatus("current")


class _RbSuCurrentScanStep_Type(DisplayString):
    """Custom type rbSuCurrentScanStep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuCurrentScanStep_Type.__name__ = "DisplayString"
_RbSuCurrentScanStep_Object = MibTableColumn
rbSuCurrentScanStep = _RbSuCurrentScanStep_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 5),
    _RbSuCurrentScanStep_Type()
)
rbSuCurrentScanStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentScanStep.setStatus("current")


class _RbSuConfiguredScanStep_Type(DisplayString):
    """Custom type rbSuConfiguredScanStep based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuConfiguredScanStep_Type.__name__ = "DisplayString"
_RbSuConfiguredScanStep_Object = MibTableColumn
rbSuConfiguredScanStep = _RbSuConfiguredScanStep_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 6),
    _RbSuConfiguredScanStep_Type()
)
rbSuConfiguredScanStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredScanStep.setStatus("current")


class _RbSuCurrentScanMask_Type(OctetString):
    """Custom type rbSuCurrentScanMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RbSuCurrentScanMask_Type.__name__ = "OctetString"
_RbSuCurrentScanMask_Object = MibTableColumn
rbSuCurrentScanMask = _RbSuCurrentScanMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 7),
    _RbSuCurrentScanMask_Type()
)
rbSuCurrentScanMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentScanMask.setStatus("current")


class _RbSuConfiguredScanMask_Type(OctetString):
    """Custom type rbSuConfiguredScanMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_RbSuConfiguredScanMask_Type.__name__ = "OctetString"
_RbSuConfiguredScanMask_Object = MibTableColumn
rbSuConfiguredScanMask = _RbSuConfiguredScanMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 8),
    _RbSuConfiguredScanMask_Type()
)
rbSuConfiguredScanMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredScanMask.setStatus("current")


class _RbSuDiscreteF1_Type(DisplayString):
    """Custom type rbSuDiscreteF1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF1_Type.__name__ = "DisplayString"
_RbSuDiscreteF1_Object = MibTableColumn
rbSuDiscreteF1 = _RbSuDiscreteF1_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 9),
    _RbSuDiscreteF1_Type()
)
rbSuDiscreteF1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF1.setStatus("current")


class _RbSuDiscreteF2_Type(DisplayString):
    """Custom type rbSuDiscreteF2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF2_Type.__name__ = "DisplayString"
_RbSuDiscreteF2_Object = MibTableColumn
rbSuDiscreteF2 = _RbSuDiscreteF2_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 10),
    _RbSuDiscreteF2_Type()
)
rbSuDiscreteF2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF2.setStatus("current")


class _RbSuDiscreteF3_Type(DisplayString):
    """Custom type rbSuDiscreteF3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF3_Type.__name__ = "DisplayString"
_RbSuDiscreteF3_Object = MibTableColumn
rbSuDiscreteF3 = _RbSuDiscreteF3_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 11),
    _RbSuDiscreteF3_Type()
)
rbSuDiscreteF3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF3.setStatus("current")


class _RbSuDiscreteF4_Type(DisplayString):
    """Custom type rbSuDiscreteF4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF4_Type.__name__ = "DisplayString"
_RbSuDiscreteF4_Object = MibTableColumn
rbSuDiscreteF4 = _RbSuDiscreteF4_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 12),
    _RbSuDiscreteF4_Type()
)
rbSuDiscreteF4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF4.setStatus("current")


class _RbSuDiscreteF5_Type(DisplayString):
    """Custom type rbSuDiscreteF5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF5_Type.__name__ = "DisplayString"
_RbSuDiscreteF5_Object = MibTableColumn
rbSuDiscreteF5 = _RbSuDiscreteF5_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 13),
    _RbSuDiscreteF5_Type()
)
rbSuDiscreteF5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF5.setStatus("current")


class _RbSuDiscreteF6_Type(DisplayString):
    """Custom type rbSuDiscreteF6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF6_Type.__name__ = "DisplayString"
_RbSuDiscreteF6_Object = MibTableColumn
rbSuDiscreteF6 = _RbSuDiscreteF6_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 14),
    _RbSuDiscreteF6_Type()
)
rbSuDiscreteF6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF6.setStatus("current")


class _RbSuDiscreteF7_Type(DisplayString):
    """Custom type rbSuDiscreteF7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF7_Type.__name__ = "DisplayString"
_RbSuDiscreteF7_Object = MibTableColumn
rbSuDiscreteF7 = _RbSuDiscreteF7_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 15),
    _RbSuDiscreteF7_Type()
)
rbSuDiscreteF7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF7.setStatus("current")


class _RbSuDiscreteF8_Type(DisplayString):
    """Custom type rbSuDiscreteF8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF8_Type.__name__ = "DisplayString"
_RbSuDiscreteF8_Object = MibTableColumn
rbSuDiscreteF8 = _RbSuDiscreteF8_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 16),
    _RbSuDiscreteF8_Type()
)
rbSuDiscreteF8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF8.setStatus("current")


class _RbSuDiscreteF9_Type(DisplayString):
    """Custom type rbSuDiscreteF9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF9_Type.__name__ = "DisplayString"
_RbSuDiscreteF9_Object = MibTableColumn
rbSuDiscreteF9 = _RbSuDiscreteF9_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 17),
    _RbSuDiscreteF9_Type()
)
rbSuDiscreteF9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF9.setStatus("current")


class _RbSuDiscreteF10_Type(DisplayString):
    """Custom type rbSuDiscreteF10 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbSuDiscreteF10_Type.__name__ = "DisplayString"
_RbSuDiscreteF10_Object = MibTableColumn
rbSuDiscreteF10 = _RbSuDiscreteF10_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 18),
    _RbSuDiscreteF10_Type()
)
rbSuDiscreteF10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuDiscreteF10.setStatus("current")


class _RbSuCurrentBandwidth_Type(Integer32):
    """Custom type rbSuCurrentBandwidth based on Integer32"""
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
        *(("b175", 1),
          ("b35", 2),
          ("b50", 3),
          ("b70", 4),
          ("b100", 5))
    )


_RbSuCurrentBandwidth_Type.__name__ = "Integer32"
_RbSuCurrentBandwidth_Object = MibTableColumn
rbSuCurrentBandwidth = _RbSuCurrentBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 19),
    _RbSuCurrentBandwidth_Type()
)
rbSuCurrentBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSuCurrentBandwidth.setStatus("current")


class _RbSuConfiguredBandwidth_Type(Integer32):
    """Custom type rbSuConfiguredBandwidth based on Integer32"""
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
        *(("b175", 1),
          ("b35", 2),
          ("b50", 3),
          ("b70", 4),
          ("b100", 5))
    )


_RbSuConfiguredBandwidth_Type.__name__ = "Integer32"
_RbSuConfiguredBandwidth_Object = MibTableColumn
rbSuConfiguredBandwidth = _RbSuConfiguredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 7, 2, 11, 1, 1, 20),
    _RbSuConfiguredBandwidth_Type()
)
rbSuConfiguredBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSuConfiguredBandwidth.setStatus("current")
_RbTesting_ObjectIdentity = ObjectIdentity
rbTesting = _RbTesting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8)
)
_RbBerTest_ObjectIdentity = ObjectIdentity
rbBerTest = _RbBerTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1)
)
_RbBerTestSetup_ObjectIdentity = ObjectIdentity
rbBerTestSetup = _RbBerTestSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1)
)


class _RbBerTestDataSize_Type(Integer32):
    """Custom type rbBerTestDataSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 100000000),
    )


_RbBerTestDataSize_Type.__name__ = "Integer32"
_RbBerTestDataSize_Object = MibScalar
rbBerTestDataSize = _RbBerTestDataSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1, 1),
    _RbBerTestDataSize_Type()
)
rbBerTestDataSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBerTestDataSize.setStatus("current")


class _RbBerTestModulation_Type(Integer32):
    """Custom type rbBerTestModulation based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("notDefined", 0),
          ("rBpsk12", 1),
          ("rBpsk34", 2),
          ("rQpsk12", 3),
          ("rQpsk34", 4),
          ("r16Qam12", 5),
          ("r16Qam34", 6),
          ("r64Qam23", 7),
          ("r64Qam34", 8))
    )


_RbBerTestModulation_Type.__name__ = "Integer32"
_RbBerTestModulation_Object = MibScalar
rbBerTestModulation = _RbBerTestModulation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1, 2),
    _RbBerTestModulation_Type()
)
rbBerTestModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBerTestModulation.setStatus("current")


class _RbBerTestAction_Type(Integer32):
    """Custom type rbBerTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("abort", 2),
          ("none", 3))
    )


_RbBerTestAction_Type.__name__ = "Integer32"
_RbBerTestAction_Object = MibScalar
rbBerTestAction = _RbBerTestAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1, 3),
    _RbBerTestAction_Type()
)
rbBerTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBerTestAction.setStatus("current")


class _RbBerTestStatus_Type(Integer32):
    """Custom type rbBerTestStatus based on Integer32"""
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
        *(("inactive", 1),
          ("active", 2),
          ("finished", 3),
          ("failed", 4),
          ("suDisconnected", 5))
    )


_RbBerTestStatus_Type.__name__ = "Integer32"
_RbBerTestStatus_Object = MibScalar
rbBerTestStatus = _RbBerTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1, 4),
    _RbBerTestStatus_Type()
)
rbBerTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestStatus.setStatus("current")
_RbBerTestSU_Type = MacAddress
_RbBerTestSU_Object = MibScalar
rbBerTestSU = _RbBerTestSU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1, 5),
    _RbBerTestSU_Type()
)
rbBerTestSU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestSU.setStatus("current")


class _RbBerTestTrafficPriority_Type(Integer32):
    """Custom type rbBerTestTrafficPriority based on Integer32"""
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
        *(("notDefined", 0),
          ("realTime", 1),
          ("notRealTime", 2),
          ("bestEffort", 3))
    )


_RbBerTestTrafficPriority_Type.__name__ = "Integer32"
_RbBerTestTrafficPriority_Object = MibScalar
rbBerTestTrafficPriority = _RbBerTestTrafficPriority_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1, 6),
    _RbBerTestTrafficPriority_Type()
)
rbBerTestTrafficPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBerTestTrafficPriority.setStatus("current")


class _RbBerTestMaxPacketSize_Type(Integer32):
    """Custom type rbBerTestMaxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 4000),
    )


_RbBerTestMaxPacketSize_Type.__name__ = "Integer32"
_RbBerTestMaxPacketSize_Object = MibScalar
rbBerTestMaxPacketSize = _RbBerTestMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 1, 7),
    _RbBerTestMaxPacketSize_Type()
)
rbBerTestMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBerTestMaxPacketSize.setStatus("current")
_RbBerTestResults_ObjectIdentity = ObjectIdentity
rbBerTestResults = _RbBerTestResults_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2)
)
_RbBerTestULReceivedBits_Type = Integer32
_RbBerTestULReceivedBits_Object = MibScalar
rbBerTestULReceivedBits = _RbBerTestULReceivedBits_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 1),
    _RbBerTestULReceivedBits_Type()
)
rbBerTestULReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestULReceivedBits.setStatus("current")
_RbBerTestULReceivedErrorBits_Type = Integer32
_RbBerTestULReceivedErrorBits_Object = MibScalar
rbBerTestULReceivedErrorBits = _RbBerTestULReceivedErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 2),
    _RbBerTestULReceivedErrorBits_Type()
)
rbBerTestULReceivedErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestULReceivedErrorBits.setStatus("current")
_RbBerTestDLReceivedBits_Type = Integer32
_RbBerTestDLReceivedBits_Object = MibScalar
rbBerTestDLReceivedBits = _RbBerTestDLReceivedBits_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 3),
    _RbBerTestDLReceivedBits_Type()
)
rbBerTestDLReceivedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestDLReceivedBits.setStatus("current")
_RbBerTestDLReceivedErrorBits_Type = Integer32
_RbBerTestDLReceivedErrorBits_Object = MibScalar
rbBerTestDLReceivedErrorBits = _RbBerTestDLReceivedErrorBits_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 4),
    _RbBerTestDLReceivedErrorBits_Type()
)
rbBerTestDLReceivedErrorBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestDLReceivedErrorBits.setStatus("current")
_RbBerTestDLMapLost_Type = Integer32
_RbBerTestDLMapLost_Object = MibScalar
rbBerTestDLMapLost = _RbBerTestDLMapLost_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 5),
    _RbBerTestDLMapLost_Type()
)
rbBerTestDLMapLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestDLMapLost.setStatus("current")
_RbBerTestResultsSU_Type = MacAddress
_RbBerTestResultsSU_Object = MibScalar
rbBerTestResultsSU = _RbBerTestResultsSU_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 6),
    _RbBerTestResultsSU_Type()
)
rbBerTestResultsSU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestResultsSU.setStatus("current")
_RbBerTestUplinkBER_Type = DisplayString
_RbBerTestUplinkBER_Object = MibScalar
rbBerTestUplinkBER = _RbBerTestUplinkBER_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 7),
    _RbBerTestUplinkBER_Type()
)
rbBerTestUplinkBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestUplinkBER.setStatus("current")
_RbBerTestDownlinkBER_Type = DisplayString
_RbBerTestDownlinkBER_Object = MibScalar
rbBerTestDownlinkBER = _RbBerTestDownlinkBER_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 8, 1, 2, 8),
    _RbBerTestDownlinkBER_Type()
)
rbBerTestDownlinkBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBerTestDownlinkBER.setStatus("current")
_RbIPConfig_ObjectIdentity = ObjectIdentity
rbIPConfig = _RbIPConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9)
)
_RbIpIfConfigTable_Object = MibTable
rbIpIfConfigTable = _RbIpIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1)
)
if mibBuilder.loadTexts:
    rbIpIfConfigTable.setStatus("current")
_RbIpIfConfigEntry_Object = MibTableRow
rbIpIfConfigEntry = _RbIpIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1)
)
rbIpIfConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "ipIfConfigIfIndex"),
)
if mibBuilder.loadTexts:
    rbIpIfConfigEntry.setStatus("current")


class _IpIfConfigIfIndex_Type(Integer32):
    """Custom type ipIfConfigIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IpIfConfigIfIndex_Type.__name__ = "Integer32"
_IpIfConfigIfIndex_Object = MibTableColumn
ipIfConfigIfIndex = _IpIfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1, 1),
    _IpIfConfigIfIndex_Type()
)
ipIfConfigIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipIfConfigIfIndex.setStatus("current")


class _IpIfConfigVlanId_Type(Integer32):
    """Custom type ipIfConfigVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_IpIfConfigVlanId_Type.__name__ = "Integer32"
_IpIfConfigVlanId_Object = MibTableColumn
ipIfConfigVlanId = _IpIfConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1, 2),
    _IpIfConfigVlanId_Type()
)
ipIfConfigVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfConfigVlanId.setStatus("current")
_IpIfConfigIpAddress_Type = IpAddress
_IpIfConfigIpAddress_Object = MibTableColumn
ipIfConfigIpAddress = _IpIfConfigIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1, 3),
    _IpIfConfigIpAddress_Type()
)
ipIfConfigIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfConfigIpAddress.setStatus("current")
_IpIfConfigNetworkMask_Type = IpAddress
_IpIfConfigNetworkMask_Object = MibTableColumn
ipIfConfigNetworkMask = _IpIfConfigNetworkMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1, 4),
    _IpIfConfigNetworkMask_Type()
)
ipIfConfigNetworkMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfConfigNetworkMask.setStatus("current")
_IpIfConfigDefaultGateway_Type = IpAddress
_IpIfConfigDefaultGateway_Object = MibTableColumn
ipIfConfigDefaultGateway = _IpIfConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1, 5),
    _IpIfConfigDefaultGateway_Type()
)
ipIfConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfConfigDefaultGateway.setStatus("current")
_IpIfStaticRouteSubnet_Type = IpAddress
_IpIfStaticRouteSubnet_Object = MibTableColumn
ipIfStaticRouteSubnet = _IpIfStaticRouteSubnet_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1, 6),
    _IpIfStaticRouteSubnet_Type()
)
ipIfStaticRouteSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfStaticRouteSubnet.setStatus("current")
_IpIfStaticRouteSubnetMask_Type = IpAddress
_IpIfStaticRouteSubnetMask_Object = MibTableColumn
ipIfStaticRouteSubnetMask = _IpIfStaticRouteSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 9, 1, 1, 7),
    _IpIfStaticRouteSubnetMask_Type()
)
ipIfStaticRouteSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipIfStaticRouteSubnetMask.setStatus("current")
_RbSwUpgrade_ObjectIdentity = ObjectIdentity
rbSwUpgrade = _RbSwUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10)
)
_RbSwAuFiles_Type = DisplayString
_RbSwAuFiles_Object = MibScalar
rbSwAuFiles = _RbSwAuFiles_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 1),
    _RbSwAuFiles_Type()
)
rbSwAuFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwAuFiles.setStatus("current")
_RbSwSuFiles_Type = DisplayString
_RbSwSuFiles_Object = MibScalar
rbSwSuFiles = _RbSwSuFiles_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 2),
    _RbSwSuFiles_Type()
)
rbSwSuFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwSuFiles.setStatus("current")
_RbSwDeleteFiles_Type = DisplayString
_RbSwDeleteFiles_Object = MibScalar
rbSwDeleteFiles = _RbSwDeleteFiles_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 3),
    _RbSwDeleteFiles_Type()
)
rbSwDeleteFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwDeleteFiles.setStatus("current")
_RbSwSuDefaultFile_Type = DisplayString
_RbSwSuDefaultFile_Object = MibScalar
rbSwSuDefaultFile = _RbSwSuDefaultFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 4),
    _RbSwSuDefaultFile_Type()
)
rbSwSuDefaultFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwSuDefaultFile.setStatus("current")


class _RbSwSuDefaultAction_Type(Integer32):
    """Custom type rbSwSuDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("putToShadow", 3),
          ("runFromShadow", 4),
          ("makeShadowOperational", 5))
    )


_RbSwSuDefaultAction_Type.__name__ = "Integer32"
_RbSwSuDefaultAction_Object = MibScalar
rbSwSuDefaultAction = _RbSwSuDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 5),
    _RbSwSuDefaultAction_Type()
)
rbSwSuDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwSuDefaultAction.setStatus("current")
_RbSwUpgradeLogTable_Object = MibTable
rbSwUpgradeLogTable = _RbSwUpgradeLogTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6)
)
if mibBuilder.loadTexts:
    rbSwUpgradeLogTable.setStatus("current")
_RbSwUpgradeLogEntry_Object = MibTableRow
rbSwUpgradeLogEntry = _RbSwUpgradeLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1)
)
rbSwUpgradeLogEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSwDeviceType"),
    (0, "RAINBOW-MIB", "rbSwDeviceId"),
)
if mibBuilder.loadTexts:
    rbSwUpgradeLogEntry.setStatus("current")


class _RbSwDeviceType_Type(Integer32):
    """Custom type rbSwDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("au", 1),
          ("su", 2))
    )


_RbSwDeviceType_Type.__name__ = "Integer32"
_RbSwDeviceType_Object = MibTableColumn
rbSwDeviceType = _RbSwDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1, 1),
    _RbSwDeviceType_Type()
)
rbSwDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwDeviceType.setStatus("current")


class _RbSwDeviceId_Type(OctetString):
    """Custom type rbSwDeviceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_RbSwDeviceId_Type.__name__ = "OctetString"
_RbSwDeviceId_Object = MibTableColumn
rbSwDeviceId = _RbSwDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1, 2),
    _RbSwDeviceId_Type()
)
rbSwDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwDeviceId.setStatus("current")
_RbSwUpgradeFileName_Type = DisplayString
_RbSwUpgradeFileName_Object = MibTableColumn
rbSwUpgradeFileName = _RbSwUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1, 3),
    _RbSwUpgradeFileName_Type()
)
rbSwUpgradeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwUpgradeFileName.setStatus("current")


class _RbSwUpgradeAction_Type(Integer32):
    """Custom type rbSwUpgradeAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("putToShadow", 3),
          ("resetAndRunFromShadow", 4),
          ("makeRunningVersionOperational", 5),
          ("startRegistration", 6))
    )


_RbSwUpgradeAction_Type.__name__ = "Integer32"
_RbSwUpgradeAction_Object = MibTableColumn
rbSwUpgradeAction = _RbSwUpgradeAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1, 4),
    _RbSwUpgradeAction_Type()
)
rbSwUpgradeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwUpgradeAction.setStatus("current")
_RbSwUpgradeStartTime_Type = TimeTicks
_RbSwUpgradeStartTime_Object = MibTableColumn
rbSwUpgradeStartTime = _RbSwUpgradeStartTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1, 5),
    _RbSwUpgradeStartTime_Type()
)
rbSwUpgradeStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwUpgradeStartTime.setStatus("current")
_RbSwUpgradeEndTime_Type = TimeTicks
_RbSwUpgradeEndTime_Object = MibTableColumn
rbSwUpgradeEndTime = _RbSwUpgradeEndTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1, 6),
    _RbSwUpgradeEndTime_Type()
)
rbSwUpgradeEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwUpgradeEndTime.setStatus("current")


class _RbSwUpgradeStatus_Type(Integer32):
    """Custom type rbSwUpgradeStatus based on Integer32"""
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
        *(("none", 1),
          ("success", 2),
          ("inProgress", 3),
          ("failed", 4),
          ("pending", 5))
    )


_RbSwUpgradeStatus_Type.__name__ = "Integer32"
_RbSwUpgradeStatus_Object = MibTableColumn
rbSwUpgradeStatus = _RbSwUpgradeStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 6, 1, 7),
    _RbSwUpgradeStatus_Type()
)
rbSwUpgradeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSwUpgradeStatus.setStatus("current")
_RbSwSuSiDefaultFile_Type = DisplayString
_RbSwSuSiDefaultFile_Object = MibScalar
rbSwSuSiDefaultFile = _RbSwSuSiDefaultFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 7),
    _RbSwSuSiDefaultFile_Type()
)
rbSwSuSiDefaultFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwSuSiDefaultFile.setStatus("current")


class _RbSwSuSiDefaultAction_Type(Integer32):
    """Custom type rbSwSuSiDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("putToShadow", 3),
          ("runFromShadow", 4),
          ("makeShadowOperational", 5))
    )


_RbSwSuSiDefaultAction_Type.__name__ = "Integer32"
_RbSwSuSiDefaultAction_Object = MibScalar
rbSwSuSiDefaultAction = _RbSwSuSiDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 8),
    _RbSwSuSiDefaultAction_Type()
)
rbSwSuSiDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwSuSiDefaultAction.setStatus("current")
_RbSwAuDefaultFile_Type = DisplayString
_RbSwAuDefaultFile_Object = MibScalar
rbSwAuDefaultFile = _RbSwAuDefaultFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 9),
    _RbSwAuDefaultFile_Type()
)
rbSwAuDefaultFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwAuDefaultFile.setStatus("current")


class _RbSwAuDefaultAction_Type(Integer32):
    """Custom type rbSwAuDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("putToShadow", 3),
          ("runFromShadow", 4),
          ("makeShadowOperational", 5))
    )


_RbSwAuDefaultAction_Type.__name__ = "Integer32"
_RbSwAuDefaultAction_Object = MibScalar
rbSwAuDefaultAction = _RbSwAuDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 10),
    _RbSwAuDefaultAction_Type()
)
rbSwAuDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwAuDefaultAction.setStatus("current")
_RbSwAuSiDefaultFile_Type = DisplayString
_RbSwAuSiDefaultFile_Object = MibScalar
rbSwAuSiDefaultFile = _RbSwAuSiDefaultFile_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 11),
    _RbSwAuSiDefaultFile_Type()
)
rbSwAuSiDefaultFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwAuSiDefaultFile.setStatus("current")


class _RbSwAuSiDefaultAction_Type(Integer32):
    """Custom type rbSwAuSiDefaultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("putToShadow", 3),
          ("runFromShadow", 4),
          ("makeShadowOperational", 5))
    )


_RbSwAuSiDefaultAction_Type.__name__ = "Integer32"
_RbSwAuSiDefaultAction_Object = MibScalar
rbSwAuSiDefaultAction = _RbSwAuSiDefaultAction_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 12),
    _RbSwAuSiDefaultAction_Type()
)
rbSwAuSiDefaultAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbSwAuSiDefaultAction.setStatus("current")


class _RbBstClearAllSuSwUpgradeParams_Type(Integer32):
    """Custom type rbBstClearAllSuSwUpgradeParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clearAllSuSwUpgradeParams", 2))
    )


_RbBstClearAllSuSwUpgradeParams_Type.__name__ = "Integer32"
_RbBstClearAllSuSwUpgradeParams_Object = MibScalar
rbBstClearAllSuSwUpgradeParams = _RbBstClearAllSuSwUpgradeParams_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 13),
    _RbBstClearAllSuSwUpgradeParams_Type()
)
rbBstClearAllSuSwUpgradeParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBstClearAllSuSwUpgradeParams.setStatus("current")


class _RbBstClearAllAuSwUpgradeParams_Type(Integer32):
    """Custom type rbBstClearAllAuSwUpgradeParams based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("clearAllAuSwUpgradeParams", 2))
    )


_RbBstClearAllAuSwUpgradeParams_Type.__name__ = "Integer32"
_RbBstClearAllAuSwUpgradeParams_Object = MibScalar
rbBstClearAllAuSwUpgradeParams = _RbBstClearAllAuSwUpgradeParams_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 10, 14),
    _RbBstClearAllAuSwUpgradeParams_Type()
)
rbBstClearAllAuSwUpgradeParams.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBstClearAllAuSwUpgradeParams.setStatus("current")
_RbBaseStation_ObjectIdentity = ObjectIdentity
rbBaseStation = _RbBaseStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11)
)
_RbBsAtpcParameters_ObjectIdentity = ObjectIdentity
rbBsAtpcParameters = _RbBsAtpcParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 1)
)


class _RbBsATPCSupport_Type(Integer32):
    """Custom type rbBsATPCSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("notDefined", 3))
    )


_RbBsATPCSupport_Type.__name__ = "Integer32"
_RbBsATPCSupport_Object = MibScalar
rbBsATPCSupport = _RbBsATPCSupport_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 1, 1),
    _RbBsATPCSupport_Type()
)
rbBsATPCSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBsATPCSupport.setStatus("current")


class _RbBsOptimalRSSI_Type(Integer32):
    """Custom type rbBsOptimalRSSI based on Integer32"""
    defaultValue = -73

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90, -60),
    )


_RbBsOptimalRSSI_Type.__name__ = "Integer32"
_RbBsOptimalRSSI_Object = MibScalar
rbBsOptimalRSSI = _RbBsOptimalRSSI_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 1, 2),
    _RbBsOptimalRSSI_Type()
)
rbBsOptimalRSSI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBsOptimalRSSI.setStatus("current")
_RbBsCellParameters_ObjectIdentity = ObjectIdentity
rbBsCellParameters = _RbBsCellParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 2)
)


class _RbBSConfiguredOperatorId_Type(OctetString):
    """Custom type rbBSConfiguredOperatorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_RbBSConfiguredOperatorId_Type.__name__ = "OctetString"
_RbBSConfiguredOperatorId_Object = MibScalar
rbBSConfiguredOperatorId = _RbBSConfiguredOperatorId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 2, 1),
    _RbBSConfiguredOperatorId_Type()
)
rbBSConfiguredOperatorId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBSConfiguredOperatorId.setStatus("current")


class _RbBSConfiguredCellId_Type(OctetString):
    """Custom type rbBSConfiguredCellId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_RbBSConfiguredCellId_Type.__name__ = "OctetString"
_RbBSConfiguredCellId_Object = MibScalar
rbBSConfiguredCellId = _RbBSConfiguredCellId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 2, 2),
    _RbBSConfiguredCellId_Type()
)
rbBSConfiguredCellId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBSConfiguredCellId.setStatus("current")
_RbBsRFModeParameters_ObjectIdentity = ObjectIdentity
rbBsRFModeParameters = _RbBsRFModeParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 3)
)


class _RbBsRFConfiguredDuplexMode_Type(Integer32):
    """Custom type rbBsRFConfiguredDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fdd", 1),
          ("tdd", 2))
    )


_RbBsRFConfiguredDuplexMode_Type.__name__ = "Integer32"
_RbBsRFConfiguredDuplexMode_Object = MibScalar
rbBsRFConfiguredDuplexMode = _RbBsRFConfiguredDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 3, 1),
    _RbBsRFConfiguredDuplexMode_Type()
)
rbBsRFConfiguredDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBsRFConfiguredDuplexMode.setStatus("current")


class _RbBsRFCurrentDuplexMode_Type(Integer32):
    """Custom type rbBsRFCurrentDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fdd", 1),
          ("tdd", 2))
    )


_RbBsRFCurrentDuplexMode_Type.__name__ = "Integer32"
_RbBsRFCurrentDuplexMode_Object = MibScalar
rbBsRFCurrentDuplexMode = _RbBsRFCurrentDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 3, 2),
    _RbBsRFCurrentDuplexMode_Type()
)
rbBsRFCurrentDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBsRFCurrentDuplexMode.setStatus("current")


class _RbBsRFConfiguredDlUlRatio_Type(Integer32):
    """Custom type rbBsRFConfiguredDlUlRatio based on Integer32"""
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
        *(("unavailable", 0),
          ("tdd65", 1),
          ("tdd60", 2),
          ("tdd55", 3),
          ("tdd50", 4),
          ("tdd45", 5),
          ("tdd40", 6),
          ("tdd35", 7))
    )


_RbBsRFConfiguredDlUlRatio_Type.__name__ = "Integer32"
_RbBsRFConfiguredDlUlRatio_Object = MibScalar
rbBsRFConfiguredDlUlRatio = _RbBsRFConfiguredDlUlRatio_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 3, 3),
    _RbBsRFConfiguredDlUlRatio_Type()
)
rbBsRFConfiguredDlUlRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBsRFConfiguredDlUlRatio.setStatus("current")


class _RbBsRFCurrentDlUlRatio_Type(Integer32):
    """Custom type rbBsRFCurrentDlUlRatio based on Integer32"""
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
        *(("unavailable", 0),
          ("tdd65", 1),
          ("tdd60", 2),
          ("tdd55", 3),
          ("tdd50", 4),
          ("tdd45", 5),
          ("tdd40", 6),
          ("tdd35", 7))
    )


_RbBsRFCurrentDlUlRatio_Type.__name__ = "Integer32"
_RbBsRFCurrentDlUlRatio_Object = MibScalar
rbBsRFCurrentDlUlRatio = _RbBsRFCurrentDlUlRatio_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 3, 4),
    _RbBsRFCurrentDlUlRatio_Type()
)
rbBsRFCurrentDlUlRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBsRFCurrentDlUlRatio.setStatus("current")
_RbBSClockConfigParameters_ObjectIdentity = ObjectIdentity
rbBSClockConfigParameters = _RbBSClockConfigParameters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 4)
)


class _RbBSConfiguredExternalPPSClock_Type(Integer32):
    """Custom type rbBSConfiguredExternalPPSClock based on Integer32"""
    defaultValue = 1

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


_RbBSConfiguredExternalPPSClock_Type.__name__ = "Integer32"
_RbBSConfiguredExternalPPSClock_Object = MibScalar
rbBSConfiguredExternalPPSClock = _RbBSConfiguredExternalPPSClock_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 4, 1),
    _RbBSConfiguredExternalPPSClock_Type()
)
rbBSConfiguredExternalPPSClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBSConfiguredExternalPPSClock.setStatus("current")


class _RbBSCurrentExternalPPSClock_Type(Integer32):
    """Custom type rbBSCurrentExternalPPSClock based on Integer32"""
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


_RbBSCurrentExternalPPSClock_Type.__name__ = "Integer32"
_RbBSCurrentExternalPPSClock_Object = MibScalar
rbBSCurrentExternalPPSClock = _RbBSCurrentExternalPPSClock_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 4, 2),
    _RbBSCurrentExternalPPSClock_Type()
)
rbBSCurrentExternalPPSClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBSCurrentExternalPPSClock.setStatus("current")


class _RbBSConfiguredExternal16MhzClock_Type(Integer32):
    """Custom type rbBSConfiguredExternal16MhzClock based on Integer32"""
    defaultValue = 2

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


_RbBSConfiguredExternal16MhzClock_Type.__name__ = "Integer32"
_RbBSConfiguredExternal16MhzClock_Object = MibScalar
rbBSConfiguredExternal16MhzClock = _RbBSConfiguredExternal16MhzClock_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 4, 3),
    _RbBSConfiguredExternal16MhzClock_Type()
)
rbBSConfiguredExternal16MhzClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbBSConfiguredExternal16MhzClock.setStatus("current")


class _RbBSCurrentExternal16MhzClock_Type(Integer32):
    """Custom type rbBSCurrentExternal16MhzClock based on Integer32"""
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


_RbBSCurrentExternal16MhzClock_Type.__name__ = "Integer32"
_RbBSCurrentExternal16MhzClock_Object = MibScalar
rbBSCurrentExternal16MhzClock = _RbBSCurrentExternal16MhzClock_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 11, 4, 4),
    _RbBSCurrentExternal16MhzClock_Type()
)
rbBSCurrentExternal16MhzClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBSCurrentExternal16MhzClock.setStatus("current")
_RbRadioCluster_ObjectIdentity = ObjectIdentity
rbRadioCluster = _RbRadioCluster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12)
)
_RbRadioClusterTable_Object = MibTable
rbRadioClusterTable = _RbRadioClusterTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    rbRadioClusterTable.setStatus("current")
_RbRadioClusterEntry_Object = MibTableRow
rbRadioClusterEntry = _RbRadioClusterEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1, 1)
)
rbRadioClusterEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbRadioClusterId"),
)
if mibBuilder.loadTexts:
    rbRadioClusterEntry.setStatus("current")


class _RbRadioClusterId_Type(Integer32):
    """Custom type rbRadioClusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RbRadioClusterId_Type.__name__ = "Integer32"
_RbRadioClusterId_Object = MibTableColumn
rbRadioClusterId = _RbRadioClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1, 1, 1),
    _RbRadioClusterId_Type()
)
rbRadioClusterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbRadioClusterId.setStatus("current")


class _RbRadioClusterName_Type(DisplayString):
    """Custom type rbRadioClusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbRadioClusterName_Type.__name__ = "DisplayString"
_RbRadioClusterName_Object = MibTableColumn
rbRadioClusterName = _RbRadioClusterName_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1, 1, 2),
    _RbRadioClusterName_Type()
)
rbRadioClusterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadioClusterName.setStatus("current")


class _RbRadioClusterLocation_Type(DisplayString):
    """Custom type rbRadioClusterLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbRadioClusterLocation_Type.__name__ = "DisplayString"
_RbRadioClusterLocation_Object = MibTableColumn
rbRadioClusterLocation = _RbRadioClusterLocation_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1, 1, 3),
    _RbRadioClusterLocation_Type()
)
rbRadioClusterLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadioClusterLocation.setStatus("current")


class _RbRadioClusterSectorHeading_Type(Integer32):
    """Custom type rbRadioClusterSectorHeading based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 359),
    )


_RbRadioClusterSectorHeading_Type.__name__ = "Integer32"
_RbRadioClusterSectorHeading_Object = MibTableColumn
rbRadioClusterSectorHeading = _RbRadioClusterSectorHeading_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1, 1, 4),
    _RbRadioClusterSectorHeading_Type()
)
rbRadioClusterSectorHeading.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadioClusterSectorHeading.setStatus("current")


class _RbRadioClusterSectorBeamWidth_Type(Integer32):
    """Custom type rbRadioClusterSectorBeamWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 359),
    )


_RbRadioClusterSectorBeamWidth_Type.__name__ = "Integer32"
_RbRadioClusterSectorBeamWidth_Object = MibTableColumn
rbRadioClusterSectorBeamWidth = _RbRadioClusterSectorBeamWidth_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1, 1, 5),
    _RbRadioClusterSectorBeamWidth_Type()
)
rbRadioClusterSectorBeamWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadioClusterSectorBeamWidth.setStatus("current")
_RbRadioClusterRowStatus_Type = RowStatus
_RbRadioClusterRowStatus_Object = MibTableColumn
rbRadioClusterRowStatus = _RbRadioClusterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 12, 1, 1, 6),
    _RbRadioClusterRowStatus_Type()
)
rbRadioClusterRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbRadioClusterRowStatus.setStatus("current")
_RbOduConfig_ObjectIdentity = ObjectIdentity
rbOduConfig = _RbOduConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13)
)
_RbOduConfigTable_Object = MibTable
rbOduConfigTable = _RbOduConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    rbOduConfigTable.setStatus("current")
_RbOduConfigEntry_Object = MibTableRow
rbOduConfigEntry = _RbOduConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1)
)
rbOduConfigEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbOduConfigId"),
)
if mibBuilder.loadTexts:
    rbOduConfigEntry.setStatus("current")


class _RbOduConfigId_Type(Integer32):
    """Custom type rbOduConfigId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_RbOduConfigId_Type.__name__ = "Integer32"
_RbOduConfigId_Object = MibTableColumn
rbOduConfigId = _RbOduConfigId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 1),
    _RbOduConfigId_Type()
)
rbOduConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduConfigId.setStatus("current")


class _RbOduAssociatedRadioClusterId_Type(Integer32):
    """Custom type rbOduAssociatedRadioClusterId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_RbOduAssociatedRadioClusterId_Type.__name__ = "Integer32"
_RbOduAssociatedRadioClusterId_Object = MibTableColumn
rbOduAssociatedRadioClusterId = _RbOduAssociatedRadioClusterId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 2),
    _RbOduAssociatedRadioClusterId_Type()
)
rbOduAssociatedRadioClusterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbOduAssociatedRadioClusterId.setStatus("current")
_RbOduTxPower_Type = DisplayString
_RbOduTxPower_Object = MibTableColumn
rbOduTxPower = _RbOduTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 3),
    _RbOduTxPower_Type()
)
rbOduTxPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbOduTxPower.setStatus("current")


class _RbOduAdminStatus_Type(Integer32):
    """Custom type rbOduAdminStatus based on Integer32"""
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


_RbOduAdminStatus_Type.__name__ = "Integer32"
_RbOduAdminStatus_Object = MibTableColumn
rbOduAdminStatus = _RbOduAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 4),
    _RbOduAdminStatus_Type()
)
rbOduAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbOduAdminStatus.setStatus("current")
_RbOduTemperature_Type = Integer32
_RbOduTemperature_Object = MibTableColumn
rbOduTemperature = _RbOduTemperature_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 5),
    _RbOduTemperature_Type()
)
rbOduTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduTemperature.setStatus("current")


class _RbOduHwRevision_Type(DisplayString):
    """Custom type rbOduHwRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbOduHwRevision_Type.__name__ = "DisplayString"
_RbOduHwRevision_Object = MibTableColumn
rbOduHwRevision = _RbOduHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 6),
    _RbOduHwRevision_Type()
)
rbOduHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduHwRevision.setStatus("current")


class _RbOduHwConfigDescription_Type(DisplayString):
    """Custom type rbOduHwConfigDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbOduHwConfigDescription_Type.__name__ = "DisplayString"
_RbOduHwConfigDescription_Object = MibTableColumn
rbOduHwConfigDescription = _RbOduHwConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 7),
    _RbOduHwConfigDescription_Type()
)
rbOduHwConfigDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduHwConfigDescription.setStatus("current")


class _RbOduOperationalStatus_Type(Integer32):
    """Custom type rbOduOperationalStatus based on Integer32"""
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
        *(("initFailure", 1),
          ("down", 2),
          ("powerOff", 3),
          ("powerOnWait", 4),
          ("powerOn", 5),
          ("initializing", 6),
          ("up", 7))
    )


_RbOduOperationalStatus_Type.__name__ = "Integer32"
_RbOduOperationalStatus_Object = MibTableColumn
rbOduOperationalStatus = _RbOduOperationalStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 8),
    _RbOduOperationalStatus_Type()
)
rbOduOperationalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduOperationalStatus.setStatus("current")


class _RbOduHwHC08Version_Type(DisplayString):
    """Custom type rbOduHwHC08Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbOduHwHC08Version_Type.__name__ = "DisplayString"
_RbOduHwHC08Version_Object = MibTableColumn
rbOduHwHC08Version = _RbOduHwHC08Version_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 9),
    _RbOduHwHC08Version_Type()
)
rbOduHwHC08Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduHwHC08Version.setStatus("current")


class _RbOduCpldVersion_Type(DisplayString):
    """Custom type rbOduCpldVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RbOduCpldVersion_Type.__name__ = "DisplayString"
_RbOduCpldVersion_Object = MibTableColumn
rbOduCpldVersion = _RbOduCpldVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 10),
    _RbOduCpldVersion_Type()
)
rbOduCpldVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduCpldVersion.setStatus("current")
_RbOduCardSerialNumber_Type = DisplayString
_RbOduCardSerialNumber_Object = MibTableColumn
rbOduCardSerialNumber = _RbOduCardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 11),
    _RbOduCardSerialNumber_Type()
)
rbOduCardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduCardSerialNumber.setStatus("current")
_RbOduConfigFrequencyBand_Type = Integer32
_RbOduConfigFrequencyBand_Object = MibTableColumn
rbOduConfigFrequencyBand = _RbOduConfigFrequencyBand_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 12),
    _RbOduConfigFrequencyBand_Type()
)
rbOduConfigFrequencyBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbOduConfigFrequencyBand.setStatus("current")
_RbOduRowStatus_Type = RowStatus
_RbOduRowStatus_Object = MibTableColumn
rbOduRowStatus = _RbOduRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 13),
    _RbOduRowStatus_Type()
)
rbOduRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbOduRowStatus.setStatus("current")
_RbOduMaxTxPower_Type = Integer32
_RbOduMaxTxPower_Object = MibTableColumn
rbOduMaxTxPower = _RbOduMaxTxPower_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 13, 1, 1, 14),
    _RbOduMaxTxPower_Type()
)
rbOduMaxTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbOduMaxTxPower.setStatus("current")
_RbChainConfig_ObjectIdentity = ObjectIdentity
rbChainConfig = _RbChainConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14)
)


class _RbGPSSupported_Type(Integer32):
    """Custom type rbGPSSupported based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("notSupported", 2))
    )


_RbGPSSupported_Type.__name__ = "Integer32"
_RbGPSSupported_Object = MibScalar
rbGPSSupported = _RbGPSSupported_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 1),
    _RbGPSSupported_Type()
)
rbGPSSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSSupported.setStatus("current")


class _RbConfiguredChainNumber_Type(Unsigned32):
    """Custom type rbConfiguredChainNumber based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_RbConfiguredChainNumber_Type.__name__ = "Unsigned32"
_RbConfiguredChainNumber_Object = MibScalar
rbConfiguredChainNumber = _RbConfiguredChainNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 2),
    _RbConfiguredChainNumber_Type()
)
rbConfiguredChainNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbConfiguredChainNumber.setStatus("current")


class _RbCurrentChainNumber_Type(Unsigned32):
    """Custom type rbCurrentChainNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_RbCurrentChainNumber_Type.__name__ = "Unsigned32"
_RbCurrentChainNumber_Object = MibScalar
rbCurrentChainNumber = _RbCurrentChainNumber_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 3),
    _RbCurrentChainNumber_Type()
)
rbCurrentChainNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbCurrentChainNumber.setStatus("current")


class _RbGPSConfiguredType_Type(Integer32):
    """Custom type rbGPSConfiguredType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trimble", 1),
          ("symmetricom", 2))
    )


_RbGPSConfiguredType_Type.__name__ = "Integer32"
_RbGPSConfiguredType_Object = MibScalar
rbGPSConfiguredType = _RbGPSConfiguredType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 4),
    _RbGPSConfiguredType_Type()
)
rbGPSConfiguredType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbGPSConfiguredType.setStatus("current")


class _RbGPSCurrentType_Type(Integer32):
    """Custom type rbGPSCurrentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("trimble", 1),
          ("symmetricom", 2))
    )


_RbGPSCurrentType_Type.__name__ = "Integer32"
_RbGPSCurrentType_Object = MibScalar
rbGPSCurrentType = _RbGPSCurrentType_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 5),
    _RbGPSCurrentType_Type()
)
rbGPSCurrentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSCurrentType.setStatus("current")


class _RbTimeZoneOffsetFromUTC_Type(DisplayString):
    """Custom type rbTimeZoneOffsetFromUTC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_RbTimeZoneOffsetFromUTC_Type.__name__ = "DisplayString"
_RbTimeZoneOffsetFromUTC_Object = MibScalar
rbTimeZoneOffsetFromUTC = _RbTimeZoneOffsetFromUTC_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 6),
    _RbTimeZoneOffsetFromUTC_Type()
)
rbTimeZoneOffsetFromUTC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbTimeZoneOffsetFromUTC.setStatus("current")


class _RbStopTxAfterHoldOverTimeout_Type(Integer32):
    """Custom type rbStopTxAfterHoldOverTimeout based on Integer32"""
    defaultValue = 2

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


_RbStopTxAfterHoldOverTimeout_Type.__name__ = "Integer32"
_RbStopTxAfterHoldOverTimeout_Object = MibScalar
rbStopTxAfterHoldOverTimeout = _RbStopTxAfterHoldOverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 7),
    _RbStopTxAfterHoldOverTimeout_Type()
)
rbStopTxAfterHoldOverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbStopTxAfterHoldOverTimeout.setStatus("current")


class _RbHoldOverPassedTimeout_Type(Unsigned32):
    """Custom type rbHoldOverPassedTimeout based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2880),
    )


_RbHoldOverPassedTimeout_Type.__name__ = "Unsigned32"
_RbHoldOverPassedTimeout_Object = MibScalar
rbHoldOverPassedTimeout = _RbHoldOverPassedTimeout_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 14, 8),
    _RbHoldOverPassedTimeout_Type()
)
rbHoldOverPassedTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rbHoldOverPassedTimeout.setStatus("current")
_RbGPSInfo_ObjectIdentity = ObjectIdentity
rbGPSInfo = _RbGPSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15)
)


class _RbGPSNumberOfRxSatellites_Type(Unsigned32):
    """Custom type rbGPSNumberOfRxSatellites based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RbGPSNumberOfRxSatellites_Type.__name__ = "Unsigned32"
_RbGPSNumberOfRxSatellites_Object = MibScalar
rbGPSNumberOfRxSatellites = _RbGPSNumberOfRxSatellites_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15, 1),
    _RbGPSNumberOfRxSatellites_Type()
)
rbGPSNumberOfRxSatellites.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSNumberOfRxSatellites.setStatus("current")
_RbGPSLongitude_Type = DisplayString
_RbGPSLongitude_Object = MibScalar
rbGPSLongitude = _RbGPSLongitude_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15, 2),
    _RbGPSLongitude_Type()
)
rbGPSLongitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSLongitude.setStatus("current")
_RbGPSLatitude_Type = DisplayString
_RbGPSLatitude_Object = MibScalar
rbGPSLatitude = _RbGPSLatitude_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15, 3),
    _RbGPSLatitude_Type()
)
rbGPSLatitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSLatitude.setStatus("current")
_RbGPSAltitude_Type = DisplayString
_RbGPSAltitude_Object = MibScalar
rbGPSAltitude = _RbGPSAltitude_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15, 4),
    _RbGPSAltitude_Type()
)
rbGPSAltitude.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSAltitude.setStatus("current")


class _RbGPSLocalDateAndTime_Type(DisplayString):
    """Custom type rbGPSLocalDateAndTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_RbGPSLocalDateAndTime_Type.__name__ = "DisplayString"
_RbGPSLocalDateAndTime_Object = MibScalar
rbGPSLocalDateAndTime = _RbGPSLocalDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15, 5),
    _RbGPSLocalDateAndTime_Type()
)
rbGPSLocalDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSLocalDateAndTime.setStatus("current")


class _RbGPSNavigationProcessorSWVersion_Type(DisplayString):
    """Custom type rbGPSNavigationProcessorSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbGPSNavigationProcessorSWVersion_Type.__name__ = "DisplayString"
_RbGPSNavigationProcessorSWVersion_Object = MibScalar
rbGPSNavigationProcessorSWVersion = _RbGPSNavigationProcessorSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15, 6),
    _RbGPSNavigationProcessorSWVersion_Type()
)
rbGPSNavigationProcessorSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSNavigationProcessorSWVersion.setStatus("current")


class _RbGPSSignalProcessorSWVersion_Type(DisplayString):
    """Custom type rbGPSSignalProcessorSWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbGPSSignalProcessorSWVersion_Type.__name__ = "DisplayString"
_RbGPSSignalProcessorSWVersion_Object = MibScalar
rbGPSSignalProcessorSWVersion = _RbGPSSignalProcessorSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 15, 7),
    _RbGPSSignalProcessorSWVersion_Type()
)
rbGPSSignalProcessorSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbGPSSignalProcessorSWVersion.setStatus("current")
_RbLicense_ObjectIdentity = ObjectIdentity
rbLicense = _RbLicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50)
)
_RbLicenseBankTable_Object = MibTable
rbLicenseBankTable = _RbLicenseBankTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 1)
)
if mibBuilder.loadTexts:
    rbLicenseBankTable.setStatus("current")
_RbLicenseBankEntry_Object = MibTableRow
rbLicenseBankEntry = _RbLicenseBankEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 1, 1)
)
rbLicenseBankEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbLicenseId"),
    (0, "RAINBOW-MIB", "rbLicenseValue"),
)
if mibBuilder.loadTexts:
    rbLicenseBankEntry.setStatus("current")


class _RbLicenseId_Type(Integer32):
    """Custom type rbLicenseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bandwidth", 1)
    )


_RbLicenseId_Type.__name__ = "Integer32"
_RbLicenseId_Object = MibTableColumn
rbLicenseId = _RbLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 1, 1, 1),
    _RbLicenseId_Type()
)
rbLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbLicenseId.setStatus("current")
_RbLicenseValue_Type = Unsigned32
_RbLicenseValue_Object = MibTableColumn
rbLicenseValue = _RbLicenseValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 1, 1, 2),
    _RbLicenseValue_Type()
)
rbLicenseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbLicenseValue.setStatus("current")
_RbLicenseCount_Type = Unsigned32
_RbLicenseCount_Object = MibTableColumn
rbLicenseCount = _RbLicenseCount_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 1, 1, 3),
    _RbLicenseCount_Type()
)
rbLicenseCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbLicenseCount.setStatus("current")


class _RbLicenseDescription_Type(DisplayString):
    """Custom type rbLicenseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbLicenseDescription_Type.__name__ = "DisplayString"
_RbLicenseDescription_Object = MibTableColumn
rbLicenseDescription = _RbLicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 1, 1, 4),
    _RbLicenseDescription_Type()
)
rbLicenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbLicenseDescription.setStatus("current")
_RbLicenseBst_ObjectIdentity = ObjectIdentity
rbLicenseBst = _RbLicenseBst_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 2)
)
_RbLicenseBstTable_Object = MibTable
rbLicenseBstTable = _RbLicenseBstTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 2, 1)
)
if mibBuilder.loadTexts:
    rbLicenseBstTable.setStatus("current")
_RbLicenseBstEntry_Object = MibTableRow
rbLicenseBstEntry = _RbLicenseBstEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 2, 1, 1)
)
rbLicenseBstEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbBstLicenseId"),
)
if mibBuilder.loadTexts:
    rbLicenseBstEntry.setStatus("current")


class _RbBstLicenseId_Type(Integer32):
    """Custom type rbBstLicenseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bandwidth", 1),
          ("maxNumberOfSUs", 2))
    )


_RbBstLicenseId_Type.__name__ = "Integer32"
_RbBstLicenseId_Object = MibTableColumn
rbBstLicenseId = _RbBstLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 2, 1, 1, 1),
    _RbBstLicenseId_Type()
)
rbBstLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstLicenseId.setStatus("current")
_RbBstLicenseValue_Type = Unsigned32
_RbBstLicenseValue_Object = MibTableColumn
rbBstLicenseValue = _RbBstLicenseValue_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 2, 1, 1, 2),
    _RbBstLicenseValue_Type()
)
rbBstLicenseValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstLicenseValue.setStatus("current")


class _RbBstLicenseDescription_Type(DisplayString):
    """Custom type rbBstLicenseDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RbBstLicenseDescription_Type.__name__ = "DisplayString"
_RbBstLicenseDescription_Object = MibTableColumn
rbBstLicenseDescription = _RbBstLicenseDescription_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 2, 1, 1, 3),
    _RbBstLicenseDescription_Type()
)
rbBstLicenseDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbBstLicenseDescription.setStatus("current")
_RbNumberOfSUsGraceEndDate_Type = DisplayString
_RbNumberOfSUsGraceEndDate_Object = MibScalar
rbNumberOfSUsGraceEndDate = _RbNumberOfSUsGraceEndDate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 2, 2),
    _RbNumberOfSUsGraceEndDate_Type()
)
rbNumberOfSUsGraceEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbNumberOfSUsGraceEndDate.setStatus("current")
_RbSUTempGracePeriodLicenseTable_Object = MibTable
rbSUTempGracePeriodLicenseTable = _RbSUTempGracePeriodLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 3)
)
if mibBuilder.loadTexts:
    rbSUTempGracePeriodLicenseTable.setStatus("current")
_RbSUTempGracePeriodLicenseEntry_Object = MibTableRow
rbSUTempGracePeriodLicenseEntry = _RbSUTempGracePeriodLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 3, 1)
)
rbSUTempGracePeriodLicenseEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSUTempGracePeriodIndex"),
)
if mibBuilder.loadTexts:
    rbSUTempGracePeriodLicenseEntry.setStatus("current")
_RbSUTempGracePeriodIndex_Type = Unsigned32
_RbSUTempGracePeriodIndex_Object = MibTableColumn
rbSUTempGracePeriodIndex = _RbSUTempGracePeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 3, 1, 1),
    _RbSUTempGracePeriodIndex_Type()
)
rbSUTempGracePeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUTempGracePeriodIndex.setStatus("current")
_RbSUTempGracePeriodSuMacAddr_Type = MacAddress
_RbSUTempGracePeriodSuMacAddr_Object = MibTableColumn
rbSUTempGracePeriodSuMacAddr = _RbSUTempGracePeriodSuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 3, 1, 2),
    _RbSUTempGracePeriodSuMacAddr_Type()
)
rbSUTempGracePeriodSuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUTempGracePeriodSuMacAddr.setStatus("current")


class _RbSUTempGracePeriodLicenseId_Type(Integer32):
    """Custom type rbSUTempGracePeriodLicenseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bandwidth", 1)
    )


_RbSUTempGracePeriodLicenseId_Type.__name__ = "Integer32"
_RbSUTempGracePeriodLicenseId_Object = MibTableColumn
rbSUTempGracePeriodLicenseId = _RbSUTempGracePeriodLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 3, 1, 3),
    _RbSUTempGracePeriodLicenseId_Type()
)
rbSUTempGracePeriodLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUTempGracePeriodLicenseId.setStatus("current")
_RbSUTempGracePeriodLicenseEndDate_Type = DisplayString
_RbSUTempGracePeriodLicenseEndDate_Object = MibTableColumn
rbSUTempGracePeriodLicenseEndDate = _RbSUTempGracePeriodLicenseEndDate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 3, 1, 4),
    _RbSUTempGracePeriodLicenseEndDate_Type()
)
rbSUTempGracePeriodLicenseEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUTempGracePeriodLicenseEndDate.setStatus("current")
_RbSUGracePeriodLicenseTable_Object = MibTable
rbSUGracePeriodLicenseTable = _RbSUGracePeriodLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 4)
)
if mibBuilder.loadTexts:
    rbSUGracePeriodLicenseTable.setStatus("current")
_RbSUGracePeriodLicenseEntry_Object = MibTableRow
rbSUGracePeriodLicenseEntry = _RbSUGracePeriodLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 4, 1)
)
rbSUGracePeriodLicenseEntry.setIndexNames(
    (0, "RAINBOW-MIB", "rbSUGracePeriodIndex"),
)
if mibBuilder.loadTexts:
    rbSUGracePeriodLicenseEntry.setStatus("current")
_RbSUGracePeriodIndex_Type = Unsigned32
_RbSUGracePeriodIndex_Object = MibTableColumn
rbSUGracePeriodIndex = _RbSUGracePeriodIndex_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 4, 1, 1),
    _RbSUGracePeriodIndex_Type()
)
rbSUGracePeriodIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUGracePeriodIndex.setStatus("current")
_RbSUGracePeriodSuMacAddr_Type = MacAddress
_RbSUGracePeriodSuMacAddr_Object = MibTableColumn
rbSUGracePeriodSuMacAddr = _RbSUGracePeriodSuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 4, 1, 2),
    _RbSUGracePeriodSuMacAddr_Type()
)
rbSUGracePeriodSuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUGracePeriodSuMacAddr.setStatus("current")


class _RbSUGracePeriodLicenseId_Type(Integer32):
    """Custom type rbSUGracePeriodLicenseId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("bandwidth", 1)
    )


_RbSUGracePeriodLicenseId_Type.__name__ = "Integer32"
_RbSUGracePeriodLicenseId_Object = MibTableColumn
rbSUGracePeriodLicenseId = _RbSUGracePeriodLicenseId_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 4, 1, 3),
    _RbSUGracePeriodLicenseId_Type()
)
rbSUGracePeriodLicenseId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUGracePeriodLicenseId.setStatus("current")
_RbSUGracePeriodLicenseEndDate_Type = DisplayString
_RbSUGracePeriodLicenseEndDate_Object = MibTableColumn
rbSUGracePeriodLicenseEndDate = _RbSUGracePeriodLicenseEndDate_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 4, 1, 4),
    _RbSUGracePeriodLicenseEndDate_Type()
)
rbSUGracePeriodLicenseEndDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUGracePeriodLicenseEndDate.setStatus("current")


class _RbSUGracePeriodLicenseStatus_Type(Integer32):
    """Custom type rbSUGracePeriodLicenseStatus based on Integer32"""
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
        *(("licenseNone", 1),
          ("licenseActivated", 2),
          ("licenseActiveWarnIssued", 3),
          ("licenseUsed", 4))
    )


_RbSUGracePeriodLicenseStatus_Type.__name__ = "Integer32"
_RbSUGracePeriodLicenseStatus_Object = MibTableColumn
rbSUGracePeriodLicenseStatus = _RbSUGracePeriodLicenseStatus_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 50, 4, 1, 5),
    _RbSUGracePeriodLicenseStatus_Type()
)
rbSUGracePeriodLicenseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbSUGracePeriodLicenseStatus.setStatus("current")


class _EndOfMib_Type(Integer32):
    """Custom type endOfMib based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("endOfMib", 1)
    )


_EndOfMib_Type.__name__ = "Integer32"
_EndOfMib_Object = MibScalar
endOfMib = _EndOfMib_Object(
    (1, 3, 6, 1, 4, 1, 12394, 1, 2, 300),
    _EndOfMib_Type()
)
endOfMib.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    endOfMib.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAINBOW-MIB",
    **{"TrapSeverity": TrapSeverity,
       "Modulation": Modulation,
       "LinkSpeedAndDuplex": LinkSpeedAndDuplex,
       "TenthdB": TenthdB,
       "rainbow": rainbow,
       "rbSysConfig": rbSysConfig,
       "rbSysGeneral": rbSysGeneral,
       "rbSysFaultStatus": rbSysFaultStatus,
       "rbSysLastTrapSeqNumber": rbSysLastTrapSeqNumber,
       "rbChassisConfig": rbChassisConfig,
       "rbSlotConfigTable": rbSlotConfigTable,
       "rbSlotConfigEntry": rbSlotConfigEntry,
       "rbSlotNumber": rbSlotNumber,
       "rbSlotDetectedCard": rbSlotDetectedCard,
       "rbSlotConfiguredCard": rbSlotConfiguredCard,
       "rbSlotAllowedCard": rbSlotAllowedCard,
       "rbSlotLedStatus": rbSlotLedStatus,
       "rbSlotFaultStatus": rbSlotFaultStatus,
       "rbSlotExtractorState": rbSlotExtractorState,
       "rbNpuConfiguration": rbNpuConfiguration,
       "rbNpuConfigTable": rbNpuConfigTable,
       "rbNpuConfigEntry": rbNpuConfigEntry,
       "rbNpuSerialNo": rbNpuSerialNo,
       "rbNpuSysName": rbNpuSysName,
       "rbNpuFaultStatus": rbNpuFaultStatus,
       "rbNpuHwRevision": rbNpuHwRevision,
       "rbNpuOperSwFileName": rbNpuOperSwFileName,
       "rbNpuOperSwVersion": rbNpuOperSwVersion,
       "rbNpuShadowSwFileName": rbNpuShadowSwFileName,
       "rbNpuShadowSwVersion": rbNpuShadowSwVersion,
       "rbNpuRunningSoftware": rbNpuRunningSoftware,
       "rbNpuOperVersionValidity": rbNpuOperVersionValidity,
       "rbNpuShadowVersionValidity": rbNpuShadowVersionValidity,
       "rbNpuRedundancyStatus": rbNpuRedundancyStatus,
       "rbNpuUnitControl": rbNpuUnitControl,
       "rbNpuSetDefaults": rbNpuSetDefaults,
       "rbNpuHwConfigDescription": rbNpuHwConfigDescription,
       "rbNpuManagementInterface": rbNpuManagementInterface,
       "rbNpuCreateConfigFile": rbNpuCreateConfigFile,
       "rbNpuCreateBackupConfigFile": rbNpuCreateBackupConfigFile,
       "rbNpuCumulativePowerOnTime": rbNpuCumulativePowerOnTime,
       "rbNpuBootSwVersion": rbNpuBootSwVersion,
       "rbNpuTemperature": rbNpuTemperature,
       "rbNpuDrapTtlRetries": rbNpuDrapTtlRetries,
       "rbNpuRedundantCPLDVersion": rbNpuRedundantCPLDVersion,
       "rbNpuBridgingParameters": rbNpuBridgingParameters,
       "rbNpuBridgeAgingTime": rbNpuBridgeAgingTime,
       "rbNpuFrequencyBandsParameters": rbNpuFrequencyBandsParameters,
       "rbFrequencyBandsFileVersion": rbFrequencyBandsFileVersion,
       "rbFrequencyBandsTable": rbFrequencyBandsTable,
       "rbFrequencyBandsEntry": rbFrequencyBandsEntry,
       "rbFrequencyBandId": rbFrequencyBandId,
       "rbFrequencyBandName": rbFrequencyBandName,
       "rbFrequencyBandRevision": rbFrequencyBandRevision,
       "rbFrequencyBandGroupId": rbFrequencyBandGroupId,
       "rbFrequencyBandStartFrequency": rbFrequencyBandStartFrequency,
       "rbFrequencyBandStopFrequency": rbFrequencyBandStopFrequency,
       "rbFrequencyBandStep": rbFrequencyBandStep,
       "rbFrequencyBandDuplexSeparation": rbFrequencyBandDuplexSeparation,
       "rbAuConfigTable": rbAuConfigTable,
       "rbAuConfigEntry": rbAuConfigEntry,
       "rbAuSerialNo": rbAuSerialNo,
       "rbAuSysName": rbAuSysName,
       "rbAuFaultStatus": rbAuFaultStatus,
       "rbAuIduTemperature": rbAuIduTemperature,
       "rbAuIduHwRevision": rbAuIduHwRevision,
       "rbAuOperSwFileName": rbAuOperSwFileName,
       "rbAuOperSwVersion": rbAuOperSwVersion,
       "rbAuShadowSwFileName": rbAuShadowSwFileName,
       "rbAuShadowSwVersion": rbAuShadowSwVersion,
       "rbAuRunningSoftware": rbAuRunningSoftware,
       "rbAuUnitControl": rbAuUnitControl,
       "rbAuOperVersionValidity": rbAuOperVersionValidity,
       "rbAuShadowVersionValidity": rbAuShadowVersionValidity,
       "rbAuSetDefaults": rbAuSetDefaults,
       "rbAuIduHwConfigDescription": rbAuIduHwConfigDescription,
       "rbAuOduHwConfigDescription": rbAuOduHwConfigDescription,
       "rbAuUpgradeSwFileName": rbAuUpgradeSwFileName,
       "rbAuOduHwRevision": rbAuOduHwRevision,
       "rbAuMaxNumberOfCalls": rbAuMaxNumberOfCalls,
       "rbAuNumberOfRegisteredSUs": rbAuNumberOfRegisteredSUs,
       "rbAuAirInterfaceType": rbAuAirInterfaceType,
       "rbAuCumulativePowerOnTime": rbAuCumulativePowerOnTime,
       "rbAuBeStarvationProtectLevelCurrent": rbAuBeStarvationProtectLevelCurrent,
       "rbAuBeStarvationProtectLevelConfig": rbAuBeStarvationProtectLevelConfig,
       "rbAuNrtStarvationProtectLevelCurrent": rbAuNrtStarvationProtectLevelCurrent,
       "rbAuNrtStarvationProtectLevelConfig": rbAuNrtStarvationProtectLevelConfig,
       "rbAuActiveVoiceCalls": rbAuActiveVoiceCalls,
       "rbAuSuUpgradeSwFileName": rbAuSuUpgradeSwFileName,
       "rbAuSuUpgradeSwAction": rbAuSuUpgradeSwAction,
       "rbAuClearAllSuSwUpgradeParams": rbAuClearAllSuSwUpgradeParams,
       "rbAuDiversityMode": rbAuDiversityMode,
       "rbAcuConfiguration": rbAcuConfiguration,
       "rbAcuOperStatus": rbAcuOperStatus,
       "rbAcuFaultStatus": rbAcuFaultStatus,
       "rbAcuLedStatus": rbAcuLedStatus,
       "rbPsuConfigTable": rbPsuConfigTable,
       "rbPsuConfigEntry": rbPsuConfigEntry,
       "rbPsuNumber": rbPsuNumber,
       "rbPsuStatus": rbPsuStatus,
       "rbPiuConfigTable": rbPiuConfigTable,
       "rbPiuConfigEntry": rbPiuConfigEntry,
       "rbPiuNumber": rbPiuNumber,
       "rbPiuStatus": rbPiuStatus,
       "rbPiuMode": rbPiuMode,
       "rbAuHwComponentsInfoTable": rbAuHwComponentsInfoTable,
       "rbAuHwComponentsInfoEntry": rbAuHwComponentsInfoEntry,
       "rbAuIduIfCardRevision": rbAuIduIfCardRevision,
       "rbAuIduIfCardConfiguration": rbAuIduIfCardConfiguration,
       "rbAuIduBootVersion": rbAuIduBootVersion,
       "rbAuOduHC08Version": rbAuOduHC08Version,
       "rbAuOduCpldVersion": rbAuOduCpldVersion,
       "rbAuOduCardSerialNumber": rbAuOduCardSerialNumber,
       "rbAuIduType": rbAuIduType,
       "rbChannelConfigTable": rbChannelConfigTable,
       "rbChannelConfigEntry": rbChannelConfigEntry,
       "rbChannelId": rbChannelId,
       "rbChannelAssociatedRadioClusterId": rbChannelAssociatedRadioClusterId,
       "rbChannelAssociatedOduId": rbChannelAssociatedOduId,
       "rbChannelTxFrequency": rbChannelTxFrequency,
       "rbChannelRxFrequency": rbChannelRxFrequency,
       "rbChannelAdminStatus": rbChannelAdminStatus,
       "rbChannelConfiguredTxFrequency": rbChannelConfiguredTxFrequency,
       "rbChannelOduActualFrequencyBand": rbChannelOduActualFrequencyBand,
       "rbChannelOperStatus": rbChannelOperStatus,
       "rbSubcriberUnitConfig": rbSubcriberUnitConfig,
       "rbRegisteredSuTable": rbRegisteredSuTable,
       "rbRegisteredSuEntry": rbRegisteredSuEntry,
       "rbAuId": rbAuId,
       "rbSuMacAddr": rbSuMacAddr,
       "rbSuID": rbSuID,
       "rbSuRegistrationState": rbSuRegistrationState,
       "rbSuPersistence": rbSuPersistence,
       "rbSuSerialNo": rbSuSerialNo,
       "rbSuSysName": rbSuSysName,
       "rbSuFaultStatus": rbSuFaultStatus,
       "rbSuHwRevision": rbSuHwRevision,
       "rbSuOperSwFileName": rbSuOperSwFileName,
       "rbSuOperSwVersion": rbSuOperSwVersion,
       "rbSuShadowSwFileName": rbSuShadowSwFileName,
       "rbSuShadowSwVersion": rbSuShadowSwVersion,
       "rbSuRunningSoftware": rbSuRunningSoftware,
       "rbSuOperVersionValidity": rbSuOperVersionValidity,
       "rbSuShadowVersionValidity": rbSuShadowVersionValidity,
       "rbSuUnitControl": rbSuUnitControl,
       "rbSuSetDefaults": rbSuSetDefaults,
       "rbSuAllowedUsersType": rbSuAllowedUsersType,
       "rbSuAllowedQoS": rbSuAllowedQoS,
       "rbSuAllowedService": rbSuAllowedService,
       "rbSuRowStatus": rbSuRowStatus,
       "rbSuInstallerPassword": rbSuInstallerPassword,
       "rbSuHwConfigDescription": rbSuHwConfigDescription,
       "rbSuUpgradeSwFileName": rbSuUpgradeSwFileName,
       "rbSuServiceType": rbSuServiceType,
       "rbSuIduType": rbSuIduType,
       "rbSuExternalDevNumber": rbSuExternalDevNumber,
       "rbSuServiceFaultBitMap": rbSuServiceFaultBitMap,
       "rbSuCumulativePowerOnTime": rbSuCumulativePowerOnTime,
       "rbSuOrganizationName": rbSuOrganizationName,
       "rbSuAddress": rbSuAddress,
       "rbSuCountry": rbSuCountry,
       "rbSuMACControlNumber": rbSuMACControlNumber,
       "rbSuAirInterfaceType": rbSuAirInterfaceType,
       "rbSuSubDevicesTable": rbSuSubDevicesTable,
       "rbSuSubDevicesEntry": rbSuSubDevicesEntry,
       "rbSubDeviceIpAddress": rbSubDeviceIpAddress,
       "rbSuMacAddress": rbSuMacAddress,
       "rbSubDeviceType": rbSubDeviceType,
       "rbSubDeviceVlanID": rbSubDeviceVlanID,
       "rbSuHwComponentsInfoTable": rbSuHwComponentsInfoTable,
       "rbSuHwComponentsInfoEntry": rbSuHwComponentsInfoEntry,
       "rbSuRfCardRevision": rbSuRfCardRevision,
       "rbSuRfCardConfiguration": rbSuRfCardConfiguration,
       "rbSuBootVersion": rbSuBootVersion,
       "rbSuType": rbSuType,
       "suBridgingParameters": suBridgingParameters,
       "rbSuSupportDevicesLimit": rbSuSupportDevicesLimit,
       "rbSuMaxNumberOfSupportedDevices": rbSuMaxNumberOfSupportedDevices,
       "rbSuBridgeAgingTime": rbSuBridgeAgingTime,
       "rbMACBehindSUList": rbMACBehindSUList,
       "rbMACBehindSUListTable": rbMACBehindSUListTable,
       "rbMACBehindSUListEntry": rbMACBehindSUListEntry,
       "rbMacBehindSuAddr": rbMacBehindSuAddr,
       "rbMacBehindSuVlan": rbMacBehindSuVlan,
       "rbSiSuInfo": rbSiSuInfo,
       "rbSiSuInfoTable": rbSiSuInfoTable,
       "rbSiSuInfoEntry": rbSiSuInfoEntry,
       "rbSiSuAntennaSelection": rbSiSuAntennaSelection,
       "rbSiSuSmartCardStatus": rbSiSuSmartCardStatus,
       "rbSiSuInterfaceType": rbSiSuInterfaceType,
       "rbSuLicenses": rbSuLicenses,
       "rbSuLicensesTable": rbSuLicensesTable,
       "rbSuLicensesEntry": rbSuLicensesEntry,
       "rbSuLicenseIdx": rbSuLicenseIdx,
       "rbSuLicenseId": rbSuLicenseId,
       "rbSuLicenseValue": rbSuLicenseValue,
       "rbAuthorizationAndTraps": rbAuthorizationAndTraps,
       "rbAuthorizedManagersTable": rbAuthorizedManagersTable,
       "rbAuthorizedManagersEntry": rbAuthorizedManagersEntry,
       "authMngrIpAddr": authMngrIpAddr,
       "authMngrReadCommunity": authMngrReadCommunity,
       "authMngrWriteCommunity": authMngrWriteCommunity,
       "authMngrTrapEnable": authMngrTrapEnable,
       "authMngrRowStatus": authMngrRowStatus,
       "rbTrapConfigTable": rbTrapConfigTable,
       "rbTrapConfigEntry": rbTrapConfigEntry,
       "trapEnterprizeId": trapEnterprizeId,
       "trapId": trapId,
       "trapEnable": trapEnable,
       "trapSeverity": trapSeverity,
       "trapSuppressionInterval": trapSuppressionInterval,
       "rbTrapGetActive": rbTrapGetActive,
       "rbTrapSeqNumber": rbTrapSeqNumber,
       "rbTrapSeverity": rbTrapSeverity,
       "rbTrapSource": rbTrapSource,
       "rbTrapAdditionalInfo": rbTrapAdditionalInfo,
       "rbTrapCategory": rbTrapCategory,
       "rbTrapMinSeverity": rbTrapMinSeverity,
       "rbTrapLedStatus": rbTrapLedStatus,
       "rbTrapIpAddress": rbTrapIpAddress,
       "rbTrapSetFailureReason": rbTrapSetFailureReason,
       "rbTrapRestoreDefaults": rbTrapRestoreDefaults,
       "rbTrapThresholdsTable": rbTrapThresholdsTable,
       "rbTrapThresholdsEntry": rbTrapThresholdsEntry,
       "counterId": counterId,
       "counterName": counterName,
       "counterType": counterType,
       "counterIntValue": counterIntValue,
       "counterStringValue": counterStringValue,
       "rbTrapEventLogTable": rbTrapEventLogTable,
       "rbTrapEventLogEntry": rbTrapEventLogEntry,
       "trapEventLogSeqNum": trapEventLogSeqNum,
       "trapEventLogId": trapEventLogId,
       "trapEventLogSeverity": trapEventLogSeverity,
       "trapEventLogType": trapEventLogType,
       "trapEventLogCategory": trapEventLogCategory,
       "trapEventLogSource": trapEventLogSource,
       "trapEventLogVarBindNumber": trapEventLogVarBindNumber,
       "trapEventLogVarBindSize": trapEventLogVarBindSize,
       "trapEventLogAddVarAttributes": trapEventLogAddVarAttributes,
       "trapEventLogDateAndTime": trapEventLogDateAndTime,
       "rbTrapAlarmLogTable": rbTrapAlarmLogTable,
       "rbTrapAlarmLogEntry": rbTrapAlarmLogEntry,
       "trapAlarmLogAlarmId": trapAlarmLogAlarmId,
       "trapAlarmLogSource": trapAlarmLogSource,
       "trapAlarmLogSlotId": trapAlarmLogSlotId,
       "trapAlarmLogEventId": trapAlarmLogEventId,
       "trapAlarmLogName": trapAlarmLogName,
       "trapAlarmLogSeverity": trapAlarmLogSeverity,
       "trapAlarmLogCategory": trapAlarmLogCategory,
       "trapAlarmLogStrOn": trapAlarmLogStrOn,
       "trapAlarmLogVarBindNumber": trapAlarmLogVarBindNumber,
       "trapAlarmLogVarBindSize": trapAlarmLogVarBindSize,
       "trapAlarmLogAddVarAttributes": trapAlarmLogAddVarAttributes,
       "trapAlarmLogLed": trapAlarmLogLed,
       "rbInterfaces": rbInterfaces,
       "rbEthernetInterface": rbEthernetInterface,
       "rbEthIfConfigTable": rbEthIfConfigTable,
       "rbEthIfConfigEntry": rbEthIfConfigEntry,
       "ethConfigIfIndex": ethConfigIfIndex,
       "ethConfigAutoNegotiation": ethConfigAutoNegotiation,
       "ethConfigLinkSpeedAndDuplex": ethConfigLinkSpeedAndDuplex,
       "ethConfigCurrentdAutoNegotiation": ethConfigCurrentdAutoNegotiation,
       "ethConfigCurrentLinkSpeedAndDuplex": ethConfigCurrentLinkSpeedAndDuplex,
       "rbAirInterface": rbAirInterface,
       "rbAuMacParameters": rbAuMacParameters,
       "rbAuBaseStationId": rbAuBaseStationId,
       "rbAuMaxCellRadius": rbAuMaxCellRadius,
       "rbAuConfiguredBaseStationId": rbAuConfiguredBaseStationId,
       "rbAuARQState": rbAuARQState,
       "rbAuConfiguredARQState": rbAuConfiguredARQState,
       "rbAuConfiguredSectorId": rbAuConfiguredSectorId,
       "rbAuCurrentMaxCellRadius": rbAuCurrentMaxCellRadius,
       "rbSuMacParameters": rbSuMacParameters,
       "rbSuBaseStationId": rbSuBaseStationId,
       "rbSuBaseStationIdMask": rbSuBaseStationIdMask,
       "rbSuConfiguredBaseStationId": rbSuConfiguredBaseStationId,
       "rbSuConfiguredBaseStationIdMask": rbSuConfiguredBaseStationIdMask,
       "rbAuMultirateParameters": rbAuMultirateParameters,
       "rbAuMultirateSupport": rbAuMultirateSupport,
       "rbAuUlBasicRate": rbAuUlBasicRate,
       "rbAuDlBasicRate": rbAuDlBasicRate,
       "rbAuUlMinNoOfSubChannels": rbAuUlMinNoOfSubChannels,
       "rbAuATPCParameters": rbAuATPCParameters,
       "rbAuATPCSupport": rbAuATPCSupport,
       "rbAuOptimalRSSI": rbAuOptimalRSSI,
       "rbSuMultirateParameters": rbSuMultirateParameters,
       "rbSuTxPower": rbSuTxPower,
       "rbSuUlSNR": rbSuUlSNR,
       "rbSuUlRSSI": rbSuUlRSSI,
       "rbSuUlCurrentRate": rbSuUlCurrentRate,
       "rbSuDlSNR": rbSuDlSNR,
       "rbSuDlRSSI": rbSuDlRSSI,
       "rbSuDlCurrentRate": rbSuDlCurrentRate,
       "rbSuMultirateSupport": rbSuMultirateSupport,
       "rbSuEstDistance": rbSuEstDistance,
       "rbSuUlSNRValue": rbSuUlSNRValue,
       "rbSuUlRSSIValue": rbSuUlRSSIValue,
       "rbSuDlSNRValue": rbSuDlSNRValue,
       "rbSuDlRSSIValue": rbSuDlRSSIValue,
       "rbSuATPCParameters": rbSuATPCParameters,
       "rbSuATPCSupport": rbSuATPCSupport,
       "rbAuPhyParameters": rbAuPhyParameters,
       "rbAuCurrentPhyBandwidth": rbAuCurrentPhyBandwidth,
       "rbAuPhyTxFrequencyChannel": rbAuPhyTxFrequencyChannel,
       "rbAuPhyTxConfiguredFrequencyChannel": rbAuPhyTxConfiguredFrequencyChannel,
       "rbAuConfiguredPhyBandwidth": rbAuConfiguredPhyBandwidth,
       "rbAuOutdoorConfigTable": rbAuOutdoorConfigTable,
       "rbAuOutdoorConfigEntry": rbAuOutdoorConfigEntry,
       "auOutdoorUnitIndex": auOutdoorUnitIndex,
       "auFrequencyBand": auFrequencyBand,
       "auTxPower": auTxPower,
       "rbSuPhyParameters": rbSuPhyParameters,
       "suPhyCurrentBandwidth": suPhyCurrentBandwidth,
       "suPhyCurrentTxFrequencyChannel": suPhyCurrentTxFrequencyChannel,
       "suPhyConfiguredBandwidth": suPhyConfiguredBandwidth,
       "suPhyConfiguredTxFrequencyChannel": suPhyConfiguredTxFrequencyChannel,
       "rbSuBestBstAuParams": rbSuBestBstAuParams,
       "rbSuBestBstAuParamsTable": rbSuBestBstAuParamsTable,
       "rbSuBestBstAuParamsEntry": rbSuBestBstAuParamsEntry,
       "rbSuCurrentBestBstAuSupport": rbSuCurrentBestBstAuSupport,
       "rbSuConfiguredBestBstAuSupport": rbSuConfiguredBestBstAuSupport,
       "rbSuCurrentPreferredBstAuId": rbSuCurrentPreferredBstAuId,
       "rbSuConfiguredPreferredBstAuId": rbSuConfiguredPreferredBstAuId,
       "rbSuCurrentPreferredBstAuMask": rbSuCurrentPreferredBstAuMask,
       "rbSuConfiguredPreferredBstAuMask": rbSuConfiguredPreferredBstAuMask,
       "rbSuSelectedBstAu": rbSuSelectedBstAu,
       "rbSuSelectedRxFrequency": rbSuSelectedRxFrequency,
       "rbSuSelectedTxFrequency": rbSuSelectedTxFrequency,
       "rbSuCurrentBstAuId": rbSuCurrentBstAuId,
       "rbSuConfiguredBstAuId": rbSuConfiguredBstAuId,
       "rbSuCurrentBstAuMask": rbSuCurrentBstAuMask,
       "rbSuConfiguredBstAuMask": rbSuConfiguredBstAuMask,
       "rbSuBestBstAuDataTable": rbSuBestBstAuDataTable,
       "rbSuBestBstAuDataEntry": rbSuBestBstAuDataEntry,
       "rbBstAuIndx": rbBstAuIndx,
       "rbBstAuId": rbBstAuId,
       "rbBstAuRxFrequency": rbBstAuRxFrequency,
       "rbBstAuSNR": rbBstAuSNR,
       "rbBstAuRxAntennaNumber": rbBstAuRxAntennaNumber,
       "rbSuRadioParameters": rbSuRadioParameters,
       "rbSuRadioParametersTable": rbSuRadioParametersTable,
       "rbSuRadioParametersEntry": rbSuRadioParametersEntry,
       "rbSuCurrentScanStartFreq": rbSuCurrentScanStartFreq,
       "rbSuConfiguredScanStartFreq": rbSuConfiguredScanStartFreq,
       "rbSuCurrentScanEndFreq": rbSuCurrentScanEndFreq,
       "rbSuConfiguredScanEndFreq": rbSuConfiguredScanEndFreq,
       "rbSuCurrentScanStep": rbSuCurrentScanStep,
       "rbSuConfiguredScanStep": rbSuConfiguredScanStep,
       "rbSuCurrentScanMask": rbSuCurrentScanMask,
       "rbSuConfiguredScanMask": rbSuConfiguredScanMask,
       "rbSuDiscreteF1": rbSuDiscreteF1,
       "rbSuDiscreteF2": rbSuDiscreteF2,
       "rbSuDiscreteF3": rbSuDiscreteF3,
       "rbSuDiscreteF4": rbSuDiscreteF4,
       "rbSuDiscreteF5": rbSuDiscreteF5,
       "rbSuDiscreteF6": rbSuDiscreteF6,
       "rbSuDiscreteF7": rbSuDiscreteF7,
       "rbSuDiscreteF8": rbSuDiscreteF8,
       "rbSuDiscreteF9": rbSuDiscreteF9,
       "rbSuDiscreteF10": rbSuDiscreteF10,
       "rbSuCurrentBandwidth": rbSuCurrentBandwidth,
       "rbSuConfiguredBandwidth": rbSuConfiguredBandwidth,
       "rbTesting": rbTesting,
       "rbBerTest": rbBerTest,
       "rbBerTestSetup": rbBerTestSetup,
       "rbBerTestDataSize": rbBerTestDataSize,
       "rbBerTestModulation": rbBerTestModulation,
       "rbBerTestAction": rbBerTestAction,
       "rbBerTestStatus": rbBerTestStatus,
       "rbBerTestSU": rbBerTestSU,
       "rbBerTestTrafficPriority": rbBerTestTrafficPriority,
       "rbBerTestMaxPacketSize": rbBerTestMaxPacketSize,
       "rbBerTestResults": rbBerTestResults,
       "rbBerTestULReceivedBits": rbBerTestULReceivedBits,
       "rbBerTestULReceivedErrorBits": rbBerTestULReceivedErrorBits,
       "rbBerTestDLReceivedBits": rbBerTestDLReceivedBits,
       "rbBerTestDLReceivedErrorBits": rbBerTestDLReceivedErrorBits,
       "rbBerTestDLMapLost": rbBerTestDLMapLost,
       "rbBerTestResultsSU": rbBerTestResultsSU,
       "rbBerTestUplinkBER": rbBerTestUplinkBER,
       "rbBerTestDownlinkBER": rbBerTestDownlinkBER,
       "rbIPConfig": rbIPConfig,
       "rbIpIfConfigTable": rbIpIfConfigTable,
       "rbIpIfConfigEntry": rbIpIfConfigEntry,
       "ipIfConfigIfIndex": ipIfConfigIfIndex,
       "ipIfConfigVlanId": ipIfConfigVlanId,
       "ipIfConfigIpAddress": ipIfConfigIpAddress,
       "ipIfConfigNetworkMask": ipIfConfigNetworkMask,
       "ipIfConfigDefaultGateway": ipIfConfigDefaultGateway,
       "ipIfStaticRouteSubnet": ipIfStaticRouteSubnet,
       "ipIfStaticRouteSubnetMask": ipIfStaticRouteSubnetMask,
       "rbSwUpgrade": rbSwUpgrade,
       "rbSwAuFiles": rbSwAuFiles,
       "rbSwSuFiles": rbSwSuFiles,
       "rbSwDeleteFiles": rbSwDeleteFiles,
       "rbSwSuDefaultFile": rbSwSuDefaultFile,
       "rbSwSuDefaultAction": rbSwSuDefaultAction,
       "rbSwUpgradeLogTable": rbSwUpgradeLogTable,
       "rbSwUpgradeLogEntry": rbSwUpgradeLogEntry,
       "rbSwDeviceType": rbSwDeviceType,
       "rbSwDeviceId": rbSwDeviceId,
       "rbSwUpgradeFileName": rbSwUpgradeFileName,
       "rbSwUpgradeAction": rbSwUpgradeAction,
       "rbSwUpgradeStartTime": rbSwUpgradeStartTime,
       "rbSwUpgradeEndTime": rbSwUpgradeEndTime,
       "rbSwUpgradeStatus": rbSwUpgradeStatus,
       "rbSwSuSiDefaultFile": rbSwSuSiDefaultFile,
       "rbSwSuSiDefaultAction": rbSwSuSiDefaultAction,
       "rbSwAuDefaultFile": rbSwAuDefaultFile,
       "rbSwAuDefaultAction": rbSwAuDefaultAction,
       "rbSwAuSiDefaultFile": rbSwAuSiDefaultFile,
       "rbSwAuSiDefaultAction": rbSwAuSiDefaultAction,
       "rbBstClearAllSuSwUpgradeParams": rbBstClearAllSuSwUpgradeParams,
       "rbBstClearAllAuSwUpgradeParams": rbBstClearAllAuSwUpgradeParams,
       "rbBaseStation": rbBaseStation,
       "rbBsAtpcParameters": rbBsAtpcParameters,
       "rbBsATPCSupport": rbBsATPCSupport,
       "rbBsOptimalRSSI": rbBsOptimalRSSI,
       "rbBsCellParameters": rbBsCellParameters,
       "rbBSConfiguredOperatorId": rbBSConfiguredOperatorId,
       "rbBSConfiguredCellId": rbBSConfiguredCellId,
       "rbBsRFModeParameters": rbBsRFModeParameters,
       "rbBsRFConfiguredDuplexMode": rbBsRFConfiguredDuplexMode,
       "rbBsRFCurrentDuplexMode": rbBsRFCurrentDuplexMode,
       "rbBsRFConfiguredDlUlRatio": rbBsRFConfiguredDlUlRatio,
       "rbBsRFCurrentDlUlRatio": rbBsRFCurrentDlUlRatio,
       "rbBSClockConfigParameters": rbBSClockConfigParameters,
       "rbBSConfiguredExternalPPSClock": rbBSConfiguredExternalPPSClock,
       "rbBSCurrentExternalPPSClock": rbBSCurrentExternalPPSClock,
       "rbBSConfiguredExternal16MhzClock": rbBSConfiguredExternal16MhzClock,
       "rbBSCurrentExternal16MhzClock": rbBSCurrentExternal16MhzClock,
       "rbRadioCluster": rbRadioCluster,
       "rbRadioClusterTable": rbRadioClusterTable,
       "rbRadioClusterEntry": rbRadioClusterEntry,
       "rbRadioClusterId": rbRadioClusterId,
       "rbRadioClusterName": rbRadioClusterName,
       "rbRadioClusterLocation": rbRadioClusterLocation,
       "rbRadioClusterSectorHeading": rbRadioClusterSectorHeading,
       "rbRadioClusterSectorBeamWidth": rbRadioClusterSectorBeamWidth,
       "rbRadioClusterRowStatus": rbRadioClusterRowStatus,
       "rbOduConfig": rbOduConfig,
       "rbOduConfigTable": rbOduConfigTable,
       "rbOduConfigEntry": rbOduConfigEntry,
       "rbOduConfigId": rbOduConfigId,
       "rbOduAssociatedRadioClusterId": rbOduAssociatedRadioClusterId,
       "rbOduTxPower": rbOduTxPower,
       "rbOduAdminStatus": rbOduAdminStatus,
       "rbOduTemperature": rbOduTemperature,
       "rbOduHwRevision": rbOduHwRevision,
       "rbOduHwConfigDescription": rbOduHwConfigDescription,
       "rbOduOperationalStatus": rbOduOperationalStatus,
       "rbOduHwHC08Version": rbOduHwHC08Version,
       "rbOduCpldVersion": rbOduCpldVersion,
       "rbOduCardSerialNumber": rbOduCardSerialNumber,
       "rbOduConfigFrequencyBand": rbOduConfigFrequencyBand,
       "rbOduRowStatus": rbOduRowStatus,
       "rbOduMaxTxPower": rbOduMaxTxPower,
       "rbChainConfig": rbChainConfig,
       "rbGPSSupported": rbGPSSupported,
       "rbConfiguredChainNumber": rbConfiguredChainNumber,
       "rbCurrentChainNumber": rbCurrentChainNumber,
       "rbGPSConfiguredType": rbGPSConfiguredType,
       "rbGPSCurrentType": rbGPSCurrentType,
       "rbTimeZoneOffsetFromUTC": rbTimeZoneOffsetFromUTC,
       "rbStopTxAfterHoldOverTimeout": rbStopTxAfterHoldOverTimeout,
       "rbHoldOverPassedTimeout": rbHoldOverPassedTimeout,
       "rbGPSInfo": rbGPSInfo,
       "rbGPSNumberOfRxSatellites": rbGPSNumberOfRxSatellites,
       "rbGPSLongitude": rbGPSLongitude,
       "rbGPSLatitude": rbGPSLatitude,
       "rbGPSAltitude": rbGPSAltitude,
       "rbGPSLocalDateAndTime": rbGPSLocalDateAndTime,
       "rbGPSNavigationProcessorSWVersion": rbGPSNavigationProcessorSWVersion,
       "rbGPSSignalProcessorSWVersion": rbGPSSignalProcessorSWVersion,
       "rbLicense": rbLicense,
       "rbLicenseBankTable": rbLicenseBankTable,
       "rbLicenseBankEntry": rbLicenseBankEntry,
       "rbLicenseId": rbLicenseId,
       "rbLicenseValue": rbLicenseValue,
       "rbLicenseCount": rbLicenseCount,
       "rbLicenseDescription": rbLicenseDescription,
       "rbLicenseBst": rbLicenseBst,
       "rbLicenseBstTable": rbLicenseBstTable,
       "rbLicenseBstEntry": rbLicenseBstEntry,
       "rbBstLicenseId": rbBstLicenseId,
       "rbBstLicenseValue": rbBstLicenseValue,
       "rbBstLicenseDescription": rbBstLicenseDescription,
       "rbNumberOfSUsGraceEndDate": rbNumberOfSUsGraceEndDate,
       "rbSUTempGracePeriodLicenseTable": rbSUTempGracePeriodLicenseTable,
       "rbSUTempGracePeriodLicenseEntry": rbSUTempGracePeriodLicenseEntry,
       "rbSUTempGracePeriodIndex": rbSUTempGracePeriodIndex,
       "rbSUTempGracePeriodSuMacAddr": rbSUTempGracePeriodSuMacAddr,
       "rbSUTempGracePeriodLicenseId": rbSUTempGracePeriodLicenseId,
       "rbSUTempGracePeriodLicenseEndDate": rbSUTempGracePeriodLicenseEndDate,
       "rbSUGracePeriodLicenseTable": rbSUGracePeriodLicenseTable,
       "rbSUGracePeriodLicenseEntry": rbSUGracePeriodLicenseEntry,
       "rbSUGracePeriodIndex": rbSUGracePeriodIndex,
       "rbSUGracePeriodSuMacAddr": rbSUGracePeriodSuMacAddr,
       "rbSUGracePeriodLicenseId": rbSUGracePeriodLicenseId,
       "rbSUGracePeriodLicenseEndDate": rbSUGracePeriodLicenseEndDate,
       "rbSUGracePeriodLicenseStatus": rbSUGracePeriodLicenseStatus,
       "endOfMib": endOfMib}
)
