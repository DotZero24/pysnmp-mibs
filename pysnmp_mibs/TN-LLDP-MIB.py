# SNMP MIB module (TN-LLDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-LLDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:52:33 2025
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

(AddressFamilyNumbers,) = mibBuilder.importSymbols(
    "IANA-ADDRESS-FAMILY-NUMBERS-MIB",
    "AddressFamilyNumbers")

(LldpChassisId,
 LldpChassisIdSubtype,
 LldpManAddrIfSubtype,
 LldpManAddress,
 LldpPortId,
 LldpPortIdSubtype,
 LldpSystemCapabilitiesMap) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpChassisId",
    "LldpChassisIdSubtype",
    "LldpManAddrIfSubtype",
    "LldpManAddress",
    "LldpPortId",
    "LldpPortIdSubtype",
    "LldpSystemCapabilitiesMap")

(TimeFilter,
 ZeroBasedCounter32) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter",
    "ZeroBasedCounter32")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnPortPortID,) = mibBuilder.importSymbols(
    "TN-PORT-MIB",
    "tnPortPortID")

(TmnxEnabledDisabled,) = mibBuilder.importSymbols(
    "TN-TC-MIB",
    "TmnxEnabledDisabled")

(tnSRMIBModules,
 tnSRNotifyPrefix,
 tnSRObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSRMIBModules",
    "tnSRNotifyPrefix",
    "tnSRObjs")

(tnSysSwitchId,) = mibBuilder.importSymbols(
    "TROPIC-SYSTEM-MIB",
    "tnSysSwitchId")


# MODULE-IDENTITY

tnLldpMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 5, 1, 3, 59)
)
if mibBuilder.loadTexts:
    tnLldpMIBModule.setRevisions(
        ("2020-09-25 00:00",
         "2019-04-19 00:00",
         "2017-01-13 00:00",
         "2016-12-17 00:00",
         "2016-06-21 00:00",
         "2016-03-05 00:00",
         "2016-02-23 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxLldpDestAddressTableIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class TmnxLldpManAddressIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("system", 1)
    )



# MIB Managed Objects in the order of their OIDs

_TnLldpObjects_ObjectIdentity = ObjectIdentity
tnLldpObjects = _TnLldpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59)
)
_TnLldpConfiguration_ObjectIdentity = ObjectIdentity
tnLldpConfiguration = _TnLldpConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1)
)
_TnLldpConfigTable_Object = MibTable
tnLldpConfigTable = _TnLldpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1)
)
if mibBuilder.loadTexts:
    tnLldpConfigTable.setStatus("current")
_TnLldpConfigEntry_Object = MibTableRow
tnLldpConfigEntry = _TnLldpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1)
)
tnLldpConfigEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnLldpConfigEntry.setStatus("current")


class _TnLldpMessageTxInterval_Type(Integer32):
    """Custom type tnLldpMessageTxInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 32768),
    )


_TnLldpMessageTxInterval_Type.__name__ = "Integer32"
_TnLldpMessageTxInterval_Object = MibTableColumn
tnLldpMessageTxInterval = _TnLldpMessageTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 1),
    _TnLldpMessageTxInterval_Type()
)
tnLldpMessageTxInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpMessageTxInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpMessageTxInterval.setUnits("seconds")


class _TnLldpMessageTxHoldMultiplier_Type(Integer32):
    """Custom type tnLldpMessageTxHoldMultiplier based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_TnLldpMessageTxHoldMultiplier_Type.__name__ = "Integer32"
_TnLldpMessageTxHoldMultiplier_Object = MibTableColumn
tnLldpMessageTxHoldMultiplier = _TnLldpMessageTxHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 2),
    _TnLldpMessageTxHoldMultiplier_Type()
)
tnLldpMessageTxHoldMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpMessageTxHoldMultiplier.setStatus("current")


class _TnLldpReinitDelay_Type(Integer32):
    """Custom type tnLldpReinitDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TnLldpReinitDelay_Type.__name__ = "Integer32"
_TnLldpReinitDelay_Object = MibTableColumn
tnLldpReinitDelay = _TnLldpReinitDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 3),
    _TnLldpReinitDelay_Type()
)
tnLldpReinitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpReinitDelay.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpReinitDelay.setUnits("seconds")


class _TnLldpTxDelay_Type(Integer32):
    """Custom type tnLldpTxDelay based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8192),
    )


_TnLldpTxDelay_Type.__name__ = "Integer32"
_TnLldpTxDelay_Object = MibTableColumn
tnLldpTxDelay = _TnLldpTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 4),
    _TnLldpTxDelay_Type()
)
tnLldpTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpTxDelay.setUnits("seconds")


class _TnLldpNotificationInterval_Type(Integer32):
    """Custom type tnLldpNotificationInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 3600),
    )


_TnLldpNotificationInterval_Type.__name__ = "Integer32"
_TnLldpNotificationInterval_Object = MibTableColumn
tnLldpNotificationInterval = _TnLldpNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 5),
    _TnLldpNotificationInterval_Type()
)
tnLldpNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpNotificationInterval.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpNotificationInterval.setUnits("seconds")


class _TnLldpTxCreditMax_Type(Integer32):
    """Custom type tnLldpTxCreditMax based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TnLldpTxCreditMax_Type.__name__ = "Integer32"
_TnLldpTxCreditMax_Object = MibTableColumn
tnLldpTxCreditMax = _TnLldpTxCreditMax_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 6),
    _TnLldpTxCreditMax_Type()
)
tnLldpTxCreditMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpTxCreditMax.setStatus("current")


class _TnLldpMessageFastTx_Type(Integer32):
    """Custom type tnLldpMessageFastTx based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_TnLldpMessageFastTx_Type.__name__ = "Integer32"
_TnLldpMessageFastTx_Object = MibTableColumn
tnLldpMessageFastTx = _TnLldpMessageFastTx_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 7),
    _TnLldpMessageFastTx_Type()
)
tnLldpMessageFastTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpMessageFastTx.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpMessageFastTx.setUnits("seconds")


class _TnLldpMessageFastTxInit_Type(Integer32):
    """Custom type tnLldpMessageFastTxInit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_TnLldpMessageFastTxInit_Type.__name__ = "Integer32"
_TnLldpMessageFastTxInit_Object = MibTableColumn
tnLldpMessageFastTxInit = _TnLldpMessageFastTxInit_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 8),
    _TnLldpMessageFastTxInit_Type()
)
tnLldpMessageFastTxInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpMessageFastTxInit.setStatus("current")
_TnLldpAdminStatus_Type = TmnxEnabledDisabled
_TnLldpAdminStatus_Object = MibTableColumn
tnLldpAdminStatus = _TnLldpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 1, 1, 9),
    _TnLldpAdminStatus_Type()
)
tnLldpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpAdminStatus.setStatus("current")
_TnLldpPortConfigTable_Object = MibTable
tnLldpPortConfigTable = _TnLldpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 2)
)
if mibBuilder.loadTexts:
    tnLldpPortConfigTable.setStatus("current")
