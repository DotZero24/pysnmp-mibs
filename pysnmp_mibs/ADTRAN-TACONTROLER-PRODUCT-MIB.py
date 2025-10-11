# SNMP MIB module (ADTRAN-TACONTROLER-PRODUCT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TACONTROLER-PRODUCT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:40 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,
 adGenSlotProdCLEIcode,
 adGenSlotProdName,
 adGenSlotProdPartNumber) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex",
    "adGenSlotProdCLEIcode",
    "adGenSlotProdName",
    "adGenSlotProdPartNumber")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adShared")

(adTAeSCUTrapAlarmLevel,
 adTAeSCUenvAlarmInputLevel,
 adTAeSCUenvAlarmUserName) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel",
    "adTAeSCUenvAlarmInputLevel",
    "adTAeSCUenvAlarmUserName")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adTaControllerMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63)
)
if mibBuilder.loadTexts:
    adTaControllerMgmt.setRevisions(
        ("2021-07-20 15:40",
         "2021-06-30 00:00",
         "2016-06-13 00:00",
         "2013-10-23 11:39",
         "2013-10-17 13:55",
         "2013-10-15 15:00",
         "2013-05-03 15:00",
         "2012-06-19 15:00",
         "2011-07-18 16:39",
         "2011-06-30 00:00",
         "2011-05-09 12:56",
         "2016-11-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTaControllerMgmtTraps_ObjectIdentity = ObjectIdentity
adTaControllerMgmtTraps = _AdTaControllerMgmtTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0)
)
_AdTaSysCtrlShelf_ObjectIdentity = ObjectIdentity
adTaSysCtrlShelf = _AdTaSysCtrlShelf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30)
)
_AdTASysCtrlShelfTable_Object = MibTable
adTASysCtrlShelfTable = _AdTASysCtrlShelfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30, 3)
)
if mibBuilder.loadTexts:
    adTASysCtrlShelfTable.setStatus("current")
_AdTASysCtrlShelfEntry_Object = MibTableRow
adTASysCtrlShelfEntry = _AdTASysCtrlShelfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30, 3, 1)
)
adTASysCtrlShelfEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlShelfNumber"),
)
if mibBuilder.loadTexts:
    adTASysCtrlShelfEntry.setStatus("current")


class _AdTASysCtrlShelfNumber_Type(Integer32):
    """Custom type adTASysCtrlShelfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTASysCtrlShelfNumber_Type.__name__ = "Integer32"
_AdTASysCtrlShelfNumber_Object = MibTableColumn
adTASysCtrlShelfNumber = _AdTASysCtrlShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30, 3, 1, 1),
    _AdTASysCtrlShelfNumber_Type()
)
adTASysCtrlShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysCtrlShelfNumber.setStatus("current")


class _AdTASysCtrlModuleRemovedStatus_Type(OctetString):
    """Custom type adTASysCtrlModuleRemovedStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdTASysCtrlModuleRemovedStatus_Type.__name__ = "OctetString"
_AdTASysCtrlModuleRemovedStatus_Object = MibTableColumn
adTASysCtrlModuleRemovedStatus = _AdTASysCtrlModuleRemovedStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30, 3, 1, 2),
    _AdTASysCtrlModuleRemovedStatus_Type()
)
adTASysCtrlModuleRemovedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysCtrlModuleRemovedStatus.setStatus("current")


class _AdTASysCtrlAlarmSeverityLevel_Type(Integer32):
    """Custom type adTASysCtrlAlarmSeverityLevel based on Integer32"""
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
        *(("none", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTASysCtrlAlarmSeverityLevel_Type.__name__ = "Integer32"
_AdTASysCtrlAlarmSeverityLevel_Object = MibScalar
adTASysCtrlAlarmSeverityLevel = _AdTASysCtrlAlarmSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30, 4),
    _AdTASysCtrlAlarmSeverityLevel_Type()
)
adTASysCtrlAlarmSeverityLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysCtrlAlarmSeverityLevel.setStatus("deprecated")


class _AdTASysConfigurationChangeTimer_Type(Integer32):
    """Custom type adTASysConfigurationChangeTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AdTASysConfigurationChangeTimer_Type.__name__ = "Integer32"
_AdTASysConfigurationChangeTimer_Object = MibScalar
adTASysConfigurationChangeTimer = _AdTASysConfigurationChangeTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30, 6),
    _AdTASysConfigurationChangeTimer_Type()
)
adTASysConfigurationChangeTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysConfigurationChangeTimer.setStatus("current")
_AdTASysLastConfigChangeAlarmTime_Type = TimeTicks
_AdTASysLastConfigChangeAlarmTime_Object = MibScalar
adTASysLastConfigChangeAlarmTime = _AdTASysLastConfigChangeAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 30, 8),
    _AdTASysLastConfigChangeAlarmTime_Type()
)
adTASysLastConfigChangeAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysLastConfigChangeAlarmTime.setStatus("current")
_AdTaSysCtrlSlot_ObjectIdentity = ObjectIdentity
adTaSysCtrlSlot = _AdTaSysCtrlSlot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 40)
)
_AdTASysCtrlModuleTable_Object = MibTable
adTASysCtrlModuleTable = _AdTASysCtrlModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 40, 3)
)
if mibBuilder.loadTexts:
    adTASysCtrlModuleTable.setStatus("current")
_AdTASysCtrlModuleEntry_Object = MibTableRow
adTASysCtrlModuleEntry = _AdTASysCtrlModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 40, 3, 1)
)
adTASysCtrlModuleEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlModuleNumber"),
)
if mibBuilder.loadTexts:
    adTASysCtrlModuleEntry.setStatus("current")


class _AdTASysCtrlModuleNumber_Type(Integer32):
    """Custom type adTASysCtrlModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTASysCtrlModuleNumber_Type.__name__ = "Integer32"
_AdTASysCtrlModuleNumber_Object = MibTableColumn
adTASysCtrlModuleNumber = _AdTASysCtrlModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 40, 3, 1, 1),
    _AdTASysCtrlModuleNumber_Type()
)
adTASysCtrlModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysCtrlModuleNumber.setStatus("current")


class _AdTASysCtrlModuleDiscoveryStatus_Type(Integer32):
    """Custom type adTASysCtrlModuleDiscoveryStatus based on Integer32"""
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
        *(("empty", 1),
          ("discovering", 2),
          ("ok-no-rmd", 3),
          ("ok", 4),
          ("unresponsive", 5),
          ("unknown", 6))
    )


_AdTASysCtrlModuleDiscoveryStatus_Type.__name__ = "Integer32"
_AdTASysCtrlModuleDiscoveryStatus_Object = MibTableColumn
adTASysCtrlModuleDiscoveryStatus = _AdTASysCtrlModuleDiscoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 40, 3, 1, 2),
    _AdTASysCtrlModuleDiscoveryStatus_Type()
)
adTASysCtrlModuleDiscoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysCtrlModuleDiscoveryStatus.setStatus("current")
_AdTaSysCtrlScaMgmt_ObjectIdentity = ObjectIdentity
adTaSysCtrlScaMgmt = _AdTaSysCtrlScaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50)
)
_AdTaSysCtrlSCAConfigChangeVersion_Type = Counter32
_AdTaSysCtrlSCAConfigChangeVersion_Object = MibScalar
adTaSysCtrlSCAConfigChangeVersion = _AdTaSysCtrlSCAConfigChangeVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 3),
    _AdTaSysCtrlSCAConfigChangeVersion_Type()
)
adTaSysCtrlSCAConfigChangeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSCAConfigChangeVersion.setStatus("current")
_AdTaSysCtrlScaTable_Object = MibTable
adTaSysCtrlScaTable = _AdTaSysCtrlScaTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 20)
)
if mibBuilder.loadTexts:
    adTaSysCtrlScaTable.setStatus("current")
_AdTaSysCtrlScaEntry_Object = MibTableRow
adTaSysCtrlScaEntry = _AdTaSysCtrlScaEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 20, 1)
)
adTaSysCtrlScaEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlCUShelfNumber"),
)
if mibBuilder.loadTexts:
    adTaSysCtrlScaEntry.setStatus("current")


class _AdTaSysCtrlCUShelfNumber_Type(Integer32):
    """Custom type adTaSysCtrlCUShelfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_AdTaSysCtrlCUShelfNumber_Type.__name__ = "Integer32"
_AdTaSysCtrlCUShelfNumber_Object = MibTableColumn
adTaSysCtrlCUShelfNumber = _AdTaSysCtrlCUShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 20, 1, 1),
    _AdTaSysCtrlCUShelfNumber_Type()
)
adTaSysCtrlCUShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlCUShelfNumber.setStatus("current")


class _AdTaSysCtrlSCAProvItemChanged_Type(OctetString):
    """Custom type adTaSysCtrlSCAProvItemChanged based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlSCAProvItemChanged_Type.__name__ = "OctetString"
_AdTaSysCtrlSCAProvItemChanged_Object = MibTableColumn
adTaSysCtrlSCAProvItemChanged = _AdTaSysCtrlSCAProvItemChanged_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 20, 1, 5),
    _AdTaSysCtrlSCAProvItemChanged_Type()
)
adTaSysCtrlSCAProvItemChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSCAProvItemChanged.setStatus("current")


class _AdTaSysCtrlSCAPresentCards_Type(OctetString):
    """Custom type adTaSysCtrlSCAPresentCards based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlSCAPresentCards_Type.__name__ = "OctetString"
_AdTaSysCtrlSCAPresentCards_Object = MibTableColumn
adTaSysCtrlSCAPresentCards = _AdTaSysCtrlSCAPresentCards_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 20, 1, 7),
    _AdTaSysCtrlSCAPresentCards_Type()
)
adTaSysCtrlSCAPresentCards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSCAPresentCards.setStatus("current")


class _AdTaSysCtrlSCASlotsWithProvData_Type(OctetString):
    """Custom type adTaSysCtrlSCASlotsWithProvData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlSCASlotsWithProvData_Type.__name__ = "OctetString"
_AdTaSysCtrlSCASlotsWithProvData_Object = MibTableColumn
adTaSysCtrlSCASlotsWithProvData = _AdTaSysCtrlSCASlotsWithProvData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 20, 1, 9),
    _AdTaSysCtrlSCASlotsWithProvData_Type()
)
adTaSysCtrlSCASlotsWithProvData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSCASlotsWithProvData.setStatus("current")


class _AdTaSysCtrlSCAoptRestoreCardBitmask_Type(OctetString):
    """Custom type adTaSysCtrlSCAoptRestoreCardBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlSCAoptRestoreCardBitmask_Type.__name__ = "OctetString"
_AdTaSysCtrlSCAoptRestoreCardBitmask_Object = MibTableColumn
adTaSysCtrlSCAoptRestoreCardBitmask = _AdTaSysCtrlSCAoptRestoreCardBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 50, 20, 1, 11),
    _AdTaSysCtrlSCAoptRestoreCardBitmask_Type()
)
adTaSysCtrlSCAoptRestoreCardBitmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSCAoptRestoreCardBitmask.setStatus("current")
_AdTaSysCtrlProvMgmt_ObjectIdentity = ObjectIdentity
adTaSysCtrlProvMgmt = _AdTaSysCtrlProvMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 60)
)


class _AdTATIDSysNameSyncEnable_Type(Integer32):
    """Custom type adTATIDSysNameSyncEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTATIDSysNameSyncEnable_Type.__name__ = "Integer32"
_AdTATIDSysNameSyncEnable_Object = MibScalar
adTATIDSysNameSyncEnable = _AdTATIDSysNameSyncEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 60, 10),
    _AdTATIDSysNameSyncEnable_Type()
)
adTATIDSysNameSyncEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTATIDSysNameSyncEnable.setStatus("current")


class _AdTATL1echoEnable_Type(Integer32):
    """Custom type adTATL1echoEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTATL1echoEnable_Type.__name__ = "Integer32"
_AdTATL1echoEnable_Object = MibScalar
adTATL1echoEnable = _AdTATL1echoEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 60, 11),
    _AdTATL1echoEnable_Type()
)
adTATL1echoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTATL1echoEnable.setStatus("current")


class _AdTATL1PortExchange_Type(Integer32):
    """Custom type adTATL1PortExchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exchange", 1)
    )


_AdTATL1PortExchange_Type.__name__ = "Integer32"
_AdTATL1PortExchange_Object = MibScalar
adTATL1PortExchange = _AdTATL1PortExchange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 60, 12),
    _AdTATL1PortExchange_Type()
)
adTATL1PortExchange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTATL1PortExchange.setStatus("current")
_AdTAScmEthernetInterfaceModeTable_Object = MibTable
adTAScmEthernetInterfaceModeTable = _AdTAScmEthernetInterfaceModeTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 60, 13)
)
if mibBuilder.loadTexts:
    adTAScmEthernetInterfaceModeTable.setStatus("current")
_AdTAScmEthernetInterfaceModeEntry_Object = MibTableRow
adTAScmEthernetInterfaceModeEntry = _AdTAScmEthernetInterfaceModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 60, 13, 1)
)
adTAScmEthernetInterfaceModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adTAScmEthernetInterfaceModeEntry.setStatus("current")


class _AdTAScmEthernetInterfaceMode_Type(Integer32):
    """Custom type adTAScmEthernetInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ethercraft", 1),
          ("ethernet", 2))
    )


_AdTAScmEthernetInterfaceMode_Type.__name__ = "Integer32"
_AdTAScmEthernetInterfaceMode_Object = MibTableColumn
adTAScmEthernetInterfaceMode = _AdTAScmEthernetInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 60, 13, 1, 1),
    _AdTAScmEthernetInterfaceMode_Type()
)
adTAScmEthernetInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTAScmEthernetInterfaceMode.setStatus("current")
_AdTaSysCtrlPowerShed_ObjectIdentity = ObjectIdentity
adTaSysCtrlPowerShed = _AdTaSysCtrlPowerShed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70)
)


class _AdTASysCtrlPowerShedEnable_Type(Integer32):
    """Custom type adTASysCtrlPowerShedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTASysCtrlPowerShedEnable_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedEnable_Object = MibScalar
adTASysCtrlPowerShedEnable = _AdTASysCtrlPowerShedEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 10),
    _AdTASysCtrlPowerShedEnable_Type()
)
adTASysCtrlPowerShedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedEnable.setStatus("current")


class _AdTASysCtrlPowerShedAlmInput_Type(Integer32):
    """Custom type adTASysCtrlPowerShedAlmInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 18),
    )


_AdTASysCtrlPowerShedAlmInput_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedAlmInput_Object = MibScalar
adTASysCtrlPowerShedAlmInput = _AdTASysCtrlPowerShedAlmInput_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 11),
    _AdTASysCtrlPowerShedAlmInput_Type()
)
adTASysCtrlPowerShedAlmInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedAlmInput.setStatus("current")


class _AdTASysCtrlPowerShedActivateDelay_Type(Integer32):
    """Custom type adTASysCtrlPowerShedActivateDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AdTASysCtrlPowerShedActivateDelay_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedActivateDelay_Object = MibScalar
adTASysCtrlPowerShedActivateDelay = _AdTASysCtrlPowerShedActivateDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 12),
    _AdTASysCtrlPowerShedActivateDelay_Type()
)
adTASysCtrlPowerShedActivateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedActivateDelay.setStatus("current")


class _AdTASysCtrlPowerShedDeActivateDelay_Type(Integer32):
    """Custom type adTASysCtrlPowerShedDeActivateDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1440),
    )


_AdTASysCtrlPowerShedDeActivateDelay_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedDeActivateDelay_Object = MibScalar
adTASysCtrlPowerShedDeActivateDelay = _AdTASysCtrlPowerShedDeActivateDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 13),
    _AdTASysCtrlPowerShedDeActivateDelay_Type()
)
adTASysCtrlPowerShedDeActivateDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedDeActivateDelay.setStatus("current")


class _AdTASysCtrlPowerShedACFailAlarmDescription_Type(DisplayString):
    """Custom type adTASysCtrlPowerShedACFailAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AdTASysCtrlPowerShedACFailAlarmDescription_Type.__name__ = "DisplayString"
_AdTASysCtrlPowerShedACFailAlarmDescription_Object = MibScalar
adTASysCtrlPowerShedACFailAlarmDescription = _AdTASysCtrlPowerShedACFailAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 14),
    _AdTASysCtrlPowerShedACFailAlarmDescription_Type()
)
adTASysCtrlPowerShedACFailAlarmDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedACFailAlarmDescription.setStatus("current")


class _AdTASysCtrlPowerShedACFailAlarmSeverity_Type(Integer32):
    """Custom type adTASysCtrlPowerShedACFailAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTASysCtrlPowerShedACFailAlarmSeverity_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedACFailAlarmSeverity_Object = MibScalar
adTASysCtrlPowerShedACFailAlarmSeverity = _AdTASysCtrlPowerShedACFailAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 15),
    _AdTASysCtrlPowerShedACFailAlarmSeverity_Type()
)
adTASysCtrlPowerShedACFailAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedACFailAlarmSeverity.setStatus("current")


class _AdTASysCtrlPowerShedACFailAlarmAIDIndex_Type(Integer32):
    """Custom type adTASysCtrlPowerShedACFailAlarmAIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_AdTASysCtrlPowerShedACFailAlarmAIDIndex_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedACFailAlarmAIDIndex_Object = MibScalar
