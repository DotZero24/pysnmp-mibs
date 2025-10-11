# SNMP MIB module (QTECH-GBNL2QACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-GBNL2QACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:53 2025
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

(TOSType,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "TOSType")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId")

(gbnL2,) = mibBuilder.importSymbols(
    "QTECH-MASTER-MIB",
    "gbnL2")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

gbnL2QACL = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4)
)
if mibBuilder.loadTexts:
    gbnL2QACL.setRevisions(
        ("1903-09-26 00:01",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdminStatus(TextualConvention, Integer32):
    status = "current"
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



class Action(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              101)
        )
    )
    namedValues = NamedValues(
        *(("deny", 100),
          ("permit", 101))
    )



class Dscp(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )



class AclType(TextualConvention, Integer32):
    status = "current"
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
        *(("standard", 1),
          ("extend", 2),
          ("link", 3),
          ("user", 4))
    )



class PacketFlowType(TextualConvention, Integer32):
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
        *(("broadcast", 1),
          ("multicast", 2),
          ("unicast", 3))
    )



# MIB Managed Objects in the order of their OIDs

_QosQueueSchedulerGroup_ObjectIdentity = ObjectIdentity
qosQueueSchedulerGroup = _QosQueueSchedulerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1)
)


class _QosWrrQueue1Weight_Type(Integer32):
    """Custom type qosWrrQueue1Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue1Weight_Type.__name__ = "Integer32"
_QosWrrQueue1Weight_Object = MibScalar
qosWrrQueue1Weight = _QosWrrQueue1Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 1),
    _QosWrrQueue1Weight_Type()
)
qosWrrQueue1Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue1Weight.setStatus("current")


class _QosWrrQueue2Weight_Type(Integer32):
    """Custom type qosWrrQueue2Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue2Weight_Type.__name__ = "Integer32"
_QosWrrQueue2Weight_Object = MibScalar
qosWrrQueue2Weight = _QosWrrQueue2Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 2),
    _QosWrrQueue2Weight_Type()
)
qosWrrQueue2Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue2Weight.setStatus("current")


class _QosWrrQueue3Weight_Type(Integer32):
    """Custom type qosWrrQueue3Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue3Weight_Type.__name__ = "Integer32"
_QosWrrQueue3Weight_Object = MibScalar
qosWrrQueue3Weight = _QosWrrQueue3Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 3),
    _QosWrrQueue3Weight_Type()
)
qosWrrQueue3Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue3Weight.setStatus("current")


class _QosWrrQueue4Weight_Type(Integer32):
    """Custom type qosWrrQueue4Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue4Weight_Type.__name__ = "Integer32"
_QosWrrQueue4Weight_Object = MibScalar
qosWrrQueue4Weight = _QosWrrQueue4Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 4),
    _QosWrrQueue4Weight_Type()
)
qosWrrQueue4Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue4Weight.setStatus("current")


class _QosWrrMaxDelayValue_Type(Integer32):
    """Custom type qosWrrMaxDelayValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_QosWrrMaxDelayValue_Type.__name__ = "Integer32"
_QosWrrMaxDelayValue_Object = MibScalar
qosWrrMaxDelayValue = _QosWrrMaxDelayValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 5),
    _QosWrrMaxDelayValue_Type()
)
qosWrrMaxDelayValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrMaxDelayValue.setStatus("current")


class _QosQueueSchedulerMode_Type(Integer32):
    """Custom type qosQueueSchedulerMode based on Integer32"""
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
        *(("strictPriority", 1),
          ("wrr", 2),
          ("wrrMaxDelay", 3))
    )


_QosQueueSchedulerMode_Type.__name__ = "Integer32"
_QosQueueSchedulerMode_Object = MibScalar
qosQueueSchedulerMode = _QosQueueSchedulerMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 6),
    _QosQueueSchedulerMode_Type()
)
qosQueueSchedulerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosQueueSchedulerMode.setStatus("current")


class _QosWrrQueue5Weight_Type(Integer32):
    """Custom type qosWrrQueue5Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue5Weight_Type.__name__ = "Integer32"
_QosWrrQueue5Weight_Object = MibScalar
qosWrrQueue5Weight = _QosWrrQueue5Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 7),
    _QosWrrQueue5Weight_Type()
)
qosWrrQueue5Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue5Weight.setStatus("current")


class _QosWrrQueue6Weight_Type(Integer32):
    """Custom type qosWrrQueue6Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue6Weight_Type.__name__ = "Integer32"
_QosWrrQueue6Weight_Object = MibScalar
qosWrrQueue6Weight = _QosWrrQueue6Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 8),
    _QosWrrQueue6Weight_Type()
)
qosWrrQueue6Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue6Weight.setStatus("current")


class _QosWrrQueue7Weight_Type(Integer32):
    """Custom type qosWrrQueue7Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue7Weight_Type.__name__ = "Integer32"
_QosWrrQueue7Weight_Object = MibScalar
qosWrrQueue7Weight = _QosWrrQueue7Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 9),
    _QosWrrQueue7Weight_Type()
)
qosWrrQueue7Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue7Weight.setStatus("current")


class _QosWrrQueue8Weight_Type(Integer32):
    """Custom type qosWrrQueue8Weight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 97),
    )


_QosWrrQueue8Weight_Type.__name__ = "Integer32"
_QosWrrQueue8Weight_Object = MibScalar
qosWrrQueue8Weight = _QosWrrQueue8Weight_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 1, 10),
    _QosWrrQueue8Weight_Type()
)
qosWrrQueue8Weight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosWrrQueue8Weight.setStatus("current")
_AclNumTable_Object = MibTable
aclNumTable = _AclNumTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    aclNumTable.setStatus("current")
_AclNumEntry_Object = MibTableRow
aclNumEntry = _AclNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 2, 1)
)
aclNumEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNumNumber"),
)
if mibBuilder.loadTexts:
    aclNumEntry.setStatus("current")
_AclNumNumber_Type = Integer32
_AclNumNumber_Object = MibTableColumn
aclNumNumber = _AclNumNumber_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 2, 1, 1),
    _AclNumNumber_Type()
)
aclNumNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumNumber.setStatus("current")
_AclNumType_Type = AclType
_AclNumType_Object = MibTableColumn
aclNumType = _AclNumType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 2, 1, 2),
    _AclNumType_Type()
)
aclNumType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumType.setStatus("current")


class _AclNumMatchOrder_Type(Integer32):
    """Custom type aclNumMatchOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("config", 0),
          ("auto", 1))
    )


_AclNumMatchOrder_Type.__name__ = "Integer32"
_AclNumMatchOrder_Object = MibTableColumn
aclNumMatchOrder = _AclNumMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 2, 1, 3),
    _AclNumMatchOrder_Type()
)
aclNumMatchOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumMatchOrder.setStatus("current")
_AclNumTotleSubitems_Type = Integer32
_AclNumTotleSubitems_Object = MibTableColumn
aclNumTotleSubitems = _AclNumTotleSubitems_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 2, 1, 4),
    _AclNumTotleSubitems_Type()
)
aclNumTotleSubitems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumTotleSubitems.setStatus("current")
_AclNumRowStatus_Type = RowStatus
_AclNumRowStatus_Object = MibTableColumn
aclNumRowStatus = _AclNumRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 2, 1, 5),
    _AclNumRowStatus_Type()
)
aclNumRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumRowStatus.setStatus("current")
_AclNumStdSubitemTable_Object = MibTable
aclNumStdSubitemTable = _AclNumStdSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3)
)
if mibBuilder.loadTexts:
    aclNumStdSubitemTable.setStatus("current")
_AclNumStdSubitemEntry_Object = MibTableRow
aclNumStdSubitemEntry = _AclNumStdSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1)
)
aclNumStdSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNumStdNum"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNumStdSubNum"),
)
if mibBuilder.loadTexts:
    aclNumStdSubitemEntry.setStatus("current")


class _AclNumStdNum_Type(Integer32):
    """Custom type aclNumStdNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_AclNumStdNum_Type.__name__ = "Integer32"
_AclNumStdNum_Object = MibTableColumn
aclNumStdNum = _AclNumStdNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 1),
    _AclNumStdNum_Type()
)
aclNumStdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumStdNum.setStatus("current")


class _AclNumStdSubNum_Type(Integer32):
    """Custom type aclNumStdSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNumStdSubNum_Type.__name__ = "Integer32"
_AclNumStdSubNum_Object = MibTableColumn
aclNumStdSubNum = _AclNumStdSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 2),
    _AclNumStdSubNum_Type()
)
aclNumStdSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumStdSubNum.setStatus("current")
_AclNumStdSubitemAdminStatus_Type = AdminStatus
_AclNumStdSubitemAdminStatus_Object = MibTableColumn
aclNumStdSubitemAdminStatus = _AclNumStdSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 3),
    _AclNumStdSubitemAdminStatus_Type()
)
aclNumStdSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumStdSubitemAdminStatus.setStatus("current")
_AclNumStdSubitemAction_Type = Action
_AclNumStdSubitemAction_Object = MibTableColumn
aclNumStdSubitemAction = _AclNumStdSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 4),
    _AclNumStdSubitemAction_Type()
)
aclNumStdSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumStdSubitemAction.setStatus("current")
_AclNumStdSubitemSrcAddr_Type = IpAddress
_AclNumStdSubitemSrcAddr_Object = MibTableColumn
aclNumStdSubitemSrcAddr = _AclNumStdSubitemSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 5),
    _AclNumStdSubitemSrcAddr_Type()
)
aclNumStdSubitemSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumStdSubitemSrcAddr.setStatus("current")
_AclNumStdSubitemSrcAddrWldmsk_Type = IpAddress
_AclNumStdSubitemSrcAddrWldmsk_Object = MibTableColumn
aclNumStdSubitemSrcAddrWldmsk = _AclNumStdSubitemSrcAddrWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 6),
    _AclNumStdSubitemSrcAddrWldmsk_Type()
)
aclNumStdSubitemSrcAddrWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumStdSubitemSrcAddrWldmsk.setStatus("current")


class _AclNumStdFragments_Type(TruthValue):
    """Custom type aclNumStdFragments based on TruthValue"""
    defaultValue = 2


_AclNumStdFragments_Type.__name__ = "TruthValue"
_AclNumStdFragments_Object = MibTableColumn
aclNumStdFragments = _AclNumStdFragments_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 7),
    _AclNumStdFragments_Type()
)
aclNumStdFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumStdFragments.setStatus("current")


class _AclNumStdTimeRange_Type(OctetString):
    """Custom type aclNumStdTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNumStdTimeRange_Type.__name__ = "OctetString"
_AclNumStdTimeRange_Object = MibTableColumn
aclNumStdTimeRange = _AclNumStdTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 8),
    _AclNumStdTimeRange_Type()
)
aclNumStdTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumStdTimeRange.setStatus("current")
_AclNumStdSubitemRowStatus_Type = RowStatus
_AclNumStdSubitemRowStatus_Object = MibTableColumn
aclNumStdSubitemRowStatus = _AclNumStdSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 3, 1, 9),
    _AclNumStdSubitemRowStatus_Type()
)
aclNumStdSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumStdSubitemRowStatus.setStatus("current")
_AclNumExdSubitemTable_Object = MibTable
aclNumExdSubitemTable = _AclNumExdSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4)
)
if mibBuilder.loadTexts:
    aclNumExdSubitemTable.setStatus("current")
_AclNumExdSubitemEntry_Object = MibTableRow
aclNumExdSubitemEntry = _AclNumExdSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1)
)
aclNumExdSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNumExdNum"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNumExdSubNum"),
)
if mibBuilder.loadTexts:
    aclNumExdSubitemEntry.setStatus("current")


class _AclNumExdNum_Type(Integer32):
    """Custom type aclNumExdNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 199),
    )


_AclNumExdNum_Type.__name__ = "Integer32"
_AclNumExdNum_Object = MibTableColumn
aclNumExdNum = _AclNumExdNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 1),
    _AclNumExdNum_Type()
)
aclNumExdNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumExdNum.setStatus("current")


class _AclNumExdSubNum_Type(Integer32):
    """Custom type aclNumExdSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNumExdSubNum_Type.__name__ = "Integer32"
_AclNumExdSubNum_Object = MibTableColumn
aclNumExdSubNum = _AclNumExdSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 2),
    _AclNumExdSubNum_Type()
)
aclNumExdSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumExdSubNum.setStatus("current")
_AclNumExdSubitemAdminStatus_Type = AdminStatus
_AclNumExdSubitemAdminStatus_Object = MibTableColumn
aclNumExdSubitemAdminStatus = _AclNumExdSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 3),
    _AclNumExdSubitemAdminStatus_Type()
)
aclNumExdSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumExdSubitemAdminStatus.setStatus("current")
_AclNumExdSubitemAction_Type = Action
_AclNumExdSubitemAction_Object = MibTableColumn
aclNumExdSubitemAction = _AclNumExdSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 4),
    _AclNumExdSubitemAction_Type()
)
aclNumExdSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemAction.setStatus("current")


class _AclNumExdSubitemProtocal_Type(Integer32):
    """Custom type aclNumExdSubitemProtocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclNumExdSubitemProtocal_Type.__name__ = "Integer32"
_AclNumExdSubitemProtocal_Object = MibTableColumn
aclNumExdSubitemProtocal = _AclNumExdSubitemProtocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 5),
    _AclNumExdSubitemProtocal_Type()
)
aclNumExdSubitemProtocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemProtocal.setStatus("current")
_AclNumExdSubitemSrcAddr_Type = IpAddress
_AclNumExdSubitemSrcAddr_Object = MibTableColumn
aclNumExdSubitemSrcAddr = _AclNumExdSubitemSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 6),
    _AclNumExdSubitemSrcAddr_Type()
)
aclNumExdSubitemSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemSrcAddr.setStatus("current")
_AclNumExdSubitemSrcAddrWldmsk_Type = IpAddress
_AclNumExdSubitemSrcAddrWldmsk_Object = MibTableColumn
aclNumExdSubitemSrcAddrWldmsk = _AclNumExdSubitemSrcAddrWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 7),
    _AclNumExdSubitemSrcAddrWldmsk_Type()
)
aclNumExdSubitemSrcAddrWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemSrcAddrWldmsk.setStatus("current")
_AclNumExdSubitemDstAddr_Type = IpAddress
_AclNumExdSubitemDstAddr_Object = MibTableColumn
aclNumExdSubitemDstAddr = _AclNumExdSubitemDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 8),
    _AclNumExdSubitemDstAddr_Type()
)
aclNumExdSubitemDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemDstAddr.setStatus("current")
_AclNumExdSubitemDstAddrWldmsk_Type = IpAddress
_AclNumExdSubitemDstAddrWldmsk_Object = MibTableColumn
aclNumExdSubitemDstAddrWldmsk = _AclNumExdSubitemDstAddrWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 9),
    _AclNumExdSubitemDstAddrWldmsk_Type()
)
aclNumExdSubitemDstAddrWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemDstAddrWldmsk.setStatus("current")


class _AclNumExdSubitemSrcPort_Type(Integer32):
    """Custom type aclNumExdSubitemSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNumExdSubitemSrcPort_Type.__name__ = "Integer32"
_AclNumExdSubitemSrcPort_Object = MibTableColumn
aclNumExdSubitemSrcPort = _AclNumExdSubitemSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 10),
    _AclNumExdSubitemSrcPort_Type()
)
aclNumExdSubitemSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemSrcPort.setStatus("current")


class _AclNumExdSubitemSrcPortWldmsk_Type(Integer32):
    """Custom type aclNumExdSubitemSrcPortWldmsk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNumExdSubitemSrcPortWldmsk_Type.__name__ = "Integer32"
_AclNumExdSubitemSrcPortWldmsk_Object = MibTableColumn
aclNumExdSubitemSrcPortWldmsk = _AclNumExdSubitemSrcPortWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 11),
    _AclNumExdSubitemSrcPortWldmsk_Type()
)
aclNumExdSubitemSrcPortWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemSrcPortWldmsk.setStatus("current")


class _AclNumExdSubitemDstPort_Type(Integer32):
    """Custom type aclNumExdSubitemDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNumExdSubitemDstPort_Type.__name__ = "Integer32"
_AclNumExdSubitemDstPort_Object = MibTableColumn
aclNumExdSubitemDstPort = _AclNumExdSubitemDstPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 12),
    _AclNumExdSubitemDstPort_Type()
)
aclNumExdSubitemDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemDstPort.setStatus("current")


class _AclNumExdSubitemDstPortWldmsk_Type(Integer32):
    """Custom type aclNumExdSubitemDstPortWldmsk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNumExdSubitemDstPortWldmsk_Type.__name__ = "Integer32"
_AclNumExdSubitemDstPortWldmsk_Object = MibTableColumn
aclNumExdSubitemDstPortWldmsk = _AclNumExdSubitemDstPortWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 13),
    _AclNumExdSubitemDstPortWldmsk_Type()
)
aclNumExdSubitemDstPortWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemDstPortWldmsk.setStatus("current")


class _AclNumExdSubitemIcmpType_Type(Integer32):
    """Custom type aclNumExdSubitemIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclNumExdSubitemIcmpType_Type.__name__ = "Integer32"
_AclNumExdSubitemIcmpType_Object = MibTableColumn
aclNumExdSubitemIcmpType = _AclNumExdSubitemIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 14),
    _AclNumExdSubitemIcmpType_Type()
)
aclNumExdSubitemIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemIcmpType.setStatus("current")


class _AclNumExdSubitemIcmpCode_Type(Integer32):
    """Custom type aclNumExdSubitemIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclNumExdSubitemIcmpCode_Type.__name__ = "Integer32"
_AclNumExdSubitemIcmpCode_Object = MibTableColumn
aclNumExdSubitemIcmpCode = _AclNumExdSubitemIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 15),
    _AclNumExdSubitemIcmpCode_Type()
)
aclNumExdSubitemIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemIcmpCode.setStatus("current")


class _AclNumExdSubitemTcpEstablished_Type(TruthValue):
    """Custom type aclNumExdSubitemTcpEstablished based on TruthValue"""
    defaultValue = 2


_AclNumExdSubitemTcpEstablished_Type.__name__ = "TruthValue"
_AclNumExdSubitemTcpEstablished_Object = MibTableColumn
aclNumExdSubitemTcpEstablished = _AclNumExdSubitemTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 16),
    _AclNumExdSubitemTcpEstablished_Type()
)
aclNumExdSubitemTcpEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemTcpEstablished.setStatus("current")


class _AclNumExdSubitemPrecedence_Type(Integer32):
    """Custom type aclNumExdSubitemPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclNumExdSubitemPrecedence_Type.__name__ = "Integer32"
_AclNumExdSubitemPrecedence_Object = MibTableColumn
aclNumExdSubitemPrecedence = _AclNumExdSubitemPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 17),
    _AclNumExdSubitemPrecedence_Type()
)
aclNumExdSubitemPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemPrecedence.setStatus("current")
_AclNumExdSubitemTos_Type = TOSType
_AclNumExdSubitemTos_Object = MibTableColumn
aclNumExdSubitemTos = _AclNumExdSubitemTos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 18),
    _AclNumExdSubitemTos_Type()
)
aclNumExdSubitemTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemTos.setStatus("current")
_AclNumExdSubitemDscp_Type = Dscp
_AclNumExdSubitemDscp_Object = MibTableColumn
aclNumExdSubitemDscp = _AclNumExdSubitemDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 19),
    _AclNumExdSubitemDscp_Type()
)
aclNumExdSubitemDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemDscp.setStatus("current")


class _AclNumExdSubitemFragments_Type(TruthValue):
    """Custom type aclNumExdSubitemFragments based on TruthValue"""
    defaultValue = 2


_AclNumExdSubitemFragments_Type.__name__ = "TruthValue"
_AclNumExdSubitemFragments_Object = MibTableColumn
aclNumExdSubitemFragments = _AclNumExdSubitemFragments_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 20),
    _AclNumExdSubitemFragments_Type()
)
aclNumExdSubitemFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemFragments.setStatus("current")


class _AclNumExdSubitemTimeRange_Type(OctetString):
    """Custom type aclNumExdSubitemTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNumExdSubitemTimeRange_Type.__name__ = "OctetString"
_AclNumExdSubitemTimeRange_Object = MibTableColumn
aclNumExdSubitemTimeRange = _AclNumExdSubitemTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 21),
    _AclNumExdSubitemTimeRange_Type()
)
aclNumExdSubitemTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemTimeRange.setStatus("current")
_AclNumExdSubitemRowStatus_Type = RowStatus
_AclNumExdSubitemRowStatus_Object = MibTableColumn
aclNumExdSubitemRowStatus = _AclNumExdSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 4, 1, 22),
    _AclNumExdSubitemRowStatus_Type()
)
aclNumExdSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumExdSubitemRowStatus.setStatus("current")
_AclNumLnkSubitemTable_Object = MibTable
aclNumLnkSubitemTable = _AclNumLnkSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5)
)
if mibBuilder.loadTexts:
    aclNumLnkSubitemTable.setStatus("current")
_AclNumLnkSubitemEntry_Object = MibTableRow
aclNumLnkSubitemEntry = _AclNumLnkSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1)
)
aclNumLnkSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNumLnkNum"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNumLnkSubNum"),
)
if mibBuilder.loadTexts:
    aclNumLnkSubitemEntry.setStatus("current")


class _AclNumLnkNum_Type(Integer32):
    """Custom type aclNumLnkNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 299),
    )


_AclNumLnkNum_Type.__name__ = "Integer32"
_AclNumLnkNum_Object = MibTableColumn
aclNumLnkNum = _AclNumLnkNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 1),
    _AclNumLnkNum_Type()
)
aclNumLnkNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumLnkNum.setStatus("current")


class _AclNumLnkSubNum_Type(Integer32):
    """Custom type aclNumLnkSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNumLnkSubNum_Type.__name__ = "Integer32"
_AclNumLnkSubNum_Object = MibTableColumn
aclNumLnkSubNum = _AclNumLnkSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 2),
    _AclNumLnkSubNum_Type()
)
aclNumLnkSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumLnkSubNum.setStatus("current")
_AclNumLnkSubitemAdminStatus_Type = AdminStatus
_AclNumLnkSubitemAdminStatus_Object = MibTableColumn
aclNumLnkSubitemAdminStatus = _AclNumLnkSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 3),
    _AclNumLnkSubitemAdminStatus_Type()
)
aclNumLnkSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumLnkSubitemAdminStatus.setStatus("current")
_AclNumLnkSubitemAction_Type = Action
_AclNumLnkSubitemAction_Object = MibTableColumn
aclNumLnkSubitemAction = _AclNumLnkSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 4),
    _AclNumLnkSubitemAction_Type()
)
aclNumLnkSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemAction.setStatus("current")


