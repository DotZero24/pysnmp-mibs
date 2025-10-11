# SNMP MIB module (RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:17 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(EntryStatus,) = mibBuilder.importSymbols(
    "SWITCH-RMON-MIB",
    "EntryStatus")

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

raisecomRemoteManagementLocal = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RcRemoteVlanStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("vlan-forbid", 1),
          ("vlan-dot1q", 2),
          ("vlan-port", 3))
    )



class RcRemotePortTagStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("untag", 1),
          ("tag", 2))
    )



class RcRemoteConfigFrameSendStatus(TextualConvention, Integer32):
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
        *(("send", 1),
          ("save", 2),
          ("sendandsave", 3),
          ("waitting", 4),
          ("successful", 5),
          ("failed", 6))
    )



class RcRemoteSfpDdmMode(TextualConvention, Integer32):
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
        *(("unknown", 0),
          ("inside", 1),
          ("outside", 2))
    )



class RcRemoteSfpDdmAlarmStatus(TextualConvention, Integer32):
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
        *(("normal", 0),
          ("low", 1),
          ("high", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RaisecomRemoteManagementLocalMibObjects_ObjectIdentity = ObjectIdentity
raisecomRemoteManagementLocalMibObjects = _RaisecomRemoteManagementLocalMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1)
)
_RaisecomRemoteTrapEnable_Type = EnableVar
_RaisecomRemoteTrapEnable_Object = MibScalar
raisecomRemoteTrapEnable = _RaisecomRemoteTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 1),
    _RaisecomRemoteTrapEnable_Type()
)
raisecomRemoteTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteTrapEnable.setStatus("current")
_RaisecomRemoteInvariableInfoTable_Object = MibTable
raisecomRemoteInvariableInfoTable = _RaisecomRemoteInvariableInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomRemoteInvariableInfoTable.setStatus("current")
_RaisecomRemoteInvariableInfoEntry_Object = MibTableRow
raisecomRemoteInvariableInfoEntry = _RaisecomRemoteInvariableInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1)
)
raisecomRemoteInvariableInfoEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteInvariableInfoIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteInvariableInfoEntry.setStatus("current")
_RaisecomRemoteInvariableInfoIndex_Type = Integer32
_RaisecomRemoteInvariableInfoIndex_Object = MibTableColumn
raisecomRemoteInvariableInfoIndex = _RaisecomRemoteInvariableInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 1),
    _RaisecomRemoteInvariableInfoIndex_Type()
)
raisecomRemoteInvariableInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteInvariableInfoIndex.setStatus("current")
_RaisecomRemoteSysOid_Type = ObjectIdentifier
_RaisecomRemoteSysOid_Object = MibTableColumn
raisecomRemoteSysOid = _RaisecomRemoteSysOid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 2),
    _RaisecomRemoteSysOid_Type()
)
raisecomRemoteSysOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSysOid.setStatus("current")
_RaisecomRemoteModuleType_Type = Integer32
_RaisecomRemoteModuleType_Object = MibTableColumn
raisecomRemoteModuleType = _RaisecomRemoteModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 3),
    _RaisecomRemoteModuleType_Type()
)
raisecomRemoteModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteModuleType.setStatus("current")


class _RaisecomRemoteOidCapability_Type(TruthValue):
    """Custom type raisecomRemoteOidCapability based on TruthValue"""
    defaultValue = 2


_RaisecomRemoteOidCapability_Type.__name__ = "TruthValue"
_RaisecomRemoteOidCapability_Object = MibTableColumn
raisecomRemoteOidCapability = _RaisecomRemoteOidCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 4),
    _RaisecomRemoteOidCapability_Type()
)
raisecomRemoteOidCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteOidCapability.setStatus("current")


class _RaisecomRemoteFileTransCapability_Type(TruthValue):
    """Custom type raisecomRemoteFileTransCapability based on TruthValue"""
    defaultValue = 2


_RaisecomRemoteFileTransCapability_Type.__name__ = "TruthValue"
_RaisecomRemoteFileTransCapability_Object = MibTableColumn
raisecomRemoteFileTransCapability = _RaisecomRemoteFileTransCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 5),
    _RaisecomRemoteFileTransCapability_Type()
)
raisecomRemoteFileTransCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteFileTransCapability.setStatus("current")


class _RaisecomRemoteOtherCapability_Type(Integer32):
    """Custom type raisecomRemoteOtherCapability based on Integer32"""
    defaultValue = 0


_RaisecomRemoteOtherCapability_Type.__name__ = "Integer32"
_RaisecomRemoteOtherCapability_Object = MibTableColumn
raisecomRemoteOtherCapability = _RaisecomRemoteOtherCapability_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 6),
    _RaisecomRemoteOtherCapability_Type()
)
raisecomRemoteOtherCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteOtherCapability.setStatus("current")


class _RaisecomRemoteMainChipId_Type(Integer32):
    """Custom type raisecomRemoteMainChipId based on Integer32"""
    defaultValue = 0


_RaisecomRemoteMainChipId_Type.__name__ = "Integer32"
_RaisecomRemoteMainChipId_Object = MibTableColumn
raisecomRemoteMainChipId = _RaisecomRemoteMainChipId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 7),
    _RaisecomRemoteMainChipId_Type()
)
raisecomRemoteMainChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteMainChipId.setStatus("current")


class _RaisecomRemoteFpgaChipId_Type(Integer32):
    """Custom type raisecomRemoteFpgaChipId based on Integer32"""
    defaultValue = 0


_RaisecomRemoteFpgaChipId_Type.__name__ = "Integer32"
_RaisecomRemoteFpgaChipId_Object = MibTableColumn
raisecomRemoteFpgaChipId = _RaisecomRemoteFpgaChipId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 8),
    _RaisecomRemoteFpgaChipId_Type()
)
raisecomRemoteFpgaChipId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteFpgaChipId.setStatus("current")
_RaisecomRemoteFpgaSwVer_Type = OctetString
_RaisecomRemoteFpgaSwVer_Object = MibTableColumn
raisecomRemoteFpgaSwVer = _RaisecomRemoteFpgaSwVer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 9),
    _RaisecomRemoteFpgaSwVer_Type()
)
raisecomRemoteFpgaSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteFpgaSwVer.setStatus("current")
_RaisecomRemoteSystemSwVer_Type = OctetString
_RaisecomRemoteSystemSwVer_Object = MibTableColumn
raisecomRemoteSystemSwVer = _RaisecomRemoteSystemSwVer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 10),
    _RaisecomRemoteSystemSwVer_Type()
)
raisecomRemoteSystemSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSystemSwVer.setStatus("current")
_RaisecomRemoteSystemHwVer_Type = OctetString
_RaisecomRemoteSystemHwVer_Object = MibTableColumn
raisecomRemoteSystemHwVer = _RaisecomRemoteSystemHwVer_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 11),
    _RaisecomRemoteSystemHwVer_Type()
)
raisecomRemoteSystemHwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSystemHwVer.setStatus("current")
_RaisecomRemotePortNum_Type = Integer32
_RaisecomRemotePortNum_Object = MibTableColumn
raisecomRemotePortNum = _RaisecomRemotePortNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 12),
    _RaisecomRemotePortNum_Type()
)
raisecomRemotePortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortNum.setStatus("current")
_RaisecomRemoteDeviceName_Type = OctetString
_RaisecomRemoteDeviceName_Object = MibTableColumn
raisecomRemoteDeviceName = _RaisecomRemoteDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 13),
    _RaisecomRemoteDeviceName_Type()
)
raisecomRemoteDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteDeviceName.setStatus("current")
_RaisecomRemoteInvariableInfoStatus_Type = EntryStatus
_RaisecomRemoteInvariableInfoStatus_Object = MibTableColumn
raisecomRemoteInvariableInfoStatus = _RaisecomRemoteInvariableInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 2, 1, 14),
    _RaisecomRemoteInvariableInfoStatus_Type()
)
raisecomRemoteInvariableInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteInvariableInfoStatus.setStatus("current")
_RaisecomRemoteEnvironmentTable_Object = MibTable
raisecomRemoteEnvironmentTable = _RaisecomRemoteEnvironmentTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomRemoteEnvironmentTable.setStatus("current")
_RaisecomRemoteEnvironmentEntry_Object = MibTableRow
raisecomRemoteEnvironmentEntry = _RaisecomRemoteEnvironmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1)
)
raisecomRemoteEnvironmentEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteEnvironmentIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteEnvironmentEntry.setStatus("current")
_RaisecomRemoteEnvironmentIndex_Type = Integer32
_RaisecomRemoteEnvironmentIndex_Object = MibTableColumn
raisecomRemoteEnvironmentIndex = _RaisecomRemoteEnvironmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1, 1),
    _RaisecomRemoteEnvironmentIndex_Type()
)
raisecomRemoteEnvironmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteEnvironmentIndex.setStatus("current")


class _RaisecomRemoteTemperature_Type(Integer32):
    """Custom type raisecomRemoteTemperature based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteTemperature_Type.__name__ = "Integer32"
_RaisecomRemoteTemperature_Object = MibTableColumn
raisecomRemoteTemperature = _RaisecomRemoteTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1, 2),
    _RaisecomRemoteTemperature_Type()
)
raisecomRemoteTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteTemperature.setStatus("current")


class _RaisecomRemoteVolt3300_Type(Integer32):
    """Custom type raisecomRemoteVolt3300 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt3300_Type.__name__ = "Integer32"
_RaisecomRemoteVolt3300_Object = MibTableColumn
raisecomRemoteVolt3300 = _RaisecomRemoteVolt3300_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1, 3),
    _RaisecomRemoteVolt3300_Type()
)
raisecomRemoteVolt3300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt3300.setStatus("current")


class _RaisecomRemoteVolt2500_Type(Integer32):
    """Custom type raisecomRemoteVolt2500 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt2500_Type.__name__ = "Integer32"
_RaisecomRemoteVolt2500_Object = MibTableColumn
raisecomRemoteVolt2500 = _RaisecomRemoteVolt2500_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1, 4),
    _RaisecomRemoteVolt2500_Type()
)
raisecomRemoteVolt2500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt2500.setStatus("current")


class _RaisecomRemoteVolt1800_Type(Integer32):
    """Custom type raisecomRemoteVolt1800 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt1800_Type.__name__ = "Integer32"
_RaisecomRemoteVolt1800_Object = MibTableColumn
raisecomRemoteVolt1800 = _RaisecomRemoteVolt1800_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1, 5),
    _RaisecomRemoteVolt1800_Type()
)
raisecomRemoteVolt1800.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt1800.setStatus("current")


class _RaisecomRemoteVolt1200_Type(Integer32):
    """Custom type raisecomRemoteVolt1200 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt1200_Type.__name__ = "Integer32"
_RaisecomRemoteVolt1200_Object = MibTableColumn
raisecomRemoteVolt1200 = _RaisecomRemoteVolt1200_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1, 6),
    _RaisecomRemoteVolt1200_Type()
)
raisecomRemoteVolt1200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt1200.setStatus("current")


class _RaisecomRemoteVoltNormal_Type(Integer32):
    """Custom type raisecomRemoteVoltNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("high", 2),
          ("low", 3))
    )


