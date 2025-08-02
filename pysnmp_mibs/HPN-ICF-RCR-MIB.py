_U='hpnicfRcrCRAdjuPrefPreOutIfName'
_T='hpnicfRcrCRAdjuPrefPreMRName'
_S='hpnicfRcrCRAdjuPrefMaskLen'
_R='hpnicfRcrCRAdjuPrefDestAddr'
_Q='hpnicfRcrCRAdjuPrefDestAddrType'
_P='hpnicfRcrCRMatPrefPerfDestMaskLen'
_O='hpnicfRcrCRMatPrefPerfDestIPAddr'
_N='hpnicfRcrCRMatPrefPerfAddrType'
_M='hpnicfRcrCRRcrPlyID'
_L='hpnicfRcrMROutIfName'
_K='down'
_J='hpnicfRcrMRName'
_I='second'
_H='%'
_G='OctetString'
_F='read-only'
_E='not-accessible'
_D='HPN-ICF-RCR-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_G,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfRcr=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,48))
if mibBuilder.loadTexts:hpnicfRcr.setRevisions(('2005-06-28 19:36',))
_HpnicfRcrMR_ObjectIdentity=ObjectIdentity
hpnicfRcrMR=_HpnicfRcrMR_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,48,1))
_HpnicfRcrMRGroup_ObjectIdentity=ObjectIdentity
hpnicfRcrMRGroup=_HpnicfRcrMRGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,48,1,1))
class _HpnicfRcrMRAllMaxUsedBandRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfRcrMRAllMaxUsedBandRate_Type.__name__=_B
_HpnicfRcrMRAllMaxUsedBandRate_Object=MibScalar
hpnicfRcrMRAllMaxUsedBandRate=_HpnicfRcrMRAllMaxUsedBandRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,1,1),_HpnicfRcrMRAllMaxUsedBandRate_Type())
hpnicfRcrMRAllMaxUsedBandRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrMRAllMaxUsedBandRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrMRAllMaxUsedBandRate.setUnits(_H)
class _HpnicfRcrMRAllMinUsedBandRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfRcrMRAllMinUsedBandRate_Type.__name__=_B
_HpnicfRcrMRAllMinUsedBandRate_Object=MibScalar
hpnicfRcrMRAllMinUsedBandRate=_HpnicfRcrMRAllMinUsedBandRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,1,2),_HpnicfRcrMRAllMinUsedBandRate_Type())
hpnicfRcrMRAllMinUsedBandRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrMRAllMinUsedBandRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrMRAllMinUsedBandRate.setUnits(_H)
class _HpnicfRcrMRListenTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1440))
_HpnicfRcrMRListenTime_Type.__name__=_B
_HpnicfRcrMRListenTime_Object=MibScalar
hpnicfRcrMRListenTime=_HpnicfRcrMRListenTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,1,3),_HpnicfRcrMRListenTime_Type())
hpnicfRcrMRListenTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrMRListenTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrMRListenTime.setUnits('minute')
_HpnicfRcrMRStateTable_Object=MibTable
hpnicfRcrMRStateTable=_HpnicfRcrMRStateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,2))
if mibBuilder.loadTexts:hpnicfRcrMRStateTable.setStatus(_A)
_HpnicfRcrMRStateEntry_Object=MibTableRow
hpnicfRcrMRStateEntry=_HpnicfRcrMRStateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,2,1))
hpnicfRcrMRStateEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpnicfRcrMRStateEntry.setStatus(_A)
class _HpnicfRcrMRName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfRcrMRName_Type.__name__=_G
_HpnicfRcrMRName_Object=MibTableColumn
hpnicfRcrMRName=_HpnicfRcrMRName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,2,1,1),_HpnicfRcrMRName_Type())
hpnicfRcrMRName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrMRName.setStatus(_A)
class _HpnicfRcrMRState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('up',2),('controlled',3)))
_HpnicfRcrMRState_Type.__name__=_B
_HpnicfRcrMRState_Object=MibTableColumn
hpnicfRcrMRState=_HpnicfRcrMRState_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,2,1,2),_HpnicfRcrMRState_Type())
hpnicfRcrMRState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrMRState.setStatus(_A)
class _HpnicfRcrMRAuthType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('simple',1),('md5',2)))
_HpnicfRcrMRAuthType_Type.__name__=_B
_HpnicfRcrMRAuthType_Object=MibTableColumn
hpnicfRcrMRAuthType=_HpnicfRcrMRAuthType_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,2,1,3),_HpnicfRcrMRAuthType_Type())
hpnicfRcrMRAuthType.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrMRAuthType.setStatus(_A)
_HpnicfRcrMRAuthPwd_Type=OctetString
_HpnicfRcrMRAuthPwd_Object=MibTableColumn
hpnicfRcrMRAuthPwd=_HpnicfRcrMRAuthPwd_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,2,1,4),_HpnicfRcrMRAuthPwd_Type())
hpnicfRcrMRAuthPwd.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrMRAuthPwd.setStatus(_A)
_HpnicfRcrMROutIfStateTable_Object=MibTable
hpnicfRcrMROutIfStateTable=_HpnicfRcrMROutIfStateTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,3))
if mibBuilder.loadTexts:hpnicfRcrMROutIfStateTable.setStatus(_A)
_HpnicfRcrMROutIfStateEntry_Object=MibTableRow
hpnicfRcrMROutIfStateEntry=_HpnicfRcrMROutIfStateEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,3,1))
hpnicfRcrMROutIfStateEntry.setIndexNames((0,_D,_J),(0,_D,_L))
if mibBuilder.loadTexts:hpnicfRcrMROutIfStateEntry.setStatus(_A)
class _HpnicfRcrMROutIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_HpnicfRcrMROutIfName_Type.__name__=_G
_HpnicfRcrMROutIfName_Object=MibTableColumn
hpnicfRcrMROutIfName=_HpnicfRcrMROutIfName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,3,1,1),_HpnicfRcrMROutIfName_Type())
hpnicfRcrMROutIfName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrMROutIfName.setStatus(_A)
class _HpnicfRcrMROutIfState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('up',2),('notExist',3)))
_HpnicfRcrMROutIfState_Type.__name__=_B
_HpnicfRcrMROutIfState_Object=MibTableColumn
hpnicfRcrMROutIfState=_HpnicfRcrMROutIfState_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,3,1,2),_HpnicfRcrMROutIfState_Type())
hpnicfRcrMROutIfState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrMROutIfState.setStatus(_A)
class _HpnicfRcrMROutIfMaxUsedBandRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfRcrMROutIfMaxUsedBandRate_Type.__name__=_B
_HpnicfRcrMROutIfMaxUsedBandRate_Object=MibTableColumn
hpnicfRcrMROutIfMaxUsedBandRate=_HpnicfRcrMROutIfMaxUsedBandRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,3,1,3),_HpnicfRcrMROutIfMaxUsedBandRate_Type())
hpnicfRcrMROutIfMaxUsedBandRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrMROutIfMaxUsedBandRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrMROutIfMaxUsedBandRate.setUnits(_H)
class _HpnicfRcrMROutIfMinUsedBandRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfRcrMROutIfMinUsedBandRate_Type.__name__=_B
_HpnicfRcrMROutIfMinUsedBandRate_Object=MibTableColumn
hpnicfRcrMROutIfMinUsedBandRate=_HpnicfRcrMROutIfMinUsedBandRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,3,1,4),_HpnicfRcrMROutIfMinUsedBandRate_Type())
hpnicfRcrMROutIfMinUsedBandRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrMROutIfMinUsedBandRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrMROutIfMinUsedBandRate.setUnits(_H)
class _HpnicfRcrMROutIfUsedBandRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_HpnicfRcrMROutIfUsedBandRate_Type.__name__=_B
_HpnicfRcrMROutIfUsedBandRate_Object=MibTableColumn
hpnicfRcrMROutIfUsedBandRate=_HpnicfRcrMROutIfUsedBandRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,1,3,1,5),_HpnicfRcrMROutIfUsedBandRate_Type())
hpnicfRcrMROutIfUsedBandRate.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrMROutIfUsedBandRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrMROutIfUsedBandRate.setUnits(_H)
_HpnicfRcrCR_ObjectIdentity=ObjectIdentity
hpnicfRcrCR=_HpnicfRcrCR_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,48,2))
_HpnicfRcrCRGroup_ObjectIdentity=ObjectIdentity
hpnicfRcrCRGroup=_HpnicfRcrCRGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1))
class _HpnicfRcrCRState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('init',2),('active',3)))
_HpnicfRcrCRState_Type.__name__=_B
_HpnicfRcrCRState_Object=MibScalar
hpnicfRcrCRState=_HpnicfRcrCRState_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,1),_HpnicfRcrCRState_Type())
hpnicfRcrCRState.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRState.setStatus(_A)
_HpnicfRcrCRPortNum_Type=Integer32
_HpnicfRcrCRPortNum_Object=MibScalar
hpnicfRcrCRPortNum=_HpnicfRcrCRPortNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,2),_HpnicfRcrCRPortNum_Type())
hpnicfRcrCRPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRPortNum.setStatus(_A)
class _HpnicfRcrCRCtrlMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('control',1),('observe',2)))
_HpnicfRcrCRCtrlMode_Type.__name__=_B
_HpnicfRcrCRCtrlMode_Object=MibScalar
hpnicfRcrCRCtrlMode=_HpnicfRcrCRCtrlMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,3),_HpnicfRcrCRCtrlMode_Type())
hpnicfRcrCRCtrlMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRCtrlMode.setStatus(_A)
class _HpnicfRcrCRChooseMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('good',1),('best',2)))
_HpnicfRcrCRChooseMode_Type.__name__=_B
_HpnicfRcrCRChooseMode_Object=MibScalar
hpnicfRcrCRChooseMode=_HpnicfRcrCRChooseMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,4),_HpnicfRcrCRChooseMode_Type())
hpnicfRcrCRChooseMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRChooseMode.setStatus(_A)
class _HpnicfRcrCRKeepaliveTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_HpnicfRcrCRKeepaliveTime_Type.__name__=_B
_HpnicfRcrCRKeepaliveTime_Object=MibScalar
hpnicfRcrCRKeepaliveTime=_HpnicfRcrCRKeepaliveTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,5),_HpnicfRcrCRKeepaliveTime_Type())
hpnicfRcrCRKeepaliveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRKeepaliveTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRKeepaliveTime.setUnits(_I)
class _HpnicfRcrCRPolicyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('prefix',1),('operation',2),('study',3)))
_HpnicfRcrCRPolicyMode_Type.__name__=_B
_HpnicfRcrCRPolicyMode_Object=MibScalar
hpnicfRcrCRPolicyMode=_HpnicfRcrCRPolicyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,6),_HpnicfRcrCRPolicyMode_Type())
hpnicfRcrCRPolicyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRPolicyMode.setStatus(_A)
class _HpnicfRcrCRStudyMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('maxThoughout',1),('maxDelay',2)))
_HpnicfRcrCRStudyMode_Type.__name__=_B
_HpnicfRcrCRStudyMode_Object=MibScalar
hpnicfRcrCRStudyMode=_HpnicfRcrCRStudyMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,7),_HpnicfRcrCRStudyMode_Type())
hpnicfRcrCRStudyMode.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRStudyMode.setStatus(_A)
class _HpnicfRcrCRStudyIpPrefixNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2500))
_HpnicfRcrCRStudyIpPrefixNum_Type.__name__=_B
_HpnicfRcrCRStudyIpPrefixNum_Object=MibScalar
hpnicfRcrCRStudyIpPrefixNum=_HpnicfRcrCRStudyIpPrefixNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,8),_HpnicfRcrCRStudyIpPrefixNum_Type())
hpnicfRcrCRStudyIpPrefixNum.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRStudyIpPrefixNum.setStatus(_A)
class _HpnicfRcrCRIpPrefixLen_Type(Integer32):defaultValue=24;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_HpnicfRcrCRIpPrefixLen_Type.__name__=_B
_HpnicfRcrCRIpPrefixLen_Object=MibScalar
hpnicfRcrCRIpPrefixLen=_HpnicfRcrCRIpPrefixLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,1,9),_HpnicfRcrCRIpPrefixLen_Type())
hpnicfRcrCRIpPrefixLen.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRIpPrefixLen.setStatus(_A)
_HpnicfRcrCRRcrPolicyTable_Object=MibTable
hpnicfRcrCRRcrPolicyTable=_HpnicfRcrCRRcrPolicyTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2))
if mibBuilder.loadTexts:hpnicfRcrCRRcrPolicyTable.setStatus(_A)
_HpnicfRcrCRRcrPolicyEntry_Object=MibTableRow
hpnicfRcrCRRcrPolicyEntry=_HpnicfRcrCRRcrPolicyEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1))
hpnicfRcrCRRcrPolicyEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:hpnicfRcrCRRcrPolicyEntry.setStatus(_A)
_HpnicfRcrCRRcrPlyID_Type=Integer32
_HpnicfRcrCRRcrPlyID_Object=MibTableColumn
hpnicfRcrCRRcrPlyID=_HpnicfRcrCRRcrPlyID_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1,1),_HpnicfRcrCRRcrPlyID_Type())
hpnicfRcrCRRcrPlyID.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyID.setStatus(_A)
class _HpnicfRcrCRRcrPlyMatchIPListName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_HpnicfRcrCRRcrPlyMatchIPListName_Type.__name__=_G
_HpnicfRcrCRRcrPlyMatchIPListName_Object=MibTableColumn
hpnicfRcrCRRcrPlyMatchIPListName=_HpnicfRcrCRRcrPlyMatchIPListName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1,2),_HpnicfRcrCRRcrPlyMatchIPListName_Type())
hpnicfRcrCRRcrPlyMatchIPListName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyMatchIPListName.setStatus(_A)
class _HpnicfRcrCRRcrPlyMatchStudyEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disable',1),('enable',2)))
_HpnicfRcrCRRcrPlyMatchStudyEnable_Type.__name__=_B
_HpnicfRcrCRRcrPlyMatchStudyEnable_Object=MibTableColumn
hpnicfRcrCRRcrPlyMatchStudyEnable=_HpnicfRcrCRRcrPlyMatchStudyEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1,3),_HpnicfRcrCRRcrPlyMatchStudyEnable_Type())
hpnicfRcrCRRcrPlyMatchStudyEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyMatchStudyEnable.setStatus(_A)
class _HpnicfRcrCRRcrPlyMatchOperPlyName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,19))
_HpnicfRcrCRRcrPlyMatchOperPlyName_Type.__name__=_G
_HpnicfRcrCRRcrPlyMatchOperPlyName_Object=MibTableColumn
hpnicfRcrCRRcrPlyMatchOperPlyName=_HpnicfRcrCRRcrPlyMatchOperPlyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1,4),_HpnicfRcrCRRcrPlyMatchOperPlyName_Type())
hpnicfRcrCRRcrPlyMatchOperPlyName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyMatchOperPlyName.setStatus(_A)
class _HpnicfRcrCRRcrAclNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(3000,3999))
_HpnicfRcrCRRcrAclNumber_Type.__name__=_B
_HpnicfRcrCRRcrAclNumber_Object=MibTableColumn
hpnicfRcrCRRcrAclNumber=_HpnicfRcrCRRcrAclNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1,5),_HpnicfRcrCRRcrAclNumber_Type())
hpnicfRcrCRRcrAclNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRRcrAclNumber.setStatus(_A)
class _HpnicfRcrCRRcrPlyDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_HpnicfRcrCRRcrPlyDelayTime_Type.__name__=_B
_HpnicfRcrCRRcrPlyDelayTime_Object=MibTableColumn
hpnicfRcrCRRcrPlyDelayTime=_HpnicfRcrCRRcrPlyDelayTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1,6),_HpnicfRcrCRRcrPlyDelayTime_Type())
hpnicfRcrCRRcrPlyDelayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyDelayTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyDelayTime.setUnits('millisecond')
class _HpnicfRcrCRRcrPlyLossRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfRcrCRRcrPlyLossRate_Type.__name__=_B
_HpnicfRcrCRRcrPlyLossRate_Object=MibTableColumn
hpnicfRcrCRRcrPlyLossRate=_HpnicfRcrCRRcrPlyLossRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,2,1,7),_HpnicfRcrCRRcrPlyLossRate_Type())
hpnicfRcrCRRcrPlyLossRate.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyLossRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRRcrPlyLossRate.setUnits(_H)
_HpnicfRcrCRMatPrefixPerfTable_Object=MibTable
hpnicfRcrCRMatPrefixPerfTable=_HpnicfRcrCRMatPrefixPerfTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3))
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefixPerfTable.setStatus(_A)
_HpnicfRcrCRMatPrefixPerfEntry_Object=MibTableRow
hpnicfRcrCRMatPrefixPerfEntry=_HpnicfRcrCRMatPrefixPerfEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3,1))
hpnicfRcrCRMatPrefixPerfEntry.setIndexNames((0,_D,_N),(0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefixPerfEntry.setStatus(_A)
_HpnicfRcrCRMatPrefPerfAddrType_Type=InetAddressType
_HpnicfRcrCRMatPrefPerfAddrType_Object=MibTableColumn
hpnicfRcrCRMatPrefPerfAddrType=_HpnicfRcrCRMatPrefPerfAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3,1,1),_HpnicfRcrCRMatPrefPerfAddrType_Type())
hpnicfRcrCRMatPrefPerfAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfAddrType.setStatus(_A)
_HpnicfRcrCRMatPrefPerfDestIPAddr_Type=InetAddress
_HpnicfRcrCRMatPrefPerfDestIPAddr_Object=MibTableColumn
hpnicfRcrCRMatPrefPerfDestIPAddr=_HpnicfRcrCRMatPrefPerfDestIPAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3,1,2),_HpnicfRcrCRMatPrefPerfDestIPAddr_Type())
hpnicfRcrCRMatPrefPerfDestIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfDestIPAddr.setStatus(_A)
class _HpnicfRcrCRMatPrefPerfDestMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HpnicfRcrCRMatPrefPerfDestMaskLen_Type.__name__=_B
_HpnicfRcrCRMatPrefPerfDestMaskLen_Object=MibTableColumn
hpnicfRcrCRMatPrefPerfDestMaskLen=_HpnicfRcrCRMatPrefPerfDestMaskLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3,1,3),_HpnicfRcrCRMatPrefPerfDestMaskLen_Type())
hpnicfRcrCRMatPrefPerfDestMaskLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfDestMaskLen.setStatus(_A)
class _HpnicfRcrCRMatPrefPerfDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10000))
_HpnicfRcrCRMatPrefPerfDelayTime_Type.__name__=_B
_HpnicfRcrCRMatPrefPerfDelayTime_Object=MibTableColumn
hpnicfRcrCRMatPrefPerfDelayTime=_HpnicfRcrCRMatPrefPerfDelayTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3,1,4),_HpnicfRcrCRMatPrefPerfDelayTime_Type())
hpnicfRcrCRMatPrefPerfDelayTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfDelayTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfDelayTime.setUnits(_I)
class _HpnicfRcrCRMatPrefPerfLossRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_HpnicfRcrCRMatPrefPerfLossRate_Type.__name__=_B
_HpnicfRcrCRMatPrefPerfLossRate_Object=MibTableColumn
hpnicfRcrCRMatPrefPerfLossRate=_HpnicfRcrCRMatPrefPerfLossRate_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3,1,5),_HpnicfRcrCRMatPrefPerfLossRate_Type())
hpnicfRcrCRMatPrefPerfLossRate.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfLossRate.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfLossRate.setUnits(_H)
_HpnicfRcrCRMatPrefPerfThroughput_Type=Integer32
_HpnicfRcrCRMatPrefPerfThroughput_Object=MibTableColumn
hpnicfRcrCRMatPrefPerfThroughput=_HpnicfRcrCRMatPrefPerfThroughput_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,3,1,6),_HpnicfRcrCRMatPrefPerfThroughput_Type())
hpnicfRcrCRMatPrefPerfThroughput.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfThroughput.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRMatPrefPerfThroughput.setUnits('kb')
_HpnicfRcrCRAdjustPrefixTable_Object=MibTable
hpnicfRcrCRAdjustPrefixTable=_HpnicfRcrCRAdjustPrefixTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4))
if mibBuilder.loadTexts:hpnicfRcrCRAdjustPrefixTable.setStatus(_A)
_HpnicfRcrCRAdjustPrefixEntry_Object=MibTableRow
hpnicfRcrCRAdjustPrefixEntry=_HpnicfRcrCRAdjustPrefixEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1))
hpnicfRcrCRAdjustPrefixEntry.setIndexNames((0,_D,_Q),(0,_D,_R),(0,_D,_S),(0,_D,_T),(0,_D,_U))
if mibBuilder.loadTexts:hpnicfRcrCRAdjustPrefixEntry.setStatus(_A)
_HpnicfRcrCRAdjuPrefDestAddrType_Type=InetAddressType
_HpnicfRcrCRAdjuPrefDestAddrType_Object=MibTableColumn
hpnicfRcrCRAdjuPrefDestAddrType=_HpnicfRcrCRAdjuPrefDestAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,1),_HpnicfRcrCRAdjuPrefDestAddrType_Type())
hpnicfRcrCRAdjuPrefDestAddrType.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefDestAddrType.setStatus(_A)
_HpnicfRcrCRAdjuPrefDestAddr_Type=InetAddress
_HpnicfRcrCRAdjuPrefDestAddr_Object=MibTableColumn
hpnicfRcrCRAdjuPrefDestAddr=_HpnicfRcrCRAdjuPrefDestAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,2),_HpnicfRcrCRAdjuPrefDestAddr_Type())
hpnicfRcrCRAdjuPrefDestAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefDestAddr.setStatus(_A)
class _HpnicfRcrCRAdjuPrefMaskLen_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_HpnicfRcrCRAdjuPrefMaskLen_Type.__name__=_B
_HpnicfRcrCRAdjuPrefMaskLen_Object=MibTableColumn
hpnicfRcrCRAdjuPrefMaskLen=_HpnicfRcrCRAdjuPrefMaskLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,3),_HpnicfRcrCRAdjuPrefMaskLen_Type())
hpnicfRcrCRAdjuPrefMaskLen.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefMaskLen.setStatus(_A)
class _HpnicfRcrCRAdjuPrefPreMRName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfRcrCRAdjuPrefPreMRName_Type.__name__=_G
_HpnicfRcrCRAdjuPrefPreMRName_Object=MibTableColumn
hpnicfRcrCRAdjuPrefPreMRName=_HpnicfRcrCRAdjuPrefPreMRName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,4),_HpnicfRcrCRAdjuPrefPreMRName_Type())
hpnicfRcrCRAdjuPrefPreMRName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefPreMRName.setStatus(_A)
class _HpnicfRcrCRAdjuPrefPreOutIfName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,48))
_HpnicfRcrCRAdjuPrefPreOutIfName_Type.__name__=_G
_HpnicfRcrCRAdjuPrefPreOutIfName_Object=MibTableColumn
hpnicfRcrCRAdjuPrefPreOutIfName=_HpnicfRcrCRAdjuPrefPreOutIfName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,5),_HpnicfRcrCRAdjuPrefPreOutIfName_Type())
hpnicfRcrCRAdjuPrefPreOutIfName.setMaxAccess(_E)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefPreOutIfName.setStatus(_A)
class _HpnicfRcrCRAdjuPrefCurMRName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_HpnicfRcrCRAdjuPrefCurMRName_Type.__name__=_G
_HpnicfRcrCRAdjuPrefCurMRName_Object=MibTableColumn
hpnicfRcrCRAdjuPrefCurMRName=_HpnicfRcrCRAdjuPrefCurMRName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,6),_HpnicfRcrCRAdjuPrefCurMRName_Type())
hpnicfRcrCRAdjuPrefCurMRName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefCurMRName.setStatus(_A)
_HpnicfRcrCRAdjuPrefCurOutIfName_Type=OctetString
_HpnicfRcrCRAdjuPrefCurOutIfName_Object=MibTableColumn
hpnicfRcrCRAdjuPrefCurOutIfName=_HpnicfRcrCRAdjuPrefCurOutIfName_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,7),_HpnicfRcrCRAdjuPrefCurOutIfName_Type())
hpnicfRcrCRAdjuPrefCurOutIfName.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefCurOutIfName.setStatus(_A)
_HpnicfRcrCRAdjuPrefPersistTime_Type=Integer32
_HpnicfRcrCRAdjuPrefPersistTime_Object=MibTableColumn
hpnicfRcrCRAdjuPrefPersistTime=_HpnicfRcrCRAdjuPrefPersistTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,8),_HpnicfRcrCRAdjuPrefPersistTime_Type())
hpnicfRcrCRAdjuPrefPersistTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefPersistTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefPersistTime.setUnits(_I)
_HpnicfRcrCRAdjuPrefAgeTime_Type=Integer32
_HpnicfRcrCRAdjuPrefAgeTime_Object=MibTableColumn
hpnicfRcrCRAdjuPrefAgeTime=_HpnicfRcrCRAdjuPrefAgeTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,48,2,4,1,9),_HpnicfRcrCRAdjuPrefAgeTime_Type())
hpnicfRcrCRAdjuPrefAgeTime.setMaxAccess(_F)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefAgeTime.setStatus(_A)
if mibBuilder.loadTexts:hpnicfRcrCRAdjuPrefAgeTime.setUnits(_I)
mibBuilder.exportSymbols(_D,**{'hpnicfRcr':hpnicfRcr,'hpnicfRcrMR':hpnicfRcrMR,'hpnicfRcrMRGroup':hpnicfRcrMRGroup,'hpnicfRcrMRAllMaxUsedBandRate':hpnicfRcrMRAllMaxUsedBandRate,'hpnicfRcrMRAllMinUsedBandRate':hpnicfRcrMRAllMinUsedBandRate,'hpnicfRcrMRListenTime':hpnicfRcrMRListenTime,'hpnicfRcrMRStateTable':hpnicfRcrMRStateTable,'hpnicfRcrMRStateEntry':hpnicfRcrMRStateEntry,_J:hpnicfRcrMRName,'hpnicfRcrMRState':hpnicfRcrMRState,'hpnicfRcrMRAuthType':hpnicfRcrMRAuthType,'hpnicfRcrMRAuthPwd':hpnicfRcrMRAuthPwd,'hpnicfRcrMROutIfStateTable':hpnicfRcrMROutIfStateTable,'hpnicfRcrMROutIfStateEntry':hpnicfRcrMROutIfStateEntry,_L:hpnicfRcrMROutIfName,'hpnicfRcrMROutIfState':hpnicfRcrMROutIfState,'hpnicfRcrMROutIfMaxUsedBandRate':hpnicfRcrMROutIfMaxUsedBandRate,'hpnicfRcrMROutIfMinUsedBandRate':hpnicfRcrMROutIfMinUsedBandRate,'hpnicfRcrMROutIfUsedBandRate':hpnicfRcrMROutIfUsedBandRate,'hpnicfRcrCR':hpnicfRcrCR,'hpnicfRcrCRGroup':hpnicfRcrCRGroup,'hpnicfRcrCRState':hpnicfRcrCRState,'hpnicfRcrCRPortNum':hpnicfRcrCRPortNum,'hpnicfRcrCRCtrlMode':hpnicfRcrCRCtrlMode,'hpnicfRcrCRChooseMode':hpnicfRcrCRChooseMode,'hpnicfRcrCRKeepaliveTime':hpnicfRcrCRKeepaliveTime,'hpnicfRcrCRPolicyMode':hpnicfRcrCRPolicyMode,'hpnicfRcrCRStudyMode':hpnicfRcrCRStudyMode,'hpnicfRcrCRStudyIpPrefixNum':hpnicfRcrCRStudyIpPrefixNum,'hpnicfRcrCRIpPrefixLen':hpnicfRcrCRIpPrefixLen,'hpnicfRcrCRRcrPolicyTable':hpnicfRcrCRRcrPolicyTable,'hpnicfRcrCRRcrPolicyEntry':hpnicfRcrCRRcrPolicyEntry,_M:hpnicfRcrCRRcrPlyID,'hpnicfRcrCRRcrPlyMatchIPListName':hpnicfRcrCRRcrPlyMatchIPListName,'hpnicfRcrCRRcrPlyMatchStudyEnable':hpnicfRcrCRRcrPlyMatchStudyEnable,'hpnicfRcrCRRcrPlyMatchOperPlyName':hpnicfRcrCRRcrPlyMatchOperPlyName,'hpnicfRcrCRRcrAclNumber':hpnicfRcrCRRcrAclNumber,'hpnicfRcrCRRcrPlyDelayTime':hpnicfRcrCRRcrPlyDelayTime,'hpnicfRcrCRRcrPlyLossRate':hpnicfRcrCRRcrPlyLossRate,'hpnicfRcrCRMatPrefixPerfTable':hpnicfRcrCRMatPrefixPerfTable,'hpnicfRcrCRMatPrefixPerfEntry':hpnicfRcrCRMatPrefixPerfEntry,_N:hpnicfRcrCRMatPrefPerfAddrType,_O:hpnicfRcrCRMatPrefPerfDestIPAddr,_P:hpnicfRcrCRMatPrefPerfDestMaskLen,'hpnicfRcrCRMatPrefPerfDelayTime':hpnicfRcrCRMatPrefPerfDelayTime,'hpnicfRcrCRMatPrefPerfLossRate':hpnicfRcrCRMatPrefPerfLossRate,'hpnicfRcrCRMatPrefPerfThroughput':hpnicfRcrCRMatPrefPerfThroughput,'hpnicfRcrCRAdjustPrefixTable':hpnicfRcrCRAdjustPrefixTable,'hpnicfRcrCRAdjustPrefixEntry':hpnicfRcrCRAdjustPrefixEntry,_Q:hpnicfRcrCRAdjuPrefDestAddrType,_R:hpnicfRcrCRAdjuPrefDestAddr,_S:hpnicfRcrCRAdjuPrefMaskLen,_T:hpnicfRcrCRAdjuPrefPreMRName,_U:hpnicfRcrCRAdjuPrefPreOutIfName,'hpnicfRcrCRAdjuPrefCurMRName':hpnicfRcrCRAdjuPrefCurMRName,'hpnicfRcrCRAdjuPrefCurOutIfName':hpnicfRcrCRAdjuPrefCurOutIfName,'hpnicfRcrCRAdjuPrefPersistTime':hpnicfRcrCRAdjuPrefPersistTime,'hpnicfRcrCRAdjuPrefAgeTime':hpnicfRcrCRAdjuPrefAgeTime})