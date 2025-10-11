# SNMP MIB module (RC002-INTERVAL-PERFORMANCE-STAT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RC002-INTERVAL-PERFORMANCE-STAT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:00 2025
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcftSlotWANFxPortCurrentTable_Object = MibTable
rcftSlotWANFxPortCurrentTable = _RcftSlotWANFxPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4)
)
if mibBuilder.loadTexts:
    rcftSlotWANFxPortCurrentTable.setStatus("current")
_RcftSlotWANFxPortCurrentEntry_Object = MibTableRow
rcftSlotWANFxPortCurrentEntry = _RcftSlotWANFxPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4, 1)
)
rcftSlotWANFxPortCurrentEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotWANFxPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotWANFxPortCurrentEntry.setStatus("current")
_RcftSlotWANFxPortIndex_Type = Integer32
_RcftSlotWANFxPortIndex_Object = MibTableColumn
rcftSlotWANFxPortIndex = _RcftSlotWANFxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4, 1, 1),
    _RcftSlotWANFxPortIndex_Type()
)
rcftSlotWANFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIndex.setStatus("current")


class _RcftSlotWANFxPortCurrentTemperature_Type(OctetString):
    """Custom type rcftSlotWANFxPortCurrentTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortCurrentTemperature_Type.__name__ = "OctetString"
_RcftSlotWANFxPortCurrentTemperature_Object = MibTableColumn
rcftSlotWANFxPortCurrentTemperature = _RcftSlotWANFxPortCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4, 1, 2),
    _RcftSlotWANFxPortCurrentTemperature_Type()
)
rcftSlotWANFxPortCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortCurrentTemperature.setStatus("current")


class _RcftSlotWANFxPortCurrentVoltage_Type(OctetString):
    """Custom type rcftSlotWANFxPortCurrentVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortCurrentVoltage_Type.__name__ = "OctetString"
_RcftSlotWANFxPortCurrentVoltage_Object = MibTableColumn
rcftSlotWANFxPortCurrentVoltage = _RcftSlotWANFxPortCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4, 1, 3),
    _RcftSlotWANFxPortCurrentVoltage_Type()
)
rcftSlotWANFxPortCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortCurrentVoltage.setStatus("current")


class _RcftSlotWANFxPortCurrentOffsetCurr_Type(OctetString):
    """Custom type rcftSlotWANFxPortCurrentOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortCurrentOffsetCurr_Type.__name__ = "OctetString"
_RcftSlotWANFxPortCurrentOffsetCurr_Object = MibTableColumn
rcftSlotWANFxPortCurrentOffsetCurr = _RcftSlotWANFxPortCurrentOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4, 1, 4),
    _RcftSlotWANFxPortCurrentOffsetCurr_Type()
)
rcftSlotWANFxPortCurrentOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortCurrentOffsetCurr.setStatus("current")


class _RcftSlotWANFxPortCurrentRecvPower_Type(OctetString):
    """Custom type rcftSlotWANFxPortCurrentRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortCurrentRecvPower_Type.__name__ = "OctetString"
_RcftSlotWANFxPortCurrentRecvPower_Object = MibTableColumn
rcftSlotWANFxPortCurrentRecvPower = _RcftSlotWANFxPortCurrentRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4, 1, 5),
    _RcftSlotWANFxPortCurrentRecvPower_Type()
)
rcftSlotWANFxPortCurrentRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortCurrentRecvPower.setStatus("current")


class _RcftSlotWANFxPortCurrentSendPower_Type(OctetString):
    """Custom type rcftSlotWANFxPortCurrentSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortCurrentSendPower_Type.__name__ = "OctetString"
_RcftSlotWANFxPortCurrentSendPower_Object = MibTableColumn
rcftSlotWANFxPortCurrentSendPower = _RcftSlotWANFxPortCurrentSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 4, 1, 6),
    _RcftSlotWANFxPortCurrentSendPower_Type()
)
rcftSlotWANFxPortCurrentSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortCurrentSendPower.setStatus("current")
_RcftSlotWANFxPortIntervalTable_Object = MibTable
rcftSlotWANFxPortIntervalTable = _RcftSlotWANFxPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5)
)
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIntervalTable.setStatus("current")
_RcftSlotWANFxPortIntervalEntry_Object = MibTableRow
rcftSlotWANFxPortIntervalEntry = _RcftSlotWANFxPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5, 1)
)
rcftSlotWANFxPortIntervalEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotWANFxPortIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotWANFxIntervalNumber"),
)
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIntervalEntry.setStatus("current")
_RcftSlotWANFxIntervalNumber_Type = Integer32
_RcftSlotWANFxIntervalNumber_Object = MibTableColumn
rcftSlotWANFxIntervalNumber = _RcftSlotWANFxIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5, 1, 1),
    _RcftSlotWANFxIntervalNumber_Type()
)
rcftSlotWANFxIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxIntervalNumber.setStatus("current")


class _RcftSlotWANFxPortIntervalTemperature_Type(OctetString):
    """Custom type rcftSlotWANFxPortIntervalTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortIntervalTemperature_Type.__name__ = "OctetString"
