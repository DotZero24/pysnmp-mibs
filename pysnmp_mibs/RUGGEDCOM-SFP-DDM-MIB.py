# SNMP MIB module (RUGGEDCOM-SFP-DDM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-SFP-DDM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:34 2025
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

(ruggedcomMgmt,
 ruggedcomTraps) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt",
    "ruggedcomTraps")

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

rcSfpDdm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RcSfpDdmAlarmWarnStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("notAvailable", 1),
          ("ok", 2),
          ("warning", 3),
          ("alarm", 4))
    )



# MIB Managed Objects in the order of their OIDs

_RcSfpDdmGlobalConfig_ObjectIdentity = ObjectIdentity
rcSfpDdmGlobalConfig = _RcSfpDdmGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 1)
)


class _RcSfpDdmPollingInterval_Type(Integer32):
    """Custom type rcSfpDdmPollingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_RcSfpDdmPollingInterval_Type.__name__ = "Integer32"
_RcSfpDdmPollingInterval_Object = MibScalar
rcSfpDdmPollingInterval = _RcSfpDdmPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 1, 1),
    _RcSfpDdmPollingInterval_Type()
)
rcSfpDdmPollingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSfpDdmPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    rcSfpDdmPollingInterval.setUnits("minutes")
_RcSfpDdmTables_ObjectIdentity = ObjectIdentity
rcSfpDdmTables = _RcSfpDdmTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2)
)
_RcSfpDdmPortTable_Object = MibTable
rcSfpDdmPortTable = _RcSfpDdmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1)
)
if mibBuilder.loadTexts:
    rcSfpDdmPortTable.setStatus("current")
_RcSfpDdmPortEntry_Object = MibTableRow
rcSfpDdmPortEntry = _RcSfpDdmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1)
)
rcSfpDdmPortEntry.setIndexNames(
    (0, "RUGGEDCOM-SFP-DDM-MIB", "rcSfpPortId"),
)
if mibBuilder.loadTexts:
    rcSfpDdmPortEntry.setStatus("current")


class _RcSfpPortId_Type(Integer32):
    """Custom type rcSfpPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcSfpPortId_Type.__name__ = "Integer32"
