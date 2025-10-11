# SNMP MIB module (HMIT-SW-PORTMGR-DDMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SW-PORTMGR-DDMI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:08 2025
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

(hmITSwPortmgrMIB,) = mibBuilder.importSymbols(
    "HMIT-SW-PORT-MGR-MIB",
    "hmITSwPortmgrMIB")

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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PortDDMITable_Object = MibTable
portDDMITable = _PortDDMITable_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6)
)
if mibBuilder.loadTexts:
    portDDMITable.setStatus("current")
_PortDDMIEntry_Object = MibTableRow
portDDMIEntry = _PortDDMIEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1)
)
portDDMIEntry.setIndexNames(
    (0, "HMIT-SW-PORTMGR-DDMI-MIB", "portDDMIIFindex"),
)
if mibBuilder.loadTexts:
    portDDMIEntry.setStatus("current")


class _PortDDMIIFindex_Type(Integer32):
    """Custom type portDDMIIFindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_PortDDMIIFindex_Type.__name__ = "Integer32"
_PortDDMIIFindex_Object = MibTableColumn
portDDMIIFindex = _PortDDMIIFindex_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 1),
    _PortDDMIIFindex_Type()
)
portDDMIIFindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIIFindex.setStatus("current")


class _PortDDMIDeviceId_Type(DisplayString):
    """Custom type portDDMIDeviceId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIDeviceId_Type.__name__ = "DisplayString"
_PortDDMIDeviceId_Object = MibTableColumn
portDDMIDeviceId = _PortDDMIDeviceId_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 2),
    _PortDDMIDeviceId_Type()
)
portDDMIDeviceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIDeviceId.setStatus("current")


class _PortDDMIConnector_Type(DisplayString):
    """Custom type portDDMIConnector based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortDDMIConnector_Type.__name__ = "DisplayString"
_PortDDMIConnector_Object = MibTableColumn
portDDMIConnector = _PortDDMIConnector_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 3),
    _PortDDMIConnector_Type()
)
portDDMIConnector.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIConnector.setStatus("current")


class _PortDDMIEncoding_Type(DisplayString):
    """Custom type portDDMIEncoding based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortDDMIEncoding_Type.__name__ = "DisplayString"
_PortDDMIEncoding_Object = MibTableColumn
portDDMIEncoding = _PortDDMIEncoding_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 4),
    _PortDDMIEncoding_Type()
)
portDDMIEncoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIEncoding.setStatus("current")


class _PortDDMITransmitLen_Type(DisplayString):
    """Custom type portDDMITransmitLen based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortDDMITransmitLen_Type.__name__ = "DisplayString"
_PortDDMITransmitLen_Object = MibTableColumn
portDDMITransmitLen = _PortDDMITransmitLen_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 6),
    _PortDDMITransmitLen_Type()
)
portDDMITransmitLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITransmitLen.setStatus("current")
_PortDDMIVendorOUI_Type = OctetString
_PortDDMIVendorOUI_Object = MibTableColumn
portDDMIVendorOUI = _PortDDMIVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 7),
    _PortDDMIVendorOUI_Type()
)
portDDMIVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVendorOUI.setStatus("current")


class _PortDDMIVendorName_Type(DisplayString):
    """Custom type portDDMIVendorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIVendorName_Type.__name__ = "DisplayString"
_PortDDMIVendorName_Object = MibTableColumn
portDDMIVendorName = _PortDDMIVendorName_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 8),
    _PortDDMIVendorName_Type()
)
portDDMIVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVendorName.setStatus("current")


class _PortDDMIPartName_Type(DisplayString):
    """Custom type portDDMIPartName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIPartName_Type.__name__ = "DisplayString"
_PortDDMIPartName_Object = MibTableColumn
portDDMIPartName = _PortDDMIPartName_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 9),
    _PortDDMIPartName_Type()
)
portDDMIPartName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIPartName.setStatus("current")


class _PortDDMIRevisionNum_Type(DisplayString):
    """Custom type portDDMIRevisionNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_PortDDMIRevisionNum_Type.__name__ = "DisplayString"
