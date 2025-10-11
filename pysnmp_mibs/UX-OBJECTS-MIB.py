# SNMP MIB module (UX-OBJECTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonus/UX-OBJECTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:50 2025
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

(dsx0ConfigEntry,) = mibBuilder.importSymbols(
    "DS0-MIB",
    "dsx0ConfigEntry")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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

ux = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15)
)
if mibBuilder.loadTexts:
    ux.setRevisions(
        ("2009-11-04 17:05",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Net_ObjectIdentity = ObjectIdentity
net = _Net_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177)
)
_UxObjects_ObjectIdentity = ObjectIdentity
uxObjects = _UxObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1)
)
_UxChassis_ObjectIdentity = ObjectIdentity
uxChassis = _UxChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 1)
)
_ChasiDescUX2000_Type = DisplayString
_ChasiDescUX2000_Object = MibScalar
chasiDescUX2000 = _ChasiDescUX2000_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 1, 1),
    _ChasiDescUX2000_Type()
)
chasiDescUX2000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasiDescUX2000.setStatus("deprecated")
_ChasiDescUX1000_Type = DisplayString
_ChasiDescUX1000_Object = MibScalar
chasiDescUX1000 = _ChasiDescUX1000_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 1, 2),
    _ChasiDescUX1000_Type()
)
chasiDescUX1000.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasiDescUX1000.setStatus("deprecated")
_ChasiType_Type = DisplayString
_ChasiType_Object = MibScalar
chasiType = _ChasiType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 1, 3),
    _ChasiType_Type()
)
chasiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    chasiType.setStatus("current")
_UxAlarmCfgTable_Object = MibTable
uxAlarmCfgTable = _UxAlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2)
)
if mibBuilder.loadTexts:
    uxAlarmCfgTable.setStatus("current")
_UxAlarmCfgEntry_Object = MibTableRow
uxAlarmCfgEntry = _UxAlarmCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1)
)
uxAlarmCfgEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxAlarmIndex"),
)
if mibBuilder.loadTexts:
    uxAlarmCfgEntry.setStatus("current")


class _UxAlarmIndex_Type(Integer32):
    """Custom type uxAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147418112),
    )


_UxAlarmIndex_Type.__name__ = "Integer32"
_UxAlarmIndex_Object = MibTableColumn
uxAlarmIndex = _UxAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 1),
    _UxAlarmIndex_Type()
)
uxAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmIndex.setStatus("current")


class _UxAlarmID_Type(Integer32):
    """Custom type uxAlarmID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_UxAlarmID_Type.__name__ = "Integer32"
_UxAlarmID_Object = MibTableColumn
uxAlarmID = _UxAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 2),
    _UxAlarmID_Type()
)
uxAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmID.setStatus("current")


class _UxAlarmSubID_Type(Integer32):
    """Custom type uxAlarmSubID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxAlarmSubID_Type.__name__ = "Integer32"
_UxAlarmSubID_Object = MibTableColumn
uxAlarmSubID = _UxAlarmSubID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 3),
    _UxAlarmSubID_Type()
)
uxAlarmSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmSubID.setStatus("current")
_UxAlarmCondition_Type = DisplayString
_UxAlarmCondition_Object = MibTableColumn
uxAlarmCondition = _UxAlarmCondition_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 4),
    _UxAlarmCondition_Type()
)
uxAlarmCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmCondition.setStatus("current")


class _UxAlarmSeverity_Type(Integer32):
    """Custom type uxAlarmSeverity based on Integer32"""
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
        *(("none", 0),
          ("warning", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_UxAlarmSeverity_Type.__name__ = "Integer32"
_UxAlarmSeverity_Object = MibTableColumn
uxAlarmSeverity = _UxAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 5),
    _UxAlarmSeverity_Type()
)
uxAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmSeverity.setStatus("current")


class _UxAlarmCategory_Type(Integer32):
    """Custom type uxAlarmCategory based on Integer32"""
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
        *(("communication", 1),
          ("equipment", 2),
          ("processing", 3),
          ("general", 4),
          ("environmental", 5),
          ("qos", 6),
          ("security", 7))
    )


_UxAlarmCategory_Type.__name__ = "Integer32"
_UxAlarmCategory_Object = MibTableColumn
uxAlarmCategory = _UxAlarmCategory_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 6),
    _UxAlarmCategory_Type()
)
uxAlarmCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmCategory.setStatus("current")


class _UxAlarmCancelType_Type(Integer32):
    """Custom type uxAlarmCancelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonAutoCancel", 0),
          ("autoCancel", 1))
    )


_UxAlarmCancelType_Type.__name__ = "Integer32"
_UxAlarmCancelType_Object = MibTableColumn
uxAlarmCancelType = _UxAlarmCancelType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 7),
    _UxAlarmCancelType_Type()
)
uxAlarmCancelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmCancelType.setStatus("current")


class _UxAlarmEvtType_Type(Integer32):
    """Custom type uxAlarmEvtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alarm", 1),
          ("event", 2))
    )


_UxAlarmEvtType_Type.__name__ = "Integer32"
_UxAlarmEvtType_Object = MibTableColumn
uxAlarmEvtType = _UxAlarmEvtType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 8),
    _UxAlarmEvtType_Type()
)
uxAlarmEvtType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmEvtType.setStatus("current")
_UxAlarmDecodeKey_Type = DisplayString
_UxAlarmDecodeKey_Object = MibTableColumn
uxAlarmDecodeKey = _UxAlarmDecodeKey_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 9),
    _UxAlarmDecodeKey_Type()
)
uxAlarmDecodeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmDecodeKey.setStatus("current")


class _UxAlarmClrID_Type(Integer32):
    """Custom type uxAlarmClrID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_UxAlarmClrID_Type.__name__ = "Integer32"
_UxAlarmClrID_Object = MibTableColumn
uxAlarmClrID = _UxAlarmClrID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 10),
    _UxAlarmClrID_Type()
)
uxAlarmClrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmClrID.setStatus("current")


