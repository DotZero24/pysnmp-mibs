# SNMP MIB module (ARICENT-IPDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-IPDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:23 2025
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

fsipdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2)
)
if mibBuilder.loadTexts:
    fsipdb.setRevisions(
        ("2012-09-05 00:00",
         "2010-05-24 00:00",
         "2010-05-17 00:00")
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

_FsIpDbScalars_ObjectIdentity = ObjectIdentity
fsIpDbScalars = _FsIpDbScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1)
)
_FsIpDbNoOfBindings_Type = Counter32
_FsIpDbNoOfBindings_Object = MibScalar
fsIpDbNoOfBindings = _FsIpDbNoOfBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 1),
    _FsIpDbNoOfBindings_Type()
)
fsIpDbNoOfBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfBindings.setStatus("current")
_FsIpDbNoOfStaticBindings_Type = Counter32
_FsIpDbNoOfStaticBindings_Object = MibScalar
fsIpDbNoOfStaticBindings = _FsIpDbNoOfStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 2),
    _FsIpDbNoOfStaticBindings_Type()
)
fsIpDbNoOfStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfStaticBindings.setStatus("current")
_FsIpDbNoOfDHCPBindings_Type = Counter32
_FsIpDbNoOfDHCPBindings_Object = MibScalar
fsIpDbNoOfDHCPBindings = _FsIpDbNoOfDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 3),
    _FsIpDbNoOfDHCPBindings_Type()
)
fsIpDbNoOfDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfDHCPBindings.setStatus("current")
_FsIpDbNoOfPPPBindings_Type = Counter32
_FsIpDbNoOfPPPBindings_Object = MibScalar
fsIpDbNoOfPPPBindings = _FsIpDbNoOfPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 4),
    _FsIpDbNoOfPPPBindings_Type()
)
fsIpDbNoOfPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfPPPBindings.setStatus("current")
_FsIpDbTraceLevel_Type = Integer32
_FsIpDbTraceLevel_Object = MibScalar
fsIpDbTraceLevel = _FsIpDbTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 5),
    _FsIpDbTraceLevel_Type()
)
fsIpDbTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbTraceLevel.setStatus("current")


class _FsIpDbv6DynamicDbSaveStatus_Type(Integer32):
    """Custom type fsIpDbv6DynamicDbSaveStatus based on Integer32"""
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


_FsIpDbv6DynamicDbSaveStatus_Type.__name__ = "Integer32"
_FsIpDbv6DynamicDbSaveStatus_Object = MibScalar
fsIpDbv6DynamicDbSaveStatus = _FsIpDbv6DynamicDbSaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 6),
    _FsIpDbv6DynamicDbSaveStatus_Type()
)
fsIpDbv6DynamicDbSaveStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6DynamicDbSaveStatus.setStatus("current")


class _FsIpDbClearBindingStatus_Type(TruthValue):
    """Custom type fsIpDbClearBindingStatus based on TruthValue"""
    defaultValue = 2


_FsIpDbClearBindingStatus_Type.__name__ = "TruthValue"
_FsIpDbClearBindingStatus_Object = MibScalar
fsIpDbClearBindingStatus = _FsIpDbClearBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 7),
    _FsIpDbClearBindingStatus_Type()
)
fsIpDbClearBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbClearBindingStatus.setStatus("current")


class _FsIpDbv6ClearBindingStatus_Type(TruthValue):
    """Custom type fsIpDbv6ClearBindingStatus based on TruthValue"""
    defaultValue = 2


_FsIpDbv6ClearBindingStatus_Type.__name__ = "TruthValue"
_FsIpDbv6ClearBindingStatus_Object = MibScalar
fsIpDbv6ClearBindingStatus = _FsIpDbv6ClearBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 1, 8),
    _FsIpDbv6ClearBindingStatus_Type()
)
fsIpDbv6ClearBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6ClearBindingStatus.setStatus("current")
_FsIpDbStatic_ObjectIdentity = ObjectIdentity
fsIpDbStatic = _FsIpDbStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2)
)
_FsIpDbStaticBindingTable_Object = MibTable
fsIpDbStaticBindingTable = _FsIpDbStaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fsIpDbStaticBindingTable.setStatus("current")
_FsIpDbStaticBindingEntry_Object = MibTableRow
fsIpDbStaticBindingEntry = _FsIpDbStaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1, 1)
)
fsIpDbStaticBindingEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpDbStaticHostVlanId"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbStaticHostMac"),
)
if mibBuilder.loadTexts:
    fsIpDbStaticBindingEntry.setStatus("current")