_PortDDMIRevisionNum_Object = MibTableColumn
portDDMIRevisionNum = _PortDDMIRevisionNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 10),
    _PortDDMIRevisionNum_Type()
)
portDDMIRevisionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRevisionNum.setStatus("current")


class _PortDDMILaserWaveLen_Type(Integer32):
    """Custom type portDDMILaserWaveLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDDMILaserWaveLen_Type.__name__ = "Integer32"
_PortDDMILaserWaveLen_Object = MibTableColumn
portDDMILaserWaveLen = _PortDDMILaserWaveLen_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 11),
    _PortDDMILaserWaveLen_Type()
)
portDDMILaserWaveLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMILaserWaveLen.setStatus("current")


class _PortDDMISerialNum_Type(DisplayString):
    """Custom type portDDMISerialNum based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMISerialNum_Type.__name__ = "DisplayString"
_PortDDMISerialNum_Object = MibTableColumn
portDDMISerialNum = _PortDDMISerialNum_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 12),
    _PortDDMISerialNum_Type()
)
portDDMISerialNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMISerialNum.setStatus("current")


class _PortDDMIClass_Type(Integer32):
    """Custom type portDDMIClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PortDDMIClass_Type.__name__ = "Integer32"
_PortDDMIClass_Object = MibTableColumn
portDDMIClass = _PortDDMIClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 13),
    _PortDDMIClass_Type()
)
portDDMIClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIClass.setStatus("current")


class _PortDDMIProductDate_Type(DisplayString):
    """Custom type portDDMIProductDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_PortDDMIProductDate_Type.__name__ = "DisplayString"
_PortDDMIProductDate_Object = MibTableColumn
portDDMIProductDate = _PortDDMIProductDate_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 14),
    _PortDDMIProductDate_Type()
)
portDDMIProductDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIProductDate.setStatus("current")
_PortDDMIVendorSpecific_Type = OctetString
_PortDDMIVendorSpecific_Object = MibTableColumn
portDDMIVendorSpecific = _PortDDMIVendorSpecific_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 15),
    _PortDDMIVendorSpecific_Type()
)
portDDMIVendorSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVendorSpecific.setStatus("current")


class _PortDDMITmperature_Type(DisplayString):
    """Custom type portDDMITmperature based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITmperature_Type.__name__ = "DisplayString"
_PortDDMITmperature_Object = MibTableColumn
portDDMITmperature = _PortDDMITmperature_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 16),
    _PortDDMITmperature_Type()
)
portDDMITmperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITmperature.setStatus("current")


class _PortDDMITempHighAlarmThreshold_Type(DisplayString):
    """Custom type portDDMITempHighAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITempHighAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMITempHighAlarmThreshold_Object = MibTableColumn
portDDMITempHighAlarmThreshold = _PortDDMITempHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 17),
    _PortDDMITempHighAlarmThreshold_Type()
)
portDDMITempHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITempHighAlarmThreshold.setStatus("current")


class _PortDDMITempLowAlarmThreshold_Type(DisplayString):
    """Custom type portDDMITempLowAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITempLowAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMITempLowAlarmThreshold_Object = MibTableColumn
portDDMITempLowAlarmThreshold = _PortDDMITempLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 18),
    _PortDDMITempLowAlarmThreshold_Type()
)
portDDMITempLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITempLowAlarmThreshold.setStatus("current")


class _PortDDMITempHighWarningThreshold_Type(DisplayString):
    """Custom type portDDMITempHighWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITempHighWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMITempHighWarningThreshold_Object = MibTableColumn
portDDMITempHighWarningThreshold = _PortDDMITempHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 19),
    _PortDDMITempHighWarningThreshold_Type()
)
portDDMITempHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITempHighWarningThreshold.setStatus("current")


