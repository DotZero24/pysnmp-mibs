# SNMP MIB module (ARICENT-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/ARICENT-DHCP-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:13 2025
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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

futureDhcpSrvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 84)
)
if mibBuilder.loadTexts:
    futureDhcpSrvMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhcpSrvConfig_ObjectIdentity = ObjectIdentity
dhcpSrvConfig = _DhcpSrvConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1)
)
_DhcpSrvEnable_Type = TruthValue
_DhcpSrvEnable_Object = MibScalar
dhcpSrvEnable = _DhcpSrvEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 1),
    _DhcpSrvEnable_Type()
)
dhcpSrvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvEnable.setStatus("current")


class _DhcpSrvDebugLevel_Type(Integer32):
    """Custom type dhcpSrvDebugLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DhcpSrvDebugLevel_Type.__name__ = "Integer32"
_DhcpSrvDebugLevel_Object = MibScalar
dhcpSrvDebugLevel = _DhcpSrvDebugLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 2),
    _DhcpSrvDebugLevel_Type()
)
dhcpSrvDebugLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvDebugLevel.setStatus("current")


class _DhcpSrvOfferReuseTimeOut_Type(TimeTicks):
    """Custom type dhcpSrvOfferReuseTimeOut based on TimeTicks"""
    defaultValue = 5


_DhcpSrvOfferReuseTimeOut_Type.__name__ = "TimeTicks"
_DhcpSrvOfferReuseTimeOut_Object = MibScalar
dhcpSrvOfferReuseTimeOut = _DhcpSrvOfferReuseTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 3),
    _DhcpSrvOfferReuseTimeOut_Type()
)
dhcpSrvOfferReuseTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvOfferReuseTimeOut.setStatus("current")


class _DhcpSrvIcmpEchoEnable_Type(TruthValue):
    """Custom type dhcpSrvIcmpEchoEnable based on TruthValue"""
    defaultValue = 2


_DhcpSrvIcmpEchoEnable_Type.__name__ = "TruthValue"
_DhcpSrvIcmpEchoEnable_Object = MibScalar
dhcpSrvIcmpEchoEnable = _DhcpSrvIcmpEchoEnable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 4),
    _DhcpSrvIcmpEchoEnable_Type()
)
dhcpSrvIcmpEchoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvIcmpEchoEnable.setStatus("current")
_DhcpSrvBootServerAddress_Type = IpAddress
_DhcpSrvBootServerAddress_Object = MibScalar
dhcpSrvBootServerAddress = _DhcpSrvBootServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 5),
    _DhcpSrvBootServerAddress_Type()
)
dhcpSrvBootServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvBootServerAddress.setStatus("current")


class _DhcpSrvDefBootFilename_Type(OctetString):
    """Custom type dhcpSrvDefBootFilename based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpSrvDefBootFilename_Type.__name__ = "OctetString"
_DhcpSrvDefBootFilename_Object = MibScalar
dhcpSrvDefBootFilename = _DhcpSrvDefBootFilename_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 6),
    _DhcpSrvDefBootFilename_Type()
)
dhcpSrvDefBootFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvDefBootFilename.setStatus("current")


class _DhcpSrvBootpClientsSupported_Type(TruthValue):
    """Custom type dhcpSrvBootpClientsSupported based on TruthValue"""
    defaultValue = 1


_DhcpSrvBootpClientsSupported_Type.__name__ = "TruthValue"
_DhcpSrvBootpClientsSupported_Object = MibScalar
dhcpSrvBootpClientsSupported = _DhcpSrvBootpClientsSupported_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 7),
    _DhcpSrvBootpClientsSupported_Type()
)
dhcpSrvBootpClientsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvBootpClientsSupported.setStatus("current")


class _DhcpSrvAutomaticBootpEnabled_Type(TruthValue):
    """Custom type dhcpSrvAutomaticBootpEnabled based on TruthValue"""
    defaultValue = 1


_DhcpSrvAutomaticBootpEnabled_Type.__name__ = "TruthValue"
_DhcpSrvAutomaticBootpEnabled_Object = MibScalar
dhcpSrvAutomaticBootpEnabled = _DhcpSrvAutomaticBootpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 8),
    _DhcpSrvAutomaticBootpEnabled_Type()
)
dhcpSrvAutomaticBootpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvAutomaticBootpEnabled.setStatus("current")
_DhcpSrvSubnetPoolConfigTable_Object = MibTable
dhcpSrvSubnetPoolConfigTable = _DhcpSrvSubnetPoolConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9)
)
if mibBuilder.loadTexts:
    dhcpSrvSubnetPoolConfigTable.setStatus("current")