_RaisecomRemoteVoltNormal_Type.__name__ = "Integer32"
_RaisecomRemoteVoltNormal_Object = MibTableColumn
raisecomRemoteVoltNormal = _RaisecomRemoteVoltNormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 3, 1, 7),
    _RaisecomRemoteVoltNormal_Type()
)
raisecomRemoteVoltNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVoltNormal.setStatus("current")
_RaisecomRemoteSysCfgTable_Object = MibTable
raisecomRemoteSysCfgTable = _RaisecomRemoteSysCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4)
)
if mibBuilder.loadTexts:
    raisecomRemoteSysCfgTable.setStatus("current")
_RaisecomRemoteSysCfgEntry_Object = MibTableRow
raisecomRemoteSysCfgEntry = _RaisecomRemoteSysCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4, 1)
)
raisecomRemoteSysCfgEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteSysCfgIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteSysCfgEntry.setStatus("current")
_RaisecomRemoteSysCfgIndex_Type = Integer32
_RaisecomRemoteSysCfgIndex_Object = MibTableColumn
raisecomRemoteSysCfgIndex = _RaisecomRemoteSysCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4, 1, 1),
    _RaisecomRemoteSysCfgIndex_Type()
)
raisecomRemoteSysCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteSysCfgIndex.setStatus("current")


class _RaisecomRemoteSysOperation_Type(Integer32):
    """Custom type raisecomRemoteSysOperation based on Integer32"""
    defaultValue = 1

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
        *(("ready", 1),
          ("write", 2),
          ("erase", 3),
          ("reboot", 4))
    )


_RaisecomRemoteSysOperation_Type.__name__ = "Integer32"
_RaisecomRemoteSysOperation_Object = MibTableColumn
raisecomRemoteSysOperation = _RaisecomRemoteSysOperation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4, 1, 2),
    _RaisecomRemoteSysOperation_Type()
)
raisecomRemoteSysOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteSysOperation.setStatus("current")


class _RaisecomRemoteSysOperationState_Type(Integer32):
    """Custom type raisecomRemoteSysOperationState based on Integer32"""
    defaultValue = 1

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
        *(("ready", 1),
          ("running", 2),
          ("successful", 3),
          ("failed", 4))
    )


_RaisecomRemoteSysOperationState_Type.__name__ = "Integer32"
_RaisecomRemoteSysOperationState_Object = MibTableColumn
raisecomRemoteSysOperationState = _RaisecomRemoteSysOperationState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4, 1, 3),
    _RaisecomRemoteSysOperationState_Type()
)
raisecomRemoteSysOperationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSysOperationState.setStatus("current")


class _RaisecomRemoteHostName_Type(OctetString):
    """Custom type raisecomRemoteHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomRemoteHostName_Type.__name__ = "OctetString"
_RaisecomRemoteHostName_Object = MibTableColumn
raisecomRemoteHostName = _RaisecomRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4, 1, 4),
    _RaisecomRemoteHostName_Type()
)
raisecomRemoteHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteHostName.setStatus("current")
_RaisecomRemoteOamNotificationEnable_Type = EnableVar
_RaisecomRemoteOamNotificationEnable_Object = MibTableColumn
raisecomRemoteOamNotificationEnable = _RaisecomRemoteOamNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4, 1, 5),
    _RaisecomRemoteOamNotificationEnable_Type()
)
raisecomRemoteOamNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteOamNotificationEnable.setStatus("current")
_RaisecomRemoteMaxAllowedFrameLength_Type = Integer32
_RaisecomRemoteMaxAllowedFrameLength_Object = MibTableColumn
raisecomRemoteMaxAllowedFrameLength = _RaisecomRemoteMaxAllowedFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 4, 1, 6),
    _RaisecomRemoteMaxAllowedFrameLength_Type()
)
raisecomRemoteMaxAllowedFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteMaxAllowedFrameLength.setStatus("current")
_RaisecomRemoteCommunityTable_Object = MibTable
raisecomRemoteCommunityTable = _RaisecomRemoteCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 5)
)
if mibBuilder.loadTexts:
    raisecomRemoteCommunityTable.setStatus("current")
_RaisecomRemoteCommunityEntry_Object = MibTableRow
raisecomRemoteCommunityEntry = _RaisecomRemoteCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 5, 1)
)
raisecomRemoteCommunityEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteSysCfgIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteCommunityEntry.setStatus("current")
_RaisecomRemoteCommunityIndex_Type = Integer32
_RaisecomRemoteCommunityIndex_Object = MibTableColumn
raisecomRemoteCommunityIndex = _RaisecomRemoteCommunityIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 5, 1, 1),
    _RaisecomRemoteCommunityIndex_Type()
)
raisecomRemoteCommunityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteCommunityIndex.setStatus("current")


class _RaisecomRemoteCommunityName_Type(OctetString):
    """Custom type raisecomRemoteCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RaisecomRemoteCommunityName_Type.__name__ = "OctetString"
_RaisecomRemoteCommunityName_Object = MibTableColumn
raisecomRemoteCommunityName = _RaisecomRemoteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 5, 1, 2),
    _RaisecomRemoteCommunityName_Type()
)
raisecomRemoteCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCommunityName.setStatus("current")


class _RaisecomRemoteCommunityPermission_Type(Integer32):
    """Custom type raisecomRemoteCommunityPermission based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("readOnly", 1),
          ("readWrite", 2),
          ("invalid", 3))
    )


_RaisecomRemoteCommunityPermission_Type.__name__ = "Integer32"
_RaisecomRemoteCommunityPermission_Object = MibTableColumn
raisecomRemoteCommunityPermission = _RaisecomRemoteCommunityPermission_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 5, 1, 3),
    _RaisecomRemoteCommunityPermission_Type()
)
raisecomRemoteCommunityPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCommunityPermission.setStatus("current")
_RaisecomRemoteL3Table_Object = MibTable
raisecomRemoteL3Table = _RaisecomRemoteL3Table_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6)
)
if mibBuilder.loadTexts:
    raisecomRemoteL3Table.setStatus("current")
_RaisecomRemoteL3Entry_Object = MibTableRow
raisecomRemoteL3Entry = _RaisecomRemoteL3Entry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1)
)
raisecomRemoteL3Entry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteL3Index"),
)
if mibBuilder.loadTexts:
    raisecomRemoteL3Entry.setStatus("current")
_RaisecomRemoteL3Index_Type = Integer32
_RaisecomRemoteL3Index_Object = MibTableColumn
raisecomRemoteL3Index = _RaisecomRemoteL3Index_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 1),
    _RaisecomRemoteL3Index_Type()
)
raisecomRemoteL3Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteL3Index.setStatus("current")
_RaisecomRemoteL3IpAddr_Type = IpAddress
_RaisecomRemoteL3IpAddr_Object = MibTableColumn
raisecomRemoteL3IpAddr = _RaisecomRemoteL3IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 2),
    _RaisecomRemoteL3IpAddr_Type()
)
raisecomRemoteL3IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3IpAddr.setStatus("current")
_RaisecomRemoteL3Mask_Type = IpAddress
_RaisecomRemoteL3Mask_Object = MibTableColumn
raisecomRemoteL3Mask = _RaisecomRemoteL3Mask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 3),
    _RaisecomRemoteL3Mask_Type()
)
raisecomRemoteL3Mask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3Mask.setStatus("current")


class _RaisecomRemoteL3VidIface_Type(Integer32):
    """Custom type raisecomRemoteL3VidIface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomRemoteL3VidIface_Type.__name__ = "Integer32"
_RaisecomRemoteL3VidIface_Object = MibTableColumn
raisecomRemoteL3VidIface = _RaisecomRemoteL3VidIface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 4),
    _RaisecomRemoteL3VidIface_Type()
)
raisecomRemoteL3VidIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3VidIface.setStatus("current")
_RaisecomRemoteL3VidMemberPorts_Type = PortList
_RaisecomRemoteL3VidMemberPorts_Object = MibTableColumn
raisecomRemoteL3VidMemberPorts = _RaisecomRemoteL3VidMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 5),
    _RaisecomRemoteL3VidMemberPorts_Type()
)
raisecomRemoteL3VidMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteL3VidMemberPorts.setStatus("current")
_RaisecomRemoteL3VidUntaggedPorts_Type = PortList
_RaisecomRemoteL3VidUntaggedPorts_Object = MibTableColumn
raisecomRemoteL3VidUntaggedPorts = _RaisecomRemoteL3VidUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 6),
    _RaisecomRemoteL3VidUntaggedPorts_Type()
)
raisecomRemoteL3VidUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteL3VidUntaggedPorts.setStatus("current")
_RaisecomRemoteL3DefaultGateway_Type = IpAddress
_RaisecomRemoteL3DefaultGateway_Object = MibTableColumn
raisecomRemoteL3DefaultGateway = _RaisecomRemoteL3DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 7),
    _RaisecomRemoteL3DefaultGateway_Type()
)
raisecomRemoteL3DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3DefaultGateway.setStatus("current")
_RaisecomRemoteL3ObIpAddr_Type = IpAddress
_RaisecomRemoteL3ObIpAddr_Object = MibTableColumn
raisecomRemoteL3ObIpAddr = _RaisecomRemoteL3ObIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 8),
    _RaisecomRemoteL3ObIpAddr_Type()
)
raisecomRemoteL3ObIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3ObIpAddr.setStatus("current")
_RaisecomRemoteL3ObMask_Type = IpAddress
_RaisecomRemoteL3ObMask_Object = MibTableColumn
raisecomRemoteL3ObMask = _RaisecomRemoteL3ObMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 6, 1, 9),
    _RaisecomRemoteL3ObMask_Type()
)
raisecomRemoteL3ObMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3ObMask.setStatus("current")
_RaisecomRemotePortTable_Object = MibTable
raisecomRemotePortTable = _RaisecomRemotePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7)
)
if mibBuilder.loadTexts:
    raisecomRemotePortTable.setStatus("current")
_RaisecomRemotePortEntry_Object = MibTableRow
raisecomRemotePortEntry = _RaisecomRemotePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1)
)
raisecomRemotePortEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteIfindex"),
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemotePortIfindex"),
)
if mibBuilder.loadTexts:
    raisecomRemotePortEntry.setStatus("current")
_RaisecomRemoteIfindex_Type = Integer32
_RaisecomRemoteIfindex_Object = MibTableColumn
raisecomRemoteIfindex = _RaisecomRemoteIfindex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 1),
    _RaisecomRemoteIfindex_Type()
)
raisecomRemoteIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteIfindex.setStatus("current")
_RaisecomRemotePortIfindex_Type = Integer32
_RaisecomRemotePortIfindex_Object = MibTableColumn
raisecomRemotePortIfindex = _RaisecomRemotePortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 2),
    _RaisecomRemotePortIfindex_Type()
)
raisecomRemotePortIfindex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortIfindex.setStatus("current")


class _RaisecomRemotePortType_Type(Integer32):
    """Custom type raisecomRemotePortType based on Integer32"""
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
        *(("inexistence", 0),
          ("fx-1000M", 1),
          ("tx-1000M", 2),
          ("fx-100M", 3),
          ("tx-100M", 4))
    )


_RaisecomRemotePortType_Type.__name__ = "Integer32"
_RaisecomRemotePortType_Object = MibTableColumn
raisecomRemotePortType = _RaisecomRemotePortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 3),
    _RaisecomRemotePortType_Type()
)
raisecomRemotePortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortType.setStatus("current")


