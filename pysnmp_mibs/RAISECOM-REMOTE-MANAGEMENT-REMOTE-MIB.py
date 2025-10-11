# SNMP MIB module (RAISECOM-REMOTE-MANAGEMENT-REMOTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-REMOTE-MANAGEMENT-REMOTE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:03 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

(EntryStatus,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus")

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

(EnableVar,
 PortList) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList")


# MODULE-IDENTITY

raisecomRemoteManagementRemote = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomRemoteManagementRemoteHideMibObjects_ObjectIdentity = ObjectIdentity
raisecomRemoteManagementRemoteHideMibObjects = _RaisecomRemoteManagementRemoteHideMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1)
)


class _RaisecomRemoteTemperature_Type(Integer32):
    """Custom type raisecomRemoteTemperature based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteTemperature_Type.__name__ = "Integer32"
_RaisecomRemoteTemperature_Object = MibScalar
raisecomRemoteTemperature = _RaisecomRemoteTemperature_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 1),
    _RaisecomRemoteTemperature_Type()
)
raisecomRemoteTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteTemperature.setStatus("current")


class _RaisecomRemoteVolt3300_Type(Integer32):
    """Custom type raisecomRemoteVolt3300 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt3300_Type.__name__ = "Integer32"
_RaisecomRemoteVolt3300_Object = MibScalar
raisecomRemoteVolt3300 = _RaisecomRemoteVolt3300_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 2),
    _RaisecomRemoteVolt3300_Type()
)
raisecomRemoteVolt3300.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt3300.setStatus("current")


class _RaisecomRemoteVolt2500_Type(Integer32):
    """Custom type raisecomRemoteVolt2500 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt2500_Type.__name__ = "Integer32"
_RaisecomRemoteVolt2500_Object = MibScalar
raisecomRemoteVolt2500 = _RaisecomRemoteVolt2500_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 3),
    _RaisecomRemoteVolt2500_Type()
)
raisecomRemoteVolt2500.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt2500.setStatus("current")


class _RaisecomRemoteVolt1800_Type(Integer32):
    """Custom type raisecomRemoteVolt1800 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt1800_Type.__name__ = "Integer32"
_RaisecomRemoteVolt1800_Object = MibScalar
raisecomRemoteVolt1800 = _RaisecomRemoteVolt1800_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 4),
    _RaisecomRemoteVolt1800_Type()
)
raisecomRemoteVolt1800.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt1800.setStatus("current")


class _RaisecomRemoteVolt1200_Type(Integer32):
    """Custom type raisecomRemoteVolt1200 based on Integer32"""
    defaultValue = 65535


_RaisecomRemoteVolt1200_Type.__name__ = "Integer32"
_RaisecomRemoteVolt1200_Object = MibScalar
raisecomRemoteVolt1200 = _RaisecomRemoteVolt1200_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 5),
    _RaisecomRemoteVolt1200_Type()
)
raisecomRemoteVolt1200.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVolt1200.setStatus("current")


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
_RaisecomRemoteSysOperation_Object = MibScalar
raisecomRemoteSysOperation = _RaisecomRemoteSysOperation_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 6),
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
_RaisecomRemoteSysOperationState_Object = MibScalar
raisecomRemoteSysOperationState = _RaisecomRemoteSysOperationState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 7),
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
_RaisecomRemoteHostName_Object = MibScalar
raisecomRemoteHostName = _RaisecomRemoteHostName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 8),
    _RaisecomRemoteHostName_Type()
)
raisecomRemoteHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteHostName.setStatus("current")
_RaisecomRemoteOamNotificationEnable_Type = EnableVar
_RaisecomRemoteOamNotificationEnable_Object = MibScalar
raisecomRemoteOamNotificationEnable = _RaisecomRemoteOamNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 9),
    _RaisecomRemoteOamNotificationEnable_Type()
)
raisecomRemoteOamNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteOamNotificationEnable.setStatus("current")