_RcftSlotWANFxPortIntervalTemperature_Object = MibTableColumn
rcftSlotWANFxPortIntervalTemperature = _RcftSlotWANFxPortIntervalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5, 1, 2),
    _RcftSlotWANFxPortIntervalTemperature_Type()
)
rcftSlotWANFxPortIntervalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIntervalTemperature.setStatus("current")


class _RcftSlotWANFxPortIntervalVoltage_Type(OctetString):
    """Custom type rcftSlotWANFxPortIntervalVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortIntervalVoltage_Type.__name__ = "OctetString"
_RcftSlotWANFxPortIntervalVoltage_Object = MibTableColumn
rcftSlotWANFxPortIntervalVoltage = _RcftSlotWANFxPortIntervalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5, 1, 3),
    _RcftSlotWANFxPortIntervalVoltage_Type()
)
rcftSlotWANFxPortIntervalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIntervalVoltage.setStatus("current")


class _RcftSlotWANFxPortIntervalOffsetCurr_Type(OctetString):
    """Custom type rcftSlotWANFxPortIntervalOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortIntervalOffsetCurr_Type.__name__ = "OctetString"
_RcftSlotWANFxPortIntervalOffsetCurr_Object = MibTableColumn
rcftSlotWANFxPortIntervalOffsetCurr = _RcftSlotWANFxPortIntervalOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5, 1, 4),
    _RcftSlotWANFxPortIntervalOffsetCurr_Type()
)
rcftSlotWANFxPortIntervalOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIntervalOffsetCurr.setStatus("current")


class _RcftSlotWANFxPortIntervalRecvPower_Type(OctetString):
    """Custom type rcftSlotWANFxPortIntervalRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortIntervalRecvPower_Type.__name__ = "OctetString"
_RcftSlotWANFxPortIntervalRecvPower_Object = MibTableColumn
rcftSlotWANFxPortIntervalRecvPower = _RcftSlotWANFxPortIntervalRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5, 1, 5),
    _RcftSlotWANFxPortIntervalRecvPower_Type()
)
rcftSlotWANFxPortIntervalRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIntervalRecvPower.setStatus("current")


class _RcftSlotWANFxPortIntervalSendPower_Type(OctetString):
    """Custom type rcftSlotWANFxPortIntervalSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortIntervalSendPower_Type.__name__ = "OctetString"
_RcftSlotWANFxPortIntervalSendPower_Object = MibTableColumn
rcftSlotWANFxPortIntervalSendPower = _RcftSlotWANFxPortIntervalSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 5, 1, 6),
    _RcftSlotWANFxPortIntervalSendPower_Type()
)
rcftSlotWANFxPortIntervalSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortIntervalSendPower.setStatus("current")
_RcftSlotLANFxPortCurrentTable_Object = MibTable
rcftSlotLANFxPortCurrentTable = _RcftSlotLANFxPortCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6)
)
if mibBuilder.loadTexts:
    rcftSlotLANFxPortCurrentTable.setStatus("current")
_RcftSlotLANFxPortCurrentEntry_Object = MibTableRow
rcftSlotLANFxPortCurrentEntry = _RcftSlotLANFxPortCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6, 1)
)
rcftSlotLANFxPortCurrentEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotLANFxPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotLANFxPortCurrentEntry.setStatus("current")
_RcftSlotLANFxPortIndex_Type = Integer32
_RcftSlotLANFxPortIndex_Object = MibTableColumn
rcftSlotLANFxPortIndex = _RcftSlotLANFxPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6, 1, 1),
    _RcftSlotLANFxPortIndex_Type()
)
rcftSlotLANFxPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIndex.setStatus("current")