class _AclNumLnkSubitemProtocal_Type(Integer32):
    """Custom type aclNumLnkSubitemProtocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclNumLnkSubitemProtocal_Type.__name__ = "Integer32"
_AclNumLnkSubitemProtocal_Object = MibTableColumn
aclNumLnkSubitemProtocal = _AclNumLnkSubitemProtocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 5),
    _AclNumLnkSubitemProtocal_Type()
)
aclNumLnkSubitemProtocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemProtocal.setStatus("current")


class _AclNumLnkSubitemCos_Type(Integer32):
    """Custom type aclNumLnkSubitemCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclNumLnkSubitemCos_Type.__name__ = "Integer32"
_AclNumLnkSubitemCos_Object = MibTableColumn
aclNumLnkSubitemCos = _AclNumLnkSubitemCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 6),
    _AclNumLnkSubitemCos_Type()
)
aclNumLnkSubitemCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemCos.setStatus("current")
_AclNumLnkSubitemSrcVlanID_Type = VlanId
_AclNumLnkSubitemSrcVlanID_Object = MibTableColumn
aclNumLnkSubitemSrcVlanID = _AclNumLnkSubitemSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 7),
    _AclNumLnkSubitemSrcVlanID_Type()
)
aclNumLnkSubitemSrcVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemSrcVlanID.setStatus("current")
_AclNumLnkSubitemSrcMacAddr_Type = MacAddress
_AclNumLnkSubitemSrcMacAddr_Object = MibTableColumn
aclNumLnkSubitemSrcMacAddr = _AclNumLnkSubitemSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 8),
    _AclNumLnkSubitemSrcMacAddr_Type()
)
aclNumLnkSubitemSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemSrcMacAddr.setStatus("current")
_AclNumLnkSubitemSrcMacWldmsk_Type = MacAddress
_AclNumLnkSubitemSrcMacWldmsk_Object = MibTableColumn
aclNumLnkSubitemSrcMacWldmsk = _AclNumLnkSubitemSrcMacWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 9),
    _AclNumLnkSubitemSrcMacWldmsk_Type()
)
aclNumLnkSubitemSrcMacWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemSrcMacWldmsk.setStatus("current")
_AclNumLnkSubitemDstMacAddr_Type = MacAddress
_AclNumLnkSubitemDstMacAddr_Object = MibTableColumn
aclNumLnkSubitemDstMacAddr = _AclNumLnkSubitemDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 10),
    _AclNumLnkSubitemDstMacAddr_Type()
)
aclNumLnkSubitemDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemDstMacAddr.setStatus("current")
_AclNumLnkSubitemDstMacWldmsk_Type = MacAddress
_AclNumLnkSubitemDstMacWldmsk_Object = MibTableColumn
aclNumLnkSubitemDstMacWldmsk = _AclNumLnkSubitemDstMacWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 11),
    _AclNumLnkSubitemDstMacWldmsk_Type()
)
aclNumLnkSubitemDstMacWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemDstMacWldmsk.setStatus("current")


class _AclNumLnkSubitemSrcPortNum_Type(Integer32):
    """Custom type aclNumLnkSubitemSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_AclNumLnkSubitemSrcPortNum_Type.__name__ = "Integer32"
_AclNumLnkSubitemSrcPortNum_Object = MibTableColumn
aclNumLnkSubitemSrcPortNum = _AclNumLnkSubitemSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 12),
    _AclNumLnkSubitemSrcPortNum_Type()
)
aclNumLnkSubitemSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemSrcPortNum.setStatus("current")


class _AclNumLnkSubitemDstPortNum_Type(Integer32):
    """Custom type aclNumLnkSubitemDstPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 29),
    )


_AclNumLnkSubitemDstPortNum_Type.__name__ = "Integer32"
_AclNumLnkSubitemDstPortNum_Object = MibTableColumn
aclNumLnkSubitemDstPortNum = _AclNumLnkSubitemDstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 13),
    _AclNumLnkSubitemDstPortNum_Type()
)
aclNumLnkSubitemDstPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemDstPortNum.setStatus("current")


class _AclNumLnkSubitemTimeRange_Type(OctetString):
    """Custom type aclNumLnkSubitemTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNumLnkSubitemTimeRange_Type.__name__ = "OctetString"
_AclNumLnkSubitemTimeRange_Object = MibTableColumn
aclNumLnkSubitemTimeRange = _AclNumLnkSubitemTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 14),
    _AclNumLnkSubitemTimeRange_Type()
)
aclNumLnkSubitemTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemTimeRange.setStatus("current")
_AclNumLnkSubitemRowStatus_Type = RowStatus
_AclNumLnkSubitemRowStatus_Object = MibTableColumn
aclNumLnkSubitemRowStatus = _AclNumLnkSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 5, 1, 15),
    _AclNumLnkSubitemRowStatus_Type()
)
aclNumLnkSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumLnkSubitemRowStatus.setStatus("current")
_AclNumUserSubitemTable_Object = MibTable
aclNumUserSubitemTable = _AclNumUserSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6)
)
if mibBuilder.loadTexts:
    aclNumUserSubitemTable.setStatus("current")
_AclNumUserSubitemEntry_Object = MibTableRow
aclNumUserSubitemEntry = _AclNumUserSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1)
)
aclNumUserSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNumUserNum"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNumUserSubNum"),
)
if mibBuilder.loadTexts:
    aclNumUserSubitemEntry.setStatus("current")


class _AclNumUserNum_Type(Integer32):
    """Custom type aclNumUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 399),
    )


_AclNumUserNum_Type.__name__ = "Integer32"
_AclNumUserNum_Object = MibTableColumn
aclNumUserNum = _AclNumUserNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 1),
    _AclNumUserNum_Type()
)
aclNumUserNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumUserNum.setStatus("current")


class _AclNumUserSubNum_Type(Integer32):
    """Custom type aclNumUserSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNumUserSubNum_Type.__name__ = "Integer32"
_AclNumUserSubNum_Object = MibTableColumn
aclNumUserSubNum = _AclNumUserSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 2),
    _AclNumUserSubNum_Type()
)
aclNumUserSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumUserSubNum.setStatus("current")
_AclNumUserSubitemAdminStatus_Type = AdminStatus
_AclNumUserSubitemAdminStatus_Object = MibTableColumn
aclNumUserSubitemAdminStatus = _AclNumUserSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 3),
    _AclNumUserSubitemAdminStatus_Type()
)
aclNumUserSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNumUserSubitemAdminStatus.setStatus("current")
_AclNumUserSubitemAction_Type = Action
_AclNumUserSubitemAction_Object = MibTableColumn
aclNumUserSubitemAction = _AclNumUserSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 4),
    _AclNumUserSubitemAction_Type()
)
aclNumUserSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumUserSubitemAction.setStatus("current")
_AclNumUserSubitemSrcPortNum_Type = Integer32
_AclNumUserSubitemSrcPortNum_Object = MibTableColumn
aclNumUserSubitemSrcPortNum = _AclNumUserSubitemSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 5),
    _AclNumUserSubitemSrcPortNum_Type()
)
aclNumUserSubitemSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumUserSubitemSrcPortNum.setStatus("current")


class _AclNumUserSubitemDstPortNum_Type(Integer32):
    """Custom type aclNumUserSubitemDstPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 29),
    )


_AclNumUserSubitemDstPortNum_Type.__name__ = "Integer32"
_AclNumUserSubitemDstPortNum_Object = MibTableColumn
aclNumUserSubitemDstPortNum = _AclNumUserSubitemDstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 6),
    _AclNumUserSubitemDstPortNum_Type()
)
aclNumUserSubitemDstPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumUserSubitemDstPortNum.setStatus("current")


class _AclNumUserSubitemRule_Type(OctetString):
    """Custom type aclNumUserSubitemRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_AclNumUserSubitemRule_Type.__name__ = "OctetString"
_AclNumUserSubitemRule_Object = MibTableColumn
aclNumUserSubitemRule = _AclNumUserSubitemRule_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 7),
    _AclNumUserSubitemRule_Type()
)
aclNumUserSubitemRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumUserSubitemRule.setStatus("current")


class _AclNumUserSubitemMask_Type(OctetString):
    """Custom type aclNumUserSubitemMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_AclNumUserSubitemMask_Type.__name__ = "OctetString"
_AclNumUserSubitemMask_Object = MibTableColumn
aclNumUserSubitemMask = _AclNumUserSubitemMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 8),
    _AclNumUserSubitemMask_Type()
)
aclNumUserSubitemMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumUserSubitemMask.setStatus("current")


class _AclNumUserTimeRange_Type(OctetString):
    """Custom type aclNumUserTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNumUserTimeRange_Type.__name__ = "OctetString"
_AclNumUserTimeRange_Object = MibTableColumn
aclNumUserTimeRange = _AclNumUserTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 9),
    _AclNumUserTimeRange_Type()
)
aclNumUserTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumUserTimeRange.setStatus("current")
_AclNumUserSubitemRowStatus_Type = RowStatus
_AclNumUserSubitemRowStatus_Object = MibTableColumn
aclNumUserSubitemRowStatus = _AclNumUserSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 6, 1, 10),
    _AclNumUserSubitemRowStatus_Type()
)
aclNumUserSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNumUserSubitemRowStatus.setStatus("current")
_AclNamedTable_Object = MibTable
aclNamedTable = _AclNamedTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 7)
)
if mibBuilder.loadTexts:
    aclNamedTable.setStatus("current")
_AclNamedEntry_Object = MibTableRow
aclNamedEntry = _AclNamedEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 7, 1)
)
aclNamedEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedName"),
)
if mibBuilder.loadTexts:
    aclNamedEntry.setStatus("current")


class _AclNamedName_Type(OctetString):
    """Custom type aclNamedName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNamedName_Type.__name__ = "OctetString"
_AclNamedName_Object = MibTableColumn
aclNamedName = _AclNamedName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 7, 1, 1),
    _AclNamedName_Type()
)
aclNamedName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedName.setStatus("current")
_AclNamedType_Type = AclType
_AclNamedType_Object = MibTableColumn
aclNamedType = _AclNamedType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 7, 1, 2),
    _AclNamedType_Type()
)
aclNamedType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedType.setStatus("current")


class _AclNamedMatchOrder_Type(Integer32):
    """Custom type aclNamedMatchOrder based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("config", 0),
          ("auto", 1))
    )


_AclNamedMatchOrder_Type.__name__ = "Integer32"
_AclNamedMatchOrder_Object = MibTableColumn
aclNamedMatchOrder = _AclNamedMatchOrder_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 7, 1, 3),
    _AclNamedMatchOrder_Type()
)
aclNamedMatchOrder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedMatchOrder.setStatus("current")
_AclNamedTotleSubitems_Type = Integer32
_AclNamedTotleSubitems_Object = MibTableColumn
aclNamedTotleSubitems = _AclNamedTotleSubitems_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 7, 1, 4),
    _AclNamedTotleSubitems_Type()
)
aclNamedTotleSubitems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedTotleSubitems.setStatus("current")
_AclNamedRowStatus_Type = RowStatus
_AclNamedRowStatus_Object = MibTableColumn
aclNamedRowStatus = _AclNamedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 7, 1, 5),
    _AclNamedRowStatus_Type()
)
aclNamedRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedRowStatus.setStatus("current")
_AclNamedStdSubitemTable_Object = MibTable
aclNamedStdSubitemTable = _AclNamedStdSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8)
)
if mibBuilder.loadTexts:
    aclNamedStdSubitemTable.setStatus("current")
_AclNamedStdSubitemEntry_Object = MibTableRow
aclNamedStdSubitemEntry = _AclNamedStdSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1)
)
aclNamedStdSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedStdName"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedStdSubNum"),
)
if mibBuilder.loadTexts:
    aclNamedStdSubitemEntry.setStatus("current")


class _AclNamedStdName_Type(OctetString):
    """Custom type aclNamedStdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNamedStdName_Type.__name__ = "OctetString"
_AclNamedStdName_Object = MibTableColumn
aclNamedStdName = _AclNamedStdName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 1),
    _AclNamedStdName_Type()
)
aclNamedStdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedStdName.setStatus("current")


class _AclNamedStdSubNum_Type(Integer32):
    """Custom type aclNamedStdSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNamedStdSubNum_Type.__name__ = "Integer32"
_AclNamedStdSubNum_Object = MibTableColumn
aclNamedStdSubNum = _AclNamedStdSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 2),
    _AclNamedStdSubNum_Type()
)
aclNamedStdSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedStdSubNum.setStatus("current")
_AclNamedStdSubitemAdminStatus_Type = AdminStatus
_AclNamedStdSubitemAdminStatus_Object = MibTableColumn
aclNamedStdSubitemAdminStatus = _AclNamedStdSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 3),
    _AclNamedStdSubitemAdminStatus_Type()
)
aclNamedStdSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedStdSubitemAdminStatus.setStatus("current")
_AclNamedStdSubitemAction_Type = Action
_AclNamedStdSubitemAction_Object = MibTableColumn
aclNamedStdSubitemAction = _AclNamedStdSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 4),
    _AclNamedStdSubitemAction_Type()
)
aclNamedStdSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedStdSubitemAction.setStatus("current")
_AclNamedStdSubitemSrcAddr_Type = IpAddress
_AclNamedStdSubitemSrcAddr_Object = MibTableColumn
aclNamedStdSubitemSrcAddr = _AclNamedStdSubitemSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 5),
    _AclNamedStdSubitemSrcAddr_Type()
)
aclNamedStdSubitemSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedStdSubitemSrcAddr.setStatus("current")
_AclNamedStdSubitemSrcAddrWldmsk_Type = IpAddress
_AclNamedStdSubitemSrcAddrWldmsk_Object = MibTableColumn
aclNamedStdSubitemSrcAddrWldmsk = _AclNamedStdSubitemSrcAddrWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 6),
    _AclNamedStdSubitemSrcAddrWldmsk_Type()
)
aclNamedStdSubitemSrcAddrWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedStdSubitemSrcAddrWldmsk.setStatus("current")


class _AclNamedStdFragments_Type(TruthValue):
    """Custom type aclNamedStdFragments based on TruthValue"""
    defaultValue = 2


_AclNamedStdFragments_Type.__name__ = "TruthValue"
_AclNamedStdFragments_Object = MibTableColumn
aclNamedStdFragments = _AclNamedStdFragments_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 7),
    _AclNamedStdFragments_Type()
)
aclNamedStdFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedStdFragments.setStatus("current")


class _AclNamedStdTimeRange_Type(OctetString):
    """Custom type aclNamedStdTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AclNamedStdTimeRange_Type.__name__ = "OctetString"
_AclNamedStdTimeRange_Object = MibTableColumn
aclNamedStdTimeRange = _AclNamedStdTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 8),
    _AclNamedStdTimeRange_Type()
)
aclNamedStdTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedStdTimeRange.setStatus("current")
_AclNamedStdSubitemRowStatus_Type = RowStatus
_AclNamedStdSubitemRowStatus_Object = MibTableColumn
aclNamedStdSubitemRowStatus = _AclNamedStdSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 8, 1, 9),
    _AclNamedStdSubitemRowStatus_Type()
)
aclNamedStdSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedStdSubitemRowStatus.setStatus("current")
_AclNamedExdSubitemTable_Object = MibTable
aclNamedExdSubitemTable = _AclNamedExdSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9)
)
if mibBuilder.loadTexts:
    aclNamedExdSubitemTable.setStatus("current")
_AclNamedExdSubitemEntry_Object = MibTableRow
aclNamedExdSubitemEntry = _AclNamedExdSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1)
)
aclNamedExdSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedExdName"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedExdSubNum"),
)
if mibBuilder.loadTexts:
    aclNamedExdSubitemEntry.setStatus("current")


class _AclNamedExdName_Type(OctetString):
    """Custom type aclNamedExdName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNamedExdName_Type.__name__ = "OctetString"
_AclNamedExdName_Object = MibTableColumn
aclNamedExdName = _AclNamedExdName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 1),
    _AclNamedExdName_Type()
)
aclNamedExdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedExdName.setStatus("current")


class _AclNamedExdSubNum_Type(Integer32):
    """Custom type aclNamedExdSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNamedExdSubNum_Type.__name__ = "Integer32"
_AclNamedExdSubNum_Object = MibTableColumn
aclNamedExdSubNum = _AclNamedExdSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 2),
    _AclNamedExdSubNum_Type()
)
aclNamedExdSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedExdSubNum.setStatus("current")
_AclNamedExdSubitemAdminStatus_Type = AdminStatus
_AclNamedExdSubitemAdminStatus_Object = MibTableColumn
aclNamedExdSubitemAdminStatus = _AclNamedExdSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 3),
    _AclNamedExdSubitemAdminStatus_Type()
)
aclNamedExdSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedExdSubitemAdminStatus.setStatus("current")
_AclNamedExdSubitemAction_Type = Action
_AclNamedExdSubitemAction_Object = MibTableColumn
aclNamedExdSubitemAction = _AclNamedExdSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 4),
    _AclNamedExdSubitemAction_Type()
)
aclNamedExdSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemAction.setStatus("current")


class _AclNamedExdSubitemProtocal_Type(Integer32):
    """Custom type aclNamedExdSubitemProtocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclNamedExdSubitemProtocal_Type.__name__ = "Integer32"
_AclNamedExdSubitemProtocal_Object = MibTableColumn
aclNamedExdSubitemProtocal = _AclNamedExdSubitemProtocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 5),
    _AclNamedExdSubitemProtocal_Type()
)
aclNamedExdSubitemProtocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemProtocal.setStatus("current")
_AclNamedExdSubitemSrcAddr_Type = IpAddress
_AclNamedExdSubitemSrcAddr_Object = MibTableColumn
aclNamedExdSubitemSrcAddr = _AclNamedExdSubitemSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 6),
    _AclNamedExdSubitemSrcAddr_Type()
)
aclNamedExdSubitemSrcAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemSrcAddr.setStatus("current")
_AclNamedExdSubitemSrcAddrWldmsk_Type = IpAddress
_AclNamedExdSubitemSrcAddrWldmsk_Object = MibTableColumn
aclNamedExdSubitemSrcAddrWldmsk = _AclNamedExdSubitemSrcAddrWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 7),
    _AclNamedExdSubitemSrcAddrWldmsk_Type()
)
aclNamedExdSubitemSrcAddrWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemSrcAddrWldmsk.setStatus("current")
_AclNamedExdSubitemDstAddr_Type = IpAddress
_AclNamedExdSubitemDstAddr_Object = MibTableColumn
aclNamedExdSubitemDstAddr = _AclNamedExdSubitemDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 8),
    _AclNamedExdSubitemDstAddr_Type()
)
aclNamedExdSubitemDstAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemDstAddr.setStatus("current")
_AclNamedExdSubitemDstAddrWldmsk_Type = IpAddress
_AclNamedExdSubitemDstAddrWldmsk_Object = MibTableColumn
aclNamedExdSubitemDstAddrWldmsk = _AclNamedExdSubitemDstAddrWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 9),
    _AclNamedExdSubitemDstAddrWldmsk_Type()
)
aclNamedExdSubitemDstAddrWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemDstAddrWldmsk.setStatus("current")


class _AclNamedExdSubitemSrcPort_Type(Integer32):
    """Custom type aclNamedExdSubitemSrcPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNamedExdSubitemSrcPort_Type.__name__ = "Integer32"
_AclNamedExdSubitemSrcPort_Object = MibTableColumn
aclNamedExdSubitemSrcPort = _AclNamedExdSubitemSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 10),
    _AclNamedExdSubitemSrcPort_Type()
)
aclNamedExdSubitemSrcPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemSrcPort.setStatus("current")


class _AclNamedExdSubitemSrcPortWldmsk_Type(Integer32):
    """Custom type aclNamedExdSubitemSrcPortWldmsk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNamedExdSubitemSrcPortWldmsk_Type.__name__ = "Integer32"
_AclNamedExdSubitemSrcPortWldmsk_Object = MibTableColumn
aclNamedExdSubitemSrcPortWldmsk = _AclNamedExdSubitemSrcPortWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 11),
    _AclNamedExdSubitemSrcPortWldmsk_Type()
)
aclNamedExdSubitemSrcPortWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemSrcPortWldmsk.setStatus("current")


class _AclNamedExdSubitemDstPort_Type(Integer32):
    """Custom type aclNamedExdSubitemDstPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNamedExdSubitemDstPort_Type.__name__ = "Integer32"
_AclNamedExdSubitemDstPort_Object = MibTableColumn
aclNamedExdSubitemDstPort = _AclNamedExdSubitemDstPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 12),
    _AclNamedExdSubitemDstPort_Type()
)
aclNamedExdSubitemDstPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemDstPort.setStatus("current")


class _AclNamedExdSubitemDstPortWldmsk_Type(Integer32):
    """Custom type aclNamedExdSubitemDstPortWldmsk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclNamedExdSubitemDstPortWldmsk_Type.__name__ = "Integer32"
_AclNamedExdSubitemDstPortWldmsk_Object = MibTableColumn
aclNamedExdSubitemDstPortWldmsk = _AclNamedExdSubitemDstPortWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 13),
    _AclNamedExdSubitemDstPortWldmsk_Type()
)
aclNamedExdSubitemDstPortWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemDstPortWldmsk.setStatus("current")


class _AclNamedExdSubitemIcmpType_Type(Integer32):
    """Custom type aclNamedExdSubitemIcmpType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclNamedExdSubitemIcmpType_Type.__name__ = "Integer32"
_AclNamedExdSubitemIcmpType_Object = MibTableColumn
aclNamedExdSubitemIcmpType = _AclNamedExdSubitemIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 14),
    _AclNamedExdSubitemIcmpType_Type()
)
aclNamedExdSubitemIcmpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemIcmpType.setStatus("current")