_TnLldpPortConfigEntry_Object = MibTableRow
tnLldpPortConfigEntry = _TnLldpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 2, 1)
)
tnLldpPortConfigEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpPortCfgDestAddressIndex"),
)
if mibBuilder.loadTexts:
    tnLldpPortConfigEntry.setStatus("current")
_TnLldpPortCfgDestAddressIndex_Type = TmnxLldpDestAddressTableIndex
_TnLldpPortCfgDestAddressIndex_Object = MibTableColumn
tnLldpPortCfgDestAddressIndex = _TnLldpPortCfgDestAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 2, 1, 1),
    _TnLldpPortCfgDestAddressIndex_Type()
)
tnLldpPortCfgDestAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpPortCfgDestAddressIndex.setStatus("current")


class _TnLldpPortCfgAdminStatus_Type(Integer32):
    """Custom type tnLldpPortCfgAdminStatus based on Integer32"""
    defaultValue = 4

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
        *(("txOnly", 1),
          ("rxOnly", 2),
          ("txAndRx", 3),
          ("disabled", 4))
    )


_TnLldpPortCfgAdminStatus_Type.__name__ = "Integer32"
_TnLldpPortCfgAdminStatus_Object = MibTableColumn
tnLldpPortCfgAdminStatus = _TnLldpPortCfgAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 2, 1, 2),
    _TnLldpPortCfgAdminStatus_Type()
)
tnLldpPortCfgAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpPortCfgAdminStatus.setStatus("current")


class _TnLldpPortCfgNotifyEnable_Type(TruthValue):
    """Custom type tnLldpPortCfgNotifyEnable based on TruthValue"""
    defaultValue = 2


_TnLldpPortCfgNotifyEnable_Type.__name__ = "TruthValue"
_TnLldpPortCfgNotifyEnable_Object = MibTableColumn
tnLldpPortCfgNotifyEnable = _TnLldpPortCfgNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 2, 1, 3),
    _TnLldpPortCfgNotifyEnable_Type()
)
tnLldpPortCfgNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpPortCfgNotifyEnable.setStatus("current")