class _UxAlarmClrSubID_Type(Integer32):
    """Custom type uxAlarmClrSubID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxAlarmClrSubID_Type.__name__ = "Integer32"
_UxAlarmClrSubID_Object = MibTableColumn
uxAlarmClrSubID = _UxAlarmClrSubID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 11),
    _UxAlarmClrSubID_Type()
)
uxAlarmClrSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmClrSubID.setStatus("current")
_UxAlarmDescription_Type = DisplayString
_UxAlarmDescription_Object = MibTableColumn
uxAlarmDescription = _UxAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 2, 1, 12),
    _UxAlarmDescription_Type()
)
uxAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmDescription.setStatus("current")
_UxActAlarmTable_Object = MibTable
uxActAlarmTable = _UxActAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3)
)
if mibBuilder.loadTexts:
    uxActAlarmTable.setStatus("current")
_UxActAlarmEntry_Object = MibTableRow
uxActAlarmEntry = _UxActAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1)
)
uxActAlarmEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxAlarmActiveIndex"),
)
if mibBuilder.loadTexts:
    uxActAlarmEntry.setStatus("current")


class _UxAlarmActiveIndex_Type(Integer32):
    """Custom type uxAlarmActiveIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147418112),
    )


_UxAlarmActiveIndex_Type.__name__ = "Integer32"
_UxAlarmActiveIndex_Object = MibTableColumn
uxAlarmActiveIndex = _UxAlarmActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 1),
    _UxAlarmActiveIndex_Type()
)
uxAlarmActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveIndex.setStatus("current")


class _UxAlarmConfigIndex_Type(Integer32):
    """Custom type uxAlarmConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147418112),
    )


_UxAlarmConfigIndex_Type.__name__ = "Integer32"
_UxAlarmConfigIndex_Object = MibTableColumn
uxAlarmConfigIndex = _UxAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 2),
    _UxAlarmConfigIndex_Type()
)
uxAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmConfigIndex.setStatus("current")


class _UxAlarmActiveID_Type(Integer32):
    """Custom type uxAlarmActiveID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_UxAlarmActiveID_Type.__name__ = "Integer32"
_UxAlarmActiveID_Object = MibTableColumn
uxAlarmActiveID = _UxAlarmActiveID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 3),
    _UxAlarmActiveID_Type()
)
uxAlarmActiveID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveID.setStatus("current")


class _UxAlarmActiveSubID_Type(Integer32):
    """Custom type uxAlarmActiveSubID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxAlarmActiveSubID_Type.__name__ = "Integer32"
_UxAlarmActiveSubID_Object = MibTableColumn
uxAlarmActiveSubID = _UxAlarmActiveSubID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 4),
    _UxAlarmActiveSubID_Type()
)
uxAlarmActiveSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveSubID.setStatus("current")
_UxAlarmActiveCondition_Type = DisplayString
_UxAlarmActiveCondition_Object = MibTableColumn
uxAlarmActiveCondition = _UxAlarmActiveCondition_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 5),
    _UxAlarmActiveCondition_Type()
)
uxAlarmActiveCondition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveCondition.setStatus("current")


class _UxAlarmActiveSeverity_Type(Integer32):
    """Custom type uxAlarmActiveSeverity based on Integer32"""
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
        *(("none", 0),
          ("warning", 1),
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_UxAlarmActiveSeverity_Type.__name__ = "Integer32"
_UxAlarmActiveSeverity_Object = MibTableColumn
uxAlarmActiveSeverity = _UxAlarmActiveSeverity_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 6),
    _UxAlarmActiveSeverity_Type()
)
uxAlarmActiveSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveSeverity.setStatus("current")


class _UxAlarmActiveCategory_Type(Integer32):
    """Custom type uxAlarmActiveCategory based on Integer32"""
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
        *(("communication", 1),
          ("equipment", 2),
          ("processing", 3),
          ("general", 4),
          ("environmental", 5),
          ("qos", 6),
          ("security", 7))
    )


_UxAlarmActiveCategory_Type.__name__ = "Integer32"
_UxAlarmActiveCategory_Object = MibTableColumn
uxAlarmActiveCategory = _UxAlarmActiveCategory_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 7),
    _UxAlarmActiveCategory_Type()
)
uxAlarmActiveCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveCategory.setStatus("current")


class _UxAlarmActiveCancelType_Type(Integer32):
    """Custom type uxAlarmActiveCancelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nonAutoCancel", 0),
          ("autoCancel", 1))
    )


_UxAlarmActiveCancelType_Type.__name__ = "Integer32"
_UxAlarmActiveCancelType_Object = MibTableColumn
uxAlarmActiveCancelType = _UxAlarmActiveCancelType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 8),
    _UxAlarmActiveCancelType_Type()
)
uxAlarmActiveCancelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveCancelType.setStatus("current")
_UxAlarmActiveFirstOccur_Type = Counter64
_UxAlarmActiveFirstOccur_Object = MibTableColumn
uxAlarmActiveFirstOccur = _UxAlarmActiveFirstOccur_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 9),
    _UxAlarmActiveFirstOccur_Type()
)
uxAlarmActiveFirstOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveFirstOccur.setStatus("current")
_UxAlarmActiveLastOccur_Type = Counter64
_UxAlarmActiveLastOccur_Object = MibTableColumn
uxAlarmActiveLastOccur = _UxAlarmActiveLastOccur_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 10),
    _UxAlarmActiveLastOccur_Type()
)
uxAlarmActiveLastOccur.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveLastOccur.setStatus("current")


class _UxAlarmActiveCount_Type(Integer32):
    """Custom type uxAlarmActiveCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UxAlarmActiveCount_Type.__name__ = "Integer32"
_UxAlarmActiveCount_Object = MibTableColumn
uxAlarmActiveCount = _UxAlarmActiveCount_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 11),
    _UxAlarmActiveCount_Type()
)
uxAlarmActiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveCount.setStatus("current")
_UxAlarmActiveDecodeKey_Type = DisplayString
_UxAlarmActiveDecodeKey_Object = MibTableColumn
uxAlarmActiveDecodeKey = _UxAlarmActiveDecodeKey_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 12),
    _UxAlarmActiveDecodeKey_Type()
)
uxAlarmActiveDecodeKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveDecodeKey.setStatus("current")
_UxAlarmActiveSourceInstance_Type = DisplayString
_UxAlarmActiveSourceInstance_Object = MibTableColumn
uxAlarmActiveSourceInstance = _UxAlarmActiveSourceInstance_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 13),
    _UxAlarmActiveSourceInstance_Type()
)
uxAlarmActiveSourceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveSourceInstance.setStatus("current")


class _UxAlarmActiveState_Type(Integer32):
    """Custom type uxAlarmActiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("acklnowledged", 1),
          ("unacknowledged", 2),
          ("cancel", 3))
    )