class _AclNamedExdSubitemIcmpCode_Type(Integer32):
    """Custom type aclNamedExdSubitemIcmpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AclNamedExdSubitemIcmpCode_Type.__name__ = "Integer32"
_AclNamedExdSubitemIcmpCode_Object = MibTableColumn
aclNamedExdSubitemIcmpCode = _AclNamedExdSubitemIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 15),
    _AclNamedExdSubitemIcmpCode_Type()
)
aclNamedExdSubitemIcmpCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemIcmpCode.setStatus("current")


class _AclNamedExdSubitemTcpEstablished_Type(TruthValue):
    """Custom type aclNamedExdSubitemTcpEstablished based on TruthValue"""
    defaultValue = 2


_AclNamedExdSubitemTcpEstablished_Type.__name__ = "TruthValue"
_AclNamedExdSubitemTcpEstablished_Object = MibTableColumn
aclNamedExdSubitemTcpEstablished = _AclNamedExdSubitemTcpEstablished_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 16),
    _AclNamedExdSubitemTcpEstablished_Type()
)
aclNamedExdSubitemTcpEstablished.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemTcpEstablished.setStatus("current")


class _AclNamedExdSubitemPrecedence_Type(Integer32):
    """Custom type aclNamedExdSubitemPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclNamedExdSubitemPrecedence_Type.__name__ = "Integer32"
_AclNamedExdSubitemPrecedence_Object = MibTableColumn
aclNamedExdSubitemPrecedence = _AclNamedExdSubitemPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 17),
    _AclNamedExdSubitemPrecedence_Type()
)
aclNamedExdSubitemPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemPrecedence.setStatus("current")
_AclNamedExdSubitemTos_Type = TOSType
_AclNamedExdSubitemTos_Object = MibTableColumn
aclNamedExdSubitemTos = _AclNamedExdSubitemTos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 18),
    _AclNamedExdSubitemTos_Type()
)
aclNamedExdSubitemTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemTos.setStatus("current")
_AclNamedExdSubitemDscp_Type = Dscp
_AclNamedExdSubitemDscp_Object = MibTableColumn
aclNamedExdSubitemDscp = _AclNamedExdSubitemDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 19),
    _AclNamedExdSubitemDscp_Type()
)
aclNamedExdSubitemDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemDscp.setStatus("current")


class _AclNamedExdSubitemFragments_Type(TruthValue):
    """Custom type aclNamedExdSubitemFragments based on TruthValue"""
    defaultValue = 2


_AclNamedExdSubitemFragments_Type.__name__ = "TruthValue"
_AclNamedExdSubitemFragments_Object = MibTableColumn
aclNamedExdSubitemFragments = _AclNamedExdSubitemFragments_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 20),
    _AclNamedExdSubitemFragments_Type()
)
aclNamedExdSubitemFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemFragments.setStatus("current")


class _AclNamedExdSubitemTimeRange_Type(OctetString):
    """Custom type aclNamedExdSubitemTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AclNamedExdSubitemTimeRange_Type.__name__ = "OctetString"
_AclNamedExdSubitemTimeRange_Object = MibTableColumn
aclNamedExdSubitemTimeRange = _AclNamedExdSubitemTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 21),
    _AclNamedExdSubitemTimeRange_Type()
)
aclNamedExdSubitemTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemTimeRange.setStatus("current")
_AclNamedExdSubitemRowStatus_Type = RowStatus
_AclNamedExdSubitemRowStatus_Object = MibTableColumn
aclNamedExdSubitemRowStatus = _AclNamedExdSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 9, 1, 22),
    _AclNamedExdSubitemRowStatus_Type()
)
aclNamedExdSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedExdSubitemRowStatus.setStatus("current")
_AclNamedLnkSubitemTable_Object = MibTable
aclNamedLnkSubitemTable = _AclNamedLnkSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10)
)
if mibBuilder.loadTexts:
    aclNamedLnkSubitemTable.setStatus("current")
_AclNamedLnkSubitemEntry_Object = MibTableRow
aclNamedLnkSubitemEntry = _AclNamedLnkSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1)
)
aclNamedLnkSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedLnkName"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedLnkSubNum"),
)
if mibBuilder.loadTexts:
    aclNamedLnkSubitemEntry.setStatus("current")


class _AclNamedLnkName_Type(OctetString):
    """Custom type aclNamedLnkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNamedLnkName_Type.__name__ = "OctetString"
_AclNamedLnkName_Object = MibTableColumn
aclNamedLnkName = _AclNamedLnkName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 1),
    _AclNamedLnkName_Type()
)
aclNamedLnkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedLnkName.setStatus("current")


class _AclNamedLnkSubNum_Type(Integer32):
    """Custom type aclNamedLnkSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNamedLnkSubNum_Type.__name__ = "Integer32"
_AclNamedLnkSubNum_Object = MibTableColumn
aclNamedLnkSubNum = _AclNamedLnkSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 2),
    _AclNamedLnkSubNum_Type()
)
aclNamedLnkSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedLnkSubNum.setStatus("current")
_AclNamedLnkSubitemAdminStatus_Type = AdminStatus
_AclNamedLnkSubitemAdminStatus_Object = MibTableColumn
aclNamedLnkSubitemAdminStatus = _AclNamedLnkSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 3),
    _AclNamedLnkSubitemAdminStatus_Type()
)
aclNamedLnkSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemAdminStatus.setStatus("current")
_AclNamedLnkSubitemAction_Type = Action
_AclNamedLnkSubitemAction_Object = MibTableColumn
aclNamedLnkSubitemAction = _AclNamedLnkSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 4),
    _AclNamedLnkSubitemAction_Type()
)
aclNamedLnkSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemAction.setStatus("current")


class _AclNamedLnkSubitemProtocal_Type(Integer32):
    """Custom type aclNamedLnkSubitemProtocal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AclNamedLnkSubitemProtocal_Type.__name__ = "Integer32"
_AclNamedLnkSubitemProtocal_Object = MibTableColumn
aclNamedLnkSubitemProtocal = _AclNamedLnkSubitemProtocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 5),
    _AclNamedLnkSubitemProtocal_Type()
)
aclNamedLnkSubitemProtocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemProtocal.setStatus("current")


class _AclNamedLnkSubitemCos_Type(Integer32):
    """Custom type aclNamedLnkSubitemCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AclNamedLnkSubitemCos_Type.__name__ = "Integer32"
_AclNamedLnkSubitemCos_Object = MibTableColumn
aclNamedLnkSubitemCos = _AclNamedLnkSubitemCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 6),
    _AclNamedLnkSubitemCos_Type()
)
aclNamedLnkSubitemCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemCos.setStatus("current")
_AclNamedLnkSubitemSrcVlanID_Type = VlanId
_AclNamedLnkSubitemSrcVlanID_Object = MibTableColumn
aclNamedLnkSubitemSrcVlanID = _AclNamedLnkSubitemSrcVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 7),
    _AclNamedLnkSubitemSrcVlanID_Type()
)
aclNamedLnkSubitemSrcVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemSrcVlanID.setStatus("current")
_AclNamedLnkSubitemSrcMacAddr_Type = MacAddress
_AclNamedLnkSubitemSrcMacAddr_Object = MibTableColumn
aclNamedLnkSubitemSrcMacAddr = _AclNamedLnkSubitemSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 8),
    _AclNamedLnkSubitemSrcMacAddr_Type()
)
aclNamedLnkSubitemSrcMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemSrcMacAddr.setStatus("current")
_AclNamedLnkSubitemSrcMacWldmsk_Type = MacAddress
_AclNamedLnkSubitemSrcMacWldmsk_Object = MibTableColumn
aclNamedLnkSubitemSrcMacWldmsk = _AclNamedLnkSubitemSrcMacWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 9),
    _AclNamedLnkSubitemSrcMacWldmsk_Type()
)
aclNamedLnkSubitemSrcMacWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemSrcMacWldmsk.setStatus("current")
_AclNamedLnkSubitemDstMacAddr_Type = MacAddress
_AclNamedLnkSubitemDstMacAddr_Object = MibTableColumn
aclNamedLnkSubitemDstMacAddr = _AclNamedLnkSubitemDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 10),
    _AclNamedLnkSubitemDstMacAddr_Type()
)
aclNamedLnkSubitemDstMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemDstMacAddr.setStatus("current")
_AclNamedLnkSubitemDstMacWldmsk_Type = MacAddress
_AclNamedLnkSubitemDstMacWldmsk_Object = MibTableColumn
aclNamedLnkSubitemDstMacWldmsk = _AclNamedLnkSubitemDstMacWldmsk_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 11),
    _AclNamedLnkSubitemDstMacWldmsk_Type()
)
aclNamedLnkSubitemDstMacWldmsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemDstMacWldmsk.setStatus("current")


class _AclNamedLnkSubitemSrcPortNum_Type(Integer32):
    """Custom type aclNamedLnkSubitemSrcPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_AclNamedLnkSubitemSrcPortNum_Type.__name__ = "Integer32"
_AclNamedLnkSubitemSrcPortNum_Object = MibTableColumn
aclNamedLnkSubitemSrcPortNum = _AclNamedLnkSubitemSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 12),
    _AclNamedLnkSubitemSrcPortNum_Type()
)
aclNamedLnkSubitemSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemSrcPortNum.setStatus("current")


class _AclNamedLnkSubitemDstPortNum_Type(Integer32):
    """Custom type aclNamedLnkSubitemDstPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 29),
    )


_AclNamedLnkSubitemDstPortNum_Type.__name__ = "Integer32"
_AclNamedLnkSubitemDstPortNum_Object = MibTableColumn
aclNamedLnkSubitemDstPortNum = _AclNamedLnkSubitemDstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 13),
    _AclNamedLnkSubitemDstPortNum_Type()
)
aclNamedLnkSubitemDstPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemDstPortNum.setStatus("current")


class _AclNamedLnkSubitemTimeRange_Type(OctetString):
    """Custom type aclNamedLnkSubitemTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNamedLnkSubitemTimeRange_Type.__name__ = "OctetString"
_AclNamedLnkSubitemTimeRange_Object = MibTableColumn
aclNamedLnkSubitemTimeRange = _AclNamedLnkSubitemTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 14),
    _AclNamedLnkSubitemTimeRange_Type()
)
aclNamedLnkSubitemTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemTimeRange.setStatus("current")
_AclNamedLnkSubitemRowStatus_Type = RowStatus
_AclNamedLnkSubitemRowStatus_Object = MibTableColumn
aclNamedLnkSubitemRowStatus = _AclNamedLnkSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 10, 1, 15),
    _AclNamedLnkSubitemRowStatus_Type()
)
aclNamedLnkSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedLnkSubitemRowStatus.setStatus("current")
_AclNamedUserSubitemTable_Object = MibTable
aclNamedUserSubitemTable = _AclNamedUserSubitemTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11)
)
if mibBuilder.loadTexts:
    aclNamedUserSubitemTable.setStatus("current")
_AclNamedUserSubitemEntry_Object = MibTableRow
aclNamedUserSubitemEntry = _AclNamedUserSubitemEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1)
)
aclNamedUserSubitemEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedUserName"),
    (0, "QTECH-GBNL2QACL-MIB", "aclNamedUserSubNum"),
)
if mibBuilder.loadTexts:
    aclNamedUserSubitemEntry.setStatus("current")


class _AclNamedUserName_Type(OctetString):
    """Custom type aclNamedUserName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclNamedUserName_Type.__name__ = "OctetString"
_AclNamedUserName_Object = MibTableColumn
aclNamedUserName = _AclNamedUserName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 1),
    _AclNamedUserName_Type()
)
aclNamedUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedUserName.setStatus("current")


class _AclNamedUserSubNum_Type(Integer32):
    """Custom type aclNamedUserSubNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclNamedUserSubNum_Type.__name__ = "Integer32"
_AclNamedUserSubNum_Object = MibTableColumn
aclNamedUserSubNum = _AclNamedUserSubNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 2),
    _AclNamedUserSubNum_Type()
)
aclNamedUserSubNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedUserSubNum.setStatus("current")
_AclNamedUserSubitemAdminStatus_Type = AdminStatus
_AclNamedUserSubitemAdminStatus_Object = MibTableColumn
aclNamedUserSubitemAdminStatus = _AclNamedUserSubitemAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 3),
    _AclNamedUserSubitemAdminStatus_Type()
)
aclNamedUserSubitemAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclNamedUserSubitemAdminStatus.setStatus("current")
_AclNamedUserSubitemAction_Type = Action
_AclNamedUserSubitemAction_Object = MibTableColumn
aclNamedUserSubitemAction = _AclNamedUserSubitemAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 4),
    _AclNamedUserSubitemAction_Type()
)
aclNamedUserSubitemAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedUserSubitemAction.setStatus("current")
_AclNamedUserSubitemSrcPortNum_Type = Integer32
_AclNamedUserSubitemSrcPortNum_Object = MibTableColumn
aclNamedUserSubitemSrcPortNum = _AclNamedUserSubitemSrcPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 5),
    _AclNamedUserSubitemSrcPortNum_Type()
)
aclNamedUserSubitemSrcPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedUserSubitemSrcPortNum.setStatus("current")


class _AclNamedUserSubitemDstPortNum_Type(Integer32):
    """Custom type aclNamedUserSubitemDstPortNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 29),
    )


_AclNamedUserSubitemDstPortNum_Type.__name__ = "Integer32"
_AclNamedUserSubitemDstPortNum_Object = MibTableColumn
aclNamedUserSubitemDstPortNum = _AclNamedUserSubitemDstPortNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 6),
    _AclNamedUserSubitemDstPortNum_Type()
)
aclNamedUserSubitemDstPortNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedUserSubitemDstPortNum.setStatus("current")


class _AclNamedUserSubitemRule_Type(OctetString):
    """Custom type aclNamedUserSubitemRule based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_AclNamedUserSubitemRule_Type.__name__ = "OctetString"
_AclNamedUserSubitemRule_Object = MibTableColumn
aclNamedUserSubitemRule = _AclNamedUserSubitemRule_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 7),
    _AclNamedUserSubitemRule_Type()
)
aclNamedUserSubitemRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedUserSubitemRule.setStatus("current")


class _AclNamedUserSubitemMask_Type(OctetString):
    """Custom type aclNamedUserSubitemMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 160),
    )


_AclNamedUserSubitemMask_Type.__name__ = "OctetString"
_AclNamedUserSubitemMask_Object = MibTableColumn
aclNamedUserSubitemMask = _AclNamedUserSubitemMask_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 8),
    _AclNamedUserSubitemMask_Type()
)
aclNamedUserSubitemMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedUserSubitemMask.setStatus("current")


class _AclNamedUserTimeRange_Type(OctetString):
    """Custom type aclNamedUserTimeRange based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_AclNamedUserTimeRange_Type.__name__ = "OctetString"
_AclNamedUserTimeRange_Object = MibTableColumn
aclNamedUserTimeRange = _AclNamedUserTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 9),
    _AclNamedUserTimeRange_Type()
)
aclNamedUserTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedUserTimeRange.setStatus("current")
_AclNamedUserSubitemRowStatus_Type = RowStatus
_AclNamedUserSubitemRowStatus_Object = MibTableColumn
aclNamedUserSubitemRowStatus = _AclNamedUserSubitemRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 11, 1, 10),
    _AclNamedUserSubitemRowStatus_Type()
)
aclNamedUserSubitemRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclNamedUserSubitemRowStatus.setStatus("current")
_AclTimeRangeTable_Object = MibTable
aclTimeRangeTable = _AclTimeRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 12)
)
if mibBuilder.loadTexts:
    aclTimeRangeTable.setStatus("current")
_AclTimeRangeEntry_Object = MibTableRow
aclTimeRangeEntry = _AclTimeRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 12, 1)
)
aclTimeRangeEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangeName"),
)
if mibBuilder.loadTexts:
    aclTimeRangeEntry.setStatus("current")


class _AclTimeRangeName_Type(OctetString):
    """Custom type aclTimeRangeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclTimeRangeName_Type.__name__ = "OctetString"
_AclTimeRangeName_Object = MibTableColumn
aclTimeRangeName = _AclTimeRangeName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 12, 1, 1),
    _AclTimeRangeName_Type()
)
aclTimeRangeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangeName.setStatus("current")
_AclTimeRangeTotleAbsolutes_Type = Integer32
_AclTimeRangeTotleAbsolutes_Object = MibTableColumn
aclTimeRangeTotleAbsolutes = _AclTimeRangeTotleAbsolutes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 12, 1, 2),
    _AclTimeRangeTotleAbsolutes_Type()
)
aclTimeRangeTotleAbsolutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangeTotleAbsolutes.setStatus("current")
_AclTimeRangeTotlePeriods_Type = Integer32
_AclTimeRangeTotlePeriods_Object = MibTableColumn
aclTimeRangeTotlePeriods = _AclTimeRangeTotlePeriods_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 12, 1, 3),
    _AclTimeRangeTotlePeriods_Type()
)
aclTimeRangeTotlePeriods.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangeTotlePeriods.setStatus("current")
_AclTimeRangeActive_Type = TruthValue
_AclTimeRangeActive_Object = MibTableColumn
aclTimeRangeActive = _AclTimeRangeActive_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 12, 1, 4),
    _AclTimeRangeActive_Type()
)
aclTimeRangeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangeActive.setStatus("current")
_AclTimeRangeRowStatus_Type = RowStatus
_AclTimeRangeRowStatus_Object = MibTableColumn
aclTimeRangeRowStatus = _AclTimeRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 12, 1, 5),
    _AclTimeRangeRowStatus_Type()
)
aclTimeRangeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclTimeRangeRowStatus.setStatus("current")
_AclTimeRangeAbsoluteTable_Object = MibTable
aclTimeRangeAbsoluteTable = _AclTimeRangeAbsoluteTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 13)
)
if mibBuilder.loadTexts:
    aclTimeRangeAbsoluteTable.setStatus("current")
_AclTimeRangeAbsoluteEntry_Object = MibTableRow
aclTimeRangeAbsoluteEntry = _AclTimeRangeAbsoluteEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 13, 1)
)
aclTimeRangeAbsoluteEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangeAbsoluteName"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangeAbsoluteStartTime"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangeAbsoluteEndTime"),
)
if mibBuilder.loadTexts:
    aclTimeRangeAbsoluteEntry.setStatus("current")


class _AclTimeRangeAbsoluteName_Type(OctetString):
    """Custom type aclTimeRangeAbsoluteName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclTimeRangeAbsoluteName_Type.__name__ = "OctetString"
_AclTimeRangeAbsoluteName_Object = MibTableColumn
aclTimeRangeAbsoluteName = _AclTimeRangeAbsoluteName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 13, 1, 1),
    _AclTimeRangeAbsoluteName_Type()
)
aclTimeRangeAbsoluteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangeAbsoluteName.setStatus("current")
_AclTimeRangeAbsoluteStartTime_Type = Unsigned32
_AclTimeRangeAbsoluteStartTime_Object = MibTableColumn
aclTimeRangeAbsoluteStartTime = _AclTimeRangeAbsoluteStartTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 13, 1, 2),
    _AclTimeRangeAbsoluteStartTime_Type()
)
aclTimeRangeAbsoluteStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangeAbsoluteStartTime.setStatus("current")
_AclTimeRangeAbsoluteEndTime_Type = Unsigned32
_AclTimeRangeAbsoluteEndTime_Object = MibTableColumn
aclTimeRangeAbsoluteEndTime = _AclTimeRangeAbsoluteEndTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 13, 1, 3),
    _AclTimeRangeAbsoluteEndTime_Type()
)
aclTimeRangeAbsoluteEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangeAbsoluteEndTime.setStatus("current")
_AclTimeRangeAbsoluteRowStatus_Type = RowStatus
_AclTimeRangeAbsoluteRowStatus_Object = MibTableColumn
aclTimeRangeAbsoluteRowStatus = _AclTimeRangeAbsoluteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 13, 1, 4),
    _AclTimeRangeAbsoluteRowStatus_Type()
)
aclTimeRangeAbsoluteRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclTimeRangeAbsoluteRowStatus.setStatus("current")
_AclTimeRangePeriodTable_Object = MibTable
aclTimeRangePeriodTable = _AclTimeRangePeriodTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14)
)
if mibBuilder.loadTexts:
    aclTimeRangePeriodTable.setStatus("current")
_AclTimeRangePeriodEntry_Object = MibTableRow
aclTimeRangePeriodEntry = _AclTimeRangePeriodEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1)
)
aclTimeRangePeriodEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangePeriodName"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangePeriodStartWeekDay"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangePeriodStartHour"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangePeriodStartMin"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangePeriodEndWeekDay"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangePeriodEndHour"),
    (0, "QTECH-GBNL2QACL-MIB", "aclTimeRangePeriodEndMin"),
)
if mibBuilder.loadTexts:
    aclTimeRangePeriodEntry.setStatus("current")


class _AclTimeRangePeriodName_Type(OctetString):
    """Custom type aclTimeRangePeriodName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AclTimeRangePeriodName_Type.__name__ = "OctetString"
_AclTimeRangePeriodName_Object = MibTableColumn
aclTimeRangePeriodName = _AclTimeRangePeriodName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 1),
    _AclTimeRangePeriodName_Type()
)
aclTimeRangePeriodName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangePeriodName.setStatus("current")
_AclTimeRangePeriodStartWeekDay_Type = Unsigned32
_AclTimeRangePeriodStartWeekDay_Object = MibTableColumn
aclTimeRangePeriodStartWeekDay = _AclTimeRangePeriodStartWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 2),
    _AclTimeRangePeriodStartWeekDay_Type()
)
aclTimeRangePeriodStartWeekDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangePeriodStartWeekDay.setStatus("current")
_AclTimeRangePeriodStartHour_Type = Unsigned32
_AclTimeRangePeriodStartHour_Object = MibTableColumn
aclTimeRangePeriodStartHour = _AclTimeRangePeriodStartHour_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 3),
    _AclTimeRangePeriodStartHour_Type()
)
aclTimeRangePeriodStartHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangePeriodStartHour.setStatus("current")
_AclTimeRangePeriodStartMin_Type = Unsigned32
_AclTimeRangePeriodStartMin_Object = MibTableColumn
aclTimeRangePeriodStartMin = _AclTimeRangePeriodStartMin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 4),
    _AclTimeRangePeriodStartMin_Type()
)
aclTimeRangePeriodStartMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangePeriodStartMin.setStatus("current")
_AclTimeRangePeriodEndWeekDay_Type = Unsigned32
_AclTimeRangePeriodEndWeekDay_Object = MibTableColumn
aclTimeRangePeriodEndWeekDay = _AclTimeRangePeriodEndWeekDay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 5),
    _AclTimeRangePeriodEndWeekDay_Type()
)
aclTimeRangePeriodEndWeekDay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangePeriodEndWeekDay.setStatus("current")
_AclTimeRangePeriodEndHour_Type = Unsigned32
_AclTimeRangePeriodEndHour_Object = MibTableColumn
aclTimeRangePeriodEndHour = _AclTimeRangePeriodEndHour_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 6),
    _AclTimeRangePeriodEndHour_Type()
)
aclTimeRangePeriodEndHour.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangePeriodEndHour.setStatus("current")
_AclTimeRangePeriodEndMin_Type = Unsigned32
_AclTimeRangePeriodEndMin_Object = MibTableColumn
aclTimeRangePeriodEndMin = _AclTimeRangePeriodEndMin_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 7),
    _AclTimeRangePeriodEndMin_Type()
)
aclTimeRangePeriodEndMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclTimeRangePeriodEndMin.setStatus("current")
_AclTimeRangePeriodRowStatus_Type = RowStatus
_AclTimeRangePeriodRowStatus_Object = MibTableColumn
aclTimeRangePeriodRowStatus = _AclTimeRangePeriodRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 14, 1, 8),
    _AclTimeRangePeriodRowStatus_Type()
)
aclTimeRangePeriodRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclTimeRangePeriodRowStatus.setStatus("current")
_AclActiveTable_Object = MibTable
aclActiveTable = _AclActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15)
)
if mibBuilder.loadTexts:
    aclActiveTable.setStatus("current")
_AclActiveEntry_Object = MibTableRow
aclActiveEntry = _AclActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1)
)
aclActiveEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "aclActiveIndex"),
)
if mibBuilder.loadTexts:
    aclActiveEntry.setStatus("current")
_AclActiveIndex_Type = Integer32
_AclActiveIndex_Object = MibTableColumn
aclActiveIndex = _AclActiveIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 1),
    _AclActiveIndex_Type()
)
aclActiveIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveIndex.setStatus("current")


class _AclActiveUserGroupName_Type(OctetString):
    """Custom type aclActiveUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AclActiveUserGroupName_Type.__name__ = "OctetString"
