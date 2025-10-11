# SNMP MIB module (IPE-COMMON1000-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-COMMON1000-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:51 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class OffOnValue(TextualConvention, Integer32):
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
          ("off", 1),
          ("on", 2))
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
_System5_ObjectIdentity = ObjectIdentity
system5 = _System5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5)
)
_IpeConfigurationGroup_ObjectIdentity = ObjectIdentity
ipeConfigurationGroup = _IpeConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3)
)
_IpeCfgPortGroup_ObjectIdentity = ObjectIdentity
ipeCfgPortGroup = _IpeCfgPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15)
)
_IpeCfgPortLct1kTable_Object = MibTable
ipeCfgPortLct1kTable = _IpeCfgPortLct1kTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8)
)
if mibBuilder.loadTexts:
    ipeCfgPortLct1kTable.setStatus("current")
_IpeCfgPortLct1kEntry_Object = MibTableRow
ipeCfgPortLct1kEntry = _IpeCfgPortLct1kEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1)
)
ipeCfgPortLct1kEntry.setIndexNames(
    (0, "IPE-COMMON1000-MIB", "ipeCfgPortLct1kIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgPortLct1kEntry.setStatus("current")


class _IpeCfgPortLct1kIndex_Type(Integer32):
    """Custom type ipeCfgPortLct1kIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IpeCfgPortLct1kIndex_Type.__name__ = "Integer32"
_IpeCfgPortLct1kIndex_Object = MibTableColumn
ipeCfgPortLct1kIndex = _IpeCfgPortLct1kIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1, 1),
    _IpeCfgPortLct1kIndex_Type()
)
ipeCfgPortLct1kIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortLct1kIndex.setStatus("current")
_IpeCfgPortLct1kNEAddress_Type = IpAddress
_IpeCfgPortLct1kNEAddress_Object = MibTableColumn
ipeCfgPortLct1kNEAddress = _IpeCfgPortLct1kNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1, 2),
    _IpeCfgPortLct1kNEAddress_Type()
)
ipeCfgPortLct1kNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgPortLct1kNEAddress.setStatus("current")
_IpeCfgPortLct1kIpAddress_Type = IpAddress
_IpeCfgPortLct1kIpAddress_Object = MibTableColumn
ipeCfgPortLct1kIpAddress = _IpeCfgPortLct1kIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1, 3),
    _IpeCfgPortLct1kIpAddress_Type()
)
ipeCfgPortLct1kIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLct1kIpAddress.setStatus("current")
_IpeCfgPortLct1kNetMask_Type = IpAddress
_IpeCfgPortLct1kNetMask_Object = MibTableColumn
ipeCfgPortLct1kNetMask = _IpeCfgPortLct1kNetMask_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1, 4),
    _IpeCfgPortLct1kNetMask_Type()
)
ipeCfgPortLct1kNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLct1kNetMask.setStatus("current")


class _IpeCfgPortLct1kEnable_Type(Integer32):
    """Custom type ipeCfgPortLct1kEnable based on Integer32"""
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


_IpeCfgPortLct1kEnable_Type.__name__ = "Integer32"
_IpeCfgPortLct1kEnable_Object = MibTableColumn
ipeCfgPortLct1kEnable = _IpeCfgPortLct1kEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1, 5),
    _IpeCfgPortLct1kEnable_Type()
)
ipeCfgPortLct1kEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLct1kEnable.setStatus("current")


class _IpeCfgPortLct1kMtu_Type(Integer32):
    """Custom type ipeCfgPortLct1kMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(256, 1500),
    )


_IpeCfgPortLct1kMtu_Type.__name__ = "Integer32"
_IpeCfgPortLct1kMtu_Object = MibTableColumn
ipeCfgPortLct1kMtu = _IpeCfgPortLct1kMtu_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1, 6),
    _IpeCfgPortLct1kMtu_Type()
)
ipeCfgPortLct1kMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLct1kMtu.setStatus("current")


class _IpeCfgPortLct1kAutoNeg_Type(Integer32):
    """Custom type ipeCfgPortLct1kAutoNeg based on Integer32"""
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


_IpeCfgPortLct1kAutoNeg_Type.__name__ = "Integer32"
_IpeCfgPortLct1kAutoNeg_Object = MibTableColumn
ipeCfgPortLct1kAutoNeg = _IpeCfgPortLct1kAutoNeg_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 15, 8, 1, 7),
    _IpeCfgPortLct1kAutoNeg_Type()
)
ipeCfgPortLct1kAutoNeg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgPortLct1kAutoNeg.setStatus("current")
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_AlarmStatusGroup_ObjectIdentity = ObjectIdentity
alarmStatusGroup = _AlarmStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3)
)
_AsMainCtrlGroup_ObjectIdentity = ObjectIdentity
asMainCtrlGroup = _AsMainCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35)
)
_AsMainCtrlGroupTable_Object = MibTable
asMainCtrlGroupTable = _AsMainCtrlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1)
)
if mibBuilder.loadTexts:
    asMainCtrlGroupTable.setStatus("current")
