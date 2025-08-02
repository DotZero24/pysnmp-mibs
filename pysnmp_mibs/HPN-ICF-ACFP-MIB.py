_Y='hpnicfAcfpServerInfo'
_X='hpnicfAcfpClientMode'
_W='hpnicfAcfpServerCurContextType'
_V='invalid'
_U='greaterThan'
_T='lessThan'
_S='seconds'
_R='passThrough'
_Q='ipserver'
_P='hpnicfAcfpPolicyLifetime'
_O='hpnicfAcfpPolicyIndex'
_N='accessible-for-notify'
_M='mirror'
_L='redirect'
_K='OctetString'
_J='TruthValue'
_I='Bits'
_H='hpnicfAcfpRuleIndex'
_G='DisplayString'
_F='read-only'
_E='hpnicfAcfpClientID'
_D='HPN-ICF-ACFP-MIB'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_K,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddressPrefixLength,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressPrefixLength')
Ipv6Address,=mibBuilder.importSymbols('IPV6-TC','Ipv6Address')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_I,'Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_G,'MacAddress','PhysAddress','RowStatus','TextualConvention',_J)
hpnicfAcfp=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74))
if mibBuilder.loadTexts:hpnicfAcfp.setRevisions(('2006-07-04 19:36',))
_HpnicfAcfpObjects_ObjectIdentity=ObjectIdentity
hpnicfAcfpObjects=_HpnicfAcfpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74,1))
_HpnicfAcfpOAP_ObjectIdentity=ObjectIdentity
hpnicfAcfpOAP=_HpnicfAcfpOAP_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1))
_HpnicfAcfpServer_ObjectIdentity=ObjectIdentity
hpnicfAcfpServer=_HpnicfAcfpServer_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,1))
class _HpnicfAcfpServerInfo_Type(Bits):namedValues=NamedValues(*((_Q,0),(_L,1),(_M,2),(_R,3)))
_HpnicfAcfpServerInfo_Type.__name__=_I
_HpnicfAcfpServerInfo_Object=MibScalar
hpnicfAcfpServerInfo=_HpnicfAcfpServerInfo_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,1,1),_HpnicfAcfpServerInfo_Type())
hpnicfAcfpServerInfo.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfAcfpServerInfo.setStatus(_A)
class _HpnicfAcfpServerMaxLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfAcfpServerMaxLifetime_Type.__name__=_C
_HpnicfAcfpServerMaxLifetime_Object=MibScalar
hpnicfAcfpServerMaxLifetime=_HpnicfAcfpServerMaxLifetime_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,1,2),_HpnicfAcfpServerMaxLifetime_Type())
hpnicfAcfpServerMaxLifetime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfAcfpServerMaxLifetime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfAcfpServerMaxLifetime.setUnits(_S)
_HpnicfAcfpServerPersistentRules_Type=TruthValue
_HpnicfAcfpServerPersistentRules_Object=MibScalar
hpnicfAcfpServerPersistentRules=_HpnicfAcfpServerPersistentRules_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,1,3),_HpnicfAcfpServerPersistentRules_Type())
hpnicfAcfpServerPersistentRules.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfAcfpServerPersistentRules.setStatus(_A)
class _HpnicfAcfpServerCurContextType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('no-context',1),('context-VLANID',2),('context-HG',3),('context-FlowID',4),('context-HGPlus',5)))
_HpnicfAcfpServerCurContextType_Type.__name__=_C
_HpnicfAcfpServerCurContextType_Object=MibScalar
hpnicfAcfpServerCurContextType=_HpnicfAcfpServerCurContextType_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,1,4),_HpnicfAcfpServerCurContextType_Type())
hpnicfAcfpServerCurContextType.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfAcfpServerCurContextType.setStatus(_A)
_HpnicfAcfpClientInfo_ObjectIdentity=ObjectIdentity
hpnicfAcfpClientInfo=_HpnicfAcfpClientInfo_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2))
_HpnicfAcfpClientInfoTable_Object=MibTable
hpnicfAcfpClientInfoTable=_HpnicfAcfpClientInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1))
if mibBuilder.loadTexts:hpnicfAcfpClientInfoTable.setStatus(_A)
_HpnicfAcfpClientInfoEntry_Object=MibTableRow
hpnicfAcfpClientInfoEntry=_HpnicfAcfpClientInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1))
hpnicfAcfpClientInfoEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfAcfpClientInfoEntry.setStatus(_A)
class _HpnicfAcfpClientID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfAcfpClientID_Type.__name__=_C
_HpnicfAcfpClientID_Object=MibTableColumn
hpnicfAcfpClientID=_HpnicfAcfpClientID_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,1),_HpnicfAcfpClientID_Type())
hpnicfAcfpClientID.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfAcfpClientID.setStatus(_A)
class _HpnicfAcfpClientDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfAcfpClientDescription_Type.__name__=_G
_HpnicfAcfpClientDescription_Object=MibTableColumn
hpnicfAcfpClientDescription=_HpnicfAcfpClientDescription_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,2),_HpnicfAcfpClientDescription_Type())
hpnicfAcfpClientDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpClientDescription.setStatus(_A)
class _HpnicfAcfpClientHwVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfAcfpClientHwVersion_Type.__name__=_G
_HpnicfAcfpClientHwVersion_Object=MibTableColumn
hpnicfAcfpClientHwVersion=_HpnicfAcfpClientHwVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,3),_HpnicfAcfpClientHwVersion_Type())
hpnicfAcfpClientHwVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpClientHwVersion.setStatus(_A)
class _HpnicfAcfpClientOSVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfAcfpClientOSVersion_Type.__name__=_G
_HpnicfAcfpClientOSVersion_Object=MibTableColumn
hpnicfAcfpClientOSVersion=_HpnicfAcfpClientOSVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,4),_HpnicfAcfpClientOSVersion_Type())
hpnicfAcfpClientOSVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpClientOSVersion.setStatus(_A)
class _HpnicfAcfpClientAppVersion_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_HpnicfAcfpClientAppVersion_Type.__name__=_G
_HpnicfAcfpClientAppVersion_Object=MibTableColumn
hpnicfAcfpClientAppVersion=_HpnicfAcfpClientAppVersion_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,5),_HpnicfAcfpClientAppVersion_Type())
hpnicfAcfpClientAppVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpClientAppVersion.setStatus(_A)
_HpnicfAcfpClientIP_Type=IpAddress
_HpnicfAcfpClientIP_Object=MibTableColumn
hpnicfAcfpClientIP=_HpnicfAcfpClientIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,6),_HpnicfAcfpClientIP_Type())
hpnicfAcfpClientIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpClientIP.setStatus(_A)
class _HpnicfAcfpClientMode_Type(Bits):defaultHexValue='';namedValues=NamedValues(*((_Q,0),(_L,1),(_M,2),(_R,3)))
_HpnicfAcfpClientMode_Type.__name__=_I
_HpnicfAcfpClientMode_Object=MibTableColumn
hpnicfAcfpClientMode=_HpnicfAcfpClientMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,7),_HpnicfAcfpClientMode_Type())
hpnicfAcfpClientMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpClientMode.setStatus(_A)
_HpnicfAcfpClientRowStatus_Type=RowStatus
_HpnicfAcfpClientRowStatus_Object=MibTableColumn
hpnicfAcfpClientRowStatus=_HpnicfAcfpClientRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,2,1,1,8),_HpnicfAcfpClientRowStatus_Type())
hpnicfAcfpClientRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpClientRowStatus.setStatus(_A)
_HpnicfAcfpPolicy_ObjectIdentity=ObjectIdentity
hpnicfAcfpPolicy=_HpnicfAcfpPolicy_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3))
_HpnicfAcfpPolicyTable_Object=MibTable
hpnicfAcfpPolicyTable=_HpnicfAcfpPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1))
if mibBuilder.loadTexts:hpnicfAcfpPolicyTable.setStatus(_A)
_HpnicfAcfpPolicyEntry_Object=MibTableRow
hpnicfAcfpPolicyEntry=_HpnicfAcfpPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1))
hpnicfAcfpPolicyEntry.setIndexNames((0,_D,_E),(0,_D,_O))
if mibBuilder.loadTexts:hpnicfAcfpPolicyEntry.setStatus(_A)
class _HpnicfAcfpPolicyIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfAcfpPolicyIndex_Type.__name__=_C
_HpnicfAcfpPolicyIndex_Object=MibTableColumn
hpnicfAcfpPolicyIndex=_HpnicfAcfpPolicyIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,1),_HpnicfAcfpPolicyIndex_Type())
hpnicfAcfpPolicyIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfAcfpPolicyIndex.setStatus(_A)
class _HpnicfAcfpPolicyInIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfAcfpPolicyInIfIndex_Type.__name__=_C
_HpnicfAcfpPolicyInIfIndex_Object=MibTableColumn
hpnicfAcfpPolicyInIfIndex=_HpnicfAcfpPolicyInIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,2),_HpnicfAcfpPolicyInIfIndex_Type())
hpnicfAcfpPolicyInIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyInIfIndex.setStatus(_A)
class _HpnicfAcfpPolicyOutIfIndex_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfAcfpPolicyOutIfIndex_Type.__name__=_C
_HpnicfAcfpPolicyOutIfIndex_Object=MibTableColumn
hpnicfAcfpPolicyOutIfIndex=_HpnicfAcfpPolicyOutIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,3),_HpnicfAcfpPolicyOutIfIndex_Type())
hpnicfAcfpPolicyOutIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyOutIfIndex.setStatus(_A)
class _HpnicfAcfpPolicyDestIfIndex_Type(Integer32):defaultValue=0
_HpnicfAcfpPolicyDestIfIndex_Type.__name__=_C
_HpnicfAcfpPolicyDestIfIndex_Object=MibTableColumn
hpnicfAcfpPolicyDestIfIndex=_HpnicfAcfpPolicyDestIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,4),_HpnicfAcfpPolicyDestIfIndex_Type())
hpnicfAcfpPolicyDestIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyDestIfIndex.setStatus(_A)
class _HpnicfAcfpPolicyContextID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfAcfpPolicyContextID_Type.__name__=_C
_HpnicfAcfpPolicyContextID_Object=MibTableColumn
hpnicfAcfpPolicyContextID=_HpnicfAcfpPolicyContextID_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,5),_HpnicfAcfpPolicyContextID_Type())
hpnicfAcfpPolicyContextID.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfAcfpPolicyContextID.setStatus(_A)
class _HpnicfAcfpPolicyAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_HpnicfAcfpPolicyAdminStatus_Type.__name__=_C
_HpnicfAcfpPolicyAdminStatus_Object=MibTableColumn
hpnicfAcfpPolicyAdminStatus=_HpnicfAcfpPolicyAdminStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,6),_HpnicfAcfpPolicyAdminStatus_Type())
hpnicfAcfpPolicyAdminStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyAdminStatus.setStatus(_A)
class _HpnicfAcfpPolicyLifetime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_HpnicfAcfpPolicyLifetime_Type.__name__=_C
_HpnicfAcfpPolicyLifetime_Object=MibTableColumn
hpnicfAcfpPolicyLifetime=_HpnicfAcfpPolicyLifetime_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,7),_HpnicfAcfpPolicyLifetime_Type())
hpnicfAcfpPolicyLifetime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyLifetime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfAcfpPolicyLifetime.setUnits(_S)
class _HpnicfAcfpPolicyTimeStart_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfAcfpPolicyTimeStart_Type.__name__=_K
_HpnicfAcfpPolicyTimeStart_Object=MibTableColumn
hpnicfAcfpPolicyTimeStart=_HpnicfAcfpPolicyTimeStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,8),_HpnicfAcfpPolicyTimeStart_Type())
hpnicfAcfpPolicyTimeStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyTimeStart.setStatus(_A)
class _HpnicfAcfpPolicyTimeEnd_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_HpnicfAcfpPolicyTimeEnd_Type.__name__=_K
_HpnicfAcfpPolicyTimeEnd_Object=MibTableColumn
hpnicfAcfpPolicyTimeEnd=_HpnicfAcfpPolicyTimeEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,9),_HpnicfAcfpPolicyTimeEnd_Type())
hpnicfAcfpPolicyTimeEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyTimeEnd.setStatus(_A)
_HpnicfAcfpPolicyRowStatus_Type=RowStatus
_HpnicfAcfpPolicyRowStatus_Object=MibTableColumn
hpnicfAcfpPolicyRowStatus=_HpnicfAcfpPolicyRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,10),_HpnicfAcfpPolicyRowStatus_Type())
hpnicfAcfpPolicyRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyRowStatus.setStatus(_A)
class _HpnicfAcfpPolicyDestIfFailAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('delete',1),('reserve',2)))
_HpnicfAcfpPolicyDestIfFailAction_Type.__name__=_C
_HpnicfAcfpPolicyDestIfFailAction_Object=MibTableColumn
hpnicfAcfpPolicyDestIfFailAction=_HpnicfAcfpPolicyDestIfFailAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,11),_HpnicfAcfpPolicyDestIfFailAction_Type())
hpnicfAcfpPolicyDestIfFailAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyDestIfFailAction.setStatus(_A)
class _HpnicfAcfpPolicyPriority_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('priority1',1),('priority2',2),('priority3',3),('priority4',4),('priority5',5),('priority6',6),('priority7',7),('priority8',8)))
_HpnicfAcfpPolicyPriority_Type.__name__=_C
_HpnicfAcfpPolicyPriority_Object=MibTableColumn
hpnicfAcfpPolicyPriority=_HpnicfAcfpPolicyPriority_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,3,1,1,12),_HpnicfAcfpPolicyPriority_Type())
hpnicfAcfpPolicyPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpPolicyPriority.setStatus(_A)
_HpnicfAcfpRule_ObjectIdentity=ObjectIdentity
hpnicfAcfpRule=_HpnicfAcfpRule_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4))
_HpnicfAcfpRuleTable_Object=MibTable
hpnicfAcfpRuleTable=_HpnicfAcfpRuleTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1))
if mibBuilder.loadTexts:hpnicfAcfpRuleTable.setStatus(_A)
_HpnicfAcfpRuleEntry_Object=MibTableRow
hpnicfAcfpRuleEntry=_HpnicfAcfpRuleEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1))
hpnicfAcfpRuleEntry.setIndexNames((0,_D,_E),(0,_D,_O),(0,_D,_H))
if mibBuilder.loadTexts:hpnicfAcfpRuleEntry.setStatus(_A)
class _HpnicfAcfpRuleIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HpnicfAcfpRuleIndex_Type.__name__=_C
_HpnicfAcfpRuleIndex_Object=MibTableColumn
hpnicfAcfpRuleIndex=_HpnicfAcfpRuleIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,1),_HpnicfAcfpRuleIndex_Type())
hpnicfAcfpRuleIndex.setMaxAccess(_N)
if mibBuilder.loadTexts:hpnicfAcfpRuleIndex.setStatus(_A)
class _HpnicfAcfpRuleOperStatus_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('success',1),('fail',2)))
_HpnicfAcfpRuleOperStatus_Type.__name__=_C
_HpnicfAcfpRuleOperStatus_Object=MibTableColumn
hpnicfAcfpRuleOperStatus=_HpnicfAcfpRuleOperStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,2),_HpnicfAcfpRuleOperStatus_Type())
hpnicfAcfpRuleOperStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfAcfpRuleOperStatus.setStatus(_A)
class _HpnicfAcfpRuleAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('permit',1),('deny',2),(_L,3),(_M,4),('rate',5)))
_HpnicfAcfpRuleAction_Type.__name__=_C
_HpnicfAcfpRuleAction_Object=MibTableColumn
hpnicfAcfpRuleAction=_HpnicfAcfpRuleAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,3),_HpnicfAcfpRuleAction_Type())
hpnicfAcfpRuleAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleAction.setStatus(_A)
class _HpnicfAcfpRuleAll_Type(TruthValue):defaultValue=2
_HpnicfAcfpRuleAll_Type.__name__=_J
_HpnicfAcfpRuleAll_Object=MibTableColumn
hpnicfAcfpRuleAll=_HpnicfAcfpRuleAll_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,4),_HpnicfAcfpRuleAll_Type())
hpnicfAcfpRuleAll.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleAll.setStatus(_A)
_HpnicfAcfpRuleSrcMAC_Type=MacAddress
_HpnicfAcfpRuleSrcMAC_Object=MibTableColumn
hpnicfAcfpRuleSrcMAC=_HpnicfAcfpRuleSrcMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,5),_HpnicfAcfpRuleSrcMAC_Type())
hpnicfAcfpRuleSrcMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcMAC.setStatus(_A)
_HpnicfAcfpRuleDstMAC_Type=MacAddress
_HpnicfAcfpRuleDstMAC_Object=MibTableColumn
hpnicfAcfpRuleDstMAC=_HpnicfAcfpRuleDstMAC_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,6),_HpnicfAcfpRuleDstMAC_Type())
hpnicfAcfpRuleDstMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstMAC.setStatus(_A)
class _HpnicfAcfpRuleVlanStart_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfAcfpRuleVlanStart_Type.__name__=_C
_HpnicfAcfpRuleVlanStart_Object=MibTableColumn
hpnicfAcfpRuleVlanStart=_HpnicfAcfpRuleVlanStart_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,7),_HpnicfAcfpRuleVlanStart_Type())
hpnicfAcfpRuleVlanStart.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleVlanStart.setStatus(_A)
class _HpnicfAcfpRuleVlanEnd_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4094))
_HpnicfAcfpRuleVlanEnd_Type.__name__=_C
_HpnicfAcfpRuleVlanEnd_Object=MibTableColumn
hpnicfAcfpRuleVlanEnd=_HpnicfAcfpRuleVlanEnd_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,8),_HpnicfAcfpRuleVlanEnd_Type())
hpnicfAcfpRuleVlanEnd.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleVlanEnd.setStatus(_A)
class _HpnicfAcfpRuleProtocol_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_HpnicfAcfpRuleProtocol_Type.__name__=_C
_HpnicfAcfpRuleProtocol_Object=MibTableColumn
hpnicfAcfpRuleProtocol=_HpnicfAcfpRuleProtocol_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,9),_HpnicfAcfpRuleProtocol_Type())
hpnicfAcfpRuleProtocol.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleProtocol.setStatus(_A)
_HpnicfAcfpRuleSrcIP_Type=IpAddress
_HpnicfAcfpRuleSrcIP_Object=MibTableColumn
hpnicfAcfpRuleSrcIP=_HpnicfAcfpRuleSrcIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,10),_HpnicfAcfpRuleSrcIP_Type())
hpnicfAcfpRuleSrcIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcIP.setStatus(_A)
_HpnicfAcfpRuleSrcIPMask_Type=IpAddress
_HpnicfAcfpRuleSrcIPMask_Object=MibTableColumn
hpnicfAcfpRuleSrcIPMask=_HpnicfAcfpRuleSrcIPMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,11),_HpnicfAcfpRuleSrcIPMask_Type())
hpnicfAcfpRuleSrcIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcIPMask.setStatus(_A)
class _HpnicfAcfpRuleSrcOp_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('equal',1),('notEqual',2),(_T,3),(_U,4),('range',5),(_V,6)))
_HpnicfAcfpRuleSrcOp_Type.__name__=_C
_HpnicfAcfpRuleSrcOp_Object=MibTableColumn
hpnicfAcfpRuleSrcOp=_HpnicfAcfpRuleSrcOp_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,12),_HpnicfAcfpRuleSrcOp_Type())
hpnicfAcfpRuleSrcOp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcOp.setStatus(_A)
class _HpnicfAcfpRuleSrcStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfAcfpRuleSrcStartPort_Type.__name__=_C
_HpnicfAcfpRuleSrcStartPort_Object=MibTableColumn
hpnicfAcfpRuleSrcStartPort=_HpnicfAcfpRuleSrcStartPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,13),_HpnicfAcfpRuleSrcStartPort_Type())
hpnicfAcfpRuleSrcStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcStartPort.setStatus(_A)
class _HpnicfAcfpRuleSrcEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfAcfpRuleSrcEndPort_Type.__name__=_C
_HpnicfAcfpRuleSrcEndPort_Object=MibTableColumn
hpnicfAcfpRuleSrcEndPort=_HpnicfAcfpRuleSrcEndPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,14),_HpnicfAcfpRuleSrcEndPort_Type())
hpnicfAcfpRuleSrcEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcEndPort.setStatus(_A)
_HpnicfAcfpRuleDstIP_Type=IpAddress
_HpnicfAcfpRuleDstIP_Object=MibTableColumn
hpnicfAcfpRuleDstIP=_HpnicfAcfpRuleDstIP_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,15),_HpnicfAcfpRuleDstIP_Type())
hpnicfAcfpRuleDstIP.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstIP.setStatus(_A)
_HpnicfAcfpRuleDstIPMask_Type=IpAddress
_HpnicfAcfpRuleDstIPMask_Object=MibTableColumn
hpnicfAcfpRuleDstIPMask=_HpnicfAcfpRuleDstIPMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,16),_HpnicfAcfpRuleDstIPMask_Type())
hpnicfAcfpRuleDstIPMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstIPMask.setStatus(_A)
class _HpnicfAcfpRuleDstOp_Type(Integer32):defaultValue=6;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('equal',1),('nonEqual',2),(_T,3),(_U,4),('range',5),(_V,6)))
_HpnicfAcfpRuleDstOp_Type.__name__=_C
_HpnicfAcfpRuleDstOp_Object=MibTableColumn
hpnicfAcfpRuleDstOp=_HpnicfAcfpRuleDstOp_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,17),_HpnicfAcfpRuleDstOp_Type())
hpnicfAcfpRuleDstOp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstOp.setStatus(_A)
class _HpnicfAcfpRuleDstStartPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfAcfpRuleDstStartPort_Type.__name__=_C
_HpnicfAcfpRuleDstStartPort_Object=MibTableColumn
hpnicfAcfpRuleDstStartPort=_HpnicfAcfpRuleDstStartPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,18),_HpnicfAcfpRuleDstStartPort_Type())
hpnicfAcfpRuleDstStartPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstStartPort.setStatus(_A)
class _HpnicfAcfpRuleDstEndPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfAcfpRuleDstEndPort_Type.__name__=_C
_HpnicfAcfpRuleDstEndPort_Object=MibTableColumn
hpnicfAcfpRuleDstEndPort=_HpnicfAcfpRuleDstEndPort_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,19),_HpnicfAcfpRuleDstEndPort_Type())
hpnicfAcfpRuleDstEndPort.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstEndPort.setStatus(_A)
class _HpnicfAcfpRulePrecedence_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_HpnicfAcfpRulePrecedence_Type.__name__=_C
_HpnicfAcfpRulePrecedence_Object=MibTableColumn
hpnicfAcfpRulePrecedence=_HpnicfAcfpRulePrecedence_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,20),_HpnicfAcfpRulePrecedence_Type())
hpnicfAcfpRulePrecedence.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRulePrecedence.setStatus(_A)
class _HpnicfAcfpRuleTos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,15),ValueRangeConstraint(255,255))
_HpnicfAcfpRuleTos_Type.__name__=_C
_HpnicfAcfpRuleTos_Object=MibTableColumn
hpnicfAcfpRuleTos=_HpnicfAcfpRuleTos_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,21),_HpnicfAcfpRuleTos_Type())
hpnicfAcfpRuleTos.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleTos.setStatus(_A)
class _HpnicfAcfpRuleDscp_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63),ValueRangeConstraint(255,255))
_HpnicfAcfpRuleDscp_Type.__name__=_C
_HpnicfAcfpRuleDscp_Object=MibTableColumn
hpnicfAcfpRuleDscp=_HpnicfAcfpRuleDscp_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,22),_HpnicfAcfpRuleDscp_Type())
hpnicfAcfpRuleDscp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDscp.setStatus(_A)
class _HpnicfAcfpRuleEstablish_Type(TruthValue):defaultValue=2
_HpnicfAcfpRuleEstablish_Type.__name__=_J
_HpnicfAcfpRuleEstablish_Object=MibTableColumn
hpnicfAcfpRuleEstablish=_HpnicfAcfpRuleEstablish_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,23),_HpnicfAcfpRuleEstablish_Type())
hpnicfAcfpRuleEstablish.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleEstablish.setStatus('deprecated')
class _HpnicfAcfpRuleFragment_Type(TruthValue):defaultValue=2
_HpnicfAcfpRuleFragment_Type.__name__=_J
_HpnicfAcfpRuleFragment_Object=MibTableColumn
hpnicfAcfpRuleFragment=_HpnicfAcfpRuleFragment_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,24),_HpnicfAcfpRuleFragment_Type())
hpnicfAcfpRuleFragment.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleFragment.setStatus(_A)
_HpnicfAcfpRulePacketRate_Type=Integer32
_HpnicfAcfpRulePacketRate_Object=MibTableColumn
hpnicfAcfpRulePacketRate=_HpnicfAcfpRulePacketRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,25),_HpnicfAcfpRulePacketRate_Type())
hpnicfAcfpRulePacketRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRulePacketRate.setStatus(_A)
_HpnicfAcfpRuleRowStatus_Type=RowStatus
_HpnicfAcfpRuleRowStatus_Object=MibTableColumn
hpnicfAcfpRuleRowStatus=_HpnicfAcfpRuleRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,26),_HpnicfAcfpRuleRowStatus_Type())
hpnicfAcfpRuleRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleRowStatus.setStatus(_A)
class _HpnicfAcfpRuleTCPFlag_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfAcfpRuleTCPFlag_Type.__name__=_C
_HpnicfAcfpRuleTCPFlag_Object=MibTableColumn
hpnicfAcfpRuleTCPFlag=_HpnicfAcfpRuleTCPFlag_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,27),_HpnicfAcfpRuleTCPFlag_Type())
hpnicfAcfpRuleTCPFlag.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleTCPFlag.setStatus(_A)
_HpnicfAcfpRuleSrcIPV6Address_Type=Ipv6Address
_HpnicfAcfpRuleSrcIPV6Address_Object=MibTableColumn
hpnicfAcfpRuleSrcIPV6Address=_HpnicfAcfpRuleSrcIPV6Address_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,28),_HpnicfAcfpRuleSrcIPV6Address_Type())
hpnicfAcfpRuleSrcIPV6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcIPV6Address.setStatus(_A)
_HpnicfAcfpRuleSrcPrefixLen_Type=InetAddressPrefixLength
_HpnicfAcfpRuleSrcPrefixLen_Object=MibTableColumn
hpnicfAcfpRuleSrcPrefixLen=_HpnicfAcfpRuleSrcPrefixLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,29),_HpnicfAcfpRuleSrcPrefixLen_Type())
hpnicfAcfpRuleSrcPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleSrcPrefixLen.setStatus(_A)
_HpnicfAcfpRuleDstIPV6Address_Type=Ipv6Address
_HpnicfAcfpRuleDstIPV6Address_Object=MibTableColumn
hpnicfAcfpRuleDstIPV6Address=_HpnicfAcfpRuleDstIPV6Address_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,30),_HpnicfAcfpRuleDstIPV6Address_Type())
hpnicfAcfpRuleDstIPV6Address.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstIPV6Address.setStatus(_A)
_HpnicfAcfpRuleDstPrefixLen_Type=InetAddressPrefixLength
_HpnicfAcfpRuleDstPrefixLen_Object=MibTableColumn
hpnicfAcfpRuleDstPrefixLen=_HpnicfAcfpRuleDstPrefixLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,31),_HpnicfAcfpRuleDstPrefixLen_Type())
hpnicfAcfpRuleDstPrefixLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleDstPrefixLen.setStatus(_A)
class _HpnicfAcfpRuleTrafficType_Type(Bits):namedValues=NamedValues(*(('unicast',0),('multicast',1),('broadcast',2)))
_HpnicfAcfpRuleTrafficType_Type.__name__=_I
_HpnicfAcfpRuleTrafficType_Object=MibTableColumn
hpnicfAcfpRuleTrafficType=_HpnicfAcfpRuleTrafficType_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,32),_HpnicfAcfpRuleTrafficType_Type())
hpnicfAcfpRuleTrafficType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleTrafficType.setStatus(_A)
class _HpnicfAcfpRuleTypeOrLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_HpnicfAcfpRuleTypeOrLen_Type.__name__=_C
_HpnicfAcfpRuleTypeOrLen_Object=MibTableColumn
hpnicfAcfpRuleTypeOrLen=_HpnicfAcfpRuleTypeOrLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,4,1,1,33),_HpnicfAcfpRuleTypeOrLen_Type())
hpnicfAcfpRuleTypeOrLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfAcfpRuleTypeOrLen.setStatus(_A)
_HpnicfAcfpNotifications_ObjectIdentity=ObjectIdentity
hpnicfAcfpNotifications=_HpnicfAcfpNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5))
hpnicfAcfpCurContextChanged=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,1))
hpnicfAcfpCurContextChanged.setObjects((_D,_W))
if mibBuilder.loadTexts:hpnicfAcfpCurContextChanged.setStatus(_A)
hpnicfAcfpClientRegister=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,2))
hpnicfAcfpClientRegister.setObjects((_D,_E))
if mibBuilder.loadTexts:hpnicfAcfpClientRegister.setStatus(_A)
hpnicfAcfpClientUnRegister=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,3))
hpnicfAcfpClientUnRegister.setObjects((_D,_E))
if mibBuilder.loadTexts:hpnicfAcfpClientUnRegister.setStatus(_A)
hpnicfAcfpClientDead=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,4))
hpnicfAcfpClientDead.setObjects((_D,_E))
if mibBuilder.loadTexts:hpnicfAcfpClientDead.setStatus(_A)
hpnicfAcfpNotSupportedOAPMode=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,5))
hpnicfAcfpNotSupportedOAPMode.setObjects(*((_D,_E),(_D,_X),(_D,_Y)))
if mibBuilder.loadTexts:hpnicfAcfpNotSupportedOAPMode.setStatus(_A)
hpnicfAcfpLifetimeChangeEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,6))
hpnicfAcfpLifetimeChangeEvent.setObjects((_D,_P))
if mibBuilder.loadTexts:hpnicfAcfpLifetimeChangeEvent.setStatus(_A)
hpnicfAcfpRuleCreatedEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,7))
hpnicfAcfpRuleCreatedEvent.setObjects((_D,_H))
if mibBuilder.loadTexts:hpnicfAcfpRuleCreatedEvent.setStatus(_A)
hpnicfAcfpRuleDeletedEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,8))
hpnicfAcfpRuleDeletedEvent.setObjects((_D,_H))
if mibBuilder.loadTexts:hpnicfAcfpRuleDeletedEvent.setStatus(_A)
hpnicfAcfpRuleErrorEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,9))
hpnicfAcfpRuleErrorEvent.setObjects((_D,_H))
if mibBuilder.loadTexts:hpnicfAcfpRuleErrorEvent.setStatus(_A)
hpnicfAcfpLifetimeExpireEvent=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,74,1,1,5,10))
hpnicfAcfpLifetimeExpireEvent.setObjects((_D,_P))
if mibBuilder.loadTexts:hpnicfAcfpLifetimeExpireEvent.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpnicfAcfp':hpnicfAcfp,'hpnicfAcfpObjects':hpnicfAcfpObjects,'hpnicfAcfpOAP':hpnicfAcfpOAP,'hpnicfAcfpServer':hpnicfAcfpServer,_Y:hpnicfAcfpServerInfo,'hpnicfAcfpServerMaxLifetime':hpnicfAcfpServerMaxLifetime,'hpnicfAcfpServerPersistentRules':hpnicfAcfpServerPersistentRules,_W:hpnicfAcfpServerCurContextType,'hpnicfAcfpClientInfo':hpnicfAcfpClientInfo,'hpnicfAcfpClientInfoTable':hpnicfAcfpClientInfoTable,'hpnicfAcfpClientInfoEntry':hpnicfAcfpClientInfoEntry,_E:hpnicfAcfpClientID,'hpnicfAcfpClientDescription':hpnicfAcfpClientDescription,'hpnicfAcfpClientHwVersion':hpnicfAcfpClientHwVersion,'hpnicfAcfpClientOSVersion':hpnicfAcfpClientOSVersion,'hpnicfAcfpClientAppVersion':hpnicfAcfpClientAppVersion,'hpnicfAcfpClientIP':hpnicfAcfpClientIP,_X:hpnicfAcfpClientMode,'hpnicfAcfpClientRowStatus':hpnicfAcfpClientRowStatus,'hpnicfAcfpPolicy':hpnicfAcfpPolicy,'hpnicfAcfpPolicyTable':hpnicfAcfpPolicyTable,'hpnicfAcfpPolicyEntry':hpnicfAcfpPolicyEntry,_O:hpnicfAcfpPolicyIndex,'hpnicfAcfpPolicyInIfIndex':hpnicfAcfpPolicyInIfIndex,'hpnicfAcfpPolicyOutIfIndex':hpnicfAcfpPolicyOutIfIndex,'hpnicfAcfpPolicyDestIfIndex':hpnicfAcfpPolicyDestIfIndex,'hpnicfAcfpPolicyContextID':hpnicfAcfpPolicyContextID,'hpnicfAcfpPolicyAdminStatus':hpnicfAcfpPolicyAdminStatus,_P:hpnicfAcfpPolicyLifetime,'hpnicfAcfpPolicyTimeStart':hpnicfAcfpPolicyTimeStart,'hpnicfAcfpPolicyTimeEnd':hpnicfAcfpPolicyTimeEnd,'hpnicfAcfpPolicyRowStatus':hpnicfAcfpPolicyRowStatus,'hpnicfAcfpPolicyDestIfFailAction':hpnicfAcfpPolicyDestIfFailAction,'hpnicfAcfpPolicyPriority':hpnicfAcfpPolicyPriority,'hpnicfAcfpRule':hpnicfAcfpRule,'hpnicfAcfpRuleTable':hpnicfAcfpRuleTable,'hpnicfAcfpRuleEntry':hpnicfAcfpRuleEntry,_H:hpnicfAcfpRuleIndex,'hpnicfAcfpRuleOperStatus':hpnicfAcfpRuleOperStatus,'hpnicfAcfpRuleAction':hpnicfAcfpRuleAction,'hpnicfAcfpRuleAll':hpnicfAcfpRuleAll,'hpnicfAcfpRuleSrcMAC':hpnicfAcfpRuleSrcMAC,'hpnicfAcfpRuleDstMAC':hpnicfAcfpRuleDstMAC,'hpnicfAcfpRuleVlanStart':hpnicfAcfpRuleVlanStart,'hpnicfAcfpRuleVlanEnd':hpnicfAcfpRuleVlanEnd,'hpnicfAcfpRuleProtocol':hpnicfAcfpRuleProtocol,'hpnicfAcfpRuleSrcIP':hpnicfAcfpRuleSrcIP,'hpnicfAcfpRuleSrcIPMask':hpnicfAcfpRuleSrcIPMask,'hpnicfAcfpRuleSrcOp':hpnicfAcfpRuleSrcOp,'hpnicfAcfpRuleSrcStartPort':hpnicfAcfpRuleSrcStartPort,'hpnicfAcfpRuleSrcEndPort':hpnicfAcfpRuleSrcEndPort,'hpnicfAcfpRuleDstIP':hpnicfAcfpRuleDstIP,'hpnicfAcfpRuleDstIPMask':hpnicfAcfpRuleDstIPMask,'hpnicfAcfpRuleDstOp':hpnicfAcfpRuleDstOp,'hpnicfAcfpRuleDstStartPort':hpnicfAcfpRuleDstStartPort,'hpnicfAcfpRuleDstEndPort':hpnicfAcfpRuleDstEndPort,'hpnicfAcfpRulePrecedence':hpnicfAcfpRulePrecedence,'hpnicfAcfpRuleTos':hpnicfAcfpRuleTos,'hpnicfAcfpRuleDscp':hpnicfAcfpRuleDscp,'hpnicfAcfpRuleEstablish':hpnicfAcfpRuleEstablish,'hpnicfAcfpRuleFragment':hpnicfAcfpRuleFragment,'hpnicfAcfpRulePacketRate':hpnicfAcfpRulePacketRate,'hpnicfAcfpRuleRowStatus':hpnicfAcfpRuleRowStatus,'hpnicfAcfpRuleTCPFlag':hpnicfAcfpRuleTCPFlag,'hpnicfAcfpRuleSrcIPV6Address':hpnicfAcfpRuleSrcIPV6Address,'hpnicfAcfpRuleSrcPrefixLen':hpnicfAcfpRuleSrcPrefixLen,'hpnicfAcfpRuleDstIPV6Address':hpnicfAcfpRuleDstIPV6Address,'hpnicfAcfpRuleDstPrefixLen':hpnicfAcfpRuleDstPrefixLen,'hpnicfAcfpRuleTrafficType':hpnicfAcfpRuleTrafficType,'hpnicfAcfpRuleTypeOrLen':hpnicfAcfpRuleTypeOrLen,'hpnicfAcfpNotifications':hpnicfAcfpNotifications,'hpnicfAcfpCurContextChanged':hpnicfAcfpCurContextChanged,'hpnicfAcfpClientRegister':hpnicfAcfpClientRegister,'hpnicfAcfpClientUnRegister':hpnicfAcfpClientUnRegister,'hpnicfAcfpClientDead':hpnicfAcfpClientDead,'hpnicfAcfpNotSupportedOAPMode':hpnicfAcfpNotSupportedOAPMode,'hpnicfAcfpLifetimeChangeEvent':hpnicfAcfpLifetimeChangeEvent,'hpnicfAcfpRuleCreatedEvent':hpnicfAcfpRuleCreatedEvent,'hpnicfAcfpRuleDeletedEvent':hpnicfAcfpRuleDeletedEvent,'hpnicfAcfpRuleErrorEvent':hpnicfAcfpRuleErrorEvent,'hpnicfAcfpLifetimeExpireEvent':hpnicfAcfpLifetimeExpireEvent})