_DhcpSrvSubnetPoolConfigEntry_Object = MibTableRow
dhcpSrvSubnetPoolConfigEntry = _DhcpSrvSubnetPoolConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1)
)
dhcpSrvSubnetPoolConfigEntry.setIndexNames(
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetPoolIndex"),
)
if mibBuilder.loadTexts:
    dhcpSrvSubnetPoolConfigEntry.setStatus("current")


class _DhcpSrvSubnetPoolIndex_Type(Integer32):
    """Custom type dhcpSrvSubnetPoolIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpSrvSubnetPoolIndex_Type.__name__ = "Integer32"
_DhcpSrvSubnetPoolIndex_Object = MibTableColumn
dhcpSrvSubnetPoolIndex = _DhcpSrvSubnetPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 1),
    _DhcpSrvSubnetPoolIndex_Type()
)
dhcpSrvSubnetPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvSubnetPoolIndex.setStatus("current")
_DhcpSrvSubnetSubnet_Type = IpAddress
_DhcpSrvSubnetSubnet_Object = MibTableColumn
dhcpSrvSubnetSubnet = _DhcpSrvSubnetSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 2),
    _DhcpSrvSubnetSubnet_Type()
)
dhcpSrvSubnetSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetSubnet.setStatus("current")
_DhcpSrvSubnetPortNumber_Type = Integer32
_DhcpSrvSubnetPortNumber_Object = MibTableColumn
dhcpSrvSubnetPortNumber = _DhcpSrvSubnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 3),
    _DhcpSrvSubnetPortNumber_Type()
)
dhcpSrvSubnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetPortNumber.setStatus("current")
_DhcpSrvSubnetMask_Type = IpAddress
_DhcpSrvSubnetMask_Object = MibTableColumn
dhcpSrvSubnetMask = _DhcpSrvSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 4),
    _DhcpSrvSubnetMask_Type()
)
dhcpSrvSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetMask.setStatus("current")
_DhcpSrvSubnetStartIpAddress_Type = IpAddress
_DhcpSrvSubnetStartIpAddress_Object = MibTableColumn
dhcpSrvSubnetStartIpAddress = _DhcpSrvSubnetStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 5),
    _DhcpSrvSubnetStartIpAddress_Type()
)
dhcpSrvSubnetStartIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetStartIpAddress.setStatus("current")
_DhcpSrvSubnetEndIpAddress_Type = IpAddress
_DhcpSrvSubnetEndIpAddress_Object = MibTableColumn
dhcpSrvSubnetEndIpAddress = _DhcpSrvSubnetEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 6),
    _DhcpSrvSubnetEndIpAddress_Type()
)
dhcpSrvSubnetEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetEndIpAddress.setStatus("current")
_DhcpSrvSubnetLeaseTime_Type = Integer32
_DhcpSrvSubnetLeaseTime_Object = MibTableColumn
dhcpSrvSubnetLeaseTime = _DhcpSrvSubnetLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 7),
    _DhcpSrvSubnetLeaseTime_Type()
)
dhcpSrvSubnetLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetLeaseTime.setStatus("current")


class _DhcpSrvSubnetPoolName_Type(DisplayString):
    """Custom type dhcpSrvSubnetPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpSrvSubnetPoolName_Type.__name__ = "DisplayString"
_DhcpSrvSubnetPoolName_Object = MibTableColumn
dhcpSrvSubnetPoolName = _DhcpSrvSubnetPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 8),
    _DhcpSrvSubnetPoolName_Type()
)
dhcpSrvSubnetPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetPoolName.setStatus("current")


class _DhcpSrvSubnetUtlThreshold_Type(Integer32):
    """Custom type dhcpSrvSubnetUtlThreshold based on Integer32"""
    defaultValue = 75

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_DhcpSrvSubnetUtlThreshold_Type.__name__ = "Integer32"
_DhcpSrvSubnetUtlThreshold_Object = MibTableColumn
dhcpSrvSubnetUtlThreshold = _DhcpSrvSubnetUtlThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 9),
    _DhcpSrvSubnetUtlThreshold_Type()
)
dhcpSrvSubnetUtlThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetUtlThreshold.setStatus("current")
_DhcpSrvSubnetPoolRowStatus_Type = RowStatus
_DhcpSrvSubnetPoolRowStatus_Object = MibTableColumn
dhcpSrvSubnetPoolRowStatus = _DhcpSrvSubnetPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 9, 1, 10),
    _DhcpSrvSubnetPoolRowStatus_Type()
)
dhcpSrvSubnetPoolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetPoolRowStatus.setStatus("current")
_DhcpSrvExcludeIpAddressTable_Object = MibTable
dhcpSrvExcludeIpAddressTable = _DhcpSrvExcludeIpAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 10)
)
if mibBuilder.loadTexts:
    dhcpSrvExcludeIpAddressTable.setStatus("current")
