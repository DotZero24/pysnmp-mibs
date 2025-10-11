# SNMP MIB module (FS-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SNMP-AGENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:00 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(FSTrapType,) = mibBuilder.importSymbols(
    "FS-TC",
    "FSTrapType")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsSnmpAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5)
)
if mibBuilder.loadTexts:
    fsSnmpAgentMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Community(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



# MIB Managed Objects in the order of their OIDs

_FsSnmpAgentMIBObjects_ObjectIdentity = ObjectIdentity
fsSnmpAgentMIBObjects = _FsSnmpAgentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1)
)
_FsSnmpCommunityObjects_ObjectIdentity = ObjectIdentity
fsSnmpCommunityObjects = _FsSnmpCommunityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1)
)
_FsCommunityMaxNum_Type = Integer32
_FsCommunityMaxNum_Object = MibScalar
fsCommunityMaxNum = _FsCommunityMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 1),
    _FsCommunityMaxNum_Type()
)
fsCommunityMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCommunityMaxNum.setStatus("current")
_FsCommunityTable_Object = MibTable
fsCommunityTable = _FsCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsCommunityTable.setStatus("current")
_FsCommunityEntry_Object = MibTableRow
fsCommunityEntry = _FsCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 2, 1)
)
fsCommunityEntry.setIndexNames(
    (0, "FS-SNMP-AGENT-MIB", "fsCommunityName"),
)
if mibBuilder.loadTexts:
    fsCommunityEntry.setStatus("current")
_FsCommunityName_Type = Community
_FsCommunityName_Object = MibTableColumn
fsCommunityName = _FsCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 2, 1, 1),
    _FsCommunityName_Type()
)
fsCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCommunityName.setStatus("current")


class _FsCommunityWritable_Type(Integer32):
    """Custom type fsCommunityWritable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("readonly", 1),
          ("readwrite", 2))
    )


_FsCommunityWritable_Type.__name__ = "Integer32"
_FsCommunityWritable_Object = MibTableColumn
fsCommunityWritable = _FsCommunityWritable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 2, 1, 2),
    _FsCommunityWritable_Type()
)
fsCommunityWritable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCommunityWritable.setStatus("current")
_FsCommunityUserIpAddr_Type = IpAddress
_FsCommunityUserIpAddr_Object = MibTableColumn
fsCommunityUserIpAddr = _FsCommunityUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 2, 1, 3),
    _FsCommunityUserIpAddr_Type()
)
fsCommunityUserIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCommunityUserIpAddr.setStatus("current")
_FsCommunityEnableIpAddrAuthen_Type = EnabledStatus
_FsCommunityEnableIpAddrAuthen_Object = MibTableColumn
fsCommunityEnableIpAddrAuthen = _FsCommunityEnableIpAddrAuthen_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 2, 1, 4),
    _FsCommunityEnableIpAddrAuthen_Type()
)
fsCommunityEnableIpAddrAuthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCommunityEnableIpAddrAuthen.setStatus("current")
_FsCommunityStatus_Type = RowStatus
_FsCommunityStatus_Object = MibTableColumn
fsCommunityStatus = _FsCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 2, 1, 5),
    _FsCommunityStatus_Type()
)
fsCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsCommunityStatus.setStatus("current")
_FsReadCommunityName_Type = DisplayString
_FsReadCommunityName_Object = MibScalar
fsReadCommunityName = _FsReadCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 3),
    _FsReadCommunityName_Type()
)
fsReadCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsReadCommunityName.setStatus("current")
_FsWriteCommunityName_Type = DisplayString
_FsWriteCommunityName_Object = MibScalar
fsWriteCommunityName = _FsWriteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 1, 4),
    _FsWriteCommunityName_Type()
)
fsWriteCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWriteCommunityName.setStatus("current")
_FsSnmpTrapObjects_ObjectIdentity = ObjectIdentity
fsSnmpTrapObjects = _FsSnmpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2)
)
_FsTrapDstMaxNumber_Type = Integer32
_FsTrapDstMaxNumber_Object = MibScalar
fsTrapDstMaxNumber = _FsTrapDstMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 1),
    _FsTrapDstMaxNumber_Type()
)
fsTrapDstMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapDstMaxNumber.setStatus("current")
_FsTrapDstTable_Object = MibTable
fsTrapDstTable = _FsTrapDstTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsTrapDstTable.setStatus("current")
_FsTrapDstEntry_Object = MibTableRow
fsTrapDstEntry = _FsTrapDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 2, 1)
)
fsTrapDstEntry.setIndexNames(
    (0, "FS-SNMP-AGENT-MIB", "fsTrapDstAddr"),
)
if mibBuilder.loadTexts:
    fsTrapDstEntry.setStatus("current")
_FsTrapDstAddr_Type = IpAddress
_FsTrapDstAddr_Object = MibTableColumn
fsTrapDstAddr = _FsTrapDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 2, 1, 1),
    _FsTrapDstAddr_Type()
)
fsTrapDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapDstAddr.setStatus("current")


class _FsTrapDstCommunity_Type(Community):
    """Custom type fsTrapDstCommunity based on Community"""
    defaultValue = OctetString("public")


_FsTrapDstCommunity_Type.__name__ = "Community"
_FsTrapDstCommunity_Object = MibTableColumn
fsTrapDstCommunity = _FsTrapDstCommunity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 2, 1, 2),
    _FsTrapDstCommunity_Type()
)
fsTrapDstCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTrapDstCommunity.setStatus("current")


class _FsTrapDstSendTrapClass_Type(Integer32):
    """Custom type fsTrapDstSendTrapClass based on Integer32"""
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
        *(("snmpv1-Trap", 1),
          ("snmpv2c-Trap", 2),
          ("snmpv3-trap", 3))
    )


_FsTrapDstSendTrapClass_Type.__name__ = "Integer32"
_FsTrapDstSendTrapClass_Object = MibTableColumn
fsTrapDstSendTrapClass = _FsTrapDstSendTrapClass_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 2, 1, 3),
    _FsTrapDstSendTrapClass_Type()
)
fsTrapDstSendTrapClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTrapDstSendTrapClass.setStatus("current")
_FsTrapDstEntryStatus_Type = RowStatus
_FsTrapDstEntryStatus_Object = MibTableColumn
fsTrapDstEntryStatus = _FsTrapDstEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 2, 1, 4),
    _FsTrapDstEntryStatus_Type()
)
fsTrapDstEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTrapDstEntryStatus.setStatus("current")
_FsTrapActionTable_Object = MibTable
fsTrapActionTable = _FsTrapActionTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    fsTrapActionTable.setStatus("current")
_FsTrapActionEntry_Object = MibTableRow
fsTrapActionEntry = _FsTrapActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 3, 1)
)
fsTrapActionEntry.setIndexNames(
    (0, "FS-SNMP-AGENT-MIB", "fsTrapType"),
)
if mibBuilder.loadTexts:
    fsTrapActionEntry.setStatus("current")
_FsTrapType_Type = FSTrapType
_FsTrapType_Object = MibTableColumn
fsTrapType = _FsTrapType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 3, 1, 1),
    _FsTrapType_Type()
)
fsTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapType.setStatus("current")


class _FsTrapAction_Type(Integer32):
    """Custom type fsTrapAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("sendtrap", 2))
    )