class _PortDDMITempLowWarningThreshold_Type(DisplayString):
    """Custom type portDDMITempLowWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITempLowWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMITempLowWarningThreshold_Object = MibTableColumn
portDDMITempLowWarningThreshold = _PortDDMITempLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 20),
    _PortDDMITempLowWarningThreshold_Type()
)
portDDMITempLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITempLowWarningThreshold.setStatus("current")


class _PortDDMIVoltage_Type(DisplayString):
    """Custom type portDDMIVoltage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIVoltage_Type.__name__ = "DisplayString"
_PortDDMIVoltage_Object = MibTableColumn
portDDMIVoltage = _PortDDMIVoltage_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 21),
    _PortDDMIVoltage_Type()
)
portDDMIVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVoltage.setStatus("current")


class _PortDDMIVolHighAlarmThreshold_Type(DisplayString):
    """Custom type portDDMIVolHighAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIVolHighAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMIVolHighAlarmThreshold_Object = MibTableColumn
portDDMIVolHighAlarmThreshold = _PortDDMIVolHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 22),
    _PortDDMIVolHighAlarmThreshold_Type()
)
portDDMIVolHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVolHighAlarmThreshold.setStatus("current")


class _PortDDMIVolLowAlarmThreshold_Type(DisplayString):
    """Custom type portDDMIVolLowAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIVolLowAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMIVolLowAlarmThreshold_Object = MibTableColumn
portDDMIVolLowAlarmThreshold = _PortDDMIVolLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 23),
    _PortDDMIVolLowAlarmThreshold_Type()
)
portDDMIVolLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVolLowAlarmThreshold.setStatus("current")


class _PortDDMIVolHighWarningThreshold_Type(DisplayString):
    """Custom type portDDMIVolHighWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIVolHighWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMIVolHighWarningThreshold_Object = MibTableColumn
portDDMIVolHighWarningThreshold = _PortDDMIVolHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 24),
    _PortDDMIVolHighWarningThreshold_Type()
)
portDDMIVolHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVolHighWarningThreshold.setStatus("current")


class _PortDDMIVolLowWarningThreshold_Type(DisplayString):
    """Custom type portDDMIVolLowWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIVolLowWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMIVolLowWarningThreshold_Object = MibTableColumn
portDDMIVolLowWarningThreshold = _PortDDMIVolLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 25),
    _PortDDMIVolLowWarningThreshold_Type()
)
portDDMIVolLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIVolLowWarningThreshold.setStatus("current")


class _PortDDMITxBias_Type(DisplayString):
    """Custom type portDDMITxBias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBias_Type.__name__ = "DisplayString"
_PortDDMITxBias_Object = MibTableColumn
portDDMITxBias = _PortDDMITxBias_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 26),
    _PortDDMITxBias_Type()
)
portDDMITxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBias.setStatus("current")


class _PortDDMITxBiasHighAlarmThreshold_Type(DisplayString):
    """Custom type portDDMITxBiasHighAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBiasHighAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMITxBiasHighAlarmThreshold_Object = MibTableColumn
portDDMITxBiasHighAlarmThreshold = _PortDDMITxBiasHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 27),
    _PortDDMITxBiasHighAlarmThreshold_Type()
)
portDDMITxBiasHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBiasHighAlarmThreshold.setStatus("current")


class _PortDDMITxBiasLowAlarmThreshold_Type(DisplayString):
    """Custom type portDDMITxBiasLowAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBiasLowAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMITxBiasLowAlarmThreshold_Object = MibTableColumn
portDDMITxBiasLowAlarmThreshold = _PortDDMITxBiasLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 28),
    _PortDDMITxBiasLowAlarmThreshold_Type()
)
portDDMITxBiasLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBiasLowAlarmThreshold.setStatus("current")


class _PortDDMITxBiasHighWarningThreshold_Type(DisplayString):
    """Custom type portDDMITxBiasHighWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBiasHighWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMITxBiasHighWarningThreshold_Object = MibTableColumn