class _TnLldpPortCfgTLVsTxEnable_Type(Bits):
    """Custom type tnLldpPortCfgTLVsTxEnable based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("portDesc", 0),
          ("sysName", 1),
          ("sysDesc", 2),
          ("sysCap", 3))
    )

_TnLldpPortCfgTLVsTxEnable_Type.__name__ = "Bits"
_TnLldpPortCfgTLVsTxEnable_Object = MibTableColumn
tnLldpPortCfgTLVsTxEnable = _TnLldpPortCfgTLVsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 2, 1, 4),
    _TnLldpPortCfgTLVsTxEnable_Type()
)
tnLldpPortCfgTLVsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpPortCfgTLVsTxEnable.setStatus("current")
_TnLldpConfigManAddrPortsTable_Object = MibTable
tnLldpConfigManAddrPortsTable = _TnLldpConfigManAddrPortsTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 3)
)
if mibBuilder.loadTexts:
    tnLldpConfigManAddrPortsTable.setStatus("current")
_TnLldpConfigManAddrPortsEntry_Object = MibTableRow
tnLldpConfigManAddrPortsEntry = _TnLldpConfigManAddrPortsEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 3, 1)
)
tnLldpConfigManAddrPortsEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpPortCfgDestAddressIndex"),
    (0, "TN-LLDP-MIB", "tnLldpPortCfgAddressIndex"),
)
if mibBuilder.loadTexts:
    tnLldpConfigManAddrPortsEntry.setStatus("current")
_TnLldpPortCfgAddressIndex_Type = TmnxLldpManAddressIndex
_TnLldpPortCfgAddressIndex_Object = MibTableColumn
tnLldpPortCfgAddressIndex = _TnLldpPortCfgAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 3, 1, 1),
    _TnLldpPortCfgAddressIndex_Type()
)
tnLldpPortCfgAddressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpPortCfgAddressIndex.setStatus("current")


class _TnLldpPortCfgManAddrTxEnabled_Type(TmnxEnabledDisabled):
    """Custom type tnLldpPortCfgManAddrTxEnabled based on TmnxEnabledDisabled"""
    defaultValue = 2


_TnLldpPortCfgManAddrTxEnabled_Type.__name__ = "TmnxEnabledDisabled"
_TnLldpPortCfgManAddrTxEnabled_Object = MibTableColumn
tnLldpPortCfgManAddrTxEnabled = _TnLldpPortCfgManAddrTxEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 3, 1, 2),
    _TnLldpPortCfgManAddrTxEnabled_Type()
)
tnLldpPortCfgManAddrTxEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnLldpPortCfgManAddrTxEnabled.setStatus("current")
_TnLldpPortCfgManAddrSubtype_Type = AddressFamilyNumbers
_TnLldpPortCfgManAddrSubtype_Object = MibTableColumn
tnLldpPortCfgManAddrSubtype = _TnLldpPortCfgManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 3, 1, 3),
    _TnLldpPortCfgManAddrSubtype_Type()
)
tnLldpPortCfgManAddrSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpPortCfgManAddrSubtype.setStatus("current")
_TnLldpPortCfgManAddress_Type = LldpManAddress
_TnLldpPortCfgManAddress_Object = MibTableColumn
tnLldpPortCfgManAddress = _TnLldpPortCfgManAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 3, 1, 4),
    _TnLldpPortCfgManAddress_Type()
)
tnLldpPortCfgManAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpPortCfgManAddress.setStatus("current")
_TnLldpDestAddressTable_Object = MibTable
tnLldpDestAddressTable = _TnLldpDestAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 4)
)
if mibBuilder.loadTexts:
    tnLldpDestAddressTable.setStatus("current")
_TnLldpDestAddressTableEntry_Object = MibTableRow
tnLldpDestAddressTableEntry = _TnLldpDestAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 4, 1)
)
tnLldpDestAddressTableEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LLDP-MIB", "tnLldpAddressTableIndex"),
)
if mibBuilder.loadTexts:
    tnLldpDestAddressTableEntry.setStatus("current")
_TnLldpAddressTableIndex_Type = TmnxLldpDestAddressTableIndex
_TnLldpAddressTableIndex_Object = MibTableColumn
tnLldpAddressTableIndex = _TnLldpAddressTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 4, 1, 1),
    _TnLldpAddressTableIndex_Type()
)
tnLldpAddressTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpAddressTableIndex.setStatus("current")
_TnLldpDestMacAddress_Type = MacAddress
_TnLldpDestMacAddress_Object = MibTableColumn
tnLldpDestMacAddress = _TnLldpDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 1, 4, 1, 2),
    _TnLldpDestMacAddress_Type()
)
tnLldpDestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpDestMacAddress.setStatus("current")
_TnLldpStatistics_ObjectIdentity = ObjectIdentity
tnLldpStatistics = _TnLldpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2)
)
_TnLldpStatsTxPortTable_Object = MibTable
tnLldpStatsTxPortTable = _TnLldpStatsTxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 1)
)
if mibBuilder.loadTexts:
    tnLldpStatsTxPortTable.setStatus("current")
_TnLldpStatsTxPortEntry_Object = MibTableRow
tnLldpStatsTxPortEntry = _TnLldpStatsTxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 1, 1)
)
tnLldpStatsTxPortEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpStatsTxDestMACAddress"),
)
if mibBuilder.loadTexts:
    tnLldpStatsTxPortEntry.setStatus("current")
_TnLldpStatsTxDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TnLldpStatsTxDestMACAddress_Object = MibTableColumn
tnLldpStatsTxDestMACAddress = _TnLldpStatsTxDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 1, 1, 1),
    _TnLldpStatsTxDestMACAddress_Type()
)
tnLldpStatsTxDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatsTxDestMACAddress.setStatus("current")
_TnLldpStatsTxPortFrames_Type = Counter32
_TnLldpStatsTxPortFrames_Object = MibTableColumn
tnLldpStatsTxPortFrames = _TnLldpStatsTxPortFrames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 1, 1, 2),
    _TnLldpStatsTxPortFrames_Type()
)
tnLldpStatsTxPortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsTxPortFrames.setStatus("current")
_TnLldpStatsTxLLDPDULengthErrs_Type = Counter32
_TnLldpStatsTxLLDPDULengthErrs_Object = MibTableColumn
tnLldpStatsTxLLDPDULengthErrs = _TnLldpStatsTxLLDPDULengthErrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 1, 1, 3),
    _TnLldpStatsTxLLDPDULengthErrs_Type()
)
tnLldpStatsTxLLDPDULengthErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsTxLLDPDULengthErrs.setStatus("current")
_TnLldpStatsRemTable_Object = MibTable
tnLldpStatsRemTable = _TnLldpStatsRemTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 2)
)
if mibBuilder.loadTexts:
    tnLldpStatsRemTable.setStatus("current")
_TnLldpStatsRemEntry_Object = MibTableRow
tnLldpStatsRemEntry = _TnLldpStatsRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 2, 1)
)
tnLldpStatsRemEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnLldpStatsRemEntry.setStatus("current")
_TnLldpStatsRemTablesLastChangeTime_Type = Unsigned32
_TnLldpStatsRemTablesLastChangeTime_Object = MibTableColumn
tnLldpStatsRemTablesLastChangeTime = _TnLldpStatsRemTablesLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 2, 1, 1),
    _TnLldpStatsRemTablesLastChangeTime_Type()
)
tnLldpStatsRemTablesLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesLastChangeTime.setStatus("current")
_TnLldpStatsRemTablesInserts_Type = ZeroBasedCounter32
_TnLldpStatsRemTablesInserts_Object = MibTableColumn
tnLldpStatsRemTablesInserts = _TnLldpStatsRemTablesInserts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 2, 1, 2),
    _TnLldpStatsRemTablesInserts_Type()
)
tnLldpStatsRemTablesInserts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesInserts.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesInserts.setUnits("table entries")
_TnLldpStatsRemTablesDeletes_Type = ZeroBasedCounter32
_TnLldpStatsRemTablesDeletes_Object = MibTableColumn
tnLldpStatsRemTablesDeletes = _TnLldpStatsRemTablesDeletes_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 2, 1, 3),
    _TnLldpStatsRemTablesDeletes_Type()
)
tnLldpStatsRemTablesDeletes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesDeletes.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesDeletes.setUnits("table entries")
_TnLldpStatsRemTablesDrops_Type = ZeroBasedCounter32
_TnLldpStatsRemTablesDrops_Object = MibTableColumn
tnLldpStatsRemTablesDrops = _TnLldpStatsRemTablesDrops_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 2, 1, 4),
    _TnLldpStatsRemTablesDrops_Type()
)
tnLldpStatsRemTablesDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesDrops.setStatus("current")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesDrops.setUnits("table entries")
_TnLldpStatsRemTablesAgeouts_Type = ZeroBasedCounter32
_TnLldpStatsRemTablesAgeouts_Object = MibTableColumn
tnLldpStatsRemTablesAgeouts = _TnLldpStatsRemTablesAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 2, 1, 5),
    _TnLldpStatsRemTablesAgeouts_Type()
)
tnLldpStatsRemTablesAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRemTablesAgeouts.setStatus("current")
_TnLldpStatsRxPortTable_Object = MibTable
tnLldpStatsRxPortTable = _TnLldpStatsRxPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3)
)
if mibBuilder.loadTexts:
    tnLldpStatsRxPortTable.setStatus("current")
_TnLldpStatsRxPortEntry_Object = MibTableRow
tnLldpStatsRxPortEntry = _TnLldpStatsRxPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1)
)
tnLldpStatsRxPortEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpStatsRxDestMACAddress"),
)
if mibBuilder.loadTexts:
    tnLldpStatsRxPortEntry.setStatus("current")
_TnLldpStatsRxDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TnLldpStatsRxDestMACAddress_Object = MibTableColumn
tnLldpStatsRxDestMACAddress = _TnLldpStatsRxDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 1),
    _TnLldpStatsRxDestMACAddress_Type()
)
tnLldpStatsRxDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpStatsRxDestMACAddress.setStatus("current")
_TnLldpStatsRxPortFrameDiscard_Type = Counter32
_TnLldpStatsRxPortFrameDiscard_Object = MibTableColumn
tnLldpStatsRxPortFrameDiscard = _TnLldpStatsRxPortFrameDiscard_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 2),
    _TnLldpStatsRxPortFrameDiscard_Type()
)
tnLldpStatsRxPortFrameDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRxPortFrameDiscard.setStatus("current")
_TnLldpStatsRxPortFrameErrs_Type = Counter32
_TnLldpStatsRxPortFrameErrs_Object = MibTableColumn
tnLldpStatsRxPortFrameErrs = _TnLldpStatsRxPortFrameErrs_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 3),
    _TnLldpStatsRxPortFrameErrs_Type()
)
tnLldpStatsRxPortFrameErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRxPortFrameErrs.setStatus("current")
_TnLldpStatsRxPortFrames_Type = Counter32
_TnLldpStatsRxPortFrames_Object = MibTableColumn
tnLldpStatsRxPortFrames = _TnLldpStatsRxPortFrames_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 4),
    _TnLldpStatsRxPortFrames_Type()
)
tnLldpStatsRxPortFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRxPortFrames.setStatus("current")
_TnLldpStatsRxPortTLVDiscard_Type = Counter32
_TnLldpStatsRxPortTLVDiscard_Object = MibTableColumn
tnLldpStatsRxPortTLVDiscard = _TnLldpStatsRxPortTLVDiscard_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 5),
    _TnLldpStatsRxPortTLVDiscard_Type()
)
tnLldpStatsRxPortTLVDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRxPortTLVDiscard.setStatus("current")
_TnLldpStatsRxPortTLVUnknown_Type = Counter32
_TnLldpStatsRxPortTLVUnknown_Object = MibTableColumn
tnLldpStatsRxPortTLVUnknown = _TnLldpStatsRxPortTLVUnknown_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 6),
    _TnLldpStatsRxPortTLVUnknown_Type()
)
tnLldpStatsRxPortTLVUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRxPortTLVUnknown.setStatus("current")
_TnLldpStatsRxPortAgeouts_Type = ZeroBasedCounter32
_TnLldpStatsRxPortAgeouts_Object = MibTableColumn
tnLldpStatsRxPortAgeouts = _TnLldpStatsRxPortAgeouts_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 7),
    _TnLldpStatsRxPortAgeouts_Type()
)
tnLldpStatsRxPortAgeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRxPortAgeouts.setStatus("current")
_TnLldpStatsRxPortTtl_Type = Unsigned32
_TnLldpStatsRxPortTtl_Object = MibTableColumn
tnLldpStatsRxPortTtl = _TnLldpStatsRxPortTtl_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 2, 3, 1, 8),
    _TnLldpStatsRxPortTtl_Type()
)
tnLldpStatsRxPortTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpStatsRxPortTtl.setStatus("current")
_TnLldpLocalSystemData_ObjectIdentity = ObjectIdentity
tnLldpLocalSystemData = _TnLldpLocalSystemData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3)
)
_TnLldpLocSysDataTable_Object = MibTable
tnLldpLocSysDataTable = _TnLldpLocSysDataTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1)
)
if mibBuilder.loadTexts:
    tnLldpLocSysDataTable.setStatus("current")
_TnLldpLocSysDataEntry_Object = MibTableRow
tnLldpLocSysDataEntry = _TnLldpLocSysDataEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1, 1)
)
tnLldpLocSysDataEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
)
if mibBuilder.loadTexts:
    tnLldpLocSysDataEntry.setStatus("current")
_TnLldpLocChassisIdSubtype_Type = LldpChassisIdSubtype
_TnLldpLocChassisIdSubtype_Object = MibTableColumn
tnLldpLocChassisIdSubtype = _TnLldpLocChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1, 1, 1),
    _TnLldpLocChassisIdSubtype_Type()
)
tnLldpLocChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocChassisIdSubtype.setStatus("current")
_TnLldpLocChassisId_Type = LldpChassisId
_TnLldpLocChassisId_Object = MibTableColumn
tnLldpLocChassisId = _TnLldpLocChassisId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1, 1, 2),
    _TnLldpLocChassisId_Type()
)
tnLldpLocChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocChassisId.setStatus("current")


class _TnLldpLocSysName_Type(SnmpAdminString):
    """Custom type tnLldpLocSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpLocSysName_Type.__name__ = "SnmpAdminString"
