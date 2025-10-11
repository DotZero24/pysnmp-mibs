# SNMP MIB module (OA-FEC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-FEC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:55 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oaFecMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19)
)
if mibBuilder.loadTexts:
    oaFecMib.setRevisions(
        ("2007-11-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Oaccess_ObjectIdentity = ObjectIdentity
oaccess = _Oaccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926)
)
_OaManagement_ObjectIdentity = ObjectIdentity
oaManagement = _OaManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1)
)
_OaFecMibGen_ObjectIdentity = ObjectIdentity
oaFecMibGen = _OaFecMibGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 1)
)


class _OaFecMibSupport_Type(Integer32):
    """Custom type oaFecMibSupport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("supported", 2))
    )


_OaFecMibSupport_Type.__name__ = "Integer32"
_OaFecMibSupport_Object = MibScalar
oaFecMibSupport = _OaFecMibSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 1, 1),
    _OaFecMibSupport_Type()
)
oaFecMibSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecMibSupport.setStatus("current")


class _OaFecMibFecSlotsNumber_Type(Integer32):
    """Custom type oaFecMibFecSlotsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecMibFecSlotsNumber_Type.__name__ = "Integer32"
_OaFecMibFecSlotsNumber_Object = MibScalar
oaFecMibFecSlotsNumber = _OaFecMibFecSlotsNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 1, 2),
    _OaFecMibFecSlotsNumber_Type()
)
oaFecMibFecSlotsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecMibFecSlotsNumber.setStatus("current")
_OaFecMibParams_ObjectIdentity = ObjectIdentity
oaFecMibParams = _OaFecMibParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2)
)
_OaFecConfigurationTable_Object = MibTable
oaFecConfigurationTable = _OaFecConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 1)
)
if mibBuilder.loadTexts:
    oaFecConfigurationTable.setStatus("current")
_OaFecConfigurationEntry_Object = MibTableRow
oaFecConfigurationEntry = _OaFecConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 1, 1)
)
oaFecConfigurationEntry.setIndexNames(
    (0, "OA-FEC-MIB", "oaFecConfigurationSlotIndex"),
)
if mibBuilder.loadTexts:
    oaFecConfigurationEntry.setStatus("current")


class _OaFecConfigurationSlotIndex_Type(Integer32):
    """Custom type oaFecConfigurationSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecConfigurationSlotIndex_Type.__name__ = "Integer32"
_OaFecConfigurationSlotIndex_Object = MibTableColumn
oaFecConfigurationSlotIndex = _OaFecConfigurationSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 1, 1, 1),
    _OaFecConfigurationSlotIndex_Type()
)
oaFecConfigurationSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecConfigurationSlotIndex.setStatus("current")


class _OaFecConfigurationSupportedPorts_Type(Integer32):
    """Custom type oaFecConfigurationSupportedPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecConfigurationSupportedPorts_Type.__name__ = "Integer32"
_OaFecConfigurationSupportedPorts_Object = MibTableColumn
oaFecConfigurationSupportedPorts = _OaFecConfigurationSupportedPorts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 1, 1, 2),
    _OaFecConfigurationSupportedPorts_Type()
)
oaFecConfigurationSupportedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecConfigurationSupportedPorts.setStatus("current")


class _OaFecConfigurationMode_Type(Integer32):
    """Custom type oaFecConfigurationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("oaFecModeOther", 1),
          ("oaFecModeG709", 2),
          ("oaFecModeEfec", 3))
    )


_OaFecConfigurationMode_Type.__name__ = "Integer32"
_OaFecConfigurationMode_Object = MibTableColumn
oaFecConfigurationMode = _OaFecConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 1, 1, 3),
    _OaFecConfigurationMode_Type()
)
oaFecConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    oaFecConfigurationMode.setStatus("current")
_OaFecStatisticsCurrentTable_Object = MibTable
oaFecStatisticsCurrentTable = _OaFecStatisticsCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 2)
)
if mibBuilder.loadTexts:
    oaFecStatisticsCurrentTable.setStatus("current")
_OaFecStatisticsCurrentEntry_Object = MibTableRow
oaFecStatisticsCurrentEntry = _OaFecStatisticsCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 2, 1)
)
oaFecStatisticsCurrentEntry.setIndexNames(
    (0, "OA-FEC-MIB", "oaFecStatisticsSlotIndex"),
    (0, "OA-FEC-MIB", "oaFecStatisticsPortIndex"),
)
if mibBuilder.loadTexts:
    oaFecStatisticsCurrentEntry.setStatus("current")


class _OaFecStatisticsSlotIndex_Type(Integer32):
    """Custom type oaFecStatisticsSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecStatisticsSlotIndex_Type.__name__ = "Integer32"