_AsMainCtrlGroupEntry_Object = MibTableRow
asMainCtrlGroupEntry = _AsMainCtrlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1)
)
asMainCtrlGroupEntry.setIndexNames(
    (0, "IPE-COMMON1000-MIB", "asMainCtrlGroupIndex"),
)
if mibBuilder.loadTexts:
    asMainCtrlGroupEntry.setStatus("current")


class _AsMainCtrlGroupIndex_Type(Integer32):
    """Custom type asMainCtrlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AsMainCtrlGroupIndex_Type.__name__ = "Integer32"
_AsMainCtrlGroupIndex_Object = MibTableColumn
asMainCtrlGroupIndex = _AsMainCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 1),
    _AsMainCtrlGroupIndex_Type()
)
asMainCtrlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMainCtrlGroupIndex.setStatus("current")
_AsMainCtrlGroupNEAddress_Type = IpAddress
_AsMainCtrlGroupNEAddress_Object = MibTableColumn
asMainCtrlGroupNEAddress = _AsMainCtrlGroupNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 2),
    _AsMainCtrlGroupNEAddress_Type()
)
asMainCtrlGroupNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMainCtrlGroupNEAddress.setStatus("current")
_CtrlGroupSvLineAlarm_Type = SeverityValue
_CtrlGroupSvLineAlarm_Object = MibTableColumn
ctrlGroupSvLineAlarm = _CtrlGroupSvLineAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 3),
    _CtrlGroupSvLineAlarm_Type()
)
ctrlGroupSvLineAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSvLineAlarm.setStatus("current")
_CtrlGroupIduTotalAlarm_Type = SeverityValue
_CtrlGroupIduTotalAlarm_Object = MibTableColumn
ctrlGroupIduTotalAlarm = _CtrlGroupIduTotalAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 4),
    _CtrlGroupIduTotalAlarm_Type()
)
ctrlGroupIduTotalAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupIduTotalAlarm.setStatus("current")
_CtrlGroupMaintenance_Type = OffOnValue
_CtrlGroupMaintenance_Object = MibTableColumn
ctrlGroupMaintenance = _CtrlGroupMaintenance_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 5),
    _CtrlGroupMaintenance_Type()
)
ctrlGroupMaintenance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupMaintenance.setStatus("current")
_CtrlGroupComFail_Type = SeverityValue
_CtrlGroupComFail_Object = MibTableColumn
ctrlGroupComFail = _CtrlGroupComFail_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 6),
    _CtrlGroupComFail_Type()
)
ctrlGroupComFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupComFail.setStatus("current")
_CtrlGroupFirmwareVerMismatch_Type = SeverityValue
_CtrlGroupFirmwareVerMismatch_Object = MibTableColumn
ctrlGroupFirmwareVerMismatch = _CtrlGroupFirmwareVerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 7),
    _CtrlGroupFirmwareVerMismatch_Type()
)
ctrlGroupFirmwareVerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupFirmwareVerMismatch.setStatus("current")
_CtrlGroupCardMismatch_Type = SeverityValue
_CtrlGroupCardMismatch_Object = MibTableColumn
ctrlGroupCardMismatch = _CtrlGroupCardMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 8),
    _CtrlGroupCardMismatch_Type()
)
ctrlGroupCardMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupCardMismatch.setStatus("current")
_CtrlGroupHardwareVerMismatch_Type = SeverityValue
_CtrlGroupHardwareVerMismatch_Object = MibTableColumn
ctrlGroupHardwareVerMismatch = _CtrlGroupHardwareVerMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 9),
    _CtrlGroupHardwareVerMismatch_Type()
)
ctrlGroupHardwareVerMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupHardwareVerMismatch.setStatus("current")
_CtrlGroupMountedClk2mMismatch_Type = SeverityValue
_CtrlGroupMountedClk2mMismatch_Object = MibTableColumn
ctrlGroupMountedClk2mMismatch = _CtrlGroupMountedClk2mMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 10),
    _CtrlGroupMountedClk2mMismatch_Type()
)
ctrlGroupMountedClk2mMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupMountedClk2mMismatch.setStatus("current")
_CtrlGroupSwitchOverFailure_Type = OffOnValue
_CtrlGroupSwitchOverFailure_Object = MibTableColumn
ctrlGroupSwitchOverFailure = _CtrlGroupSwitchOverFailure_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 11),
    _CtrlGroupSwitchOverFailure_Type()
)
ctrlGroupSwitchOverFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSwitchOverFailure.setStatus("current")
_CtrlGroupSwitchComplete_Type = OffOnValue
_CtrlGroupSwitchComplete_Object = MibTableColumn
ctrlGroupSwitchComplete = _CtrlGroupSwitchComplete_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 12),
    _CtrlGroupSwitchComplete_Type()
)
ctrlGroupSwitchComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSwitchComplete.setStatus("current")
_CtrlGroupForcedSbySwitchComplete_Type = OffOnValue
_CtrlGroupForcedSbySwitchComplete_Object = MibTableColumn
ctrlGroupForcedSbySwitchComplete = _CtrlGroupForcedSbySwitchComplete_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 13),
    _CtrlGroupForcedSbySwitchComplete_Type()
)
ctrlGroupForcedSbySwitchComplete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupForcedSbySwitchComplete.setStatus("current")
_CtrlGroupSwitchedTime_Type = DateAndTime
_CtrlGroupSwitchedTime_Object = MibTableColumn
ctrlGroupSwitchedTime = _CtrlGroupSwitchedTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 14),
    _CtrlGroupSwitchedTime_Type()
)
ctrlGroupSwitchedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSwitchedTime.setStatus("current")


class _CtrlGroupSwitchedReason_Type(DisplayString):
    """Custom type ctrlGroupSwitchedReason based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CtrlGroupSwitchedReason_Type.__name__ = "DisplayString"