_TnLldpLocSysName_Object = MibTableColumn
tnLldpLocSysName = _TnLldpLocSysName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1, 1, 3),
    _TnLldpLocSysName_Type()
)
tnLldpLocSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocSysName.setStatus("current")


class _TnLldpLocSysDesc_Type(SnmpAdminString):
    """Custom type tnLldpLocSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpLocSysDesc_Type.__name__ = "SnmpAdminString"
_TnLldpLocSysDesc_Object = MibTableColumn
tnLldpLocSysDesc = _TnLldpLocSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1, 1, 4),
    _TnLldpLocSysDesc_Type()
)
tnLldpLocSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocSysDesc.setStatus("current")
_TnLldpLocSysCapSupported_Type = LldpSystemCapabilitiesMap
_TnLldpLocSysCapSupported_Object = MibTableColumn
tnLldpLocSysCapSupported = _TnLldpLocSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1, 1, 5),
    _TnLldpLocSysCapSupported_Type()
)
tnLldpLocSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocSysCapSupported.setStatus("current")
_TnLldpLocSysCapEnabled_Type = LldpSystemCapabilitiesMap
_TnLldpLocSysCapEnabled_Object = MibTableColumn
tnLldpLocSysCapEnabled = _TnLldpLocSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 1, 1, 6),
    _TnLldpLocSysCapEnabled_Type()
)
tnLldpLocSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocSysCapEnabled.setStatus("current")
_TnLldpLocPortTable_Object = MibTable
tnLldpLocPortTable = _TnLldpLocPortTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 2)
)
if mibBuilder.loadTexts:
    tnLldpLocPortTable.setStatus("current")
_TnLldpLocPortEntry_Object = MibTableRow
tnLldpLocPortEntry = _TnLldpLocPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 2, 1)
)
tnLldpLocPortEntry.setIndexNames(
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpLocPortDestMACAddress"),
)
if mibBuilder.loadTexts:
    tnLldpLocPortEntry.setStatus("current")
_TnLldpLocPortDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TnLldpLocPortDestMACAddress_Object = MibTableColumn
tnLldpLocPortDestMACAddress = _TnLldpLocPortDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 2, 1, 1),
    _TnLldpLocPortDestMACAddress_Type()
)
tnLldpLocPortDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpLocPortDestMACAddress.setStatus("current")
_TnLldpLocPortIdSubtype_Type = LldpPortIdSubtype
_TnLldpLocPortIdSubtype_Object = MibTableColumn
tnLldpLocPortIdSubtype = _TnLldpLocPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 2, 1, 2),
    _TnLldpLocPortIdSubtype_Type()
)
tnLldpLocPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocPortIdSubtype.setStatus("current")
_TnLldpLocPortId_Type = LldpPortId
_TnLldpLocPortId_Object = MibTableColumn
tnLldpLocPortId = _TnLldpLocPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 2, 1, 3),
    _TnLldpLocPortId_Type()
)
tnLldpLocPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocPortId.setStatus("current")


class _TnLldpLocPortDesc_Type(SnmpAdminString):
    """Custom type tnLldpLocPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpLocPortDesc_Type.__name__ = "SnmpAdminString"
_TnLldpLocPortDesc_Object = MibTableColumn
tnLldpLocPortDesc = _TnLldpLocPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 2, 1, 4),
    _TnLldpLocPortDesc_Type()
)
tnLldpLocPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocPortDesc.setStatus("current")
_TnLldpLocManAddrTable_Object = MibTable
tnLldpLocManAddrTable = _TnLldpLocManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3)
)
if mibBuilder.loadTexts:
    tnLldpLocManAddrTable.setStatus("current")
_TnLldpLocManAddrEntry_Object = MibTableRow
tnLldpLocManAddrEntry = _TnLldpLocManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3, 1)
)
tnLldpLocManAddrEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LLDP-MIB", "tnLldpLocManAddrSubtype"),
    (0, "TN-LLDP-MIB", "tnLldpLocManAddr"),
)
if mibBuilder.loadTexts:
    tnLldpLocManAddrEntry.setStatus("current")
