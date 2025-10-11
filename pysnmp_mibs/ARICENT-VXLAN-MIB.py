# SNMP MIB module (ARICENT-VXLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-VXLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:32 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsvxlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89)
)
if mibBuilder.loadTexts:
    fsvxlan.setRevisions(
        ("2014-05-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class VniId(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4096, 16777215),
    )



class EviId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )



class EvpnVxlanBgpRD(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )



class EvpnVxlanESI(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )



class EvpnVxlanBgpRTType(TextualConvention, Integer32):
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
        *(("import", 1),
          ("export", 2),
          ("both", 3))
    )



class EvpnVxlanVrfName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )



# MIB Managed Objects in the order of their OIDs

_FsVxlanObjects_ObjectIdentity = ObjectIdentity
fsVxlanObjects = _FsVxlanObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1)
)
_FsVxlanSystem_ObjectIdentity = ObjectIdentity
fsVxlanSystem = _FsVxlanSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 1)
)


class _FsVxlanEnable_Type(Integer32):
    """Custom type fsVxlanEnable based on Integer32"""
    defaultValue = 2

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


_FsVxlanEnable_Type.__name__ = "Integer32"
_FsVxlanEnable_Object = MibScalar
fsVxlanEnable = _FsVxlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 1, 1),
    _FsVxlanEnable_Type()
)
fsVxlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanEnable.setStatus("current")


class _FsVxlanUdpPort_Type(Unsigned32):
    """Custom type fsVxlanUdpPort based on Unsigned32"""
    defaultValue = 4789

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 65535),
    )


_FsVxlanUdpPort_Type.__name__ = "Unsigned32"
_FsVxlanUdpPort_Object = MibScalar
fsVxlanUdpPort = _FsVxlanUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 1, 2),
    _FsVxlanUdpPort_Type()
)
fsVxlanUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanUdpPort.setStatus("current")