class _RcftSlotLANFxPortCurrentTemperature_Type(OctetString):
    """Custom type rcftSlotLANFxPortCurrentTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortCurrentTemperature_Type.__name__ = "OctetString"
_RcftSlotLANFxPortCurrentTemperature_Object = MibTableColumn
rcftSlotLANFxPortCurrentTemperature = _RcftSlotLANFxPortCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6, 1, 2),
    _RcftSlotLANFxPortCurrentTemperature_Type()
)
rcftSlotLANFxPortCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortCurrentTemperature.setStatus("current")


class _RcftSlotLANFxPortCurrentVoltage_Type(OctetString):
    """Custom type rcftSlotLANFxPortCurrentVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortCurrentVoltage_Type.__name__ = "OctetString"
_RcftSlotLANFxPortCurrentVoltage_Object = MibTableColumn
rcftSlotLANFxPortCurrentVoltage = _RcftSlotLANFxPortCurrentVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6, 1, 3),
    _RcftSlotLANFxPortCurrentVoltage_Type()
)
rcftSlotLANFxPortCurrentVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortCurrentVoltage.setStatus("current")


class _RcftSlotLANFxPortCurrentOffsetCurr_Type(OctetString):
    """Custom type rcftSlotLANFxPortCurrentOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortCurrentOffsetCurr_Type.__name__ = "OctetString"
_RcftSlotLANFxPortCurrentOffsetCurr_Object = MibTableColumn
rcftSlotLANFxPortCurrentOffsetCurr = _RcftSlotLANFxPortCurrentOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6, 1, 4),
    _RcftSlotLANFxPortCurrentOffsetCurr_Type()
)
rcftSlotLANFxPortCurrentOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortCurrentOffsetCurr.setStatus("current")


class _RcftSlotLANFxPortCurrentRecvPower_Type(OctetString):
    """Custom type rcftSlotLANFxPortCurrentRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortCurrentRecvPower_Type.__name__ = "OctetString"
_RcftSlotLANFxPortCurrentRecvPower_Object = MibTableColumn
rcftSlotLANFxPortCurrentRecvPower = _RcftSlotLANFxPortCurrentRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6, 1, 5),
    _RcftSlotLANFxPortCurrentRecvPower_Type()
)
rcftSlotLANFxPortCurrentRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortCurrentRecvPower.setStatus("current")


class _RcftSlotLANFxPortCurrentSendPower_Type(OctetString):
    """Custom type rcftSlotLANFxPortCurrentSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortCurrentSendPower_Type.__name__ = "OctetString"
_RcftSlotLANFxPortCurrentSendPower_Object = MibTableColumn
rcftSlotLANFxPortCurrentSendPower = _RcftSlotLANFxPortCurrentSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 6, 1, 6),
    _RcftSlotLANFxPortCurrentSendPower_Type()
)
rcftSlotLANFxPortCurrentSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortCurrentSendPower.setStatus("current")
_RcftSlotLANFxPortIntervalTable_Object = MibTable
rcftSlotLANFxPortIntervalTable = _RcftSlotLANFxPortIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7)
)
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIntervalTable.setStatus("current")
_RcftSlotLANFxPortIntervalEntry_Object = MibTableRow
rcftSlotLANFxPortIntervalEntry = _RcftSlotLANFxPortIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7, 1)
)
rcftSlotLANFxPortIntervalEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotLANFxPortIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotLANFxIntervalNumber"),
)
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIntervalEntry.setStatus("current")
_RcftSlotLANFxIntervalNumber_Type = Integer32
_RcftSlotLANFxIntervalNumber_Object = MibTableColumn
rcftSlotLANFxIntervalNumber = _RcftSlotLANFxIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7, 1, 1),
    _RcftSlotLANFxIntervalNumber_Type()
)
rcftSlotLANFxIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxIntervalNumber.setStatus("current")


class _RcftSlotLANFxPortIntervalTemperature_Type(OctetString):
    """Custom type rcftSlotLANFxPortIntervalTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortIntervalTemperature_Type.__name__ = "OctetString"
_RcftSlotLANFxPortIntervalTemperature_Object = MibTableColumn
rcftSlotLANFxPortIntervalTemperature = _RcftSlotLANFxPortIntervalTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7, 1, 2),
    _RcftSlotLANFxPortIntervalTemperature_Type()
)
rcftSlotLANFxPortIntervalTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIntervalTemperature.setStatus("current")


