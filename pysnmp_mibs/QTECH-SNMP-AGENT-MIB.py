# SNMP MIB module (QTECH-SNMP-AGENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SNMP-AGENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:08 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(QtechTrapType,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "QtechTrapType")

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

qtechSnmpAgentMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5)
)
if mibBuilder.loadTexts:
    qtechSnmpAgentMIB.setRevisions(
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

_QtechSnmpAgentMIBObjects_ObjectIdentity = ObjectIdentity
qtechSnmpAgentMIBObjects = _QtechSnmpAgentMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1)
)
_QtechSnmpCommunityObjects_ObjectIdentity = ObjectIdentity
qtechSnmpCommunityObjects = _QtechSnmpCommunityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1)
)
_QtechCommunityMaxNum_Type = Integer32
_QtechCommunityMaxNum_Object = MibScalar
qtechCommunityMaxNum = _QtechCommunityMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 1),
    _QtechCommunityMaxNum_Type()
)
qtechCommunityMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCommunityMaxNum.setStatus("current")
_QtechCommunityTable_Object = MibTable
qtechCommunityTable = _QtechCommunityTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 2)
)
if mibBuilder.loadTexts:
    qtechCommunityTable.setStatus("current")
_QtechCommunityEntry_Object = MibTableRow
qtechCommunityEntry = _QtechCommunityEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 2, 1)
)
qtechCommunityEntry.setIndexNames(
    (0, "QTECH-SNMP-AGENT-MIB", "qtechCommunityName"),
)
if mibBuilder.loadTexts:
    qtechCommunityEntry.setStatus("current")
_QtechCommunityName_Type = Community
_QtechCommunityName_Object = MibTableColumn
qtechCommunityName = _QtechCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 2, 1, 1),
    _QtechCommunityName_Type()
)
qtechCommunityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechCommunityName.setStatus("current")


class _QtechCommunityWritable_Type(Integer32):
    """Custom type qtechCommunityWritable based on Integer32"""
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


_QtechCommunityWritable_Type.__name__ = "Integer32"
_QtechCommunityWritable_Object = MibTableColumn
qtechCommunityWritable = _QtechCommunityWritable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 2, 1, 2),
    _QtechCommunityWritable_Type()
)
qtechCommunityWritable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCommunityWritable.setStatus("current")
_QtechCommunityUserIpAddr_Type = IpAddress
_QtechCommunityUserIpAddr_Object = MibTableColumn
qtechCommunityUserIpAddr = _QtechCommunityUserIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 2, 1, 3),
    _QtechCommunityUserIpAddr_Type()
)
qtechCommunityUserIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCommunityUserIpAddr.setStatus("current")
_QtechCommunityEnableIpAddrAuthen_Type = EnabledStatus
_QtechCommunityEnableIpAddrAuthen_Object = MibTableColumn
qtechCommunityEnableIpAddrAuthen = _QtechCommunityEnableIpAddrAuthen_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 2, 1, 4),
    _QtechCommunityEnableIpAddrAuthen_Type()
)
qtechCommunityEnableIpAddrAuthen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCommunityEnableIpAddrAuthen.setStatus("current")
_QtechCommunityStatus_Type = RowStatus
_QtechCommunityStatus_Object = MibTableColumn
qtechCommunityStatus = _QtechCommunityStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 2, 1, 5),
    _QtechCommunityStatus_Type()
)
qtechCommunityStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechCommunityStatus.setStatus("current")
_QtechReadCommunityName_Type = DisplayString
_QtechReadCommunityName_Object = MibScalar
qtechReadCommunityName = _QtechReadCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 3),
    _QtechReadCommunityName_Type()
)
qtechReadCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechReadCommunityName.setStatus("current")
_QtechWriteCommunityName_Type = DisplayString
_QtechWriteCommunityName_Object = MibScalar
qtechWriteCommunityName = _QtechWriteCommunityName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 1, 4),
    _QtechWriteCommunityName_Type()
)
qtechWriteCommunityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWriteCommunityName.setStatus("current")
_QtechSnmpTrapObjects_ObjectIdentity = ObjectIdentity
qtechSnmpTrapObjects = _QtechSnmpTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2)
)
_QtechTrapDstMaxNumber_Type = Integer32
_QtechTrapDstMaxNumber_Object = MibScalar
qtechTrapDstMaxNumber = _QtechTrapDstMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 1),
    _QtechTrapDstMaxNumber_Type()
)
qtechTrapDstMaxNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapDstMaxNumber.setStatus("current")
_QtechTrapDstTable_Object = MibTable
qtechTrapDstTable = _QtechTrapDstTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechTrapDstTable.setStatus("current")
_QtechTrapDstEntry_Object = MibTableRow
qtechTrapDstEntry = _QtechTrapDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 2, 1)
)
qtechTrapDstEntry.setIndexNames(
    (0, "QTECH-SNMP-AGENT-MIB", "qtechTrapDstAddr"),
)
if mibBuilder.loadTexts:
    qtechTrapDstEntry.setStatus("current")