class _FsVxlanTraceOption_Type(Unsigned32):
    """Custom type fsVxlanTraceOption based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsVxlanTraceOption_Type.__name__ = "Unsigned32"
_FsVxlanTraceOption_Object = MibScalar
fsVxlanTraceOption = _FsVxlanTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 1, 3),
    _FsVxlanTraceOption_Type()
)
fsVxlanTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanTraceOption.setStatus("current")


class _FsVxlanNotificationCntl_Type(Integer32):
    """Custom type fsVxlanNotificationCntl based on Integer32"""
    defaultValue = 2

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


_FsVxlanNotificationCntl_Type.__name__ = "Integer32"
_FsVxlanNotificationCntl_Object = MibScalar
fsVxlanNotificationCntl = _FsVxlanNotificationCntl_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 1, 4),
    _FsVxlanNotificationCntl_Type()
)
fsVxlanNotificationCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanNotificationCntl.setStatus("current")


class _FsEvpnVxlanEnable_Type(Integer32):
    """Custom type fsEvpnVxlanEnable based on Integer32"""
    defaultValue = 2

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


_FsEvpnVxlanEnable_Type.__name__ = "Integer32"
_FsEvpnVxlanEnable_Object = MibScalar
fsEvpnVxlanEnable = _FsEvpnVxlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 1, 5),
    _FsEvpnVxlanEnable_Type()
)
fsEvpnVxlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEnable.setStatus("current")
_FsVxlanConfigObjects_ObjectIdentity = ObjectIdentity
fsVxlanConfigObjects = _FsVxlanConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2)
)
_FsVxlanVtepTable_Object = MibTable
fsVxlanVtepTable = _FsVxlanVtepTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsVxlanVtepTable.setStatus("current")
_FsVxlanVtepEntry_Object = MibTableRow
fsVxlanVtepEntry = _FsVxlanVtepEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 1, 1)
)
fsVxlanVtepEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsVxlanVtepNveIfIndex"),
)
if mibBuilder.loadTexts:
    fsVxlanVtepEntry.setStatus("current")
_FsVxlanVtepNveIfIndex_Type = InterfaceIndexOrZero
_FsVxlanVtepNveIfIndex_Object = MibTableColumn
fsVxlanVtepNveIfIndex = _FsVxlanVtepNveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 1, 1, 1),
    _FsVxlanVtepNveIfIndex_Type()
)
fsVxlanVtepNveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanVtepNveIfIndex.setStatus("current")
_FsVxlanVtepAddressType_Type = InetAddressType
_FsVxlanVtepAddressType_Object = MibTableColumn
fsVxlanVtepAddressType = _FsVxlanVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 1, 1, 2),
    _FsVxlanVtepAddressType_Type()
)
fsVxlanVtepAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanVtepAddressType.setStatus("current")
_FsVxlanVtepAddress_Type = InetAddress
_FsVxlanVtepAddress_Object = MibTableColumn
fsVxlanVtepAddress = _FsVxlanVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 1, 1, 3),
    _FsVxlanVtepAddress_Type()
)
fsVxlanVtepAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanVtepAddress.setStatus("current")
_FsVxlanVtepRowStatus_Type = RowStatus
_FsVxlanVtepRowStatus_Object = MibTableColumn
fsVxlanVtepRowStatus = _FsVxlanVtepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 1, 1, 4),
    _FsVxlanVtepRowStatus_Type()
)
fsVxlanVtepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVxlanVtepRowStatus.setStatus("current")
_FsVxlanNveTable_Object = MibTable
fsVxlanNveTable = _FsVxlanNveTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsVxlanNveTable.setStatus("current")
_FsVxlanNveEntry_Object = MibTableRow
fsVxlanNveEntry = _FsVxlanNveEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1)
)
fsVxlanNveEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsVxlanNveIfIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanNveVniNumber"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanNveDestVmMac"),
)
if mibBuilder.loadTexts:
    fsVxlanNveEntry.setStatus("current")
_FsVxlanNveIfIndex_Type = InterfaceIndexOrZero
_FsVxlanNveIfIndex_Object = MibTableColumn
fsVxlanNveIfIndex = _FsVxlanNveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 1),
    _FsVxlanNveIfIndex_Type()
)
fsVxlanNveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanNveIfIndex.setStatus("current")
_FsVxlanNveVniNumber_Type = VniId
_FsVxlanNveVniNumber_Object = MibTableColumn
fsVxlanNveVniNumber = _FsVxlanNveVniNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 2),
    _FsVxlanNveVniNumber_Type()
)
fsVxlanNveVniNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanNveVniNumber.setStatus("current")
_FsVxlanNveDestVmMac_Type = MacAddress
_FsVxlanNveDestVmMac_Object = MibTableColumn
fsVxlanNveDestVmMac = _FsVxlanNveDestVmMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 3),
    _FsVxlanNveDestVmMac_Type()
)
fsVxlanNveDestVmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanNveDestVmMac.setStatus("current")
_FsVxlanNveVtepAddressType_Type = InetAddressType
_FsVxlanNveVtepAddressType_Object = MibTableColumn
fsVxlanNveVtepAddressType = _FsVxlanNveVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 4),
    _FsVxlanNveVtepAddressType_Type()
)
fsVxlanNveVtepAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanNveVtepAddressType.setStatus("current")
_FsVxlanNveVtepAddress_Type = InetAddress
_FsVxlanNveVtepAddress_Object = MibTableColumn
fsVxlanNveVtepAddress = _FsVxlanNveVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 5),
    _FsVxlanNveVtepAddress_Type()
)
fsVxlanNveVtepAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanNveVtepAddress.setStatus("current")
_FsVxlanNveRemoteVtepAddressType_Type = InetAddressType
_FsVxlanNveRemoteVtepAddressType_Object = MibTableColumn
fsVxlanNveRemoteVtepAddressType = _FsVxlanNveRemoteVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 6),
    _FsVxlanNveRemoteVtepAddressType_Type()
)
fsVxlanNveRemoteVtepAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanNveRemoteVtepAddressType.setStatus("current")
_FsVxlanNveRemoteVtepAddress_Type = InetAddress
_FsVxlanNveRemoteVtepAddress_Object = MibTableColumn
fsVxlanNveRemoteVtepAddress = _FsVxlanNveRemoteVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 7),
    _FsVxlanNveRemoteVtepAddress_Type()
)
fsVxlanNveRemoteVtepAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanNveRemoteVtepAddress.setStatus("current")
_FsVxlanNveStorageType_Type = StorageType
_FsVxlanNveStorageType_Object = MibTableColumn
fsVxlanNveStorageType = _FsVxlanNveStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 8),
    _FsVxlanNveStorageType_Type()
)
fsVxlanNveStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanNveStorageType.setStatus("current")
_FsVxlanNveRowStatus_Type = RowStatus
_FsVxlanNveRowStatus_Object = MibTableColumn
fsVxlanNveRowStatus = _FsVxlanNveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 9),
    _FsVxlanNveRowStatus_Type()
)
fsVxlanNveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVxlanNveRowStatus.setStatus("current")


class _FsVxlanSuppressArp_Type(Integer32):
    """Custom type fsVxlanSuppressArp based on Integer32"""
    defaultValue = 2

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


_FsVxlanSuppressArp_Type.__name__ = "Integer32"
_FsVxlanSuppressArp_Object = MibTableColumn
fsVxlanSuppressArp = _FsVxlanSuppressArp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 2, 1, 10),
    _FsVxlanSuppressArp_Type()
)
fsVxlanSuppressArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanSuppressArp.setStatus("current")
_FsVxlanMCastTable_Object = MibTable
fsVxlanMCastTable = _FsVxlanMCastTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsVxlanMCastTable.setStatus("current")
_FsVxlanMCastEntry_Object = MibTableRow
fsVxlanMCastEntry = _FsVxlanMCastEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1)
)
fsVxlanMCastEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsVxlanMCastNveIfIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanMCastVniNumber"),
)
if mibBuilder.loadTexts:
    fsVxlanMCastEntry.setStatus("current")
_FsVxlanMCastNveIfIndex_Type = InterfaceIndexOrZero
_FsVxlanMCastNveIfIndex_Object = MibTableColumn
fsVxlanMCastNveIfIndex = _FsVxlanMCastNveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1, 1),
    _FsVxlanMCastNveIfIndex_Type()
)
fsVxlanMCastNveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanMCastNveIfIndex.setStatus("current")
_FsVxlanMCastVniNumber_Type = VniId
_FsVxlanMCastVniNumber_Object = MibTableColumn
fsVxlanMCastVniNumber = _FsVxlanMCastVniNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1, 2),
    _FsVxlanMCastVniNumber_Type()
)
fsVxlanMCastVniNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanMCastVniNumber.setStatus("current")
_FsVxlanMCastGroupAddressType_Type = InetAddressType
_FsVxlanMCastGroupAddressType_Object = MibTableColumn
fsVxlanMCastGroupAddressType = _FsVxlanMCastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1, 3),
    _FsVxlanMCastGroupAddressType_Type()
)
fsVxlanMCastGroupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanMCastGroupAddressType.setStatus("current")
_FsVxlanMCastGroupAddress_Type = InetAddress
_FsVxlanMCastGroupAddress_Object = MibTableColumn
fsVxlanMCastGroupAddress = _FsVxlanMCastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1, 4),
    _FsVxlanMCastGroupAddress_Type()
)
fsVxlanMCastGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanMCastGroupAddress.setStatus("current")
_FsVxlanMCastVtepAddressType_Type = InetAddressType
_FsVxlanMCastVtepAddressType_Object = MibTableColumn
fsVxlanMCastVtepAddressType = _FsVxlanMCastVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1, 5),
    _FsVxlanMCastVtepAddressType_Type()
)
fsVxlanMCastVtepAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanMCastVtepAddressType.setStatus("current")
_FsVxlanMCastVtepAddress_Type = InetAddress
_FsVxlanMCastVtepAddress_Object = MibTableColumn
fsVxlanMCastVtepAddress = _FsVxlanMCastVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1, 6),
    _FsVxlanMCastVtepAddress_Type()
)
fsVxlanMCastVtepAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanMCastVtepAddress.setStatus("current")
_FsVxlanMCastRowStatus_Type = RowStatus
_FsVxlanMCastRowStatus_Object = MibTableColumn
fsVxlanMCastRowStatus = _FsVxlanMCastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 3, 1, 7),
    _FsVxlanMCastRowStatus_Type()
)
fsVxlanMCastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVxlanMCastRowStatus.setStatus("current")
_FsVxlanVniVlanMapTable_Object = MibTable
fsVxlanVniVlanMapTable = _FsVxlanVniVlanMapTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapTable.setStatus("current")
_FsVxlanVniVlanMapEntry_Object = MibTableRow
fsVxlanVniVlanMapEntry = _FsVxlanVniVlanMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1)
)
fsVxlanVniVlanMapEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsVxlanVniVlanMapVlanId"),
)
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapEntry.setStatus("current")
_FsVxlanVniVlanMapVlanId_Type = VlanId
_FsVxlanVniVlanMapVlanId_Object = MibTableColumn
fsVxlanVniVlanMapVlanId = _FsVxlanVniVlanMapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1, 1),
    _FsVxlanVniVlanMapVlanId_Type()
)
fsVxlanVniVlanMapVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapVlanId.setStatus("current")
_FsVxlanVniVlanMapVniNumber_Type = VniId
_FsVxlanVniVlanMapVniNumber_Object = MibTableColumn
fsVxlanVniVlanMapVniNumber = _FsVxlanVniVlanMapVniNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1, 2),
    _FsVxlanVniVlanMapVniNumber_Type()
)
fsVxlanVniVlanMapVniNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapVniNumber.setStatus("current")


class _FsVxlanVniVlanMapPktSent_Type(Unsigned32):
    """Custom type fsVxlanVniVlanMapPktSent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsVxlanVniVlanMapPktSent_Type.__name__ = "Unsigned32"