class _RcftSlotLANFxPortIntervalVoltage_Type(OctetString):
    """Custom type rcftSlotLANFxPortIntervalVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortIntervalVoltage_Type.__name__ = "OctetString"
_RcftSlotLANFxPortIntervalVoltage_Object = MibTableColumn
rcftSlotLANFxPortIntervalVoltage = _RcftSlotLANFxPortIntervalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7, 1, 3),
    _RcftSlotLANFxPortIntervalVoltage_Type()
)
rcftSlotLANFxPortIntervalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIntervalVoltage.setStatus("current")


class _RcftSlotLANFxPortIntervalOffsetCurr_Type(OctetString):
    """Custom type rcftSlotLANFxPortIntervalOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortIntervalOffsetCurr_Type.__name__ = "OctetString"
_RcftSlotLANFxPortIntervalOffsetCurr_Object = MibTableColumn
rcftSlotLANFxPortIntervalOffsetCurr = _RcftSlotLANFxPortIntervalOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7, 1, 4),
    _RcftSlotLANFxPortIntervalOffsetCurr_Type()
)
rcftSlotLANFxPortIntervalOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIntervalOffsetCurr.setStatus("current")


class _RcftSlotLANFxPortIntervalRecvPower_Type(OctetString):
    """Custom type rcftSlotLANFxPortIntervalRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortIntervalRecvPower_Type.__name__ = "OctetString"
_RcftSlotLANFxPortIntervalRecvPower_Object = MibTableColumn
rcftSlotLANFxPortIntervalRecvPower = _RcftSlotLANFxPortIntervalRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7, 1, 5),
    _RcftSlotLANFxPortIntervalRecvPower_Type()
)
rcftSlotLANFxPortIntervalRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIntervalRecvPower.setStatus("current")


class _RcftSlotLANFxPortIntervalSendPower_Type(OctetString):
    """Custom type rcftSlotLANFxPortIntervalSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortIntervalSendPower_Type.__name__ = "OctetString"
_RcftSlotLANFxPortIntervalSendPower_Object = MibTableColumn
rcftSlotLANFxPortIntervalSendPower = _RcftSlotLANFxPortIntervalSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 7, 1, 6),
    _RcftSlotLANFxPortIntervalSendPower_Type()
)
rcftSlotLANFxPortIntervalSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortIntervalSendPower.setStatus("current")
_RcftSlotWANFxPortTable_Object = MibTable
rcftSlotWANFxPortTable = _RcftSlotWANFxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 8)
)
if mibBuilder.loadTexts:
    rcftSlotWANFxPortTable.setStatus("current")
_RcftSlotWANFxPortEntry_Object = MibTableRow
rcftSlotWANFxPortEntry = _RcftSlotWANFxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 8, 1)
)
rcftSlotWANFxPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotWANFxPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotWANFxPortEntry.setStatus("current")


class _RcftSlotWANFxPortTemperature_Type(OctetString):
    """Custom type rcftSlotWANFxPortTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortTemperature_Type.__name__ = "OctetString"
_RcftSlotWANFxPortTemperature_Object = MibTableColumn
rcftSlotWANFxPortTemperature = _RcftSlotWANFxPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 8, 1, 1),
    _RcftSlotWANFxPortTemperature_Type()
)
rcftSlotWANFxPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortTemperature.setStatus("current")


class _RcftSlotWANFxPortVoltage_Type(OctetString):
    """Custom type rcftSlotWANFxPortVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortVoltage_Type.__name__ = "OctetString"
_RcftSlotWANFxPortVoltage_Object = MibTableColumn
rcftSlotWANFxPortVoltage = _RcftSlotWANFxPortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 8, 1, 2),
    _RcftSlotWANFxPortVoltage_Type()
)
rcftSlotWANFxPortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortVoltage.setStatus("current")


class _RcftSlotWANFxPortOffsetCurr_Type(OctetString):
    """Custom type rcftSlotWANFxPortOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortOffsetCurr_Type.__name__ = "OctetString"
_RcftSlotWANFxPortOffsetCurr_Object = MibTableColumn
rcftSlotWANFxPortOffsetCurr = _RcftSlotWANFxPortOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 8, 1, 3),
    _RcftSlotWANFxPortOffsetCurr_Type()
)
rcftSlotWANFxPortOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortOffsetCurr.setStatus("current")


class _RcftSlotWANFxPortRecvPower_Type(OctetString):
    """Custom type rcftSlotWANFxPortRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortRecvPower_Type.__name__ = "OctetString"
_RcftSlotWANFxPortRecvPower_Object = MibTableColumn
rcftSlotWANFxPortRecvPower = _RcftSlotWANFxPortRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 8, 1, 4),
    _RcftSlotWANFxPortRecvPower_Type()
)
rcftSlotWANFxPortRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortRecvPower.setStatus("current")


