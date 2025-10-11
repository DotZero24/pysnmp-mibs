# SNMP MIB module (RAD-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:19 2025
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
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason,
 systemsEvents) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason",
    "systemsEvents")

(radSecurity,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radSecurity")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 RowPointer,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

radAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AceMarkingType(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("dscp", 0),
          ("ipPrecedence", 1),
          ("pBit", 2))
    )


class DscpMark(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class IpPrecedenceMark(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class PbitMark(TextualConvention, Unsigned32):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class UdpTcpPortOp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("lt", 2),
          ("gt", 3),
          ("eq", 4),
          ("neq", 5),
          ("range", 6))
    )



# MIB Managed Objects in the order of their OIDs

_AclConf_ObjectIdentity = ObjectIdentity
aclConf = _AclConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1)
)
_AclMainTable_Object = MibTable
aclMainTable = _AclMainTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    aclMainTable.setStatus("current")
_AclMainEntry_Object = MibTableRow
aclMainEntry = _AclMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1)
)
aclMainEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclName"),
)
if mibBuilder.loadTexts:
    aclMainEntry.setStatus("current")


class _AclName_Type(SnmpAdminString):
    """Custom type aclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_AclName_Type.__name__ = "SnmpAdminString"
_AclName_Object = MibTableColumn
aclName = _AclName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1, 1),
    _AclName_Type()
)
aclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclName.setStatus("current")
_AclNumberOfAce_Type = Unsigned32
_AclNumberOfAce_Object = MibTableColumn
aclNumberOfAce = _AclNumberOfAce_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1, 2),
    _AclNumberOfAce_Type()
)
aclNumberOfAce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumberOfAce.setStatus("current")
_AclLastSeqeunceNumber_Type = Unsigned32
_AclLastSeqeunceNumber_Object = MibTableColumn
aclLastSeqeunceNumber = _AclLastSeqeunceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1, 3),
    _AclLastSeqeunceNumber_Type()
)
aclLastSeqeunceNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclLastSeqeunceNumber.setStatus("current")
_AclResequenceCmd_Type = Unsigned32
_AclResequenceCmd_Object = MibTableColumn
aclResequenceCmd = _AclResequenceCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1, 4),
    _AclResequenceCmd_Type()
)
aclResequenceCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclResequenceCmd.setStatus("current")


class _AclType_Type(Integer32):
    """Custom type aclType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AclType_Type.__name__ = "Integer32"
_AclType_Object = MibTableColumn
aclType = _AclType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1, 5),
    _AclType_Type()
)
aclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclType.setStatus("current")


class _AclIllegalEntityTypes_Type(Bits):
    """Custom type aclIllegalEntityTypes based on Bits"""
    namedValues = NamedValues(
        *(("management", 0),
          ("routerInterface", 1))
    )

_AclIllegalEntityTypes_Type.__name__ = "Bits"
_AclIllegalEntityTypes_Object = MibTableColumn
aclIllegalEntityTypes = _AclIllegalEntityTypes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1, 6),
    _AclIllegalEntityTypes_Type()
)
aclIllegalEntityTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIllegalEntityTypes.setStatus("current")
_AclRowStatus_Type = RowStatus
_AclRowStatus_Object = MibTableColumn
aclRowStatus = _AclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 1, 1, 7),
    _AclRowStatus_Type()
)
aclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclRowStatus.setStatus("current")
_AclAceTable_Object = MibTable
aclAceTable = _AclAceTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2)
)
if mibBuilder.loadTexts:
    aclAceTable.setStatus("current")
_AclAceEntry_Object = MibTableRow
aclAceEntry = _AclAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1)
)
aclAceEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclAceIdx"),
)
if mibBuilder.loadTexts:
    aclAceEntry.setStatus("current")
_AclAceIdx_Type = Unsigned32
_AclAceIdx_Object = MibTableColumn
aclAceIdx = _AclAceIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 1),
    _AclAceIdx_Type()
)
aclAceIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclAceIdx.setStatus("current")
_AclAceSequenceNumber_Type = Unsigned32
_AclAceSequenceNumber_Object = MibTableColumn
aclAceSequenceNumber = _AclAceSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 2),
    _AclAceSequenceNumber_Type()
)
aclAceSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceSequenceNumber.setStatus("current")


class _AclAceType_Type(Integer32):
    """Custom type aclAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remark", 1),
          ("deny", 2),
          ("permit", 3))
    )


_AclAceType_Type.__name__ = "Integer32"
_AclAceType_Object = MibTableColumn
aclAceType = _AclAceType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 3),
    _AclAceType_Type()
)
aclAceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceType.setStatus("current")
_AclAcePointer_Type = RowPointer
_AclAcePointer_Object = MibTableColumn
aclAcePointer = _AclAcePointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 4),
    _AclAcePointer_Type()
)
aclAcePointer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAcePointer.setStatus("current")


class _AclAcelog_Type(Integer32):
    """Custom type aclAcelog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_AclAcelog_Type.__name__ = "Integer32"
_AclAcelog_Object = MibTableColumn
aclAcelog = _AclAcelog_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 5),
    _AclAcelog_Type()
)
aclAcelog.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAcelog.setStatus("current")


class _AclAceIllegalEntityTypes_Type(Bits):
    """Custom type aclAceIllegalEntityTypes based on Bits"""
    namedValues = NamedValues(
        *(("management", 0),
          ("routerInterface", 1))
    )

_AclAceIllegalEntityTypes_Type.__name__ = "Bits"
_AclAceIllegalEntityTypes_Object = MibTableColumn
aclAceIllegalEntityTypes = _AclAceIllegalEntityTypes_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 6),
    _AclAceIllegalEntityTypes_Type()
)
aclAceIllegalEntityTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceIllegalEntityTypes.setStatus("current")


class _AclAceAclName_Type(SnmpAdminString):
    """Custom type aclAceAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_AclAceAclName_Type.__name__ = "SnmpAdminString"
_AclAceAclName_Object = MibTableColumn
aclAceAclName = _AclAceAclName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 7),
    _AclAceAclName_Type()
)
aclAceAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceAclName.setStatus("current")
_AclAceRowStatus_Type = RowStatus
_AclAceRowStatus_Object = MibTableColumn
aclAceRowStatus = _AclAceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 2, 1, 8),
    _AclAceRowStatus_Type()
)
aclAceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceRowStatus.setStatus("current")
_AclAceRemarkTable_Object = MibTable
aclAceRemarkTable = _AclAceRemarkTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 3)
)
if mibBuilder.loadTexts:
    aclAceRemarkTable.setStatus("current")
_AclAceRemarkEntry_Object = MibTableRow
aclAceRemarkEntry = _AclAceRemarkEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 3, 1)
)
aclAceRemarkEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclAceIdx"),
)
if mibBuilder.loadTexts:
    aclAceRemarkEntry.setStatus("current")


class _AclAceRemark_Type(SnmpAdminString):
    """Custom type aclAceRemark based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_AclAceRemark_Type.__name__ = "SnmpAdminString"