_AclActiveUserGroupName_Object = MibTableColumn
aclActiveUserGroupName = _AclActiveUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 2),
    _AclActiveUserGroupName_Type()
)
aclActiveUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclActiveUserGroupName.setStatus("current")


class _AclActiveUserGroupSubitem_Type(Integer32):
    """Custom type aclActiveUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclActiveUserGroupSubitem_Type.__name__ = "Integer32"
_AclActiveUserGroupSubitem_Object = MibTableColumn
aclActiveUserGroupSubitem = _AclActiveUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 3),
    _AclActiveUserGroupSubitem_Type()
)
aclActiveUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclActiveUserGroupSubitem.setStatus("current")


class _AclActiveIpGroupName_Type(OctetString):
    """Custom type aclActiveIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AclActiveIpGroupName_Type.__name__ = "OctetString"
_AclActiveIpGroupName_Object = MibTableColumn
aclActiveIpGroupName = _AclActiveIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 4),
    _AclActiveIpGroupName_Type()
)
aclActiveIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclActiveIpGroupName.setStatus("current")


class _AclActiveIpGroupSubitem_Type(Integer32):
    """Custom type aclActiveIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclActiveIpGroupSubitem_Type.__name__ = "Integer32"
_AclActiveIpGroupSubitem_Object = MibTableColumn
aclActiveIpGroupSubitem = _AclActiveIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 5),
    _AclActiveIpGroupSubitem_Type()
)
aclActiveIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclActiveIpGroupSubitem.setStatus("current")


class _AclActiveLinkGroupName_Type(OctetString):
    """Custom type aclActiveLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AclActiveLinkGroupName_Type.__name__ = "OctetString"
_AclActiveLinkGroupName_Object = MibTableColumn
aclActiveLinkGroupName = _AclActiveLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 6),
    _AclActiveLinkGroupName_Type()
)
aclActiveLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclActiveLinkGroupName.setStatus("current")


class _AclActiveLinkGroupSubitem_Type(Integer32):
    """Custom type aclActiveLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AclActiveLinkGroupSubitem_Type.__name__ = "Integer32"
_AclActiveLinkGroupSubitem_Object = MibTableColumn
aclActiveLinkGroupSubitem = _AclActiveLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 7),
    _AclActiveLinkGroupSubitem_Type()
)
aclActiveLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclActiveLinkGroupSubitem.setStatus("current")


class _AclActiveBlock0Priority_Type(Integer32):
    """Custom type aclActiveBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock0Priority_Type.__name__ = "Integer32"
_AclActiveBlock0Priority_Object = MibTableColumn
aclActiveBlock0Priority = _AclActiveBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 8),
    _AclActiveBlock0Priority_Type()
)
aclActiveBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock0Priority.setStatus("current")


class _AclActiveBlock1Priority_Type(Integer32):
    """Custom type aclActiveBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock1Priority_Type.__name__ = "Integer32"
_AclActiveBlock1Priority_Object = MibTableColumn
aclActiveBlock1Priority = _AclActiveBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 9),
    _AclActiveBlock1Priority_Type()
)
aclActiveBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock1Priority.setStatus("current")


class _AclActiveBlock2Priority_Type(Integer32):
    """Custom type aclActiveBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock2Priority_Type.__name__ = "Integer32"
_AclActiveBlock2Priority_Object = MibTableColumn
aclActiveBlock2Priority = _AclActiveBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 10),
    _AclActiveBlock2Priority_Type()
)
aclActiveBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock2Priority.setStatus("current")


class _AclActiveBlock3Priority_Type(Integer32):
    """Custom type aclActiveBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock3Priority_Type.__name__ = "Integer32"
_AclActiveBlock3Priority_Object = MibTableColumn
aclActiveBlock3Priority = _AclActiveBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 11),
    _AclActiveBlock3Priority_Type()
)
aclActiveBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock3Priority.setStatus("current")


class _AclActiveBlock4Priority_Type(Integer32):
    """Custom type aclActiveBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock4Priority_Type.__name__ = "Integer32"
_AclActiveBlock4Priority_Object = MibTableColumn
aclActiveBlock4Priority = _AclActiveBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 12),
    _AclActiveBlock4Priority_Type()
)
aclActiveBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock4Priority.setStatus("current")


class _AclActiveConfigSequence_Type(Integer32):
    """Custom type aclActiveConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_AclActiveConfigSequence_Type.__name__ = "Integer32"
_AclActiveConfigSequence_Object = MibTableColumn
aclActiveConfigSequence = _AclActiveConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 13),
    _AclActiveConfigSequence_Type()
)
aclActiveConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveConfigSequence.setStatus("current")
_AclActiveRunning_Type = TruthValue
_AclActiveRunning_Object = MibTableColumn
aclActiveRunning = _AclActiveRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 14),
    _AclActiveRunning_Type()
)
aclActiveRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveRunning.setStatus("current")
_AclActiveRowStatus_Type = RowStatus
_AclActiveRowStatus_Object = MibTableColumn
aclActiveRowStatus = _AclActiveRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 15),
    _AclActiveRowStatus_Type()
)
aclActiveRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclActiveRowStatus.setStatus("current")


class _AclActiveBlock5Priority_Type(Integer32):
    """Custom type aclActiveBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock5Priority_Type.__name__ = "Integer32"
_AclActiveBlock5Priority_Object = MibTableColumn
aclActiveBlock5Priority = _AclActiveBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 16),
    _AclActiveBlock5Priority_Type()
)
aclActiveBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock5Priority.setStatus("current")


class _AclActiveBlock6Priority_Type(Integer32):
    """Custom type aclActiveBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock6Priority_Type.__name__ = "Integer32"
_AclActiveBlock6Priority_Object = MibTableColumn
aclActiveBlock6Priority = _AclActiveBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 17),
    _AclActiveBlock6Priority_Type()
)
aclActiveBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock6Priority.setStatus("current")


class _AclActiveBlock7Priority_Type(Integer32):
    """Custom type aclActiveBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock7Priority_Type.__name__ = "Integer32"
_AclActiveBlock7Priority_Object = MibTableColumn
aclActiveBlock7Priority = _AclActiveBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 18),
    _AclActiveBlock7Priority_Type()
)
aclActiveBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock7Priority.setStatus("current")


class _AclActiveBlock8Priority_Type(Integer32):
    """Custom type aclActiveBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock8Priority_Type.__name__ = "Integer32"
_AclActiveBlock8Priority_Object = MibTableColumn
aclActiveBlock8Priority = _AclActiveBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 19),
    _AclActiveBlock8Priority_Type()
)
aclActiveBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock8Priority.setStatus("current")


class _AclActiveBlock9Priority_Type(Integer32):
    """Custom type aclActiveBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock9Priority_Type.__name__ = "Integer32"
_AclActiveBlock9Priority_Object = MibTableColumn
aclActiveBlock9Priority = _AclActiveBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 20),
    _AclActiveBlock9Priority_Type()
)
aclActiveBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock9Priority.setStatus("current")


class _AclActiveBlock10Priority_Type(Integer32):
    """Custom type aclActiveBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock10Priority_Type.__name__ = "Integer32"
_AclActiveBlock10Priority_Object = MibTableColumn
aclActiveBlock10Priority = _AclActiveBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 21),
    _AclActiveBlock10Priority_Type()
)
aclActiveBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock10Priority.setStatus("current")


class _AclActiveBlock11Priority_Type(Integer32):
    """Custom type aclActiveBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclActiveBlock11Priority_Type.__name__ = "Integer32"
_AclActiveBlock11Priority_Object = MibTableColumn
aclActiveBlock11Priority = _AclActiveBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 15, 1, 22),
    _AclActiveBlock11Priority_Type()
)
aclActiveBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclActiveBlock11Priority.setStatus("current")
_QosMirrorToTable_Object = MibTable
qosMirrorToTable = _QosMirrorToTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16)
)
if mibBuilder.loadTexts:
    qosMirrorToTable.setStatus("current")
_QosMirrorToEntry_Object = MibTableRow
qosMirrorToEntry = _QosMirrorToEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1)
)
qosMirrorToEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosMirrorToIndex"),
)
if mibBuilder.loadTexts:
    qosMirrorToEntry.setStatus("current")
_QosMirrorToIndex_Type = Integer32
_QosMirrorToIndex_Object = MibTableColumn
qosMirrorToIndex = _QosMirrorToIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 1),
    _QosMirrorToIndex_Type()
)
qosMirrorToIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToIndex.setStatus("current")


class _QosMirrorToUserGroupName_Type(OctetString):
    """Custom type qosMirrorToUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosMirrorToUserGroupName_Type.__name__ = "OctetString"
_QosMirrorToUserGroupName_Object = MibTableColumn
qosMirrorToUserGroupName = _QosMirrorToUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 2),
    _QosMirrorToUserGroupName_Type()
)
qosMirrorToUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMirrorToUserGroupName.setStatus("current")


class _QosMirrorToUserGroupSubitem_Type(Integer32):
    """Custom type qosMirrorToUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosMirrorToUserGroupSubitem_Type.__name__ = "Integer32"
_QosMirrorToUserGroupSubitem_Object = MibTableColumn
qosMirrorToUserGroupSubitem = _QosMirrorToUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 3),
    _QosMirrorToUserGroupSubitem_Type()
)
qosMirrorToUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMirrorToUserGroupSubitem.setStatus("current")


class _QosMirrorToIpGroupName_Type(OctetString):
    """Custom type qosMirrorToIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosMirrorToIpGroupName_Type.__name__ = "OctetString"
_QosMirrorToIpGroupName_Object = MibTableColumn
qosMirrorToIpGroupName = _QosMirrorToIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 4),
    _QosMirrorToIpGroupName_Type()
)
qosMirrorToIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMirrorToIpGroupName.setStatus("current")


class _QosMirrorToIpGroupSubitem_Type(Integer32):
    """Custom type qosMirrorToIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosMirrorToIpGroupSubitem_Type.__name__ = "Integer32"
_QosMirrorToIpGroupSubitem_Object = MibTableColumn
qosMirrorToIpGroupSubitem = _QosMirrorToIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 5),
    _QosMirrorToIpGroupSubitem_Type()
)
qosMirrorToIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMirrorToIpGroupSubitem.setStatus("current")


class _QosMirrorToLinkGroupName_Type(OctetString):
    """Custom type qosMirrorToLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosMirrorToLinkGroupName_Type.__name__ = "OctetString"
_QosMirrorToLinkGroupName_Object = MibTableColumn
qosMirrorToLinkGroupName = _QosMirrorToLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 6),
    _QosMirrorToLinkGroupName_Type()
)
qosMirrorToLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMirrorToLinkGroupName.setStatus("current")


class _QosMirrorToLinkGroupSubitem_Type(Integer32):
    """Custom type qosMirrorToLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosMirrorToLinkGroupSubitem_Type.__name__ = "Integer32"
_QosMirrorToLinkGroupSubitem_Object = MibTableColumn
qosMirrorToLinkGroupSubitem = _QosMirrorToLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 7),
    _QosMirrorToLinkGroupSubitem_Type()
)
qosMirrorToLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMirrorToLinkGroupSubitem.setStatus("current")


class _QosMirrorToInterface_Type(Integer32):
    """Custom type qosMirrorToInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_QosMirrorToInterface_Type.__name__ = "Integer32"
_QosMirrorToInterface_Object = MibTableColumn
qosMirrorToInterface = _QosMirrorToInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 8),
    _QosMirrorToInterface_Type()
)
qosMirrorToInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosMirrorToInterface.setStatus("current")


class _QosMirrorToBlock0Priority_Type(Integer32):
    """Custom type qosMirrorToBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock0Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock0Priority_Object = MibTableColumn
qosMirrorToBlock0Priority = _QosMirrorToBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 9),
    _QosMirrorToBlock0Priority_Type()
)
qosMirrorToBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock0Priority.setStatus("current")


class _QosMirrorToBlock1Priority_Type(Integer32):
    """Custom type qosMirrorToBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock1Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock1Priority_Object = MibTableColumn
qosMirrorToBlock1Priority = _QosMirrorToBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 10),
    _QosMirrorToBlock1Priority_Type()
)
qosMirrorToBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock1Priority.setStatus("current")


class _QosMirrorToBlock2Priority_Type(Integer32):
    """Custom type qosMirrorToBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock2Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock2Priority_Object = MibTableColumn
qosMirrorToBlock2Priority = _QosMirrorToBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 11),
    _QosMirrorToBlock2Priority_Type()
)
qosMirrorToBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock2Priority.setStatus("current")


class _QosMirrorToBlock3Priority_Type(Integer32):
    """Custom type qosMirrorToBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock3Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock3Priority_Object = MibTableColumn
qosMirrorToBlock3Priority = _QosMirrorToBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 12),
    _QosMirrorToBlock3Priority_Type()
)
qosMirrorToBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock3Priority.setStatus("current")


class _QosMirrorToBlock4Priority_Type(Integer32):
    """Custom type qosMirrorToBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock4Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock4Priority_Object = MibTableColumn
qosMirrorToBlock4Priority = _QosMirrorToBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 13),
    _QosMirrorToBlock4Priority_Type()
)
qosMirrorToBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock4Priority.setStatus("current")


class _QosMirrorToConfigSequence_Type(Integer32):
    """Custom type qosMirrorToConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosMirrorToConfigSequence_Type.__name__ = "Integer32"
_QosMirrorToConfigSequence_Object = MibTableColumn
qosMirrorToConfigSequence = _QosMirrorToConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 14),
    _QosMirrorToConfigSequence_Type()
)
qosMirrorToConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToConfigSequence.setStatus("current")
_QosMirrorToRunning_Type = TruthValue
_QosMirrorToRunning_Object = MibTableColumn
qosMirrorToRunning = _QosMirrorToRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 15),
    _QosMirrorToRunning_Type()
)
qosMirrorToRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToRunning.setStatus("current")
_QosMirrorToRowStatus_Type = RowStatus
_QosMirrorToRowStatus_Object = MibTableColumn
qosMirrorToRowStatus = _QosMirrorToRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 16),
    _QosMirrorToRowStatus_Type()
)
qosMirrorToRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosMirrorToRowStatus.setStatus("current")


class _QosMirrorToBlock5Priority_Type(Integer32):
    """Custom type qosMirrorToBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock5Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock5Priority_Object = MibTableColumn
qosMirrorToBlock5Priority = _QosMirrorToBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 17),
    _QosMirrorToBlock5Priority_Type()
)
qosMirrorToBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock5Priority.setStatus("current")


class _QosMirrorToBlock6Priority_Type(Integer32):
    """Custom type qosMirrorToBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock6Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock6Priority_Object = MibTableColumn
qosMirrorToBlock6Priority = _QosMirrorToBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 18),
    _QosMirrorToBlock6Priority_Type()
)
qosMirrorToBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock6Priority.setStatus("current")


class _QosMirrorToBlock7Priority_Type(Integer32):
    """Custom type qosMirrorToBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock7Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock7Priority_Object = MibTableColumn
qosMirrorToBlock7Priority = _QosMirrorToBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 19),
    _QosMirrorToBlock7Priority_Type()
)
qosMirrorToBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock7Priority.setStatus("current")


class _QosMirrorToBlock8Priority_Type(Integer32):
    """Custom type qosMirrorToBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock8Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock8Priority_Object = MibTableColumn
qosMirrorToBlock8Priority = _QosMirrorToBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 20),
    _QosMirrorToBlock8Priority_Type()
)
qosMirrorToBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock8Priority.setStatus("current")


class _QosMirrorToBlock9Priority_Type(Integer32):
    """Custom type qosMirrorToBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock9Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock9Priority_Object = MibTableColumn
qosMirrorToBlock9Priority = _QosMirrorToBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 21),
    _QosMirrorToBlock9Priority_Type()
)
qosMirrorToBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock9Priority.setStatus("current")


class _QosMirrorToBlock10Priority_Type(Integer32):
    """Custom type qosMirrorToBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock10Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock10Priority_Object = MibTableColumn
qosMirrorToBlock10Priority = _QosMirrorToBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 22),
    _QosMirrorToBlock10Priority_Type()
)
qosMirrorToBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock10Priority.setStatus("current")


class _QosMirrorToBlock11Priority_Type(Integer32):
    """Custom type qosMirrorToBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosMirrorToBlock11Priority_Type.__name__ = "Integer32"
_QosMirrorToBlock11Priority_Object = MibTableColumn
qosMirrorToBlock11Priority = _QosMirrorToBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 16, 1, 23),
    _QosMirrorToBlock11Priority_Type()
)
qosMirrorToBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosMirrorToBlock11Priority.setStatus("current")
_QosRateLimitTable_Object = MibTable
qosRateLimitTable = _QosRateLimitTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17)
)
if mibBuilder.loadTexts:
    qosRateLimitTable.setStatus("current")
_QosRateLimitEntry_Object = MibTableRow
qosRateLimitEntry = _QosRateLimitEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1)
)
qosRateLimitEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosRateLimitIndex"),
)
if mibBuilder.loadTexts:
    qosRateLimitEntry.setStatus("current")
_QosRateLimitIndex_Type = Integer32
_QosRateLimitIndex_Object = MibTableColumn
qosRateLimitIndex = _QosRateLimitIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 1),
    _QosRateLimitIndex_Type()
)
qosRateLimitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitIndex.setStatus("current")


class _QosRateLimitUserGroupName_Type(OctetString):
    """Custom type qosRateLimitUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosRateLimitUserGroupName_Type.__name__ = "OctetString"
_QosRateLimitUserGroupName_Object = MibTableColumn
qosRateLimitUserGroupName = _QosRateLimitUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 2),
    _QosRateLimitUserGroupName_Type()
)
qosRateLimitUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitUserGroupName.setStatus("current")


class _QosRateLimitUserGroupSubitem_Type(Integer32):
    """Custom type qosRateLimitUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosRateLimitUserGroupSubitem_Type.__name__ = "Integer32"
_QosRateLimitUserGroupSubitem_Object = MibTableColumn
qosRateLimitUserGroupSubitem = _QosRateLimitUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 3),
    _QosRateLimitUserGroupSubitem_Type()
)
qosRateLimitUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitUserGroupSubitem.setStatus("current")


class _QosRateLimitIpGroupName_Type(OctetString):
    """Custom type qosRateLimitIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosRateLimitIpGroupName_Type.__name__ = "OctetString"
_QosRateLimitIpGroupName_Object = MibTableColumn
qosRateLimitIpGroupName = _QosRateLimitIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 4),
    _QosRateLimitIpGroupName_Type()
)
qosRateLimitIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitIpGroupName.setStatus("current")


class _QosRateLimitIpGroupSubitem_Type(Integer32):
    """Custom type qosRateLimitIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosRateLimitIpGroupSubitem_Type.__name__ = "Integer32"
_QosRateLimitIpGroupSubitem_Object = MibTableColumn
qosRateLimitIpGroupSubitem = _QosRateLimitIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 5),
    _QosRateLimitIpGroupSubitem_Type()
)
qosRateLimitIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitIpGroupSubitem.setStatus("current")


class _QosRateLimitLinkGroupName_Type(OctetString):
    """Custom type qosRateLimitLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosRateLimitLinkGroupName_Type.__name__ = "OctetString"
_QosRateLimitLinkGroupName_Object = MibTableColumn
qosRateLimitLinkGroupName = _QosRateLimitLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 6),
    _QosRateLimitLinkGroupName_Type()
)
qosRateLimitLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitLinkGroupName.setStatus("current")


class _QosRateLimitLinkGroupSubitem_Type(Integer32):
    """Custom type qosRateLimitLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosRateLimitLinkGroupSubitem_Type.__name__ = "Integer32"
_QosRateLimitLinkGroupSubitem_Object = MibTableColumn
qosRateLimitLinkGroupSubitem = _QosRateLimitLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 7),
    _QosRateLimitLinkGroupSubitem_Type()
)
qosRateLimitLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitLinkGroupSubitem.setStatus("current")


class _QosRateLimitIntf_Type(Integer32):
    """Custom type qosRateLimitIntf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_QosRateLimitIntf_Type.__name__ = "Integer32"
_QosRateLimitIntf_Object = MibTableColumn
qosRateLimitIntf = _QosRateLimitIntf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 8),
    _QosRateLimitIntf_Type()
)
qosRateLimitIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitIntf.setStatus("current")


class _QosRateLimitTargetRate_Type(Integer32):
    """Custom type qosRateLimitTargetRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosRateLimitTargetRate_Type.__name__ = "Integer32"
