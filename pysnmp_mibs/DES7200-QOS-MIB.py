_u='myQoSTrafficClassMIBGroup'
_t='myQoSPriorityMIBGroup'
_s='myIfOutPoliceMapName'
_r='myIfInPoliceMapName'
_q='myQoSPoliceMapConfMaxHighBandWidth'
_p='myQoSPoliceMapCfgEntryStatus'
_o='myQoSPoliceMapConfNewDscp'
_n='myQoSPoliceMapConfExceedDscp'
_m='myQoSPoliceMapConfExceedAction'
_l='myQoSPoliceMapConfMaxBandWidth'
_k='myQosPoliceMapEntryStatus'
_j='myQosClassMapEntryStatus'
_i='myQosClassAclName'
_h='myIpPreToDscp'
_g='myIfPriorityQosTrustMode'
_f='myIfPriorityBandwidth'
_e='myIfPriTrafficClassOperMode'
_d='myIfPriority'
_c='myPriorityBandWidth'
_b='myPriorityTrafficClassOperMode'
_a='myDscpTrafficClassPriority'
_Z='myPriorityToDscp'
_Y='myTrafficClass'
_X='myPriorityDscpMaxValue'
_W='myPriorityClassNum'
_V='myPriorityTrafficClassNum'
_U='myQoSGlobalStatus'
_T='myIfRateLimitIndex'
_S='qos-drr'
_R='qos-wrr'
_Q='qos-sp'
_P='myQosPoliceIfIndex'
_O='myQoSPoliceCfgClassMapName'
_N='myQoSPoliceCfgPoliceMapName'
_M='myQosPoliceMapName'
_L='read-create'
_K='myQosClassMapName'
_J='myIpPreClassPriority'
_I='myIfPriorityIfIndex'
_H='myDscpClass'
_G='myTrafficClassPriority'
_F='Integer32'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='DES7200-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('DES7200-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('DES7200-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myQoSMIB=ModuleIdentity((1,3,6,1,4,1,171,10,97,2,18))
if mibBuilder.loadTexts:myQoSMIB.setRevisions(('2002-03-20 00:00',))
_MyQoSPriorityMIBObjects_ObjectIdentity=ObjectIdentity
myQoSPriorityMIBObjects=_MyQoSPriorityMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,18,1))
_MyQoSGlobalStatus_Type=EnabledStatus
_MyQoSGlobalStatus_Object=MibScalar
myQoSGlobalStatus=_MyQoSGlobalStatus_Object((1,3,6,1,4,1,171,10,97,2,18,1,1),_MyQoSGlobalStatus_Type())
myQoSGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSGlobalStatus.setStatus(_A)
_MyPriorityTrafficClassNum_Type=Integer32
_MyPriorityTrafficClassNum_Object=MibScalar
myPriorityTrafficClassNum=_MyPriorityTrafficClassNum_Object((1,3,6,1,4,1,171,10,97,2,18,1,2),_MyPriorityTrafficClassNum_Type())
myPriorityTrafficClassNum.setMaxAccess(_D)
if mibBuilder.loadTexts:myPriorityTrafficClassNum.setStatus(_A)
_MyPriorityClassNum_Type=Integer32
_MyPriorityClassNum_Object=MibScalar
myPriorityClassNum=_MyPriorityClassNum_Object((1,3,6,1,4,1,171,10,97,2,18,1,3),_MyPriorityClassNum_Type())
myPriorityClassNum.setMaxAccess(_D)
if mibBuilder.loadTexts:myPriorityClassNum.setStatus(_A)
_MyPriorityDscpMaxValue_Type=Integer32
_MyPriorityDscpMaxValue_Object=MibScalar
myPriorityDscpMaxValue=_MyPriorityDscpMaxValue_Object((1,3,6,1,4,1,171,10,97,2,18,1,4),_MyPriorityDscpMaxValue_Type())
myPriorityDscpMaxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:myPriorityDscpMaxValue.setStatus(_A)
_MyTrafficClassTable_Object=MibTable
myTrafficClassTable=_MyTrafficClassTable_Object((1,3,6,1,4,1,171,10,97,2,18,1,5))
if mibBuilder.loadTexts:myTrafficClassTable.setStatus(_A)
_MyTrafficClassEntry_Object=MibTableRow
myTrafficClassEntry=_MyTrafficClassEntry_Object((1,3,6,1,4,1,171,10,97,2,18,1,5,1))
myTrafficClassEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:myTrafficClassEntry.setStatus(_A)
_MyTrafficClassPriority_Type=Integer32
_MyTrafficClassPriority_Object=MibTableColumn
myTrafficClassPriority=_MyTrafficClassPriority_Object((1,3,6,1,4,1,171,10,97,2,18,1,5,1,1),_MyTrafficClassPriority_Type())
myTrafficClassPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:myTrafficClassPriority.setStatus(_A)
_MyTrafficClass_Type=Integer32
_MyTrafficClass_Object=MibTableColumn
myTrafficClass=_MyTrafficClass_Object((1,3,6,1,4,1,171,10,97,2,18,1,5,1,2),_MyTrafficClass_Type())
myTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:myTrafficClass.setStatus(_A)
_MyPriorityToDscp_Type=Integer32
_MyPriorityToDscp_Object=MibTableColumn
myPriorityToDscp=_MyPriorityToDscp_Object((1,3,6,1,4,1,171,10,97,2,18,1,5,1,3),_MyPriorityToDscp_Type())
myPriorityToDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:myPriorityToDscp.setStatus(_A)
_MyDscpClassTable_Object=MibTable
myDscpClassTable=_MyDscpClassTable_Object((1,3,6,1,4,1,171,10,97,2,18,1,6))
if mibBuilder.loadTexts:myDscpClassTable.setStatus(_A)
_MyDscpClassEntry_Object=MibTableRow
myDscpClassEntry=_MyDscpClassEntry_Object((1,3,6,1,4,1,171,10,97,2,18,1,6,1))
myDscpClassEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:myDscpClassEntry.setStatus(_A)
_MyDscpClass_Type=Integer32
_MyDscpClass_Object=MibTableColumn
myDscpClass=_MyDscpClass_Object((1,3,6,1,4,1,171,10,97,2,18,1,6,1,1),_MyDscpClass_Type())
myDscpClass.setMaxAccess(_D)
if mibBuilder.loadTexts:myDscpClass.setStatus(_A)
_MyDscpTrafficClassPriority_Type=Integer32
_MyDscpTrafficClassPriority_Object=MibTableColumn
myDscpTrafficClassPriority=_MyDscpTrafficClassPriority_Object((1,3,6,1,4,1,171,10,97,2,18,1,6,1,2),_MyDscpTrafficClassPriority_Type())
myDscpTrafficClassPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:myDscpTrafficClassPriority.setStatus(_A)
class _MyPriorityTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_MyPriorityTrafficClassOperMode_Type.__name__=_F
_MyPriorityTrafficClassOperMode_Object=MibScalar
myPriorityTrafficClassOperMode=_MyPriorityTrafficClassOperMode_Object((1,3,6,1,4,1,171,10,97,2,18,1,7),_MyPriorityTrafficClassOperMode_Type())
myPriorityTrafficClassOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myPriorityTrafficClassOperMode.setStatus(_A)
_MyPriorityBandWidth_Type=OctetString
_MyPriorityBandWidth_Object=MibScalar
myPriorityBandWidth=_MyPriorityBandWidth_Object((1,3,6,1,4,1,171,10,97,2,18,1,8),_MyPriorityBandWidth_Type())
myPriorityBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myPriorityBandWidth.setStatus(_A)
_MyIfPriorityTable_Object=MibTable
myIfPriorityTable=_MyIfPriorityTable_Object((1,3,6,1,4,1,171,10,97,2,18,1,9))
if mibBuilder.loadTexts:myIfPriorityTable.setStatus(_A)
_MyIfPriorityEntry_Object=MibTableRow
myIfPriorityEntry=_MyIfPriorityEntry_Object((1,3,6,1,4,1,171,10,97,2,18,1,9,1))
myIfPriorityEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:myIfPriorityEntry.setStatus(_A)
_MyIfPriorityIfIndex_Type=IfIndex
_MyIfPriorityIfIndex_Object=MibTableColumn
myIfPriorityIfIndex=_MyIfPriorityIfIndex_Object((1,3,6,1,4,1,171,10,97,2,18,1,9,1,1),_MyIfPriorityIfIndex_Type())
myIfPriorityIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myIfPriorityIfIndex.setStatus(_A)
_MyIfPriority_Type=Integer32
_MyIfPriority_Object=MibTableColumn
myIfPriority=_MyIfPriority_Object((1,3,6,1,4,1,171,10,97,2,18,1,9,1,2),_MyIfPriority_Type())
myIfPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriority.setStatus(_A)
class _MyIfPriTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3)))
_MyIfPriTrafficClassOperMode_Type.__name__=_F
_MyIfPriTrafficClassOperMode_Object=MibTableColumn
myIfPriTrafficClassOperMode=_MyIfPriTrafficClassOperMode_Object((1,3,6,1,4,1,171,10,97,2,18,1,9,1,3),_MyIfPriTrafficClassOperMode_Type())
myIfPriTrafficClassOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriTrafficClassOperMode.setStatus(_A)
_MyIfPriorityBandwidth_Type=OctetString
_MyIfPriorityBandwidth_Object=MibTableColumn
myIfPriorityBandwidth=_MyIfPriorityBandwidth_Object((1,3,6,1,4,1,171,10,97,2,18,1,9,1,4),_MyIfPriorityBandwidth_Type())
myIfPriorityBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriorityBandwidth.setStatus(_A)
class _MyIfPriorityQosTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('not-trust',1),('trust-cos',2),('trust-dscp',3),('trust-ip-precedence',4)))
_MyIfPriorityQosTrustMode_Type.__name__=_F
_MyIfPriorityQosTrustMode_Object=MibTableColumn
myIfPriorityQosTrustMode=_MyIfPriorityQosTrustMode_Object((1,3,6,1,4,1,171,10,97,2,18,1,9,1,5),_MyIfPriorityQosTrustMode_Type())
myIfPriorityQosTrustMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriorityQosTrustMode.setStatus(_A)
_MyIpPreClassTable_Object=MibTable
myIpPreClassTable=_MyIpPreClassTable_Object((1,3,6,1,4,1,171,10,97,2,18,1,10))
if mibBuilder.loadTexts:myIpPreClassTable.setStatus(_A)
_MyIpPreClassEntry_Object=MibTableRow
myIpPreClassEntry=_MyIpPreClassEntry_Object((1,3,6,1,4,1,171,10,97,2,18,1,10,1))
myIpPreClassEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:myIpPreClassEntry.setStatus(_A)
_MyIpPreClassPriority_Type=Integer32
_MyIpPreClassPriority_Object=MibTableColumn
myIpPreClassPriority=_MyIpPreClassPriority_Object((1,3,6,1,4,1,171,10,97,2,18,1,10,1,1),_MyIpPreClassPriority_Type())
myIpPreClassPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:myIpPreClassPriority.setStatus(_A)
_MyIpPreToDscp_Type=Integer32
_MyIpPreToDscp_Object=MibTableColumn
myIpPreToDscp=_MyIpPreToDscp_Object((1,3,6,1,4,1,171,10,97,2,18,1,10,1,2),_MyIpPreToDscp_Type())
myIpPreToDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:myIpPreToDscp.setStatus(_A)
_MyIfRateLimitTable_Object=MibTable
myIfRateLimitTable=_MyIfRateLimitTable_Object((1,3,6,1,4,1,171,10,97,2,18,1,11))
if mibBuilder.loadTexts:myIfRateLimitTable.setStatus(_A)
_MyIfRateLimitEntry_Object=MibTableRow
myIfRateLimitEntry=_MyIfRateLimitEntry_Object((1,3,6,1,4,1,171,10,97,2,18,1,11,1))
myIfRateLimitEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:myIfRateLimitEntry.setStatus(_A)
_MyIfRateLimitIndex_Type=IfIndex
_MyIfRateLimitIndex_Object=MibTableColumn
myIfRateLimitIndex=_MyIfRateLimitIndex_Object((1,3,6,1,4,1,171,10,97,2,18,1,11,1,1),_MyIfRateLimitIndex_Type())
myIfRateLimitIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myIfRateLimitIndex.setStatus(_A)
_MyIfRateLimitInMaxBandWidth_Type=Unsigned32
_MyIfRateLimitInMaxBandWidth_Object=MibTableColumn
myIfRateLimitInMaxBandWidth=_MyIfRateLimitInMaxBandWidth_Object((1,3,6,1,4,1,171,10,97,2,18,1,11,1,2),_MyIfRateLimitInMaxBandWidth_Type())
myIfRateLimitInMaxBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfRateLimitInMaxBandWidth.setStatus(_A)
_MyIfRateLimitInBurstFlowLimit_Type=Integer32
_MyIfRateLimitInBurstFlowLimit_Object=MibTableColumn
myIfRateLimitInBurstFlowLimit=_MyIfRateLimitInBurstFlowLimit_Object((1,3,6,1,4,1,171,10,97,2,18,1,11,1,3),_MyIfRateLimitInBurstFlowLimit_Type())
myIfRateLimitInBurstFlowLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfRateLimitInBurstFlowLimit.setStatus(_A)
_MyIfRateLimitOutMaxBandWidth_Type=Unsigned32
_MyIfRateLimitOutMaxBandWidth_Object=MibTableColumn
myIfRateLimitOutMaxBandWidth=_MyIfRateLimitOutMaxBandWidth_Object((1,3,6,1,4,1,171,10,97,2,18,1,11,1,4),_MyIfRateLimitOutMaxBandWidth_Type())
myIfRateLimitOutMaxBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfRateLimitOutMaxBandWidth.setStatus(_A)
_MyIfRateLimitOutBurstFlowLimit_Type=Integer32
_MyIfRateLimitOutBurstFlowLimit_Object=MibTableColumn
myIfRateLimitOutBurstFlowLimit=_MyIfRateLimitOutBurstFlowLimit_Object((1,3,6,1,4,1,171,10,97,2,18,1,11,1,5),_MyIfRateLimitOutBurstFlowLimit_Type())
myIfRateLimitOutBurstFlowLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfRateLimitOutBurstFlowLimit.setStatus(_A)
_MyQoSTrafficClassMIBObjects_ObjectIdentity=ObjectIdentity
myQoSTrafficClassMIBObjects=_MyQoSTrafficClassMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,18,2))
_MyQoSTrafficClassTable_Object=MibTable
myQoSTrafficClassTable=_MyQoSTrafficClassTable_Object((1,3,6,1,4,1,171,10,97,2,18,2,1))
if mibBuilder.loadTexts:myQoSTrafficClassTable.setStatus(_A)
_MyQoSTrafficClassEntry_Object=MibTableRow
myQoSTrafficClassEntry=_MyQoSTrafficClassEntry_Object((1,3,6,1,4,1,171,10,97,2,18,2,1,1))
myQoSTrafficClassEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:myQoSTrafficClassEntry.setStatus(_A)
class _MyQosClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQosClassMapName_Type.__name__=_E
_MyQosClassMapName_Object=MibTableColumn
myQosClassMapName=_MyQosClassMapName_Object((1,3,6,1,4,1,171,10,97,2,18,2,1,1,1),_MyQosClassMapName_Type())
myQosClassMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:myQosClassMapName.setStatus(_A)
class _MyQosClassAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyQosClassAclName_Type.__name__=_E
_MyQosClassAclName_Object=MibTableColumn
myQosClassAclName=_MyQosClassAclName_Object((1,3,6,1,4,1,171,10,97,2,18,2,1,1,2),_MyQosClassAclName_Type())
myQosClassAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:myQosClassAclName.setStatus(_A)
_MyQosClassMapEntryStatus_Type=ConfigStatus
_MyQosClassMapEntryStatus_Object=MibTableColumn
myQosClassMapEntryStatus=_MyQosClassMapEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,18,2,1,1,3),_MyQosClassMapEntryStatus_Type())
myQosClassMapEntryStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:myQosClassMapEntryStatus.setStatus(_A)
_MyQoSPoliceMapTable_Object=MibTable
myQoSPoliceMapTable=_MyQoSPoliceMapTable_Object((1,3,6,1,4,1,171,10,97,2,18,2,2))
if mibBuilder.loadTexts:myQoSPoliceMapTable.setStatus(_A)
_MyQoSPoliceMapEntry_Object=MibTableRow
myQoSPoliceMapEntry=_MyQoSPoliceMapEntry_Object((1,3,6,1,4,1,171,10,97,2,18,2,2,1))
myQoSPoliceMapEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:myQoSPoliceMapEntry.setStatus(_A)
class _MyQosPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQosPoliceMapName_Type.__name__=_E
_MyQosPoliceMapName_Object=MibTableColumn
myQosPoliceMapName=_MyQosPoliceMapName_Object((1,3,6,1,4,1,171,10,97,2,18,2,2,1,1),_MyQosPoliceMapName_Type())
myQosPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:myQosPoliceMapName.setStatus(_A)
_MyQosPoliceMapEntryStatus_Type=ConfigStatus
_MyQosPoliceMapEntryStatus_Object=MibTableColumn
myQosPoliceMapEntryStatus=_MyQosPoliceMapEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,18,2,2,1,2),_MyQosPoliceMapEntryStatus_Type())
myQosPoliceMapEntryStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:myQosPoliceMapEntryStatus.setStatus(_A)
_MyQoSPoliceMapConfTable_Object=MibTable
myQoSPoliceMapConfTable=_MyQoSPoliceMapConfTable_Object((1,3,6,1,4,1,171,10,97,2,18,2,3))
if mibBuilder.loadTexts:myQoSPoliceMapConfTable.setStatus(_A)
_MyQoSPoliceMapConfEntry_Object=MibTableRow
myQoSPoliceMapConfEntry=_MyQoSPoliceMapConfEntry_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1))
myQoSPoliceMapConfEntry.setIndexNames((0,_B,_N),(0,_B,_O))
if mibBuilder.loadTexts:myQoSPoliceMapConfEntry.setStatus(_A)
class _MyQoSPoliceCfgPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQoSPoliceCfgPoliceMapName_Type.__name__=_E
_MyQoSPoliceCfgPoliceMapName_Object=MibTableColumn
myQoSPoliceCfgPoliceMapName=_MyQoSPoliceCfgPoliceMapName_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,1),_MyQoSPoliceCfgPoliceMapName_Type())
myQoSPoliceCfgPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:myQoSPoliceCfgPoliceMapName.setStatus(_A)
class _MyQoSPoliceCfgClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQoSPoliceCfgClassMapName_Type.__name__=_E
_MyQoSPoliceCfgClassMapName_Object=MibTableColumn
myQoSPoliceCfgClassMapName=_MyQoSPoliceCfgClassMapName_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,2),_MyQoSPoliceCfgClassMapName_Type())
myQoSPoliceCfgClassMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceCfgClassMapName.setStatus(_A)
_MyQoSPoliceMapConfMaxBandWidth_Type=Unsigned32
_MyQoSPoliceMapConfMaxBandWidth_Object=MibTableColumn
myQoSPoliceMapConfMaxBandWidth=_MyQoSPoliceMapConfMaxBandWidth_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,3),_MyQoSPoliceMapConfMaxBandWidth_Type())
myQoSPoliceMapConfMaxBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfMaxBandWidth.setStatus(_A)
_MyQoSPoliceMapConfBurstFlowLimit_Type=Integer32
_MyQoSPoliceMapConfBurstFlowLimit_Object=MibTableColumn
myQoSPoliceMapConfBurstFlowLimit=_MyQoSPoliceMapConfBurstFlowLimit_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,4),_MyQoSPoliceMapConfBurstFlowLimit_Type())
myQoSPoliceMapConfBurstFlowLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfBurstFlowLimit.setStatus(_A)
class _MyQoSPoliceMapConfExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard',1),('modify-dscp',2)))
_MyQoSPoliceMapConfExceedAction_Type.__name__=_F
_MyQoSPoliceMapConfExceedAction_Object=MibTableColumn
myQoSPoliceMapConfExceedAction=_MyQoSPoliceMapConfExceedAction_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,5),_MyQoSPoliceMapConfExceedAction_Type())
myQoSPoliceMapConfExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfExceedAction.setStatus(_A)
_MyQoSPoliceMapConfExceedDscp_Type=Integer32
_MyQoSPoliceMapConfExceedDscp_Object=MibTableColumn
myQoSPoliceMapConfExceedDscp=_MyQoSPoliceMapConfExceedDscp_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,6),_MyQoSPoliceMapConfExceedDscp_Type())
myQoSPoliceMapConfExceedDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfExceedDscp.setStatus(_A)
_MyQoSPoliceMapConfNewDscp_Type=Integer32
_MyQoSPoliceMapConfNewDscp_Object=MibTableColumn
myQoSPoliceMapConfNewDscp=_MyQoSPoliceMapConfNewDscp_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,7),_MyQoSPoliceMapConfNewDscp_Type())
myQoSPoliceMapConfNewDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfNewDscp.setStatus(_A)
_MyQoSPoliceMapCfgEntryStatus_Type=ConfigStatus
_MyQoSPoliceMapCfgEntryStatus_Object=MibTableColumn
myQoSPoliceMapCfgEntryStatus=_MyQoSPoliceMapCfgEntryStatus_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,8),_MyQoSPoliceMapCfgEntryStatus_Type())
myQoSPoliceMapCfgEntryStatus.setMaxAccess(_L)
if mibBuilder.loadTexts:myQoSPoliceMapCfgEntryStatus.setStatus(_A)
_MyQoSPoliceMapConfMaxHighBandWidth_Type=Unsigned32
_MyQoSPoliceMapConfMaxHighBandWidth_Object=MibTableColumn
myQoSPoliceMapConfMaxHighBandWidth=_MyQoSPoliceMapConfMaxHighBandWidth_Object((1,3,6,1,4,1,171,10,97,2,18,2,3,1,9),_MyQoSPoliceMapConfMaxHighBandWidth_Type())
myQoSPoliceMapConfMaxHighBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfMaxHighBandWidth.setStatus(_A)
_MyQosPoliceIfExtTable_Object=MibTable
myQosPoliceIfExtTable=_MyQosPoliceIfExtTable_Object((1,3,6,1,4,1,171,10,97,2,18,2,5))
if mibBuilder.loadTexts:myQosPoliceIfExtTable.setStatus(_A)
_MyQosPoliceIfExtEntry_Object=MibTableRow
myQosPoliceIfExtEntry=_MyQosPoliceIfExtEntry_Object((1,3,6,1,4,1,171,10,97,2,18,2,5,1))
myQosPoliceIfExtEntry.setIndexNames((0,_B,_P))
if mibBuilder.loadTexts:myQosPoliceIfExtEntry.setStatus(_A)
_MyQosPoliceIfIndex_Type=IfIndex
_MyQosPoliceIfIndex_Object=MibTableColumn
myQosPoliceIfIndex=_MyQosPoliceIfIndex_Object((1,3,6,1,4,1,171,10,97,2,18,2,5,1,1),_MyQosPoliceIfIndex_Type())
myQosPoliceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myQosPoliceIfIndex.setStatus(_A)
class _MyIfInPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyIfInPoliceMapName_Type.__name__=_E
_MyIfInPoliceMapName_Object=MibTableColumn
myIfInPoliceMapName=_MyIfInPoliceMapName_Object((1,3,6,1,4,1,171,10,97,2,18,2,5,1,2),_MyIfInPoliceMapName_Type())
myIfInPoliceMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfInPoliceMapName.setStatus(_A)
class _MyIfOutPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyIfOutPoliceMapName_Type.__name__=_E
_MyIfOutPoliceMapName_Object=MibTableColumn
myIfOutPoliceMapName=_MyIfOutPoliceMapName_Object((1,3,6,1,4,1,171,10,97,2,18,2,5,1,3),_MyIfOutPoliceMapName_Type())
myIfOutPoliceMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfOutPoliceMapName.setStatus(_A)
_MyQoSMIBConformance_ObjectIdentity=ObjectIdentity
myQoSMIBConformance=_MyQoSMIBConformance_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,18,3))
_MyQoSMIBCompliances_ObjectIdentity=ObjectIdentity
myQoSMIBCompliances=_MyQoSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,18,3,1))
_MyQoSMIBGroups_ObjectIdentity=ObjectIdentity
myQoSMIBGroups=_MyQoSMIBGroups_ObjectIdentity((1,3,6,1,4,1,171,10,97,2,18,3,2))
myQoSPriorityMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,18,3,2,1))
myQoSPriorityMIBGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_G),(_B,_Y),(_B,_Z),(_B,_H),(_B,_a),(_B,_b),(_B,_c),(_B,_I),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_J),(_B,_h)))
if mibBuilder.loadTexts:myQoSPriorityMIBGroup.setStatus(_A)
myQoSTrafficClassMIBGroup=ObjectGroup((1,3,6,1,4,1,171,10,97,2,18,3,2,2))
myQoSTrafficClassMIBGroup.setObjects(*((_B,_K),(_B,_i),(_B,_j),(_B,_M),(_B,_k),(_B,_N),(_B,_O),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_P),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:myQoSTrafficClassMIBGroup.setStatus(_A)
myQoSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,171,10,97,2,18,3,1,1))
myQoSMIBCompliance.setObjects(*((_B,_t),(_B,_u)))
if mibBuilder.loadTexts:myQoSMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myQoSMIB':myQoSMIB,'myQoSPriorityMIBObjects':myQoSPriorityMIBObjects,_U:myQoSGlobalStatus,_V:myPriorityTrafficClassNum,_W:myPriorityClassNum,_X:myPriorityDscpMaxValue,'myTrafficClassTable':myTrafficClassTable,'myTrafficClassEntry':myTrafficClassEntry,_G:myTrafficClassPriority,_Y:myTrafficClass,_Z:myPriorityToDscp,'myDscpClassTable':myDscpClassTable,'myDscpClassEntry':myDscpClassEntry,_H:myDscpClass,_a:myDscpTrafficClassPriority,_b:myPriorityTrafficClassOperMode,_c:myPriorityBandWidth,'myIfPriorityTable':myIfPriorityTable,'myIfPriorityEntry':myIfPriorityEntry,_I:myIfPriorityIfIndex,_d:myIfPriority,_e:myIfPriTrafficClassOperMode,_f:myIfPriorityBandwidth,_g:myIfPriorityQosTrustMode,'myIpPreClassTable':myIpPreClassTable,'myIpPreClassEntry':myIpPreClassEntry,_J:myIpPreClassPriority,_h:myIpPreToDscp,'myIfRateLimitTable':myIfRateLimitTable,'myIfRateLimitEntry':myIfRateLimitEntry,_T:myIfRateLimitIndex,'myIfRateLimitInMaxBandWidth':myIfRateLimitInMaxBandWidth,'myIfRateLimitInBurstFlowLimit':myIfRateLimitInBurstFlowLimit,'myIfRateLimitOutMaxBandWidth':myIfRateLimitOutMaxBandWidth,'myIfRateLimitOutBurstFlowLimit':myIfRateLimitOutBurstFlowLimit,'myQoSTrafficClassMIBObjects':myQoSTrafficClassMIBObjects,'myQoSTrafficClassTable':myQoSTrafficClassTable,'myQoSTrafficClassEntry':myQoSTrafficClassEntry,_K:myQosClassMapName,_i:myQosClassAclName,_j:myQosClassMapEntryStatus,'myQoSPoliceMapTable':myQoSPoliceMapTable,'myQoSPoliceMapEntry':myQoSPoliceMapEntry,_M:myQosPoliceMapName,_k:myQosPoliceMapEntryStatus,'myQoSPoliceMapConfTable':myQoSPoliceMapConfTable,'myQoSPoliceMapConfEntry':myQoSPoliceMapConfEntry,_N:myQoSPoliceCfgPoliceMapName,_O:myQoSPoliceCfgClassMapName,_l:myQoSPoliceMapConfMaxBandWidth,'myQoSPoliceMapConfBurstFlowLimit':myQoSPoliceMapConfBurstFlowLimit,_m:myQoSPoliceMapConfExceedAction,_n:myQoSPoliceMapConfExceedDscp,_o:myQoSPoliceMapConfNewDscp,_p:myQoSPoliceMapCfgEntryStatus,_q:myQoSPoliceMapConfMaxHighBandWidth,'myQosPoliceIfExtTable':myQosPoliceIfExtTable,'myQosPoliceIfExtEntry':myQosPoliceIfExtEntry,_P:myQosPoliceIfIndex,_r:myIfInPoliceMapName,_s:myIfOutPoliceMapName,'myQoSMIBConformance':myQoSMIBConformance,'myQoSMIBCompliances':myQoSMIBCompliances,'myQoSMIBCompliance':myQoSMIBCompliance,'myQoSMIBGroups':myQoSMIBGroups,_t:myQoSPriorityMIBGroup,_u:myQoSTrafficClassMIBGroup})