_OaFecStatisticsSlotIndex_Object = MibTableColumn
oaFecStatisticsSlotIndex = _OaFecStatisticsSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 2, 1, 1),
    _OaFecStatisticsSlotIndex_Type()
)
oaFecStatisticsSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecStatisticsSlotIndex.setStatus("current")


class _OaFecStatisticsPortIndex_Type(Integer32):
    """Custom type oaFecStatisticsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecStatisticsPortIndex_Type.__name__ = "Integer32"
_OaFecStatisticsPortIndex_Object = MibTableColumn
oaFecStatisticsPortIndex = _OaFecStatisticsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 2, 1, 2),
    _OaFecStatisticsPortIndex_Type()
)
oaFecStatisticsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecStatisticsPortIndex.setStatus("current")
_OaFecStatisticsCorrectedBits_Type = Integer32
_OaFecStatisticsCorrectedBits_Object = MibTableColumn
oaFecStatisticsCorrectedBits = _OaFecStatisticsCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 2, 1, 3),
    _OaFecStatisticsCorrectedBits_Type()
)
oaFecStatisticsCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecStatisticsCorrectedBits.setStatus("current")
_OaFecStatisticsUncorrectedBlocks_Type = Integer32
_OaFecStatisticsUncorrectedBlocks_Object = MibTableColumn
oaFecStatisticsUncorrectedBlocks = _OaFecStatisticsUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 2, 1, 4),
    _OaFecStatisticsUncorrectedBlocks_Type()
)
oaFecStatisticsUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecStatisticsUncorrectedBlocks.setStatus("current")
_OaFecStatIntervalTable_Object = MibTable
oaFecStatIntervalTable = _OaFecStatIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3)
)
if mibBuilder.loadTexts:
    oaFecStatIntervalTable.setStatus("current")
_OaFecStatIntervalEntry_Object = MibTableRow
oaFecStatIntervalEntry = _OaFecStatIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3, 1)
)
oaFecStatIntervalEntry.setIndexNames(
    (0, "OA-FEC-MIB", "oaFecStatIntervalSlotNumber"),
    (0, "OA-FEC-MIB", "oaFecStatIntervalPortNumber"),
    (0, "OA-FEC-MIB", "oaFecStatIntervalNumber"),
)
if mibBuilder.loadTexts:
    oaFecStatIntervalEntry.setStatus("current")


class _OaFecStatIntervalSlotNumber_Type(Integer32):
    """Custom type oaFecStatIntervalSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecStatIntervalSlotNumber_Type.__name__ = "Integer32"
_OaFecStatIntervalSlotNumber_Object = MibTableColumn
oaFecStatIntervalSlotNumber = _OaFecStatIntervalSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3, 1, 1),
    _OaFecStatIntervalSlotNumber_Type()
)
oaFecStatIntervalSlotNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecStatIntervalSlotNumber.setStatus("current")


class _OaFecStatIntervalPortNumber_Type(Integer32):
    """Custom type oaFecStatIntervalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecStatIntervalPortNumber_Type.__name__ = "Integer32"
_OaFecStatIntervalPortNumber_Object = MibTableColumn
oaFecStatIntervalPortNumber = _OaFecStatIntervalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3, 1, 2),
    _OaFecStatIntervalPortNumber_Type()
)
oaFecStatIntervalPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecStatIntervalPortNumber.setStatus("current")


class _OaFecStatIntervalNumber_Type(Integer32):
    """Custom type oaFecStatIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_OaFecStatIntervalNumber_Type.__name__ = "Integer32"
_OaFecStatIntervalNumber_Object = MibTableColumn
oaFecStatIntervalNumber = _OaFecStatIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3, 1, 3),
    _OaFecStatIntervalNumber_Type()
)
oaFecStatIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecStatIntervalNumber.setStatus("current")
_OaFecStatIntervalCorrectedBits_Type = Integer32
_OaFecStatIntervalCorrectedBits_Object = MibTableColumn
oaFecStatIntervalCorrectedBits = _OaFecStatIntervalCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3, 1, 4),
    _OaFecStatIntervalCorrectedBits_Type()
)
oaFecStatIntervalCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecStatIntervalCorrectedBits.setStatus("current")
_OaFecStatIntervalUncorrectedBlocks_Type = Integer32
_OaFecStatIntervalUncorrectedBlocks_Object = MibTableColumn
oaFecStatIntervalUncorrectedBlocks = _OaFecStatIntervalUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3, 1, 5),
    _OaFecStatIntervalUncorrectedBlocks_Type()
)
oaFecStatIntervalUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecStatIntervalUncorrectedBlocks.setStatus("current")
_OaFecStatIntervalValidData_Type = TruthValue
_OaFecStatIntervalValidData_Object = MibTableColumn
oaFecStatIntervalValidData = _OaFecStatIntervalValidData_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 3, 1, 6),
    _OaFecStatIntervalValidData_Type()
)
oaFecStatIntervalValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecStatIntervalValidData.setStatus("current")
_OaFecStatCurrentDayTable_Object = MibTable
oaFecStatCurrentDayTable = _OaFecStatCurrentDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 4)
)
if mibBuilder.loadTexts:
    oaFecStatCurrentDayTable.setStatus("current")