_FsTrapAction_Type.__name__ = "Integer32"
_FsTrapAction_Object = MibTableColumn
fsTrapAction = _FsTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 3, 1, 2),
    _FsTrapAction_Type()
)
fsTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTrapAction.setStatus("current")
_FsTrapControlTable_Object = MibTable
fsTrapControlTable = _FsTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    fsTrapControlTable.setStatus("current")
_FsTrapControlEntry_Object = MibTableRow
fsTrapControlEntry = _FsTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 4, 1)
)
fsTrapControlEntry.setIndexNames(
    (0, "FS-SNMP-AGENT-MIB", "fsTrapName"),
)
if mibBuilder.loadTexts:
    fsTrapControlEntry.setStatus("current")


class _FsTrapName_Type(DisplayString):
    """Custom type fsTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FsTrapName_Type.__name__ = "DisplayString"
_FsTrapName_Object = MibTableColumn
fsTrapName = _FsTrapName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 4, 1, 1),
    _FsTrapName_Type()
)
fsTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapName.setStatus("current")


class _FsTrapDescr_Type(DisplayString):
    """Custom type fsTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FsTrapDescr_Type.__name__ = "DisplayString"
_FsTrapDescr_Object = MibTableColumn
fsTrapDescr = _FsTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 4, 1, 2),
    _FsTrapDescr_Type()
)
fsTrapDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTrapDescr.setStatus("current")