_FsVxlanVniVlanMapPktSent_Object = MibTableColumn
fsVxlanVniVlanMapPktSent = _FsVxlanVniVlanMapPktSent_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1, 3),
    _FsVxlanVniVlanMapPktSent_Type()
)
fsVxlanVniVlanMapPktSent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapPktSent.setStatus("current")


class _FsVxlanVniVlanMapPktRcvd_Type(Unsigned32):
    """Custom type fsVxlanVniVlanMapPktRcvd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsVxlanVniVlanMapPktRcvd_Type.__name__ = "Unsigned32"
_FsVxlanVniVlanMapPktRcvd_Object = MibTableColumn
fsVxlanVniVlanMapPktRcvd = _FsVxlanVniVlanMapPktRcvd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1, 4),
    _FsVxlanVniVlanMapPktRcvd_Type()
)
fsVxlanVniVlanMapPktRcvd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapPktRcvd.setStatus("current")


class _FsVxlanVniVlanMapPktDrpd_Type(Unsigned32):
    """Custom type fsVxlanVniVlanMapPktDrpd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsVxlanVniVlanMapPktDrpd_Type.__name__ = "Unsigned32"
_FsVxlanVniVlanMapPktDrpd_Object = MibTableColumn
fsVxlanVniVlanMapPktDrpd = _FsVxlanVniVlanMapPktDrpd_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1, 5),
    _FsVxlanVniVlanMapPktDrpd_Type()
)
fsVxlanVniVlanMapPktDrpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapPktDrpd.setStatus("current")
_FsVxlanVniVlanMapRowStatus_Type = RowStatus
_FsVxlanVniVlanMapRowStatus_Object = MibTableColumn
fsVxlanVniVlanMapRowStatus = _FsVxlanVniVlanMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1, 6),
    _FsVxlanVniVlanMapRowStatus_Type()
)
fsVxlanVniVlanMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVxlanVniVlanMapRowStatus.setStatus("current")


class _FsVxlanVniVlanDfElection_Type(TruthValue):
    """Custom type fsVxlanVniVlanDfElection based on TruthValue"""
    defaultValue = 2


_FsVxlanVniVlanDfElection_Type.__name__ = "TruthValue"
_FsVxlanVniVlanDfElection_Object = MibTableColumn
fsVxlanVniVlanDfElection = _FsVxlanVniVlanDfElection_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 4, 1, 7),
    _FsVxlanVniVlanDfElection_Type()
)
fsVxlanVniVlanDfElection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanVniVlanDfElection.setStatus("current")
_FsVxlanInReplicaTable_Object = MibTable
fsVxlanInReplicaTable = _FsVxlanInReplicaTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fsVxlanInReplicaTable.setStatus("current")
_FsVxlanInReplicaEntry_Object = MibTableRow
fsVxlanInReplicaEntry = _FsVxlanInReplicaEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1)
)
fsVxlanInReplicaEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsVxlanInReplicaNveIfIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanInReplicaVniNumber"),
)
if mibBuilder.loadTexts:
    fsVxlanInReplicaEntry.setStatus("current")
_FsVxlanInReplicaNveIfIndex_Type = InterfaceIndexOrZero
_FsVxlanInReplicaNveIfIndex_Object = MibTableColumn
fsVxlanInReplicaNveIfIndex = _FsVxlanInReplicaNveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 1),
    _FsVxlanInReplicaNveIfIndex_Type()
)
fsVxlanInReplicaNveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanInReplicaNveIfIndex.setStatus("current")
_FsVxlanInReplicaVniNumber_Type = VniId
_FsVxlanInReplicaVniNumber_Object = MibTableColumn
fsVxlanInReplicaVniNumber = _FsVxlanInReplicaVniNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 2),
    _FsVxlanInReplicaVniNumber_Type()
)
fsVxlanInReplicaVniNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanInReplicaVniNumber.setStatus("current")
_FsVxlanInReplicaVtepAddressType_Type = InetAddressType
_FsVxlanInReplicaVtepAddressType_Object = MibTableColumn
fsVxlanInReplicaVtepAddressType = _FsVxlanInReplicaVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 3),
    _FsVxlanInReplicaVtepAddressType_Type()
)
fsVxlanInReplicaVtepAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanInReplicaVtepAddressType.setStatus("current")
_FsVxlanInReplicaVtepAddress_Type = InetAddress
_FsVxlanInReplicaVtepAddress_Object = MibTableColumn
fsVxlanInReplicaVtepAddress = _FsVxlanInReplicaVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 4),
    _FsVxlanInReplicaVtepAddress_Type()
)
fsVxlanInReplicaVtepAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanInReplicaVtepAddress.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddressType_Type = InetAddressType
_FsVxlanInReplicaRemoteVtepAddressType_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddressType = _FsVxlanInReplicaRemoteVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 5),
    _FsVxlanInReplicaRemoteVtepAddressType_Type()
)
fsVxlanInReplicaRemoteVtepAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddressType.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress1_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress1_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress1 = _FsVxlanInReplicaRemoteVtepAddress1_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 6),
    _FsVxlanInReplicaRemoteVtepAddress1_Type()
)
fsVxlanInReplicaRemoteVtepAddress1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress1.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress2_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress2_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress2 = _FsVxlanInReplicaRemoteVtepAddress2_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 7),
    _FsVxlanInReplicaRemoteVtepAddress2_Type()
)
fsVxlanInReplicaRemoteVtepAddress2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress2.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress3_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress3_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress3 = _FsVxlanInReplicaRemoteVtepAddress3_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 8),
    _FsVxlanInReplicaRemoteVtepAddress3_Type()
)
fsVxlanInReplicaRemoteVtepAddress3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress3.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress4_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress4_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress4 = _FsVxlanInReplicaRemoteVtepAddress4_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 9),
    _FsVxlanInReplicaRemoteVtepAddress4_Type()
)
fsVxlanInReplicaRemoteVtepAddress4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress4.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress5_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress5_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress5 = _FsVxlanInReplicaRemoteVtepAddress5_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 10),
    _FsVxlanInReplicaRemoteVtepAddress5_Type()
)
fsVxlanInReplicaRemoteVtepAddress5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress5.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress6_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress6_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress6 = _FsVxlanInReplicaRemoteVtepAddress6_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 11),
    _FsVxlanInReplicaRemoteVtepAddress6_Type()
)
fsVxlanInReplicaRemoteVtepAddress6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress6.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress7_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress7_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress7 = _FsVxlanInReplicaRemoteVtepAddress7_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 12),
    _FsVxlanInReplicaRemoteVtepAddress7_Type()
)
fsVxlanInReplicaRemoteVtepAddress7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress7.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress8_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress8_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress8 = _FsVxlanInReplicaRemoteVtepAddress8_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 13),
    _FsVxlanInReplicaRemoteVtepAddress8_Type()
)
fsVxlanInReplicaRemoteVtepAddress8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress8.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress9_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress9_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress9 = _FsVxlanInReplicaRemoteVtepAddress9_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 14),
    _FsVxlanInReplicaRemoteVtepAddress9_Type()
)
fsVxlanInReplicaRemoteVtepAddress9.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress9.setStatus("current")
_FsVxlanInReplicaRemoteVtepAddress10_Type = InetAddress
_FsVxlanInReplicaRemoteVtepAddress10_Object = MibTableColumn
fsVxlanInReplicaRemoteVtepAddress10 = _FsVxlanInReplicaRemoteVtepAddress10_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 15),
    _FsVxlanInReplicaRemoteVtepAddress10_Type()
)
fsVxlanInReplicaRemoteVtepAddress10.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRemoteVtepAddress10.setStatus("current")
_FsVxlanInReplicaRowStatus_Type = RowStatus
_FsVxlanInReplicaRowStatus_Object = MibTableColumn
fsVxlanInReplicaRowStatus = _FsVxlanInReplicaRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 5, 1, 16),
    _FsVxlanInReplicaRowStatus_Type()
)
fsVxlanInReplicaRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsVxlanInReplicaRowStatus.setStatus("current")
_FsEvpnVxlanEviVniMapTable_Object = MibTable
fsEvpnVxlanEviVniMapTable = _FsEvpnVxlanEviVniMapTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6)
)
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapTable.setStatus("current")
_FsEvpnVxlanEviVniMapEntry_Object = MibTableRow
fsEvpnVxlanEviVniMapEntry = _FsEvpnVxlanEviVniMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1)
)
fsEvpnVxlanEviVniMapEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanEviVniMapEviIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanEviVniMapVniNumber"),
)
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapEntry.setStatus("current")
_FsEvpnVxlanEviVniMapEviIndex_Type = EviId
_FsEvpnVxlanEviVniMapEviIndex_Object = MibTableColumn
fsEvpnVxlanEviVniMapEviIndex = _FsEvpnVxlanEviVniMapEviIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 1),
    _FsEvpnVxlanEviVniMapEviIndex_Type()
)
fsEvpnVxlanEviVniMapEviIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapEviIndex.setStatus("current")
_FsEvpnVxlanEviVniMapVniNumber_Type = VniId
_FsEvpnVxlanEviVniMapVniNumber_Object = MibTableColumn
fsEvpnVxlanEviVniMapVniNumber = _FsEvpnVxlanEviVniMapVniNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 2),
    _FsEvpnVxlanEviVniMapVniNumber_Type()
)
fsEvpnVxlanEviVniMapVniNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapVniNumber.setStatus("current")
_FsEvpnVxlanEviVniMapBgpRD_Type = EvpnVxlanBgpRD
_FsEvpnVxlanEviVniMapBgpRD_Object = MibTableColumn
fsEvpnVxlanEviVniMapBgpRD = _FsEvpnVxlanEviVniMapBgpRD_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 3),
    _FsEvpnVxlanEviVniMapBgpRD_Type()
)
fsEvpnVxlanEviVniMapBgpRD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapBgpRD.setStatus("current")
_FsEvpnVxlanEviVniESI_Type = EvpnVxlanESI
_FsEvpnVxlanEviVniESI_Object = MibTableColumn
fsEvpnVxlanEviVniESI = _FsEvpnVxlanEviVniESI_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 4),
    _FsEvpnVxlanEviVniESI_Type()
)
fsEvpnVxlanEviVniESI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniESI.setStatus("current")


