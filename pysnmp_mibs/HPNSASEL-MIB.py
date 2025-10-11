# SNMP MIB module (HPNSASEL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HPNSASEL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:41:56 2025
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

_Hp_ObjectIdentity = ObjectIdentity
hp = _Hp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11)
)
_Nm_ObjectIdentity = ObjectIdentity
nm = _Nm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2)
)
_Hpnsa_ObjectIdentity = ObjectIdentity
hpnsa = _Hpnsa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23)
)
_HpSELAgt_ObjectIdentity = ObjectIdentity
hpSELAgt = _HpSELAgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29)
)


class _HpSELAgtVersion_Type(Integer32):
    """Custom type hpSELAgtVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSELAgtVersion_Type.__name__ = "Integer32"
_HpSELAgtVersion_Object = MibScalar
hpSELAgtVersion = _HpSELAgtVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 1),
    _HpSELAgtVersion_Type()
)
hpSELAgtVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtVersion.setStatus("mandatory")


class _HpSELAgtRevision_Type(Integer32):
    """Custom type hpSELAgtRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSELAgtRevision_Type.__name__ = "Integer32"
_HpSELAgtRevision_Object = MibScalar
hpSELAgtRevision = _HpSELAgtRevision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 2),
    _HpSELAgtRevision_Type()
)
hpSELAgtRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtRevision.setStatus("mandatory")


class _HpSELAgtMibVersion_Type(Integer32):
    """Custom type hpSELAgtMibVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSELAgtMibVersion_Type.__name__ = "Integer32"
_HpSELAgtMibVersion_Object = MibScalar
hpSELAgtMibVersion = _HpSELAgtMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 3),
    _HpSELAgtMibVersion_Type()
)
hpSELAgtMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtMibVersion.setStatus("mandatory")


class _HpSELAgtMibRevision_Type(Integer32):
    """Custom type hpSELAgtMibRevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSELAgtMibRevision_Type.__name__ = "Integer32"
_HpSELAgtMibRevision_Object = MibScalar
hpSELAgtMibRevision = _HpSELAgtMibRevision_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 4),
    _HpSELAgtMibRevision_Type()
)
hpSELAgtMibRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtMibRevision.setStatus("mandatory")


class _HpSELAgtNumEntries_Type(Integer32):
    """Custom type hpSELAgtNumEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSELAgtNumEntries_Type.__name__ = "Integer32"
_HpSELAgtNumEntries_Object = MibScalar
hpSELAgtNumEntries = _HpSELAgtNumEntries_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 5),
    _HpSELAgtNumEntries_Type()
)
hpSELAgtNumEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtNumEntries.setStatus("mandatory")
_HpSELAgtLogTable_Object = MibTable
hpSELAgtLogTable = _HpSELAgtLogTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6)
)
if mibBuilder.loadTexts:
    hpSELAgtLogTable.setStatus("mandatory")
_HpSELAgtLogEntry_Object = MibTableRow
hpSELAgtLogEntry = _HpSELAgtLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1)
)
hpSELAgtLogEntry.setIndexNames(
    (0, "HPNSASEL-MIB", "hpSELAgtIndex"),
)
if mibBuilder.loadTexts:
    hpSELAgtLogEntry.setStatus("mandatory")
_HpSELAgtIndex_Type = Integer32
_HpSELAgtIndex_Object = MibTableColumn
hpSELAgtIndex = _HpSELAgtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 1),
    _HpSELAgtIndex_Type()
)
hpSELAgtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtIndex.setStatus("mandatory")


class _HpSELAgtRecordID_Type(Integer32):
    """Custom type hpSELAgtRecordID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpSELAgtRecordID_Type.__name__ = "Integer32"
_HpSELAgtRecordID_Object = MibTableColumn
hpSELAgtRecordID = _HpSELAgtRecordID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 2),
    _HpSELAgtRecordID_Type()
)
hpSELAgtRecordID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtRecordID.setStatus("mandatory")


class _HpSELAgtRecordType_Type(Integer32):
    """Custom type hpSELAgtRecordType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtRecordType_Type.__name__ = "Integer32"
_HpSELAgtRecordType_Object = MibTableColumn
hpSELAgtRecordType = _HpSELAgtRecordType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 3),
    _HpSELAgtRecordType_Type()
)
hpSELAgtRecordType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtRecordType.setStatus("mandatory")
_HpSELAgtTimestamp_Type = Integer32
_HpSELAgtTimestamp_Object = MibTableColumn
hpSELAgtTimestamp = _HpSELAgtTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 4),
    _HpSELAgtTimestamp_Type()
)
hpSELAgtTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtTimestamp.setStatus("mandatory")


class _HpSELAgtGeneratorID_Type(Integer32):
    """Custom type hpSELAgtGeneratorID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtGeneratorID_Type.__name__ = "Integer32"