_OaFecStatCurrentDayEntry_Object = MibTableRow
oaFecStatCurrentDayEntry = _OaFecStatCurrentDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 4, 1)
)
oaFecStatCurrentDayEntry.setIndexNames(
    (0, "OA-FEC-MIB", "oaFecDayStatSlotIndex"),
    (0, "OA-FEC-MIB", "oaFecDayStatPortIndex"),
)
if mibBuilder.loadTexts:
    oaFecStatCurrentDayEntry.setStatus("current")


class _OaFecDayStatSlotIndex_Type(Integer32):
    """Custom type oaFecDayStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecDayStatSlotIndex_Type.__name__ = "Integer32"
_OaFecDayStatSlotIndex_Object = MibTableColumn
oaFecDayStatSlotIndex = _OaFecDayStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 4, 1, 1),
    _OaFecDayStatSlotIndex_Type()
)
oaFecDayStatSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecDayStatSlotIndex.setStatus("current")


class _OaFecDayStatPortIndex_Type(Integer32):
    """Custom type oaFecDayStatPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecDayStatPortIndex_Type.__name__ = "Integer32"
_OaFecDayStatPortIndex_Object = MibTableColumn
oaFecDayStatPortIndex = _OaFecDayStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 4, 1, 2),
    _OaFecDayStatPortIndex_Type()
)
oaFecDayStatPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecDayStatPortIndex.setStatus("current")
_OaFecDayStatCorrectedBits_Type = Integer32
_OaFecDayStatCorrectedBits_Object = MibTableColumn
oaFecDayStatCorrectedBits = _OaFecDayStatCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 4, 1, 3),
    _OaFecDayStatCorrectedBits_Type()
)
oaFecDayStatCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecDayStatCorrectedBits.setStatus("current")
_OaFecDayStatUncorrectedBlocks_Type = Integer32
_OaFecDayStatUncorrectedBlocks_Object = MibTableColumn
oaFecDayStatUncorrectedBlocks = _OaFecDayStatUncorrectedBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 4, 1, 4),
    _OaFecDayStatUncorrectedBlocks_Type()
)
oaFecDayStatUncorrectedBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecDayStatUncorrectedBlocks.setStatus("current")
_OaFecStatPrevDayTable_Object = MibTable
oaFecStatPrevDayTable = _OaFecStatPrevDayTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 5)
)
if mibBuilder.loadTexts:
    oaFecStatPrevDayTable.setStatus("current")
_OaFecStatPrevDayEntry_Object = MibTableRow
oaFecStatPrevDayEntry = _OaFecStatPrevDayEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 5, 1)
)
oaFecStatPrevDayEntry.setIndexNames(
    (0, "OA-FEC-MIB", "oaFecPrevDayStatSlotIndex"),
    (0, "OA-FEC-MIB", "oaFecPrevDayStatPortIndex"),
)
if mibBuilder.loadTexts:
    oaFecStatPrevDayEntry.setStatus("current")


class _OaFecPrevDayStatSlotIndex_Type(Integer32):
    """Custom type oaFecPrevDayStatSlotIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecPrevDayStatSlotIndex_Type.__name__ = "Integer32"
_OaFecPrevDayStatSlotIndex_Object = MibTableColumn
oaFecPrevDayStatSlotIndex = _OaFecPrevDayStatSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 5, 1, 1),
    _OaFecPrevDayStatSlotIndex_Type()
)
oaFecPrevDayStatSlotIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecPrevDayStatSlotIndex.setStatus("current")


class _OaFecPrevDayStatPortIndex_Type(Integer32):
    """Custom type oaFecPrevDayStatPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_OaFecPrevDayStatPortIndex_Type.__name__ = "Integer32"