class _FsIpDbStaticHostVlanId_Type(Integer32):
    """Custom type fsIpDbStaticHostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsIpDbStaticHostVlanId_Type.__name__ = "Integer32"
_FsIpDbStaticHostVlanId_Object = MibTableColumn
fsIpDbStaticHostVlanId = _FsIpDbStaticHostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1, 1, 1),
    _FsIpDbStaticHostVlanId_Type()
)
fsIpDbStaticHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbStaticHostVlanId.setStatus("current")
_FsIpDbStaticHostMac_Type = MacAddress
_FsIpDbStaticHostMac_Object = MibTableColumn
fsIpDbStaticHostMac = _FsIpDbStaticHostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1, 1, 2),
    _FsIpDbStaticHostMac_Type()
)
fsIpDbStaticHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbStaticHostMac.setStatus("current")
_FsIpDbStaticHostIp_Type = IpAddress
_FsIpDbStaticHostIp_Object = MibTableColumn
fsIpDbStaticHostIp = _FsIpDbStaticHostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1, 1, 3),
    _FsIpDbStaticHostIp_Type()
)
fsIpDbStaticHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticHostIp.setStatus("current")
_FsIpDbStaticInIfIndex_Type = Integer32
_FsIpDbStaticInIfIndex_Object = MibTableColumn
fsIpDbStaticInIfIndex = _FsIpDbStaticInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1, 1, 4),
    _FsIpDbStaticInIfIndex_Type()
)
fsIpDbStaticInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticInIfIndex.setStatus("current")
_FsIpDbStaticGateway_Type = IpAddress
_FsIpDbStaticGateway_Object = MibTableColumn
fsIpDbStaticGateway = _FsIpDbStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1, 1, 5),
    _FsIpDbStaticGateway_Type()
)
fsIpDbStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticGateway.setStatus("current")
_FsIpDbStaticBindingStatus_Type = RowStatus
_FsIpDbStaticBindingStatus_Object = MibTableColumn
fsIpDbStaticBindingStatus = _FsIpDbStaticBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 2, 1, 1, 6),
    _FsIpDbStaticBindingStatus_Type()
)
fsIpDbStaticBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticBindingStatus.setStatus("current")
_FsIpDbBindings_ObjectIdentity = ObjectIdentity
fsIpDbBindings = _FsIpDbBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3)
)
_FsIpDbBindingTable_Object = MibTable
fsIpDbBindingTable = _FsIpDbBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fsIpDbBindingTable.setStatus("current")
_FsIpDbBindingEntry_Object = MibTableRow
fsIpDbBindingEntry = _FsIpDbBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1)
)
fsIpDbBindingEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpDbHostVlanId"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbHostMac"),
)
if mibBuilder.loadTexts:
    fsIpDbBindingEntry.setStatus("current")


class _FsIpDbHostVlanId_Type(Integer32):
    """Custom type fsIpDbHostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsIpDbHostVlanId_Type.__name__ = "Integer32"
_FsIpDbHostVlanId_Object = MibTableColumn
fsIpDbHostVlanId = _FsIpDbHostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1, 1),
    _FsIpDbHostVlanId_Type()
)
fsIpDbHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbHostVlanId.setStatus("current")
_FsIpDbHostMac_Type = MacAddress
_FsIpDbHostMac_Object = MibTableColumn
fsIpDbHostMac = _FsIpDbHostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1, 2),
    _FsIpDbHostMac_Type()
)
fsIpDbHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbHostMac.setStatus("current")


class _FsIpDbHostBindingType_Type(Integer32):
    """Custom type fsIpDbHostBindingType based on Integer32"""
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


_FsIpDbHostBindingType_Type.__name__ = "Integer32"
_FsIpDbHostBindingType_Object = MibTableColumn
fsIpDbHostBindingType = _FsIpDbHostBindingType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1, 3),
    _FsIpDbHostBindingType_Type()
)
fsIpDbHostBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostBindingType.setStatus("current")
_FsIpDbHostIp_Type = IpAddress
_FsIpDbHostIp_Object = MibTableColumn
fsIpDbHostIp = _FsIpDbHostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1, 4),
    _FsIpDbHostIp_Type()
)
fsIpDbHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostIp.setStatus("current")
_FsIpDbHostInIfIndex_Type = Integer32
_FsIpDbHostInIfIndex_Object = MibTableColumn
fsIpDbHostInIfIndex = _FsIpDbHostInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1, 5),
    _FsIpDbHostInIfIndex_Type()
)
fsIpDbHostInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostInIfIndex.setStatus("current")
_FsIpDbHostRemLeaseTime_Type = Integer32
_FsIpDbHostRemLeaseTime_Object = MibTableColumn
fsIpDbHostRemLeaseTime = _FsIpDbHostRemLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1, 6),
    _FsIpDbHostRemLeaseTime_Type()
)
fsIpDbHostRemLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostRemLeaseTime.setStatus("current")
_FsIpDbHostBindingID_Type = Unsigned32
_FsIpDbHostBindingID_Object = MibTableColumn
fsIpDbHostBindingID = _FsIpDbHostBindingID_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 1, 1, 7),
    _FsIpDbHostBindingID_Type()
)
fsIpDbHostBindingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostBindingID.setStatus("current")
_FsIpDbGatewayIpTable_Object = MibTable
fsIpDbGatewayIpTable = _FsIpDbGatewayIpTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fsIpDbGatewayIpTable.setStatus("current")
_FsIpDbGatewayIpEntry_Object = MibTableRow
fsIpDbGatewayIpEntry = _FsIpDbGatewayIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 2, 1)
)
fsIpDbGatewayIpEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpDbHostMac"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbHostVlanId"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbGatewayNetwork"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbGatewayNetMask"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbGatewayIp"),
)
if mibBuilder.loadTexts:
    fsIpDbGatewayIpEntry.setStatus("current")
