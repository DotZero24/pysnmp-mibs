# SNMP MIB module (MPACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MPACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:08 2025
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

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

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
 ObjectName,
 ObjectSyntax,
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
    "ObjectName",
    "ObjectSyntax",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

mpAclMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpAclConf_ObjectIdentity = ObjectIdentity
mpAclConf = _MpAclConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5)
)
_MpAclStdTable_Object = MibTable
mpAclStdTable = _MpAclStdTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10)
)
if mibBuilder.loadTexts:
    mpAclStdTable.setStatus("current")
_MpAclStdEntry_Object = MibTableRow
mpAclStdEntry = _MpAclStdEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1)
)
mpAclStdEntry.setIndexNames(
    (0, "MPACL-MIB", "aclStdName"),
    (0, "MPACL-MIB", "aclStdSequence"),
)
if mibBuilder.loadTexts:
    mpAclStdEntry.setStatus("current")


class _AclStdName_Type(DisplayString):
    """Custom type aclStdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclStdName_Type.__name__ = "DisplayString"
_AclStdName_Object = MibTableColumn
aclStdName = _AclStdName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 1),
    _AclStdName_Type()
)
aclStdName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStdName.setStatus("current")


class _AclStdSequence_Type(Integer32):
    """Custom type aclStdSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AclStdSequence_Type.__name__ = "Integer32"
_AclStdSequence_Object = MibTableColumn
aclStdSequence = _AclStdSequence_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 2),
    _AclStdSequence_Type()
)
aclStdSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStdSequence.setStatus("current")


class _AclStdType_Type(Integer32):
    """Custom type aclStdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("remark", 3))
    )


_AclStdType_Type.__name__ = "Integer32"
_AclStdType_Object = MibTableColumn
aclStdType = _AclStdType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 3),
    _AclStdType_Type()
)
aclStdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStdType.setStatus("current")
_AclStdSrcAddr_Type = IpAddress
_AclStdSrcAddr_Object = MibTableColumn
aclStdSrcAddr = _AclStdSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 4),
    _AclStdSrcAddr_Type()
)
aclStdSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStdSrcAddr.setStatus("current")
_AclStdSrcWildcard_Type = IpAddress
_AclStdSrcWildcard_Object = MibTableColumn
aclStdSrcWildcard = _AclStdSrcWildcard_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 5),
    _AclStdSrcWildcard_Type()
)
aclStdSrcWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStdSrcWildcard.setStatus("current")


class _AclStdLogEnable_Type(Integer32):
    """Custom type aclStdLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AclStdLogEnable_Type.__name__ = "Integer32"
_AclStdLogEnable_Object = MibTableColumn
aclStdLogEnable = _AclStdLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 6),
    _AclStdLogEnable_Type()
)
aclStdLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStdLogEnable.setStatus("current")


class _AclStdTimeRngName_Type(DisplayString):
    """Custom type aclStdTimeRngName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AclStdTimeRngName_Type.__name__ = "DisplayString"
_AclStdTimeRngName_Object = MibTableColumn
aclStdTimeRngName = _AclStdTimeRngName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 8),
    _AclStdTimeRngName_Type()
)
aclStdTimeRngName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStdTimeRngName.setStatus("current")


class _AclStdRemark_Type(DisplayString):
    """Custom type aclStdRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_AclStdRemark_Type.__name__ = "DisplayString"
_AclStdRemark_Object = MibTableColumn
aclStdRemark = _AclStdRemark_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 9),
    _AclStdRemark_Type()
)
aclStdRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclStdRemark.setStatus("current")
_AclStdMatchPkts_Type = Counter64
_AclStdMatchPkts_Object = MibTableColumn
aclStdMatchPkts = _AclStdMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 10),
    _AclStdMatchPkts_Type()
)
aclStdMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclStdMatchPkts.setStatus("current")
_AclStdRowStatus_Type = RowStatus
_AclStdRowStatus_Object = MibTableColumn
aclStdRowStatus = _AclStdRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 10, 1, 12),
    _AclStdRowStatus_Type()
)
aclStdRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclStdRowStatus.setStatus("current")
_MpAclExtTable_Object = MibTable
mpAclExtTable = _MpAclExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20)
)
if mibBuilder.loadTexts:
    mpAclExtTable.setStatus("current")
_MpAclExtEntry_Object = MibTableRow
mpAclExtEntry = _MpAclExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1)
)
mpAclExtEntry.setIndexNames(
    (0, "MPACL-MIB", "aclExtName"),
    (0, "MPACL-MIB", "aclExtSequence"),
)
if mibBuilder.loadTexts:
    mpAclExtEntry.setStatus("current")