_UxAlarmActiveState_Type.__name__ = "Integer32"
_UxAlarmActiveState_Object = MibTableColumn
uxAlarmActiveState = _UxAlarmActiveState_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 14),
    _UxAlarmActiveState_Type()
)
uxAlarmActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveState.setStatus("current")


class _UxAlarmActiveClrEvtID_Type(Integer32):
    """Custom type uxAlarmActiveClrEvtID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_UxAlarmActiveClrEvtID_Type.__name__ = "Integer32"
_UxAlarmActiveClrEvtID_Object = MibTableColumn
uxAlarmActiveClrEvtID = _UxAlarmActiveClrEvtID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 15),
    _UxAlarmActiveClrEvtID_Type()
)
uxAlarmActiveClrEvtID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveClrEvtID.setStatus("current")


class _UxAlarmActiveClrEvtSubID_Type(Integer32):
    """Custom type uxAlarmActiveClrEvtSubID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxAlarmActiveClrEvtSubID_Type.__name__ = "Integer32"
_UxAlarmActiveClrEvtSubID_Object = MibTableColumn
uxAlarmActiveClrEvtSubID = _UxAlarmActiveClrEvtSubID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 16),
    _UxAlarmActiveClrEvtSubID_Type()
)
uxAlarmActiveClrEvtSubID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveClrEvtSubID.setStatus("current")
_UxAlarmActiveDescription_Type = DisplayString
_UxAlarmActiveDescription_Object = MibTableColumn
uxAlarmActiveDescription = _UxAlarmActiveDescription_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 17),
    _UxAlarmActiveDescription_Type()
)
uxAlarmActiveDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveDescription.setStatus("current")


class _UxAlarmActiveHighestSeverityAlarm_Type(Integer32):
    """Custom type uxAlarmActiveHighestSeverityAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_UxAlarmActiveHighestSeverityAlarm_Type.__name__ = "Integer32"
_UxAlarmActiveHighestSeverityAlarm_Object = MibTableColumn
uxAlarmActiveHighestSeverityAlarm = _UxAlarmActiveHighestSeverityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 18),
    _UxAlarmActiveHighestSeverityAlarm_Type()
)
uxAlarmActiveHighestSeverityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveHighestSeverityAlarm.setStatus("current")
_UxAlarmActiveHardWareID_Type = DisplayString
_UxAlarmActiveHardWareID_Object = MibTableColumn
uxAlarmActiveHardWareID = _UxAlarmActiveHardWareID_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 3, 1, 19),
    _UxAlarmActiveHardWareID_Type()
)
uxAlarmActiveHardWareID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxAlarmActiveHardWareID.setStatus("current")
_IpTelephony_ObjectIdentity = ObjectIdentity
ipTelephony = _IpTelephony_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5)
)
_UxSystemUsageStatsIntervalTable_Object = MibTable
uxSystemUsageStatsIntervalTable = _UxSystemUsageStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 9)
)
if mibBuilder.loadTexts:
    uxSystemUsageStatsIntervalTable.setStatus("current")
_UxSystemUsageIntervalEntry_Object = MibTableRow
uxSystemUsageIntervalEntry = _UxSystemUsageIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 9, 1)
)
uxSystemUsageIntervalEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxSystemUsageIntervalNumber"),
)
if mibBuilder.loadTexts:
    uxSystemUsageIntervalEntry.setStatus("current")


class _UxSystemUsageIntervalNumber_Type(Integer32):
    """Custom type uxSystemUsageIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_UxSystemUsageIntervalNumber_Type.__name__ = "Integer32"
_UxSystemUsageIntervalNumber_Object = MibTableColumn
uxSystemUsageIntervalNumber = _UxSystemUsageIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 9, 1, 1),
    _UxSystemUsageIntervalNumber_Type()
)
uxSystemUsageIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSystemUsageIntervalNumber.setStatus("current")
_UxSystemUsageIntervalCPUUsage_Type = PerfTotalCount
_UxSystemUsageIntervalCPUUsage_Object = MibTableColumn
uxSystemUsageIntervalCPUUsage = _UxSystemUsageIntervalCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 9, 1, 2),
    _UxSystemUsageIntervalCPUUsage_Type()
)
uxSystemUsageIntervalCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSystemUsageIntervalCPUUsage.setStatus("current")
_UxSystemUsageIntervalMemoryUsage_Type = PerfTotalCount
_UxSystemUsageIntervalMemoryUsage_Object = MibTableColumn
uxSystemUsageIntervalMemoryUsage = _UxSystemUsageIntervalMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 9, 1, 3),
    _UxSystemUsageIntervalMemoryUsage_Type()
)
uxSystemUsageIntervalMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSystemUsageIntervalMemoryUsage.setStatus("current")
_UxDSPPeakUsageStatsIntervalTable_Object = MibTable
uxDSPPeakUsageStatsIntervalTable = _UxDSPPeakUsageStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 14)
)
if mibBuilder.loadTexts:
    uxDSPPeakUsageStatsIntervalTable.setStatus("current")
_UxDSPPeakUsageIntervalEntry_Object = MibTableRow
uxDSPPeakUsageIntervalEntry = _UxDSPPeakUsageIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 14, 1)
)
uxDSPPeakUsageIntervalEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxDSPPeakUsageIntervalIndex"),
)
if mibBuilder.loadTexts:
    uxDSPPeakUsageIntervalEntry.setStatus("current")


class _UxDSPPeakUsageIntervalIndex_Type(Integer32):
    """Custom type uxDSPPeakUsageIntervalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UxDSPPeakUsageIntervalIndex_Type.__name__ = "Integer32"
_UxDSPPeakUsageIntervalIndex_Object = MibTableColumn
uxDSPPeakUsageIntervalIndex = _UxDSPPeakUsageIntervalIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 14, 1, 1),
    _UxDSPPeakUsageIntervalIndex_Type()
)
uxDSPPeakUsageIntervalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPPeakUsageIntervalIndex.setStatus("current")
_UxDSPPeakIntervalUsage_Type = PerfCurrentCount
_UxDSPPeakIntervalUsage_Object = MibTableColumn
uxDSPPeakIntervalUsage = _UxDSPPeakIntervalUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 5, 14, 1, 2),
    _UxDSPPeakIntervalUsage_Type()
)
uxDSPPeakIntervalUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPPeakIntervalUsage.setStatus("current")
_UxDSPResourceTable_Object = MibTable
uxDSPResourceTable = _UxDSPResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6)
)
if mibBuilder.loadTexts:
    uxDSPResourceTable.setStatus("current")
_UxDSPResourceEntry_Object = MibTableRow
uxDSPResourceEntry = _UxDSPResourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1)
)
uxDSPResourceEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxDSPIndex"),
)
if mibBuilder.loadTexts:
    uxDSPResourceEntry.setStatus("current")


class _UxDSPIndex_Type(Integer32):
    """Custom type uxDSPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxDSPIndex_Type.__name__ = "Integer32"
