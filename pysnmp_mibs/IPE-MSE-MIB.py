# SNMP MIB module (IPE-MSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-MSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:45 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 Opaque,
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
    "Opaque",
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



class IpeEnableDisableValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disabled", 1),
          ("enabled", 2))
    )



class SeverityValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("indetermine", 2),
          ("critical", 3),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_AlarmStatusGroup_ObjectIdentity = ObjectIdentity
alarmStatusGroup = _AlarmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3)
)
_AsMseGroup_ObjectIdentity = ObjectIdentity
asMseGroup = _AsMseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40)
)
_AsMseCardTable_Object = MibTable
asMseCardTable = _AsMseCardTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1)
)
if mibBuilder.loadTexts:
    asMseCardTable.setStatus("current")
_AsMseCardEntry_Object = MibTableRow
asMseCardEntry = _AsMseCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1)
)
asMseCardEntry.setIndexNames(
    (0, "IPE-MSE-MIB", "asMseCardIndex"),
)
if mibBuilder.loadTexts:
    asMseCardEntry.setStatus("current")
_AsMseCardIndex_Type = Integer32
_AsMseCardIndex_Object = MibTableColumn
asMseCardIndex = _AsMseCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 1),
    _AsMseCardIndex_Type()
)
asMseCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMseCardIndex.setStatus("current")
_AsMseCardNEAddress_Type = IpAddress
_AsMseCardNEAddress_Object = MibTableColumn
asMseCardNEAddress = _AsMseCardNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 2),
    _AsMseCardNEAddress_Type()
)
asMseCardNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMseCardNEAddress.setStatus("current")
_AsMseCardModuleFail_Type = SeverityValue
_AsMseCardModuleFail_Object = MibTableColumn
asMseCardModuleFail = _AsMseCardModuleFail_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 3),
    _AsMseCardModuleFail_Type()
)
asMseCardModuleFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseCardModuleFail.setStatus("current")
_AsMseCardComFailAlarm_Type = SeverityValue
_AsMseCardComFailAlarm_Object = MibTableColumn
asMseCardComFailAlarm = _AsMseCardComFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 4),
    _AsMseCardComFailAlarm_Type()
)
asMseCardComFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseCardComFailAlarm.setStatus("current")
_AsMseCardUnequipped_Type = SeverityValue
_AsMseCardUnequipped_Object = MibTableColumn
asMseCardUnequipped = _AsMseCardUnequipped_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 5),
    _AsMseCardUnequipped_Type()
)
asMseCardUnequipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseCardUnequipped.setStatus("current")
_AsMseCardTypeMismatch_Type = SeverityValue
_AsMseCardTypeMismatch_Object = MibTableColumn
asMseCardTypeMismatch = _AsMseCardTypeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 6),
    _AsMseCardTypeMismatch_Type()
)
asMseCardTypeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseCardTypeMismatch.setStatus("current")
_AsMseCardBusErrorTx_Type = SeverityValue
_AsMseCardBusErrorTx_Object = MibTableColumn
asMseCardBusErrorTx = _AsMseCardBusErrorTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 7),
    _AsMseCardBusErrorTx_Type()
)
asMseCardBusErrorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseCardBusErrorTx.setStatus("current")
_AsMseCardBusErrorRx_Type = SeverityValue
_AsMseCardBusErrorRx_Object = MibTableColumn
asMseCardBusErrorRx = _AsMseCardBusErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 8),
    _AsMseCardBusErrorRx_Type()
)
asMseCardBusErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseCardBusErrorRx.setStatus("current")
_AsMseCardClkFail_Type = SeverityValue
_AsMseCardClkFail_Object = MibTableColumn
asMseCardClkFail = _AsMseCardClkFail_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 1, 1, 9),
    _AsMseCardClkFail_Type()
)
asMseCardClkFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseCardClkFail.setStatus("obsolete")
_AsMseLineTable_Object = MibTable
asMseLineTable = _AsMseLineTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 2)
)
if mibBuilder.loadTexts:
    asMseLineTable.setStatus("current")
_AsMseLineEntry_Object = MibTableRow
asMseLineEntry = _AsMseLineEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 2, 1)
)
asMseLineEntry.setIndexNames(
    (0, "IPE-MSE-MIB", "asMseLineIfIndex"),
)
if mibBuilder.loadTexts:
    asMseLineEntry.setStatus("current")