_CtrlGroupSwitchedReason_Object = MibTableColumn
ctrlGroupSwitchedReason = _CtrlGroupSwitchedReason_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 15),
    _CtrlGroupSwitchedReason_Type()
)
ctrlGroupSwitchedReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSwitchedReason.setStatus("current")
_CtrlGroupConfigDataStoredTime_Type = DateAndTime
_CtrlGroupConfigDataStoredTime_Object = MibTableColumn
ctrlGroupConfigDataStoredTime = _CtrlGroupConfigDataStoredTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 16),
    _CtrlGroupConfigDataStoredTime_Type()
)
ctrlGroupConfigDataStoredTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupConfigDataStoredTime.setStatus("current")
_CtrlGroupSbyBusErrorTx_Type = SeverityValue
_CtrlGroupSbyBusErrorTx_Object = MibTableColumn
ctrlGroupSbyBusErrorTx = _CtrlGroupSbyBusErrorTx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 17),
    _CtrlGroupSbyBusErrorTx_Type()
)
ctrlGroupSbyBusErrorTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSbyBusErrorTx.setStatus("current")
_CtrlGroupSbyBusErrorRx_Type = SeverityValue
_CtrlGroupSbyBusErrorRx_Object = MibTableColumn
ctrlGroupSbyBusErrorRx = _CtrlGroupSbyBusErrorRx_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 18),
    _CtrlGroupSbyBusErrorRx_Type()
)
ctrlGroupSbyBusErrorRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSbyBusErrorRx.setStatus("current")
_CtrlGroupSbyTermComFailAlarm_Type = SeverityValue
_CtrlGroupSbyTermComFailAlarm_Object = MibTableColumn
ctrlGroupSbyTermComFailAlarm = _CtrlGroupSbyTermComFailAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 19),
    _CtrlGroupSbyTermComFailAlarm_Type()
)
ctrlGroupSbyTermComFailAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSbyTermComFailAlarm.setStatus("current")
_CtrlGroupDbMismatch_Type = SeverityValue
_CtrlGroupDbMismatch_Object = MibTableColumn
ctrlGroupDbMismatch = _CtrlGroupDbMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 20),
    _CtrlGroupDbMismatch_Type()
)
ctrlGroupDbMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupDbMismatch.setStatus("current")
_CtrlGroupSoftkeyEquipSerialMismatch_Type = SeverityValue
_CtrlGroupSoftkeyEquipSerialMismatch_Object = MibTableColumn
ctrlGroupSoftkeyEquipSerialMismatch = _CtrlGroupSoftkeyEquipSerialMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 1, 1, 21),
    _CtrlGroupSoftkeyEquipSerialMismatch_Type()
)
ctrlGroupSoftkeyEquipSerialMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctrlGroupSoftkeyEquipSerialMismatch.setStatus("current")
_AsMainCtrlCardTable_Object = MibTable
asMainCtrlCardTable = _AsMainCtrlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2)
)
if mibBuilder.loadTexts:
    asMainCtrlCardTable.setStatus("current")