_FsIpDbGatewayNetwork_Type = IpAddress
_FsIpDbGatewayNetwork_Object = MibTableColumn
fsIpDbGatewayNetwork = _FsIpDbGatewayNetwork_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 2, 1, 1),
    _FsIpDbGatewayNetwork_Type()
)
fsIpDbGatewayNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbGatewayNetwork.setStatus("current")
_FsIpDbGatewayNetMask_Type = IpAddress
_FsIpDbGatewayNetMask_Object = MibTableColumn
fsIpDbGatewayNetMask = _FsIpDbGatewayNetMask_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 2, 1, 2),
    _FsIpDbGatewayNetMask_Type()
)
fsIpDbGatewayNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbGatewayNetMask.setStatus("current")
_FsIpDbGatewayIp_Type = IpAddress
_FsIpDbGatewayIp_Object = MibTableColumn
fsIpDbGatewayIp = _FsIpDbGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 2, 1, 3),
    _FsIpDbGatewayIp_Type()
)
fsIpDbGatewayIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbGatewayIp.setStatus("current")


class _FsIpDbGatewayIpMode_Type(Integer32):
    """Custom type fsIpDbGatewayIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("active", 0)
    )


_FsIpDbGatewayIpMode_Type.__name__ = "Integer32"
_FsIpDbGatewayIpMode_Object = MibTableColumn
fsIpDbGatewayIpMode = _FsIpDbGatewayIpMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 3, 2, 1, 4),
    _FsIpDbGatewayIpMode_Type()
)
fsIpDbGatewayIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbGatewayIpMode.setStatus("current")
_FsIpDbInterface_ObjectIdentity = ObjectIdentity
fsIpDbInterface = _FsIpDbInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4)
)
_FsIpDbInterfaceTable_Object = MibTable
fsIpDbInterfaceTable = _FsIpDbInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fsIpDbInterfaceTable.setStatus("current")
_FsIpDbInterfaceEntry_Object = MibTableRow
fsIpDbInterfaceEntry = _FsIpDbInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1)
)
fsIpDbInterfaceEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpDbIntfVlanId"),
)
if mibBuilder.loadTexts:
    fsIpDbInterfaceEntry.setStatus("current")


class _FsIpDbIntfVlanId_Type(Integer32):
    """Custom type fsIpDbIntfVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsIpDbIntfVlanId_Type.__name__ = "Integer32"
_FsIpDbIntfVlanId_Object = MibTableColumn
fsIpDbIntfVlanId = _FsIpDbIntfVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1, 1),
    _FsIpDbIntfVlanId_Type()
)
fsIpDbIntfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbIntfVlanId.setStatus("current")
_FsIpDbIntfNoOfVlanBindings_Type = Counter32
_FsIpDbIntfNoOfVlanBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanBindings = _FsIpDbIntfNoOfVlanBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1, 2),
    _FsIpDbIntfNoOfVlanBindings_Type()
)
fsIpDbIntfNoOfVlanBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanBindings.setStatus("current")
_FsIpDbIntfNoOfVlanStaticBindings_Type = Counter32
_FsIpDbIntfNoOfVlanStaticBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanStaticBindings = _FsIpDbIntfNoOfVlanStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1, 3),
    _FsIpDbIntfNoOfVlanStaticBindings_Type()
)
fsIpDbIntfNoOfVlanStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanStaticBindings.setStatus("current")
_FsIpDbIntfNoOfVlanDHCPBindings_Type = Counter32
_FsIpDbIntfNoOfVlanDHCPBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanDHCPBindings = _FsIpDbIntfNoOfVlanDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1, 4),
    _FsIpDbIntfNoOfVlanDHCPBindings_Type()
)
fsIpDbIntfNoOfVlanDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanDHCPBindings.setStatus("current")
_FsIpDbIntfNoOfVlanPPPBindings_Type = Counter32
_FsIpDbIntfNoOfVlanPPPBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanPPPBindings = _FsIpDbIntfNoOfVlanPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1, 5),
    _FsIpDbIntfNoOfVlanPPPBindings_Type()
)
fsIpDbIntfNoOfVlanPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanPPPBindings.setStatus("current")
_FsIpDbIntfNoOfVlanDHCPv6Bindings_Type = Counter32
_FsIpDbIntfNoOfVlanDHCPv6Bindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanDHCPv6Bindings = _FsIpDbIntfNoOfVlanDHCPv6Bindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1, 6),
    _FsIpDbIntfNoOfVlanDHCPv6Bindings_Type()
)
fsIpDbIntfNoOfVlanDHCPv6Bindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanDHCPv6Bindings.setStatus("current")
_FsIpDbIntfNoOfVlanStaticv6Bindings_Type = Counter32
_FsIpDbIntfNoOfVlanStaticv6Bindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanStaticv6Bindings = _FsIpDbIntfNoOfVlanStaticv6Bindings_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 4, 1, 1, 7),
    _FsIpDbIntfNoOfVlanStaticv6Bindings_Type()
)
fsIpDbIntfNoOfVlanStaticv6Bindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanStaticv6Bindings.setStatus("current")
_FsIpDbSrcGuard_ObjectIdentity = ObjectIdentity
fsIpDbSrcGuard = _FsIpDbSrcGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 5)
)
_FsIpDbSrcGuardConfigTable_Object = MibTable
fsIpDbSrcGuardConfigTable = _FsIpDbSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    fsIpDbSrcGuardConfigTable.setStatus("current")
_FsIpDbSrcGuardConfigEntry_Object = MibTableRow
fsIpDbSrcGuardConfigEntry = _FsIpDbSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 5, 1, 1)
)
fsIpDbSrcGuardConfigEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpDbSrcGuardIndex"),
)
if mibBuilder.loadTexts:
    fsIpDbSrcGuardConfigEntry.setStatus("current")