_AsMseLineIfIndex_Type = InterfaceIndex
_AsMseLineIfIndex_Object = MibTableColumn
asMseLineIfIndex = _AsMseLineIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 2, 1, 1),
    _AsMseLineIfIndex_Type()
)
asMseLineIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMseLineIfIndex.setStatus("current")
_AsMseLineNEAddress_Type = IpAddress
_AsMseLineNEAddress_Object = MibTableColumn
asMseLineNEAddress = _AsMseLineNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 2, 1, 2),
    _AsMseLineNEAddress_Type()
)
asMseLineNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMseLineNEAddress.setStatus("current")
_AsMseLineBfrUnderrun_Type = SeverityValue
_AsMseLineBfrUnderrun_Object = MibTableColumn
asMseLineBfrUnderrun = _AsMseLineBfrUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 2, 1, 5),
    _AsMseLineBfrUnderrun_Type()
)
asMseLineBfrUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseLineBfrUnderrun.setStatus("current")


class _AsMseLineAdaptiveClkStatus_Type(Integer32):
    """Custom type asMseLineAdaptiveClkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("holdover", 1),
          ("acquiring", 2),
          ("acquired", 3))
    )


_AsMseLineAdaptiveClkStatus_Type.__name__ = "Integer32"
_AsMseLineAdaptiveClkStatus_Object = MibTableColumn
asMseLineAdaptiveClkStatus = _AsMseLineAdaptiveClkStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 40, 2, 1, 6),
    _AsMseLineAdaptiveClkStatus_Type()
)
asMseLineAdaptiveClkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asMseLineAdaptiveClkStatus.setStatus("current")
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5)
)
_ProvMseGroup_ObjectIdentity = ObjectIdentity
provMseGroup = _ProvMseGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40)
)
_ProvMseLineModeTable_Object = MibTable
provMseLineModeTable = _ProvMseLineModeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 1)
)
if mibBuilder.loadTexts:
    provMseLineModeTable.setStatus("current")
_ProvMseLineModeEntry_Object = MibTableRow
provMseLineModeEntry = _ProvMseLineModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 1, 1)
)
provMseLineModeEntry.setIndexNames(
    (0, "IPE-MSE-MIB", "provMseLineModeIfIndex"),
)
if mibBuilder.loadTexts:
    provMseLineModeEntry.setStatus("current")
_ProvMseLineModeIfIndex_Type = InterfaceIndex
_ProvMseLineModeIfIndex_Object = MibTableColumn
provMseLineModeIfIndex = _ProvMseLineModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 1, 1, 1),
    _ProvMseLineModeIfIndex_Type()
)
provMseLineModeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseLineModeIfIndex.setStatus("current")
_ProvMseLineModeNEAddress_Type = IpAddress
_ProvMseLineModeNEAddress_Object = MibTableColumn
provMseLineModeNEAddress = _ProvMseLineModeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 1, 1, 2),
    _ProvMseLineModeNEAddress_Type()
)
provMseLineModeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseLineModeNEAddress.setStatus("current")


class _ProvMseLineModeType_Type(Integer32):
    """Custom type provMseLineModeType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("satop", 2))
    )


_ProvMseLineModeType_Type.__name__ = "Integer32"
_ProvMseLineModeType_Object = MibTableColumn
provMseLineModeType = _ProvMseLineModeType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 1, 1, 3),
    _ProvMseLineModeType_Type()
)
provMseLineModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMseLineModeType.setStatus("current")
_ProvMseClockModeTable_Object = MibTable
provMseClockModeTable = _ProvMseClockModeTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 2)
)
if mibBuilder.loadTexts:
    provMseClockModeTable.setStatus("current")
_ProvMseClockModeEntry_Object = MibTableRow
provMseClockModeEntry = _ProvMseClockModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 2, 1)
)
provMseClockModeEntry.setIndexNames(
    (0, "IPE-MSE-MIB", "provMseClockModeIfIndex"),
)
if mibBuilder.loadTexts:
    provMseClockModeEntry.setStatus("current")
