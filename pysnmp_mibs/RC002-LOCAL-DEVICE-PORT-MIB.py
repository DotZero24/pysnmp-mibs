# SNMP MIB module (RC002-LOCAL-DEVICE-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RC002-LOCAL-DEVICE-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:04 2025
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

(rcftChassisIndex,
 rcftMibObjects,
 rcftSlotIndex,
 rcftSlotStat) = mibBuilder.importSymbols(
    "RAISECOM-RCFT-MIB",
    "rcftChassisIndex",
    "rcftMibObjects",
    "rcftSlotIndex",
    "rcftSlotStat")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rcftSlotPortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10)
)
if mibBuilder.loadTexts:
    rcftSlotPortMib.setRevisions(
        ("1909-01-19 00:00",
         "1909-03-17 00:00",
         "1909-05-14 00:00",
         "1909-05-15 00:00",
         "1909-05-19 00:00",
         "1909-05-26 00:00",
         "1909-05-27 16:00",
         "1909-06-09 16:00",
         "1909-06-17 16:00",
         "1909-07-02 16:00",
         "1909-07-17 16:00",
         "1909-08-28 00:00",
         "1909-09-09 00:00",
         "1909-09-18 00:00",
         "1909-09-27 00:00",
         "1909-10-30 09:48",
         "1909-12-21 14:18",
         "1909-12-21 00:00",
         "1912-01-10 14:31")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcftEthPortMib_ObjectIdentity = ObjectIdentity
rcftEthPortMib = _RcftEthPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1)
)
_RcftEthFxPortMib_ObjectIdentity = ObjectIdentity
rcftEthFxPortMib = _RcftEthFxPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1)
)
_RcftEthFxPortObjects_ObjectIdentity = ObjectIdentity
rcftEthFxPortObjects = _RcftEthFxPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1)
)
_RcftEthFxPortTable_Object = MibTable
rcftEthFxPortTable = _RcftEthFxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rcftEthFxPortTable.setStatus("current")
_RcftEthFxPortEntry_Object = MibTableRow
rcftEthFxPortEntry = _RcftEthFxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1)
)
rcftEthFxPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortIndex"),
)
if mibBuilder.loadTexts:
    rcftEthFxPortEntry.setStatus("current")
_RcftEthFxPortIndex_Type = Integer32
_RcftEthFxPortIndex_Object = MibTableColumn
rcftEthFxPortIndex = _RcftEthFxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 1),
    _RcftEthFxPortIndex_Type()
)
rcftEthFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortIndex.setStatus("current")
_RcftEthFxPortStatus_Type = Integer32
_RcftEthFxPortStatus_Object = MibTableColumn
rcftEthFxPortStatus = _RcftEthFxPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 2),
    _RcftEthFxPortStatus_Type()
)
rcftEthFxPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFxPortStatus.setStatus("current")


class _RcftEthFxPortModuleMaxSpeed_Type(Integer32):
    """Custom type rcftEthFxPortModuleMaxSpeed based on Integer32"""
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
        *(("stm16", 1),
          ("stm8", 2),
          ("stm4", 3),
          ("stm1", 4))
    )


_RcftEthFxPortModuleMaxSpeed_Type.__name__ = "Integer32"
_RcftEthFxPortModuleMaxSpeed_Object = MibTableColumn
rcftEthFxPortModuleMaxSpeed = _RcftEthFxPortModuleMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 3),
    _RcftEthFxPortModuleMaxSpeed_Type()
)
rcftEthFxPortModuleMaxSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortModuleMaxSpeed.setStatus("current")


class _RcftEthFxPortConnectorType_Type(Integer32):
    """Custom type rcftEthFxPortConnectorType based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("unkkown", 1),
          ("rj45", 2),
          ("sc", 3),
          ("style1", 4),
          ("style2", 5),
          ("bnctnc", 6),
          ("coaheader", 7),
          ("jack", 8),
          ("lc", 9),
          ("mtrj", 10),
          ("mu", 11),
          ("sg", 12),
          ("opticalpigtail", 13),
          ("hssdc2", 14),
          ("copperpigtail", 15))
    )


_RcftEthFxPortConnectorType_Type.__name__ = "Integer32"
_RcftEthFxPortConnectorType_Object = MibTableColumn
rcftEthFxPortConnectorType = _RcftEthFxPortConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 4),
    _RcftEthFxPortConnectorType_Type()
)
rcftEthFxPortConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortConnectorType.setStatus("current")


class _RcftEthFxPortTransmitMedia_Type(Integer32):
    """Custom type rcftEthFxPortTransmitMedia based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              15)
        )
    )
    namedValues = NamedValues(
        *(("unkkown", 1),
          ("singleMode9um", 2),
          ("multiMode50um", 3),
          ("multiMode62point5um", 4),
          ("copperline", 15))
    )


_RcftEthFxPortTransmitMedia_Type.__name__ = "Integer32"
_RcftEthFxPortTransmitMedia_Object = MibTableColumn
rcftEthFxPortTransmitMedia = _RcftEthFxPortTransmitMedia_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 5),
    _RcftEthFxPortTransmitMedia_Type()
)
rcftEthFxPortTransmitMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortTransmitMedia.setStatus("current")
_RcftEthFxPortModuleWaveLen_Type = Integer32
_RcftEthFxPortModuleWaveLen_Object = MibTableColumn
rcftEthFxPortModuleWaveLen = _RcftEthFxPortModuleWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 6),
    _RcftEthFxPortModuleWaveLen_Type()
)
rcftEthFxPortModuleWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortModuleWaveLen.setStatus("current")


class _RcftEthFxPortModuleManufacturer_Type(OctetString):
    """Custom type rcftEthFxPortModuleManufacturer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftEthFxPortModuleManufacturer_Type.__name__ = "OctetString"
_RcftEthFxPortModuleManufacturer_Object = MibTableColumn
rcftEthFxPortModuleManufacturer = _RcftEthFxPortModuleManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 7),
    _RcftEthFxPortModuleManufacturer_Type()
)
rcftEthFxPortModuleManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortModuleManufacturer.setStatus("current")


class _RcftEthFxPortModuleDescr_Type(OctetString):
    """Custom type rcftEthFxPortModuleDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftEthFxPortModuleDescr_Type.__name__ = "OctetString"
_RcftEthFxPortModuleDescr_Object = MibTableColumn
rcftEthFxPortModuleDescr = _RcftEthFxPortModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 8),
    _RcftEthFxPortModuleDescr_Type()
)
rcftEthFxPortModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortModuleDescr.setStatus("current")


class _RcftEthFxPortModuleVersion_Type(OctetString):
    """Custom type rcftEthFxPortModuleVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_RcftEthFxPortModuleVersion_Type.__name__ = "OctetString"
_RcftEthFxPortModuleVersion_Object = MibTableColumn
rcftEthFxPortModuleVersion = _RcftEthFxPortModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 9),
    _RcftEthFxPortModuleVersion_Type()
)
rcftEthFxPortModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortModuleVersion.setStatus("current")


class _RcftEthFxPortModuleSerialNumber_Type(OctetString):
    """Custom type rcftEthFxPortModuleSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_RcftEthFxPortModuleSerialNumber_Type.__name__ = "OctetString"
_RcftEthFxPortModuleSerialNumber_Object = MibTableColumn
rcftEthFxPortModuleSerialNumber = _RcftEthFxPortModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 10),
    _RcftEthFxPortModuleSerialNumber_Type()
)
rcftEthFxPortModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortModuleSerialNumber.setStatus("current")


class _RcftEthFxPortModuleType_Type(Integer32):
    """Custom type rcftEthFxPortModuleType based on Integer32"""
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
              12,
              15,
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS34", 9),
          ("optical-SS35", 10),
          ("optical-S15", 12),
          ("optical_SFP", 15),
          ("unknown-type", 100))
    )


_RcftEthFxPortModuleType_Type.__name__ = "Integer32"
_RcftEthFxPortModuleType_Object = MibTableColumn
rcftEthFxPortModuleType = _RcftEthFxPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 11),
    _RcftEthFxPortModuleType_Type()
)
rcftEthFxPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortModuleType.setStatus("current")
_RcftEthFxPortRxRestrictSpeed_Type = Integer32
_RcftEthFxPortRxRestrictSpeed_Object = MibTableColumn
rcftEthFxPortRxRestrictSpeed = _RcftEthFxPortRxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 12),
    _RcftEthFxPortRxRestrictSpeed_Type()
)
rcftEthFxPortRxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFxPortRxRestrictSpeed.setStatus("current")
_RcftEthFxPortTxRestrictSpeed_Type = Integer32
_RcftEthFxPortTxRestrictSpeed_Object = MibTableColumn
rcftEthFxPortTxRestrictSpeed = _RcftEthFxPortTxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 13),
    _RcftEthFxPortTxRestrictSpeed_Type()
)
rcftEthFxPortTxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFxPortTxRestrictSpeed.setStatus("current")
_RcftEthFxPortRestrictSpeedStep_Type = Integer32
_RcftEthFxPortRestrictSpeedStep_Object = MibTableColumn
rcftEthFxPortRestrictSpeedStep = _RcftEthFxPortRestrictSpeedStep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 14),
    _RcftEthFxPortRestrictSpeedStep_Type()
)
rcftEthFxPortRestrictSpeedStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortRestrictSpeedStep.setStatus("current")


class _RcftEthFxPortLoopOrder_Type(Integer32):
    """Custom type rcftEthFxPortLoopOrder based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethFxinsideLoopEnable", 1),
          ("ethFxinsideLoopDisable", 2),
          ("ethFxLoopbackTest", 3))
    )


_RcftEthFxPortLoopOrder_Type.__name__ = "Integer32"
_RcftEthFxPortLoopOrder_Object = MibTableColumn
rcftEthFxPortLoopOrder = _RcftEthFxPortLoopOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 15),
    _RcftEthFxPortLoopOrder_Type()
)
rcftEthFxPortLoopOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFxPortLoopOrder.setStatus("current")


class _RcftEthFxPortLoopStatus_Type(Integer32):
    """Custom type rcftEthFxPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              100)
        )
    )
    namedValues = NamedValues(
        *(("ethFxPortoutsideLoop", 1),
          ("ethFxPortnormal", 100))
    )


_RcftEthFxPortLoopStatus_Type.__name__ = "Integer32"
_RcftEthFxPortLoopStatus_Object = MibTableColumn
rcftEthFxPortLoopStatus = _RcftEthFxPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 16),
    _RcftEthFxPortLoopStatus_Type()
)
rcftEthFxPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortLoopStatus.setStatus("current")
_RcftEthFxPortSFPDiagnoInfo_Type = Integer32
_RcftEthFxPortSFPDiagnoInfo_Object = MibTableColumn
rcftEthFxPortSFPDiagnoInfo = _RcftEthFxPortSFPDiagnoInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 17),
    _RcftEthFxPortSFPDiagnoInfo_Type()
)
rcftEthFxPortSFPDiagnoInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortSFPDiagnoInfo.setStatus("current")
_RcftEthFxPortSFPDiagnoAlarmStatus_Type = Integer32
_RcftEthFxPortSFPDiagnoAlarmStatus_Object = MibTableColumn
rcftEthFxPortSFPDiagnoAlarmStatus = _RcftEthFxPortSFPDiagnoAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 18),
    _RcftEthFxPortSFPDiagnoAlarmStatus_Type()
)
rcftEthFxPortSFPDiagnoAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortSFPDiagnoAlarmStatus.setStatus("current")
_RcftEthFxPortSFPDiagnoWarningStatus_Type = Integer32
_RcftEthFxPortSFPDiagnoWarningStatus_Object = MibTableColumn
rcftEthFxPortSFPDiagnoWarningStatus = _RcftEthFxPortSFPDiagnoWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 19),
    _RcftEthFxPortSFPDiagnoWarningStatus_Type()
)
rcftEthFxPortSFPDiagnoWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortSFPDiagnoWarningStatus.setStatus("current")
_RcftEthFxPortTranDistance_Type = Integer32
_RcftEthFxPortTranDistance_Object = MibTableColumn
rcftEthFxPortTranDistance = _RcftEthFxPortTranDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 20),
    _RcftEthFxPortTranDistance_Type()
)
rcftEthFxPortTranDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortTranDistance.setStatus("current")


