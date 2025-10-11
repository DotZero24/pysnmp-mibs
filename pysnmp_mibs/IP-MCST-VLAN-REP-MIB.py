# SNMP MIB module (IP-MCST-VLAN-REP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/IP-MCST-VLAN-REP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:37 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swIpMcstVlanRepMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 71)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )





class VlanId(Integer32):
    """Custom type VlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwIpMcstVlanRepCtrl_ObjectIdentity = ObjectIdentity
swIpMcstVlanRepCtrl = _SwIpMcstVlanRepCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 1)
)


class _SwIpMcstVlanRepState_Type(Integer32):
    """Custom type swIpMcstVlanRepState based on Integer32"""
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


_SwIpMcstVlanRepState_Type.__name__ = "Integer32"
_SwIpMcstVlanRepState_Object = MibScalar
swIpMcstVlanRepState = _SwIpMcstVlanRepState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 1, 1),
    _SwIpMcstVlanRepState_Type()
)
swIpMcstVlanRepState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMcstVlanRepState.setStatus("current")
_SwIpMcstVlanRepInfo_ObjectIdentity = ObjectIdentity
swIpMcstVlanRepInfo = _SwIpMcstVlanRepInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2)
)
_SwIpMcastVlanRepInfoTable_Object = MibTable
swIpMcastVlanRepInfoTable = _SwIpMcastVlanRepInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2, 1)
)
if mibBuilder.loadTexts:
    swIpMcastVlanRepInfoTable.setStatus("current")
_SwIpMcastVlanRepInfoEntry_Object = MibTableRow
swIpMcastVlanRepInfoEntry = _SwIpMcastVlanRepInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2, 1, 1)
)
swIpMcastVlanRepInfoEntry.setIndexNames(
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepName"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepGroupAddrType"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepGroupAddr"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepSourceAddrType"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepSourceAddr"),
)
if mibBuilder.loadTexts:
    swIpMcastVlanRepInfoEntry.setStatus("current")
_SwIpMcstVlanRepGroupAddrType_Type = InetAddressType
_SwIpMcstVlanRepGroupAddrType_Object = MibTableColumn
swIpMcstVlanRepGroupAddrType = _SwIpMcstVlanRepGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2, 1, 1, 1),
    _SwIpMcstVlanRepGroupAddrType_Type()
)
swIpMcstVlanRepGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIpMcstVlanRepGroupAddrType.setStatus("current")
_SwIpMcstVlanRepGroupAddr_Type = InetAddress
_SwIpMcstVlanRepGroupAddr_Object = MibTableColumn
swIpMcstVlanRepGroupAddr = _SwIpMcstVlanRepGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2, 1, 1, 2),
    _SwIpMcstVlanRepGroupAddr_Type()
)
swIpMcstVlanRepGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIpMcstVlanRepGroupAddr.setStatus("current")
_SwIpMcstVlanRepSourceAddrType_Type = InetAddressType
_SwIpMcstVlanRepSourceAddrType_Object = MibTableColumn
swIpMcstVlanRepSourceAddrType = _SwIpMcstVlanRepSourceAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2, 1, 1, 3),
    _SwIpMcstVlanRepSourceAddrType_Type()
)
swIpMcstVlanRepSourceAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIpMcstVlanRepSourceAddrType.setStatus("current")
_SwIpMcstVlanRepSourceAddr_Type = InetAddress
_SwIpMcstVlanRepSourceAddr_Object = MibTableColumn
swIpMcstVlanRepSourceAddr = _SwIpMcstVlanRepSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2, 1, 1, 4),
    _SwIpMcstVlanRepSourceAddr_Type()
)
swIpMcstVlanRepSourceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swIpMcstVlanRepSourceAddr.setStatus("current")


class _SwIpMcstVlanRepStatus_Type(Integer32):
    """Custom type swIpMcstVlanRepStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_SwIpMcstVlanRepStatus_Type.__name__ = "Integer32"
