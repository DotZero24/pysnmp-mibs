# SNMP MIB module (ARICENT-MIIPDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MIIPDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:37 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsMIIpdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48)
)
if mibBuilder.loadTexts:
    fsMIIpdb.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Ipv6Address(TextualConvention, OctetString):
    status = "current"
    displayHint = "2x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16



# MIB Managed Objects in the order of their OIDs

_FsMIIpDbScalars_ObjectIdentity = ObjectIdentity
fsMIIpDbScalars = _FsMIIpDbScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1)
)
_FsMIIpDbNoOfBindings_Type = Counter32
_FsMIIpDbNoOfBindings_Object = MibScalar
fsMIIpDbNoOfBindings = _FsMIIpDbNoOfBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 1),
    _FsMIIpDbNoOfBindings_Type()
)
fsMIIpDbNoOfBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfBindings.setStatus("current")
_FsMIIpDbNoOfStaticBindings_Type = Counter32
_FsMIIpDbNoOfStaticBindings_Object = MibScalar
fsMIIpDbNoOfStaticBindings = _FsMIIpDbNoOfStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 2),
    _FsMIIpDbNoOfStaticBindings_Type()
)
fsMIIpDbNoOfStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfStaticBindings.setStatus("current")
_FsMIIpDbNoOfDHCPBindings_Type = Counter32
_FsMIIpDbNoOfDHCPBindings_Object = MibScalar
fsMIIpDbNoOfDHCPBindings = _FsMIIpDbNoOfDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 3),
    _FsMIIpDbNoOfDHCPBindings_Type()
)
fsMIIpDbNoOfDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfDHCPBindings.setStatus("current")
_FsMIIpDbNoOfPPPBindings_Type = Counter32
_FsMIIpDbNoOfPPPBindings_Object = MibScalar
fsMIIpDbNoOfPPPBindings = _FsMIIpDbNoOfPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 4),
    _FsMIIpDbNoOfPPPBindings_Type()
)
fsMIIpDbNoOfPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfPPPBindings.setStatus("current")
_FsMIIpDbTraceLevel_Type = Integer32
_FsMIIpDbTraceLevel_Object = MibScalar
fsMIIpDbTraceLevel = _FsMIIpDbTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 5),
    _FsMIIpDbTraceLevel_Type()
)
fsMIIpDbTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbTraceLevel.setStatus("current")


class _FsMIIpDbv6DynamicDbSaveStatus_Type(Integer32):
    """Custom type fsMIIpDbv6DynamicDbSaveStatus based on Integer32"""
    defaultValue = 1

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


_FsMIIpDbv6DynamicDbSaveStatus_Type.__name__ = "Integer32"
_FsMIIpDbv6DynamicDbSaveStatus_Object = MibScalar
fsMIIpDbv6DynamicDbSaveStatus = _FsMIIpDbv6DynamicDbSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 6),
    _FsMIIpDbv6DynamicDbSaveStatus_Type()
)
fsMIIpDbv6DynamicDbSaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6DynamicDbSaveStatus.setStatus("current")


class _FsMIIpDbClearBindingStatus_Type(TruthValue):
    """Custom type fsMIIpDbClearBindingStatus based on TruthValue"""
    defaultValue = 2


_FsMIIpDbClearBindingStatus_Type.__name__ = "TruthValue"
_FsMIIpDbClearBindingStatus_Object = MibScalar
fsMIIpDbClearBindingStatus = _FsMIIpDbClearBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 7),
    _FsMIIpDbClearBindingStatus_Type()
)
fsMIIpDbClearBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbClearBindingStatus.setStatus("current")


class _FsMIIpDbv6ClearBindingStatus_Type(TruthValue):
    """Custom type fsMIIpDbv6ClearBindingStatus based on TruthValue"""
    defaultValue = 2


_FsMIIpDbv6ClearBindingStatus_Type.__name__ = "TruthValue"
_FsMIIpDbv6ClearBindingStatus_Object = MibScalar
fsMIIpDbv6ClearBindingStatus = _FsMIIpDbv6ClearBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 1, 8),
    _FsMIIpDbv6ClearBindingStatus_Type()
)
fsMIIpDbv6ClearBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6ClearBindingStatus.setStatus("current")
_FsMIIpDbStatic_ObjectIdentity = ObjectIdentity
fsMIIpDbStatic = _FsMIIpDbStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2)
)
_FsMIIpDbStaticBindingTable_Object = MibTable
fsMIIpDbStaticBindingTable = _FsMIIpDbStaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbStaticBindingTable.setStatus("current")
_FsMIIpDbStaticBindingEntry_Object = MibTableRow
fsMIIpDbStaticBindingEntry = _FsMIIpDbStaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1)
)
fsMIIpDbStaticBindingEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbContextId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbStaticHostVlanId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbStaticHostMac"),
)
if mibBuilder.loadTexts:
    fsMIIpDbStaticBindingEntry.setStatus("current")


class _FsMIIpDbContextId_Type(Integer32):
    """Custom type fsMIIpDbContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIIpDbContextId_Type.__name__ = "Integer32"
_FsMIIpDbContextId_Object = MibTableColumn
fsMIIpDbContextId = _FsMIIpDbContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1, 1),
    _FsMIIpDbContextId_Type()
)
fsMIIpDbContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbContextId.setStatus("current")


class _FsMIIpDbStaticHostVlanId_Type(Integer32):
    """Custom type fsMIIpDbStaticHostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIIpDbStaticHostVlanId_Type.__name__ = "Integer32"