class _RaisecomRemotePortName_Type(OctetString):
    """Custom type raisecomRemotePortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RaisecomRemotePortName_Type.__name__ = "OctetString"
_RaisecomRemotePortName_Object = MibTableColumn
raisecomRemotePortName = _RaisecomRemotePortName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 4),
    _RaisecomRemotePortName_Type()
)
raisecomRemotePortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortName.setStatus("current")


class _RaisecomRemotePortAdminStatus_Type(Integer32):
    """Custom type raisecomRemotePortAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RaisecomRemotePortAdminStatus_Type.__name__ = "Integer32"
_RaisecomRemotePortAdminStatus_Object = MibTableColumn
raisecomRemotePortAdminStatus = _RaisecomRemotePortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 5),
    _RaisecomRemotePortAdminStatus_Type()
)
raisecomRemotePortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortAdminStatus.setStatus("current")


class _RaisecomRemotePortOperStatus_Type(Integer32):
    """Custom type raisecomRemotePortOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_RaisecomRemotePortOperStatus_Type.__name__ = "Integer32"
_RaisecomRemotePortOperStatus_Object = MibTableColumn
raisecomRemotePortOperStatus = _RaisecomRemotePortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 6),
    _RaisecomRemotePortOperStatus_Type()
)
raisecomRemotePortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOperStatus.setStatus("current")


class _RaisecomRemotePortDuplexSpeedSet_Type(Integer32):
    """Custom type raisecomRemotePortDuplexSpeedSet based on Integer32"""
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
        *(("autonegotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("half-1000", 6),
          ("full-1000", 7))
    )


_RaisecomRemotePortDuplexSpeedSet_Type.__name__ = "Integer32"
_RaisecomRemotePortDuplexSpeedSet_Object = MibTableColumn
raisecomRemotePortDuplexSpeedSet = _RaisecomRemotePortDuplexSpeedSet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 7),
    _RaisecomRemotePortDuplexSpeedSet_Type()
)
raisecomRemotePortDuplexSpeedSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortDuplexSpeedSet.setStatus("current")


class _RaisecomRemotePortDuplexSpeedGet_Type(Integer32):
    """Custom type raisecomRemotePortDuplexSpeedGet based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("half-1000", 6),
          ("full-1000", 7),
          ("illegal", 99))
    )


_RaisecomRemotePortDuplexSpeedGet_Type.__name__ = "Integer32"
_RaisecomRemotePortDuplexSpeedGet_Object = MibTableColumn
raisecomRemotePortDuplexSpeedGet = _RaisecomRemotePortDuplexSpeedGet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 8),
    _RaisecomRemotePortDuplexSpeedGet_Type()
)
raisecomRemotePortDuplexSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortDuplexSpeedGet.setStatus("current")
_RaisecomRemotePortFlowControlEnable_Type = EnableVar
_RaisecomRemotePortFlowControlEnable_Object = MibTableColumn
raisecomRemotePortFlowControlEnable = _RaisecomRemotePortFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 9),
    _RaisecomRemotePortFlowControlEnable_Type()
)
raisecomRemotePortFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortFlowControlEnable.setStatus("current")
_RaisecomRemotePortFlowControlStatus_Type = EnableVar
_RaisecomRemotePortFlowControlStatus_Object = MibTableColumn
raisecomRemotePortFlowControlStatus = _RaisecomRemotePortFlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 10),
    _RaisecomRemotePortFlowControlStatus_Type()
)
raisecomRemotePortFlowControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortFlowControlStatus.setStatus("current")


class _RaisecomRemotePortIngressRate_Type(Integer32):
    """Custom type raisecomRemotePortIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RaisecomRemotePortIngressRate_Type.__name__ = "Integer32"
_RaisecomRemotePortIngressRate_Object = MibTableColumn
raisecomRemotePortIngressRate = _RaisecomRemotePortIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 11),
    _RaisecomRemotePortIngressRate_Type()
)
raisecomRemotePortIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortIngressRate.setStatus("current")


class _RaisecomRemotePortEgressRate_Type(Integer32):
    """Custom type raisecomRemotePortEgressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RaisecomRemotePortEgressRate_Type.__name__ = "Integer32"
_RaisecomRemotePortEgressRate_Object = MibTableColumn
raisecomRemotePortEgressRate = _RaisecomRemotePortEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 12),
    _RaisecomRemotePortEgressRate_Type()
)
raisecomRemotePortEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortEgressRate.setStatus("current")
_RaisecomRemotePortFaultPassEnable_Type = EnableVar
_RaisecomRemotePortFaultPassEnable_Object = MibTableColumn
raisecomRemotePortFaultPassEnable = _RaisecomRemotePortFaultPassEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 13),
    _RaisecomRemotePortFaultPassEnable_Type()
)
raisecomRemotePortFaultPassEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortFaultPassEnable.setStatus("current")
_RaisecomRemotePortFaultPassPorts_Type = PortList
_RaisecomRemotePortFaultPassPorts_Object = MibTableColumn
raisecomRemotePortFaultPassPorts = _RaisecomRemotePortFaultPassPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 14),
    _RaisecomRemotePortFaultPassPorts_Type()
)
raisecomRemotePortFaultPassPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortFaultPassPorts.setStatus("current")


class _RaisecomRemotePortFaultPassStatus_Type(Integer32):
    """Custom type raisecomRemotePortFaultPassStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("down", 2))
    )


_RaisecomRemotePortFaultPassStatus_Type.__name__ = "Integer32"
_RaisecomRemotePortFaultPassStatus_Object = MibTableColumn
raisecomRemotePortFaultPassStatus = _RaisecomRemotePortFaultPassStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 15),
    _RaisecomRemotePortFaultPassStatus_Type()
)
raisecomRemotePortFaultPassStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortFaultPassStatus.setStatus("current")


class _RaisecomRemotePortFaultReturnEnable_Type(Integer32):
    """Custom type raisecomRemotePortFaultReturnEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("unavailable", 3))
    )


_RaisecomRemotePortFaultReturnEnable_Type.__name__ = "Integer32"
_RaisecomRemotePortFaultReturnEnable_Object = MibTableColumn
raisecomRemotePortFaultReturnEnable = _RaisecomRemotePortFaultReturnEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 16),
    _RaisecomRemotePortFaultReturnEnable_Type()
)
raisecomRemotePortFaultReturnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortFaultReturnEnable.setStatus("current")


class _RaisecomRemotePortFaultReturnStatus_Type(Integer32):
    """Custom type raisecomRemotePortFaultReturnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("down", 2),
          ("unavailable", 3))
    )


_RaisecomRemotePortFaultReturnStatus_Type.__name__ = "Integer32"
_RaisecomRemotePortFaultReturnStatus_Object = MibTableColumn
raisecomRemotePortFaultReturnStatus = _RaisecomRemotePortFaultReturnStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 17),
    _RaisecomRemotePortFaultReturnStatus_Type()
)
raisecomRemotePortFaultReturnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortFaultReturnStatus.setStatus("current")


class _RaisecomRemotePortSD_Type(Integer32):
    """Custom type raisecomRemotePortSD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("sd", 2),
          ("unavailable", 3))
    )


_RaisecomRemotePortSD_Type.__name__ = "Integer32"
_RaisecomRemotePortSD_Object = MibTableColumn
raisecomRemotePortSD = _RaisecomRemotePortSD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 18),
    _RaisecomRemotePortSD_Type()
)
raisecomRemotePortSD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortSD.setStatus("current")


class _RaisecomRemoteOptModuleType_Type(Integer32):
    """Custom type raisecomRemoteOptModuleType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("optical-M", 1),
          ("optical-S1", 2),
          ("optical-S2", 3),
          ("optical-S3", 4),
          ("optical-SS13", 5),
          ("optical-SS15", 6),
          ("optical-SS23", 7),
          ("optical-SS25", 8),
          ("optical-SS35", 9),
          ("unknown", 10))
    )


_RaisecomRemoteOptModuleType_Type.__name__ = "Integer32"
_RaisecomRemoteOptModuleType_Object = MibTableColumn
raisecomRemoteOptModuleType = _RaisecomRemoteOptModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 19),
    _RaisecomRemoteOptModuleType_Type()
)
raisecomRemoteOptModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteOptModuleType.setStatus("current")


class _RaisecomRemotePortDescr_Type(OctetString):
    """Custom type raisecomRemotePortDescr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RaisecomRemotePortDescr_Type.__name__ = "OctetString"
_RaisecomRemotePortDescr_Object = MibTableColumn
raisecomRemotePortDescr = _RaisecomRemotePortDescr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 7, 1, 20),
    _RaisecomRemotePortDescr_Type()
)
raisecomRemotePortDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortDescr.setStatus("current")
_RaisecomRemotePortStatsTable_Object = MibTable
raisecomRemotePortStatsTable = _RaisecomRemotePortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8)
)
if mibBuilder.loadTexts:
    raisecomRemotePortStatsTable.setStatus("current")
_RaisecomRemotePortStatsEntry_Object = MibTableRow
raisecomRemotePortStatsEntry = _RaisecomRemotePortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1)
)
raisecomRemotePortStatsEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteStatsIfindex"),
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteStatsPortIfindex"),
)
if mibBuilder.loadTexts:
    raisecomRemotePortStatsEntry.setStatus("current")