_RcSfpPortId_Object = MibTableColumn
rcSfpPortId = _RcSfpPortId_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 1),
    _RcSfpPortId_Type()
)
rcSfpPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcSfpPortId.setStatus("current")
_RcSfpPlugged_Type = TruthValue
_RcSfpPlugged_Object = MibTableColumn
rcSfpPlugged = _RcSfpPlugged_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 2),
    _RcSfpPlugged_Type()
)
rcSfpPlugged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpPlugged.setStatus("current")
_RcSfpDdmVendorName_Type = DisplayString
_RcSfpDdmVendorName_Object = MibTableColumn
rcSfpDdmVendorName = _RcSfpDdmVendorName_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 3),
    _RcSfpDdmVendorName_Type()
)
rcSfpDdmVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmVendorName.setStatus("current")
_RcSfpDdmVendorPartNumber_Type = DisplayString
_RcSfpDdmVendorPartNumber_Object = MibTableColumn
rcSfpDdmVendorPartNumber = _RcSfpDdmVendorPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 4),
    _RcSfpDdmVendorPartNumber_Type()
)
rcSfpDdmVendorPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmVendorPartNumber.setStatus("current")
_RcSfpDdmVendorRevision_Type = DisplayString
_RcSfpDdmVendorRevision_Object = MibTableColumn
rcSfpDdmVendorRevision = _RcSfpDdmVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 5),
    _RcSfpDdmVendorRevision_Type()
)
rcSfpDdmVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmVendorRevision.setStatus("current")
_RcSfpDdmVendorSerialNumber_Type = DisplayString
_RcSfpDdmVendorSerialNumber_Object = MibTableColumn
rcSfpDdmVendorSerialNumber = _RcSfpDdmVendorSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 6),
    _RcSfpDdmVendorSerialNumber_Type()
)
rcSfpDdmVendorSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmVendorSerialNumber.setStatus("current")
_RcSfpDdmEncoding_Type = DisplayString
_RcSfpDdmEncoding_Object = MibTableColumn
rcSfpDdmEncoding = _RcSfpDdmEncoding_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 7),
    _RcSfpDdmEncoding_Type()
)
rcSfpDdmEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmEncoding.setStatus("current")
_RcSfpDdmNominalBitrate_Type = DisplayString
_RcSfpDdmNominalBitrate_Object = MibTableColumn
rcSfpDdmNominalBitrate = _RcSfpDdmNominalBitrate_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 8),
    _RcSfpDdmNominalBitrate_Type()
)
rcSfpDdmNominalBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmNominalBitrate.setStatus("current")
_RcSfpDdmConnectorType_Type = DisplayString
_RcSfpDdmConnectorType_Object = MibTableColumn
rcSfpDdmConnectorType = _RcSfpDdmConnectorType_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 9),
    _RcSfpDdmConnectorType_Type()
)
rcSfpDdmConnectorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmConnectorType.setStatus("current")
_RcSfpDdmWavelength_Type = DisplayString
_RcSfpDdmWavelength_Object = MibTableColumn
rcSfpDdmWavelength = _RcSfpDdmWavelength_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 10),
    _RcSfpDdmWavelength_Type()
)
rcSfpDdmWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmWavelength.setStatus("current")
_RcSfpDdmLinkLength_Type = DisplayString
_RcSfpDdmLinkLength_Object = MibTableColumn
rcSfpDdmLinkLength = _RcSfpDdmLinkLength_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 11),
    _RcSfpDdmLinkLength_Type()
)
rcSfpDdmLinkLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmLinkLength.setStatus("current")
_RcSfpDdmImplemented_Type = TruthValue
_RcSfpDdmImplemented_Object = MibTableColumn
rcSfpDdmImplemented = _RcSfpDdmImplemented_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 12),
    _RcSfpDdmImplemented_Type()
)
rcSfpDdmImplemented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmImplemented.setStatus("current")
_RcSfpDdmCurrentStatus_Type = RcSfpDdmAlarmWarnStatus
_RcSfpDdmCurrentStatus_Object = MibTableColumn
rcSfpDdmCurrentStatus = _RcSfpDdmCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 13),
    _RcSfpDdmCurrentStatus_Type()
)
rcSfpDdmCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmCurrentStatus.setStatus("current")


class _RcSfpDdmCurrentTemperature_Type(Integer32):
    """Custom type rcSfpDdmCurrentTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_RcSfpDdmCurrentTemperature_Type.__name__ = "Integer32"
_RcSfpDdmCurrentTemperature_Object = MibTableColumn
rcSfpDdmCurrentTemperature = _RcSfpDdmCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 14),
    _RcSfpDdmCurrentTemperature_Type()
)
rcSfpDdmCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmCurrentTemperature.setStatus("current")


class _RcSfpDdmThreshTempAlarmLow_Type(Integer32):
    """Custom type rcSfpDdmThreshTempAlarmLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_RcSfpDdmThreshTempAlarmLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshTempAlarmLow_Object = MibTableColumn
rcSfpDdmThreshTempAlarmLow = _RcSfpDdmThreshTempAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 15),
    _RcSfpDdmThreshTempAlarmLow_Type()
)
rcSfpDdmThreshTempAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTempAlarmLow.setStatus("current")


class _RcSfpDdmThreshTempWarnLow_Type(Integer32):
    """Custom type rcSfpDdmThreshTempWarnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_RcSfpDdmThreshTempWarnLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshTempWarnLow_Object = MibTableColumn
rcSfpDdmThreshTempWarnLow = _RcSfpDdmThreshTempWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 16),
    _RcSfpDdmThreshTempWarnLow_Type()
)
rcSfpDdmThreshTempWarnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTempWarnLow.setStatus("current")


class _RcSfpDdmThreshTempWarnHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshTempWarnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_RcSfpDdmThreshTempWarnHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshTempWarnHigh_Object = MibTableColumn
rcSfpDdmThreshTempWarnHigh = _RcSfpDdmThreshTempWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 17),
    _RcSfpDdmThreshTempWarnHigh_Type()
)
rcSfpDdmThreshTempWarnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTempWarnHigh.setStatus("current")


class _RcSfpDdmThreshTempAlarmHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshTempAlarmHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 128000),
    )


_RcSfpDdmThreshTempAlarmHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshTempAlarmHigh_Object = MibTableColumn
rcSfpDdmThreshTempAlarmHigh = _RcSfpDdmThreshTempAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 18),
    _RcSfpDdmThreshTempAlarmHigh_Type()
)
rcSfpDdmThreshTempAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTempAlarmHigh.setStatus("current")


class _RcSfpDdmCurrentVoltage_Type(Integer32):
    """Custom type rcSfpDdmCurrentVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmCurrentVoltage_Type.__name__ = "Integer32"