_UxDSPIndex_Object = MibTableColumn
uxDSPIndex = _UxDSPIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1, 1),
    _UxDSPIndex_Type()
)
uxDSPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPIndex.setStatus("current")
_UxDSPModType_Type = DisplayString
_UxDSPModType_Object = MibTableColumn
uxDSPModType = _UxDSPModType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1, 2),
    _UxDSPModType_Type()
)
uxDSPModType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPModType.setStatus("current")


class _UxDSPIsPresent_Type(Integer32):
    """Custom type uxDSPIsPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_UxDSPIsPresent_Type.__name__ = "Integer32"
_UxDSPIsPresent_Object = MibTableColumn
uxDSPIsPresent = _UxDSPIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1, 3),
    _UxDSPIsPresent_Type()
)
uxDSPIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPIsPresent.setStatus("current")
_UxDSPCPUUsage_Type = Integer32
_UxDSPCPUUsage_Object = MibTableColumn
uxDSPCPUUsage = _UxDSPCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1, 4),
    _UxDSPCPUUsage_Type()
)
uxDSPCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPCPUUsage.setStatus("current")
_UxDSPChannelsInUse_Type = Integer32
_UxDSPChannelsInUse_Object = MibTableColumn
uxDSPChannelsInUse = _UxDSPChannelsInUse_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1, 5),
    _UxDSPChannelsInUse_Type()
)
uxDSPChannelsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPChannelsInUse.setStatus("current")


class _UxDSPServiceStatus_Type(Integer32):
    """Custom type uxDSPServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_UxDSPServiceStatus_Type.__name__ = "Integer32"
_UxDSPServiceStatus_Object = MibTableColumn
uxDSPServiceStatus = _UxDSPServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1, 6),
    _UxDSPServiceStatus_Type()
)
uxDSPServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPServiceStatus.setStatus("current")
_UxCodecsSupported_Type = DisplayString
_UxCodecsSupported_Object = MibTableColumn
uxCodecsSupported = _UxCodecsSupported_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 6, 1, 7),
    _UxCodecsSupported_Type()
)
uxCodecsSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCodecsSupported.setStatus("current")
_UxDSX0ConfigTable_Object = MibTable
uxDSX0ConfigTable = _UxDSX0ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 7)
)
if mibBuilder.loadTexts:
    uxDSX0ConfigTable.setStatus("current")
_UxDSX0ConfigEntry_Object = MibTableRow
uxDSX0ConfigEntry = _UxDSX0ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 7, 1)
)
if mibBuilder.loadTexts:
    uxDSX0ConfigEntry.setStatus("current")


class _UxDSX0Type_Type(Integer32):
    """Custom type uxDSX0Type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("e1", 0),
          ("t1", 1))
    )


_UxDSX0Type_Type.__name__ = "Integer32"
_UxDSX0Type_Object = MibTableColumn
uxDSX0Type = _UxDSX0Type_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 7, 1, 1),
    _UxDSX0Type_Type()
)
uxDSX0Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSX0Type.setStatus("current")
_UxDSX0Speed_Type = Integer32
_UxDSX0Speed_Object = MibTableColumn
uxDSX0Speed = _UxDSX0Speed_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 7, 1, 2),
    _UxDSX0Speed_Type()
)
uxDSX0Speed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSX0Speed.setStatus("current")
_UxDSX0Lastchange_Type = Integer32
_UxDSX0Lastchange_Object = MibTableColumn
uxDSX0Lastchange = _UxDSX0Lastchange_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 7, 1, 3),
    _UxDSX0Lastchange_Type()
)
uxDSX0Lastchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSX0Lastchange.setStatus("current")


class _UxDSX0AdminState_Type(Integer32):
    """Custom type uxDSX0AdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_UxDSX0AdminState_Type.__name__ = "Integer32"
_UxDSX0AdminState_Object = MibTableColumn
uxDSX0AdminState = _UxDSX0AdminState_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 7, 1, 4),
    _UxDSX0AdminState_Type()
)
uxDSX0AdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSX0AdminState.setStatus("current")
_UxModuleTable_Object = MibTable
uxModuleTable = _UxModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8)
)
if mibBuilder.loadTexts:
    uxModuleTable.setStatus("current")
_UxModuleEntry_Object = MibTableRow
uxModuleEntry = _UxModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1)
)
uxModuleEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxModuleIndex"),
)
if mibBuilder.loadTexts:
    uxModuleEntry.setStatus("current")