_FsIpDbSrcGuardIndex_Type = InterfaceIndex
_FsIpDbSrcGuardIndex_Object = MibTableColumn
fsIpDbSrcGuardIndex = _FsIpDbSrcGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 5, 1, 1, 1),
    _FsIpDbSrcGuardIndex_Type()
)
fsIpDbSrcGuardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbSrcGuardIndex.setStatus("current")


class _FsIpDbSrcGuardStatus_Type(Integer32):
    """Custom type fsIpDbSrcGuardStatus based on Integer32"""
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


_FsIpDbSrcGuardStatus_Type.__name__ = "Integer32"
_FsIpDbSrcGuardStatus_Object = MibTableColumn
fsIpDbSrcGuardStatus = _FsIpDbSrcGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 5, 1, 1, 2),
    _FsIpDbSrcGuardStatus_Type()
)
fsIpDbSrcGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbSrcGuardStatus.setStatus("current")


class _FsIpDbv6SrcGuardStatus_Type(Integer32):
    """Custom type fsIpDbv6SrcGuardStatus based on Integer32"""
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


_FsIpDbv6SrcGuardStatus_Type.__name__ = "Integer32"
_FsIpDbv6SrcGuardStatus_Object = MibTableColumn
fsIpDbv6SrcGuardStatus = _FsIpDbv6SrcGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 5, 1, 1, 3),
    _FsIpDbv6SrcGuardStatus_Type()
)
fsIpDbv6SrcGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6SrcGuardStatus.setStatus("current")
_FsIpArpInspect_ObjectIdentity = ObjectIdentity
fsIpArpInspect = _FsIpArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6)
)


class _FsIpArpInspectionStatus_Type(Integer32):
    """Custom type fsIpArpInspectionStatus based on Integer32"""
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


_FsIpArpInspectionStatus_Type.__name__ = "Integer32"
_FsIpArpInspectionStatus_Object = MibScalar
fsIpArpInspectionStatus = _FsIpArpInspectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 1),
    _FsIpArpInspectionStatus_Type()
)
fsIpArpInspectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpArpInspectionStatus.setStatus("current")


class _FsIpArpInsValidateOption_Type(Bits):
    """Custom type fsIpArpInsValidateOption based on Bits"""
    defaultHexValue = ""

    namedValues = NamedValues(
        *(("srcmac", 1),
          ("dstmac", 2),
          ("ip", 3))
    )

_FsIpArpInsValidateOption_Type.__name__ = "Bits"
_FsIpArpInsValidateOption_Object = MibScalar
fsIpArpInsValidateOption = _FsIpArpInsValidateOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 2),
    _FsIpArpInsValidateOption_Type()
)
fsIpArpInsValidateOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpArpInsValidateOption.setStatus("current")
_FsIpArpInsArpPktsForwarded_Type = Counter32
_FsIpArpInsArpPktsForwarded_Object = MibScalar
fsIpArpInsArpPktsForwarded = _FsIpArpInsArpPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 3),
    _FsIpArpInsArpPktsForwarded_Type()
)
fsIpArpInsArpPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsArpPktsForwarded.setStatus("current")
_FsIpArpInsArpPktsDropped_Type = Counter32
_FsIpArpInsArpPktsDropped_Object = MibScalar
fsIpArpInsArpPktsDropped = _FsIpArpInsArpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 4),
    _FsIpArpInsArpPktsDropped_Type()
)
fsIpArpInsArpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsArpPktsDropped.setStatus("current")
_FsIpArpInsIPValidFailures_Type = Counter32
_FsIpArpInsIPValidFailures_Object = MibScalar
fsIpArpInsIPValidFailures = _FsIpArpInsIPValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 5),
    _FsIpArpInsIPValidFailures_Type()
)
fsIpArpInsIPValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsIPValidFailures.setStatus("current")
_FsIpArpInsDestMACFailures_Type = Counter32
_FsIpArpInsDestMACFailures_Object = MibScalar
fsIpArpInsDestMACFailures = _FsIpArpInsDestMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 6),
    _FsIpArpInsDestMACFailures_Type()
)
fsIpArpInsDestMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsDestMACFailures.setStatus("current")
_FsIpArpInsSrcMACFailures_Type = Counter32
_FsIpArpInsSrcMACFailures_Object = MibScalar
fsIpArpInsSrcMACFailures = _FsIpArpInsSrcMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 7),
    _FsIpArpInsSrcMACFailures_Type()
)
fsIpArpInsSrcMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsSrcMACFailures.setStatus("current")