class _RaisecomRemoteCommunityName_Type(OctetString):
    """Custom type raisecomRemoteCommunityName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_RaisecomRemoteCommunityName_Type.__name__ = "OctetString"
_RaisecomRemoteCommunityName_Object = MibScalar
raisecomRemoteCommunityName = _RaisecomRemoteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 10),
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
_RaisecomRemoteCommunityPermission_Object = MibScalar
raisecomRemoteCommunityPermission = _RaisecomRemoteCommunityPermission_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 11),
    _RaisecomRemoteCommunityPermission_Type()
)
raisecomRemoteCommunityPermission.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteCommunityPermission.setStatus("current")
_RaisecomRemoteL3IpAddr_Type = IpAddress
_RaisecomRemoteL3IpAddr_Object = MibScalar
raisecomRemoteL3IpAddr = _RaisecomRemoteL3IpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 12),
    _RaisecomRemoteL3IpAddr_Type()
)
raisecomRemoteL3IpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3IpAddr.setStatus("current")
_RaisecomRemoteL3Mask_Type = IpAddress
_RaisecomRemoteL3Mask_Object = MibScalar
raisecomRemoteL3Mask = _RaisecomRemoteL3Mask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 13),
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
_RaisecomRemoteL3VidIface_Object = MibScalar
raisecomRemoteL3VidIface = _RaisecomRemoteL3VidIface_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 14),
    _RaisecomRemoteL3VidIface_Type()
)
raisecomRemoteL3VidIface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3VidIface.setStatus("current")
_RaisecomRemoteL3VidMemberPorts_Type = PortList
_RaisecomRemoteL3VidMemberPorts_Object = MibScalar
raisecomRemoteL3VidMemberPorts = _RaisecomRemoteL3VidMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 15),
    _RaisecomRemoteL3VidMemberPorts_Type()
)
raisecomRemoteL3VidMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteL3VidMemberPorts.setStatus("current")
_RaisecomRemoteL3VidUntaggedPorts_Type = PortList
_RaisecomRemoteL3VidUntaggedPorts_Object = MibScalar
raisecomRemoteL3VidUntaggedPorts = _RaisecomRemoteL3VidUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 16),
    _RaisecomRemoteL3VidUntaggedPorts_Type()
)
raisecomRemoteL3VidUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteL3VidUntaggedPorts.setStatus("current")
_RaisecomRemoteL3DefaultGateway_Type = IpAddress
_RaisecomRemoteL3DefaultGateway_Object = MibScalar
raisecomRemoteL3DefaultGateway = _RaisecomRemoteL3DefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 17),
    _RaisecomRemoteL3DefaultGateway_Type()
)
raisecomRemoteL3DefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3DefaultGateway.setStatus("current")
_RaisecomRemotePortTable_Object = MibTable
raisecomRemotePortTable = _RaisecomRemotePortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18)
)
if mibBuilder.loadTexts:
    raisecomRemotePortTable.setStatus("current")
_RaisecomRemotePortEntry_Object = MibTableRow
raisecomRemotePortEntry = _RaisecomRemotePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1)
)
raisecomRemotePortEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-REMOTE-MIB", "raisecomRemotePortIfindex"),
)
if mibBuilder.loadTexts:
    raisecomRemotePortEntry.setStatus("current")
_RaisecomRemotePortIfindex_Type = Integer32
_RaisecomRemotePortIfindex_Object = MibTableColumn
raisecomRemotePortIfindex = _RaisecomRemotePortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 2),
    _RaisecomRemotePortIfindex_Type()
)
raisecomRemotePortIfindex.setMaxAccess("not-accessible")
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
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("inexistence", 0),
          ("fx-DulMode-1000M", 1),
          ("tx-1000M", 2),
          ("fx-SigMode-1000M", 3),
          ("fx-DulMode-100M", 4),
          ("fx-SigMode-100M", 5),
          ("tx-100M", 6))
    )


_RaisecomRemotePortType_Type.__name__ = "Integer32"
_RaisecomRemotePortType_Object = MibTableColumn
raisecomRemotePortType = _RaisecomRemotePortType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 8),
    _RaisecomRemotePortDuplexSpeedGet_Type()
)
raisecomRemotePortDuplexSpeedGet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortDuplexSpeedGet.setStatus("current")
_RaisecomRemotePortFlowControlEnable_Type = EnableVar
_RaisecomRemotePortFlowControlEnable_Object = MibTableColumn
raisecomRemotePortFlowControlEnable = _RaisecomRemotePortFlowControlEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 9),
    _RaisecomRemotePortFlowControlEnable_Type()
)
raisecomRemotePortFlowControlEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortFlowControlEnable.setStatus("current")
_RaisecomRemotePortFlowControlStatus_Type = EnableVar
_RaisecomRemotePortFlowControlStatus_Object = MibTableColumn
raisecomRemotePortFlowControlStatus = _RaisecomRemotePortFlowControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 12),
    _RaisecomRemotePortEgressRate_Type()
)
raisecomRemotePortEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortEgressRate.setStatus("current")
_RaisecomRemotePortFaultPassEnable_Type = EnableVar
_RaisecomRemotePortFaultPassEnable_Object = MibTableColumn
raisecomRemotePortFaultPassEnable = _RaisecomRemotePortFaultPassEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 13),
    _RaisecomRemotePortFaultPassEnable_Type()
)
raisecomRemotePortFaultPassEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortFaultPassEnable.setStatus("current")
_RaisecomRemotePortFaultPassPorts_Type = PortList
_RaisecomRemotePortFaultPassPorts_Object = MibTableColumn
raisecomRemotePortFaultPassPorts = _RaisecomRemotePortFaultPassPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 18, 1, 20),
    _RaisecomRemotePortDescr_Type()
)
raisecomRemotePortDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemotePortDescr.setStatus("current")
_RaisecomRemotePortStatsTable_Object = MibTable
raisecomRemotePortStatsTable = _RaisecomRemotePortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19)
)
if mibBuilder.loadTexts:
    raisecomRemotePortStatsTable.setStatus("current")
_RaisecomRemotePortStatsEntry_Object = MibTableRow
raisecomRemotePortStatsEntry = _RaisecomRemotePortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1)
)
raisecomRemotePortStatsEntry.setIndexNames(
    (0, "RAISECOM-REMOTE-MANAGEMENT-REMOTE-MIB", "raisecomRemoteStatsPortIfindex"),
)
if mibBuilder.loadTexts:
    raisecomRemotePortStatsEntry.setStatus("current")
_RaisecomRemoteStatsPortIfindex_Type = Integer32
_RaisecomRemoteStatsPortIfindex_Object = MibTableColumn
raisecomRemoteStatsPortIfindex = _RaisecomRemoteStatsPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 1),
    _RaisecomRemoteStatsPortIfindex_Type()
)
raisecomRemoteStatsPortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomRemoteStatsPortIfindex.setStatus("current")
_RaisecomRemotePortInOctets_Type = Counter64
_RaisecomRemotePortInOctets_Object = MibTableColumn
raisecomRemotePortInOctets = _RaisecomRemotePortInOctets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 2),
    _RaisecomRemotePortInOctets_Type()
)
raisecomRemotePortInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInOctets.setStatus("current")
_RaisecomRemotePortInPkts_Type = Counter64
_RaisecomRemotePortInPkts_Object = MibTableColumn
raisecomRemotePortInPkts = _RaisecomRemotePortInPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 3),
    _RaisecomRemotePortInPkts_Type()
)
raisecomRemotePortInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInPkts.setStatus("current")
_RaisecomRemotePortInUcastPkts_Type = Counter64
_RaisecomRemotePortInUcastPkts_Object = MibTableColumn
raisecomRemotePortInUcastPkts = _RaisecomRemotePortInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 4),
    _RaisecomRemotePortInUcastPkts_Type()
)
raisecomRemotePortInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInUcastPkts.setStatus("current")
_RaisecomRemotePortInMulticastPkts_Type = Counter64
_RaisecomRemotePortInMulticastPkts_Object = MibTableColumn
raisecomRemotePortInMulticastPkts = _RaisecomRemotePortInMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 5),
    _RaisecomRemotePortInMulticastPkts_Type()
)
raisecomRemotePortInMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInMulticastPkts.setStatus("current")
_RaisecomRemotePortInBroadcastPkts_Type = Counter64
_RaisecomRemotePortInBroadcastPkts_Object = MibTableColumn
raisecomRemotePortInBroadcastPkts = _RaisecomRemotePortInBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 6),
    _RaisecomRemotePortInBroadcastPkts_Type()
)
raisecomRemotePortInBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortInBroadcastPkts.setStatus("current")
_RaisecomRemotePortOutOctets_Type = Counter64
_RaisecomRemotePortOutOctets_Object = MibTableColumn
raisecomRemotePortOutOctets = _RaisecomRemotePortOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 7),
    _RaisecomRemotePortOutOctets_Type()
)
raisecomRemotePortOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutOctets.setStatus("current")
_RaisecomRemotePortOutPkts_Type = Counter64
_RaisecomRemotePortOutPkts_Object = MibTableColumn
raisecomRemotePortOutPkts = _RaisecomRemotePortOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 8),
    _RaisecomRemotePortOutPkts_Type()
)
raisecomRemotePortOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutPkts.setStatus("current")
_RaisecomRemotePortOutUcastPkts_Type = Counter64
_RaisecomRemotePortOutUcastPkts_Object = MibTableColumn
raisecomRemotePortOutUcastPkts = _RaisecomRemotePortOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 9),
    _RaisecomRemotePortOutUcastPkts_Type()
)
raisecomRemotePortOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutUcastPkts.setStatus("current")
_RaisecomRemotePortOutMulticastPkts_Type = Counter64
_RaisecomRemotePortOutMulticastPkts_Object = MibTableColumn
raisecomRemotePortOutMulticastPkts = _RaisecomRemotePortOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 10),
    _RaisecomRemotePortOutMulticastPkts_Type()
)
raisecomRemotePortOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutMulticastPkts.setStatus("current")
_RaisecomRemotePortOutBroadcastPkts_Type = Counter64
_RaisecomRemotePortOutBroadcastPkts_Object = MibTableColumn
raisecomRemotePortOutBroadcastPkts = _RaisecomRemotePortOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 11),
    _RaisecomRemotePortOutBroadcastPkts_Type()
)
raisecomRemotePortOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOutBroadcastPkts.setStatus("current")
_RaisecomRemotePortErrorPkts_Type = Counter32
_RaisecomRemotePortErrorPkts_Object = MibTableColumn
raisecomRemotePortErrorPkts = _RaisecomRemotePortErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 12),
    _RaisecomRemotePortErrorPkts_Type()
)
raisecomRemotePortErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortErrorPkts.setStatus("current")
_RaisecomRemotePortDropEvents_Type = Counter32
_RaisecomRemotePortDropEvents_Object = MibTableColumn
raisecomRemotePortDropEvents = _RaisecomRemotePortDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 13),
    _RaisecomRemotePortDropEvents_Type()
)
raisecomRemotePortDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortDropEvents.setStatus("current")
_RaisecomRemotePortCRCAlignErrors_Type = Counter32
_RaisecomRemotePortCRCAlignErrors_Object = MibTableColumn
raisecomRemotePortCRCAlignErrors = _RaisecomRemotePortCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 14),
    _RaisecomRemotePortCRCAlignErrors_Type()
)
raisecomRemotePortCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortCRCAlignErrors.setStatus("current")
_RaisecomRemotePortUndersizePkts_Type = Counter32
_RaisecomRemotePortUndersizePkts_Object = MibTableColumn
raisecomRemotePortUndersizePkts = _RaisecomRemotePortUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 15),
    _RaisecomRemotePortUndersizePkts_Type()
)
raisecomRemotePortUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortUndersizePkts.setStatus("current")
_RaisecomRemotePortOversizePkts_Type = Counter32
_RaisecomRemotePortOversizePkts_Object = MibTableColumn
raisecomRemotePortOversizePkts = _RaisecomRemotePortOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 16),
    _RaisecomRemotePortOversizePkts_Type()
)
raisecomRemotePortOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortOversizePkts.setStatus("current")
_RaisecomRemotePortFragments_Type = Counter32
_RaisecomRemotePortFragments_Object = MibTableColumn
raisecomRemotePortFragments = _RaisecomRemotePortFragments_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 17),
    _RaisecomRemotePortFragments_Type()
)
raisecomRemotePortFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortFragments.setStatus("current")
_RaisecomRemotePortJabbers_Type = Counter32
_RaisecomRemotePortJabbers_Object = MibTableColumn
raisecomRemotePortJabbers = _RaisecomRemotePortJabbers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 18),
    _RaisecomRemotePortJabbers_Type()
)
raisecomRemotePortJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortJabbers.setStatus("current")
_RaisecomRemotePortCollisions_Type = Counter32
_RaisecomRemotePortCollisions_Object = MibTableColumn
raisecomRemotePortCollisions = _RaisecomRemotePortCollisions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 19, 1, 19),
    _RaisecomRemotePortCollisions_Type()
)
raisecomRemotePortCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemotePortCollisions.setStatus("current")


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
_RaisecomRemoteVoltNormal_Object = MibScalar
raisecomRemoteVoltNormal = _RaisecomRemoteVoltNormal_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 20),
    _RaisecomRemoteVoltNormal_Type()
)
raisecomRemoteVoltNormal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomRemoteVoltNormal.setStatus("current")
_RaisecomRemoteMaxAllowedFrameLength_Type = Integer32
_RaisecomRemoteMaxAllowedFrameLength_Object = MibScalar
raisecomRemoteMaxAllowedFrameLength = _RaisecomRemoteMaxAllowedFrameLength_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 21),
    _RaisecomRemoteMaxAllowedFrameLength_Type()
)
raisecomRemoteMaxAllowedFrameLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteMaxAllowedFrameLength.setStatus("current")
_RaisecomRemoteL3ObPortIpAddr_Type = IpAddress
_RaisecomRemoteL3ObPortIpAddr_Object = MibScalar
raisecomRemoteL3ObPortIpAddr = _RaisecomRemoteL3ObPortIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 22),
    _RaisecomRemoteL3ObPortIpAddr_Type()
)
raisecomRemoteL3ObPortIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3ObPortIpAddr.setStatus("current")
_RaisecomRemoteL3ObPortMask_Type = IpAddress
_RaisecomRemoteL3ObPortMask_Object = MibScalar
raisecomRemoteL3ObPortMask = _RaisecomRemoteL3ObPortMask_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 13, 1, 23),
    _RaisecomRemoteL3ObPortMask_Type()
)
raisecomRemoteL3ObPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomRemoteL3ObPortMask.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-REMOTE-MANAGEMENT-REMOTE-MIB",
    **{"raisecomRemoteManagementRemote": raisecomRemoteManagementRemote,
       "raisecomRemoteManagementRemoteHideMibObjects": raisecomRemoteManagementRemoteHideMibObjects,
       "raisecomRemoteTemperature": raisecomRemoteTemperature,
       "raisecomRemoteVolt3300": raisecomRemoteVolt3300,
       "raisecomRemoteVolt2500": raisecomRemoteVolt2500,
       "raisecomRemoteVolt1800": raisecomRemoteVolt1800,
       "raisecomRemoteVolt1200": raisecomRemoteVolt1200,
       "raisecomRemoteSysOperation": raisecomRemoteSysOperation,
       "raisecomRemoteSysOperationState": raisecomRemoteSysOperationState,
       "raisecomRemoteHostName": raisecomRemoteHostName,
       "raisecomRemoteOamNotificationEnable": raisecomRemoteOamNotificationEnable,
       "raisecomRemoteCommunityName": raisecomRemoteCommunityName,
       "raisecomRemoteCommunityPermission": raisecomRemoteCommunityPermission,
       "raisecomRemoteL3IpAddr": raisecomRemoteL3IpAddr,
       "raisecomRemoteL3Mask": raisecomRemoteL3Mask,
       "raisecomRemoteL3VidIface": raisecomRemoteL3VidIface,
       "raisecomRemoteL3VidMemberPorts": raisecomRemoteL3VidMemberPorts,
       "raisecomRemoteL3VidUntaggedPorts": raisecomRemoteL3VidUntaggedPorts,
       "raisecomRemoteL3DefaultGateway": raisecomRemoteL3DefaultGateway,
       "raisecomRemotePortTable": raisecomRemotePortTable,
       "raisecomRemotePortEntry": raisecomRemotePortEntry,
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
       "raisecomRemoteVoltNormal": raisecomRemoteVoltNormal,
       "raisecomRemoteMaxAllowedFrameLength": raisecomRemoteMaxAllowedFrameLength,
       "raisecomRemoteL3ObPortIpAddr": raisecomRemoteL3ObPortIpAddr,
       "raisecomRemoteL3ObPortMask": raisecomRemoteL3ObPortMask}
)
