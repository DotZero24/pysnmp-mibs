# SNMP MIB module (DPS-MIB-V38-V2) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/dps/DPS-MIB-V38-V2
# Produced by pysmi-1.6.2 at Fri Oct 10 21:10:58 2025
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

(dpsAlarmControl,
 tmonXM) = mibBuilder.importSymbols(
    "DPS-MIB-V38",
    "dpsAlarmControl",
    "tmonXM")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

tmonV2XM = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3)
)
if mibBuilder.loadTexts:
    tmonV2XM.setRevisions(
        ("2012-08-08 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TmonV2Ident_ObjectIdentity = ObjectIdentity
tmonV2Ident = _TmonV2Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 1)
)
_TmonV2IdentManufacturer_Type = DisplayString
_TmonV2IdentManufacturer_Object = MibScalar
tmonV2IdentManufacturer = _TmonV2IdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 1),
    _TmonV2IdentManufacturer_Type()
)
tmonV2IdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2IdentManufacturer.setStatus("current")
_TmonV2IdentModel_Type = DisplayString
_TmonV2IdentModel_Object = MibScalar
tmonV2IdentModel = _TmonV2IdentModel_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 2),
    _TmonV2IdentModel_Type()
)
tmonV2IdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2IdentModel.setStatus("current")
_TmonV2IdentSoftwareVersion_Type = DisplayString
_TmonV2IdentSoftwareVersion_Object = MibScalar
tmonV2IdentSoftwareVersion = _TmonV2IdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 1, 3),
    _TmonV2IdentSoftwareVersion_Type()
)
tmonV2IdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2IdentSoftwareVersion.setStatus("current")
_TmonV2AlarmTable_Object = MibTable
tmonV2AlarmTable = _TmonV2AlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tmonV2AlarmTable.setStatus("current")
_TmonV2AlarmEntry_Object = MibTableRow
tmonV2AlarmEntry = _TmonV2AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1)
)
tmonV2AlarmEntry.setIndexNames(
    (0, "DPS-MIB-V38-V2", "tmonV2AIndex"),
)
if mibBuilder.loadTexts:
    tmonV2AlarmEntry.setStatus("current")


class _TmonV2AIndex_Type(Integer32):
    """Custom type tmonV2AIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2AIndex_Type.__name__ = "Integer32"
_TmonV2AIndex_Object = MibTableColumn
tmonV2AIndex = _TmonV2AIndex_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 1),
    _TmonV2AIndex_Type()
)
tmonV2AIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tmonV2AIndex.setStatus("current")
_TmonV2ASite_Type = DisplayString
_TmonV2ASite_Object = MibTableColumn
tmonV2ASite = _TmonV2ASite_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 2),
    _TmonV2ASite_Type()
)
tmonV2ASite.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2ASite.setStatus("current")
_TmonV2ADesc_Type = DisplayString
_TmonV2ADesc_Object = MibTableColumn
tmonV2ADesc = _TmonV2ADesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 3),
    _TmonV2ADesc_Type()
)
tmonV2ADesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2ADesc.setStatus("current")
_TmonV2AState_Type = DisplayString
_TmonV2AState_Object = MibTableColumn
tmonV2AState = _TmonV2AState_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 4),
    _TmonV2AState_Type()
)
tmonV2AState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2AState.setStatus("current")
_TmonV2ASeverity_Type = DisplayString
_TmonV2ASeverity_Object = MibTableColumn
tmonV2ASeverity = _TmonV2ASeverity_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 5),
    _TmonV2ASeverity_Type()
)
tmonV2ASeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2ASeverity.setStatus("current")
_TmonV2AChgDate_Type = DisplayString
_TmonV2AChgDate_Object = MibTableColumn
tmonV2AChgDate = _TmonV2AChgDate_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 6),
    _TmonV2AChgDate_Type()
)
tmonV2AChgDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2AChgDate.setStatus("current")
_TmonV2AChgTime_Type = DisplayString
_TmonV2AChgTime_Object = MibTableColumn
tmonV2AChgTime = _TmonV2AChgTime_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 7),
    _TmonV2AChgTime_Type()
)
tmonV2AChgTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2AChgTime.setStatus("current")
_TmonV2AAuxDesc_Type = DisplayString
_TmonV2AAuxDesc_Object = MibTableColumn
tmonV2AAuxDesc = _TmonV2AAuxDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 8),
    _TmonV2AAuxDesc_Type()
)
tmonV2AAuxDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2AAuxDesc.setStatus("current")
_TmonV2ADispDesc_Type = DisplayString
_TmonV2ADispDesc_Object = MibTableColumn
tmonV2ADispDesc = _TmonV2ADispDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 9),
    _TmonV2ADispDesc_Type()
)
tmonV2ADispDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2ADispDesc.setStatus("current")


class _TmonV2APntType_Type(Integer32):
    """Custom type tmonV2APntType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_TmonV2APntType_Type.__name__ = "Integer32"