_AsMainCtrlCardEntry_Object = MibTableRow
asMainCtrlCardEntry = _AsMainCtrlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1)
)
asMainCtrlCardEntry.setIndexNames(
    (0, "IPE-COMMON1000-MIB", "asMainCtrlCardIndex"),
)
if mibBuilder.loadTexts:
    asMainCtrlCardEntry.setStatus("current")


class _AsMainCtrlCardIndex_Type(Integer32):
    """Custom type asMainCtrlCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 18),
    )


_AsMainCtrlCardIndex_Type.__name__ = "Integer32"
_AsMainCtrlCardIndex_Object = MibTableColumn
asMainCtrlCardIndex = _AsMainCtrlCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 1),
    _AsMainCtrlCardIndex_Type()
)
asMainCtrlCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMainCtrlCardIndex.setStatus("current")
_AsMainCtrlCardNEAddress_Type = IpAddress
_AsMainCtrlCardNEAddress_Object = MibTableColumn
asMainCtrlCardNEAddress = _AsMainCtrlCardNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 2),
    _AsMainCtrlCardNEAddress_Type()
)
asMainCtrlCardNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asMainCtrlCardNEAddress.setStatus("current")
_MainCardAlarm_Type = SeverityValue
_MainCardAlarm_Object = MibTableColumn
mainCardAlarm = _MainCardAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 3),
    _MainCardAlarm_Type()
)
mainCardAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardAlarm.setStatus("current")
_MainUsbFailure_Type = SeverityValue
_MainUsbFailure_Object = MibTableColumn
mainUsbFailure = _MainUsbFailure_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 4),
    _MainUsbFailure_Type()
)
mainUsbFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainUsbFailure.setStatus("current")
_MainCpuAlarm_Type = SeverityValue
_MainCpuAlarm_Object = MibTableColumn
mainCpuAlarm = _MainCpuAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 5),
    _MainCpuAlarm_Type()
)
mainCpuAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCpuAlarm.setStatus("current")
_MainMemoryFailure_Type = SeverityValue
_MainMemoryFailure_Object = MibTableColumn
mainMemoryFailure = _MainMemoryFailure_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 6),
    _MainMemoryFailure_Type()
)
mainMemoryFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainMemoryFailure.setStatus("current")


class _MainClk2mMount_Type(Integer32):
    """Custom type mainClk2mMount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unmount", 1),
          ("mount", 2))
    )


_MainClk2mMount_Type.__name__ = "Integer32"
_MainClk2mMount_Object = MibTableColumn
mainClk2mMount = _MainClk2mMount_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 7),
    _MainClk2mMount_Type()
)
mainClk2mMount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainClk2mMount.setStatus("current")


class _MainCardRunningStatus_Type(Integer32):
    """Custom type mainCardRunningStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("act", 1),
          ("sby", 2),
          ("flt", 3),
          ("actFlt", 4),
          ("sbyFlt", 5),
          ("init", 6),
          ("oos", 7),
          ("initFlt", 8),
          ("unmount", 9))
    )


_MainCardRunningStatus_Type.__name__ = "Integer32"
_MainCardRunningStatus_Object = MibTableColumn
mainCardRunningStatus = _MainCardRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 8),
    _MainCardRunningStatus_Type()
)
mainCardRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCardRunningStatus.setStatus("current")
_MainTempAlarm_Type = SeverityValue
_MainTempAlarm_Object = MibTableColumn
mainTempAlarm = _MainTempAlarm_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 9),
    _MainTempAlarm_Type()
)
mainTempAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainTempAlarm.setStatus("current")
_MainCtrlUnequipped_Type = SeverityValue
_MainCtrlUnequipped_Object = MibTableColumn
mainCtrlUnequipped = _MainCtrlUnequipped_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 10),
    _MainCtrlUnequipped_Type()
)
mainCtrlUnequipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCtrlUnequipped.setStatus("current")
_MainCtrlBusError_Type = SeverityValue
_MainCtrlBusError_Object = MibTableColumn
mainCtrlBusError = _MainCtrlBusError_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 11),
    _MainCtrlBusError_Type()
)
mainCtrlBusError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainCtrlBusError.setStatus("current")


class _MainTemperature_Type(Integer32):
    """Custom type mainTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -999),
        ValueRangeConstraint(-500, 1500),
    )


