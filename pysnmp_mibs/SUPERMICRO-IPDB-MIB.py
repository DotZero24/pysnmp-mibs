# SNMP MIB module (SUPERMICRO-IPDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-IPDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:02:08 2025
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

fsipdb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2)
)
if mibBuilder.loadTexts:
    fsipdb.setRevisions(
        ("2012-09-05 00:00",
         "2010-05-24 00:00",
         "2010-05-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIpDbScalars_ObjectIdentity = ObjectIdentity
fsIpDbScalars = _FsIpDbScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 1)
)
_FsIpDbNoOfBindings_Type = Counter32
_FsIpDbNoOfBindings_Object = MibScalar
fsIpDbNoOfBindings = _FsIpDbNoOfBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 1, 1),
    _FsIpDbNoOfBindings_Type()
)
fsIpDbNoOfBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfBindings.setStatus("current")
_FsIpDbNoOfStaticBindings_Type = Counter32
_FsIpDbNoOfStaticBindings_Object = MibScalar
fsIpDbNoOfStaticBindings = _FsIpDbNoOfStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 1, 2),
    _FsIpDbNoOfStaticBindings_Type()
)
fsIpDbNoOfStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfStaticBindings.setStatus("current")
_FsIpDbNoOfDHCPBindings_Type = Counter32
_FsIpDbNoOfDHCPBindings_Object = MibScalar
fsIpDbNoOfDHCPBindings = _FsIpDbNoOfDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 1, 3),
    _FsIpDbNoOfDHCPBindings_Type()
)
fsIpDbNoOfDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfDHCPBindings.setStatus("current")
_FsIpDbNoOfPPPBindings_Type = Counter32
_FsIpDbNoOfPPPBindings_Object = MibScalar
fsIpDbNoOfPPPBindings = _FsIpDbNoOfPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 1, 4),
    _FsIpDbNoOfPPPBindings_Type()
)
fsIpDbNoOfPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbNoOfPPPBindings.setStatus("current")
_FsIpDbTraceLevel_Type = Integer32
_FsIpDbTraceLevel_Object = MibScalar
fsIpDbTraceLevel = _FsIpDbTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 1, 5),
    _FsIpDbTraceLevel_Type()
)
fsIpDbTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbTraceLevel.setStatus("current")
_FsIpDbStatic_ObjectIdentity = ObjectIdentity
fsIpDbStatic = _FsIpDbStatic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2)
)
_FsIpDbStaticBindingTable_Object = MibTable
fsIpDbStaticBindingTable = _FsIpDbStaticBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fsIpDbStaticBindingTable.setStatus("current")
_FsIpDbStaticBindingEntry_Object = MibTableRow
fsIpDbStaticBindingEntry = _FsIpDbStaticBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1, 1)
)
fsIpDbStaticBindingEntry.setIndexNames(
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbStaticHostVlanId"),
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbStaticHostMac"),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1, 1, 1),
    _FsIpDbStaticHostVlanId_Type()
)
fsIpDbStaticHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbStaticHostVlanId.setStatus("current")
_FsIpDbStaticHostMac_Type = MacAddress
_FsIpDbStaticHostMac_Object = MibTableColumn
fsIpDbStaticHostMac = _FsIpDbStaticHostMac_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1, 1, 2),
    _FsIpDbStaticHostMac_Type()
)
fsIpDbStaticHostMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbStaticHostMac.setStatus("current")
_FsIpDbStaticHostIp_Type = IpAddress
_FsIpDbStaticHostIp_Object = MibTableColumn
fsIpDbStaticHostIp = _FsIpDbStaticHostIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1, 1, 3),
    _FsIpDbStaticHostIp_Type()
)
fsIpDbStaticHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticHostIp.setStatus("current")
_FsIpDbStaticInIfIndex_Type = Integer32
_FsIpDbStaticInIfIndex_Object = MibTableColumn
fsIpDbStaticInIfIndex = _FsIpDbStaticInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1, 1, 4),
    _FsIpDbStaticInIfIndex_Type()
)
fsIpDbStaticInIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticInIfIndex.setStatus("current")
_FsIpDbStaticGateway_Type = IpAddress
_FsIpDbStaticGateway_Object = MibTableColumn
fsIpDbStaticGateway = _FsIpDbStaticGateway_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1, 1, 5),
    _FsIpDbStaticGateway_Type()
)
fsIpDbStaticGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticGateway.setStatus("current")
_FsIpDbStaticBindingStatus_Type = RowStatus
_FsIpDbStaticBindingStatus_Object = MibTableColumn
fsIpDbStaticBindingStatus = _FsIpDbStaticBindingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 2, 1, 1, 6),
    _FsIpDbStaticBindingStatus_Type()
)
fsIpDbStaticBindingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbStaticBindingStatus.setStatus("current")
_FsIpDbBindings_ObjectIdentity = ObjectIdentity
fsIpDbBindings = _FsIpDbBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3)
)
_FsIpDbBindingTable_Object = MibTable
fsIpDbBindingTable = _FsIpDbBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fsIpDbBindingTable.setStatus("current")
_FsIpDbBindingEntry_Object = MibTableRow
fsIpDbBindingEntry = _FsIpDbBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1)
)
fsIpDbBindingEntry.setIndexNames(
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbHostVlanId"),
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbHostMac"),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1, 1),
    _FsIpDbHostVlanId_Type()
)
fsIpDbHostVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbHostVlanId.setStatus("current")
_FsIpDbHostMac_Type = MacAddress
_FsIpDbHostMac_Object = MibTableColumn
fsIpDbHostMac = _FsIpDbHostMac_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1, 3),
    _FsIpDbHostBindingType_Type()
)
fsIpDbHostBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostBindingType.setStatus("current")
_FsIpDbHostIp_Type = IpAddress
_FsIpDbHostIp_Object = MibTableColumn
fsIpDbHostIp = _FsIpDbHostIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1, 4),
    _FsIpDbHostIp_Type()
)
fsIpDbHostIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostIp.setStatus("current")
_FsIpDbHostInIfIndex_Type = Integer32
_FsIpDbHostInIfIndex_Object = MibTableColumn
fsIpDbHostInIfIndex = _FsIpDbHostInIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1, 5),
    _FsIpDbHostInIfIndex_Type()
)
fsIpDbHostInIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostInIfIndex.setStatus("current")
_FsIpDbHostRemLeaseTime_Type = Integer32
_FsIpDbHostRemLeaseTime_Object = MibTableColumn
fsIpDbHostRemLeaseTime = _FsIpDbHostRemLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1, 6),
    _FsIpDbHostRemLeaseTime_Type()
)
fsIpDbHostRemLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostRemLeaseTime.setStatus("current")
_FsIpDbHostBindingID_Type = Unsigned32
_FsIpDbHostBindingID_Object = MibTableColumn
fsIpDbHostBindingID = _FsIpDbHostBindingID_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 1, 1, 7),
    _FsIpDbHostBindingID_Type()
)
fsIpDbHostBindingID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbHostBindingID.setStatus("current")
_FsIpDbGatewayIpTable_Object = MibTable
fsIpDbGatewayIpTable = _FsIpDbGatewayIpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fsIpDbGatewayIpTable.setStatus("current")
_FsIpDbGatewayIpEntry_Object = MibTableRow
fsIpDbGatewayIpEntry = _FsIpDbGatewayIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 2, 1)
)
fsIpDbGatewayIpEntry.setIndexNames(
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbHostMac"),
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbHostVlanId"),
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbGatewayNetwork"),
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbGatewayNetMask"),
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbGatewayIp"),
)
if mibBuilder.loadTexts:
    fsIpDbGatewayIpEntry.setStatus("current")