_TmonV2APntType_Object = MibTableColumn
tmonV2APntType = _TmonV2APntType_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 10),
    _TmonV2APntType_Type()
)
tmonV2APntType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2APntType.setStatus("current")


class _TmonV2APort_Type(Integer32):
    """Custom type tmonV2APort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2APort_Type.__name__ = "Integer32"
_TmonV2APort_Object = MibTableColumn
tmonV2APort = _TmonV2APort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 11),
    _TmonV2APort_Type()
)
tmonV2APort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2APort.setStatus("current")


class _TmonV2AAddress_Type(Integer32):
    """Custom type tmonV2AAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_TmonV2AAddress_Type.__name__ = "Integer32"
_TmonV2AAddress_Object = MibTableColumn
tmonV2AAddress = _TmonV2AAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 12),
    _TmonV2AAddress_Type()
)
tmonV2AAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2AAddress.setStatus("current")


class _TmonV2ADisplay_Type(Integer32):
    """Custom type tmonV2ADisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2ADisplay_Type.__name__ = "Integer32"
_TmonV2ADisplay_Object = MibTableColumn
tmonV2ADisplay = _TmonV2ADisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 13),
    _TmonV2ADisplay_Type()
)
tmonV2ADisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2ADisplay.setStatus("current")


class _TmonV2APoint_Type(Integer32):
    """Custom type tmonV2APoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TmonV2APoint_Type.__name__ = "Integer32"
_TmonV2APoint_Object = MibTableColumn
tmonV2APoint = _TmonV2APoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 14),
    _TmonV2APoint_Type()
)
tmonV2APoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2APoint.setStatus("current")


class _TmonV2AEvent_Type(Integer32):
    """Custom type tmonV2AEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2AEvent_Type.__name__ = "Integer32"
_TmonV2AEvent_Object = MibTableColumn
tmonV2AEvent = _TmonV2AEvent_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 15),
    _TmonV2AEvent_Type()
)
tmonV2AEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2AEvent.setStatus("current")
_TmonV2AIPAddr_Type = DisplayString
_TmonV2AIPAddr_Object = MibTableColumn
tmonV2AIPAddr = _TmonV2AIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 16),
    _TmonV2AIPAddr_Type()
)
tmonV2AIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2AIPAddr.setStatus("current")
_TmonV2ADevDesc_Type = DisplayString
_TmonV2ADevDesc_Object = MibTableColumn
tmonV2ADevDesc = _TmonV2ADevDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 2, 1, 17),
    _TmonV2ADevDesc_Type()
)
tmonV2ADevDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2ADevDesc.setStatus("current")
_TmonV2CommandGrid_ObjectIdentity = ObjectIdentity
tmonV2CommandGrid = _TmonV2CommandGrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3)
)


class _TmonV2CPType_Type(Integer32):
    """Custom type tmonV2CPType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2CPType_Type.__name__ = "Integer32"