_RaisecomRemoteStatsIfindex_Type = Integer32
_RaisecomRemoteStatsIfindex_Object = MibTableColumn
raisecomRemoteStatsIfindex = _RaisecomRemoteStatsIfindex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 1),
    _RaisecomRemoteStatsIfindex_Type()
)
raisecomRemoteStatsIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteStatsIfindex.setStatus("current")
_RaisecomRemoteStatsPortIfindex_Type = Integer32
_RaisecomRemoteStatsPortIfindex_Object = MibTableColumn
raisecomRemoteStatsPortIfindex = _RaisecomRemoteStatsPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 2),
    _RaisecomRemoteStatsPortIfindex_Type()
)
raisecomRemoteStatsPortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteStatsPortIfindex.setStatus("current")
_RaisecomRemotePortInOctets_Type = Counter64
_RaisecomRemotePortInOctets_Object = MibTableColumn
raisecomRemotePortInOctets = _RaisecomRemotePortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 3),
    _RaisecomRemotePortInOctets_Type()
)
raisecomRemotePortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInOctets.setStatus("current")
_RaisecomRemotePortInPkts_Type = Counter64
_RaisecomRemotePortInPkts_Object = MibTableColumn
raisecomRemotePortInPkts = _RaisecomRemotePortInPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 4),
    _RaisecomRemotePortInPkts_Type()
)
raisecomRemotePortInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInPkts.setStatus("current")
_RaisecomRemotePortInUcastPkts_Type = Counter64
_RaisecomRemotePortInUcastPkts_Object = MibTableColumn
raisecomRemotePortInUcastPkts = _RaisecomRemotePortInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 5),
    _RaisecomRemotePortInUcastPkts_Type()
)
raisecomRemotePortInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInUcastPkts.setStatus("current")
_RaisecomRemotePortInMulticastPkts_Type = Counter64
_RaisecomRemotePortInMulticastPkts_Object = MibTableColumn
raisecomRemotePortInMulticastPkts = _RaisecomRemotePortInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 6),
    _RaisecomRemotePortInMulticastPkts_Type()
)
raisecomRemotePortInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInMulticastPkts.setStatus("current")
_RaisecomRemotePortInBroadcastPkts_Type = Counter64
_RaisecomRemotePortInBroadcastPkts_Object = MibTableColumn
raisecomRemotePortInBroadcastPkts = _RaisecomRemotePortInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 7),
    _RaisecomRemotePortInBroadcastPkts_Type()
)
raisecomRemotePortInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInBroadcastPkts.setStatus("current")
_RaisecomRemotePortOutOctets_Type = Counter64
_RaisecomRemotePortOutOctets_Object = MibTableColumn
raisecomRemotePortOutOctets = _RaisecomRemotePortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 8),
    _RaisecomRemotePortOutOctets_Type()
)
raisecomRemotePortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutOctets.setStatus("current")
_RaisecomRemotePortOutPkts_Type = Counter64
_RaisecomRemotePortOutPkts_Object = MibTableColumn
raisecomRemotePortOutPkts = _RaisecomRemotePortOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 9),
    _RaisecomRemotePortOutPkts_Type()
)
raisecomRemotePortOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutPkts.setStatus("current")
_RaisecomRemotePortOutUcastPkts_Type = Counter64
_RaisecomRemotePortOutUcastPkts_Object = MibTableColumn
raisecomRemotePortOutUcastPkts = _RaisecomRemotePortOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 10),
    _RaisecomRemotePortOutUcastPkts_Type()
)
raisecomRemotePortOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutUcastPkts.setStatus("current")
_RaisecomRemotePortOutMulticastPkts_Type = Counter64
_RaisecomRemotePortOutMulticastPkts_Object = MibTableColumn
raisecomRemotePortOutMulticastPkts = _RaisecomRemotePortOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 11),
    _RaisecomRemotePortOutMulticastPkts_Type()
)
raisecomRemotePortOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutMulticastPkts.setStatus("current")
_RaisecomRemotePortOutBroadcastPkts_Type = Counter64
_RaisecomRemotePortOutBroadcastPkts_Object = MibTableColumn
raisecomRemotePortOutBroadcastPkts = _RaisecomRemotePortOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 12),
    _RaisecomRemotePortOutBroadcastPkts_Type()
)
raisecomRemotePortOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutBroadcastPkts.setStatus("current")
_RaisecomRemotePortErrorPkts_Type = Counter32
_RaisecomRemotePortErrorPkts_Object = MibTableColumn
raisecomRemotePortErrorPkts = _RaisecomRemotePortErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 13),
    _RaisecomRemotePortErrorPkts_Type()
)
raisecomRemotePortErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortErrorPkts.setStatus("current")
_RaisecomRemotePortDropEvents_Type = Counter32
_RaisecomRemotePortDropEvents_Object = MibTableColumn
raisecomRemotePortDropEvents = _RaisecomRemotePortDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 14),
    _RaisecomRemotePortDropEvents_Type()
)
raisecomRemotePortDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortDropEvents.setStatus("current")
_RaisecomRemotePortCRCAlignErrors_Type = Counter32
_RaisecomRemotePortCRCAlignErrors_Object = MibTableColumn
raisecomRemotePortCRCAlignErrors = _RaisecomRemotePortCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 15),
    _RaisecomRemotePortCRCAlignErrors_Type()
)
raisecomRemotePortCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortCRCAlignErrors.setStatus("current")
_RaisecomRemotePortUndersizePkts_Type = Counter32
_RaisecomRemotePortUndersizePkts_Object = MibTableColumn
raisecomRemotePortUndersizePkts = _RaisecomRemotePortUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 16),
    _RaisecomRemotePortUndersizePkts_Type()
)
raisecomRemotePortUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortUndersizePkts.setStatus("current")
_RaisecomRemotePortOversizePkts_Type = Counter32
_RaisecomRemotePortOversizePkts_Object = MibTableColumn
raisecomRemotePortOversizePkts = _RaisecomRemotePortOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 17),
    _RaisecomRemotePortOversizePkts_Type()
)
raisecomRemotePortOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOversizePkts.setStatus("current")
_RaisecomRemotePortFragments_Type = Counter32
_RaisecomRemotePortFragments_Object = MibTableColumn
raisecomRemotePortFragments = _RaisecomRemotePortFragments_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 18),
    _RaisecomRemotePortFragments_Type()
)
raisecomRemotePortFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortFragments.setStatus("current")
_RaisecomRemotePortJabbers_Type = Counter32
_RaisecomRemotePortJabbers_Object = MibTableColumn
raisecomRemotePortJabbers = _RaisecomRemotePortJabbers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 19),
    _RaisecomRemotePortJabbers_Type()
)
raisecomRemotePortJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortJabbers.setStatus("current")
_RaisecomRemotePortCollisions_Type = Counter32
_RaisecomRemotePortCollisions_Object = MibTableColumn
raisecomRemotePortCollisions = _RaisecomRemotePortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 8, 1, 20),
    _RaisecomRemotePortCollisions_Type()
)
raisecomRemotePortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortCollisions.setStatus("current")
_RaisecomRemoteSfpTable_Object = MibTable
raisecomRemoteSfpTable = _RaisecomRemoteSfpTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9)
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpTable.setStatus("current")
_RaisecomRemoteSfpEntry_Object = MibTableRow
raisecomRemoteSfpEntry = _RaisecomRemoteSfpEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1)
)
raisecomRemoteSfpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpEntry.setStatus("current")
_RaisecomRemoteSfpInterfaceId_Type = Integer32
_RaisecomRemoteSfpInterfaceId_Object = MibTableColumn
raisecomRemoteSfpInterfaceId = _RaisecomRemoteSfpInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 1),
    _RaisecomRemoteSfpInterfaceId_Type()
)
raisecomRemoteSfpInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpInterfaceId.setStatus("current")


class _RaisecomRemoteSfpExist_Type(Integer32):
    """Custom type raisecomRemoteSfpExist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exist", 1),
          ("notexist", 2))
    )


_RaisecomRemoteSfpExist_Type.__name__ = "Integer32"
_RaisecomRemoteSfpExist_Object = MibTableColumn
raisecomRemoteSfpExist = _RaisecomRemoteSfpExist_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 2),
    _RaisecomRemoteSfpExist_Type()
)
raisecomRemoteSfpExist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpExist.setStatus("current")


class _RaisecomRemoteSfpMediaType_Type(Integer32):
    """Custom type raisecomRemoteSfpMediaType based on Integer32"""
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
        *(("fibersingle", 0),
          ("fiber50um", 1),
          ("fiber625um", 2),
          ("copper", 3))
    )


_RaisecomRemoteSfpMediaType_Type.__name__ = "Integer32"
_RaisecomRemoteSfpMediaType_Object = MibTableColumn
raisecomRemoteSfpMediaType = _RaisecomRemoteSfpMediaType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 3),
    _RaisecomRemoteSfpMediaType_Type()
)
raisecomRemoteSfpMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpMediaType.setStatus("current")


class _RaisecomRemoteSfpRXLOS_Type(Integer32):
    """Custom type raisecomRemoteSfpRXLOS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RaisecomRemoteSfpRXLOS_Type.__name__ = "Integer32"
_RaisecomRemoteSfpRXLOS_Object = MibTableColumn
raisecomRemoteSfpRXLOS = _RaisecomRemoteSfpRXLOS_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 4),
    _RaisecomRemoteSfpRXLOS_Type()
)
raisecomRemoteSfpRXLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpRXLOS.setStatus("current")


class _RaisecomRemoteSfpTXFault_Type(Integer32):
    """Custom type raisecomRemoteSfpTXFault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("alarm", 2))
    )


_RaisecomRemoteSfpTXFault_Type.__name__ = "Integer32"
_RaisecomRemoteSfpTXFault_Object = MibTableColumn
raisecomRemoteSfpTXFault = _RaisecomRemoteSfpTXFault_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 5),
    _RaisecomRemoteSfpTXFault_Type()
)
raisecomRemoteSfpTXFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpTXFault.setStatus("current")


class _RaisecomRemoteSfpTXDisable_Type(Integer32):
    """Custom type raisecomRemoteSfpTXDisable based on Integer32"""
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


_RaisecomRemoteSfpTXDisable_Type.__name__ = "Integer32"
_RaisecomRemoteSfpTXDisable_Object = MibTableColumn
raisecomRemoteSfpTXDisable = _RaisecomRemoteSfpTXDisable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 6),
    _RaisecomRemoteSfpTXDisable_Type()
)
raisecomRemoteSfpTXDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteSfpTXDisable.setStatus("current")


class _RaisecomRemoteSfpModuleType_Type(Integer32):
    """Custom type raisecomRemoteSfpModuleType based on Integer32"""
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
        *(("unknown", 1),
          ("gbic", 2),
          ("sff", 3),
          ("sfp", 4))
    )


_RaisecomRemoteSfpModuleType_Type.__name__ = "Integer32"
_RaisecomRemoteSfpModuleType_Object = MibTableColumn
raisecomRemoteSfpModuleType = _RaisecomRemoteSfpModuleType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 7),
    _RaisecomRemoteSfpModuleType_Type()
)
raisecomRemoteSfpModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpModuleType.setStatus("current")


class _RaisecomRemoteSfpOpticalInterface_Type(Integer32):
    """Custom type raisecomRemoteSfpOpticalInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              7,
              34)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("sc", 1),
          ("lc", 7),
          ("rj45", 34))
    )


_RaisecomRemoteSfpOpticalInterface_Type.__name__ = "Integer32"
_RaisecomRemoteSfpOpticalInterface_Object = MibTableColumn
raisecomRemoteSfpOpticalInterface = _RaisecomRemoteSfpOpticalInterface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 8),
    _RaisecomRemoteSfpOpticalInterface_Type()
)
raisecomRemoteSfpOpticalInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpOpticalInterface.setStatus("current")


class _RaisecomRemoteSfpSpeedStatus_Type(Integer32):
    """Custom type raisecomRemoteSfpSpeedStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              6,
              12,
              25)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("speed125M", 1),
          ("speed155M", 2),
          ("speed622M", 6),
          ("speed1250M", 12),
          ("speed2500M", 25))
    )


_RaisecomRemoteSfpSpeedStatus_Type.__name__ = "Integer32"
_RaisecomRemoteSfpSpeedStatus_Object = MibTableColumn
raisecomRemoteSfpSpeedStatus = _RaisecomRemoteSfpSpeedStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 9),
    _RaisecomRemoteSfpSpeedStatus_Type()
)
raisecomRemoteSfpSpeedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpSpeedStatus.setStatus("current")


class _RaisecomRemoteSfpTransportDistance_Type(Integer32):
    """Custom type raisecomRemoteSfpTransportDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomRemoteSfpTransportDistance_Type.__name__ = "Integer32"
_RaisecomRemoteSfpTransportDistance_Object = MibTableColumn
raisecomRemoteSfpTransportDistance = _RaisecomRemoteSfpTransportDistance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 10),
    _RaisecomRemoteSfpTransportDistance_Type()
)
raisecomRemoteSfpTransportDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpTransportDistance.setStatus("current")