class _UxModuleIndex_Type(Integer32):
    """Custom type uxModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxModuleIndex_Type.__name__ = "Integer32"
_UxModuleIndex_Object = MibTableColumn
uxModuleIndex = _UxModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1, 1),
    _UxModuleIndex_Type()
)
uxModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxModuleIndex.setStatus("current")


class _UxModuleType_Type(Integer32):
    """Custom type uxModuleType based on Integer32"""
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dS1-2Spans", 1),
          ("dS1-4Spans", 2),
          ("dS1-8Spans", 3),
          ("eX", 4),
          ("mSPDC910DSP", 5),
          ("mSPDC300DSP", 6),
          ("reservedModule1", 7),
          ("reservedModule2", 8),
          ("reservedModule3", 9),
          ("reservedModule4", 10),
          ("aSM", 11),
          ("mainBoard", 12),
          ("chassis", 13),
          ("powerSupply", 14),
          ("reservedModule5", 15),
          ("node", 16),
          ("fXS-8PortsLineCard", 17),
          ("fXS-16PortsLineCard", 18),
          ("fXS-24PortsLineCard", 19),
          ("fXS-4PortsLowerBoard", 20),
          ("fXS-4PortsUpperBoard", 21),
          ("fXO-4PortsLowerBoard", 22),
          ("fXO-4PortsUpperBoard", 23),
          ("bRI-4PortsBoard", 24),
          ("dS1-1SpanBoard", 25),
          ("dS1-2SpansBoard", 26),
          ("fXS-4PortsNRLowerBoard", 27))
    )


_UxModuleType_Type.__name__ = "Integer32"
_UxModuleType_Object = MibTableColumn
uxModuleType = _UxModuleType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1, 2),
    _UxModuleType_Type()
)
uxModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxModuleType.setStatus("current")
_UxModulePartNumber_Type = DisplayString
_UxModulePartNumber_Object = MibTableColumn
uxModulePartNumber = _UxModulePartNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1, 3),
    _UxModulePartNumber_Type()
)
uxModulePartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxModulePartNumber.setStatus("current")
_UxModuleVersionNumber_Type = DisplayString
_UxModuleVersionNumber_Object = MibTableColumn
uxModuleVersionNumber = _UxModuleVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1, 4),
    _UxModuleVersionNumber_Type()
)
uxModuleVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxModuleVersionNumber.setStatus("current")
_UxModuleSerialNumber_Type = DisplayString
_UxModuleSerialNumber_Object = MibTableColumn
uxModuleSerialNumber = _UxModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1, 5),
    _UxModuleSerialNumber_Type()
)
uxModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxModuleSerialNumber.setStatus("current")
_UxModuleMfgWeek_Type = Integer32
_UxModuleMfgWeek_Object = MibTableColumn
uxModuleMfgWeek = _UxModuleMfgWeek_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1, 6),
    _UxModuleMfgWeek_Type()
)
uxModuleMfgWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxModuleMfgWeek.setStatus("current")
_UxModuleMfgYear_Type = Integer32
_UxModuleMfgYear_Object = MibTableColumn
uxModuleMfgYear = _UxModuleMfgYear_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 8, 1, 7),
    _UxModuleMfgYear_Type()
)
uxModuleMfgYear.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxModuleMfgYear.setStatus("current")
_UxPSUTable_Object = MibTable
uxPSUTable = _UxPSUTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9)
)
if mibBuilder.loadTexts:
    uxPSUTable.setStatus("current")
_UxPSUEntry_Object = MibTableRow
uxPSUEntry = _UxPSUEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1)
)
uxPSUEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxPSUIndex"),
)
if mibBuilder.loadTexts:
    uxPSUEntry.setStatus("current")


class _UxPSUIndex_Type(Integer32):
    """Custom type uxPSUIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UxPSUIndex_Type.__name__ = "Integer32"
_UxPSUIndex_Object = MibTableColumn
uxPSUIndex = _UxPSUIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 1),
    _UxPSUIndex_Type()
)
uxPSUIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUIndex.setStatus("current")


class _UxPSUIsPresent_Type(Integer32):
    """Custom type uxPSUIsPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("present", 1),
          ("notpresent", 2))
    )


_UxPSUIsPresent_Type.__name__ = "Integer32"
_UxPSUIsPresent_Object = MibTableColumn
uxPSUIsPresent = _UxPSUIsPresent_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 2),
    _UxPSUIsPresent_Type()
)
uxPSUIsPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUIsPresent.setStatus("current")


class _UxPSUIsInputGood_Type(Integer32):
    """Custom type uxPSUIsInputGood based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_UxPSUIsInputGood_Type.__name__ = "Integer32"
_UxPSUIsInputGood_Object = MibTableColumn
uxPSUIsInputGood = _UxPSUIsInputGood_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 3),
    _UxPSUIsInputGood_Type()
)
uxPSUIsInputGood.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUIsInputGood.setStatus("current")


class _UxPSUInputType_Type(Integer32):
    """Custom type uxPSUInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notapplicable", 0),
          ("ac", 1),
          ("dc", 2))
    )


_UxPSUInputType_Type.__name__ = "Integer32"
_UxPSUInputType_Object = MibTableColumn
uxPSUInputType = _UxPSUInputType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 4),
    _UxPSUInputType_Type()
)
uxPSUInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUInputType.setStatus("current")


class _UxPSUPowerIn_Type(Integer32):
    """Custom type uxPSUPowerIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_UxPSUPowerIn_Type.__name__ = "Integer32"
_UxPSUPowerIn_Object = MibTableColumn
uxPSUPowerIn = _UxPSUPowerIn_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 5),
    _UxPSUPowerIn_Type()
)
uxPSUPowerIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUPowerIn.setStatus("current")


class _UxPSUPowerOut_Type(Integer32):
    """Custom type uxPSUPowerOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_UxPSUPowerOut_Type.__name__ = "Integer32"
_UxPSUPowerOut_Object = MibTableColumn
uxPSUPowerOut = _UxPSUPowerOut_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 6),
    _UxPSUPowerOut_Type()
)
uxPSUPowerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUPowerOut.setStatus("current")


class _UxPSUVoltageIn_Type(Integer32):
    """Custom type uxPSUVoltageIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_UxPSUVoltageIn_Type.__name__ = "Integer32"
_UxPSUVoltageIn_Object = MibTableColumn
uxPSUVoltageIn = _UxPSUVoltageIn_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 7),
    _UxPSUVoltageIn_Type()
)
uxPSUVoltageIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUVoltageIn.setStatus("current")


class _UxPSUVoltageOut_Type(Integer32):
    """Custom type uxPSUVoltageOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_UxPSUVoltageOut_Type.__name__ = "Integer32"
_UxPSUVoltageOut_Object = MibTableColumn
uxPSUVoltageOut = _UxPSUVoltageOut_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 8),
    _UxPSUVoltageOut_Type()
)
uxPSUVoltageOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUVoltageOut.setStatus("current")


class _UxPSUCurrentIn_Type(Integer32):
    """Custom type uxPSUCurrentIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UxPSUCurrentIn_Type.__name__ = "Integer32"
_UxPSUCurrentIn_Object = MibTableColumn
uxPSUCurrentIn = _UxPSUCurrentIn_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 9),
    _UxPSUCurrentIn_Type()
)
uxPSUCurrentIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUCurrentIn.setStatus("current")


class _UxPSUCurrentOut_Type(Integer32):
    """Custom type uxPSUCurrentOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_UxPSUCurrentOut_Type.__name__ = "Integer32"
_UxPSUCurrentOut_Object = MibTableColumn
uxPSUCurrentOut = _UxPSUCurrentOut_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 10),
    _UxPSUCurrentOut_Type()
)
uxPSUCurrentOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUCurrentOut.setStatus("current")


class _UxPSUTemperature_Type(Integer32):
    """Custom type uxPSUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_UxPSUTemperature_Type.__name__ = "Integer32"