_MainTemperature_Type.__name__ = "Integer32"
_MainTemperature_Object = MibTableColumn
mainTemperature = _MainTemperature_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 12),
    _MainTemperature_Type()
)
mainTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainTemperature.setStatus("current")
if mibBuilder.loadTexts:
    mainTemperature.setUnits("0.1 degree")
_MainFPGAMismatch_Type = SeverityValue
_MainFPGAMismatch_Object = MibTableColumn
mainFPGAMismatch = _MainFPGAMismatch_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 3, 35, 2, 1, 13),
    _MainFPGAMismatch_Type()
)
mainFPGAMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mainFPGAMismatch.setStatus("current")
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5)
)
_ProvCtrl1kGroup_ObjectIdentity = ObjectIdentity
provCtrl1kGroup = _ProvCtrl1kGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35)
)
_ProvMiscDescriptionTable_Object = MibTable
provMiscDescriptionTable = _ProvMiscDescriptionTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1)
)
if mibBuilder.loadTexts:
    provMiscDescriptionTable.setStatus("current")
_ProvMiscDescriptionEntry_Object = MibTableRow
provMiscDescriptionEntry = _ProvMiscDescriptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1)
)
provMiscDescriptionEntry.setIndexNames(
    (0, "IPE-COMMON1000-MIB", "provMiscDescriptionIndex"),
)
if mibBuilder.loadTexts:
    provMiscDescriptionEntry.setStatus("current")


class _ProvMiscDescriptionIndex_Type(Integer32):
    """Custom type provMiscDescriptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 23),
    )


_ProvMiscDescriptionIndex_Type.__name__ = "Integer32"
_ProvMiscDescriptionIndex_Object = MibTableColumn
provMiscDescriptionIndex = _ProvMiscDescriptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 1),
    _ProvMiscDescriptionIndex_Type()
)
provMiscDescriptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMiscDescriptionIndex.setStatus("current")
_ProvMiscDescriptionNEAddress_Type = IpAddress
_ProvMiscDescriptionNEAddress_Object = MibTableColumn
provMiscDescriptionNEAddress = _ProvMiscDescriptionNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 2),
    _ProvMiscDescriptionNEAddress_Type()
)
provMiscDescriptionNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    provMiscDescriptionNEAddress.setStatus("current")


class _ProvMiscDescription1_Type(DisplayString):
    """Custom type provMiscDescription1 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription1_Type.__name__ = "DisplayString"
_ProvMiscDescription1_Object = MibTableColumn
provMiscDescription1 = _ProvMiscDescription1_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 3),
    _ProvMiscDescription1_Type()
)
provMiscDescription1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription1.setStatus("current")


class _ProvMiscDescription2_Type(DisplayString):
    """Custom type provMiscDescription2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription2_Type.__name__ = "DisplayString"
_ProvMiscDescription2_Object = MibTableColumn
provMiscDescription2 = _ProvMiscDescription2_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 4),
    _ProvMiscDescription2_Type()
)
provMiscDescription2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription2.setStatus("current")


class _ProvMiscDescription3_Type(DisplayString):
    """Custom type provMiscDescription3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription3_Type.__name__ = "DisplayString"
_ProvMiscDescription3_Object = MibTableColumn
provMiscDescription3 = _ProvMiscDescription3_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 5),
    _ProvMiscDescription3_Type()
)
provMiscDescription3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription3.setStatus("current")


class _ProvMiscDescription4_Type(DisplayString):
    """Custom type provMiscDescription4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription4_Type.__name__ = "DisplayString"
_ProvMiscDescription4_Object = MibTableColumn
provMiscDescription4 = _ProvMiscDescription4_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 6),
    _ProvMiscDescription4_Type()
)
provMiscDescription4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription4.setStatus("current")


class _ProvMiscDescription5_Type(DisplayString):
    """Custom type provMiscDescription5 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription5_Type.__name__ = "DisplayString"
_ProvMiscDescription5_Object = MibTableColumn
provMiscDescription5 = _ProvMiscDescription5_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 7),
    _ProvMiscDescription5_Type()
)
provMiscDescription5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription5.setStatus("current")


class _ProvMiscDescription6_Type(DisplayString):
    """Custom type provMiscDescription6 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription6_Type.__name__ = "DisplayString"
_ProvMiscDescription6_Object = MibTableColumn
provMiscDescription6 = _ProvMiscDescription6_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 8),
    _ProvMiscDescription6_Type()
)
provMiscDescription6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription6.setStatus("current")


class _ProvMiscDescription7_Type(DisplayString):
    """Custom type provMiscDescription7 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription7_Type.__name__ = "DisplayString"