_OaFecPrevDayStatPortIndex_Object = MibTableColumn
oaFecPrevDayStatPortIndex = _OaFecPrevDayStatPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 5, 1, 2),
    _OaFecPrevDayStatPortIndex_Type()
)
oaFecPrevDayStatPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oaFecPrevDayStatPortIndex.setStatus("current")
_OaFecPrevDayStatCorrectedBits_Type = Integer32
_OaFecPrevDayStatCorrectedBits_Object = MibTableColumn
oaFecPrevDayStatCorrectedBits = _OaFecPrevDayStatCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 5, 1, 3),
    _OaFecPrevDayStatCorrectedBits_Type()
)
oaFecPrevDayStatCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecPrevDayStatCorrectedBits.setStatus("current")
_OaFecPrevDayStatUncorrBlocks_Type = Integer32
_OaFecPrevDayStatUncorrBlocks_Object = MibTableColumn
oaFecPrevDayStatUncorrBlocks = _OaFecPrevDayStatUncorrBlocks_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 5, 1, 4),
    _OaFecPrevDayStatUncorrBlocks_Type()
)
oaFecPrevDayStatUncorrBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecPrevDayStatUncorrBlocks.setStatus("current")
_OaFecPrevDayStatValidData_Type = TruthValue
_OaFecPrevDayStatValidData_Object = MibTableColumn
oaFecPrevDayStatValidData = _OaFecPrevDayStatValidData_Object(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 2, 5, 1, 5),
    _OaFecPrevDayStatValidData_Type()
)
oaFecPrevDayStatValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaFecPrevDayStatValidData.setStatus("current")
_OaFecMibConformance_ObjectIdentity = ObjectIdentity
oaFecMibConformance = _OaFecMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101)
)
_OaFecMibMIBCompliances_ObjectIdentity = ObjectIdentity
oaFecMibMIBCompliances = _OaFecMibMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 1)
)
_OaFecMibMIBGroups_ObjectIdentity = ObjectIdentity
oaFecMibMIBGroups = _OaFecMibMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 2)
)

# Managed Objects groups

oaFecMibMandatoryConfigurationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 2, 1)
)
oaFecMibMandatoryConfigurationGroup.setObjects(
      *(("OA-FEC-MIB", "oaFecMibSupport"),
        ("OA-FEC-MIB", "oaFecMibFecSlotsNumber"),
        ("OA-FEC-MIB", "oaFecConfigurationSupportedPorts"),
        ("OA-FEC-MIB", "oaFecConfigurationMode"))
)
if mibBuilder.loadTexts:
    oaFecMibMandatoryConfigurationGroup.setStatus("current")

oaFecMibMandatoryStatCurrentGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 2, 2)
)
oaFecMibMandatoryStatCurrentGroup.setObjects(
      *(("OA-FEC-MIB", "oaFecStatisticsCorrectedBits"),
        ("OA-FEC-MIB", "oaFecStatisticsUncorrectedBlocks"))
)
if mibBuilder.loadTexts:
    oaFecMibMandatoryStatCurrentGroup.setStatus("current")

oaFecMibMandatoryStatIntervalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 2, 3)
)
oaFecMibMandatoryStatIntervalGroup.setObjects(
      *(("OA-FEC-MIB", "oaFecStatIntervalCorrectedBits"),
        ("OA-FEC-MIB", "oaFecStatIntervalUncorrectedBlocks"),
        ("OA-FEC-MIB", "oaFecStatIntervalValidData"))
)
if mibBuilder.loadTexts:
    oaFecMibMandatoryStatIntervalGroup.setStatus("current")

oaFecMibMandatoryStatCurrentDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 2, 4)
)
oaFecMibMandatoryStatCurrentDayGroup.setObjects(
      *(("OA-FEC-MIB", "oaFecDayStatCorrectedBits"),
        ("OA-FEC-MIB", "oaFecDayStatUncorrectedBlocks"))
)
if mibBuilder.loadTexts:
    oaFecMibMandatoryStatCurrentDayGroup.setStatus("current")

oaFecMibMandatoryStatPrevDayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 2, 5)
)
oaFecMibMandatoryStatPrevDayGroup.setObjects(
      *(("OA-FEC-MIB", "oaFecPrevDayStatCorrectedBits"),
        ("OA-FEC-MIB", "oaFecPrevDayStatUncorrBlocks"),
        ("OA-FEC-MIB", "oaFecPrevDayStatValidData"))
)
if mibBuilder.loadTexts:
    oaFecMibMandatoryStatPrevDayGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oaFecMibMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 1, 19, 101, 1, 1)
)
oaFecMibMIBCompliance.setObjects(
      *(("OA-FEC-MIB", "oaFecMibMandatoryConfigurationGroup"),
        ("OA-FEC-MIB", "oaFecMibMandatoryStatCurrentGroup"),
        ("OA-FEC-MIB", "oaFecMibMandatoryStatIntervalGroup"),
        ("OA-FEC-MIB", "oaFecMibMandatoryStatCurrentDayGroup"),
        ("OA-FEC-MIB", "oaFecMibMandatoryStatPrevDayGroup"))
)
if mibBuilder.loadTexts:
    oaFecMibMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-FEC-MIB",
    **{"oaccess": oaccess,
       "oaManagement": oaManagement,
       "oaFecMib": oaFecMib,
       "oaFecMibGen": oaFecMibGen,
       "oaFecMibSupport": oaFecMibSupport,
       "oaFecMibFecSlotsNumber": oaFecMibFecSlotsNumber,
       "oaFecMibParams": oaFecMibParams,
       "oaFecConfigurationTable": oaFecConfigurationTable,
       "oaFecConfigurationEntry": oaFecConfigurationEntry,
       "oaFecConfigurationSlotIndex": oaFecConfigurationSlotIndex,
       "oaFecConfigurationSupportedPorts": oaFecConfigurationSupportedPorts,
       "oaFecConfigurationMode": oaFecConfigurationMode,
       "oaFecStatisticsCurrentTable": oaFecStatisticsCurrentTable,
       "oaFecStatisticsCurrentEntry": oaFecStatisticsCurrentEntry,
       "oaFecStatisticsSlotIndex": oaFecStatisticsSlotIndex,
       "oaFecStatisticsPortIndex": oaFecStatisticsPortIndex,
       "oaFecStatisticsCorrectedBits": oaFecStatisticsCorrectedBits,
       "oaFecStatisticsUncorrectedBlocks": oaFecStatisticsUncorrectedBlocks,
       "oaFecStatIntervalTable": oaFecStatIntervalTable,
       "oaFecStatIntervalEntry": oaFecStatIntervalEntry,
       "oaFecStatIntervalSlotNumber": oaFecStatIntervalSlotNumber,
       "oaFecStatIntervalPortNumber": oaFecStatIntervalPortNumber,
       "oaFecStatIntervalNumber": oaFecStatIntervalNumber,
       "oaFecStatIntervalCorrectedBits": oaFecStatIntervalCorrectedBits,
       "oaFecStatIntervalUncorrectedBlocks": oaFecStatIntervalUncorrectedBlocks,
       "oaFecStatIntervalValidData": oaFecStatIntervalValidData,
       "oaFecStatCurrentDayTable": oaFecStatCurrentDayTable,
       "oaFecStatCurrentDayEntry": oaFecStatCurrentDayEntry,
       "oaFecDayStatSlotIndex": oaFecDayStatSlotIndex,
       "oaFecDayStatPortIndex": oaFecDayStatPortIndex,
       "oaFecDayStatCorrectedBits": oaFecDayStatCorrectedBits,
       "oaFecDayStatUncorrectedBlocks": oaFecDayStatUncorrectedBlocks,
       "oaFecStatPrevDayTable": oaFecStatPrevDayTable,
       "oaFecStatPrevDayEntry": oaFecStatPrevDayEntry,
       "oaFecPrevDayStatSlotIndex": oaFecPrevDayStatSlotIndex,
       "oaFecPrevDayStatPortIndex": oaFecPrevDayStatPortIndex,
       "oaFecPrevDayStatCorrectedBits": oaFecPrevDayStatCorrectedBits,
       "oaFecPrevDayStatUncorrBlocks": oaFecPrevDayStatUncorrBlocks,
       "oaFecPrevDayStatValidData": oaFecPrevDayStatValidData,
       "oaFecMibConformance": oaFecMibConformance,
       "oaFecMibMIBCompliances": oaFecMibMIBCompliances,
       "oaFecMibMIBCompliance": oaFecMibMIBCompliance,
       "oaFecMibMIBGroups": oaFecMibMIBGroups,
       "oaFecMibMandatoryConfigurationGroup": oaFecMibMandatoryConfigurationGroup,
       "oaFecMibMandatoryStatCurrentGroup": oaFecMibMandatoryStatCurrentGroup,
       "oaFecMibMandatoryStatIntervalGroup": oaFecMibMandatoryStatIntervalGroup,
       "oaFecMibMandatoryStatCurrentDayGroup": oaFecMibMandatoryStatCurrentDayGroup,
       "oaFecMibMandatoryStatPrevDayGroup": oaFecMibMandatoryStatPrevDayGroup}
)
