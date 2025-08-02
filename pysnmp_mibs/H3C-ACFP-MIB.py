_Y='h3cAcfpServerInfo'
_X='h3cAcfpClientMode'
_W='h3cAcfpServerCurContextType'
_V='invalid'
_U='greaterThan'
_T='lessThan'
_S='seconds'
_R='passThrough'
_Q='ipserver'
_P='h3cAcfpPolicyLifetime'
_O='h3cAcfpPolicyIndex'
_N='accessible-for-notify'
_M='mirror'
_L='redirect'
_K='OctetString'
_J='TruthValue'
_I='Bits'
_H='h3cAcfpRuleIndex'
_G='DisplayString'
_F='read-only'
_E='h3cAcfpClientID'
_D='H3C-ACFP-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddressPrefixLength,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressPrefixLength')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
h3cAcfp=ModuleIdentity((1,3,6,1,4,1,2011,10,2,74))
if mibBuilder.loadTexts:h3cAcfp.setRevisions(('2006-07-04 19:36',))
_H3cAcfpObjects_ObjectIdentity=ObjectIdentity
h3cAcfpObjects=_H3cAcfpObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,74,1))
_H3cAcfpOAP_ObjectIdentity=ObjectIdentity
h3cAcfpOAP=_H3cAcfpOAP_ObjectIdentity((1,3,6,1,4,1,2011,10,2,74,1,1))
_H3cAcfpServer_ObjectIdentity=ObjectIdentity
h3cAcfpServer=_H3cAcfpServer_ObjectIdentity((1,3,6,1,4,1,2011,10,2,74,1,1,1))
class _H3cAcfpServerInfo_Type(Bits):namedValues=NamedValues(*((_Q,0),(_L,1),(_M,2),(_R,3)))
_H3cAcfpServerInfo_Type.__name__=_I
_H3cAcfpServerInfo_Object=MibScalar
h3cAcfpServerInfo=_H3cAcfpServerInfo_Object((1,3,6,1,4,1,2011,10,2,74,1,1,1,1),_H3cAcfpServerInfo_Type())
h3cAcfpServerInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cAcfpServerInfo.setStatus(_A)
class _H3cAcfpServerMaxLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cAcfpServerMaxLifetime_Type.__name__=_C
_H3cAcfpServerMaxLifetime_Object=MibScalar
h3cAcfpServerMaxLifetime=_H3cAcfpServerMaxLifetime_Object((1,3,6,1,4,1,2011,10,2,74,1,1,1,2),_H3cAcfpServerMaxLifetime_Type())
h3cAcfpServerMaxLifetime.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cAcfpServerMaxLifetime.setStatus(_A)
if mibBuilder.loadTexts:h3cAcfpServerMaxLifetime.setUnits(_S)
_H3cAcfpServerPersistentRules_Type=TruthValue
_H3cAcfpServerPersistentRules_Object=MibScalar
h3cAcfpServerPersistentRules=_H3cAcfpServerPersistentRules_Object((1,3,6,1,4,1,2011,10,2,74,1,1,1,3),_H3cAcfpServerPersistentRules_Type())
h3cAcfpServerPersistentRules.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cAcfpServerPersistentRules.setStatus(_A)
class _H3cAcfpServerCurContextType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('no-context',1),('context-VLANID',2),('context-HG',3),('context-FlowID',4),('context-HGPlus',5)))
_H3cAcfpServerCurContextType_Type.__name__=_C
_H3cAcfpServerCurContextType_Object=MibScalar
h3cAcfpServerCurContextType=_H3cAcfpServerCurContextType_Object((1,3,6,1,4,1,2011,10,2,74,1,1,1,4),_H3cAcfpServerCurContextType_Type())
h3cAcfpServerCurContextType.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cAcfpServerCurContextType.setStatus(_A)
_H3cAcfpClientInfo_ObjectIdentity=ObjectIdentity
h3cAcfpClientInfo=_H3cAcfpClientInfo_ObjectIdentity((1,3,6,1,4,1,2011,10,2,74,1,1,2))
_H3cAcfpClientInfoTable_Object=MibTable
h3cAcfpClientInfoTable=_H3cAcfpClientInfoTable_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1))
if mibBuilder.loadTexts:h3cAcfpClientInfoTable.setStatus(_A)
_H3cAcfpClientInfoEntry_Object=MibTableRow
h3cAcfpClientInfoEntry=_H3cAcfpClientInfoEntry_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1))
h3cAcfpClientInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:h3cAcfpClientInfoEntry.setStatus(_A)
class _H3cAcfpClientID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cAcfpClientID_Type.__name__=_C
_H3cAcfpClientID_Object=MibTableColumn
h3cAcfpClientID=_H3cAcfpClientID_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,1),_H3cAcfpClientID_Type())
h3cAcfpClientID.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cAcfpClientID.setStatus(_A)
class _H3cAcfpClientDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cAcfpClientDescription_Type.__name__=_G
_H3cAcfpClientDescription_Object=MibTableColumn
h3cAcfpClientDescription=_H3cAcfpClientDescription_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,2),_H3cAcfpClientDescription_Type())
h3cAcfpClientDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpClientDescription.setStatus(_A)
class _H3cAcfpClientHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cAcfpClientHwVersion_Type.__name__=_G
_H3cAcfpClientHwVersion_Object=MibTableColumn
h3cAcfpClientHwVersion=_H3cAcfpClientHwVersion_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,3),_H3cAcfpClientHwVersion_Type())
h3cAcfpClientHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpClientHwVersion.setStatus(_A)
class _H3cAcfpClientOSVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cAcfpClientOSVersion_Type.__name__=_G
_H3cAcfpClientOSVersion_Object=MibTableColumn
h3cAcfpClientOSVersion=_H3cAcfpClientOSVersion_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,4),_H3cAcfpClientOSVersion_Type())
h3cAcfpClientOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpClientOSVersion.setStatus(_A)
class _H3cAcfpClientAppVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_H3cAcfpClientAppVersion_Type.__name__=_G
_H3cAcfpClientAppVersion_Object=MibTableColumn
h3cAcfpClientAppVersion=_H3cAcfpClientAppVersion_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,5),_H3cAcfpClientAppVersion_Type())
h3cAcfpClientAppVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpClientAppVersion.setStatus(_A)
_H3cAcfpClientIP_Type=IpAddress
_H3cAcfpClientIP_Object=MibTableColumn
h3cAcfpClientIP=_H3cAcfpClientIP_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,6),_H3cAcfpClientIP_Type())
h3cAcfpClientIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpClientIP.setStatus(_A)
class _H3cAcfpClientMode_Type(Bits):defaultHexValue='';namedValues=NamedValues(*((_Q,0),(_L,1),(_M,2),(_R,3)))
_H3cAcfpClientMode_Type.__name__=_I
_H3cAcfpClientMode_Object=MibTableColumn
h3cAcfpClientMode=_H3cAcfpClientMode_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,7),_H3cAcfpClientMode_Type())
h3cAcfpClientMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpClientMode.setStatus(_A)
_H3cAcfpClientRowStatus_Type=RowStatus
_H3cAcfpClientRowStatus_Object=MibTableColumn
h3cAcfpClientRowStatus=_H3cAcfpClientRowStatus_Object((1,3,6,1,4,1,2011,10,2,74,1,1,2,1,1,8),_H3cAcfpClientRowStatus_Type())
h3cAcfpClientRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpClientRowStatus.setStatus(_A)
_H3cAcfpPolicy_ObjectIdentity=ObjectIdentity
h3cAcfpPolicy=_H3cAcfpPolicy_ObjectIdentity((1,3,6,1,4,1,2011,10,2,74,1,1,3))
_H3cAcfpPolicyTable_Object=MibTable
h3cAcfpPolicyTable=_H3cAcfpPolicyTable_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1))
if mibBuilder.loadTexts:h3cAcfpPolicyTable.setStatus(_A)
_H3cAcfpPolicyEntry_Object=MibTableRow
h3cAcfpPolicyEntry=_H3cAcfpPolicyEntry_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1))
h3cAcfpPolicyEntry.setIndexNames((0,_D,_E),(0,_D,_O))
if mibBuilder.loadTexts:h3cAcfpPolicyEntry.setStatus(_A)
class _H3cAcfpPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cAcfpPolicyIndex_Type.__name__=_C
_H3cAcfpPolicyIndex_Object=MibTableColumn
h3cAcfpPolicyIndex=_H3cAcfpPolicyIndex_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,1),_H3cAcfpPolicyIndex_Type())
h3cAcfpPolicyIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cAcfpPolicyIndex.setStatus(_A)
class _H3cAcfpPolicyInIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cAcfpPolicyInIfIndex_Type.__name__=_C
_H3cAcfpPolicyInIfIndex_Object=MibTableColumn
h3cAcfpPolicyInIfIndex=_H3cAcfpPolicyInIfIndex_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,2),_H3cAcfpPolicyInIfIndex_Type())
h3cAcfpPolicyInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyInIfIndex.setStatus(_A)
class _H3cAcfpPolicyOutIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cAcfpPolicyOutIfIndex_Type.__name__=_C
_H3cAcfpPolicyOutIfIndex_Object=MibTableColumn
h3cAcfpPolicyOutIfIndex=_H3cAcfpPolicyOutIfIndex_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,3),_H3cAcfpPolicyOutIfIndex_Type())
h3cAcfpPolicyOutIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyOutIfIndex.setStatus(_A)
class _H3cAcfpPolicyDestIfIndex_Type(Integer32):defaultValue=0
_H3cAcfpPolicyDestIfIndex_Type.__name__=_C
_H3cAcfpPolicyDestIfIndex_Object=MibTableColumn
h3cAcfpPolicyDestIfIndex=_H3cAcfpPolicyDestIfIndex_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,4),_H3cAcfpPolicyDestIfIndex_Type())
h3cAcfpPolicyDestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyDestIfIndex.setStatus(_A)
class _H3cAcfpPolicyContextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cAcfpPolicyContextID_Type.__name__=_C
_H3cAcfpPolicyContextID_Object=MibTableColumn
h3cAcfpPolicyContextID=_H3cAcfpPolicyContextID_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,5),_H3cAcfpPolicyContextID_Type())
h3cAcfpPolicyContextID.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cAcfpPolicyContextID.setStatus(_A)
class _H3cAcfpPolicyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_H3cAcfpPolicyAdminStatus_Type.__name__=_C
_H3cAcfpPolicyAdminStatus_Object=MibTableColumn
h3cAcfpPolicyAdminStatus=_H3cAcfpPolicyAdminStatus_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,6),_H3cAcfpPolicyAdminStatus_Type())
h3cAcfpPolicyAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyAdminStatus.setStatus(_A)
class _H3cAcfpPolicyLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_H3cAcfpPolicyLifetime_Type.__name__=_C
_H3cAcfpPolicyLifetime_Object=MibTableColumn
h3cAcfpPolicyLifetime=_H3cAcfpPolicyLifetime_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,7),_H3cAcfpPolicyLifetime_Type())
h3cAcfpPolicyLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyLifetime.setStatus(_A)
if mibBuilder.loadTexts:h3cAcfpPolicyLifetime.setUnits(_S)
class _H3cAcfpPolicyTimeStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_H3cAcfpPolicyTimeStart_Type.__name__=_K
_H3cAcfpPolicyTimeStart_Object=MibTableColumn
h3cAcfpPolicyTimeStart=_H3cAcfpPolicyTimeStart_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,8),_H3cAcfpPolicyTimeStart_Type())
h3cAcfpPolicyTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyTimeStart.setStatus(_A)
class _H3cAcfpPolicyTimeEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_H3cAcfpPolicyTimeEnd_Type.__name__=_K
_H3cAcfpPolicyTimeEnd_Object=MibTableColumn
h3cAcfpPolicyTimeEnd=_H3cAcfpPolicyTimeEnd_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,9),_H3cAcfpPolicyTimeEnd_Type())
h3cAcfpPolicyTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyTimeEnd.setStatus(_A)
_H3cAcfpPolicyRowStatus_Type=RowStatus
_H3cAcfpPolicyRowStatus_Object=MibTableColumn
h3cAcfpPolicyRowStatus=_H3cAcfpPolicyRowStatus_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,10),_H3cAcfpPolicyRowStatus_Type())
h3cAcfpPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyRowStatus.setStatus(_A)
class _H3cAcfpPolicyDestIfFailAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delete',1),('reserve',2)))
_H3cAcfpPolicyDestIfFailAction_Type.__name__=_C
_H3cAcfpPolicyDestIfFailAction_Object=MibTableColumn
h3cAcfpPolicyDestIfFailAction=_H3cAcfpPolicyDestIfFailAction_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,11),_H3cAcfpPolicyDestIfFailAction_Type())
h3cAcfpPolicyDestIfFailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyDestIfFailAction.setStatus(_A)
class _H3cAcfpPolicyPriority_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('priority1',1),('priority2',2),('priority3',3),('priority4',4),('priority5',5),('priority6',6),('priority7',7),('priority8',8)))
_H3cAcfpPolicyPriority_Type.__name__=_C
_H3cAcfpPolicyPriority_Object=MibTableColumn
h3cAcfpPolicyPriority=_H3cAcfpPolicyPriority_Object((1,3,6,1,4,1,2011,10,2,74,1,1,3,1,1,12),_H3cAcfpPolicyPriority_Type())
h3cAcfpPolicyPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpPolicyPriority.setStatus(_A)
_H3cAcfpRule_ObjectIdentity=ObjectIdentity
h3cAcfpRule=_H3cAcfpRule_ObjectIdentity((1,3,6,1,4,1,2011,10,2,74,1,1,4))
_H3cAcfpRuleTable_Object=MibTable
h3cAcfpRuleTable=_H3cAcfpRuleTable_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1))
if mibBuilder.loadTexts:h3cAcfpRuleTable.setStatus(_A)
_H3cAcfpRuleEntry_Object=MibTableRow
h3cAcfpRuleEntry=_H3cAcfpRuleEntry_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1))
h3cAcfpRuleEntry.setIndexNames((0,_D,_E),(0,_D,_O),(0,_D,_H))
if mibBuilder.loadTexts:h3cAcfpRuleEntry.setStatus(_A)
class _H3cAcfpRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_H3cAcfpRuleIndex_Type.__name__=_C
_H3cAcfpRuleIndex_Object=MibTableColumn
h3cAcfpRuleIndex=_H3cAcfpRuleIndex_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,1),_H3cAcfpRuleIndex_Type())
h3cAcfpRuleIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:h3cAcfpRuleIndex.setStatus(_A)
class _H3cAcfpRuleOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('fail',2)))
_H3cAcfpRuleOperStatus_Type.__name__=_C
_H3cAcfpRuleOperStatus_Object=MibTableColumn
h3cAcfpRuleOperStatus=_H3cAcfpRuleOperStatus_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,2),_H3cAcfpRuleOperStatus_Type())
h3cAcfpRuleOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:h3cAcfpRuleOperStatus.setStatus(_A)
class _H3cAcfpRuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('permit',1),('deny',2),(_L,3),(_M,4),('rate',5)))
_H3cAcfpRuleAction_Type.__name__=_C
_H3cAcfpRuleAction_Object=MibTableColumn
h3cAcfpRuleAction=_H3cAcfpRuleAction_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,3),_H3cAcfpRuleAction_Type())
h3cAcfpRuleAction.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleAction.setStatus(_A)
class _H3cAcfpRuleAll_Type(TruthValue):defaultValue=2
_H3cAcfpRuleAll_Type.__name__=_J
_H3cAcfpRuleAll_Object=MibTableColumn
h3cAcfpRuleAll=_H3cAcfpRuleAll_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,4),_H3cAcfpRuleAll_Type())
h3cAcfpRuleAll.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleAll.setStatus(_A)
_H3cAcfpRuleSrcMAC_Type=MacAddress
_H3cAcfpRuleSrcMAC_Object=MibTableColumn
h3cAcfpRuleSrcMAC=_H3cAcfpRuleSrcMAC_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,5),_H3cAcfpRuleSrcMAC_Type())
h3cAcfpRuleSrcMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcMAC.setStatus(_A)
_H3cAcfpRuleDstMAC_Type=MacAddress
_H3cAcfpRuleDstMAC_Object=MibTableColumn
h3cAcfpRuleDstMAC=_H3cAcfpRuleDstMAC_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,6),_H3cAcfpRuleDstMAC_Type())
h3cAcfpRuleDstMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstMAC.setStatus(_A)
class _H3cAcfpRuleVlanStart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_H3cAcfpRuleVlanStart_Type.__name__=_C
_H3cAcfpRuleVlanStart_Object=MibTableColumn
h3cAcfpRuleVlanStart=_H3cAcfpRuleVlanStart_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,7),_H3cAcfpRuleVlanStart_Type())
h3cAcfpRuleVlanStart.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleVlanStart.setStatus(_A)
class _H3cAcfpRuleVlanEnd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_H3cAcfpRuleVlanEnd_Type.__name__=_C
_H3cAcfpRuleVlanEnd_Object=MibTableColumn
h3cAcfpRuleVlanEnd=_H3cAcfpRuleVlanEnd_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,8),_H3cAcfpRuleVlanEnd_Type())
h3cAcfpRuleVlanEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleVlanEnd.setStatus(_A)
class _H3cAcfpRuleProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_H3cAcfpRuleProtocol_Type.__name__=_C
_H3cAcfpRuleProtocol_Object=MibTableColumn
h3cAcfpRuleProtocol=_H3cAcfpRuleProtocol_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,9),_H3cAcfpRuleProtocol_Type())
h3cAcfpRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleProtocol.setStatus(_A)
_H3cAcfpRuleSrcIP_Type=IpAddress
_H3cAcfpRuleSrcIP_Object=MibTableColumn
h3cAcfpRuleSrcIP=_H3cAcfpRuleSrcIP_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,10),_H3cAcfpRuleSrcIP_Type())
h3cAcfpRuleSrcIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcIP.setStatus(_A)
_H3cAcfpRuleSrcIPMask_Type=IpAddress
_H3cAcfpRuleSrcIPMask_Object=MibTableColumn
h3cAcfpRuleSrcIPMask=_H3cAcfpRuleSrcIPMask_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,11),_H3cAcfpRuleSrcIPMask_Type())
h3cAcfpRuleSrcIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcIPMask.setStatus(_A)
class _H3cAcfpRuleSrcOp_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('equal',1),('notEqual',2),(_T,3),(_U,4),('range',5),(_V,6)))
_H3cAcfpRuleSrcOp_Type.__name__=_C
_H3cAcfpRuleSrcOp_Object=MibTableColumn
h3cAcfpRuleSrcOp=_H3cAcfpRuleSrcOp_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,12),_H3cAcfpRuleSrcOp_Type())
h3cAcfpRuleSrcOp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcOp.setStatus(_A)
class _H3cAcfpRuleSrcStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cAcfpRuleSrcStartPort_Type.__name__=_C
_H3cAcfpRuleSrcStartPort_Object=MibTableColumn
h3cAcfpRuleSrcStartPort=_H3cAcfpRuleSrcStartPort_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,13),_H3cAcfpRuleSrcStartPort_Type())
h3cAcfpRuleSrcStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcStartPort.setStatus(_A)
class _H3cAcfpRuleSrcEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cAcfpRuleSrcEndPort_Type.__name__=_C
_H3cAcfpRuleSrcEndPort_Object=MibTableColumn
h3cAcfpRuleSrcEndPort=_H3cAcfpRuleSrcEndPort_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,14),_H3cAcfpRuleSrcEndPort_Type())
h3cAcfpRuleSrcEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcEndPort.setStatus(_A)
_H3cAcfpRuleDstIP_Type=IpAddress
_H3cAcfpRuleDstIP_Object=MibTableColumn
h3cAcfpRuleDstIP=_H3cAcfpRuleDstIP_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,15),_H3cAcfpRuleDstIP_Type())
h3cAcfpRuleDstIP.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstIP.setStatus(_A)
_H3cAcfpRuleDstIPMask_Type=IpAddress
_H3cAcfpRuleDstIPMask_Object=MibTableColumn
h3cAcfpRuleDstIPMask=_H3cAcfpRuleDstIPMask_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,16),_H3cAcfpRuleDstIPMask_Type())
h3cAcfpRuleDstIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstIPMask.setStatus(_A)
class _H3cAcfpRuleDstOp_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('equal',1),('nonEqual',2),(_T,3),(_U,4),('range',5),(_V,6)))
_H3cAcfpRuleDstOp_Type.__name__=_C
_H3cAcfpRuleDstOp_Object=MibTableColumn
h3cAcfpRuleDstOp=_H3cAcfpRuleDstOp_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,17),_H3cAcfpRuleDstOp_Type())
h3cAcfpRuleDstOp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstOp.setStatus(_A)
class _H3cAcfpRuleDstStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cAcfpRuleDstStartPort_Type.__name__=_C
_H3cAcfpRuleDstStartPort_Object=MibTableColumn
h3cAcfpRuleDstStartPort=_H3cAcfpRuleDstStartPort_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,18),_H3cAcfpRuleDstStartPort_Type())
h3cAcfpRuleDstStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstStartPort.setStatus(_A)
class _H3cAcfpRuleDstEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cAcfpRuleDstEndPort_Type.__name__=_C
_H3cAcfpRuleDstEndPort_Object=MibTableColumn
h3cAcfpRuleDstEndPort=_H3cAcfpRuleDstEndPort_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,19),_H3cAcfpRuleDstEndPort_Type())
h3cAcfpRuleDstEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstEndPort.setStatus(_A)
class _H3cAcfpRulePrecedence_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_H3cAcfpRulePrecedence_Type.__name__=_C
_H3cAcfpRulePrecedence_Object=MibTableColumn
h3cAcfpRulePrecedence=_H3cAcfpRulePrecedence_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,20),_H3cAcfpRulePrecedence_Type())
h3cAcfpRulePrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRulePrecedence.setStatus(_A)
class _H3cAcfpRuleTos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15),ValueRangeConstraint(255,255))
_H3cAcfpRuleTos_Type.__name__=_C
_H3cAcfpRuleTos_Object=MibTableColumn
h3cAcfpRuleTos=_H3cAcfpRuleTos_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,21),_H3cAcfpRuleTos_Type())
h3cAcfpRuleTos.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleTos.setStatus(_A)
class _H3cAcfpRuleDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_H3cAcfpRuleDscp_Type.__name__=_C
_H3cAcfpRuleDscp_Object=MibTableColumn
h3cAcfpRuleDscp=_H3cAcfpRuleDscp_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,22),_H3cAcfpRuleDscp_Type())
h3cAcfpRuleDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDscp.setStatus(_A)
class _H3cAcfpRuleEstablish_Type(TruthValue):defaultValue=2
_H3cAcfpRuleEstablish_Type.__name__=_J
_H3cAcfpRuleEstablish_Object=MibTableColumn
h3cAcfpRuleEstablish=_H3cAcfpRuleEstablish_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,23),_H3cAcfpRuleEstablish_Type())
h3cAcfpRuleEstablish.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleEstablish.setStatus('deprecated')
class _H3cAcfpRuleFragment_Type(TruthValue):defaultValue=2
_H3cAcfpRuleFragment_Type.__name__=_J
_H3cAcfpRuleFragment_Object=MibTableColumn
h3cAcfpRuleFragment=_H3cAcfpRuleFragment_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,24),_H3cAcfpRuleFragment_Type())
h3cAcfpRuleFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleFragment.setStatus(_A)
_H3cAcfpRulePacketRate_Type=Integer32
_H3cAcfpRulePacketRate_Object=MibTableColumn
h3cAcfpRulePacketRate=_H3cAcfpRulePacketRate_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,25),_H3cAcfpRulePacketRate_Type())
h3cAcfpRulePacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRulePacketRate.setStatus(_A)
_H3cAcfpRuleRowStatus_Type=RowStatus
_H3cAcfpRuleRowStatus_Object=MibTableColumn
h3cAcfpRuleRowStatus=_H3cAcfpRuleRowStatus_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,26),_H3cAcfpRuleRowStatus_Type())
h3cAcfpRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleRowStatus.setStatus(_A)
class _H3cAcfpRuleTCPFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cAcfpRuleTCPFlag_Type.__name__=_C
_H3cAcfpRuleTCPFlag_Object=MibTableColumn
h3cAcfpRuleTCPFlag=_H3cAcfpRuleTCPFlag_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,27),_H3cAcfpRuleTCPFlag_Type())
h3cAcfpRuleTCPFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleTCPFlag.setStatus(_A)
_H3cAcfpRuleSrcIPV6Address_Type=Ipv6Address
_H3cAcfpRuleSrcIPV6Address_Object=MibTableColumn
h3cAcfpRuleSrcIPV6Address=_H3cAcfpRuleSrcIPV6Address_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,28),_H3cAcfpRuleSrcIPV6Address_Type())
h3cAcfpRuleSrcIPV6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcIPV6Address.setStatus(_A)
_H3cAcfpRuleSrcPrefixLen_Type=InetAddressPrefixLength
_H3cAcfpRuleSrcPrefixLen_Object=MibTableColumn
h3cAcfpRuleSrcPrefixLen=_H3cAcfpRuleSrcPrefixLen_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,29),_H3cAcfpRuleSrcPrefixLen_Type())
h3cAcfpRuleSrcPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleSrcPrefixLen.setStatus(_A)
_H3cAcfpRuleDstIPV6Address_Type=Ipv6Address
_H3cAcfpRuleDstIPV6Address_Object=MibTableColumn
h3cAcfpRuleDstIPV6Address=_H3cAcfpRuleDstIPV6Address_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,30),_H3cAcfpRuleDstIPV6Address_Type())
h3cAcfpRuleDstIPV6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstIPV6Address.setStatus(_A)
_H3cAcfpRuleDstPrefixLen_Type=InetAddressPrefixLength
_H3cAcfpRuleDstPrefixLen_Object=MibTableColumn
h3cAcfpRuleDstPrefixLen=_H3cAcfpRuleDstPrefixLen_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,31),_H3cAcfpRuleDstPrefixLen_Type())
h3cAcfpRuleDstPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleDstPrefixLen.setStatus(_A)
class _H3cAcfpRuleTrafficType_Type(Bits):namedValues=NamedValues(*(('unicast',0),('multicast',1),('broadcast',2)))
_H3cAcfpRuleTrafficType_Type.__name__=_I
_H3cAcfpRuleTrafficType_Object=MibTableColumn
h3cAcfpRuleTrafficType=_H3cAcfpRuleTrafficType_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,32),_H3cAcfpRuleTrafficType_Type())
h3cAcfpRuleTrafficType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleTrafficType.setStatus(_A)
class _H3cAcfpRuleTypeOrLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_H3cAcfpRuleTypeOrLen_Type.__name__=_C
_H3cAcfpRuleTypeOrLen_Object=MibTableColumn
h3cAcfpRuleTypeOrLen=_H3cAcfpRuleTypeOrLen_Object((1,3,6,1,4,1,2011,10,2,74,1,1,4,1,1,33),_H3cAcfpRuleTypeOrLen_Type())
h3cAcfpRuleTypeOrLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cAcfpRuleTypeOrLen.setStatus(_A)
_H3cAcfpNotifications_ObjectIdentity=ObjectIdentity
h3cAcfpNotifications=_H3cAcfpNotifications_ObjectIdentity((1,3,6,1,4,1,2011,10,2,74,1,1,5))
h3cAcfpCurContextChanged=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,1))
h3cAcfpCurContextChanged.setObjects((_D,_W))
if mibBuilder.loadTexts:h3cAcfpCurContextChanged.setStatus(_A)
h3cAcfpClientRegister=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,2))
h3cAcfpClientRegister.setObjects((_D,_E))
if mibBuilder.loadTexts:h3cAcfpClientRegister.setStatus(_A)
h3cAcfpClientUnRegister=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,3))
h3cAcfpClientUnRegister.setObjects((_D,_E))
if mibBuilder.loadTexts:h3cAcfpClientUnRegister.setStatus(_A)
h3cAcfpClientDead=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,4))
h3cAcfpClientDead.setObjects((_D,_E))
if mibBuilder.loadTexts:h3cAcfpClientDead.setStatus(_A)
h3cAcfpNotSupportedOAPMode=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,5))
h3cAcfpNotSupportedOAPMode.setObjects(*((_D,_E),(_D,_X),(_D,_Y)))
if mibBuilder.loadTexts:h3cAcfpNotSupportedOAPMode.setStatus(_A)
h3cAcfpLifetimeChangeEvent=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,6))
h3cAcfpLifetimeChangeEvent.setObjects((_D,_P))
if mibBuilder.loadTexts:h3cAcfpLifetimeChangeEvent.setStatus(_A)
h3cAcfpRuleCreatedEvent=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,7))
h3cAcfpRuleCreatedEvent.setObjects((_D,_H))
if mibBuilder.loadTexts:h3cAcfpRuleCreatedEvent.setStatus(_A)
h3cAcfpRuleDeletedEvent=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,8))
h3cAcfpRuleDeletedEvent.setObjects((_D,_H))
if mibBuilder.loadTexts:h3cAcfpRuleDeletedEvent.setStatus(_A)
h3cAcfpRuleErrorEvent=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,9))
h3cAcfpRuleErrorEvent.setObjects((_D,_H))
if mibBuilder.loadTexts:h3cAcfpRuleErrorEvent.setStatus(_A)
h3cAcfpLifetimeExpireEvent=NotificationType((1,3,6,1,4,1,2011,10,2,74,1,1,5,10))
h3cAcfpLifetimeExpireEvent.setObjects((_D,_P))
if mibBuilder.loadTexts:h3cAcfpLifetimeExpireEvent.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'h3cAcfp':h3cAcfp,'h3cAcfpObjects':h3cAcfpObjects,'h3cAcfpOAP':h3cAcfpOAP,'h3cAcfpServer':h3cAcfpServer,_Y:h3cAcfpServerInfo,'h3cAcfpServerMaxLifetime':h3cAcfpServerMaxLifetime,'h3cAcfpServerPersistentRules':h3cAcfpServerPersistentRules,_W:h3cAcfpServerCurContextType,'h3cAcfpClientInfo':h3cAcfpClientInfo,'h3cAcfpClientInfoTable':h3cAcfpClientInfoTable,'h3cAcfpClientInfoEntry':h3cAcfpClientInfoEntry,_E:h3cAcfpClientID,'h3cAcfpClientDescription':h3cAcfpClientDescription,'h3cAcfpClientHwVersion':h3cAcfpClientHwVersion,'h3cAcfpClientOSVersion':h3cAcfpClientOSVersion,'h3cAcfpClientAppVersion':h3cAcfpClientAppVersion,'h3cAcfpClientIP':h3cAcfpClientIP,_X:h3cAcfpClientMode,'h3cAcfpClientRowStatus':h3cAcfpClientRowStatus,'h3cAcfpPolicy':h3cAcfpPolicy,'h3cAcfpPolicyTable':h3cAcfpPolicyTable,'h3cAcfpPolicyEntry':h3cAcfpPolicyEntry,_O:h3cAcfpPolicyIndex,'h3cAcfpPolicyInIfIndex':h3cAcfpPolicyInIfIndex,'h3cAcfpPolicyOutIfIndex':h3cAcfpPolicyOutIfIndex,'h3cAcfpPolicyDestIfIndex':h3cAcfpPolicyDestIfIndex,'h3cAcfpPolicyContextID':h3cAcfpPolicyContextID,'h3cAcfpPolicyAdminStatus':h3cAcfpPolicyAdminStatus,_P:h3cAcfpPolicyLifetime,'h3cAcfpPolicyTimeStart':h3cAcfpPolicyTimeStart,'h3cAcfpPolicyTimeEnd':h3cAcfpPolicyTimeEnd,'h3cAcfpPolicyRowStatus':h3cAcfpPolicyRowStatus,'h3cAcfpPolicyDestIfFailAction':h3cAcfpPolicyDestIfFailAction,'h3cAcfpPolicyPriority':h3cAcfpPolicyPriority,'h3cAcfpRule':h3cAcfpRule,'h3cAcfpRuleTable':h3cAcfpRuleTable,'h3cAcfpRuleEntry':h3cAcfpRuleEntry,_H:h3cAcfpRuleIndex,'h3cAcfpRuleOperStatus':h3cAcfpRuleOperStatus,'h3cAcfpRuleAction':h3cAcfpRuleAction,'h3cAcfpRuleAll':h3cAcfpRuleAll,'h3cAcfpRuleSrcMAC':h3cAcfpRuleSrcMAC,'h3cAcfpRuleDstMAC':h3cAcfpRuleDstMAC,'h3cAcfpRuleVlanStart':h3cAcfpRuleVlanStart,'h3cAcfpRuleVlanEnd':h3cAcfpRuleVlanEnd,'h3cAcfpRuleProtocol':h3cAcfpRuleProtocol,'h3cAcfpRuleSrcIP':h3cAcfpRuleSrcIP,'h3cAcfpRuleSrcIPMask':h3cAcfpRuleSrcIPMask,'h3cAcfpRuleSrcOp':h3cAcfpRuleSrcOp,'h3cAcfpRuleSrcStartPort':h3cAcfpRuleSrcStartPort,'h3cAcfpRuleSrcEndPort':h3cAcfpRuleSrcEndPort,'h3cAcfpRuleDstIP':h3cAcfpRuleDstIP,'h3cAcfpRuleDstIPMask':h3cAcfpRuleDstIPMask,'h3cAcfpRuleDstOp':h3cAcfpRuleDstOp,'h3cAcfpRuleDstStartPort':h3cAcfpRuleDstStartPort,'h3cAcfpRuleDstEndPort':h3cAcfpRuleDstEndPort,'h3cAcfpRulePrecedence':h3cAcfpRulePrecedence,'h3cAcfpRuleTos':h3cAcfpRuleTos,'h3cAcfpRuleDscp':h3cAcfpRuleDscp,'h3cAcfpRuleEstablish':h3cAcfpRuleEstablish,'h3cAcfpRuleFragment':h3cAcfpRuleFragment,'h3cAcfpRulePacketRate':h3cAcfpRulePacketRate,'h3cAcfpRuleRowStatus':h3cAcfpRuleRowStatus,'h3cAcfpRuleTCPFlag':h3cAcfpRuleTCPFlag,'h3cAcfpRuleSrcIPV6Address':h3cAcfpRuleSrcIPV6Address,'h3cAcfpRuleSrcPrefixLen':h3cAcfpRuleSrcPrefixLen,'h3cAcfpRuleDstIPV6Address':h3cAcfpRuleDstIPV6Address,'h3cAcfpRuleDstPrefixLen':h3cAcfpRuleDstPrefixLen,'h3cAcfpRuleTrafficType':h3cAcfpRuleTrafficType,'h3cAcfpRuleTypeOrLen':h3cAcfpRuleTypeOrLen,'h3cAcfpNotifications':h3cAcfpNotifications,'h3cAcfpCurContextChanged':h3cAcfpCurContextChanged,'h3cAcfpClientRegister':h3cAcfpClientRegister,'h3cAcfpClientUnRegister':h3cAcfpClientUnRegister,'h3cAcfpClientDead':h3cAcfpClientDead,'h3cAcfpNotSupportedOAPMode':h3cAcfpNotSupportedOAPMode,'h3cAcfpLifetimeChangeEvent':h3cAcfpLifetimeChangeEvent,'h3cAcfpRuleCreatedEvent':h3cAcfpRuleCreatedEvent,'h3cAcfpRuleDeletedEvent':h3cAcfpRuleDeletedEvent,'h3cAcfpRuleErrorEvent':h3cAcfpRuleErrorEvent,'h3cAcfpLifetimeExpireEvent':h3cAcfpLifetimeExpireEvent})