class _RcftSlotWANFxPortSendPower_Type(OctetString):
    """Custom type rcftSlotWANFxPortSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotWANFxPortSendPower_Type.__name__ = "OctetString"
_RcftSlotWANFxPortSendPower_Object = MibTableColumn
rcftSlotWANFxPortSendPower = _RcftSlotWANFxPortSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 8, 1, 5),
    _RcftSlotWANFxPortSendPower_Type()
)
rcftSlotWANFxPortSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotWANFxPortSendPower.setStatus("current")
_RcftSlotLANFxPortTable_Object = MibTable
rcftSlotLANFxPortTable = _RcftSlotLANFxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 9)
)
if mibBuilder.loadTexts:
    rcftSlotLANFxPortTable.setStatus("current")
_RcftSlotLANFxPortEntry_Object = MibTableRow
rcftSlotLANFxPortEntry = _RcftSlotLANFxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 9, 1)
)
rcftSlotLANFxPortEntry.setIndexNames(
    (0, "RAISECOM-RCFT-MIB", "rcftChassisIndex"),
    (0, "RAISECOM-RCFT-MIB", "rcftSlotIndex"),
    (0, "RC002-INTERVAL-PERFORMANCE-STAT-MIB", "rcftSlotLANFxPortIndex"),
)
if mibBuilder.loadTexts:
    rcftSlotLANFxPortEntry.setStatus("current")


class _RcftSlotLANFxPortTemperature_Type(OctetString):
    """Custom type rcftSlotLANFxPortTemperature based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortTemperature_Type.__name__ = "OctetString"
_RcftSlotLANFxPortTemperature_Object = MibTableColumn
rcftSlotLANFxPortTemperature = _RcftSlotLANFxPortTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 9, 1, 1),
    _RcftSlotLANFxPortTemperature_Type()
)
rcftSlotLANFxPortTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortTemperature.setStatus("current")


class _RcftSlotLANFxPortVoltage_Type(OctetString):
    """Custom type rcftSlotLANFxPortVoltage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortVoltage_Type.__name__ = "OctetString"
_RcftSlotLANFxPortVoltage_Object = MibTableColumn
rcftSlotLANFxPortVoltage = _RcftSlotLANFxPortVoltage_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 9, 1, 2),
    _RcftSlotLANFxPortVoltage_Type()
)
rcftSlotLANFxPortVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortVoltage.setStatus("current")


class _RcftSlotLANFxPortOffsetCurr_Type(OctetString):
    """Custom type rcftSlotLANFxPortOffsetCurr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortOffsetCurr_Type.__name__ = "OctetString"
_RcftSlotLANFxPortOffsetCurr_Object = MibTableColumn
rcftSlotLANFxPortOffsetCurr = _RcftSlotLANFxPortOffsetCurr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 9, 1, 3),
    _RcftSlotLANFxPortOffsetCurr_Type()
)
rcftSlotLANFxPortOffsetCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortOffsetCurr.setStatus("current")


class _RcftSlotLANFxPortRecvPower_Type(OctetString):
    """Custom type rcftSlotLANFxPortRecvPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortRecvPower_Type.__name__ = "OctetString"
_RcftSlotLANFxPortRecvPower_Object = MibTableColumn
rcftSlotLANFxPortRecvPower = _RcftSlotLANFxPortRecvPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 9, 1, 4),
    _RcftSlotLANFxPortRecvPower_Type()
)
rcftSlotLANFxPortRecvPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortRecvPower.setStatus("current")


class _RcftSlotLANFxPortSendPower_Type(OctetString):
    """Custom type rcftSlotLANFxPortSendPower based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RcftSlotLANFxPortSendPower_Type.__name__ = "OctetString"