class _FsTrapOnOff_Type(Integer32):
    """Custom type fsTrapOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_FsTrapOnOff_Type.__name__ = "Integer32"
_FsTrapOnOff_Object = MibTableColumn
fsTrapOnOff = _FsTrapOnOff_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 4, 1, 3),
    _FsTrapOnOff_Type()
)
fsTrapOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTrapOnOff.setStatus("current")
_FsTrapDesTable_Object = MibTable
fsTrapDesTable = _FsTrapDesTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fsTrapDesTable.setStatus("current")
_FsTrapDesEntry_Object = MibTableRow
fsTrapDesEntry = _FsTrapDesEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 5, 1)
)
fsTrapDesEntry.setIndexNames(
    (0, "FS-SNMP-AGENT-MIB", "fsTrapDesIndex"),
)
if mibBuilder.loadTexts:
    fsTrapDesEntry.setStatus("current")
_FsTrapDesIndex_Type = Integer32
_FsTrapDesIndex_Object = MibTableColumn
fsTrapDesIndex = _FsTrapDesIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 5, 1, 1),
    _FsTrapDesIndex_Type()
)
fsTrapDesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTrapDesIndex.setStatus("current")
_FsTrapDesIPAddress_Type = TAddress
_FsTrapDesIPAddress_Object = MibTableColumn
fsTrapDesIPAddress = _FsTrapDesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 5, 1, 2),
    _FsTrapDesIPAddress_Type()
)
fsTrapDesIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTrapDesIPAddress.setStatus("current")
_FsTrapDesCommunity_Type = Community
_FsTrapDesCommunity_Object = MibTableColumn
fsTrapDesCommunity = _FsTrapDesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 5, 1, 3),
    _FsTrapDesCommunity_Type()
)
fsTrapDesCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTrapDesCommunity.setStatus("current")


class _FsTrapDesVersion_Type(Integer32):
    """Custom type fsTrapDesVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("snmpv1-Trap", 1),
          ("snmpv2c-Trap", 2),
          ("snmpv3-trap", 3))
    )


_FsTrapDesVersion_Type.__name__ = "Integer32"
_FsTrapDesVersion_Object = MibTableColumn
fsTrapDesVersion = _FsTrapDesVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 5, 1, 4),
    _FsTrapDesVersion_Type()
)
fsTrapDesVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTrapDesVersion.setStatus("current")
_FsTrapDesStatus_Type = RowStatus
_FsTrapDesStatus_Object = MibTableColumn
fsTrapDesStatus = _FsTrapDesStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 2, 5, 1, 5),
    _FsTrapDesStatus_Type()
)
fsTrapDesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsTrapDesStatus.setStatus("current")
_FsSnmpUdpPortObjects_ObjectIdentity = ObjectIdentity
fsSnmpUdpPortObjects = _FsSnmpUdpPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 3)
)
_FsSNMPGetSetPort_Type = Integer32
_FsSNMPGetSetPort_Object = MibScalar
fsSNMPGetSetPort = _FsSNMPGetSetPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 3, 1),
    _FsSNMPGetSetPort_Type()
)
fsSNMPGetSetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNMPGetSetPort.setStatus("current")
_FsSNMPTrapPort_Type = Integer32
_FsSNMPTrapPort_Object = MibScalar
fsSNMPTrapPort = _FsSNMPTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 3, 2),
    _FsSNMPTrapPort_Type()
)
fsSNMPTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSNMPTrapPort.setStatus("current")
_FsSnmpNetObjects_ObjectIdentity = ObjectIdentity
fsSnmpNetObjects = _FsSnmpNetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 4)
)
_FsSysNetID_Type = DisplayString
_FsSysNetID_Object = MibScalar
fsSysNetID = _FsSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 1, 4, 1),
    _FsSysNetID_Type()
)
fsSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSysNetID.setStatus("current")
_FsSnmpAgentMIBConformance_ObjectIdentity = ObjectIdentity
fsSnmpAgentMIBConformance = _FsSnmpAgentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 2)
)
_FsSnmpAgentMIBCompliances_ObjectIdentity = ObjectIdentity
fsSnmpAgentMIBCompliances = _FsSnmpAgentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 2, 1)
)
_FsSnmpAgentMIBGroups_ObjectIdentity = ObjectIdentity
fsSnmpAgentMIBGroups = _FsSnmpAgentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 2, 2)
)

# Managed Objects groups

fsCommunityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 2, 2, 1)
)
fsCommunityMIBGroup.setObjects(
      *(("FS-SNMP-AGENT-MIB", "fsCommunityMaxNum"),
        ("FS-SNMP-AGENT-MIB", "fsCommunityName"),
        ("FS-SNMP-AGENT-MIB", "fsCommunityWritable"),
        ("FS-SNMP-AGENT-MIB", "fsCommunityUserIpAddr"),
        ("FS-SNMP-AGENT-MIB", "fsCommunityEnableIpAddrAuthen"),
        ("FS-SNMP-AGENT-MIB", "fsCommunityStatus"),
        ("FS-SNMP-AGENT-MIB", "fsReadCommunityName"),
        ("FS-SNMP-AGENT-MIB", "fsWriteCommunityName"))
)
if mibBuilder.loadTexts:
    fsCommunityMIBGroup.setStatus("current")

fsSnmpTrapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 2, 2, 2)
)
fsSnmpTrapMIBGroup.setObjects(
      *(("FS-SNMP-AGENT-MIB", "fsTrapDstSendTrapClass"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDstMaxNumber"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDstAddr"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDstCommunity"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDstEntryStatus"),
        ("FS-SNMP-AGENT-MIB", "fsTrapType"),
        ("FS-SNMP-AGENT-MIB", "fsTrapAction"),
        ("FS-SNMP-AGENT-MIB", "fsTrapName"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDescr"),
        ("FS-SNMP-AGENT-MIB", "fsTrapOnOff"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDesIndex"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDesIPAddress"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDesCommunity"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDesVersion"),
        ("FS-SNMP-AGENT-MIB", "fsTrapDesStatus"),
        ("FS-SNMP-AGENT-MIB", "fsSysNetID"))
)
if mibBuilder.loadTexts:
    fsSnmpTrapMIBGroup.setStatus("current")

fsSnmpUdpPortMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 2, 2, 3)
)
fsSnmpUdpPortMIBGroup.setObjects(
      *(("FS-SNMP-AGENT-MIB", "fsSNMPGetSetPort"),
        ("FS-SNMP-AGENT-MIB", "fsSNMPTrapPort"))
)
if mibBuilder.loadTexts:
    fsSnmpUdpPortMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsSnmpAgentMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 5, 2, 1, 1)
)
fsSnmpAgentMIBCompliance.setObjects(
      *(("FS-SNMP-AGENT-MIB", "fsCommunityMIBGroup"),
        ("FS-SNMP-AGENT-MIB", "fsSnmpTrapMIBGroup"),
        ("FS-SNMP-AGENT-MIB", "fsSnmpUdpPortMIBGroup"))
)
if mibBuilder.loadTexts:
    fsSnmpAgentMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SNMP-AGENT-MIB",
    **{"Community": Community,
       "fsSnmpAgentMIB": fsSnmpAgentMIB,
       "fsSnmpAgentMIBObjects": fsSnmpAgentMIBObjects,
       "fsSnmpCommunityObjects": fsSnmpCommunityObjects,
       "fsCommunityMaxNum": fsCommunityMaxNum,
       "fsCommunityTable": fsCommunityTable,
       "fsCommunityEntry": fsCommunityEntry,
       "fsCommunityName": fsCommunityName,
       "fsCommunityWritable": fsCommunityWritable,
       "fsCommunityUserIpAddr": fsCommunityUserIpAddr,
       "fsCommunityEnableIpAddrAuthen": fsCommunityEnableIpAddrAuthen,
       "fsCommunityStatus": fsCommunityStatus,
       "fsReadCommunityName": fsReadCommunityName,
       "fsWriteCommunityName": fsWriteCommunityName,
       "fsSnmpTrapObjects": fsSnmpTrapObjects,
       "fsTrapDstMaxNumber": fsTrapDstMaxNumber,
       "fsTrapDstTable": fsTrapDstTable,
       "fsTrapDstEntry": fsTrapDstEntry,
       "fsTrapDstAddr": fsTrapDstAddr,
       "fsTrapDstCommunity": fsTrapDstCommunity,
       "fsTrapDstSendTrapClass": fsTrapDstSendTrapClass,
       "fsTrapDstEntryStatus": fsTrapDstEntryStatus,
       "fsTrapActionTable": fsTrapActionTable,
       "fsTrapActionEntry": fsTrapActionEntry,
       "fsTrapType": fsTrapType,
       "fsTrapAction": fsTrapAction,
       "fsTrapControlTable": fsTrapControlTable,
       "fsTrapControlEntry": fsTrapControlEntry,
       "fsTrapName": fsTrapName,
       "fsTrapDescr": fsTrapDescr,
       "fsTrapOnOff": fsTrapOnOff,
       "fsTrapDesTable": fsTrapDesTable,
       "fsTrapDesEntry": fsTrapDesEntry,
       "fsTrapDesIndex": fsTrapDesIndex,
       "fsTrapDesIPAddress": fsTrapDesIPAddress,
       "fsTrapDesCommunity": fsTrapDesCommunity,
       "fsTrapDesVersion": fsTrapDesVersion,
       "fsTrapDesStatus": fsTrapDesStatus,
       "fsSnmpUdpPortObjects": fsSnmpUdpPortObjects,
       "fsSNMPGetSetPort": fsSNMPGetSetPort,
       "fsSNMPTrapPort": fsSNMPTrapPort,
       "fsSnmpNetObjects": fsSnmpNetObjects,
       "fsSysNetID": fsSysNetID,
       "fsSnmpAgentMIBConformance": fsSnmpAgentMIBConformance,
       "fsSnmpAgentMIBCompliances": fsSnmpAgentMIBCompliances,
       "fsSnmpAgentMIBCompliance": fsSnmpAgentMIBCompliance,
       "fsSnmpAgentMIBGroups": fsSnmpAgentMIBGroups,
       "fsCommunityMIBGroup": fsCommunityMIBGroup,
       "fsSnmpTrapMIBGroup": fsSnmpTrapMIBGroup,
       "fsSnmpUdpPortMIBGroup": fsSnmpUdpPortMIBGroup}
)