class _AclExtName_Type(DisplayString):
    """Custom type aclExtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_AclExtName_Type.__name__ = "DisplayString"
_AclExtName_Object = MibTableColumn
aclExtName = _AclExtName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 1),
    _AclExtName_Type()
)
aclExtName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExtName.setStatus("current")


class _AclExtSequence_Type(Integer32):
    """Custom type aclExtSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AclExtSequence_Type.__name__ = "Integer32"
_AclExtSequence_Object = MibTableColumn
aclExtSequence = _AclExtSequence_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 2),
    _AclExtSequence_Type()
)
aclExtSequence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExtSequence.setStatus("current")


class _AclExtType_Type(Integer32):
    """Custom type aclExtType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2),
          ("remark", 3),
          ("evaluate", 4))
    )


_AclExtType_Type.__name__ = "Integer32"
_AclExtType_Object = MibTableColumn
aclExtType = _AclExtType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 3),
    _AclExtType_Type()
)
aclExtType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtType.setStatus("current")


class _AclExtProtocol_Type(Integer32):
    """Custom type aclExtProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclExtProtocol_Type.__name__ = "Integer32"
_AclExtProtocol_Object = MibTableColumn
aclExtProtocol = _AclExtProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 4),
    _AclExtProtocol_Type()
)
aclExtProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtProtocol.setStatus("current")
_AclExtSrcAddr_Type = IpAddress
_AclExtSrcAddr_Object = MibTableColumn
aclExtSrcAddr = _AclExtSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 5),
    _AclExtSrcAddr_Type()
)
aclExtSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtSrcAddr.setStatus("current")
_AclExtSrcWildcard_Type = IpAddress
_AclExtSrcWildcard_Object = MibTableColumn
aclExtSrcWildcard = _AclExtSrcWildcard_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 6),
    _AclExtSrcWildcard_Type()
)
aclExtSrcWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtSrcWildcard.setStatus("current")
_AclExtDestAddr_Type = IpAddress
_AclExtDestAddr_Object = MibTableColumn
aclExtDestAddr = _AclExtDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 7),
    _AclExtDestAddr_Type()
)
aclExtDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtDestAddr.setStatus("current")
_AclExtDestWildcard_Type = IpAddress
_AclExtDestWildcard_Object = MibTableColumn
aclExtDestWildcard = _AclExtDestWildcard_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 8),
    _AclExtDestWildcard_Type()
)
aclExtDestWildcard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtDestWildcard.setStatus("current")


class _AclExtPrecedence_Type(Integer32):
    """Custom type aclExtPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AclExtPrecedence_Type.__name__ = "Integer32"
_AclExtPrecedence_Object = MibTableColumn
aclExtPrecedence = _AclExtPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 9),
    _AclExtPrecedence_Type()
)
aclExtPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtPrecedence.setStatus("current")


class _AclExtTos_Type(Integer32):
    """Custom type aclExtTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_AclExtTos_Type.__name__ = "Integer32"
_AclExtTos_Object = MibTableColumn
aclExtTos = _AclExtTos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 10),
    _AclExtTos_Type()
)
aclExtTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTos.setStatus("current")


class _AclExtIcmpMsgType_Type(Integer32):
    """Custom type aclExtIcmpMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclExtIcmpMsgType_Type.__name__ = "Integer32"
_AclExtIcmpMsgType_Object = MibTableColumn
aclExtIcmpMsgType = _AclExtIcmpMsgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 11),
    _AclExtIcmpMsgType_Type()
)
aclExtIcmpMsgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtIcmpMsgType.setStatus("current")


class _AclExtIcmpMsgCode_Type(Integer32):
    """Custom type aclExtIcmpMsgCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 255),
    )


_AclExtIcmpMsgCode_Type.__name__ = "Integer32"
_AclExtIcmpMsgCode_Object = MibTableColumn
aclExtIcmpMsgCode = _AclExtIcmpMsgCode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 12),
    _AclExtIcmpMsgCode_Type()
)
aclExtIcmpMsgCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtIcmpMsgCode.setStatus("current")


