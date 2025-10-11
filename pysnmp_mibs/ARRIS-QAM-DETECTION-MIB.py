# SNMP MIB module (ARRIS-QAM-DETECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-QAM-DETECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:09:11 2025
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

(arrisProdIdCM,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdCM")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arrisQamDetectionMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12)
)
if mibBuilder.loadTexts:
    arrisQamDetectionMib.setRevisions(
        ("1911-08-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArrisQamDetectionMibObjects_ObjectIdentity = ObjectIdentity
arrisQamDetectionMibObjects = _ArrisQamDetectionMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1)
)
_ArrisQamDetectionConfig_ObjectIdentity = ObjectIdentity
arrisQamDetectionConfig = _ArrisQamDetectionConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 1)
)
_ArrisQamDetectionConfigEnable_Type = TruthValue
_ArrisQamDetectionConfigEnable_Object = MibScalar
arrisQamDetectionConfigEnable = _ArrisQamDetectionConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 1, 1),
    _ArrisQamDetectionConfigEnable_Type()
)
arrisQamDetectionConfigEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisQamDetectionConfigEnable.setStatus("current")
_ArrisQamDetectionConfigFrequencyTable_Object = MibTable
arrisQamDetectionConfigFrequencyTable = _ArrisQamDetectionConfigFrequencyTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 1, 2)
)
if mibBuilder.loadTexts:
    arrisQamDetectionConfigFrequencyTable.setStatus("current")
_ArrisQamDetectionConfigFrequencyEntry_Object = MibTableRow
arrisQamDetectionConfigFrequencyEntry = _ArrisQamDetectionConfigFrequencyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 1, 2, 1)
)
arrisQamDetectionConfigFrequencyEntry.setIndexNames(
    (0, "ARRIS-QAM-DETECTION-MIB", "arrisQamDetectionConfigFrequencyIndex"),
)
if mibBuilder.loadTexts:
    arrisQamDetectionConfigFrequencyEntry.setStatus("current")


class _ArrisQamDetectionConfigFrequencyIndex_Type(Integer32):
    """Custom type arrisQamDetectionConfigFrequencyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ArrisQamDetectionConfigFrequencyIndex_Type.__name__ = "Integer32"
_ArrisQamDetectionConfigFrequencyIndex_Object = MibTableColumn
arrisQamDetectionConfigFrequencyIndex = _ArrisQamDetectionConfigFrequencyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 1, 2, 1, 1),
    _ArrisQamDetectionConfigFrequencyIndex_Type()
)
arrisQamDetectionConfigFrequencyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisQamDetectionConfigFrequencyIndex.setStatus("current")


class _ArrisQamDetectionConfigFrequency_Type(Integer32):
    """Custom type arrisQamDetectionConfigFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(91000000, 999000000),
    )


_ArrisQamDetectionConfigFrequency_Type.__name__ = "Integer32"
_ArrisQamDetectionConfigFrequency_Object = MibTableColumn
arrisQamDetectionConfigFrequency = _ArrisQamDetectionConfigFrequency_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 1, 2, 1, 2),
    _ArrisQamDetectionConfigFrequency_Type()
)
arrisQamDetectionConfigFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisQamDetectionConfigFrequency.setStatus("current")
if mibBuilder.loadTexts:
    arrisQamDetectionConfigFrequency.setUnits("hertz")
_ArrisQamDetectionConfigClearResults_Type = TruthValue
_ArrisQamDetectionConfigClearResults_Object = MibScalar
arrisQamDetectionConfigClearResults = _ArrisQamDetectionConfigClearResults_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 1, 3),
    _ArrisQamDetectionConfigClearResults_Type()
)
arrisQamDetectionConfigClearResults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisQamDetectionConfigClearResults.setStatus("current")
_ArrisQamDetectionResultsTable_Object = MibTable
arrisQamDetectionResultsTable = _ArrisQamDetectionResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 2)
)
if mibBuilder.loadTexts:
    arrisQamDetectionResultsTable.setStatus("current")
_ArrisQamDetectionResultsEntry_Object = MibTableRow
arrisQamDetectionResultsEntry = _ArrisQamDetectionResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 2, 1)
)
arrisQamDetectionResultsEntry.setIndexNames(
    (0, "ARRIS-QAM-DETECTION-MIB", "arrisQamDetectionResultsIndex"),
)
if mibBuilder.loadTexts:
    arrisQamDetectionResultsEntry.setStatus("current")


class _ArrisQamDetectionResultsIndex_Type(Integer32):
    """Custom type arrisQamDetectionResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_ArrisQamDetectionResultsIndex_Type.__name__ = "Integer32"
_ArrisQamDetectionResultsIndex_Object = MibTableColumn
arrisQamDetectionResultsIndex = _ArrisQamDetectionResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 2, 1, 1),
    _ArrisQamDetectionResultsIndex_Type()
)
arrisQamDetectionResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisQamDetectionResultsIndex.setStatus("current")


class _ArrisQamDetectionResultsFreq_Type(Integer32):
    """Custom type arrisQamDetectionResultsFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(91000000, 999000000),
    )


_ArrisQamDetectionResultsFreq_Type.__name__ = "Integer32"
_ArrisQamDetectionResultsFreq_Object = MibTableColumn
arrisQamDetectionResultsFreq = _ArrisQamDetectionResultsFreq_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 2, 1, 2),
    _ArrisQamDetectionResultsFreq_Type()
)
arrisQamDetectionResultsFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisQamDetectionResultsFreq.setStatus("current")
if mibBuilder.loadTexts:
    arrisQamDetectionResultsFreq.setUnits("hertz")
_ArrisQamDetectionResultsTimestamp_Type = DisplayString
_ArrisQamDetectionResultsTimestamp_Object = MibTableColumn
arrisQamDetectionResultsTimestamp = _ArrisQamDetectionResultsTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 12, 1, 2, 1, 3),
    _ArrisQamDetectionResultsTimestamp_Type()
)
arrisQamDetectionResultsTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisQamDetectionResultsTimestamp.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-QAM-DETECTION-MIB",
    **{"arrisQamDetectionMib": arrisQamDetectionMib,
       "arrisQamDetectionMibObjects": arrisQamDetectionMibObjects,
       "arrisQamDetectionConfig": arrisQamDetectionConfig,
       "arrisQamDetectionConfigEnable": arrisQamDetectionConfigEnable,
       "arrisQamDetectionConfigFrequencyTable": arrisQamDetectionConfigFrequencyTable,
       "arrisQamDetectionConfigFrequencyEntry": arrisQamDetectionConfigFrequencyEntry,
       "arrisQamDetectionConfigFrequencyIndex": arrisQamDetectionConfigFrequencyIndex,
       "arrisQamDetectionConfigFrequency": arrisQamDetectionConfigFrequency,
       "arrisQamDetectionConfigClearResults": arrisQamDetectionConfigClearResults,
       "arrisQamDetectionResultsTable": arrisQamDetectionResultsTable,
       "arrisQamDetectionResultsEntry": arrisQamDetectionResultsEntry,
       "arrisQamDetectionResultsIndex": arrisQamDetectionResultsIndex,
       "arrisQamDetectionResultsFreq": arrisQamDetectionResultsFreq,
       "arrisQamDetectionResultsTimestamp": arrisQamDetectionResultsTimestamp}
)