adTASysCtrlPowerShedACFailAlarmAIDIndex = _AdTASysCtrlPowerShedACFailAlarmAIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 16),
    _AdTASysCtrlPowerShedACFailAlarmAIDIndex_Type()
)
adTASysCtrlPowerShedACFailAlarmAIDIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedACFailAlarmAIDIndex.setStatus("current")


class _AdTASysCtrlPowerShedACFailAlarmConditionCode_Type(DisplayString):
    """Custom type adTASysCtrlPowerShedACFailAlarmConditionCode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 11),
    )


_AdTASysCtrlPowerShedACFailAlarmConditionCode_Type.__name__ = "DisplayString"
_AdTASysCtrlPowerShedACFailAlarmConditionCode_Object = MibScalar
adTASysCtrlPowerShedACFailAlarmConditionCode = _AdTASysCtrlPowerShedACFailAlarmConditionCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 17),
    _AdTASysCtrlPowerShedACFailAlarmConditionCode_Type()
)
adTASysCtrlPowerShedACFailAlarmConditionCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedACFailAlarmConditionCode.setStatus("current")


class _AdTASysCtrlPowerShedStatus_Type(Integer32):
    """Custom type adTASysCtrlPowerShedStatus based on Integer32"""
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
        *(("inactive", 1),
          ("inactiveWaitingToActivate", 2),
          ("active", 3),
          ("activeWaitingToDeactivate", 4))
    )


_AdTASysCtrlPowerShedStatus_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedStatus_Object = MibScalar
adTASysCtrlPowerShedStatus = _AdTASysCtrlPowerShedStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 30),
    _AdTASysCtrlPowerShedStatus_Type()
)
adTASysCtrlPowerShedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedStatus.setStatus("current")


class _AdTASysCtrlPowerShedCountDown_Type(Integer32):
    """Custom type adTASysCtrlPowerShedCountDown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AdTASysCtrlPowerShedCountDown_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedCountDown_Object = MibScalar
adTASysCtrlPowerShedCountDown = _AdTASysCtrlPowerShedCountDown_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 31),
    _AdTASysCtrlPowerShedCountDown_Type()
)
adTASysCtrlPowerShedCountDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedCountDown.setStatus("current")


class _AdTASysCtrlPowerShedStateAlarmSeverity_Type(Integer32):
    """Custom type adTASysCtrlPowerShedStateAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdTASysCtrlPowerShedStateAlarmSeverity_Type.__name__ = "Integer32"
_AdTASysCtrlPowerShedStateAlarmSeverity_Object = MibScalar
adTASysCtrlPowerShedStateAlarmSeverity = _AdTASysCtrlPowerShedStateAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 32),
    _AdTASysCtrlPowerShedStateAlarmSeverity_Type()
)
adTASysCtrlPowerShedStateAlarmSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedStateAlarmSeverity.setStatus("current")
_AdTASysCtrlPowerShedRemoteServerIP_Type = IpAddress
_AdTASysCtrlPowerShedRemoteServerIP_Object = MibScalar
adTASysCtrlPowerShedRemoteServerIP = _AdTASysCtrlPowerShedRemoteServerIP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 70, 33),
    _AdTASysCtrlPowerShedRemoteServerIP_Type()
)
adTASysCtrlPowerShedRemoteServerIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASysCtrlPowerShedRemoteServerIP.setStatus("current")
_AdTaSysCtrlSysSSHMgmt_ObjectIdentity = ObjectIdentity
adTaSysCtrlSysSSHMgmt = _AdTaSysCtrlSysSSHMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80)
)
_AdTaSysCtrlSysSshKeyMgmt_ObjectIdentity = ObjectIdentity
adTaSysCtrlSysSshKeyMgmt = _AdTaSysCtrlSysSshKeyMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80, 10)
)


class _AdTaSysCtrlCurrentKeySize_Type(Integer32):
    """Custom type adTaSysCtrlCurrentKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_AdTaSysCtrlCurrentKeySize_Type.__name__ = "Integer32"
_AdTaSysCtrlCurrentKeySize_Object = MibScalar
adTaSysCtrlCurrentKeySize = _AdTaSysCtrlCurrentKeySize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80, 10, 1),
    _AdTaSysCtrlCurrentKeySize_Type()
)
adTaSysCtrlCurrentKeySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlCurrentKeySize.setStatus("current")


class _AdTaSysCtrlKeySize_Type(Integer32):
    """Custom type adTaSysCtrlKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 2048),
    )


_AdTaSysCtrlKeySize_Type.__name__ = "Integer32"
_AdTaSysCtrlKeySize_Object = MibScalar
adTaSysCtrlKeySize = _AdTaSysCtrlKeySize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80, 10, 2),
    _AdTaSysCtrlKeySize_Type()
)
adTaSysCtrlKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlKeySize.setStatus("current")


class _AdTaSysCtrlGenerateKeys_Type(Integer32):
    """Custom type adTaSysCtrlGenerateKeys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTaSysCtrlGenerateKeys_Type.__name__ = "Integer32"
_AdTaSysCtrlGenerateKeys_Object = MibScalar
adTaSysCtrlGenerateKeys = _AdTaSysCtrlGenerateKeys_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80, 10, 15),
    _AdTaSysCtrlGenerateKeys_Type()
)
adTaSysCtrlGenerateKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlGenerateKeys.setStatus("current")


class _AdTaSysCtrlGenKeyStatus_Type(Integer32):
    """Custom type adTaSysCtrlGenKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_AdTaSysCtrlGenKeyStatus_Type.__name__ = "Integer32"
_AdTaSysCtrlGenKeyStatus_Object = MibScalar
adTaSysCtrlGenKeyStatus = _AdTaSysCtrlGenKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80, 10, 16),
    _AdTaSysCtrlGenKeyStatus_Type()
)
adTaSysCtrlGenKeyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlGenKeyStatus.setStatus("current")


class _AdTaSysCtrlReKeyTimeout_Type(Integer32):
    """Custom type adTaSysCtrlReKeyTimeout based on Integer32"""
    defaultValue = 480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_AdTaSysCtrlReKeyTimeout_Type.__name__ = "Integer32"
_AdTaSysCtrlReKeyTimeout_Object = MibScalar
adTaSysCtrlReKeyTimeout = _AdTaSysCtrlReKeyTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80, 10, 20),
    _AdTaSysCtrlReKeyTimeout_Type()
)
adTaSysCtrlReKeyTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlReKeyTimeout.setStatus("current")


class _AdTaSysCtrlReKeyDataLimit_Type(Integer32):
    """Custom type adTaSysCtrlReKeyDataLimit based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_AdTaSysCtrlReKeyDataLimit_Type.__name__ = "Integer32"
_AdTaSysCtrlReKeyDataLimit_Object = MibScalar
adTaSysCtrlReKeyDataLimit = _AdTaSysCtrlReKeyDataLimit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 80, 10, 21),
    _AdTaSysCtrlReKeyDataLimit_Type()
)
adTaSysCtrlReKeyDataLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlReKeyDataLimit.setStatus("current")
_AdTaSysCtrlSysRlsMgmt_ObjectIdentity = ObjectIdentity
adTaSysCtrlSysRlsMgmt = _AdTaSysCtrlSysRlsMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90)
)
_AdTaSysCtrlSysRlsTable_Object = MibTable
adTaSysCtrlSysRlsTable = _AdTaSysCtrlSysRlsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1)
)
if mibBuilder.loadTexts:
    adTaSysCtrlSysRlsTable.setStatus("current")
_AdTaSysCtrlSysRlsEntry_Object = MibTableRow
adTaSysCtrlSysRlsEntry = _AdTaSysCtrlSysRlsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1)
)
adTaSysCtrlSysRlsEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseIndex"),
)
if mibBuilder.loadTexts:
    adTaSysCtrlSysRlsEntry.setStatus("current")


class _AdTaSysCtrlSrmReleaseIndex_Type(Integer32):
    """Custom type adTaSysCtrlSrmReleaseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AdTaSysCtrlSrmReleaseIndex_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmReleaseIndex_Object = MibTableColumn
adTaSysCtrlSrmReleaseIndex = _AdTaSysCtrlSrmReleaseIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 1),
    _AdTaSysCtrlSrmReleaseIndex_Type()
)
adTaSysCtrlSrmReleaseIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseIndex.setStatus("current")


class _AdTaSysCtrlSrmReleaseName_Type(DisplayString):
    """Custom type adTaSysCtrlSrmReleaseName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSysCtrlSrmReleaseName_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmReleaseName_Object = MibTableColumn
adTaSysCtrlSrmReleaseName = _AdTaSysCtrlSrmReleaseName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 2),
    _AdTaSysCtrlSrmReleaseName_Type()
)
adTaSysCtrlSrmReleaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseName.setStatus("current")


class _AdTaSysCtrlSrmReleaseFilename_Type(DisplayString):
    """Custom type adTaSysCtrlSrmReleaseFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdTaSysCtrlSrmReleaseFilename_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmReleaseFilename_Object = MibTableColumn
adTaSysCtrlSrmReleaseFilename = _AdTaSysCtrlSrmReleaseFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 3),
    _AdTaSysCtrlSrmReleaseFilename_Type()
)
adTaSysCtrlSrmReleaseFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseFilename.setStatus("current")


class _AdTaSysCtrlSrmReleaseStatus_Type(DisplayString):
    """Custom type adTaSysCtrlSrmReleaseStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSysCtrlSrmReleaseStatus_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmReleaseStatus_Object = MibTableColumn
adTaSysCtrlSrmReleaseStatus = _AdTaSysCtrlSrmReleaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 4),
    _AdTaSysCtrlSrmReleaseStatus_Type()
)
adTaSysCtrlSrmReleaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseStatus.setStatus("current")
_AdTaSysCtrlSrmReleaseMemoryUsageKB_Type = Integer32
_AdTaSysCtrlSrmReleaseMemoryUsageKB_Object = MibTableColumn
adTaSysCtrlSrmReleaseMemoryUsageKB = _AdTaSysCtrlSrmReleaseMemoryUsageKB_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 5),
    _AdTaSysCtrlSrmReleaseMemoryUsageKB_Type()
)
adTaSysCtrlSrmReleaseMemoryUsageKB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseMemoryUsageKB.setStatus("current")
_AdTaSysCtrlSrmReleaseFileCount_Type = Integer32
_AdTaSysCtrlSrmReleaseFileCount_Object = MibTableColumn
adTaSysCtrlSrmReleaseFileCount = _AdTaSysCtrlSrmReleaseFileCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 6),
    _AdTaSysCtrlSrmReleaseFileCount_Type()
)
adTaSysCtrlSrmReleaseFileCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseFileCount.setStatus("current")
_AdTaSysCtrlSrmReleaseProductCount_Type = Integer32
_AdTaSysCtrlSrmReleaseProductCount_Object = MibTableColumn
adTaSysCtrlSrmReleaseProductCount = _AdTaSysCtrlSrmReleaseProductCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 7),
    _AdTaSysCtrlSrmReleaseProductCount_Type()
)
adTaSysCtrlSrmReleaseProductCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseProductCount.setStatus("current")
_AdTaSysCtrlSrmReleaseFilesTableEntries_Type = Integer32
_AdTaSysCtrlSrmReleaseFilesTableEntries_Object = MibTableColumn
adTaSysCtrlSrmReleaseFilesTableEntries = _AdTaSysCtrlSrmReleaseFilesTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 8),
    _AdTaSysCtrlSrmReleaseFilesTableEntries_Type()
)
adTaSysCtrlSrmReleaseFilesTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseFilesTableEntries.setStatus("current")
_AdTaSysCtrlSrmReleaseErrorBitmask_Type = Integer32
_AdTaSysCtrlSrmReleaseErrorBitmask_Object = MibTableColumn
adTaSysCtrlSrmReleaseErrorBitmask = _AdTaSysCtrlSrmReleaseErrorBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 1, 1, 9),
    _AdTaSysCtrlSrmReleaseErrorBitmask_Type()
)
adTaSysCtrlSrmReleaseErrorBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmReleaseErrorBitmask.setStatus("current")
_AdTaSysCtrlSysRlsFilesTable_Object = MibTable
adTaSysCtrlSysRlsFilesTable = _AdTaSysCtrlSysRlsFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 2)
)
if mibBuilder.loadTexts:
    adTaSysCtrlSysRlsFilesTable.setStatus("current")
_AdTaSysCtrlSysRlsFilesEntry_Object = MibTableRow
adTaSysCtrlSysRlsFilesEntry = _AdTaSysCtrlSysRlsFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 2, 1)
)
adTaSysCtrlSysRlsFilesEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseIndex"),
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmRlsFilesIndex"),
)
if mibBuilder.loadTexts:
    adTaSysCtrlSysRlsFilesEntry.setStatus("current")
_AdTaSysCtrlSrmRlsFilesIndex_Type = Integer32
_AdTaSysCtrlSrmRlsFilesIndex_Object = MibTableColumn
adTaSysCtrlSrmRlsFilesIndex = _AdTaSysCtrlSrmRlsFilesIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 2, 1, 1),
    _AdTaSysCtrlSrmRlsFilesIndex_Type()
)
adTaSysCtrlSrmRlsFilesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmRlsFilesIndex.setStatus("current")


class _AdTaSysCtrlSrmRlsFilesInfo_Type(DisplayString):
    """Custom type adTaSysCtrlSrmRlsFilesInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdTaSysCtrlSrmRlsFilesInfo_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmRlsFilesInfo_Object = MibTableColumn
adTaSysCtrlSrmRlsFilesInfo = _AdTaSysCtrlSrmRlsFilesInfo_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 2, 1, 2),
    _AdTaSysCtrlSrmRlsFilesInfo_Type()
)
adTaSysCtrlSrmRlsFilesInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmRlsFilesInfo.setStatus("current")


class _AdTaSysCtrlSrmCancel_Type(Integer32):
    """Custom type adTaSysCtrlSrmCancel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("cancelSrmCommand", 1)
    )


_AdTaSysCtrlSrmCancel_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmCancel_Object = MibScalar
adTaSysCtrlSrmCancel = _AdTaSysCtrlSrmCancel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 10),
    _AdTaSysCtrlSrmCancel_Type()
)
adTaSysCtrlSrmCancel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmCancel.setStatus("current")


class _AdTaSysCtrlSrmActivateBrls_Type(Integer32):
    """Custom type adTaSysCtrlSrmActivateBrls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("activateBackupRls", 1)
    )


_AdTaSysCtrlSrmActivateBrls_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmActivateBrls_Object = MibScalar
adTaSysCtrlSrmActivateBrls = _AdTaSysCtrlSrmActivateBrls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 11),
    _AdTaSysCtrlSrmActivateBrls_Type()
)
adTaSysCtrlSrmActivateBrls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmActivateBrls.setStatus("current")


class _AdTaSysCtrlSrmBackupArls_Type(Integer32):
    """Custom type adTaSysCtrlSrmBackupArls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("backupActiveRls", 1)
    )


_AdTaSysCtrlSrmBackupArls_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmBackupArls_Object = MibScalar
adTaSysCtrlSrmBackupArls = _AdTaSysCtrlSrmBackupArls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 12),
    _AdTaSysCtrlSrmBackupArls_Type()
)
adTaSysCtrlSrmBackupArls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmBackupArls.setStatus("current")


class _AdTaSysCtrlSrmDownloadInitiate_Type(Integer32):
    """Custom type adTaSysCtrlSrmDownloadInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiateSrmDownload", 1)
    )


_AdTaSysCtrlSrmDownloadInitiate_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmDownloadInitiate_Object = MibScalar
adTaSysCtrlSrmDownloadInitiate = _AdTaSysCtrlSrmDownloadInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 13),
    _AdTaSysCtrlSrmDownloadInitiate_Type()
)
adTaSysCtrlSrmDownloadInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmDownloadInitiate.setStatus("current")


class _AdTaSysCtrlSrmDownloadSameFiles_Type(Integer32):
    """Custom type adTaSysCtrlSrmDownloadSameFiles based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSrmDownloadSameFiles_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmDownloadSameFiles_Object = MibScalar
adTaSysCtrlSrmDownloadSameFiles = _AdTaSysCtrlSrmDownloadSameFiles_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 14),
    _AdTaSysCtrlSrmDownloadSameFiles_Type()
)
adTaSysCtrlSrmDownloadSameFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmDownloadSameFiles.setStatus("current")


class _AdTaSysCtrlSrmDownloadRetries_Type(Integer32):
    """Custom type adTaSysCtrlSrmDownloadRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AdTaSysCtrlSrmDownloadRetries_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmDownloadRetries_Object = MibScalar
adTaSysCtrlSrmDownloadRetries = _AdTaSysCtrlSrmDownloadRetries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 15),
    _AdTaSysCtrlSrmDownloadRetries_Type()
)
adTaSysCtrlSrmDownloadRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmDownloadRetries.setStatus("current")


class _AdTaSysCtrlSrmDownloadFilename_Type(DisplayString):
    """Custom type adTaSysCtrlSrmDownloadFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AdTaSysCtrlSrmDownloadFilename_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmDownloadFilename_Object = MibScalar
adTaSysCtrlSrmDownloadFilename = _AdTaSysCtrlSrmDownloadFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 16),
    _AdTaSysCtrlSrmDownloadFilename_Type()
)
adTaSysCtrlSrmDownloadFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmDownloadFilename.setStatus("current")