_TnLldpLocManAddrSubtype_Type = AddressFamilyNumbers
_TnLldpLocManAddrSubtype_Object = MibTableColumn
tnLldpLocManAddrSubtype = _TnLldpLocManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3, 1, 1),
    _TnLldpLocManAddrSubtype_Type()
)
tnLldpLocManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpLocManAddrSubtype.setStatus("current")
_TnLldpLocManAddr_Type = LldpManAddress
_TnLldpLocManAddr_Object = MibTableColumn
tnLldpLocManAddr = _TnLldpLocManAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3, 1, 2),
    _TnLldpLocManAddr_Type()
)
tnLldpLocManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpLocManAddr.setStatus("current")
_TnLldpLocManAddrLen_Type = Integer32
_TnLldpLocManAddrLen_Object = MibTableColumn
tnLldpLocManAddrLen = _TnLldpLocManAddrLen_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3, 1, 3),
    _TnLldpLocManAddrLen_Type()
)
tnLldpLocManAddrLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocManAddrLen.setStatus("current")
_TnLldpLocManAddrIfSubtype_Type = LldpManAddrIfSubtype
_TnLldpLocManAddrIfSubtype_Object = MibTableColumn
tnLldpLocManAddrIfSubtype = _TnLldpLocManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3, 1, 4),
    _TnLldpLocManAddrIfSubtype_Type()
)
tnLldpLocManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocManAddrIfSubtype.setStatus("current")
_TnLldpLocManAddrIfId_Type = Integer32
_TnLldpLocManAddrIfId_Object = MibTableColumn
tnLldpLocManAddrIfId = _TnLldpLocManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3, 1, 5),
    _TnLldpLocManAddrIfId_Type()
)
tnLldpLocManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocManAddrIfId.setStatus("current")
_TnLldpLocManAddrOID_Type = ObjectIdentifier
_TnLldpLocManAddrOID_Object = MibTableColumn
tnLldpLocManAddrOID = _TnLldpLocManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 3, 3, 1, 6),
    _TnLldpLocManAddrOID_Type()
)
tnLldpLocManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpLocManAddrOID.setStatus("current")
_TnLldpRemoteSystemsData_ObjectIdentity = ObjectIdentity
tnLldpRemoteSystemsData = _TnLldpRemoteSystemsData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4)
)
_TnLldpRemTable_Object = MibTable
tnLldpRemTable = _TnLldpRemTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1)
)
if mibBuilder.loadTexts:
    tnLldpRemTable.setStatus("current")
_TnLldpRemEntry_Object = MibTableRow
tnLldpRemEntry = _TnLldpRemEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1)
)
tnLldpRemEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LLDP-MIB", "tnLldpRemTimeMark"),
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpRemLocalDestMACAddress"),
    (0, "TN-LLDP-MIB", "tnLldpRemIndex"),
)
if mibBuilder.loadTexts:
    tnLldpRemEntry.setStatus("current")
_TnLldpRemTimeMark_Type = TimeFilter
_TnLldpRemTimeMark_Object = MibTableColumn
tnLldpRemTimeMark = _TnLldpRemTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 1),
    _TnLldpRemTimeMark_Type()
)
tnLldpRemTimeMark.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpRemTimeMark.setStatus("current")
_TnLldpRemLocalDestMACAddress_Type = TmnxLldpDestAddressTableIndex
_TnLldpRemLocalDestMACAddress_Object = MibTableColumn
tnLldpRemLocalDestMACAddress = _TnLldpRemLocalDestMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 2),
    _TnLldpRemLocalDestMACAddress_Type()
)
tnLldpRemLocalDestMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpRemLocalDestMACAddress.setStatus("current")


class _TnLldpRemIndex_Type(Integer32):
    """Custom type tnLldpRemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_TnLldpRemIndex_Type.__name__ = "Integer32"
_TnLldpRemIndex_Object = MibTableColumn
tnLldpRemIndex = _TnLldpRemIndex_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 3),
    _TnLldpRemIndex_Type()
)
tnLldpRemIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpRemIndex.setStatus("current")
_TnLldpRemChassisIdSubtype_Type = LldpChassisIdSubtype
_TnLldpRemChassisIdSubtype_Object = MibTableColumn
tnLldpRemChassisIdSubtype = _TnLldpRemChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 4),
    _TnLldpRemChassisIdSubtype_Type()
)
tnLldpRemChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemChassisIdSubtype.setStatus("current")
_TnLldpRemChassisId_Type = LldpChassisId
_TnLldpRemChassisId_Object = MibTableColumn
tnLldpRemChassisId = _TnLldpRemChassisId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 5),
    _TnLldpRemChassisId_Type()
)
tnLldpRemChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemChassisId.setStatus("current")
_TnLldpRemPortIdSubtype_Type = LldpPortIdSubtype
_TnLldpRemPortIdSubtype_Object = MibTableColumn
tnLldpRemPortIdSubtype = _TnLldpRemPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 6),
    _TnLldpRemPortIdSubtype_Type()
)
tnLldpRemPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIdSubtype.setStatus("current")
_TnLldpRemPortId_Type = LldpPortId
_TnLldpRemPortId_Object = MibTableColumn
tnLldpRemPortId = _TnLldpRemPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 7),
    _TnLldpRemPortId_Type()
)
tnLldpRemPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortId.setStatus("current")


class _TnLldpRemPortDesc_Type(SnmpAdminString):
    """Custom type tnLldpRemPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpRemPortDesc_Type.__name__ = "SnmpAdminString"
_TnLldpRemPortDesc_Object = MibTableColumn
tnLldpRemPortDesc = _TnLldpRemPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 8),
    _TnLldpRemPortDesc_Type()
)
tnLldpRemPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortDesc.setStatus("current")


class _TnLldpRemSysName_Type(SnmpAdminString):
    """Custom type tnLldpRemSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpRemSysName_Type.__name__ = "SnmpAdminString"
_TnLldpRemSysName_Object = MibTableColumn
tnLldpRemSysName = _TnLldpRemSysName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 9),
    _TnLldpRemSysName_Type()
)
tnLldpRemSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemSysName.setStatus("current")


class _TnLldpRemSysDesc_Type(SnmpAdminString):
    """Custom type tnLldpRemSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpRemSysDesc_Type.__name__ = "SnmpAdminString"