portDDMITxBiasHighWarningThreshold = _PortDDMITxBiasHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 29),
    _PortDDMITxBiasHighWarningThreshold_Type()
)
portDDMITxBiasHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBiasHighWarningThreshold.setStatus("current")


class _PortDDMITxBiasLowWarningThreshold_Type(DisplayString):
    """Custom type portDDMITxBiasLowWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBiasLowWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMITxBiasLowWarningThreshold_Object = MibTableColumn
portDDMITxBiasLowWarningThreshold = _PortDDMITxBiasLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 30),
    _PortDDMITxBiasLowWarningThreshold_Type()
)
portDDMITxBiasLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBiasLowWarningThreshold.setStatus("current")


class _PortDDMITxPower_Type(DisplayString):
    """Custom type portDDMITxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPower_Type.__name__ = "DisplayString"
_PortDDMITxPower_Object = MibTableColumn
portDDMITxPower = _PortDDMITxPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 31),
    _PortDDMITxPower_Type()
)
portDDMITxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPower.setStatus("current")


class _PortDDMITxPowerHighAlarmThreshold_Type(DisplayString):
    """Custom type portDDMITxPowerHighAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPowerHighAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMITxPowerHighAlarmThreshold_Object = MibTableColumn
portDDMITxPowerHighAlarmThreshold = _PortDDMITxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 32),
    _PortDDMITxPowerHighAlarmThreshold_Type()
)
portDDMITxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPowerHighAlarmThreshold.setStatus("current")


class _PortDDMITxPowerLowAlarmThreshold_Type(DisplayString):
    """Custom type portDDMITxPowerLowAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPowerLowAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMITxPowerLowAlarmThreshold_Object = MibTableColumn
portDDMITxPowerLowAlarmThreshold = _PortDDMITxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 33),
    _PortDDMITxPowerLowAlarmThreshold_Type()
)
portDDMITxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPowerLowAlarmThreshold.setStatus("current")


class _PortDDMITxPowerHighWarningThreshold_Type(DisplayString):
    """Custom type portDDMITxPowerHighWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPowerHighWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMITxPowerHighWarningThreshold_Object = MibTableColumn
portDDMITxPowerHighWarningThreshold = _PortDDMITxPowerHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 34),
    _PortDDMITxPowerHighWarningThreshold_Type()
)
portDDMITxPowerHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPowerHighWarningThreshold.setStatus("current")


class _PortDDMITxPowerLowWarningThreshold_Type(DisplayString):
    """Custom type portDDMITxPowerLowWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPowerLowWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMITxPowerLowWarningThreshold_Object = MibTableColumn
portDDMITxPowerLowWarningThreshold = _PortDDMITxPowerLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 35),
    _PortDDMITxPowerLowWarningThreshold_Type()
)
portDDMITxPowerLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPowerLowWarningThreshold.setStatus("current")


class _PortDDMIRxPower_Type(DisplayString):
    """Custom type portDDMIRxPower based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPower_Type.__name__ = "DisplayString"
_PortDDMIRxPower_Object = MibTableColumn
portDDMIRxPower = _PortDDMIRxPower_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 36),
    _PortDDMIRxPower_Type()
)
portDDMIRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPower.setStatus("current")


class _PortDDMIRxPowerHighAlarmThreshold_Type(DisplayString):
    """Custom type portDDMIRxPowerHighAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPowerHighAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMIRxPowerHighAlarmThreshold_Object = MibTableColumn
portDDMIRxPowerHighAlarmThreshold = _PortDDMIRxPowerHighAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 37),
    _PortDDMIRxPowerHighAlarmThreshold_Type()
)
portDDMIRxPowerHighAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPowerHighAlarmThreshold.setStatus("current")


