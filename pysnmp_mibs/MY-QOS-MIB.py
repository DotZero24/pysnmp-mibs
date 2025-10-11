# SNMP MIB module (MY-QOS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-QOS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:34:50 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "IfIndex")

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

myQoSMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18)
)
if mibBuilder.loadTexts:
    myQoSMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyQoSPriorityMIBObjects_ObjectIdentity = ObjectIdentity
myQoSPriorityMIBObjects = _MyQoSPriorityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1)
)
_MyQoSGlobalStatus_Type = EnabledStatus
_MyQoSGlobalStatus_Object = MibScalar
myQoSGlobalStatus = _MyQoSGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 1),
    _MyQoSGlobalStatus_Type()
)
myQoSGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSGlobalStatus.setStatus("current")
_MyPriorityTrafficClassNum_Type = Integer32
_MyPriorityTrafficClassNum_Object = MibScalar
myPriorityTrafficClassNum = _MyPriorityTrafficClassNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 2),
    _MyPriorityTrafficClassNum_Type()
)
myPriorityTrafficClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPriorityTrafficClassNum.setStatus("current")
_MyPriorityClassNum_Type = Integer32
_MyPriorityClassNum_Object = MibScalar
myPriorityClassNum = _MyPriorityClassNum_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 3),
    _MyPriorityClassNum_Type()
)
myPriorityClassNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPriorityClassNum.setStatus("current")
_MyPriorityDscpMaxValue_Type = Integer32
_MyPriorityDscpMaxValue_Object = MibScalar
myPriorityDscpMaxValue = _MyPriorityDscpMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 4),
    _MyPriorityDscpMaxValue_Type()
)
myPriorityDscpMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myPriorityDscpMaxValue.setStatus("current")
_MyTrafficClassTable_Object = MibTable
myTrafficClassTable = _MyTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5)
)
if mibBuilder.loadTexts:
    myTrafficClassTable.setStatus("current")
_MyTrafficClassEntry_Object = MibTableRow
myTrafficClassEntry = _MyTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1)
)
myTrafficClassEntry.setIndexNames(
    (0, "MY-QOS-MIB", "myTrafficClassPriority"),
)
if mibBuilder.loadTexts:
    myTrafficClassEntry.setStatus("current")
_MyTrafficClassPriority_Type = Integer32
_MyTrafficClassPriority_Object = MibTableColumn
myTrafficClassPriority = _MyTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1, 1),
    _MyTrafficClassPriority_Type()
)
myTrafficClassPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myTrafficClassPriority.setStatus("current")
_MyTrafficClass_Type = Integer32
_MyTrafficClass_Object = MibTableColumn
myTrafficClass = _MyTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1, 2),
    _MyTrafficClass_Type()
)
myTrafficClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myTrafficClass.setStatus("current")
_MyPriorityToDscp_Type = Integer32
_MyPriorityToDscp_Object = MibTableColumn
myPriorityToDscp = _MyPriorityToDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 5, 1, 3),
    _MyPriorityToDscp_Type()
)
myPriorityToDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPriorityToDscp.setStatus("current")
_MyDscpClassTable_Object = MibTable
myDscpClassTable = _MyDscpClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6)
)
if mibBuilder.loadTexts:
    myDscpClassTable.setStatus("current")
_MyDscpClassEntry_Object = MibTableRow
myDscpClassEntry = _MyDscpClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6, 1)
)
myDscpClassEntry.setIndexNames(
    (0, "MY-QOS-MIB", "myDscpClass"),
)
if mibBuilder.loadTexts:
    myDscpClassEntry.setStatus("current")
_MyDscpClass_Type = Integer32
_MyDscpClass_Object = MibTableColumn
myDscpClass = _MyDscpClass_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6, 1, 1),
    _MyDscpClass_Type()
)
myDscpClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myDscpClass.setStatus("current")
_MyDscpTrafficClassPriority_Type = Integer32
_MyDscpTrafficClassPriority_Object = MibTableColumn
myDscpTrafficClassPriority = _MyDscpTrafficClassPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 6, 1, 2),
    _MyDscpTrafficClassPriority_Type()
)
myDscpTrafficClassPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDscpTrafficClassPriority.setStatus("current")