_RcSfpDdmCurrentVoltage_Object = MibTableColumn
rcSfpDdmCurrentVoltage = _RcSfpDdmCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 19),
    _RcSfpDdmCurrentVoltage_Type()
)
rcSfpDdmCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmCurrentVoltage.setStatus("current")


class _RcSfpDdmThreshVoltageAlarmLow_Type(Integer32):
    """Custom type rcSfpDdmThreshVoltageAlarmLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshVoltageAlarmLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshVoltageAlarmLow_Object = MibTableColumn
rcSfpDdmThreshVoltageAlarmLow = _RcSfpDdmThreshVoltageAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 20),
    _RcSfpDdmThreshVoltageAlarmLow_Type()
)
rcSfpDdmThreshVoltageAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshVoltageAlarmLow.setStatus("current")


class _RcSfpDdmThreshVoltageWarnLow_Type(Integer32):
    """Custom type rcSfpDdmThreshVoltageWarnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshVoltageWarnLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshVoltageWarnLow_Object = MibTableColumn
rcSfpDdmThreshVoltageWarnLow = _RcSfpDdmThreshVoltageWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 21),
    _RcSfpDdmThreshVoltageWarnLow_Type()
)
rcSfpDdmThreshVoltageWarnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshVoltageWarnLow.setStatus("current")


class _RcSfpDdmThreshVoltageWarnHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshVoltageWarnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshVoltageWarnHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshVoltageWarnHigh_Object = MibTableColumn
rcSfpDdmThreshVoltageWarnHigh = _RcSfpDdmThreshVoltageWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 22),
    _RcSfpDdmThreshVoltageWarnHigh_Type()
)
rcSfpDdmThreshVoltageWarnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshVoltageWarnHigh.setStatus("current")


class _RcSfpDdmThreshVoltageAlarmHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshVoltageAlarmHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshVoltageAlarmHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshVoltageAlarmHigh_Object = MibTableColumn
rcSfpDdmThreshVoltageAlarmHigh = _RcSfpDdmThreshVoltageAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 23),
    _RcSfpDdmThreshVoltageAlarmHigh_Type()
)
rcSfpDdmThreshVoltageAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshVoltageAlarmHigh.setStatus("current")


class _RcSfpDdmCurrentTxBiasCurrent_Type(Integer32):
    """Custom type rcSfpDdmCurrentTxBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131070),
    )


_RcSfpDdmCurrentTxBiasCurrent_Type.__name__ = "Integer32"
_RcSfpDdmCurrentTxBiasCurrent_Object = MibTableColumn
rcSfpDdmCurrentTxBiasCurrent = _RcSfpDdmCurrentTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 24),
    _RcSfpDdmCurrentTxBiasCurrent_Type()
)
rcSfpDdmCurrentTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmCurrentTxBiasCurrent.setStatus("current")


class _RcSfpDdmThreshTxBiasAlarmLow_Type(Integer32):
    """Custom type rcSfpDdmThreshTxBiasAlarmLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131070),
    )


_RcSfpDdmThreshTxBiasAlarmLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxBiasAlarmLow_Object = MibTableColumn
rcSfpDdmThreshTxBiasAlarmLow = _RcSfpDdmThreshTxBiasAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 25),
    _RcSfpDdmThreshTxBiasAlarmLow_Type()
)
rcSfpDdmThreshTxBiasAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxBiasAlarmLow.setStatus("current")