_ProvMiscDescription7_Object = MibTableColumn
provMiscDescription7 = _ProvMiscDescription7_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 9),
    _ProvMiscDescription7_Type()
)
provMiscDescription7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription7.setStatus("current")


class _ProvMiscDescription8_Type(DisplayString):
    """Custom type provMiscDescription8 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription8_Type.__name__ = "DisplayString"
_ProvMiscDescription8_Object = MibTableColumn
provMiscDescription8 = _ProvMiscDescription8_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 10),
    _ProvMiscDescription8_Type()
)
provMiscDescription8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription8.setStatus("current")


class _ProvMiscDescription9_Type(DisplayString):
    """Custom type provMiscDescription9 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ProvMiscDescription9_Type.__name__ = "DisplayString"
_ProvMiscDescription9_Object = MibTableColumn
provMiscDescription9 = _ProvMiscDescription9_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 5, 35, 1, 1, 11),
    _ProvMiscDescription9_Type()
)
provMiscDescription9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    provMiscDescription9.setStatus("current")
_MaintenanceGroup_ObjectIdentity = ObjectIdentity
maintenanceGroup = _MaintenanceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6)
)
_MaintCtrlGroup_ObjectIdentity = ObjectIdentity
maintCtrlGroup = _MaintCtrlGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35)
)
_MaintCtrlGroupTable_Object = MibTable
maintCtrlGroupTable = _MaintCtrlGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 1)
)
if mibBuilder.loadTexts:
    maintCtrlGroupTable.setStatus("current")
_MaintCtrlGroupEntry_Object = MibTableRow
maintCtrlGroupEntry = _MaintCtrlGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 1, 1)
)
maintCtrlGroupEntry.setIndexNames(
    (0, "IPE-COMMON1000-MIB", "maintCtrlGroupIndex"),
)
if mibBuilder.loadTexts:
    maintCtrlGroupEntry.setStatus("current")


class _MaintCtrlGroupIndex_Type(Integer32):
    """Custom type maintCtrlGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_MaintCtrlGroupIndex_Type.__name__ = "Integer32"
_MaintCtrlGroupIndex_Object = MibTableColumn
maintCtrlGroupIndex = _MaintCtrlGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 1, 1, 1),
    _MaintCtrlGroupIndex_Type()
)
maintCtrlGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintCtrlGroupIndex.setStatus("current")
_MaintCtrlGroupNEAddress_Type = IpAddress
_MaintCtrlGroupNEAddress_Object = MibTableColumn
maintCtrlGroupNEAddress = _MaintCtrlGroupNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 1, 1, 2),
    _MaintCtrlGroupNEAddress_Type()
)
maintCtrlGroupNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintCtrlGroupNEAddress.setStatus("current")


class _MaintCtrlGroupSwControl_Type(Integer32):
    """Custom type maintCtrlGroupSwControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("switchOver", 1))
    )


_MaintCtrlGroupSwControl_Type.__name__ = "Integer32"
_MaintCtrlGroupSwControl_Object = MibTableColumn
maintCtrlGroupSwControl = _MaintCtrlGroupSwControl_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 1, 1, 4),
    _MaintCtrlGroupSwControl_Type()
)
maintCtrlGroupSwControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintCtrlGroupSwControl.setStatus("current")


class _MaintCtrlGroupMain1Oos_Type(Integer32):
    """Custom type maintCtrlGroupMain1Oos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("oos", 1))
    )


_MaintCtrlGroupMain1Oos_Type.__name__ = "Integer32"
_MaintCtrlGroupMain1Oos_Object = MibTableColumn
maintCtrlGroupMain1Oos = _MaintCtrlGroupMain1Oos_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 1, 1, 5),
    _MaintCtrlGroupMain1Oos_Type()
)
maintCtrlGroupMain1Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintCtrlGroupMain1Oos.setStatus("current")


class _MaintCtrlGroupMain2Oos_Type(Integer32):
    """Custom type maintCtrlGroupMain2Oos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("oos", 1))
    )


_MaintCtrlGroupMain2Oos_Type.__name__ = "Integer32"
_MaintCtrlGroupMain2Oos_Object = MibTableColumn
maintCtrlGroupMain2Oos = _MaintCtrlGroupMain2Oos_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 1, 1, 6),
    _MaintCtrlGroupMain2Oos_Type()
)
maintCtrlGroupMain2Oos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintCtrlGroupMain2Oos.setStatus("current")
_MaintCtrlCardTable_Object = MibTable
maintCtrlCardTable = _MaintCtrlCardTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 2)
)
if mibBuilder.loadTexts:
    maintCtrlCardTable.setStatus("current")