_TmonV2CPType_Object = MibScalar
tmonV2CPType = _TmonV2CPType_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 1),
    _TmonV2CPType_Type()
)
tmonV2CPType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CPType.setStatus("current")


class _TmonV2CPort_Type(Integer32):
    """Custom type tmonV2CPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2CPort_Type.__name__ = "Integer32"
_TmonV2CPort_Object = MibScalar
tmonV2CPort = _TmonV2CPort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 2),
    _TmonV2CPort_Type()
)
tmonV2CPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CPort.setStatus("current")


class _TmonV2CAddress_Type(Integer32):
    """Custom type tmonV2CAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_TmonV2CAddress_Type.__name__ = "Integer32"
_TmonV2CAddress_Object = MibScalar
tmonV2CAddress = _TmonV2CAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 3),
    _TmonV2CAddress_Type()
)
tmonV2CAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CAddress.setStatus("current")


class _TmonV2CDisplay_Type(Integer32):
    """Custom type tmonV2CDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2CDisplay_Type.__name__ = "Integer32"
_TmonV2CDisplay_Object = MibScalar
tmonV2CDisplay = _TmonV2CDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 4),
    _TmonV2CDisplay_Type()
)
tmonV2CDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CDisplay.setStatus("current")


class _TmonV2CPoint_Type(Integer32):
    """Custom type tmonV2CPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_TmonV2CPoint_Type.__name__ = "Integer32"
_TmonV2CPoint_Object = MibScalar
tmonV2CPoint = _TmonV2CPoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 5),
    _TmonV2CPoint_Type()
)
tmonV2CPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CPoint.setStatus("current")


class _TmonV2CEvent_Type(Integer32):
    """Custom type tmonV2CEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TmonV2CEvent_Type.__name__ = "Integer32"
_TmonV2CEvent_Object = MibScalar
tmonV2CEvent = _TmonV2CEvent_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 6),
    _TmonV2CEvent_Type()
)
tmonV2CEvent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CEvent.setStatus("current")


class _TmonV2CAction_Type(Integer32):
    """Custom type tmonV2CAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("latch", 1),
          ("release", 2),
          ("momentary", 3),
          ("ack", 17),
          ("tag", 18),
          ("untag", 19))
    )


_TmonV2CAction_Type.__name__ = "Integer32"
_TmonV2CAction_Object = MibScalar
tmonV2CAction = _TmonV2CAction_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 7),
    _TmonV2CAction_Type()
)
tmonV2CAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CAction.setStatus("current")
_TmonV2CAuxText_Type = DisplayString
_TmonV2CAuxText_Object = MibScalar
tmonV2CAuxText = _TmonV2CAuxText_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 8),
    _TmonV2CAuxText_Type()
)
tmonV2CAuxText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tmonV2CAuxText.setStatus("current")


class _TmonV2CResult_Type(Integer32):
    """Custom type tmonV2CResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("success", 1),
          ("failure", 2),
          ("pending", 3))
    )


_TmonV2CResult_Type.__name__ = "Integer32"
_TmonV2CResult_Object = MibScalar
tmonV2CResult = _TmonV2CResult_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 3, 3, 9),
    _TmonV2CResult_Type()
)
tmonV2CResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tmonV2CResult.setStatus("current")
_DpsRTUv2_ObjectIdentity = ObjectIdentity
dpsRTUv2 = _DpsRTUv2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4)
)
_DpsRTUv2Ident_ObjectIdentity = ObjectIdentity
dpsRTUv2Ident = _DpsRTUv2Ident_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 1)
)
_DpsRTUv2Manufacturer_Type = DisplayString
_DpsRTUv2Manufacturer_Object = MibScalar
dpsRTUv2Manufacturer = _DpsRTUv2Manufacturer_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 1),
    _DpsRTUv2Manufacturer_Type()
)
dpsRTUv2Manufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2Manufacturer.setStatus("current")
_DpsRTUv2Model_Type = DisplayString
_DpsRTUv2Model_Object = MibScalar
dpsRTUv2Model = _DpsRTUv2Model_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 2),
    _DpsRTUv2Model_Type()
)
dpsRTUv2Model.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2Model.setStatus("current")
_DpsRTUv2FirmwareVersion_Type = DisplayString
_DpsRTUv2FirmwareVersion_Object = MibScalar
dpsRTUv2FirmwareVersion = _DpsRTUv2FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 3),
    _DpsRTUv2FirmwareVersion_Type()
)
dpsRTUv2FirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2FirmwareVersion.setStatus("current")
_DpsRTUv2DateTime_Type = DisplayString
_DpsRTUv2DateTime_Object = MibScalar
dpsRTUv2DateTime = _DpsRTUv2DateTime_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 4),
    _DpsRTUv2DateTime_Type()
)
dpsRTUv2DateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUv2DateTime.setStatus("current")


class _DpsRTUv2SyncReq_Type(Integer32):
    """Custom type dpsRTUv2SyncReq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("sync", 1)
    )