_FsMIIpDbStaticHostVlanId_Object = MibTableColumn
fsMIIpDbStaticHostVlanId = _FsMIIpDbStaticHostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1, 2),
    _FsMIIpDbStaticHostVlanId_Type()
)
fsMIIpDbStaticHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbStaticHostVlanId.setStatus("current")
_FsMIIpDbStaticHostMac_Type = MacAddress
_FsMIIpDbStaticHostMac_Object = MibTableColumn
fsMIIpDbStaticHostMac = _FsMIIpDbStaticHostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1, 3),
    _FsMIIpDbStaticHostMac_Type()
)
fsMIIpDbStaticHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbStaticHostMac.setStatus("current")
_FsMIIpDbStaticHostIp_Type = IpAddress
_FsMIIpDbStaticHostIp_Object = MibTableColumn
fsMIIpDbStaticHostIp = _FsMIIpDbStaticHostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1, 4),
    _FsMIIpDbStaticHostIp_Type()
)
fsMIIpDbStaticHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticHostIp.setStatus("current")
_FsMIIpDbStaticInIfIndex_Type = Integer32
_FsMIIpDbStaticInIfIndex_Object = MibTableColumn
fsMIIpDbStaticInIfIndex = _FsMIIpDbStaticInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1, 5),
    _FsMIIpDbStaticInIfIndex_Type()
)
fsMIIpDbStaticInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticInIfIndex.setStatus("current")
_FsMIIpDbStaticGateway_Type = IpAddress
_FsMIIpDbStaticGateway_Object = MibTableColumn
fsMIIpDbStaticGateway = _FsMIIpDbStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1, 6),
    _FsMIIpDbStaticGateway_Type()
)
fsMIIpDbStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticGateway.setStatus("current")
_FsMIIpDbStaticBindingStatus_Type = RowStatus
_FsMIIpDbStaticBindingStatus_Object = MibTableColumn
fsMIIpDbStaticBindingStatus = _FsMIIpDbStaticBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 2, 1, 1, 7),
    _FsMIIpDbStaticBindingStatus_Type()
)
fsMIIpDbStaticBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticBindingStatus.setStatus("current")
_FsMIIpDbBindings_ObjectIdentity = ObjectIdentity
fsMIIpDbBindings = _FsMIIpDbBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3)
)
_FsMIIpDbBindingTable_Object = MibTable
fsMIIpDbBindingTable = _FsMIIpDbBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbBindingTable.setStatus("current")
_FsMIIpDbBindingEntry_Object = MibTableRow
fsMIIpDbBindingEntry = _FsMIIpDbBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1)
)
fsMIIpDbBindingEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbHostContextId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbHostVlanId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbHostMac"),
)
if mibBuilder.loadTexts:
    fsMIIpDbBindingEntry.setStatus("current")


class _FsMIIpDbHostContextId_Type(Integer32):
    """Custom type fsMIIpDbHostContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIIpDbHostContextId_Type.__name__ = "Integer32"
_FsMIIpDbHostContextId_Object = MibTableColumn
fsMIIpDbHostContextId = _FsMIIpDbHostContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 1),
    _FsMIIpDbHostContextId_Type()
)
fsMIIpDbHostContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbHostContextId.setStatus("current")


class _FsMIIpDbHostVlanId_Type(Integer32):
    """Custom type fsMIIpDbHostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIIpDbHostVlanId_Type.__name__ = "Integer32"
_FsMIIpDbHostVlanId_Object = MibTableColumn
fsMIIpDbHostVlanId = _FsMIIpDbHostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 2),
    _FsMIIpDbHostVlanId_Type()
)
fsMIIpDbHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbHostVlanId.setStatus("current")
_FsMIIpDbHostMac_Type = MacAddress
_FsMIIpDbHostMac_Object = MibTableColumn
fsMIIpDbHostMac = _FsMIIpDbHostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 3),
    _FsMIIpDbHostMac_Type()
)
fsMIIpDbHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbHostMac.setStatus("current")