class _FsEvpnVxlanEviVniLoadBalance_Type(Integer32):
    """Custom type fsEvpnVxlanEviVniLoadBalance based on Integer32"""
    defaultValue = 2

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


_FsEvpnVxlanEviVniLoadBalance_Type.__name__ = "Integer32"
_FsEvpnVxlanEviVniLoadBalance_Object = MibTableColumn
fsEvpnVxlanEviVniLoadBalance = _FsEvpnVxlanEviVniLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 5),
    _FsEvpnVxlanEviVniLoadBalance_Type()
)
fsEvpnVxlanEviVniLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniLoadBalance.setStatus("current")


class _FsEvpnVxlanEviVniMapSentPkts_Type(Unsigned32):
    """Custom type fsEvpnVxlanEviVniMapSentPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsEvpnVxlanEviVniMapSentPkts_Type.__name__ = "Unsigned32"
_FsEvpnVxlanEviVniMapSentPkts_Object = MibTableColumn
fsEvpnVxlanEviVniMapSentPkts = _FsEvpnVxlanEviVniMapSentPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 6),
    _FsEvpnVxlanEviVniMapSentPkts_Type()
)
fsEvpnVxlanEviVniMapSentPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapSentPkts.setStatus("current")


class _FsEvpnVxlanEviVniMapRcvdPkts_Type(Unsigned32):
    """Custom type fsEvpnVxlanEviVniMapRcvdPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsEvpnVxlanEviVniMapRcvdPkts_Type.__name__ = "Unsigned32"
_FsEvpnVxlanEviVniMapRcvdPkts_Object = MibTableColumn
fsEvpnVxlanEviVniMapRcvdPkts = _FsEvpnVxlanEviVniMapRcvdPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 7),
    _FsEvpnVxlanEviVniMapRcvdPkts_Type()
)
fsEvpnVxlanEviVniMapRcvdPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapRcvdPkts.setStatus("current")