_ProvMseClockModeIfIndex_Type = InterfaceIndex
_ProvMseClockModeIfIndex_Object = MibTableColumn
provMseClockModeIfIndex = _ProvMseClockModeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 2, 1, 1),
    _ProvMseClockModeIfIndex_Type()
)
provMseClockModeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseClockModeIfIndex.setStatus("current")
_ProvMseClockModeNEAddress_Type = IpAddress
_ProvMseClockModeNEAddress_Object = MibTableColumn
provMseClockModeNEAddress = _ProvMseClockModeNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 2, 1, 2),
    _ProvMseClockModeNEAddress_Type()
)
provMseClockModeNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseClockModeNEAddress.setStatus("current")


class _ProvMseClockModeType_Type(Integer32):
    """Custom type provMseClockModeType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("syncToSystem", 1),
          ("syncToPw", 2),
          ("syncToLine", 3))
    )


_ProvMseClockModeType_Type.__name__ = "Integer32"
_ProvMseClockModeType_Object = MibTableColumn
provMseClockModeType = _ProvMseClockModeType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 2, 1, 3),
    _ProvMseClockModeType_Type()
)
provMseClockModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMseClockModeType.setStatus("current")


class _ProvMseClockACRLineSelect_Type(Integer32):
    """Custom type provMseClockACRLineSelect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ProvMseClockACRLineSelect_Type.__name__ = "Integer32"
_ProvMseClockACRLineSelect_Object = MibTableColumn
provMseClockACRLineSelect = _ProvMseClockACRLineSelect_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 2, 1, 4),
    _ProvMseClockACRLineSelect_Type()
)
provMseClockACRLineSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMseClockACRLineSelect.setStatus("current")
_ProvMseClockModeExtTable_Object = MibTable
provMseClockModeExtTable = _ProvMseClockModeExtTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 3)
)
if mibBuilder.loadTexts:
    provMseClockModeExtTable.setStatus("current")
_ProvMseClockModeExtEntry_Object = MibTableRow
provMseClockModeExtEntry = _ProvMseClockModeExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 3, 1)
)
provMseClockModeExtEntry.setIndexNames(
    (0, "IPE-MSE-MIB", "provMseClockModeExtIfIndex"),
)
if mibBuilder.loadTexts:
    provMseClockModeExtEntry.setStatus("current")
_ProvMseClockModeExtIfIndex_Type = InterfaceIndex
_ProvMseClockModeExtIfIndex_Object = MibTableColumn
provMseClockModeExtIfIndex = _ProvMseClockModeExtIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 3, 1, 1),
    _ProvMseClockModeExtIfIndex_Type()
)
provMseClockModeExtIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseClockModeExtIfIndex.setStatus("current")
_ProvMseClockModeExtNEAddress_Type = IpAddress
_ProvMseClockModeExtNEAddress_Object = MibTableColumn
provMseClockModeExtNEAddress = _ProvMseClockModeExtNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 3, 1, 2),
    _ProvMseClockModeExtNEAddress_Type()
)
provMseClockModeExtNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseClockModeExtNEAddress.setStatus("current")


class _ProvMseClockModeReply2Master_Type(IpeEnableDisableValue):
    """Custom type provMseClockModeReply2Master based on IpeEnableDisableValue"""
    defaultValue = 2


_ProvMseClockModeReply2Master_Type.__name__ = "IpeEnableDisableValue"
_ProvMseClockModeReply2Master_Object = MibTableColumn
provMseClockModeReply2Master = _ProvMseClockModeReply2Master_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 3, 1, 3),
    _ProvMseClockModeReply2Master_Type()
)
provMseClockModeReply2Master.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMseClockModeReply2Master.setStatus("current")


class _ProvMseClockSupplyMode_Type(IpeEnableDisableValue):
    """Custom type provMseClockSupplyMode based on IpeEnableDisableValue"""
    defaultValue = 1


_ProvMseClockSupplyMode_Type.__name__ = "IpeEnableDisableValue"
_ProvMseClockSupplyMode_Object = MibTableColumn
provMseClockSupplyMode = _ProvMseClockSupplyMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 3, 1, 4),
    _ProvMseClockSupplyMode_Type()
)
provMseClockSupplyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMseClockSupplyMode.setStatus("current")
_ProvMseClockSelectTable_Object = MibTable
provMseClockSelectTable = _ProvMseClockSelectTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 4)
)
if mibBuilder.loadTexts:
    provMseClockSelectTable.setStatus("current")