class _MyPriorityTrafficClassOperMode_Type(Integer32):
    """Custom type myPriorityTrafficClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qos-sp", 1),
          ("qos-wrr", 2))
    )


_MyPriorityTrafficClassOperMode_Type.__name__ = "Integer32"
_MyPriorityTrafficClassOperMode_Object = MibScalar
myPriorityTrafficClassOperMode = _MyPriorityTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 7),
    _MyPriorityTrafficClassOperMode_Type()
)
myPriorityTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPriorityTrafficClassOperMode.setStatus("current")
_MyPriorityBandWidth_Type = OctetString
_MyPriorityBandWidth_Object = MibScalar
myPriorityBandWidth = _MyPriorityBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 8),
    _MyPriorityBandWidth_Type()
)
myPriorityBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myPriorityBandWidth.setStatus("current")
_MyIfPriorityTable_Object = MibTable
myIfPriorityTable = _MyIfPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9)
)
if mibBuilder.loadTexts:
    myIfPriorityTable.setStatus("current")
_MyIfPriorityEntry_Object = MibTableRow
myIfPriorityEntry = _MyIfPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1)
)
myIfPriorityEntry.setIndexNames(
    (0, "MY-QOS-MIB", "myIfPriorityIfIndex"),
)
if mibBuilder.loadTexts:
    myIfPriorityEntry.setStatus("current")
_MyIfPriorityIfIndex_Type = IfIndex
_MyIfPriorityIfIndex_Object = MibTableColumn
myIfPriorityIfIndex = _MyIfPriorityIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 1),
    _MyIfPriorityIfIndex_Type()
)
myIfPriorityIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myIfPriorityIfIndex.setStatus("current")
_MyIfPriority_Type = Integer32
_MyIfPriority_Object = MibTableColumn
myIfPriority = _MyIfPriority_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 2),
    _MyIfPriority_Type()
)
myIfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfPriority.setStatus("current")


class _MyIfPriTrafficClassOperMode_Type(Integer32):
    """Custom type myIfPriTrafficClassOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("qos-sp", 1),
          ("qos-wrr", 2))
    )


_MyIfPriTrafficClassOperMode_Type.__name__ = "Integer32"
_MyIfPriTrafficClassOperMode_Object = MibTableColumn
myIfPriTrafficClassOperMode = _MyIfPriTrafficClassOperMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 3),
    _MyIfPriTrafficClassOperMode_Type()
)
myIfPriTrafficClassOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfPriTrafficClassOperMode.setStatus("current")
_MyIfPriorityBandwidth_Type = OctetString
_MyIfPriorityBandwidth_Object = MibTableColumn
myIfPriorityBandwidth = _MyIfPriorityBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 4),
    _MyIfPriorityBandwidth_Type()
)
myIfPriorityBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfPriorityBandwidth.setStatus("current")


class _MyIfPriorityQosTrustMode_Type(Integer32):
    """Custom type myIfPriorityQosTrustMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-trust", 1),
          ("trust-cos", 2),
          ("trust-dscp", 3))
    )


_MyIfPriorityQosTrustMode_Type.__name__ = "Integer32"
_MyIfPriorityQosTrustMode_Object = MibTableColumn
myIfPriorityQosTrustMode = _MyIfPriorityQosTrustMode_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 1, 9, 1, 5),
    _MyIfPriorityQosTrustMode_Type()
)
myIfPriorityQosTrustMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfPriorityQosTrustMode.setStatus("current")
_MyQoSTrafficClassMIBObjects_ObjectIdentity = ObjectIdentity
myQoSTrafficClassMIBObjects = _MyQoSTrafficClassMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2)
)
_MyQoSTrafficClassTable_Object = MibTable
myQoSTrafficClassTable = _MyQoSTrafficClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1)
)
if mibBuilder.loadTexts:
    myQoSTrafficClassTable.setStatus("current")
_MyQoSTrafficClassEntry_Object = MibTableRow
myQoSTrafficClassEntry = _MyQoSTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1)
)
myQoSTrafficClassEntry.setIndexNames(
    (0, "MY-QOS-MIB", "myQosClassMapName"),
)
if mibBuilder.loadTexts:
    myQoSTrafficClassEntry.setStatus("current")


class _MyQosClassMapName_Type(DisplayString):
    """Custom type myQosClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyQosClassMapName_Type.__name__ = "DisplayString"