class _AdTaSysCtrlSrmDownloadBasepath_Type(DisplayString):
    """Custom type adTaSysCtrlSrmDownloadBasepath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSysCtrlSrmDownloadBasepath_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmDownloadBasepath_Object = MibScalar
adTaSysCtrlSrmDownloadBasepath = _AdTaSysCtrlSrmDownloadBasepath_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 17),
    _AdTaSysCtrlSrmDownloadBasepath_Type()
)
adTaSysCtrlSrmDownloadBasepath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmDownloadBasepath.setStatus("current")


class _AdTaSysCtrlSrmScheduledDownload_Type(DisplayString):
    """Custom type adTaSysCtrlSrmScheduledDownload based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AdTaSysCtrlSrmScheduledDownload_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmScheduledDownload_Object = MibScalar
adTaSysCtrlSrmScheduledDownload = _AdTaSysCtrlSrmScheduledDownload_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 18),
    _AdTaSysCtrlSrmScheduledDownload_Type()
)
adTaSysCtrlSrmScheduledDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmScheduledDownload.setStatus("current")


class _AdTaSysCtrlSrmScheduledActivate_Type(DisplayString):
    """Custom type adTaSysCtrlSrmScheduledActivate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 14),
    )


_AdTaSysCtrlSrmScheduledActivate_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmScheduledActivate_Object = MibScalar
adTaSysCtrlSrmScheduledActivate = _AdTaSysCtrlSrmScheduledActivate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 19),
    _AdTaSysCtrlSrmScheduledActivate_Type()
)
adTaSysCtrlSrmScheduledActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmScheduledActivate.setStatus("current")


class _AdTaSysCtrlSrmValidateInterval_Type(Integer32):
    """Custom type adTaSysCtrlSrmValidateInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 365),
    )


_AdTaSysCtrlSrmValidateInterval_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmValidateInterval_Object = MibScalar
adTaSysCtrlSrmValidateInterval = _AdTaSysCtrlSrmValidateInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 20),
    _AdTaSysCtrlSrmValidateInterval_Type()
)
adTaSysCtrlSrmValidateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmValidateInterval.setStatus("current")


class _AdTaSysCtrlSrmStatus_Type(DisplayString):
    """Custom type adTaSysCtrlSrmStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSysCtrlSrmStatus_Type.__name__ = "DisplayString"
_AdTaSysCtrlSrmStatus_Object = MibScalar
adTaSysCtrlSrmStatus = _AdTaSysCtrlSrmStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 21),
    _AdTaSysCtrlSrmStatus_Type()
)
adTaSysCtrlSrmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmStatus.setStatus("current")


class _AdTaSysCtrlSrmAutoUpgradeCtrl_Type(Integer32):
    """Custom type adTaSysCtrlSrmAutoUpgradeCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSrmAutoUpgradeCtrl_Type.__name__ = "Integer32"
_AdTaSysCtrlSrmAutoUpgradeCtrl_Object = MibScalar
adTaSysCtrlSrmAutoUpgradeCtrl = _AdTaSysCtrlSrmAutoUpgradeCtrl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 90, 22),
    _AdTaSysCtrlSrmAutoUpgradeCtrl_Type()
)
adTaSysCtrlSrmAutoUpgradeCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSrmAutoUpgradeCtrl.setStatus("current")
_AdTaSysCtrlAutoUpgrade_ObjectIdentity = ObjectIdentity
adTaSysCtrlAutoUpgrade = _AdTaSysCtrlAutoUpgrade_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100)
)


class _AdTaSysCtrlAutoUpgradeActiveSlots_Type(DisplayString):
    """Custom type adTaSysCtrlAutoUpgradeActiveSlots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSysCtrlAutoUpgradeActiveSlots_Type.__name__ = "DisplayString"
_AdTaSysCtrlAutoUpgradeActiveSlots_Object = MibScalar
adTaSysCtrlAutoUpgradeActiveSlots = _AdTaSysCtrlAutoUpgradeActiveSlots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 1),
    _AdTaSysCtrlAutoUpgradeActiveSlots_Type()
)
adTaSysCtrlAutoUpgradeActiveSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeActiveSlots.setStatus("current")


class _AdTaSysCtrlAutoUpgradeErrorSlots_Type(DisplayString):
    """Custom type adTaSysCtrlAutoUpgradeErrorSlots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSysCtrlAutoUpgradeErrorSlots_Type.__name__ = "DisplayString"
_AdTaSysCtrlAutoUpgradeErrorSlots_Object = MibScalar
adTaSysCtrlAutoUpgradeErrorSlots = _AdTaSysCtrlAutoUpgradeErrorSlots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 2),
    _AdTaSysCtrlAutoUpgradeErrorSlots_Type()
)
adTaSysCtrlAutoUpgradeErrorSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeErrorSlots.setStatus("current")


class _AdTaSysCtrlAutoUpgradeNeededSlots_Type(DisplayString):
    """Custom type adTaSysCtrlAutoUpgradeNeededSlots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSysCtrlAutoUpgradeNeededSlots_Type.__name__ = "DisplayString"
_AdTaSysCtrlAutoUpgradeNeededSlots_Object = MibScalar
adTaSysCtrlAutoUpgradeNeededSlots = _AdTaSysCtrlAutoUpgradeNeededSlots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 3),
    _AdTaSysCtrlAutoUpgradeNeededSlots_Type()
)
adTaSysCtrlAutoUpgradeNeededSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeNeededSlots.setStatus("current")


class _AdTaSysCtrlAutoUpgradeDeferredResetSlots_Type(DisplayString):
    """Custom type adTaSysCtrlAutoUpgradeDeferredResetSlots based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSysCtrlAutoUpgradeDeferredResetSlots_Type.__name__ = "DisplayString"
_AdTaSysCtrlAutoUpgradeDeferredResetSlots_Object = MibScalar
adTaSysCtrlAutoUpgradeDeferredResetSlots = _AdTaSysCtrlAutoUpgradeDeferredResetSlots_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 4),
    _AdTaSysCtrlAutoUpgradeDeferredResetSlots_Type()
)
adTaSysCtrlAutoUpgradeDeferredResetSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeDeferredResetSlots.setStatus("current")


class _AdTaSysCtrlAutoUpgradeActiveSlotsBitmask_Type(OctetString):
    """Custom type adTaSysCtrlAutoUpgradeActiveSlotsBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlAutoUpgradeActiveSlotsBitmask_Type.__name__ = "OctetString"
_AdTaSysCtrlAutoUpgradeActiveSlotsBitmask_Object = MibScalar
adTaSysCtrlAutoUpgradeActiveSlotsBitmask = _AdTaSysCtrlAutoUpgradeActiveSlotsBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 5),
    _AdTaSysCtrlAutoUpgradeActiveSlotsBitmask_Type()
)
adTaSysCtrlAutoUpgradeActiveSlotsBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeActiveSlotsBitmask.setStatus("current")


class _AdTaSysCtrlAutoUpgradeErrorSlotsBitmask_Type(OctetString):
    """Custom type adTaSysCtrlAutoUpgradeErrorSlotsBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlAutoUpgradeErrorSlotsBitmask_Type.__name__ = "OctetString"
_AdTaSysCtrlAutoUpgradeErrorSlotsBitmask_Object = MibScalar
adTaSysCtrlAutoUpgradeErrorSlotsBitmask = _AdTaSysCtrlAutoUpgradeErrorSlotsBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 6),
    _AdTaSysCtrlAutoUpgradeErrorSlotsBitmask_Type()
)
adTaSysCtrlAutoUpgradeErrorSlotsBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeErrorSlotsBitmask.setStatus("current")


class _AdTaSysCtrlAutoUpgradeNeededSlotsBitmask_Type(OctetString):
    """Custom type adTaSysCtrlAutoUpgradeNeededSlotsBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlAutoUpgradeNeededSlotsBitmask_Type.__name__ = "OctetString"
_AdTaSysCtrlAutoUpgradeNeededSlotsBitmask_Object = MibScalar
adTaSysCtrlAutoUpgradeNeededSlotsBitmask = _AdTaSysCtrlAutoUpgradeNeededSlotsBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 7),
    _AdTaSysCtrlAutoUpgradeNeededSlotsBitmask_Type()
)
adTaSysCtrlAutoUpgradeNeededSlotsBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeNeededSlotsBitmask.setStatus("current")


class _AdTaSysCtrlAutoUpgradeDeferResetSlotsBitmask_Type(OctetString):
    """Custom type adTaSysCtrlAutoUpgradeDeferResetSlotsBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlAutoUpgradeDeferResetSlotsBitmask_Type.__name__ = "OctetString"
_AdTaSysCtrlAutoUpgradeDeferResetSlotsBitmask_Object = MibScalar
adTaSysCtrlAutoUpgradeDeferResetSlotsBitmask = _AdTaSysCtrlAutoUpgradeDeferResetSlotsBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 8),
    _AdTaSysCtrlAutoUpgradeDeferResetSlotsBitmask_Type()
)
adTaSysCtrlAutoUpgradeDeferResetSlotsBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeDeferResetSlotsBitmask.setStatus("current")


class _AdTaSysCtrlAutoUpgradeUseSCR_Type(Integer32):
    """Custom type adTaSysCtrlAutoUpgradeUseSCR based on Integer32"""
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


_AdTaSysCtrlAutoUpgradeUseSCR_Type.__name__ = "Integer32"
_AdTaSysCtrlAutoUpgradeUseSCR_Object = MibScalar
adTaSysCtrlAutoUpgradeUseSCR = _AdTaSysCtrlAutoUpgradeUseSCR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 10),
    _AdTaSysCtrlAutoUpgradeUseSCR_Type()
)
adTaSysCtrlAutoUpgradeUseSCR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeUseSCR.setStatus("current")


class _AdTaSysCtrlAutoUpgradeSCRStatus_Type(Integer32):
    """Custom type adTaSysCtrlAutoUpgradeSCRStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("nonePending", 1),
          ("readyForSCR", 2),
          ("scrBusy", 3),
          ("auNeeded", 4),
          ("auBusy", 5),
          ("auErrors", 6),
          ("auNotUsingSCR", 7),
          ("noneWaitingForSCR", 8))
    )


_AdTaSysCtrlAutoUpgradeSCRStatus_Type.__name__ = "Integer32"
_AdTaSysCtrlAutoUpgradeSCRStatus_Object = MibScalar
adTaSysCtrlAutoUpgradeSCRStatus = _AdTaSysCtrlAutoUpgradeSCRStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 12),
    _AdTaSysCtrlAutoUpgradeSCRStatus_Type()
)
adTaSysCtrlAutoUpgradeSCRStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeSCRStatus.setStatus("current")


class _AdTaSysCtrlAutoUpgradeEOSSCapable_Type(Integer32):
    """Custom type adTaSysCtrlAutoUpgradeEOSSCapable based on Integer32"""
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


_AdTaSysCtrlAutoUpgradeEOSSCapable_Type.__name__ = "Integer32"
_AdTaSysCtrlAutoUpgradeEOSSCapable_Object = MibScalar
adTaSysCtrlAutoUpgradeEOSSCapable = _AdTaSysCtrlAutoUpgradeEOSSCapable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 30),
    _AdTaSysCtrlAutoUpgradeEOSSCapable_Type()
)
adTaSysCtrlAutoUpgradeEOSSCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeEOSSCapable.setStatus("current")


class _AdTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask_Type(OctetString):
    """Custom type adTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask_Type.__name__ = "OctetString"
_AdTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask_Object = MibScalar
adTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask = _AdTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 32),
    _AdTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask_Type()
)
adTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask.setStatus("current")


class _AdTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask_Type(OctetString):
    """Custom type adTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AdTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask_Type.__name__ = "OctetString"
_AdTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask_Object = MibScalar
adTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask = _AdTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 100, 34),
    _AdTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask_Type()
)
adTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask.setStatus("current")
_AdTaSysCtrlFileExport_ObjectIdentity = ObjectIdentity
adTaSysCtrlFileExport = _AdTaSysCtrlFileExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110)
)
_AdTaSysCtrlSystemLog_ObjectIdentity = ObjectIdentity
adTaSysCtrlSystemLog = _AdTaSysCtrlSystemLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1)
)


class _AdTASystemEventLogAutoExportMode_Type(Integer32):
    """Custom type adTASystemEventLogAutoExportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoExportAt90PercentFull", 1),
          ("autoExportAtScheduledTime", 2),
          ("autoExportDisabled", 3))
    )


_AdTASystemEventLogAutoExportMode_Type.__name__ = "Integer32"
_AdTASystemEventLogAutoExportMode_Object = MibScalar
adTASystemEventLogAutoExportMode = _AdTASystemEventLogAutoExportMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 1),
    _AdTASystemEventLogAutoExportMode_Type()
)
adTASystemEventLogAutoExportMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTASystemEventLogAutoExportMode.setStatus("current")


class _AdTaSystemEventLogPreventFileOverlap_Type(Integer32):
    """Custom type adTaSystemEventLogPreventFileOverlap based on Integer32"""
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


_AdTaSystemEventLogPreventFileOverlap_Type.__name__ = "Integer32"
_AdTaSystemEventLogPreventFileOverlap_Object = MibScalar
adTaSystemEventLogPreventFileOverlap = _AdTaSystemEventLogPreventFileOverlap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 3),
    _AdTaSystemEventLogPreventFileOverlap_Type()
)
adTaSystemEventLogPreventFileOverlap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogPreventFileOverlap.setStatus("current")


class _AdTaSystemEventLogFilePrefix_Type(DisplayString):
    """Custom type adTaSystemEventLogFilePrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdTaSystemEventLogFilePrefix_Type.__name__ = "DisplayString"
_AdTaSystemEventLogFilePrefix_Object = MibScalar
adTaSystemEventLogFilePrefix = _AdTaSystemEventLogFilePrefix_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 5),
    _AdTaSystemEventLogFilePrefix_Type()
)
adTaSystemEventLogFilePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogFilePrefix.setStatus("current")


class _AdTaSystemEventLogFileSuffix_Type(DisplayString):
    """Custom type adTaSystemEventLogFileSuffix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_AdTaSystemEventLogFileSuffix_Type.__name__ = "DisplayString"
_AdTaSystemEventLogFileSuffix_Object = MibScalar
adTaSystemEventLogFileSuffix = _AdTaSystemEventLogFileSuffix_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 7),
    _AdTaSystemEventLogFileSuffix_Type()
)
adTaSystemEventLogFileSuffix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogFileSuffix.setStatus("current")


class _AdTaSystemEventLogRemoteDirectory_Type(DisplayString):
    """Custom type adTaSystemEventLogRemoteDirectory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSystemEventLogRemoteDirectory_Type.__name__ = "DisplayString"
_AdTaSystemEventLogRemoteDirectory_Object = MibScalar
adTaSystemEventLogRemoteDirectory = _AdTaSystemEventLogRemoteDirectory_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 9),
    _AdTaSystemEventLogRemoteDirectory_Type()
)
adTaSystemEventLogRemoteDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogRemoteDirectory.setStatus("current")


class _AdTaSystemEventLogRemoteFileName_Type(DisplayString):
    """Custom type adTaSystemEventLogRemoteFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdTaSystemEventLogRemoteFileName_Type.__name__ = "DisplayString"
_AdTaSystemEventLogRemoteFileName_Object = MibScalar
adTaSystemEventLogRemoteFileName = _AdTaSystemEventLogRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 11),
    _AdTaSystemEventLogRemoteFileName_Type()
)
adTaSystemEventLogRemoteFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSystemEventLogRemoteFileName.setStatus("current")


class _AdTaSystemEventLogAutoExportNumberOfDays_Type(Integer32):
    """Custom type adTaSystemEventLogAutoExportNumberOfDays based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90),
    )


_AdTaSystemEventLogAutoExportNumberOfDays_Type.__name__ = "Integer32"
_AdTaSystemEventLogAutoExportNumberOfDays_Object = MibScalar
adTaSystemEventLogAutoExportNumberOfDays = _AdTaSystemEventLogAutoExportNumberOfDays_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 13),
    _AdTaSystemEventLogAutoExportNumberOfDays_Type()
)
adTaSystemEventLogAutoExportNumberOfDays.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogAutoExportNumberOfDays.setStatus("current")


class _AdTaSystemEventLogHourOfDayToExportSysLog_Type(Integer32):
    """Custom type adTaSystemEventLogHourOfDayToExportSysLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 23),
    )


_AdTaSystemEventLogHourOfDayToExportSysLog_Type.__name__ = "Integer32"
_AdTaSystemEventLogHourOfDayToExportSysLog_Object = MibScalar
adTaSystemEventLogHourOfDayToExportSysLog = _AdTaSystemEventLogHourOfDayToExportSysLog_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 15),
    _AdTaSystemEventLogHourOfDayToExportSysLog_Type()
)
adTaSystemEventLogHourOfDayToExportSysLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogHourOfDayToExportSysLog.setStatus("current")


class _AdTaSystemEventLogMinuteOfDayToExportSysLog_Type(Integer32):
    """Custom type adTaSystemEventLogMinuteOfDayToExportSysLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AdTaSystemEventLogMinuteOfDayToExportSysLog_Type.__name__ = "Integer32"
_AdTaSystemEventLogMinuteOfDayToExportSysLog_Object = MibScalar
adTaSystemEventLogMinuteOfDayToExportSysLog = _AdTaSystemEventLogMinuteOfDayToExportSysLog_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 17),
    _AdTaSystemEventLogMinuteOfDayToExportSysLog_Type()
)
adTaSystemEventLogMinuteOfDayToExportSysLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogMinuteOfDayToExportSysLog.setStatus("current")


class _AdTaSystemEventLogExportRetries_Type(Integer32):
    """Custom type adTaSystemEventLogExportRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AdTaSystemEventLogExportRetries_Type.__name__ = "Integer32"