_HpSELAgtGeneratorID_Object = MibTableColumn
hpSELAgtGeneratorID = _HpSELAgtGeneratorID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 5),
    _HpSELAgtGeneratorID_Type()
)
hpSELAgtGeneratorID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtGeneratorID.setStatus("mandatory")


class _HpSELAgtGeneratorLUN_Type(Integer32):
    """Custom type hpSELAgtGeneratorLUN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtGeneratorLUN_Type.__name__ = "Integer32"
_HpSELAgtGeneratorLUN_Object = MibTableColumn
hpSELAgtGeneratorLUN = _HpSELAgtGeneratorLUN_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 6),
    _HpSELAgtGeneratorLUN_Type()
)
hpSELAgtGeneratorLUN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtGeneratorLUN.setStatus("mandatory")


class _HpSELAgtEventVersion_Type(Integer32):
    """Custom type hpSELAgtEventVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtEventVersion_Type.__name__ = "Integer32"
_HpSELAgtEventVersion_Object = MibTableColumn
hpSELAgtEventVersion = _HpSELAgtEventVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 7),
    _HpSELAgtEventVersion_Type()
)
hpSELAgtEventVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtEventVersion.setStatus("mandatory")


class _HpSELAgtSensorType_Type(Integer32):
    """Custom type hpSELAgtSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtSensorType_Type.__name__ = "Integer32"
_HpSELAgtSensorType_Object = MibTableColumn
hpSELAgtSensorType = _HpSELAgtSensorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 8),
    _HpSELAgtSensorType_Type()
)
hpSELAgtSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtSensorType.setStatus("mandatory")


class _HpSELAgtSensorNumber_Type(Integer32):
    """Custom type hpSELAgtSensorNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtSensorNumber_Type.__name__ = "Integer32"
_HpSELAgtSensorNumber_Object = MibTableColumn
hpSELAgtSensorNumber = _HpSELAgtSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 9),
    _HpSELAgtSensorNumber_Type()
)
hpSELAgtSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtSensorNumber.setStatus("mandatory")


class _HpSELAgtEventTrigger_Type(Integer32):
    """Custom type hpSELAgtEventTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtEventTrigger_Type.__name__ = "Integer32"
_HpSELAgtEventTrigger_Object = MibTableColumn
hpSELAgtEventTrigger = _HpSELAgtEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 10),
    _HpSELAgtEventTrigger_Type()
)
hpSELAgtEventTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtEventTrigger.setStatus("mandatory")


class _HpSELAgtEventData1_Type(Integer32):
    """Custom type hpSELAgtEventData1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtEventData1_Type.__name__ = "Integer32"
_HpSELAgtEventData1_Object = MibTableColumn
hpSELAgtEventData1 = _HpSELAgtEventData1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 11),
    _HpSELAgtEventData1_Type()
)
hpSELAgtEventData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtEventData1.setStatus("mandatory")


class _HpSELAgtEventData2_Type(Integer32):
    """Custom type hpSELAgtEventData2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtEventData2_Type.__name__ = "Integer32"
_HpSELAgtEventData2_Object = MibTableColumn
hpSELAgtEventData2 = _HpSELAgtEventData2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 12),
    _HpSELAgtEventData2_Type()
)
hpSELAgtEventData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtEventData2.setStatus("mandatory")


class _HpSELAgtEventData3_Type(Integer32):
    """Custom type hpSELAgtEventData3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtEventData3_Type.__name__ = "Integer32"
_HpSELAgtEventData3_Object = MibTableColumn
hpSELAgtEventData3 = _HpSELAgtEventData3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 13),
    _HpSELAgtEventData3_Type()
)
hpSELAgtEventData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtEventData3.setStatus("mandatory")
_HpSELAgtLineNum_Type = Integer32
_HpSELAgtLineNum_Object = MibTableColumn
hpSELAgtLineNum = _HpSELAgtLineNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 14),
    _HpSELAgtLineNum_Type()
)
hpSELAgtLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtLineNum.setStatus("mandatory")
_HpSELAgtStrInfo_Type = DisplayString
_HpSELAgtStrInfo_Object = MibTableColumn
hpSELAgtStrInfo = _HpSELAgtStrInfo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 15),
    _HpSELAgtStrInfo_Type()
)
hpSELAgtStrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtStrInfo.setStatus("mandatory")
_HpSELAgtSeverity_Type = DisplayString
_HpSELAgtSeverity_Object = MibTableColumn
hpSELAgtSeverity = _HpSELAgtSeverity_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 6, 1, 16),
    _HpSELAgtSeverity_Type()
)
hpSELAgtSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtSeverity.setStatus("mandatory")