_DhcpSrvExcludeIpAddressEntry_Object = MibTableRow
dhcpSrvExcludeIpAddressEntry = _DhcpSrvExcludeIpAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 10, 1)
)
dhcpSrvExcludeIpAddressEntry.setIndexNames(
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetPoolIndex"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvExcludeStartIpAddress"),
)
if mibBuilder.loadTexts:
    dhcpSrvExcludeIpAddressEntry.setStatus("current")
_DhcpSrvExcludeStartIpAddress_Type = IpAddress
_DhcpSrvExcludeStartIpAddress_Object = MibTableColumn
dhcpSrvExcludeStartIpAddress = _DhcpSrvExcludeStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 10, 1, 1),
    _DhcpSrvExcludeStartIpAddress_Type()
)
dhcpSrvExcludeStartIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvExcludeStartIpAddress.setStatus("current")
_DhcpSrvExcludeEndIpAddress_Type = IpAddress
_DhcpSrvExcludeEndIpAddress_Object = MibTableColumn
dhcpSrvExcludeEndIpAddress = _DhcpSrvExcludeEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 10, 1, 2),
    _DhcpSrvExcludeEndIpAddress_Type()
)
dhcpSrvExcludeEndIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvExcludeEndIpAddress.setStatus("current")
_DhcpSrvExcludeAddressRowStatus_Type = RowStatus
_DhcpSrvExcludeAddressRowStatus_Object = MibTableColumn
dhcpSrvExcludeAddressRowStatus = _DhcpSrvExcludeAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 10, 1, 3),
    _DhcpSrvExcludeAddressRowStatus_Type()
)
dhcpSrvExcludeAddressRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvExcludeAddressRowStatus.setStatus("current")
_DhcpSrvGblOptTable_Object = MibTable
dhcpSrvGblOptTable = _DhcpSrvGblOptTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 11)
)
if mibBuilder.loadTexts:
    dhcpSrvGblOptTable.setStatus("current")
_DhcpSrvGblOptEntry_Object = MibTableRow
dhcpSrvGblOptEntry = _DhcpSrvGblOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 11, 1)
)
dhcpSrvGblOptEntry.setIndexNames(
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvGblOptType"),
)
if mibBuilder.loadTexts:
    dhcpSrvGblOptEntry.setStatus("current")


class _DhcpSrvGblOptType_Type(Integer32):
    """Custom type dhcpSrvGblOptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpSrvGblOptType_Type.__name__ = "Integer32"
_DhcpSrvGblOptType_Object = MibTableColumn
dhcpSrvGblOptType = _DhcpSrvGblOptType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 11, 1, 1),
    _DhcpSrvGblOptType_Type()
)
dhcpSrvGblOptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvGblOptType.setStatus("current")
_DhcpSrvGblOptLen_Type = Integer32
_DhcpSrvGblOptLen_Object = MibTableColumn
dhcpSrvGblOptLen = _DhcpSrvGblOptLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 11, 1, 2),
    _DhcpSrvGblOptLen_Type()
)
dhcpSrvGblOptLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvGblOptLen.setStatus("current")
_DhcpSrvGblOptVal_Type = OctetString
_DhcpSrvGblOptVal_Object = MibTableColumn
dhcpSrvGblOptVal = _DhcpSrvGblOptVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 11, 1, 3),
    _DhcpSrvGblOptVal_Type()
)
dhcpSrvGblOptVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvGblOptVal.setStatus("current")
_DhcpSrvGblOptRowStatus_Type = RowStatus
_DhcpSrvGblOptRowStatus_Object = MibTableColumn
dhcpSrvGblOptRowStatus = _DhcpSrvGblOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 11, 1, 4),
    _DhcpSrvGblOptRowStatus_Type()
)
dhcpSrvGblOptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvGblOptRowStatus.setStatus("current")
_DhcpSrvSubnetOptTable_Object = MibTable
dhcpSrvSubnetOptTable = _DhcpSrvSubnetOptTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 12)
)
if mibBuilder.loadTexts:
    dhcpSrvSubnetOptTable.setStatus("current")
_DhcpSrvSubnetOptEntry_Object = MibTableRow
dhcpSrvSubnetOptEntry = _DhcpSrvSubnetOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 12, 1)
)
dhcpSrvSubnetOptEntry.setIndexNames(
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetPoolIndex"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetOptType"),
)
if mibBuilder.loadTexts:
    dhcpSrvSubnetOptEntry.setStatus("current")


class _DhcpSrvSubnetOptType_Type(Integer32):
    """Custom type dhcpSrvSubnetOptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpSrvSubnetOptType_Type.__name__ = "Integer32"