_AdTaSystemEventLogExportRetries_Object = MibScalar
adTaSystemEventLogExportRetries = _AdTaSystemEventLogExportRetries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 19),
    _AdTaSystemEventLogExportRetries_Type()
)
adTaSystemEventLogExportRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogExportRetries.setStatus("current")


class _AdTaSystemEventLogRemotetHost_Type(DisplayString):
    """Custom type adTaSystemEventLogRemotetHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSystemEventLogRemotetHost_Type.__name__ = "DisplayString"
_AdTaSystemEventLogRemotetHost_Object = MibScalar
adTaSystemEventLogRemotetHost = _AdTaSystemEventLogRemotetHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 21),
    _AdTaSystemEventLogRemotetHost_Type()
)
adTaSystemEventLogRemotetHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogRemotetHost.setStatus("deprecated")


class _AdTaSystemEventLogPrevExportTime_Type(DisplayString):
    """Custom type adTaSystemEventLogPrevExportTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSystemEventLogPrevExportTime_Type.__name__ = "DisplayString"
_AdTaSystemEventLogPrevExportTime_Object = MibScalar
adTaSystemEventLogPrevExportTime = _AdTaSystemEventLogPrevExportTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 23),
    _AdTaSystemEventLogPrevExportTime_Type()
)
adTaSystemEventLogPrevExportTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSystemEventLogPrevExportTime.setStatus("current")


class _AdTaSystemEventLogPrevExportStatus_Type(DisplayString):
    """Custom type adTaSystemEventLogPrevExportStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSystemEventLogPrevExportStatus_Type.__name__ = "DisplayString"
_AdTaSystemEventLogPrevExportStatus_Object = MibScalar
adTaSystemEventLogPrevExportStatus = _AdTaSystemEventLogPrevExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 25),
    _AdTaSystemEventLogPrevExportStatus_Type()
)
adTaSystemEventLogPrevExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSystemEventLogPrevExportStatus.setStatus("current")


class _AdTaSystemEventLogNextAutoExportScheduled_Type(DisplayString):
    """Custom type adTaSystemEventLogNextAutoExportScheduled based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSystemEventLogNextAutoExportScheduled_Type.__name__ = "DisplayString"
_AdTaSystemEventLogNextAutoExportScheduled_Object = MibScalar
adTaSystemEventLogNextAutoExportScheduled = _AdTaSystemEventLogNextAutoExportScheduled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 27),
    _AdTaSystemEventLogNextAutoExportScheduled_Type()
)
adTaSystemEventLogNextAutoExportScheduled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSystemEventLogNextAutoExportScheduled.setStatus("current")


class _AdTaSystemEventLogManualExport_Type(Integer32):
    """Custom type adTaSystemEventLogManualExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exportFullSystemLog", 1),
          ("exportUnsentEvents", 2))
    )


_AdTaSystemEventLogManualExport_Type.__name__ = "Integer32"
_AdTaSystemEventLogManualExport_Object = MibScalar
adTaSystemEventLogManualExport = _AdTaSystemEventLogManualExport_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 29),
    _AdTaSystemEventLogManualExport_Type()
)
adTaSystemEventLogManualExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogManualExport.setStatus("current")


class _AdTaSystemEventLogCurrentStatus_Type(DisplayString):
    """Custom type adTaSystemEventLogCurrentStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSystemEventLogCurrentStatus_Type.__name__ = "DisplayString"
_AdTaSystemEventLogCurrentStatus_Object = MibScalar
adTaSystemEventLogCurrentStatus = _AdTaSystemEventLogCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 31),
    _AdTaSystemEventLogCurrentStatus_Type()
)
adTaSystemEventLogCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSystemEventLogCurrentStatus.setStatus("current")
_AdTaSystemEventLogRemotetHostInetAddressType_Type = InetAddressType
_AdTaSystemEventLogRemotetHostInetAddressType_Object = MibScalar
adTaSystemEventLogRemotetHostInetAddressType = _AdTaSystemEventLogRemotetHostInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 32),
    _AdTaSystemEventLogRemotetHostInetAddressType_Type()
)
adTaSystemEventLogRemotetHostInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSystemEventLogRemotetHostInetAddressType.setStatus("current")
_AdTaSystemEventLogRemotetHostInetAddress_Type = InetAddress
_AdTaSystemEventLogRemotetHostInetAddress_Object = MibScalar
adTaSystemEventLogRemotetHostInetAddress = _AdTaSystemEventLogRemotetHostInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 1, 33),
    _AdTaSystemEventLogRemotetHostInetAddress_Type()
)
adTaSystemEventLogRemotetHostInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSystemEventLogRemotetHostInetAddress.setStatus("current")
_AdTaSysCtrlGeneralFileExport_ObjectIdentity = ObjectIdentity
adTaSysCtrlGeneralFileExport = _AdTaSysCtrlGeneralFileExport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20)
)


class _AdTaGenExportRemotetHost_Type(DisplayString):
    """Custom type adTaGenExportRemotetHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaGenExportRemotetHost_Type.__name__ = "DisplayString"
_AdTaGenExportRemotetHost_Object = MibScalar
adTaGenExportRemotetHost = _AdTaGenExportRemotetHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 1),
    _AdTaGenExportRemotetHost_Type()
)
adTaGenExportRemotetHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenExportRemotetHost.setStatus("deprecated")


class _AdTaGeneralExportRemoteHostMethod_Type(Integer32):
    """Custom type adTaGeneralExportRemoteHostMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ftmTFTP", 1),
          ("ftmFTOT", 2),
          ("ftmFTP", 3),
          ("ftmSFTP", 4),
          ("ftmLFFS", 5))
    )


_AdTaGeneralExportRemoteHostMethod_Type.__name__ = "Integer32"
_AdTaGeneralExportRemoteHostMethod_Object = MibScalar
adTaGeneralExportRemoteHostMethod = _AdTaGeneralExportRemoteHostMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 2),
    _AdTaGeneralExportRemoteHostMethod_Type()
)
adTaGeneralExportRemoteHostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGeneralExportRemoteHostMethod.setStatus("current")


class _AdTaGenExportRemoteFilePath_Type(DisplayString):
    """Custom type adTaGenExportRemoteFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaGenExportRemoteFilePath_Type.__name__ = "DisplayString"
_AdTaGenExportRemoteFilePath_Object = MibScalar
adTaGenExportRemoteFilePath = _AdTaGenExportRemoteFilePath_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 3),
    _AdTaGenExportRemoteFilePath_Type()
)
adTaGenExportRemoteFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenExportRemoteFilePath.setStatus("current")


class _AdTaGenExportStatus_Type(DisplayString):
    """Custom type adTaGenExportStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaGenExportStatus_Type.__name__ = "DisplayString"
_AdTaGenExportStatus_Object = MibScalar
adTaGenExportStatus = _AdTaGenExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 5),
    _AdTaGenExportStatus_Type()
)
adTaGenExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaGenExportStatus.setStatus("current")


class _AdTaGenExportFileName_Type(DisplayString):
    """Custom type adTaGenExportFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaGenExportFileName_Type.__name__ = "DisplayString"
_AdTaGenExportFileName_Object = MibScalar
adTaGenExportFileName = _AdTaGenExportFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 7),
    _AdTaGenExportFileName_Type()
)
adTaGenExportFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaGenExportFileName.setStatus("current")


class _AdTaGeneralExportRetries_Type(Integer32):
    """Custom type adTaGeneralExportRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AdTaGeneralExportRetries_Type.__name__ = "Integer32"
_AdTaGeneralExportRetries_Object = MibScalar
adTaGeneralExportRetries = _AdTaGeneralExportRetries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 9),
    _AdTaGeneralExportRetries_Type()
)
adTaGeneralExportRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGeneralExportRetries.setStatus("current")


class _AdTaGenExportPrefixString_Type(DisplayString):
    """Custom type adTaGenExportPrefixString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_AdTaGenExportPrefixString_Type.__name__ = "DisplayString"
_AdTaGenExportPrefixString_Object = MibScalar
adTaGenExportPrefixString = _AdTaGenExportPrefixString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 11),
    _AdTaGenExportPrefixString_Type()
)
adTaGenExportPrefixString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenExportPrefixString.setStatus("current")


class _AdTaGenExportSuffixString_Type(DisplayString):
    """Custom type adTaGenExportSuffixString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AdTaGenExportSuffixString_Type.__name__ = "DisplayString"
_AdTaGenExportSuffixString_Object = MibScalar
adTaGenExportSuffixString = _AdTaGenExportSuffixString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 12),
    _AdTaGenExportSuffixString_Type()
)
adTaGenExportSuffixString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenExportSuffixString.setStatus("current")


class _AdTaGenExportExceptionReportEnable_Type(Integer32):
    """Custom type adTaGenExportExceptionReportEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaGenExportExceptionReportEnable_Type.__name__ = "Integer32"
_AdTaGenExportExceptionReportEnable_Object = MibScalar
adTaGenExportExceptionReportEnable = _AdTaGenExportExceptionReportEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 14),
    _AdTaGenExportExceptionReportEnable_Type()
)
adTaGenExportExceptionReportEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenExportExceptionReportEnable.setStatus("current")
_AdTaGenExportRemotetHostInetAddressType_Type = InetAddressType
_AdTaGenExportRemotetHostInetAddressType_Object = MibScalar
adTaGenExportRemotetHostInetAddressType = _AdTaGenExportRemotetHostInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 15),
    _AdTaGenExportRemotetHostInetAddressType_Type()
)
adTaGenExportRemotetHostInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaGenExportRemotetHostInetAddressType.setStatus("current")
_AdTaGenExportRemotetHostInetAddress_Type = InetAddress
_AdTaGenExportRemotetHostInetAddress_Object = MibScalar
adTaGenExportRemotetHostInetAddress = _AdTaGenExportRemotetHostInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 110, 20, 16),
    _AdTaGenExportRemotetHostInetAddress_Type()
)
adTaGenExportRemotetHostInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenExportRemotetHostInetAddress.setStatus("current")
_AdTaSysCtrlSNTP_ObjectIdentity = ObjectIdentity
adTaSysCtrlSNTP = _AdTaSysCtrlSNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120)
)


class _AdTaSntpServer_Type(DisplayString):
    """Custom type adTaSntpServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSntpServer_Type.__name__ = "DisplayString"
_AdTaSntpServer_Object = MibScalar
adTaSntpServer = _AdTaSntpServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 1),
    _AdTaSntpServer_Type()
)
adTaSntpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSntpServer.setStatus("current")


class _AdTaDSTAutomaticAdjustment_Type(Integer32):
    """Custom type adTaDSTAutomaticAdjustment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("pre2007Adjustment", 3))
    )


_AdTaDSTAutomaticAdjustment_Type.__name__ = "Integer32"
_AdTaDSTAutomaticAdjustment_Object = MibScalar
adTaDSTAutomaticAdjustment = _AdTaDSTAutomaticAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 3),
    _AdTaDSTAutomaticAdjustment_Type()
)
adTaDSTAutomaticAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaDSTAutomaticAdjustment.setStatus("current")


class _AdTaLocalTimeZone_Type(Integer32):
    """Custom type adTaLocalTimeZone based on Integer32"""
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
        *(("hawaii", 1),
          ("alaska", 2),
          ("pacific", 3),
          ("mountain", 4),
          ("central", 5),
          ("eastern", 6),
          ("atlantic", 7))
    )


_AdTaLocalTimeZone_Type.__name__ = "Integer32"
_AdTaLocalTimeZone_Object = MibScalar
adTaLocalTimeZone = _AdTaLocalTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 5),
    _AdTaLocalTimeZone_Type()
)
adTaLocalTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaLocalTimeZone.setStatus("deprecated")


class _AdTaRefreshPeriod_Type(Integer32):
    """Custom type adTaRefreshPeriod based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("oneMinute", 1),
          ("fiveMinute", 2),
          ("tenMinute", 3),
          ("fifteenMinute", 4),
          ("twentyMinute", 5),
          ("twentyFiveMinute", 6),
          ("thirtyMinute", 7),
          ("thirtyFiveMinute", 8),
          ("fortyMinute", 9),
          ("fortyFiveMinute", 10),
          ("fiftyMinute", 11),
          ("fiftyFiveMinute", 12),
          ("sixtyMinute", 13))
    )


_AdTaRefreshPeriod_Type.__name__ = "Integer32"
_AdTaRefreshPeriod_Object = MibScalar
adTaRefreshPeriod = _AdTaRefreshPeriod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 7),
    _AdTaRefreshPeriod_Type()
)
adTaRefreshPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaRefreshPeriod.setStatus("current")


class _AdTaTimeProtocolState_Type(Integer32):
    """Custom type adTaTimeProtocolState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("sntp", 2),
          ("netTime", 3))
    )


_AdTaTimeProtocolState_Type.__name__ = "Integer32"
_AdTaTimeProtocolState_Object = MibScalar
adTaTimeProtocolState = _AdTaTimeProtocolState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 9),
    _AdTaTimeProtocolState_Type()
)
adTaTimeProtocolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaTimeProtocolState.setStatus("current")


class _AdTaSntpOperationStaus_Type(DisplayString):
    """Custom type adTaSntpOperationStaus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdTaSntpOperationStaus_Type.__name__ = "DisplayString"
_AdTaSntpOperationStaus_Object = MibScalar
adTaSntpOperationStaus = _AdTaSntpOperationStaus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 11),
    _AdTaSntpOperationStaus_Type()
)
adTaSntpOperationStaus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSntpOperationStaus.setStatus("current")
_AdTaSntpTimeOutCount_Type = Integer32
_AdTaSntpTimeOutCount_Object = MibScalar
adTaSntpTimeOutCount = _AdTaSntpTimeOutCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 13),
    _AdTaSntpTimeOutCount_Type()
)
adTaSntpTimeOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSntpTimeOutCount.setStatus("current")
_AdTaSntpGMTtimeZoneString_Type = DisplayString
_AdTaSntpGMTtimeZoneString_Object = MibScalar
adTaSntpGMTtimeZoneString = _AdTaSntpGMTtimeZoneString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 15),
    _AdTaSntpGMTtimeZoneString_Type()
)
adTaSntpGMTtimeZoneString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSntpGMTtimeZoneString.setStatus("current")


class _AdTaSntpServer2_Type(DisplayString):
    """Custom type adTaSntpServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSntpServer2_Type.__name__ = "DisplayString"
_AdTaSntpServer2_Object = MibScalar
adTaSntpServer2 = _AdTaSntpServer2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 17),
    _AdTaSntpServer2_Type()
)
adTaSntpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSntpServer2.setStatus("current")


class _AdTaSntpServer3_Type(DisplayString):
    """Custom type adTaSntpServer3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSntpServer3_Type.__name__ = "DisplayString"
_AdTaSntpServer3_Object = MibScalar
adTaSntpServer3 = _AdTaSntpServer3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 18),
    _AdTaSntpServer3_Type()
)
adTaSntpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSntpServer3.setStatus("current")


class _AdTaSntpServer4_Type(DisplayString):
    """Custom type adTaSntpServer4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSntpServer4_Type.__name__ = "DisplayString"
_AdTaSntpServer4_Object = MibScalar
adTaSntpServer4 = _AdTaSntpServer4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 19),
    _AdTaSntpServer4_Type()
)
adTaSntpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSntpServer4.setStatus("current")


class _AdTaSntpTimeOutProv_Type(Integer32):
    """Custom type adTaSntpTimeOutProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AdTaSntpTimeOutProv_Type.__name__ = "Integer32"
_AdTaSntpTimeOutProv_Object = MibScalar
adTaSntpTimeOutProv = _AdTaSntpTimeOutProv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 21),
    _AdTaSntpTimeOutProv_Type()
)
adTaSntpTimeOutProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSntpTimeOutProv.setStatus("current")


class _AdTaSntpTimeRetryProv_Type(Integer32):
    """Custom type adTaSntpTimeRetryProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_AdTaSntpTimeRetryProv_Type.__name__ = "Integer32"
_AdTaSntpTimeRetryProv_Object = MibScalar
adTaSntpTimeRetryProv = _AdTaSntpTimeRetryProv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 23),
    _AdTaSntpTimeRetryProv_Type()
)
adTaSntpTimeRetryProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSntpTimeRetryProv.setStatus("current")
_AdTaSntpTimeOutCountServer2_Type = Integer32
_AdTaSntpTimeOutCountServer2_Object = MibScalar
adTaSntpTimeOutCountServer2 = _AdTaSntpTimeOutCountServer2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 25),
    _AdTaSntpTimeOutCountServer2_Type()
)
adTaSntpTimeOutCountServer2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSntpTimeOutCountServer2.setStatus("current")
_AdTaSntpTimeOutCountServer3_Type = Integer32
_AdTaSntpTimeOutCountServer3_Object = MibScalar
adTaSntpTimeOutCountServer3 = _AdTaSntpTimeOutCountServer3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 26),
    _AdTaSntpTimeOutCountServer3_Type()
)
adTaSntpTimeOutCountServer3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSntpTimeOutCountServer3.setStatus("current")
_AdTaSntpTimeOutCountServer4_Type = Integer32
_AdTaSntpTimeOutCountServer4_Object = MibScalar
adTaSntpTimeOutCountServer4 = _AdTaSntpTimeOutCountServer4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 27),
    _AdTaSntpTimeOutCountServer4_Type()
)
adTaSntpTimeOutCountServer4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSntpTimeOutCountServer4.setStatus("current")
_AdTaSntpCurrentServer_Type = Integer32
_AdTaSntpCurrentServer_Object = MibScalar
adTaSntpCurrentServer = _AdTaSntpCurrentServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 120, 29),
    _AdTaSntpCurrentServer_Type()
)
adTaSntpCurrentServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSntpCurrentServer.setStatus("current")
_AdTaSysLog_ObjectIdentity = ObjectIdentity
adTaSysLog = _AdTaSysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130)
)


class _AdTaSysLogServer_Type(DisplayString):
    """Custom type adTaSysLogServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSysLogServer_Type.__name__ = "DisplayString"