class _RaisecomRemoteSfpWaveLength_Type(Integer32):
    """Custom type raisecomRemoteSfpWaveLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomRemoteSfpWaveLength_Type.__name__ = "Integer32"
_RaisecomRemoteSfpWaveLength_Object = MibTableColumn
raisecomRemoteSfpWaveLength = _RaisecomRemoteSfpWaveLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 11),
    _RaisecomRemoteSfpWaveLength_Type()
)
raisecomRemoteSfpWaveLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpWaveLength.setStatus("current")


class _RaisecomRemoteSfpVendor_Type(OctetString):
    """Custom type raisecomRemoteSfpVendor based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RaisecomRemoteSfpVendor_Type.__name__ = "OctetString"
_RaisecomRemoteSfpVendor_Object = MibTableColumn
raisecomRemoteSfpVendor = _RaisecomRemoteSfpVendor_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 12),
    _RaisecomRemoteSfpVendor_Type()
)
raisecomRemoteSfpVendor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpVendor.setStatus("current")


class _RaisecomRemoteSfpProductType_Type(OctetString):
    """Custom type raisecomRemoteSfpProductType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RaisecomRemoteSfpProductType_Type.__name__ = "OctetString"
_RaisecomRemoteSfpProductType_Object = MibTableColumn
raisecomRemoteSfpProductType = _RaisecomRemoteSfpProductType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 13),
    _RaisecomRemoteSfpProductType_Type()
)
raisecomRemoteSfpProductType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpProductType.setStatus("current")


class _RaisecomRemoteSfpVersion_Type(OctetString):
    """Custom type raisecomRemoteSfpVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_RaisecomRemoteSfpVersion_Type.__name__ = "OctetString"
_RaisecomRemoteSfpVersion_Object = MibTableColumn
raisecomRemoteSfpVersion = _RaisecomRemoteSfpVersion_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 14),
    _RaisecomRemoteSfpVersion_Type()
)
raisecomRemoteSfpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpVersion.setStatus("current")


class _RaisecomRemoteSfpSerialNumber_Type(OctetString):
    """Custom type raisecomRemoteSfpSerialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_RaisecomRemoteSfpSerialNumber_Type.__name__ = "OctetString"
_RaisecomRemoteSfpSerialNumber_Object = MibTableColumn
raisecomRemoteSfpSerialNumber = _RaisecomRemoteSfpSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 9, 1, 15),
    _RaisecomRemoteSfpSerialNumber_Type()
)
raisecomRemoteSfpSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpSerialNumber.setStatus("current")
_RaisecomRemoteDtTable_Object = MibTable
raisecomRemoteDtTable = _RaisecomRemoteDtTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 10)
)
if mibBuilder.loadTexts:
    raisecomRemoteDtTable.setStatus("current")
_RaisecomRemoteDtEntry_Object = MibTableRow
raisecomRemoteDtEntry = _RaisecomRemoteDtEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 10, 1)
)
raisecomRemoteDtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteDtEntry.setStatus("current")


class _RaisecomRemoteDtSwitchMode_Type(Integer32):
    """Custom type raisecomRemoteDtSwitchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("transparent", 1),
          ("dot1q-vlan", 2),
          ("double-tagged-vlan", 3))
    )


_RaisecomRemoteDtSwitchMode_Type.__name__ = "Integer32"
_RaisecomRemoteDtSwitchMode_Object = MibTableColumn
raisecomRemoteDtSwitchMode = _RaisecomRemoteDtSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 10, 1, 1),
    _RaisecomRemoteDtSwitchMode_Type()
)
raisecomRemoteDtSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteDtSwitchMode.setStatus("current")


class _RaisecomRemoteDtOuterTpid_Type(Integer32):
    """Custom type raisecomRemoteDtOuterTpid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomRemoteDtOuterTpid_Type.__name__ = "Integer32"
_RaisecomRemoteDtOuterTpid_Object = MibTableColumn
raisecomRemoteDtOuterTpid = _RaisecomRemoteDtOuterTpid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 10, 1, 2),
    _RaisecomRemoteDtOuterTpid_Type()
)
raisecomRemoteDtOuterTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteDtOuterTpid.setStatus("current")


class _RaisecomRemoteDtNativeVlan_Type(Integer32):
    """Custom type raisecomRemoteDtNativeVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomRemoteDtNativeVlan_Type.__name__ = "Integer32"
_RaisecomRemoteDtNativeVlan_Object = MibTableColumn
raisecomRemoteDtNativeVlan = _RaisecomRemoteDtNativeVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 10, 1, 3),
    _RaisecomRemoteDtNativeVlan_Type()
)
raisecomRemoteDtNativeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteDtNativeVlan.setStatus("current")


class _RaisecomRemoteDtAccessPort_Type(Integer32):
    """Custom type raisecomRemoteDtAccessPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("client", 2))
    )


_RaisecomRemoteDtAccessPort_Type.__name__ = "Integer32"
_RaisecomRemoteDtAccessPort_Object = MibTableColumn
raisecomRemoteDtAccessPort = _RaisecomRemoteDtAccessPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 10, 1, 4),
    _RaisecomRemoteDtAccessPort_Type()
)
raisecomRemoteDtAccessPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteDtAccessPort.setStatus("current")
_RaisecomRemoteSendConfTable_Object = MibTable
raisecomRemoteSendConfTable = _RaisecomRemoteSendConfTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 11)
)
if mibBuilder.loadTexts:
    raisecomRemoteSendConfTable.setStatus("current")
_RaisecomRemoteSendConfEntry_Object = MibTableRow
raisecomRemoteSendConfEntry = _RaisecomRemoteSendConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 11, 1)
)
raisecomRemoteSendConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteSendConfEntry.setStatus("current")


class _RaisecomRemoteSendConf_Type(RcRemoteConfigFrameSendStatus):
    """Custom type raisecomRemoteSendConf based on RcRemoteConfigFrameSendStatus"""
    defaultValue = 5


_RaisecomRemoteSendConf_Type.__name__ = "RcRemoteConfigFrameSendStatus"
_RaisecomRemoteSendConf_Object = MibTableColumn
raisecomRemoteSendConf = _RaisecomRemoteSendConf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 11, 1, 1),
    _RaisecomRemoteSendConf_Type()
)
raisecomRemoteSendConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteSendConf.setStatus("current")
_RaisecomRemoteInLoopbackTable_Object = MibTable
raisecomRemoteInLoopbackTable = _RaisecomRemoteInLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 12)
)
if mibBuilder.loadTexts:
    raisecomRemoteInLoopbackTable.setStatus("current")
_RaisecomRemoteInLoopbackEntry_Object = MibTableRow
raisecomRemoteInLoopbackEntry = _RaisecomRemoteInLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 12, 1)
)
raisecomRemoteInLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteInLoopbackEntry.setStatus("current")


class _RaisecomRemoteInLoopbackMacExchange_Type(Integer32):
    """Custom type raisecomRemoteInLoopbackMacExchange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("exchange", 1),
          ("noexchange", 2))
    )


_RaisecomRemoteInLoopbackMacExchange_Type.__name__ = "Integer32"
_RaisecomRemoteInLoopbackMacExchange_Object = MibTableColumn
raisecomRemoteInLoopbackMacExchange = _RaisecomRemoteInLoopbackMacExchange_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 12, 1, 1),
    _RaisecomRemoteInLoopbackMacExchange_Type()
)
raisecomRemoteInLoopbackMacExchange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteInLoopbackMacExchange.setStatus("current")


class _RaisecomRemoteInLoopbackCrcRecalSet_Type(Integer32):
    """Custom type raisecomRemoteInLoopbackCrcRecalSet based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("recalculate", 1),
          ("norecalculate", 2))
    )


_RaisecomRemoteInLoopbackCrcRecalSet_Type.__name__ = "Integer32"
_RaisecomRemoteInLoopbackCrcRecalSet_Object = MibTableColumn
raisecomRemoteInLoopbackCrcRecalSet = _RaisecomRemoteInLoopbackCrcRecalSet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 12, 1, 2),
    _RaisecomRemoteInLoopbackCrcRecalSet_Type()
)
raisecomRemoteInLoopbackCrcRecalSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteInLoopbackCrcRecalSet.setStatus("current")


class _RaisecomRemoteInLoopbackCrcRecal_Type(Integer32):
    """Custom type raisecomRemoteInLoopbackCrcRecal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("recalculate", 1),
          ("norecalculate", 2))
    )


_RaisecomRemoteInLoopbackCrcRecal_Type.__name__ = "Integer32"
_RaisecomRemoteInLoopbackCrcRecal_Object = MibTableColumn
raisecomRemoteInLoopbackCrcRecal = _RaisecomRemoteInLoopbackCrcRecal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 12, 1, 3),
    _RaisecomRemoteInLoopbackCrcRecal_Type()
)
raisecomRemoteInLoopbackCrcRecal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteInLoopbackCrcRecal.setStatus("current")


class _RaisecomRemoteInLoopbackStatus_Type(Integer32):
    """Custom type raisecomRemoteInLoopbackStatus based on Integer32"""
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
        *(("noloopback", 1),
          ("initiatinginloopback", 2),
          ("inloopback", 3),
          ("outloopback", 4),
          ("terminatingInloopback", 5))
    )


_RaisecomRemoteInLoopbackStatus_Type.__name__ = "Integer32"
_RaisecomRemoteInLoopbackStatus_Object = MibTableColumn
raisecomRemoteInLoopbackStatus = _RaisecomRemoteInLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 12, 1, 4),
    _RaisecomRemoteInLoopbackStatus_Type()
)
raisecomRemoteInLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteInLoopbackStatus.setStatus("current")
_RaisecomRemoteVctTable_Object = MibTable
raisecomRemoteVctTable = _RaisecomRemoteVctTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 13)
)
if mibBuilder.loadTexts:
    raisecomRemoteVctTable.setStatus("current")
_RaisecomRemoteVctEntry_Object = MibTableRow
raisecomRemoteVctEntry = _RaisecomRemoteVctEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 13, 1)
)
raisecomRemoteVctEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteVctEntry.setStatus("current")


class _RaisecomRemoteVctAttribute_Type(Integer32):
    """Custom type raisecomRemoteVctAttribute based on Integer32"""
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
        *(("unSupported", 1),
          ("neverIssued", 2),
          ("issued", 3),
          ("testing", 4),
          ("begin", 5))
    )


_RaisecomRemoteVctAttribute_Type.__name__ = "Integer32"
_RaisecomRemoteVctAttribute_Object = MibTableColumn
raisecomRemoteVctAttribute = _RaisecomRemoteVctAttribute_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 13, 1, 1),
    _RaisecomRemoteVctAttribute_Type()
)
raisecomRemoteVctAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteVctAttribute.setStatus("current")


class _RaisecomRemoteVctStatus_Type(Integer32):
    """Custom type raisecomRemoteVctStatus based on Integer32"""
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
        *(("normal", 1),
          ("open", 2),
          ("shorted", 3),
          ("error", 4),
          ("invalidation", 5))
    )


_RaisecomRemoteVctStatus_Type.__name__ = "Integer32"
_RaisecomRemoteVctStatus_Object = MibTableColumn
raisecomRemoteVctStatus = _RaisecomRemoteVctStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 13, 1, 2),
    _RaisecomRemoteVctStatus_Type()
)
raisecomRemoteVctStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVctStatus.setStatus("current")
_RaisecomRemoteVctLength_Type = Integer32
_RaisecomRemoteVctLength_Object = MibTableColumn
raisecomRemoteVctLength = _RaisecomRemoteVctLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 13, 1, 3),
    _RaisecomRemoteVctLength_Type()
)
raisecomRemoteVctLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVctLength.setStatus("current")
_RaisecomRemoteVlanConfigTable_Object = MibTable
raisecomRemoteVlanConfigTable = _RaisecomRemoteVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14)
)
if mibBuilder.loadTexts:
    raisecomRemoteVlanConfigTable.setStatus("current")