class _AclExtIgmpMsgType_Type(Integer32):
    """Custom type aclExtIgmpMsgType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 15),
    )


_AclExtIgmpMsgType_Type.__name__ = "Integer32"
_AclExtIgmpMsgType_Object = MibTableColumn
aclExtIgmpMsgType = _AclExtIgmpMsgType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 13),
    _AclExtIgmpMsgType_Type()
)
aclExtIgmpMsgType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtIgmpMsgType.setStatus("current")


class _AclExtTUSrcPortType_Type(Integer32):
    """Custom type aclExtTUSrcPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no-care", 0),
          ("eq", 1),
          ("gt", 2),
          ("lt", 3),
          ("neq", 4),
          ("range", 5),
          ("wildcard", 6))
    )


_AclExtTUSrcPortType_Type.__name__ = "Integer32"
_AclExtTUSrcPortType_Object = MibTableColumn
aclExtTUSrcPortType = _AclExtTUSrcPortType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 14),
    _AclExtTUSrcPortType_Type()
)
aclExtTUSrcPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTUSrcPortType.setStatus("current")


class _AclExtTUSrcPort_Type(Integer32):
    """Custom type aclExtTUSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclExtTUSrcPort_Type.__name__ = "Integer32"
_AclExtTUSrcPort_Object = MibTableColumn
aclExtTUSrcPort = _AclExtTUSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 15),
    _AclExtTUSrcPort_Type()
)
aclExtTUSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTUSrcPort.setStatus("current")


class _AclExtTUSrcEndPort_Type(Integer32):
    """Custom type aclExtTUSrcEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclExtTUSrcEndPort_Type.__name__ = "Integer32"
_AclExtTUSrcEndPort_Object = MibTableColumn
aclExtTUSrcEndPort = _AclExtTUSrcEndPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 16),
    _AclExtTUSrcEndPort_Type()
)
aclExtTUSrcEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTUSrcEndPort.setStatus("current")


class _AclExtTUDestPortType_Type(Integer32):
    """Custom type aclExtTUDestPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("no-care", 0),
          ("eq", 1),
          ("gt", 2),
          ("lt", 3),
          ("neq", 4),
          ("range", 5),
          ("wildcard", 6))
    )


_AclExtTUDestPortType_Type.__name__ = "Integer32"
_AclExtTUDestPortType_Object = MibTableColumn
aclExtTUDestPortType = _AclExtTUDestPortType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 17),
    _AclExtTUDestPortType_Type()
)
aclExtTUDestPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTUDestPortType.setStatus("current")


class _AclExtTUDestPort_Type(Integer32):
    """Custom type aclExtTUDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclExtTUDestPort_Type.__name__ = "Integer32"
_AclExtTUDestPort_Object = MibTableColumn
aclExtTUDestPort = _AclExtTUDestPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 18),
    _AclExtTUDestPort_Type()
)
aclExtTUDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTUDestPort.setStatus("current")


class _AclExtTUDestEndPort_Type(Integer32):
    """Custom type aclExtTUDestEndPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclExtTUDestEndPort_Type.__name__ = "Integer32"
_AclExtTUDestEndPort_Object = MibTableColumn
aclExtTUDestEndPort = _AclExtTUDestEndPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 19),
    _AclExtTUDestEndPort_Type()
)
aclExtTUDestEndPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTUDestEndPort.setStatus("current")


class _AclExtTcpFlag_Type(Integer32):
    """Custom type aclExtTcpFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 63),
    )


_AclExtTcpFlag_Type.__name__ = "Integer32"
_AclExtTcpFlag_Object = MibTableColumn
aclExtTcpFlag = _AclExtTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 20),
    _AclExtTcpFlag_Type()
)
aclExtTcpFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTcpFlag.setStatus("current")


class _AclExtLogEnable_Type(Integer32):
    """Custom type aclExtLogEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_AclExtLogEnable_Type.__name__ = "Integer32"
_AclExtLogEnable_Object = MibTableColumn
aclExtLogEnable = _AclExtLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 21),
    _AclExtLogEnable_Type()
)
aclExtLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtLogEnable.setStatus("current")


class _AclExtTimeRngName_Type(DisplayString):
    """Custom type aclExtTimeRngName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AclExtTimeRngName_Type.__name__ = "DisplayString"
_AclExtTimeRngName_Object = MibTableColumn
aclExtTimeRngName = _AclExtTimeRngName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 23),
    _AclExtTimeRngName_Type()
)
aclExtTimeRngName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtTimeRngName.setStatus("current")