_QosRateLimitTargetRate_Object = MibTableColumn
qosRateLimitTargetRate = _QosRateLimitTargetRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 9),
    _QosRateLimitTargetRate_Type()
)
qosRateLimitTargetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitTargetRate.setStatus("current")


class _QosRateLimitExceedAction_Type(Integer32):
    """Custom type qosRateLimitExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("set-dscp-value", 2))
    )


_QosRateLimitExceedAction_Type.__name__ = "Integer32"
_QosRateLimitExceedAction_Object = MibTableColumn
qosRateLimitExceedAction = _QosRateLimitExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 10),
    _QosRateLimitExceedAction_Type()
)
qosRateLimitExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitExceedAction.setStatus("current")


class _QosRateLimitDscpValue_Type(Integer32):
    """Custom type qosRateLimitDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QosRateLimitDscpValue_Type.__name__ = "Integer32"
_QosRateLimitDscpValue_Object = MibTableColumn
qosRateLimitDscpValue = _QosRateLimitDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 11),
    _QosRateLimitDscpValue_Type()
)
qosRateLimitDscpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosRateLimitDscpValue.setStatus("current")


class _QosRateLimitBlock0Priority_Type(Integer32):
    """Custom type qosRateLimitBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock0Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock0Priority_Object = MibTableColumn
qosRateLimitBlock0Priority = _QosRateLimitBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 12),
    _QosRateLimitBlock0Priority_Type()
)
qosRateLimitBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock0Priority.setStatus("current")


class _QosRateLimitBlock1Priority_Type(Integer32):
    """Custom type qosRateLimitBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock1Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock1Priority_Object = MibTableColumn
qosRateLimitBlock1Priority = _QosRateLimitBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 13),
    _QosRateLimitBlock1Priority_Type()
)
qosRateLimitBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock1Priority.setStatus("current")


class _QosRateLimitBlock2Priority_Type(Integer32):
    """Custom type qosRateLimitBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock2Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock2Priority_Object = MibTableColumn
qosRateLimitBlock2Priority = _QosRateLimitBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 14),
    _QosRateLimitBlock2Priority_Type()
)
qosRateLimitBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock2Priority.setStatus("current")


class _QosRateLimitBlock3Priority_Type(Integer32):
    """Custom type qosRateLimitBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock3Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock3Priority_Object = MibTableColumn
qosRateLimitBlock3Priority = _QosRateLimitBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 15),
    _QosRateLimitBlock3Priority_Type()
)
qosRateLimitBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock3Priority.setStatus("current")


class _QosRateLimitBlock4Priority_Type(Integer32):
    """Custom type qosRateLimitBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock4Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock4Priority_Object = MibTableColumn
qosRateLimitBlock4Priority = _QosRateLimitBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 16),
    _QosRateLimitBlock4Priority_Type()
)
qosRateLimitBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock4Priority.setStatus("current")


class _QosRateLimitConfigSequence_Type(Integer32):
    """Custom type qosRateLimitConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosRateLimitConfigSequence_Type.__name__ = "Integer32"
_QosRateLimitConfigSequence_Object = MibTableColumn
qosRateLimitConfigSequence = _QosRateLimitConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 17),
    _QosRateLimitConfigSequence_Type()
)
qosRateLimitConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitConfigSequence.setStatus("current")
_QosRateLimitRunning_Type = TruthValue
_QosRateLimitRunning_Object = MibTableColumn
qosRateLimitRunning = _QosRateLimitRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 18),
    _QosRateLimitRunning_Type()
)
qosRateLimitRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitRunning.setStatus("current")
_QosRateLimitRowStatus_Type = RowStatus
_QosRateLimitRowStatus_Object = MibTableColumn
qosRateLimitRowStatus = _QosRateLimitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 19),
    _QosRateLimitRowStatus_Type()
)
qosRateLimitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosRateLimitRowStatus.setStatus("current")


class _QosRateLimitBlock5Priority_Type(Integer32):
    """Custom type qosRateLimitBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock5Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock5Priority_Object = MibTableColumn
qosRateLimitBlock5Priority = _QosRateLimitBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 20),
    _QosRateLimitBlock5Priority_Type()
)
qosRateLimitBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock5Priority.setStatus("current")


class _QosRateLimitBlock6Priority_Type(Integer32):
    """Custom type qosRateLimitBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock6Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock6Priority_Object = MibTableColumn
qosRateLimitBlock6Priority = _QosRateLimitBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 21),
    _QosRateLimitBlock6Priority_Type()
)
qosRateLimitBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock6Priority.setStatus("current")


class _QosRateLimitBlock7Priority_Type(Integer32):
    """Custom type qosRateLimitBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock7Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock7Priority_Object = MibTableColumn
qosRateLimitBlock7Priority = _QosRateLimitBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 22),
    _QosRateLimitBlock7Priority_Type()
)
qosRateLimitBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock7Priority.setStatus("current")


class _QosRateLimitBlock8Priority_Type(Integer32):
    """Custom type qosRateLimitBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock8Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock8Priority_Object = MibTableColumn
qosRateLimitBlock8Priority = _QosRateLimitBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 23),
    _QosRateLimitBlock8Priority_Type()
)
qosRateLimitBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock8Priority.setStatus("current")


class _QosRateLimitBlock9Priority_Type(Integer32):
    """Custom type qosRateLimitBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock9Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock9Priority_Object = MibTableColumn
qosRateLimitBlock9Priority = _QosRateLimitBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 24),
    _QosRateLimitBlock9Priority_Type()
)
qosRateLimitBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock9Priority.setStatus("current")


class _QosRateLimitBlock10Priority_Type(Integer32):
    """Custom type qosRateLimitBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock10Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock10Priority_Object = MibTableColumn
qosRateLimitBlock10Priority = _QosRateLimitBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 25),
    _QosRateLimitBlock10Priority_Type()
)
qosRateLimitBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock10Priority.setStatus("current")


class _QosRateLimitBlock11Priority_Type(Integer32):
    """Custom type qosRateLimitBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosRateLimitBlock11Priority_Type.__name__ = "Integer32"
_QosRateLimitBlock11Priority_Object = MibTableColumn
qosRateLimitBlock11Priority = _QosRateLimitBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 17, 1, 26),
    _QosRateLimitBlock11Priority_Type()
)
qosRateLimitBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosRateLimitBlock11Priority.setStatus("current")
_QosTrafficPriorityTable_Object = MibTable
qosTrafficPriorityTable = _QosTrafficPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18)
)
if mibBuilder.loadTexts:
    qosTrafficPriorityTable.setStatus("current")
_QosTrafficPriorityEntry_Object = MibTableRow
qosTrafficPriorityEntry = _QosTrafficPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1)
)
qosTrafficPriorityEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosTrafficPriorityIndex"),
)
if mibBuilder.loadTexts:
    qosTrafficPriorityEntry.setStatus("current")
_QosTrafficPriorityIndex_Type = Integer32
_QosTrafficPriorityIndex_Object = MibTableColumn
qosTrafficPriorityIndex = _QosTrafficPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 1),
    _QosTrafficPriorityIndex_Type()
)
qosTrafficPriorityIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityIndex.setStatus("current")


class _QosTrafficPriorityUserGroupName_Type(OctetString):
    """Custom type qosTrafficPriorityUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficPriorityUserGroupName_Type.__name__ = "OctetString"
_QosTrafficPriorityUserGroupName_Object = MibTableColumn
qosTrafficPriorityUserGroupName = _QosTrafficPriorityUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 2),
    _QosTrafficPriorityUserGroupName_Type()
)
qosTrafficPriorityUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityUserGroupName.setStatus("current")


class _QosTrafficPriorityUserGroupSubitem_Type(Integer32):
    """Custom type qosTrafficPriorityUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficPriorityUserGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficPriorityUserGroupSubitem_Object = MibTableColumn
qosTrafficPriorityUserGroupSubitem = _QosTrafficPriorityUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 3),
    _QosTrafficPriorityUserGroupSubitem_Type()
)
qosTrafficPriorityUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityUserGroupSubitem.setStatus("current")


class _QosTrafficPriorityIpGroupName_Type(OctetString):
    """Custom type qosTrafficPriorityIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficPriorityIpGroupName_Type.__name__ = "OctetString"
_QosTrafficPriorityIpGroupName_Object = MibTableColumn
qosTrafficPriorityIpGroupName = _QosTrafficPriorityIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 4),
    _QosTrafficPriorityIpGroupName_Type()
)
qosTrafficPriorityIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityIpGroupName.setStatus("current")


class _QosTrafficPriorityIpGroupSubitem_Type(Integer32):
    """Custom type qosTrafficPriorityIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficPriorityIpGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficPriorityIpGroupSubitem_Object = MibTableColumn
qosTrafficPriorityIpGroupSubitem = _QosTrafficPriorityIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 5),
    _QosTrafficPriorityIpGroupSubitem_Type()
)
qosTrafficPriorityIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityIpGroupSubitem.setStatus("current")


class _QosTrafficPriorityLinkGroupName_Type(OctetString):
    """Custom type qosTrafficPriorityLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficPriorityLinkGroupName_Type.__name__ = "OctetString"
_QosTrafficPriorityLinkGroupName_Object = MibTableColumn
qosTrafficPriorityLinkGroupName = _QosTrafficPriorityLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 6),
    _QosTrafficPriorityLinkGroupName_Type()
)
qosTrafficPriorityLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityLinkGroupName.setStatus("current")


class _QosTrafficPriorityLinkGroupSubitem_Type(Integer32):
    """Custom type qosTrafficPriorityLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficPriorityLinkGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficPriorityLinkGroupSubitem_Object = MibTableColumn
qosTrafficPriorityLinkGroupSubitem = _QosTrafficPriorityLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 7),
    _QosTrafficPriorityLinkGroupSubitem_Type()
)
qosTrafficPriorityLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityLinkGroupSubitem.setStatus("current")


class _QosTrafficPriorityDscp_Type(Integer32):
    """Custom type qosTrafficPriorityDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_QosTrafficPriorityDscp_Type.__name__ = "Integer32"
_QosTrafficPriorityDscp_Object = MibTableColumn
qosTrafficPriorityDscp = _QosTrafficPriorityDscp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 8),
    _QosTrafficPriorityDscp_Type()
)
qosTrafficPriorityDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityDscp.setStatus("current")


class _QosTrafficPriorityIpPrecedence_Type(Integer32):
    """Custom type qosTrafficPriorityIpPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTrafficPriorityIpPrecedence_Type.__name__ = "Integer32"
_QosTrafficPriorityIpPrecedence_Object = MibTableColumn
qosTrafficPriorityIpPrecedence = _QosTrafficPriorityIpPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 9),
    _QosTrafficPriorityIpPrecedence_Type()
)
qosTrafficPriorityIpPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityIpPrecedence.setStatus("current")


class _QosTrafficPriorityCos_Type(Integer32):
    """Custom type qosTrafficPriorityCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTrafficPriorityCos_Type.__name__ = "Integer32"
_QosTrafficPriorityCos_Object = MibTableColumn
qosTrafficPriorityCos = _QosTrafficPriorityCos_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 10),
    _QosTrafficPriorityCos_Type()
)
qosTrafficPriorityCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityCos.setStatus("current")


class _QosTrafficPriorityLocalPrecedence_Type(Integer32):
    """Custom type qosTrafficPriorityLocalPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_QosTrafficPriorityLocalPrecedence_Type.__name__ = "Integer32"
_QosTrafficPriorityLocalPrecedence_Object = MibTableColumn
qosTrafficPriorityLocalPrecedence = _QosTrafficPriorityLocalPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 11),
    _QosTrafficPriorityLocalPrecedence_Type()
)
qosTrafficPriorityLocalPrecedence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficPriorityLocalPrecedence.setStatus("current")


class _QosTrafficPriorityBlock0Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock0Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock0Priority_Object = MibTableColumn
qosTrafficPriorityBlock0Priority = _QosTrafficPriorityBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 12),
    _QosTrafficPriorityBlock0Priority_Type()
)
qosTrafficPriorityBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock0Priority.setStatus("current")


class _QosTrafficPriorityBlock1Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock1Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock1Priority_Object = MibTableColumn
qosTrafficPriorityBlock1Priority = _QosTrafficPriorityBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 13),
    _QosTrafficPriorityBlock1Priority_Type()
)
qosTrafficPriorityBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock1Priority.setStatus("current")


class _QosTrafficPriorityBlock2Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock2Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock2Priority_Object = MibTableColumn
qosTrafficPriorityBlock2Priority = _QosTrafficPriorityBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 14),
    _QosTrafficPriorityBlock2Priority_Type()
)
qosTrafficPriorityBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock2Priority.setStatus("current")


class _QosTrafficPriorityBlock3Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock3Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock3Priority_Object = MibTableColumn
qosTrafficPriorityBlock3Priority = _QosTrafficPriorityBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 15),
    _QosTrafficPriorityBlock3Priority_Type()
)
qosTrafficPriorityBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock3Priority.setStatus("current")


class _QosTrafficPriorityBlock4Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock4Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock4Priority_Object = MibTableColumn
qosTrafficPriorityBlock4Priority = _QosTrafficPriorityBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 16),
    _QosTrafficPriorityBlock4Priority_Type()
)
qosTrafficPriorityBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock4Priority.setStatus("current")


class _QosTrafficPriorityConfigSequence_Type(Integer32):
    """Custom type qosTrafficPriorityConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosTrafficPriorityConfigSequence_Type.__name__ = "Integer32"
_QosTrafficPriorityConfigSequence_Object = MibTableColumn
qosTrafficPriorityConfigSequence = _QosTrafficPriorityConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 17),
    _QosTrafficPriorityConfigSequence_Type()
)
qosTrafficPriorityConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityConfigSequence.setStatus("current")
_QosTrafficPriorityRunning_Type = TruthValue
_QosTrafficPriorityRunning_Object = MibTableColumn
qosTrafficPriorityRunning = _QosTrafficPriorityRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 18),
    _QosTrafficPriorityRunning_Type()
)
qosTrafficPriorityRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityRunning.setStatus("current")
_QosTrafficPriorityRowStatus_Type = RowStatus
_QosTrafficPriorityRowStatus_Object = MibTableColumn
qosTrafficPriorityRowStatus = _QosTrafficPriorityRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 19),
    _QosTrafficPriorityRowStatus_Type()
)
qosTrafficPriorityRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTrafficPriorityRowStatus.setStatus("current")


class _QosTrafficPriorityBlock5Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock5Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock5Priority_Object = MibTableColumn
qosTrafficPriorityBlock5Priority = _QosTrafficPriorityBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 20),
    _QosTrafficPriorityBlock5Priority_Type()
)
qosTrafficPriorityBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock5Priority.setStatus("current")


class _QosTrafficPriorityBlock6Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock6Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock6Priority_Object = MibTableColumn
qosTrafficPriorityBlock6Priority = _QosTrafficPriorityBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 21),
    _QosTrafficPriorityBlock6Priority_Type()
)
qosTrafficPriorityBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock6Priority.setStatus("current")


class _QosTrafficPriorityBlock7Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock7Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock7Priority_Object = MibTableColumn
qosTrafficPriorityBlock7Priority = _QosTrafficPriorityBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 22),
    _QosTrafficPriorityBlock7Priority_Type()
)
qosTrafficPriorityBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock7Priority.setStatus("current")


class _QosTrafficPriorityBlock8Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock8Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock8Priority_Object = MibTableColumn
qosTrafficPriorityBlock8Priority = _QosTrafficPriorityBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 23),
    _QosTrafficPriorityBlock8Priority_Type()
)
qosTrafficPriorityBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock8Priority.setStatus("current")


class _QosTrafficPriorityBlock9Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock9Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock9Priority_Object = MibTableColumn
qosTrafficPriorityBlock9Priority = _QosTrafficPriorityBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 24),
    _QosTrafficPriorityBlock9Priority_Type()
)
qosTrafficPriorityBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock9Priority.setStatus("current")


class _QosTrafficPriorityBlock10Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock10Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock10Priority_Object = MibTableColumn
qosTrafficPriorityBlock10Priority = _QosTrafficPriorityBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 25),
    _QosTrafficPriorityBlock10Priority_Type()
)
qosTrafficPriorityBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock10Priority.setStatus("current")


class _QosTrafficPriorityBlock11Priority_Type(Integer32):
    """Custom type qosTrafficPriorityBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficPriorityBlock11Priority_Type.__name__ = "Integer32"
_QosTrafficPriorityBlock11Priority_Object = MibTableColumn
qosTrafficPriorityBlock11Priority = _QosTrafficPriorityBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 18, 1, 26),
    _QosTrafficPriorityBlock11Priority_Type()
)
qosTrafficPriorityBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficPriorityBlock11Priority.setStatus("current")
_QosTrafficRedirectTable_Object = MibTable
qosTrafficRedirectTable = _QosTrafficRedirectTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19)
)
if mibBuilder.loadTexts:
    qosTrafficRedirectTable.setStatus("current")
_QosTrafficRedirectEntry_Object = MibTableRow
qosTrafficRedirectEntry = _QosTrafficRedirectEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1)
)
qosTrafficRedirectEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosTrafficRedirectIndex"),
)
if mibBuilder.loadTexts:
    qosTrafficRedirectEntry.setStatus("current")
_QosTrafficRedirectIndex_Type = Integer32
_QosTrafficRedirectIndex_Object = MibTableColumn
qosTrafficRedirectIndex = _QosTrafficRedirectIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 1),
    _QosTrafficRedirectIndex_Type()
)
qosTrafficRedirectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectIndex.setStatus("current")


class _QosTrafficRedirectUserGroupName_Type(OctetString):
    """Custom type qosTrafficRedirectUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficRedirectUserGroupName_Type.__name__ = "OctetString"
_QosTrafficRedirectUserGroupName_Object = MibTableColumn
qosTrafficRedirectUserGroupName = _QosTrafficRedirectUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 2),
    _QosTrafficRedirectUserGroupName_Type()
)
qosTrafficRedirectUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRedirectUserGroupName.setStatus("current")


class _QosTrafficRedirectUserGroupSubitem_Type(Integer32):
    """Custom type qosTrafficRedirectUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficRedirectUserGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficRedirectUserGroupSubitem_Object = MibTableColumn
qosTrafficRedirectUserGroupSubitem = _QosTrafficRedirectUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 3),
    _QosTrafficRedirectUserGroupSubitem_Type()
)
qosTrafficRedirectUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRedirectUserGroupSubitem.setStatus("current")


class _QosTrafficRedirectIpGroupName_Type(OctetString):
    """Custom type qosTrafficRedirectIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficRedirectIpGroupName_Type.__name__ = "OctetString"
_QosTrafficRedirectIpGroupName_Object = MibTableColumn
qosTrafficRedirectIpGroupName = _QosTrafficRedirectIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 4),
    _QosTrafficRedirectIpGroupName_Type()
)
qosTrafficRedirectIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRedirectIpGroupName.setStatus("current")


class _QosTrafficRedirectIpGroupSubitem_Type(Integer32):
    """Custom type qosTrafficRedirectIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficRedirectIpGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficRedirectIpGroupSubitem_Object = MibTableColumn
qosTrafficRedirectIpGroupSubitem = _QosTrafficRedirectIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 5),
    _QosTrafficRedirectIpGroupSubitem_Type()
)
qosTrafficRedirectIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRedirectIpGroupSubitem.setStatus("current")


class _QosTrafficRedirectLinkGroupName_Type(OctetString):
    """Custom type qosTrafficRedirectLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficRedirectLinkGroupName_Type.__name__ = "OctetString"
_QosTrafficRedirectLinkGroupName_Object = MibTableColumn
qosTrafficRedirectLinkGroupName = _QosTrafficRedirectLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 6),
    _QosTrafficRedirectLinkGroupName_Type()
)
qosTrafficRedirectLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRedirectLinkGroupName.setStatus("current")


class _QosTrafficRedirectLinkGroupSubitem_Type(Integer32):
    """Custom type qosTrafficRedirectLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficRedirectLinkGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficRedirectLinkGroupSubitem_Object = MibTableColumn
qosTrafficRedirectLinkGroupSubitem = _QosTrafficRedirectLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 7),
    _QosTrafficRedirectLinkGroupSubitem_Type()
)
qosTrafficRedirectLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRedirectLinkGroupSubitem.setStatus("current")


class _QosTrafficRedirectInterface_Type(Integer32):
    """Custom type qosTrafficRedirectInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_QosTrafficRedirectInterface_Type.__name__ = "Integer32"
_QosTrafficRedirectInterface_Object = MibTableColumn
qosTrafficRedirectInterface = _QosTrafficRedirectInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 8),
    _QosTrafficRedirectInterface_Type()
)
qosTrafficRedirectInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRedirectInterface.setStatus("current")


class _QosTrafficRedirectBlock0Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock0Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock0Priority_Object = MibTableColumn
qosTrafficRedirectBlock0Priority = _QosTrafficRedirectBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 9),
    _QosTrafficRedirectBlock0Priority_Type()
)
qosTrafficRedirectBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock0Priority.setStatus("current")


class _QosTrafficRedirectBlock1Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock1Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock1Priority_Object = MibTableColumn
qosTrafficRedirectBlock1Priority = _QosTrafficRedirectBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 10),
    _QosTrafficRedirectBlock1Priority_Type()
)
qosTrafficRedirectBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock1Priority.setStatus("current")


class _QosTrafficRedirectBlock2Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock2Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock2Priority_Object = MibTableColumn
qosTrafficRedirectBlock2Priority = _QosTrafficRedirectBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 11),
    _QosTrafficRedirectBlock2Priority_Type()
)
qosTrafficRedirectBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock2Priority.setStatus("current")


class _QosTrafficRedirectBlock3Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock3Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock3Priority_Object = MibTableColumn
qosTrafficRedirectBlock3Priority = _QosTrafficRedirectBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 12),
    _QosTrafficRedirectBlock3Priority_Type()
)
qosTrafficRedirectBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock3Priority.setStatus("current")


class _QosTrafficRedirectBlock4Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock4Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock4Priority_Object = MibTableColumn
qosTrafficRedirectBlock4Priority = _QosTrafficRedirectBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 13),
    _QosTrafficRedirectBlock4Priority_Type()
)
qosTrafficRedirectBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock4Priority.setStatus("current")