_DhcpSrvSubnetOptType_Object = MibTableColumn
dhcpSrvSubnetOptType = _DhcpSrvSubnetOptType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 12, 1, 1),
    _DhcpSrvSubnetOptType_Type()
)
dhcpSrvSubnetOptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvSubnetOptType.setStatus("current")
_DhcpSrvSubnetOptLen_Type = Integer32
_DhcpSrvSubnetOptLen_Object = MibTableColumn
dhcpSrvSubnetOptLen = _DhcpSrvSubnetOptLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 12, 1, 2),
    _DhcpSrvSubnetOptLen_Type()
)
dhcpSrvSubnetOptLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetOptLen.setStatus("current")
_DhcpSrvSubnetOptVal_Type = OctetString
_DhcpSrvSubnetOptVal_Object = MibTableColumn
dhcpSrvSubnetOptVal = _DhcpSrvSubnetOptVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 12, 1, 3),
    _DhcpSrvSubnetOptVal_Type()
)
dhcpSrvSubnetOptVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetOptVal.setStatus("current")
_DhcpSrvSubnetOptRowStatus_Type = RowStatus
_DhcpSrvSubnetOptRowStatus_Object = MibTableColumn
dhcpSrvSubnetOptRowStatus = _DhcpSrvSubnetOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 12, 1, 4),
    _DhcpSrvSubnetOptRowStatus_Type()
)
dhcpSrvSubnetOptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvSubnetOptRowStatus.setStatus("current")
_DhcpSrvHostOptTable_Object = MibTable
dhcpSrvHostOptTable = _DhcpSrvHostOptTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13)
)
if mibBuilder.loadTexts:
    dhcpSrvHostOptTable.setStatus("current")
_DhcpSrvHostOptEntry_Object = MibTableRow
dhcpSrvHostOptEntry = _DhcpSrvHostOptEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13, 1)
)
dhcpSrvHostOptEntry.setIndexNames(
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvHostType"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvHostId"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetPoolIndex"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvHostOptType"),
)
if mibBuilder.loadTexts:
    dhcpSrvHostOptEntry.setStatus("current")


class _DhcpSrvHostType_Type(Integer32):
    """Custom type dhcpSrvHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpSrvHostType_Type.__name__ = "Integer32"
_DhcpSrvHostType_Object = MibTableColumn
dhcpSrvHostType = _DhcpSrvHostType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13, 1, 1),
    _DhcpSrvHostType_Type()
)
dhcpSrvHostType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvHostType.setStatus("current")


class _DhcpSrvHostId_Type(OctetString):
    """Custom type dhcpSrvHostId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpSrvHostId_Type.__name__ = "OctetString"
_DhcpSrvHostId_Object = MibTableColumn
dhcpSrvHostId = _DhcpSrvHostId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13, 1, 2),
    _DhcpSrvHostId_Type()
)
dhcpSrvHostId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvHostId.setStatus("current")