_QtechTrapDstAddr_Type = IpAddress
_QtechTrapDstAddr_Object = MibTableColumn
qtechTrapDstAddr = _QtechTrapDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 2, 1, 1),
    _QtechTrapDstAddr_Type()
)
qtechTrapDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapDstAddr.setStatus("current")


class _QtechTrapDstCommunity_Type(Community):
    """Custom type qtechTrapDstCommunity based on Community"""
    defaultValue = OctetString("public")


_QtechTrapDstCommunity_Type.__name__ = "Community"
_QtechTrapDstCommunity_Object = MibTableColumn
qtechTrapDstCommunity = _QtechTrapDstCommunity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 2, 1, 2),
    _QtechTrapDstCommunity_Type()
)
qtechTrapDstCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTrapDstCommunity.setStatus("current")


class _QtechTrapDstSendTrapClass_Type(Integer32):
    """Custom type qtechTrapDstSendTrapClass based on Integer32"""
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


_QtechTrapDstSendTrapClass_Type.__name__ = "Integer32"
_QtechTrapDstSendTrapClass_Object = MibTableColumn
qtechTrapDstSendTrapClass = _QtechTrapDstSendTrapClass_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 2, 1, 3),
    _QtechTrapDstSendTrapClass_Type()
)
qtechTrapDstSendTrapClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTrapDstSendTrapClass.setStatus("current")
_QtechTrapDstEntryStatus_Type = RowStatus
_QtechTrapDstEntryStatus_Object = MibTableColumn
qtechTrapDstEntryStatus = _QtechTrapDstEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 2, 1, 4),
    _QtechTrapDstEntryStatus_Type()
)
qtechTrapDstEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTrapDstEntryStatus.setStatus("current")
_QtechTrapActionTable_Object = MibTable
qtechTrapActionTable = _QtechTrapActionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 3)
)
if mibBuilder.loadTexts:
    qtechTrapActionTable.setStatus("current")
_QtechTrapActionEntry_Object = MibTableRow
qtechTrapActionEntry = _QtechTrapActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 3, 1)
)
qtechTrapActionEntry.setIndexNames(
    (0, "QTECH-SNMP-AGENT-MIB", "qtechTrapType"),
)
if mibBuilder.loadTexts:
    qtechTrapActionEntry.setStatus("current")
_QtechTrapType_Type = QtechTrapType
_QtechTrapType_Object = MibTableColumn
qtechTrapType = _QtechTrapType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 3, 1, 1),
    _QtechTrapType_Type()
)
qtechTrapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapType.setStatus("current")


class _QtechTrapAction_Type(Integer32):
    """Custom type qtechTrapAction based on Integer32"""
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


_QtechTrapAction_Type.__name__ = "Integer32"
_QtechTrapAction_Object = MibTableColumn
qtechTrapAction = _QtechTrapAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 3, 1, 2),
    _QtechTrapAction_Type()
)
qtechTrapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechTrapAction.setStatus("current")
_QtechTrapControlTable_Object = MibTable
qtechTrapControlTable = _QtechTrapControlTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 4)
)
if mibBuilder.loadTexts:
    qtechTrapControlTable.setStatus("current")
