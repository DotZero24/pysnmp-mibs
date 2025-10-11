# SNMP MIB module (SUPERMICRO-MIIPDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIIPDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:55 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsMIIpdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48)
)
if mibBuilder.loadTexts:
    fsMIIpdb.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIIpDbScalars_ObjectIdentity = ObjectIdentity
fsMIIpDbScalars = _FsMIIpDbScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 1)
)
_FsMIIpDbNoOfBindings_Type = Counter32
_FsMIIpDbNoOfBindings_Object = MibScalar
fsMIIpDbNoOfBindings = _FsMIIpDbNoOfBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 1, 1),
    _FsMIIpDbNoOfBindings_Type()
)
fsMIIpDbNoOfBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfBindings.setStatus("current")
_FsMIIpDbNoOfStaticBindings_Type = Counter32
_FsMIIpDbNoOfStaticBindings_Object = MibScalar
fsMIIpDbNoOfStaticBindings = _FsMIIpDbNoOfStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 1, 2),
    _FsMIIpDbNoOfStaticBindings_Type()
)
fsMIIpDbNoOfStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfStaticBindings.setStatus("current")
_FsMIIpDbNoOfDHCPBindings_Type = Counter32
_FsMIIpDbNoOfDHCPBindings_Object = MibScalar
fsMIIpDbNoOfDHCPBindings = _FsMIIpDbNoOfDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 1, 3),
    _FsMIIpDbNoOfDHCPBindings_Type()
)
fsMIIpDbNoOfDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfDHCPBindings.setStatus("current")
_FsMIIpDbNoOfPPPBindings_Type = Counter32
_FsMIIpDbNoOfPPPBindings_Object = MibScalar
fsMIIpDbNoOfPPPBindings = _FsMIIpDbNoOfPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 1, 4),
    _FsMIIpDbNoOfPPPBindings_Type()
)
fsMIIpDbNoOfPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbNoOfPPPBindings.setStatus("current")
_FsMIIpDbTraceLevel_Type = Integer32
_FsMIIpDbTraceLevel_Object = MibScalar
fsMIIpDbTraceLevel = _FsMIIpDbTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 1, 5),
    _FsMIIpDbTraceLevel_Type()
)
fsMIIpDbTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbTraceLevel.setStatus("current")
_FsMIIpDbStatic_ObjectIdentity = ObjectIdentity
fsMIIpDbStatic = _FsMIIpDbStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2)
)
_FsMIIpDbStaticBindingTable_Object = MibTable
fsMIIpDbStaticBindingTable = _FsMIIpDbStaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbStaticBindingTable.setStatus("current")
_FsMIIpDbStaticBindingEntry_Object = MibTableRow
fsMIIpDbStaticBindingEntry = _FsMIIpDbStaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1)
)
fsMIIpDbStaticBindingEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbContextId"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbStaticHostVlanId"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbStaticHostMac"),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1, 2),
    _FsMIIpDbStaticHostVlanId_Type()
)
fsMIIpDbStaticHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbStaticHostVlanId.setStatus("current")
_FsMIIpDbStaticHostMac_Type = MacAddress
_FsMIIpDbStaticHostMac_Object = MibTableColumn
fsMIIpDbStaticHostMac = _FsMIIpDbStaticHostMac_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1, 3),
    _FsMIIpDbStaticHostMac_Type()
)
fsMIIpDbStaticHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbStaticHostMac.setStatus("current")
_FsMIIpDbStaticHostIp_Type = IpAddress
_FsMIIpDbStaticHostIp_Object = MibTableColumn
fsMIIpDbStaticHostIp = _FsMIIpDbStaticHostIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1, 4),
    _FsMIIpDbStaticHostIp_Type()
)
fsMIIpDbStaticHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticHostIp.setStatus("current")
_FsMIIpDbStaticInIfIndex_Type = Integer32
_FsMIIpDbStaticInIfIndex_Object = MibTableColumn
fsMIIpDbStaticInIfIndex = _FsMIIpDbStaticInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1, 5),
    _FsMIIpDbStaticInIfIndex_Type()
)
fsMIIpDbStaticInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticInIfIndex.setStatus("current")
_FsMIIpDbStaticGateway_Type = IpAddress
_FsMIIpDbStaticGateway_Object = MibTableColumn
fsMIIpDbStaticGateway = _FsMIIpDbStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1, 6),
    _FsMIIpDbStaticGateway_Type()
)
fsMIIpDbStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticGateway.setStatus("current")
_FsMIIpDbStaticBindingStatus_Type = RowStatus
_FsMIIpDbStaticBindingStatus_Object = MibTableColumn
fsMIIpDbStaticBindingStatus = _FsMIIpDbStaticBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 2, 1, 1, 7),
    _FsMIIpDbStaticBindingStatus_Type()
)
fsMIIpDbStaticBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbStaticBindingStatus.setStatus("current")
_FsMIIpDbBindings_ObjectIdentity = ObjectIdentity
fsMIIpDbBindings = _FsMIIpDbBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3)
)
_FsMIIpDbBindingTable_Object = MibTable
fsMIIpDbBindingTable = _FsMIIpDbBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbBindingTable.setStatus("current")
_FsMIIpDbBindingEntry_Object = MibTableRow
fsMIIpDbBindingEntry = _FsMIIpDbBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1)
)
fsMIIpDbBindingEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbHostContextId"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbHostVlanId"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbHostMac"),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 2),
    _FsMIIpDbHostVlanId_Type()
)
fsMIIpDbHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbHostVlanId.setStatus("current")
_FsMIIpDbHostMac_Type = MacAddress
_FsMIIpDbHostMac_Object = MibTableColumn
fsMIIpDbHostMac = _FsMIIpDbHostMac_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 4),
    _FsMIIpDbHostBindingType_Type()
)
fsMIIpDbHostBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostBindingType.setStatus("current")
_FsMIIpDbHostIp_Type = IpAddress
_FsMIIpDbHostIp_Object = MibTableColumn
fsMIIpDbHostIp = _FsMIIpDbHostIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 5),
    _FsMIIpDbHostIp_Type()
)
fsMIIpDbHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostIp.setStatus("current")
_FsMIIpDbHostInIfIndex_Type = Integer32
_FsMIIpDbHostInIfIndex_Object = MibTableColumn
fsMIIpDbHostInIfIndex = _FsMIIpDbHostInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 6),
    _FsMIIpDbHostInIfIndex_Type()
)
fsMIIpDbHostInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostInIfIndex.setStatus("current")
_FsMIIpDbHostRemLeaseTime_Type = Integer32
_FsMIIpDbHostRemLeaseTime_Object = MibTableColumn
fsMIIpDbHostRemLeaseTime = _FsMIIpDbHostRemLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 7),
    _FsMIIpDbHostRemLeaseTime_Type()
)
fsMIIpDbHostRemLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostRemLeaseTime.setStatus("current")
_FsMIIpDbHostBindingID_Type = Unsigned32
_FsMIIpDbHostBindingID_Object = MibTableColumn
fsMIIpDbHostBindingID = _FsMIIpDbHostBindingID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 1, 1, 8),
    _FsMIIpDbHostBindingID_Type()
)
fsMIIpDbHostBindingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbHostBindingID.setStatus("current")
_FsMIIpDbGatewayIpTable_Object = MibTable
fsMIIpDbGatewayIpTable = _FsMIIpDbGatewayIpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 2)
)
if mibBuilder.loadTexts:
    fsMIIpDbGatewayIpTable.setStatus("current")