class _DhcpSrvHostOptType_Type(Integer32):
    """Custom type dhcpSrvHostOptType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DhcpSrvHostOptType_Type.__name__ = "Integer32"
_DhcpSrvHostOptType_Object = MibTableColumn
dhcpSrvHostOptType = _DhcpSrvHostOptType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13, 1, 3),
    _DhcpSrvHostOptType_Type()
)
dhcpSrvHostOptType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvHostOptType.setStatus("current")
_DhcpSrvHostOptLen_Type = Integer32
_DhcpSrvHostOptLen_Object = MibTableColumn
dhcpSrvHostOptLen = _DhcpSrvHostOptLen_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13, 1, 4),
    _DhcpSrvHostOptLen_Type()
)
dhcpSrvHostOptLen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostOptLen.setStatus("current")
_DhcpSrvHostOptVal_Type = OctetString
_DhcpSrvHostOptVal_Object = MibTableColumn
dhcpSrvHostOptVal = _DhcpSrvHostOptVal_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13, 1, 5),
    _DhcpSrvHostOptVal_Type()
)
dhcpSrvHostOptVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostOptVal.setStatus("current")
_DhcpSrvHostOptRowStatus_Type = RowStatus
_DhcpSrvHostOptRowStatus_Object = MibTableColumn
dhcpSrvHostOptRowStatus = _DhcpSrvHostOptRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 13, 1, 6),
    _DhcpSrvHostOptRowStatus_Type()
)
dhcpSrvHostOptRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostOptRowStatus.setStatus("current")
_DhcpSrvHostConfigTable_Object = MibTable
dhcpSrvHostConfigTable = _DhcpSrvHostConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 14)
)
if mibBuilder.loadTexts:
    dhcpSrvHostConfigTable.setStatus("current")
_DhcpSrvHostConfigEntry_Object = MibTableRow
dhcpSrvHostConfigEntry = _DhcpSrvHostConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 14, 1)
)
dhcpSrvHostConfigEntry.setIndexNames(
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvHostType"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvHostId"),
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetPoolIndex"),
)
if mibBuilder.loadTexts:
    dhcpSrvHostConfigEntry.setStatus("current")
_DhcpSrvHostIpAddress_Type = IpAddress
_DhcpSrvHostIpAddress_Object = MibTableColumn
dhcpSrvHostIpAddress = _DhcpSrvHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 14, 1, 1),
    _DhcpSrvHostIpAddress_Type()
)
dhcpSrvHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostIpAddress.setStatus("current")
_DhcpSrvHostPoolName_Type = Integer32
_DhcpSrvHostPoolName_Object = MibTableColumn
dhcpSrvHostPoolName = _DhcpSrvHostPoolName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 14, 1, 2),
    _DhcpSrvHostPoolName_Type()
)
dhcpSrvHostPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostPoolName.setStatus("current")


class _DhcpSrvHostBootFileName_Type(DisplayString):
    """Custom type dhcpSrvHostBootFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DhcpSrvHostBootFileName_Type.__name__ = "DisplayString"
_DhcpSrvHostBootFileName_Object = MibTableColumn
dhcpSrvHostBootFileName = _DhcpSrvHostBootFileName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 14, 1, 3),
    _DhcpSrvHostBootFileName_Type()
)
dhcpSrvHostBootFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostBootFileName.setStatus("current")
_DhcpSrvHostBootServerAddress_Type = IpAddress
_DhcpSrvHostBootServerAddress_Object = MibTableColumn
dhcpSrvHostBootServerAddress = _DhcpSrvHostBootServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 14, 1, 4),
    _DhcpSrvHostBootServerAddress_Type()
)
dhcpSrvHostBootServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostBootServerAddress.setStatus("current")
_DhcpSrvHostConfigRowStatus_Type = RowStatus
_DhcpSrvHostConfigRowStatus_Object = MibTableColumn
dhcpSrvHostConfigRowStatus = _DhcpSrvHostConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 1, 14, 1, 5),
    _DhcpSrvHostConfigRowStatus_Type()
)
dhcpSrvHostConfigRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvHostConfigRowStatus.setStatus("current")
_DhcpSrvBinding_ObjectIdentity = ObjectIdentity
dhcpSrvBinding = _DhcpSrvBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2)
)
_DhcpSrvBindingTable_Object = MibTable
dhcpSrvBindingTable = _DhcpSrvBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSrvBindingTable.setStatus("current")
_DhcpSrvBindingEntry_Object = MibTableRow
dhcpSrvBindingEntry = _DhcpSrvBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1)
)
dhcpSrvBindingEntry.setIndexNames(
    (0, "ARICENT-DHCP-SERVER-MIB", "dhcpSrvBindIpAddress"),
)
if mibBuilder.loadTexts:
    dhcpSrvBindingEntry.setStatus("current")
_DhcpSrvBindIpAddress_Type = IpAddress
_DhcpSrvBindIpAddress_Object = MibTableColumn
dhcpSrvBindIpAddress = _DhcpSrvBindIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 1),
    _DhcpSrvBindIpAddress_Type()
)
dhcpSrvBindIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSrvBindIpAddress.setStatus("current")