_AclAceRemark_Object = MibTableColumn
aclAceRemark = _AclAceRemark_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 3, 1, 1),
    _AclAceRemark_Type()
)
aclAceRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceRemark.setStatus("current")
_AclAceIPTable_Object = MibTable
aclAceIPTable = _AclAceIPTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4)
)
if mibBuilder.loadTexts:
    aclAceIPTable.setStatus("current")
_AclAceIPEntry_Object = MibTableRow
aclAceIPEntry = _AclAceIPEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1)
)
aclAceIPEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclAceIdx"),
)
if mibBuilder.loadTexts:
    aclAceIPEntry.setStatus("current")
_AclAceIPSrcAddressType_Type = InetAddressType
_AclAceIPSrcAddressType_Object = MibTableColumn
aclAceIPSrcAddressType = _AclAceIPSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 1),
    _AclAceIPSrcAddressType_Type()
)
aclAceIPSrcAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPSrcAddressType.setStatus("current")
_AclAceIPSrcAddress_Type = InetAddress
_AclAceIPSrcAddress_Object = MibTableColumn
aclAceIPSrcAddress = _AclAceIPSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 2),
    _AclAceIPSrcAddress_Type()
)
aclAceIPSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPSrcAddress.setStatus("current")
_AclAceIPSrcAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceIPSrcAddressPrefixLength_Object = MibTableColumn
aclAceIPSrcAddressPrefixLength = _AclAceIPSrcAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 3),
    _AclAceIPSrcAddressPrefixLength_Type()
)
aclAceIPSrcAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPSrcAddressPrefixLength.setStatus("current")
_AclAceIPDstAddressType_Type = InetAddressType
_AclAceIPDstAddressType_Object = MibTableColumn
aclAceIPDstAddressType = _AclAceIPDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 4),
    _AclAceIPDstAddressType_Type()
)
aclAceIPDstAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPDstAddressType.setStatus("current")
_AclAceIPDstAddress_Type = InetAddress
_AclAceIPDstAddress_Object = MibTableColumn
aclAceIPDstAddress = _AclAceIPDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 5),
    _AclAceIPDstAddress_Type()
)
aclAceIPDstAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPDstAddress.setStatus("current")
_AclAceIPDstAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceIPDstAddressPrefixLength_Object = MibTableColumn
aclAceIPDstAddressPrefixLength = _AclAceIPDstAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 6),
    _AclAceIPDstAddressPrefixLength_Type()
)
aclAceIPDstAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPDstAddressPrefixLength.setStatus("current")
_AclAceIPMarkingType_Type = AceMarkingType
_AclAceIPMarkingType_Object = MibTableColumn
aclAceIPMarkingType = _AclAceIPMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 7),
    _AclAceIPMarkingType_Type()
)
aclAceIPMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPMarkingType.setStatus("current")
_AclAceIPDscp_Type = DscpMark
_AclAceIPDscp_Object = MibTableColumn
aclAceIPDscp = _AclAceIPDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 8),
    _AclAceIPDscp_Type()
)
aclAceIPDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPDscp.setStatus("current")
_AclAceIPIpPrecedence_Type = IpPrecedenceMark
_AclAceIPIpPrecedence_Object = MibTableColumn
aclAceIPIpPrecedence = _AclAceIPIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 9),
    _AclAceIPIpPrecedence_Type()
)
aclAceIPIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPIpPrecedence.setStatus("current")
_AclAceIPProtocolNumber_Type = Unsigned32
_AclAceIPProtocolNumber_Object = MibTableColumn
aclAceIPProtocolNumber = _AclAceIPProtocolNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 10),
    _AclAceIPProtocolNumber_Type()
)
aclAceIPProtocolNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPProtocolNumber.setStatus("current")
_AclAceIPSetMarkingType_Type = AceMarkingType
_AclAceIPSetMarkingType_Object = MibTableColumn
aclAceIPSetMarkingType = _AclAceIPSetMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 11),
    _AclAceIPSetMarkingType_Type()
)
aclAceIPSetMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPSetMarkingType.setStatus("current")
_AclAceIPSetDscp_Type = DscpMark
_AclAceIPSetDscp_Object = MibTableColumn
aclAceIPSetDscp = _AclAceIPSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 12),
    _AclAceIPSetDscp_Type()
)
aclAceIPSetDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPSetDscp.setStatus("current")
_AclAceIPSetIpPrecedence_Type = IpPrecedenceMark
_AclAceIPSetIpPrecedence_Object = MibTableColumn
aclAceIPSetIpPrecedence = _AclAceIPSetIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 13),
    _AclAceIPSetIpPrecedence_Type()
)
aclAceIPSetIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPSetIpPrecedence.setStatus("current")
_AclAceIPSetPbit_Type = PbitMark
_AclAceIPSetPbit_Object = MibTableColumn
aclAceIPSetPbit = _AclAceIPSetPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 4, 1, 14),
    _AclAceIPSetPbit_Type()
)
aclAceIPSetPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceIPSetPbit.setStatus("current")
_AclAceICMPTable_Object = MibTable
aclAceICMPTable = _AclAceICMPTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5)
)
if mibBuilder.loadTexts:
    aclAceICMPTable.setStatus("current")
_AclAceICMPEntry_Object = MibTableRow
aclAceICMPEntry = _AclAceICMPEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1)
)
aclAceICMPEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclAceIdx"),
)
if mibBuilder.loadTexts:
    aclAceICMPEntry.setStatus("current")