class _FsMIIpDbHostBindingType_Type(Integer32):
    """Custom type fsMIIpDbHostBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2),
          ("ppp", 3))
    )


_FsMIIpDbHostBindingType_Type.__name__ = "Integer32"
_FsMIIpDbHostBindingType_Object = MibTableColumn
fsMIIpDbHostBindingType = _FsMIIpDbHostBindingType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 4),
    _FsMIIpDbHostBindingType_Type()
)
fsMIIpDbHostBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostBindingType.setStatus("current")
_FsMIIpDbHostIp_Type = IpAddress
_FsMIIpDbHostIp_Object = MibTableColumn
fsMIIpDbHostIp = _FsMIIpDbHostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 5),
    _FsMIIpDbHostIp_Type()
)
fsMIIpDbHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostIp.setStatus("current")
_FsMIIpDbHostInIfIndex_Type = Integer32
_FsMIIpDbHostInIfIndex_Object = MibTableColumn
fsMIIpDbHostInIfIndex = _FsMIIpDbHostInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 6),
    _FsMIIpDbHostInIfIndex_Type()
)
fsMIIpDbHostInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostInIfIndex.setStatus("current")
_FsMIIpDbHostRemLeaseTime_Type = Integer32
_FsMIIpDbHostRemLeaseTime_Object = MibTableColumn
fsMIIpDbHostRemLeaseTime = _FsMIIpDbHostRemLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 7),
    _FsMIIpDbHostRemLeaseTime_Type()
)
fsMIIpDbHostRemLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostRemLeaseTime.setStatus("current")
_FsMIIpDbHostBindingID_Type = Unsigned32
_FsMIIpDbHostBindingID_Object = MibTableColumn
fsMIIpDbHostBindingID = _FsMIIpDbHostBindingID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 1, 1, 8),
    _FsMIIpDbHostBindingID_Type()
)
fsMIIpDbHostBindingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostBindingID.setStatus("current")
_FsMIIpDbGatewayIpTable_Object = MibTable
fsMIIpDbGatewayIpTable = _FsMIIpDbGatewayIpTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 2)
)
if mibBuilder.loadTexts:
    fsMIIpDbGatewayIpTable.setStatus("current")
_FsMIIpDbGatewayIpEntry_Object = MibTableRow
fsMIIpDbGatewayIpEntry = _FsMIIpDbGatewayIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 2, 1)
)
fsMIIpDbGatewayIpEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbHostContextId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbHostMac"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbHostVlanId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbGatewayNetwork"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbGatewayNetMask"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbGatewayIp"),
)
if mibBuilder.loadTexts:
    fsMIIpDbGatewayIpEntry.setStatus("current")
_FsMIIpDbGatewayNetwork_Type = IpAddress
_FsMIIpDbGatewayNetwork_Object = MibTableColumn
fsMIIpDbGatewayNetwork = _FsMIIpDbGatewayNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 2, 1, 1),
    _FsMIIpDbGatewayNetwork_Type()
)
fsMIIpDbGatewayNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbGatewayNetwork.setStatus("current")
_FsMIIpDbGatewayNetMask_Type = IpAddress
_FsMIIpDbGatewayNetMask_Object = MibTableColumn
fsMIIpDbGatewayNetMask = _FsMIIpDbGatewayNetMask_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 2, 1, 2),
    _FsMIIpDbGatewayNetMask_Type()
)
fsMIIpDbGatewayNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbGatewayNetMask.setStatus("current")
_FsMIIpDbGatewayIp_Type = IpAddress
_FsMIIpDbGatewayIp_Object = MibTableColumn
fsMIIpDbGatewayIp = _FsMIIpDbGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 2, 1, 3),
    _FsMIIpDbGatewayIp_Type()
)
fsMIIpDbGatewayIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbGatewayIp.setStatus("current")


class _FsMIIpDbGatewayIpMode_Type(Integer32):
    """Custom type fsMIIpDbGatewayIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("active", 0)
    )


_FsMIIpDbGatewayIpMode_Type.__name__ = "Integer32"
_FsMIIpDbGatewayIpMode_Object = MibTableColumn
fsMIIpDbGatewayIpMode = _FsMIIpDbGatewayIpMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 3, 2, 1, 4),
    _FsMIIpDbGatewayIpMode_Type()
)
fsMIIpDbGatewayIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbGatewayIpMode.setStatus("current")
_FsMIIpDbInterface_ObjectIdentity = ObjectIdentity
fsMIIpDbInterface = _FsMIIpDbInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4)
)
_FsMIIpDbInterfaceTable_Object = MibTable
fsMIIpDbInterfaceTable = _FsMIIpDbInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbInterfaceTable.setStatus("current")
_FsMIIpDbInterfaceEntry_Object = MibTableRow
fsMIIpDbInterfaceEntry = _FsMIIpDbInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1)
)
fsMIIpDbInterfaceEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbIntfContextId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbIntfVlanId"),
)
if mibBuilder.loadTexts:
    fsMIIpDbInterfaceEntry.setStatus("current")


class _FsMIIpDbIntfContextId_Type(Integer32):
    """Custom type fsMIIpDbIntfContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIIpDbIntfContextId_Type.__name__ = "Integer32"
_FsMIIpDbIntfContextId_Object = MibTableColumn
fsMIIpDbIntfContextId = _FsMIIpDbIntfContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 1),
    _FsMIIpDbIntfContextId_Type()
)
fsMIIpDbIntfContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbIntfContextId.setStatus("current")


class _FsMIIpDbIntfVlanId_Type(Integer32):
    """Custom type fsMIIpDbIntfVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIIpDbIntfVlanId_Type.__name__ = "Integer32"
_FsMIIpDbIntfVlanId_Object = MibTableColumn
fsMIIpDbIntfVlanId = _FsMIIpDbIntfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 2),
    _FsMIIpDbIntfVlanId_Type()
)
fsMIIpDbIntfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbIntfVlanId.setStatus("current")
_FsMIIpDbIntfNoOfVlanBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanBindings = _FsMIIpDbIntfNoOfVlanBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 3),
    _FsMIIpDbIntfNoOfVlanBindings_Type()
)
fsMIIpDbIntfNoOfVlanBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanBindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanStaticBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanStaticBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanStaticBindings = _FsMIIpDbIntfNoOfVlanStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 4),
    _FsMIIpDbIntfNoOfVlanStaticBindings_Type()
)
fsMIIpDbIntfNoOfVlanStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanStaticBindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanDHCPBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanDHCPBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanDHCPBindings = _FsMIIpDbIntfNoOfVlanDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 5),
    _FsMIIpDbIntfNoOfVlanDHCPBindings_Type()
)
fsMIIpDbIntfNoOfVlanDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanDHCPBindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanPPPBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanPPPBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanPPPBindings = _FsMIIpDbIntfNoOfVlanPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 6),
    _FsMIIpDbIntfNoOfVlanPPPBindings_Type()
)
fsMIIpDbIntfNoOfVlanPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanPPPBindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanDHCPv6Bindings = _FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 7),
    _FsMIIpDbIntfNoOfVlanDHCPv6Bindings_Type()
)
fsMIIpDbIntfNoOfVlanDHCPv6Bindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanDHCPv6Bindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanStaticv6Bindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanStaticv6Bindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanStaticv6Bindings = _FsMIIpDbIntfNoOfVlanStaticv6Bindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 4, 1, 1, 8),
    _FsMIIpDbIntfNoOfVlanStaticv6Bindings_Type()
)
fsMIIpDbIntfNoOfVlanStaticv6Bindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanStaticv6Bindings.setStatus("current")
_FsMIIpDbSrcGuard_ObjectIdentity = ObjectIdentity
fsMIIpDbSrcGuard = _FsMIIpDbSrcGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 5)
)
_FsMIIpDbSrcGuardConfigTable_Object = MibTable
fsMIIpDbSrcGuardConfigTable = _FsMIIpDbSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 5, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbSrcGuardConfigTable.setStatus("current")
_FsMIIpDbSrcGuardConfigEntry_Object = MibTableRow
fsMIIpDbSrcGuardConfigEntry = _FsMIIpDbSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 5, 1, 1)
)
fsMIIpDbSrcGuardConfigEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbSrcGuardIndex"),
)
if mibBuilder.loadTexts:
    fsMIIpDbSrcGuardConfigEntry.setStatus("current")