class _RcSfpDdmThreshTxBiasWarnLow_Type(Integer32):
    """Custom type rcSfpDdmThreshTxBiasWarnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131070),
    )


_RcSfpDdmThreshTxBiasWarnLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxBiasWarnLow_Object = MibTableColumn
rcSfpDdmThreshTxBiasWarnLow = _RcSfpDdmThreshTxBiasWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 26),
    _RcSfpDdmThreshTxBiasWarnLow_Type()
)
rcSfpDdmThreshTxBiasWarnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxBiasWarnLow.setStatus("current")


class _RcSfpDdmThreshTxBiasWarnHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshTxBiasWarnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131070),
    )


_RcSfpDdmThreshTxBiasWarnHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxBiasWarnHigh_Object = MibTableColumn
rcSfpDdmThreshTxBiasWarnHigh = _RcSfpDdmThreshTxBiasWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 27),
    _RcSfpDdmThreshTxBiasWarnHigh_Type()
)
rcSfpDdmThreshTxBiasWarnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxBiasWarnHigh.setStatus("current")


class _RcSfpDdmThreshTxBiasAlarmHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshTxBiasAlarmHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 131070),
    )


_RcSfpDdmThreshTxBiasAlarmHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxBiasAlarmHigh_Object = MibTableColumn
rcSfpDdmThreshTxBiasAlarmHigh = _RcSfpDdmThreshTxBiasAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 28),
    _RcSfpDdmThreshTxBiasAlarmHigh_Type()
)
rcSfpDdmThreshTxBiasAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxBiasAlarmHigh.setStatus("current")


class _RcSfpDdmCurrentRxPower_Type(Integer32):
    """Custom type rcSfpDdmCurrentRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553500),
    )


_RcSfpDdmCurrentRxPower_Type.__name__ = "Integer32"
_RcSfpDdmCurrentRxPower_Object = MibTableColumn
rcSfpDdmCurrentRxPower = _RcSfpDdmCurrentRxPower_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 29),
    _RcSfpDdmCurrentRxPower_Type()
)
rcSfpDdmCurrentRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmCurrentRxPower.setStatus("current")


class _RcSfpDdmThreshRxPowerAlarmLow_Type(Integer32):
    """Custom type rcSfpDdmThreshRxPowerAlarmLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553500),
    )


_RcSfpDdmThreshRxPowerAlarmLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshRxPowerAlarmLow_Object = MibTableColumn
rcSfpDdmThreshRxPowerAlarmLow = _RcSfpDdmThreshRxPowerAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 30),
    _RcSfpDdmThreshRxPowerAlarmLow_Type()
)
rcSfpDdmThreshRxPowerAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshRxPowerAlarmLow.setStatus("current")


class _RcSfpDdmThreshRxPowerWarnLow_Type(Integer32):
    """Custom type rcSfpDdmThreshRxPowerWarnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553500),
    )


_RcSfpDdmThreshRxPowerWarnLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshRxPowerWarnLow_Object = MibTableColumn
rcSfpDdmThreshRxPowerWarnLow = _RcSfpDdmThreshRxPowerWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 31),
    _RcSfpDdmThreshRxPowerWarnLow_Type()
)
rcSfpDdmThreshRxPowerWarnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshRxPowerWarnLow.setStatus("current")


class _RcSfpDdmThreshRxPowerWarnHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshRxPowerWarnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553500),
    )


_RcSfpDdmThreshRxPowerWarnHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshRxPowerWarnHigh_Object = MibTableColumn
rcSfpDdmThreshRxPowerWarnHigh = _RcSfpDdmThreshRxPowerWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 32),
    _RcSfpDdmThreshRxPowerWarnHigh_Type()
)
rcSfpDdmThreshRxPowerWarnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshRxPowerWarnHigh.setStatus("current")


class _RcSfpDdmThreshRxPowerAlarmHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshRxPowerAlarmHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6553500),
    )


_RcSfpDdmThreshRxPowerAlarmHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshRxPowerAlarmHigh_Object = MibTableColumn
rcSfpDdmThreshRxPowerAlarmHigh = _RcSfpDdmThreshRxPowerAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 33),
    _RcSfpDdmThreshRxPowerAlarmHigh_Type()
)
rcSfpDdmThreshRxPowerAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshRxPowerAlarmHigh.setStatus("current")


class _RcSfpDdmCurrentTxPower_Type(Integer32):
    """Custom type rcSfpDdmCurrentTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmCurrentTxPower_Type.__name__ = "Integer32"
_RcSfpDdmCurrentTxPower_Object = MibTableColumn
rcSfpDdmCurrentTxPower = _RcSfpDdmCurrentTxPower_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 34),
    _RcSfpDdmCurrentTxPower_Type()
)
rcSfpDdmCurrentTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmCurrentTxPower.setStatus("current")


class _RcSfpDdmThreshTxPowerAlarmLow_Type(Integer32):
    """Custom type rcSfpDdmThreshTxPowerAlarmLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshTxPowerAlarmLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxPowerAlarmLow_Object = MibTableColumn