class _FsEvpnVxlanEviVniMapDroppedPkts_Type(Unsigned32):
    """Custom type fsEvpnVxlanEviVniMapDroppedPkts based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsEvpnVxlanEviVniMapDroppedPkts_Type.__name__ = "Unsigned32"
_FsEvpnVxlanEviVniMapDroppedPkts_Object = MibTableColumn
fsEvpnVxlanEviVniMapDroppedPkts = _FsEvpnVxlanEviVniMapDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 8),
    _FsEvpnVxlanEviVniMapDroppedPkts_Type()
)
fsEvpnVxlanEviVniMapDroppedPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapDroppedPkts.setStatus("current")
_FsEvpnVxlanEviVniMapRowStatus_Type = RowStatus
_FsEvpnVxlanEviVniMapRowStatus_Object = MibTableColumn
fsEvpnVxlanEviVniMapRowStatus = _FsEvpnVxlanEviVniMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 9),
    _FsEvpnVxlanEviVniMapRowStatus_Type()
)
fsEvpnVxlanEviVniMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapRowStatus.setStatus("current")


class _FsEvpnVxlanEviVniMapBgpRDAuto_Type(TruthValue):
    """Custom type fsEvpnVxlanEviVniMapBgpRDAuto based on TruthValue"""
    defaultValue = 2


_FsEvpnVxlanEviVniMapBgpRDAuto_Type.__name__ = "TruthValue"
_FsEvpnVxlanEviVniMapBgpRDAuto_Object = MibTableColumn
fsEvpnVxlanEviVniMapBgpRDAuto = _FsEvpnVxlanEviVniMapBgpRDAuto_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 6, 1, 10),
    _FsEvpnVxlanEviVniMapBgpRDAuto_Type()
)
fsEvpnVxlanEviVniMapBgpRDAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanEviVniMapBgpRDAuto.setStatus("current")
_FsEvpnVxlanBgpRTTable_Object = MibTable
fsEvpnVxlanBgpRTTable = _FsEvpnVxlanBgpRTTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fsEvpnVxlanBgpRTTable.setStatus("current")
_FsEvpnVxlanBgpRTEntry_Object = MibTableRow
fsEvpnVxlanBgpRTEntry = _FsEvpnVxlanBgpRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 7, 1)
)
fsEvpnVxlanBgpRTEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanEviVniMapEviIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanEviVniMapVniNumber"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanBgpRTIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanBgpRTType"),
)
if mibBuilder.loadTexts:
    fsEvpnVxlanBgpRTEntry.setStatus("current")
_FsEvpnVxlanBgpRTIndex_Type = Unsigned32
_FsEvpnVxlanBgpRTIndex_Object = MibTableColumn
fsEvpnVxlanBgpRTIndex = _FsEvpnVxlanBgpRTIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 7, 1, 1),
    _FsEvpnVxlanBgpRTIndex_Type()
)
fsEvpnVxlanBgpRTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanBgpRTIndex.setStatus("current")
_FsEvpnVxlanBgpRTType_Type = EvpnVxlanBgpRTType
_FsEvpnVxlanBgpRTType_Object = MibTableColumn
fsEvpnVxlanBgpRTType = _FsEvpnVxlanBgpRTType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 7, 1, 2),
    _FsEvpnVxlanBgpRTType_Type()
)
fsEvpnVxlanBgpRTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanBgpRTType.setStatus("current")
_FsEvpnVxlanBgpRT_Type = EvpnVxlanBgpRD
_FsEvpnVxlanBgpRT_Object = MibTableColumn
fsEvpnVxlanBgpRT = _FsEvpnVxlanBgpRT_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 7, 1, 3),
    _FsEvpnVxlanBgpRT_Type()
)
fsEvpnVxlanBgpRT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEvpnVxlanBgpRT.setStatus("current")
_FsEvpnVxlanBgpRTRowStatus_Type = RowStatus
_FsEvpnVxlanBgpRTRowStatus_Object = MibTableColumn
fsEvpnVxlanBgpRTRowStatus = _FsEvpnVxlanBgpRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 7, 1, 4),
    _FsEvpnVxlanBgpRTRowStatus_Type()
)
fsEvpnVxlanBgpRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEvpnVxlanBgpRTRowStatus.setStatus("current")


class _FsEvpnVxlanBgpRTAuto_Type(TruthValue):
    """Custom type fsEvpnVxlanBgpRTAuto based on TruthValue"""
    defaultValue = 2


_FsEvpnVxlanBgpRTAuto_Type.__name__ = "TruthValue"
_FsEvpnVxlanBgpRTAuto_Object = MibTableColumn
fsEvpnVxlanBgpRTAuto = _FsEvpnVxlanBgpRTAuto_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 7, 1, 5),
    _FsEvpnVxlanBgpRTAuto_Type()
)
fsEvpnVxlanBgpRTAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanBgpRTAuto.setStatus("current")
_FsEvpnVxlanVrfTable_Object = MibTable
fsEvpnVxlanVrfTable = _FsEvpnVxlanVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 8)
)
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfTable.setStatus("current")
_FsEvpnVxlanVrfEntry_Object = MibTableRow
fsEvpnVxlanVrfEntry = _FsEvpnVxlanVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 8, 1)
)
fsEvpnVxlanVrfEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanVrfName"),
)
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfEntry.setStatus("current")
_FsEvpnVxlanVrfName_Type = EvpnVxlanVrfName
_FsEvpnVxlanVrfName_Object = MibTableColumn
fsEvpnVxlanVrfName = _FsEvpnVxlanVrfName_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 8, 1, 1),
    _FsEvpnVxlanVrfName_Type()
)
fsEvpnVxlanVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfName.setStatus("current")
_FsEvpnVxlanVrfRD_Type = EvpnVxlanBgpRD
_FsEvpnVxlanVrfRD_Object = MibTableColumn
fsEvpnVxlanVrfRD = _FsEvpnVxlanVrfRD_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 8, 1, 2),
    _FsEvpnVxlanVrfRD_Type()
)
fsEvpnVxlanVrfRD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRD.setStatus("current")
_FsEvpnVxlanVrfRowStatus_Type = RowStatus
_FsEvpnVxlanVrfRowStatus_Object = MibTableColumn
fsEvpnVxlanVrfRowStatus = _FsEvpnVxlanVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 8, 1, 3),
    _FsEvpnVxlanVrfRowStatus_Type()
)
fsEvpnVxlanVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRowStatus.setStatus("current")
_FsEvpnVxlanVrfRTTable_Object = MibTable
fsEvpnVxlanVrfRTTable = _FsEvpnVxlanVrfRTTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 9)
)
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRTTable.setStatus("current")
_FsEvpnVxlanVrfRTEntry_Object = MibTableRow
fsEvpnVxlanVrfRTEntry = _FsEvpnVxlanVrfRTEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 9, 1)
)
fsEvpnVxlanVrfRTEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanVrfName"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanVrfRTIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanVrfRTType"),
)
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRTEntry.setStatus("current")
_FsEvpnVxlanVrfRTIndex_Type = Unsigned32
_FsEvpnVxlanVrfRTIndex_Object = MibTableColumn
fsEvpnVxlanVrfRTIndex = _FsEvpnVxlanVrfRTIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 9, 1, 1),
    _FsEvpnVxlanVrfRTIndex_Type()
)
fsEvpnVxlanVrfRTIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRTIndex.setStatus("current")
_FsEvpnVxlanVrfRTType_Type = EvpnVxlanBgpRTType
_FsEvpnVxlanVrfRTType_Object = MibTableColumn
fsEvpnVxlanVrfRTType = _FsEvpnVxlanVrfRTType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 9, 1, 2),
    _FsEvpnVxlanVrfRTType_Type()
)
fsEvpnVxlanVrfRTType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRTType.setStatus("current")
_FsEvpnVxlanVrfRT_Type = EvpnVxlanBgpRD
_FsEvpnVxlanVrfRT_Object = MibTableColumn
fsEvpnVxlanVrfRT = _FsEvpnVxlanVrfRT_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 9, 1, 3),
    _FsEvpnVxlanVrfRT_Type()
)
fsEvpnVxlanVrfRT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRT.setStatus("current")
_FsEvpnVxlanVrfRTRowStatus_Type = RowStatus
_FsEvpnVxlanVrfRTRowStatus_Object = MibTableColumn
fsEvpnVxlanVrfRTRowStatus = _FsEvpnVxlanVrfRTRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 9, 1, 4),
    _FsEvpnVxlanVrfRTRowStatus_Type()
)
fsEvpnVxlanVrfRTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEvpnVxlanVrfRTRowStatus.setStatus("current")
_FsEvpnVxlanMultihomedPeerTable_Object = MibTable
fsEvpnVxlanMultihomedPeerTable = _FsEvpnVxlanMultihomedPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 10)
)
if mibBuilder.loadTexts:
    fsEvpnVxlanMultihomedPeerTable.setStatus("current")
_FsEvpnVxlanMultihomedPeerEntry_Object = MibTableRow
fsEvpnVxlanMultihomedPeerEntry = _FsEvpnVxlanMultihomedPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 10, 1)
)
fsEvpnVxlanMultihomedPeerEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanPeerIpAddressType"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanPeerIpAddress"),
    (0, "ARICENT-VXLAN-MIB", "fsEvpnVxlanMHEviVniESI"),
)
if mibBuilder.loadTexts:
    fsEvpnVxlanMultihomedPeerEntry.setStatus("current")
_FsEvpnVxlanPeerIpAddressType_Type = InetAddressType
_FsEvpnVxlanPeerIpAddressType_Object = MibTableColumn
fsEvpnVxlanPeerIpAddressType = _FsEvpnVxlanPeerIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 10, 1, 1),
    _FsEvpnVxlanPeerIpAddressType_Type()
)
fsEvpnVxlanPeerIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanPeerIpAddressType.setStatus("current")
_FsEvpnVxlanPeerIpAddress_Type = InetAddress
_FsEvpnVxlanPeerIpAddress_Object = MibTableColumn
fsEvpnVxlanPeerIpAddress = _FsEvpnVxlanPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 10, 1, 2),
    _FsEvpnVxlanPeerIpAddress_Type()
)
fsEvpnVxlanPeerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanPeerIpAddress.setStatus("current")
_FsEvpnVxlanMHEviVniESI_Type = EvpnVxlanESI
_FsEvpnVxlanMHEviVniESI_Object = MibTableColumn
fsEvpnVxlanMHEviVniESI = _FsEvpnVxlanMHEviVniESI_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 10, 1, 3),
    _FsEvpnVxlanMHEviVniESI_Type()
)
fsEvpnVxlanMHEviVniESI.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsEvpnVxlanMHEviVniESI.setStatus("current")


class _FsEvpnVxlanOrdinalNum_Type(Unsigned32):
    """Custom type fsEvpnVxlanOrdinalNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsEvpnVxlanOrdinalNum_Type.__name__ = "Unsigned32"