class _RcftEthFxPortSFPType_Type(Integer32):
    """Custom type rcftEthFxPortSFPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("utp", 1),
          ("fiber", 2))
    )


_RcftEthFxPortSFPType_Type.__name__ = "Integer32"
_RcftEthFxPortSFPType_Object = MibTableColumn
rcftEthFxPortSFPType = _RcftEthFxPortSFPType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 21),
    _RcftEthFxPortSFPType_Type()
)
rcftEthFxPortSFPType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortSFPType.setStatus("current")
_RcftEthFxPortSFPInfo_Type = Integer32
_RcftEthFxPortSFPInfo_Object = MibTableColumn
rcftEthFxPortSFPInfo = _RcftEthFxPortSFPInfo_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 22),
    _RcftEthFxPortSFPInfo_Type()
)
rcftEthFxPortSFPInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxPortSFPInfo.setStatus("current")
_RcftEthFxPortPVID_Type = Integer32
_RcftEthFxPortPVID_Object = MibTableColumn
rcftEthFxPortPVID = _RcftEthFxPortPVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 23),
    _RcftEthFxPortPVID_Type()
)
rcftEthFxPortPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFxPortPVID.setStatus("current")
_RcftEthFxPorttag_Type = Integer32
_RcftEthFxPorttag_Object = MibTableColumn
rcftEthFxPorttag = _RcftEthFxPorttag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 24),
    _RcftEthFxPorttag_Type()
)
rcftEthFxPorttag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFxPorttag.setStatus("current")
_RcftEthFxPortCOS_Type = Integer32
_RcftEthFxPortCOS_Object = MibTableColumn
rcftEthFxPortCOS = _RcftEthFxPortCOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 1, 1, 1, 25),
    _RcftEthFxPortCOS_Type()
)
rcftEthFxPortCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFxPortCOS.setStatus("current")
_RcftEthFxPortPerformance_ObjectIdentity = ObjectIdentity
rcftEthFxPortPerformance = _RcftEthFxPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2)
)
_RcftEthFxStatisticTable_Object = MibTable
rcftEthFxStatisticTable = _RcftEthFxStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    rcftEthFxStatisticTable.setStatus("current")
_RcftEthFxStatisticEntry_Object = MibTableRow
rcftEthFxStatisticEntry = _RcftEthFxStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftEthFxStatisticEntry.setStatus("current")
_RcftEthFxTxPackets_Type = Counter32
_RcftEthFxTxPackets_Object = MibTableColumn
rcftEthFxTxPackets = _RcftEthFxTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 1),
    _RcftEthFxTxPackets_Type()
)
rcftEthFxTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxTxPackets.setStatus("current")
_RcftEthFxRxPackets_Type = Counter32
_RcftEthFxRxPackets_Object = MibTableColumn
rcftEthFxRxPackets = _RcftEthFxRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 2),
    _RcftEthFxRxPackets_Type()
)
rcftEthFxRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxRxPackets.setStatus("current")
_RcftEthFxTxErrPackets_Type = Counter32
_RcftEthFxTxErrPackets_Object = MibTableColumn
rcftEthFxTxErrPackets = _RcftEthFxTxErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 3),
    _RcftEthFxTxErrPackets_Type()
)
rcftEthFxTxErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxTxErrPackets.setStatus("current")
_RcftEthFxRxErrPackets_Type = Counter32
_RcftEthFxRxErrPackets_Object = MibTableColumn
rcftEthFxRxErrPackets = _RcftEthFxRxErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 4),
    _RcftEthFxRxErrPackets_Type()
)
rcftEthFxRxErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxRxErrPackets.setStatus("current")
_RcftEthFxFluxTimer_Type = Counter32
_RcftEthFxFluxTimer_Object = MibTableColumn
rcftEthFxFluxTimer = _RcftEthFxFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 5),
    _RcftEthFxFluxTimer_Type()
)
rcftEthFxFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxFluxTimer.setStatus("current")
_RcftEthFxRxBytes_Type = Counter32
_RcftEthFxRxBytes_Object = MibTableColumn
rcftEthFxRxBytes = _RcftEthFxRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 6),
    _RcftEthFxRxBytes_Type()
)
rcftEthFxRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxRxBytes.setStatus("current")
_RcftEthFxTxBytes_Type = Counter32
_RcftEthFxTxBytes_Object = MibTableColumn
rcftEthFxTxBytes = _RcftEthFxTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 7),
    _RcftEthFxTxBytes_Type()
)
rcftEthFxTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFxTxBytes.setStatus("current")
_RcftEthFx64RxBytes_Type = Counter64
_RcftEthFx64RxBytes_Object = MibTableColumn
rcftEthFx64RxBytes = _RcftEthFx64RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 8),
    _RcftEthFx64RxBytes_Type()
)
rcftEthFx64RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFx64RxBytes.setStatus("current")
_RcftEthFx64TxBytes_Type = Counter64
_RcftEthFx64TxBytes_Object = MibTableColumn
rcftEthFx64TxBytes = _RcftEthFx64TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 2, 1, 1, 9),
    _RcftEthFx64TxBytes_Type()
)
rcftEthFx64TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFx64TxBytes.setStatus("current")
_RcftEthFxPortTraps_ObjectIdentity = ObjectIdentity
rcftEthFxPortTraps = _RcftEthFxPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10)
)
_RcftEthFePortMib_ObjectIdentity = ObjectIdentity
rcftEthFePortMib = _RcftEthFePortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2)
)
_RcftEthFePortObjects_ObjectIdentity = ObjectIdentity
rcftEthFePortObjects = _RcftEthFePortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1)
)
_RcftEthFePortTable_Object = MibTable
rcftEthFePortTable = _RcftEthFePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftEthFePortTable.setStatus("current")
_RcftEthFePortEntry_Object = MibTableRow
rcftEthFePortEntry = _RcftEthFePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1)
)
rcftEthFePortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFePortIndex"),
)
if mibBuilder.loadTexts:
    rcftEthFePortEntry.setStatus("current")
_RcftEthFePortIndex_Type = Integer32
_RcftEthFePortIndex_Object = MibTableColumn
rcftEthFePortIndex = _RcftEthFePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 1),
    _RcftEthFePortIndex_Type()
)
rcftEthFePortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFePortIndex.setStatus("current")
_RcftEthFePortStatus_Type = Integer32
_RcftEthFePortStatus_Object = MibTableColumn
rcftEthFePortStatus = _RcftEthFePortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 2),
    _RcftEthFePortStatus_Type()
)
rcftEthFePortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFePortStatus.setStatus("current")
_RcftEthFePortRxRestrictSpeed_Type = Integer32
_RcftEthFePortRxRestrictSpeed_Object = MibTableColumn
rcftEthFePortRxRestrictSpeed = _RcftEthFePortRxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 3),
    _RcftEthFePortRxRestrictSpeed_Type()
)
rcftEthFePortRxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFePortRxRestrictSpeed.setStatus("current")
_RcftEthFePortTxRestrictSpeed_Type = Integer32
_RcftEthFePortTxRestrictSpeed_Object = MibTableColumn
rcftEthFePortTxRestrictSpeed = _RcftEthFePortTxRestrictSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 4),
    _RcftEthFePortTxRestrictSpeed_Type()
)
rcftEthFePortTxRestrictSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFePortTxRestrictSpeed.setStatus("current")
_RcftEthFePortRestrictSpeedStep_Type = Integer32
_RcftEthFePortRestrictSpeedStep_Object = MibTableColumn
rcftEthFePortRestrictSpeedStep = _RcftEthFePortRestrictSpeedStep_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 5),
    _RcftEthFePortRestrictSpeedStep_Type()
)
rcftEthFePortRestrictSpeedStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFePortRestrictSpeedStep.setStatus("current")
_RcftEthFePortOrder_Type = Integer32
_RcftEthFePortOrder_Object = MibTableColumn
rcftEthFePortOrder = _RcftEthFePortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 6),
    _RcftEthFePortOrder_Type()
)
rcftEthFePortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFePortOrder.setStatus("current")
_RcftEthFePortPosition_Type = Integer32
_RcftEthFePortPosition_Object = MibTableColumn
rcftEthFePortPosition = _RcftEthFePortPosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 7),
    _RcftEthFePortPosition_Type()
)
rcftEthFePortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFePortPosition.setStatus("current")
_RcftEthFePortPVID_Type = Integer32
_RcftEthFePortPVID_Object = MibTableColumn
rcftEthFePortPVID = _RcftEthFePortPVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 8),
    _RcftEthFePortPVID_Type()
)
rcftEthFePortPVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFePortPVID.setStatus("current")
_RcftEthFePorttag_Type = Integer32
_RcftEthFePorttag_Object = MibTableColumn
rcftEthFePorttag = _RcftEthFePorttag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 9),
    _RcftEthFePorttag_Type()
)
rcftEthFePorttag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFePorttag.setStatus("current")
_RcftEthFePortCOS_Type = Integer32
_RcftEthFePortCOS_Object = MibTableColumn
rcftEthFePortCOS = _RcftEthFePortCOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 1, 1, 1, 10),
    _RcftEthFePortCOS_Type()
)
rcftEthFePortCOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftEthFePortCOS.setStatus("current")
_RcftEthFePortPerformance_ObjectIdentity = ObjectIdentity
rcftEthFePortPerformance = _RcftEthFePortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2)
)
_RcftEthFeStatisticTable_Object = MibTable
rcftEthFeStatisticTable = _RcftEthFeStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rcftEthFeStatisticTable.setStatus("current")
_RcftEthFeStatisticEntry_Object = MibTableRow
rcftEthFeStatisticEntry = _RcftEthFeStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftEthFeStatisticEntry.setStatus("current")
_RcftEthFeTxPackets_Type = Counter32
_RcftEthFeTxPackets_Object = MibTableColumn
rcftEthFeTxPackets = _RcftEthFeTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1, 1),
    _RcftEthFeTxPackets_Type()
)
rcftEthFeTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFeTxPackets.setStatus("current")
_RcftEthFeTxBytes_Type = Counter32
_RcftEthFeTxBytes_Object = MibTableColumn
rcftEthFeTxBytes = _RcftEthFeTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1, 2),
    _RcftEthFeTxBytes_Type()
)
rcftEthFeTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFeTxBytes.setStatus("current")
_RcftEthFeTxFailurePackets_Type = Counter32
_RcftEthFeTxFailurePackets_Object = MibTableColumn
rcftEthFeTxFailurePackets = _RcftEthFeTxFailurePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1, 3),
    _RcftEthFeTxFailurePackets_Type()
)
rcftEthFeTxFailurePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFeTxFailurePackets.setStatus("current")
_RcftEthFeRxPackets_Type = Counter32
_RcftEthFeRxPackets_Object = MibTableColumn
rcftEthFeRxPackets = _RcftEthFeRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1, 4),
    _RcftEthFeRxPackets_Type()
)
rcftEthFeRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFeRxPackets.setStatus("current")
_RcftEthFeRxBytes_Type = Counter32
_RcftEthFeRxBytes_Object = MibTableColumn
rcftEthFeRxBytes = _RcftEthFeRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1, 5),
    _RcftEthFeRxBytes_Type()
)
rcftEthFeRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFeRxBytes.setStatus("current")
_RcftEthFeRxErrorPackets_Type = Counter32
_RcftEthFeRxErrorPackets_Object = MibTableColumn
rcftEthFeRxErrorPackets = _RcftEthFeRxErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1, 6),
    _RcftEthFeRxErrorPackets_Type()
)
rcftEthFeRxErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFeRxErrorPackets.setStatus("current")
_RcftEthFeFluxTimer_Type = Counter32
_RcftEthFeFluxTimer_Object = MibTableColumn
rcftEthFeFluxTimer = _RcftEthFeFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 2, 1, 1, 7),
    _RcftEthFeFluxTimer_Type()
)
rcftEthFeFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftEthFeFluxTimer.setStatus("current")
_RcftEthFePortTraps_ObjectIdentity = ObjectIdentity
rcftEthFePortTraps = _RcftEthFePortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 10)
)
_RcftPdhPortMib_ObjectIdentity = ObjectIdentity
rcftPdhPortMib = _RcftPdhPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2)
)
_RcftPdhPortObjects_ObjectIdentity = ObjectIdentity
rcftPdhPortObjects = _RcftPdhPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1)
)
_RcftPdhPortTable_Object = MibTable
rcftPdhPortTable = _RcftPdhPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftPdhPortTable.setStatus("current")
_RcftPdhPortEntry_Object = MibTableRow
rcftPdhPortEntry = _RcftPdhPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1)
)
rcftPdhPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortIndex"),
)
if mibBuilder.loadTexts:
    rcftPdhPortEntry.setStatus("current")
_RcftPdhPortIndex_Type = Integer32
_RcftPdhPortIndex_Object = MibTableColumn
rcftPdhPortIndex = _RcftPdhPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 1),
    _RcftPdhPortIndex_Type()
)
rcftPdhPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortIndex.setStatus("current")
_RcftPdhPortAlarmStatus_Type = Integer32
_RcftPdhPortAlarmStatus_Object = MibTableColumn
rcftPdhPortAlarmStatus = _RcftPdhPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 2),
    _RcftPdhPortAlarmStatus_Type()
)
rcftPdhPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortAlarmStatus.setStatus("current")
_RcftPdhPortStatus_Type = Integer32
_RcftPdhPortStatus_Object = MibTableColumn
rcftPdhPortStatus = _RcftPdhPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 3),
    _RcftPdhPortStatus_Type()
)
rcftPdhPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftPdhPortStatus.setStatus("current")
_RcftPdhPortECSCnt_Type = Integer32
_RcftPdhPortECSCnt_Object = MibTableColumn
rcftPdhPortECSCnt = _RcftPdhPortECSCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 4),
    _RcftPdhPortECSCnt_Type()
)
rcftPdhPortECSCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortECSCnt.setStatus("current")
_RcftPdhPortSECSCnt_Type = Integer32
_RcftPdhPortSECSCnt_Object = MibTableColumn
rcftPdhPortSECSCnt = _RcftPdhPortSECSCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 5),
    _RcftPdhPortSECSCnt_Type()
)
rcftPdhPortSECSCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortSECSCnt.setStatus("current")


class _RcftPdhPortModuleType_Type(Integer32):
    """Custom type rcftPdhPortModuleType based on Integer32"""
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
              12,
              15,
              23,
              50,
              51,
              52,
              53,
              100)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS34", 9),
          ("optical-SS35", 10),
          ("optical-S15", 12),
          ("optical-SFP", 15),
          ("optical-SS24", 23),
          ("optical-S1FC", 50),
          ("optical-S1A", 51),
          ("optical-S2A", 52),
          ("optical-S3A", 53),
          ("unknown-type", 100))
    )


_RcftPdhPortModuleType_Type.__name__ = "Integer32"
_RcftPdhPortModuleType_Object = MibTableColumn
rcftPdhPortModuleType = _RcftPdhPortModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 6),
    _RcftPdhPortModuleType_Type()
)
rcftPdhPortModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortModuleType.setStatus("current")
_RcftPdhPortLoopStatus_Type = Integer32
_RcftPdhPortLoopStatus_Object = MibTableColumn
rcftPdhPortLoopStatus = _RcftPdhPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 7),
    _RcftPdhPortLoopStatus_Type()
)
rcftPdhPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortLoopStatus.setStatus("current")
_RcftPdhPortOrder_Type = Integer32
_RcftPdhPortOrder_Object = MibTableColumn
rcftPdhPortOrder = _RcftPdhPortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 8),
    _RcftPdhPortOrder_Type()
)
rcftPdhPortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftPdhPortOrder.setStatus("current")
_RcftPdhPortBertStatus_Type = Integer32
_RcftPdhPortBertStatus_Object = MibTableColumn
rcftPdhPortBertStatus = _RcftPdhPortBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 9),
    _RcftPdhPortBertStatus_Type()
)
rcftPdhPortBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortBertStatus.setStatus("current")
_RcftPdhPortBertErrCode_Type = Unsigned32
_RcftPdhPortBertErrCode_Object = MibTableColumn
rcftPdhPortBertErrCode = _RcftPdhPortBertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 1, 1, 1, 10),
    _RcftPdhPortBertErrCode_Type()
)
rcftPdhPortBertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPdhPortBertErrCode.setStatus("current")
_RcftPdhPortPerformance_ObjectIdentity = ObjectIdentity
rcftPdhPortPerformance = _RcftPdhPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 2)
)
_RcftPdhPortTraps_ObjectIdentity = ObjectIdentity
rcftPdhPortTraps = _RcftPdhPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10)
)
_RcftE1PortMib_ObjectIdentity = ObjectIdentity
rcftE1PortMib = _RcftE1PortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3)
)
_RcftE1PortObjects_ObjectIdentity = ObjectIdentity
rcftE1PortObjects = _RcftE1PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1)
)
_RcftE1PortTable_Object = MibTable
rcftE1PortTable = _RcftE1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1)
)
if mibBuilder.loadTexts:
    rcftE1PortTable.setStatus("current")
_RcftE1PortEntry_Object = MibTableRow
rcftE1PortEntry = _RcftE1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1)
)
rcftE1PortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortIndex"),
)
if mibBuilder.loadTexts:
    rcftE1PortEntry.setStatus("current")
_RcftE1PortIndex_Type = Integer32
_RcftE1PortIndex_Object = MibTableColumn
rcftE1PortIndex = _RcftE1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 1),
    _RcftE1PortIndex_Type()
)
rcftE1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortIndex.setStatus("current")
_RcftE1PortAlarmStatus_Type = Integer32
_RcftE1PortAlarmStatus_Object = MibTableColumn
rcftE1PortAlarmStatus = _RcftE1PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 2),
    _RcftE1PortAlarmStatus_Type()
)
rcftE1PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortAlarmStatus.setStatus("current")
_RcftE1PortStatus_Type = Integer32
_RcftE1PortStatus_Object = MibTableColumn
rcftE1PortStatus = _RcftE1PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 3),
    _RcftE1PortStatus_Type()
)
rcftE1PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1PortStatus.setStatus("current")
_RcftE1TimeSlots_Type = Integer32
_RcftE1TimeSlots_Object = MibTableColumn
rcftE1TimeSlots = _RcftE1TimeSlots_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 4),
    _RcftE1TimeSlots_Type()
)
rcftE1TimeSlots.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1TimeSlots.setStatus("current")
_RcftE1TS0Mode_Type = Integer32
_RcftE1TS0Mode_Object = MibTableColumn
rcftE1TS0Mode = _RcftE1TS0Mode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 5),
    _RcftE1TS0Mode_Type()
)
rcftE1TS0Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1TS0Mode.setStatus("current")
_RcftE1IdleCode_Type = Integer32
_RcftE1IdleCode_Object = MibTableColumn
rcftE1IdleCode = _RcftE1IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 6),
    _RcftE1IdleCode_Type()
)
rcftE1IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1IdleCode.setStatus("current")


class _RcftE1LoopStatus_Type(Integer32):
    """Custom type rcftE1LoopStatus based on Integer32"""
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
        *(("localDoubleLoopEnable", 1),
          ("localDoubleLoopDisable", 2),
          ("remoteDoubleLoopEnable", 3),
          ("remoteDoubleLoopDisable", 4))
    )


_RcftE1LoopStatus_Type.__name__ = "Integer32"
_RcftE1LoopStatus_Object = MibTableColumn
rcftE1LoopStatus = _RcftE1LoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 7),
    _RcftE1LoopStatus_Type()
)
rcftE1LoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1LoopStatus.setStatus("current")
_RcftE1Order_Type = Integer32
_RcftE1Order_Object = MibTableColumn
rcftE1Order = _RcftE1Order_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 8),
    _RcftE1Order_Type()
)
rcftE1Order.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1Order.setStatus("current")
_RcftE1PortType_Type = Integer32
_RcftE1PortType_Object = MibTableColumn
rcftE1PortType = _RcftE1PortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 9),
    _RcftE1PortType_Type()
)
rcftE1PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortType.setStatus("current")
_RcftE1BertStatus_Type = Integer32
_RcftE1BertStatus_Object = MibTableColumn
rcftE1BertStatus = _RcftE1BertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 10),
    _RcftE1BertStatus_Type()
)
rcftE1BertStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1BertStatus.setStatus("current")
_RcftE1BertTime_Type = Unsigned32
_RcftE1BertTime_Object = MibTableColumn
rcftE1BertTime = _RcftE1BertTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 11),
    _RcftE1BertTime_Type()
)
rcftE1BertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1BertTime.setStatus("current")
_RcftE1BertErrCode_Type = Unsigned32
_RcftE1BertErrCode_Object = MibTableColumn
rcftE1BertErrCode = _RcftE1BertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 12),
    _RcftE1BertErrCode_Type()
)
rcftE1BertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1BertErrCode.setStatus("current")
_RcftE1BertUnusedTime_Type = Unsigned32
_RcftE1BertUnusedTime_Object = MibTableColumn
rcftE1BertUnusedTime = _RcftE1BertUnusedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 13),
    _RcftE1BertUnusedTime_Type()
)
rcftE1BertUnusedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1BertUnusedTime.setStatus("current")
_RcftE1BertPortSpeed_Type = Unsigned32
_RcftE1BertPortSpeed_Object = MibTableColumn
rcftE1BertPortSpeed = _RcftE1BertPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 14),
    _RcftE1BertPortSpeed_Type()
)
rcftE1BertPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1BertPortSpeed.setStatus("current")
_RcftE1BertCodeType_Type = Integer32
_RcftE1BertCodeType_Object = MibTableColumn
rcftE1BertCodeType = _RcftE1BertCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 15),
    _RcftE1BertCodeType_Type()
)
rcftE1BertCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1BertCodeType.setStatus("current")
_RcftE1BertCodeNum_Type = Integer32
_RcftE1BertCodeNum_Object = MibTableColumn
rcftE1BertCodeNum = _RcftE1BertCodeNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 16),
    _RcftE1BertCodeNum_Type()
)
rcftE1BertCodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftE1BertCodeNum.setStatus("current")
_RcftE1AlarmRejest_Type = Integer32
_RcftE1AlarmRejest_Object = MibTableColumn
rcftE1AlarmRejest = _RcftE1AlarmRejest_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 17),
    _RcftE1AlarmRejest_Type()
)
rcftE1AlarmRejest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1AlarmRejest.setStatus("current")
_RcfT1PortAlarmStatus_Type = Integer32
_RcfT1PortAlarmStatus_Object = MibTableColumn
rcfT1PortAlarmStatus = _RcfT1PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 18),
    _RcfT1PortAlarmStatus_Type()
)
rcfT1PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcfT1PortAlarmStatus.setStatus("current")
_RcftE1PortVCGNumber_Type = Integer32
_RcftE1PortVCGNumber_Object = MibTableColumn
rcftE1PortVCGNumber = _RcftE1PortVCGNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 19),
    _RcftE1PortVCGNumber_Type()
)
rcftE1PortVCGNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortVCGNumber.setStatus("current")
_RcftE1PortErrorRate_Type = Integer32
_RcftE1PortErrorRate_Object = MibTableColumn
rcftE1PortErrorRate = _RcftE1PortErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 20),
    _RcftE1PortErrorRate_Type()
)
rcftE1PortErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortErrorRate.setStatus("current")
_RcftE1PortESCont_Type = Integer32
_RcftE1PortESCont_Object = MibTableColumn
rcftE1PortESCont = _RcftE1PortESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 21),
    _RcftE1PortESCont_Type()
)
rcftE1PortESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortESCont.setStatus("current")
_RcftE1PortSESCont_Type = Integer32
_RcftE1PortSESCont_Object = MibTableColumn
rcftE1PortSESCont = _RcftE1PortSESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 22),
    _RcftE1PortSESCont_Type()
)
rcftE1PortSESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortSESCont.setStatus("current")
_RcftE1PortToRNumber_Type = Integer32
_RcftE1PortToRNumber_Object = MibTableColumn
rcftE1PortToRNumber = _RcftE1PortToRNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 23),
    _RcftE1PortToRNumber_Type()
)
rcftE1PortToRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1PortToRNumber.setStatus("current")
_RcftE1CVCnt_Type = Integer32
_RcftE1CVCnt_Object = MibTableColumn
rcftE1CVCnt = _RcftE1CVCnt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 1, 1, 1, 24),
    _RcftE1CVCnt_Type()
)
rcftE1CVCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftE1CVCnt.setStatus("current")
_RcftE1PortPerformance_ObjectIdentity = ObjectIdentity
rcftE1PortPerformance = _RcftE1PortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 2)
)
_RcftE1PortTraps_ObjectIdentity = ObjectIdentity
rcftE1PortTraps = _RcftE1PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10)
)
_RcftV35PortMib_ObjectIdentity = ObjectIdentity
rcftV35PortMib = _RcftV35PortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4)
)
_RcftV35PortObjects_ObjectIdentity = ObjectIdentity
rcftV35PortObjects = _RcftV35PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1)
)
_RcftV35PortTable_Object = MibTable
rcftV35PortTable = _RcftV35PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rcftV35PortTable.setStatus("current")
_RcftV35PortEntry_Object = MibTableRow
rcftV35PortEntry = _RcftV35PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1)
)
rcftV35PortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortIndex"),
)
if mibBuilder.loadTexts:
    rcftV35PortEntry.setStatus("current")
_RcftV35PortIndex_Type = Integer32
_RcftV35PortIndex_Object = MibTableColumn
rcftV35PortIndex = _RcftV35PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 1),
    _RcftV35PortIndex_Type()
)
rcftV35PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortIndex.setStatus("current")
_RcftV35PortAlarmStatus_Type = Integer32
_RcftV35PortAlarmStatus_Object = MibTableColumn
rcftV35PortAlarmStatus = _RcftV35PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 2),
    _RcftV35PortAlarmStatus_Type()
)
rcftV35PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortAlarmStatus.setStatus("current")
_RcftV35PortStatus_Type = Integer32
_RcftV35PortStatus_Object = MibTableColumn
rcftV35PortStatus = _RcftV35PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 3),
    _RcftV35PortStatus_Type()
)
rcftV35PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftV35PortStatus.setStatus("current")
_RcftV35PortSpeed_Type = Unsigned32
_RcftV35PortSpeed_Object = MibTableColumn
rcftV35PortSpeed = _RcftV35PortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 4),
    _RcftV35PortSpeed_Type()
)
rcftV35PortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftV35PortSpeed.setStatus("current")
_RcftV35PortBertStatus_Type = Integer32
_RcftV35PortBertStatus_Object = MibTableColumn
rcftV35PortBertStatus = _RcftV35PortBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 5),
    _RcftV35PortBertStatus_Type()
)
rcftV35PortBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortBertStatus.setStatus("current")
_RcftV35PortBertTime_Type = Unsigned32
_RcftV35PortBertTime_Object = MibTableColumn
rcftV35PortBertTime = _RcftV35PortBertTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 6),
    _RcftV35PortBertTime_Type()
)
rcftV35PortBertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortBertTime.setStatus("current")
_RcftV35PortBertErrCode_Type = Unsigned32
_RcftV35PortBertErrCode_Object = MibTableColumn
rcftV35PortBertErrCode = _RcftV35PortBertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 7),
    _RcftV35PortBertErrCode_Type()
)
rcftV35PortBertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortBertErrCode.setStatus("current")
_RcftV35PortBertUnusedTime_Type = Unsigned32
_RcftV35PortBertUnusedTime_Object = MibTableColumn
rcftV35PortBertUnusedTime = _RcftV35PortBertUnusedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 8),
    _RcftV35PortBertUnusedTime_Type()
)
rcftV35PortBertUnusedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortBertUnusedTime.setStatus("current")
_RcftV35PortBertPortSpeed_Type = Unsigned32
_RcftV35PortBertPortSpeed_Object = MibTableColumn
rcftV35PortBertPortSpeed = _RcftV35PortBertPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 9),
    _RcftV35PortBertPortSpeed_Type()
)
rcftV35PortBertPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortBertPortSpeed.setStatus("current")
_RcftV35PortBertCodeType_Type = Integer32
_RcftV35PortBertCodeType_Object = MibTableColumn
rcftV35PortBertCodeType = _RcftV35PortBertCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 10),
    _RcftV35PortBertCodeType_Type()
)
rcftV35PortBertCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftV35PortBertCodeType.setStatus("current")
_RcftV35PortBertCodeNum_Type = Integer32
_RcftV35PortBertCodeNum_Object = MibTableColumn
rcftV35PortBertCodeNum = _RcftV35PortBertCodeNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 11),
    _RcftV35PortBertCodeNum_Type()
)
rcftV35PortBertCodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftV35PortBertCodeNum.setStatus("current")
_RcftV35PortLoopStatus_Type = Integer32
_RcftV35PortLoopStatus_Object = MibTableColumn
rcftV35PortLoopStatus = _RcftV35PortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 12),
    _RcftV35PortLoopStatus_Type()
)
rcftV35PortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftV35PortLoopStatus.setStatus("current")
_RcftV35PortOrder_Type = Integer32
_RcftV35PortOrder_Object = MibTableColumn
rcftV35PortOrder = _RcftV35PortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 1, 1, 1, 13),
    _RcftV35PortOrder_Type()
)
rcftV35PortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftV35PortOrder.setStatus("current")
_RcftV35PortPerformance_ObjectIdentity = ObjectIdentity
rcftV35PortPerformance = _RcftV35PortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 2)
)
_RcftV35PortTraps_ObjectIdentity = ObjectIdentity
rcftV35PortTraps = _RcftV35PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10)
)
_RcftSHDSLPortMib_ObjectIdentity = ObjectIdentity
rcftSHDSLPortMib = _RcftSHDSLPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5)
)
_RcftSHDSLPortObjects_ObjectIdentity = ObjectIdentity
rcftSHDSLPortObjects = _RcftSHDSLPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1)
)
_RcftSHDSLPortTable_Object = MibTable
rcftSHDSLPortTable = _RcftSHDSLPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1)
)
if mibBuilder.loadTexts:
    rcftSHDSLPortTable.setStatus("current")
_RcftSHDSLPortEntry_Object = MibTableRow
rcftSHDSLPortEntry = _RcftSHDSLPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1)
)
rcftSHDSLPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSHDSLPortEntry.setStatus("current")
_RcftSHDSLPortIndex_Type = Integer32
_RcftSHDSLPortIndex_Object = MibTableColumn
rcftSHDSLPortIndex = _RcftSHDSLPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 1),
    _RcftSHDSLPortIndex_Type()
)
rcftSHDSLPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIndex.setStatus("current")
_RcftSHDSLPortAlarmStatus_Type = Integer32
_RcftSHDSLPortAlarmStatus_Object = MibTableColumn
rcftSHDSLPortAlarmStatus = _RcftSHDSLPortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 2),
    _RcftSHDSLPortAlarmStatus_Type()
)
rcftSHDSLPortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortAlarmStatus.setStatus("current")
_RcftSHDSLPortStatus_Type = Integer32
_RcftSHDSLPortStatus_Object = MibTableColumn
rcftSHDSLPortStatus = _RcftSHDSLPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 3),
    _RcftSHDSLPortStatus_Type()
)
rcftSHDSLPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortStatus.setStatus("current")
_RcftSHDSLPortCapableSpeed_Type = Integer32
_RcftSHDSLPortCapableSpeed_Object = MibTableColumn
rcftSHDSLPortCapableSpeed = _RcftSHDSLPortCapableSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 4),
    _RcftSHDSLPortCapableSpeed_Type()
)
rcftSHDSLPortCapableSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCapableSpeed.setStatus("current")
_RcftSHDSLPortWorkSpeed_Type = Integer32
_RcftSHDSLPortWorkSpeed_Object = MibTableColumn
rcftSHDSLPortWorkSpeed = _RcftSHDSLPortWorkSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 5),
    _RcftSHDSLPortWorkSpeed_Type()
)
rcftSHDSLPortWorkSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortWorkSpeed.setStatus("current")
_RcftSHDSLPortProbeMaxSpeed_Type = Integer32
_RcftSHDSLPortProbeMaxSpeed_Object = MibTableColumn
rcftSHDSLPortProbeMaxSpeed = _RcftSHDSLPortProbeMaxSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 6),
    _RcftSHDSLPortProbeMaxSpeed_Type()
)
rcftSHDSLPortProbeMaxSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortProbeMaxSpeed.setStatus("current")
_RcftSHDSLPortProbeMinSpeed_Type = Integer32
_RcftSHDSLPortProbeMinSpeed_Object = MibTableColumn
rcftSHDSLPortProbeMinSpeed = _RcftSHDSLPortProbeMinSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 7),
    _RcftSHDSLPortProbeMinSpeed_Type()
)
rcftSHDSLPortProbeMinSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortProbeMinSpeed.setStatus("current")
_RcftSDHSLPortSNR_Type = Integer32
_RcftSDHSLPortSNR_Object = MibTableColumn
rcftSDHSLPortSNR = _RcftSDHSLPortSNR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 8),
    _RcftSDHSLPortSNR_Type()
)
rcftSDHSLPortSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSDHSLPortSNR.setStatus("current")
_RcftSHDSLPortConfigSNR_Type = Integer32
_RcftSHDSLPortConfigSNR_Object = MibTableColumn
rcftSHDSLPortConfigSNR = _RcftSHDSLPortConfigSNR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 9),
    _RcftSHDSLPortConfigSNR_Type()
)
rcftSHDSLPortConfigSNR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortConfigSNR.setStatus("current")
_RcftSHDSLPortSNRThreshold_Type = Integer32
_RcftSHDSLPortSNRThreshold_Object = MibTableColumn
rcftSHDSLPortSNRThreshold = _RcftSHDSLPortSNRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 10),
    _RcftSHDSLPortSNRThreshold_Type()
)
rcftSHDSLPortSNRThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortSNRThreshold.setStatus("current")
_RcftSHDSLPortAttenuation_Type = Integer32
_RcftSHDSLPortAttenuation_Object = MibTableColumn
rcftSHDSLPortAttenuation = _RcftSHDSLPortAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 11),
    _RcftSHDSLPortAttenuation_Type()
)
rcftSHDSLPortAttenuation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortAttenuation.setStatus("current")
_RcftSHDSLPortAttenuationThreshold_Type = Integer32
_RcftSHDSLPortAttenuationThreshold_Object = MibTableColumn
rcftSHDSLPortAttenuationThreshold = _RcftSHDSLPortAttenuationThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 12),
    _RcftSHDSLPortAttenuationThreshold_Type()
)
rcftSHDSLPortAttenuationThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortAttenuationThreshold.setStatus("current")
_RcftSHDSLPortPBO_Type = Integer32
_RcftSHDSLPortPBO_Object = MibTableColumn
rcftSHDSLPortPBO = _RcftSHDSLPortPBO_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 13),
    _RcftSHDSLPortPBO_Type()
)
rcftSHDSLPortPBO.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortPBO.setStatus("current")
_RcftSHDSLPortLOSThreshold_Type = Integer32
_RcftSHDSLPortLOSThreshold_Object = MibTableColumn
rcftSHDSLPortLOSThreshold = _RcftSHDSLPortLOSThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 14),
    _RcftSHDSLPortLOSThreshold_Type()
)
rcftSHDSLPortLOSThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortLOSThreshold.setStatus("current")
_RcftSHDSLPortLOSWThreshold_Type = Integer32
_RcftSHDSLPortLOSWThreshold_Object = MibTableColumn
rcftSHDSLPortLOSWThreshold = _RcftSHDSLPortLOSWThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 15),
    _RcftSHDSLPortLOSWThreshold_Type()
)
rcftSHDSLPortLOSWThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortLOSWThreshold.setStatus("current")
_RcftSHDSLPortLOLKThreshold_Type = Integer32
_RcftSHDSLPortLOLKThreshold_Object = MibTableColumn
rcftSHDSLPortLOLKThreshold = _RcftSHDSLPortLOLKThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 16),
    _RcftSHDSLPortLOLKThreshold_Type()
)
rcftSHDSLPortLOLKThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortLOLKThreshold.setStatus("current")
_RcftSHDSLPortESThreshold_Type = Integer32
_RcftSHDSLPortESThreshold_Object = MibTableColumn
rcftSHDSLPortESThreshold = _RcftSHDSLPortESThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 17),
    _RcftSHDSLPortESThreshold_Type()
)
rcftSHDSLPortESThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortESThreshold.setStatus("current")


class _RcftSHDSLPortLoopStatus_Type(Integer32):
    """Custom type rcftSHDSLPortLoopStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              100)
        )
    )
    namedValues = NamedValues(
        *(("insideLoop", 1),
          ("outsideLoop", 2),
          ("doubleloop", 3),
          ("normal", 100))
    )