rcSfpDdmThreshTxPowerAlarmLow = _RcSfpDdmThreshTxPowerAlarmLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 35),
    _RcSfpDdmThreshTxPowerAlarmLow_Type()
)
rcSfpDdmThreshTxPowerAlarmLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxPowerAlarmLow.setStatus("current")


class _RcSfpDdmThreshTxPowerWarnLow_Type(Integer32):
    """Custom type rcSfpDdmThreshTxPowerWarnLow based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshTxPowerWarnLow_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxPowerWarnLow_Object = MibTableColumn
rcSfpDdmThreshTxPowerWarnLow = _RcSfpDdmThreshTxPowerWarnLow_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 36),
    _RcSfpDdmThreshTxPowerWarnLow_Type()
)
rcSfpDdmThreshTxPowerWarnLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxPowerWarnLow.setStatus("current")


class _RcSfpDdmThreshTxPowerWarnHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshTxPowerWarnHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshTxPowerWarnHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxPowerWarnHigh_Object = MibTableColumn
rcSfpDdmThreshTxPowerWarnHigh = _RcSfpDdmThreshTxPowerWarnHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 37),
    _RcSfpDdmThreshTxPowerWarnHigh_Type()
)
rcSfpDdmThreshTxPowerWarnHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxPowerWarnHigh.setStatus("current")


class _RcSfpDdmThreshTxPowerAlarmHigh_Type(Integer32):
    """Custom type rcSfpDdmThreshTxPowerAlarmHigh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6554),
    )


_RcSfpDdmThreshTxPowerAlarmHigh_Type.__name__ = "Integer32"
_RcSfpDdmThreshTxPowerAlarmHigh_Object = MibTableColumn
rcSfpDdmThreshTxPowerAlarmHigh = _RcSfpDdmThreshTxPowerAlarmHigh_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 38),
    _RcSfpDdmThreshTxPowerAlarmHigh_Type()
)
rcSfpDdmThreshTxPowerAlarmHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmThreshTxPowerAlarmHigh.setStatus("current")


class _RcSfpDdmWarningFlags_Type(Bits):
    """Custom type rcSfpDdmWarningFlags based on Bits"""
    namedValues = NamedValues(
        *(("tempHighWarning", 0),
          ("tempLowWarning", 1),
          ("vccHighWarning", 2),
          ("vccLowWarning", 3),
          ("txbiasHighWarning", 4),
          ("txbiasLowWarning", 5),
          ("rxpowerHighWarning", 6),
          ("rxpowerLowWarning", 7),
          ("txpowerHighWarning", 8),
          ("txpowerLowWarning", 9))
    )

_RcSfpDdmWarningFlags_Type.__name__ = "Bits"
_RcSfpDdmWarningFlags_Object = MibTableColumn
rcSfpDdmWarningFlags = _RcSfpDdmWarningFlags_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 39),
    _RcSfpDdmWarningFlags_Type()
)
rcSfpDdmWarningFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmWarningFlags.setStatus("current")


class _RcSfpDdmAlarmFlags_Type(Bits):
    """Custom type rcSfpDdmAlarmFlags based on Bits"""
    namedValues = NamedValues(
        *(("tempHighAlarm", 0),
          ("tempLowAlarm", 1),
          ("vccHighAlarm", 2),
          ("vccLowAlarm", 3),
          ("txbiasHighAlarm", 4),
          ("txbiasLowAlarm", 5),
          ("rxpowerHighAlarm", 6),
          ("rxpowerLowAlarm", 7),
          ("txpowerHighAlarm", 8),
          ("txpowerLowAlarm", 9))
    )