_FsMIIpDbSrcGuardIndex_Type = InterfaceIndex
_FsMIIpDbSrcGuardIndex_Object = MibTableColumn
fsMIIpDbSrcGuardIndex = _FsMIIpDbSrcGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 5, 1, 1, 1),
    _FsMIIpDbSrcGuardIndex_Type()
)
fsMIIpDbSrcGuardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbSrcGuardIndex.setStatus("current")


class _FsMIIpDbSrcGuardStatus_Type(Integer32):
    """Custom type fsMIIpDbSrcGuardStatus based on Integer32"""
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
        *(("disable", 1),
          ("ip", 2),
          ("ipMac", 3))
    )


_FsMIIpDbSrcGuardStatus_Type.__name__ = "Integer32"
_FsMIIpDbSrcGuardStatus_Object = MibTableColumn
fsMIIpDbSrcGuardStatus = _FsMIIpDbSrcGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 5, 1, 1, 2),
    _FsMIIpDbSrcGuardStatus_Type()
)
fsMIIpDbSrcGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbSrcGuardStatus.setStatus("current")


class _FsMIIpDbv6SrcGuardStatus_Type(Integer32):
    """Custom type fsMIIpDbv6SrcGuardStatus based on Integer32"""
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


_FsMIIpDbv6SrcGuardStatus_Type.__name__ = "Integer32"
_FsMIIpDbv6SrcGuardStatus_Object = MibTableColumn
fsMIIpDbv6SrcGuardStatus = _FsMIIpDbv6SrcGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 5, 1, 1, 3),
    _FsMIIpDbv6SrcGuardStatus_Type()
)
fsMIIpDbv6SrcGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6SrcGuardStatus.setStatus("current")
_FsMIIpArpInspect_ObjectIdentity = ObjectIdentity
fsMIIpArpInspect = _FsMIIpArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6)
)


class _FsMIIpArpInspectionStatus_Type(Integer32):
    """Custom type fsMIIpArpInspectionStatus based on Integer32"""
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


_FsMIIpArpInspectionStatus_Type.__name__ = "Integer32"
_FsMIIpArpInspectionStatus_Object = MibScalar
fsMIIpArpInspectionStatus = _FsMIIpArpInspectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 1),
    _FsMIIpArpInspectionStatus_Type()
)
fsMIIpArpInspectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpArpInspectionStatus.setStatus("current")


class _FsMIIpArpInsValidateOption_Type(Bits):
    """Custom type fsMIIpArpInsValidateOption based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        *(("srcmac", 1),
          ("dstmac", 2),
          ("ip", 3))
    )

_FsMIIpArpInsValidateOption_Type.__name__ = "Bits"
_FsMIIpArpInsValidateOption_Object = MibScalar
fsMIIpArpInsValidateOption = _FsMIIpArpInsValidateOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 2),
    _FsMIIpArpInsValidateOption_Type()
)
fsMIIpArpInsValidateOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpArpInsValidateOption.setStatus("current")
_FsMIIpArpInsArpPktsForwarded_Type = Counter32
_FsMIIpArpInsArpPktsForwarded_Object = MibScalar
fsMIIpArpInsArpPktsForwarded = _FsMIIpArpInsArpPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 3),
    _FsMIIpArpInsArpPktsForwarded_Type()
)
fsMIIpArpInsArpPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsArpPktsForwarded.setStatus("current")
_FsMIIpArpInsArpPktsDropped_Type = Counter32
_FsMIIpArpInsArpPktsDropped_Object = MibScalar
fsMIIpArpInsArpPktsDropped = _FsMIIpArpInsArpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 4),
    _FsMIIpArpInsArpPktsDropped_Type()
)
fsMIIpArpInsArpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsArpPktsDropped.setStatus("current")
_FsMIIpArpInsIPValidFailures_Type = Counter32
_FsMIIpArpInsIPValidFailures_Object = MibScalar
fsMIIpArpInsIPValidFailures = _FsMIIpArpInsIPValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 5),
    _FsMIIpArpInsIPValidFailures_Type()
)
fsMIIpArpInsIPValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsIPValidFailures.setStatus("current")
_FsMIIpArpInsDestMACFailures_Type = Counter32
_FsMIIpArpInsDestMACFailures_Object = MibScalar
fsMIIpArpInsDestMACFailures = _FsMIIpArpInsDestMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 6),
    _FsMIIpArpInsDestMACFailures_Type()
)
fsMIIpArpInsDestMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsDestMACFailures.setStatus("current")
_FsMIIpArpInsSrcMACFailures_Type = Counter32
_FsMIIpArpInsSrcMACFailures_Object = MibScalar
fsMIIpArpInsSrcMACFailures = _FsMIIpArpInsSrcMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 7),
    _FsMIIpArpInsSrcMACFailures_Type()
)
fsMIIpArpInsSrcMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsSrcMACFailures.setStatus("current")


class _FsMIIpArpInsGlobalStatsClear_Type(TruthValue):
    """Custom type fsMIIpArpInsGlobalStatsClear based on TruthValue"""
    defaultValue = 2


_FsMIIpArpInsGlobalStatsClear_Type.__name__ = "TruthValue"
_FsMIIpArpInsGlobalStatsClear_Object = MibScalar
fsMIIpArpInsGlobalStatsClear = _FsMIIpArpInsGlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 8),
    _FsMIIpArpInsGlobalStatsClear_Type()
)
fsMIIpArpInsGlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpArpInsGlobalStatsClear.setStatus("current")
_FsMIIpArpInsVlanTable_Object = MibTable
fsMIIpArpInsVlanTable = _FsMIIpArpInsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9)
)
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanTable.setStatus("current")
_FsMIIpArpInsVlanEntry_Object = MibTableRow
fsMIIpArpInsVlanEntry = _FsMIIpArpInsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1)
)
fsMIIpArpInsVlanEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpArpInsVlanContextId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpArpInsVlanId"),
)
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanEntry.setStatus("current")


class _FsMIIpArpInsVlanContextId_Type(Integer32):
    """Custom type fsMIIpArpInsVlanContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMIIpArpInsVlanContextId_Type.__name__ = "Integer32"