_AclAceICMPSrcAddressType_Type = InetAddressType
_AclAceICMPSrcAddressType_Object = MibTableColumn
aclAceICMPSrcAddressType = _AclAceICMPSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 1),
    _AclAceICMPSrcAddressType_Type()
)
aclAceICMPSrcAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPSrcAddressType.setStatus("current")
_AclAceICMPSrcAddress_Type = InetAddress
_AclAceICMPSrcAddress_Object = MibTableColumn
aclAceICMPSrcAddress = _AclAceICMPSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 2),
    _AclAceICMPSrcAddress_Type()
)
aclAceICMPSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPSrcAddress.setStatus("current")
_AclAceICMPSrcAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceICMPSrcAddressPrefixLength_Object = MibTableColumn
aclAceICMPSrcAddressPrefixLength = _AclAceICMPSrcAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 3),
    _AclAceICMPSrcAddressPrefixLength_Type()
)
aclAceICMPSrcAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPSrcAddressPrefixLength.setStatus("current")
_AclAceICMPDstAddressType_Type = InetAddressType
_AclAceICMPDstAddressType_Object = MibTableColumn
aclAceICMPDstAddressType = _AclAceICMPDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 4),
    _AclAceICMPDstAddressType_Type()
)
aclAceICMPDstAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPDstAddressType.setStatus("current")
_AclAceICMPDstAddress_Type = InetAddress
_AclAceICMPDstAddress_Object = MibTableColumn
aclAceICMPDstAddress = _AclAceICMPDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 5),
    _AclAceICMPDstAddress_Type()
)
aclAceICMPDstAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPDstAddress.setStatus("current")
_AclAceICMPDstAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceICMPDstAddressPrefixLength_Object = MibTableColumn
aclAceICMPDstAddressPrefixLength = _AclAceICMPDstAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 6),
    _AclAceICMPDstAddressPrefixLength_Type()
)
aclAceICMPDstAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPDstAddressPrefixLength.setStatus("current")
_AclAceICMPMarkingType_Type = AceMarkingType
_AclAceICMPMarkingType_Object = MibTableColumn
aclAceICMPMarkingType = _AclAceICMPMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 7),
    _AclAceICMPMarkingType_Type()
)
aclAceICMPMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPMarkingType.setStatus("current")
_AclAceICMPDscp_Type = DscpMark
_AclAceICMPDscp_Object = MibTableColumn
aclAceICMPDscp = _AclAceICMPDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 8),
    _AclAceICMPDscp_Type()
)
aclAceICMPDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPDscp.setStatus("current")
_AclAceICMPIpPrecedence_Type = IpPrecedenceMark
_AclAceICMPIpPrecedence_Object = MibTableColumn
aclAceICMPIpPrecedence = _AclAceICMPIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 9),
    _AclAceICMPIpPrecedence_Type()
)
aclAceICMPIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPIpPrecedence.setStatus("current")
_AclAceICMPType_Type = Unsigned32
_AclAceICMPType_Object = MibTableColumn
aclAceICMPType = _AclAceICMPType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 10),
    _AclAceICMPType_Type()
)
aclAceICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPType.setStatus("current")
_AclAceICMPCode_Type = Unsigned32
_AclAceICMPCode_Object = MibTableColumn
aclAceICMPCode = _AclAceICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 11),
    _AclAceICMPCode_Type()
)
aclAceICMPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPCode.setStatus("current")
_AclAceICMPSetMarkingType_Type = AceMarkingType
_AclAceICMPSetMarkingType_Object = MibTableColumn
aclAceICMPSetMarkingType = _AclAceICMPSetMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 12),
    _AclAceICMPSetMarkingType_Type()
)
aclAceICMPSetMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPSetMarkingType.setStatus("current")
_AclAceICMPSetDscp_Type = DscpMark
_AclAceICMPSetDscp_Object = MibTableColumn
aclAceICMPSetDscp = _AclAceICMPSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 13),
    _AclAceICMPSetDscp_Type()
)
aclAceICMPSetDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPSetDscp.setStatus("current")
_AclAceICMPSetIpPrecedence_Type = IpPrecedenceMark
_AclAceICMPSetIpPrecedence_Object = MibTableColumn
aclAceICMPSetIpPrecedence = _AclAceICMPSetIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 14),
    _AclAceICMPSetIpPrecedence_Type()
)
aclAceICMPSetIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPSetIpPrecedence.setStatus("current")
_AclAceICMPSetPbit_Type = PbitMark
_AclAceICMPSetPbit_Object = MibTableColumn
aclAceICMPSetPbit = _AclAceICMPSetPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 5, 1, 15),
    _AclAceICMPSetPbit_Type()
)
aclAceICMPSetPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceICMPSetPbit.setStatus("current")
_AclAceTCPTable_Object = MibTable
aclAceTCPTable = _AclAceTCPTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6)
)
if mibBuilder.loadTexts:
    aclAceTCPTable.setStatus("current")
_AclAceTCPEntry_Object = MibTableRow
aclAceTCPEntry = _AclAceTCPEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1)
)
aclAceTCPEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclAceIdx"),
)
if mibBuilder.loadTexts:
    aclAceTCPEntry.setStatus("current")