_RcftSHDSLPortLoopStatus_Type.__name__ = "Integer32"
_RcftSHDSLPortLoopStatus_Object = MibTableColumn
rcftSHDSLPortLoopStatus = _RcftSHDSLPortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 18),
    _RcftSHDSLPortLoopStatus_Type()
)
rcftSHDSLPortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortLoopStatus.setStatus("current")
_RcftSHDSLPortAttenuationInitThreshhold_Type = Integer32
_RcftSHDSLPortAttenuationInitThreshhold_Object = MibTableColumn
rcftSHDSLPortAttenuationInitThreshhold = _RcftSHDSLPortAttenuationInitThreshhold_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 19),
    _RcftSHDSLPortAttenuationInitThreshhold_Type()
)
rcftSHDSLPortAttenuationInitThreshhold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortAttenuationInitThreshhold.setStatus("current")
_RcftSHDSLPortBertStatus_Type = Integer32
_RcftSHDSLPortBertStatus_Object = MibTableColumn
rcftSHDSLPortBertStatus = _RcftSHDSLPortBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 20),
    _RcftSHDSLPortBertStatus_Type()
)
rcftSHDSLPortBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortBertStatus.setStatus("current")
_RcftSHDSLPortBertTime_Type = Unsigned32
_RcftSHDSLPortBertTime_Object = MibTableColumn
rcftSHDSLPortBertTime = _RcftSHDSLPortBertTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 21),
    _RcftSHDSLPortBertTime_Type()
)
rcftSHDSLPortBertTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortBertTime.setStatus("current")
_RcftSHDSLPortBertErrCode_Type = Unsigned32
_RcftSHDSLPortBertErrCode_Object = MibTableColumn
rcftSHDSLPortBertErrCode = _RcftSHDSLPortBertErrCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 22),
    _RcftSHDSLPortBertErrCode_Type()
)
rcftSHDSLPortBertErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortBertErrCode.setStatus("current")
_RcftSHDSLPortBertUnusedTime_Type = Unsigned32
_RcftSHDSLPortBertUnusedTime_Object = MibTableColumn
rcftSHDSLPortBertUnusedTime = _RcftSHDSLPortBertUnusedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 23),
    _RcftSHDSLPortBertUnusedTime_Type()
)
rcftSHDSLPortBertUnusedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortBertUnusedTime.setStatus("current")
_RcftSHDSLPortBertPortSpeed_Type = Unsigned32
_RcftSHDSLPortBertPortSpeed_Object = MibTableColumn
rcftSHDSLPortBertPortSpeed = _RcftSHDSLPortBertPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 24),
    _RcftSHDSLPortBertPortSpeed_Type()
)
rcftSHDSLPortBertPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortBertPortSpeed.setStatus("current")
_RcftSHDSLPortBertCodeType_Type = Integer32
_RcftSHDSLPortBertCodeType_Object = MibTableColumn
rcftSHDSLPortBertCodeType = _RcftSHDSLPortBertCodeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 25),
    _RcftSHDSLPortBertCodeType_Type()
)
rcftSHDSLPortBertCodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortBertCodeType.setStatus("current")
_RcftSHDSLPortBertCodeNum_Type = Integer32
_RcftSHDSLPortBertCodeNum_Object = MibTableColumn
rcftSHDSLPortBertCodeNum = _RcftSHDSLPortBertCodeNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 26),
    _RcftSHDSLPortBertCodeNum_Type()
)
rcftSHDSLPortBertCodeNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortBertCodeNum.setStatus("current")
_RcftSHDSLPortOrder_Type = Integer32
_RcftSHDSLPortOrder_Object = MibTableColumn
rcftSHDSLPortOrder = _RcftSHDSLPortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 27),
    _RcftSHDSLPortOrder_Type()
)
rcftSHDSLPortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortOrder.setStatus("current")
_RcftSHDSLPortOrderTimeParameter_Type = Integer32
_RcftSHDSLPortOrderTimeParameter_Object = MibTableColumn
rcftSHDSLPortOrderTimeParameter = _RcftSHDSLPortOrderTimeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 28),
    _RcftSHDSLPortOrderTimeParameter_Type()
)
rcftSHDSLPortOrderTimeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortOrderTimeParameter.setStatus("current")
_RcftSHDSLPortOrderModeParameter_Type = Integer32
_RcftSHDSLPortOrderModeParameter_Object = MibTableColumn
rcftSHDSLPortOrderModeParameter = _RcftSHDSLPortOrderModeParameter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 1, 1, 1, 29),
    _RcftSHDSLPortOrderModeParameter_Type()
)
rcftSHDSLPortOrderModeParameter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSHDSLPortOrderModeParameter.setStatus("current")
_RcftSHDSLPortPerformance_ObjectIdentity = ObjectIdentity
rcftSHDSLPortPerformance = _RcftSHDSLPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2)
)
_RcftSHDSLPortCurrentTable_Object = MibTable
rcftSHDSLPortCurrentTable = _RcftSHDSLPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1)
)
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentTable.setStatus("current")
_RcftSHDSLPortCurrentEntry_Object = MibTableRow
rcftSHDSLPortCurrentEntry = _RcftSHDSLPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1)
)
rcftSHDSLPortCurrentEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentEntry.setStatus("current")
_RcftSHDSLPortCurrentLOSTimes_Type = Integer32
_RcftSHDSLPortCurrentLOSTimes_Object = MibTableColumn
rcftSHDSLPortCurrentLOSTimes = _RcftSHDSLPortCurrentLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 1),
    _RcftSHDSLPortCurrentLOSTimes_Type()
)
rcftSHDSLPortCurrentLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentLOSTimes.setStatus("current")
_RcftSHDSLPortCurrentLOSWTimes_Type = Integer32
_RcftSHDSLPortCurrentLOSWTimes_Object = MibTableColumn
rcftSHDSLPortCurrentLOSWTimes = _RcftSHDSLPortCurrentLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 2),
    _RcftSHDSLPortCurrentLOSWTimes_Type()
)
rcftSHDSLPortCurrentLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentLOSWTimes.setStatus("current")
_RcftSHDSLPortCurrentLOLKTimes_Type = Integer32
_RcftSHDSLPortCurrentLOLKTimes_Object = MibTableColumn
rcftSHDSLPortCurrentLOLKTimes = _RcftSHDSLPortCurrentLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 3),
    _RcftSHDSLPortCurrentLOLKTimes_Type()
)
rcftSHDSLPortCurrentLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentLOLKTimes.setStatus("current")
_RcftSHDSLPortCurrentCVTimes_Type = Integer32
_RcftSHDSLPortCurrentCVTimes_Object = MibTableColumn
rcftSHDSLPortCurrentCVTimes = _RcftSHDSLPortCurrentCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 4),
    _RcftSHDSLPortCurrentCVTimes_Type()
)
rcftSHDSLPortCurrentCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentCVTimes.setStatus("current")
_RcftSHDSLPortCurrentES_Type = Integer32
_RcftSHDSLPortCurrentES_Object = MibTableColumn
rcftSHDSLPortCurrentES = _RcftSHDSLPortCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 5),
    _RcftSHDSLPortCurrentES_Type()
)
rcftSHDSLPortCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentES.setStatus("current")
_RcftSHDSLPortCurrentSES_Type = Integer32
_RcftSHDSLPortCurrentSES_Object = MibTableColumn
rcftSHDSLPortCurrentSES = _RcftSHDSLPortCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 6),
    _RcftSHDSLPortCurrentSES_Type()
)
rcftSHDSLPortCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentSES.setStatus("current")
_RcftSHDSLPortCurrentUAS_Type = Integer32
_RcftSHDSLPortCurrentUAS_Object = MibTableColumn
rcftSHDSLPortCurrentUAS = _RcftSHDSLPortCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 7),
    _RcftSHDSLPortCurrentUAS_Type()
)
rcftSHDSLPortCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentUAS.setStatus("current")
_RcftSHDSLPortCurrentLOSWS_Type = Integer32
_RcftSHDSLPortCurrentLOSWS_Object = MibTableColumn
rcftSHDSLPortCurrentLOSWS = _RcftSHDSLPortCurrentLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 8),
    _RcftSHDSLPortCurrentLOSWS_Type()
)
rcftSHDSLPortCurrentLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentLOSWS.setStatus("current")
_RcftSHDSLPortCurrentLOFTimes_Type = Integer32
_RcftSHDSLPortCurrentLOFTimes_Object = MibTableColumn
rcftSHDSLPortCurrentLOFTimes = _RcftSHDSLPortCurrentLOFTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 9),
    _RcftSHDSLPortCurrentLOFTimes_Type()
)
rcftSHDSLPortCurrentLOFTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentLOFTimes.setStatus("current")
_RcftSHDSLPortCurrentCRCTimes_Type = Integer32
_RcftSHDSLPortCurrentCRCTimes_Object = MibTableColumn
rcftSHDSLPortCurrentCRCTimes = _RcftSHDSLPortCurrentCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 1, 1, 10),
    _RcftSHDSLPortCurrentCRCTimes_Type()
)
rcftSHDSLPortCurrentCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentCRCTimes.setStatus("current")
_RcftSHDSLPortIntervalTable_Object = MibTable
rcftSHDSLPortIntervalTable = _RcftSHDSLPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2)
)
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalTable.setStatus("current")
_RcftSHDSLPortIntervalEntry_Object = MibTableRow
rcftSHDSLPortIntervalEntry = _RcftSHDSLPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1)
)
rcftSHDSLPortIntervalEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortIntervalNumber"),
)
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalEntry.setStatus("current")
_RcftSHDSLPortIntervalNumber_Type = Integer32
_RcftSHDSLPortIntervalNumber_Object = MibTableColumn
rcftSHDSLPortIntervalNumber = _RcftSHDSLPortIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 1),
    _RcftSHDSLPortIntervalNumber_Type()
)
rcftSHDSLPortIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalNumber.setStatus("current")
_RcftSHDSLPortIntervalLOSTimes_Type = Integer32
_RcftSHDSLPortIntervalLOSTimes_Object = MibTableColumn
rcftSHDSLPortIntervalLOSTimes = _RcftSHDSLPortIntervalLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 2),
    _RcftSHDSLPortIntervalLOSTimes_Type()
)
rcftSHDSLPortIntervalLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalLOSTimes.setStatus("current")
_RcftSHDSLPortIntervalLOSWTimes_Type = Integer32
_RcftSHDSLPortIntervalLOSWTimes_Object = MibTableColumn
rcftSHDSLPortIntervalLOSWTimes = _RcftSHDSLPortIntervalLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 3),
    _RcftSHDSLPortIntervalLOSWTimes_Type()
)
rcftSHDSLPortIntervalLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalLOSWTimes.setStatus("current")
_RcftSHDSLPortIntervalLOLKTimes_Type = Integer32
_RcftSHDSLPortIntervalLOLKTimes_Object = MibTableColumn
rcftSHDSLPortIntervalLOLKTimes = _RcftSHDSLPortIntervalLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 4),
    _RcftSHDSLPortIntervalLOLKTimes_Type()
)
rcftSHDSLPortIntervalLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalLOLKTimes.setStatus("current")
_RcftSHDSLPortIntervalCVTimes_Type = Integer32
_RcftSHDSLPortIntervalCVTimes_Object = MibTableColumn
rcftSHDSLPortIntervalCVTimes = _RcftSHDSLPortIntervalCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 5),
    _RcftSHDSLPortIntervalCVTimes_Type()
)
rcftSHDSLPortIntervalCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalCVTimes.setStatus("current")
_RcftSHDSLPortIntervalES_Type = Integer32
_RcftSHDSLPortIntervalES_Object = MibTableColumn
rcftSHDSLPortIntervalES = _RcftSHDSLPortIntervalES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 6),
    _RcftSHDSLPortIntervalES_Type()
)
rcftSHDSLPortIntervalES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalES.setStatus("current")
_RcftSHDSLPortIntervalSES_Type = Integer32
_RcftSHDSLPortIntervalSES_Object = MibTableColumn
rcftSHDSLPortIntervalSES = _RcftSHDSLPortIntervalSES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 7),
    _RcftSHDSLPortIntervalSES_Type()
)
rcftSHDSLPortIntervalSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalSES.setStatus("current")
_RcftSHDSLPortIntervalUAS_Type = Integer32
_RcftSHDSLPortIntervalUAS_Object = MibTableColumn
rcftSHDSLPortIntervalUAS = _RcftSHDSLPortIntervalUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 8),
    _RcftSHDSLPortIntervalUAS_Type()
)
rcftSHDSLPortIntervalUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalUAS.setStatus("current")
_RcftSHDSLPortIntervalLOSWS_Type = Integer32
_RcftSHDSLPortIntervalLOSWS_Object = MibTableColumn
rcftSHDSLPortIntervalLOSWS = _RcftSHDSLPortIntervalLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 9),
    _RcftSHDSLPortIntervalLOSWS_Type()
)
rcftSHDSLPortIntervalLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalLOSWS.setStatus("current")
_RcftSHDSLPortIntervalLOFTimes_Type = Integer32
_RcftSHDSLPortIntervalLOFTimes_Object = MibTableColumn
rcftSHDSLPortIntervalLOFTimes = _RcftSHDSLPortIntervalLOFTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 10),
    _RcftSHDSLPortIntervalLOFTimes_Type()
)
rcftSHDSLPortIntervalLOFTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalLOFTimes.setStatus("current")
_RcftSHDSLPortIntervalCRCTimes_Type = Integer32
_RcftSHDSLPortIntervalCRCTimes_Object = MibTableColumn
rcftSHDSLPortIntervalCRCTimes = _RcftSHDSLPortIntervalCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 2, 1, 11),
    _RcftSHDSLPortIntervalCRCTimes_Type()
)
rcftSHDSLPortIntervalCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalCRCTimes.setStatus("current")
_RcftSHDSLPortCurrentDayTable_Object = MibTable
rcftSHDSLPortCurrentDayTable = _RcftSHDSLPortCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3)
)
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayTable.setStatus("current")
_RcftSHDSLPortCurrentDayEntry_Object = MibTableRow
rcftSHDSLPortCurrentDayEntry = _RcftSHDSLPortCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1)
)
rcftSHDSLPortCurrentDayEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayEntry.setStatus("current")
_RcftSHDSLPortCurrentDayLOSTimes_Type = Integer32
_RcftSHDSLPortCurrentDayLOSTimes_Object = MibTableColumn
rcftSHDSLPortCurrentDayLOSTimes = _RcftSHDSLPortCurrentDayLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 1),
    _RcftSHDSLPortCurrentDayLOSTimes_Type()
)
rcftSHDSLPortCurrentDayLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayLOSTimes.setStatus("current")
_RcftSHDSLPortCurrentDayLOSWTimes_Type = Integer32
_RcftSHDSLPortCurrentDayLOSWTimes_Object = MibTableColumn
rcftSHDSLPortCurrentDayLOSWTimes = _RcftSHDSLPortCurrentDayLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 2),
    _RcftSHDSLPortCurrentDayLOSWTimes_Type()
)
rcftSHDSLPortCurrentDayLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayLOSWTimes.setStatus("current")
_RcftSHDSLPortCurrentDayLOLKTimes_Type = Integer32
_RcftSHDSLPortCurrentDayLOLKTimes_Object = MibTableColumn
rcftSHDSLPortCurrentDayLOLKTimes = _RcftSHDSLPortCurrentDayLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 3),
    _RcftSHDSLPortCurrentDayLOLKTimes_Type()
)
rcftSHDSLPortCurrentDayLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayLOLKTimes.setStatus("current")
_RcftSHDSLPortCurrentDayCVTimes_Type = Integer32
_RcftSHDSLPortCurrentDayCVTimes_Object = MibTableColumn
rcftSHDSLPortCurrentDayCVTimes = _RcftSHDSLPortCurrentDayCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 4),
    _RcftSHDSLPortCurrentDayCVTimes_Type()
)
rcftSHDSLPortCurrentDayCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayCVTimes.setStatus("current")
_RcftSHDSLPortCurrentDayES_Type = Integer32
_RcftSHDSLPortCurrentDayES_Object = MibTableColumn
rcftSHDSLPortCurrentDayES = _RcftSHDSLPortCurrentDayES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 5),
    _RcftSHDSLPortCurrentDayES_Type()
)
rcftSHDSLPortCurrentDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayES.setStatus("current")
_RcftSHDSLPortCurrentDaySES_Type = Integer32
_RcftSHDSLPortCurrentDaySES_Object = MibTableColumn
rcftSHDSLPortCurrentDaySES = _RcftSHDSLPortCurrentDaySES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 6),
    _RcftSHDSLPortCurrentDaySES_Type()
)
rcftSHDSLPortCurrentDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDaySES.setStatus("current")
_RcftSHDSLPortCurrentDayUAS_Type = Integer32
_RcftSHDSLPortCurrentDayUAS_Object = MibTableColumn
rcftSHDSLPortCurrentDayUAS = _RcftSHDSLPortCurrentDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 7),
    _RcftSHDSLPortCurrentDayUAS_Type()
)
rcftSHDSLPortCurrentDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayUAS.setStatus("current")
_RcftSHDSLPortCurrentDayLOSWS_Type = Integer32
_RcftSHDSLPortCurrentDayLOSWS_Object = MibTableColumn
rcftSHDSLPortCurrentDayLOSWS = _RcftSHDSLPortCurrentDayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 8),
    _RcftSHDSLPortCurrentDayLOSWS_Type()
)
rcftSHDSLPortCurrentDayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayLOSWS.setStatus("current")
_RcftSHDSLPortCurrentDayLOFTimes_Type = Integer32
_RcftSHDSLPortCurrentDayLOFTimes_Object = MibTableColumn
rcftSHDSLPortCurrentDayLOFTimes = _RcftSHDSLPortCurrentDayLOFTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 9),
    _RcftSHDSLPortCurrentDayLOFTimes_Type()
)
rcftSHDSLPortCurrentDayLOFTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayLOFTimes.setStatus("current")
_RcftSHDSLPortCurrentDayCRCTimes_Type = Integer32
_RcftSHDSLPortCurrentDayCRCTimes_Object = MibTableColumn
rcftSHDSLPortCurrentDayCRCTimes = _RcftSHDSLPortCurrentDayCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 3, 1, 10),
    _RcftSHDSLPortCurrentDayCRCTimes_Type()
)
rcftSHDSLPortCurrentDayCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortCurrentDayCRCTimes.setStatus("current")
_RcftSHDSLPortIntervalDayTable_Object = MibTable
rcftSHDSLPortIntervalDayTable = _RcftSHDSLPortIntervalDayTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4)
)
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayTable.setStatus("current")
_RcftSHDSLPortIntervalDayEntry_Object = MibTableRow
rcftSHDSLPortIntervalDayEntry = _RcftSHDSLPortIntervalDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1)
)
rcftSHDSLPortIntervalDayEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortIntervalDayNumber"),
)
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayEntry.setStatus("current")
_RcftSHDSLPortIntervalDayNumber_Type = Integer32
_RcftSHDSLPortIntervalDayNumber_Object = MibTableColumn
rcftSHDSLPortIntervalDayNumber = _RcftSHDSLPortIntervalDayNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 1),
    _RcftSHDSLPortIntervalDayNumber_Type()
)
rcftSHDSLPortIntervalDayNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayNumber.setStatus("current")
_RcftSHDSLPortIntervalDayLOSTimes_Type = Integer32
_RcftSHDSLPortIntervalDayLOSTimes_Object = MibTableColumn
rcftSHDSLPortIntervalDayLOSTimes = _RcftSHDSLPortIntervalDayLOSTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 2),
    _RcftSHDSLPortIntervalDayLOSTimes_Type()
)
rcftSHDSLPortIntervalDayLOSTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayLOSTimes.setStatus("current")
_RcftSHDSLPortIntervalDayLOSWTimes_Type = Integer32
_RcftSHDSLPortIntervalDayLOSWTimes_Object = MibTableColumn
rcftSHDSLPortIntervalDayLOSWTimes = _RcftSHDSLPortIntervalDayLOSWTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 3),
    _RcftSHDSLPortIntervalDayLOSWTimes_Type()
)
rcftSHDSLPortIntervalDayLOSWTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayLOSWTimes.setStatus("current")
_RcftSHDSLPortIntervalDayLOLKTimes_Type = Integer32
_RcftSHDSLPortIntervalDayLOLKTimes_Object = MibTableColumn
rcftSHDSLPortIntervalDayLOLKTimes = _RcftSHDSLPortIntervalDayLOLKTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 4),
    _RcftSHDSLPortIntervalDayLOLKTimes_Type()
)
rcftSHDSLPortIntervalDayLOLKTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayLOLKTimes.setStatus("current")
_RcftSHDSLPortIntervalDayCVTimes_Type = Integer32
_RcftSHDSLPortIntervalDayCVTimes_Object = MibTableColumn
rcftSHDSLPortIntervalDayCVTimes = _RcftSHDSLPortIntervalDayCVTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 5),
    _RcftSHDSLPortIntervalDayCVTimes_Type()
)
rcftSHDSLPortIntervalDayCVTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayCVTimes.setStatus("current")
_RcftSHDSLPortIntervalDayES_Type = Integer32
_RcftSHDSLPortIntervalDayES_Object = MibTableColumn
rcftSHDSLPortIntervalDayES = _RcftSHDSLPortIntervalDayES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 6),
    _RcftSHDSLPortIntervalDayES_Type()
)
rcftSHDSLPortIntervalDayES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayES.setStatus("current")
_RcftSHDSLPortIntervalDaySES_Type = Integer32
_RcftSHDSLPortIntervalDaySES_Object = MibTableColumn
rcftSHDSLPortIntervalDaySES = _RcftSHDSLPortIntervalDaySES_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 7),
    _RcftSHDSLPortIntervalDaySES_Type()
)
rcftSHDSLPortIntervalDaySES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDaySES.setStatus("current")
_RcftSHDSLPortIntervalDayUAS_Type = Integer32
_RcftSHDSLPortIntervalDayUAS_Object = MibTableColumn
rcftSHDSLPortIntervalDayUAS = _RcftSHDSLPortIntervalDayUAS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 8),
    _RcftSHDSLPortIntervalDayUAS_Type()
)
rcftSHDSLPortIntervalDayUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayUAS.setStatus("current")
_RcftSHDSLPortIntervalDayLOSWS_Type = Integer32
_RcftSHDSLPortIntervalDayLOSWS_Object = MibTableColumn
rcftSHDSLPortIntervalDayLOSWS = _RcftSHDSLPortIntervalDayLOSWS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 9),
    _RcftSHDSLPortIntervalDayLOSWS_Type()
)
rcftSHDSLPortIntervalDayLOSWS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayLOSWS.setStatus("current")
_RcftSHDSLPortIntervalDayLOFTimes_Type = Integer32
_RcftSHDSLPortIntervalDayLOFTimes_Object = MibTableColumn
rcftSHDSLPortIntervalDayLOFTimes = _RcftSHDSLPortIntervalDayLOFTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 10),
    _RcftSHDSLPortIntervalDayLOFTimes_Type()
)
rcftSHDSLPortIntervalDayLOFTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayLOFTimes.setStatus("current")
_RcftSHDSLPortIntervalDayCRCTimes_Type = Integer32
_RcftSHDSLPortIntervalDayCRCTimes_Object = MibTableColumn
rcftSHDSLPortIntervalDayCRCTimes = _RcftSHDSLPortIntervalDayCRCTimes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 2, 4, 1, 11),
    _RcftSHDSLPortIntervalDayCRCTimes_Type()
)
rcftSHDSLPortIntervalDayCRCTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSHDSLPortIntervalDayCRCTimes.setStatus("current")
_RcftSHDSLPortTraps_ObjectIdentity = ObjectIdentity
rcftSHDSLPortTraps = _RcftSHDSLPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10)
)
_RcftAudioPortMib_ObjectIdentity = ObjectIdentity
rcftAudioPortMib = _RcftAudioPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6)
)
_RcftAudioPortObjects_ObjectIdentity = ObjectIdentity
rcftAudioPortObjects = _RcftAudioPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 1)
)
_RcftAudioPortTable_Object = MibTable
rcftAudioPortTable = _RcftAudioPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 1, 1)
)
if mibBuilder.loadTexts:
    rcftAudioPortTable.setStatus("current")