_TnLldpRemSysDesc_Object = MibTableColumn
tnLldpRemSysDesc = _TnLldpRemSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 10),
    _TnLldpRemSysDesc_Type()
)
tnLldpRemSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemSysDesc.setStatus("current")
_TnLldpRemSysCapSupported_Type = LldpSystemCapabilitiesMap
_TnLldpRemSysCapSupported_Object = MibTableColumn
tnLldpRemSysCapSupported = _TnLldpRemSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 11),
    _TnLldpRemSysCapSupported_Type()
)
tnLldpRemSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemSysCapSupported.setStatus("current")
_TnLldpRemSysCapEnabled_Type = LldpSystemCapabilitiesMap
_TnLldpRemSysCapEnabled_Object = MibTableColumn
tnLldpRemSysCapEnabled = _TnLldpRemSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 1, 1, 12),
    _TnLldpRemSysCapEnabled_Type()
)
tnLldpRemSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemSysCapEnabled.setStatus("current")
_TnLldpRemManAddrTable_Object = MibTable
tnLldpRemManAddrTable = _TnLldpRemManAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 2)
)
if mibBuilder.loadTexts:
    tnLldpRemManAddrTable.setStatus("current")
_TnLldpRemManAddrEntry_Object = MibTableRow
tnLldpRemManAddrEntry = _TnLldpRemManAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 2, 1)
)
tnLldpRemManAddrEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-LLDP-MIB", "tnLldpRemTimeMark"),
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpRemLocalDestMACAddress"),
    (0, "TN-LLDP-MIB", "tnLldpRemIndex"),
    (0, "TN-LLDP-MIB", "tnLldpRemManAddrSubtype"),
    (0, "TN-LLDP-MIB", "tnLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    tnLldpRemManAddrEntry.setStatus("current")
_TnLldpRemManAddrSubtype_Type = AddressFamilyNumbers
_TnLldpRemManAddrSubtype_Object = MibTableColumn
tnLldpRemManAddrSubtype = _TnLldpRemManAddrSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 2, 1, 1),
    _TnLldpRemManAddrSubtype_Type()
)
tnLldpRemManAddrSubtype.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpRemManAddrSubtype.setStatus("current")
_TnLldpRemManAddr_Type = LldpManAddress
_TnLldpRemManAddr_Object = MibTableColumn
tnLldpRemManAddr = _TnLldpRemManAddr_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 2, 1, 2),
    _TnLldpRemManAddr_Type()
)
tnLldpRemManAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnLldpRemManAddr.setStatus("current")
_TnLldpRemManAddrIfSubtype_Type = LldpManAddrIfSubtype
_TnLldpRemManAddrIfSubtype_Object = MibTableColumn
tnLldpRemManAddrIfSubtype = _TnLldpRemManAddrIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 2, 1, 3),
    _TnLldpRemManAddrIfSubtype_Type()
)
tnLldpRemManAddrIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemManAddrIfSubtype.setStatus("current")
_TnLldpRemManAddrIfId_Type = Integer32
_TnLldpRemManAddrIfId_Object = MibTableColumn
tnLldpRemManAddrIfId = _TnLldpRemManAddrIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 2, 1, 4),
    _TnLldpRemManAddrIfId_Type()
)
tnLldpRemManAddrIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemManAddrIfId.setStatus("current")
_TnLldpRemManAddrOID_Type = ObjectIdentifier
_TnLldpRemManAddrOID_Object = MibTableColumn
tnLldpRemManAddrOID = _TnLldpRemManAddrOID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 2, 1, 5),
    _TnLldpRemManAddrOID_Type()
)
tnLldpRemManAddrOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemManAddrOID.setStatus("current")
_TnLldpRemPortIndexTable_Object = MibTable
tnLldpRemPortIndexTable = _TnLldpRemPortIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3)
)
if mibBuilder.loadTexts:
    tnLldpRemPortIndexTable.setStatus("current")
_TnLldpRemPortIndexEntry_Object = MibTableRow
tnLldpRemPortIndexEntry = _TnLldpRemPortIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1)
)
tnLldpRemPortIndexEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpRemTimeMark"),
    (0, "TN-LLDP-MIB", "tnLldpRemLocalDestMACAddress"),
    (0, "TN-LLDP-MIB", "tnLldpRemIndex"),
)
if mibBuilder.loadTexts:
    tnLldpRemPortIndexEntry.setStatus("current")
_TnLldpRemPortIndexChassisIdSubtype_Type = LldpChassisIdSubtype
_TnLldpRemPortIndexChassisIdSubtype_Object = MibTableColumn
tnLldpRemPortIndexChassisIdSubtype = _TnLldpRemPortIndexChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 1),
    _TnLldpRemPortIndexChassisIdSubtype_Type()
)
tnLldpRemPortIndexChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexChassisIdSubtype.setStatus("current")
_TnLldpRemPortIndexChassisId_Type = LldpChassisId
_TnLldpRemPortIndexChassisId_Object = MibTableColumn
tnLldpRemPortIndexChassisId = _TnLldpRemPortIndexChassisId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 2),
    _TnLldpRemPortIndexChassisId_Type()
)
tnLldpRemPortIndexChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexChassisId.setStatus("current")
_TnLldpRemPortIndexPortIdSubtype_Type = LldpPortIdSubtype
_TnLldpRemPortIndexPortIdSubtype_Object = MibTableColumn
tnLldpRemPortIndexPortIdSubtype = _TnLldpRemPortIndexPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 3),
    _TnLldpRemPortIndexPortIdSubtype_Type()
)
tnLldpRemPortIndexPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexPortIdSubtype.setStatus("current")
_TnLldpRemPortIndexPortId_Type = LldpPortId
_TnLldpRemPortIndexPortId_Object = MibTableColumn
tnLldpRemPortIndexPortId = _TnLldpRemPortIndexPortId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 4),
    _TnLldpRemPortIndexPortId_Type()
)
tnLldpRemPortIndexPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexPortId.setStatus("current")


class _TnLldpRemPortIndexPortDesc_Type(SnmpAdminString):
    """Custom type tnLldpRemPortIndexPortDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpRemPortIndexPortDesc_Type.__name__ = "SnmpAdminString"
_TnLldpRemPortIndexPortDesc_Object = MibTableColumn
tnLldpRemPortIndexPortDesc = _TnLldpRemPortIndexPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 5),
    _TnLldpRemPortIndexPortDesc_Type()
)
tnLldpRemPortIndexPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexPortDesc.setStatus("current")


class _TnLldpRemPortIndexSysName_Type(SnmpAdminString):
    """Custom type tnLldpRemPortIndexSysName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpRemPortIndexSysName_Type.__name__ = "SnmpAdminString"
_TnLldpRemPortIndexSysName_Object = MibTableColumn
tnLldpRemPortIndexSysName = _TnLldpRemPortIndexSysName_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 6),
    _TnLldpRemPortIndexSysName_Type()
)
tnLldpRemPortIndexSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexSysName.setStatus("current")