_AclAceTCPSrcAddressType_Type = InetAddressType
_AclAceTCPSrcAddressType_Object = MibTableColumn
aclAceTCPSrcAddressType = _AclAceTCPSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 1),
    _AclAceTCPSrcAddressType_Type()
)
aclAceTCPSrcAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSrcAddressType.setStatus("current")
_AclAceTCPSrcAddress_Type = InetAddress
_AclAceTCPSrcAddress_Object = MibTableColumn
aclAceTCPSrcAddress = _AclAceTCPSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 2),
    _AclAceTCPSrcAddress_Type()
)
aclAceTCPSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSrcAddress.setStatus("current")
_AclAceTCPSrcAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceTCPSrcAddressPrefixLength_Object = MibTableColumn
aclAceTCPSrcAddressPrefixLength = _AclAceTCPSrcAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 3),
    _AclAceTCPSrcAddressPrefixLength_Type()
)
aclAceTCPSrcAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSrcAddressPrefixLength.setStatus("current")
_AclAceTCPDstAddressType_Type = InetAddressType
_AclAceTCPDstAddressType_Object = MibTableColumn
aclAceTCPDstAddressType = _AclAceTCPDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 4),
    _AclAceTCPDstAddressType_Type()
)
aclAceTCPDstAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPDstAddressType.setStatus("current")
_AclAceTCPDstAddress_Type = InetAddress
_AclAceTCPDstAddress_Object = MibTableColumn
aclAceTCPDstAddress = _AclAceTCPDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 5),
    _AclAceTCPDstAddress_Type()
)
aclAceTCPDstAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPDstAddress.setStatus("current")
_AclAceTCPDstAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceTCPDstAddressPrefixLength_Object = MibTableColumn
aclAceTCPDstAddressPrefixLength = _AclAceTCPDstAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 6),
    _AclAceTCPDstAddressPrefixLength_Type()
)
aclAceTCPDstAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPDstAddressPrefixLength.setStatus("current")
_AclAceTCPMarkingType_Type = AceMarkingType
_AclAceTCPMarkingType_Object = MibTableColumn
aclAceTCPMarkingType = _AclAceTCPMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 7),
    _AclAceTCPMarkingType_Type()
)
aclAceTCPMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPMarkingType.setStatus("current")
_AclAceTCPDscp_Type = DscpMark
_AclAceTCPDscp_Object = MibTableColumn
aclAceTCPDscp = _AclAceTCPDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 8),
    _AclAceTCPDscp_Type()
)
aclAceTCPDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPDscp.setStatus("current")
_AclAceTCPIpPrecedence_Type = IpPrecedenceMark
_AclAceTCPIpPrecedence_Object = MibTableColumn
aclAceTCPIpPrecedence = _AclAceTCPIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 9),
    _AclAceTCPIpPrecedence_Type()
)
aclAceTCPIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPIpPrecedence.setStatus("current")
_AclAceTCPSrcPortOp_Type = UdpTcpPortOp
_AclAceTCPSrcPortOp_Object = MibTableColumn
aclAceTCPSrcPortOp = _AclAceTCPSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 10),
    _AclAceTCPSrcPortOp_Type()
)
aclAceTCPSrcPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSrcPortOp.setStatus("current")
_AclAceTCPSrcPort_Type = InetPortNumber
_AclAceTCPSrcPort_Object = MibTableColumn
aclAceTCPSrcPort = _AclAceTCPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 11),
    _AclAceTCPSrcPort_Type()
)
aclAceTCPSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSrcPort.setStatus("current")
_AclAceTCPSrcPortRange_Type = InetPortNumber
_AclAceTCPSrcPortRange_Object = MibTableColumn
aclAceTCPSrcPortRange = _AclAceTCPSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 12),
    _AclAceTCPSrcPortRange_Type()
)
aclAceTCPSrcPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSrcPortRange.setStatus("current")
_AclAceTCPDstPortOp_Type = UdpTcpPortOp
_AclAceTCPDstPortOp_Object = MibTableColumn
aclAceTCPDstPortOp = _AclAceTCPDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 13),
    _AclAceTCPDstPortOp_Type()
)
aclAceTCPDstPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPDstPortOp.setStatus("current")
_AclAceTCPDstPort_Type = InetPortNumber
_AclAceTCPDstPort_Object = MibTableColumn
aclAceTCPDstPort = _AclAceTCPDstPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 14),
    _AclAceTCPDstPort_Type()
)
aclAceTCPDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPDstPort.setStatus("current")
_AclAceTCPDstPortRange_Type = InetPortNumber
_AclAceTCPDstPortRange_Object = MibTableColumn
aclAceTCPDstPortRange = _AclAceTCPDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 15),
    _AclAceTCPDstPortRange_Type()
)
aclAceTCPDstPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPDstPortRange.setStatus("current")
_AclAceTCPSetMarkingType_Type = AceMarkingType
_AclAceTCPSetMarkingType_Object = MibTableColumn
aclAceTCPSetMarkingType = _AclAceTCPSetMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 16),
    _AclAceTCPSetMarkingType_Type()
)
aclAceTCPSetMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSetMarkingType.setStatus("current")
_AclAceTCPSetDscp_Type = DscpMark
_AclAceTCPSetDscp_Object = MibTableColumn
aclAceTCPSetDscp = _AclAceTCPSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 17),
    _AclAceTCPSetDscp_Type()
)
aclAceTCPSetDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSetDscp.setStatus("current")
_AclAceTCPSetIpPrecedence_Type = IpPrecedenceMark
_AclAceTCPSetIpPrecedence_Object = MibTableColumn
aclAceTCPSetIpPrecedence = _AclAceTCPSetIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 18),
    _AclAceTCPSetIpPrecedence_Type()
)
aclAceTCPSetIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSetIpPrecedence.setStatus("current")
_AclAceTCPSetPbit_Type = PbitMark
_AclAceTCPSetPbit_Object = MibTableColumn
aclAceTCPSetPbit = _AclAceTCPSetPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 6, 1, 19),
    _AclAceTCPSetPbit_Type()
)
aclAceTCPSetPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceTCPSetPbit.setStatus("current")
_AclAceUDPTable_Object = MibTable
aclAceUDPTable = _AclAceUDPTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7)
)
if mibBuilder.loadTexts:
    aclAceUDPTable.setStatus("current")
_AclAceUDPEntry_Object = MibTableRow
aclAceUDPEntry = _AclAceUDPEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1)
)
aclAceUDPEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclAceIdx"),
)
if mibBuilder.loadTexts:
    aclAceUDPEntry.setStatus("current")