_RcftAudioPortEntry_Object = MibTableRow
rcftAudioPortEntry = _RcftAudioPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 1, 1, 1)
)
rcftAudioPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftAudioPortIndex"),
)
if mibBuilder.loadTexts:
    rcftAudioPortEntry.setStatus("current")
_RcftAudioPortIndex_Type = Integer32
_RcftAudioPortIndex_Object = MibTableColumn
rcftAudioPortIndex = _RcftAudioPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 1, 1, 1, 1),
    _RcftAudioPortIndex_Type()
)
rcftAudioPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftAudioPortIndex.setStatus("current")
_RcftAudioPortStatus_Type = Integer32
_RcftAudioPortStatus_Object = MibTableColumn
rcftAudioPortStatus = _RcftAudioPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 1, 1, 1, 2),
    _RcftAudioPortStatus_Type()
)
rcftAudioPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftAudioPortStatus.setStatus("current")
_RcftAudioPortPosition_Type = Integer32
_RcftAudioPortPosition_Object = MibTableColumn
rcftAudioPortPosition = _RcftAudioPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 1, 1, 1, 3),
    _RcftAudioPortPosition_Type()
)
rcftAudioPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftAudioPortPosition.setStatus("current")
_RcftAudioPortType_Type = Integer32
_RcftAudioPortType_Object = MibTableColumn
rcftAudioPortType = _RcftAudioPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 1, 1, 1, 4),
    _RcftAudioPortType_Type()
)
rcftAudioPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftAudioPortType.setStatus("current")
_RcftAudioPortPerformance_ObjectIdentity = ObjectIdentity
rcftAudioPortPerformance = _RcftAudioPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 2)
)
_RcftAudioPortTraps_ObjectIdentity = ObjectIdentity
rcftAudioPortTraps = _RcftAudioPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 6, 10)
)
_RcftDS3E3PortMib_ObjectIdentity = ObjectIdentity
rcftDS3E3PortMib = _RcftDS3E3PortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7)
)
_RcftDS3E3PortObjects_ObjectIdentity = ObjectIdentity
rcftDS3E3PortObjects = _RcftDS3E3PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1)
)
_RcftDS3E3PortTable_Object = MibTable
rcftDS3E3PortTable = _RcftDS3E3PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1)
)
if mibBuilder.loadTexts:
    rcftDS3E3PortTable.setStatus("current")
_RcftDS3E3PortEntry_Object = MibTableRow
rcftDS3E3PortEntry = _RcftDS3E3PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1, 1)
)
rcftDS3E3PortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortIndex"),
)
if mibBuilder.loadTexts:
    rcftDS3E3PortEntry.setStatus("current")
_RcftDS3E3PortIndex_Type = Integer32
_RcftDS3E3PortIndex_Object = MibTableColumn
rcftDS3E3PortIndex = _RcftDS3E3PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1, 1, 1),
    _RcftDS3E3PortIndex_Type()
)
rcftDS3E3PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3PortIndex.setStatus("current")
_RcftDS3E3PortAlarmStatus_Type = Integer32
_RcftDS3E3PortAlarmStatus_Object = MibTableColumn
rcftDS3E3PortAlarmStatus = _RcftDS3E3PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1, 1, 2),
    _RcftDS3E3PortAlarmStatus_Type()
)
rcftDS3E3PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3PortAlarmStatus.setStatus("current")
_RcftDS3E3PortStatus_Type = Integer32
_RcftDS3E3PortStatus_Object = MibTableColumn
rcftDS3E3PortStatus = _RcftDS3E3PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1, 1, 3),
    _RcftDS3E3PortStatus_Type()
)
rcftDS3E3PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDS3E3PortStatus.setStatus("current")
_RcftDS3E3PortESCont_Type = Integer32
_RcftDS3E3PortESCont_Object = MibTableColumn
rcftDS3E3PortESCont = _RcftDS3E3PortESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1, 1, 4),
    _RcftDS3E3PortESCont_Type()
)
rcftDS3E3PortESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3PortESCont.setStatus("current")
_RcftDS3E3PortLoopStatus_Type = Integer32
_RcftDS3E3PortLoopStatus_Object = MibTableColumn
rcftDS3E3PortLoopStatus = _RcftDS3E3PortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1, 1, 5),
    _RcftDS3E3PortLoopStatus_Type()
)
rcftDS3E3PortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3PortLoopStatus.setStatus("current")
_RcftDS3E3PortOrder_Type = Integer32
_RcftDS3E3PortOrder_Object = MibTableColumn
rcftDS3E3PortOrder = _RcftDS3E3PortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 1, 1, 1, 6),
    _RcftDS3E3PortOrder_Type()
)
rcftDS3E3PortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDS3E3PortOrder.setStatus("current")
_RcftDS3E3PortPerformance_ObjectIdentity = ObjectIdentity
rcftDS3E3PortPerformance = _RcftDS3E3PortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2)
)
_RcftDS3E3StatisticTable_Object = MibTable
rcftDS3E3StatisticTable = _RcftDS3E3StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1)
)
if mibBuilder.loadTexts:
    rcftDS3E3StatisticTable.setStatus("current")
_RcftDS3E3StatisticEntry_Object = MibTableRow
rcftDS3E3StatisticEntry = _RcftDS3E3StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftDS3E3StatisticEntry.setStatus("current")
_RcftDS3E3TxPackets_Type = Counter32
_RcftDS3E3TxPackets_Object = MibTableColumn
rcftDS3E3TxPackets = _RcftDS3E3TxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1, 1),
    _RcftDS3E3TxPackets_Type()
)
rcftDS3E3TxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3TxPackets.setStatus("current")
_RcftDS3E3TxBytes_Type = Counter32
_RcftDS3E3TxBytes_Object = MibTableColumn
rcftDS3E3TxBytes = _RcftDS3E3TxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1, 2),
    _RcftDS3E3TxBytes_Type()
)
rcftDS3E3TxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3TxBytes.setStatus("current")
_RcftDS3E3TxFailurePackets_Type = Counter32
_RcftDS3E3TxFailurePackets_Object = MibTableColumn
rcftDS3E3TxFailurePackets = _RcftDS3E3TxFailurePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1, 3),
    _RcftDS3E3TxFailurePackets_Type()
)
rcftDS3E3TxFailurePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3TxFailurePackets.setStatus("current")
_RcftDS3E3RxPackets_Type = Counter32
_RcftDS3E3RxPackets_Object = MibTableColumn
rcftDS3E3RxPackets = _RcftDS3E3RxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1, 4),
    _RcftDS3E3RxPackets_Type()
)
rcftDS3E3RxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3RxPackets.setStatus("current")
_RcftDS3E3RxBytes_Type = Counter32
_RcftDS3E3RxBytes_Object = MibTableColumn
rcftDS3E3RxBytes = _RcftDS3E3RxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1, 5),
    _RcftDS3E3RxBytes_Type()
)
rcftDS3E3RxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3RxBytes.setStatus("current")
_RcftDS3E3RxErrorPackets_Type = Counter32
_RcftDS3E3RxErrorPackets_Object = MibTableColumn
rcftDS3E3RxErrorPackets = _RcftDS3E3RxErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1, 6),
    _RcftDS3E3RxErrorPackets_Type()
)
rcftDS3E3RxErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3RxErrorPackets.setStatus("current")
_RcftDS3E3FluxTimer_Type = Counter32
_RcftDS3E3FluxTimer_Object = MibTableColumn
rcftDS3E3FluxTimer = _RcftDS3E3FluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 2, 1, 1, 7),
    _RcftDS3E3FluxTimer_Type()
)
rcftDS3E3FluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS3E3FluxTimer.setStatus("current")
_RcftDS3E3PortTraps_ObjectIdentity = ObjectIdentity
rcftDS3E3PortTraps = _RcftDS3E3PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10)
)
_RcftDS1PortMib_ObjectIdentity = ObjectIdentity
rcftDS1PortMib = _RcftDS1PortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8)
)
_RcftDS1PortObjects_ObjectIdentity = ObjectIdentity
rcftDS1PortObjects = _RcftDS1PortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1)
)
_RcftDS1PortTable_Object = MibTable
rcftDS1PortTable = _RcftDS1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1)
)
if mibBuilder.loadTexts:
    rcftDS1PortTable.setStatus("current")
_RcftDS1PortEntry_Object = MibTableRow
rcftDS1PortEntry = _RcftDS1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1)
)
rcftDS1PortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortIndex"),
)
if mibBuilder.loadTexts:
    rcftDS1PortEntry.setStatus("current")
_RcftDS1PortIndex_Type = Integer32
_RcftDS1PortIndex_Object = MibTableColumn
rcftDS1PortIndex = _RcftDS1PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 1),
    _RcftDS1PortIndex_Type()
)
rcftDS1PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortIndex.setStatus("current")
_RcftDS1PortAlarmStatus_Type = Integer32
_RcftDS1PortAlarmStatus_Object = MibTableColumn
rcftDS1PortAlarmStatus = _RcftDS1PortAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 2),
    _RcftDS1PortAlarmStatus_Type()
)
rcftDS1PortAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortAlarmStatus.setStatus("current")
_RcftDS1PortStatus_Type = Integer32
_RcftDS1PortStatus_Object = MibTableColumn
rcftDS1PortStatus = _RcftDS1PortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 3),
    _RcftDS1PortStatus_Type()
)
rcftDS1PortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDS1PortStatus.setStatus("current")
_RcftDS1PortBertStatus_Type = Integer32
_RcftDS1PortBertStatus_Object = MibTableColumn
rcftDS1PortBertStatus = _RcftDS1PortBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 4),
    _RcftDS1PortBertStatus_Type()
)
rcftDS1PortBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortBertStatus.setStatus("current")
_RcftDS1PortESCont_Type = Integer32
_RcftDS1PortESCont_Object = MibTableColumn
rcftDS1PortESCont = _RcftDS1PortESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 5),
    _RcftDS1PortESCont_Type()
)
rcftDS1PortESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortESCont.setStatus("current")
_RcftDS1PortSESCont_Type = Integer32
_RcftDS1PortSESCont_Object = MibTableColumn
rcftDS1PortSESCont = _RcftDS1PortSESCont_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 6),
    _RcftDS1PortSESCont_Type()
)
rcftDS1PortSESCont.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortSESCont.setStatus("current")
_RcftDS1PortLoopStatus_Type = Integer32
_RcftDS1PortLoopStatus_Object = MibTableColumn
rcftDS1PortLoopStatus = _RcftDS1PortLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 7),
    _RcftDS1PortLoopStatus_Type()
)
rcftDS1PortLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortLoopStatus.setStatus("current")
_RcftDS1PortOrder_Type = Integer32
_RcftDS1PortOrder_Object = MibTableColumn
rcftDS1PortOrder = _RcftDS1PortOrder_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 8),
    _RcftDS1PortOrder_Type()
)
rcftDS1PortOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDS1PortOrder.setStatus("current")
_RcftDS1PortTranLength_Type = Integer32
_RcftDS1PortTranLength_Object = MibTableColumn
rcftDS1PortTranLength = _RcftDS1PortTranLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 9),
    _RcftDS1PortTranLength_Type()
)
rcftDS1PortTranLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDS1PortTranLength.setStatus("current")
_RcftDS1PortFaultPassIndicator_Type = Integer32
_RcftDS1PortFaultPassIndicator_Object = MibTableColumn
rcftDS1PortFaultPassIndicator = _RcftDS1PortFaultPassIndicator_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 10),
    _RcftDS1PortFaultPassIndicator_Type()
)
rcftDS1PortFaultPassIndicator.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortFaultPassIndicator.setStatus("current")
_RcftDS1PortframeType_Type = Integer32
_RcftDS1PortframeType_Object = MibTableColumn
rcftDS1PortframeType = _RcftDS1PortframeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 11),
    _RcftDS1PortframeType_Type()
)
rcftDS1PortframeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDS1PortframeType.setStatus("current")
_RcftDS1PortChannel_Type = Integer32
_RcftDS1PortChannel_Object = MibTableColumn
rcftDS1PortChannel = _RcftDS1PortChannel_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 1, 1, 1, 12),
    _RcftDS1PortChannel_Type()
)
rcftDS1PortChannel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDS1PortChannel.setStatus("current")
_RcftDS1PortPerformance_ObjectIdentity = ObjectIdentity
rcftDS1PortPerformance = _RcftDS1PortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2)
)
_RcftDS1StatisticTable_Object = MibTable
rcftDS1StatisticTable = _RcftDS1StatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1)
)
if mibBuilder.loadTexts:
    rcftDS1StatisticTable.setStatus("current")
_RcftDS1StatisticEntry_Object = MibTableRow
rcftDS1StatisticEntry = _RcftDS1StatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftDS1StatisticEntry.setStatus("current")
_RcftDS1PortTxPackets_Type = Counter32
_RcftDS1PortTxPackets_Object = MibTableColumn
rcftDS1PortTxPackets = _RcftDS1PortTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1, 1),
    _RcftDS1PortTxPackets_Type()
)
rcftDS1PortTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortTxPackets.setStatus("current")
_RcftDS1PortTxBytes_Type = Counter32
_RcftDS1PortTxBytes_Object = MibTableColumn
rcftDS1PortTxBytes = _RcftDS1PortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1, 2),
    _RcftDS1PortTxBytes_Type()
)
rcftDS1PortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortTxBytes.setStatus("current")
_RcftDS1PortTxFailurePackets_Type = Counter32
_RcftDS1PortTxFailurePackets_Object = MibTableColumn
rcftDS1PortTxFailurePackets = _RcftDS1PortTxFailurePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1, 3),
    _RcftDS1PortTxFailurePackets_Type()
)
rcftDS1PortTxFailurePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortTxFailurePackets.setStatus("current")
_RcftDS1PortRxPackets_Type = Counter32
_RcftDS1PortRxPackets_Object = MibTableColumn
rcftDS1PortRxPackets = _RcftDS1PortRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1, 4),
    _RcftDS1PortRxPackets_Type()
)
rcftDS1PortRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortRxPackets.setStatus("current")
_RcftDS1PortRxBytes_Type = Counter32
_RcftDS1PortRxBytes_Object = MibTableColumn
rcftDS1PortRxBytes = _RcftDS1PortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1, 5),
    _RcftDS1PortRxBytes_Type()
)
rcftDS1PortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortRxBytes.setStatus("current")
_RcftDS1PortRxErrorPackets_Type = Counter32
_RcftDS1PortRxErrorPackets_Object = MibTableColumn
rcftDS1PortRxErrorPackets = _RcftDS1PortRxErrorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1, 6),
    _RcftDS1PortRxErrorPackets_Type()
)
rcftDS1PortRxErrorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortRxErrorPackets.setStatus("current")
_RcftDS1PortFluxTimer_Type = Counter32
_RcftDS1PortFluxTimer_Object = MibTableColumn
rcftDS1PortFluxTimer = _RcftDS1PortFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 2, 1, 1, 7),
    _RcftDS1PortFluxTimer_Type()
)
rcftDS1PortFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDS1PortFluxTimer.setStatus("current")
_RcftDS1PortTraps_ObjectIdentity = ObjectIdentity
rcftDS1PortTraps = _RcftDS1PortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10)
)
_RcftVideoPortMib_ObjectIdentity = ObjectIdentity
rcftVideoPortMib = _RcftVideoPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9)
)
_RcftVideoPortObjects_ObjectIdentity = ObjectIdentity
rcftVideoPortObjects = _RcftVideoPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 1)
)
_RcftVideoPortTable_Object = MibTable
rcftVideoPortTable = _RcftVideoPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 1, 1)
)
if mibBuilder.loadTexts:
    rcftVideoPortTable.setStatus("current")
_RcftVideoPortEntry_Object = MibTableRow
rcftVideoPortEntry = _RcftVideoPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 1, 1, 1)
)
rcftVideoPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftVideoPortIndex"),
)
if mibBuilder.loadTexts:
    rcftVideoPortEntry.setStatus("current")
_RcftVideoPortIndex_Type = Integer32
_RcftVideoPortIndex_Object = MibTableColumn
rcftVideoPortIndex = _RcftVideoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 1, 1, 1, 1),
    _RcftVideoPortIndex_Type()
)
rcftVideoPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVideoPortIndex.setStatus("current")
_RcftVideoPortStatus_Type = Integer32
_RcftVideoPortStatus_Object = MibTableColumn
rcftVideoPortStatus = _RcftVideoPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 1, 1, 1, 2),
    _RcftVideoPortStatus_Type()
)
rcftVideoPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftVideoPortStatus.setStatus("current")
_RcftVideoPortPosition_Type = Integer32
_RcftVideoPortPosition_Object = MibTableColumn
rcftVideoPortPosition = _RcftVideoPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 1, 1, 1, 3),
    _RcftVideoPortPosition_Type()
)
rcftVideoPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVideoPortPosition.setStatus("current")
_RcftVideoPortSourceID_Type = Integer32
_RcftVideoPortSourceID_Object = MibTableColumn
rcftVideoPortSourceID = _RcftVideoPortSourceID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 1, 1, 1, 4),
    _RcftVideoPortSourceID_Type()
)
rcftVideoPortSourceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftVideoPortSourceID.setStatus("current")
_RcftVideoPortPerformance_ObjectIdentity = ObjectIdentity
rcftVideoPortPerformance = _RcftVideoPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 2)
)
_RcftVideoPortTraps_ObjectIdentity = ObjectIdentity
rcftVideoPortTraps = _RcftVideoPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 10)
)
_RcftDataPortMib_ObjectIdentity = ObjectIdentity
rcftDataPortMib = _RcftDataPortMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10)
)
_RcftDataPortObjects_ObjectIdentity = ObjectIdentity
rcftDataPortObjects = _RcftDataPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 1)
)
_RcftDataPortTable_Object = MibTable
rcftDataPortTable = _RcftDataPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 1, 1)
)
if mibBuilder.loadTexts:
    rcftDataPortTable.setStatus("current")
_RcftDataPortEntry_Object = MibTableRow
rcftDataPortEntry = _RcftDataPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 1, 1, 1)
)
rcftDataPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftDataPortIndex"),
)
if mibBuilder.loadTexts:
    rcftDataPortEntry.setStatus("current")