_AdTaSysLogServer_Object = MibScalar
adTaSysLogServer = _AdTaSysLogServer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 1),
    _AdTaSysLogServer_Type()
)
adTaSysLogServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysLogServer.setStatus("deprecated")


class _AdTaSysLogServer2_Type(DisplayString):
    """Custom type adTaSysLogServer2 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSysLogServer2_Type.__name__ = "DisplayString"
_AdTaSysLogServer2_Object = MibScalar
adTaSysLogServer2 = _AdTaSysLogServer2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 2),
    _AdTaSysLogServer2_Type()
)
adTaSysLogServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysLogServer2.setStatus("deprecated")


class _AdTaSysLogMode_Type(Integer32):
    """Custom type adTaSysLogMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enableSysLog", 1),
          ("disableSysLog", 2))
    )


_AdTaSysLogMode_Type.__name__ = "Integer32"
_AdTaSysLogMode_Object = MibScalar
adTaSysLogMode = _AdTaSysLogMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 3),
    _AdTaSysLogMode_Type()
)
adTaSysLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysLogMode.setStatus("current")


class _AdTaExportCtrlToSysLog_Type(Integer32):
    """Custom type adTaExportCtrlToSysLog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exportSystemEventToSyslogServer", 1)
    )


_AdTaExportCtrlToSysLog_Type.__name__ = "Integer32"
_AdTaExportCtrlToSysLog_Object = MibScalar
adTaExportCtrlToSysLog = _AdTaExportCtrlToSysLog_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 4),
    _AdTaExportCtrlToSysLog_Type()
)
adTaExportCtrlToSysLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaExportCtrlToSysLog.setStatus("current")


class _AdTaSysLogServer3_Type(DisplayString):
    """Custom type adTaSysLogServer3 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSysLogServer3_Type.__name__ = "DisplayString"
_AdTaSysLogServer3_Object = MibScalar
adTaSysLogServer3 = _AdTaSysLogServer3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 6),
    _AdTaSysLogServer3_Type()
)
adTaSysLogServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysLogServer3.setStatus("deprecated")


class _AdTaSysLogServer4_Type(DisplayString):
    """Custom type adTaSysLogServer4 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSysLogServer4_Type.__name__ = "DisplayString"
_AdTaSysLogServer4_Object = MibScalar
adTaSysLogServer4 = _AdTaSysLogServer4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 7),
    _AdTaSysLogServer4_Type()
)
adTaSysLogServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysLogServer4.setStatus("deprecated")
_AdTaSysLogServerTable_Object = MibTable
adTaSysLogServerTable = _AdTaSysLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 10)
)
if mibBuilder.loadTexts:
    adTaSysLogServerTable.setStatus("current")
_AdTaSysLogServerEntry_Object = MibTableRow
adTaSysLogServerEntry = _AdTaSysLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 10, 1)
)
adTaSysLogServerEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysLogServerIndex"),
)
if mibBuilder.loadTexts:
    adTaSysLogServerEntry.setStatus("current")
_AdTaSysLogServerIndex_Type = Integer32
_AdTaSysLogServerIndex_Object = MibTableColumn
adTaSysLogServerIndex = _AdTaSysLogServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 10, 1, 1),
    _AdTaSysLogServerIndex_Type()
)
adTaSysLogServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTaSysLogServerIndex.setStatus("current")
_AdTaSysLogServerAddressType_Type = InetAddressType
_AdTaSysLogServerAddressType_Object = MibTableColumn
adTaSysLogServerAddressType = _AdTaSysLogServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 10, 1, 2),
    _AdTaSysLogServerAddressType_Type()
)
adTaSysLogServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysLogServerAddressType.setStatus("current")
_AdTaSysLogServerInetAddress_Type = InetAddress
_AdTaSysLogServerInetAddress_Object = MibTableColumn
adTaSysLogServerInetAddress = _AdTaSysLogServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 130, 10, 1, 3),
    _AdTaSysLogServerInetAddress_Type()
)
adTaSysLogServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysLogServerInetAddress.setStatus("current")
_AdTaDhcpServer_ObjectIdentity = ObjectIdentity
adTaDhcpServer = _AdTaDhcpServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140)
)


class _AdTaDhcpNetworkInterface_Type(DisplayString):
    """Custom type adTaDhcpNetworkInterface based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaDhcpNetworkInterface_Type.__name__ = "DisplayString"
_AdTaDhcpNetworkInterface_Object = MibScalar
adTaDhcpNetworkInterface = _AdTaDhcpNetworkInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 10),
    _AdTaDhcpNetworkInterface_Type()
)
adTaDhcpNetworkInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaDhcpNetworkInterface.setStatus("current")
_AdTaDhcpSubNetMask_Type = IpAddress
_AdTaDhcpSubNetMask_Object = MibScalar
adTaDhcpSubNetMask = _AdTaDhcpSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 12),
    _AdTaDhcpSubNetMask_Type()
)
adTaDhcpSubNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaDhcpSubNetMask.setStatus("current")


class _AdTaDhcpSubNetLength_Type(Integer32):
    """Custom type adTaDhcpSubNetLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(24, 32),
    )


_AdTaDhcpSubNetLength_Type.__name__ = "Integer32"
_AdTaDhcpSubNetLength_Object = MibScalar
adTaDhcpSubNetLength = _AdTaDhcpSubNetLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 14),
    _AdTaDhcpSubNetLength_Type()
)
adTaDhcpSubNetLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaDhcpSubNetLength.setStatus("current")
_AdTaDhcpStartIpAddress_Type = IpAddress
_AdTaDhcpStartIpAddress_Object = MibScalar
adTaDhcpStartIpAddress = _AdTaDhcpStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 16),
    _AdTaDhcpStartIpAddress_Type()
)
adTaDhcpStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaDhcpStartIpAddress.setStatus("current")
_AdTaDhcpEndIpAddress_Type = IpAddress
_AdTaDhcpEndIpAddress_Object = MibScalar
adTaDhcpEndIpAddress = _AdTaDhcpEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 18),
    _AdTaDhcpEndIpAddress_Type()
)
adTaDhcpEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaDhcpEndIpAddress.setStatus("current")
_AdTaDhcpSubNetAddress_Type = IpAddress
_AdTaDhcpSubNetAddress_Object = MibScalar
adTaDhcpSubNetAddress = _AdTaDhcpSubNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 20),
    _AdTaDhcpSubNetAddress_Type()
)
adTaDhcpSubNetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaDhcpSubNetAddress.setStatus("current")


class _AdTaDhcpLeasDurationHours_Type(Integer32):
    """Custom type adTaDhcpLeasDurationHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_AdTaDhcpLeasDurationHours_Type.__name__ = "Integer32"
_AdTaDhcpLeasDurationHours_Object = MibScalar
adTaDhcpLeasDurationHours = _AdTaDhcpLeasDurationHours_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 22),
    _AdTaDhcpLeasDurationHours_Type()
)
adTaDhcpLeasDurationHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaDhcpLeasDurationHours.setStatus("current")


class _AdTaDhcpLeasDurationMintues_Type(Integer32):
    """Custom type adTaDhcpLeasDurationMintues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 59),
    )


_AdTaDhcpLeasDurationMintues_Type.__name__ = "Integer32"
_AdTaDhcpLeasDurationMintues_Object = MibScalar
adTaDhcpLeasDurationMintues = _AdTaDhcpLeasDurationMintues_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 24),
    _AdTaDhcpLeasDurationMintues_Type()
)
adTaDhcpLeasDurationMintues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaDhcpLeasDurationMintues.setStatus("current")


class _AdTaDhcpServerCommands_Type(Integer32):
    """Custom type adTaDhcpServerCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              999)
        )
    )
    namedValues = NamedValues(
        *(("startDhcpServer", 1),
          ("stopDhcpServer", 2),
          ("dhcpNoCommand", 999))
    )


_AdTaDhcpServerCommands_Type.__name__ = "Integer32"
_AdTaDhcpServerCommands_Object = MibScalar
adTaDhcpServerCommands = _AdTaDhcpServerCommands_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 26),
    _AdTaDhcpServerCommands_Type()
)
adTaDhcpServerCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaDhcpServerCommands.setStatus("current")


class _AdTaDhcpServerOperationStatus_Type(DisplayString):
    """Custom type adTaDhcpServerOperationStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdTaDhcpServerOperationStatus_Type.__name__ = "DisplayString"
_AdTaDhcpServerOperationStatus_Object = MibScalar
adTaDhcpServerOperationStatus = _AdTaDhcpServerOperationStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 28),
    _AdTaDhcpServerOperationStatus_Type()
)
adTaDhcpServerOperationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaDhcpServerOperationStatus.setStatus("current")
_AdTaDhcpServerStatusTable_Object = MibTable
adTaDhcpServerStatusTable = _AdTaDhcpServerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 40)
)
if mibBuilder.loadTexts:
    adTaDhcpServerStatusTable.setStatus("current")
_AdTaDhcpServerStatusTableEntry_Object = MibTableRow
adTaDhcpServerStatusTableEntry = _AdTaDhcpServerStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 40, 1)
)
adTaDhcpServerStatusTableEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseIndex"),
    (0, "ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmRlsFilesIndex"),
)
if mibBuilder.loadTexts:
    adTaDhcpServerStatusTableEntry.setStatus("current")
_AdTaDhcpServerStatusIndex_Type = Integer32
_AdTaDhcpServerStatusIndex_Object = MibTableColumn
adTaDhcpServerStatusIndex = _AdTaDhcpServerStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 40, 1, 1),
    _AdTaDhcpServerStatusIndex_Type()
)
adTaDhcpServerStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaDhcpServerStatusIndex.setStatus("current")


class _AdTaDhcpServerStatus_Type(DisplayString):
    """Custom type adTaDhcpServerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 200),
    )


_AdTaDhcpServerStatus_Type.__name__ = "DisplayString"
_AdTaDhcpServerStatus_Object = MibTableColumn
adTaDhcpServerStatus = _AdTaDhcpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 140, 40, 1, 4),
    _AdTaDhcpServerStatus_Type()
)
adTaDhcpServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaDhcpServerStatus.setStatus("current")
_AdTaModuleReset_ObjectIdentity = ObjectIdentity
adTaModuleReset = _AdTaModuleReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 150)
)
_AdTaModuleResetSlot_Type = Integer32
_AdTaModuleResetSlot_Object = MibScalar
adTaModuleResetSlot = _AdTaModuleResetSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 150, 10),
    _AdTaModuleResetSlot_Type()
)
adTaModuleResetSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaModuleResetSlot.setStatus("current")
_AdTaModuleResetCtrl_Type = Integer32
_AdTaModuleResetCtrl_Object = MibScalar
adTaModuleResetCtrl = _AdTaModuleResetCtrl_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 150, 12),
    _AdTaModuleResetCtrl_Type()
)
adTaModuleResetCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaModuleResetCtrl.setStatus("current")
_AdTaSecurity_ObjectIdentity = ObjectIdentity
adTaSecurity = _AdTaSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160)
)
_AdTaSSLConfiguration_ObjectIdentity = ObjectIdentity
adTaSSLConfiguration = _AdTaSSLConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50)
)


class _AdTaSSLKeySizeBits_Type(Integer32):
    """Custom type adTaSSLKeySizeBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(512,
              1024,
              2048)
        )
    )
    namedValues = NamedValues(
        *(("bits512", 512),
          ("bits1024", 1024),
          ("bits2048", 2048))
    )


_AdTaSSLKeySizeBits_Type.__name__ = "Integer32"
_AdTaSSLKeySizeBits_Object = MibScalar
adTaSSLKeySizeBits = _AdTaSSLKeySizeBits_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 5),
    _AdTaSSLKeySizeBits_Type()
)
adTaSSLKeySizeBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLKeySizeBits.setStatus("current")


class _AdTaSSLKeyType_Type(Integer32):
    """Custom type adTaSSLKeyType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rsa", 1),
          ("dsa", 2))
    )


_AdTaSSLKeyType_Type.__name__ = "Integer32"
_AdTaSSLKeyType_Object = MibScalar
adTaSSLKeyType = _AdTaSSLKeyType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 7),
    _AdTaSSLKeyType_Type()
)
adTaSSLKeyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLKeyType.setStatus("current")


class _AdTaSSLInputPassword_Type(DisplayString):
    """Custom type adTaSSLInputPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_AdTaSSLInputPassword_Type.__name__ = "DisplayString"
_AdTaSSLInputPassword_Object = MibScalar
adTaSSLInputPassword = _AdTaSSLInputPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 9),
    _AdTaSSLInputPassword_Type()
)
adTaSSLInputPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLInputPassword.setStatus("current")


class _AdTaSSLOutputPassword_Type(DisplayString):
    """Custom type adTaSSLOutputPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_AdTaSSLOutputPassword_Type.__name__ = "DisplayString"
_AdTaSSLOutputPassword_Object = MibScalar
adTaSSLOutputPassword = _AdTaSSLOutputPassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 11),
    _AdTaSSLOutputPassword_Type()
)
adTaSSLOutputPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLOutputPassword.setStatus("current")


class _AdTaSSLCertificateCountry_Type(DisplayString):
    """Custom type adTaSSLCertificateCountry based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_AdTaSSLCertificateCountry_Type.__name__ = "DisplayString"
_AdTaSSLCertificateCountry_Object = MibScalar
adTaSSLCertificateCountry = _AdTaSSLCertificateCountry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 13),
    _AdTaSSLCertificateCountry_Type()
)
adTaSSLCertificateCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateCountry.setStatus("current")


class _AdTaSSLCertificateStateOrProvince_Type(DisplayString):
    """Custom type adTaSSLCertificateStateOrProvince based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 64),
    )


_AdTaSSLCertificateStateOrProvince_Type.__name__ = "DisplayString"
_AdTaSSLCertificateStateOrProvince_Object = MibScalar
adTaSSLCertificateStateOrProvince = _AdTaSSLCertificateStateOrProvince_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 15),
    _AdTaSSLCertificateStateOrProvince_Type()
)
adTaSSLCertificateStateOrProvince.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateStateOrProvince.setStatus("current")


class _AdTaSSLCertificateChallengePassword_Type(DisplayString):
    """Custom type adTaSSLCertificateChallengePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 20),
    )


_AdTaSSLCertificateChallengePassword_Type.__name__ = "DisplayString"
_AdTaSSLCertificateChallengePassword_Object = MibScalar
adTaSSLCertificateChallengePassword = _AdTaSSLCertificateChallengePassword_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 17),
    _AdTaSSLCertificateChallengePassword_Type()
)
adTaSSLCertificateChallengePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateChallengePassword.setStatus("current")


class _AdTaSSLCertificateLocality_Type(DisplayString):
    """Custom type adTaSSLCertificateLocality based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLCertificateLocality_Type.__name__ = "DisplayString"
_AdTaSSLCertificateLocality_Object = MibScalar
adTaSSLCertificateLocality = _AdTaSSLCertificateLocality_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 19),
    _AdTaSSLCertificateLocality_Type()
)
adTaSSLCertificateLocality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateLocality.setStatus("current")


class _AdTaSSLCertificateOrganization_Type(DisplayString):
    """Custom type adTaSSLCertificateOrganization based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLCertificateOrganization_Type.__name__ = "DisplayString"
_AdTaSSLCertificateOrganization_Object = MibScalar
adTaSSLCertificateOrganization = _AdTaSSLCertificateOrganization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 21),
    _AdTaSSLCertificateOrganization_Type()
)
adTaSSLCertificateOrganization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateOrganization.setStatus("current")


class _AdTaSSLCertificateOrganizationalUnitName_Type(DisplayString):
    """Custom type adTaSSLCertificateOrganizationalUnitName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLCertificateOrganizationalUnitName_Type.__name__ = "DisplayString"
_AdTaSSLCertificateOrganizationalUnitName_Object = MibScalar
adTaSSLCertificateOrganizationalUnitName = _AdTaSSLCertificateOrganizationalUnitName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 23),
    _AdTaSSLCertificateOrganizationalUnitName_Type()
)
adTaSSLCertificateOrganizationalUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateOrganizationalUnitName.setStatus("current")