_UxPSUTemperature_Object = MibTableColumn
uxPSUTemperature = _UxPSUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 11),
    _UxPSUTemperature_Type()
)
uxPSUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUTemperature.setStatus("current")


class _UxPSUFanSpeed1_Type(Integer32):
    """Custom type uxPSUFanSpeed1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UxPSUFanSpeed1_Type.__name__ = "Integer32"
_UxPSUFanSpeed1_Object = MibTableColumn
uxPSUFanSpeed1 = _UxPSUFanSpeed1_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 12),
    _UxPSUFanSpeed1_Type()
)
uxPSUFanSpeed1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUFanSpeed1.setStatus("current")


class _UxPSUFanSpeed2_Type(Integer32):
    """Custom type uxPSUFanSpeed2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UxPSUFanSpeed2_Type.__name__ = "Integer32"
_UxPSUFanSpeed2_Object = MibTableColumn
uxPSUFanSpeed2 = _UxPSUFanSpeed2_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 9, 1, 13),
    _UxPSUFanSpeed2_Type()
)
uxPSUFanSpeed2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxPSUFanSpeed2.setStatus("current")
_UxFanTable_Object = MibTable
uxFanTable = _UxFanTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 10)
)
if mibBuilder.loadTexts:
    uxFanTable.setStatus("current")
_UxFanEntry_Object = MibTableRow
uxFanEntry = _UxFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 10, 1)
)
uxFanEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxFanIndex"),
)
if mibBuilder.loadTexts:
    uxFanEntry.setStatus("current")


class _UxFanIndex_Type(Integer32):
    """Custom type uxFanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_UxFanIndex_Type.__name__ = "Integer32"
_UxFanIndex_Object = MibTableColumn
uxFanIndex = _UxFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 10, 1, 1),
    _UxFanIndex_Type()
)
uxFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxFanIndex.setStatus("current")


class _UxFanSpeed_Type(Integer32):
    """Custom type uxFanSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UxFanSpeed_Type.__name__ = "Integer32"
_UxFanSpeed_Object = MibTableColumn
uxFanSpeed = _UxFanSpeed_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 10, 1, 2),
    _UxFanSpeed_Type()
)
uxFanSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxFanSpeed.setStatus("current")
_UxCardTable_Object = MibTable
uxCardTable = _UxCardTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 11)
)
if mibBuilder.loadTexts:
    uxCardTable.setStatus("current")
_UxCardEntry_Object = MibTableRow
uxCardEntry = _UxCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 11, 1)
)
uxCardEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxCardIndex"),
)
if mibBuilder.loadTexts:
    uxCardEntry.setStatus("current")


class _UxCardIndex_Type(Integer32):
    """Custom type uxCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxCardIndex_Type.__name__ = "Integer32"
_UxCardIndex_Object = MibTableColumn
uxCardIndex = _UxCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 11, 1, 1),
    _UxCardIndex_Type()
)
uxCardIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCardIndex.setStatus("current")


class _UxCardType_Type(Integer32):
    """Custom type uxCardType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
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
              27)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("dS1-2Spans", 1),
          ("dS1-4Spans", 2),
          ("dS1-8Spans", 3),
          ("eX", 4),
          ("fXS-8PortsLineCard", 17),
          ("fXS-16PortsLineCard", 18),
          ("fXS-24PortsLineCard", 19),
          ("fXS-4PortsLowerBoard", 20),
          ("fXS-4PortsUpperBoard", 21),
          ("fXO-4PortsLowerBoard", 22),
          ("fXO-4PortsUpperBoard", 23),
          ("bRI-4PortsBoard", 24),
          ("dS1-1SpanBoard", 25),
          ("dS1-2SpansBoard", 26),
          ("fXS-4PortsNRLowerBoard", 27))
    )


_UxCardType_Type.__name__ = "Integer32"
_UxCardType_Object = MibTableColumn
uxCardType = _UxCardType_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 11, 1, 2),
    _UxCardType_Type()
)
uxCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCardType.setStatus("current")


class _UxCardServiceStatus_Type(Integer32):
    """Custom type uxCardServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1),
          ("notapplicable", 2))
    )


_UxCardServiceStatus_Type.__name__ = "Integer32"
_UxCardServiceStatus_Object = MibTableColumn
uxCardServiceStatus = _UxCardServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 11, 1, 3),
    _UxCardServiceStatus_Type()
)
uxCardServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxCardServiceStatus.setStatus("current")
_UxSystem_ObjectIdentity = ObjectIdentity
uxSystem = _UxSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12)
)


class _UxSystemHighestSeverityAlarm_Type(Integer32):
    """Custom type uxSystemHighestSeverityAlarm based on Integer32"""
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
        *(("unknown", 0),
          ("normal", 1),
          ("warning", 2),
          ("minor", 3),
          ("major", 4),
          ("critical", 5))
    )


_UxSystemHighestSeverityAlarm_Type.__name__ = "Integer32"
_UxSystemHighestSeverityAlarm_Object = MibScalar
uxSystemHighestSeverityAlarm = _UxSystemHighestSeverityAlarm_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 1),
    _UxSystemHighestSeverityAlarm_Type()
)
uxSystemHighestSeverityAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSystemHighestSeverityAlarm.setStatus("current")


class _UxSystemCoreSwitchTemp_Type(Integer32):
    """Custom type uxSystemCoreSwitchTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UxSystemCoreSwitchTemp_Type.__name__ = "Integer32"