_DpsRTUv2SyncReq_Type.__name__ = "Integer32"
_DpsRTUv2SyncReq_Object = MibScalar
dpsRTUv2SyncReq = _DpsRTUv2SyncReq_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 1, 5),
    _DpsRTUv2SyncReq_Type()
)
dpsRTUv2SyncReq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUv2SyncReq.setStatus("current")
_DpsRTUv2DisplayGrid_Object = MibTable
dpsRTUv2DisplayGrid = _DpsRTUv2DisplayGrid_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dpsRTUv2DisplayGrid.setStatus("current")
_DpsRTUv2DisplayEntry_Object = MibTableRow
dpsRTUv2DisplayEntry = _DpsRTUv2DisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1)
)
dpsRTUv2DisplayEntry.setIndexNames(
    (0, "DPS-MIB-V38-V2", "dpsRTUv2Port"),
    (0, "DPS-MIB-V38-V2", "dpsRTUv2Address"),
    (0, "DPS-MIB-V38-V2", "dpsRTUv2Display"),
)
if mibBuilder.loadTexts:
    dpsRTUv2DisplayEntry.setStatus("current")


class _DpsRTUv2Port_Type(Integer32):
    """Custom type dpsRTUv2Port based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DpsRTUv2Port_Type.__name__ = "Integer32"
_DpsRTUv2Port_Object = MibTableColumn
dpsRTUv2Port = _DpsRTUv2Port_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 1),
    _DpsRTUv2Port_Type()
)
dpsRTUv2Port.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2Port.setStatus("current")


class _DpsRTUv2Address_Type(Integer32):
    """Custom type dpsRTUv2Address based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DpsRTUv2Address_Type.__name__ = "Integer32"
_DpsRTUv2Address_Object = MibTableColumn
dpsRTUv2Address = _DpsRTUv2Address_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 2),
    _DpsRTUv2Address_Type()
)
dpsRTUv2Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2Address.setStatus("current")


class _DpsRTUv2Display_Type(Integer32):
    """Custom type dpsRTUv2Display based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DpsRTUv2Display_Type.__name__ = "Integer32"
_DpsRTUv2Display_Object = MibTableColumn
dpsRTUv2Display = _DpsRTUv2Display_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 3),
    _DpsRTUv2Display_Type()
)
dpsRTUv2Display.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2Display.setStatus("current")
_DpsRTUv2DispDesc_Type = DisplayString
_DpsRTUv2DispDesc_Object = MibTableColumn
dpsRTUv2DispDesc = _DpsRTUv2DispDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 4),
    _DpsRTUv2DispDesc_Type()
)
dpsRTUv2DispDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2DispDesc.setStatus("current")
_DpsRTUv2PntMap_Type = DisplayString
_DpsRTUv2PntMap_Object = MibTableColumn
dpsRTUv2PntMap = _DpsRTUv2PntMap_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 2, 1, 5),
    _DpsRTUv2PntMap_Type()
)
dpsRTUv2PntMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2PntMap.setStatus("current")
_DpsRTUv2ControlGrid_ObjectIdentity = ObjectIdentity
dpsRTUv2ControlGrid = _DpsRTUv2ControlGrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 3)
)


class _DpsRTUv2CPort_Type(Integer32):
    """Custom type dpsRTUv2CPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DpsRTUv2CPort_Type.__name__ = "Integer32"
