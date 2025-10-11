# SNMP MIB module (CAMBIUM-NETWORKS-TRANSCEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cambium/CAMBIUM-NETWORKS-TRANSCEIVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:07:45 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

cnTransceiverMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1)
)
if mibBuilder.loadTexts:
    cnTransceiverMib.setRevisions(
        ("2022-09-29 00:00",
         "2018-12-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CnTransceiverNotifications_ObjectIdentity = ObjectIdentity
cnTransceiverNotifications = _CnTransceiverNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 0)
)
_CnTransceiverObjects_ObjectIdentity = ObjectIdentity
cnTransceiverObjects = _CnTransceiverObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1)
)
_CnTransceiverPortTable_Object = MibTable
cnTransceiverPortTable = _CnTransceiverPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cnTransceiverPortTable.setStatus("current")
_CnTransceiverPortEntry_Object = MibTableRow
cnTransceiverPortEntry = _CnTransceiverPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1)
)
cnTransceiverPortEntry.setIndexNames(
    (0, "CAMBIUM-NETWORKS-TRANSCEIVER-MIB", "cnTransceiverPortIfIndex"),
)
if mibBuilder.loadTexts:
    cnTransceiverPortEntry.setStatus("current")


class _CnTransceiverPortIfIndex_Type(Integer32):
    """Custom type cnTransceiverPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnTransceiverPortIfIndex_Type.__name__ = "Integer32"
_CnTransceiverPortIfIndex_Object = MibTableColumn
cnTransceiverPortIfIndex = _CnTransceiverPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 1),
    _CnTransceiverPortIfIndex_Type()
)
cnTransceiverPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cnTransceiverPortIfIndex.setStatus("current")


class _CnTransceiverTxEnabled_Type(Integer32):
    """Custom type cnTransceiverTxEnabled based on Integer32"""
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


_CnTransceiverTxEnabled_Type.__name__ = "Integer32"
_CnTransceiverTxEnabled_Object = MibTableColumn
cnTransceiverTxEnabled = _CnTransceiverTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 2),
    _CnTransceiverTxEnabled_Type()
)
cnTransceiverTxEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverTxEnabled.setStatus("current")


class _CnTransceiverType_Type(Integer32):
    """Custom type cnTransceiverType based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("cn1000BASE-T", 1),
          ("cn1000BASE-CX", 2),
          ("cn1000BASE-LX", 3),
          ("cn1000BASE-SX", 4),
          ("cn10GBASE-SR", 5),
          ("cn10GBASE-LR", 6),
          ("cn10GBASE-ER", 7),
          ("cn10GBASE-LRM", 8),
          ("cn10GBASE-SW", 9),
          ("cn10GBASE-LW", 10),
          ("cn10GBASE-EW", 11))
    )


_CnTransceiverType_Type.__name__ = "Integer32"
_CnTransceiverType_Object = MibTableColumn
cnTransceiverType = _CnTransceiverType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 3),
    _CnTransceiverType_Type()
)
cnTransceiverType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverType.setStatus("current")


class _CnTransceiverWavelength_Type(Integer32):
    """Custom type cnTransceiverWavelength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CnTransceiverWavelength_Type.__name__ = "Integer32"
_CnTransceiverWavelength_Object = MibTableColumn
cnTransceiverWavelength = _CnTransceiverWavelength_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 4),
    _CnTransceiverWavelength_Type()
)
cnTransceiverWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverWavelength.setStatus("current")


class _CnTransceiverVendorName_Type(OctetString):
    """Custom type cnTransceiverVendorName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnTransceiverVendorName_Type.__name__ = "OctetString"
_CnTransceiverVendorName_Object = MibTableColumn
cnTransceiverVendorName = _CnTransceiverVendorName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 5),
    _CnTransceiverVendorName_Type()
)
cnTransceiverVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverVendorName.setStatus("current")


class _CnTransceiverVendorOUI_Type(OctetString):
    """Custom type cnTransceiverVendorOUI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnTransceiverVendorOUI_Type.__name__ = "OctetString"
_CnTransceiverVendorOUI_Object = MibTableColumn
cnTransceiverVendorOUI = _CnTransceiverVendorOUI_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 6),
    _CnTransceiverVendorOUI_Type()
)
cnTransceiverVendorOUI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverVendorOUI.setStatus("current")


class _CnTransceiverVendorPartNo_Type(OctetString):
    """Custom type cnTransceiverVendorPartNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnTransceiverVendorPartNo_Type.__name__ = "OctetString"
_CnTransceiverVendorPartNo_Object = MibTableColumn
cnTransceiverVendorPartNo = _CnTransceiverVendorPartNo_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 7),
    _CnTransceiverVendorPartNo_Type()
)
cnTransceiverVendorPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverVendorPartNo.setStatus("current")


class _CnTransceiverVendorRevision_Type(OctetString):
    """Custom type cnTransceiverVendorRevision based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnTransceiverVendorRevision_Type.__name__ = "OctetString"
_CnTransceiverVendorRevision_Object = MibTableColumn
cnTransceiverVendorRevision = _CnTransceiverVendorRevision_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 8),
    _CnTransceiverVendorRevision_Type()
)
cnTransceiverVendorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverVendorRevision.setStatus("current")


class _CnTransceiverVendorSerial_Type(OctetString):
    """Custom type cnTransceiverVendorSerial based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnTransceiverVendorSerial_Type.__name__ = "OctetString"