class _DhcpSrvBindHwType_Type(Integer32):
    """Custom type dhcpSrvBindHwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clientid", 0),
          ("ethernet", 1))
    )


_DhcpSrvBindHwType_Type.__name__ = "Integer32"
_DhcpSrvBindHwType_Object = MibTableColumn
dhcpSrvBindHwType = _DhcpSrvBindHwType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 2),
    _DhcpSrvBindHwType_Type()
)
dhcpSrvBindHwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSrvBindHwType.setStatus("current")
_DhcpSrvBindHwAddress_Type = OctetString
_DhcpSrvBindHwAddress_Object = MibTableColumn
dhcpSrvBindHwAddress = _DhcpSrvBindHwAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 3),
    _DhcpSrvBindHwAddress_Type()
)
dhcpSrvBindHwAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSrvBindHwAddress.setStatus("current")
_DhcpSrvBindExpireTime_Type = Integer32
_DhcpSrvBindExpireTime_Object = MibTableColumn
dhcpSrvBindExpireTime = _DhcpSrvBindExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 4),
    _DhcpSrvBindExpireTime_Type()
)
dhcpSrvBindExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSrvBindExpireTime.setStatus("current")


class _DhcpSrvBindAllocMethod_Type(Integer32):
    """Custom type dhcpSrvBindAllocMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("manual", 2))
    )


_DhcpSrvBindAllocMethod_Type.__name__ = "Integer32"
_DhcpSrvBindAllocMethod_Object = MibTableColumn
dhcpSrvBindAllocMethod = _DhcpSrvBindAllocMethod_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 5),
    _DhcpSrvBindAllocMethod_Type()
)
dhcpSrvBindAllocMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSrvBindAllocMethod.setStatus("current")


class _DhcpSrvBindState_Type(Integer32):
    """Custom type dhcpSrvBindState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("offered", 1),
          ("assigned", 2),
          ("probing", 5))
    )


_DhcpSrvBindState_Type.__name__ = "Integer32"
_DhcpSrvBindState_Object = MibTableColumn
dhcpSrvBindState = _DhcpSrvBindState_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 6),
    _DhcpSrvBindState_Type()
)
dhcpSrvBindState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSrvBindState.setStatus("current")
_DhcpSrvBindXid_Type = Unsigned32
_DhcpSrvBindXid_Object = MibTableColumn
dhcpSrvBindXid = _DhcpSrvBindXid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 7),
    _DhcpSrvBindXid_Type()
)
dhcpSrvBindXid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSrvBindXid.setStatus("current")
_DhcpSrvBindEntryStatus_Type = RowStatus
_DhcpSrvBindEntryStatus_Object = MibTableColumn
dhcpSrvBindEntryStatus = _DhcpSrvBindEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 2, 1, 1, 8),
    _DhcpSrvBindEntryStatus_Type()
)
dhcpSrvBindEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSrvBindEntryStatus.setStatus("current")
_DhcpSrvCounters_ObjectIdentity = ObjectIdentity
dhcpSrvCounters = _DhcpSrvCounters_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3)
)
_DhcpCountDiscovers_Type = Counter32
_DhcpCountDiscovers_Object = MibScalar
dhcpCountDiscovers = _DhcpCountDiscovers_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 1),
    _DhcpCountDiscovers_Type()
)
dhcpCountDiscovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDiscovers.setStatus("current")
_DhcpCountRequests_Type = Counter32
_DhcpCountRequests_Object = MibScalar
dhcpCountRequests = _DhcpCountRequests_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 2),
    _DhcpCountRequests_Type()
)
dhcpCountRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountRequests.setStatus("current")
_DhcpCountReleases_Type = Counter32
_DhcpCountReleases_Object = MibScalar
dhcpCountReleases = _DhcpCountReleases_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 3),
    _DhcpCountReleases_Type()
)
dhcpCountReleases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountReleases.setStatus("current")
_DhcpCountDeclines_Type = Counter32
_DhcpCountDeclines_Object = MibScalar
dhcpCountDeclines = _DhcpCountDeclines_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 4),
    _DhcpCountDeclines_Type()
)
dhcpCountDeclines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDeclines.setStatus("current")
_DhcpCountInforms_Type = Counter32
_DhcpCountInforms_Object = MibScalar
dhcpCountInforms = _DhcpCountInforms_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 5),
    _DhcpCountInforms_Type()
)
dhcpCountInforms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountInforms.setStatus("current")
_DhcpCountInvalids_Type = Counter32
_DhcpCountInvalids_Object = MibScalar
dhcpCountInvalids = _DhcpCountInvalids_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 6),
    _DhcpCountInvalids_Type()
)
dhcpCountInvalids.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountInvalids.setStatus("current")
_DhcpCountOffers_Type = Counter32
_DhcpCountOffers_Object = MibScalar
dhcpCountOffers = _DhcpCountOffers_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 7),
    _DhcpCountOffers_Type()
)
dhcpCountOffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountOffers.setStatus("current")
_DhcpCountAcks_Type = Counter32
_DhcpCountAcks_Object = MibScalar
dhcpCountAcks = _DhcpCountAcks_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 8),
    _DhcpCountAcks_Type()
)
dhcpCountAcks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountAcks.setStatus("current")
_DhcpCountNacks_Type = Counter32
_DhcpCountNacks_Object = MibScalar
dhcpCountNacks = _DhcpCountNacks_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 9),
    _DhcpCountNacks_Type()
)
dhcpCountNacks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountNacks.setStatus("current")
_DhcpCountDroppedUnknownClient_Type = Counter32
_DhcpCountDroppedUnknownClient_Object = MibScalar
dhcpCountDroppedUnknownClient = _DhcpCountDroppedUnknownClient_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 10),
    _DhcpCountDroppedUnknownClient_Type()
)
dhcpCountDroppedUnknownClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDroppedUnknownClient.setStatus("current")
_DhcpCountDroppedNotServingSubnet_Type = Counter32
_DhcpCountDroppedNotServingSubnet_Object = MibScalar
dhcpCountDroppedNotServingSubnet = _DhcpCountDroppedNotServingSubnet_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 11),
    _DhcpCountDroppedNotServingSubnet_Type()
)
dhcpCountDroppedNotServingSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpCountDroppedNotServingSubnet.setStatus("current")


class _DhcpCountResetCounters_Type(Integer32):
    """Custom type dhcpCountResetCounters based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("set", 1),
          ("notset", 2))
    )