_RaisecomRemoteVlanConfigEntry_Object = MibTableRow
raisecomRemoteVlanConfigEntry = _RaisecomRemoteVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1)
)
raisecomRemoteVlanConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteVlanConfigEntry.setStatus("current")
_RaisecomRemoteVlanStatus_Type = RcRemoteVlanStatus
_RaisecomRemoteVlanStatus_Object = MibTableColumn
raisecomRemoteVlanStatus = _RaisecomRemoteVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 1),
    _RaisecomRemoteVlanStatus_Type()
)
raisecomRemoteVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteVlanStatus.setStatus("current")
_RaisecomRemoteCosStatus_Type = TruthValue
_RaisecomRemoteCosStatus_Object = MibTableColumn
raisecomRemoteCosStatus = _RaisecomRemoteCosStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 2),
    _RaisecomRemoteCosStatus_Type()
)
raisecomRemoteCosStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCosStatus.setStatus("current")
_RaisecomRemoteFiberPortTagType_Type = RcRemotePortTagStatus
_RaisecomRemoteFiberPortTagType_Object = MibTableColumn
raisecomRemoteFiberPortTagType = _RaisecomRemoteFiberPortTagType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 3),
    _RaisecomRemoteFiberPortTagType_Type()
)
raisecomRemoteFiberPortTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteFiberPortTagType.setStatus("current")


class _RaisecomRemoteFiberPortPriority_Type(Integer32):
    """Custom type raisecomRemoteFiberPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomRemoteFiberPortPriority_Type.__name__ = "Integer32"
_RaisecomRemoteFiberPortPriority_Object = MibTableColumn
raisecomRemoteFiberPortPriority = _RaisecomRemoteFiberPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 4),
    _RaisecomRemoteFiberPortPriority_Type()
)
raisecomRemoteFiberPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteFiberPortPriority.setStatus("current")


class _RaisecomRemoteFiberPortPvid_Type(Integer32):
    """Custom type raisecomRemoteFiberPortPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomRemoteFiberPortPvid_Type.__name__ = "Integer32"
_RaisecomRemoteFiberPortPvid_Object = MibTableColumn
raisecomRemoteFiberPortPvid = _RaisecomRemoteFiberPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 5),
    _RaisecomRemoteFiberPortPvid_Type()
)
raisecomRemoteFiberPortPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteFiberPortPvid.setStatus("current")
_RaisecomRemoteCablePortTagType_Type = RcRemotePortTagStatus
_RaisecomRemoteCablePortTagType_Object = MibTableColumn
raisecomRemoteCablePortTagType = _RaisecomRemoteCablePortTagType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 6),
    _RaisecomRemoteCablePortTagType_Type()
)
raisecomRemoteCablePortTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCablePortTagType.setStatus("current")


class _RaisecomRemoteCablePortPriority_Type(Integer32):
    """Custom type raisecomRemoteCablePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomRemoteCablePortPriority_Type.__name__ = "Integer32"
_RaisecomRemoteCablePortPriority_Object = MibTableColumn
raisecomRemoteCablePortPriority = _RaisecomRemoteCablePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 7),
    _RaisecomRemoteCablePortPriority_Type()
)
raisecomRemoteCablePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCablePortPriority.setStatus("current")


class _RaisecomRemoteCablePortPvid_Type(Integer32):
    """Custom type raisecomRemoteCablePortPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomRemoteCablePortPvid_Type.__name__ = "Integer32"
_RaisecomRemoteCablePortPvid_Object = MibTableColumn
raisecomRemoteCablePortPvid = _RaisecomRemoteCablePortPvid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 8),
    _RaisecomRemoteCablePortPvid_Type()
)
raisecomRemoteCablePortPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCablePortPvid.setStatus("current")
_RaisecomRemoteCpuPortTagType_Type = RcRemotePortTagStatus
_RaisecomRemoteCpuPortTagType_Object = MibTableColumn
raisecomRemoteCpuPortTagType = _RaisecomRemoteCpuPortTagType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 9),
    _RaisecomRemoteCpuPortTagType_Type()
)
raisecomRemoteCpuPortTagType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCpuPortTagType.setStatus("current")


class _RaisecomRemoteCpuPortPriority_Type(Integer32):
    """Custom type raisecomRemoteCpuPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomRemoteCpuPortPriority_Type.__name__ = "Integer32"
_RaisecomRemoteCpuPortPriority_Object = MibTableColumn
raisecomRemoteCpuPortPriority = _RaisecomRemoteCpuPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 10),
    _RaisecomRemoteCpuPortPriority_Type()
)
raisecomRemoteCpuPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCpuPortPriority.setStatus("current")


class _RaisecomRemoteCpuPortPvid_Type(Integer32):
    """Custom type raisecomRemoteCpuPortPvid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomRemoteCpuPortPvid_Type.__name__ = "Integer32"
_RaisecomRemoteCpuPortPvid_Object = MibTableColumn
raisecomRemoteCpuPortPvid = _RaisecomRemoteCpuPortPvid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 11),
    _RaisecomRemoteCpuPortPvid_Type()
)
raisecomRemoteCpuPortPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCpuPortPvid.setStatus("current")


class _RaisecomRemoteSendVlanConf_Type(RcRemoteConfigFrameSendStatus):
    """Custom type raisecomRemoteSendVlanConf based on RcRemoteConfigFrameSendStatus"""
    defaultValue = 5


_RaisecomRemoteSendVlanConf_Type.__name__ = "RcRemoteConfigFrameSendStatus"
_RaisecomRemoteSendVlanConf_Object = MibTableColumn
raisecomRemoteSendVlanConf = _RaisecomRemoteSendVlanConf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 14, 1, 12),
    _RaisecomRemoteSendVlanConf_Type()
)
raisecomRemoteSendVlanConf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteSendVlanConf.setStatus("current")
_RaisecomRemoteVlanGroupTable_Object = MibTable
raisecomRemoteVlanGroupTable = _RaisecomRemoteVlanGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 15)
)
if mibBuilder.loadTexts:
    raisecomRemoteVlanGroupTable.setStatus("current")
_RaisecomRemoteVlanGroupEntry_Object = MibTableRow
raisecomRemoteVlanGroupEntry = _RaisecomRemoteVlanGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 15, 1)
)
raisecomRemoteVlanGroupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemoteVlanGroupIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteVlanGroupEntry.setStatus("current")


class _RaisecomRemoteVlanGroupIndex_Type(Integer32):
    """Custom type raisecomRemoteVlanGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RaisecomRemoteVlanGroupIndex_Type.__name__ = "Integer32"
_RaisecomRemoteVlanGroupIndex_Object = MibTableColumn
raisecomRemoteVlanGroupIndex = _RaisecomRemoteVlanGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 15, 1, 1),
    _RaisecomRemoteVlanGroupIndex_Type()
)
raisecomRemoteVlanGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteVlanGroupIndex.setStatus("current")


class _RaisecomRemoteVlanId_Type(Integer32):
    """Custom type raisecomRemoteVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RaisecomRemoteVlanId_Type.__name__ = "Integer32"
_RaisecomRemoteVlanId_Object = MibTableColumn
raisecomRemoteVlanId = _RaisecomRemoteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 15, 1, 2),
    _RaisecomRemoteVlanId_Type()
)
raisecomRemoteVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteVlanId.setStatus("current")


class _RaisecomRemoteVlanMember_Type(Integer32):
    """Custom type raisecomRemoteVlanMember based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RaisecomRemoteVlanMember_Type.__name__ = "Integer32"
_RaisecomRemoteVlanMember_Object = MibTableColumn
raisecomRemoteVlanMember = _RaisecomRemoteVlanMember_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 15, 1, 3),
    _RaisecomRemoteVlanMember_Type()
)
raisecomRemoteVlanMember.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteVlanMember.setStatus("current")
_RaisecomRemoteSfpDdmTable_Object = MibTable
raisecomRemoteSfpDdmTable = _RaisecomRemoteSfpDdmTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16)
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmTable.setStatus("current")
_RaisecomRemoteSfpDdmEntry_Object = MibTableRow
raisecomRemoteSfpDdmEntry = _RaisecomRemoteSfpDdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1)
)
raisecomRemoteSfpDdmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmEntry.setStatus("current")
_RaisecomRemoteSfpDdmValid_Type = TruthValue
_RaisecomRemoteSfpDdmValid_Object = MibTableColumn
raisecomRemoteSfpDdmValid = _RaisecomRemoteSfpDdmValid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 1),
    _RaisecomRemoteSfpDdmValid_Type()
)
raisecomRemoteSfpDdmValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmValid.setStatus("current")
_RaisecomRemoteSfpDdmMode_Type = RcRemoteSfpDdmMode
_RaisecomRemoteSfpDdmMode_Object = MibTableColumn
raisecomRemoteSfpDdmMode = _RaisecomRemoteSfpDdmMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 2),
    _RaisecomRemoteSfpDdmMode_Type()
)
raisecomRemoteSfpDdmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmMode.setStatus("current")


class _RaisecomRemoteSfpDdmTemperature_Type(Integer32):
    """Custom type raisecomRemoteSfpDdmTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128000, 127996),
    )


_RaisecomRemoteSfpDdmTemperature_Type.__name__ = "Integer32"
_RaisecomRemoteSfpDdmTemperature_Object = MibTableColumn
raisecomRemoteSfpDdmTemperature = _RaisecomRemoteSfpDdmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 3),
    _RaisecomRemoteSfpDdmTemperature_Type()
)
raisecomRemoteSfpDdmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmTemperature.setStatus("current")


class _RaisecomRemoteSfpDdmSupplyVolt_Type(Integer32):
    """Custom type raisecomRemoteSfpDdmSupplyVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_RaisecomRemoteSfpDdmSupplyVolt_Type.__name__ = "Integer32"
_RaisecomRemoteSfpDdmSupplyVolt_Object = MibTableColumn
raisecomRemoteSfpDdmSupplyVolt = _RaisecomRemoteSfpDdmSupplyVolt_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 4),
    _RaisecomRemoteSfpDdmSupplyVolt_Type()
)
raisecomRemoteSfpDdmSupplyVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmSupplyVolt.setStatus("current")


class _RaisecomRemoteSfpDdmBiasCurrent_Type(Integer32):
    """Custom type raisecomRemoteSfpDdmBiasCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65500),
    )


_RaisecomRemoteSfpDdmBiasCurrent_Type.__name__ = "Integer32"
_RaisecomRemoteSfpDdmBiasCurrent_Object = MibTableColumn
raisecomRemoteSfpDdmBiasCurrent = _RaisecomRemoteSfpDdmBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 5),
    _RaisecomRemoteSfpDdmBiasCurrent_Type()
)
raisecomRemoteSfpDdmBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmBiasCurrent.setStatus("current")