_RcftDataPortIndex_Type = Integer32
_RcftDataPortIndex_Object = MibTableColumn
rcftDataPortIndex = _RcftDataPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 1, 1, 1, 1),
    _RcftDataPortIndex_Type()
)
rcftDataPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDataPortIndex.setStatus("current")
_RcftDataPortStatus_Type = Integer32
_RcftDataPortStatus_Object = MibTableColumn
rcftDataPortStatus = _RcftDataPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 1, 1, 1, 2),
    _RcftDataPortStatus_Type()
)
rcftDataPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftDataPortStatus.setStatus("current")
_RcftDataPortPosition_Type = Integer32
_RcftDataPortPosition_Object = MibTableColumn
rcftDataPortPosition = _RcftDataPortPosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 1, 1, 1, 3),
    _RcftDataPortPosition_Type()
)
rcftDataPortPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDataPortPosition.setStatus("current")
_RcftDataPortType_Type = Integer32
_RcftDataPortType_Object = MibTableColumn
rcftDataPortType = _RcftDataPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 1, 1, 1, 4),
    _RcftDataPortType_Type()
)
rcftDataPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftDataPortType.setStatus("current")
_RcftDataPortPerformance_ObjectIdentity = ObjectIdentity
rcftDataPortPerformance = _RcftDataPortPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 2)
)
_RcftDataPortTraps_ObjectIdentity = ObjectIdentity
rcftDataPortTraps = _RcftDataPortTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 10, 10)
)
_RcftSimpleModuleMib_ObjectIdentity = ObjectIdentity
rcftSimpleModuleMib = _RcftSimpleModuleMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11)
)
_RcftSimpleModuleObjects_ObjectIdentity = ObjectIdentity
rcftSimpleModuleObjects = _RcftSimpleModuleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1)
)
_RcftSimpleModuleTable_Object = MibTable
rcftSimpleModuleTable = _RcftSimpleModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1, 1)
)
if mibBuilder.loadTexts:
    rcftSimpleModuleTable.setStatus("current")
_RcftSimpleModuleEntry_Object = MibTableRow
rcftSimpleModuleEntry = _RcftSimpleModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1, 1, 1)
)
rcftSimpleModuleEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSimpleModuleIndex"),
)
if mibBuilder.loadTexts:
    rcftSimpleModuleEntry.setStatus("current")
_RcftSimpleModuleIndex_Type = Integer32
_RcftSimpleModuleIndex_Object = MibTableColumn
rcftSimpleModuleIndex = _RcftSimpleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1, 1, 1, 1),
    _RcftSimpleModuleIndex_Type()
)
rcftSimpleModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSimpleModuleIndex.setStatus("current")
_RcftSimpleModuleExist_Type = Integer32
_RcftSimpleModuleExist_Object = MibTableColumn
rcftSimpleModuleExist = _RcftSimpleModuleExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1, 1, 1, 2),
    _RcftSimpleModuleExist_Type()
)
rcftSimpleModuleExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSimpleModuleExist.setStatus("current")
_RcftSimpleModulePosition_Type = Integer32
_RcftSimpleModulePosition_Object = MibTableColumn
rcftSimpleModulePosition = _RcftSimpleModulePosition_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1, 1, 1, 3),
    _RcftSimpleModulePosition_Type()
)
rcftSimpleModulePosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSimpleModulePosition.setStatus("current")
_RcftSimpleModuleStatus_Type = Integer32
_RcftSimpleModuleStatus_Object = MibTableColumn
rcftSimpleModuleStatus = _RcftSimpleModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1, 1, 1, 4),
    _RcftSimpleModuleStatus_Type()
)
rcftSimpleModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSimpleModuleStatus.setStatus("current")
_RcftSimpleModuleType_Type = Integer32
_RcftSimpleModuleType_Object = MibTableColumn
rcftSimpleModuleType = _RcftSimpleModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 1, 1, 1, 5),
    _RcftSimpleModuleType_Type()
)
rcftSimpleModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSimpleModuleType.setStatus("current")
_RcftSimpleModulePerformance_ObjectIdentity = ObjectIdentity
rcftSimpleModulePerformance = _RcftSimpleModulePerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 2)
)
_RcftSimpleModuleTraps_ObjectIdentity = ObjectIdentity
rcftSimpleModuleTraps = _RcftSimpleModuleTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 10)
)
_RcftSlotPerformaceMib_ObjectIdentity = ObjectIdentity
rcftSlotPerformaceMib = _RcftSlotPerformaceMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12)
)
_RcftSlotPerformance_ObjectIdentity = ObjectIdentity
rcftSlotPerformance = _RcftSlotPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1)
)
_RcftSlotStatisticTable_Object = MibTable
rcftSlotStatisticTable = _RcftSlotStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1)
)
if mibBuilder.loadTexts:
    rcftSlotStatisticTable.setStatus("current")
_RcftSlotStatisticEntry_Object = MibTableRow
rcftSlotStatisticEntry = _RcftSlotStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1)
)
rcftSlotStatisticEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotStatisticEntry.setStatus("current")
_RcftPortIndex_Type = Integer32
_RcftPortIndex_Object = MibTableColumn
rcftPortIndex = _RcftPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 1),
    _RcftPortIndex_Type()
)
rcftPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPortIndex.setStatus("current")
_RcftPortType_Type = Integer32
_RcftPortType_Object = MibTableColumn
rcftPortType = _RcftPortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 2),
    _RcftPortType_Type()
)
rcftPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftPortType.setStatus("current")
_RcftRxPackets_Type = Counter32
_RcftRxPackets_Object = MibTableColumn
rcftRxPackets = _RcftRxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 3),
    _RcftRxPackets_Type()
)
rcftRxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxPackets.setStatus("current")
_RcftRxLosPackets_Type = Counter32
_RcftRxLosPackets_Object = MibTableColumn
rcftRxLosPackets = _RcftRxLosPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 4),
    _RcftRxLosPackets_Type()
)
rcftRxLosPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxLosPackets.setStatus("current")
_RcftRxPreabErrPackets_Type = Counter32
_RcftRxPreabErrPackets_Object = MibTableColumn
rcftRxPreabErrPackets = _RcftRxPreabErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 5),
    _RcftRxPreabErrPackets_Type()
)
rcftRxPreabErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxPreabErrPackets.setStatus("current")
_RcftRxFCSErrPackets_Type = Counter32
_RcftRxFCSErrPackets_Object = MibTableColumn
rcftRxFCSErrPackets = _RcftRxFCSErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 6),
    _RcftRxFCSErrPackets_Type()
)
rcftRxFCSErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxFCSErrPackets.setStatus("current")
_RcftRxUnderSizePackets_Type = Counter32
_RcftRxUnderSizePackets_Object = MibTableColumn
rcftRxUnderSizePackets = _RcftRxUnderSizePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 7),
    _RcftRxUnderSizePackets_Type()
)
rcftRxUnderSizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxUnderSizePackets.setStatus("current")
_RcftRxOverSizePackets_Type = Counter32
_RcftRxOverSizePackets_Object = MibTableColumn
rcftRxOverSizePackets = _RcftRxOverSizePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 8),
    _RcftRxOverSizePackets_Type()
)
rcftRxOverSizePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxOverSizePackets.setStatus("current")
_RcftRxPausePackets_Type = Counter32
_RcftRxPausePackets_Object = MibTableColumn
rcftRxPausePackets = _RcftRxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 9),
    _RcftRxPausePackets_Type()
)
rcftRxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxPausePackets.setStatus("current")
_RcftRxOamPackets_Type = Counter32
_RcftRxOamPackets_Object = MibTableColumn
rcftRxOamPackets = _RcftRxOamPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 10),
    _RcftRxOamPackets_Type()
)
rcftRxOamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxOamPackets.setStatus("current")
_RcftRxBytes_Type = Counter32
_RcftRxBytes_Object = MibTableColumn
rcftRxBytes = _RcftRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 11),
    _RcftRxBytes_Type()
)
rcftRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftRxBytes.setStatus("current")
_RcftTxPackets_Type = Counter32
_RcftTxPackets_Object = MibTableColumn
rcftTxPackets = _RcftTxPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 12),
    _RcftTxPackets_Type()
)
rcftTxPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftTxPackets.setStatus("current")
_RcftTxFCSErrPackets_Type = Counter32
_RcftTxFCSErrPackets_Object = MibTableColumn
rcftTxFCSErrPackets = _RcftTxFCSErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 13),
    _RcftTxFCSErrPackets_Type()
)
rcftTxFCSErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftTxFCSErrPackets.setStatus("current")
_RcftTxPausePackets_Type = Counter32
_RcftTxPausePackets_Object = MibTableColumn
rcftTxPausePackets = _RcftTxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 14),
    _RcftTxPausePackets_Type()
)
rcftTxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftTxPausePackets.setStatus("current")
_RcftTxOamPackets_Type = Counter32
_RcftTxOamPackets_Object = MibTableColumn
rcftTxOamPackets = _RcftTxOamPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 15),
    _RcftTxOamPackets_Type()
)
rcftTxOamPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftTxOamPackets.setStatus("current")
_RcftTxBytes_Type = Counter32
_RcftTxBytes_Object = MibTableColumn
rcftTxBytes = _RcftTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 16),
    _RcftTxBytes_Type()
)
rcftTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftTxBytes.setStatus("current")
_RcftFluxTimer_Type = Counter32
_RcftFluxTimer_Object = MibTableColumn
rcftFluxTimer = _RcftFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 12, 1, 1, 1, 17),
    _RcftFluxTimer_Type()
)
rcftFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftFluxTimer.setStatus("current")
_RcftSlotVCGMib_ObjectIdentity = ObjectIdentity
rcftSlotVCGMib = _RcftSlotVCGMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13)
)
_RcftSlotVCGObjects_ObjectIdentity = ObjectIdentity
rcftSlotVCGObjects = _RcftSlotVCGObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1)
)
_RcftSlotVCGTable_Object = MibTable
rcftSlotVCGTable = _RcftSlotVCGTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1)
)
if mibBuilder.loadTexts:
    rcftSlotVCGTable.setStatus("current")
_RcftSlotVCGEntry_Object = MibTableRow
rcftSlotVCGEntry = _RcftSlotVCGEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1)
)
rcftSlotVCGEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotVCGEntry.setStatus("current")
_RcftSlotVCGIndex_Type = Integer32
_RcftSlotVCGIndex_Object = MibTableColumn
rcftSlotVCGIndex = _RcftSlotVCGIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 1),
    _RcftSlotVCGIndex_Type()
)
rcftSlotVCGIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGIndex.setStatus("current")
_RcftSlotVCGStatus_Type = Integer32
_RcftSlotVCGStatus_Object = MibTableColumn
rcftSlotVCGStatus = _RcftSlotVCGStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 2),
    _RcftSlotVCGStatus_Type()
)
rcftSlotVCGStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVCGStatus.setStatus("current")
_RcftSlotVCGLoopStatus_Type = Integer32
_RcftSlotVCGLoopStatus_Object = MibTableColumn
rcftSlotVCGLoopStatus = _RcftSlotVCGLoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 3),
    _RcftSlotVCGLoopStatus_Type()
)
rcftSlotVCGLoopStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGLoopStatus.setStatus("current")
_RcftSlotVCGLcasXPR_Type = Integer32
_RcftSlotVCGLcasXPR_Object = MibTableColumn
rcftSlotVCGLcasXPR = _RcftSlotVCGLcasXPR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 4),
    _RcftSlotVCGLcasXPR_Type()
)
rcftSlotVCGLcasXPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGLcasXPR.setStatus("current")
_RcftSlotVCGLcasXAR_Type = Integer32
_RcftSlotVCGLcasXAR_Object = MibTableColumn
rcftSlotVCGLcasXAR = _RcftSlotVCGLcasXAR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 5),
    _RcftSlotVCGLcasXAR_Type()
)
rcftSlotVCGLcasXAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGLcasXAR.setStatus("current")
_RcftSlotVCGLcasXPT_Type = Integer32
_RcftSlotVCGLcasXPT_Object = MibTableColumn
rcftSlotVCGLcasXPT = _RcftSlotVCGLcasXPT_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 6),
    _RcftSlotVCGLcasXPT_Type()
)
rcftSlotVCGLcasXPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGLcasXPT.setStatus("current")
_RcftSlotVCGLcasXAT_Type = Integer32
_RcftSlotVCGLcasXAT_Object = MibTableColumn
rcftSlotVCGLcasXAT = _RcftSlotVCGLcasXAT_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 7),
    _RcftSlotVCGLcasXAT_Type()
)
rcftSlotVCGLcasXAT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGLcasXAT.setStatus("current")
_RcftSlotVCGAlarmStatus_Type = Integer32
_RcftSlotVCGAlarmStatus_Object = MibTableColumn
rcftSlotVCGAlarmStatus = _RcftSlotVCGAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 8),
    _RcftSlotVCGAlarmStatus_Type()
)
rcftSlotVCGAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGAlarmStatus.setStatus("current")
_RcftSlotVCGTxISPTPID_Type = Integer32
_RcftSlotVCGTxISPTPID_Object = MibTableColumn
rcftSlotVCGTxISPTPID = _RcftSlotVCGTxISPTPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 9),
    _RcftSlotVCGTxISPTPID_Type()
)
rcftSlotVCGTxISPTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVCGTxISPTPID.setStatus("current")
_RcftSlotVCGRxISPTPID_Type = Integer32
_RcftSlotVCGRxISPTPID_Object = MibTableColumn
rcftSlotVCGRxISPTPID = _RcftSlotVCGRxISPTPID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 10),
    _RcftSlotVCGRxISPTPID_Type()
)
rcftSlotVCGRxISPTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVCGRxISPTPID.setStatus("current")
_RcftSlotVCGBaseCoS_Type = Integer32
_RcftSlotVCGBaseCoS_Object = MibTableColumn
rcftSlotVCGBaseCoS = _RcftSlotVCGBaseCoS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 11),
    _RcftSlotVCGBaseCoS_Type()
)
rcftSlotVCGBaseCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVCGBaseCoS.setStatus("current")
_RcftSlotVCGVLANID_Type = Integer32
_RcftSlotVCGVLANID_Object = MibTableColumn
rcftSlotVCGVLANID = _RcftSlotVCGVLANID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 12),
    _RcftSlotVCGVLANID_Type()
)
rcftSlotVCGVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVCGVLANID.setStatus("current")


class _RcftSlotVCGMemberList_Type(OctetString):
    """Custom type rcftSlotVCGMemberList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftSlotVCGMemberList_Type.__name__ = "OctetString"
_RcftSlotVCGMemberList_Object = MibTableColumn
rcftSlotVCGMemberList = _RcftSlotVCGMemberList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 13),
    _RcftSlotVCGMemberList_Type()
)
rcftSlotVCGMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVCGMemberList.setStatus("current")


class _RcftSlotToRVCGMemberList_Type(OctetString):
    """Custom type rcftSlotToRVCGMemberList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftSlotToRVCGMemberList_Type.__name__ = "OctetString"
_RcftSlotToRVCGMemberList_Object = MibTableColumn
rcftSlotToRVCGMemberList = _RcftSlotToRVCGMemberList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 14),
    _RcftSlotToRVCGMemberList_Type()
)
rcftSlotToRVCGMemberList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotToRVCGMemberList.setStatus("current")


class _RcftSlotVCGMemberStatus_Type(OctetString):
    """Custom type rcftSlotVCGMemberStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftSlotVCGMemberStatus_Type.__name__ = "OctetString"
_RcftSlotVCGMemberStatus_Object = MibTableColumn
rcftSlotVCGMemberStatus = _RcftSlotVCGMemberStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 15),
    _RcftSlotVCGMemberStatus_Type()
)
rcftSlotVCGMemberStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVCGMemberStatus.setStatus("current")


class _RcftSlotVCGMemberRxCode_Type(OctetString):
    """Custom type rcftSlotVCGMemberRxCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftSlotVCGMemberRxCode_Type.__name__ = "OctetString"
_RcftSlotVCGMemberRxCode_Object = MibTableColumn
rcftSlotVCGMemberRxCode = _RcftSlotVCGMemberRxCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 16),
    _RcftSlotVCGMemberRxCode_Type()
)
rcftSlotVCGMemberRxCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGMemberRxCode.setStatus("current")


class _RcftSlotVCGMemberTxCode_Type(OctetString):
    """Custom type rcftSlotVCGMemberTxCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftSlotVCGMemberTxCode_Type.__name__ = "OctetString"
_RcftSlotVCGMemberTxCode_Object = MibTableColumn
rcftSlotVCGMemberTxCode = _RcftSlotVCGMemberTxCode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 17),
    _RcftSlotVCGMemberTxCode_Type()
)
rcftSlotVCGMemberTxCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGMemberTxCode.setStatus("current")


class _RcftSlotVCGMemberAlarmStatus_Type(OctetString):
    """Custom type rcftSlotVCGMemberAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftSlotVCGMemberAlarmStatus_Type.__name__ = "OctetString"
_RcftSlotVCGMemberAlarmStatus_Object = MibTableColumn
rcftSlotVCGMemberAlarmStatus = _RcftSlotVCGMemberAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 18),
    _RcftSlotVCGMemberAlarmStatus_Type()
)
rcftSlotVCGMemberAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVCGMemberAlarmStatus.setStatus("current")