_AclAceUDPSrcAddressType_Type = InetAddressType
_AclAceUDPSrcAddressType_Object = MibTableColumn
aclAceUDPSrcAddressType = _AclAceUDPSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 1),
    _AclAceUDPSrcAddressType_Type()
)
aclAceUDPSrcAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSrcAddressType.setStatus("current")
_AclAceUDPSrcAddress_Type = InetAddress
_AclAceUDPSrcAddress_Object = MibTableColumn
aclAceUDPSrcAddress = _AclAceUDPSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 2),
    _AclAceUDPSrcAddress_Type()
)
aclAceUDPSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSrcAddress.setStatus("current")
_AclAceUDPSrcAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceUDPSrcAddressPrefixLength_Object = MibTableColumn
aclAceUDPSrcAddressPrefixLength = _AclAceUDPSrcAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 3),
    _AclAceUDPSrcAddressPrefixLength_Type()
)
aclAceUDPSrcAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSrcAddressPrefixLength.setStatus("current")
_AclAceUDPDstAddressType_Type = InetAddressType
_AclAceUDPDstAddressType_Object = MibTableColumn
aclAceUDPDstAddressType = _AclAceUDPDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 4),
    _AclAceUDPDstAddressType_Type()
)
aclAceUDPDstAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPDstAddressType.setStatus("current")
_AclAceUDPDstAddress_Type = InetAddress
_AclAceUDPDstAddress_Object = MibTableColumn
aclAceUDPDstAddress = _AclAceUDPDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 5),
    _AclAceUDPDstAddress_Type()
)
aclAceUDPDstAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPDstAddress.setStatus("current")
_AclAceUDPDstAddressPrefixLength_Type = InetAddressPrefixLength
_AclAceUDPDstAddressPrefixLength_Object = MibTableColumn
aclAceUDPDstAddressPrefixLength = _AclAceUDPDstAddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 6),
    _AclAceUDPDstAddressPrefixLength_Type()
)
aclAceUDPDstAddressPrefixLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPDstAddressPrefixLength.setStatus("current")
_AclAceUDPMarkingType_Type = AceMarkingType
_AclAceUDPMarkingType_Object = MibTableColumn
aclAceUDPMarkingType = _AclAceUDPMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 7),
    _AclAceUDPMarkingType_Type()
)
aclAceUDPMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPMarkingType.setStatus("current")
_AclAceUDPDscp_Type = DscpMark
_AclAceUDPDscp_Object = MibTableColumn
aclAceUDPDscp = _AclAceUDPDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 8),
    _AclAceUDPDscp_Type()
)
aclAceUDPDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPDscp.setStatus("current")
_AclAceUDPIpPrecedence_Type = IpPrecedenceMark
_AclAceUDPIpPrecedence_Object = MibTableColumn
aclAceUDPIpPrecedence = _AclAceUDPIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 9),
    _AclAceUDPIpPrecedence_Type()
)
aclAceUDPIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPIpPrecedence.setStatus("current")
_AclAceUDPSrcPortOp_Type = UdpTcpPortOp
_AclAceUDPSrcPortOp_Object = MibTableColumn
aclAceUDPSrcPortOp = _AclAceUDPSrcPortOp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 10),
    _AclAceUDPSrcPortOp_Type()
)
aclAceUDPSrcPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSrcPortOp.setStatus("current")
_AclAceUDPSrcPort_Type = InetPortNumber
_AclAceUDPSrcPort_Object = MibTableColumn
aclAceUDPSrcPort = _AclAceUDPSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 11),
    _AclAceUDPSrcPort_Type()
)
aclAceUDPSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSrcPort.setStatus("current")
_AclAceUDPSrcPortRange_Type = InetPortNumber
_AclAceUDPSrcPortRange_Object = MibTableColumn
aclAceUDPSrcPortRange = _AclAceUDPSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 12),
    _AclAceUDPSrcPortRange_Type()
)
aclAceUDPSrcPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSrcPortRange.setStatus("current")
_AclAceUDPDstPortOp_Type = UdpTcpPortOp
_AclAceUDPDstPortOp_Object = MibTableColumn
aclAceUDPDstPortOp = _AclAceUDPDstPortOp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 13),
    _AclAceUDPDstPortOp_Type()
)
aclAceUDPDstPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPDstPortOp.setStatus("current")
_AclAceUDPDstPort_Type = InetPortNumber
_AclAceUDPDstPort_Object = MibTableColumn
aclAceUDPDstPort = _AclAceUDPDstPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 14),
    _AclAceUDPDstPort_Type()
)
aclAceUDPDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPDstPort.setStatus("current")
_AclAceUDPDstPortRange_Type = InetPortNumber
_AclAceUDPDstPortRange_Object = MibTableColumn
aclAceUDPDstPortRange = _AclAceUDPDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 15),
    _AclAceUDPDstPortRange_Type()
)
aclAceUDPDstPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPDstPortRange.setStatus("current")
_AclAceUDPSetMarkingType_Type = AceMarkingType
_AclAceUDPSetMarkingType_Object = MibTableColumn
aclAceUDPSetMarkingType = _AclAceUDPSetMarkingType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 16),
    _AclAceUDPSetMarkingType_Type()
)
aclAceUDPSetMarkingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSetMarkingType.setStatus("current")
_AclAceUDPSetDscp_Type = DscpMark
_AclAceUDPSetDscp_Object = MibTableColumn
aclAceUDPSetDscp = _AclAceUDPSetDscp_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 17),
    _AclAceUDPSetDscp_Type()
)
aclAceUDPSetDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSetDscp.setStatus("current")
_AclAceUDPSetIpPrecedence_Type = IpPrecedenceMark
_AclAceUDPSetIpPrecedence_Object = MibTableColumn
aclAceUDPSetIpPrecedence = _AclAceUDPSetIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 18),
    _AclAceUDPSetIpPrecedence_Type()
)
aclAceUDPSetIpPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSetIpPrecedence.setStatus("current")
_AclAceUDPSetPbit_Type = PbitMark
_AclAceUDPSetPbit_Object = MibTableColumn
aclAceUDPSetPbit = _AclAceUDPSetPbit_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 7, 1, 19),
    _AclAceUDPSetPbit_Type()
)
aclAceUDPSetPbit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceUDPSetPbit.setStatus("current")
_AclBindTable_Object = MibTable
aclBindTable = _AclBindTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8)
)
if mibBuilder.loadTexts:
    aclBindTable.setStatus("current")
_AclBindEntry_Object = MibTableRow
aclBindEntry = _AclBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1)
)
aclBindEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclBindEntityType"),
    (0, "RAD-ACL-MIB", "aclBindEntityIndex"),
    (0, "RAD-ACL-MIB", "aclBindDirection"),
    (0, "RAD-ACL-MIB", "aclBindAclType"),
)
if mibBuilder.loadTexts:
    aclBindEntry.setStatus("current")


class _AclBindEntityType_Type(Integer32):
    """Custom type aclBindEntityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("routerInterface", 1),
          ("management", 2))
    )


_AclBindEntityType_Type.__name__ = "Integer32"
_AclBindEntityType_Object = MibTableColumn
aclBindEntityType = _AclBindEntityType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 1),
    _AclBindEntityType_Type()
)
aclBindEntityType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclBindEntityType.setStatus("current")
_AclBindEntityIndex_Type = Integer32
_AclBindEntityIndex_Object = MibTableColumn
aclBindEntityIndex = _AclBindEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 2),
    _AclBindEntityIndex_Type()
)
aclBindEntityIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclBindEntityIndex.setStatus("current")


class _AclBindDirection_Type(Integer32):
    """Custom type aclBindDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 2),
          ("outbound", 3))
    )


_AclBindDirection_Type.__name__ = "Integer32"
_AclBindDirection_Object = MibTableColumn
aclBindDirection = _AclBindDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 3),
    _AclBindDirection_Type()
)
aclBindDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclBindDirection.setStatus("current")


class _AclBindAclType_Type(Integer32):
    """Custom type aclBindAclType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AclBindAclType_Type.__name__ = "Integer32"
_AclBindAclType_Object = MibTableColumn
aclBindAclType = _AclBindAclType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 4),
    _AclBindAclType_Type()
)
aclBindAclType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclBindAclType.setStatus("current")


class _AclBindAclName_Type(SnmpAdminString):
    """Custom type aclBindAclName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 252),
    )