_MyQosClassMapName_Object = MibTableColumn
myQosClassMapName = _MyQosClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1, 1),
    _MyQosClassMapName_Type()
)
myQosClassMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myQosClassMapName.setStatus("current")


class _MyQosClassAclName_Type(DisplayString):
    """Custom type myQosClassAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MyQosClassAclName_Type.__name__ = "DisplayString"
_MyQosClassAclName_Object = MibTableColumn
myQosClassAclName = _MyQosClassAclName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1, 2),
    _MyQosClassAclName_Type()
)
myQosClassAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQosClassAclName.setStatus("current")
_MyQosClassMapEntryStatus_Type = ConfigStatus
_MyQosClassMapEntryStatus_Object = MibTableColumn
myQosClassMapEntryStatus = _MyQosClassMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 1, 1, 3),
    _MyQosClassMapEntryStatus_Type()
)
myQosClassMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myQosClassMapEntryStatus.setStatus("current")
_MyQoSPoliceMapTable_Object = MibTable
myQoSPoliceMapTable = _MyQoSPoliceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2)
)
if mibBuilder.loadTexts:
    myQoSPoliceMapTable.setStatus("current")
_MyQoSPoliceMapEntry_Object = MibTableRow
myQoSPoliceMapEntry = _MyQoSPoliceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2, 1)
)
myQoSPoliceMapEntry.setIndexNames(
    (0, "MY-QOS-MIB", "myQosPoliceMapName"),
)
if mibBuilder.loadTexts:
    myQoSPoliceMapEntry.setStatus("current")


class _MyQosPoliceMapName_Type(DisplayString):
    """Custom type myQosPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyQosPoliceMapName_Type.__name__ = "DisplayString"
_MyQosPoliceMapName_Object = MibTableColumn
myQosPoliceMapName = _MyQosPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2, 1, 1),
    _MyQosPoliceMapName_Type()
)
myQosPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myQosPoliceMapName.setStatus("current")
_MyQosPoliceMapEntryStatus_Type = ConfigStatus
_MyQosPoliceMapEntryStatus_Object = MibTableColumn
myQosPoliceMapEntryStatus = _MyQosPoliceMapEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 2, 1, 2),
    _MyQosPoliceMapEntryStatus_Type()
)
myQosPoliceMapEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myQosPoliceMapEntryStatus.setStatus("current")
_MyQoSPoliceMapConfTable_Object = MibTable
myQoSPoliceMapConfTable = _MyQoSPoliceMapConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3)
)
if mibBuilder.loadTexts:
    myQoSPoliceMapConfTable.setStatus("current")
_MyQoSPoliceMapConfEntry_Object = MibTableRow
myQoSPoliceMapConfEntry = _MyQoSPoliceMapConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1)
)
myQoSPoliceMapConfEntry.setIndexNames(
    (0, "MY-QOS-MIB", "myQoSPoliceCfgPoliceMapName"),
    (0, "MY-QOS-MIB", "myQoSPoliceCfgClassMapName"),
)
if mibBuilder.loadTexts:
    myQoSPoliceMapConfEntry.setStatus("current")


class _MyQoSPoliceCfgPoliceMapName_Type(DisplayString):
    """Custom type myQoSPoliceCfgPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyQoSPoliceCfgPoliceMapName_Type.__name__ = "DisplayString"
_MyQoSPoliceCfgPoliceMapName_Object = MibTableColumn
myQoSPoliceCfgPoliceMapName = _MyQoSPoliceCfgPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 1),
    _MyQoSPoliceCfgPoliceMapName_Type()
)
myQoSPoliceCfgPoliceMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myQoSPoliceCfgPoliceMapName.setStatus("current")


class _MyQoSPoliceCfgClassMapName_Type(DisplayString):
    """Custom type myQoSPoliceCfgClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyQoSPoliceCfgClassMapName_Type.__name__ = "DisplayString"