class _RaisecomRemoteSfpDdmOpticalTxPower_Type(Integer32):
    """Custom type raisecomRemoteSfpDdmOpticalTxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomRemoteSfpDdmOpticalTxPower_Type.__name__ = "Integer32"
_RaisecomRemoteSfpDdmOpticalTxPower_Object = MibTableColumn
raisecomRemoteSfpDdmOpticalTxPower = _RaisecomRemoteSfpDdmOpticalTxPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 6),
    _RaisecomRemoteSfpDdmOpticalTxPower_Type()
)
raisecomRemoteSfpDdmOpticalTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmOpticalTxPower.setStatus("current")


class _RaisecomRemoteSfpDdmOpticalRxPower_Type(Integer32):
    """Custom type raisecomRemoteSfpDdmOpticalRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomRemoteSfpDdmOpticalRxPower_Type.__name__ = "Integer32"
_RaisecomRemoteSfpDdmOpticalRxPower_Object = MibTableColumn
raisecomRemoteSfpDdmOpticalRxPower = _RaisecomRemoteSfpDdmOpticalRxPower_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 7),
    _RaisecomRemoteSfpDdmOpticalRxPower_Type()
)
raisecomRemoteSfpDdmOpticalRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmOpticalRxPower.setStatus("current")
_RaisecomRemoteSfpDdmAlarm_Type = TruthValue
_RaisecomRemoteSfpDdmAlarm_Object = MibTableColumn
raisecomRemoteSfpDdmAlarm = _RaisecomRemoteSfpDdmAlarm_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 8),
    _RaisecomRemoteSfpDdmAlarm_Type()
)
raisecomRemoteSfpDdmAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmAlarm.setStatus("current")
_RaisecomRemoteSfpDdmAlarmTemStatus_Type = RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmTemStatus_Object = MibTableColumn
raisecomRemoteSfpDdmAlarmTemStatus = _RaisecomRemoteSfpDdmAlarmTemStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 9),
    _RaisecomRemoteSfpDdmAlarmTemStatus_Type()
)
raisecomRemoteSfpDdmAlarmTemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmAlarmTemStatus.setStatus("current")
_RaisecomRemoteSfpDdmAlarmVoltStatus_Type = RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmVoltStatus_Object = MibTableColumn
raisecomRemoteSfpDdmAlarmVoltStatus = _RaisecomRemoteSfpDdmAlarmVoltStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 10),
    _RaisecomRemoteSfpDdmAlarmVoltStatus_Type()
)
raisecomRemoteSfpDdmAlarmVoltStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmAlarmVoltStatus.setStatus("current")
_RaisecomRemoteSfpDdmAlarmCurrentStatus_Type = RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmCurrentStatus_Object = MibTableColumn
raisecomRemoteSfpDdmAlarmCurrentStatus = _RaisecomRemoteSfpDdmAlarmCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 11),
    _RaisecomRemoteSfpDdmAlarmCurrentStatus_Type()
)
raisecomRemoteSfpDdmAlarmCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmAlarmCurrentStatus.setStatus("current")
_RaisecomRemoteSfpDdmAlarmTxPowerStatus_Type = RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmTxPowerStatus_Object = MibTableColumn
raisecomRemoteSfpDdmAlarmTxPowerStatus = _RaisecomRemoteSfpDdmAlarmTxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 12),
    _RaisecomRemoteSfpDdmAlarmTxPowerStatus_Type()
)
raisecomRemoteSfpDdmAlarmTxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmAlarmTxPowerStatus.setStatus("current")
_RaisecomRemoteSfpDdmAlarmRxPowerStatus_Type = RcRemoteSfpDdmAlarmStatus
_RaisecomRemoteSfpDdmAlarmRxPowerStatus_Object = MibTableColumn
raisecomRemoteSfpDdmAlarmRxPowerStatus = _RaisecomRemoteSfpDdmAlarmRxPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 1, 16, 1, 13),
    _RaisecomRemoteSfpDdmAlarmRxPowerStatus_Type()
)
raisecomRemoteSfpDdmAlarmRxPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmAlarmRxPowerStatus.setStatus("current")
_RaisecomRemoteManagementLocalMibTraps_ObjectIdentity = ObjectIdentity
raisecomRemoteManagementLocalMibTraps = _RaisecomRemoteManagementLocalMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2)
)

# Managed Objects groups


# Notification objects

raisecomRemotePortLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 1)
)
raisecomRemotePortLinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemotePortIfindex"))
)
if mibBuilder.loadTexts:
    raisecomRemotePortLinkUp.setStatus(
        "current"
    )

raisecomRemotePortLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 2)
)
raisecomRemotePortLinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB", "raisecomRemotePortIfindex"))
)
if mibBuilder.loadTexts:
    raisecomRemotePortLinkDown.setStatus(
        "current"
    )

raisecomRemoteSfpDdmTemNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 3)
)
raisecomRemoteSfpDdmTemNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmTemNormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmTemAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 4)
)
raisecomRemoteSfpDdmTemAbnormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmTemAbnormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmVoltNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 5)
)
raisecomRemoteSfpDdmVoltNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmVoltNormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmVoltAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 6)
)
raisecomRemoteSfpDdmVoltAbnormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmVoltAbnormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmCurrentNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 7)
)
raisecomRemoteSfpDdmCurrentNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmCurrentNormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmCurrentAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 8)
)
raisecomRemoteSfpDdmCurrentAbnormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmCurrentAbnormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmTxPowerNomal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 9)
)
raisecomRemoteSfpDdmTxPowerNomal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmTxPowerNomal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmTxPowerAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 10)
)
raisecomRemoteSfpDdmTxPowerAbnormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmTxPowerAbnormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmRxPowerNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 11)
)
raisecomRemoteSfpDdmRxPowerNormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmRxPowerNormal.setStatus(
        "current"
    )

raisecomRemoteSfpDdmRxPowerAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 12, 2, 12)
)
raisecomRemoteSfpDdmRxPowerAbnormal.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    raisecomRemoteSfpDdmRxPowerAbnormal.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-REMOTE-MANAGEMENT-LOCAL-MIB",
    **{"RcRemoteVlanStatus": RcRemoteVlanStatus,
       "RcRemotePortTagStatus": RcRemotePortTagStatus,
       "RcRemoteConfigFrameSendStatus": RcRemoteConfigFrameSendStatus,
       "RcRemoteSfpDdmMode": RcRemoteSfpDdmMode,
       "RcRemoteSfpDdmAlarmStatus": RcRemoteSfpDdmAlarmStatus,
       "raisecomRemoteManagementLocal": raisecomRemoteManagementLocal,
       "raisecomRemoteManagementLocalMibObjects": raisecomRemoteManagementLocalMibObjects,
       "raisecomRemoteTrapEnable": raisecomRemoteTrapEnable,
       "raisecomRemoteInvariableInfoTable": raisecomRemoteInvariableInfoTable,
       "raisecomRemoteInvariableInfoEntry": raisecomRemoteInvariableInfoEntry,
       "raisecomRemoteInvariableInfoIndex": raisecomRemoteInvariableInfoIndex,
       "raisecomRemoteSysOid": raisecomRemoteSysOid,
       "raisecomRemoteModuleType": raisecomRemoteModuleType,
       "raisecomRemoteOidCapability": raisecomRemoteOidCapability,
       "raisecomRemoteFileTransCapability": raisecomRemoteFileTransCapability,
       "raisecomRemoteOtherCapability": raisecomRemoteOtherCapability,
       "raisecomRemoteMainChipId": raisecomRemoteMainChipId,
       "raisecomRemoteFpgaChipId": raisecomRemoteFpgaChipId,
       "raisecomRemoteFpgaSwVer": raisecomRemoteFpgaSwVer,
       "raisecomRemoteSystemSwVer": raisecomRemoteSystemSwVer,
       "raisecomRemoteSystemHwVer": raisecomRemoteSystemHwVer,
       "raisecomRemotePortNum": raisecomRemotePortNum,
       "raisecomRemoteDeviceName": raisecomRemoteDeviceName,
       "raisecomRemoteInvariableInfoStatus": raisecomRemoteInvariableInfoStatus,
       "raisecomRemoteEnvironmentTable": raisecomRemoteEnvironmentTable,
       "raisecomRemoteEnvironmentEntry": raisecomRemoteEnvironmentEntry,
       "raisecomRemoteEnvironmentIndex": raisecomRemoteEnvironmentIndex,
       "raisecomRemoteTemperature": raisecomRemoteTemperature,
       "raisecomRemoteVolt3300": raisecomRemoteVolt3300,
       "raisecomRemoteVolt2500": raisecomRemoteVolt2500,
       "raisecomRemoteVolt1800": raisecomRemoteVolt1800,
       "raisecomRemoteVolt1200": raisecomRemoteVolt1200,
       "raisecomRemoteVoltNormal": raisecomRemoteVoltNormal,
       "raisecomRemoteSysCfgTable": raisecomRemoteSysCfgTable,
       "raisecomRemoteSysCfgEntry": raisecomRemoteSysCfgEntry,
       "raisecomRemoteSysCfgIndex": raisecomRemoteSysCfgIndex,
       "raisecomRemoteSysOperation": raisecomRemoteSysOperation,
       "raisecomRemoteSysOperationState": raisecomRemoteSysOperationState,
       "raisecomRemoteHostName": raisecomRemoteHostName,
       "raisecomRemoteOamNotificationEnable": raisecomRemoteOamNotificationEnable,
       "raisecomRemoteMaxAllowedFrameLength": raisecomRemoteMaxAllowedFrameLength,
       "raisecomRemoteCommunityTable": raisecomRemoteCommunityTable,
       "raisecomRemoteCommunityEntry": raisecomRemoteCommunityEntry,
       "raisecomRemoteCommunityIndex": raisecomRemoteCommunityIndex,
       "raisecomRemoteCommunityName": raisecomRemoteCommunityName,
       "raisecomRemoteCommunityPermission": raisecomRemoteCommunityPermission,
       "raisecomRemoteL3Table": raisecomRemoteL3Table,
       "raisecomRemoteL3Entry": raisecomRemoteL3Entry,
       "raisecomRemoteL3Index": raisecomRemoteL3Index,
       "raisecomRemoteL3IpAddr": raisecomRemoteL3IpAddr,
       "raisecomRemoteL3Mask": raisecomRemoteL3Mask,
       "raisecomRemoteL3VidIface": raisecomRemoteL3VidIface,
       "raisecomRemoteL3VidMemberPorts": raisecomRemoteL3VidMemberPorts,
       "raisecomRemoteL3VidUntaggedPorts": raisecomRemoteL3VidUntaggedPorts,
       "raisecomRemoteL3DefaultGateway": raisecomRemoteL3DefaultGateway,
       "raisecomRemoteL3ObIpAddr": raisecomRemoteL3ObIpAddr,
       "raisecomRemoteL3ObMask": raisecomRemoteL3ObMask,
       "raisecomRemotePortTable": raisecomRemotePortTable,
       "raisecomRemotePortEntry": raisecomRemotePortEntry,
       "raisecomRemoteIfindex": raisecomRemoteIfindex,
       "raisecomRemotePortIfindex": raisecomRemotePortIfindex,
       "raisecomRemotePortType": raisecomRemotePortType,
       "raisecomRemotePortName": raisecomRemotePortName,
       "raisecomRemotePortAdminStatus": raisecomRemotePortAdminStatus,
       "raisecomRemotePortOperStatus": raisecomRemotePortOperStatus,
       "raisecomRemotePortDuplexSpeedSet": raisecomRemotePortDuplexSpeedSet,
       "raisecomRemotePortDuplexSpeedGet": raisecomRemotePortDuplexSpeedGet,
       "raisecomRemotePortFlowControlEnable": raisecomRemotePortFlowControlEnable,
       "raisecomRemotePortFlowControlStatus": raisecomRemotePortFlowControlStatus,
       "raisecomRemotePortIngressRate": raisecomRemotePortIngressRate,
       "raisecomRemotePortEgressRate": raisecomRemotePortEgressRate,
       "raisecomRemotePortFaultPassEnable": raisecomRemotePortFaultPassEnable,
       "raisecomRemotePortFaultPassPorts": raisecomRemotePortFaultPassPorts,
       "raisecomRemotePortFaultPassStatus": raisecomRemotePortFaultPassStatus,
       "raisecomRemotePortFaultReturnEnable": raisecomRemotePortFaultReturnEnable,
       "raisecomRemotePortFaultReturnStatus": raisecomRemotePortFaultReturnStatus,
       "raisecomRemotePortSD": raisecomRemotePortSD,
       "raisecomRemoteOptModuleType": raisecomRemoteOptModuleType,
       "raisecomRemotePortDescr": raisecomRemotePortDescr,
       "raisecomRemotePortStatsTable": raisecomRemotePortStatsTable,
       "raisecomRemotePortStatsEntry": raisecomRemotePortStatsEntry,
       "raisecomRemoteStatsIfindex": raisecomRemoteStatsIfindex,
       "raisecomRemoteStatsPortIfindex": raisecomRemoteStatsPortIfindex,
       "raisecomRemotePortInOctets": raisecomRemotePortInOctets,
       "raisecomRemotePortInPkts": raisecomRemotePortInPkts,
       "raisecomRemotePortInUcastPkts": raisecomRemotePortInUcastPkts,
       "raisecomRemotePortInMulticastPkts": raisecomRemotePortInMulticastPkts,
       "raisecomRemotePortInBroadcastPkts": raisecomRemotePortInBroadcastPkts,
       "raisecomRemotePortOutOctets": raisecomRemotePortOutOctets,
       "raisecomRemotePortOutPkts": raisecomRemotePortOutPkts,
       "raisecomRemotePortOutUcastPkts": raisecomRemotePortOutUcastPkts,
       "raisecomRemotePortOutMulticastPkts": raisecomRemotePortOutMulticastPkts,
       "raisecomRemotePortOutBroadcastPkts": raisecomRemotePortOutBroadcastPkts,
       "raisecomRemotePortErrorPkts": raisecomRemotePortErrorPkts,
       "raisecomRemotePortDropEvents": raisecomRemotePortDropEvents,
       "raisecomRemotePortCRCAlignErrors": raisecomRemotePortCRCAlignErrors,
       "raisecomRemotePortUndersizePkts": raisecomRemotePortUndersizePkts,
       "raisecomRemotePortOversizePkts": raisecomRemotePortOversizePkts,
       "raisecomRemotePortFragments": raisecomRemotePortFragments,
       "raisecomRemotePortJabbers": raisecomRemotePortJabbers,
       "raisecomRemotePortCollisions": raisecomRemotePortCollisions,
       "raisecomRemoteSfpTable": raisecomRemoteSfpTable,
       "raisecomRemoteSfpEntry": raisecomRemoteSfpEntry,
       "raisecomRemoteSfpInterfaceId": raisecomRemoteSfpInterfaceId,
       "raisecomRemoteSfpExist": raisecomRemoteSfpExist,
       "raisecomRemoteSfpMediaType": raisecomRemoteSfpMediaType,
       "raisecomRemoteSfpRXLOS": raisecomRemoteSfpRXLOS,
       "raisecomRemoteSfpTXFault": raisecomRemoteSfpTXFault,
       "raisecomRemoteSfpTXDisable": raisecomRemoteSfpTXDisable,
       "raisecomRemoteSfpModuleType": raisecomRemoteSfpModuleType,
       "raisecomRemoteSfpOpticalInterface": raisecomRemoteSfpOpticalInterface,
       "raisecomRemoteSfpSpeedStatus": raisecomRemoteSfpSpeedStatus,
       "raisecomRemoteSfpTransportDistance": raisecomRemoteSfpTransportDistance,
       "raisecomRemoteSfpWaveLength": raisecomRemoteSfpWaveLength,
       "raisecomRemoteSfpVendor": raisecomRemoteSfpVendor,
       "raisecomRemoteSfpProductType": raisecomRemoteSfpProductType,
       "raisecomRemoteSfpVersion": raisecomRemoteSfpVersion,
       "raisecomRemoteSfpSerialNumber": raisecomRemoteSfpSerialNumber,
       "raisecomRemoteDtTable": raisecomRemoteDtTable,
       "raisecomRemoteDtEntry": raisecomRemoteDtEntry,
       "raisecomRemoteDtSwitchMode": raisecomRemoteDtSwitchMode,
       "raisecomRemoteDtOuterTpid": raisecomRemoteDtOuterTpid,
       "raisecomRemoteDtNativeVlan": raisecomRemoteDtNativeVlan,
       "raisecomRemoteDtAccessPort": raisecomRemoteDtAccessPort,
       "raisecomRemoteSendConfTable": raisecomRemoteSendConfTable,
       "raisecomRemoteSendConfEntry": raisecomRemoteSendConfEntry,
       "raisecomRemoteSendConf": raisecomRemoteSendConf,
       "raisecomRemoteInLoopbackTable": raisecomRemoteInLoopbackTable,
       "raisecomRemoteInLoopbackEntry": raisecomRemoteInLoopbackEntry,
       "raisecomRemoteInLoopbackMacExchange": raisecomRemoteInLoopbackMacExchange,
       "raisecomRemoteInLoopbackCrcRecalSet": raisecomRemoteInLoopbackCrcRecalSet,
       "raisecomRemoteInLoopbackCrcRecal": raisecomRemoteInLoopbackCrcRecal,
       "raisecomRemoteInLoopbackStatus": raisecomRemoteInLoopbackStatus,
       "raisecomRemoteVctTable": raisecomRemoteVctTable,
       "raisecomRemoteVctEntry": raisecomRemoteVctEntry,
       "raisecomRemoteVctAttribute": raisecomRemoteVctAttribute,
       "raisecomRemoteVctStatus": raisecomRemoteVctStatus,
       "raisecomRemoteVctLength": raisecomRemoteVctLength,
       "raisecomRemoteVlanConfigTable": raisecomRemoteVlanConfigTable,
       "raisecomRemoteVlanConfigEntry": raisecomRemoteVlanConfigEntry,
       "raisecomRemoteVlanStatus": raisecomRemoteVlanStatus,
       "raisecomRemoteCosStatus": raisecomRemoteCosStatus,
       "raisecomRemoteFiberPortTagType": raisecomRemoteFiberPortTagType,
       "raisecomRemoteFiberPortPriority": raisecomRemoteFiberPortPriority,
       "raisecomRemoteFiberPortPvid": raisecomRemoteFiberPortPvid,
       "raisecomRemoteCablePortTagType": raisecomRemoteCablePortTagType,
       "raisecomRemoteCablePortPriority": raisecomRemoteCablePortPriority,
       "raisecomRemoteCablePortPvid": raisecomRemoteCablePortPvid,
       "raisecomRemoteCpuPortTagType": raisecomRemoteCpuPortTagType,
       "raisecomRemoteCpuPortPriority": raisecomRemoteCpuPortPriority,
       "raisecomRemoteCpuPortPvid": raisecomRemoteCpuPortPvid,
       "raisecomRemoteSendVlanConf": raisecomRemoteSendVlanConf,
       "raisecomRemoteVlanGroupTable": raisecomRemoteVlanGroupTable,
       "raisecomRemoteVlanGroupEntry": raisecomRemoteVlanGroupEntry,
       "raisecomRemoteVlanGroupIndex": raisecomRemoteVlanGroupIndex,
       "raisecomRemoteVlanId": raisecomRemoteVlanId,
       "raisecomRemoteVlanMember": raisecomRemoteVlanMember,
       "raisecomRemoteSfpDdmTable": raisecomRemoteSfpDdmTable,
       "raisecomRemoteSfpDdmEntry": raisecomRemoteSfpDdmEntry,
       "raisecomRemoteSfpDdmValid": raisecomRemoteSfpDdmValid,
       "raisecomRemoteSfpDdmMode": raisecomRemoteSfpDdmMode,
       "raisecomRemoteSfpDdmTemperature": raisecomRemoteSfpDdmTemperature,
       "raisecomRemoteSfpDdmSupplyVolt": raisecomRemoteSfpDdmSupplyVolt,
       "raisecomRemoteSfpDdmBiasCurrent": raisecomRemoteSfpDdmBiasCurrent,
       "raisecomRemoteSfpDdmOpticalTxPower": raisecomRemoteSfpDdmOpticalTxPower,
       "raisecomRemoteSfpDdmOpticalRxPower": raisecomRemoteSfpDdmOpticalRxPower,
       "raisecomRemoteSfpDdmAlarm": raisecomRemoteSfpDdmAlarm,
       "raisecomRemoteSfpDdmAlarmTemStatus": raisecomRemoteSfpDdmAlarmTemStatus,
       "raisecomRemoteSfpDdmAlarmVoltStatus": raisecomRemoteSfpDdmAlarmVoltStatus,
       "raisecomRemoteSfpDdmAlarmCurrentStatus": raisecomRemoteSfpDdmAlarmCurrentStatus,
       "raisecomRemoteSfpDdmAlarmTxPowerStatus": raisecomRemoteSfpDdmAlarmTxPowerStatus,
       "raisecomRemoteSfpDdmAlarmRxPowerStatus": raisecomRemoteSfpDdmAlarmRxPowerStatus,
       "raisecomRemoteManagementLocalMibTraps": raisecomRemoteManagementLocalMibTraps,
       "raisecomRemotePortLinkUp": raisecomRemotePortLinkUp,
       "raisecomRemotePortLinkDown": raisecomRemotePortLinkDown,
       "raisecomRemoteSfpDdmTemNormal": raisecomRemoteSfpDdmTemNormal,
       "raisecomRemoteSfpDdmTemAbnormal": raisecomRemoteSfpDdmTemAbnormal,
       "raisecomRemoteSfpDdmVoltNormal": raisecomRemoteSfpDdmVoltNormal,
       "raisecomRemoteSfpDdmVoltAbnormal": raisecomRemoteSfpDdmVoltAbnormal,
       "raisecomRemoteSfpDdmCurrentNormal": raisecomRemoteSfpDdmCurrentNormal,
       "raisecomRemoteSfpDdmCurrentAbnormal": raisecomRemoteSfpDdmCurrentAbnormal,
       "raisecomRemoteSfpDdmTxPowerNomal": raisecomRemoteSfpDdmTxPowerNomal,
       "raisecomRemoteSfpDdmTxPowerAbnormal": raisecomRemoteSfpDdmTxPowerAbnormal,
       "raisecomRemoteSfpDdmRxPowerNormal": raisecomRemoteSfpDdmRxPowerNormal,
       "raisecomRemoteSfpDdmRxPowerAbnormal": raisecomRemoteSfpDdmRxPowerAbnormal}
)