class _HpSELAgtFilterSensorType_Type(Integer32):
    """Custom type hpSELAgtFilterSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtFilterSensorType_Type.__name__ = "Integer32"
_HpSELAgtFilterSensorType_Object = MibScalar
hpSELAgtFilterSensorType = _HpSELAgtFilterSensorType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 7),
    _HpSELAgtFilterSensorType_Type()
)
hpSELAgtFilterSensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSELAgtFilterSensorType.setStatus("mandatory")


class _HpSELAgtFilterEventTrigger_Type(Integer32):
    """Custom type hpSELAgtFilterEventTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtFilterEventTrigger_Type.__name__ = "Integer32"
_HpSELAgtFilterEventTrigger_Object = MibScalar
hpSELAgtFilterEventTrigger = _HpSELAgtFilterEventTrigger_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 8),
    _HpSELAgtFilterEventTrigger_Type()
)
hpSELAgtFilterEventTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSELAgtFilterEventTrigger.setStatus("mandatory")


class _HpSELAgtFilterOffset_Type(Integer32):
    """Custom type hpSELAgtFilterOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HpSELAgtFilterOffset_Type.__name__ = "Integer32"
_HpSELAgtFilterOffset_Object = MibScalar
hpSELAgtFilterOffset = _HpSELAgtFilterOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 9),
    _HpSELAgtFilterOffset_Type()
)
hpSELAgtFilterOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSELAgtFilterOffset.setStatus("mandatory")
_HpSELAgtLogFile_Type = DisplayString
_HpSELAgtLogFile_Object = MibScalar
hpSELAgtLogFile = _HpSELAgtLogFile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 23, 29, 10),
    _HpSELAgtLogFile_Type()
)
hpSELAgtLogFile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSELAgtLogFile.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPNSASEL-MIB",
    **{"hp": hp,
       "nm": nm,
       "hpnsa": hpnsa,
       "hpSELAgt": hpSELAgt,
       "hpSELAgtVersion": hpSELAgtVersion,
       "hpSELAgtRevision": hpSELAgtRevision,
       "hpSELAgtMibVersion": hpSELAgtMibVersion,
       "hpSELAgtMibRevision": hpSELAgtMibRevision,
       "hpSELAgtNumEntries": hpSELAgtNumEntries,
       "hpSELAgtLogTable": hpSELAgtLogTable,
       "hpSELAgtLogEntry": hpSELAgtLogEntry,
       "hpSELAgtIndex": hpSELAgtIndex,
       "hpSELAgtRecordID": hpSELAgtRecordID,
       "hpSELAgtRecordType": hpSELAgtRecordType,
       "hpSELAgtTimestamp": hpSELAgtTimestamp,
       "hpSELAgtGeneratorID": hpSELAgtGeneratorID,
       "hpSELAgtGeneratorLUN": hpSELAgtGeneratorLUN,
       "hpSELAgtEventVersion": hpSELAgtEventVersion,
       "hpSELAgtSensorType": hpSELAgtSensorType,
       "hpSELAgtSensorNumber": hpSELAgtSensorNumber,
       "hpSELAgtEventTrigger": hpSELAgtEventTrigger,
       "hpSELAgtEventData1": hpSELAgtEventData1,
       "hpSELAgtEventData2": hpSELAgtEventData2,
       "hpSELAgtEventData3": hpSELAgtEventData3,
       "hpSELAgtLineNum": hpSELAgtLineNum,
       "hpSELAgtStrInfo": hpSELAgtStrInfo,
       "hpSELAgtSeverity": hpSELAgtSeverity,
       "hpSELAgtFilterSensorType": hpSELAgtFilterSensorType,
       "hpSELAgtFilterEventTrigger": hpSELAgtFilterEventTrigger,
       "hpSELAgtFilterOffset": hpSELAgtFilterOffset,
       "hpSELAgtLogFile": hpSELAgtLogFile}
)
