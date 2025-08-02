_p='myQoSTrafficClassMIBGroup'
_o='myQoSPriorityMIBGroup'
_n='myIfPoliceMapName'
_m='myQoSPoliceMapConfMaxHighBandWidth'
_l='myQoSPoliceMapCfgEntryStatus'
_k='myQoSPoliceMapConfNewDscp'
_j='myQoSPoliceMapConfExceedDscp'
_i='myQoSPoliceMapConfExceedAction'
_h='myQoSPoliceMapConfMaxBandWidth'
_g='myQosPoliceMapEntryStatus'
_f='myQosClassMapEntryStatus'
_e='myQosClassAclName'
_d='myIfPriorityQosTrustMode'
_c='myIfPriorityBandwidth'
_b='myIfPriTrafficClassOperMode'
_a='myIfPriority'
_Z='myPriorityBandWidth'
_Y='myPriorityTrafficClassOperMode'
_X='myDscpTrafficClassPriority'
_W='myPriorityToDscp'
_V='myTrafficClass'
_U='myPriorityDscpMaxValue'
_T='myPriorityClassNum'
_S='myPriorityTrafficClassNum'
_R='myQoSGlobalStatus'
_Q='qos-wrr'
_P='qos-sp'
_O='myQosPoliceIfIndex'
_N='myQoSPoliceCfgClassMapName'
_M='myQoSPoliceCfgPoliceMapName'
_L='myQosPoliceMapName'
_K='read-create'
_J='myQosClassMapName'
_I='myIfPriorityIfIndex'
_H='myDscpClass'
_G='myTrafficClassPriority'
_F='Integer32'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='MY-QOS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
myMgmt,=mibBuilder.importSymbols('MY-SMI','myMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('MY-TC','ConfigStatus','IfIndex')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
myQoSMIB=ModuleIdentity((1,3,6,1,4,1,4881,1,1,10,2,18))
if mibBuilder.loadTexts:myQoSMIB.setRevisions(('2002-03-20 00:00',))
_MyQoSPriorityMIBObjects_ObjectIdentity=ObjectIdentity
myQoSPriorityMIBObjects=_MyQoSPriorityMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,18,1))
_MyQoSGlobalStatus_Type=EnabledStatus
_MyQoSGlobalStatus_Object=MibScalar
myQoSGlobalStatus=_MyQoSGlobalStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,1),_MyQoSGlobalStatus_Type())
myQoSGlobalStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSGlobalStatus.setStatus(_A)
_MyPriorityTrafficClassNum_Type=Integer32
_MyPriorityTrafficClassNum_Object=MibScalar
myPriorityTrafficClassNum=_MyPriorityTrafficClassNum_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,2),_MyPriorityTrafficClassNum_Type())
myPriorityTrafficClassNum.setMaxAccess(_D)
if mibBuilder.loadTexts:myPriorityTrafficClassNum.setStatus(_A)
_MyPriorityClassNum_Type=Integer32
_MyPriorityClassNum_Object=MibScalar
myPriorityClassNum=_MyPriorityClassNum_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,3),_MyPriorityClassNum_Type())
myPriorityClassNum.setMaxAccess(_D)
if mibBuilder.loadTexts:myPriorityClassNum.setStatus(_A)
_MyPriorityDscpMaxValue_Type=Integer32
_MyPriorityDscpMaxValue_Object=MibScalar
myPriorityDscpMaxValue=_MyPriorityDscpMaxValue_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,4),_MyPriorityDscpMaxValue_Type())
myPriorityDscpMaxValue.setMaxAccess(_D)
if mibBuilder.loadTexts:myPriorityDscpMaxValue.setStatus(_A)
_MyTrafficClassTable_Object=MibTable
myTrafficClassTable=_MyTrafficClassTable_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,5))
if mibBuilder.loadTexts:myTrafficClassTable.setStatus(_A)
_MyTrafficClassEntry_Object=MibTableRow
myTrafficClassEntry=_MyTrafficClassEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,5,1))
myTrafficClassEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:myTrafficClassEntry.setStatus(_A)
_MyTrafficClassPriority_Type=Integer32
_MyTrafficClassPriority_Object=MibTableColumn
myTrafficClassPriority=_MyTrafficClassPriority_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,5,1,1),_MyTrafficClassPriority_Type())
myTrafficClassPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:myTrafficClassPriority.setStatus(_A)
_MyTrafficClass_Type=Integer32
_MyTrafficClass_Object=MibTableColumn
myTrafficClass=_MyTrafficClass_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,5,1,2),_MyTrafficClass_Type())
myTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:myTrafficClass.setStatus(_A)
_MyPriorityToDscp_Type=Integer32
_MyPriorityToDscp_Object=MibTableColumn
myPriorityToDscp=_MyPriorityToDscp_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,5,1,3),_MyPriorityToDscp_Type())
myPriorityToDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:myPriorityToDscp.setStatus(_A)
_MyDscpClassTable_Object=MibTable
myDscpClassTable=_MyDscpClassTable_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,6))
if mibBuilder.loadTexts:myDscpClassTable.setStatus(_A)
_MyDscpClassEntry_Object=MibTableRow
myDscpClassEntry=_MyDscpClassEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,6,1))
myDscpClassEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:myDscpClassEntry.setStatus(_A)
_MyDscpClass_Type=Integer32
_MyDscpClass_Object=MibTableColumn
myDscpClass=_MyDscpClass_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,6,1,1),_MyDscpClass_Type())
myDscpClass.setMaxAccess(_D)
if mibBuilder.loadTexts:myDscpClass.setStatus(_A)
_MyDscpTrafficClassPriority_Type=Integer32
_MyDscpTrafficClassPriority_Object=MibTableColumn
myDscpTrafficClassPriority=_MyDscpTrafficClassPriority_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,6,1,2),_MyDscpTrafficClassPriority_Type())
myDscpTrafficClassPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:myDscpTrafficClassPriority.setStatus(_A)
class _MyPriorityTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_MyPriorityTrafficClassOperMode_Type.__name__=_F
_MyPriorityTrafficClassOperMode_Object=MibScalar
myPriorityTrafficClassOperMode=_MyPriorityTrafficClassOperMode_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,7),_MyPriorityTrafficClassOperMode_Type())
myPriorityTrafficClassOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myPriorityTrafficClassOperMode.setStatus(_A)
_MyPriorityBandWidth_Type=OctetString
_MyPriorityBandWidth_Object=MibScalar
myPriorityBandWidth=_MyPriorityBandWidth_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,8),_MyPriorityBandWidth_Type())
myPriorityBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myPriorityBandWidth.setStatus(_A)
_MyIfPriorityTable_Object=MibTable
myIfPriorityTable=_MyIfPriorityTable_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,9))
if mibBuilder.loadTexts:myIfPriorityTable.setStatus(_A)
_MyIfPriorityEntry_Object=MibTableRow
myIfPriorityEntry=_MyIfPriorityEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,9,1))
myIfPriorityEntry.setIndexNames((0,_B,_I))
if mibBuilder.loadTexts:myIfPriorityEntry.setStatus(_A)
_MyIfPriorityIfIndex_Type=IfIndex
_MyIfPriorityIfIndex_Object=MibTableColumn
myIfPriorityIfIndex=_MyIfPriorityIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,9,1,1),_MyIfPriorityIfIndex_Type())
myIfPriorityIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myIfPriorityIfIndex.setStatus(_A)
_MyIfPriority_Type=Integer32
_MyIfPriority_Object=MibTableColumn
myIfPriority=_MyIfPriority_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,9,1,2),_MyIfPriority_Type())
myIfPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriority.setStatus(_A)
class _MyIfPriTrafficClassOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_P,1),(_Q,2)))
_MyIfPriTrafficClassOperMode_Type.__name__=_F
_MyIfPriTrafficClassOperMode_Object=MibTableColumn
myIfPriTrafficClassOperMode=_MyIfPriTrafficClassOperMode_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,9,1,3),_MyIfPriTrafficClassOperMode_Type())
myIfPriTrafficClassOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriTrafficClassOperMode.setStatus(_A)
_MyIfPriorityBandwidth_Type=OctetString
_MyIfPriorityBandwidth_Object=MibTableColumn
myIfPriorityBandwidth=_MyIfPriorityBandwidth_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,9,1,4),_MyIfPriorityBandwidth_Type())
myIfPriorityBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriorityBandwidth.setStatus(_A)
class _MyIfPriorityQosTrustMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('not-trust',1),('trust-cos',2),('trust-dscp',3)))
_MyIfPriorityQosTrustMode_Type.__name__=_F
_MyIfPriorityQosTrustMode_Object=MibTableColumn
myIfPriorityQosTrustMode=_MyIfPriorityQosTrustMode_Object((1,3,6,1,4,1,4881,1,1,10,2,18,1,9,1,5),_MyIfPriorityQosTrustMode_Type())
myIfPriorityQosTrustMode.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPriorityQosTrustMode.setStatus(_A)
_MyQoSTrafficClassMIBObjects_ObjectIdentity=ObjectIdentity
myQoSTrafficClassMIBObjects=_MyQoSTrafficClassMIBObjects_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,18,2))
_MyQoSTrafficClassTable_Object=MibTable
myQoSTrafficClassTable=_MyQoSTrafficClassTable_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,1))
if mibBuilder.loadTexts:myQoSTrafficClassTable.setStatus(_A)
_MyQoSTrafficClassEntry_Object=MibTableRow
myQoSTrafficClassEntry=_MyQoSTrafficClassEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,1,1))
myQoSTrafficClassEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:myQoSTrafficClassEntry.setStatus(_A)
class _MyQosClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQosClassMapName_Type.__name__=_E
_MyQosClassMapName_Object=MibTableColumn
myQosClassMapName=_MyQosClassMapName_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,1,1,1),_MyQosClassMapName_Type())
myQosClassMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:myQosClassMapName.setStatus(_A)
class _MyQosClassAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MyQosClassAclName_Type.__name__=_E
_MyQosClassAclName_Object=MibTableColumn
myQosClassAclName=_MyQosClassAclName_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,1,1,2),_MyQosClassAclName_Type())
myQosClassAclName.setMaxAccess(_C)
if mibBuilder.loadTexts:myQosClassAclName.setStatus(_A)
_MyQosClassMapEntryStatus_Type=ConfigStatus
_MyQosClassMapEntryStatus_Object=MibTableColumn
myQosClassMapEntryStatus=_MyQosClassMapEntryStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,1,1,3),_MyQosClassMapEntryStatus_Type())
myQosClassMapEntryStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:myQosClassMapEntryStatus.setStatus(_A)
_MyQoSPoliceMapTable_Object=MibTable
myQoSPoliceMapTable=_MyQoSPoliceMapTable_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,2))
if mibBuilder.loadTexts:myQoSPoliceMapTable.setStatus(_A)
_MyQoSPoliceMapEntry_Object=MibTableRow
myQoSPoliceMapEntry=_MyQoSPoliceMapEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,2,1))
myQoSPoliceMapEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:myQoSPoliceMapEntry.setStatus(_A)
class _MyQosPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQosPoliceMapName_Type.__name__=_E
_MyQosPoliceMapName_Object=MibTableColumn
myQosPoliceMapName=_MyQosPoliceMapName_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,2,1,1),_MyQosPoliceMapName_Type())
myQosPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:myQosPoliceMapName.setStatus(_A)
_MyQosPoliceMapEntryStatus_Type=ConfigStatus
_MyQosPoliceMapEntryStatus_Object=MibTableColumn
myQosPoliceMapEntryStatus=_MyQosPoliceMapEntryStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,2,1,2),_MyQosPoliceMapEntryStatus_Type())
myQosPoliceMapEntryStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:myQosPoliceMapEntryStatus.setStatus(_A)
_MyQoSPoliceMapConfTable_Object=MibTable
myQoSPoliceMapConfTable=_MyQoSPoliceMapConfTable_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3))
if mibBuilder.loadTexts:myQoSPoliceMapConfTable.setStatus(_A)
_MyQoSPoliceMapConfEntry_Object=MibTableRow
myQoSPoliceMapConfEntry=_MyQoSPoliceMapConfEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1))
myQoSPoliceMapConfEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:myQoSPoliceMapConfEntry.setStatus(_A)
class _MyQoSPoliceCfgPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQoSPoliceCfgPoliceMapName_Type.__name__=_E
_MyQoSPoliceCfgPoliceMapName_Object=MibTableColumn
myQoSPoliceCfgPoliceMapName=_MyQoSPoliceCfgPoliceMapName_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,1),_MyQoSPoliceCfgPoliceMapName_Type())
myQoSPoliceCfgPoliceMapName.setMaxAccess(_D)
if mibBuilder.loadTexts:myQoSPoliceCfgPoliceMapName.setStatus(_A)
class _MyQoSPoliceCfgClassMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyQoSPoliceCfgClassMapName_Type.__name__=_E
_MyQoSPoliceCfgClassMapName_Object=MibTableColumn
myQoSPoliceCfgClassMapName=_MyQoSPoliceCfgClassMapName_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,2),_MyQoSPoliceCfgClassMapName_Type())
myQoSPoliceCfgClassMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceCfgClassMapName.setStatus(_A)
_MyQoSPoliceMapConfMaxBandWidth_Type=Unsigned32
_MyQoSPoliceMapConfMaxBandWidth_Object=MibTableColumn
myQoSPoliceMapConfMaxBandWidth=_MyQoSPoliceMapConfMaxBandWidth_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,3),_MyQoSPoliceMapConfMaxBandWidth_Type())
myQoSPoliceMapConfMaxBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfMaxBandWidth.setStatus(_A)
_MyQoSPoliceMapConfBurstFlowLimit_Type=Integer32
_MyQoSPoliceMapConfBurstFlowLimit_Object=MibTableColumn
myQoSPoliceMapConfBurstFlowLimit=_MyQoSPoliceMapConfBurstFlowLimit_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,4),_MyQoSPoliceMapConfBurstFlowLimit_Type())
myQoSPoliceMapConfBurstFlowLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfBurstFlowLimit.setStatus(_A)
class _MyQoSPoliceMapConfExceedAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('discard',1),('modify-dscp',2)))
_MyQoSPoliceMapConfExceedAction_Type.__name__=_F
_MyQoSPoliceMapConfExceedAction_Object=MibTableColumn
myQoSPoliceMapConfExceedAction=_MyQoSPoliceMapConfExceedAction_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,5),_MyQoSPoliceMapConfExceedAction_Type())
myQoSPoliceMapConfExceedAction.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfExceedAction.setStatus(_A)
_MyQoSPoliceMapConfExceedDscp_Type=Integer32
_MyQoSPoliceMapConfExceedDscp_Object=MibTableColumn
myQoSPoliceMapConfExceedDscp=_MyQoSPoliceMapConfExceedDscp_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,6),_MyQoSPoliceMapConfExceedDscp_Type())
myQoSPoliceMapConfExceedDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfExceedDscp.setStatus(_A)
_MyQoSPoliceMapConfNewDscp_Type=Integer32
_MyQoSPoliceMapConfNewDscp_Object=MibTableColumn
myQoSPoliceMapConfNewDscp=_MyQoSPoliceMapConfNewDscp_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,7),_MyQoSPoliceMapConfNewDscp_Type())
myQoSPoliceMapConfNewDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfNewDscp.setStatus(_A)
_MyQoSPoliceMapCfgEntryStatus_Type=ConfigStatus
_MyQoSPoliceMapCfgEntryStatus_Object=MibTableColumn
myQoSPoliceMapCfgEntryStatus=_MyQoSPoliceMapCfgEntryStatus_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,8),_MyQoSPoliceMapCfgEntryStatus_Type())
myQoSPoliceMapCfgEntryStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:myQoSPoliceMapCfgEntryStatus.setStatus(_A)
_MyQoSPoliceMapConfMaxHighBandWidth_Type=Unsigned32
_MyQoSPoliceMapConfMaxHighBandWidth_Object=MibTableColumn
myQoSPoliceMapConfMaxHighBandWidth=_MyQoSPoliceMapConfMaxHighBandWidth_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,3,1,9),_MyQoSPoliceMapConfMaxHighBandWidth_Type())
myQoSPoliceMapConfMaxHighBandWidth.setMaxAccess(_C)
if mibBuilder.loadTexts:myQoSPoliceMapConfMaxHighBandWidth.setStatus(_A)
_MyQosPoliceIfTable_Object=MibTable
myQosPoliceIfTable=_MyQosPoliceIfTable_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,4))
if mibBuilder.loadTexts:myQosPoliceIfTable.setStatus(_A)
_MyQosPoliceIfEntry_Object=MibTableRow
myQosPoliceIfEntry=_MyQosPoliceIfEntry_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,4,1))
myQosPoliceIfEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:myQosPoliceIfEntry.setStatus(_A)
_MyQosPoliceIfIndex_Type=IfIndex
_MyQosPoliceIfIndex_Object=MibTableColumn
myQosPoliceIfIndex=_MyQosPoliceIfIndex_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,4,1,1),_MyQosPoliceIfIndex_Type())
myQosPoliceIfIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:myQosPoliceIfIndex.setStatus(_A)
class _MyIfPoliceMapName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_MyIfPoliceMapName_Type.__name__=_E
_MyIfPoliceMapName_Object=MibTableColumn
myIfPoliceMapName=_MyIfPoliceMapName_Object((1,3,6,1,4,1,4881,1,1,10,2,18,2,4,1,2),_MyIfPoliceMapName_Type())
myIfPoliceMapName.setMaxAccess(_C)
if mibBuilder.loadTexts:myIfPoliceMapName.setStatus(_A)
_MyQoSMIBConformance_ObjectIdentity=ObjectIdentity
myQoSMIBConformance=_MyQoSMIBConformance_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,18,3))
_MyQoSMIBCompliances_ObjectIdentity=ObjectIdentity
myQoSMIBCompliances=_MyQoSMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,18,3,1))
_MyQoSMIBGroups_ObjectIdentity=ObjectIdentity
myQoSMIBGroups=_MyQoSMIBGroups_ObjectIdentity((1,3,6,1,4,1,4881,1,1,10,2,18,3,2))
myQoSPriorityMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,18,3,2,1))
myQoSPriorityMIBGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_G),(_B,_V),(_B,_W),(_B,_H),(_B,_X),(_B,_Y),(_B,_Z),(_B,_I),(_B,_a),(_B,_b),(_B,_c),(_B,_d)))
if mibBuilder.loadTexts:myQoSPriorityMIBGroup.setStatus(_A)
myQoSTrafficClassMIBGroup=ObjectGroup((1,3,6,1,4,1,4881,1,1,10,2,18,3,2,2))
myQoSTrafficClassMIBGroup.setObjects(*((_B,_J),(_B,_e),(_B,_f),(_B,_L),(_B,_g),(_B,_M),(_B,_N),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_O),(_B,_n)))
if mibBuilder.loadTexts:myQoSTrafficClassMIBGroup.setStatus(_A)
myQoSMIBCompliance=ModuleCompliance((1,3,6,1,4,1,4881,1,1,10,2,18,3,1,1))
myQoSMIBCompliance.setObjects(*((_B,_o),(_B,_p)))
if mibBuilder.loadTexts:myQoSMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'myQoSMIB':myQoSMIB,'myQoSPriorityMIBObjects':myQoSPriorityMIBObjects,_R:myQoSGlobalStatus,_S:myPriorityTrafficClassNum,_T:myPriorityClassNum,_U:myPriorityDscpMaxValue,'myTrafficClassTable':myTrafficClassTable,'myTrafficClassEntry':myTrafficClassEntry,_G:myTrafficClassPriority,_V:myTrafficClass,_W:myPriorityToDscp,'myDscpClassTable':myDscpClassTable,'myDscpClassEntry':myDscpClassEntry,_H:myDscpClass,_X:myDscpTrafficClassPriority,_Y:myPriorityTrafficClassOperMode,_Z:myPriorityBandWidth,'myIfPriorityTable':myIfPriorityTable,'myIfPriorityEntry':myIfPriorityEntry,_I:myIfPriorityIfIndex,_a:myIfPriority,_b:myIfPriTrafficClassOperMode,_c:myIfPriorityBandwidth,_d:myIfPriorityQosTrustMode,'myQoSTrafficClassMIBObjects':myQoSTrafficClassMIBObjects,'myQoSTrafficClassTable':myQoSTrafficClassTable,'myQoSTrafficClassEntry':myQoSTrafficClassEntry,_J:myQosClassMapName,_e:myQosClassAclName,_f:myQosClassMapEntryStatus,'myQoSPoliceMapTable':myQoSPoliceMapTable,'myQoSPoliceMapEntry':myQoSPoliceMapEntry,_L:myQosPoliceMapName,_g:myQosPoliceMapEntryStatus,'myQoSPoliceMapConfTable':myQoSPoliceMapConfTable,'myQoSPoliceMapConfEntry':myQoSPoliceMapConfEntry,_M:myQoSPoliceCfgPoliceMapName,_N:myQoSPoliceCfgClassMapName,_h:myQoSPoliceMapConfMaxBandWidth,'myQoSPoliceMapConfBurstFlowLimit':myQoSPoliceMapConfBurstFlowLimit,_i:myQoSPoliceMapConfExceedAction,_j:myQoSPoliceMapConfExceedDscp,_k:myQoSPoliceMapConfNewDscp,_l:myQoSPoliceMapCfgEntryStatus,_m:myQoSPoliceMapConfMaxHighBandWidth,'myQosPoliceIfTable':myQosPoliceIfTable,'myQosPoliceIfEntry':myQosPoliceIfEntry,_O:myQosPoliceIfIndex,_n:myIfPoliceMapName,'myQoSMIBConformance':myQoSMIBConformance,'myQoSMIBCompliances':myQoSMIBCompliances,'myQoSMIBCompliance':myQoSMIBCompliance,'myQoSMIBGroups':myQoSMIBGroups,_o:myQoSPriorityMIBGroup,_p:myQoSTrafficClassMIBGroup})