class _FsIpArpInsGlobalStatsClear_Type(TruthValue):
    """Custom type fsIpArpInsGlobalStatsClear based on TruthValue"""
    defaultValue = 2


_FsIpArpInsGlobalStatsClear_Type.__name__ = "TruthValue"
_FsIpArpInsGlobalStatsClear_Object = MibScalar
fsIpArpInsGlobalStatsClear = _FsIpArpInsGlobalStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 8),
    _FsIpArpInsGlobalStatsClear_Type()
)
fsIpArpInsGlobalStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpArpInsGlobalStatsClear.setStatus("current")
_FsIpArpInsVlanTable_Object = MibTable
fsIpArpInsVlanTable = _FsIpArpInsVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9)
)
if mibBuilder.loadTexts:
    fsIpArpInsVlanTable.setStatus("current")
_FsIpArpInsVlanEntry_Object = MibTableRow
fsIpArpInsVlanEntry = _FsIpArpInsVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1)
)
fsIpArpInsVlanEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpArpInsVlanId"),
)
if mibBuilder.loadTexts:
    fsIpArpInsVlanEntry.setStatus("current")


class _FsIpArpInsVlanId_Type(Integer32):
    """Custom type fsIpArpInsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsIpArpInsVlanId_Type.__name__ = "Integer32"
_FsIpArpInsVlanId_Object = MibTableColumn
fsIpArpInsVlanId = _FsIpArpInsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 1),
    _FsIpArpInsVlanId_Type()
)
fsIpArpInsVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpArpInsVlanId.setStatus("current")


class _FsIpArpInsVlanStatus_Type(Integer32):
    """Custom type fsIpArpInsVlanStatus based on Integer32"""
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


_FsIpArpInsVlanStatus_Type.__name__ = "Integer32"
_FsIpArpInsVlanStatus_Object = MibTableColumn
fsIpArpInsVlanStatus = _FsIpArpInsVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 2),
    _FsIpArpInsVlanStatus_Type()
)
fsIpArpInsVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpArpInsVlanStatus.setStatus("current")
_FsIpArpInsVlanArpPktsForwarded_Type = Integer32
_FsIpArpInsVlanArpPktsForwarded_Object = MibTableColumn
fsIpArpInsVlanArpPktsForwarded = _FsIpArpInsVlanArpPktsForwarded_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 3),
    _FsIpArpInsVlanArpPktsForwarded_Type()
)
fsIpArpInsVlanArpPktsForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsVlanArpPktsForwarded.setStatus("current")
_FsIpArpInsVlanArpPktsDropped_Type = Integer32
_FsIpArpInsVlanArpPktsDropped_Object = MibTableColumn
fsIpArpInsVlanArpPktsDropped = _FsIpArpInsVlanArpPktsDropped_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 4),
    _FsIpArpInsVlanArpPktsDropped_Type()
)
fsIpArpInsVlanArpPktsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsVlanArpPktsDropped.setStatus("current")
_FsIpArpInsVlanIPValidFailures_Type = Integer32
_FsIpArpInsVlanIPValidFailures_Object = MibTableColumn
fsIpArpInsVlanIPValidFailures = _FsIpArpInsVlanIPValidFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 5),
    _FsIpArpInsVlanIPValidFailures_Type()
)
fsIpArpInsVlanIPValidFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsVlanIPValidFailures.setStatus("current")
_FsIpArpInsVlanDestMACFailures_Type = Integer32
_FsIpArpInsVlanDestMACFailures_Object = MibTableColumn
fsIpArpInsVlanDestMACFailures = _FsIpArpInsVlanDestMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 6),
    _FsIpArpInsVlanDestMACFailures_Type()
)
fsIpArpInsVlanDestMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsVlanDestMACFailures.setStatus("current")
_FsIpArpInsVlanSrcMACFailures_Type = Integer32
_FsIpArpInsVlanSrcMACFailures_Object = MibTableColumn
fsIpArpInsVlanSrcMACFailures = _FsIpArpInsVlanSrcMACFailures_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 7),
    _FsIpArpInsVlanSrcMACFailures_Type()
)
fsIpArpInsVlanSrcMACFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpArpInsVlanSrcMACFailures.setStatus("current")


class _FsIpArpInsVlanClearStats_Type(TruthValue):
    """Custom type fsIpArpInsVlanClearStats based on TruthValue"""
    defaultValue = 2


_FsIpArpInsVlanClearStats_Type.__name__ = "TruthValue"
_FsIpArpInsVlanClearStats_Object = MibTableColumn
fsIpArpInsVlanClearStats = _FsIpArpInsVlanClearStats_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 8),
    _FsIpArpInsVlanClearStats_Type()
)
fsIpArpInsVlanClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpArpInsVlanClearStats.setStatus("current")
_FsIpArpInsVlanRowStatus_Type = RowStatus
_FsIpArpInsVlanRowStatus_Object = MibTableColumn
fsIpArpInsVlanRowStatus = _FsIpArpInsVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 6, 9, 1, 9),
    _FsIpArpInsVlanRowStatus_Type()
)
fsIpArpInsVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpArpInsVlanRowStatus.setStatus("current")
_FsIpDbv6Static_ObjectIdentity = ObjectIdentity
fsIpDbv6Static = _FsIpDbv6Static_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7)
)
_FsIpDbv6StaticBindingTable_Object = MibTable
fsIpDbv6StaticBindingTable = _FsIpDbv6StaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7, 1)
)
if mibBuilder.loadTexts:
    fsIpDbv6StaticBindingTable.setStatus("current")
_FsIpDbv6StaticBindingEntry_Object = MibTableRow
fsIpDbv6StaticBindingEntry = _FsIpDbv6StaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7, 1, 1)
)
fsIpDbv6StaticBindingEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpDbv6StaticHostVlanId"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbv6StaticHostMac"),
)
if mibBuilder.loadTexts:
    fsIpDbv6StaticBindingEntry.setStatus("current")


class _FsIpDbv6StaticHostVlanId_Type(Integer32):
    """Custom type fsIpDbv6StaticHostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsIpDbv6StaticHostVlanId_Type.__name__ = "Integer32"