_MaintCtrlCardEntry_Object = MibTableRow
maintCtrlCardEntry = _MaintCtrlCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 2, 1)
)
maintCtrlCardEntry.setIndexNames(
    (0, "IPE-COMMON1000-MIB", "maintCtrlCardIndex"),
)
if mibBuilder.loadTexts:
    maintCtrlCardEntry.setStatus("current")


class _MaintCtrlCardIndex_Type(Integer32):
    """Custom type maintCtrlCardIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(17, 18),
    )


_MaintCtrlCardIndex_Type.__name__ = "Integer32"
_MaintCtrlCardIndex_Object = MibTableColumn
maintCtrlCardIndex = _MaintCtrlCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 2, 1, 1),
    _MaintCtrlCardIndex_Type()
)
maintCtrlCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintCtrlCardIndex.setStatus("current")
_MaintCtrlCardNEAddress_Type = IpAddress
_MaintCtrlCardNEAddress_Object = MibTableColumn
maintCtrlCardNEAddress = _MaintCtrlCardNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 2, 1, 2),
    _MaintCtrlCardNEAddress_Type()
)
maintCtrlCardNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintCtrlCardNEAddress.setStatus("current")


class _MaintCtrlCardReset_Type(Integer32):
    """Custom type maintCtrlCardReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("reset", 1))
    )


_MaintCtrlCardReset_Type.__name__ = "Integer32"
_MaintCtrlCardReset_Object = MibTableColumn
maintCtrlCardReset = _MaintCtrlCardReset_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 2, 1, 3),
    _MaintCtrlCardReset_Type()
)
maintCtrlCardReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintCtrlCardReset.setStatus("current")


class _MaintCtrlSoftwareReset_Type(Integer32):
    """Custom type maintCtrlSoftwareReset based on Integer32"""
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
          ("resetNormal", 1),
          ("resetRevert", 2),
          ("resetNone", 3))
    )


_MaintCtrlSoftwareReset_Type.__name__ = "Integer32"
_MaintCtrlSoftwareReset_Object = MibTableColumn
maintCtrlSoftwareReset = _MaintCtrlSoftwareReset_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 2, 1, 5),
    _MaintCtrlSoftwareReset_Type()
)
maintCtrlSoftwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintCtrlSoftwareReset.setStatus("current")