class _QosTrafficRedirectConfigSequence_Type(Integer32):
    """Custom type qosTrafficRedirectConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosTrafficRedirectConfigSequence_Type.__name__ = "Integer32"
_QosTrafficRedirectConfigSequence_Object = MibTableColumn
qosTrafficRedirectConfigSequence = _QosTrafficRedirectConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 14),
    _QosTrafficRedirectConfigSequence_Type()
)
qosTrafficRedirectConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectConfigSequence.setStatus("current")
_QosTrafficRedirectRunning_Type = TruthValue
_QosTrafficRedirectRunning_Object = MibTableColumn
qosTrafficRedirectRunning = _QosTrafficRedirectRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 15),
    _QosTrafficRedirectRunning_Type()
)
qosTrafficRedirectRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectRunning.setStatus("current")
_QosTrafficRedirectRowStatus_Type = RowStatus
_QosTrafficRedirectRowStatus_Object = MibTableColumn
qosTrafficRedirectRowStatus = _QosTrafficRedirectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 16),
    _QosTrafficRedirectRowStatus_Type()
)
qosTrafficRedirectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTrafficRedirectRowStatus.setStatus("current")


class _QosTrafficRedirectBlock5Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock5Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock5Priority_Object = MibTableColumn
qosTrafficRedirectBlock5Priority = _QosTrafficRedirectBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 17),
    _QosTrafficRedirectBlock5Priority_Type()
)
qosTrafficRedirectBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock5Priority.setStatus("current")


class _QosTrafficRedirectBlock6Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock6Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock6Priority_Object = MibTableColumn
qosTrafficRedirectBlock6Priority = _QosTrafficRedirectBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 18),
    _QosTrafficRedirectBlock6Priority_Type()
)
qosTrafficRedirectBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock6Priority.setStatus("current")


class _QosTrafficRedirectBlock7Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock7Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock7Priority_Object = MibTableColumn
qosTrafficRedirectBlock7Priority = _QosTrafficRedirectBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 19),
    _QosTrafficRedirectBlock7Priority_Type()
)
qosTrafficRedirectBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock7Priority.setStatus("current")


class _QosTrafficRedirectBlock8Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock8Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock8Priority_Object = MibTableColumn
qosTrafficRedirectBlock8Priority = _QosTrafficRedirectBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 20),
    _QosTrafficRedirectBlock8Priority_Type()
)
qosTrafficRedirectBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock8Priority.setStatus("current")


class _QosTrafficRedirectBlock9Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock9Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock9Priority_Object = MibTableColumn
qosTrafficRedirectBlock9Priority = _QosTrafficRedirectBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 21),
    _QosTrafficRedirectBlock9Priority_Type()
)
qosTrafficRedirectBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock9Priority.setStatus("current")


class _QosTrafficRedirectBlock10Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock10Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock10Priority_Object = MibTableColumn
qosTrafficRedirectBlock10Priority = _QosTrafficRedirectBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 22),
    _QosTrafficRedirectBlock10Priority_Type()
)
qosTrafficRedirectBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock10Priority.setStatus("current")


class _QosTrafficRedirectBlock11Priority_Type(Integer32):
    """Custom type qosTrafficRedirectBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRedirectBlock11Priority_Type.__name__ = "Integer32"
_QosTrafficRedirectBlock11Priority_Object = MibTableColumn
qosTrafficRedirectBlock11Priority = _QosTrafficRedirectBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 19, 1, 23),
    _QosTrafficRedirectBlock11Priority_Type()
)
qosTrafficRedirectBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRedirectBlock11Priority.setStatus("current")
_QosTrafficStatisticsTable_Object = MibTable
qosTrafficStatisticsTable = _QosTrafficStatisticsTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20)
)
if mibBuilder.loadTexts:
    qosTrafficStatisticsTable.setStatus("current")
_QosTrafficStatisticsEntry_Object = MibTableRow
qosTrafficStatisticsEntry = _QosTrafficStatisticsEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1)
)
qosTrafficStatisticsEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosTrafficStatisticsIndex"),
)
if mibBuilder.loadTexts:
    qosTrafficStatisticsEntry.setStatus("current")
_QosTrafficStatisticsIndex_Type = Integer32
_QosTrafficStatisticsIndex_Object = MibTableColumn
qosTrafficStatisticsIndex = _QosTrafficStatisticsIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 1),
    _QosTrafficStatisticsIndex_Type()
)
qosTrafficStatisticsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsIndex.setStatus("current")


class _QosTrafficStatisticsUserGroupName_Type(OctetString):
    """Custom type qosTrafficStatisticsUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficStatisticsUserGroupName_Type.__name__ = "OctetString"
_QosTrafficStatisticsUserGroupName_Object = MibTableColumn
qosTrafficStatisticsUserGroupName = _QosTrafficStatisticsUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 2),
    _QosTrafficStatisticsUserGroupName_Type()
)
qosTrafficStatisticsUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficStatisticsUserGroupName.setStatus("current")


class _QosTrafficStatisticsUserGroupSubitem_Type(Integer32):
    """Custom type qosTrafficStatisticsUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficStatisticsUserGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficStatisticsUserGroupSubitem_Object = MibTableColumn
qosTrafficStatisticsUserGroupSubitem = _QosTrafficStatisticsUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 3),
    _QosTrafficStatisticsUserGroupSubitem_Type()
)
qosTrafficStatisticsUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficStatisticsUserGroupSubitem.setStatus("current")


class _QosTrafficStatisticsIpGroupName_Type(OctetString):
    """Custom type qosTrafficStatisticsIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficStatisticsIpGroupName_Type.__name__ = "OctetString"
_QosTrafficStatisticsIpGroupName_Object = MibTableColumn
qosTrafficStatisticsIpGroupName = _QosTrafficStatisticsIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 4),
    _QosTrafficStatisticsIpGroupName_Type()
)
qosTrafficStatisticsIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficStatisticsIpGroupName.setStatus("current")


class _QosTrafficStatisticsIpGroupSubitem_Type(Integer32):
    """Custom type qosTrafficStatisticsIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficStatisticsIpGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficStatisticsIpGroupSubitem_Object = MibTableColumn
qosTrafficStatisticsIpGroupSubitem = _QosTrafficStatisticsIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 5),
    _QosTrafficStatisticsIpGroupSubitem_Type()
)
qosTrafficStatisticsIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficStatisticsIpGroupSubitem.setStatus("current")


class _QosTrafficStatisticsLinkGroupName_Type(OctetString):
    """Custom type qosTrafficStatisticsLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficStatisticsLinkGroupName_Type.__name__ = "OctetString"
_QosTrafficStatisticsLinkGroupName_Object = MibTableColumn
qosTrafficStatisticsLinkGroupName = _QosTrafficStatisticsLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 6),
    _QosTrafficStatisticsLinkGroupName_Type()
)
qosTrafficStatisticsLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficStatisticsLinkGroupName.setStatus("current")


class _QosTrafficStatisticsLinkGroupSubitem_Type(Integer32):
    """Custom type qosTrafficStatisticsLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficStatisticsLinkGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficStatisticsLinkGroupSubitem_Object = MibTableColumn
qosTrafficStatisticsLinkGroupSubitem = _QosTrafficStatisticsLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 7),
    _QosTrafficStatisticsLinkGroupSubitem_Type()
)
qosTrafficStatisticsLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficStatisticsLinkGroupSubitem.setStatus("current")


class _QosTrafficStatisticsBlock0Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock0Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock0Priority_Object = MibTableColumn
qosTrafficStatisticsBlock0Priority = _QosTrafficStatisticsBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 8),
    _QosTrafficStatisticsBlock0Priority_Type()
)
qosTrafficStatisticsBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock0Priority.setStatus("current")


class _QosTrafficStatisticsBlock1Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock1Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock1Priority_Object = MibTableColumn
qosTrafficStatisticsBlock1Priority = _QosTrafficStatisticsBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 9),
    _QosTrafficStatisticsBlock1Priority_Type()
)
qosTrafficStatisticsBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock1Priority.setStatus("current")


class _QosTrafficStatisticsBlock2Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock2Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock2Priority_Object = MibTableColumn
qosTrafficStatisticsBlock2Priority = _QosTrafficStatisticsBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 10),
    _QosTrafficStatisticsBlock2Priority_Type()
)
qosTrafficStatisticsBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock2Priority.setStatus("current")


class _QosTrafficStatisticsBlock3Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock3Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock3Priority_Object = MibTableColumn
qosTrafficStatisticsBlock3Priority = _QosTrafficStatisticsBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 11),
    _QosTrafficStatisticsBlock3Priority_Type()
)
qosTrafficStatisticsBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock3Priority.setStatus("current")


class _QosTrafficStatisticsBlock4Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock4Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock4Priority_Object = MibTableColumn
qosTrafficStatisticsBlock4Priority = _QosTrafficStatisticsBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 12),
    _QosTrafficStatisticsBlock4Priority_Type()
)
qosTrafficStatisticsBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock4Priority.setStatus("current")


class _QosTrafficStatisticsConfigSequence_Type(Integer32):
    """Custom type qosTrafficStatisticsConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosTrafficStatisticsConfigSequence_Type.__name__ = "Integer32"
_QosTrafficStatisticsConfigSequence_Object = MibTableColumn
qosTrafficStatisticsConfigSequence = _QosTrafficStatisticsConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 13),
    _QosTrafficStatisticsConfigSequence_Type()
)
qosTrafficStatisticsConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsConfigSequence.setStatus("current")
_QosTrafficStatisticsRunning_Type = TruthValue
_QosTrafficStatisticsRunning_Object = MibTableColumn
qosTrafficStatisticsRunning = _QosTrafficStatisticsRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 14),
    _QosTrafficStatisticsRunning_Type()
)
qosTrafficStatisticsRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsRunning.setStatus("current")
_QosTrafficStatisticsRowStatus_Type = RowStatus
_QosTrafficStatisticsRowStatus_Object = MibTableColumn
qosTrafficStatisticsRowStatus = _QosTrafficStatisticsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 15),
    _QosTrafficStatisticsRowStatus_Type()
)
qosTrafficStatisticsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTrafficStatisticsRowStatus.setStatus("current")
_QosTrafficStatisticsCounter_Type = Integer32
_QosTrafficStatisticsCounter_Object = MibTableColumn
qosTrafficStatisticsCounter = _QosTrafficStatisticsCounter_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 16),
    _QosTrafficStatisticsCounter_Type()
)
qosTrafficStatisticsCounter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTrafficStatisticsCounter.setStatus("current")


class _QosTrafficStatisticsBlock5Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock5Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock5Priority_Object = MibTableColumn
qosTrafficStatisticsBlock5Priority = _QosTrafficStatisticsBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 17),
    _QosTrafficStatisticsBlock5Priority_Type()
)
qosTrafficStatisticsBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock5Priority.setStatus("current")


class _QosTrafficStatisticsBlock6Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock6Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock6Priority_Object = MibTableColumn
qosTrafficStatisticsBlock6Priority = _QosTrafficStatisticsBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 18),
    _QosTrafficStatisticsBlock6Priority_Type()
)
qosTrafficStatisticsBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock6Priority.setStatus("current")


class _QosTrafficStatisticsBlock7Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock7Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock7Priority_Object = MibTableColumn
qosTrafficStatisticsBlock7Priority = _QosTrafficStatisticsBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 19),
    _QosTrafficStatisticsBlock7Priority_Type()
)
qosTrafficStatisticsBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock7Priority.setStatus("current")


class _QosTrafficStatisticsBlock8Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock8Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock8Priority_Object = MibTableColumn
qosTrafficStatisticsBlock8Priority = _QosTrafficStatisticsBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 20),
    _QosTrafficStatisticsBlock8Priority_Type()
)
qosTrafficStatisticsBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock8Priority.setStatus("current")


class _QosTrafficStatisticsBlock9Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock9Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock9Priority_Object = MibTableColumn
qosTrafficStatisticsBlock9Priority = _QosTrafficStatisticsBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 21),
    _QosTrafficStatisticsBlock9Priority_Type()
)
qosTrafficStatisticsBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock9Priority.setStatus("current")


class _QosTrafficStatisticsBlock10Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock10Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock10Priority_Object = MibTableColumn
qosTrafficStatisticsBlock10Priority = _QosTrafficStatisticsBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 22),
    _QosTrafficStatisticsBlock10Priority_Type()
)
qosTrafficStatisticsBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock10Priority.setStatus("current")


class _QosTrafficStatisticsBlock11Priority_Type(Integer32):
    """Custom type qosTrafficStatisticsBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficStatisticsBlock11Priority_Type.__name__ = "Integer32"
_QosTrafficStatisticsBlock11Priority_Object = MibTableColumn
qosTrafficStatisticsBlock11Priority = _QosTrafficStatisticsBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 20, 1, 23),
    _QosTrafficStatisticsBlock11Priority_Type()
)
qosTrafficStatisticsBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficStatisticsBlock11Priority.setStatus("current")
_QosLineRateTable_Object = MibTable
qosLineRateTable = _QosLineRateTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 21)
)
if mibBuilder.loadTexts:
    qosLineRateTable.setStatus("current")
_QosLineRateEntry_Object = MibTableRow
qosLineRateEntry = _QosLineRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 21, 1)
)
qosLineRateEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosLineRateInterface"),
)
if mibBuilder.loadTexts:
    qosLineRateEntry.setStatus("current")


class _QosLineRateInterface_Type(Integer32):
    """Custom type qosLineRateInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_QosLineRateInterface_Type.__name__ = "Integer32"
_QosLineRateInterface_Object = MibTableColumn
qosLineRateInterface = _QosLineRateInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 21, 1, 1),
    _QosLineRateInterface_Type()
)
qosLineRateInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosLineRateInterface.setStatus("current")


class _QosLineRateTargetRate_Type(Integer32):
    """Custom type qosLineRateTargetRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_QosLineRateTargetRate_Type.__name__ = "Integer32"
_QosLineRateTargetRate_Object = MibTableColumn
qosLineRateTargetRate = _QosLineRateTargetRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 21, 1, 2),
    _QosLineRateTargetRate_Type()
)
qosLineRateTargetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosLineRateTargetRate.setStatus("current")
_QosTrafficCopyToCpuTable_Object = MibTable
qosTrafficCopyToCpuTable = _QosTrafficCopyToCpuTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22)
)
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuTable.setStatus("current")
_QosTrafficCopyToCpuEntry_Object = MibTableRow
qosTrafficCopyToCpuEntry = _QosTrafficCopyToCpuEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1)
)
qosTrafficCopyToCpuEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosTrafficCopyToCpuIndex"),
)
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuEntry.setStatus("current")
_QosTrafficCopyToCpuIndex_Type = Integer32
_QosTrafficCopyToCpuIndex_Object = MibTableColumn
qosTrafficCopyToCpuIndex = _QosTrafficCopyToCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 1),
    _QosTrafficCopyToCpuIndex_Type()
)
qosTrafficCopyToCpuIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuIndex.setStatus("current")


class _QosTrafficCopyToCpuUserGroupName_Type(OctetString):
    """Custom type qosTrafficCopyToCpuUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficCopyToCpuUserGroupName_Type.__name__ = "OctetString"
_QosTrafficCopyToCpuUserGroupName_Object = MibTableColumn
qosTrafficCopyToCpuUserGroupName = _QosTrafficCopyToCpuUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 2),
    _QosTrafficCopyToCpuUserGroupName_Type()
)
qosTrafficCopyToCpuUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuUserGroupName.setStatus("current")


class _QosTrafficCopyToCpuUserGroupSubitem_Type(Integer32):
    """Custom type qosTrafficCopyToCpuUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficCopyToCpuUserGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuUserGroupSubitem_Object = MibTableColumn
qosTrafficCopyToCpuUserGroupSubitem = _QosTrafficCopyToCpuUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 3),
    _QosTrafficCopyToCpuUserGroupSubitem_Type()
)
qosTrafficCopyToCpuUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuUserGroupSubitem.setStatus("current")


class _QosTrafficCopyToCpuIpGroupName_Type(OctetString):
    """Custom type qosTrafficCopyToCpuIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficCopyToCpuIpGroupName_Type.__name__ = "OctetString"
_QosTrafficCopyToCpuIpGroupName_Object = MibTableColumn
qosTrafficCopyToCpuIpGroupName = _QosTrafficCopyToCpuIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 4),
    _QosTrafficCopyToCpuIpGroupName_Type()
)
qosTrafficCopyToCpuIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuIpGroupName.setStatus("current")


class _QosTrafficCopyToCpuIpGroupSubitem_Type(Integer32):
    """Custom type qosTrafficCopyToCpuIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficCopyToCpuIpGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuIpGroupSubitem_Object = MibTableColumn
qosTrafficCopyToCpuIpGroupSubitem = _QosTrafficCopyToCpuIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 5),
    _QosTrafficCopyToCpuIpGroupSubitem_Type()
)
qosTrafficCopyToCpuIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuIpGroupSubitem.setStatus("current")


class _QosTrafficCopyToCpuLinkGroupName_Type(OctetString):
    """Custom type qosTrafficCopyToCpuLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficCopyToCpuLinkGroupName_Type.__name__ = "OctetString"
_QosTrafficCopyToCpuLinkGroupName_Object = MibTableColumn
qosTrafficCopyToCpuLinkGroupName = _QosTrafficCopyToCpuLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 6),
    _QosTrafficCopyToCpuLinkGroupName_Type()
)
qosTrafficCopyToCpuLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuLinkGroupName.setStatus("current")


class _QosTrafficCopyToCpuLinkGroupSubitem_Type(Integer32):
    """Custom type qosTrafficCopyToCpuLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficCopyToCpuLinkGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuLinkGroupSubitem_Object = MibTableColumn
qosTrafficCopyToCpuLinkGroupSubitem = _QosTrafficCopyToCpuLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 7),
    _QosTrafficCopyToCpuLinkGroupSubitem_Type()
)
qosTrafficCopyToCpuLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuLinkGroupSubitem.setStatus("current")


class _QosTrafficCopyToCpuBlock0Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock0Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock0Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock0Priority = _QosTrafficCopyToCpuBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 8),
    _QosTrafficCopyToCpuBlock0Priority_Type()
)
qosTrafficCopyToCpuBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock0Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock1Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock1Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock1Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock1Priority = _QosTrafficCopyToCpuBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 9),
    _QosTrafficCopyToCpuBlock1Priority_Type()
)
qosTrafficCopyToCpuBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock1Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock2Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock2Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock2Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock2Priority = _QosTrafficCopyToCpuBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 10),
    _QosTrafficCopyToCpuBlock2Priority_Type()
)
qosTrafficCopyToCpuBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock2Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock3Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock3Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock3Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock3Priority = _QosTrafficCopyToCpuBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 11),
    _QosTrafficCopyToCpuBlock3Priority_Type()
)
qosTrafficCopyToCpuBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock3Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock4Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock4Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock4Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock4Priority = _QosTrafficCopyToCpuBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 12),
    _QosTrafficCopyToCpuBlock4Priority_Type()
)
qosTrafficCopyToCpuBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock4Priority.setStatus("current")


class _QosTrafficCopyToCpuConfigSequence_Type(Integer32):
    """Custom type qosTrafficCopyToCpuConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosTrafficCopyToCpuConfigSequence_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuConfigSequence_Object = MibTableColumn
qosTrafficCopyToCpuConfigSequence = _QosTrafficCopyToCpuConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 13),
    _QosTrafficCopyToCpuConfigSequence_Type()
)
qosTrafficCopyToCpuConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuConfigSequence.setStatus("current")
_QosTrafficCopyToCpuRunning_Type = TruthValue
_QosTrafficCopyToCpuRunning_Object = MibTableColumn
qosTrafficCopyToCpuRunning = _QosTrafficCopyToCpuRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 14),
    _QosTrafficCopyToCpuRunning_Type()
)
qosTrafficCopyToCpuRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuRunning.setStatus("current")
_QosTrafficCopyToCpuRowStatus_Type = RowStatus
_QosTrafficCopyToCpuRowStatus_Object = MibTableColumn
qosTrafficCopyToCpuRowStatus = _QosTrafficCopyToCpuRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 15),
    _QosTrafficCopyToCpuRowStatus_Type()
)
qosTrafficCopyToCpuRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuRowStatus.setStatus("current")


class _QosTrafficCopyToCpuBlock5Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock5Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock5Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock5Priority = _QosTrafficCopyToCpuBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 16),
    _QosTrafficCopyToCpuBlock5Priority_Type()
)
qosTrafficCopyToCpuBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock5Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock6Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock6Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock6Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock6Priority = _QosTrafficCopyToCpuBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 17),
    _QosTrafficCopyToCpuBlock6Priority_Type()
)
qosTrafficCopyToCpuBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock6Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock7Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock7Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock7Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock7Priority = _QosTrafficCopyToCpuBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 18),
    _QosTrafficCopyToCpuBlock7Priority_Type()
)
qosTrafficCopyToCpuBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock7Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock8Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock8Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock8Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock8Priority = _QosTrafficCopyToCpuBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 19),
    _QosTrafficCopyToCpuBlock8Priority_Type()
)
qosTrafficCopyToCpuBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock8Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock9Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock9Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock9Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock9Priority = _QosTrafficCopyToCpuBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 20),
    _QosTrafficCopyToCpuBlock9Priority_Type()
)
qosTrafficCopyToCpuBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock9Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock10Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock10Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock10Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock10Priority = _QosTrafficCopyToCpuBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 21),
    _QosTrafficCopyToCpuBlock10Priority_Type()
)
qosTrafficCopyToCpuBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock10Priority.setStatus("current")


class _QosTrafficCopyToCpuBlock11Priority_Type(Integer32):
    """Custom type qosTrafficCopyToCpuBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficCopyToCpuBlock11Priority_Type.__name__ = "Integer32"