_MyQoSPoliceCfgClassMapName_Object = MibTableColumn
myQoSPoliceCfgClassMapName = _MyQoSPoliceCfgClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 2),
    _MyQoSPoliceCfgClassMapName_Type()
)
myQoSPoliceCfgClassMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSPoliceCfgClassMapName.setStatus("current")
_MyQoSPoliceMapConfMaxBandWidth_Type = Unsigned32
_MyQoSPoliceMapConfMaxBandWidth_Object = MibTableColumn
myQoSPoliceMapConfMaxBandWidth = _MyQoSPoliceMapConfMaxBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 3),
    _MyQoSPoliceMapConfMaxBandWidth_Type()
)
myQoSPoliceMapConfMaxBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSPoliceMapConfMaxBandWidth.setStatus("current")
_MyQoSPoliceMapConfBurstFlowLimit_Type = Integer32
_MyQoSPoliceMapConfBurstFlowLimit_Object = MibTableColumn
myQoSPoliceMapConfBurstFlowLimit = _MyQoSPoliceMapConfBurstFlowLimit_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 4),
    _MyQoSPoliceMapConfBurstFlowLimit_Type()
)
myQoSPoliceMapConfBurstFlowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSPoliceMapConfBurstFlowLimit.setStatus("current")


class _MyQoSPoliceMapConfExceedAction_Type(Integer32):
    """Custom type myQoSPoliceMapConfExceedAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("discard", 1),
          ("modify-dscp", 2))
    )


_MyQoSPoliceMapConfExceedAction_Type.__name__ = "Integer32"
_MyQoSPoliceMapConfExceedAction_Object = MibTableColumn
myQoSPoliceMapConfExceedAction = _MyQoSPoliceMapConfExceedAction_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 5),
    _MyQoSPoliceMapConfExceedAction_Type()
)
myQoSPoliceMapConfExceedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSPoliceMapConfExceedAction.setStatus("current")
_MyQoSPoliceMapConfExceedDscp_Type = Integer32
_MyQoSPoliceMapConfExceedDscp_Object = MibTableColumn
myQoSPoliceMapConfExceedDscp = _MyQoSPoliceMapConfExceedDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 6),
    _MyQoSPoliceMapConfExceedDscp_Type()
)
myQoSPoliceMapConfExceedDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSPoliceMapConfExceedDscp.setStatus("current")
_MyQoSPoliceMapConfNewDscp_Type = Integer32
_MyQoSPoliceMapConfNewDscp_Object = MibTableColumn
myQoSPoliceMapConfNewDscp = _MyQoSPoliceMapConfNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 7),
    _MyQoSPoliceMapConfNewDscp_Type()
)
myQoSPoliceMapConfNewDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSPoliceMapConfNewDscp.setStatus("current")
_MyQoSPoliceMapCfgEntryStatus_Type = ConfigStatus
_MyQoSPoliceMapCfgEntryStatus_Object = MibTableColumn
myQoSPoliceMapCfgEntryStatus = _MyQoSPoliceMapCfgEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 8),
    _MyQoSPoliceMapCfgEntryStatus_Type()
)
myQoSPoliceMapCfgEntryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    myQoSPoliceMapCfgEntryStatus.setStatus("current")
_MyQoSPoliceMapConfMaxHighBandWidth_Type = Unsigned32
_MyQoSPoliceMapConfMaxHighBandWidth_Object = MibTableColumn
myQoSPoliceMapConfMaxHighBandWidth = _MyQoSPoliceMapConfMaxHighBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 3, 1, 9),
    _MyQoSPoliceMapConfMaxHighBandWidth_Type()
)
myQoSPoliceMapConfMaxHighBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myQoSPoliceMapConfMaxHighBandWidth.setStatus("current")
_MyQosPoliceIfTable_Object = MibTable
myQosPoliceIfTable = _MyQosPoliceIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 4)
)
if mibBuilder.loadTexts:
    myQosPoliceIfTable.setStatus("current")
_MyQosPoliceIfEntry_Object = MibTableRow
myQosPoliceIfEntry = _MyQosPoliceIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 4, 1)
)
myQosPoliceIfEntry.setIndexNames(
    (0, "MY-QOS-MIB", "myQosPoliceIfIndex"),
)
if mibBuilder.loadTexts:
    myQosPoliceIfEntry.setStatus("current")
_MyQosPoliceIfIndex_Type = IfIndex
_MyQosPoliceIfIndex_Object = MibTableColumn
myQosPoliceIfIndex = _MyQosPoliceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 4, 1, 1),
    _MyQosPoliceIfIndex_Type()
)
myQosPoliceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    myQosPoliceIfIndex.setStatus("current")


class _MyIfPoliceMapName_Type(DisplayString):
    """Custom type myIfPoliceMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MyIfPoliceMapName_Type.__name__ = "DisplayString"