class _RcftSlotToRVCGMemberAlarmStatus_Type(OctetString):
    """Custom type rcftSlotToRVCGMemberAlarmStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_RcftSlotToRVCGMemberAlarmStatus_Type.__name__ = "OctetString"
_RcftSlotToRVCGMemberAlarmStatus_Object = MibTableColumn
rcftSlotToRVCGMemberAlarmStatus = _RcftSlotToRVCGMemberAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 1, 1, 1, 19),
    _RcftSlotToRVCGMemberAlarmStatus_Type()
)
rcftSlotToRVCGMemberAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotToRVCGMemberAlarmStatus.setStatus("current")
_RcftSlotVCGPerformance_ObjectIdentity = ObjectIdentity
rcftSlotVCGPerformance = _RcftSlotVCGPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2)
)
_RcftSlotVCGStatisticTable_Object = MibTable
rcftSlotVCGStatisticTable = _RcftSlotVCGStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1)
)
if mibBuilder.loadTexts:
    rcftSlotVCGStatisticTable.setStatus("current")
_RcftSlotVCGStatisticEntry_Object = MibTableRow
rcftSlotVCGStatisticEntry = _RcftSlotVCGStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1)
)
if mibBuilder.loadTexts:
    rcftSlotVCGStatisticEntry.setStatus("current")
_RcftVCGRxClientPackets_Type = Counter32
_RcftVCGRxClientPackets_Object = MibTableColumn
rcftVCGRxClientPackets = _RcftVCGRxClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 1),
    _RcftVCGRxClientPackets_Type()
)
rcftVCGRxClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxClientPackets.setStatus("current")
_RcftVCGRxIdlePackets_Type = Counter32
_RcftVCGRxIdlePackets_Object = MibTableColumn
rcftVCGRxIdlePackets = _RcftVCGRxIdlePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 2),
    _RcftVCGRxIdlePackets_Type()
)
rcftVCGRxIdlePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxIdlePackets.setStatus("current")
_RcftVCGRxMgmntPackets_Type = Counter32
_RcftVCGRxMgmntPackets_Object = MibTableColumn
rcftVCGRxMgmntPackets = _RcftVCGRxMgmntPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 3),
    _RcftVCGRxMgmntPackets_Type()
)
rcftVCGRxMgmntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxMgmntPackets.setStatus("current")
_RcftVCGRxFCSErrMgmntPackets_Type = Counter32
_RcftVCGRxFCSErrMgmntPackets_Object = MibTableColumn
rcftVCGRxFCSErrMgmntPackets = _RcftVCGRxFCSErrMgmntPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 4),
    _RcftVCGRxFCSErrMgmntPackets_Type()
)
rcftVCGRxFCSErrMgmntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxFCSErrMgmntPackets.setStatus("current")
_RcftVCGRxLenErrPackets_Type = Counter32
_RcftVCGRxLenErrPackets_Object = MibTableColumn
rcftVCGRxLenErrPackets = _RcftVCGRxLenErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 5),
    _RcftVCGRxLenErrPackets_Type()
)
rcftVCGRxLenErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxLenErrPackets.setStatus("current")
_RcftVCGRxFCSErrClientPackets_Type = Counter32
_RcftVCGRxFCSErrClientPackets_Object = MibTableColumn
rcftVCGRxFCSErrClientPackets = _RcftVCGRxFCSErrClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 6),
    _RcftVCGRxFCSErrClientPackets_Type()
)
rcftVCGRxFCSErrClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxFCSErrClientPackets.setStatus("current")
_RcftVCGRxThecErrPackets_Type = Counter32
_RcftVCGRxThecErrPackets_Object = MibTableColumn
rcftVCGRxThecErrPackets = _RcftVCGRxThecErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 7),
    _RcftVCGRxThecErrPackets_Type()
)
rcftVCGRxThecErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxThecErrPackets.setStatus("current")
_RcftVCGRxEhecErrPackets_Type = Counter32
_RcftVCGRxEhecErrPackets_Object = MibTableColumn
rcftVCGRxEhecErrPackets = _RcftVCGRxEhecErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 8),
    _RcftVCGRxEhecErrPackets_Type()
)
rcftVCGRxEhecErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxEhecErrPackets.setStatus("current")
_RcftVCGRxCIDErrPackets_Type = Counter32
_RcftVCGRxCIDErrPackets_Object = MibTableColumn
rcftVCGRxCIDErrPackets = _RcftVCGRxCIDErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 9),
    _RcftVCGRxCIDErrPackets_Type()
)
rcftVCGRxCIDErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxCIDErrPackets.setStatus("current")
_RcftVCGRxSpareErrPackets_Type = Counter32
_RcftVCGRxSpareErrPackets_Object = MibTableColumn
rcftVCGRxSpareErrPackets = _RcftVCGRxSpareErrPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 10),
    _RcftVCGRxSpareErrPackets_Type()
)
rcftVCGRxSpareErrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxSpareErrPackets.setStatus("current")
_RcftVCGRxChecCorPackets_Type = Counter32
_RcftVCGRxChecCorPackets_Object = MibTableColumn
rcftVCGRxChecCorPackets = _RcftVCGRxChecCorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 11),
    _RcftVCGRxChecCorPackets_Type()
)
rcftVCGRxChecCorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxChecCorPackets.setStatus("current")
_RcftVCGRxThecCorPackets_Type = Counter32
_RcftVCGRxThecCorPackets_Object = MibTableColumn
rcftVCGRxThecCorPackets = _RcftVCGRxThecCorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 12),
    _RcftVCGRxThecCorPackets_Type()
)
rcftVCGRxThecCorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxThecCorPackets.setStatus("current")
_RcftVCGRxEhecCorPackets_Type = Counter32
_RcftVCGRxEhecCorPackets_Object = MibTableColumn
rcftVCGRxEhecCorPackets = _RcftVCGRxEhecCorPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 13),
    _RcftVCGRxEhecCorPackets_Type()
)
rcftVCGRxEhecCorPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxEhecCorPackets.setStatus("current")
_RcftVCGRxBytes_Type = Counter32
_RcftVCGRxBytes_Object = MibTableColumn
rcftVCGRxBytes = _RcftVCGRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 14),
    _RcftVCGRxBytes_Type()
)
rcftVCGRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGRxBytes.setStatus("current")
_RcftVCGTxClientPackets_Type = Counter32
_RcftVCGTxClientPackets_Object = MibTableColumn
rcftVCGTxClientPackets = _RcftVCGTxClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 15),
    _RcftVCGTxClientPackets_Type()
)
rcftVCGTxClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGTxClientPackets.setStatus("current")
_RcftVCGTxIdlePackets_Type = Counter32
_RcftVCGTxIdlePackets_Object = MibTableColumn
rcftVCGTxIdlePackets = _RcftVCGTxIdlePackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 16),
    _RcftVCGTxIdlePackets_Type()
)
rcftVCGTxIdlePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGTxIdlePackets.setStatus("current")
_RcftVCGTxMgmntPackets_Type = Counter32
_RcftVCGTxMgmntPackets_Object = MibTableColumn
rcftVCGTxMgmntPackets = _RcftVCGTxMgmntPackets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 17),
    _RcftVCGTxMgmntPackets_Type()
)
rcftVCGTxMgmntPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGTxMgmntPackets.setStatus("current")
_RcftVCGTxBytes_Type = Counter32
_RcftVCGTxBytes_Object = MibTableColumn
rcftVCGTxBytes = _RcftVCGTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 18),
    _RcftVCGTxBytes_Type()
)
rcftVCGTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGTxBytes.setStatus("current")
_RcftVCGFluxTimer_Type = Counter32
_RcftVCGFluxTimer_Object = MibTableColumn
rcftVCGFluxTimer = _RcftVCGFluxTimer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 2, 1, 1, 19),
    _RcftVCGFluxTimer_Type()
)
rcftVCGFluxTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftVCGFluxTimer.setStatus("current")
_RcftSlotVCGTraps_ObjectIdentity = ObjectIdentity
rcftSlotVCGTraps = _RcftSlotVCGTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10)
)
_RcftSlotVLANMib_ObjectIdentity = ObjectIdentity
rcftSlotVLANMib = _RcftSlotVLANMib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14)
)
_RcftSlotVLANObjects_ObjectIdentity = ObjectIdentity
rcftSlotVLANObjects = _RcftSlotVLANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14, 1)
)
_RcftSlotVLANTable_Object = MibTable
rcftSlotVLANTable = _RcftSlotVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14, 1, 1)
)
if mibBuilder.loadTexts:
    rcftSlotVLANTable.setStatus("current")
_RcftSlotVLANEntry_Object = MibTableRow
rcftSlotVLANEntry = _RcftSlotVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14, 1, 1, 1)
)
rcftSlotVLANEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVLANIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotVLANEntry.setStatus("current")
_RcftSlotVLANIndex_Type = Integer32
_RcftSlotVLANIndex_Object = MibTableColumn
rcftSlotVLANIndex = _RcftSlotVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14, 1, 1, 1, 1),
    _RcftSlotVLANIndex_Type()
)
rcftSlotVLANIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotVLANIndex.setStatus("current")
_RcftSlotVLANStatus_Type = Integer32
_RcftSlotVLANStatus_Object = MibTableColumn
rcftSlotVLANStatus = _RcftSlotVLANStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14, 1, 1, 1, 2),
    _RcftSlotVLANStatus_Type()
)
rcftSlotVLANStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVLANStatus.setStatus("current")
_RcftSlotVLANmember_Type = Integer32
_RcftSlotVLANmember_Object = MibTableColumn
rcftSlotVLANmember = _RcftSlotVLANmember_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14, 1, 1, 1, 3),
    _RcftSlotVLANmember_Type()
)
rcftSlotVLANmember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVLANmember.setStatus("current")
_RcftSlotVID_Type = Integer32
_RcftSlotVID_Object = MibTableColumn
rcftSlotVID = _RcftSlotVID_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 14, 1, 1, 1, 4),
    _RcftSlotVID_Type()
)
rcftSlotVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcftSlotVID.setStatus("current")
rcftEthFxPortEntry.registerAugmentions(
    ("RC002-LOCAL-DEVICE-PORT-MIB",
     "rcftEthFxStatisticEntry")
)
rcftEthFxStatisticEntry.setIndexNames(*rcftEthFxPortEntry.getIndexNames())
rcftEthFePortEntry.registerAugmentions(
    ("RC002-LOCAL-DEVICE-PORT-MIB",
     "rcftEthFeStatisticEntry")
)
rcftEthFeStatisticEntry.setIndexNames(*rcftEthFePortEntry.getIndexNames())
rcftDS3E3PortEntry.registerAugmentions(
    ("RC002-LOCAL-DEVICE-PORT-MIB",
     "rcftDS3E3StatisticEntry")
)
rcftDS3E3StatisticEntry.setIndexNames(*rcftDS3E3PortEntry.getIndexNames())
rcftDS1PortEntry.registerAugmentions(
    ("RC002-LOCAL-DEVICE-PORT-MIB",
     "rcftDS1StatisticEntry")
)
rcftDS1StatisticEntry.setIndexNames(*rcftDS1PortEntry.getIndexNames())
rcftSlotVCGEntry.registerAugmentions(
    ("RC002-LOCAL-DEVICE-PORT-MIB",
     "rcftSlotVCGStatisticEntry")
)
rcftSlotVCGStatisticEntry.setIndexNames(*rcftSlotVCGEntry.getIndexNames())

# Managed Objects groups


# Notification objects

rcftEthFxPortLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 1)
)
rcftEthFxPortLinkTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortLinkTrap.setStatus(
        "current"
    )

rcftEthFxPortExitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 2)
)
rcftEthFxPortExitTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortExitTrap.setStatus(
        "current"
    )

rcftEthFxPortTempHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 3)
)
rcftEthFxPortTempHighTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortTempHighTrap.setStatus(
        "current"
    )

rcftEthFxPortTempLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 4)
)
rcftEthFxPortTempLowTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortTempLowTrap.setStatus(
        "current"
    )

rcftEthFxPortVoltageHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 5)
)
rcftEthFxPortVoltageHighTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortVoltageHighTrap.setStatus(
        "current"
    )

rcftEthFxPortVoltageLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 6)
)
rcftEthFxPortVoltageLowTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortVoltageLowTrap.setStatus(
        "current"
    )

rcftEthFxPortOffsetCurrHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 7)
)
rcftEthFxPortOffsetCurrHighTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortOffsetCurrHighTrap.setStatus(
        "current"
    )

rcftEthFxPortOffsetCurrLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 8)
)
rcftEthFxPortOffsetCurrLowTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortOffsetCurrLowTrap.setStatus(
        "current"
    )

rcftEthFxPortSendPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 9)
)
rcftEthFxPortSendPowerHighTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortSendPowerHighTrap.setStatus(
        "current"
    )

rcftEthFxPortSendPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 10)
)
rcftEthFxPortSendPowerLowTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortSendPowerLowTrap.setStatus(
        "current"
    )

rcftEthFxPortRecvPowerHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 11)
)
rcftEthFxPortRecvPowerHighTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortRecvPowerHighTrap.setStatus(
        "current"
    )

rcftEthFxPortRecvPowerLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 12)
)
rcftEthFxPortRecvPowerLowTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortRecvPowerLowTrap.setStatus(
        "current"
    )

rcftEthFxPortTempHighWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 13)
)
rcftEthFxPortTempHighWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortTempHighWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortTempLowWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 14)
)
rcftEthFxPortTempLowWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortTempLowWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortVoltageHighWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 15)
)
rcftEthFxPortVoltageHighWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortVoltageHighWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortVoltageLowWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 16)
)
rcftEthFxPortVoltageLowWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortVoltageLowWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortOffsetCurrHighWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 17)
)
rcftEthFxPortOffsetCurrHighWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortOffsetCurrHighWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortOffsetCurrLowWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 18)
)
rcftEthFxPortOffsetCurrLowWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortOffsetCurrLowWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortSendPowerHighWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 19)
)
rcftEthFxPortSendPowerHighWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortSendPowerHighWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortSendPowerLowWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 20)
)
rcftEthFxPortSendPowerLowWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortSendPowerLowWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortRecvPowerHighWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 21)
)
rcftEthFxPortRecvPowerHighWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortRecvPowerHighWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortRecvPowerLowWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 22)
)
rcftEthFxPortRecvPowerLowWarningTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPDiagnoWarningStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortRecvPowerLowWarningTrap.setStatus(
        "current"
    )

rcftEthFxPortSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 23)
)
rcftEthFxPortSDTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortSDTrap.setStatus(
        "current"
    )

rcftEthFxPortRemotePowerDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 24)
)
rcftEthFxPortRemotePowerDownTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortRemotePowerDownTrap.setStatus(
        "current"
    )

rcftEthFxPortLaserTxfaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 25)
)
rcftEthFxPortLaserTxfaultTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPInfo")
)
if mibBuilder.loadTexts:
    rcftEthFxPortLaserTxfaultTrap.setStatus(
        "current"
    )

rcftEthFxPortInputSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 26)
)
rcftEthFxPortInputSignalLosTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortSFPInfo")
)
if mibBuilder.loadTexts:
    rcftEthFxPortInputSignalLosTrap.setStatus(
        "current"
    )

rcftEthFxPortLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 27)
)
rcftEthFxPortLOLTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortLOLTrap.setStatus(
        "current"
    )

rcftEthFxPortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 1, 10, 28)
)
rcftEthFxPortLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFxPortStatus")
)
if mibBuilder.loadTexts:
    rcftEthFxPortLOSTrap.setStatus(
        "current"
    )

rcftEthFePortLinkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 1, 2, 10, 1)
)
rcftEthFePortLinkTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftEthFePortStatus")
)
if mibBuilder.loadTexts:
    rcftEthFePortLinkTrap.setStatus(
        "current"
    )

rcftPdhPortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 1)
)
rcftPdhPortLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortLOSTrap.setStatus(
        "current"
    )

rcftPdhPortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 2)
)
rcftPdhPortLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortLOFTrap.setStatus(
        "current"
    )

rcftPdhPortE3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 3)
)
rcftPdhPortE3Trap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortE3Trap.setStatus(
        "current"
    )

rcftPdhPortE6Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 4)
)
rcftPdhPortE6Trap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortE6Trap.setStatus(
        "current"
    )

rcftPdhPortToRLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 5)
)
rcftPdhPortToRLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortToRLOSTrap.setStatus(
        "current"
    )

rcftPdhPortToRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 6)
)
rcftPdhPortToRLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortToRLOFTrap.setStatus(
        "current"
    )

rcftPdhPortToRE3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 7)
)
rcftPdhPortToRE3Trap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortToRE3Trap.setStatus(
        "current"
    )

rcftPdhPortToRE6Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 8)
)
rcftPdhPortToRE6Trap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortToRE6Trap.setStatus(
        "current"
    )

rcftPdhPortToRPowerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 2, 10, 9)
)
rcftPdhPortToRPowerDown.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftPdhPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftPdhPortToRPowerDown.setStatus(
        "current"
    )

rcftE1PortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 1)
)
rcftE1PortLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortLOSTrap.setStatus(
        "current"
    )

rcftE1PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 2)
)
rcftE1PortAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortAISTrap.setStatus(
        "current"
    )

rcftE1PortCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 3)
)
rcftE1PortCVTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortCVTrap.setStatus(
        "current"
    )

rcftE1PortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 4)
)
rcftE1PortLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortLOFTrap.setStatus(
        "current"
    )

rcftE1PortLOMFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 5)
)
rcftE1PortLOMFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortLOMFTrap.setStatus(
        "current"
    )

rcftE1PortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 6)
)
rcftE1PortCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortCRCTrap.setStatus(
        "current"
    )

rcftE1PortToRLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 7)
)
rcftE1PortToRLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortToRLOSTrap.setStatus(
        "current"
    )

rcftT1PortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 8)
)
rcftT1PortLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftT1PortLOSTrap.setStatus(
        "current"
    )

rcftT1PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 9)
)
rcftT1PortAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftT1PortAISTrap.setStatus(
        "current"
    )

rcftE1PortTSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 10)
)
rcftE1PortTSDTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortTSDTrap.setStatus(
        "current"
    )

rcftE1PortTransErrorCodeMore10E_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 11)
)
rcftE1PortTransErrorCodeMore10E_3.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortErrorRate")
)
if mibBuilder.loadTexts:
    rcftE1PortTransErrorCodeMore10E_3.setStatus(
        "current"
    )

rcftE1PortTransErrorCodeMore10E_6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 12)
)
rcftE1PortTransErrorCodeMore10E_6.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortErrorRate")
)
if mibBuilder.loadTexts:
    rcftE1PortTransErrorCodeMore10E_6.setStatus(
        "current"
    )

rcftE1PortRDITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 13)
)
rcftE1PortRDITrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortRDITrap.setStatus(
        "current"
    )

rcftE1PortToRAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 14)
)
rcftE1PortToRAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortToRAISTrap.setStatus(
        "current"
    )

rcftE1PortToRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 15)
)
rcftE1PortToRLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortToRLOFTrap.setStatus(
        "current"
    )

rcftE1PortToRCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 16)
)
rcftE1PortToRCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortToRCRCTrap.setStatus(
        "current"
    )

rcftE1PortToRTSDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 17)
)
rcftE1PortToRTSDTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortToRTSDTrap.setStatus(
        "current"
    )

rcftE1PortToRLOMFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 18)
)
rcftE1PortToRLOMFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcfT1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortToRLOMFTrap.setStatus(
        "current"
    )

rcftE1PortTransErrorCodeMoreToR10E_3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 3, 10, 19)
)
rcftE1PortTransErrorCodeMoreToR10E_3.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftE1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftE1PortTransErrorCodeMoreToR10E_3.setStatus(
        "current"
    )

rcftV35PortDCDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 1)
)
rcftV35PortDCDTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortDCDTrap.setStatus(
        "current"
    )

rcftV35PortCTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 2)
)
rcftV35PortCTSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortCTSTrap.setStatus(
        "current"
    )

rcftV35PortDTRTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 3)
)
rcftV35PortDTRTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortDTRTrap.setStatus(
        "current"
    )

rcftV35PortRTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 4)
)
rcftV35PortRTSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortRTSTrap.setStatus(
        "current"
    )

rcftV35PortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 5)
)
rcftV35PortCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortCRCTrap.setStatus(
        "current"
    )

rcftV35PortPATTTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 6)
)
rcftV35PortPATTTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortPATTTrap.setStatus(
        "current"
    )

rcftV35PortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 7)
)
rcftV35PortLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortLOFTrap.setStatus(
        "current"
    )

rcftV35PortCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 8)
)
rcftV35PortCVTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortCVTrap.setStatus(
        "current"
    )

rcftV35PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 9)
)
rcftV35PortAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortAISTrap.setStatus(
        "current"
    )

rcftV35PortToRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 10)
)
rcftV35PortToRLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortToRLOFTrap.setStatus(
        "current"
    )

rcftV35PortToRCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 11)
)
rcftV35PortToRCVTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortToRCVTrap.setStatus(
        "current"
    )

rcftV35PortToRAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 12)
)
rcftV35PortToRAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortToRAISTrap.setStatus(
        "current"
    )

rcftV35PortDSRTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 4, 10, 13)
)
rcftV35PortDSRTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftV35PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftV35PortDSRTrap.setStatus(
        "current"
    )

rcftSHDSLPortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 1)
)
rcftSHDSLPortLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortLOSTrap.setStatus(
        "current"
    )

rcftSHDSLPortLOSWTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 2)
)
rcftSHDSLPortLOSWTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortLOSWTrap.setStatus(
        "current"
    )

rcftSHDSLPortLINKTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 3)
)
rcftSHDSLPortLINKTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortLINKTrap.setStatus(
        "current"
    )

rcftSHDSLPortFECTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 4)
)
rcftSHDSLPortFECTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortFECTrap.setStatus(
        "current"
    )

rcftSHDSLPortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 5)
)
rcftSHDSLPortCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortCRCTrap.setStatus(
        "current"
    )

rcftSHDSLPortSNRThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 6)
)
rcftSHDSLPortSNRThresholdTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortSNRThreshold")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortSNRThresholdTrap.setStatus(
        "current"
    )

rcftSHDSLPortAttenuationThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 7)
)
rcftSHDSLPortAttenuationThresholdTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortAttenuationThreshold")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortAttenuationThresholdTrap.setStatus(
        "current"
    )

rcftSHDSLPortLOSThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 8)
)
rcftSHDSLPortLOSThresholdTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortLOSThreshold")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortLOSThresholdTrap.setStatus(
        "current"
    )

rcftSHDSLPortLOSWThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 9)
)
rcftSHDSLPortLOSWThresholdTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortLOSWThreshold")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortLOSWThresholdTrap.setStatus(
        "current"
    )

rcftSHDSLPortLOLKThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 10)
)
rcftSHDSLPortLOLKThresholdTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortLOLKThreshold")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortLOLKThresholdTrap.setStatus(
        "current"
    )

rcftSHDSLPortESThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 5, 10, 11)
)
rcftSHDSLPortESThresholdTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSHDSLPortESThreshold")
)
if mibBuilder.loadTexts:
    rcftSHDSLPortESThresholdTrap.setStatus(
        "current"
    )

rcftDS3E3PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 1)
)
rcftDS3E3PortAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortAISTrap.setStatus(
        "current"
    )

rcftDS3E3PortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 2)
)
rcftDS3E3PortLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortLOSTrap.setStatus(
        "current"
    )

rcftDS3E3PortLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 3)
)
rcftDS3E3PortLOLTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortLOLTrap.setStatus(
        "current"
    )

rcftDS3E3PortDMOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 4)
)
rcftDS3E3PortDMOTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortDMOTrap.setStatus(
        "current"
    )

rcftDS3E3PortCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 5)
)
rcftDS3E3PortCVTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortCVTrap.setStatus(
        "current"
    )

rcftDS3E3PortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 6)
)
rcftDS3E3PortCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortCRCTrap.setStatus(
        "current"
    )

rcftDS3E3PortToRAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 7)
)
rcftDS3E3PortToRAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRAISTrap.setStatus(
        "current"
    )

rcftDS3E3PortToRLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 8)
)
rcftDS3E3PortToRLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRLOSTrap.setStatus(
        "current"
    )

rcftDS3E3PortToRLOLTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 9)
)
rcftDS3E3PortToRLOLTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRLOLTrap.setStatus(
        "current"
    )

rcftDS3E3PortToRDMOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 10)
)
rcftDS3E3PortToRDMOTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRDMOTrap.setStatus(
        "current"
    )

rcftDS3E3PortToRCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 11)
)
rcftDS3E3PortToRCVTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRCVTrap.setStatus(
        "current"
    )

rcftDS3E3PortToRCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 12)
)
rcftDS3E3PortToRCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRCRCTrap.setStatus(
        "current"
    )

rcftDS3E3PortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 13)
)
rcftDS3E3PortLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortLOFTrap.setStatus(
        "current"
    )

rcftDS3E3PortToRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 14)
)
rcftDS3E3PortToRLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRLOFTrap.setStatus(
        "current"
    )

rcftDS3E3PortRAITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 15)
)
rcftDS3E3PortRAITrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortRAITrap.setStatus(
        "current"
    )

rcftDS3E3PortToRRAITrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 16)
)
rcftDS3E3PortToRRAITrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToRRAITrap.setStatus(
        "current"
    )

rcftDS3E3PortOOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 17)
)
rcftDS3E3PortOOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortOOFTrap.setStatus(
        "current"
    )

rcftDS3E3PortToROOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 7, 10, 18)
)
rcftDS3E3PortToROOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS3E3PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS3E3PortToROOFTrap.setStatus(
        "current"
    )

rcftDS1PortAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 1)
)
rcftDS1PortAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortAISTrap.setStatus(
        "current"
    )

rcftDS1PortLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 2)
)
rcftDS1PortLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortLOSTrap.setStatus(
        "current"
    )

rcftDS1PortToRAISTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 3)
)
rcftDS1PortToRAISTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortToRAISTrap.setStatus(
        "current"
    )

rcftDS1PortToRLOSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 4)
)
rcftDS1PortToRLOSTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortToRLOSTrap.setStatus(
        "current"
    )

rcftDS1PortLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 5)
)
rcftDS1PortLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortLOFTrap.setStatus(
        "current"
    )

rcftDS1PortCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 6)
)
rcftDS1PortCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortCRCTrap.setStatus(
        "current"
    )

rcftDS1PortToRLOFTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 7)
)
rcftDS1PortToRLOFTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortToRLOFTrap.setStatus(
        "current"
    )

rcftDS1PortToRCRCTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 8)
)
rcftDS1PortToRCRCTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortToRCRCTrap.setStatus(
        "current"
    )

rcftDS1PortFaultPassIndicatorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 9)
)
rcftDS1PortFaultPassIndicatorTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortFaultPassIndicator")
)
if mibBuilder.loadTexts:
    rcftDS1PortFaultPassIndicatorTrap.setStatus(
        "current"
    )

rcftDS1PortDMOTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 10)
)
rcftDS1PortDMOTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortDMOTrap.setStatus(
        "current"
    )

rcftDS1PortCVTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 11)
)
rcftDS1PortCVTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortCVTrap.setStatus(
        "current"
    )

rcftDS1PortYELTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 12)
)
rcftDS1PortYELTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortYELTrap.setStatus(
        "current"
    )

rcftDS1PortREDTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 8, 10, 13)
)
rcftDS1PortREDTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftDS1PortAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftDS1PortREDTrap.setStatus(
        "current"
    )

rcftVideoPortSignalLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 10, 1)
)
rcftVideoPortSignalLosTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftVideoPortStatus")
)
if mibBuilder.loadTexts:
    rcftVideoPortSignalLosTrap.setStatus(
        "current"
    )

rcftVideoPortSignalInLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 10, 2)
)
rcftVideoPortSignalInLosTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftVideoPortStatus")
)
if mibBuilder.loadTexts:
    rcftVideoPortSignalInLosTrap.setStatus(
        "current"
    )

rcftVideoPortSignalOutLosTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 9, 10, 3)
)
rcftVideoPortSignalOutLosTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftVideoPortStatus")
)
if mibBuilder.loadTexts:
    rcftVideoPortSignalOutLosTrap.setStatus(
        "current"
    )

rcftSimpleModuleShutDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 11, 10, 1)
)
rcftSimpleModuleShutDownTrap.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSimpleModuleStatus")
)
if mibBuilder.loadTexts:
    rcftSimpleModuleShutDownTrap.setStatus(
        "current"
    )

rcftSlotVCGGIDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 1)
)
rcftSlotVCGGIDTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGGIDTraps.setStatus(
        "current"
    )

rcftSlotVCGLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 2)
)
rcftSlotVCGLOATraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGLOATraps.setStatus(
        "current"
    )

rcftSlotVCGLFDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 3)
)
rcftSlotVCGLFDTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGLFDTraps.setStatus(
        "current"
    )

rcftSlotVCGCSFTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 4)
)
rcftSlotVCGCSFTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGCSFTraps.setStatus(
        "current"
    )

rcftSlotVCGTLCTTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 5)
)
rcftSlotVCGTLCTTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGTLCTTraps.setStatus(
        "current"
    )

rcftSlotVCGTLCRTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 6)
)
rcftSlotVCGTLCRTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGTLCRTraps.setStatus(
        "current"
    )

rcftSlotVCGToRGIDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 7)
)
rcftSlotVCGToRGIDTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGToRGIDTraps.setStatus(
        "current"
    )

rcftSlotVCGToRLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 8)
)
rcftSlotVCGToRLOATraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGToRLOATraps.setStatus(
        "current"
    )

rcftSlotVCGToRLFDTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 9)
)
rcftSlotVCGToRLFDTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGToRLFDTraps.setStatus(
        "current"
    )

rcftSlotVCGMemberLOMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 10)
)
rcftSlotVCGMemberLOMTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGMemberLOMTraps.setStatus(
        "current"
    )

rcftSlotVCGMemberSQMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 11)
)
rcftSlotVCGMemberSQMTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGMemberSQMTraps.setStatus(
        "current"
    )

rcftSlotVCGMemberCRCTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 12)
)
rcftSlotVCGMemberCRCTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGMemberCRCTraps.setStatus(
        "current"
    )

rcftSlotVCGMemberLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 13)
)
rcftSlotVCGMemberLOATraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotToRVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGMemberLOATraps.setStatus(
        "current"
    )

rcftSlotVCGToRMemberLOMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 14)
)
rcftSlotVCGToRMemberLOMTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotToRVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGToRMemberLOMTraps.setStatus(
        "current"
    )

rcftSlotVCGToRMemberSQMTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 15)
)
rcftSlotVCGToRMemberSQMTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotToRVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGToRMemberSQMTraps.setStatus(
        "current"
    )

rcftSlotVCGToRMemberCRCTraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 16)
)
rcftSlotVCGToRMemberCRCTraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotToRVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGToRMemberCRCTraps.setStatus(
        "current"
    )

rcftSlotVCGToRMemberLOATraps = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 10, 13, 10, 17)
)
rcftSlotVCGToRMemberLOATraps.setObjects(
    ("RC002-LOCAL-DEVICE-PORT-MIB", "rcftSlotToRVCGMemberAlarmStatus")
)
if mibBuilder.loadTexts:
    rcftSlotVCGToRMemberLOATraps.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC002-LOCAL-DEVICE-PORT-MIB",
    **{"rcftSlotPortMib": rcftSlotPortMib,
       "rcftEthPortMib": rcftEthPortMib,
       "rcftEthFxPortMib": rcftEthFxPortMib,
       "rcftEthFxPortObjects": rcftEthFxPortObjects,
       "rcftEthFxPortTable": rcftEthFxPortTable,
       "rcftEthFxPortEntry": rcftEthFxPortEntry,
       "rcftEthFxPortIndex": rcftEthFxPortIndex,
       "rcftEthFxPortStatus": rcftEthFxPortStatus,
       "rcftEthFxPortModuleMaxSpeed": rcftEthFxPortModuleMaxSpeed,
       "rcftEthFxPortConnectorType": rcftEthFxPortConnectorType,
       "rcftEthFxPortTransmitMedia": rcftEthFxPortTransmitMedia,
       "rcftEthFxPortModuleWaveLen": rcftEthFxPortModuleWaveLen,
       "rcftEthFxPortModuleManufacturer": rcftEthFxPortModuleManufacturer,
       "rcftEthFxPortModuleDescr": rcftEthFxPortModuleDescr,
       "rcftEthFxPortModuleVersion": rcftEthFxPortModuleVersion,
       "rcftEthFxPortModuleSerialNumber": rcftEthFxPortModuleSerialNumber,
       "rcftEthFxPortModuleType": rcftEthFxPortModuleType,
       "rcftEthFxPortRxRestrictSpeed": rcftEthFxPortRxRestrictSpeed,
       "rcftEthFxPortTxRestrictSpeed": rcftEthFxPortTxRestrictSpeed,
       "rcftEthFxPortRestrictSpeedStep": rcftEthFxPortRestrictSpeedStep,
       "rcftEthFxPortLoopOrder": rcftEthFxPortLoopOrder,
       "rcftEthFxPortLoopStatus": rcftEthFxPortLoopStatus,
       "rcftEthFxPortSFPDiagnoInfo": rcftEthFxPortSFPDiagnoInfo,
       "rcftEthFxPortSFPDiagnoAlarmStatus": rcftEthFxPortSFPDiagnoAlarmStatus,
       "rcftEthFxPortSFPDiagnoWarningStatus": rcftEthFxPortSFPDiagnoWarningStatus,
       "rcftEthFxPortTranDistance": rcftEthFxPortTranDistance,
       "rcftEthFxPortSFPType": rcftEthFxPortSFPType,
       "rcftEthFxPortSFPInfo": rcftEthFxPortSFPInfo,
       "rcftEthFxPortPVID": rcftEthFxPortPVID,
       "rcftEthFxPorttag": rcftEthFxPorttag,
       "rcftEthFxPortCOS": rcftEthFxPortCOS,
       "rcftEthFxPortPerformance": rcftEthFxPortPerformance,
       "rcftEthFxStatisticTable": rcftEthFxStatisticTable,
       "rcftEthFxStatisticEntry": rcftEthFxStatisticEntry,
       "rcftEthFxTxPackets": rcftEthFxTxPackets,
       "rcftEthFxRxPackets": rcftEthFxRxPackets,
       "rcftEthFxTxErrPackets": rcftEthFxTxErrPackets,
       "rcftEthFxRxErrPackets": rcftEthFxRxErrPackets,
       "rcftEthFxFluxTimer": rcftEthFxFluxTimer,
       "rcftEthFxRxBytes": rcftEthFxRxBytes,
       "rcftEthFxTxBytes": rcftEthFxTxBytes,
       "rcftEthFx64RxBytes": rcftEthFx64RxBytes,
       "rcftEthFx64TxBytes": rcftEthFx64TxBytes,
       "rcftEthFxPortTraps": rcftEthFxPortTraps,
       "rcftEthFxPortLinkTrap": rcftEthFxPortLinkTrap,
       "rcftEthFxPortExitTrap": rcftEthFxPortExitTrap,
       "rcftEthFxPortTempHighTrap": rcftEthFxPortTempHighTrap,
       "rcftEthFxPortTempLowTrap": rcftEthFxPortTempLowTrap,
       "rcftEthFxPortVoltageHighTrap": rcftEthFxPortVoltageHighTrap,
       "rcftEthFxPortVoltageLowTrap": rcftEthFxPortVoltageLowTrap,
       "rcftEthFxPortOffsetCurrHighTrap": rcftEthFxPortOffsetCurrHighTrap,
       "rcftEthFxPortOffsetCurrLowTrap": rcftEthFxPortOffsetCurrLowTrap,
       "rcftEthFxPortSendPowerHighTrap": rcftEthFxPortSendPowerHighTrap,
       "rcftEthFxPortSendPowerLowTrap": rcftEthFxPortSendPowerLowTrap,
       "rcftEthFxPortRecvPowerHighTrap": rcftEthFxPortRecvPowerHighTrap,
       "rcftEthFxPortRecvPowerLowTrap": rcftEthFxPortRecvPowerLowTrap,
       "rcftEthFxPortTempHighWarningTrap": rcftEthFxPortTempHighWarningTrap,
       "rcftEthFxPortTempLowWarningTrap": rcftEthFxPortTempLowWarningTrap,
       "rcftEthFxPortVoltageHighWarningTrap": rcftEthFxPortVoltageHighWarningTrap,
       "rcftEthFxPortVoltageLowWarningTrap": rcftEthFxPortVoltageLowWarningTrap,
       "rcftEthFxPortOffsetCurrHighWarningTrap": rcftEthFxPortOffsetCurrHighWarningTrap,
       "rcftEthFxPortOffsetCurrLowWarningTrap": rcftEthFxPortOffsetCurrLowWarningTrap,
       "rcftEthFxPortSendPowerHighWarningTrap": rcftEthFxPortSendPowerHighWarningTrap,
       "rcftEthFxPortSendPowerLowWarningTrap": rcftEthFxPortSendPowerLowWarningTrap,
       "rcftEthFxPortRecvPowerHighWarningTrap": rcftEthFxPortRecvPowerHighWarningTrap,
       "rcftEthFxPortRecvPowerLowWarningTrap": rcftEthFxPortRecvPowerLowWarningTrap,
       "rcftEthFxPortSDTrap": rcftEthFxPortSDTrap,
       "rcftEthFxPortRemotePowerDownTrap": rcftEthFxPortRemotePowerDownTrap,
       "rcftEthFxPortLaserTxfaultTrap": rcftEthFxPortLaserTxfaultTrap,
       "rcftEthFxPortInputSignalLosTrap": rcftEthFxPortInputSignalLosTrap,
       "rcftEthFxPortLOLTrap": rcftEthFxPortLOLTrap,
       "rcftEthFxPortLOSTrap": rcftEthFxPortLOSTrap,
       "rcftEthFePortMib": rcftEthFePortMib,
       "rcftEthFePortObjects": rcftEthFePortObjects,
       "rcftEthFePortTable": rcftEthFePortTable,
       "rcftEthFePortEntry": rcftEthFePortEntry,
       "rcftEthFePortIndex": rcftEthFePortIndex,
       "rcftEthFePortStatus": rcftEthFePortStatus,
       "rcftEthFePortRxRestrictSpeed": rcftEthFePortRxRestrictSpeed,
       "rcftEthFePortTxRestrictSpeed": rcftEthFePortTxRestrictSpeed,
       "rcftEthFePortRestrictSpeedStep": rcftEthFePortRestrictSpeedStep,
       "rcftEthFePortOrder": rcftEthFePortOrder,
       "rcftEthFePortPosition": rcftEthFePortPosition,
       "rcftEthFePortPVID": rcftEthFePortPVID,
       "rcftEthFePorttag": rcftEthFePorttag,
       "rcftEthFePortCOS": rcftEthFePortCOS,
       "rcftEthFePortPerformance": rcftEthFePortPerformance,
       "rcftEthFeStatisticTable": rcftEthFeStatisticTable,
       "rcftEthFeStatisticEntry": rcftEthFeStatisticEntry,
       "rcftEthFeTxPackets": rcftEthFeTxPackets,
       "rcftEthFeTxBytes": rcftEthFeTxBytes,
       "rcftEthFeTxFailurePackets": rcftEthFeTxFailurePackets,
       "rcftEthFeRxPackets": rcftEthFeRxPackets,
       "rcftEthFeRxBytes": rcftEthFeRxBytes,
       "rcftEthFeRxErrorPackets": rcftEthFeRxErrorPackets,
       "rcftEthFeFluxTimer": rcftEthFeFluxTimer,
       "rcftEthFePortTraps": rcftEthFePortTraps,
       "rcftEthFePortLinkTrap": rcftEthFePortLinkTrap,
       "rcftPdhPortMib": rcftPdhPortMib,
       "rcftPdhPortObjects": rcftPdhPortObjects,
       "rcftPdhPortTable": rcftPdhPortTable,
       "rcftPdhPortEntry": rcftPdhPortEntry,
       "rcftPdhPortIndex": rcftPdhPortIndex,
       "rcftPdhPortAlarmStatus": rcftPdhPortAlarmStatus,
       "rcftPdhPortStatus": rcftPdhPortStatus,
       "rcftPdhPortECSCnt": rcftPdhPortECSCnt,
       "rcftPdhPortSECSCnt": rcftPdhPortSECSCnt,
       "rcftPdhPortModuleType": rcftPdhPortModuleType,
       "rcftPdhPortLoopStatus": rcftPdhPortLoopStatus,
       "rcftPdhPortOrder": rcftPdhPortOrder,
       "rcftPdhPortBertStatus": rcftPdhPortBertStatus,
       "rcftPdhPortBertErrCode": rcftPdhPortBertErrCode,
       "rcftPdhPortPerformance": rcftPdhPortPerformance,
       "rcftPdhPortTraps": rcftPdhPortTraps,
       "rcftPdhPortLOSTrap": rcftPdhPortLOSTrap,
       "rcftPdhPortLOFTrap": rcftPdhPortLOFTrap,
       "rcftPdhPortE3Trap": rcftPdhPortE3Trap,
       "rcftPdhPortE6Trap": rcftPdhPortE6Trap,
       "rcftPdhPortToRLOSTrap": rcftPdhPortToRLOSTrap,
       "rcftPdhPortToRLOFTrap": rcftPdhPortToRLOFTrap,
       "rcftPdhPortToRE3Trap": rcftPdhPortToRE3Trap,
       "rcftPdhPortToRE6Trap": rcftPdhPortToRE6Trap,
       "rcftPdhPortToRPowerDown": rcftPdhPortToRPowerDown,
       "rcftE1PortMib": rcftE1PortMib,
       "rcftE1PortObjects": rcftE1PortObjects,
       "rcftE1PortTable": rcftE1PortTable,
       "rcftE1PortEntry": rcftE1PortEntry,
       "rcftE1PortIndex": rcftE1PortIndex,
       "rcftE1PortAlarmStatus": rcftE1PortAlarmStatus,
       "rcftE1PortStatus": rcftE1PortStatus,
       "rcftE1TimeSlots": rcftE1TimeSlots,
       "rcftE1TS0Mode": rcftE1TS0Mode,
       "rcftE1IdleCode": rcftE1IdleCode,
       "rcftE1LoopStatus": rcftE1LoopStatus,
       "rcftE1Order": rcftE1Order,
       "rcftE1PortType": rcftE1PortType,
       "rcftE1BertStatus": rcftE1BertStatus,
       "rcftE1BertTime": rcftE1BertTime,
       "rcftE1BertErrCode": rcftE1BertErrCode,
       "rcftE1BertUnusedTime": rcftE1BertUnusedTime,
       "rcftE1BertPortSpeed": rcftE1BertPortSpeed,
       "rcftE1BertCodeType": rcftE1BertCodeType,
       "rcftE1BertCodeNum": rcftE1BertCodeNum,
       "rcftE1AlarmRejest": rcftE1AlarmRejest,
       "rcfT1PortAlarmStatus": rcfT1PortAlarmStatus,
       "rcftE1PortVCGNumber": rcftE1PortVCGNumber,
       "rcftE1PortErrorRate": rcftE1PortErrorRate,
       "rcftE1PortESCont": rcftE1PortESCont,
       "rcftE1PortSESCont": rcftE1PortSESCont,
       "rcftE1PortToRNumber": rcftE1PortToRNumber,
       "rcftE1CVCnt": rcftE1CVCnt,
       "rcftE1PortPerformance": rcftE1PortPerformance,
       "rcftE1PortTraps": rcftE1PortTraps,
       "rcftE1PortLOSTrap": rcftE1PortLOSTrap,
       "rcftE1PortAISTrap": rcftE1PortAISTrap,
       "rcftE1PortCVTrap": rcftE1PortCVTrap,
       "rcftE1PortLOFTrap": rcftE1PortLOFTrap,
       "rcftE1PortLOMFTrap": rcftE1PortLOMFTrap,
       "rcftE1PortCRCTrap": rcftE1PortCRCTrap,
       "rcftE1PortToRLOSTrap": rcftE1PortToRLOSTrap,
       "rcftT1PortLOSTrap": rcftT1PortLOSTrap,
       "rcftT1PortAISTrap": rcftT1PortAISTrap,
       "rcftE1PortTSDTrap": rcftE1PortTSDTrap,
       "rcftE1PortTransErrorCodeMore10E-3": rcftE1PortTransErrorCodeMore10E_3,
       "rcftE1PortTransErrorCodeMore10E-6": rcftE1PortTransErrorCodeMore10E_6,
       "rcftE1PortRDITrap": rcftE1PortRDITrap,
       "rcftE1PortToRAISTrap": rcftE1PortToRAISTrap,
       "rcftE1PortToRLOFTrap": rcftE1PortToRLOFTrap,
       "rcftE1PortToRCRCTrap": rcftE1PortToRCRCTrap,
       "rcftE1PortToRTSDTrap": rcftE1PortToRTSDTrap,
       "rcftE1PortToRLOMFTrap": rcftE1PortToRLOMFTrap,
       "rcftE1PortTransErrorCodeMoreToR10E-3": rcftE1PortTransErrorCodeMoreToR10E_3,
       "rcftV35PortMib": rcftV35PortMib,
       "rcftV35PortObjects": rcftV35PortObjects,
       "rcftV35PortTable": rcftV35PortTable,
       "rcftV35PortEntry": rcftV35PortEntry,
       "rcftV35PortIndex": rcftV35PortIndex,
       "rcftV35PortAlarmStatus": rcftV35PortAlarmStatus,
       "rcftV35PortStatus": rcftV35PortStatus,
       "rcftV35PortSpeed": rcftV35PortSpeed,
       "rcftV35PortBertStatus": rcftV35PortBertStatus,
       "rcftV35PortBertTime": rcftV35PortBertTime,
       "rcftV35PortBertErrCode": rcftV35PortBertErrCode,
       "rcftV35PortBertUnusedTime": rcftV35PortBertUnusedTime,
       "rcftV35PortBertPortSpeed": rcftV35PortBertPortSpeed,
       "rcftV35PortBertCodeType": rcftV35PortBertCodeType,
       "rcftV35PortBertCodeNum": rcftV35PortBertCodeNum,
       "rcftV35PortLoopStatus": rcftV35PortLoopStatus,
       "rcftV35PortOrder": rcftV35PortOrder,
       "rcftV35PortPerformance": rcftV35PortPerformance,
       "rcftV35PortTraps": rcftV35PortTraps,
       "rcftV35PortDCDTrap": rcftV35PortDCDTrap,
       "rcftV35PortCTSTrap": rcftV35PortCTSTrap,
       "rcftV35PortDTRTrap": rcftV35PortDTRTrap,
       "rcftV35PortRTSTrap": rcftV35PortRTSTrap,
       "rcftV35PortCRCTrap": rcftV35PortCRCTrap,
       "rcftV35PortPATTTrap": rcftV35PortPATTTrap,
       "rcftV35PortLOFTrap": rcftV35PortLOFTrap,
       "rcftV35PortCVTrap": rcftV35PortCVTrap,
       "rcftV35PortAISTrap": rcftV35PortAISTrap,
       "rcftV35PortToRLOFTrap": rcftV35PortToRLOFTrap,
       "rcftV35PortToRCVTrap": rcftV35PortToRCVTrap,
       "rcftV35PortToRAISTrap": rcftV35PortToRAISTrap,
       "rcftV35PortDSRTrap": rcftV35PortDSRTrap,
       "rcftSHDSLPortMib": rcftSHDSLPortMib,
       "rcftSHDSLPortObjects": rcftSHDSLPortObjects,
       "rcftSHDSLPortTable": rcftSHDSLPortTable,
       "rcftSHDSLPortEntry": rcftSHDSLPortEntry,
       "rcftSHDSLPortIndex": rcftSHDSLPortIndex,
       "rcftSHDSLPortAlarmStatus": rcftSHDSLPortAlarmStatus,
       "rcftSHDSLPortStatus": rcftSHDSLPortStatus,
       "rcftSHDSLPortCapableSpeed": rcftSHDSLPortCapableSpeed,
       "rcftSHDSLPortWorkSpeed": rcftSHDSLPortWorkSpeed,
       "rcftSHDSLPortProbeMaxSpeed": rcftSHDSLPortProbeMaxSpeed,
       "rcftSHDSLPortProbeMinSpeed": rcftSHDSLPortProbeMinSpeed,
       "rcftSDHSLPortSNR": rcftSDHSLPortSNR,
       "rcftSHDSLPortConfigSNR": rcftSHDSLPortConfigSNR,
       "rcftSHDSLPortSNRThreshold": rcftSHDSLPortSNRThreshold,
       "rcftSHDSLPortAttenuation": rcftSHDSLPortAttenuation,
       "rcftSHDSLPortAttenuationThreshold": rcftSHDSLPortAttenuationThreshold,
       "rcftSHDSLPortPBO": rcftSHDSLPortPBO,
       "rcftSHDSLPortLOSThreshold": rcftSHDSLPortLOSThreshold,
       "rcftSHDSLPortLOSWThreshold": rcftSHDSLPortLOSWThreshold,
       "rcftSHDSLPortLOLKThreshold": rcftSHDSLPortLOLKThreshold,
       "rcftSHDSLPortESThreshold": rcftSHDSLPortESThreshold,
       "rcftSHDSLPortLoopStatus": rcftSHDSLPortLoopStatus,
       "rcftSHDSLPortAttenuationInitThreshhold": rcftSHDSLPortAttenuationInitThreshhold,
       "rcftSHDSLPortBertStatus": rcftSHDSLPortBertStatus,
       "rcftSHDSLPortBertTime": rcftSHDSLPortBertTime,
       "rcftSHDSLPortBertErrCode": rcftSHDSLPortBertErrCode,
       "rcftSHDSLPortBertUnusedTime": rcftSHDSLPortBertUnusedTime,
       "rcftSHDSLPortBertPortSpeed": rcftSHDSLPortBertPortSpeed,
       "rcftSHDSLPortBertCodeType": rcftSHDSLPortBertCodeType,
       "rcftSHDSLPortBertCodeNum": rcftSHDSLPortBertCodeNum,
       "rcftSHDSLPortOrder": rcftSHDSLPortOrder,
       "rcftSHDSLPortOrderTimeParameter": rcftSHDSLPortOrderTimeParameter,
       "rcftSHDSLPortOrderModeParameter": rcftSHDSLPortOrderModeParameter,
       "rcftSHDSLPortPerformance": rcftSHDSLPortPerformance,
       "rcftSHDSLPortCurrentTable": rcftSHDSLPortCurrentTable,
       "rcftSHDSLPortCurrentEntry": rcftSHDSLPortCurrentEntry,
       "rcftSHDSLPortCurrentLOSTimes": rcftSHDSLPortCurrentLOSTimes,
       "rcftSHDSLPortCurrentLOSWTimes": rcftSHDSLPortCurrentLOSWTimes,
       "rcftSHDSLPortCurrentLOLKTimes": rcftSHDSLPortCurrentLOLKTimes,
       "rcftSHDSLPortCurrentCVTimes": rcftSHDSLPortCurrentCVTimes,
       "rcftSHDSLPortCurrentES": rcftSHDSLPortCurrentES,
       "rcftSHDSLPortCurrentSES": rcftSHDSLPortCurrentSES,
       "rcftSHDSLPortCurrentUAS": rcftSHDSLPortCurrentUAS,
       "rcftSHDSLPortCurrentLOSWS": rcftSHDSLPortCurrentLOSWS,
       "rcftSHDSLPortCurrentLOFTimes": rcftSHDSLPortCurrentLOFTimes,
       "rcftSHDSLPortCurrentCRCTimes": rcftSHDSLPortCurrentCRCTimes,
       "rcftSHDSLPortIntervalTable": rcftSHDSLPortIntervalTable,
       "rcftSHDSLPortIntervalEntry": rcftSHDSLPortIntervalEntry,
       "rcftSHDSLPortIntervalNumber": rcftSHDSLPortIntervalNumber,
       "rcftSHDSLPortIntervalLOSTimes": rcftSHDSLPortIntervalLOSTimes,
       "rcftSHDSLPortIntervalLOSWTimes": rcftSHDSLPortIntervalLOSWTimes,
       "rcftSHDSLPortIntervalLOLKTimes": rcftSHDSLPortIntervalLOLKTimes,
       "rcftSHDSLPortIntervalCVTimes": rcftSHDSLPortIntervalCVTimes,
       "rcftSHDSLPortIntervalES": rcftSHDSLPortIntervalES,
       "rcftSHDSLPortIntervalSES": rcftSHDSLPortIntervalSES,
       "rcftSHDSLPortIntervalUAS": rcftSHDSLPortIntervalUAS,
       "rcftSHDSLPortIntervalLOSWS": rcftSHDSLPortIntervalLOSWS,
       "rcftSHDSLPortIntervalLOFTimes": rcftSHDSLPortIntervalLOFTimes,
       "rcftSHDSLPortIntervalCRCTimes": rcftSHDSLPortIntervalCRCTimes,
       "rcftSHDSLPortCurrentDayTable": rcftSHDSLPortCurrentDayTable,
       "rcftSHDSLPortCurrentDayEntry": rcftSHDSLPortCurrentDayEntry,
       "rcftSHDSLPortCurrentDayLOSTimes": rcftSHDSLPortCurrentDayLOSTimes,
       "rcftSHDSLPortCurrentDayLOSWTimes": rcftSHDSLPortCurrentDayLOSWTimes,
       "rcftSHDSLPortCurrentDayLOLKTimes": rcftSHDSLPortCurrentDayLOLKTimes,
       "rcftSHDSLPortCurrentDayCVTimes": rcftSHDSLPortCurrentDayCVTimes,
       "rcftSHDSLPortCurrentDayES": rcftSHDSLPortCurrentDayES,
       "rcftSHDSLPortCurrentDaySES": rcftSHDSLPortCurrentDaySES,
       "rcftSHDSLPortCurrentDayUAS": rcftSHDSLPortCurrentDayUAS,
       "rcftSHDSLPortCurrentDayLOSWS": rcftSHDSLPortCurrentDayLOSWS,
       "rcftSHDSLPortCurrentDayLOFTimes": rcftSHDSLPortCurrentDayLOFTimes,
       "rcftSHDSLPortCurrentDayCRCTimes": rcftSHDSLPortCurrentDayCRCTimes,
       "rcftSHDSLPortIntervalDayTable": rcftSHDSLPortIntervalDayTable,
       "rcftSHDSLPortIntervalDayEntry": rcftSHDSLPortIntervalDayEntry,
       "rcftSHDSLPortIntervalDayNumber": rcftSHDSLPortIntervalDayNumber,
       "rcftSHDSLPortIntervalDayLOSTimes": rcftSHDSLPortIntervalDayLOSTimes,
       "rcftSHDSLPortIntervalDayLOSWTimes": rcftSHDSLPortIntervalDayLOSWTimes,
       "rcftSHDSLPortIntervalDayLOLKTimes": rcftSHDSLPortIntervalDayLOLKTimes,
       "rcftSHDSLPortIntervalDayCVTimes": rcftSHDSLPortIntervalDayCVTimes,
       "rcftSHDSLPortIntervalDayES": rcftSHDSLPortIntervalDayES,
       "rcftSHDSLPortIntervalDaySES": rcftSHDSLPortIntervalDaySES,
       "rcftSHDSLPortIntervalDayUAS": rcftSHDSLPortIntervalDayUAS,
       "rcftSHDSLPortIntervalDayLOSWS": rcftSHDSLPortIntervalDayLOSWS,
       "rcftSHDSLPortIntervalDayLOFTimes": rcftSHDSLPortIntervalDayLOFTimes,
       "rcftSHDSLPortIntervalDayCRCTimes": rcftSHDSLPortIntervalDayCRCTimes,
       "rcftSHDSLPortTraps": rcftSHDSLPortTraps,
       "rcftSHDSLPortLOSTrap": rcftSHDSLPortLOSTrap,
       "rcftSHDSLPortLOSWTrap": rcftSHDSLPortLOSWTrap,
       "rcftSHDSLPortLINKTrap": rcftSHDSLPortLINKTrap,
       "rcftSHDSLPortFECTrap": rcftSHDSLPortFECTrap,
       "rcftSHDSLPortCRCTrap": rcftSHDSLPortCRCTrap,
       "rcftSHDSLPortSNRThresholdTrap": rcftSHDSLPortSNRThresholdTrap,
       "rcftSHDSLPortAttenuationThresholdTrap": rcftSHDSLPortAttenuationThresholdTrap,
       "rcftSHDSLPortLOSThresholdTrap": rcftSHDSLPortLOSThresholdTrap,
       "rcftSHDSLPortLOSWThresholdTrap": rcftSHDSLPortLOSWThresholdTrap,
       "rcftSHDSLPortLOLKThresholdTrap": rcftSHDSLPortLOLKThresholdTrap,
       "rcftSHDSLPortESThresholdTrap": rcftSHDSLPortESThresholdTrap,
       "rcftAudioPortMib": rcftAudioPortMib,
       "rcftAudioPortObjects": rcftAudioPortObjects,
       "rcftAudioPortTable": rcftAudioPortTable,
       "rcftAudioPortEntry": rcftAudioPortEntry,
       "rcftAudioPortIndex": rcftAudioPortIndex,
       "rcftAudioPortStatus": rcftAudioPortStatus,
       "rcftAudioPortPosition": rcftAudioPortPosition,
       "rcftAudioPortType": rcftAudioPortType,
       "rcftAudioPortPerformance": rcftAudioPortPerformance,
       "rcftAudioPortTraps": rcftAudioPortTraps,
       "rcftDS3E3PortMib": rcftDS3E3PortMib,
       "rcftDS3E3PortObjects": rcftDS3E3PortObjects,
       "rcftDS3E3PortTable": rcftDS3E3PortTable,
       "rcftDS3E3PortEntry": rcftDS3E3PortEntry,
       "rcftDS3E3PortIndex": rcftDS3E3PortIndex,
       "rcftDS3E3PortAlarmStatus": rcftDS3E3PortAlarmStatus,
       "rcftDS3E3PortStatus": rcftDS3E3PortStatus,
       "rcftDS3E3PortESCont": rcftDS3E3PortESCont,
       "rcftDS3E3PortLoopStatus": rcftDS3E3PortLoopStatus,
       "rcftDS3E3PortOrder": rcftDS3E3PortOrder,
       "rcftDS3E3PortPerformance": rcftDS3E3PortPerformance,
       "rcftDS3E3StatisticTable": rcftDS3E3StatisticTable,
       "rcftDS3E3StatisticEntry": rcftDS3E3StatisticEntry,
       "rcftDS3E3TxPackets": rcftDS3E3TxPackets,
       "rcftDS3E3TxBytes": rcftDS3E3TxBytes,
       "rcftDS3E3TxFailurePackets": rcftDS3E3TxFailurePackets,
       "rcftDS3E3RxPackets": rcftDS3E3RxPackets,
       "rcftDS3E3RxBytes": rcftDS3E3RxBytes,
       "rcftDS3E3RxErrorPackets": rcftDS3E3RxErrorPackets,
       "rcftDS3E3FluxTimer": rcftDS3E3FluxTimer,
       "rcftDS3E3PortTraps": rcftDS3E3PortTraps,
       "rcftDS3E3PortAISTrap": rcftDS3E3PortAISTrap,
       "rcftDS3E3PortLOSTrap": rcftDS3E3PortLOSTrap,
       "rcftDS3E3PortLOLTrap": rcftDS3E3PortLOLTrap,
       "rcftDS3E3PortDMOTrap": rcftDS3E3PortDMOTrap,
       "rcftDS3E3PortCVTrap": rcftDS3E3PortCVTrap,
       "rcftDS3E3PortCRCTrap": rcftDS3E3PortCRCTrap,
       "rcftDS3E3PortToRAISTrap": rcftDS3E3PortToRAISTrap,
       "rcftDS3E3PortToRLOSTrap": rcftDS3E3PortToRLOSTrap,
       "rcftDS3E3PortToRLOLTrap": rcftDS3E3PortToRLOLTrap,
       "rcftDS3E3PortToRDMOTrap": rcftDS3E3PortToRDMOTrap,
       "rcftDS3E3PortToRCVTrap": rcftDS3E3PortToRCVTrap,
       "rcftDS3E3PortToRCRCTrap": rcftDS3E3PortToRCRCTrap,
       "rcftDS3E3PortLOFTrap": rcftDS3E3PortLOFTrap,
       "rcftDS3E3PortToRLOFTrap": rcftDS3E3PortToRLOFTrap,
       "rcftDS3E3PortRAITrap": rcftDS3E3PortRAITrap,
       "rcftDS3E3PortToRRAITrap": rcftDS3E3PortToRRAITrap,
       "rcftDS3E3PortOOFTrap": rcftDS3E3PortOOFTrap,
       "rcftDS3E3PortToROOFTrap": rcftDS3E3PortToROOFTrap,
       "rcftDS1PortMib": rcftDS1PortMib,
       "rcftDS1PortObjects": rcftDS1PortObjects,
       "rcftDS1PortTable": rcftDS1PortTable,
       "rcftDS1PortEntry": rcftDS1PortEntry,
       "rcftDS1PortIndex": rcftDS1PortIndex,
       "rcftDS1PortAlarmStatus": rcftDS1PortAlarmStatus,
       "rcftDS1PortStatus": rcftDS1PortStatus,
       "rcftDS1PortBertStatus": rcftDS1PortBertStatus,
       "rcftDS1PortESCont": rcftDS1PortESCont,
       "rcftDS1PortSESCont": rcftDS1PortSESCont,
       "rcftDS1PortLoopStatus": rcftDS1PortLoopStatus,
       "rcftDS1PortOrder": rcftDS1PortOrder,
       "rcftDS1PortTranLength": rcftDS1PortTranLength,
       "rcftDS1PortFaultPassIndicator": rcftDS1PortFaultPassIndicator,
       "rcftDS1PortframeType": rcftDS1PortframeType,
       "rcftDS1PortChannel": rcftDS1PortChannel,
       "rcftDS1PortPerformance": rcftDS1PortPerformance,
       "rcftDS1StatisticTable": rcftDS1StatisticTable,
       "rcftDS1StatisticEntry": rcftDS1StatisticEntry,
       "rcftDS1PortTxPackets": rcftDS1PortTxPackets,
       "rcftDS1PortTxBytes": rcftDS1PortTxBytes,
       "rcftDS1PortTxFailurePackets": rcftDS1PortTxFailurePackets,
       "rcftDS1PortRxPackets": rcftDS1PortRxPackets,
       "rcftDS1PortRxBytes": rcftDS1PortRxBytes,
       "rcftDS1PortRxErrorPackets": rcftDS1PortRxErrorPackets,
       "rcftDS1PortFluxTimer": rcftDS1PortFluxTimer,
       "rcftDS1PortTraps": rcftDS1PortTraps,
       "rcftDS1PortAISTrap": rcftDS1PortAISTrap,
       "rcftDS1PortLOSTrap": rcftDS1PortLOSTrap,
       "rcftDS1PortToRAISTrap": rcftDS1PortToRAISTrap,
       "rcftDS1PortToRLOSTrap": rcftDS1PortToRLOSTrap,
       "rcftDS1PortLOFTrap": rcftDS1PortLOFTrap,
       "rcftDS1PortCRCTrap": rcftDS1PortCRCTrap,
       "rcftDS1PortToRLOFTrap": rcftDS1PortToRLOFTrap,
       "rcftDS1PortToRCRCTrap": rcftDS1PortToRCRCTrap,
       "rcftDS1PortFaultPassIndicatorTrap": rcftDS1PortFaultPassIndicatorTrap,
       "rcftDS1PortDMOTrap": rcftDS1PortDMOTrap,
       "rcftDS1PortCVTrap": rcftDS1PortCVTrap,
       "rcftDS1PortYELTrap": rcftDS1PortYELTrap,
       "rcftDS1PortREDTrap": rcftDS1PortREDTrap,
       "rcftVideoPortMib": rcftVideoPortMib,
       "rcftVideoPortObjects": rcftVideoPortObjects,
       "rcftVideoPortTable": rcftVideoPortTable,
       "rcftVideoPortEntry": rcftVideoPortEntry,
       "rcftVideoPortIndex": rcftVideoPortIndex,
       "rcftVideoPortStatus": rcftVideoPortStatus,
       "rcftVideoPortPosition": rcftVideoPortPosition,
       "rcftVideoPortSourceID": rcftVideoPortSourceID,
       "rcftVideoPortPerformance": rcftVideoPortPerformance,
       "rcftVideoPortTraps": rcftVideoPortTraps,
       "rcftVideoPortSignalLosTrap": rcftVideoPortSignalLosTrap,
       "rcftVideoPortSignalInLosTrap": rcftVideoPortSignalInLosTrap,
       "rcftVideoPortSignalOutLosTrap": rcftVideoPortSignalOutLosTrap,
       "rcftDataPortMib": rcftDataPortMib,
       "rcftDataPortObjects": rcftDataPortObjects,
       "rcftDataPortTable": rcftDataPortTable,
       "rcftDataPortEntry": rcftDataPortEntry,
       "rcftDataPortIndex": rcftDataPortIndex,
       "rcftDataPortStatus": rcftDataPortStatus,
       "rcftDataPortPosition": rcftDataPortPosition,
       "rcftDataPortType": rcftDataPortType,
       "rcftDataPortPerformance": rcftDataPortPerformance,
       "rcftDataPortTraps": rcftDataPortTraps,
       "rcftSimpleModuleMib": rcftSimpleModuleMib,
       "rcftSimpleModuleObjects": rcftSimpleModuleObjects,
       "rcftSimpleModuleTable": rcftSimpleModuleTable,
       "rcftSimpleModuleEntry": rcftSimpleModuleEntry,
       "rcftSimpleModuleIndex": rcftSimpleModuleIndex,
       "rcftSimpleModuleExist": rcftSimpleModuleExist,
       "rcftSimpleModulePosition": rcftSimpleModulePosition,
       "rcftSimpleModuleStatus": rcftSimpleModuleStatus,
       "rcftSimpleModuleType": rcftSimpleModuleType,
       "rcftSimpleModulePerformance": rcftSimpleModulePerformance,
       "rcftSimpleModuleTraps": rcftSimpleModuleTraps,
       "rcftSimpleModuleShutDownTrap": rcftSimpleModuleShutDownTrap,
       "rcftSlotPerformaceMib": rcftSlotPerformaceMib,
       "rcftSlotPerformance": rcftSlotPerformance,
       "rcftSlotStatisticTable": rcftSlotStatisticTable,
       "rcftSlotStatisticEntry": rcftSlotStatisticEntry,
       "rcftPortIndex": rcftPortIndex,
       "rcftPortType": rcftPortType,
       "rcftRxPackets": rcftRxPackets,
       "rcftRxLosPackets": rcftRxLosPackets,
       "rcftRxPreabErrPackets": rcftRxPreabErrPackets,
       "rcftRxFCSErrPackets": rcftRxFCSErrPackets,
       "rcftRxUnderSizePackets": rcftRxUnderSizePackets,
       "rcftRxOverSizePackets": rcftRxOverSizePackets,
       "rcftRxPausePackets": rcftRxPausePackets,
       "rcftRxOamPackets": rcftRxOamPackets,
       "rcftRxBytes": rcftRxBytes,
       "rcftTxPackets": rcftTxPackets,
       "rcftTxFCSErrPackets": rcftTxFCSErrPackets,
       "rcftTxPausePackets": rcftTxPausePackets,
       "rcftTxOamPackets": rcftTxOamPackets,
       "rcftTxBytes": rcftTxBytes,
       "rcftFluxTimer": rcftFluxTimer,
       "rcftSlotVCGMib": rcftSlotVCGMib,
       "rcftSlotVCGObjects": rcftSlotVCGObjects,
       "rcftSlotVCGTable": rcftSlotVCGTable,
       "rcftSlotVCGEntry": rcftSlotVCGEntry,
       "rcftSlotVCGIndex": rcftSlotVCGIndex,
       "rcftSlotVCGStatus": rcftSlotVCGStatus,
       "rcftSlotVCGLoopStatus": rcftSlotVCGLoopStatus,
       "rcftSlotVCGLcasXPR": rcftSlotVCGLcasXPR,
       "rcftSlotVCGLcasXAR": rcftSlotVCGLcasXAR,
       "rcftSlotVCGLcasXPT": rcftSlotVCGLcasXPT,
       "rcftSlotVCGLcasXAT": rcftSlotVCGLcasXAT,
       "rcftSlotVCGAlarmStatus": rcftSlotVCGAlarmStatus,
       "rcftSlotVCGTxISPTPID": rcftSlotVCGTxISPTPID,
       "rcftSlotVCGRxISPTPID": rcftSlotVCGRxISPTPID,
       "rcftSlotVCGBaseCoS": rcftSlotVCGBaseCoS,
       "rcftSlotVCGVLANID": rcftSlotVCGVLANID,
       "rcftSlotVCGMemberList": rcftSlotVCGMemberList,
       "rcftSlotToRVCGMemberList": rcftSlotToRVCGMemberList,
       "rcftSlotVCGMemberStatus": rcftSlotVCGMemberStatus,
       "rcftSlotVCGMemberRxCode": rcftSlotVCGMemberRxCode,
       "rcftSlotVCGMemberTxCode": rcftSlotVCGMemberTxCode,
       "rcftSlotVCGMemberAlarmStatus": rcftSlotVCGMemberAlarmStatus,
       "rcftSlotToRVCGMemberAlarmStatus": rcftSlotToRVCGMemberAlarmStatus,
       "rcftSlotVCGPerformance": rcftSlotVCGPerformance,
       "rcftSlotVCGStatisticTable": rcftSlotVCGStatisticTable,
       "rcftSlotVCGStatisticEntry": rcftSlotVCGStatisticEntry,
       "rcftVCGRxClientPackets": rcftVCGRxClientPackets,
       "rcftVCGRxIdlePackets": rcftVCGRxIdlePackets,
       "rcftVCGRxMgmntPackets": rcftVCGRxMgmntPackets,
       "rcftVCGRxFCSErrMgmntPackets": rcftVCGRxFCSErrMgmntPackets,
       "rcftVCGRxLenErrPackets": rcftVCGRxLenErrPackets,
       "rcftVCGRxFCSErrClientPackets": rcftVCGRxFCSErrClientPackets,
       "rcftVCGRxThecErrPackets": rcftVCGRxThecErrPackets,
       "rcftVCGRxEhecErrPackets": rcftVCGRxEhecErrPackets,
       "rcftVCGRxCIDErrPackets": rcftVCGRxCIDErrPackets,
       "rcftVCGRxSpareErrPackets": rcftVCGRxSpareErrPackets,
       "rcftVCGRxChecCorPackets": rcftVCGRxChecCorPackets,
       "rcftVCGRxThecCorPackets": rcftVCGRxThecCorPackets,
       "rcftVCGRxEhecCorPackets": rcftVCGRxEhecCorPackets,
       "rcftVCGRxBytes": rcftVCGRxBytes,
       "rcftVCGTxClientPackets": rcftVCGTxClientPackets,
       "rcftVCGTxIdlePackets": rcftVCGTxIdlePackets,
       "rcftVCGTxMgmntPackets": rcftVCGTxMgmntPackets,
       "rcftVCGTxBytes": rcftVCGTxBytes,
       "rcftVCGFluxTimer": rcftVCGFluxTimer,
       "rcftSlotVCGTraps": rcftSlotVCGTraps,
       "rcftSlotVCGGIDTraps": rcftSlotVCGGIDTraps,
       "rcftSlotVCGLOATraps": rcftSlotVCGLOATraps,
       "rcftSlotVCGLFDTraps": rcftSlotVCGLFDTraps,
       "rcftSlotVCGCSFTraps": rcftSlotVCGCSFTraps,
       "rcftSlotVCGTLCTTraps": rcftSlotVCGTLCTTraps,
       "rcftSlotVCGTLCRTraps": rcftSlotVCGTLCRTraps,
       "rcftSlotVCGToRGIDTraps": rcftSlotVCGToRGIDTraps,
       "rcftSlotVCGToRLOATraps": rcftSlotVCGToRLOATraps,
       "rcftSlotVCGToRLFDTraps": rcftSlotVCGToRLFDTraps,
       "rcftSlotVCGMemberLOMTraps": rcftSlotVCGMemberLOMTraps,
       "rcftSlotVCGMemberSQMTraps": rcftSlotVCGMemberSQMTraps,
       "rcftSlotVCGMemberCRCTraps": rcftSlotVCGMemberCRCTraps,
       "rcftSlotVCGMemberLOATraps": rcftSlotVCGMemberLOATraps,
       "rcftSlotVCGToRMemberLOMTraps": rcftSlotVCGToRMemberLOMTraps,
       "rcftSlotVCGToRMemberSQMTraps": rcftSlotVCGToRMemberSQMTraps,
       "rcftSlotVCGToRMemberCRCTraps": rcftSlotVCGToRMemberCRCTraps,
       "rcftSlotVCGToRMemberLOATraps": rcftSlotVCGToRMemberLOATraps,
       "rcftSlotVLANMib": rcftSlotVLANMib,
       "rcftSlotVLANObjects": rcftSlotVLANObjects,
       "rcftSlotVLANTable": rcftSlotVLANTable,
       "rcftSlotVLANEntry": rcftSlotVLANEntry,
       "rcftSlotVLANIndex": rcftSlotVLANIndex,
       "rcftSlotVLANStatus": rcftSlotVLANStatus,
       "rcftSlotVLANmember": rcftSlotVLANmember,
       "rcftSlotVID": rcftSlotVID}
)