_QosTrafficCopyToCpuBlock11Priority_Object = MibTableColumn
qosTrafficCopyToCpuBlock11Priority = _QosTrafficCopyToCpuBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 22, 1, 22),
    _QosTrafficCopyToCpuBlock11Priority_Type()
)
qosTrafficCopyToCpuBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficCopyToCpuBlock11Priority.setStatus("current")
_QaclAppPortIsolationGroup_ObjectIdentity = ObjectIdentity
qaclAppPortIsolationGroup = _QaclAppPortIsolationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 23)
)
_QaclAppPortIsolationDownLinkPorts_Type = PortList
_QaclAppPortIsolationDownLinkPorts_Object = MibScalar
qaclAppPortIsolationDownLinkPorts = _QaclAppPortIsolationDownLinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 23, 1),
    _QaclAppPortIsolationDownLinkPorts_Type()
)
qaclAppPortIsolationDownLinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qaclAppPortIsolationDownLinkPorts.setStatus("current")
_StormControlTable_Object = MibTable
stormControlTable = _StormControlTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 24)
)
if mibBuilder.loadTexts:
    stormControlTable.setStatus("current")
_StormControlEntry_Object = MibTableRow
stormControlEntry = _StormControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 24, 1)
)
stormControlEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "stormControlInterface"),
    (0, "QTECH-GBNL2QACL-MIB", "stormControlType"),
)
if mibBuilder.loadTexts:
    stormControlEntry.setStatus("current")


class _StormControlInterface_Type(Integer32):
    """Custom type stormControlInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 26),
    )


_StormControlInterface_Type.__name__ = "Integer32"
_StormControlInterface_Object = MibTableColumn
stormControlInterface = _StormControlInterface_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 24, 1, 1),
    _StormControlInterface_Type()
)
stormControlInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormControlInterface.setStatus("current")
_StormControlType_Type = PacketFlowType
_StormControlType_Object = MibTableColumn
stormControlType = _StormControlType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 24, 1, 2),
    _StormControlType_Type()
)
stormControlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stormControlType.setStatus("current")


class _StormControlTargetRate_Type(Integer32):
    """Custom type stormControlTargetRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_StormControlTargetRate_Type.__name__ = "Integer32"
_StormControlTargetRate_Object = MibTableColumn
stormControlTargetRate = _StormControlTargetRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 24, 1, 3),
    _StormControlTargetRate_Type()
)
stormControlTargetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormControlTargetRate.setStatus("current")
_StormControlRowStatus_Type = RowStatus
_StormControlRowStatus_Object = MibTableColumn
stormControlRowStatus = _StormControlRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 24, 1, 4),
    _StormControlRowStatus_Type()
)
stormControlRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stormControlRowStatus.setStatus("current")
_QosTrafficRewriteVlanTable_Object = MibTable
qosTrafficRewriteVlanTable = _QosTrafficRewriteVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25)
)
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanTable.setStatus("current")
_QosTrafficRewriteVlanEntry_Object = MibTableRow
qosTrafficRewriteVlanEntry = _QosTrafficRewriteVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1)
)
qosTrafficRewriteVlanEntry.setIndexNames(
    (0, "QTECH-GBNL2QACL-MIB", "qosTrafficRewriteVlanIndex"),
)
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanEntry.setStatus("current")
_QosTrafficRewriteVlanIndex_Type = Integer32
_QosTrafficRewriteVlanIndex_Object = MibTableColumn
qosTrafficRewriteVlanIndex = _QosTrafficRewriteVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 1),
    _QosTrafficRewriteVlanIndex_Type()
)
qosTrafficRewriteVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanIndex.setStatus("current")


class _QosTrafficRewriteVlanUserGroupName_Type(OctetString):
    """Custom type qosTrafficRewriteVlanUserGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficRewriteVlanUserGroupName_Type.__name__ = "OctetString"
_QosTrafficRewriteVlanUserGroupName_Object = MibTableColumn
qosTrafficRewriteVlanUserGroupName = _QosTrafficRewriteVlanUserGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 2),
    _QosTrafficRewriteVlanUserGroupName_Type()
)
qosTrafficRewriteVlanUserGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanUserGroupName.setStatus("current")


class _QosTrafficRewriteVlanUserGroupSubitem_Type(Integer32):
    """Custom type qosTrafficRewriteVlanUserGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficRewriteVlanUserGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanUserGroupSubitem_Object = MibTableColumn
qosTrafficRewriteVlanUserGroupSubitem = _QosTrafficRewriteVlanUserGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 3),
    _QosTrafficRewriteVlanUserGroupSubitem_Type()
)
qosTrafficRewriteVlanUserGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanUserGroupSubitem.setStatus("current")


class _QosTrafficRewriteVlanIpGroupName_Type(OctetString):
    """Custom type qosTrafficRewriteVlanIpGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficRewriteVlanIpGroupName_Type.__name__ = "OctetString"
_QosTrafficRewriteVlanIpGroupName_Object = MibTableColumn
qosTrafficRewriteVlanIpGroupName = _QosTrafficRewriteVlanIpGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 4),
    _QosTrafficRewriteVlanIpGroupName_Type()
)
qosTrafficRewriteVlanIpGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanIpGroupName.setStatus("current")


class _QosTrafficRewriteVlanIpGroupSubitem_Type(Integer32):
    """Custom type qosTrafficRewriteVlanIpGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficRewriteVlanIpGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanIpGroupSubitem_Object = MibTableColumn
qosTrafficRewriteVlanIpGroupSubitem = _QosTrafficRewriteVlanIpGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 5),
    _QosTrafficRewriteVlanIpGroupSubitem_Type()
)
qosTrafficRewriteVlanIpGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanIpGroupSubitem.setStatus("current")


class _QosTrafficRewriteVlanLinkGroupName_Type(OctetString):
    """Custom type qosTrafficRewriteVlanLinkGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_QosTrafficRewriteVlanLinkGroupName_Type.__name__ = "OctetString"
_QosTrafficRewriteVlanLinkGroupName_Object = MibTableColumn
qosTrafficRewriteVlanLinkGroupName = _QosTrafficRewriteVlanLinkGroupName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 6),
    _QosTrafficRewriteVlanLinkGroupName_Type()
)
qosTrafficRewriteVlanLinkGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanLinkGroupName.setStatus("current")


class _QosTrafficRewriteVlanLinkGroupSubitem_Type(Integer32):
    """Custom type qosTrafficRewriteVlanLinkGroupSubitem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_QosTrafficRewriteVlanLinkGroupSubitem_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanLinkGroupSubitem_Object = MibTableColumn
qosTrafficRewriteVlanLinkGroupSubitem = _QosTrafficRewriteVlanLinkGroupSubitem_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 7),
    _QosTrafficRewriteVlanLinkGroupSubitem_Type()
)
qosTrafficRewriteVlanLinkGroupSubitem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanLinkGroupSubitem.setStatus("current")


class _QosTrafficRewriteVlanVid_Type(Integer32):
    """Custom type qosTrafficRewriteVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 28),
    )


_QosTrafficRewriteVlanVid_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanVid_Object = MibScalar
qosTrafficRewriteVlanVid = _QosTrafficRewriteVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 8),
    _QosTrafficRewriteVlanVid_Type()
)
qosTrafficRewriteVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanVid.setStatus("current")


class _QosTrafficRewriteVlanBlock0Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock0Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock0Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock0Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock0Priority = _QosTrafficRewriteVlanBlock0Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 9),
    _QosTrafficRewriteVlanBlock0Priority_Type()
)
qosTrafficRewriteVlanBlock0Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock0Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock1Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock1Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock1Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock1Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock1Priority = _QosTrafficRewriteVlanBlock1Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 10),
    _QosTrafficRewriteVlanBlock1Priority_Type()
)
qosTrafficRewriteVlanBlock1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock1Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock2Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock2Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock2Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock2Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock2Priority = _QosTrafficRewriteVlanBlock2Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 11),
    _QosTrafficRewriteVlanBlock2Priority_Type()
)
qosTrafficRewriteVlanBlock2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock2Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock3Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock3Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock3Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock3Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock3Priority = _QosTrafficRewriteVlanBlock3Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 12),
    _QosTrafficRewriteVlanBlock3Priority_Type()
)
qosTrafficRewriteVlanBlock3Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock3Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock4Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock4Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock4Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock4Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock4Priority = _QosTrafficRewriteVlanBlock4Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 13),
    _QosTrafficRewriteVlanBlock4Priority_Type()
)
qosTrafficRewriteVlanBlock4Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock4Priority.setStatus("current")


class _QosTrafficRewriteVlanConfigSequence_Type(Integer32):
    """Custom type qosTrafficRewriteVlanConfigSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_QosTrafficRewriteVlanConfigSequence_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanConfigSequence_Object = MibTableColumn
qosTrafficRewriteVlanConfigSequence = _QosTrafficRewriteVlanConfigSequence_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 14),
    _QosTrafficRewriteVlanConfigSequence_Type()
)
qosTrafficRewriteVlanConfigSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanConfigSequence.setStatus("current")
_QosTrafficRewriteVlanRunning_Type = TruthValue
_QosTrafficRewriteVlanRunning_Object = MibTableColumn
qosTrafficRewriteVlanRunning = _QosTrafficRewriteVlanRunning_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 15),
    _QosTrafficRewriteVlanRunning_Type()
)
qosTrafficRewriteVlanRunning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanRunning.setStatus("current")
_QosTrafficRewriteVlanRowStatus_Type = RowStatus
_QosTrafficRewriteVlanRowStatus_Object = MibTableColumn
qosTrafficRewriteVlanRowStatus = _QosTrafficRewriteVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 16),
    _QosTrafficRewriteVlanRowStatus_Type()
)
qosTrafficRewriteVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanRowStatus.setStatus("current")


class _QosTrafficRewriteVlanBlock5Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock5Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock5Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock5Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock5Priority = _QosTrafficRewriteVlanBlock5Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 17),
    _QosTrafficRewriteVlanBlock5Priority_Type()
)
qosTrafficRewriteVlanBlock5Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock5Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock6Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock6Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock6Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock6Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock6Priority = _QosTrafficRewriteVlanBlock6Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 18),
    _QosTrafficRewriteVlanBlock6Priority_Type()
)
qosTrafficRewriteVlanBlock6Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock6Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock7Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock7Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock7Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock7Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock7Priority = _QosTrafficRewriteVlanBlock7Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 19),
    _QosTrafficRewriteVlanBlock7Priority_Type()
)
qosTrafficRewriteVlanBlock7Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock7Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock8Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock8Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock8Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock8Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock8Priority = _QosTrafficRewriteVlanBlock8Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 20),
    _QosTrafficRewriteVlanBlock8Priority_Type()
)
qosTrafficRewriteVlanBlock8Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock8Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock9Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock9Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock9Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock9Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock9Priority = _QosTrafficRewriteVlanBlock9Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 21),
    _QosTrafficRewriteVlanBlock9Priority_Type()
)
qosTrafficRewriteVlanBlock9Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock9Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock10Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock10Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock10Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock10Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock10Priority = _QosTrafficRewriteVlanBlock10Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 22),
    _QosTrafficRewriteVlanBlock10Priority_Type()
)
qosTrafficRewriteVlanBlock10Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock10Priority.setStatus("current")