_FsEvpnVxlanOrdinalNum_Object = MibTableColumn
fsEvpnVxlanOrdinalNum = _FsEvpnVxlanOrdinalNum_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 10, 1, 4),
    _FsEvpnVxlanOrdinalNum_Type()
)
fsEvpnVxlanOrdinalNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEvpnVxlanOrdinalNum.setStatus("current")
_FsEvpnVxlanMultihomedPeerRowStatus_Type = RowStatus
_FsEvpnVxlanMultihomedPeerRowStatus_Object = MibTableColumn
fsEvpnVxlanMultihomedPeerRowStatus = _FsEvpnVxlanMultihomedPeerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 10, 1, 5),
    _FsEvpnVxlanMultihomedPeerRowStatus_Type()
)
fsEvpnVxlanMultihomedPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsEvpnVxlanMultihomedPeerRowStatus.setStatus("current")
_FsVxlanEcmpNveTable_Object = MibTable
fsVxlanEcmpNveTable = _FsVxlanEcmpNveTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11)
)
if mibBuilder.loadTexts:
    fsVxlanEcmpNveTable.setStatus("current")
_FsVxlanEcmpNveEntry_Object = MibTableRow
fsVxlanEcmpNveEntry = _FsVxlanEcmpNveEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1)
)
fsVxlanEcmpNveEntry.setIndexNames(
    (0, "ARICENT-VXLAN-MIB", "fsVxlanEcmpNveIfIndex"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanEcmpNveVniNumber"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanEcmpNveDestVmMac"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanEcmpNveRemoteVtepAddressType"),
    (0, "ARICENT-VXLAN-MIB", "fsVxlanEcmpNveRemoteVtepAddress"),
)
if mibBuilder.loadTexts:
    fsVxlanEcmpNveEntry.setStatus("current")
_FsVxlanEcmpNveIfIndex_Type = InterfaceIndexOrZero
_FsVxlanEcmpNveIfIndex_Object = MibTableColumn
fsVxlanEcmpNveIfIndex = _FsVxlanEcmpNveIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 1),
    _FsVxlanEcmpNveIfIndex_Type()
)
fsVxlanEcmpNveIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveIfIndex.setStatus("current")
_FsVxlanEcmpNveVniNumber_Type = VniId
_FsVxlanEcmpNveVniNumber_Object = MibTableColumn
fsVxlanEcmpNveVniNumber = _FsVxlanEcmpNveVniNumber_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 2),
    _FsVxlanEcmpNveVniNumber_Type()
)
fsVxlanEcmpNveVniNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveVniNumber.setStatus("current")
_FsVxlanEcmpNveDestVmMac_Type = MacAddress
_FsVxlanEcmpNveDestVmMac_Object = MibTableColumn
fsVxlanEcmpNveDestVmMac = _FsVxlanEcmpNveDestVmMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 3),
    _FsVxlanEcmpNveDestVmMac_Type()
)
fsVxlanEcmpNveDestVmMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveDestVmMac.setStatus("current")
_FsVxlanEcmpNveVtepAddressType_Type = InetAddressType
_FsVxlanEcmpNveVtepAddressType_Object = MibTableColumn
fsVxlanEcmpNveVtepAddressType = _FsVxlanEcmpNveVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 4),
    _FsVxlanEcmpNveVtepAddressType_Type()
)
fsVxlanEcmpNveVtepAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveVtepAddressType.setStatus("current")
_FsVxlanEcmpNveVtepAddress_Type = InetAddress
_FsVxlanEcmpNveVtepAddress_Object = MibTableColumn
fsVxlanEcmpNveVtepAddress = _FsVxlanEcmpNveVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 5),
    _FsVxlanEcmpNveVtepAddress_Type()
)
fsVxlanEcmpNveVtepAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveVtepAddress.setStatus("current")
_FsVxlanEcmpNveRemoteVtepAddressType_Type = InetAddressType
_FsVxlanEcmpNveRemoteVtepAddressType_Object = MibTableColumn
fsVxlanEcmpNveRemoteVtepAddressType = _FsVxlanEcmpNveRemoteVtepAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 6),
    _FsVxlanEcmpNveRemoteVtepAddressType_Type()
)
fsVxlanEcmpNveRemoteVtepAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveRemoteVtepAddressType.setStatus("current")
_FsVxlanEcmpNveRemoteVtepAddress_Type = InetAddress
_FsVxlanEcmpNveRemoteVtepAddress_Object = MibTableColumn
fsVxlanEcmpNveRemoteVtepAddress = _FsVxlanEcmpNveRemoteVtepAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 7),
    _FsVxlanEcmpNveRemoteVtepAddress_Type()
)
fsVxlanEcmpNveRemoteVtepAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveRemoteVtepAddress.setStatus("current")
_FsVxlanEcmpNveStorageType_Type = StorageType
_FsVxlanEcmpNveStorageType_Object = MibTableColumn
fsVxlanEcmpNveStorageType = _FsVxlanEcmpNveStorageType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 8),
    _FsVxlanEcmpNveStorageType_Type()
)
fsVxlanEcmpNveStorageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanEcmpNveStorageType.setStatus("current")