_AclBindAclName_Type.__name__ = "SnmpAdminString"
_AclBindAclName_Object = MibTableColumn
aclBindAclName = _AclBindAclName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 5),
    _AclBindAclName_Type()
)
aclBindAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclBindAclName.setStatus("current")
_AclBindTimeElapsed_Type = Gauge32
_AclBindTimeElapsed_Object = MibTableColumn
aclBindTimeElapsed = _AclBindTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 6),
    _AclBindTimeElapsed_Type()
)
aclBindTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclBindTimeElapsed.setStatus("current")


class _AclBindClearStatisticsCmd_Type(Integer32):
    """Custom type aclBindClearStatisticsCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AclBindClearStatisticsCmd_Type.__name__ = "Integer32"
_AclBindClearStatisticsCmd_Object = MibTableColumn
aclBindClearStatisticsCmd = _AclBindClearStatisticsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 7),
    _AclBindClearStatisticsCmd_Type()
)
aclBindClearStatisticsCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclBindClearStatisticsCmd.setStatus("current")
_AclBindRowStatus_Type = RowStatus
_AclBindRowStatus_Object = MibTableColumn
aclBindRowStatus = _AclBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 8, 1, 8),
    _AclBindRowStatus_Type()
)
aclBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclBindRowStatus.setStatus("current")
_AclHandleTable_Object = MibTable
aclHandleTable = _AclHandleTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 10)
)
if mibBuilder.loadTexts:
    aclHandleTable.setStatus("current")
_AclHandleEntry_Object = MibTableRow
aclHandleEntry = _AclHandleEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 10, 1)
)
aclHandleEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclHandleIndex"),
)
if mibBuilder.loadTexts:
    aclHandleEntry.setStatus("current")
_AclHandleIndex_Type = Unsigned32
_AclHandleIndex_Object = MibTableColumn
aclHandleIndex = _AclHandleIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 10, 1, 1),
    _AclHandleIndex_Type()
)
aclHandleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclHandleIndex.setStatus("current")
_AclLoggingIntervel_Type = Unsigned32
_AclLoggingIntervel_Object = MibTableColumn
aclLoggingIntervel = _AclLoggingIntervel_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 10, 1, 2),
    _AclLoggingIntervel_Type()
)
aclLoggingIntervel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclLoggingIntervel.setStatus("current")
_AclInvAceTable_Object = MibTable
aclInvAceTable = _AclInvAceTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 11)
)
if mibBuilder.loadTexts:
    aclInvAceTable.setStatus("current")
_AclInvAceEntry_Object = MibTableRow
aclInvAceEntry = _AclInvAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 11, 1)
)
aclInvAceEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclName"),
    (0, "RAD-ACL-MIB", "aclAceSequenceNumber"),
)
if mibBuilder.loadTexts:
    aclInvAceEntry.setStatus("current")
_AclInvAceIdx_Type = Unsigned32
_AclInvAceIdx_Object = MibTableColumn
aclInvAceIdx = _AclInvAceIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 11, 1, 1),
    _AclInvAceIdx_Type()
)
aclInvAceIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclInvAceIdx.setStatus("current")


class _AclInvAceType_Type(Integer32):
    """Custom type aclInvAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("remark", 1),
          ("deny", 2),
          ("permit", 3))
    )


_AclInvAceType_Type.__name__ = "Integer32"
_AclInvAceType_Object = MibTableColumn
aclInvAceType = _AclInvAceType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 11, 1, 2),
    _AclInvAceType_Type()
)
aclInvAceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclInvAceType.setStatus("current")
_AclInvAcePointer_Type = RowPointer
_AclInvAcePointer_Object = MibTableColumn
aclInvAcePointer = _AclInvAcePointer_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 11, 1, 3),
    _AclInvAcePointer_Type()
)
aclInvAcePointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclInvAcePointer.setStatus("current")


class _AclInvAcelog_Type(Integer32):
    """Custom type aclInvAcelog based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("disable", 2),
          ("enable", 3))
    )


_AclInvAcelog_Type.__name__ = "Integer32"
_AclInvAcelog_Object = MibTableColumn
aclInvAcelog = _AclInvAcelog_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 1, 11, 1, 4),
    _AclInvAcelog_Type()
)
aclInvAcelog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclInvAcelog.setStatus("current")
_AclStats_ObjectIdentity = ObjectIdentity
aclStats = _AclStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2)
)
_AclAceStatsTable_Object = MibTable
aclAceStatsTable = _AclAceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 1)
)
if mibBuilder.loadTexts:
    aclAceStatsTable.setStatus("current")
_AclAceStatsEntry_Object = MibTableRow
aclAceStatsEntry = _AclAceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 1, 1)
)
aclAceStatsEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclBindEntityType"),
    (0, "RAD-ACL-MIB", "aclBindEntityIndex"),
    (0, "RAD-ACL-MIB", "aclBindDirection"),
    (0, "RAD-ACL-MIB", "aclType"),
    (0, "RAD-ACL-MIB", "aclAceIdx"),
)
if mibBuilder.loadTexts:
    aclAceStatsEntry.setStatus("current")
_AclAceStatsMatches_Type = Gauge32
_AclAceStatsMatches_Object = MibTableColumn
aclAceStatsMatches = _AclAceStatsMatches_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 1, 1, 1),
    _AclAceStatsMatches_Type()
)
aclAceStatsMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceStatsMatches.setStatus("current")


class _AclAceStatsClearCmd_Type(Integer32):
    """Custom type aclAceStatsClearCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_AclAceStatsClearCmd_Type.__name__ = "Integer32"
_AclAceStatsClearCmd_Object = MibTableColumn
aclAceStatsClearCmd = _AclAceStatsClearCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 1, 1, 2),
    _AclAceStatsClearCmd_Type()
)
aclAceStatsClearCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclAceStatsClearCmd.setStatus("current")
_AclAceLogTable_Object = MibTable
aclAceLogTable = _AclAceLogTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2)
)
if mibBuilder.loadTexts:
    aclAceLogTable.setStatus("current")
_AclAceLogEntry_Object = MibTableRow
aclAceLogEntry = _AclAceLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1)
)
aclAceLogEntry.setIndexNames(
    (0, "RAD-ACL-MIB", "aclAceLogIndex"),
)
if mibBuilder.loadTexts:
    aclAceLogEntry.setStatus("current")