class _PortDDMIRxPowerLowAlarmThreshold_Type(DisplayString):
    """Custom type portDDMIRxPowerLowAlarmThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPowerLowAlarmThreshold_Type.__name__ = "DisplayString"
_PortDDMIRxPowerLowAlarmThreshold_Object = MibTableColumn
portDDMIRxPowerLowAlarmThreshold = _PortDDMIRxPowerLowAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 38),
    _PortDDMIRxPowerLowAlarmThreshold_Type()
)
portDDMIRxPowerLowAlarmThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPowerLowAlarmThreshold.setStatus("current")


class _PortDDMIRxPowerHighWarningThreshold_Type(DisplayString):
    """Custom type portDDMIRxPowerHighWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPowerHighWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMIRxPowerHighWarningThreshold_Object = MibTableColumn
portDDMIRxPowerHighWarningThreshold = _PortDDMIRxPowerHighWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 39),
    _PortDDMIRxPowerHighWarningThreshold_Type()
)
portDDMIRxPowerHighWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPowerHighWarningThreshold.setStatus("current")


class _PortDDMIRxPowerLowWarningThreshold_Type(DisplayString):
    """Custom type portDDMIRxPowerLowWarningThreshold based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPowerLowWarningThreshold_Type.__name__ = "DisplayString"
_PortDDMIRxPowerLowWarningThreshold_Object = MibTableColumn
portDDMIRxPowerLowWarningThreshold = _PortDDMIRxPowerLowWarningThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 40),
    _PortDDMIRxPowerLowWarningThreshold_Type()
)
portDDMIRxPowerLowWarningThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPowerLowWarningThreshold.setStatus("current")
_PortDDMIAlarmStatus_Type = OctetString
_PortDDMIAlarmStatus_Object = MibTableColumn
portDDMIAlarmStatus = _PortDDMIAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 41),
    _PortDDMIAlarmStatus_Type()
)
portDDMIAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIAlarmStatus.setStatus("current")
_PortDDMIWarningStatus_Type = OctetString
_PortDDMIWarningStatus_Object = MibTableColumn
portDDMIWarningStatus = _PortDDMIWarningStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 42),
    _PortDDMIWarningStatus_Type()
)
portDDMIWarningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIWarningStatus.setStatus("current")


class _PortDDMIIsMonotorImpt_Type(Integer32):
    """Custom type portDDMIIsMonotorImpt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no_monitor", 1),
          ("has_monitor", 2))
    )


_PortDDMIIsMonotorImpt_Type.__name__ = "Integer32"
_PortDDMIIsMonotorImpt_Object = MibTableColumn
portDDMIIsMonotorImpt = _PortDDMIIsMonotorImpt_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 43),
    _PortDDMIIsMonotorImpt_Type()
)
portDDMIIsMonotorImpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIIsMonotorImpt.setStatus("current")


class _PortDDMIResult_Type(Integer32):
    """Custom type portDDMIResult based on Integer32"""
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
        *(("ok", 1),
          ("offline", 2),
          ("timeout", 3),
          ("error", 4))
    )


_PortDDMIResult_Type.__name__ = "Integer32"
_PortDDMIResult_Object = MibTableColumn
portDDMIResult = _PortDDMIResult_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 44),
    _PortDDMIResult_Type()
)
portDDMIResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIResult.setStatus("current")


class _PortDDMITxBias2_Type(DisplayString):
    """Custom type portDDMITxBias2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBias2_Type.__name__ = "DisplayString"
_PortDDMITxBias2_Object = MibTableColumn
portDDMITxBias2 = _PortDDMITxBias2_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 45),
    _PortDDMITxBias2_Type()
)
portDDMITxBias2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBias2.setStatus("current")


class _PortDDMITxBias3_Type(DisplayString):
    """Custom type portDDMITxBias3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBias3_Type.__name__ = "DisplayString"
_PortDDMITxBias3_Object = MibTableColumn
portDDMITxBias3 = _PortDDMITxBias3_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 46),
    _PortDDMITxBias3_Type()
)
portDDMITxBias3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBias3.setStatus("current")