class _QosTrafficRewriteVlanBlock11Priority_Type(Integer32):
    """Custom type qosTrafficRewriteVlanBlock11Priority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_QosTrafficRewriteVlanBlock11Priority_Type.__name__ = "Integer32"
_QosTrafficRewriteVlanBlock11Priority_Object = MibTableColumn
qosTrafficRewriteVlanBlock11Priority = _QosTrafficRewriteVlanBlock11Priority_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 4, 4, 25, 1, 23),
    _QosTrafficRewriteVlanBlock11Priority_Type()
)
qosTrafficRewriteVlanBlock11Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qosTrafficRewriteVlanBlock11Priority.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-GBNL2QACL-MIB",
    **{"AdminStatus": AdminStatus,
       "Action": Action,
       "Dscp": Dscp,
       "AclType": AclType,
       "PacketFlowType": PacketFlowType,
       "gbnL2QACL": gbnL2QACL,
       "qosQueueSchedulerGroup": qosQueueSchedulerGroup,
       "qosWrrQueue1Weight": qosWrrQueue1Weight,
       "qosWrrQueue2Weight": qosWrrQueue2Weight,
       "qosWrrQueue3Weight": qosWrrQueue3Weight,
       "qosWrrQueue4Weight": qosWrrQueue4Weight,
       "qosWrrMaxDelayValue": qosWrrMaxDelayValue,
       "qosQueueSchedulerMode": qosQueueSchedulerMode,
       "qosWrrQueue5Weight": qosWrrQueue5Weight,
       "qosWrrQueue6Weight": qosWrrQueue6Weight,
       "qosWrrQueue7Weight": qosWrrQueue7Weight,
       "qosWrrQueue8Weight": qosWrrQueue8Weight,
       "aclNumTable": aclNumTable,
       "aclNumEntry": aclNumEntry,
       "aclNumNumber": aclNumNumber,
       "aclNumType": aclNumType,
       "aclNumMatchOrder": aclNumMatchOrder,
       "aclNumTotleSubitems": aclNumTotleSubitems,
       "aclNumRowStatus": aclNumRowStatus,
       "aclNumStdSubitemTable": aclNumStdSubitemTable,
       "aclNumStdSubitemEntry": aclNumStdSubitemEntry,
       "aclNumStdNum": aclNumStdNum,
       "aclNumStdSubNum": aclNumStdSubNum,
       "aclNumStdSubitemAdminStatus": aclNumStdSubitemAdminStatus,
       "aclNumStdSubitemAction": aclNumStdSubitemAction,
       "aclNumStdSubitemSrcAddr": aclNumStdSubitemSrcAddr,
       "aclNumStdSubitemSrcAddrWldmsk": aclNumStdSubitemSrcAddrWldmsk,
       "aclNumStdFragments": aclNumStdFragments,
       "aclNumStdTimeRange": aclNumStdTimeRange,
       "aclNumStdSubitemRowStatus": aclNumStdSubitemRowStatus,
       "aclNumExdSubitemTable": aclNumExdSubitemTable,
       "aclNumExdSubitemEntry": aclNumExdSubitemEntry,
       "aclNumExdNum": aclNumExdNum,
       "aclNumExdSubNum": aclNumExdSubNum,
       "aclNumExdSubitemAdminStatus": aclNumExdSubitemAdminStatus,
       "aclNumExdSubitemAction": aclNumExdSubitemAction,
       "aclNumExdSubitemProtocal": aclNumExdSubitemProtocal,
       "aclNumExdSubitemSrcAddr": aclNumExdSubitemSrcAddr,
       "aclNumExdSubitemSrcAddrWldmsk": aclNumExdSubitemSrcAddrWldmsk,
       "aclNumExdSubitemDstAddr": aclNumExdSubitemDstAddr,
       "aclNumExdSubitemDstAddrWldmsk": aclNumExdSubitemDstAddrWldmsk,
       "aclNumExdSubitemSrcPort": aclNumExdSubitemSrcPort,
       "aclNumExdSubitemSrcPortWldmsk": aclNumExdSubitemSrcPortWldmsk,
       "aclNumExdSubitemDstPort": aclNumExdSubitemDstPort,
       "aclNumExdSubitemDstPortWldmsk": aclNumExdSubitemDstPortWldmsk,
       "aclNumExdSubitemIcmpType": aclNumExdSubitemIcmpType,
       "aclNumExdSubitemIcmpCode": aclNumExdSubitemIcmpCode,
       "aclNumExdSubitemTcpEstablished": aclNumExdSubitemTcpEstablished,
       "aclNumExdSubitemPrecedence": aclNumExdSubitemPrecedence,
       "aclNumExdSubitemTos": aclNumExdSubitemTos,
       "aclNumExdSubitemDscp": aclNumExdSubitemDscp,
       "aclNumExdSubitemFragments": aclNumExdSubitemFragments,
       "aclNumExdSubitemTimeRange": aclNumExdSubitemTimeRange,
       "aclNumExdSubitemRowStatus": aclNumExdSubitemRowStatus,
       "aclNumLnkSubitemTable": aclNumLnkSubitemTable,
       "aclNumLnkSubitemEntry": aclNumLnkSubitemEntry,
       "aclNumLnkNum": aclNumLnkNum,
       "aclNumLnkSubNum": aclNumLnkSubNum,
       "aclNumLnkSubitemAdminStatus": aclNumLnkSubitemAdminStatus,
       "aclNumLnkSubitemAction": aclNumLnkSubitemAction,
       "aclNumLnkSubitemProtocal": aclNumLnkSubitemProtocal,
       "aclNumLnkSubitemCos": aclNumLnkSubitemCos,
       "aclNumLnkSubitemSrcVlanID": aclNumLnkSubitemSrcVlanID,
       "aclNumLnkSubitemSrcMacAddr": aclNumLnkSubitemSrcMacAddr,
       "aclNumLnkSubitemSrcMacWldmsk": aclNumLnkSubitemSrcMacWldmsk,
       "aclNumLnkSubitemDstMacAddr": aclNumLnkSubitemDstMacAddr,
       "aclNumLnkSubitemDstMacWldmsk": aclNumLnkSubitemDstMacWldmsk,
       "aclNumLnkSubitemSrcPortNum": aclNumLnkSubitemSrcPortNum,
       "aclNumLnkSubitemDstPortNum": aclNumLnkSubitemDstPortNum,
       "aclNumLnkSubitemTimeRange": aclNumLnkSubitemTimeRange,
       "aclNumLnkSubitemRowStatus": aclNumLnkSubitemRowStatus,
       "aclNumUserSubitemTable": aclNumUserSubitemTable,
       "aclNumUserSubitemEntry": aclNumUserSubitemEntry,
       "aclNumUserNum": aclNumUserNum,
       "aclNumUserSubNum": aclNumUserSubNum,
       "aclNumUserSubitemAdminStatus": aclNumUserSubitemAdminStatus,
       "aclNumUserSubitemAction": aclNumUserSubitemAction,
       "aclNumUserSubitemSrcPortNum": aclNumUserSubitemSrcPortNum,
       "aclNumUserSubitemDstPortNum": aclNumUserSubitemDstPortNum,
       "aclNumUserSubitemRule": aclNumUserSubitemRule,
       "aclNumUserSubitemMask": aclNumUserSubitemMask,
       "aclNumUserTimeRange": aclNumUserTimeRange,
       "aclNumUserSubitemRowStatus": aclNumUserSubitemRowStatus,
       "aclNamedTable": aclNamedTable,
       "aclNamedEntry": aclNamedEntry,
       "aclNamedName": aclNamedName,
       "aclNamedType": aclNamedType,
       "aclNamedMatchOrder": aclNamedMatchOrder,
       "aclNamedTotleSubitems": aclNamedTotleSubitems,
       "aclNamedRowStatus": aclNamedRowStatus,
       "aclNamedStdSubitemTable": aclNamedStdSubitemTable,
       "aclNamedStdSubitemEntry": aclNamedStdSubitemEntry,
       "aclNamedStdName": aclNamedStdName,
       "aclNamedStdSubNum": aclNamedStdSubNum,
       "aclNamedStdSubitemAdminStatus": aclNamedStdSubitemAdminStatus,
       "aclNamedStdSubitemAction": aclNamedStdSubitemAction,
       "aclNamedStdSubitemSrcAddr": aclNamedStdSubitemSrcAddr,
       "aclNamedStdSubitemSrcAddrWldmsk": aclNamedStdSubitemSrcAddrWldmsk,
       "aclNamedStdFragments": aclNamedStdFragments,
       "aclNamedStdTimeRange": aclNamedStdTimeRange,
       "aclNamedStdSubitemRowStatus": aclNamedStdSubitemRowStatus,
       "aclNamedExdSubitemTable": aclNamedExdSubitemTable,
       "aclNamedExdSubitemEntry": aclNamedExdSubitemEntry,
       "aclNamedExdName": aclNamedExdName,
       "aclNamedExdSubNum": aclNamedExdSubNum,
       "aclNamedExdSubitemAdminStatus": aclNamedExdSubitemAdminStatus,
       "aclNamedExdSubitemAction": aclNamedExdSubitemAction,
       "aclNamedExdSubitemProtocal": aclNamedExdSubitemProtocal,
       "aclNamedExdSubitemSrcAddr": aclNamedExdSubitemSrcAddr,
       "aclNamedExdSubitemSrcAddrWldmsk": aclNamedExdSubitemSrcAddrWldmsk,
       "aclNamedExdSubitemDstAddr": aclNamedExdSubitemDstAddr,
       "aclNamedExdSubitemDstAddrWldmsk": aclNamedExdSubitemDstAddrWldmsk,
       "aclNamedExdSubitemSrcPort": aclNamedExdSubitemSrcPort,
       "aclNamedExdSubitemSrcPortWldmsk": aclNamedExdSubitemSrcPortWldmsk,
       "aclNamedExdSubitemDstPort": aclNamedExdSubitemDstPort,
       "aclNamedExdSubitemDstPortWldmsk": aclNamedExdSubitemDstPortWldmsk,
       "aclNamedExdSubitemIcmpType": aclNamedExdSubitemIcmpType,
       "aclNamedExdSubitemIcmpCode": aclNamedExdSubitemIcmpCode,
       "aclNamedExdSubitemTcpEstablished": aclNamedExdSubitemTcpEstablished,
       "aclNamedExdSubitemPrecedence": aclNamedExdSubitemPrecedence,
       "aclNamedExdSubitemTos": aclNamedExdSubitemTos,
       "aclNamedExdSubitemDscp": aclNamedExdSubitemDscp,
       "aclNamedExdSubitemFragments": aclNamedExdSubitemFragments,
       "aclNamedExdSubitemTimeRange": aclNamedExdSubitemTimeRange,
       "aclNamedExdSubitemRowStatus": aclNamedExdSubitemRowStatus,
       "aclNamedLnkSubitemTable": aclNamedLnkSubitemTable,
       "aclNamedLnkSubitemEntry": aclNamedLnkSubitemEntry,
       "aclNamedLnkName": aclNamedLnkName,
       "aclNamedLnkSubNum": aclNamedLnkSubNum,
       "aclNamedLnkSubitemAdminStatus": aclNamedLnkSubitemAdminStatus,
       "aclNamedLnkSubitemAction": aclNamedLnkSubitemAction,
       "aclNamedLnkSubitemProtocal": aclNamedLnkSubitemProtocal,
       "aclNamedLnkSubitemCos": aclNamedLnkSubitemCos,
       "aclNamedLnkSubitemSrcVlanID": aclNamedLnkSubitemSrcVlanID,
       "aclNamedLnkSubitemSrcMacAddr": aclNamedLnkSubitemSrcMacAddr,
       "aclNamedLnkSubitemSrcMacWldmsk": aclNamedLnkSubitemSrcMacWldmsk,
       "aclNamedLnkSubitemDstMacAddr": aclNamedLnkSubitemDstMacAddr,
       "aclNamedLnkSubitemDstMacWldmsk": aclNamedLnkSubitemDstMacWldmsk,
       "aclNamedLnkSubitemSrcPortNum": aclNamedLnkSubitemSrcPortNum,
       "aclNamedLnkSubitemDstPortNum": aclNamedLnkSubitemDstPortNum,
       "aclNamedLnkSubitemTimeRange": aclNamedLnkSubitemTimeRange,
       "aclNamedLnkSubitemRowStatus": aclNamedLnkSubitemRowStatus,
       "aclNamedUserSubitemTable": aclNamedUserSubitemTable,
       "aclNamedUserSubitemEntry": aclNamedUserSubitemEntry,
       "aclNamedUserName": aclNamedUserName,
       "aclNamedUserSubNum": aclNamedUserSubNum,
       "aclNamedUserSubitemAdminStatus": aclNamedUserSubitemAdminStatus,
       "aclNamedUserSubitemAction": aclNamedUserSubitemAction,
       "aclNamedUserSubitemSrcPortNum": aclNamedUserSubitemSrcPortNum,
       "aclNamedUserSubitemDstPortNum": aclNamedUserSubitemDstPortNum,
       "aclNamedUserSubitemRule": aclNamedUserSubitemRule,
       "aclNamedUserSubitemMask": aclNamedUserSubitemMask,
       "aclNamedUserTimeRange": aclNamedUserTimeRange,
       "aclNamedUserSubitemRowStatus": aclNamedUserSubitemRowStatus,
       "aclTimeRangeTable": aclTimeRangeTable,
       "aclTimeRangeEntry": aclTimeRangeEntry,
       "aclTimeRangeName": aclTimeRangeName,
       "aclTimeRangeTotleAbsolutes": aclTimeRangeTotleAbsolutes,
       "aclTimeRangeTotlePeriods": aclTimeRangeTotlePeriods,
       "aclTimeRangeActive": aclTimeRangeActive,
       "aclTimeRangeRowStatus": aclTimeRangeRowStatus,
       "aclTimeRangeAbsoluteTable": aclTimeRangeAbsoluteTable,
       "aclTimeRangeAbsoluteEntry": aclTimeRangeAbsoluteEntry,
       "aclTimeRangeAbsoluteName": aclTimeRangeAbsoluteName,
       "aclTimeRangeAbsoluteStartTime": aclTimeRangeAbsoluteStartTime,
       "aclTimeRangeAbsoluteEndTime": aclTimeRangeAbsoluteEndTime,
       "aclTimeRangeAbsoluteRowStatus": aclTimeRangeAbsoluteRowStatus,
       "aclTimeRangePeriodTable": aclTimeRangePeriodTable,
       "aclTimeRangePeriodEntry": aclTimeRangePeriodEntry,
       "aclTimeRangePeriodName": aclTimeRangePeriodName,
       "aclTimeRangePeriodStartWeekDay": aclTimeRangePeriodStartWeekDay,
       "aclTimeRangePeriodStartHour": aclTimeRangePeriodStartHour,
       "aclTimeRangePeriodStartMin": aclTimeRangePeriodStartMin,
       "aclTimeRangePeriodEndWeekDay": aclTimeRangePeriodEndWeekDay,
       "aclTimeRangePeriodEndHour": aclTimeRangePeriodEndHour,
       "aclTimeRangePeriodEndMin": aclTimeRangePeriodEndMin,
       "aclTimeRangePeriodRowStatus": aclTimeRangePeriodRowStatus,
       "aclActiveTable": aclActiveTable,
       "aclActiveEntry": aclActiveEntry,
       "aclActiveIndex": aclActiveIndex,
       "aclActiveUserGroupName": aclActiveUserGroupName,
       "aclActiveUserGroupSubitem": aclActiveUserGroupSubitem,
       "aclActiveIpGroupName": aclActiveIpGroupName,
       "aclActiveIpGroupSubitem": aclActiveIpGroupSubitem,
       "aclActiveLinkGroupName": aclActiveLinkGroupName,
       "aclActiveLinkGroupSubitem": aclActiveLinkGroupSubitem,
       "aclActiveBlock0Priority": aclActiveBlock0Priority,
       "aclActiveBlock1Priority": aclActiveBlock1Priority,
       "aclActiveBlock2Priority": aclActiveBlock2Priority,
       "aclActiveBlock3Priority": aclActiveBlock3Priority,
       "aclActiveBlock4Priority": aclActiveBlock4Priority,
       "aclActiveConfigSequence": aclActiveConfigSequence,
       "aclActiveRunning": aclActiveRunning,
       "aclActiveRowStatus": aclActiveRowStatus,
       "aclActiveBlock5Priority": aclActiveBlock5Priority,
       "aclActiveBlock6Priority": aclActiveBlock6Priority,
       "aclActiveBlock7Priority": aclActiveBlock7Priority,
       "aclActiveBlock8Priority": aclActiveBlock8Priority,
       "aclActiveBlock9Priority": aclActiveBlock9Priority,
       "aclActiveBlock10Priority": aclActiveBlock10Priority,
       "aclActiveBlock11Priority": aclActiveBlock11Priority,
       "qosMirrorToTable": qosMirrorToTable,
       "qosMirrorToEntry": qosMirrorToEntry,
       "qosMirrorToIndex": qosMirrorToIndex,
       "qosMirrorToUserGroupName": qosMirrorToUserGroupName,
       "qosMirrorToUserGroupSubitem": qosMirrorToUserGroupSubitem,
       "qosMirrorToIpGroupName": qosMirrorToIpGroupName,
       "qosMirrorToIpGroupSubitem": qosMirrorToIpGroupSubitem,
       "qosMirrorToLinkGroupName": qosMirrorToLinkGroupName,
       "qosMirrorToLinkGroupSubitem": qosMirrorToLinkGroupSubitem,
       "qosMirrorToInterface": qosMirrorToInterface,
       "qosMirrorToBlock0Priority": qosMirrorToBlock0Priority,
       "qosMirrorToBlock1Priority": qosMirrorToBlock1Priority,
       "qosMirrorToBlock2Priority": qosMirrorToBlock2Priority,
       "qosMirrorToBlock3Priority": qosMirrorToBlock3Priority,
       "qosMirrorToBlock4Priority": qosMirrorToBlock4Priority,
       "qosMirrorToConfigSequence": qosMirrorToConfigSequence,
       "qosMirrorToRunning": qosMirrorToRunning,
       "qosMirrorToRowStatus": qosMirrorToRowStatus,
       "qosMirrorToBlock5Priority": qosMirrorToBlock5Priority,
       "qosMirrorToBlock6Priority": qosMirrorToBlock6Priority,
       "qosMirrorToBlock7Priority": qosMirrorToBlock7Priority,
       "qosMirrorToBlock8Priority": qosMirrorToBlock8Priority,
       "qosMirrorToBlock9Priority": qosMirrorToBlock9Priority,
       "qosMirrorToBlock10Priority": qosMirrorToBlock10Priority,
       "qosMirrorToBlock11Priority": qosMirrorToBlock11Priority,
       "qosRateLimitTable": qosRateLimitTable,
       "qosRateLimitEntry": qosRateLimitEntry,
       "qosRateLimitIndex": qosRateLimitIndex,
       "qosRateLimitUserGroupName": qosRateLimitUserGroupName,
       "qosRateLimitUserGroupSubitem": qosRateLimitUserGroupSubitem,
       "qosRateLimitIpGroupName": qosRateLimitIpGroupName,
       "qosRateLimitIpGroupSubitem": qosRateLimitIpGroupSubitem,
       "qosRateLimitLinkGroupName": qosRateLimitLinkGroupName,
       "qosRateLimitLinkGroupSubitem": qosRateLimitLinkGroupSubitem,
       "qosRateLimitIntf": qosRateLimitIntf,
       "qosRateLimitTargetRate": qosRateLimitTargetRate,
       "qosRateLimitExceedAction": qosRateLimitExceedAction,
       "qosRateLimitDscpValue": qosRateLimitDscpValue,
       "qosRateLimitBlock0Priority": qosRateLimitBlock0Priority,
       "qosRateLimitBlock1Priority": qosRateLimitBlock1Priority,
       "qosRateLimitBlock2Priority": qosRateLimitBlock2Priority,
       "qosRateLimitBlock3Priority": qosRateLimitBlock3Priority,
       "qosRateLimitBlock4Priority": qosRateLimitBlock4Priority,
       "qosRateLimitConfigSequence": qosRateLimitConfigSequence,
       "qosRateLimitRunning": qosRateLimitRunning,
       "qosRateLimitRowStatus": qosRateLimitRowStatus,
       "qosRateLimitBlock5Priority": qosRateLimitBlock5Priority,
       "qosRateLimitBlock6Priority": qosRateLimitBlock6Priority,
       "qosRateLimitBlock7Priority": qosRateLimitBlock7Priority,
       "qosRateLimitBlock8Priority": qosRateLimitBlock8Priority,
       "qosRateLimitBlock9Priority": qosRateLimitBlock9Priority,
       "qosRateLimitBlock10Priority": qosRateLimitBlock10Priority,
       "qosRateLimitBlock11Priority": qosRateLimitBlock11Priority,
       "qosTrafficPriorityTable": qosTrafficPriorityTable,
       "qosTrafficPriorityEntry": qosTrafficPriorityEntry,
       "qosTrafficPriorityIndex": qosTrafficPriorityIndex,
       "qosTrafficPriorityUserGroupName": qosTrafficPriorityUserGroupName,
       "qosTrafficPriorityUserGroupSubitem": qosTrafficPriorityUserGroupSubitem,
       "qosTrafficPriorityIpGroupName": qosTrafficPriorityIpGroupName,
       "qosTrafficPriorityIpGroupSubitem": qosTrafficPriorityIpGroupSubitem,
       "qosTrafficPriorityLinkGroupName": qosTrafficPriorityLinkGroupName,
       "qosTrafficPriorityLinkGroupSubitem": qosTrafficPriorityLinkGroupSubitem,
       "qosTrafficPriorityDscp": qosTrafficPriorityDscp,
       "qosTrafficPriorityIpPrecedence": qosTrafficPriorityIpPrecedence,
       "qosTrafficPriorityCos": qosTrafficPriorityCos,
       "qosTrafficPriorityLocalPrecedence": qosTrafficPriorityLocalPrecedence,
       "qosTrafficPriorityBlock0Priority": qosTrafficPriorityBlock0Priority,
       "qosTrafficPriorityBlock1Priority": qosTrafficPriorityBlock1Priority,
       "qosTrafficPriorityBlock2Priority": qosTrafficPriorityBlock2Priority,
       "qosTrafficPriorityBlock3Priority": qosTrafficPriorityBlock3Priority,
       "qosTrafficPriorityBlock4Priority": qosTrafficPriorityBlock4Priority,
       "qosTrafficPriorityConfigSequence": qosTrafficPriorityConfigSequence,
       "qosTrafficPriorityRunning": qosTrafficPriorityRunning,
       "qosTrafficPriorityRowStatus": qosTrafficPriorityRowStatus,
       "qosTrafficPriorityBlock5Priority": qosTrafficPriorityBlock5Priority,
       "qosTrafficPriorityBlock6Priority": qosTrafficPriorityBlock6Priority,
       "qosTrafficPriorityBlock7Priority": qosTrafficPriorityBlock7Priority,
       "qosTrafficPriorityBlock8Priority": qosTrafficPriorityBlock8Priority,
       "qosTrafficPriorityBlock9Priority": qosTrafficPriorityBlock9Priority,
       "qosTrafficPriorityBlock10Priority": qosTrafficPriorityBlock10Priority,
       "qosTrafficPriorityBlock11Priority": qosTrafficPriorityBlock11Priority,
       "qosTrafficRedirectTable": qosTrafficRedirectTable,
       "qosTrafficRedirectEntry": qosTrafficRedirectEntry,
       "qosTrafficRedirectIndex": qosTrafficRedirectIndex,
       "qosTrafficRedirectUserGroupName": qosTrafficRedirectUserGroupName,
       "qosTrafficRedirectUserGroupSubitem": qosTrafficRedirectUserGroupSubitem,
       "qosTrafficRedirectIpGroupName": qosTrafficRedirectIpGroupName,
       "qosTrafficRedirectIpGroupSubitem": qosTrafficRedirectIpGroupSubitem,
       "qosTrafficRedirectLinkGroupName": qosTrafficRedirectLinkGroupName,
       "qosTrafficRedirectLinkGroupSubitem": qosTrafficRedirectLinkGroupSubitem,
       "qosTrafficRedirectInterface": qosTrafficRedirectInterface,
       "qosTrafficRedirectBlock0Priority": qosTrafficRedirectBlock0Priority,
       "qosTrafficRedirectBlock1Priority": qosTrafficRedirectBlock1Priority,
       "qosTrafficRedirectBlock2Priority": qosTrafficRedirectBlock2Priority,
       "qosTrafficRedirectBlock3Priority": qosTrafficRedirectBlock3Priority,
       "qosTrafficRedirectBlock4Priority": qosTrafficRedirectBlock4Priority,
       "qosTrafficRedirectConfigSequence": qosTrafficRedirectConfigSequence,
       "qosTrafficRedirectRunning": qosTrafficRedirectRunning,
       "qosTrafficRedirectRowStatus": qosTrafficRedirectRowStatus,
       "qosTrafficRedirectBlock5Priority": qosTrafficRedirectBlock5Priority,
       "qosTrafficRedirectBlock6Priority": qosTrafficRedirectBlock6Priority,
       "qosTrafficRedirectBlock7Priority": qosTrafficRedirectBlock7Priority,
       "qosTrafficRedirectBlock8Priority": qosTrafficRedirectBlock8Priority,
       "qosTrafficRedirectBlock9Priority": qosTrafficRedirectBlock9Priority,
       "qosTrafficRedirectBlock10Priority": qosTrafficRedirectBlock10Priority,
       "qosTrafficRedirectBlock11Priority": qosTrafficRedirectBlock11Priority,
       "qosTrafficStatisticsTable": qosTrafficStatisticsTable,
       "qosTrafficStatisticsEntry": qosTrafficStatisticsEntry,
       "qosTrafficStatisticsIndex": qosTrafficStatisticsIndex,
       "qosTrafficStatisticsUserGroupName": qosTrafficStatisticsUserGroupName,
       "qosTrafficStatisticsUserGroupSubitem": qosTrafficStatisticsUserGroupSubitem,
       "qosTrafficStatisticsIpGroupName": qosTrafficStatisticsIpGroupName,
       "qosTrafficStatisticsIpGroupSubitem": qosTrafficStatisticsIpGroupSubitem,
       "qosTrafficStatisticsLinkGroupName": qosTrafficStatisticsLinkGroupName,
       "qosTrafficStatisticsLinkGroupSubitem": qosTrafficStatisticsLinkGroupSubitem,
       "qosTrafficStatisticsBlock0Priority": qosTrafficStatisticsBlock0Priority,
       "qosTrafficStatisticsBlock1Priority": qosTrafficStatisticsBlock1Priority,
       "qosTrafficStatisticsBlock2Priority": qosTrafficStatisticsBlock2Priority,
       "qosTrafficStatisticsBlock3Priority": qosTrafficStatisticsBlock3Priority,
       "qosTrafficStatisticsBlock4Priority": qosTrafficStatisticsBlock4Priority,
       "qosTrafficStatisticsConfigSequence": qosTrafficStatisticsConfigSequence,
       "qosTrafficStatisticsRunning": qosTrafficStatisticsRunning,
       "qosTrafficStatisticsRowStatus": qosTrafficStatisticsRowStatus,
       "qosTrafficStatisticsCounter": qosTrafficStatisticsCounter,
       "qosTrafficStatisticsBlock5Priority": qosTrafficStatisticsBlock5Priority,
       "qosTrafficStatisticsBlock6Priority": qosTrafficStatisticsBlock6Priority,
       "qosTrafficStatisticsBlock7Priority": qosTrafficStatisticsBlock7Priority,
       "qosTrafficStatisticsBlock8Priority": qosTrafficStatisticsBlock8Priority,
       "qosTrafficStatisticsBlock9Priority": qosTrafficStatisticsBlock9Priority,
       "qosTrafficStatisticsBlock10Priority": qosTrafficStatisticsBlock10Priority,
       "qosTrafficStatisticsBlock11Priority": qosTrafficStatisticsBlock11Priority,
       "qosLineRateTable": qosLineRateTable,
       "qosLineRateEntry": qosLineRateEntry,
       "qosLineRateInterface": qosLineRateInterface,
       "qosLineRateTargetRate": qosLineRateTargetRate,
       "qosTrafficCopyToCpuTable": qosTrafficCopyToCpuTable,
       "qosTrafficCopyToCpuEntry": qosTrafficCopyToCpuEntry,
       "qosTrafficCopyToCpuIndex": qosTrafficCopyToCpuIndex,
       "qosTrafficCopyToCpuUserGroupName": qosTrafficCopyToCpuUserGroupName,
       "qosTrafficCopyToCpuUserGroupSubitem": qosTrafficCopyToCpuUserGroupSubitem,
       "qosTrafficCopyToCpuIpGroupName": qosTrafficCopyToCpuIpGroupName,
       "qosTrafficCopyToCpuIpGroupSubitem": qosTrafficCopyToCpuIpGroupSubitem,
       "qosTrafficCopyToCpuLinkGroupName": qosTrafficCopyToCpuLinkGroupName,
       "qosTrafficCopyToCpuLinkGroupSubitem": qosTrafficCopyToCpuLinkGroupSubitem,
       "qosTrafficCopyToCpuBlock0Priority": qosTrafficCopyToCpuBlock0Priority,
       "qosTrafficCopyToCpuBlock1Priority": qosTrafficCopyToCpuBlock1Priority,
       "qosTrafficCopyToCpuBlock2Priority": qosTrafficCopyToCpuBlock2Priority,
       "qosTrafficCopyToCpuBlock3Priority": qosTrafficCopyToCpuBlock3Priority,
       "qosTrafficCopyToCpuBlock4Priority": qosTrafficCopyToCpuBlock4Priority,
       "qosTrafficCopyToCpuConfigSequence": qosTrafficCopyToCpuConfigSequence,
       "qosTrafficCopyToCpuRunning": qosTrafficCopyToCpuRunning,
       "qosTrafficCopyToCpuRowStatus": qosTrafficCopyToCpuRowStatus,
       "qosTrafficCopyToCpuBlock5Priority": qosTrafficCopyToCpuBlock5Priority,
       "qosTrafficCopyToCpuBlock6Priority": qosTrafficCopyToCpuBlock6Priority,
       "qosTrafficCopyToCpuBlock7Priority": qosTrafficCopyToCpuBlock7Priority,
       "qosTrafficCopyToCpuBlock8Priority": qosTrafficCopyToCpuBlock8Priority,
       "qosTrafficCopyToCpuBlock9Priority": qosTrafficCopyToCpuBlock9Priority,
       "qosTrafficCopyToCpuBlock10Priority": qosTrafficCopyToCpuBlock10Priority,
       "qosTrafficCopyToCpuBlock11Priority": qosTrafficCopyToCpuBlock11Priority,
       "qaclAppPortIsolationGroup": qaclAppPortIsolationGroup,
       "qaclAppPortIsolationDownLinkPorts": qaclAppPortIsolationDownLinkPorts,
       "stormControlTable": stormControlTable,
       "stormControlEntry": stormControlEntry,
       "stormControlInterface": stormControlInterface,
       "stormControlType": stormControlType,
       "stormControlTargetRate": stormControlTargetRate,
       "stormControlRowStatus": stormControlRowStatus,
       "qosTrafficRewriteVlanTable": qosTrafficRewriteVlanTable,
       "qosTrafficRewriteVlanEntry": qosTrafficRewriteVlanEntry,
       "qosTrafficRewriteVlanIndex": qosTrafficRewriteVlanIndex,
       "qosTrafficRewriteVlanUserGroupName": qosTrafficRewriteVlanUserGroupName,
       "qosTrafficRewriteVlanUserGroupSubitem": qosTrafficRewriteVlanUserGroupSubitem,
       "qosTrafficRewriteVlanIpGroupName": qosTrafficRewriteVlanIpGroupName,
       "qosTrafficRewriteVlanIpGroupSubitem": qosTrafficRewriteVlanIpGroupSubitem,
       "qosTrafficRewriteVlanLinkGroupName": qosTrafficRewriteVlanLinkGroupName,
       "qosTrafficRewriteVlanLinkGroupSubitem": qosTrafficRewriteVlanLinkGroupSubitem,
       "qosTrafficRewriteVlanVid": qosTrafficRewriteVlanVid,
       "qosTrafficRewriteVlanBlock0Priority": qosTrafficRewriteVlanBlock0Priority,
       "qosTrafficRewriteVlanBlock1Priority": qosTrafficRewriteVlanBlock1Priority,
       "qosTrafficRewriteVlanBlock2Priority": qosTrafficRewriteVlanBlock2Priority,
       "qosTrafficRewriteVlanBlock3Priority": qosTrafficRewriteVlanBlock3Priority,
       "qosTrafficRewriteVlanBlock4Priority": qosTrafficRewriteVlanBlock4Priority,
       "qosTrafficRewriteVlanConfigSequence": qosTrafficRewriteVlanConfigSequence,
       "qosTrafficRewriteVlanRunning": qosTrafficRewriteVlanRunning,
       "qosTrafficRewriteVlanRowStatus": qosTrafficRewriteVlanRowStatus,
       "qosTrafficRewriteVlanBlock5Priority": qosTrafficRewriteVlanBlock5Priority,
       "qosTrafficRewriteVlanBlock6Priority": qosTrafficRewriteVlanBlock6Priority,
       "qosTrafficRewriteVlanBlock7Priority": qosTrafficRewriteVlanBlock7Priority,
       "qosTrafficRewriteVlanBlock8Priority": qosTrafficRewriteVlanBlock8Priority,
       "qosTrafficRewriteVlanBlock9Priority": qosTrafficRewriteVlanBlock9Priority,
       "qosTrafficRewriteVlanBlock10Priority": qosTrafficRewriteVlanBlock10Priority,
       "qosTrafficRewriteVlanBlock11Priority": qosTrafficRewriteVlanBlock11Priority}
)