_FsIpDbv6StaticHostVlanId_Object = MibTableColumn
fsIpDbv6StaticHostVlanId = _FsIpDbv6StaticHostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7, 1, 1, 1),
    _FsIpDbv6StaticHostVlanId_Type()
)
fsIpDbv6StaticHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbv6StaticHostVlanId.setStatus("current")
_FsIpDbv6StaticHostMac_Type = MacAddress
_FsIpDbv6StaticHostMac_Object = MibTableColumn
fsIpDbv6StaticHostMac = _FsIpDbv6StaticHostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7, 1, 1, 2),
    _FsIpDbv6StaticHostMac_Type()
)
fsIpDbv6StaticHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbv6StaticHostMac.setStatus("current")
_FsIpDbv6StaticHostIp_Type = Ipv6Address
_FsIpDbv6StaticHostIp_Object = MibTableColumn
fsIpDbv6StaticHostIp = _FsIpDbv6StaticHostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7, 1, 1, 3),
    _FsIpDbv6StaticHostIp_Type()
)
fsIpDbv6StaticHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6StaticHostIp.setStatus("current")
_FsIpDbv6StaticInIfIndex_Type = Integer32
_FsIpDbv6StaticInIfIndex_Object = MibTableColumn
fsIpDbv6StaticInIfIndex = _FsIpDbv6StaticInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7, 1, 1, 4),
    _FsIpDbv6StaticInIfIndex_Type()
)
fsIpDbv6StaticInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6StaticInIfIndex.setStatus("current")
_FsIpDbv6StaticBindingStatus_Type = RowStatus
_FsIpDbv6StaticBindingStatus_Object = MibTableColumn
fsIpDbv6StaticBindingStatus = _FsIpDbv6StaticBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 7, 1, 1, 6),
    _FsIpDbv6StaticBindingStatus_Type()
)
fsIpDbv6StaticBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6StaticBindingStatus.setStatus("current")
_FsIpDbv6Bindings_ObjectIdentity = ObjectIdentity
fsIpDbv6Bindings = _FsIpDbv6Bindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8)
)
_FsIpDbv6BindingTable_Object = MibTable
fsIpDbv6BindingTable = _FsIpDbv6BindingTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1)
)
if mibBuilder.loadTexts:
    fsIpDbv6BindingTable.setStatus("current")
_FsIpDbv6BindingEntry_Object = MibTableRow
fsIpDbv6BindingEntry = _FsIpDbv6BindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1, 1)
)
fsIpDbv6BindingEntry.setIndexNames(
    (0, "ARICENT-IPDB-MIB", "fsIpDbv6HostVlanId"),
    (0, "ARICENT-IPDB-MIB", "fsIpDbv6HostMac"),
)
if mibBuilder.loadTexts:
    fsIpDbv6BindingEntry.setStatus("current")