class _TnLldpRemPortIndexSysDesc_Type(SnmpAdminString):
    """Custom type tnLldpRemPortIndexSysDesc based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TnLldpRemPortIndexSysDesc_Type.__name__ = "SnmpAdminString"
_TnLldpRemPortIndexSysDesc_Object = MibTableColumn
tnLldpRemPortIndexSysDesc = _TnLldpRemPortIndexSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 7),
    _TnLldpRemPortIndexSysDesc_Type()
)
tnLldpRemPortIndexSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexSysDesc.setStatus("current")
_TnLldpRemPortIndexSysCapSupported_Type = LldpSystemCapabilitiesMap
_TnLldpRemPortIndexSysCapSupported_Object = MibTableColumn
tnLldpRemPortIndexSysCapSupported = _TnLldpRemPortIndexSysCapSupported_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 8),
    _TnLldpRemPortIndexSysCapSupported_Type()
)
tnLldpRemPortIndexSysCapSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexSysCapSupported.setStatus("current")
_TnLldpRemPortIndexSysCapEnabled_Type = LldpSystemCapabilitiesMap
_TnLldpRemPortIndexSysCapEnabled_Object = MibTableColumn
tnLldpRemPortIndexSysCapEnabled = _TnLldpRemPortIndexSysCapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 3, 1, 9),
    _TnLldpRemPortIndexSysCapEnabled_Type()
)
tnLldpRemPortIndexSysCapEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemPortIndexSysCapEnabled.setStatus("current")
_TnLldpRemManAddrPortIndexTable_Object = MibTable
tnLldpRemManAddrPortIndexTable = _TnLldpRemManAddrPortIndexTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 4)
)
if mibBuilder.loadTexts:
    tnLldpRemManAddrPortIndexTable.setStatus("current")
_TnLldpRemManAddrPortIndexEntry_Object = MibTableRow
tnLldpRemManAddrPortIndexEntry = _TnLldpRemManAddrPortIndexEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 4, 1)
)
tnLldpRemManAddrPortIndexEntry.setIndexNames(
    (0, "TROPIC-SYSTEM-MIB", "tnSysSwitchId"),
    (0, "TN-PORT-MIB", "tnPortPortID"),
    (0, "TN-LLDP-MIB", "tnLldpRemTimeMark"),
    (0, "TN-LLDP-MIB", "tnLldpRemLocalDestMACAddress"),
    (0, "TN-LLDP-MIB", "tnLldpRemIndex"),
    (0, "TN-LLDP-MIB", "tnLldpRemManAddrSubtype"),
    (0, "TN-LLDP-MIB", "tnLldpRemManAddr"),
)
if mibBuilder.loadTexts:
    tnLldpRemManAddrPortIndexEntry.setStatus("current")
_TnLldpRemManAddrPortIndexIfSubtype_Type = LldpManAddrIfSubtype
_TnLldpRemManAddrPortIndexIfSubtype_Object = MibTableColumn
tnLldpRemManAddrPortIndexIfSubtype = _TnLldpRemManAddrPortIndexIfSubtype_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 4, 1, 1),
    _TnLldpRemManAddrPortIndexIfSubtype_Type()
)
tnLldpRemManAddrPortIndexIfSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemManAddrPortIndexIfSubtype.setStatus("current")
_TnLldpRemManAddrPortIndexIfId_Type = Integer32
_TnLldpRemManAddrPortIndexIfId_Object = MibTableColumn
tnLldpRemManAddrPortIndexIfId = _TnLldpRemManAddrPortIndexIfId_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 4, 1, 2),
    _TnLldpRemManAddrPortIndexIfId_Type()
)
tnLldpRemManAddrPortIndexIfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemManAddrPortIndexIfId.setStatus("current")
_TnLldpRemManAddrPortIndexOID_Type = ObjectIdentifier
_TnLldpRemManAddrPortIndexOID_Object = MibTableColumn
tnLldpRemManAddrPortIndexOID = _TnLldpRemManAddrPortIndexOID_Object(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 2, 59, 4, 4, 1, 3),
    _TnLldpRemManAddrPortIndexOID_Type()
)
tnLldpRemManAddrPortIndexOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnLldpRemManAddrPortIndexOID.setStatus("current")
_TnLldpNotifications_ObjectIdentity = ObjectIdentity
tnLldpNotifications = _TnLldpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 6, 1, 3, 59)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-LLDP-MIB",
    **{"TmnxLldpDestAddressTableIndex": TmnxLldpDestAddressTableIndex,
       "TmnxLldpManAddressIndex": TmnxLldpManAddressIndex,
       "tnLldpMIBModule": tnLldpMIBModule,
       "tnLldpObjects": tnLldpObjects,
       "tnLldpConfiguration": tnLldpConfiguration,
       "tnLldpConfigTable": tnLldpConfigTable,
       "tnLldpConfigEntry": tnLldpConfigEntry,
       "tnLldpMessageTxInterval": tnLldpMessageTxInterval,
       "tnLldpMessageTxHoldMultiplier": tnLldpMessageTxHoldMultiplier,
       "tnLldpReinitDelay": tnLldpReinitDelay,
       "tnLldpTxDelay": tnLldpTxDelay,
       "tnLldpNotificationInterval": tnLldpNotificationInterval,
       "tnLldpTxCreditMax": tnLldpTxCreditMax,
       "tnLldpMessageFastTx": tnLldpMessageFastTx,
       "tnLldpMessageFastTxInit": tnLldpMessageFastTxInit,
       "tnLldpAdminStatus": tnLldpAdminStatus,
       "tnLldpPortConfigTable": tnLldpPortConfigTable,
       "tnLldpPortConfigEntry": tnLldpPortConfigEntry,
       "tnLldpPortCfgDestAddressIndex": tnLldpPortCfgDestAddressIndex,
       "tnLldpPortCfgAdminStatus": tnLldpPortCfgAdminStatus,
       "tnLldpPortCfgNotifyEnable": tnLldpPortCfgNotifyEnable,
       "tnLldpPortCfgTLVsTxEnable": tnLldpPortCfgTLVsTxEnable,
       "tnLldpConfigManAddrPortsTable": tnLldpConfigManAddrPortsTable,
       "tnLldpConfigManAddrPortsEntry": tnLldpConfigManAddrPortsEntry,
       "tnLldpPortCfgAddressIndex": tnLldpPortCfgAddressIndex,
       "tnLldpPortCfgManAddrTxEnabled": tnLldpPortCfgManAddrTxEnabled,
       "tnLldpPortCfgManAddrSubtype": tnLldpPortCfgManAddrSubtype,
       "tnLldpPortCfgManAddress": tnLldpPortCfgManAddress,
       "tnLldpDestAddressTable": tnLldpDestAddressTable,
       "tnLldpDestAddressTableEntry": tnLldpDestAddressTableEntry,
       "tnLldpAddressTableIndex": tnLldpAddressTableIndex,
       "tnLldpDestMacAddress": tnLldpDestMacAddress,
       "tnLldpStatistics": tnLldpStatistics,
       "tnLldpStatsTxPortTable": tnLldpStatsTxPortTable,
       "tnLldpStatsTxPortEntry": tnLldpStatsTxPortEntry,
       "tnLldpStatsTxDestMACAddress": tnLldpStatsTxDestMACAddress,
       "tnLldpStatsTxPortFrames": tnLldpStatsTxPortFrames,
       "tnLldpStatsTxLLDPDULengthErrs": tnLldpStatsTxLLDPDULengthErrs,
       "tnLldpStatsRemTable": tnLldpStatsRemTable,
       "tnLldpStatsRemEntry": tnLldpStatsRemEntry,
       "tnLldpStatsRemTablesLastChangeTime": tnLldpStatsRemTablesLastChangeTime,
       "tnLldpStatsRemTablesInserts": tnLldpStatsRemTablesInserts,
       "tnLldpStatsRemTablesDeletes": tnLldpStatsRemTablesDeletes,
       "tnLldpStatsRemTablesDrops": tnLldpStatsRemTablesDrops,
       "tnLldpStatsRemTablesAgeouts": tnLldpStatsRemTablesAgeouts,
       "tnLldpStatsRxPortTable": tnLldpStatsRxPortTable,
       "tnLldpStatsRxPortEntry": tnLldpStatsRxPortEntry,
       "tnLldpStatsRxDestMACAddress": tnLldpStatsRxDestMACAddress,
       "tnLldpStatsRxPortFrameDiscard": tnLldpStatsRxPortFrameDiscard,
       "tnLldpStatsRxPortFrameErrs": tnLldpStatsRxPortFrameErrs,
       "tnLldpStatsRxPortFrames": tnLldpStatsRxPortFrames,
       "tnLldpStatsRxPortTLVDiscard": tnLldpStatsRxPortTLVDiscard,
       "tnLldpStatsRxPortTLVUnknown": tnLldpStatsRxPortTLVUnknown,
       "tnLldpStatsRxPortAgeouts": tnLldpStatsRxPortAgeouts,
       "tnLldpStatsRxPortTtl": tnLldpStatsRxPortTtl,
       "tnLldpLocalSystemData": tnLldpLocalSystemData,
       "tnLldpLocSysDataTable": tnLldpLocSysDataTable,
       "tnLldpLocSysDataEntry": tnLldpLocSysDataEntry,
       "tnLldpLocChassisIdSubtype": tnLldpLocChassisIdSubtype,
       "tnLldpLocChassisId": tnLldpLocChassisId,
       "tnLldpLocSysName": tnLldpLocSysName,
       "tnLldpLocSysDesc": tnLldpLocSysDesc,
       "tnLldpLocSysCapSupported": tnLldpLocSysCapSupported,
       "tnLldpLocSysCapEnabled": tnLldpLocSysCapEnabled,
       "tnLldpLocPortTable": tnLldpLocPortTable,
       "tnLldpLocPortEntry": tnLldpLocPortEntry,
       "tnLldpLocPortDestMACAddress": tnLldpLocPortDestMACAddress,
       "tnLldpLocPortIdSubtype": tnLldpLocPortIdSubtype,
       "tnLldpLocPortId": tnLldpLocPortId,
       "tnLldpLocPortDesc": tnLldpLocPortDesc,
       "tnLldpLocManAddrTable": tnLldpLocManAddrTable,
       "tnLldpLocManAddrEntry": tnLldpLocManAddrEntry,
       "tnLldpLocManAddrSubtype": tnLldpLocManAddrSubtype,
       "tnLldpLocManAddr": tnLldpLocManAddr,
       "tnLldpLocManAddrLen": tnLldpLocManAddrLen,
       "tnLldpLocManAddrIfSubtype": tnLldpLocManAddrIfSubtype,
       "tnLldpLocManAddrIfId": tnLldpLocManAddrIfId,
       "tnLldpLocManAddrOID": tnLldpLocManAddrOID,
       "tnLldpRemoteSystemsData": tnLldpRemoteSystemsData,
       "tnLldpRemTable": tnLldpRemTable,
       "tnLldpRemEntry": tnLldpRemEntry,
       "tnLldpRemTimeMark": tnLldpRemTimeMark,
       "tnLldpRemLocalDestMACAddress": tnLldpRemLocalDestMACAddress,
       "tnLldpRemIndex": tnLldpRemIndex,
       "tnLldpRemChassisIdSubtype": tnLldpRemChassisIdSubtype,
       "tnLldpRemChassisId": tnLldpRemChassisId,
       "tnLldpRemPortIdSubtype": tnLldpRemPortIdSubtype,
       "tnLldpRemPortId": tnLldpRemPortId,
       "tnLldpRemPortDesc": tnLldpRemPortDesc,
       "tnLldpRemSysName": tnLldpRemSysName,
       "tnLldpRemSysDesc": tnLldpRemSysDesc,
       "tnLldpRemSysCapSupported": tnLldpRemSysCapSupported,
       "tnLldpRemSysCapEnabled": tnLldpRemSysCapEnabled,
       "tnLldpRemManAddrTable": tnLldpRemManAddrTable,
       "tnLldpRemManAddrEntry": tnLldpRemManAddrEntry,
       "tnLldpRemManAddrSubtype": tnLldpRemManAddrSubtype,
       "tnLldpRemManAddr": tnLldpRemManAddr,
       "tnLldpRemManAddrIfSubtype": tnLldpRemManAddrIfSubtype,
       "tnLldpRemManAddrIfId": tnLldpRemManAddrIfId,
       "tnLldpRemManAddrOID": tnLldpRemManAddrOID,
       "tnLldpRemPortIndexTable": tnLldpRemPortIndexTable,
       "tnLldpRemPortIndexEntry": tnLldpRemPortIndexEntry,
       "tnLldpRemPortIndexChassisIdSubtype": tnLldpRemPortIndexChassisIdSubtype,
       "tnLldpRemPortIndexChassisId": tnLldpRemPortIndexChassisId,
       "tnLldpRemPortIndexPortIdSubtype": tnLldpRemPortIndexPortIdSubtype,
       "tnLldpRemPortIndexPortId": tnLldpRemPortIndexPortId,
       "tnLldpRemPortIndexPortDesc": tnLldpRemPortIndexPortDesc,
       "tnLldpRemPortIndexSysName": tnLldpRemPortIndexSysName,
       "tnLldpRemPortIndexSysDesc": tnLldpRemPortIndexSysDesc,
       "tnLldpRemPortIndexSysCapSupported": tnLldpRemPortIndexSysCapSupported,
       "tnLldpRemPortIndexSysCapEnabled": tnLldpRemPortIndexSysCapEnabled,
       "tnLldpRemManAddrPortIndexTable": tnLldpRemManAddrPortIndexTable,
       "tnLldpRemManAddrPortIndexEntry": tnLldpRemManAddrPortIndexEntry,
       "tnLldpRemManAddrPortIndexIfSubtype": tnLldpRemManAddrPortIndexIfSubtype,
       "tnLldpRemManAddrPortIndexIfId": tnLldpRemManAddrPortIndexIfId,
       "tnLldpRemManAddrPortIndexOID": tnLldpRemManAddrPortIndexOID,
       "tnLldpNotifications": tnLldpNotifications}
)