_SwIpMcstVlanRepStatus_Object = MibTableColumn
swIpMcstVlanRepStatus = _SwIpMcstVlanRepStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 2, 1, 1, 5),
    _SwIpMcstVlanRepStatus_Type()
)
swIpMcstVlanRepStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepStatus.setStatus("current")
_SwIpMcstVlanRepMgmt_ObjectIdentity = ObjectIdentity
swIpMcstVlanRepMgmt = _SwIpMcstVlanRepMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3)
)


class _SwIpMcstVlanRepTTLStatus_Type(Integer32):
    """Custom type swIpMcstVlanRepTTLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decrease", 1),
          ("nodecrease", 2))
    )


_SwIpMcstVlanRepTTLStatus_Type.__name__ = "Integer32"
_SwIpMcstVlanRepTTLStatus_Object = MibScalar
swIpMcstVlanRepTTLStatus = _SwIpMcstVlanRepTTLStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 1),
    _SwIpMcstVlanRepTTLStatus_Type()
)
swIpMcstVlanRepTTLStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMcstVlanRepTTLStatus.setStatus("current")


class _SwIpMcstVlanRepSrcMacStatus_Type(Integer32):
    """Custom type swIpMcstVlanRepSrcMacStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 1),
          ("noreplace", 2))
    )


_SwIpMcstVlanRepSrcMacStatus_Type.__name__ = "Integer32"
_SwIpMcstVlanRepSrcMacStatus_Object = MibScalar
swIpMcstVlanRepSrcMacStatus = _SwIpMcstVlanRepSrcMacStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 2),
    _SwIpMcstVlanRepSrcMacStatus_Type()
)
swIpMcstVlanRepSrcMacStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMcstVlanRepSrcMacStatus.setStatus("current")
_SwIpMcstVlanRepTable_Object = MibTable
swIpMcstVlanRepTable = _SwIpMcstVlanRepTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 3)
)
if mibBuilder.loadTexts:
    swIpMcstVlanRepTable.setStatus("current")
_SwIpMcstVlanRepEntry_Object = MibTableRow
swIpMcstVlanRepEntry = _SwIpMcstVlanRepEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 3, 1)
)
swIpMcstVlanRepEntry.setIndexNames(
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepName"),
)
if mibBuilder.loadTexts:
    swIpMcstVlanRepEntry.setStatus("current")
_SwIpMcstVlanRepName_Type = DisplayString
_SwIpMcstVlanRepName_Object = MibTableColumn
swIpMcstVlanRepName = _SwIpMcstVlanRepName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 3, 1, 1),
    _SwIpMcstVlanRepName_Type()
)
swIpMcstVlanRepName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepName.setStatus("current")
_SwIpMcstVlanRepSrcVID_Type = VlanId
_SwIpMcstVlanRepSrcVID_Object = MibTableColumn
swIpMcstVlanRepSrcVID = _SwIpMcstVlanRepSrcVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 3, 1, 2),
    _SwIpMcstVlanRepSrcVID_Type()
)
swIpMcstVlanRepSrcVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMcstVlanRepSrcVID.setStatus("current")
_SwIpMcstVlanRepRowStatus_Type = RowStatus
_SwIpMcstVlanRepRowStatus_Object = MibTableColumn
swIpMcstVlanRepRowStatus = _SwIpMcstVlanRepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 3, 1, 3),
    _SwIpMcstVlanRepRowStatus_Type()
)
swIpMcstVlanRepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMcstVlanRepRowStatus.setStatus("current")
_SwIpMcstVlanRepSrcTable_Object = MibTable
swIpMcstVlanRepSrcTable = _SwIpMcstVlanRepSrcTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4)
)
if mibBuilder.loadTexts:
    swIpMcstVlanRepSrcTable.setStatus("current")
_SwIpMcstVlanRepSrcEntry_Object = MibTableRow
swIpMcstVlanRepSrcEntry = _SwIpMcstVlanRepSrcEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4, 1)
)
swIpMcstVlanRepSrcEntry.setIndexNames(
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepName"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepGrpAddrType"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepGrpAddrStart"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepGrpAddrEnd"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepSrcAddrType"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepSrcAddr"),
)
if mibBuilder.loadTexts:
    swIpMcstVlanRepSrcEntry.setStatus("current")