_FsMIIpDbGatewayIpEntry_Object = MibTableRow
fsMIIpDbGatewayIpEntry = _FsMIIpDbGatewayIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 2, 1)
)
fsMIIpDbGatewayIpEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbHostContextId"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbHostMac"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbHostVlanId"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbGatewayNetwork"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbGatewayNetMask"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbGatewayIp"),
)
if mibBuilder.loadTexts:
    fsMIIpDbGatewayIpEntry.setStatus("current")
_FsMIIpDbGatewayNetwork_Type = IpAddress
_FsMIIpDbGatewayNetwork_Object = MibTableColumn
fsMIIpDbGatewayNetwork = _FsMIIpDbGatewayNetwork_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 2, 1, 1),
    _FsMIIpDbGatewayNetwork_Type()
)
fsMIIpDbGatewayNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbGatewayNetwork.setStatus("current")
_FsMIIpDbGatewayNetMask_Type = IpAddress
_FsMIIpDbGatewayNetMask_Object = MibTableColumn
fsMIIpDbGatewayNetMask = _FsMIIpDbGatewayNetMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 2, 1, 2),
    _FsMIIpDbGatewayNetMask_Type()
)
fsMIIpDbGatewayNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbGatewayNetMask.setStatus("current")
_FsMIIpDbGatewayIp_Type = IpAddress
_FsMIIpDbGatewayIp_Object = MibTableColumn
fsMIIpDbGatewayIp = _FsMIIpDbGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 3, 2, 1, 4),
    _FsMIIpDbGatewayIpMode_Type()
)
fsMIIpDbGatewayIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbGatewayIpMode.setStatus("current")
_FsMIIpDbInterface_ObjectIdentity = ObjectIdentity
fsMIIpDbInterface = _FsMIIpDbInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4)
)
_FsMIIpDbInterfaceTable_Object = MibTable
fsMIIpDbInterfaceTable = _FsMIIpDbInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbInterfaceTable.setStatus("current")
_FsMIIpDbInterfaceEntry_Object = MibTableRow
fsMIIpDbInterfaceEntry = _FsMIIpDbInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1, 1)
)
fsMIIpDbInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbIntfContextId"),
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbIntfVlanId"),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1, 1, 2),
    _FsMIIpDbIntfVlanId_Type()
)
fsMIIpDbIntfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIIpDbIntfVlanId.setStatus("current")
_FsMIIpDbIntfNoOfVlanBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanBindings = _FsMIIpDbIntfNoOfVlanBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1, 1, 3),
    _FsMIIpDbIntfNoOfVlanBindings_Type()
)
fsMIIpDbIntfNoOfVlanBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanBindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanStaticBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanStaticBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanStaticBindings = _FsMIIpDbIntfNoOfVlanStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1, 1, 4),
    _FsMIIpDbIntfNoOfVlanStaticBindings_Type()
)
fsMIIpDbIntfNoOfVlanStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanStaticBindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanDHCPBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanDHCPBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanDHCPBindings = _FsMIIpDbIntfNoOfVlanDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1, 1, 5),
    _FsMIIpDbIntfNoOfVlanDHCPBindings_Type()
)
fsMIIpDbIntfNoOfVlanDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanDHCPBindings.setStatus("current")
_FsMIIpDbIntfNoOfVlanPPPBindings_Type = Counter32
_FsMIIpDbIntfNoOfVlanPPPBindings_Object = MibTableColumn
fsMIIpDbIntfNoOfVlanPPPBindings = _FsMIIpDbIntfNoOfVlanPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 4, 1, 1, 6),
    _FsMIIpDbIntfNoOfVlanPPPBindings_Type()
)
fsMIIpDbIntfNoOfVlanPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIIpDbIntfNoOfVlanPPPBindings.setStatus("current")
_FsMIIpDbSrcGuard_ObjectIdentity = ObjectIdentity
fsMIIpDbSrcGuard = _FsMIIpDbSrcGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 5)
)
_FsMIIpDbSrcGuardConfigTable_Object = MibTable
fsMIIpDbSrcGuardConfigTable = _FsMIIpDbSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 5, 1)
)
if mibBuilder.loadTexts:
    fsMIIpDbSrcGuardConfigTable.setStatus("current")