class _PortDDMITxBias4_Type(DisplayString):
    """Custom type portDDMITxBias4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxBias4_Type.__name__ = "DisplayString"
_PortDDMITxBias4_Object = MibTableColumn
portDDMITxBias4 = _PortDDMITxBias4_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 47),
    _PortDDMITxBias4_Type()
)
portDDMITxBias4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxBias4.setStatus("current")


class _PortDDMIRxPower2_Type(DisplayString):
    """Custom type portDDMIRxPower2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPower2_Type.__name__ = "DisplayString"
_PortDDMIRxPower2_Object = MibTableColumn
portDDMIRxPower2 = _PortDDMIRxPower2_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 48),
    _PortDDMIRxPower2_Type()
)
portDDMIRxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPower2.setStatus("current")


class _PortDDMIRxPower3_Type(DisplayString):
    """Custom type portDDMIRxPower3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPower3_Type.__name__ = "DisplayString"
_PortDDMIRxPower3_Object = MibTableColumn
portDDMIRxPower3 = _PortDDMIRxPower3_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 49),
    _PortDDMIRxPower3_Type()
)
portDDMIRxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPower3.setStatus("current")


class _PortDDMIRxPower4_Type(DisplayString):
    """Custom type portDDMIRxPower4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMIRxPower4_Type.__name__ = "DisplayString"
_PortDDMIRxPower4_Object = MibTableColumn
portDDMIRxPower4 = _PortDDMIRxPower4_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 50),
    _PortDDMIRxPower4_Type()
)
portDDMIRxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIRxPower4.setStatus("current")
_PortDDMIAlarmStatus2_Type = OctetString
_PortDDMIAlarmStatus2_Object = MibTableColumn
portDDMIAlarmStatus2 = _PortDDMIAlarmStatus2_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 51),
    _PortDDMIAlarmStatus2_Type()
)
portDDMIAlarmStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIAlarmStatus2.setStatus("current")
_PortDDMIAlarmStatus3_Type = OctetString
_PortDDMIAlarmStatus3_Object = MibTableColumn
portDDMIAlarmStatus3 = _PortDDMIAlarmStatus3_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 52),
    _PortDDMIAlarmStatus3_Type()
)
portDDMIAlarmStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIAlarmStatus3.setStatus("current")
_PortDDMIAlarmStatus4_Type = OctetString
_PortDDMIAlarmStatus4_Object = MibTableColumn
portDDMIAlarmStatus4 = _PortDDMIAlarmStatus4_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 53),
    _PortDDMIAlarmStatus4_Type()
)
portDDMIAlarmStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIAlarmStatus4.setStatus("current")
_PortDDMIWarningStatus2_Type = OctetString
_PortDDMIWarningStatus2_Object = MibTableColumn
portDDMIWarningStatus2 = _PortDDMIWarningStatus2_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 54),
    _PortDDMIWarningStatus2_Type()
)
portDDMIWarningStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIWarningStatus2.setStatus("current")
_PortDDMIWarningStatus3_Type = OctetString
_PortDDMIWarningStatus3_Object = MibTableColumn
portDDMIWarningStatus3 = _PortDDMIWarningStatus3_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 55),
    _PortDDMIWarningStatus3_Type()
)
portDDMIWarningStatus3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIWarningStatus3.setStatus("current")
_PortDDMIWarningStatus4_Type = OctetString
_PortDDMIWarningStatus4_Object = MibTableColumn
portDDMIWarningStatus4 = _PortDDMIWarningStatus4_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 56),
    _PortDDMIWarningStatus4_Type()
)
portDDMIWarningStatus4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMIWarningStatus4.setStatus("current")