_QtechTrapControlEntry_Object = MibTableRow
qtechTrapControlEntry = _QtechTrapControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 4, 1)
)
qtechTrapControlEntry.setIndexNames(
    (0, "QTECH-SNMP-AGENT-MIB", "qtechTrapName"),
)
if mibBuilder.loadTexts:
    qtechTrapControlEntry.setStatus("current")


class _QtechTrapName_Type(DisplayString):
    """Custom type qtechTrapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_QtechTrapName_Type.__name__ = "DisplayString"
_QtechTrapName_Object = MibTableColumn
qtechTrapName = _QtechTrapName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 4, 1, 1),
    _QtechTrapName_Type()
)
qtechTrapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapName.setStatus("current")


class _QtechTrapDescr_Type(DisplayString):
    """Custom type qtechTrapDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_QtechTrapDescr_Type.__name__ = "DisplayString"
_QtechTrapDescr_Object = MibTableColumn
qtechTrapDescr = _QtechTrapDescr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 4, 1, 2),
    _QtechTrapDescr_Type()
)
qtechTrapDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechTrapDescr.setStatus("current")


class _QtechTrapOnOff_Type(Integer32):
    """Custom type qtechTrapOnOff based on Integer32"""
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


_QtechTrapOnOff_Type.__name__ = "Integer32"
_QtechTrapOnOff_Object = MibTableColumn
qtechTrapOnOff = _QtechTrapOnOff_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 4, 1, 3),
    _QtechTrapOnOff_Type()
)
qtechTrapOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechTrapOnOff.setStatus("current")
_QtechTrapDesTable_Object = MibTable
qtechTrapDesTable = _QtechTrapDesTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 5)
)
if mibBuilder.loadTexts:
    qtechTrapDesTable.setStatus("current")
_QtechTrapDesEntry_Object = MibTableRow
qtechTrapDesEntry = _QtechTrapDesEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 5, 1)
)
qtechTrapDesEntry.setIndexNames(
    (0, "QTECH-SNMP-AGENT-MIB", "qtechTrapDesIndex"),
)
if mibBuilder.loadTexts:
    qtechTrapDesEntry.setStatus("current")
_QtechTrapDesIndex_Type = Integer32
_QtechTrapDesIndex_Object = MibTableColumn
qtechTrapDesIndex = _QtechTrapDesIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 5, 1, 1),
    _QtechTrapDesIndex_Type()
)
qtechTrapDesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTrapDesIndex.setStatus("current")
_QtechTrapDesIPAddress_Type = TAddress
_QtechTrapDesIPAddress_Object = MibTableColumn
qtechTrapDesIPAddress = _QtechTrapDesIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 5, 1, 2),
    _QtechTrapDesIPAddress_Type()
)
qtechTrapDesIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTrapDesIPAddress.setStatus("current")
_QtechTrapDesCommunity_Type = Community
_QtechTrapDesCommunity_Object = MibTableColumn
qtechTrapDesCommunity = _QtechTrapDesCommunity_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 5, 1, 3),
    _QtechTrapDesCommunity_Type()
)
qtechTrapDesCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTrapDesCommunity.setStatus("current")


class _QtechTrapDesVersion_Type(Integer32):
    """Custom type qtechTrapDesVersion based on Integer32"""
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