_UxSystemCoreSwitchTemp_Object = MibScalar
uxSystemCoreSwitchTemp = _UxSystemCoreSwitchTemp_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 2),
    _UxSystemCoreSwitchTemp_Type()
)
uxSystemCoreSwitchTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSystemCoreSwitchTemp.setStatus("current")
_UxSystemCurrentCPUUsage_Type = PerfCurrentCount
_UxSystemCurrentCPUUsage_Object = MibScalar
uxSystemCurrentCPUUsage = _UxSystemCurrentCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 3),
    _UxSystemCurrentCPUUsage_Type()
)
uxSystemCurrentCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSystemCurrentCPUUsage.setStatus("current")
_UxSystemCurrentMemoryUsage_Type = PerfCurrentCount
_UxSystemCurrentMemoryUsage_Object = MibScalar
uxSystemCurrentMemoryUsage = _UxSystemCurrentMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 4),
    _UxSystemCurrentMemoryUsage_Type()
)
uxSystemCurrentMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxSystemCurrentMemoryUsage.setStatus("current")
_UxLicenseCurrentPeakSIPCall_Type = PerfCurrentCount
_UxLicenseCurrentPeakSIPCall_Object = MibScalar
uxLicenseCurrentPeakSIPCall = _UxLicenseCurrentPeakSIPCall_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 5),
    _UxLicenseCurrentPeakSIPCall_Type()
)
uxLicenseCurrentPeakSIPCall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseCurrentPeakSIPCall.setStatus("current")
_UxLicenseCurrentPeakSIPRegistration_Type = PerfCurrentCount
_UxLicenseCurrentPeakSIPRegistration_Object = MibScalar
uxLicenseCurrentPeakSIPRegistration = _UxLicenseCurrentPeakSIPRegistration_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 6),
    _UxLicenseCurrentPeakSIPRegistration_Type()
)
uxLicenseCurrentPeakSIPRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseCurrentPeakSIPRegistration.setStatus("current")
_UxDSPPeakCurrentUsage_Type = PerfTotalCount
_UxDSPPeakCurrentUsage_Object = MibScalar
uxDSPPeakCurrentUsage = _UxDSPPeakCurrentUsage_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 7),
    _UxDSPPeakCurrentUsage_Type()
)
uxDSPPeakCurrentUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxDSPPeakCurrentUsage.setStatus("current")
_UxLicenseCurrentPeakTDMChannel_Type = PerfCurrentCount
_UxLicenseCurrentPeakTDMChannel_Object = MibScalar
uxLicenseCurrentPeakTDMChannel = _UxLicenseCurrentPeakTDMChannel_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 8),
    _UxLicenseCurrentPeakTDMChannel_Type()
)
uxLicenseCurrentPeakTDMChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseCurrentPeakTDMChannel.setStatus("current")
_UxLicenseCurrentPeakDSP_Type = PerfCurrentCount
_UxLicenseCurrentPeakDSP_Object = MibScalar
uxLicenseCurrentPeakDSP = _UxLicenseCurrentPeakDSP_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 9),
    _UxLicenseCurrentPeakDSP_Type()
)
uxLicenseCurrentPeakDSP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxLicenseCurrentPeakDSP.setStatus("current")
_UxUserStatsPeakSessionsCurrentInerval_Type = Integer32
_UxUserStatsPeakSessionsCurrentInerval_Object = MibScalar
uxUserStatsPeakSessionsCurrentInerval = _UxUserStatsPeakSessionsCurrentInerval_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 10),
    _UxUserStatsPeakSessionsCurrentInerval_Type()
)
uxUserStatsPeakSessionsCurrentInerval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxUserStatsPeakSessionsCurrentInerval.setStatus("current")
_UxUserStatsIntervalTable_Object = MibTable
uxUserStatsIntervalTable = _UxUserStatsIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 11)
)
if mibBuilder.loadTexts:
    uxUserStatsIntervalTable.setStatus("current")
_UxUserStatsIntervalEntry_Object = MibTableRow
uxUserStatsIntervalEntry = _UxUserStatsIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 11, 1)
)
uxUserStatsIntervalEntry.setIndexNames(
    (0, "UX-OBJECTS-MIB", "uxUserStatsIntervalNumber"),
)
if mibBuilder.loadTexts:
    uxUserStatsIntervalEntry.setStatus("current")