_FsMIIpArpInsVlanContextId_Object = MibTableColumn
fsMIIpArpInsVlanContextId = _FsMIIpArpInsVlanContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 1),
    _FsMIIpArpInsVlanContextId_Type()
)
fsMIIpArpInsVlanContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanContextId.setStatus("current")


class _FsMIIpArpInsVlanId_Type(Integer32):
    """Custom type fsMIIpArpInsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIIpArpInsVlanId_Type.__name__ = "Integer32"
_FsMIIpArpInsVlanId_Object = MibTableColumn
fsMIIpArpInsVlanId = _FsMIIpArpInsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 2),
    _FsMIIpArpInsVlanId_Type()
)
fsMIIpArpInsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanId.setStatus("current")


class _FsMIIpArpInsVlanStatus_Type(Integer32):
    """Custom type fsMIIpArpInsVlanStatus based on Integer32"""
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


_FsMIIpArpInsVlanStatus_Type.__name__ = "Integer32"
_FsMIIpArpInsVlanStatus_Object = MibTableColumn
fsMIIpArpInsVlanStatus = _FsMIIpArpInsVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 3),
    _FsMIIpArpInsVlanStatus_Type()
)
fsMIIpArpInsVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanStatus.setStatus("current")
_FsMIIpArpInsVlanArpPktsForwarded_Type = Integer32
_FsMIIpArpInsVlanArpPktsForwarded_Object = MibTableColumn
fsMIIpArpInsVlanArpPktsForwarded = _FsMIIpArpInsVlanArpPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 4),
    _FsMIIpArpInsVlanArpPktsForwarded_Type()
)
fsMIIpArpInsVlanArpPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanArpPktsForwarded.setStatus("current")
_FsMIIpArpInsVlanArpPktsDropped_Type = Integer32
_FsMIIpArpInsVlanArpPktsDropped_Object = MibTableColumn
fsMIIpArpInsVlanArpPktsDropped = _FsMIIpArpInsVlanArpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 5),
    _FsMIIpArpInsVlanArpPktsDropped_Type()
)
fsMIIpArpInsVlanArpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanArpPktsDropped.setStatus("current")
_FsMIIpArpInsVlanIPValidFailures_Type = Integer32
_FsMIIpArpInsVlanIPValidFailures_Object = MibTableColumn
fsMIIpArpInsVlanIPValidFailures = _FsMIIpArpInsVlanIPValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 6),
    _FsMIIpArpInsVlanIPValidFailures_Type()
)
fsMIIpArpInsVlanIPValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanIPValidFailures.setStatus("current")
_FsMIIpArpInsVlanDestMACFailures_Type = Integer32
_FsMIIpArpInsVlanDestMACFailures_Object = MibTableColumn
fsMIIpArpInsVlanDestMACFailures = _FsMIIpArpInsVlanDestMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 7),
    _FsMIIpArpInsVlanDestMACFailures_Type()
)
fsMIIpArpInsVlanDestMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanDestMACFailures.setStatus("current")
_FsMIIpArpInsVlanSrcMACFailures_Type = Integer32
_FsMIIpArpInsVlanSrcMACFailures_Object = MibTableColumn
fsMIIpArpInsVlanSrcMACFailures = _FsMIIpArpInsVlanSrcMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 8),
    _FsMIIpArpInsVlanSrcMACFailures_Type()
)
fsMIIpArpInsVlanSrcMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanSrcMACFailures.setStatus("current")


class _FsMIIpArpInsVlanClearStats_Type(TruthValue):
    """Custom type fsMIIpArpInsVlanClearStats based on TruthValue"""
    defaultValue = 2


_FsMIIpArpInsVlanClearStats_Type.__name__ = "TruthValue"
_FsMIIpArpInsVlanClearStats_Object = MibTableColumn
fsMIIpArpInsVlanClearStats = _FsMIIpArpInsVlanClearStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 9),
    _FsMIIpArpInsVlanClearStats_Type()
)
fsMIIpArpInsVlanClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanClearStats.setStatus("current")
_FsMIIpArpInsVlanRowStatus_Type = RowStatus
_FsMIIpArpInsVlanRowStatus_Object = MibTableColumn
fsMIIpArpInsVlanRowStatus = _FsMIIpArpInsVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 6, 9, 1, 10),
    _FsMIIpArpInsVlanRowStatus_Type()
)
fsMIIpArpInsVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpArpInsVlanRowStatus.setStatus("current")
_FsMIIpDbv6Static_ObjectIdentity = ObjectIdentity
fsMIIpDbv6Static = _FsMIIpDbv6Static_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7)
)
_FsMIIpDbv6StaticBindingTable_Object = MibTable
fsMIIpDbv6StaticBindingTable = _FsMIIpDbv6StaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbv6StaticBindingTable.setStatus("current")
_FsMIIpDbv6StaticBindingEntry_Object = MibTableRow
fsMIIpDbv6StaticBindingEntry = _FsMIIpDbv6StaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1, 1)
)
fsMIIpDbv6StaticBindingEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbv6ContextId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbv6StaticHostVlanId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbv6StaticHostMac"),
)
if mibBuilder.loadTexts:
    fsMIIpDbv6StaticBindingEntry.setStatus("current")


class _FsMIIpDbv6ContextId_Type(Integer32):
    """Custom type fsMIIpDbv6ContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIIpDbv6ContextId_Type.__name__ = "Integer32"