_RcftSlotLANFxPortSendPower_Object = MibTableColumn
rcftSlotLANFxPortSendPower = _RcftSlotLANFxPortSendPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 2, 1, 5, 9, 1, 5),
    _RcftSlotLANFxPortSendPower_Type()
)
rcftSlotLANFxPortSendPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcftSlotLANFxPortSendPower.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RC002-INTERVAL-PERFORMANCE-STAT-MIB",
    **{"rcftSlotWANFxPortCurrentTable": rcftSlotWANFxPortCurrentTable,
       "rcftSlotWANFxPortCurrentEntry": rcftSlotWANFxPortCurrentEntry,
       "rcftSlotWANFxPortIndex": rcftSlotWANFxPortIndex,
       "rcftSlotWANFxPortCurrentTemperature": rcftSlotWANFxPortCurrentTemperature,
       "rcftSlotWANFxPortCurrentVoltage": rcftSlotWANFxPortCurrentVoltage,
       "rcftSlotWANFxPortCurrentOffsetCurr": rcftSlotWANFxPortCurrentOffsetCurr,
       "rcftSlotWANFxPortCurrentRecvPower": rcftSlotWANFxPortCurrentRecvPower,
       "rcftSlotWANFxPortCurrentSendPower": rcftSlotWANFxPortCurrentSendPower,
       "rcftSlotWANFxPortIntervalTable": rcftSlotWANFxPortIntervalTable,
       "rcftSlotWANFxPortIntervalEntry": rcftSlotWANFxPortIntervalEntry,
       "rcftSlotWANFxIntervalNumber": rcftSlotWANFxIntervalNumber,
       "rcftSlotWANFxPortIntervalTemperature": rcftSlotWANFxPortIntervalTemperature,
       "rcftSlotWANFxPortIntervalVoltage": rcftSlotWANFxPortIntervalVoltage,
       "rcftSlotWANFxPortIntervalOffsetCurr": rcftSlotWANFxPortIntervalOffsetCurr,
       "rcftSlotWANFxPortIntervalRecvPower": rcftSlotWANFxPortIntervalRecvPower,
       "rcftSlotWANFxPortIntervalSendPower": rcftSlotWANFxPortIntervalSendPower,
       "rcftSlotLANFxPortCurrentTable": rcftSlotLANFxPortCurrentTable,
       "rcftSlotLANFxPortCurrentEntry": rcftSlotLANFxPortCurrentEntry,
       "rcftSlotLANFxPortIndex": rcftSlotLANFxPortIndex,
       "rcftSlotLANFxPortCurrentTemperature": rcftSlotLANFxPortCurrentTemperature,
       "rcftSlotLANFxPortCurrentVoltage": rcftSlotLANFxPortCurrentVoltage,
       "rcftSlotLANFxPortCurrentOffsetCurr": rcftSlotLANFxPortCurrentOffsetCurr,
       "rcftSlotLANFxPortCurrentRecvPower": rcftSlotLANFxPortCurrentRecvPower,
       "rcftSlotLANFxPortCurrentSendPower": rcftSlotLANFxPortCurrentSendPower,
       "rcftSlotLANFxPortIntervalTable": rcftSlotLANFxPortIntervalTable,
       "rcftSlotLANFxPortIntervalEntry": rcftSlotLANFxPortIntervalEntry,
       "rcftSlotLANFxIntervalNumber": rcftSlotLANFxIntervalNumber,
       "rcftSlotLANFxPortIntervalTemperature": rcftSlotLANFxPortIntervalTemperature,
       "rcftSlotLANFxPortIntervalVoltage": rcftSlotLANFxPortIntervalVoltage,
       "rcftSlotLANFxPortIntervalOffsetCurr": rcftSlotLANFxPortIntervalOffsetCurr,
       "rcftSlotLANFxPortIntervalRecvPower": rcftSlotLANFxPortIntervalRecvPower,
       "rcftSlotLANFxPortIntervalSendPower": rcftSlotLANFxPortIntervalSendPower,
       "rcftSlotWANFxPortTable": rcftSlotWANFxPortTable,
       "rcftSlotWANFxPortEntry": rcftSlotWANFxPortEntry,
       "rcftSlotWANFxPortTemperature": rcftSlotWANFxPortTemperature,
       "rcftSlotWANFxPortVoltage": rcftSlotWANFxPortVoltage,
       "rcftSlotWANFxPortOffsetCurr": rcftSlotWANFxPortOffsetCurr,
       "rcftSlotWANFxPortRecvPower": rcftSlotWANFxPortRecvPower,
       "rcftSlotWANFxPortSendPower": rcftSlotWANFxPortSendPower,
       "rcftSlotLANFxPortTable": rcftSlotLANFxPortTable,
       "rcftSlotLANFxPortEntry": rcftSlotLANFxPortEntry,
       "rcftSlotLANFxPortTemperature": rcftSlotLANFxPortTemperature,
       "rcftSlotLANFxPortVoltage": rcftSlotLANFxPortVoltage,
       "rcftSlotLANFxPortOffsetCurr": rcftSlotLANFxPortOffsetCurr,
       "rcftSlotLANFxPortRecvPower": rcftSlotLANFxPortRecvPower,
       "rcftSlotLANFxPortSendPower": rcftSlotLANFxPortSendPower}
)