_FsMIIpDbSrcGuardConfigEntry_Object = MibTableRow
fsMIIpDbSrcGuardConfigEntry = _FsMIIpDbSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 5, 1, 1)
)
fsMIIpDbSrcGuardConfigEntry.setIndexNames(
    (0, "SUPERMICRO-MIIPDB-MIB", "fsMIIpDbSrcGuardIndex"),
)
if mibBuilder.loadTexts:
    fsMIIpDbSrcGuardConfigEntry.setStatus("current")
_FsMIIpDbSrcGuardIndex_Type = InterfaceIndex
_FsMIIpDbSrcGuardIndex_Object = MibTableColumn
fsMIIpDbSrcGuardIndex = _FsMIIpDbSrcGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 48, 5, 1, 1, 2),
    _FsMIIpDbSrcGuardStatus_Type()
)
fsMIIpDbSrcGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIIpDbSrcGuardStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIIPDB-MIB",
    **{"fsMIIpdb": fsMIIpdb,
       "fsMIIpDbScalars": fsMIIpDbScalars,
       "fsMIIpDbNoOfBindings": fsMIIpDbNoOfBindings,
       "fsMIIpDbNoOfStaticBindings": fsMIIpDbNoOfStaticBindings,
       "fsMIIpDbNoOfDHCPBindings": fsMIIpDbNoOfDHCPBindings,
       "fsMIIpDbNoOfPPPBindings": fsMIIpDbNoOfPPPBindings,
       "fsMIIpDbTraceLevel": fsMIIpDbTraceLevel,
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
       "fsMIIpDbSrcGuard": fsMIIpDbSrcGuard,
       "fsMIIpDbSrcGuardConfigTable": fsMIIpDbSrcGuardConfigTable,
       "fsMIIpDbSrcGuardConfigEntry": fsMIIpDbSrcGuardConfigEntry,
       "fsMIIpDbSrcGuardIndex": fsMIIpDbSrcGuardIndex,
       "fsMIIpDbSrcGuardStatus": fsMIIpDbSrcGuardStatus}
)