class _FsVxlanEcmpSuppressArp_Type(Integer32):
    """Custom type fsVxlanEcmpSuppressArp based on Integer32"""
    defaultValue = 2

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


_FsVxlanEcmpSuppressArp_Type.__name__ = "Integer32"
_FsVxlanEcmpSuppressArp_Object = MibTableColumn
fsVxlanEcmpSuppressArp = _FsVxlanEcmpSuppressArp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 9),
    _FsVxlanEcmpSuppressArp_Type()
)
fsVxlanEcmpSuppressArp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanEcmpSuppressArp.setStatus("current")
_FsVxlanEcmpMHEviVniESI_Type = EvpnVxlanESI
_FsVxlanEcmpMHEviVniESI_Object = MibTableColumn
fsVxlanEcmpMHEviVniESI = _FsVxlanEcmpMHEviVniESI_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 10),
    _FsVxlanEcmpMHEviVniESI_Type()
)
fsVxlanEcmpMHEviVniESI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanEcmpMHEviVniESI.setStatus("current")


class _FsVxlanEcmpActive_Type(TruthValue):
    """Custom type fsVxlanEcmpActive based on TruthValue"""
    defaultValue = 2


_FsVxlanEcmpActive_Type.__name__ = "TruthValue"
_FsVxlanEcmpActive_Object = MibTableColumn
fsVxlanEcmpActive = _FsVxlanEcmpActive_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 89, 1, 2, 11, 1, 11),
    _FsVxlanEcmpActive_Type()
)
fsVxlanEcmpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVxlanEcmpActive.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-VXLAN-MIB",
    **{"VlanId": VlanId,
       "VniId": VniId,
       "EviId": EviId,
       "EvpnVxlanBgpRD": EvpnVxlanBgpRD,
       "EvpnVxlanESI": EvpnVxlanESI,
       "EvpnVxlanBgpRTType": EvpnVxlanBgpRTType,
       "EvpnVxlanVrfName": EvpnVxlanVrfName,
       "fsvxlan": fsvxlan,
       "fsVxlanObjects": fsVxlanObjects,
       "fsVxlanSystem": fsVxlanSystem,
       "fsVxlanEnable": fsVxlanEnable,
       "fsVxlanUdpPort": fsVxlanUdpPort,
       "fsVxlanTraceOption": fsVxlanTraceOption,
       "fsVxlanNotificationCntl": fsVxlanNotificationCntl,
       "fsEvpnVxlanEnable": fsEvpnVxlanEnable,
       "fsVxlanConfigObjects": fsVxlanConfigObjects,
       "fsVxlanVtepTable": fsVxlanVtepTable,
       "fsVxlanVtepEntry": fsVxlanVtepEntry,
       "fsVxlanVtepNveIfIndex": fsVxlanVtepNveIfIndex,
       "fsVxlanVtepAddressType": fsVxlanVtepAddressType,
       "fsVxlanVtepAddress": fsVxlanVtepAddress,
       "fsVxlanVtepRowStatus": fsVxlanVtepRowStatus,
       "fsVxlanNveTable": fsVxlanNveTable,
       "fsVxlanNveEntry": fsVxlanNveEntry,
       "fsVxlanNveIfIndex": fsVxlanNveIfIndex,
       "fsVxlanNveVniNumber": fsVxlanNveVniNumber,
       "fsVxlanNveDestVmMac": fsVxlanNveDestVmMac,
       "fsVxlanNveVtepAddressType": fsVxlanNveVtepAddressType,
       "fsVxlanNveVtepAddress": fsVxlanNveVtepAddress,
       "fsVxlanNveRemoteVtepAddressType": fsVxlanNveRemoteVtepAddressType,
       "fsVxlanNveRemoteVtepAddress": fsVxlanNveRemoteVtepAddress,
       "fsVxlanNveStorageType": fsVxlanNveStorageType,
       "fsVxlanNveRowStatus": fsVxlanNveRowStatus,
       "fsVxlanSuppressArp": fsVxlanSuppressArp,
       "fsVxlanMCastTable": fsVxlanMCastTable,
       "fsVxlanMCastEntry": fsVxlanMCastEntry,
       "fsVxlanMCastNveIfIndex": fsVxlanMCastNveIfIndex,
       "fsVxlanMCastVniNumber": fsVxlanMCastVniNumber,
       "fsVxlanMCastGroupAddressType": fsVxlanMCastGroupAddressType,
       "fsVxlanMCastGroupAddress": fsVxlanMCastGroupAddress,
       "fsVxlanMCastVtepAddressType": fsVxlanMCastVtepAddressType,
       "fsVxlanMCastVtepAddress": fsVxlanMCastVtepAddress,
       "fsVxlanMCastRowStatus": fsVxlanMCastRowStatus,
       "fsVxlanVniVlanMapTable": fsVxlanVniVlanMapTable,
       "fsVxlanVniVlanMapEntry": fsVxlanVniVlanMapEntry,
       "fsVxlanVniVlanMapVlanId": fsVxlanVniVlanMapVlanId,
       "fsVxlanVniVlanMapVniNumber": fsVxlanVniVlanMapVniNumber,
       "fsVxlanVniVlanMapPktSent": fsVxlanVniVlanMapPktSent,
       "fsVxlanVniVlanMapPktRcvd": fsVxlanVniVlanMapPktRcvd,
       "fsVxlanVniVlanMapPktDrpd": fsVxlanVniVlanMapPktDrpd,
       "fsVxlanVniVlanMapRowStatus": fsVxlanVniVlanMapRowStatus,
       "fsVxlanVniVlanDfElection": fsVxlanVniVlanDfElection,
       "fsVxlanInReplicaTable": fsVxlanInReplicaTable,
       "fsVxlanInReplicaEntry": fsVxlanInReplicaEntry,
       "fsVxlanInReplicaNveIfIndex": fsVxlanInReplicaNveIfIndex,
       "fsVxlanInReplicaVniNumber": fsVxlanInReplicaVniNumber,
       "fsVxlanInReplicaVtepAddressType": fsVxlanInReplicaVtepAddressType,
       "fsVxlanInReplicaVtepAddress": fsVxlanInReplicaVtepAddress,
       "fsVxlanInReplicaRemoteVtepAddressType": fsVxlanInReplicaRemoteVtepAddressType,
       "fsVxlanInReplicaRemoteVtepAddress1": fsVxlanInReplicaRemoteVtepAddress1,
       "fsVxlanInReplicaRemoteVtepAddress2": fsVxlanInReplicaRemoteVtepAddress2,
       "fsVxlanInReplicaRemoteVtepAddress3": fsVxlanInReplicaRemoteVtepAddress3,
       "fsVxlanInReplicaRemoteVtepAddress4": fsVxlanInReplicaRemoteVtepAddress4,
       "fsVxlanInReplicaRemoteVtepAddress5": fsVxlanInReplicaRemoteVtepAddress5,
       "fsVxlanInReplicaRemoteVtepAddress6": fsVxlanInReplicaRemoteVtepAddress6,
       "fsVxlanInReplicaRemoteVtepAddress7": fsVxlanInReplicaRemoteVtepAddress7,
       "fsVxlanInReplicaRemoteVtepAddress8": fsVxlanInReplicaRemoteVtepAddress8,
       "fsVxlanInReplicaRemoteVtepAddress9": fsVxlanInReplicaRemoteVtepAddress9,
       "fsVxlanInReplicaRemoteVtepAddress10": fsVxlanInReplicaRemoteVtepAddress10,
       "fsVxlanInReplicaRowStatus": fsVxlanInReplicaRowStatus,
       "fsEvpnVxlanEviVniMapTable": fsEvpnVxlanEviVniMapTable,
       "fsEvpnVxlanEviVniMapEntry": fsEvpnVxlanEviVniMapEntry,
       "fsEvpnVxlanEviVniMapEviIndex": fsEvpnVxlanEviVniMapEviIndex,
       "fsEvpnVxlanEviVniMapVniNumber": fsEvpnVxlanEviVniMapVniNumber,
       "fsEvpnVxlanEviVniMapBgpRD": fsEvpnVxlanEviVniMapBgpRD,
       "fsEvpnVxlanEviVniESI": fsEvpnVxlanEviVniESI,
       "fsEvpnVxlanEviVniLoadBalance": fsEvpnVxlanEviVniLoadBalance,
       "fsEvpnVxlanEviVniMapSentPkts": fsEvpnVxlanEviVniMapSentPkts,
       "fsEvpnVxlanEviVniMapRcvdPkts": fsEvpnVxlanEviVniMapRcvdPkts,
       "fsEvpnVxlanEviVniMapDroppedPkts": fsEvpnVxlanEviVniMapDroppedPkts,
       "fsEvpnVxlanEviVniMapRowStatus": fsEvpnVxlanEviVniMapRowStatus,
       "fsEvpnVxlanEviVniMapBgpRDAuto": fsEvpnVxlanEviVniMapBgpRDAuto,
       "fsEvpnVxlanBgpRTTable": fsEvpnVxlanBgpRTTable,
       "fsEvpnVxlanBgpRTEntry": fsEvpnVxlanBgpRTEntry,
       "fsEvpnVxlanBgpRTIndex": fsEvpnVxlanBgpRTIndex,
       "fsEvpnVxlanBgpRTType": fsEvpnVxlanBgpRTType,
       "fsEvpnVxlanBgpRT": fsEvpnVxlanBgpRT,
       "fsEvpnVxlanBgpRTRowStatus": fsEvpnVxlanBgpRTRowStatus,
       "fsEvpnVxlanBgpRTAuto": fsEvpnVxlanBgpRTAuto,
       "fsEvpnVxlanVrfTable": fsEvpnVxlanVrfTable,
       "fsEvpnVxlanVrfEntry": fsEvpnVxlanVrfEntry,
       "fsEvpnVxlanVrfName": fsEvpnVxlanVrfName,
       "fsEvpnVxlanVrfRD": fsEvpnVxlanVrfRD,
       "fsEvpnVxlanVrfRowStatus": fsEvpnVxlanVrfRowStatus,
       "fsEvpnVxlanVrfRTTable": fsEvpnVxlanVrfRTTable,
       "fsEvpnVxlanVrfRTEntry": fsEvpnVxlanVrfRTEntry,
       "fsEvpnVxlanVrfRTIndex": fsEvpnVxlanVrfRTIndex,
       "fsEvpnVxlanVrfRTType": fsEvpnVxlanVrfRTType,
       "fsEvpnVxlanVrfRT": fsEvpnVxlanVrfRT,
       "fsEvpnVxlanVrfRTRowStatus": fsEvpnVxlanVrfRTRowStatus,
       "fsEvpnVxlanMultihomedPeerTable": fsEvpnVxlanMultihomedPeerTable,
       "fsEvpnVxlanMultihomedPeerEntry": fsEvpnVxlanMultihomedPeerEntry,
       "fsEvpnVxlanPeerIpAddressType": fsEvpnVxlanPeerIpAddressType,
       "fsEvpnVxlanPeerIpAddress": fsEvpnVxlanPeerIpAddress,
       "fsEvpnVxlanMHEviVniESI": fsEvpnVxlanMHEviVniESI,
       "fsEvpnVxlanOrdinalNum": fsEvpnVxlanOrdinalNum,
       "fsEvpnVxlanMultihomedPeerRowStatus": fsEvpnVxlanMultihomedPeerRowStatus,
       "fsVxlanEcmpNveTable": fsVxlanEcmpNveTable,
       "fsVxlanEcmpNveEntry": fsVxlanEcmpNveEntry,
       "fsVxlanEcmpNveIfIndex": fsVxlanEcmpNveIfIndex,
       "fsVxlanEcmpNveVniNumber": fsVxlanEcmpNveVniNumber,
       "fsVxlanEcmpNveDestVmMac": fsVxlanEcmpNveDestVmMac,
       "fsVxlanEcmpNveVtepAddressType": fsVxlanEcmpNveVtepAddressType,
       "fsVxlanEcmpNveVtepAddress": fsVxlanEcmpNveVtepAddress,
       "fsVxlanEcmpNveRemoteVtepAddressType": fsVxlanEcmpNveRemoteVtepAddressType,
       "fsVxlanEcmpNveRemoteVtepAddress": fsVxlanEcmpNveRemoteVtepAddress,
       "fsVxlanEcmpNveStorageType": fsVxlanEcmpNveStorageType,
       "fsVxlanEcmpSuppressArp": fsVxlanEcmpSuppressArp,
       "fsVxlanEcmpMHEviVniESI": fsVxlanEcmpMHEviVniESI,
       "fsVxlanEcmpActive": fsVxlanEcmpActive}
)