_FsMIIpDbv6ContextId_Object = MibTableColumn
fsMIIpDbv6ContextId = _FsMIIpDbv6ContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1, 1, 1),
    _FsMIIpDbv6ContextId_Type()
)
fsMIIpDbv6ContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbv6ContextId.setStatus("current")


class _FsMIIpDbv6StaticHostVlanId_Type(Integer32):
    """Custom type fsMIIpDbv6StaticHostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIIpDbv6StaticHostVlanId_Type.__name__ = "Integer32"
_FsMIIpDbv6StaticHostVlanId_Object = MibTableColumn
fsMIIpDbv6StaticHostVlanId = _FsMIIpDbv6StaticHostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1, 1, 2),
    _FsMIIpDbv6StaticHostVlanId_Type()
)
fsMIIpDbv6StaticHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbv6StaticHostVlanId.setStatus("current")
_FsMIIpDbv6StaticHostMac_Type = MacAddress
_FsMIIpDbv6StaticHostMac_Object = MibTableColumn
fsMIIpDbv6StaticHostMac = _FsMIIpDbv6StaticHostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1, 1, 3),
    _FsMIIpDbv6StaticHostMac_Type()
)
fsMIIpDbv6StaticHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbv6StaticHostMac.setStatus("current")
_FsMIIpDbv6StaticHostIp_Type = Ipv6Address
_FsMIIpDbv6StaticHostIp_Object = MibTableColumn
fsMIIpDbv6StaticHostIp = _FsMIIpDbv6StaticHostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1, 1, 4),
    _FsMIIpDbv6StaticHostIp_Type()
)
fsMIIpDbv6StaticHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6StaticHostIp.setStatus("current")
_FsMIIpDbv6StaticInIfIndex_Type = Integer32
_FsMIIpDbv6StaticInIfIndex_Object = MibTableColumn
fsMIIpDbv6StaticInIfIndex = _FsMIIpDbv6StaticInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1, 1, 5),
    _FsMIIpDbv6StaticInIfIndex_Type()
)
fsMIIpDbv6StaticInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6StaticInIfIndex.setStatus("current")
_FsMIIpDbv6StaticBindingStatus_Type = RowStatus
_FsMIIpDbv6StaticBindingStatus_Object = MibTableColumn
fsMIIpDbv6StaticBindingStatus = _FsMIIpDbv6StaticBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 7, 1, 1, 6),
    _FsMIIpDbv6StaticBindingStatus_Type()
)
fsMIIpDbv6StaticBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6StaticBindingStatus.setStatus("current")
_FsMIIpDbv6Bindings_ObjectIdentity = ObjectIdentity
fsMIIpDbv6Bindings = _FsMIIpDbv6Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8)
)
_FsMIIpDbv6BindingTable_Object = MibTable
fsMIIpDbv6BindingTable = _FsMIIpDbv6BindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbv6BindingTable.setStatus("current")
_FsMIIpDbv6BindingEntry_Object = MibTableRow
fsMIIpDbv6BindingEntry = _FsMIIpDbv6BindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1)
)
fsMIIpDbv6BindingEntry.setIndexNames(
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbv6HostContextId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbv6HostVlanId"),
    (0, "ARICENT-MIIPDB-MIB", "fsMIIpDbv6HostMac"),
)
if mibBuilder.loadTexts:
    fsMIIpDbv6BindingEntry.setStatus("current")


class _FsMIIpDbv6HostContextId_Type(Integer32):
    """Custom type fsMIIpDbv6HostContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIIpDbv6HostContextId_Type.__name__ = "Integer32"
_FsMIIpDbv6HostContextId_Object = MibTableColumn
fsMIIpDbv6HostContextId = _FsMIIpDbv6HostContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1, 1),
    _FsMIIpDbv6HostContextId_Type()
)
fsMIIpDbv6HostContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbv6HostContextId.setStatus("current")