_ProvMseClockSelectEntry_Object = MibTableRow
provMseClockSelectEntry = _ProvMseClockSelectEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 4, 1)
)
provMseClockSelectEntry.setIndexNames(
    (0, "IPE-MSE-MIB", "provMseClockSelectCardId"),
)
if mibBuilder.loadTexts:
    provMseClockSelectEntry.setStatus("current")
_ProvMseClockSelectCardId_Type = Integer32
_ProvMseClockSelectCardId_Object = MibTableColumn
provMseClockSelectCardId = _ProvMseClockSelectCardId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 4, 1, 1),
    _ProvMseClockSelectCardId_Type()
)
provMseClockSelectCardId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseClockSelectCardId.setStatus("current")
_ProvMseClockSelectNEAddress_Type = IpAddress
_ProvMseClockSelectNEAddress_Object = MibTableColumn
provMseClockSelectNEAddress = _ProvMseClockSelectNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 4, 1, 2),
    _ProvMseClockSelectNEAddress_Type()
)
provMseClockSelectNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMseClockSelectNEAddress.setStatus("current")


class _ProvMseClockSelectLineNum_Type(Integer32):
    """Custom type provMseClockSelectLineNum based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ProvMseClockSelectLineNum_Type.__name__ = "Integer32"
_ProvMseClockSelectLineNum_Object = MibTableColumn
provMseClockSelectLineNum = _ProvMseClockSelectLineNum_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 40, 4, 1, 3),
    _ProvMseClockSelectLineNum_Type()
)
provMseClockSelectLineNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMseClockSelectLineNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-MSE-MIB",
    **{"IpeEnableDisableValue": IpeEnableDisableValue,
       "SeverityValue": SeverityValue,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "alarmStatusGroup": alarmStatusGroup,
       "asMseGroup": asMseGroup,
       "asMseCardTable": asMseCardTable,
       "asMseCardEntry": asMseCardEntry,
       "asMseCardIndex": asMseCardIndex,
       "asMseCardNEAddress": asMseCardNEAddress,
       "asMseCardModuleFail": asMseCardModuleFail,
       "asMseCardComFailAlarm": asMseCardComFailAlarm,
       "asMseCardUnequipped": asMseCardUnequipped,
       "asMseCardTypeMismatch": asMseCardTypeMismatch,
       "asMseCardBusErrorTx": asMseCardBusErrorTx,
       "asMseCardBusErrorRx": asMseCardBusErrorRx,
       "asMseCardClkFail": asMseCardClkFail,
       "asMseLineTable": asMseLineTable,
       "asMseLineEntry": asMseLineEntry,
       "asMseLineIfIndex": asMseLineIfIndex,
       "asMseLineNEAddress": asMseLineNEAddress,
       "asMseLineBfrUnderrun": asMseLineBfrUnderrun,
       "asMseLineAdaptiveClkStatus": asMseLineAdaptiveClkStatus,
       "provisioningGroup": provisioningGroup,
       "provMseGroup": provMseGroup,
       "provMseLineModeTable": provMseLineModeTable,
       "provMseLineModeEntry": provMseLineModeEntry,
       "provMseLineModeIfIndex": provMseLineModeIfIndex,
       "provMseLineModeNEAddress": provMseLineModeNEAddress,
       "provMseLineModeType": provMseLineModeType,
       "provMseClockModeTable": provMseClockModeTable,
       "provMseClockModeEntry": provMseClockModeEntry,
       "provMseClockModeIfIndex": provMseClockModeIfIndex,
       "provMseClockModeNEAddress": provMseClockModeNEAddress,
       "provMseClockModeType": provMseClockModeType,
       "provMseClockACRLineSelect": provMseClockACRLineSelect,
       "provMseClockModeExtTable": provMseClockModeExtTable,
       "provMseClockModeExtEntry": provMseClockModeExtEntry,
       "provMseClockModeExtIfIndex": provMseClockModeExtIfIndex,
       "provMseClockModeExtNEAddress": provMseClockModeExtNEAddress,
       "provMseClockModeReply2Master": provMseClockModeReply2Master,
       "provMseClockSupplyMode": provMseClockSupplyMode,
       "provMseClockSelectTable": provMseClockSelectTable,
       "provMseClockSelectEntry": provMseClockSelectEntry,
       "provMseClockSelectCardId": provMseClockSelectCardId,
       "provMseClockSelectNEAddress": provMseClockSelectNEAddress,
       "provMseClockSelectLineNum": provMseClockSelectLineNum}
)