class _AdTaSSLCertificateCommonName_Type(DisplayString):
    """Custom type adTaSSLCertificateCommonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLCertificateCommonName_Type.__name__ = "DisplayString"
_AdTaSSLCertificateCommonName_Object = MibScalar
adTaSSLCertificateCommonName = _AdTaSSLCertificateCommonName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 25),
    _AdTaSSLCertificateCommonName_Type()
)
adTaSSLCertificateCommonName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateCommonName.setStatus("current")


class _AdTaSSLCertificateEmailAddress_Type(DisplayString):
    """Custom type adTaSSLCertificateEmailAddress based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_AdTaSSLCertificateEmailAddress_Type.__name__ = "DisplayString"
_AdTaSSLCertificateEmailAddress_Object = MibScalar
adTaSSLCertificateEmailAddress = _AdTaSSLCertificateEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 27),
    _AdTaSSLCertificateEmailAddress_Type()
)
adTaSSLCertificateEmailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateEmailAddress.setStatus("current")


class _AdTaGenerateNewSSLKeys_Type(Integer32):
    """Custom type adTaGenerateNewSSLKeys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("generateNewSSLKeys", 1)
    )


_AdTaGenerateNewSSLKeys_Type.__name__ = "Integer32"
_AdTaGenerateNewSSLKeys_Object = MibScalar
adTaGenerateNewSSLKeys = _AdTaGenerateNewSSLKeys_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 29),
    _AdTaGenerateNewSSLKeys_Type()
)
adTaGenerateNewSSLKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenerateNewSSLKeys.setStatus("current")


class _AdTaGenerateNewSSLCertificateRequest_Type(Integer32):
    """Custom type adTaGenerateNewSSLCertificateRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("generateNewSSLCertRequest", 1)
    )


_AdTaGenerateNewSSLCertificateRequest_Type.__name__ = "Integer32"
_AdTaGenerateNewSSLCertificateRequest_Object = MibScalar
adTaGenerateNewSSLCertificateRequest = _AdTaGenerateNewSSLCertificateRequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 30),
    _AdTaGenerateNewSSLCertificateRequest_Type()
)
adTaGenerateNewSSLCertificateRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaGenerateNewSSLCertificateRequest.setStatus("current")


class _AdTaSSLuseImportCertificate_Type(Integer32):
    """Custom type adTaSSLuseImportCertificate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSSLuseImportCertificate_Type.__name__ = "Integer32"
_AdTaSSLuseImportCertificate_Object = MibScalar
adTaSSLuseImportCertificate = _AdTaSSLuseImportCertificate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 31),
    _AdTaSSLuseImportCertificate_Type()
)
adTaSSLuseImportCertificate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLuseImportCertificate.setStatus("current")
_AdTaSSLRemoteKeyDownload_ObjectIdentity = ObjectIdentity
adTaSSLRemoteKeyDownload = _AdTaSSLRemoteKeyDownload_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100)
)


class _AdTaSSLRemotePrivateKeyFileName_Type(DisplayString):
    """Custom type adTaSSLRemotePrivateKeyFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLRemotePrivateKeyFileName_Type.__name__ = "DisplayString"
_AdTaSSLRemotePrivateKeyFileName_Object = MibScalar
adTaSSLRemotePrivateKeyFileName = _AdTaSSLRemotePrivateKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 3),
    _AdTaSSLRemotePrivateKeyFileName_Type()
)
adTaSSLRemotePrivateKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLRemotePrivateKeyFileName.setStatus("current")


class _AdTaSSLRemotedPublicKeyFileName_Type(DisplayString):
    """Custom type adTaSSLRemotedPublicKeyFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLRemotedPublicKeyFileName_Type.__name__ = "DisplayString"
_AdTaSSLRemotedPublicKeyFileName_Object = MibScalar
adTaSSLRemotedPublicKeyFileName = _AdTaSSLRemotedPublicKeyFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 5),
    _AdTaSSLRemotedPublicKeyFileName_Type()
)
adTaSSLRemotedPublicKeyFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLRemotedPublicKeyFileName.setStatus("current")


class _AdTaSSLRemoteCertificateFileName_Type(DisplayString):
    """Custom type adTaSSLRemoteCertificateFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLRemoteCertificateFileName_Type.__name__ = "DisplayString"
_AdTaSSLRemoteCertificateFileName_Object = MibScalar
adTaSSLRemoteCertificateFileName = _AdTaSSLRemoteCertificateFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 7),
    _AdTaSSLRemoteCertificateFileName_Type()
)
adTaSSLRemoteCertificateFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLRemoteCertificateFileName.setStatus("current")
_AdTaSSLRemoteKeysDownLoadStatus_Type = DisplayString
_AdTaSSLRemoteKeysDownLoadStatus_Object = MibScalar
adTaSSLRemoteKeysDownLoadStatus = _AdTaSSLRemoteKeysDownLoadStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 8),
    _AdTaSSLRemoteKeysDownLoadStatus_Type()
)
adTaSSLRemoteKeysDownLoadStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLRemoteKeysDownLoadStatus.setStatus("current")


class _AdTaSSLCertificateRequestFileName_Type(DisplayString):
    """Custom type adTaSSLCertificateRequestFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AdTaSSLCertificateRequestFileName_Type.__name__ = "DisplayString"
_AdTaSSLCertificateRequestFileName_Object = MibScalar
adTaSSLCertificateRequestFileName = _AdTaSSLCertificateRequestFileName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 9),
    _AdTaSSLCertificateRequestFileName_Type()
)
adTaSSLCertificateRequestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateRequestFileName.setStatus("current")


class _AdTaSSLCertificateRequestExport_Type(Integer32):
    """Custom type adTaSSLCertificateRequestExport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("exportSSLCertificateRequest", 1)
    )


_AdTaSSLCertificateRequestExport_Type.__name__ = "Integer32"
_AdTaSSLCertificateRequestExport_Object = MibScalar
adTaSSLCertificateRequestExport = _AdTaSSLCertificateRequestExport_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 10),
    _AdTaSSLCertificateRequestExport_Type()
)
adTaSSLCertificateRequestExport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateRequestExport.setStatus("current")


class _AdTaSSLCertificateImport_Type(Integer32):
    """Custom type adTaSSLCertificateImport based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("importSSLCertificate", 1)
    )


_AdTaSSLCertificateImport_Type.__name__ = "Integer32"
_AdTaSSLCertificateImport_Object = MibScalar
adTaSSLCertificateImport = _AdTaSSLCertificateImport_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 11),
    _AdTaSSLCertificateImport_Type()
)
adTaSSLCertificateImport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLCertificateImport.setStatus("current")


class _AdTaSSLCertificateImportStatus_Type(Integer32):
    """Custom type adTaSSLCertificateImportStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("notReady", 2))
    )


_AdTaSSLCertificateImportStatus_Type.__name__ = "Integer32"
_AdTaSSLCertificateImportStatus_Object = MibScalar
adTaSSLCertificateImportStatus = _AdTaSSLCertificateImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 12),
    _AdTaSSLCertificateImportStatus_Type()
)
adTaSSLCertificateImportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSSLCertificateImportStatus.setStatus("current")


class _AdTaSSLDownLoadRemoteKeys_Type(Integer32):
    """Custom type adTaSSLDownLoadRemoteKeys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("downloadRemoteSSLKeys", 1)
    )


_AdTaSSLDownLoadRemoteKeys_Type.__name__ = "Integer32"
_AdTaSSLDownLoadRemoteKeys_Object = MibScalar
adTaSSLDownLoadRemoteKeys = _AdTaSSLDownLoadRemoteKeys_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 13),
    _AdTaSSLDownLoadRemoteKeys_Type()
)
adTaSSLDownLoadRemoteKeys.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSSLDownLoadRemoteKeys.setStatus("current")


class _AdTaSSLCertificateSigningRequestStatus_Type(Integer32):
    """Custom type adTaSSLCertificateSigningRequestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ready", 1),
          ("notReady", 2))
    )


_AdTaSSLCertificateSigningRequestStatus_Type.__name__ = "Integer32"
_AdTaSSLCertificateSigningRequestStatus_Object = MibScalar
adTaSSLCertificateSigningRequestStatus = _AdTaSSLCertificateSigningRequestStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 14),
    _AdTaSSLCertificateSigningRequestStatus_Type()
)
adTaSSLCertificateSigningRequestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSSLCertificateSigningRequestStatus.setStatus("current")


class _AdTaSSLCertificateSignRequestExportStatus_Type(DisplayString):
    """Custom type adTaSSLCertificateSignRequestExportStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSSLCertificateSignRequestExportStatus_Type.__name__ = "DisplayString"
_AdTaSSLCertificateSignRequestExportStatus_Object = MibScalar
adTaSSLCertificateSignRequestExportStatus = _AdTaSSLCertificateSignRequestExportStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 15),
    _AdTaSSLCertificateSignRequestExportStatus_Type()
)
adTaSSLCertificateSignRequestExportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSSLCertificateSignRequestExportStatus.setStatus("current")


class _AdTaSSLSignedCertificateImportStatus_Type(DisplayString):
    """Custom type adTaSSLSignedCertificateImportStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSSLSignedCertificateImportStatus_Type.__name__ = "DisplayString"
_AdTaSSLSignedCertificateImportStatus_Object = MibScalar
adTaSSLSignedCertificateImportStatus = _AdTaSSLSignedCertificateImportStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 160, 50, 100, 16),
    _AdTaSSLSignedCertificateImportStatus_Type()
)
adTaSSLSignedCertificateImportStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSSLSignedCertificateImportStatus.setStatus("current")
_AdTaSysCtrlReboot_ObjectIdentity = ObjectIdentity
adTaSysCtrlReboot = _AdTaSysCtrlReboot_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170)
)
_AdTaSysCtrlRebootTraps_ObjectIdentity = ObjectIdentity
adTaSysCtrlRebootTraps = _AdTaSysCtrlRebootTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 0)
)


class _AdTaSysCtrlRebootOperMode_Type(Integer32):
    """Custom type adTaSysCtrlRebootOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("scheduled", 3))
    )


_AdTaSysCtrlRebootOperMode_Type.__name__ = "Integer32"
_AdTaSysCtrlRebootOperMode_Object = MibScalar
adTaSysCtrlRebootOperMode = _AdTaSysCtrlRebootOperMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 1),
    _AdTaSysCtrlRebootOperMode_Type()
)
adTaSysCtrlRebootOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlRebootOperMode.setStatus("current")


class _AdTaSysCtrlRebootSchedDateTime_Type(DisplayString):
    """Custom type adTaSysCtrlRebootSchedDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSysCtrlRebootSchedDateTime_Type.__name__ = "DisplayString"
_AdTaSysCtrlRebootSchedDateTime_Object = MibScalar
adTaSysCtrlRebootSchedDateTime = _AdTaSysCtrlRebootSchedDateTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 2),
    _AdTaSysCtrlRebootSchedDateTime_Type()
)
adTaSysCtrlRebootSchedDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlRebootSchedDateTime.setStatus("current")


class _AdTaSysCtrlRebootInitiate_Type(Integer32):
    """Custom type adTaSysCtrlRebootInitiate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("initiateSCR", 1)
    )


_AdTaSysCtrlRebootInitiate_Type.__name__ = "Integer32"
_AdTaSysCtrlRebootInitiate_Object = MibScalar
adTaSysCtrlRebootInitiate = _AdTaSysCtrlRebootInitiate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 3),
    _AdTaSysCtrlRebootInitiate_Type()
)
adTaSysCtrlRebootInitiate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlRebootInitiate.setStatus("current")


class _AdTaSysCtrlRebootLastStatus_Type(DisplayString):
    """Custom type adTaSysCtrlRebootLastStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdTaSysCtrlRebootLastStatus_Type.__name__ = "DisplayString"
_AdTaSysCtrlRebootLastStatus_Object = MibScalar
adTaSysCtrlRebootLastStatus = _AdTaSysCtrlRebootLastStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 4),
    _AdTaSysCtrlRebootLastStatus_Type()
)
adTaSysCtrlRebootLastStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaSysCtrlRebootLastStatus.setStatus("current")


class _AdTaSysCtrlRebootArmedStatus_Type(Integer32):
    """Custom type adTaSysCtrlRebootArmedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("armed", 1),
          ("notArmed", 2))
    )


_AdTaSysCtrlRebootArmedStatus_Type.__name__ = "Integer32"
_AdTaSysCtrlRebootArmedStatus_Object = MibScalar
adTaSysCtrlRebootArmedStatus = _AdTaSysCtrlRebootArmedStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 5),
    _AdTaSysCtrlRebootArmedStatus_Type()
)
adTaSysCtrlRebootArmedStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlRebootArmedStatus.setStatus("current")


class _AdTaSysCtrlRebootMode_Type(Integer32):
    """Custom type adTaSysCtrlRebootMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("concurrentMode", 1),
          ("redundancyMode", 2))
    )


_AdTaSysCtrlRebootMode_Type.__name__ = "Integer32"
_AdTaSysCtrlRebootMode_Object = MibScalar
adTaSysCtrlRebootMode = _AdTaSysCtrlRebootMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 6),
    _AdTaSysCtrlRebootMode_Type()
)
adTaSysCtrlRebootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlRebootMode.setStatus("current")
_AdTaSysAlarmVarbinds_ObjectIdentity = ObjectIdentity
adTaSysAlarmVarbinds = _AdTaSysAlarmVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 180)
)


class _AdTaDataLossDescription_Type(DisplayString):
    """Custom type adTaDataLossDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdTaDataLossDescription_Type.__name__ = "DisplayString"
_AdTaDataLossDescription_Object = MibScalar
adTaDataLossDescription = _AdTaDataLossDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 180, 3),
    _AdTaDataLossDescription_Type()
)
adTaDataLossDescription.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    adTaDataLossDescription.setStatus("current")
_AdTaSysCtrlVLANBridge_ObjectIdentity = ObjectIdentity
adTaSysCtrlVLANBridge = _AdTaSysCtrlVLANBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 190)
)


class _AdTaSysCtrlVLANBridgeMode_Type(Integer32):
    """Custom type adTaSysCtrlVLANBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlVLANBridgeMode_Type.__name__ = "Integer32"
_AdTaSysCtrlVLANBridgeMode_Object = MibScalar
adTaSysCtrlVLANBridgeMode = _AdTaSysCtrlVLANBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 190, 1),
    _AdTaSysCtrlVLANBridgeMode_Type()
)
adTaSysCtrlVLANBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlVLANBridgeMode.setStatus("current")