_MyIfPoliceMapName_Object = MibTableColumn
myIfPoliceMapName = _MyIfPoliceMapName_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 2, 4, 1, 2),
    _MyIfPoliceMapName_Type()
)
myIfPoliceMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIfPoliceMapName.setStatus("current")
_MyQoSMIBConformance_ObjectIdentity = ObjectIdentity
myQoSMIBConformance = _MyQoSMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3)
)
_MyQoSMIBCompliances_ObjectIdentity = ObjectIdentity
myQoSMIBCompliances = _MyQoSMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 1)
)
_MyQoSMIBGroups_ObjectIdentity = ObjectIdentity
myQoSMIBGroups = _MyQoSMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 2)
)

# Managed Objects groups

myQoSPriorityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 2, 1)
)
myQoSPriorityMIBGroup.setObjects(
      *(("MY-QOS-MIB", "myQoSGlobalStatus"),
        ("MY-QOS-MIB", "myPriorityTrafficClassNum"),
        ("MY-QOS-MIB", "myPriorityClassNum"),
        ("MY-QOS-MIB", "myPriorityDscpMaxValue"),
        ("MY-QOS-MIB", "myTrafficClassPriority"),
        ("MY-QOS-MIB", "myTrafficClass"),
        ("MY-QOS-MIB", "myPriorityToDscp"),
        ("MY-QOS-MIB", "myDscpClass"),
        ("MY-QOS-MIB", "myDscpTrafficClassPriority"),
        ("MY-QOS-MIB", "myPriorityTrafficClassOperMode"),
        ("MY-QOS-MIB", "myPriorityBandWidth"),
        ("MY-QOS-MIB", "myIfPriorityIfIndex"),
        ("MY-QOS-MIB", "myIfPriority"),
        ("MY-QOS-MIB", "myIfPriTrafficClassOperMode"),
        ("MY-QOS-MIB", "myIfPriorityBandwidth"),
        ("MY-QOS-MIB", "myIfPriorityQosTrustMode"))
)
if mibBuilder.loadTexts:
    myQoSPriorityMIBGroup.setStatus("current")

myQoSTrafficClassMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 2, 2)
)
myQoSTrafficClassMIBGroup.setObjects(
      *(("MY-QOS-MIB", "myQosClassMapName"),
        ("MY-QOS-MIB", "myQosClassAclName"),
        ("MY-QOS-MIB", "myQosClassMapEntryStatus"),
        ("MY-QOS-MIB", "myQosPoliceMapName"),
        ("MY-QOS-MIB", "myQosPoliceMapEntryStatus"),
        ("MY-QOS-MIB", "myQoSPoliceCfgPoliceMapName"),
        ("MY-QOS-MIB", "myQoSPoliceCfgClassMapName"),
        ("MY-QOS-MIB", "myQoSPoliceMapConfMaxBandWidth"),
        ("MY-QOS-MIB", "myQoSPoliceMapConfExceedAction"),
        ("MY-QOS-MIB", "myQoSPoliceMapConfExceedDscp"),
        ("MY-QOS-MIB", "myQoSPoliceMapConfNewDscp"),
        ("MY-QOS-MIB", "myQoSPoliceMapCfgEntryStatus"),
        ("MY-QOS-MIB", "myQoSPoliceMapConfMaxHighBandWidth"),
        ("MY-QOS-MIB", "myQosPoliceIfIndex"),
        ("MY-QOS-MIB", "myIfPoliceMapName"))
)
if mibBuilder.loadTexts:
    myQoSTrafficClassMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myQoSMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 18, 3, 1, 1)
)
myQoSMIBCompliance.setObjects(
      *(("MY-QOS-MIB", "myQoSPriorityMIBGroup"),
        ("MY-QOS-MIB", "myQoSTrafficClassMIBGroup"))
)
if mibBuilder.loadTexts:
    myQoSMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-QOS-MIB",
    **{"myQoSMIB": myQoSMIB,
       "myQoSPriorityMIBObjects": myQoSPriorityMIBObjects,
       "myQoSGlobalStatus": myQoSGlobalStatus,
       "myPriorityTrafficClassNum": myPriorityTrafficClassNum,
       "myPriorityClassNum": myPriorityClassNum,
       "myPriorityDscpMaxValue": myPriorityDscpMaxValue,
       "myTrafficClassTable": myTrafficClassTable,
       "myTrafficClassEntry": myTrafficClassEntry,
       "myTrafficClassPriority": myTrafficClassPriority,
       "myTrafficClass": myTrafficClass,
       "myPriorityToDscp": myPriorityToDscp,
       "myDscpClassTable": myDscpClassTable,
       "myDscpClassEntry": myDscpClassEntry,
       "myDscpClass": myDscpClass,
       "myDscpTrafficClassPriority": myDscpTrafficClassPriority,
       "myPriorityTrafficClassOperMode": myPriorityTrafficClassOperMode,
       "myPriorityBandWidth": myPriorityBandWidth,
       "myIfPriorityTable": myIfPriorityTable,
       "myIfPriorityEntry": myIfPriorityEntry,
       "myIfPriorityIfIndex": myIfPriorityIfIndex,
       "myIfPriority": myIfPriority,
       "myIfPriTrafficClassOperMode": myIfPriTrafficClassOperMode,
       "myIfPriorityBandwidth": myIfPriorityBandwidth,
       "myIfPriorityQosTrustMode": myIfPriorityQosTrustMode,
       "myQoSTrafficClassMIBObjects": myQoSTrafficClassMIBObjects,
       "myQoSTrafficClassTable": myQoSTrafficClassTable,
       "myQoSTrafficClassEntry": myQoSTrafficClassEntry,
       "myQosClassMapName": myQosClassMapName,
       "myQosClassAclName": myQosClassAclName,
       "myQosClassMapEntryStatus": myQosClassMapEntryStatus,
       "myQoSPoliceMapTable": myQoSPoliceMapTable,
       "myQoSPoliceMapEntry": myQoSPoliceMapEntry,
       "myQosPoliceMapName": myQosPoliceMapName,
       "myQosPoliceMapEntryStatus": myQosPoliceMapEntryStatus,
       "myQoSPoliceMapConfTable": myQoSPoliceMapConfTable,
       "myQoSPoliceMapConfEntry": myQoSPoliceMapConfEntry,
       "myQoSPoliceCfgPoliceMapName": myQoSPoliceCfgPoliceMapName,
       "myQoSPoliceCfgClassMapName": myQoSPoliceCfgClassMapName,
       "myQoSPoliceMapConfMaxBandWidth": myQoSPoliceMapConfMaxBandWidth,
       "myQoSPoliceMapConfBurstFlowLimit": myQoSPoliceMapConfBurstFlowLimit,
       "myQoSPoliceMapConfExceedAction": myQoSPoliceMapConfExceedAction,
       "myQoSPoliceMapConfExceedDscp": myQoSPoliceMapConfExceedDscp,
       "myQoSPoliceMapConfNewDscp": myQoSPoliceMapConfNewDscp,
       "myQoSPoliceMapCfgEntryStatus": myQoSPoliceMapCfgEntryStatus,
       "myQoSPoliceMapConfMaxHighBandWidth": myQoSPoliceMapConfMaxHighBandWidth,
       "myQosPoliceIfTable": myQosPoliceIfTable,
       "myQosPoliceIfEntry": myQosPoliceIfEntry,
       "myQosPoliceIfIndex": myQosPoliceIfIndex,
       "myIfPoliceMapName": myIfPoliceMapName,
       "myQoSMIBConformance": myQoSMIBConformance,
       "myQoSMIBCompliances": myQoSMIBCompliances,
       "myQoSMIBCompliance": myQoSMIBCompliance,
       "myQoSMIBGroups": myQoSMIBGroups,
       "myQoSPriorityMIBGroup": myQoSPriorityMIBGroup,
       "myQoSTrafficClassMIBGroup": myQoSTrafficClassMIBGroup}
)