class _FsMIIpDbv6HostVlanId_Type(Integer32):
    """Custom type fsMIIpDbv6HostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIIpDbv6HostVlanId_Type.__name__ = "Integer32"
_FsMIIpDbv6HostVlanId_Object = MibTableColumn
fsMIIpDbv6HostVlanId = _FsMIIpDbv6HostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1, 2),
    _FsMIIpDbv6HostVlanId_Type()
)
fsMIIpDbv6HostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbv6HostVlanId.setStatus("current")
_FsMIIpDbv6HostMac_Type = MacAddress
_FsMIIpDbv6HostMac_Object = MibTableColumn
fsMIIpDbv6HostMac = _FsMIIpDbv6HostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1, 3),
    _FsMIIpDbv6HostMac_Type()
)
fsMIIpDbv6HostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbv6HostMac.setStatus("current")


class _FsMIIpDbv6HostBindingType_Type(Integer32):
    """Custom type fsMIIpDbv6HostBindingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2))
    )


_FsMIIpDbv6HostBindingType_Type.__name__ = "Integer32"
_FsMIIpDbv6HostBindingType_Object = MibTableColumn
fsMIIpDbv6HostBindingType = _FsMIIpDbv6HostBindingType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1, 4),
    _FsMIIpDbv6HostBindingType_Type()
)
fsMIIpDbv6HostBindingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6HostBindingType.setStatus("current")
_FsMIIpDbv6HostIp_Type = Ipv6Address
_FsMIIpDbv6HostIp_Object = MibTableColumn
fsMIIpDbv6HostIp = _FsMIIpDbv6HostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1, 5),
    _FsMIIpDbv6HostIp_Type()
)
fsMIIpDbv6HostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6HostIp.setStatus("current")
_FsMIIpDbv6HostInIfIndex_Type = Integer32
_FsMIIpDbv6HostInIfIndex_Object = MibTableColumn
fsMIIpDbv6HostInIfIndex = _FsMIIpDbv6HostInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1, 6),
    _FsMIIpDbv6HostInIfIndex_Type()
)
fsMIIpDbv6HostInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6HostInIfIndex.setStatus("current")
_FsMIIpDbv6HostRemLeaseTime_Type = Integer32
_FsMIIpDbv6HostRemLeaseTime_Object = MibTableColumn
fsMIIpDbv6HostRemLeaseTime = _FsMIIpDbv6HostRemLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 48, 8, 1, 1, 7),
    _FsMIIpDbv6HostRemLeaseTime_Type()
)
fsMIIpDbv6HostRemLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbv6HostRemLeaseTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MIIPDB-MIB",
    **{"Ipv6Address": Ipv6Address,
       "fsMIIpdb": fsMIIpdb,
       "fsMIIpDbScalars": fsMIIpDbScalars,
       "fsMIIpDbNoOfBindings": fsMIIpDbNoOfBindings,
       "fsMIIpDbNoOfStaticBindings": fsMIIpDbNoOfStaticBindings,
       "fsMIIpDbNoOfDHCPBindings": fsMIIpDbNoOfDHCPBindings,
       "fsMIIpDbNoOfPPPBindings": fsMIIpDbNoOfPPPBindings,
       "fsMIIpDbTraceLevel": fsMIIpDbTraceLevel,
       "fsMIIpDbv6DynamicDbSaveStatus": fsMIIpDbv6DynamicDbSaveStatus,
       "fsMIIpDbClearBindingStatus": fsMIIpDbClearBindingStatus,
       "fsMIIpDbv6ClearBindingStatus": fsMIIpDbv6ClearBindingStatus,
       "fsMIIpDbStatic": fsMIIpDbStatic,
       "fsMIIpDbStaticBindingTable": fsMIIpDbStaticBindingTable,
       "fsMIIpDbStaticBindingEntry": fsMIIpDbStaticBindingEntry,
       "fsMIIpDbContextId": fsMIIpDbContextId,
       "fsMIIpDbStaticHostVlanId": fsMIIpDbStaticHostVlanId,
       "fsMIIpDbStaticHostMac": fsMIIpDbStaticHostMac,
       "fsMIIpDbStaticHostIp": fsMIIpDbStaticHostIp,
       "fsMIIpDbStaticInIfIndex": fsMIIpDbStaticInIfIndex,
       "fsMIIpDbStaticGateway": fsMIIpDbStaticGateway,
       "fsMIIpDbStaticBindingStatus": fsMIIpDbStaticBindingStatus,
       "fsMIIpDbBindings": fsMIIpDbBindings,
       "fsMIIpDbBindingTable": fsMIIpDbBindingTable,
       "fsMIIpDbBindingEntry": fsMIIpDbBindingEntry,
       "fsMIIpDbHostContextId": fsMIIpDbHostContextId,
       "fsMIIpDbHostVlanId": fsMIIpDbHostVlanId,
       "fsMIIpDbHostMac": fsMIIpDbHostMac,
       "fsMIIpDbHostBindingType": fsMIIpDbHostBindingType,
       "fsMIIpDbHostIp": fsMIIpDbHostIp,
       "fsMIIpDbHostInIfIndex": fsMIIpDbHostInIfIndex,
       "fsMIIpDbHostRemLeaseTime": fsMIIpDbHostRemLeaseTime,
       "fsMIIpDbHostBindingID": fsMIIpDbHostBindingID,
       "fsMIIpDbGatewayIpTable": fsMIIpDbGatewayIpTable,
       "fsMIIpDbGatewayIpEntry": fsMIIpDbGatewayIpEntry,
       "fsMIIpDbGatewayNetwork": fsMIIpDbGatewayNetwork,
       "fsMIIpDbGatewayNetMask": fsMIIpDbGatewayNetMask,
       "fsMIIpDbGatewayIp": fsMIIpDbGatewayIp,
       "fsMIIpDbGatewayIpMode": fsMIIpDbGatewayIpMode,
       "fsMIIpDbInterface": fsMIIpDbInterface,
       "fsMIIpDbInterfaceTable": fsMIIpDbInterfaceTable,
       "fsMIIpDbInterfaceEntry": fsMIIpDbInterfaceEntry,
       "fsMIIpDbIntfContextId": fsMIIpDbIntfContextId,
       "fsMIIpDbIntfVlanId": fsMIIpDbIntfVlanId,
       "fsMIIpDbIntfNoOfVlanBindings": fsMIIpDbIntfNoOfVlanBindings,
       "fsMIIpDbIntfNoOfVlanStaticBindings": fsMIIpDbIntfNoOfVlanStaticBindings,
       "fsMIIpDbIntfNoOfVlanDHCPBindings": fsMIIpDbIntfNoOfVlanDHCPBindings,
       "fsMIIpDbIntfNoOfVlanPPPBindings": fsMIIpDbIntfNoOfVlanPPPBindings,
       "fsMIIpDbIntfNoOfVlanDHCPv6Bindings": fsMIIpDbIntfNoOfVlanDHCPv6Bindings,
       "fsMIIpDbIntfNoOfVlanStaticv6Bindings": fsMIIpDbIntfNoOfVlanStaticv6Bindings,
       "fsMIIpDbSrcGuard": fsMIIpDbSrcGuard,
       "fsMIIpDbSrcGuardConfigTable": fsMIIpDbSrcGuardConfigTable,
       "fsMIIpDbSrcGuardConfigEntry": fsMIIpDbSrcGuardConfigEntry,
       "fsMIIpDbSrcGuardIndex": fsMIIpDbSrcGuardIndex,
       "fsMIIpDbSrcGuardStatus": fsMIIpDbSrcGuardStatus,
       "fsMIIpDbv6SrcGuardStatus": fsMIIpDbv6SrcGuardStatus,
       "fsMIIpArpInspect": fsMIIpArpInspect,
       "fsMIIpArpInspectionStatus": fsMIIpArpInspectionStatus,
       "fsMIIpArpInsValidateOption": fsMIIpArpInsValidateOption,
       "fsMIIpArpInsArpPktsForwarded": fsMIIpArpInsArpPktsForwarded,
       "fsMIIpArpInsArpPktsDropped": fsMIIpArpInsArpPktsDropped,
       "fsMIIpArpInsIPValidFailures": fsMIIpArpInsIPValidFailures,
       "fsMIIpArpInsDestMACFailures": fsMIIpArpInsDestMACFailures,
       "fsMIIpArpInsSrcMACFailures": fsMIIpArpInsSrcMACFailures,
       "fsMIIpArpInsGlobalStatsClear": fsMIIpArpInsGlobalStatsClear,
       "fsMIIpArpInsVlanTable": fsMIIpArpInsVlanTable,
       "fsMIIpArpInsVlanEntry": fsMIIpArpInsVlanEntry,
       "fsMIIpArpInsVlanContextId": fsMIIpArpInsVlanContextId,
       "fsMIIpArpInsVlanId": fsMIIpArpInsVlanId,
       "fsMIIpArpInsVlanStatus": fsMIIpArpInsVlanStatus,
       "fsMIIpArpInsVlanArpPktsForwarded": fsMIIpArpInsVlanArpPktsForwarded,
       "fsMIIpArpInsVlanArpPktsDropped": fsMIIpArpInsVlanArpPktsDropped,
       "fsMIIpArpInsVlanIPValidFailures": fsMIIpArpInsVlanIPValidFailures,
       "fsMIIpArpInsVlanDestMACFailures": fsMIIpArpInsVlanDestMACFailures,
       "fsMIIpArpInsVlanSrcMACFailures": fsMIIpArpInsVlanSrcMACFailures,
       "fsMIIpArpInsVlanClearStats": fsMIIpArpInsVlanClearStats,
       "fsMIIpArpInsVlanRowStatus": fsMIIpArpInsVlanRowStatus,
       "fsMIIpDbv6Static": fsMIIpDbv6Static,
       "fsMIIpDbv6StaticBindingTable": fsMIIpDbv6StaticBindingTable,
       "fsMIIpDbv6StaticBindingEntry": fsMIIpDbv6StaticBindingEntry,
       "fsMIIpDbv6ContextId": fsMIIpDbv6ContextId,
       "fsMIIpDbv6StaticHostVlanId": fsMIIpDbv6StaticHostVlanId,
       "fsMIIpDbv6StaticHostMac": fsMIIpDbv6StaticHostMac,
       "fsMIIpDbv6StaticHostIp": fsMIIpDbv6StaticHostIp,
       "fsMIIpDbv6StaticInIfIndex": fsMIIpDbv6StaticInIfIndex,
       "fsMIIpDbv6StaticBindingStatus": fsMIIpDbv6StaticBindingStatus,
       "fsMIIpDbv6Bindings": fsMIIpDbv6Bindings,
       "fsMIIpDbv6BindingTable": fsMIIpDbv6BindingTable,
       "fsMIIpDbv6BindingEntry": fsMIIpDbv6BindingEntry,
       "fsMIIpDbv6HostContextId": fsMIIpDbv6HostContextId,
       "fsMIIpDbv6HostVlanId": fsMIIpDbv6HostVlanId,
       "fsMIIpDbv6HostMac": fsMIIpDbv6HostMac,
       "fsMIIpDbv6HostBindingType": fsMIIpDbv6HostBindingType,
       "fsMIIpDbv6HostIp": fsMIIpDbv6HostIp,
       "fsMIIpDbv6HostInIfIndex": fsMIIpDbv6HostInIfIndex,
       "fsMIIpDbv6HostRemLeaseTime": fsMIIpDbv6HostRemLeaseTime}
)