_SwIpMcstVlanRepGrpAddrType_Type = InetAddressType
_SwIpMcstVlanRepGrpAddrType_Object = MibTableColumn
swIpMcstVlanRepGrpAddrType = _SwIpMcstVlanRepGrpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4, 1, 1),
    _SwIpMcstVlanRepGrpAddrType_Type()
)
swIpMcstVlanRepGrpAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepGrpAddrType.setStatus("current")
_SwIpMcstVlanRepGrpAddrStart_Type = InetAddress
_SwIpMcstVlanRepGrpAddrStart_Object = MibTableColumn
swIpMcstVlanRepGrpAddrStart = _SwIpMcstVlanRepGrpAddrStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4, 1, 2),
    _SwIpMcstVlanRepGrpAddrStart_Type()
)
swIpMcstVlanRepGrpAddrStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepGrpAddrStart.setStatus("current")
_SwIpMcstVlanRepGrpAddrEnd_Type = InetAddress
_SwIpMcstVlanRepGrpAddrEnd_Object = MibTableColumn
swIpMcstVlanRepGrpAddrEnd = _SwIpMcstVlanRepGrpAddrEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4, 1, 3),
    _SwIpMcstVlanRepGrpAddrEnd_Type()
)
swIpMcstVlanRepGrpAddrEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepGrpAddrEnd.setStatus("current")
_SwIpMcstVlanRepSrcAddrType_Type = InetAddressType
_SwIpMcstVlanRepSrcAddrType_Object = MibTableColumn
swIpMcstVlanRepSrcAddrType = _SwIpMcstVlanRepSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4, 1, 4),
    _SwIpMcstVlanRepSrcAddrType_Type()
)
swIpMcstVlanRepSrcAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepSrcAddrType.setStatus("current")
_SwIpMcstVlanRepSrcAddr_Type = InetAddress
_SwIpMcstVlanRepSrcAddr_Object = MibTableColumn
swIpMcstVlanRepSrcAddr = _SwIpMcstVlanRepSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4, 1, 5),
    _SwIpMcstVlanRepSrcAddr_Type()
)
swIpMcstVlanRepSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepSrcAddr.setStatus("current")
_SwIpMcstVlanRepSrcRowStatus_Type = RowStatus
_SwIpMcstVlanRepSrcRowStatus_Object = MibTableColumn
swIpMcstVlanRepSrcRowStatus = _SwIpMcstVlanRepSrcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 4, 1, 6),
    _SwIpMcstVlanRepSrcRowStatus_Type()
)
swIpMcstVlanRepSrcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMcstVlanRepSrcRowStatus.setStatus("current")
_SwIpMcstVlanRepDstTable_Object = MibTable
swIpMcstVlanRepDstTable = _SwIpMcstVlanRepDstTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 5)
)
if mibBuilder.loadTexts:
    swIpMcstVlanRepDstTable.setStatus("current")
_SwIpMcstVlanRepDstEntry_Object = MibTableRow
swIpMcstVlanRepDstEntry = _SwIpMcstVlanRepDstEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 5, 1)
)
swIpMcstVlanRepDstEntry.setIndexNames(
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepName"),
    (0, "IP-MCST-VLAN-REP-MIB", "swIpMcstVlanRepDstVID"),
)
if mibBuilder.loadTexts:
    swIpMcstVlanRepDstEntry.setStatus("current")