_CnTransceiverVendorSerial_Object = MibTableColumn
cnTransceiverVendorSerial = _CnTransceiverVendorSerial_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 9),
    _CnTransceiverVendorSerial_Type()
)
cnTransceiverVendorSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverVendorSerial.setStatus("current")


class _CnTransceiverDateCode_Type(OctetString):
    """Custom type cnTransceiverDateCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CnTransceiverDateCode_Type.__name__ = "OctetString"
_CnTransceiverDateCode_Object = MibTableColumn
cnTransceiverDateCode = _CnTransceiverDateCode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 10),
    _CnTransceiverDateCode_Type()
)
cnTransceiverDateCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverDateCode.setStatus("current")


class _CnTransceiverTemperature_Type(Integer32):
    """Custom type cnTransceiverTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_CnTransceiverTemperature_Type.__name__ = "Integer32"
_CnTransceiverTemperature_Object = MibTableColumn
cnTransceiverTemperature = _CnTransceiverTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 11),
    _CnTransceiverTemperature_Type()
)
cnTransceiverTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverTemperature.setStatus("current")
if mibBuilder.loadTexts:
    cnTransceiverTemperature.setUnits("celsius")


class _CnTransceiverVoltage_Type(Integer32):
    """Custom type cnTransceiverVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CnTransceiverVoltage_Type.__name__ = "Integer32"
_CnTransceiverVoltage_Object = MibTableColumn
cnTransceiverVoltage = _CnTransceiverVoltage_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 12),
    _CnTransceiverVoltage_Type()
)
cnTransceiverVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverVoltage.setStatus("current")
if mibBuilder.loadTexts:
    cnTransceiverVoltage.setUnits("milli-volts")


class _CnTransceiverTxBias_Type(Integer32):
    """Custom type cnTransceiverTxBias based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CnTransceiverTxBias_Type.__name__ = "Integer32"
_CnTransceiverTxBias_Object = MibTableColumn
cnTransceiverTxBias = _CnTransceiverTxBias_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 13),
    _CnTransceiverTxBias_Type()
)
cnTransceiverTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverTxBias.setStatus("current")
if mibBuilder.loadTexts:
    cnTransceiverTxBias.setUnits("micro-amps")


class _CnTransceiverTxPower_Type(Integer32):
    """Custom type cnTransceiverTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CnTransceiverTxPower_Type.__name__ = "Integer32"
_CnTransceiverTxPower_Object = MibTableColumn
cnTransceiverTxPower = _CnTransceiverTxPower_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 14),
    _CnTransceiverTxPower_Type()
)
cnTransceiverTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverTxPower.setStatus("current")
if mibBuilder.loadTexts:
    cnTransceiverTxPower.setUnits("micro-watts")


class _CnTransceiverRxPower_Type(Integer32):
    """Custom type cnTransceiverRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_CnTransceiverRxPower_Type.__name__ = "Integer32"
_CnTransceiverRxPower_Object = MibTableColumn
cnTransceiverRxPower = _CnTransceiverRxPower_Object(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 1, 11, 1, 15),
    _CnTransceiverRxPower_Type()
)
cnTransceiverRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cnTransceiverRxPower.setStatus("current")
if mibBuilder.loadTexts:
    cnTransceiverRxPower.setUnits("micro-watts")
_CnTransceiverNotifyObjects_ObjectIdentity = ObjectIdentity
cnTransceiverNotifyObjects = _CnTransceiverNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 81, 18, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CAMBIUM-NETWORKS-TRANSCEIVER-MIB",
    **{"cnTransceiverMib": cnTransceiverMib,
       "cnTransceiverNotifications": cnTransceiverNotifications,
       "cnTransceiverObjects": cnTransceiverObjects,
       "cnTransceiverPortTable": cnTransceiverPortTable,
       "cnTransceiverPortEntry": cnTransceiverPortEntry,
       "cnTransceiverPortIfIndex": cnTransceiverPortIfIndex,
       "cnTransceiverTxEnabled": cnTransceiverTxEnabled,
       "cnTransceiverType": cnTransceiverType,
       "cnTransceiverWavelength": cnTransceiverWavelength,
       "cnTransceiverVendorName": cnTransceiverVendorName,
       "cnTransceiverVendorOUI": cnTransceiverVendorOUI,
       "cnTransceiverVendorPartNo": cnTransceiverVendorPartNo,
       "cnTransceiverVendorRevision": cnTransceiverVendorRevision,
       "cnTransceiverVendorSerial": cnTransceiverVendorSerial,
       "cnTransceiverDateCode": cnTransceiverDateCode,
       "cnTransceiverTemperature": cnTransceiverTemperature,
       "cnTransceiverVoltage": cnTransceiverVoltage,
       "cnTransceiverTxBias": cnTransceiverTxBias,
       "cnTransceiverTxPower": cnTransceiverTxPower,
       "cnTransceiverRxPower": cnTransceiverRxPower,
       "cnTransceiverNotifyObjects": cnTransceiverNotifyObjects}
)