class _FsIpDbv6HostVlanId_Type(Integer32):
    """Custom type fsIpDbv6HostVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsIpDbv6HostVlanId_Type.__name__ = "Integer32"
_FsIpDbv6HostVlanId_Object = MibTableColumn
fsIpDbv6HostVlanId = _FsIpDbv6HostVlanId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1, 1, 1),
    _FsIpDbv6HostVlanId_Type()
)
fsIpDbv6HostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbv6HostVlanId.setStatus("current")
_FsIpDbv6HostMac_Type = MacAddress
_FsIpDbv6HostMac_Object = MibTableColumn
fsIpDbv6HostMac = _FsIpDbv6HostMac_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1, 1, 2),
    _FsIpDbv6HostMac_Type()
)
fsIpDbv6HostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbv6HostMac.setStatus("current")


class _FsIpDbv6HostBindingType_Type(Integer32):
    """Custom type fsIpDbv6HostBindingType based on Integer32"""
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


_FsIpDbv6HostBindingType_Type.__name__ = "Integer32"
_FsIpDbv6HostBindingType_Object = MibTableColumn
fsIpDbv6HostBindingType = _FsIpDbv6HostBindingType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1, 1, 3),
    _FsIpDbv6HostBindingType_Type()
)
fsIpDbv6HostBindingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6HostBindingType.setStatus("current")
_FsIpDbv6HostIp_Type = Ipv6Address
_FsIpDbv6HostIp_Object = MibTableColumn
fsIpDbv6HostIp = _FsIpDbv6HostIp_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1, 1, 4),
    _FsIpDbv6HostIp_Type()
)
fsIpDbv6HostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6HostIp.setStatus("current")
_FsIpDbv6HostInIfIndex_Type = Integer32
_FsIpDbv6HostInIfIndex_Object = MibTableColumn
fsIpDbv6HostInIfIndex = _FsIpDbv6HostInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1, 1, 5),
    _FsIpDbv6HostInIfIndex_Type()
)
fsIpDbv6HostInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6HostInIfIndex.setStatus("current")
_FsIpDbv6HostRemLeaseTime_Type = Integer32
_FsIpDbv6HostRemLeaseTime_Object = MibTableColumn
fsIpDbv6HostRemLeaseTime = _FsIpDbv6HostRemLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 2, 8, 1, 1, 6),
    _FsIpDbv6HostRemLeaseTime_Type()
)
fsIpDbv6HostRemLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbv6HostRemLeaseTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-IPDB-MIB",
    **{"Ipv6Address": Ipv6Address,
       "fsipdb": fsipdb,
       "fsIpDbScalars": fsIpDbScalars,
       "fsIpDbNoOfBindings": fsIpDbNoOfBindings,
       "fsIpDbNoOfStaticBindings": fsIpDbNoOfStaticBindings,
       "fsIpDbNoOfDHCPBindings": fsIpDbNoOfDHCPBindings,
       "fsIpDbNoOfPPPBindings": fsIpDbNoOfPPPBindings,
       "fsIpDbTraceLevel": fsIpDbTraceLevel,
       "fsIpDbv6DynamicDbSaveStatus": fsIpDbv6DynamicDbSaveStatus,
       "fsIpDbClearBindingStatus": fsIpDbClearBindingStatus,
       "fsIpDbv6ClearBindingStatus": fsIpDbv6ClearBindingStatus,
       "fsIpDbStatic": fsIpDbStatic,
       "fsIpDbStaticBindingTable": fsIpDbStaticBindingTable,
       "fsIpDbStaticBindingEntry": fsIpDbStaticBindingEntry,
       "fsIpDbStaticHostVlanId": fsIpDbStaticHostVlanId,
       "fsIpDbStaticHostMac": fsIpDbStaticHostMac,
       "fsIpDbStaticHostIp": fsIpDbStaticHostIp,
       "fsIpDbStaticInIfIndex": fsIpDbStaticInIfIndex,
       "fsIpDbStaticGateway": fsIpDbStaticGateway,
       "fsIpDbStaticBindingStatus": fsIpDbStaticBindingStatus,
       "fsIpDbBindings": fsIpDbBindings,
       "fsIpDbBindingTable": fsIpDbBindingTable,
       "fsIpDbBindingEntry": fsIpDbBindingEntry,
       "fsIpDbHostVlanId": fsIpDbHostVlanId,
       "fsIpDbHostMac": fsIpDbHostMac,
       "fsIpDbHostBindingType": fsIpDbHostBindingType,
       "fsIpDbHostIp": fsIpDbHostIp,
       "fsIpDbHostInIfIndex": fsIpDbHostInIfIndex,
       "fsIpDbHostRemLeaseTime": fsIpDbHostRemLeaseTime,
       "fsIpDbHostBindingID": fsIpDbHostBindingID,
       "fsIpDbGatewayIpTable": fsIpDbGatewayIpTable,
       "fsIpDbGatewayIpEntry": fsIpDbGatewayIpEntry,
       "fsIpDbGatewayNetwork": fsIpDbGatewayNetwork,
       "fsIpDbGatewayNetMask": fsIpDbGatewayNetMask,
       "fsIpDbGatewayIp": fsIpDbGatewayIp,
       "fsIpDbGatewayIpMode": fsIpDbGatewayIpMode,
       "fsIpDbInterface": fsIpDbInterface,
       "fsIpDbInterfaceTable": fsIpDbInterfaceTable,
       "fsIpDbInterfaceEntry": fsIpDbInterfaceEntry,
       "fsIpDbIntfVlanId": fsIpDbIntfVlanId,
       "fsIpDbIntfNoOfVlanBindings": fsIpDbIntfNoOfVlanBindings,
       "fsIpDbIntfNoOfVlanStaticBindings": fsIpDbIntfNoOfVlanStaticBindings,
       "fsIpDbIntfNoOfVlanDHCPBindings": fsIpDbIntfNoOfVlanDHCPBindings,
       "fsIpDbIntfNoOfVlanPPPBindings": fsIpDbIntfNoOfVlanPPPBindings,
       "fsIpDbIntfNoOfVlanDHCPv6Bindings": fsIpDbIntfNoOfVlanDHCPv6Bindings,
       "fsIpDbIntfNoOfVlanStaticv6Bindings": fsIpDbIntfNoOfVlanStaticv6Bindings,
       "fsIpDbSrcGuard": fsIpDbSrcGuard,
       "fsIpDbSrcGuardConfigTable": fsIpDbSrcGuardConfigTable,
       "fsIpDbSrcGuardConfigEntry": fsIpDbSrcGuardConfigEntry,
       "fsIpDbSrcGuardIndex": fsIpDbSrcGuardIndex,
       "fsIpDbSrcGuardStatus": fsIpDbSrcGuardStatus,
       "fsIpDbv6SrcGuardStatus": fsIpDbv6SrcGuardStatus,
       "fsIpArpInspect": fsIpArpInspect,
       "fsIpArpInspectionStatus": fsIpArpInspectionStatus,
       "fsIpArpInsValidateOption": fsIpArpInsValidateOption,
       "fsIpArpInsArpPktsForwarded": fsIpArpInsArpPktsForwarded,
       "fsIpArpInsArpPktsDropped": fsIpArpInsArpPktsDropped,
       "fsIpArpInsIPValidFailures": fsIpArpInsIPValidFailures,
       "fsIpArpInsDestMACFailures": fsIpArpInsDestMACFailures,
       "fsIpArpInsSrcMACFailures": fsIpArpInsSrcMACFailures,
       "fsIpArpInsGlobalStatsClear": fsIpArpInsGlobalStatsClear,
       "fsIpArpInsVlanTable": fsIpArpInsVlanTable,
       "fsIpArpInsVlanEntry": fsIpArpInsVlanEntry,
       "fsIpArpInsVlanId": fsIpArpInsVlanId,
       "fsIpArpInsVlanStatus": fsIpArpInsVlanStatus,
       "fsIpArpInsVlanArpPktsForwarded": fsIpArpInsVlanArpPktsForwarded,
       "fsIpArpInsVlanArpPktsDropped": fsIpArpInsVlanArpPktsDropped,
       "fsIpArpInsVlanIPValidFailures": fsIpArpInsVlanIPValidFailures,
       "fsIpArpInsVlanDestMACFailures": fsIpArpInsVlanDestMACFailures,
       "fsIpArpInsVlanSrcMACFailures": fsIpArpInsVlanSrcMACFailures,
       "fsIpArpInsVlanClearStats": fsIpArpInsVlanClearStats,
       "fsIpArpInsVlanRowStatus": fsIpArpInsVlanRowStatus,
       "fsIpDbv6Static": fsIpDbv6Static,
       "fsIpDbv6StaticBindingTable": fsIpDbv6StaticBindingTable,
       "fsIpDbv6StaticBindingEntry": fsIpDbv6StaticBindingEntry,
       "fsIpDbv6StaticHostVlanId": fsIpDbv6StaticHostVlanId,
       "fsIpDbv6StaticHostMac": fsIpDbv6StaticHostMac,
       "fsIpDbv6StaticHostIp": fsIpDbv6StaticHostIp,
       "fsIpDbv6StaticInIfIndex": fsIpDbv6StaticInIfIndex,
       "fsIpDbv6StaticBindingStatus": fsIpDbv6StaticBindingStatus,
       "fsIpDbv6Bindings": fsIpDbv6Bindings,
       "fsIpDbv6BindingTable": fsIpDbv6BindingTable,
       "fsIpDbv6BindingEntry": fsIpDbv6BindingEntry,
       "fsIpDbv6HostVlanId": fsIpDbv6HostVlanId,
       "fsIpDbv6HostMac": fsIpDbv6HostMac,
       "fsIpDbv6HostBindingType": fsIpDbv6HostBindingType,
       "fsIpDbv6HostIp": fsIpDbv6HostIp,
       "fsIpDbv6HostInIfIndex": fsIpDbv6HostInIfIndex,
       "fsIpDbv6HostRemLeaseTime": fsIpDbv6HostRemLeaseTime}
)