_DpsRTUv2CPort_Object = MibScalar
dpsRTUv2CPort = _DpsRTUv2CPort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 1),
    _DpsRTUv2CPort_Type()
)
dpsRTUv2CPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUv2CPort.setStatus("current")


class _DpsRTUv2CAddress_Type(Integer32):
    """Custom type dpsRTUv2CAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DpsRTUv2CAddress_Type.__name__ = "Integer32"
_DpsRTUv2CAddress_Object = MibScalar
dpsRTUv2CAddress = _DpsRTUv2CAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 2),
    _DpsRTUv2CAddress_Type()
)
dpsRTUv2CAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUv2CAddress.setStatus("current")


class _DpsRTUv2CDisplay_Type(Integer32):
    """Custom type dpsRTUv2CDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DpsRTUv2CDisplay_Type.__name__ = "Integer32"
_DpsRTUv2CDisplay_Object = MibScalar
dpsRTUv2CDisplay = _DpsRTUv2CDisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 3),
    _DpsRTUv2CDisplay_Type()
)
dpsRTUv2CDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUv2CDisplay.setStatus("current")


class _DpsRTUv2CPoint_Type(Integer32):
    """Custom type dpsRTUv2CPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DpsRTUv2CPoint_Type.__name__ = "Integer32"
_DpsRTUv2CPoint_Object = MibScalar
dpsRTUv2CPoint = _DpsRTUv2CPoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 4),
    _DpsRTUv2CPoint_Type()
)
dpsRTUv2CPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUv2CPoint.setStatus("current")


class _DpsRTUv2CAction_Type(Integer32):
    """Custom type dpsRTUv2CAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("latch", 1),
          ("release", 2),
          ("momentary", 3))
    )


_DpsRTUv2CAction_Type.__name__ = "Integer32"
_DpsRTUv2CAction_Object = MibScalar
dpsRTUv2CAction = _DpsRTUv2CAction_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 3, 5),
    _DpsRTUv2CAction_Type()
)
dpsRTUv2CAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsRTUv2CAction.setStatus("current")
_DpsRTUv2AlarmGrid_Object = MibTable
dpsRTUv2AlarmGrid = _DpsRTUv2AlarmGrid_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5)
)
if mibBuilder.loadTexts:
    dpsRTUv2AlarmGrid.setStatus("current")
_DpsRTUv2AlarmEntry_Object = MibTableRow
dpsRTUv2AlarmEntry = _DpsRTUv2AlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1)
)
dpsRTUv2AlarmEntry.setIndexNames(
    (0, "DPS-MIB-V38-V2", "dpsRTUv2APort"),
    (0, "DPS-MIB-V38-V2", "dpsRTUv2AAddress"),
    (0, "DPS-MIB-V38-V2", "dpsRTUv2ADisplay"),
    (0, "DPS-MIB-V38-V2", "dpsRTUv2APoint"),
)
if mibBuilder.loadTexts:
    dpsRTUv2AlarmEntry.setStatus("current")


class _DpsRTUv2APort_Type(Integer32):
    """Custom type dpsRTUv2APort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DpsRTUv2APort_Type.__name__ = "Integer32"
_DpsRTUv2APort_Object = MibTableColumn
dpsRTUv2APort = _DpsRTUv2APort_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 1),
    _DpsRTUv2APort_Type()
)
dpsRTUv2APort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2APort.setStatus("current")


class _DpsRTUv2AAddress_Type(Integer32):
    """Custom type dpsRTUv2AAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_DpsRTUv2AAddress_Type.__name__ = "Integer32"