class _UxUserStatsIntervalNumber_Type(Integer32):
    """Custom type uxUserStatsIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_UxUserStatsIntervalNumber_Type.__name__ = "Integer32"
_UxUserStatsIntervalNumber_Object = MibTableColumn
uxUserStatsIntervalNumber = _UxUserStatsIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 11, 1, 1),
    _UxUserStatsIntervalNumber_Type()
)
uxUserStatsIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxUserStatsIntervalNumber.setStatus("current")
_UxUserStatsPeakSessions_Type = Integer32
_UxUserStatsPeakSessions_Object = MibTableColumn
uxUserStatsPeakSessions = _UxUserStatsPeakSessions_Object(
    (1, 3, 6, 1, 4, 1, 177, 15, 1, 12, 11, 1, 2),
    _UxUserStatsPeakSessions_Type()
)
uxUserStatsPeakSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uxUserStatsPeakSessions.setStatus("current")
_UxTraps_ObjectIdentity = ObjectIdentity
uxTraps = _UxTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 177, 15, 2)
)
dsx0ConfigEntry.registerAugmentions(
    ("UX-OBJECTS-MIB",
     "uxDSX0ConfigEntry")
)
uxDSX0ConfigEntry.setIndexNames(*dsx0ConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "UX-OBJECTS-MIB",
    **{"net": net,
       "ux": ux,
       "uxObjects": uxObjects,
       "uxChassis": uxChassis,
       "chasiDescUX2000": chasiDescUX2000,
       "chasiDescUX1000": chasiDescUX1000,
       "chasiType": chasiType,
       "uxAlarmCfgTable": uxAlarmCfgTable,
       "uxAlarmCfgEntry": uxAlarmCfgEntry,
       "uxAlarmIndex": uxAlarmIndex,
       "uxAlarmID": uxAlarmID,
       "uxAlarmSubID": uxAlarmSubID,
       "uxAlarmCondition": uxAlarmCondition,
       "uxAlarmSeverity": uxAlarmSeverity,
       "uxAlarmCategory": uxAlarmCategory,
       "uxAlarmCancelType": uxAlarmCancelType,
       "uxAlarmEvtType": uxAlarmEvtType,
       "uxAlarmDecodeKey": uxAlarmDecodeKey,
       "uxAlarmClrID": uxAlarmClrID,
       "uxAlarmClrSubID": uxAlarmClrSubID,
       "uxAlarmDescription": uxAlarmDescription,
       "uxActAlarmTable": uxActAlarmTable,
       "uxActAlarmEntry": uxActAlarmEntry,
       "uxAlarmActiveIndex": uxAlarmActiveIndex,
       "uxAlarmConfigIndex": uxAlarmConfigIndex,
       "uxAlarmActiveID": uxAlarmActiveID,
       "uxAlarmActiveSubID": uxAlarmActiveSubID,
       "uxAlarmActiveCondition": uxAlarmActiveCondition,
       "uxAlarmActiveSeverity": uxAlarmActiveSeverity,
       "uxAlarmActiveCategory": uxAlarmActiveCategory,
       "uxAlarmActiveCancelType": uxAlarmActiveCancelType,
       "uxAlarmActiveFirstOccur": uxAlarmActiveFirstOccur,
       "uxAlarmActiveLastOccur": uxAlarmActiveLastOccur,
       "uxAlarmActiveCount": uxAlarmActiveCount,
       "uxAlarmActiveDecodeKey": uxAlarmActiveDecodeKey,
       "uxAlarmActiveSourceInstance": uxAlarmActiveSourceInstance,
       "uxAlarmActiveState": uxAlarmActiveState,
       "uxAlarmActiveClrEvtID": uxAlarmActiveClrEvtID,
       "uxAlarmActiveClrEvtSubID": uxAlarmActiveClrEvtSubID,
       "uxAlarmActiveDescription": uxAlarmActiveDescription,
       "uxAlarmActiveHighestSeverityAlarm": uxAlarmActiveHighestSeverityAlarm,
       "uxAlarmActiveHardWareID": uxAlarmActiveHardWareID,
       "ipTelephony": ipTelephony,
       "uxSystemUsageStatsIntervalTable": uxSystemUsageStatsIntervalTable,
       "uxSystemUsageIntervalEntry": uxSystemUsageIntervalEntry,
       "uxSystemUsageIntervalNumber": uxSystemUsageIntervalNumber,
       "uxSystemUsageIntervalCPUUsage": uxSystemUsageIntervalCPUUsage,
       "uxSystemUsageIntervalMemoryUsage": uxSystemUsageIntervalMemoryUsage,
       "uxDSPPeakUsageStatsIntervalTable": uxDSPPeakUsageStatsIntervalTable,
       "uxDSPPeakUsageIntervalEntry": uxDSPPeakUsageIntervalEntry,
       "uxDSPPeakUsageIntervalIndex": uxDSPPeakUsageIntervalIndex,
       "uxDSPPeakIntervalUsage": uxDSPPeakIntervalUsage,
       "uxDSPResourceTable": uxDSPResourceTable,
       "uxDSPResourceEntry": uxDSPResourceEntry,
       "uxDSPIndex": uxDSPIndex,
       "uxDSPModType": uxDSPModType,
       "uxDSPIsPresent": uxDSPIsPresent,
       "uxDSPCPUUsage": uxDSPCPUUsage,
       "uxDSPChannelsInUse": uxDSPChannelsInUse,
       "uxDSPServiceStatus": uxDSPServiceStatus,
       "uxCodecsSupported": uxCodecsSupported,
       "uxDSX0ConfigTable": uxDSX0ConfigTable,
       "uxDSX0ConfigEntry": uxDSX0ConfigEntry,
       "uxDSX0Type": uxDSX0Type,
       "uxDSX0Speed": uxDSX0Speed,
       "uxDSX0Lastchange": uxDSX0Lastchange,
       "uxDSX0AdminState": uxDSX0AdminState,
       "uxModuleTable": uxModuleTable,
       "uxModuleEntry": uxModuleEntry,
       "uxModuleIndex": uxModuleIndex,
       "uxModuleType": uxModuleType,
       "uxModulePartNumber": uxModulePartNumber,
       "uxModuleVersionNumber": uxModuleVersionNumber,
       "uxModuleSerialNumber": uxModuleSerialNumber,
       "uxModuleMfgWeek": uxModuleMfgWeek,
       "uxModuleMfgYear": uxModuleMfgYear,
       "uxPSUTable": uxPSUTable,
       "uxPSUEntry": uxPSUEntry,
       "uxPSUIndex": uxPSUIndex,
       "uxPSUIsPresent": uxPSUIsPresent,
       "uxPSUIsInputGood": uxPSUIsInputGood,
       "uxPSUInputType": uxPSUInputType,
       "uxPSUPowerIn": uxPSUPowerIn,
       "uxPSUPowerOut": uxPSUPowerOut,
       "uxPSUVoltageIn": uxPSUVoltageIn,
       "uxPSUVoltageOut": uxPSUVoltageOut,
       "uxPSUCurrentIn": uxPSUCurrentIn,
       "uxPSUCurrentOut": uxPSUCurrentOut,
       "uxPSUTemperature": uxPSUTemperature,
       "uxPSUFanSpeed1": uxPSUFanSpeed1,
       "uxPSUFanSpeed2": uxPSUFanSpeed2,
       "uxFanTable": uxFanTable,
       "uxFanEntry": uxFanEntry,
       "uxFanIndex": uxFanIndex,
       "uxFanSpeed": uxFanSpeed,
       "uxCardTable": uxCardTable,
       "uxCardEntry": uxCardEntry,
       "uxCardIndex": uxCardIndex,
       "uxCardType": uxCardType,
       "uxCardServiceStatus": uxCardServiceStatus,
       "uxSystem": uxSystem,
       "uxSystemHighestSeverityAlarm": uxSystemHighestSeverityAlarm,
       "uxSystemCoreSwitchTemp": uxSystemCoreSwitchTemp,
       "uxSystemCurrentCPUUsage": uxSystemCurrentCPUUsage,
       "uxSystemCurrentMemoryUsage": uxSystemCurrentMemoryUsage,
       "uxLicenseCurrentPeakSIPCall": uxLicenseCurrentPeakSIPCall,
       "uxLicenseCurrentPeakSIPRegistration": uxLicenseCurrentPeakSIPRegistration,
       "uxDSPPeakCurrentUsage": uxDSPPeakCurrentUsage,
       "uxLicenseCurrentPeakTDMChannel": uxLicenseCurrentPeakTDMChannel,
       "uxLicenseCurrentPeakDSP": uxLicenseCurrentPeakDSP,
       "uxUserStatsPeakSessionsCurrentInerval": uxUserStatsPeakSessionsCurrentInerval,
       "uxUserStatsIntervalTable": uxUserStatsIntervalTable,
       "uxUserStatsIntervalEntry": uxUserStatsIntervalEntry,
       "uxUserStatsIntervalNumber": uxUserStatsIntervalNumber,
       "uxUserStatsPeakSessions": uxUserStatsPeakSessions,
       "uxTraps": uxTraps}
)