class _MaintCtrlCardHardwareReset_Type(Integer32):
    """Custom type maintCtrlCardHardwareReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("reset", 1))
    )


_MaintCtrlCardHardwareReset_Type.__name__ = "Integer32"
_MaintCtrlCardHardwareReset_Object = MibTableColumn
maintCtrlCardHardwareReset = _MaintCtrlCardHardwareReset_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 6, 35, 2, 1, 6),
    _MaintCtrlCardHardwareReset_Type()
)
maintCtrlCardHardwareReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    maintCtrlCardHardwareReset.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-COMMON1000-MIB",
    **{"OffOnValue": OffOnValue,
       "SeverityValue": SeverityValue,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "system5": system5,
       "ipeConfigurationGroup": ipeConfigurationGroup,
       "ipeCfgPortGroup": ipeCfgPortGroup,
       "ipeCfgPortLct1kTable": ipeCfgPortLct1kTable,
       "ipeCfgPortLct1kEntry": ipeCfgPortLct1kEntry,
       "ipeCfgPortLct1kIndex": ipeCfgPortLct1kIndex,
       "ipeCfgPortLct1kNEAddress": ipeCfgPortLct1kNEAddress,
       "ipeCfgPortLct1kIpAddress": ipeCfgPortLct1kIpAddress,
       "ipeCfgPortLct1kNetMask": ipeCfgPortLct1kNetMask,
       "ipeCfgPortLct1kEnable": ipeCfgPortLct1kEnable,
       "ipeCfgPortLct1kMtu": ipeCfgPortLct1kMtu,
       "ipeCfgPortLct1kAutoNeg": ipeCfgPortLct1kAutoNeg,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "alarmStatusGroup": alarmStatusGroup,
       "asMainCtrlGroup": asMainCtrlGroup,
       "asMainCtrlGroupTable": asMainCtrlGroupTable,
       "asMainCtrlGroupEntry": asMainCtrlGroupEntry,
       "asMainCtrlGroupIndex": asMainCtrlGroupIndex,
       "asMainCtrlGroupNEAddress": asMainCtrlGroupNEAddress,
       "ctrlGroupSvLineAlarm": ctrlGroupSvLineAlarm,
       "ctrlGroupIduTotalAlarm": ctrlGroupIduTotalAlarm,
       "ctrlGroupMaintenance": ctrlGroupMaintenance,
       "ctrlGroupComFail": ctrlGroupComFail,
       "ctrlGroupFirmwareVerMismatch": ctrlGroupFirmwareVerMismatch,
       "ctrlGroupCardMismatch": ctrlGroupCardMismatch,
       "ctrlGroupHardwareVerMismatch": ctrlGroupHardwareVerMismatch,
       "ctrlGroupMountedClk2mMismatch": ctrlGroupMountedClk2mMismatch,
       "ctrlGroupSwitchOverFailure": ctrlGroupSwitchOverFailure,
       "ctrlGroupSwitchComplete": ctrlGroupSwitchComplete,
       "ctrlGroupForcedSbySwitchComplete": ctrlGroupForcedSbySwitchComplete,
       "ctrlGroupSwitchedTime": ctrlGroupSwitchedTime,
       "ctrlGroupSwitchedReason": ctrlGroupSwitchedReason,
       "ctrlGroupConfigDataStoredTime": ctrlGroupConfigDataStoredTime,
       "ctrlGroupSbyBusErrorTx": ctrlGroupSbyBusErrorTx,
       "ctrlGroupSbyBusErrorRx": ctrlGroupSbyBusErrorRx,
       "ctrlGroupSbyTermComFailAlarm": ctrlGroupSbyTermComFailAlarm,
       "ctrlGroupDbMismatch": ctrlGroupDbMismatch,
       "ctrlGroupSoftkeyEquipSerialMismatch": ctrlGroupSoftkeyEquipSerialMismatch,
       "asMainCtrlCardTable": asMainCtrlCardTable,
       "asMainCtrlCardEntry": asMainCtrlCardEntry,
       "asMainCtrlCardIndex": asMainCtrlCardIndex,
       "asMainCtrlCardNEAddress": asMainCtrlCardNEAddress,
       "mainCardAlarm": mainCardAlarm,
       "mainUsbFailure": mainUsbFailure,
       "mainCpuAlarm": mainCpuAlarm,
       "mainMemoryFailure": mainMemoryFailure,
       "mainClk2mMount": mainClk2mMount,
       "mainCardRunningStatus": mainCardRunningStatus,
       "mainTempAlarm": mainTempAlarm,
       "mainCtrlUnequipped": mainCtrlUnequipped,
       "mainCtrlBusError": mainCtrlBusError,
       "mainTemperature": mainTemperature,
       "mainFPGAMismatch": mainFPGAMismatch,
       "provisioningGroup": provisioningGroup,
       "provCtrl1kGroup": provCtrl1kGroup,
       "provMiscDescriptionTable": provMiscDescriptionTable,
       "provMiscDescriptionEntry": provMiscDescriptionEntry,
       "provMiscDescriptionIndex": provMiscDescriptionIndex,
       "provMiscDescriptionNEAddress": provMiscDescriptionNEAddress,
       "provMiscDescription1": provMiscDescription1,
       "provMiscDescription2": provMiscDescription2,
       "provMiscDescription3": provMiscDescription3,
       "provMiscDescription4": provMiscDescription4,
       "provMiscDescription5": provMiscDescription5,
       "provMiscDescription6": provMiscDescription6,
       "provMiscDescription7": provMiscDescription7,
       "provMiscDescription8": provMiscDescription8,
       "provMiscDescription9": provMiscDescription9,
       "maintenanceGroup": maintenanceGroup,
       "maintCtrlGroup": maintCtrlGroup,
       "maintCtrlGroupTable": maintCtrlGroupTable,
       "maintCtrlGroupEntry": maintCtrlGroupEntry,
       "maintCtrlGroupIndex": maintCtrlGroupIndex,
       "maintCtrlGroupNEAddress": maintCtrlGroupNEAddress,
       "maintCtrlGroupSwControl": maintCtrlGroupSwControl,
       "maintCtrlGroupMain1Oos": maintCtrlGroupMain1Oos,
       "maintCtrlGroupMain2Oos": maintCtrlGroupMain2Oos,
       "maintCtrlCardTable": maintCtrlCardTable,
       "maintCtrlCardEntry": maintCtrlCardEntry,
       "maintCtrlCardIndex": maintCtrlCardIndex,
       "maintCtrlCardNEAddress": maintCtrlCardNEAddress,
       "maintCtrlCardReset": maintCtrlCardReset,
       "maintCtrlSoftwareReset": maintCtrlSoftwareReset,
       "maintCtrlCardHardwareReset": maintCtrlCardHardwareReset}
)
