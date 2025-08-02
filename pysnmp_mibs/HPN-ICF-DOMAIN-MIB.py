_J='hpnicfDomainIpPoolNum'
_I='hpnicfDomainSchemeIndex'
_H='read-only'
_G='not-accessible'
_F='hpnicfDomainName'
_E='HPN-ICF-DOMAIN-MIB'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
hpnicfDomain=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,46))
class HpnicfModeOfDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('local',2),('radius',3),('tacacs',4),('ldap',5)))
class HpnicfAAATypeDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('accounting',1),('authentication',2),('authorization',3),('none',4)))
class HpnicfAccessModeofDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('default',1),('login',2),('lanAccess',3),('portal',4),('ppp',5),('gcm',6),('dvpn',7),('dhcp',8),('voice',9),('superauthen',10),('command',11),('reserved',12)))
_HpnicfDomainControl_ObjectIdentity=ObjectIdentity
hpnicfDomainControl=_HpnicfDomainControl_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,46,1))
class _HpnicfDomainDefault_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpnicfDomainDefault_Type.__name__=_D
_HpnicfDomainDefault_Object=MibScalar
hpnicfDomainDefault=_HpnicfDomainDefault_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,1,1),_HpnicfDomainDefault_Type())
hpnicfDomainDefault.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfDomainDefault.setStatus(_A)
_HpnicfDomainTables_ObjectIdentity=ObjectIdentity
hpnicfDomainTables=_HpnicfDomainTables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,46,2))
_HpnicfDomainInfoTable_Object=MibTable
hpnicfDomainInfoTable=_HpnicfDomainInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1))
if mibBuilder.loadTexts:hpnicfDomainInfoTable.setStatus(_A)
_HpnicfDomainInfoEntry_Object=MibTableRow
hpnicfDomainInfoEntry=_HpnicfDomainInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1))
hpnicfDomainInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:hpnicfDomainInfoEntry.setStatus(_A)
class _HpnicfDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_HpnicfDomainName_Type.__name__=_D
_HpnicfDomainName_Object=MibTableColumn
hpnicfDomainName=_HpnicfDomainName_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,1),_HpnicfDomainName_Type())
hpnicfDomainName.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDomainName.setStatus(_A)
class _HpnicfDomainState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('block',2)))
_HpnicfDomainState_Type.__name__=_C
_HpnicfDomainState_Object=MibTableColumn
hpnicfDomainState=_HpnicfDomainState_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,2),_HpnicfDomainState_Type())
hpnicfDomainState.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainState.setStatus(_A)
_HpnicfDomainMaxAccessNum_Type=Integer32
_HpnicfDomainMaxAccessNum_Object=MibTableColumn
hpnicfDomainMaxAccessNum=_HpnicfDomainMaxAccessNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,3),_HpnicfDomainMaxAccessNum_Type())
hpnicfDomainMaxAccessNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainMaxAccessNum.setStatus(_A)
class _HpnicfDomainVlanAssignMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('integer',1),('string',2),('vlanlist',3)))
_HpnicfDomainVlanAssignMode_Type.__name__=_C
_HpnicfDomainVlanAssignMode_Object=MibTableColumn
hpnicfDomainVlanAssignMode=_HpnicfDomainVlanAssignMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,4),_HpnicfDomainVlanAssignMode_Type())
hpnicfDomainVlanAssignMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainVlanAssignMode.setStatus(_A)
_HpnicfDomainIdleCutEnable_Type=TruthValue
_HpnicfDomainIdleCutEnable_Object=MibTableColumn
hpnicfDomainIdleCutEnable=_HpnicfDomainIdleCutEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,5),_HpnicfDomainIdleCutEnable_Type())
hpnicfDomainIdleCutEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainIdleCutEnable.setStatus(_A)
_HpnicfDomainIdleCutMaxTime_Type=Integer32
_HpnicfDomainIdleCutMaxTime_Object=MibTableColumn
hpnicfDomainIdleCutMaxTime=_HpnicfDomainIdleCutMaxTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,6),_HpnicfDomainIdleCutMaxTime_Type())
hpnicfDomainIdleCutMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainIdleCutMaxTime.setStatus(_A)
class _HpnicfDomainIdleCutMinFlow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10240000))
_HpnicfDomainIdleCutMinFlow_Type.__name__=_C
_HpnicfDomainIdleCutMinFlow_Object=MibTableColumn
hpnicfDomainIdleCutMinFlow=_HpnicfDomainIdleCutMinFlow_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,7),_HpnicfDomainIdleCutMinFlow_Type())
hpnicfDomainIdleCutMinFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainIdleCutMinFlow.setStatus(_A)
_HpnicfDomainMessengerEnable_Type=TruthValue
_HpnicfDomainMessengerEnable_Object=MibTableColumn
hpnicfDomainMessengerEnable=_HpnicfDomainMessengerEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,8),_HpnicfDomainMessengerEnable_Type())
hpnicfDomainMessengerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainMessengerEnable.setStatus(_A)
class _HpnicfDomainMessengerLimitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_HpnicfDomainMessengerLimitTime_Type.__name__=_C
_HpnicfDomainMessengerLimitTime_Object=MibTableColumn
hpnicfDomainMessengerLimitTime=_HpnicfDomainMessengerLimitTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,9),_HpnicfDomainMessengerLimitTime_Type())
hpnicfDomainMessengerLimitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainMessengerLimitTime.setStatus(_A)
class _HpnicfDomainMessengerSpanTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_HpnicfDomainMessengerSpanTime_Type.__name__=_C
_HpnicfDomainMessengerSpanTime_Object=MibTableColumn
hpnicfDomainMessengerSpanTime=_HpnicfDomainMessengerSpanTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,10),_HpnicfDomainMessengerSpanTime_Type())
hpnicfDomainMessengerSpanTime.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainMessengerSpanTime.setStatus(_A)
_HpnicfDomainSelfServiceEnable_Type=TruthValue
_HpnicfDomainSelfServiceEnable_Object=MibTableColumn
hpnicfDomainSelfServiceEnable=_HpnicfDomainSelfServiceEnable_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,11),_HpnicfDomainSelfServiceEnable_Type())
hpnicfDomainSelfServiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainSelfServiceEnable.setStatus(_A)
class _HpnicfDomainSelfServiceURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_HpnicfDomainSelfServiceURL_Type.__name__=_D
_HpnicfDomainSelfServiceURL_Object=MibTableColumn
hpnicfDomainSelfServiceURL=_HpnicfDomainSelfServiceURL_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,12),_HpnicfDomainSelfServiceURL_Type())
hpnicfDomainSelfServiceURL.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainSelfServiceURL.setStatus(_A)
class _HpnicfDomainAccFailureAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('reject',2)))
_HpnicfDomainAccFailureAction_Type.__name__=_C
_HpnicfDomainAccFailureAction_Object=MibTableColumn
hpnicfDomainAccFailureAction=_HpnicfDomainAccFailureAction_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,13),_HpnicfDomainAccFailureAction_Type())
hpnicfDomainAccFailureAction.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainAccFailureAction.setStatus(_A)
_HpnicfDomainRowStatus_Type=RowStatus
_HpnicfDomainRowStatus_Object=MibTableColumn
hpnicfDomainRowStatus=_HpnicfDomainRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,14),_HpnicfDomainRowStatus_Type())
hpnicfDomainRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainRowStatus.setStatus(_A)
_HpnicfDomainCurrentAccessNum_Type=Integer32
_HpnicfDomainCurrentAccessNum_Object=MibTableColumn
hpnicfDomainCurrentAccessNum=_HpnicfDomainCurrentAccessNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,15),_HpnicfDomainCurrentAccessNum_Type())
hpnicfDomainCurrentAccessNum.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDomainCurrentAccessNum.setStatus(_A)
_HpnicfDomainIdleCutTime_Type=TimeTicks
_HpnicfDomainIdleCutTime_Object=MibTableColumn
hpnicfDomainIdleCutTime=_HpnicfDomainIdleCutTime_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,1,1,16),_HpnicfDomainIdleCutTime_Type())
hpnicfDomainIdleCutTime.setMaxAccess(_H)
if mibBuilder.loadTexts:hpnicfDomainIdleCutTime.setStatus(_A)
_HpnicfDomainSchemeTable_Object=MibTable
hpnicfDomainSchemeTable=_HpnicfDomainSchemeTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2))
if mibBuilder.loadTexts:hpnicfDomainSchemeTable.setStatus(_A)
_HpnicfDomainSchemeEntry_Object=MibTableRow
hpnicfDomainSchemeEntry=_HpnicfDomainSchemeEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1))
hpnicfDomainSchemeEntry.setIndexNames((0,_E,_F),(0,_E,_I))
if mibBuilder.loadTexts:hpnicfDomainSchemeEntry.setStatus(_A)
_HpnicfDomainSchemeIndex_Type=Integer32
_HpnicfDomainSchemeIndex_Object=MibTableColumn
hpnicfDomainSchemeIndex=_HpnicfDomainSchemeIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,1),_HpnicfDomainSchemeIndex_Type())
hpnicfDomainSchemeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDomainSchemeIndex.setStatus(_A)
_HpnicfDomainSchemeMode_Type=HpnicfModeOfDomainScheme
_HpnicfDomainSchemeMode_Object=MibTableColumn
hpnicfDomainSchemeMode=_HpnicfDomainSchemeMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,2),_HpnicfDomainSchemeMode_Type())
hpnicfDomainSchemeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainSchemeMode.setStatus(_A)
class _HpnicfDomainAuthSchemeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfDomainAuthSchemeName_Type.__name__=_D
_HpnicfDomainAuthSchemeName_Object=MibTableColumn
hpnicfDomainAuthSchemeName=_HpnicfDomainAuthSchemeName_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,3),_HpnicfDomainAuthSchemeName_Type())
hpnicfDomainAuthSchemeName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainAuthSchemeName.setStatus(_A)
class _HpnicfDomainAcctSchemeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfDomainAcctSchemeName_Type.__name__=_D
_HpnicfDomainAcctSchemeName_Object=MibTableColumn
hpnicfDomainAcctSchemeName=_HpnicfDomainAcctSchemeName_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,4),_HpnicfDomainAcctSchemeName_Type())
hpnicfDomainAcctSchemeName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainAcctSchemeName.setStatus(_A)
_HpnicfDomainSchemeRowStatus_Type=RowStatus
_HpnicfDomainSchemeRowStatus_Object=MibTableColumn
hpnicfDomainSchemeRowStatus=_HpnicfDomainSchemeRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,5),_HpnicfDomainSchemeRowStatus_Type())
hpnicfDomainSchemeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainSchemeRowStatus.setStatus(_A)
_HpnicfDomainSchemeAAAType_Type=HpnicfAAATypeDomainScheme
_HpnicfDomainSchemeAAAType_Object=MibTableColumn
hpnicfDomainSchemeAAAType=_HpnicfDomainSchemeAAAType_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,6),_HpnicfDomainSchemeAAAType_Type())
hpnicfDomainSchemeAAAType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainSchemeAAAType.setStatus(_A)
class _HpnicfDomainSchemeAAAName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_HpnicfDomainSchemeAAAName_Type.__name__=_D
_HpnicfDomainSchemeAAAName_Object=MibTableColumn
hpnicfDomainSchemeAAAName=_HpnicfDomainSchemeAAAName_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,7),_HpnicfDomainSchemeAAAName_Type())
hpnicfDomainSchemeAAAName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainSchemeAAAName.setStatus(_A)
_HpnicfDomainSchemeAccessMode_Type=HpnicfAccessModeofDomainScheme
_HpnicfDomainSchemeAccessMode_Object=MibTableColumn
hpnicfDomainSchemeAccessMode=_HpnicfDomainSchemeAccessMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,2,1,8),_HpnicfDomainSchemeAccessMode_Type())
hpnicfDomainSchemeAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainSchemeAccessMode.setStatus(_A)
_HpnicfDomainIpPoolTable_Object=MibTable
hpnicfDomainIpPoolTable=_HpnicfDomainIpPoolTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,3))
if mibBuilder.loadTexts:hpnicfDomainIpPoolTable.setStatus(_A)
_HpnicfDomainIpPoolEntry_Object=MibTableRow
hpnicfDomainIpPoolEntry=_HpnicfDomainIpPoolEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,3,1))
hpnicfDomainIpPoolEntry.setIndexNames((0,_E,_F),(0,_E,_J))
if mibBuilder.loadTexts:hpnicfDomainIpPoolEntry.setStatus(_A)
class _HpnicfDomainIpPoolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_HpnicfDomainIpPoolNum_Type.__name__=_C
_HpnicfDomainIpPoolNum_Object=MibTableColumn
hpnicfDomainIpPoolNum=_HpnicfDomainIpPoolNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,3,1,1),_HpnicfDomainIpPoolNum_Type())
hpnicfDomainIpPoolNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDomainIpPoolNum.setStatus(_A)
_HpnicfDomainIpPoolLowIpAddrType_Type=InetAddressType
_HpnicfDomainIpPoolLowIpAddrType_Object=MibTableColumn
hpnicfDomainIpPoolLowIpAddrType=_HpnicfDomainIpPoolLowIpAddrType_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,3,1,2),_HpnicfDomainIpPoolLowIpAddrType_Type())
hpnicfDomainIpPoolLowIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainIpPoolLowIpAddrType.setStatus(_A)
_HpnicfDomainIpPoolLowIpAddr_Type=InetAddress
_HpnicfDomainIpPoolLowIpAddr_Object=MibTableColumn
hpnicfDomainIpPoolLowIpAddr=_HpnicfDomainIpPoolLowIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,3,1,3),_HpnicfDomainIpPoolLowIpAddr_Type())
hpnicfDomainIpPoolLowIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainIpPoolLowIpAddr.setStatus(_A)
_HpnicfDomainIpPoolLen_Type=Integer32
_HpnicfDomainIpPoolLen_Object=MibTableColumn
hpnicfDomainIpPoolLen=_HpnicfDomainIpPoolLen_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,3,1,4),_HpnicfDomainIpPoolLen_Type())
hpnicfDomainIpPoolLen.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainIpPoolLen.setStatus(_A)
_HpnicfDomainIpPoolRowStatus_Type=RowStatus
_HpnicfDomainIpPoolRowStatus_Object=MibTableColumn
hpnicfDomainIpPoolRowStatus=_HpnicfDomainIpPoolRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,46,2,3,1,5),_HpnicfDomainIpPoolRowStatus_Type())
hpnicfDomainIpPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDomainIpPoolRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'HpnicfModeOfDomainScheme':HpnicfModeOfDomainScheme,'HpnicfAAATypeDomainScheme':HpnicfAAATypeDomainScheme,'HpnicfAccessModeofDomainScheme':HpnicfAccessModeofDomainScheme,'hpnicfDomain':hpnicfDomain,'hpnicfDomainControl':hpnicfDomainControl,'hpnicfDomainDefault':hpnicfDomainDefault,'hpnicfDomainTables':hpnicfDomainTables,'hpnicfDomainInfoTable':hpnicfDomainInfoTable,'hpnicfDomainInfoEntry':hpnicfDomainInfoEntry,_F:hpnicfDomainName,'hpnicfDomainState':hpnicfDomainState,'hpnicfDomainMaxAccessNum':hpnicfDomainMaxAccessNum,'hpnicfDomainVlanAssignMode':hpnicfDomainVlanAssignMode,'hpnicfDomainIdleCutEnable':hpnicfDomainIdleCutEnable,'hpnicfDomainIdleCutMaxTime':hpnicfDomainIdleCutMaxTime,'hpnicfDomainIdleCutMinFlow':hpnicfDomainIdleCutMinFlow,'hpnicfDomainMessengerEnable':hpnicfDomainMessengerEnable,'hpnicfDomainMessengerLimitTime':hpnicfDomainMessengerLimitTime,'hpnicfDomainMessengerSpanTime':hpnicfDomainMessengerSpanTime,'hpnicfDomainSelfServiceEnable':hpnicfDomainSelfServiceEnable,'hpnicfDomainSelfServiceURL':hpnicfDomainSelfServiceURL,'hpnicfDomainAccFailureAction':hpnicfDomainAccFailureAction,'hpnicfDomainRowStatus':hpnicfDomainRowStatus,'hpnicfDomainCurrentAccessNum':hpnicfDomainCurrentAccessNum,'hpnicfDomainIdleCutTime':hpnicfDomainIdleCutTime,'hpnicfDomainSchemeTable':hpnicfDomainSchemeTable,'hpnicfDomainSchemeEntry':hpnicfDomainSchemeEntry,_I:hpnicfDomainSchemeIndex,'hpnicfDomainSchemeMode':hpnicfDomainSchemeMode,'hpnicfDomainAuthSchemeName':hpnicfDomainAuthSchemeName,'hpnicfDomainAcctSchemeName':hpnicfDomainAcctSchemeName,'hpnicfDomainSchemeRowStatus':hpnicfDomainSchemeRowStatus,'hpnicfDomainSchemeAAAType':hpnicfDomainSchemeAAAType,'hpnicfDomainSchemeAAAName':hpnicfDomainSchemeAAAName,'hpnicfDomainSchemeAccessMode':hpnicfDomainSchemeAccessMode,'hpnicfDomainIpPoolTable':hpnicfDomainIpPoolTable,'hpnicfDomainIpPoolEntry':hpnicfDomainIpPoolEntry,_J:hpnicfDomainIpPoolNum,'hpnicfDomainIpPoolLowIpAddrType':hpnicfDomainIpPoolLowIpAddrType,'hpnicfDomainIpPoolLowIpAddr':hpnicfDomainIpPoolLowIpAddr,'hpnicfDomainIpPoolLen':hpnicfDomainIpPoolLen,'hpnicfDomainIpPoolRowStatus':hpnicfDomainIpPoolRowStatus})