_DpsRTUv2AAddress_Object = MibTableColumn
dpsRTUv2AAddress = _DpsRTUv2AAddress_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 2),
    _DpsRTUv2AAddress_Type()
)
dpsRTUv2AAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2AAddress.setStatus("current")


class _DpsRTUv2ADisplay_Type(Integer32):
    """Custom type dpsRTUv2ADisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DpsRTUv2ADisplay_Type.__name__ = "Integer32"
_DpsRTUv2ADisplay_Object = MibTableColumn
dpsRTUv2ADisplay = _DpsRTUv2ADisplay_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 3),
    _DpsRTUv2ADisplay_Type()
)
dpsRTUv2ADisplay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2ADisplay.setStatus("current")


class _DpsRTUv2APoint_Type(Integer32):
    """Custom type dpsRTUv2APoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DpsRTUv2APoint_Type.__name__ = "Integer32"
_DpsRTUv2APoint_Object = MibTableColumn
dpsRTUv2APoint = _DpsRTUv2APoint_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 4),
    _DpsRTUv2APoint_Type()
)
dpsRTUv2APoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2APoint.setStatus("current")
_DpsRTUv2APntDesc_Type = DisplayString
_DpsRTUv2APntDesc_Object = MibTableColumn
dpsRTUv2APntDesc = _DpsRTUv2APntDesc_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 5),
    _DpsRTUv2APntDesc_Type()
)
dpsRTUv2APntDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2APntDesc.setStatus("current")
_DpsRTUv2AState_Type = DisplayString
_DpsRTUv2AState_Object = MibTableColumn
dpsRTUv2AState = _DpsRTUv2AState_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 5, 1, 6),
    _DpsRTUv2AState_Type()
)
dpsRTUv2AState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsRTUv2AState.setStatus("current")
_AnalogChannelsv2_Object = MibTable
analogChannelsv2 = _AnalogChannelsv2_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6)
)
if mibBuilder.loadTexts:
    analogChannelsv2.setStatus("current")
_ChannelEntryv2_Object = MibTableRow
channelEntryv2 = _ChannelEntryv2_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1)
)
channelEntryv2.setIndexNames(
    (0, "DPS-MIB-V38-V2", "channelNumberv2"),
)
if mibBuilder.loadTexts:
    channelEntryv2.setStatus("current")


class _ChannelNumberv2_Type(Integer32):
    """Custom type channelNumberv2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelNumberv2_Type.__name__ = "Integer32"
_ChannelNumberv2_Object = MibTableColumn
channelNumberv2 = _ChannelNumberv2_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 1),
    _ChannelNumberv2_Type()
)
channelNumberv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelNumberv2.setStatus("current")


class _Enabledv2_Type(Integer32):
    """Custom type enabledv2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_Enabledv2_Type.__name__ = "Integer32"
_Enabledv2_Object = MibTableColumn
enabledv2 = _Enabledv2_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 2),
    _Enabledv2_Type()
)
enabledv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    enabledv2.setStatus("current")
_Descriptionv2_Type = DisplayString
_Descriptionv2_Object = MibTableColumn
descriptionv2 = _Descriptionv2_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 3),
    _Descriptionv2_Type()
)
descriptionv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    descriptionv2.setStatus("current")
_Valuev2_Type = DisplayString
_Valuev2_Object = MibTableColumn
valuev2 = _Valuev2_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 4),
    _Valuev2_Type()
)
valuev2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    valuev2.setStatus("current")


class _Thresholdsv2_Type(Integer32):
    """Custom type thresholdsv2 based on Integer32"""
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
        *(("noAlarms", 0),
          ("minorUnder", 1),
          ("minorOver", 2),
          ("majorUnder", 3),
          ("majorOver", 4),
          ("notDetected", 5))
    )