class _PortDDMITxPower2_Type(DisplayString):
    """Custom type portDDMITxPower2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPower2_Type.__name__ = "DisplayString"
_PortDDMITxPower2_Object = MibTableColumn
portDDMITxPower2 = _PortDDMITxPower2_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 57),
    _PortDDMITxPower2_Type()
)
portDDMITxPower2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPower2.setStatus("current")


class _PortDDMITxPower3_Type(DisplayString):
    """Custom type portDDMITxPower3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPower3_Type.__name__ = "DisplayString"
_PortDDMITxPower3_Object = MibTableColumn
portDDMITxPower3 = _PortDDMITxPower3_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 58),
    _PortDDMITxPower3_Type()
)
portDDMITxPower3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPower3.setStatus("current")


class _PortDDMITxPower4_Type(DisplayString):
    """Custom type portDDMITxPower4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_PortDDMITxPower4_Type.__name__ = "DisplayString"
_PortDDMITxPower4_Object = MibTableColumn
portDDMITxPower4 = _PortDDMITxPower4_Object(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 1, 59),
    _PortDDMITxPower4_Type()
)
portDDMITxPower4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portDDMITxPower4.setStatus("current")
_OpticalModuleExceptionTrap_ObjectIdentity = ObjectIdentity
opticalModuleExceptionTrap = _OpticalModuleExceptionTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100)
)

# Managed Objects groups


# Notification objects

opticalModuleTemperatureHighWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100, 1)
)
if mibBuilder.loadTexts:
    opticalModuleTemperatureHighWarnTrap.setStatus(
        "current"
    )

opticalModuleTemperatureLowWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100, 2)
)
if mibBuilder.loadTexts:
    opticalModuleTemperatureLowWarnTrap.setStatus(
        "current"
    )

opticalModuleTemperatureRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100, 3)
)
if mibBuilder.loadTexts:
    opticalModuleTemperatureRecoverTrap.setStatus(
        "current"
    )

opticalModuleRxpowerLowWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100, 4)
)
if mibBuilder.loadTexts:
    opticalModuleRxpowerLowWarnTrap.setStatus(
        "current"
    )

opticalModuleRxpowerRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100, 6)
)
if mibBuilder.loadTexts:
    opticalModuleRxpowerRecoverTrap.setStatus(
        "current"
    )

opticalModuleTxFaultWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100, 7)
)
if mibBuilder.loadTexts:
    opticalModuleTxFaultWarnTrap.setStatus(
        "current"
    )

opticalModuleTxFaultRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3, 1, 13, 6, 100, 8)
)
if mibBuilder.loadTexts:
    opticalModuleTxFaultRecoverTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SW-PORTMGR-DDMI-MIB",
    **{"portDDMITable": portDDMITable,
       "portDDMIEntry": portDDMIEntry,
       "portDDMIIFindex": portDDMIIFindex,
       "portDDMIDeviceId": portDDMIDeviceId,
       "portDDMIConnector": portDDMIConnector,
       "portDDMIEncoding": portDDMIEncoding,
       "portDDMITransmitLen": portDDMITransmitLen,
       "portDDMIVendorOUI": portDDMIVendorOUI,
       "portDDMIVendorName": portDDMIVendorName,
       "portDDMIPartName": portDDMIPartName,
       "portDDMIRevisionNum": portDDMIRevisionNum,
       "portDDMILaserWaveLen": portDDMILaserWaveLen,
       "portDDMISerialNum": portDDMISerialNum,
       "portDDMIClass": portDDMIClass,
       "portDDMIProductDate": portDDMIProductDate,
       "portDDMIVendorSpecific": portDDMIVendorSpecific,
       "portDDMITmperature": portDDMITmperature,
       "portDDMITempHighAlarmThreshold": portDDMITempHighAlarmThreshold,
       "portDDMITempLowAlarmThreshold": portDDMITempLowAlarmThreshold,
       "portDDMITempHighWarningThreshold": portDDMITempHighWarningThreshold,
       "portDDMITempLowWarningThreshold": portDDMITempLowWarningThreshold,
       "portDDMIVoltage": portDDMIVoltage,
       "portDDMIVolHighAlarmThreshold": portDDMIVolHighAlarmThreshold,
       "portDDMIVolLowAlarmThreshold": portDDMIVolLowAlarmThreshold,
       "portDDMIVolHighWarningThreshold": portDDMIVolHighWarningThreshold,
       "portDDMIVolLowWarningThreshold": portDDMIVolLowWarningThreshold,
       "portDDMITxBias": portDDMITxBias,
       "portDDMITxBiasHighAlarmThreshold": portDDMITxBiasHighAlarmThreshold,
       "portDDMITxBiasLowAlarmThreshold": portDDMITxBiasLowAlarmThreshold,
       "portDDMITxBiasHighWarningThreshold": portDDMITxBiasHighWarningThreshold,
       "portDDMITxBiasLowWarningThreshold": portDDMITxBiasLowWarningThreshold,
       "portDDMITxPower": portDDMITxPower,
       "portDDMITxPowerHighAlarmThreshold": portDDMITxPowerHighAlarmThreshold,
       "portDDMITxPowerLowAlarmThreshold": portDDMITxPowerLowAlarmThreshold,
       "portDDMITxPowerHighWarningThreshold": portDDMITxPowerHighWarningThreshold,
       "portDDMITxPowerLowWarningThreshold": portDDMITxPowerLowWarningThreshold,
       "portDDMIRxPower": portDDMIRxPower,
       "portDDMIRxPowerHighAlarmThreshold": portDDMIRxPowerHighAlarmThreshold,
       "portDDMIRxPowerLowAlarmThreshold": portDDMIRxPowerLowAlarmThreshold,
       "portDDMIRxPowerHighWarningThreshold": portDDMIRxPowerHighWarningThreshold,
       "portDDMIRxPowerLowWarningThreshold": portDDMIRxPowerLowWarningThreshold,
       "portDDMIAlarmStatus": portDDMIAlarmStatus,
       "portDDMIWarningStatus": portDDMIWarningStatus,
       "portDDMIIsMonotorImpt": portDDMIIsMonotorImpt,
       "portDDMIResult": portDDMIResult,
       "portDDMITxBias2": portDDMITxBias2,
       "portDDMITxBias3": portDDMITxBias3,
       "portDDMITxBias4": portDDMITxBias4,
       "portDDMIRxPower2": portDDMIRxPower2,
       "portDDMIRxPower3": portDDMIRxPower3,
       "portDDMIRxPower4": portDDMIRxPower4,
       "portDDMIAlarmStatus2": portDDMIAlarmStatus2,
       "portDDMIAlarmStatus3": portDDMIAlarmStatus3,
       "portDDMIAlarmStatus4": portDDMIAlarmStatus4,
       "portDDMIWarningStatus2": portDDMIWarningStatus2,
       "portDDMIWarningStatus3": portDDMIWarningStatus3,
       "portDDMIWarningStatus4": portDDMIWarningStatus4,
       "portDDMITxPower2": portDDMITxPower2,
       "portDDMITxPower3": portDDMITxPower3,
       "portDDMITxPower4": portDDMITxPower4,
       "opticalModuleExceptionTrap": opticalModuleExceptionTrap,
       "opticalModuleTemperatureHighWarnTrap": opticalModuleTemperatureHighWarnTrap,
       "opticalModuleTemperatureLowWarnTrap": opticalModuleTemperatureLowWarnTrap,
       "opticalModuleTemperatureRecoverTrap": opticalModuleTemperatureRecoverTrap,
       "opticalModuleRxpowerLowWarnTrap": opticalModuleRxpowerLowWarnTrap,
       "opticalModuleRxpowerRecoverTrap": opticalModuleRxpowerRecoverTrap,
       "opticalModuleTxFaultWarnTrap": opticalModuleTxFaultWarnTrap,
       "opticalModuleTxFaultRecoverTrap": opticalModuleTxFaultRecoverTrap}
)