_AclAceLogIndex_Type = Unsigned32
_AclAceLogIndex_Object = MibTableColumn
aclAceLogIndex = _AclAceLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 1),
    _AclAceLogIndex_Type()
)
aclAceLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclAceLogIndex.setStatus("current")
_AclAceLogIPAddressType_Type = InetAddressType
_AclAceLogIPAddressType_Object = MibTableColumn
aclAceLogIPAddressType = _AclAceLogIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 2),
    _AclAceLogIPAddressType_Type()
)
aclAceLogIPAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceLogIPAddressType.setStatus("current")
_AclAceLogIPSrcAddress_Type = InetAddress
_AclAceLogIPSrcAddress_Object = MibTableColumn
aclAceLogIPSrcAddress = _AclAceLogIPSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 3),
    _AclAceLogIPSrcAddress_Type()
)
aclAceLogIPSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceLogIPSrcAddress.setStatus("current")
_AclAceLogIPDstAddress_Type = InetAddress
_AclAceLogIPDstAddress_Object = MibTableColumn
aclAceLogIPDstAddress = _AclAceLogIPDstAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 4),
    _AclAceLogIPDstAddress_Type()
)
aclAceLogIPDstAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceLogIPDstAddress.setStatus("current")


class _AclAceLogProtocol_Type(Integer32):
    """Custom type aclAceLogProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              255)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("icmp", 2),
          ("udp", 3),
          ("tcp", 4),
          ("unknown", 255))
    )


_AclAceLogProtocol_Type.__name__ = "Integer32"
_AclAceLogProtocol_Object = MibTableColumn
aclAceLogProtocol = _AclAceLogProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 5),
    _AclAceLogProtocol_Type()
)
aclAceLogProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceLogProtocol.setStatus("current")
_AclAceLogSrcPort_Type = Unsigned32
_AclAceLogSrcPort_Object = MibTableColumn
aclAceLogSrcPort = _AclAceLogSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 6),
    _AclAceLogSrcPort_Type()
)
aclAceLogSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceLogSrcPort.setStatus("current")
_AclAceLogDstPort_Type = Unsigned32
_AclAceLogDstPort_Object = MibTableColumn
aclAceLogDstPort = _AclAceLogDstPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 7),
    _AclAceLogDstPort_Type()
)
aclAceLogDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceLogDstPort.setStatus("current")
_AclAceLogIpProtocol_Type = Unsigned32
_AclAceLogIpProtocol_Object = MibTableColumn
aclAceLogIpProtocol = _AclAceLogIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 2, 2, 2, 1, 8),
    _AclAceLogIpProtocol_Type()
)
aclAceLogIpProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclAceLogIpProtocol.setStatus("current")

# Managed Objects groups


# Notification objects

systemAclLogging = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 0, 89)
)
systemAclLogging.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("SNMPv2-MIB", "sysName"),
        ("RAD-ACL-MIB", "aclBindAclName"),
        ("RAD-ACL-MIB", "aclAceSequenceNumber"),
        ("RAD-ACL-MIB", "aclAceType"),
        ("RAD-ACL-MIB", "aclAceStatsMatches"),
        ("RAD-ACL-MIB", "aclAceLogIPSrcAddress"),
        ("RAD-ACL-MIB", "aclAceLogIPDstAddress"),
        ("RAD-ACL-MIB", "aclAceLogProtocol"),
        ("RAD-ACL-MIB", "aclAceLogSrcPort"),
        ("RAD-ACL-MIB", "aclAceLogDstPort"),
        ("RAD-ACL-MIB", "aclAceLogIpProtocol"))
)
if mibBuilder.loadTexts:
    systemAclLogging.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-ACL-MIB",
    **{"AceMarkingType": AceMarkingType,
       "DscpMark": DscpMark,
       "IpPrecedenceMark": IpPrecedenceMark,
       "PbitMark": PbitMark,
       "UdpTcpPortOp": UdpTcpPortOp,
       "systemAclLogging": systemAclLogging,
       "radAclMIB": radAclMIB,
       "aclConf": aclConf,
       "aclMainTable": aclMainTable,
       "aclMainEntry": aclMainEntry,
       "aclName": aclName,
       "aclNumberOfAce": aclNumberOfAce,
       "aclLastSeqeunceNumber": aclLastSeqeunceNumber,
       "aclResequenceCmd": aclResequenceCmd,
       "aclType": aclType,
       "aclIllegalEntityTypes": aclIllegalEntityTypes,
       "aclRowStatus": aclRowStatus,
       "aclAceTable": aclAceTable,
       "aclAceEntry": aclAceEntry,
       "aclAceIdx": aclAceIdx,
       "aclAceSequenceNumber": aclAceSequenceNumber,
       "aclAceType": aclAceType,
       "aclAcePointer": aclAcePointer,
       "aclAcelog": aclAcelog,
       "aclAceIllegalEntityTypes": aclAceIllegalEntityTypes,
       "aclAceAclName": aclAceAclName,
       "aclAceRowStatus": aclAceRowStatus,
       "aclAceRemarkTable": aclAceRemarkTable,
       "aclAceRemarkEntry": aclAceRemarkEntry,
       "aclAceRemark": aclAceRemark,
       "aclAceIPTable": aclAceIPTable,
       "aclAceIPEntry": aclAceIPEntry,
       "aclAceIPSrcAddressType": aclAceIPSrcAddressType,
       "aclAceIPSrcAddress": aclAceIPSrcAddress,
       "aclAceIPSrcAddressPrefixLength": aclAceIPSrcAddressPrefixLength,
       "aclAceIPDstAddressType": aclAceIPDstAddressType,
       "aclAceIPDstAddress": aclAceIPDstAddress,
       "aclAceIPDstAddressPrefixLength": aclAceIPDstAddressPrefixLength,
       "aclAceIPMarkingType": aclAceIPMarkingType,
       "aclAceIPDscp": aclAceIPDscp,
       "aclAceIPIpPrecedence": aclAceIPIpPrecedence,
       "aclAceIPProtocolNumber": aclAceIPProtocolNumber,
       "aclAceIPSetMarkingType": aclAceIPSetMarkingType,
       "aclAceIPSetDscp": aclAceIPSetDscp,
       "aclAceIPSetIpPrecedence": aclAceIPSetIpPrecedence,
       "aclAceIPSetPbit": aclAceIPSetPbit,
       "aclAceICMPTable": aclAceICMPTable,
       "aclAceICMPEntry": aclAceICMPEntry,
       "aclAceICMPSrcAddressType": aclAceICMPSrcAddressType,
       "aclAceICMPSrcAddress": aclAceICMPSrcAddress,
       "aclAceICMPSrcAddressPrefixLength": aclAceICMPSrcAddressPrefixLength,
       "aclAceICMPDstAddressType": aclAceICMPDstAddressType,
       "aclAceICMPDstAddress": aclAceICMPDstAddress,
       "aclAceICMPDstAddressPrefixLength": aclAceICMPDstAddressPrefixLength,
       "aclAceICMPMarkingType": aclAceICMPMarkingType,
       "aclAceICMPDscp": aclAceICMPDscp,
       "aclAceICMPIpPrecedence": aclAceICMPIpPrecedence,
       "aclAceICMPType": aclAceICMPType,
       "aclAceICMPCode": aclAceICMPCode,
       "aclAceICMPSetMarkingType": aclAceICMPSetMarkingType,
       "aclAceICMPSetDscp": aclAceICMPSetDscp,
       "aclAceICMPSetIpPrecedence": aclAceICMPSetIpPrecedence,
       "aclAceICMPSetPbit": aclAceICMPSetPbit,
       "aclAceTCPTable": aclAceTCPTable,
       "aclAceTCPEntry": aclAceTCPEntry,
       "aclAceTCPSrcAddressType": aclAceTCPSrcAddressType,
       "aclAceTCPSrcAddress": aclAceTCPSrcAddress,
       "aclAceTCPSrcAddressPrefixLength": aclAceTCPSrcAddressPrefixLength,
       "aclAceTCPDstAddressType": aclAceTCPDstAddressType,
       "aclAceTCPDstAddress": aclAceTCPDstAddress,
       "aclAceTCPDstAddressPrefixLength": aclAceTCPDstAddressPrefixLength,
       "aclAceTCPMarkingType": aclAceTCPMarkingType,
       "aclAceTCPDscp": aclAceTCPDscp,
       "aclAceTCPIpPrecedence": aclAceTCPIpPrecedence,
       "aclAceTCPSrcPortOp": aclAceTCPSrcPortOp,
       "aclAceTCPSrcPort": aclAceTCPSrcPort,
       "aclAceTCPSrcPortRange": aclAceTCPSrcPortRange,
       "aclAceTCPDstPortOp": aclAceTCPDstPortOp,
       "aclAceTCPDstPort": aclAceTCPDstPort,
       "aclAceTCPDstPortRange": aclAceTCPDstPortRange,
       "aclAceTCPSetMarkingType": aclAceTCPSetMarkingType,
       "aclAceTCPSetDscp": aclAceTCPSetDscp,
       "aclAceTCPSetIpPrecedence": aclAceTCPSetIpPrecedence,
       "aclAceTCPSetPbit": aclAceTCPSetPbit,
       "aclAceUDPTable": aclAceUDPTable,
       "aclAceUDPEntry": aclAceUDPEntry,
       "aclAceUDPSrcAddressType": aclAceUDPSrcAddressType,
       "aclAceUDPSrcAddress": aclAceUDPSrcAddress,
       "aclAceUDPSrcAddressPrefixLength": aclAceUDPSrcAddressPrefixLength,
       "aclAceUDPDstAddressType": aclAceUDPDstAddressType,
       "aclAceUDPDstAddress": aclAceUDPDstAddress,
       "aclAceUDPDstAddressPrefixLength": aclAceUDPDstAddressPrefixLength,
       "aclAceUDPMarkingType": aclAceUDPMarkingType,
       "aclAceUDPDscp": aclAceUDPDscp,
       "aclAceUDPIpPrecedence": aclAceUDPIpPrecedence,
       "aclAceUDPSrcPortOp": aclAceUDPSrcPortOp,
       "aclAceUDPSrcPort": aclAceUDPSrcPort,
       "aclAceUDPSrcPortRange": aclAceUDPSrcPortRange,
       "aclAceUDPDstPortOp": aclAceUDPDstPortOp,
       "aclAceUDPDstPort": aclAceUDPDstPort,
       "aclAceUDPDstPortRange": aclAceUDPDstPortRange,
       "aclAceUDPSetMarkingType": aclAceUDPSetMarkingType,
       "aclAceUDPSetDscp": aclAceUDPSetDscp,
       "aclAceUDPSetIpPrecedence": aclAceUDPSetIpPrecedence,
       "aclAceUDPSetPbit": aclAceUDPSetPbit,
       "aclBindTable": aclBindTable,
       "aclBindEntry": aclBindEntry,
       "aclBindEntityType": aclBindEntityType,
       "aclBindEntityIndex": aclBindEntityIndex,
       "aclBindDirection": aclBindDirection,
       "aclBindAclType": aclBindAclType,
       "aclBindAclName": aclBindAclName,
       "aclBindTimeElapsed": aclBindTimeElapsed,
       "aclBindClearStatisticsCmd": aclBindClearStatisticsCmd,
       "aclBindRowStatus": aclBindRowStatus,
       "aclHandleTable": aclHandleTable,
       "aclHandleEntry": aclHandleEntry,
       "aclHandleIndex": aclHandleIndex,
       "aclLoggingIntervel": aclLoggingIntervel,
       "aclInvAceTable": aclInvAceTable,
       "aclInvAceEntry": aclInvAceEntry,
       "aclInvAceIdx": aclInvAceIdx,
       "aclInvAceType": aclInvAceType,
       "aclInvAcePointer": aclInvAcePointer,
       "aclInvAcelog": aclInvAcelog,
       "aclStats": aclStats,
       "aclAceStatsTable": aclAceStatsTable,
       "aclAceStatsEntry": aclAceStatsEntry,
       "aclAceStatsMatches": aclAceStatsMatches,
       "aclAceStatsClearCmd": aclAceStatsClearCmd,
       "aclAceLogTable": aclAceLogTable,
       "aclAceLogEntry": aclAceLogEntry,
       "aclAceLogIndex": aclAceLogIndex,
       "aclAceLogIPAddressType": aclAceLogIPAddressType,
       "aclAceLogIPSrcAddress": aclAceLogIPSrcAddress,
       "aclAceLogIPDstAddress": aclAceLogIPDstAddress,
       "aclAceLogProtocol": aclAceLogProtocol,
       "aclAceLogSrcPort": aclAceLogSrcPort,
       "aclAceLogDstPort": aclAceLogDstPort,
       "aclAceLogIpProtocol": aclAceLogIpProtocol}
)