_DhcpCountResetCounters_Type.__name__ = "Integer32"
_DhcpCountResetCounters_Object = MibScalar
dhcpCountResetCounters = _DhcpCountResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 2076, 84, 3, 12),
    _DhcpCountResetCounters_Type()
)
dhcpCountResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpCountResetCounters.setStatus("current")
_DhcpSrvTrapGroup_ObjectIdentity = ObjectIdentity
dhcpSrvTrapGroup = _DhcpSrvTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 84, 4)
)
_DhcpSrvTraps_ObjectIdentity = ObjectIdentity
dhcpSrvTraps = _DhcpSrvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 84, 4, 0)
)

# Managed Objects groups


# Notification objects

dhcpSrvPoolUtlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 84, 4, 0, 1)
)
dhcpSrvPoolUtlTrap.setObjects(
    ("ARICENT-DHCP-SERVER-MIB", "dhcpSrvSubnetUtlThreshold")
)
if mibBuilder.loadTexts:
    dhcpSrvPoolUtlTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-DHCP-SERVER-MIB",
    **{"futureDhcpSrvMIB": futureDhcpSrvMIB,
       "dhcpSrvConfig": dhcpSrvConfig,
       "dhcpSrvEnable": dhcpSrvEnable,
       "dhcpSrvDebugLevel": dhcpSrvDebugLevel,
       "dhcpSrvOfferReuseTimeOut": dhcpSrvOfferReuseTimeOut,
       "dhcpSrvIcmpEchoEnable": dhcpSrvIcmpEchoEnable,
       "dhcpSrvBootServerAddress": dhcpSrvBootServerAddress,
       "dhcpSrvDefBootFilename": dhcpSrvDefBootFilename,
       "dhcpSrvBootpClientsSupported": dhcpSrvBootpClientsSupported,
       "dhcpSrvAutomaticBootpEnabled": dhcpSrvAutomaticBootpEnabled,
       "dhcpSrvSubnetPoolConfigTable": dhcpSrvSubnetPoolConfigTable,
       "dhcpSrvSubnetPoolConfigEntry": dhcpSrvSubnetPoolConfigEntry,
       "dhcpSrvSubnetPoolIndex": dhcpSrvSubnetPoolIndex,
       "dhcpSrvSubnetSubnet": dhcpSrvSubnetSubnet,
       "dhcpSrvSubnetPortNumber": dhcpSrvSubnetPortNumber,
       "dhcpSrvSubnetMask": dhcpSrvSubnetMask,
       "dhcpSrvSubnetStartIpAddress": dhcpSrvSubnetStartIpAddress,
       "dhcpSrvSubnetEndIpAddress": dhcpSrvSubnetEndIpAddress,
       "dhcpSrvSubnetLeaseTime": dhcpSrvSubnetLeaseTime,
       "dhcpSrvSubnetPoolName": dhcpSrvSubnetPoolName,
       "dhcpSrvSubnetUtlThreshold": dhcpSrvSubnetUtlThreshold,
       "dhcpSrvSubnetPoolRowStatus": dhcpSrvSubnetPoolRowStatus,
       "dhcpSrvExcludeIpAddressTable": dhcpSrvExcludeIpAddressTable,
       "dhcpSrvExcludeIpAddressEntry": dhcpSrvExcludeIpAddressEntry,
       "dhcpSrvExcludeStartIpAddress": dhcpSrvExcludeStartIpAddress,
       "dhcpSrvExcludeEndIpAddress": dhcpSrvExcludeEndIpAddress,
       "dhcpSrvExcludeAddressRowStatus": dhcpSrvExcludeAddressRowStatus,
       "dhcpSrvGblOptTable": dhcpSrvGblOptTable,
       "dhcpSrvGblOptEntry": dhcpSrvGblOptEntry,
       "dhcpSrvGblOptType": dhcpSrvGblOptType,
       "dhcpSrvGblOptLen": dhcpSrvGblOptLen,
       "dhcpSrvGblOptVal": dhcpSrvGblOptVal,
       "dhcpSrvGblOptRowStatus": dhcpSrvGblOptRowStatus,
       "dhcpSrvSubnetOptTable": dhcpSrvSubnetOptTable,
       "dhcpSrvSubnetOptEntry": dhcpSrvSubnetOptEntry,
       "dhcpSrvSubnetOptType": dhcpSrvSubnetOptType,
       "dhcpSrvSubnetOptLen": dhcpSrvSubnetOptLen,
       "dhcpSrvSubnetOptVal": dhcpSrvSubnetOptVal,
       "dhcpSrvSubnetOptRowStatus": dhcpSrvSubnetOptRowStatus,
       "dhcpSrvHostOptTable": dhcpSrvHostOptTable,
       "dhcpSrvHostOptEntry": dhcpSrvHostOptEntry,
       "dhcpSrvHostType": dhcpSrvHostType,
       "dhcpSrvHostId": dhcpSrvHostId,
       "dhcpSrvHostOptType": dhcpSrvHostOptType,
       "dhcpSrvHostOptLen": dhcpSrvHostOptLen,
       "dhcpSrvHostOptVal": dhcpSrvHostOptVal,
       "dhcpSrvHostOptRowStatus": dhcpSrvHostOptRowStatus,
       "dhcpSrvHostConfigTable": dhcpSrvHostConfigTable,
       "dhcpSrvHostConfigEntry": dhcpSrvHostConfigEntry,
       "dhcpSrvHostIpAddress": dhcpSrvHostIpAddress,
       "dhcpSrvHostPoolName": dhcpSrvHostPoolName,
       "dhcpSrvHostBootFileName": dhcpSrvHostBootFileName,
       "dhcpSrvHostBootServerAddress": dhcpSrvHostBootServerAddress,
       "dhcpSrvHostConfigRowStatus": dhcpSrvHostConfigRowStatus,
       "dhcpSrvBinding": dhcpSrvBinding,
       "dhcpSrvBindingTable": dhcpSrvBindingTable,
       "dhcpSrvBindingEntry": dhcpSrvBindingEntry,
       "dhcpSrvBindIpAddress": dhcpSrvBindIpAddress,
       "dhcpSrvBindHwType": dhcpSrvBindHwType,
       "dhcpSrvBindHwAddress": dhcpSrvBindHwAddress,
       "dhcpSrvBindExpireTime": dhcpSrvBindExpireTime,
       "dhcpSrvBindAllocMethod": dhcpSrvBindAllocMethod,
       "dhcpSrvBindState": dhcpSrvBindState,
       "dhcpSrvBindXid": dhcpSrvBindXid,
       "dhcpSrvBindEntryStatus": dhcpSrvBindEntryStatus,
       "dhcpSrvCounters": dhcpSrvCounters,
       "dhcpCountDiscovers": dhcpCountDiscovers,
       "dhcpCountRequests": dhcpCountRequests,
       "dhcpCountReleases": dhcpCountReleases,
       "dhcpCountDeclines": dhcpCountDeclines,
       "dhcpCountInforms": dhcpCountInforms,
       "dhcpCountInvalids": dhcpCountInvalids,
       "dhcpCountOffers": dhcpCountOffers,
       "dhcpCountAcks": dhcpCountAcks,
       "dhcpCountNacks": dhcpCountNacks,
       "dhcpCountDroppedUnknownClient": dhcpCountDroppedUnknownClient,
       "dhcpCountDroppedNotServingSubnet": dhcpCountDroppedNotServingSubnet,
       "dhcpCountResetCounters": dhcpCountResetCounters,
       "dhcpSrvTrapGroup": dhcpSrvTrapGroup,
       "dhcpSrvTraps": dhcpSrvTraps,
       "dhcpSrvPoolUtlTrap": dhcpSrvPoolUtlTrap}
)