_QtechTrapDesVersion_Type.__name__ = "Integer32"
_QtechTrapDesVersion_Object = MibTableColumn
qtechTrapDesVersion = _QtechTrapDesVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 5, 1, 4),
    _QtechTrapDesVersion_Type()
)
qtechTrapDesVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTrapDesVersion.setStatus("current")
_QtechTrapDesStatus_Type = RowStatus
_QtechTrapDesStatus_Object = MibTableColumn
qtechTrapDesStatus = _QtechTrapDesStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 2, 5, 1, 5),
    _QtechTrapDesStatus_Type()
)
qtechTrapDesStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechTrapDesStatus.setStatus("current")
_QtechSnmpUdpPortObjects_ObjectIdentity = ObjectIdentity
qtechSnmpUdpPortObjects = _QtechSnmpUdpPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 3)
)
_QtechSNMPGetSetPort_Type = Integer32
_QtechSNMPGetSetPort_Object = MibScalar
qtechSNMPGetSetPort = _QtechSNMPGetSetPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 3, 1),
    _QtechSNMPGetSetPort_Type()
)
qtechSNMPGetSetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNMPGetSetPort.setStatus("current")
_QtechSNMPTrapPort_Type = Integer32
_QtechSNMPTrapPort_Object = MibScalar
qtechSNMPTrapPort = _QtechSNMPTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 3, 2),
    _QtechSNMPTrapPort_Type()
)
qtechSNMPTrapPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSNMPTrapPort.setStatus("current")
_QtechSnmpNetObjects_ObjectIdentity = ObjectIdentity
qtechSnmpNetObjects = _QtechSnmpNetObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 4)
)
_QtechSysNetID_Type = DisplayString
_QtechSysNetID_Object = MibScalar
qtechSysNetID = _QtechSysNetID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 1, 4, 1),
    _QtechSysNetID_Type()
)
qtechSysNetID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechSysNetID.setStatus("current")
_QtechSnmpAgentMIBConformance_ObjectIdentity = ObjectIdentity
qtechSnmpAgentMIBConformance = _QtechSnmpAgentMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 2)
)
_QtechSnmpAgentMIBCompliances_ObjectIdentity = ObjectIdentity
qtechSnmpAgentMIBCompliances = _QtechSnmpAgentMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 2, 1)
)
_QtechSnmpAgentMIBGroups_ObjectIdentity = ObjectIdentity
qtechSnmpAgentMIBGroups = _QtechSnmpAgentMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 2, 2)
)

# Managed Objects groups

qtechCommunityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 2, 2, 1)
)
qtechCommunityMIBGroup.setObjects(
      *(("QTECH-SNMP-AGENT-MIB", "qtechCommunityMaxNum"),
        ("QTECH-SNMP-AGENT-MIB", "qtechCommunityName"),
        ("QTECH-SNMP-AGENT-MIB", "qtechCommunityWritable"),
        ("QTECH-SNMP-AGENT-MIB", "qtechCommunityUserIpAddr"),
        ("QTECH-SNMP-AGENT-MIB", "qtechCommunityEnableIpAddrAuthen"),
        ("QTECH-SNMP-AGENT-MIB", "qtechCommunityStatus"),
        ("QTECH-SNMP-AGENT-MIB", "qtechReadCommunityName"),
        ("QTECH-SNMP-AGENT-MIB", "qtechWriteCommunityName"))
)
if mibBuilder.loadTexts:
    qtechCommunityMIBGroup.setStatus("current")

qtechSnmpTrapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 2, 2, 2)
)
qtechSnmpTrapMIBGroup.setObjects(
      *(("QTECH-SNMP-AGENT-MIB", "qtechTrapDstSendTrapClass"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDstMaxNumber"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDstAddr"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDstCommunity"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDstEntryStatus"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapType"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapAction"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapName"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDescr"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapOnOff"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDesIndex"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDesIPAddress"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDesCommunity"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDesVersion"),
        ("QTECH-SNMP-AGENT-MIB", "qtechTrapDesStatus"),
        ("QTECH-SNMP-AGENT-MIB", "qtechSysNetID"))
)
if mibBuilder.loadTexts:
    qtechSnmpTrapMIBGroup.setStatus("current")

qtechSnmpUdpPortMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 2, 2, 3)
)
qtechSnmpUdpPortMIBGroup.setObjects(
      *(("QTECH-SNMP-AGENT-MIB", "qtechSNMPGetSetPort"),
        ("QTECH-SNMP-AGENT-MIB", "qtechSNMPTrapPort"))
)
if mibBuilder.loadTexts:
    qtechSnmpUdpPortMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechSnmpAgentMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 5, 2, 1, 1)
)
qtechSnmpAgentMIBCompliance.setObjects(
      *(("QTECH-SNMP-AGENT-MIB", "qtechCommunityMIBGroup"),
        ("QTECH-SNMP-AGENT-MIB", "qtechSnmpTrapMIBGroup"),
        ("QTECH-SNMP-AGENT-MIB", "qtechSnmpUdpPortMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechSnmpAgentMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SNMP-AGENT-MIB",
    **{"Community": Community,
       "qtechSnmpAgentMIB": qtechSnmpAgentMIB,
       "qtechSnmpAgentMIBObjects": qtechSnmpAgentMIBObjects,
       "qtechSnmpCommunityObjects": qtechSnmpCommunityObjects,
       "qtechCommunityMaxNum": qtechCommunityMaxNum,
       "qtechCommunityTable": qtechCommunityTable,
       "qtechCommunityEntry": qtechCommunityEntry,
       "qtechCommunityName": qtechCommunityName,
       "qtechCommunityWritable": qtechCommunityWritable,
       "qtechCommunityUserIpAddr": qtechCommunityUserIpAddr,
       "qtechCommunityEnableIpAddrAuthen": qtechCommunityEnableIpAddrAuthen,
       "qtechCommunityStatus": qtechCommunityStatus,
       "qtechReadCommunityName": qtechReadCommunityName,
       "qtechWriteCommunityName": qtechWriteCommunityName,
       "qtechSnmpTrapObjects": qtechSnmpTrapObjects,
       "qtechTrapDstMaxNumber": qtechTrapDstMaxNumber,
       "qtechTrapDstTable": qtechTrapDstTable,
       "qtechTrapDstEntry": qtechTrapDstEntry,
       "qtechTrapDstAddr": qtechTrapDstAddr,
       "qtechTrapDstCommunity": qtechTrapDstCommunity,
       "qtechTrapDstSendTrapClass": qtechTrapDstSendTrapClass,
       "qtechTrapDstEntryStatus": qtechTrapDstEntryStatus,
       "qtechTrapActionTable": qtechTrapActionTable,
       "qtechTrapActionEntry": qtechTrapActionEntry,
       "qtechTrapType": qtechTrapType,
       "qtechTrapAction": qtechTrapAction,
       "qtechTrapControlTable": qtechTrapControlTable,
       "qtechTrapControlEntry": qtechTrapControlEntry,
       "qtechTrapName": qtechTrapName,
       "qtechTrapDescr": qtechTrapDescr,
       "qtechTrapOnOff": qtechTrapOnOff,
       "qtechTrapDesTable": qtechTrapDesTable,
       "qtechTrapDesEntry": qtechTrapDesEntry,
       "qtechTrapDesIndex": qtechTrapDesIndex,
       "qtechTrapDesIPAddress": qtechTrapDesIPAddress,
       "qtechTrapDesCommunity": qtechTrapDesCommunity,
       "qtechTrapDesVersion": qtechTrapDesVersion,
       "qtechTrapDesStatus": qtechTrapDesStatus,
       "qtechSnmpUdpPortObjects": qtechSnmpUdpPortObjects,
       "qtechSNMPGetSetPort": qtechSNMPGetSetPort,
       "qtechSNMPTrapPort": qtechSNMPTrapPort,
       "qtechSnmpNetObjects": qtechSnmpNetObjects,
       "qtechSysNetID": qtechSysNetID,
       "qtechSnmpAgentMIBConformance": qtechSnmpAgentMIBConformance,
       "qtechSnmpAgentMIBCompliances": qtechSnmpAgentMIBCompliances,
       "qtechSnmpAgentMIBCompliance": qtechSnmpAgentMIBCompliance,
       "qtechSnmpAgentMIBGroups": qtechSnmpAgentMIBGroups,
       "qtechCommunityMIBGroup": qtechCommunityMIBGroup,
       "qtechSnmpTrapMIBGroup": qtechSnmpTrapMIBGroup,
       "qtechSnmpUdpPortMIBGroup": qtechSnmpUdpPortMIBGroup}
)