class _AclExtReflectName_Type(DisplayString):
    """Custom type aclExtReflectName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AclExtReflectName_Type.__name__ = "DisplayString"
_AclExtReflectName_Object = MibTableColumn
aclExtReflectName = _AclExtReflectName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 24),
    _AclExtReflectName_Type()
)
aclExtReflectName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtReflectName.setStatus("current")


class _AclExtReflectTimeOut_Type(Integer32):
    """Custom type aclExtReflectTimeOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AclExtReflectTimeOut_Type.__name__ = "Integer32"
_AclExtReflectTimeOut_Object = MibTableColumn
aclExtReflectTimeOut = _AclExtReflectTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 25),
    _AclExtReflectTimeOut_Type()
)
aclExtReflectTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtReflectTimeOut.setStatus("current")


class _AclExtEvaluateName_Type(DisplayString):
    """Custom type aclExtEvaluateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AclExtEvaluateName_Type.__name__ = "DisplayString"
_AclExtEvaluateName_Object = MibTableColumn
aclExtEvaluateName = _AclExtEvaluateName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 26),
    _AclExtEvaluateName_Type()
)
aclExtEvaluateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtEvaluateName.setStatus("current")


class _AclExtRemark_Type(DisplayString):
    """Custom type aclExtRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 99),
    )


_AclExtRemark_Type.__name__ = "DisplayString"
_AclExtRemark_Object = MibTableColumn
aclExtRemark = _AclExtRemark_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 27),
    _AclExtRemark_Type()
)
aclExtRemark.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclExtRemark.setStatus("current")
_AclExtMatchPkts_Type = Counter64
_AclExtMatchPkts_Object = MibTableColumn
aclExtMatchPkts = _AclExtMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 28),
    _AclExtMatchPkts_Type()
)
aclExtMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclExtMatchPkts.setStatus("current")
_AclExtRowStatus_Type = RowStatus
_AclExtRowStatus_Object = MibTableColumn
aclExtRowStatus = _AclExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 30, 5, 20, 1, 30),
    _AclExtRowStatus_Type()
)
aclExtRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclExtRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MPACL-MIB",
    **{"mpAclMib": mpAclMib,
       "mpAclConf": mpAclConf,
       "mpAclStdTable": mpAclStdTable,
       "mpAclStdEntry": mpAclStdEntry,
       "aclStdName": aclStdName,
       "aclStdSequence": aclStdSequence,
       "aclStdType": aclStdType,
       "aclStdSrcAddr": aclStdSrcAddr,
       "aclStdSrcWildcard": aclStdSrcWildcard,
       "aclStdLogEnable": aclStdLogEnable,
       "aclStdTimeRngName": aclStdTimeRngName,
       "aclStdRemark": aclStdRemark,
       "aclStdMatchPkts": aclStdMatchPkts,
       "aclStdRowStatus": aclStdRowStatus,
       "mpAclExtTable": mpAclExtTable,
       "mpAclExtEntry": mpAclExtEntry,
       "aclExtName": aclExtName,
       "aclExtSequence": aclExtSequence,
       "aclExtType": aclExtType,
       "aclExtProtocol": aclExtProtocol,
       "aclExtSrcAddr": aclExtSrcAddr,
       "aclExtSrcWildcard": aclExtSrcWildcard,
       "aclExtDestAddr": aclExtDestAddr,
       "aclExtDestWildcard": aclExtDestWildcard,
       "aclExtPrecedence": aclExtPrecedence,
       "aclExtTos": aclExtTos,
       "aclExtIcmpMsgType": aclExtIcmpMsgType,
       "aclExtIcmpMsgCode": aclExtIcmpMsgCode,
       "aclExtIgmpMsgType": aclExtIgmpMsgType,
       "aclExtTUSrcPortType": aclExtTUSrcPortType,
       "aclExtTUSrcPort": aclExtTUSrcPort,
       "aclExtTUSrcEndPort": aclExtTUSrcEndPort,
       "aclExtTUDestPortType": aclExtTUDestPortType,
       "aclExtTUDestPort": aclExtTUDestPort,
       "aclExtTUDestEndPort": aclExtTUDestEndPort,
       "aclExtTcpFlag": aclExtTcpFlag,
       "aclExtLogEnable": aclExtLogEnable,
       "aclExtTimeRngName": aclExtTimeRngName,
       "aclExtReflectName": aclExtReflectName,
       "aclExtReflectTimeOut": aclExtReflectTimeOut,
       "aclExtEvaluateName": aclExtEvaluateName,
       "aclExtRemark": aclExtRemark,
       "aclExtMatchPkts": aclExtMatchPkts,
       "aclExtRowStatus": aclExtRowStatus}
)