_FsIpDbGatewayNetwork_Type = IpAddress
_FsIpDbGatewayNetwork_Object = MibTableColumn
fsIpDbGatewayNetwork = _FsIpDbGatewayNetwork_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 2, 1, 1),
    _FsIpDbGatewayNetwork_Type()
)
fsIpDbGatewayNetwork.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbGatewayNetwork.setStatus("current")
_FsIpDbGatewayNetMask_Type = IpAddress
_FsIpDbGatewayNetMask_Object = MibTableColumn
fsIpDbGatewayNetMask = _FsIpDbGatewayNetMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 2, 1, 2),
    _FsIpDbGatewayNetMask_Type()
)
fsIpDbGatewayNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbGatewayNetMask.setStatus("current")
_FsIpDbGatewayIp_Type = IpAddress
_FsIpDbGatewayIp_Object = MibTableColumn
fsIpDbGatewayIp = _FsIpDbGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 3, 2, 1, 4),
    _FsIpDbGatewayIpMode_Type()
)
fsIpDbGatewayIpMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbGatewayIpMode.setStatus("current")
_FsIpDbInterface_ObjectIdentity = ObjectIdentity
fsIpDbInterface = _FsIpDbInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4)
)
_FsIpDbInterfaceTable_Object = MibTable
fsIpDbInterfaceTable = _FsIpDbInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fsIpDbInterfaceTable.setStatus("current")
_FsIpDbInterfaceEntry_Object = MibTableRow
fsIpDbInterfaceEntry = _FsIpDbInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4, 1, 1)
)
fsIpDbInterfaceEntry.setIndexNames(
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbIntfVlanId"),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4, 1, 1, 1),
    _FsIpDbIntfVlanId_Type()
)
fsIpDbIntfVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIpDbIntfVlanId.setStatus("current")
_FsIpDbIntfNoOfVlanBindings_Type = Counter32
_FsIpDbIntfNoOfVlanBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanBindings = _FsIpDbIntfNoOfVlanBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4, 1, 1, 2),
    _FsIpDbIntfNoOfVlanBindings_Type()
)
fsIpDbIntfNoOfVlanBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanBindings.setStatus("current")
_FsIpDbIntfNoOfVlanStaticBindings_Type = Counter32
_FsIpDbIntfNoOfVlanStaticBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanStaticBindings = _FsIpDbIntfNoOfVlanStaticBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4, 1, 1, 3),
    _FsIpDbIntfNoOfVlanStaticBindings_Type()
)
fsIpDbIntfNoOfVlanStaticBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanStaticBindings.setStatus("current")
_FsIpDbIntfNoOfVlanDHCPBindings_Type = Counter32
_FsIpDbIntfNoOfVlanDHCPBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanDHCPBindings = _FsIpDbIntfNoOfVlanDHCPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4, 1, 1, 4),
    _FsIpDbIntfNoOfVlanDHCPBindings_Type()
)
fsIpDbIntfNoOfVlanDHCPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanDHCPBindings.setStatus("current")
_FsIpDbIntfNoOfVlanPPPBindings_Type = Counter32
_FsIpDbIntfNoOfVlanPPPBindings_Object = MibTableColumn
fsIpDbIntfNoOfVlanPPPBindings = _FsIpDbIntfNoOfVlanPPPBindings_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 4, 1, 1, 5),
    _FsIpDbIntfNoOfVlanPPPBindings_Type()
)
fsIpDbIntfNoOfVlanPPPBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpDbIntfNoOfVlanPPPBindings.setStatus("current")
_FsIpDbSrcGuard_ObjectIdentity = ObjectIdentity
fsIpDbSrcGuard = _FsIpDbSrcGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 5)
)
_FsIpDbSrcGuardConfigTable_Object = MibTable
fsIpDbSrcGuardConfigTable = _FsIpDbSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 5, 1)
)
if mibBuilder.loadTexts:
    fsIpDbSrcGuardConfigTable.setStatus("current")