_RcSfpDdmAlarmFlags_Type.__name__ = "Bits"
_RcSfpDdmAlarmFlags_Object = MibTableColumn
rcSfpDdmAlarmFlags = _RcSfpDdmAlarmFlags_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 2, 1, 1, 40),
    _RcSfpDdmAlarmFlags_Type()
)
rcSfpDdmAlarmFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSfpDdmAlarmFlags.setStatus("current")
_RcSfpDdmConformance_ObjectIdentity = ObjectIdentity
rcSfpDdmConformance = _RcSfpDdmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 3)
)
_RcSfpDdmGroups_ObjectIdentity = ObjectIdentity
rcSfpDdmGroups = _RcSfpDdmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 3, 2)
)
_RuggedcomSfpDdmTraps_ObjectIdentity = ObjectIdentity
ruggedcomSfpDdmTraps = _RuggedcomSfpDdmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 5, 52)
)

# Managed Objects groups

rcSfpDdmCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 3, 2, 1)
)
rcSfpDdmCfgGroup.setObjects(
    ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmPollingInterval")
)
if mibBuilder.loadTexts:
    rcSfpDdmCfgGroup.setStatus("current")

rcSfpDdmTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 3, 2, 2)
)
rcSfpDdmTableGroup.setObjects(
      *(("RUGGEDCOM-SFP-DDM-MIB", "rcSfpPortId"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpPlugged"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmVendorName"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmVendorPartNumber"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmVendorRevision"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmVendorSerialNumber"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmEncoding"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmNominalBitrate"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmConnectorType"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmWavelength"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmLinkLength"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmImplemented"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentStatus"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTemperature"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTempAlarmLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTempWarnLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTempWarnHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTempAlarmHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentVoltage"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshVoltageAlarmLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshVoltageWarnLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshVoltageWarnHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshVoltageAlarmHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTxBiasCurrent"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxBiasAlarmLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxBiasWarnLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxBiasWarnHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxBiasAlarmHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentRxPower"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshRxPowerAlarmLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshRxPowerWarnLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshRxPowerWarnHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshRxPowerAlarmHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTxPower"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxPowerAlarmLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxPowerWarnLow"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxPowerWarnHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmThreshTxPowerAlarmHigh"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmWarningFlags"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmAlarmFlags"))
)
if mibBuilder.loadTexts:
    rcSfpDdmTableGroup.setStatus("current")

rcSfpDdmNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 17, 3, 2, 3)
)
rcSfpDdmNotifyGroup.setObjects(
      *(("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmWarningTrap"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmAlarmTrap"))
)
if mibBuilder.loadTexts:
    rcSfpDdmNotifyGroup.setStatus("current")


# Notification objects

rcSfpDdmWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 52, 1)
)
rcSfpDdmWarningTrap.setObjects(
      *(("RUGGEDCOM-SFP-DDM-MIB", "rcSfpPortId"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmWarningFlags"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTemperature"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentVoltage"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTxBiasCurrent"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentRxPower"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTxPower"))
)
if mibBuilder.loadTexts:
    rcSfpDdmWarningTrap.setStatus(
        "current"
    )

rcSfpDdmAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 52, 2)
)
rcSfpDdmAlarmTrap.setObjects(
      *(("RUGGEDCOM-SFP-DDM-MIB", "rcSfpPortId"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmAlarmFlags"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTemperature"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentVoltage"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTxBiasCurrent"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentRxPower"),
        ("RUGGEDCOM-SFP-DDM-MIB", "rcSfpDdmCurrentTxPower"))
)
if mibBuilder.loadTexts:
    rcSfpDdmAlarmTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-SFP-DDM-MIB",
    **{"RcSfpDdmAlarmWarnStatus": RcSfpDdmAlarmWarnStatus,
       "rcSfpDdm": rcSfpDdm,
       "rcSfpDdmGlobalConfig": rcSfpDdmGlobalConfig,
       "rcSfpDdmPollingInterval": rcSfpDdmPollingInterval,
       "rcSfpDdmTables": rcSfpDdmTables,
       "rcSfpDdmPortTable": rcSfpDdmPortTable,
       "rcSfpDdmPortEntry": rcSfpDdmPortEntry,
       "rcSfpPortId": rcSfpPortId,
       "rcSfpPlugged": rcSfpPlugged,
       "rcSfpDdmVendorName": rcSfpDdmVendorName,
       "rcSfpDdmVendorPartNumber": rcSfpDdmVendorPartNumber,
       "rcSfpDdmVendorRevision": rcSfpDdmVendorRevision,
       "rcSfpDdmVendorSerialNumber": rcSfpDdmVendorSerialNumber,
       "rcSfpDdmEncoding": rcSfpDdmEncoding,
       "rcSfpDdmNominalBitrate": rcSfpDdmNominalBitrate,
       "rcSfpDdmConnectorType": rcSfpDdmConnectorType,
       "rcSfpDdmWavelength": rcSfpDdmWavelength,
       "rcSfpDdmLinkLength": rcSfpDdmLinkLength,
       "rcSfpDdmImplemented": rcSfpDdmImplemented,
       "rcSfpDdmCurrentStatus": rcSfpDdmCurrentStatus,
       "rcSfpDdmCurrentTemperature": rcSfpDdmCurrentTemperature,
       "rcSfpDdmThreshTempAlarmLow": rcSfpDdmThreshTempAlarmLow,
       "rcSfpDdmThreshTempWarnLow": rcSfpDdmThreshTempWarnLow,
       "rcSfpDdmThreshTempWarnHigh": rcSfpDdmThreshTempWarnHigh,
       "rcSfpDdmThreshTempAlarmHigh": rcSfpDdmThreshTempAlarmHigh,
       "rcSfpDdmCurrentVoltage": rcSfpDdmCurrentVoltage,
       "rcSfpDdmThreshVoltageAlarmLow": rcSfpDdmThreshVoltageAlarmLow,
       "rcSfpDdmThreshVoltageWarnLow": rcSfpDdmThreshVoltageWarnLow,
       "rcSfpDdmThreshVoltageWarnHigh": rcSfpDdmThreshVoltageWarnHigh,
       "rcSfpDdmThreshVoltageAlarmHigh": rcSfpDdmThreshVoltageAlarmHigh,
       "rcSfpDdmCurrentTxBiasCurrent": rcSfpDdmCurrentTxBiasCurrent,
       "rcSfpDdmThreshTxBiasAlarmLow": rcSfpDdmThreshTxBiasAlarmLow,
       "rcSfpDdmThreshTxBiasWarnLow": rcSfpDdmThreshTxBiasWarnLow,
       "rcSfpDdmThreshTxBiasWarnHigh": rcSfpDdmThreshTxBiasWarnHigh,
       "rcSfpDdmThreshTxBiasAlarmHigh": rcSfpDdmThreshTxBiasAlarmHigh,
       "rcSfpDdmCurrentRxPower": rcSfpDdmCurrentRxPower,
       "rcSfpDdmThreshRxPowerAlarmLow": rcSfpDdmThreshRxPowerAlarmLow,
       "rcSfpDdmThreshRxPowerWarnLow": rcSfpDdmThreshRxPowerWarnLow,
       "rcSfpDdmThreshRxPowerWarnHigh": rcSfpDdmThreshRxPowerWarnHigh,
       "rcSfpDdmThreshRxPowerAlarmHigh": rcSfpDdmThreshRxPowerAlarmHigh,
       "rcSfpDdmCurrentTxPower": rcSfpDdmCurrentTxPower,
       "rcSfpDdmThreshTxPowerAlarmLow": rcSfpDdmThreshTxPowerAlarmLow,
       "rcSfpDdmThreshTxPowerWarnLow": rcSfpDdmThreshTxPowerWarnLow,
       "rcSfpDdmThreshTxPowerWarnHigh": rcSfpDdmThreshTxPowerWarnHigh,
       "rcSfpDdmThreshTxPowerAlarmHigh": rcSfpDdmThreshTxPowerAlarmHigh,
       "rcSfpDdmWarningFlags": rcSfpDdmWarningFlags,
       "rcSfpDdmAlarmFlags": rcSfpDdmAlarmFlags,
       "rcSfpDdmConformance": rcSfpDdmConformance,
       "rcSfpDdmGroups": rcSfpDdmGroups,
       "rcSfpDdmCfgGroup": rcSfpDdmCfgGroup,
       "rcSfpDdmTableGroup": rcSfpDdmTableGroup,
       "rcSfpDdmNotifyGroup": rcSfpDdmNotifyGroup,
       "ruggedcomSfpDdmTraps": ruggedcomSfpDdmTraps,
       "rcSfpDdmWarningTrap": rcSfpDdmWarningTrap,
       "rcSfpDdmAlarmTrap": rcSfpDdmAlarmTrap}
)