_Thresholdsv2_Type.__name__ = "Integer32"
_Thresholdsv2_Object = MibTableColumn
thresholdsv2 = _Thresholdsv2_Object(
    (1, 3, 6, 1, 4, 1, 2682, 1, 4, 6, 1, 5),
    _Thresholdsv2_Type()
)
thresholdsv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thresholdsv2.setStatus("current")

# Managed Objects groups


# Notification objects

tmonV2CRalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 10)
)
tmonV2CRalarmSet.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2CRalarmSet.setStatus(
        "current"
    )

tmonV2CRalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 11)
)
tmonV2CRalarmClr.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2CRalarmClr.setStatus(
        "current"
    )

tmonV2MJalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 12)
)
tmonV2MJalarmSet.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2MJalarmSet.setStatus(
        "current"
    )

tmonV2MJalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 13)
)
tmonV2MJalarmClr.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2MJalarmClr.setStatus(
        "current"
    )

tmonV2MNalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 14)
)
tmonV2MNalarmSet.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2MNalarmSet.setStatus(
        "current"
    )

tmonV2MNalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 15)
)
tmonV2MNalarmClr.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2MNalarmClr.setStatus(
        "current"
    )

tmonV2STalarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 16)
)
tmonV2STalarmSet.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2STalarmSet.setStatus(
        "current"
    )