_SwIpMcstVlanRepDstVID_Type = VlanId
_SwIpMcstVlanRepDstVID_Object = MibTableColumn
swIpMcstVlanRepDstVID = _SwIpMcstVlanRepDstVID_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 5, 1, 1),
    _SwIpMcstVlanRepDstVID_Type()
)
swIpMcstVlanRepDstVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIpMcstVlanRepDstVID.setStatus("current")
_SwIpMcstVlanRepDstPort_Type = PortList
_SwIpMcstVlanRepDstPort_Object = MibTableColumn
swIpMcstVlanRepDstPort = _SwIpMcstVlanRepDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 5, 1, 2),
    _SwIpMcstVlanRepDstPort_Type()
)
swIpMcstVlanRepDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swIpMcstVlanRepDstPort.setStatus("current")
_SwIpMcstVlanRepDstRowStatus_Type = RowStatus
_SwIpMcstVlanRepDstRowStatus_Object = MibTableColumn
swIpMcstVlanRepDstRowStatus = _SwIpMcstVlanRepDstRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 71, 3, 5, 1, 3),
    _SwIpMcstVlanRepDstRowStatus_Type()
)
swIpMcstVlanRepDstRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swIpMcstVlanRepDstRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IP-MCST-VLAN-REP-MIB",
    **{"PortList": PortList,
       "VlanId": VlanId,
       "swIpMcstVlanRepMIB": swIpMcstVlanRepMIB,
       "swIpMcstVlanRepCtrl": swIpMcstVlanRepCtrl,
       "swIpMcstVlanRepState": swIpMcstVlanRepState,
       "swIpMcstVlanRepInfo": swIpMcstVlanRepInfo,
       "swIpMcastVlanRepInfoTable": swIpMcastVlanRepInfoTable,
       "swIpMcastVlanRepInfoEntry": swIpMcastVlanRepInfoEntry,
       "swIpMcstVlanRepGroupAddrType": swIpMcstVlanRepGroupAddrType,
       "swIpMcstVlanRepGroupAddr": swIpMcstVlanRepGroupAddr,
       "swIpMcstVlanRepSourceAddrType": swIpMcstVlanRepSourceAddrType,
       "swIpMcstVlanRepSourceAddr": swIpMcstVlanRepSourceAddr,
       "swIpMcstVlanRepStatus": swIpMcstVlanRepStatus,
       "swIpMcstVlanRepMgmt": swIpMcstVlanRepMgmt,
       "swIpMcstVlanRepTTLStatus": swIpMcstVlanRepTTLStatus,
       "swIpMcstVlanRepSrcMacStatus": swIpMcstVlanRepSrcMacStatus,
       "swIpMcstVlanRepTable": swIpMcstVlanRepTable,
       "swIpMcstVlanRepEntry": swIpMcstVlanRepEntry,
       "swIpMcstVlanRepName": swIpMcstVlanRepName,
       "swIpMcstVlanRepSrcVID": swIpMcstVlanRepSrcVID,
       "swIpMcstVlanRepRowStatus": swIpMcstVlanRepRowStatus,
       "swIpMcstVlanRepSrcTable": swIpMcstVlanRepSrcTable,
       "swIpMcstVlanRepSrcEntry": swIpMcstVlanRepSrcEntry,
       "swIpMcstVlanRepGrpAddrType": swIpMcstVlanRepGrpAddrType,
       "swIpMcstVlanRepGrpAddrStart": swIpMcstVlanRepGrpAddrStart,
       "swIpMcstVlanRepGrpAddrEnd": swIpMcstVlanRepGrpAddrEnd,
       "swIpMcstVlanRepSrcAddrType": swIpMcstVlanRepSrcAddrType,
       "swIpMcstVlanRepSrcAddr": swIpMcstVlanRepSrcAddr,
       "swIpMcstVlanRepSrcRowStatus": swIpMcstVlanRepSrcRowStatus,
       "swIpMcstVlanRepDstTable": swIpMcstVlanRepDstTable,
       "swIpMcstVlanRepDstEntry": swIpMcstVlanRepDstEntry,
       "swIpMcstVlanRepDstVID": swIpMcstVlanRepDstVID,
       "swIpMcstVlanRepDstPort": swIpMcstVlanRepDstPort,
       "swIpMcstVlanRepDstRowStatus": swIpMcstVlanRepDstRowStatus}
)