class _AdTaSysCtrlVLANBridgeInterface_Type(Integer32):
    """Custom type adTaSysCtrlVLANBridgeInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enet", 1),
          ("enet2", 2))
    )


_AdTaSysCtrlVLANBridgeInterface_Type.__name__ = "Integer32"
_AdTaSysCtrlVLANBridgeInterface_Object = MibScalar
adTaSysCtrlVLANBridgeInterface = _AdTaSysCtrlVLANBridgeInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 190, 2),
    _AdTaSysCtrlVLANBridgeInterface_Type()
)
adTaSysCtrlVLANBridgeInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlVLANBridgeInterface.setStatus("current")

# Managed Objects groups


# Notification objects

adTASetSingleServiceStateMsgFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006301)
)
adTASetSingleServiceStateMsgFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"))
)
if mibBuilder.loadTexts:
    adTASetSingleServiceStateMsgFail.setStatus(
        "current"
    )

adTAGetSingleServiceStateMsgFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006303)
)
adTAGetSingleServiceStateMsgFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"))
)
if mibBuilder.loadTexts:
    adTAGetSingleServiceStateMsgFail.setStatus(
        "current"
    )

adTASetAllServiceStateMsgFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006305)
)
adTASetAllServiceStateMsgFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"))
)
if mibBuilder.loadTexts:
    adTASetAllServiceStateMsgFail.setStatus(
        "current"
    )

adTAGetAllServiceStateMsgFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006307)
)
adTAGetAllServiceStateMsgFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"))
)
if mibBuilder.loadTexts:
    adTAGetAllServiceStateMsgFail.setStatus(
        "current"
    )

adTACriticalAudibleRelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006308)
)
adTACriticalAudibleRelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTACriticalAudibleRelayTestClear.setStatus(
        "current"
    )

adTACriticalAudibleRelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006309)
)
adTACriticalAudibleRelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTACriticalAudibleRelayTestActive.setStatus(
        "current"
    )

adTACriticalVisualRelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006310)
)
adTACriticalVisualRelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTACriticalVisualRelayTestClear.setStatus(
        "current"
    )

adTACriticalVisualRelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006311)
)
adTACriticalVisualRelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTACriticalVisualRelayTestActive.setStatus(
        "current"
    )

adTAMajAudibleRelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006312)
)
adTAMajAudibleRelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMajAudibleRelayTestClear.setStatus(
        "current"
    )

adTAMajAudibleRelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006313)
)
adTAMajAudibleRelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMajAudibleRelayTestActive.setStatus(
        "current"
    )

adTAMajVisualRelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006314)
)
adTAMajVisualRelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMajVisualRelayTestClear.setStatus(
        "current"
    )

adTAMajVisualRelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006315)
)
adTAMajVisualRelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMajVisualRelayTestActive.setStatus(
        "current"
    )

adTAMinorAudibleRelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006316)
)
adTAMinorAudibleRelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMinorAudibleRelayTestClear.setStatus(
        "current"
    )

adTAMinorAudibleRelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006317)
)
adTAMinorAudibleRelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMinorAudibleRelayTestActive.setStatus(
        "current"
    )

adTAMinorVisualRelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006318)
)
adTAMinorVisualRelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMinorVisualRelayTestClear.setStatus(
        "current"
    )

adTAMinorVisualRelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006319)
)
adTAMinorVisualRelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAMinorVisualRelayTestActive.setStatus(
        "current"
    )

adTAAux1RelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006320)
)
adTAAux1RelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAAux1RelayTestClear.setStatus(
        "current"
    )

adTAAux1RelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006321)
)
adTAAux1RelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAAux1RelayTestActive.setStatus(
        "current"
    )

adTAAux2RelayTestClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006322)
)
adTAAux2RelayTestClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAAux2RelayTestClear.setStatus(
        "current"
    )

adTAAux2RelayTestActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006323)
)
adTAAux2RelayTestActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    adTAAux2RelayTestActive.setStatus(
        "current"
    )

adTACleiCodeMisMatchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006324)
)
adTACleiCodeMisMatchClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdCLEIcode"))
)
if mibBuilder.loadTexts:
    adTACleiCodeMisMatchClear.setStatus(
        "current"
    )

adTACleiCodeMisMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006325)
)
adTACleiCodeMisMatch.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotProdCLEIcode"))
)
if mibBuilder.loadTexts:
    adTACleiCodeMisMatch.setStatus(
        "current"
    )

adTAPowerSheddingInputDeAsserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006328)
)
adTAPowerSheddingInputDeAsserted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedAlmInput"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedACFailAlarmDescription"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedACFailAlarmSeverity"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedCountDown"))
)
if mibBuilder.loadTexts:
    adTAPowerSheddingInputDeAsserted.setStatus(
        "current"
    )

adTAPowerSheddingInputAsserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006329)
)
adTAPowerSheddingInputAsserted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedAlmInput"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedACFailAlarmDescription"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedACFailAlarmSeverity"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedCountDown"))
)
if mibBuilder.loadTexts:
    adTAPowerSheddingInputAsserted.setStatus(
        "current"
    )

adTAPowerSheddingDeActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006330)
)
adTAPowerSheddingDeActivated.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedAlmInput"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedStatus"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedStateAlarmSeverity"))
)
if mibBuilder.loadTexts:
    adTAPowerSheddingDeActivated.setStatus(
        "current"
    )

adTAPowerSheddingActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006331)
)
adTAPowerSheddingActivated.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedAlmInput"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedStatus"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedStateAlarmSeverity"))
)
if mibBuilder.loadTexts:
    adTAPowerSheddingActivated.setStatus(
        "current"
    )

adTAFanMPowerAFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006332)
)
adTAFanMPowerAFailClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAFanMPowerAFailClear.setStatus(
        "current"
    )

adTAFanMPowerAFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006333)
)
adTAFanMPowerAFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAFanMPowerAFail.setStatus(
        "current"
    )

adTAFanMPowerBFailClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006334)
)
adTAFanMPowerBFailClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAFanMPowerBFailClear.setStatus(
        "current"
    )

adTAFanMPowerBFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006335)
)
adTAFanMPowerBFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmUserName"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUenvAlarmInputLevel"))
)
if mibBuilder.loadTexts:
    adTAFanMPowerBFail.setStatus(
        "current"
    )

adTASrmActiveRlsErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006340)
)
adTASrmActiveRlsErrorClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseStatus"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseErrorBitmask"))
)
if mibBuilder.loadTexts:
    adTASrmActiveRlsErrorClear.setStatus(
        "current"
    )

adTASrmActiveRlsErrorActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006341)
)
adTASrmActiveRlsErrorActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseStatus"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseErrorBitmask"))
)
if mibBuilder.loadTexts:
    adTASrmActiveRlsErrorActive.setStatus(
        "current"
    )

adTASrmBackupRlsErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006342)
)
adTASrmBackupRlsErrorClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseStatus"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseErrorBitmask"))
)
if mibBuilder.loadTexts:
    adTASrmBackupRlsErrorClear.setStatus(
        "current"
    )

adTASrmBackupRlsErrorActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006343)
)
adTASrmBackupRlsErrorActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseStatus"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseErrorBitmask"))
)
if mibBuilder.loadTexts:
    adTASrmBackupRlsErrorActive.setStatus(
        "current"
    )

adTASrmNewActiveRelease = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006344)
)
adTASrmNewActiveRelease.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"))
)
if mibBuilder.loadTexts:
    adTASrmNewActiveRelease.setStatus(
        "current"
    )

adTASrmRlsDownloadStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006346)
)
adTASrmRlsDownloadStarted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmDownloadFilename"))
)
if mibBuilder.loadTexts:
    adTASrmRlsDownloadStarted.setStatus(
        "current"
    )

adTASrmRlsDownloadCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006348)
)
adTASrmRlsDownloadCompleted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmDownloadFilename"))
)
if mibBuilder.loadTexts:
    adTASrmRlsDownloadCompleted.setStatus(
        "current"
    )

adTASrmRlsDownloadFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006350)
)
adTASrmRlsDownloadFailed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmDownloadFilename"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmStatus"))
)
if mibBuilder.loadTexts:
    adTASrmRlsDownloadFailed.setStatus(
        "current"
    )

adTASrmRlsBackupStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006352)
)
adTASrmRlsBackupStarted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"))
)
if mibBuilder.loadTexts:
    adTASrmRlsBackupStarted.setStatus(
        "current"
    )

adTASrmRlsBackupCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006354)
)
adTASrmRlsBackupCompleted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"))
)
if mibBuilder.loadTexts:
    adTASrmRlsBackupCompleted.setStatus(
        "current"
    )

adTASrmRlsBackupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006356)
)
adTASrmRlsBackupFailed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmReleaseFilename"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlSrmStatus"))
)
if mibBuilder.loadTexts:
    adTASrmRlsBackupFailed.setStatus(
        "current"
    )

adTASysCtrlAlarmSeverityChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006359)
)
adTASysCtrlAlarmSeverityChanged.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlAlarmSeverityLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlAlarmSeverityChanged.setStatus(
        "current"
    )

adTASysCtrlDeviceComFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006360)
)
adTASysCtrlDeviceComFail.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlDeviceComFail.setStatus(
        "current"
    )

adTASysCtrlSwdnldStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006363)
)
adTASysCtrlSwdnldStarted.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlSwdnldStarted.setStatus(
        "current"
    )

adTASysCtrlSwdnldComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006365)
)
adTASysCtrlSwdnldComplete.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlSwdnldComplete.setStatus(
        "current"
    )

adTASysCtrlSwdnldFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006367)
)
adTASysCtrlSwdnldFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlSwdnldFailure.setStatus(
        "current"
    )

adTAeSysSystemDataError = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006372)
)
adTAeSysSystemDataError.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaDataLossDescription"))
)
if mibBuilder.loadTexts:
    adTAeSysSystemDataError.setStatus(
        "current"
    )

adTAPowerSheddingServerTimeoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006373)
)
adTAPowerSheddingServerTimeoutClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedRemoteServerIP"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedStatus"))
)
if mibBuilder.loadTexts:
    adTAPowerSheddingServerTimeoutClear.setStatus(
        "current"
    )

adTAPowerSheddingServerTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006374)
)
adTAPowerSheddingServerTimeout.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedRemoteServerIP"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysCtrlPowerShedStatus"))
)
if mibBuilder.loadTexts:
    adTAPowerSheddingServerTimeout.setStatus(
        "current"
    )

adTASysCtrlCardSensed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006376)
)
adTASysCtrlCardSensed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlCardSensed.setStatus(
        "current"
    )

adTASysCtrlCardNotSensed = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006377)
)
adTASysCtrlCardNotSensed.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlCardNotSensed.setStatus(
        "current"
    )

adTASysCtrlCardReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006378)
)
adTASysCtrlCardReady.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlCardReady.setStatus(
        "current"
    )

adTASysCtrlCardNotReady = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006379)
)
adTASysCtrlCardNotReady.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adTASysCtrlCardNotReady.setStatus(
        "current"
    )

adTaSysCtrlAutoUpgradeEOSSWarningClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006380)
)
adTaSysCtrlAutoUpgradeEOSSWarningClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeEOSSWarningClear.setStatus(
        "current"
    )

adTaSysCtrlAutoUpgradeEOSSWarningActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006381)
)
adTaSysCtrlAutoUpgradeEOSSWarningActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeEOSSWarningActive.setStatus(
        "current"
    )

adTaSysCtrlAutoUpgradeEOSSDeniedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006382)
)
adTaSysCtrlAutoUpgradeEOSSDeniedClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeEOSSDeniedClear.setStatus(
        "current"
    )

adTaSysCtrlAutoUpgradeEOSSDeniedActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006383)
)
adTaSysCtrlAutoUpgradeEOSSDeniedActive.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"))
)
if mibBuilder.loadTexts:
    adTaSysCtrlAutoUpgradeEOSSDeniedActive.setStatus(
        "current"
    )

adTASysConfigurationChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 0, 1006384)
)
adTASysConfigurationChange.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTASysLastConfigChangeAlarmTime"))
)
if mibBuilder.loadTexts:
    adTASysConfigurationChange.setStatus(
        "current"
    )

adTaSysCtrlRebootException = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 170, 0, 1006368)
)
adTaSysCtrlRebootException.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT-MIB", "adTaSysCtrlRebootLastStatus"))
)
if mibBuilder.loadTexts:
    adTaSysCtrlRebootException.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TACONTROLER-PRODUCT-MIB",
    **{"adTaControllerMgmt": adTaControllerMgmt,
       "adTaControllerMgmtTraps": adTaControllerMgmtTraps,
       "adTASetSingleServiceStateMsgFail": adTASetSingleServiceStateMsgFail,
       "adTAGetSingleServiceStateMsgFail": adTAGetSingleServiceStateMsgFail,
       "adTASetAllServiceStateMsgFail": adTASetAllServiceStateMsgFail,
       "adTAGetAllServiceStateMsgFail": adTAGetAllServiceStateMsgFail,
       "adTACriticalAudibleRelayTestClear": adTACriticalAudibleRelayTestClear,
       "adTACriticalAudibleRelayTestActive": adTACriticalAudibleRelayTestActive,
       "adTACriticalVisualRelayTestClear": adTACriticalVisualRelayTestClear,
       "adTACriticalVisualRelayTestActive": adTACriticalVisualRelayTestActive,
       "adTAMajAudibleRelayTestClear": adTAMajAudibleRelayTestClear,
       "adTAMajAudibleRelayTestActive": adTAMajAudibleRelayTestActive,
       "adTAMajVisualRelayTestClear": adTAMajVisualRelayTestClear,
       "adTAMajVisualRelayTestActive": adTAMajVisualRelayTestActive,
       "adTAMinorAudibleRelayTestClear": adTAMinorAudibleRelayTestClear,
       "adTAMinorAudibleRelayTestActive": adTAMinorAudibleRelayTestActive,
       "adTAMinorVisualRelayTestClear": adTAMinorVisualRelayTestClear,
       "adTAMinorVisualRelayTestActive": adTAMinorVisualRelayTestActive,
       "adTAAux1RelayTestClear": adTAAux1RelayTestClear,
       "adTAAux1RelayTestActive": adTAAux1RelayTestActive,
       "adTAAux2RelayTestClear": adTAAux2RelayTestClear,
       "adTAAux2RelayTestActive": adTAAux2RelayTestActive,
       "adTACleiCodeMisMatchClear": adTACleiCodeMisMatchClear,
       "adTACleiCodeMisMatch": adTACleiCodeMisMatch,
       "adTAPowerSheddingInputDeAsserted": adTAPowerSheddingInputDeAsserted,
       "adTAPowerSheddingInputAsserted": adTAPowerSheddingInputAsserted,
       "adTAPowerSheddingDeActivated": adTAPowerSheddingDeActivated,
       "adTAPowerSheddingActivated": adTAPowerSheddingActivated,
       "adTAFanMPowerAFailClear": adTAFanMPowerAFailClear,
       "adTAFanMPowerAFail": adTAFanMPowerAFail,
       "adTAFanMPowerBFailClear": adTAFanMPowerBFailClear,
       "adTAFanMPowerBFail": adTAFanMPowerBFail,
       "adTASrmActiveRlsErrorClear": adTASrmActiveRlsErrorClear,
       "adTASrmActiveRlsErrorActive": adTASrmActiveRlsErrorActive,
       "adTASrmBackupRlsErrorClear": adTASrmBackupRlsErrorClear,
       "adTASrmBackupRlsErrorActive": adTASrmBackupRlsErrorActive,
       "adTASrmNewActiveRelease": adTASrmNewActiveRelease,
       "adTASrmRlsDownloadStarted": adTASrmRlsDownloadStarted,
       "adTASrmRlsDownloadCompleted": adTASrmRlsDownloadCompleted,
       "adTASrmRlsDownloadFailed": adTASrmRlsDownloadFailed,
       "adTASrmRlsBackupStarted": adTASrmRlsBackupStarted,
       "adTASrmRlsBackupCompleted": adTASrmRlsBackupCompleted,
       "adTASrmRlsBackupFailed": adTASrmRlsBackupFailed,
       "adTASysCtrlAlarmSeverityChanged": adTASysCtrlAlarmSeverityChanged,
       "adTASysCtrlDeviceComFail": adTASysCtrlDeviceComFail,
       "adTASysCtrlSwdnldStarted": adTASysCtrlSwdnldStarted,
       "adTASysCtrlSwdnldComplete": adTASysCtrlSwdnldComplete,
       "adTASysCtrlSwdnldFailure": adTASysCtrlSwdnldFailure,
       "adTAeSysSystemDataError": adTAeSysSystemDataError,
       "adTAPowerSheddingServerTimeoutClear": adTAPowerSheddingServerTimeoutClear,
       "adTAPowerSheddingServerTimeout": adTAPowerSheddingServerTimeout,
       "adTASysCtrlCardSensed": adTASysCtrlCardSensed,
       "adTASysCtrlCardNotSensed": adTASysCtrlCardNotSensed,
       "adTASysCtrlCardReady": adTASysCtrlCardReady,
       "adTASysCtrlCardNotReady": adTASysCtrlCardNotReady,
       "adTaSysCtrlAutoUpgradeEOSSWarningClear": adTaSysCtrlAutoUpgradeEOSSWarningClear,
       "adTaSysCtrlAutoUpgradeEOSSWarningActive": adTaSysCtrlAutoUpgradeEOSSWarningActive,
       "adTaSysCtrlAutoUpgradeEOSSDeniedClear": adTaSysCtrlAutoUpgradeEOSSDeniedClear,
       "adTaSysCtrlAutoUpgradeEOSSDeniedActive": adTaSysCtrlAutoUpgradeEOSSDeniedActive,
       "adTASysConfigurationChange": adTASysConfigurationChange,
       "adTaSysCtrlShelf": adTaSysCtrlShelf,
       "adTASysCtrlShelfTable": adTASysCtrlShelfTable,
       "adTASysCtrlShelfEntry": adTASysCtrlShelfEntry,
       "adTASysCtrlShelfNumber": adTASysCtrlShelfNumber,
       "adTASysCtrlModuleRemovedStatus": adTASysCtrlModuleRemovedStatus,
       "adTASysCtrlAlarmSeverityLevel": adTASysCtrlAlarmSeverityLevel,
       "adTASysConfigurationChangeTimer": adTASysConfigurationChangeTimer,
       "adTASysLastConfigChangeAlarmTime": adTASysLastConfigChangeAlarmTime,
       "adTaSysCtrlSlot": adTaSysCtrlSlot,
       "adTASysCtrlModuleTable": adTASysCtrlModuleTable,
       "adTASysCtrlModuleEntry": adTASysCtrlModuleEntry,
       "adTASysCtrlModuleNumber": adTASysCtrlModuleNumber,
       "adTASysCtrlModuleDiscoveryStatus": adTASysCtrlModuleDiscoveryStatus,
       "adTaSysCtrlScaMgmt": adTaSysCtrlScaMgmt,
       "adTaSysCtrlSCAConfigChangeVersion": adTaSysCtrlSCAConfigChangeVersion,
       "adTaSysCtrlScaTable": adTaSysCtrlScaTable,
       "adTaSysCtrlScaEntry": adTaSysCtrlScaEntry,
       "adTaSysCtrlCUShelfNumber": adTaSysCtrlCUShelfNumber,
       "adTaSysCtrlSCAProvItemChanged": adTaSysCtrlSCAProvItemChanged,
       "adTaSysCtrlSCAPresentCards": adTaSysCtrlSCAPresentCards,
       "adTaSysCtrlSCASlotsWithProvData": adTaSysCtrlSCASlotsWithProvData,
       "adTaSysCtrlSCAoptRestoreCardBitmask": adTaSysCtrlSCAoptRestoreCardBitmask,
       "adTaSysCtrlProvMgmt": adTaSysCtrlProvMgmt,
       "adTATIDSysNameSyncEnable": adTATIDSysNameSyncEnable,
       "adTATL1echoEnable": adTATL1echoEnable,
       "adTATL1PortExchange": adTATL1PortExchange,
       "adTAScmEthernetInterfaceModeTable": adTAScmEthernetInterfaceModeTable,
       "adTAScmEthernetInterfaceModeEntry": adTAScmEthernetInterfaceModeEntry,
       "adTAScmEthernetInterfaceMode": adTAScmEthernetInterfaceMode,
       "adTaSysCtrlPowerShed": adTaSysCtrlPowerShed,
       "adTASysCtrlPowerShedEnable": adTASysCtrlPowerShedEnable,
       "adTASysCtrlPowerShedAlmInput": adTASysCtrlPowerShedAlmInput,
       "adTASysCtrlPowerShedActivateDelay": adTASysCtrlPowerShedActivateDelay,
       "adTASysCtrlPowerShedDeActivateDelay": adTASysCtrlPowerShedDeActivateDelay,
       "adTASysCtrlPowerShedACFailAlarmDescription": adTASysCtrlPowerShedACFailAlarmDescription,
       "adTASysCtrlPowerShedACFailAlarmSeverity": adTASysCtrlPowerShedACFailAlarmSeverity,
       "adTASysCtrlPowerShedACFailAlarmAIDIndex": adTASysCtrlPowerShedACFailAlarmAIDIndex,
       "adTASysCtrlPowerShedACFailAlarmConditionCode": adTASysCtrlPowerShedACFailAlarmConditionCode,
       "adTASysCtrlPowerShedStatus": adTASysCtrlPowerShedStatus,
       "adTASysCtrlPowerShedCountDown": adTASysCtrlPowerShedCountDown,
       "adTASysCtrlPowerShedStateAlarmSeverity": adTASysCtrlPowerShedStateAlarmSeverity,
       "adTASysCtrlPowerShedRemoteServerIP": adTASysCtrlPowerShedRemoteServerIP,
       "adTaSysCtrlSysSSHMgmt": adTaSysCtrlSysSSHMgmt,
       "adTaSysCtrlSysSshKeyMgmt": adTaSysCtrlSysSshKeyMgmt,
       "adTaSysCtrlCurrentKeySize": adTaSysCtrlCurrentKeySize,
       "adTaSysCtrlKeySize": adTaSysCtrlKeySize,
       "adTaSysCtrlGenerateKeys": adTaSysCtrlGenerateKeys,
       "adTaSysCtrlGenKeyStatus": adTaSysCtrlGenKeyStatus,
       "adTaSysCtrlReKeyTimeout": adTaSysCtrlReKeyTimeout,
       "adTaSysCtrlReKeyDataLimit": adTaSysCtrlReKeyDataLimit,
       "adTaSysCtrlSysRlsMgmt": adTaSysCtrlSysRlsMgmt,
       "adTaSysCtrlSysRlsTable": adTaSysCtrlSysRlsTable,
       "adTaSysCtrlSysRlsEntry": adTaSysCtrlSysRlsEntry,
       "adTaSysCtrlSrmReleaseIndex": adTaSysCtrlSrmReleaseIndex,
       "adTaSysCtrlSrmReleaseName": adTaSysCtrlSrmReleaseName,
       "adTaSysCtrlSrmReleaseFilename": adTaSysCtrlSrmReleaseFilename,
       "adTaSysCtrlSrmReleaseStatus": adTaSysCtrlSrmReleaseStatus,
       "adTaSysCtrlSrmReleaseMemoryUsageKB": adTaSysCtrlSrmReleaseMemoryUsageKB,
       "adTaSysCtrlSrmReleaseFileCount": adTaSysCtrlSrmReleaseFileCount,
       "adTaSysCtrlSrmReleaseProductCount": adTaSysCtrlSrmReleaseProductCount,
       "adTaSysCtrlSrmReleaseFilesTableEntries": adTaSysCtrlSrmReleaseFilesTableEntries,
       "adTaSysCtrlSrmReleaseErrorBitmask": adTaSysCtrlSrmReleaseErrorBitmask,
       "adTaSysCtrlSysRlsFilesTable": adTaSysCtrlSysRlsFilesTable,
       "adTaSysCtrlSysRlsFilesEntry": adTaSysCtrlSysRlsFilesEntry,
       "adTaSysCtrlSrmRlsFilesIndex": adTaSysCtrlSrmRlsFilesIndex,
       "adTaSysCtrlSrmRlsFilesInfo": adTaSysCtrlSrmRlsFilesInfo,
       "adTaSysCtrlSrmCancel": adTaSysCtrlSrmCancel,
       "adTaSysCtrlSrmActivateBrls": adTaSysCtrlSrmActivateBrls,
       "adTaSysCtrlSrmBackupArls": adTaSysCtrlSrmBackupArls,
       "adTaSysCtrlSrmDownloadInitiate": adTaSysCtrlSrmDownloadInitiate,
       "adTaSysCtrlSrmDownloadSameFiles": adTaSysCtrlSrmDownloadSameFiles,
       "adTaSysCtrlSrmDownloadRetries": adTaSysCtrlSrmDownloadRetries,
       "adTaSysCtrlSrmDownloadFilename": adTaSysCtrlSrmDownloadFilename,
       "adTaSysCtrlSrmDownloadBasepath": adTaSysCtrlSrmDownloadBasepath,
       "adTaSysCtrlSrmScheduledDownload": adTaSysCtrlSrmScheduledDownload,
       "adTaSysCtrlSrmScheduledActivate": adTaSysCtrlSrmScheduledActivate,
       "adTaSysCtrlSrmValidateInterval": adTaSysCtrlSrmValidateInterval,
       "adTaSysCtrlSrmStatus": adTaSysCtrlSrmStatus,
       "adTaSysCtrlSrmAutoUpgradeCtrl": adTaSysCtrlSrmAutoUpgradeCtrl,
       "adTaSysCtrlAutoUpgrade": adTaSysCtrlAutoUpgrade,
       "adTaSysCtrlAutoUpgradeActiveSlots": adTaSysCtrlAutoUpgradeActiveSlots,
       "adTaSysCtrlAutoUpgradeErrorSlots": adTaSysCtrlAutoUpgradeErrorSlots,
       "adTaSysCtrlAutoUpgradeNeededSlots": adTaSysCtrlAutoUpgradeNeededSlots,
       "adTaSysCtrlAutoUpgradeDeferredResetSlots": adTaSysCtrlAutoUpgradeDeferredResetSlots,
       "adTaSysCtrlAutoUpgradeActiveSlotsBitmask": adTaSysCtrlAutoUpgradeActiveSlotsBitmask,
       "adTaSysCtrlAutoUpgradeErrorSlotsBitmask": adTaSysCtrlAutoUpgradeErrorSlotsBitmask,
       "adTaSysCtrlAutoUpgradeNeededSlotsBitmask": adTaSysCtrlAutoUpgradeNeededSlotsBitmask,
       "adTaSysCtrlAutoUpgradeDeferResetSlotsBitmask": adTaSysCtrlAutoUpgradeDeferResetSlotsBitmask,
       "adTaSysCtrlAutoUpgradeUseSCR": adTaSysCtrlAutoUpgradeUseSCR,
       "adTaSysCtrlAutoUpgradeSCRStatus": adTaSysCtrlAutoUpgradeSCRStatus,
       "adTaSysCtrlAutoUpgradeEOSSCapable": adTaSysCtrlAutoUpgradeEOSSCapable,
       "adTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask": adTaSysCtrlAutoUpgradeEOSSWarnSlotsBitmask,
       "adTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask": adTaSysCtrlAutoUpgradeEOSSDenySlotsBitmask,
       "adTaSysCtrlFileExport": adTaSysCtrlFileExport,
       "adTaSysCtrlSystemLog": adTaSysCtrlSystemLog,
       "adTASystemEventLogAutoExportMode": adTASystemEventLogAutoExportMode,
       "adTaSystemEventLogPreventFileOverlap": adTaSystemEventLogPreventFileOverlap,
       "adTaSystemEventLogFilePrefix": adTaSystemEventLogFilePrefix,
       "adTaSystemEventLogFileSuffix": adTaSystemEventLogFileSuffix,
       "adTaSystemEventLogRemoteDirectory": adTaSystemEventLogRemoteDirectory,
       "adTaSystemEventLogRemoteFileName": adTaSystemEventLogRemoteFileName,
       "adTaSystemEventLogAutoExportNumberOfDays": adTaSystemEventLogAutoExportNumberOfDays,
       "adTaSystemEventLogHourOfDayToExportSysLog": adTaSystemEventLogHourOfDayToExportSysLog,
       "adTaSystemEventLogMinuteOfDayToExportSysLog": adTaSystemEventLogMinuteOfDayToExportSysLog,
       "adTaSystemEventLogExportRetries": adTaSystemEventLogExportRetries,
       "adTaSystemEventLogRemotetHost": adTaSystemEventLogRemotetHost,
       "adTaSystemEventLogPrevExportTime": adTaSystemEventLogPrevExportTime,
       "adTaSystemEventLogPrevExportStatus": adTaSystemEventLogPrevExportStatus,
       "adTaSystemEventLogNextAutoExportScheduled": adTaSystemEventLogNextAutoExportScheduled,
       "adTaSystemEventLogManualExport": adTaSystemEventLogManualExport,
       "adTaSystemEventLogCurrentStatus": adTaSystemEventLogCurrentStatus,
       "adTaSystemEventLogRemotetHostInetAddressType": adTaSystemEventLogRemotetHostInetAddressType,
       "adTaSystemEventLogRemotetHostInetAddress": adTaSystemEventLogRemotetHostInetAddress,
       "adTaSysCtrlGeneralFileExport": adTaSysCtrlGeneralFileExport,
       "adTaGenExportRemotetHost": adTaGenExportRemotetHost,
       "adTaGeneralExportRemoteHostMethod": adTaGeneralExportRemoteHostMethod,
       "adTaGenExportRemoteFilePath": adTaGenExportRemoteFilePath,
       "adTaGenExportStatus": adTaGenExportStatus,
       "adTaGenExportFileName": adTaGenExportFileName,
       "adTaGeneralExportRetries": adTaGeneralExportRetries,
       "adTaGenExportPrefixString": adTaGenExportPrefixString,
       "adTaGenExportSuffixString": adTaGenExportSuffixString,
       "adTaGenExportExceptionReportEnable": adTaGenExportExceptionReportEnable,
       "adTaGenExportRemotetHostInetAddressType": adTaGenExportRemotetHostInetAddressType,
       "adTaGenExportRemotetHostInetAddress": adTaGenExportRemotetHostInetAddress,
       "adTaSysCtrlSNTP": adTaSysCtrlSNTP,
       "adTaSntpServer": adTaSntpServer,
       "adTaDSTAutomaticAdjustment": adTaDSTAutomaticAdjustment,
       "adTaLocalTimeZone": adTaLocalTimeZone,
       "adTaRefreshPeriod": adTaRefreshPeriod,
       "adTaTimeProtocolState": adTaTimeProtocolState,
       "adTaSntpOperationStaus": adTaSntpOperationStaus,
       "adTaSntpTimeOutCount": adTaSntpTimeOutCount,
       "adTaSntpGMTtimeZoneString": adTaSntpGMTtimeZoneString,
       "adTaSntpServer2": adTaSntpServer2,
       "adTaSntpServer3": adTaSntpServer3,
       "adTaSntpServer4": adTaSntpServer4,
       "adTaSntpTimeOutProv": adTaSntpTimeOutProv,
       "adTaSntpTimeRetryProv": adTaSntpTimeRetryProv,
       "adTaSntpTimeOutCountServer2": adTaSntpTimeOutCountServer2,
       "adTaSntpTimeOutCountServer3": adTaSntpTimeOutCountServer3,
       "adTaSntpTimeOutCountServer4": adTaSntpTimeOutCountServer4,
       "adTaSntpCurrentServer": adTaSntpCurrentServer,
       "adTaSysLog": adTaSysLog,
       "adTaSysLogServer": adTaSysLogServer,
       "adTaSysLogServer2": adTaSysLogServer2,
       "adTaSysLogMode": adTaSysLogMode,
       "adTaExportCtrlToSysLog": adTaExportCtrlToSysLog,
       "adTaSysLogServer3": adTaSysLogServer3,
       "adTaSysLogServer4": adTaSysLogServer4,
       "adTaSysLogServerTable": adTaSysLogServerTable,
       "adTaSysLogServerEntry": adTaSysLogServerEntry,
       "adTaSysLogServerIndex": adTaSysLogServerIndex,
       "adTaSysLogServerAddressType": adTaSysLogServerAddressType,
       "adTaSysLogServerInetAddress": adTaSysLogServerInetAddress,
       "adTaDhcpServer": adTaDhcpServer,
       "adTaDhcpNetworkInterface": adTaDhcpNetworkInterface,
       "adTaDhcpSubNetMask": adTaDhcpSubNetMask,
       "adTaDhcpSubNetLength": adTaDhcpSubNetLength,
       "adTaDhcpStartIpAddress": adTaDhcpStartIpAddress,
       "adTaDhcpEndIpAddress": adTaDhcpEndIpAddress,
       "adTaDhcpSubNetAddress": adTaDhcpSubNetAddress,
       "adTaDhcpLeasDurationHours": adTaDhcpLeasDurationHours,
       "adTaDhcpLeasDurationMintues": adTaDhcpLeasDurationMintues,
       "adTaDhcpServerCommands": adTaDhcpServerCommands,
       "adTaDhcpServerOperationStatus": adTaDhcpServerOperationStatus,
       "adTaDhcpServerStatusTable": adTaDhcpServerStatusTable,
       "adTaDhcpServerStatusTableEntry": adTaDhcpServerStatusTableEntry,
       "adTaDhcpServerStatusIndex": adTaDhcpServerStatusIndex,
       "adTaDhcpServerStatus": adTaDhcpServerStatus,
       "adTaModuleReset": adTaModuleReset,
       "adTaModuleResetSlot": adTaModuleResetSlot,
       "adTaModuleResetCtrl": adTaModuleResetCtrl,
       "adTaSecurity": adTaSecurity,
       "adTaSSLConfiguration": adTaSSLConfiguration,
       "adTaSSLKeySizeBits": adTaSSLKeySizeBits,
       "adTaSSLKeyType": adTaSSLKeyType,
       "adTaSSLInputPassword": adTaSSLInputPassword,
       "adTaSSLOutputPassword": adTaSSLOutputPassword,
       "adTaSSLCertificateCountry": adTaSSLCertificateCountry,
       "adTaSSLCertificateStateOrProvince": adTaSSLCertificateStateOrProvince,
       "adTaSSLCertificateChallengePassword": adTaSSLCertificateChallengePassword,
       "adTaSSLCertificateLocality": adTaSSLCertificateLocality,
       "adTaSSLCertificateOrganization": adTaSSLCertificateOrganization,
       "adTaSSLCertificateOrganizationalUnitName": adTaSSLCertificateOrganizationalUnitName,
       "adTaSSLCertificateCommonName": adTaSSLCertificateCommonName,
       "adTaSSLCertificateEmailAddress": adTaSSLCertificateEmailAddress,
       "adTaGenerateNewSSLKeys": adTaGenerateNewSSLKeys,
       "adTaGenerateNewSSLCertificateRequest": adTaGenerateNewSSLCertificateRequest,
       "adTaSSLuseImportCertificate": adTaSSLuseImportCertificate,
       "adTaSSLRemoteKeyDownload": adTaSSLRemoteKeyDownload,
       "adTaSSLRemotePrivateKeyFileName": adTaSSLRemotePrivateKeyFileName,
       "adTaSSLRemotedPublicKeyFileName": adTaSSLRemotedPublicKeyFileName,
       "adTaSSLRemoteCertificateFileName": adTaSSLRemoteCertificateFileName,
       "adTaSSLRemoteKeysDownLoadStatus": adTaSSLRemoteKeysDownLoadStatus,
       "adTaSSLCertificateRequestFileName": adTaSSLCertificateRequestFileName,
       "adTaSSLCertificateRequestExport": adTaSSLCertificateRequestExport,
       "adTaSSLCertificateImport": adTaSSLCertificateImport,
       "adTaSSLCertificateImportStatus": adTaSSLCertificateImportStatus,
       "adTaSSLDownLoadRemoteKeys": adTaSSLDownLoadRemoteKeys,
       "adTaSSLCertificateSigningRequestStatus": adTaSSLCertificateSigningRequestStatus,
       "adTaSSLCertificateSignRequestExportStatus": adTaSSLCertificateSignRequestExportStatus,
       "adTaSSLSignedCertificateImportStatus": adTaSSLSignedCertificateImportStatus,
       "adTaSysCtrlReboot": adTaSysCtrlReboot,
       "adTaSysCtrlRebootTraps": adTaSysCtrlRebootTraps,
       "adTaSysCtrlRebootException": adTaSysCtrlRebootException,
       "adTaSysCtrlRebootOperMode": adTaSysCtrlRebootOperMode,
       "adTaSysCtrlRebootSchedDateTime": adTaSysCtrlRebootSchedDateTime,
       "adTaSysCtrlRebootInitiate": adTaSysCtrlRebootInitiate,
       "adTaSysCtrlRebootLastStatus": adTaSysCtrlRebootLastStatus,
       "adTaSysCtrlRebootArmedStatus": adTaSysCtrlRebootArmedStatus,
       "adTaSysCtrlRebootMode": adTaSysCtrlRebootMode,
       "adTaSysAlarmVarbinds": adTaSysAlarmVarbinds,
       "adTaDataLossDescription": adTaDataLossDescription,
       "adTaSysCtrlVLANBridge": adTaSysCtrlVLANBridge,
       "adTaSysCtrlVLANBridgeMode": adTaSysCtrlVLANBridgeMode,
       "adTaSysCtrlVLANBridgeInterface": adTaSysCtrlVLANBridgeInterface}
)