_FsIpDbSrcGuardConfigEntry_Object = MibTableRow
fsIpDbSrcGuardConfigEntry = _FsIpDbSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 5, 1, 1)
)
fsIpDbSrcGuardConfigEntry.setIndexNames(
    (0, "SUPERMICRO-IPDB-MIB", "fsIpDbSrcGuardIndex"),
)
if mibBuilder.loadTexts:
    fsIpDbSrcGuardConfigEntry.setStatus("current")
_FsIpDbSrcGuardIndex_Type = InterfaceIndex
_FsIpDbSrcGuardIndex_Object = MibTableColumn
fsIpDbSrcGuardIndex = _FsIpDbSrcGuardIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 5, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 2, 5, 1, 1, 2),
    _FsIpDbSrcGuardStatus_Type()
)
fsIpDbSrcGuardStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDbSrcGuardStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-IPDB-MIB",
    **{"fsipdb": fsipdb,
       "fsIpDbScalars": fsIpDbScalars,
       "fsIpDbNoOfBindings": fsIpDbNoOfBindings,
       "fsIpDbNoOfStaticBindings": fsIpDbNoOfStaticBindings,
       "fsIpDbNoOfDHCPBindings": fsIpDbNoOfDHCPBindings,
       "fsIpDbNoOfPPPBindings": fsIpDbNoOfPPPBindings,
       "fsIpDbTraceLevel": fsIpDbTraceLevel,
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
       "fsIpDbSrcGuard": fsIpDbSrcGuard,
       "fsIpDbSrcGuardConfigTable": fsIpDbSrcGuardConfigTable,
       "fsIpDbSrcGuardConfigEntry": fsIpDbSrcGuardConfigEntry,
       "fsIpDbSrcGuardIndex": fsIpDbSrcGuardIndex,
       "fsIpDbSrcGuardStatus": fsIpDbSrcGuardStatus}
)