tmonV2STalarmClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 2682, 1, 1, 17)
)
tmonV2STalarmClr.setObjects(
      *(("DPS-MIB-V38-V2", "tmonV2ASite"),
        ("DPS-MIB-V38-V2", "tmonV2ADesc"),
        ("DPS-MIB-V38-V2", "tmonV2AState"),
        ("DPS-MIB-V38-V2", "tmonV2ASeverity"),
        ("DPS-MIB-V38-V2", "tmonV2AChgDate"),
        ("DPS-MIB-V38-V2", "tmonV2AChgTime"),
        ("DPS-MIB-V38-V2", "tmonV2AAuxDesc"),
        ("DPS-MIB-V38-V2", "tmonV2ADispDesc"),
        ("DPS-MIB-V38-V2", "tmonV2APntType"),
        ("DPS-MIB-V38-V2", "tmonV2APort"),
        ("DPS-MIB-V38-V2", "tmonV2AAddress"),
        ("DPS-MIB-V38-V2", "tmonV2ADisplay"),
        ("DPS-MIB-V38-V2", "tmonV2APoint"),
        ("DPS-MIB-V38-V2", "tmonV2CEvent"),
        ("DPS-MIB-V38-V2", "tmonV2AIPAddr"),
        ("DPS-MIB-V38-V2", "tmonV2ADevDesc"))
)
if mibBuilder.loadTexts:
    tmonV2STalarmClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DPS-MIB-V38-V2",
    **{"tmonV2CRalarmSet": tmonV2CRalarmSet,
       "tmonV2CRalarmClr": tmonV2CRalarmClr,
       "tmonV2MJalarmSet": tmonV2MJalarmSet,
       "tmonV2MJalarmClr": tmonV2MJalarmClr,
       "tmonV2MNalarmSet": tmonV2MNalarmSet,
       "tmonV2MNalarmClr": tmonV2MNalarmClr,
       "tmonV2STalarmSet": tmonV2STalarmSet,
       "tmonV2STalarmClr": tmonV2STalarmClr,
       "tmonV2XM": tmonV2XM,
       "tmonV2Ident": tmonV2Ident,
       "tmonV2IdentManufacturer": tmonV2IdentManufacturer,
       "tmonV2IdentModel": tmonV2IdentModel,
       "tmonV2IdentSoftwareVersion": tmonV2IdentSoftwareVersion,
       "tmonV2AlarmTable": tmonV2AlarmTable,
       "tmonV2AlarmEntry": tmonV2AlarmEntry,
       "tmonV2AIndex": tmonV2AIndex,
       "tmonV2ASite": tmonV2ASite,
       "tmonV2ADesc": tmonV2ADesc,
       "tmonV2AState": tmonV2AState,
       "tmonV2ASeverity": tmonV2ASeverity,
       "tmonV2AChgDate": tmonV2AChgDate,
       "tmonV2AChgTime": tmonV2AChgTime,
       "tmonV2AAuxDesc": tmonV2AAuxDesc,
       "tmonV2ADispDesc": tmonV2ADispDesc,
       "tmonV2APntType": tmonV2APntType,
       "tmonV2APort": tmonV2APort,
       "tmonV2AAddress": tmonV2AAddress,
       "tmonV2ADisplay": tmonV2ADisplay,
       "tmonV2APoint": tmonV2APoint,
       "tmonV2AEvent": tmonV2AEvent,
       "tmonV2AIPAddr": tmonV2AIPAddr,
       "tmonV2ADevDesc": tmonV2ADevDesc,
       "tmonV2CommandGrid": tmonV2CommandGrid,
       "tmonV2CPType": tmonV2CPType,
       "tmonV2CPort": tmonV2CPort,
       "tmonV2CAddress": tmonV2CAddress,
       "tmonV2CDisplay": tmonV2CDisplay,
       "tmonV2CPoint": tmonV2CPoint,
       "tmonV2CEvent": tmonV2CEvent,
       "tmonV2CAction": tmonV2CAction,
       "tmonV2CAuxText": tmonV2CAuxText,
       "tmonV2CResult": tmonV2CResult,
       "dpsRTUv2": dpsRTUv2,
       "dpsRTUv2Ident": dpsRTUv2Ident,
       "dpsRTUv2Manufacturer": dpsRTUv2Manufacturer,
       "dpsRTUv2Model": dpsRTUv2Model,
       "dpsRTUv2FirmwareVersion": dpsRTUv2FirmwareVersion,
       "dpsRTUv2DateTime": dpsRTUv2DateTime,
       "dpsRTUv2SyncReq": dpsRTUv2SyncReq,
       "dpsRTUv2DisplayGrid": dpsRTUv2DisplayGrid,
       "dpsRTUv2DisplayEntry": dpsRTUv2DisplayEntry,
       "dpsRTUv2Port": dpsRTUv2Port,
       "dpsRTUv2Address": dpsRTUv2Address,
       "dpsRTUv2Display": dpsRTUv2Display,
       "dpsRTUv2DispDesc": dpsRTUv2DispDesc,
       "dpsRTUv2PntMap": dpsRTUv2PntMap,
       "dpsRTUv2ControlGrid": dpsRTUv2ControlGrid,
       "dpsRTUv2CPort": dpsRTUv2CPort,
       "dpsRTUv2CAddress": dpsRTUv2CAddress,
       "dpsRTUv2CDisplay": dpsRTUv2CDisplay,
       "dpsRTUv2CPoint": dpsRTUv2CPoint,
       "dpsRTUv2CAction": dpsRTUv2CAction,
       "dpsRTUv2AlarmGrid": dpsRTUv2AlarmGrid,
       "dpsRTUv2AlarmEntry": dpsRTUv2AlarmEntry,
       "dpsRTUv2APort": dpsRTUv2APort,
       "dpsRTUv2AAddress": dpsRTUv2AAddress,
       "dpsRTUv2ADisplay": dpsRTUv2ADisplay,
       "dpsRTUv2APoint": dpsRTUv2APoint,
       "dpsRTUv2APntDesc": dpsRTUv2APntDesc,
       "dpsRTUv2AState": dpsRTUv2AState,
       "analogChannelsv2": analogChannelsv2,
       "channelEntryv2": channelEntryv2,
       "channelNumberv2": channelNumberv2,
       "enabledv2": enabledv2,
       "descriptionv2": descriptionv2,
       "valuev2": valuev2,
       "thresholdsv2": thresholdsv2}
)
