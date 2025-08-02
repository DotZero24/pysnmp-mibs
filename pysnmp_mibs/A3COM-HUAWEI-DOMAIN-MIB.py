_I='h3cDomainIpPoolNum'
_H='h3cDomainSchemeIndex'
_G='not-accessible'
_F='h3cDomainName'
_E='A3COM-HUAWEI-DOMAIN-MIB'
_D='OctetString'
_C='Integer32'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('A3COM-HUAWEI-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cDomain=ModuleIdentity((1,3,6,1,4,1,43,45,1,10,2,46))
class H3cModeOfDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('local',2),('radius',3),('tacacs',4)))
class H3cAAATypeDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('accounting',1),('authentication',2),('authorization',3),('none',4)))
class H3cAccessModeofDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('default',1),('login',2),('lanAccess',3),('portal',4),('ppp',5),('gcm',6),('dvpn',7),('dhcp',8),('voice',9),('superauthen',10),('command',11),('wapi',12)))
_H3cDomainControl_ObjectIdentity=ObjectIdentity
h3cDomainControl=_H3cDomainControl_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,46,1))
class _H3cDomainDefault_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_H3cDomainDefault_Type.__name__=_D
_H3cDomainDefault_Object=MibScalar
h3cDomainDefault=_H3cDomainDefault_Object((1,3,6,1,4,1,43,45,1,10,2,46,1,1),_H3cDomainDefault_Type())
h3cDomainDefault.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cDomainDefault.setStatus(_A)
_H3cDomainTables_ObjectIdentity=ObjectIdentity
h3cDomainTables=_H3cDomainTables_ObjectIdentity((1,3,6,1,4,1,43,45,1,10,2,46,2))
_H3cDomainInfoTable_Object=MibTable
h3cDomainInfoTable=_H3cDomainInfoTable_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1))
if mibBuilder.loadTexts:h3cDomainInfoTable.setStatus(_A)
_H3cDomainInfoEntry_Object=MibTableRow
h3cDomainInfoEntry=_H3cDomainInfoEntry_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1))
h3cDomainInfoEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h3cDomainInfoEntry.setStatus(_A)
class _H3cDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,128))
_H3cDomainName_Type.__name__=_D
_H3cDomainName_Object=MibTableColumn
h3cDomainName=_H3cDomainName_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,1),_H3cDomainName_Type())
h3cDomainName.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDomainName.setStatus(_A)
class _H3cDomainState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('block',2)))
_H3cDomainState_Type.__name__=_C
_H3cDomainState_Object=MibTableColumn
h3cDomainState=_H3cDomainState_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,2),_H3cDomainState_Type())
h3cDomainState.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainState.setStatus(_A)
_H3cDomainMaxAccessNum_Type=Integer32
_H3cDomainMaxAccessNum_Object=MibTableColumn
h3cDomainMaxAccessNum=_H3cDomainMaxAccessNum_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,3),_H3cDomainMaxAccessNum_Type())
h3cDomainMaxAccessNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainMaxAccessNum.setStatus(_A)
class _H3cDomainVlanAssignMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('integer',1),('string',2),('vlanlist',3)))
_H3cDomainVlanAssignMode_Type.__name__=_C
_H3cDomainVlanAssignMode_Object=MibTableColumn
h3cDomainVlanAssignMode=_H3cDomainVlanAssignMode_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,4),_H3cDomainVlanAssignMode_Type())
h3cDomainVlanAssignMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainVlanAssignMode.setStatus(_A)
_H3cDomainIdleCutEnable_Type=TruthValue
_H3cDomainIdleCutEnable_Object=MibTableColumn
h3cDomainIdleCutEnable=_H3cDomainIdleCutEnable_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,5),_H3cDomainIdleCutEnable_Type())
h3cDomainIdleCutEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIdleCutEnable.setStatus(_A)
class _H3cDomainIdleCutMaxTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,120))
_H3cDomainIdleCutMaxTime_Type.__name__=_C
_H3cDomainIdleCutMaxTime_Object=MibTableColumn
h3cDomainIdleCutMaxTime=_H3cDomainIdleCutMaxTime_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,6),_H3cDomainIdleCutMaxTime_Type())
h3cDomainIdleCutMaxTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIdleCutMaxTime.setStatus(_A)
class _H3cDomainIdleCutMinFlow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10240000))
_H3cDomainIdleCutMinFlow_Type.__name__=_C
_H3cDomainIdleCutMinFlow_Object=MibTableColumn
h3cDomainIdleCutMinFlow=_H3cDomainIdleCutMinFlow_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,7),_H3cDomainIdleCutMinFlow_Type())
h3cDomainIdleCutMinFlow.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIdleCutMinFlow.setStatus(_A)
_H3cDomainMessengerEnable_Type=TruthValue
_H3cDomainMessengerEnable_Object=MibTableColumn
h3cDomainMessengerEnable=_H3cDomainMessengerEnable_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,8),_H3cDomainMessengerEnable_Type())
h3cDomainMessengerEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainMessengerEnable.setStatus(_A)
class _H3cDomainMessengerLimitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_H3cDomainMessengerLimitTime_Type.__name__=_C
_H3cDomainMessengerLimitTime_Object=MibTableColumn
h3cDomainMessengerLimitTime=_H3cDomainMessengerLimitTime_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,9),_H3cDomainMessengerLimitTime_Type())
h3cDomainMessengerLimitTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainMessengerLimitTime.setStatus(_A)
class _H3cDomainMessengerSpanTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_H3cDomainMessengerSpanTime_Type.__name__=_C
_H3cDomainMessengerSpanTime_Object=MibTableColumn
h3cDomainMessengerSpanTime=_H3cDomainMessengerSpanTime_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,10),_H3cDomainMessengerSpanTime_Type())
h3cDomainMessengerSpanTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainMessengerSpanTime.setStatus(_A)
_H3cDomainSelfServiceEnable_Type=TruthValue
_H3cDomainSelfServiceEnable_Object=MibTableColumn
h3cDomainSelfServiceEnable=_H3cDomainSelfServiceEnable_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,11),_H3cDomainSelfServiceEnable_Type())
h3cDomainSelfServiceEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainSelfServiceEnable.setStatus(_A)
class _H3cDomainSelfServiceURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cDomainSelfServiceURL_Type.__name__=_D
_H3cDomainSelfServiceURL_Object=MibTableColumn
h3cDomainSelfServiceURL=_H3cDomainSelfServiceURL_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,12),_H3cDomainSelfServiceURL_Type())
h3cDomainSelfServiceURL.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainSelfServiceURL.setStatus(_A)
class _H3cDomainAccFailureAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('reject',2)))
_H3cDomainAccFailureAction_Type.__name__=_C
_H3cDomainAccFailureAction_Object=MibTableColumn
h3cDomainAccFailureAction=_H3cDomainAccFailureAction_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,13),_H3cDomainAccFailureAction_Type())
h3cDomainAccFailureAction.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainAccFailureAction.setStatus(_A)
_H3cDomainRowStatus_Type=RowStatus
_H3cDomainRowStatus_Object=MibTableColumn
h3cDomainRowStatus=_H3cDomainRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,14),_H3cDomainRowStatus_Type())
h3cDomainRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainRowStatus.setStatus(_A)
_H3cDomainCurrentAccessNum_Type=Integer32
_H3cDomainCurrentAccessNum_Object=MibTableColumn
h3cDomainCurrentAccessNum=_H3cDomainCurrentAccessNum_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,1,1,15),_H3cDomainCurrentAccessNum_Type())
h3cDomainCurrentAccessNum.setMaxAccess('read-only')
if mibBuilder.loadTexts:h3cDomainCurrentAccessNum.setStatus(_A)
_H3cDomainSchemeTable_Object=MibTable
h3cDomainSchemeTable=_H3cDomainSchemeTable_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2))
if mibBuilder.loadTexts:h3cDomainSchemeTable.setStatus(_A)
_H3cDomainSchemeEntry_Object=MibTableRow
h3cDomainSchemeEntry=_H3cDomainSchemeEntry_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1))
h3cDomainSchemeEntry.setIndexNames((0,_E,_F),(0,_E,_H))
if mibBuilder.loadTexts:h3cDomainSchemeEntry.setStatus(_A)
_H3cDomainSchemeIndex_Type=Integer32
_H3cDomainSchemeIndex_Object=MibTableColumn
h3cDomainSchemeIndex=_H3cDomainSchemeIndex_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,1),_H3cDomainSchemeIndex_Type())
h3cDomainSchemeIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDomainSchemeIndex.setStatus(_A)
_H3cDomainSchemeMode_Type=H3cModeOfDomainScheme
_H3cDomainSchemeMode_Object=MibTableColumn
h3cDomainSchemeMode=_H3cDomainSchemeMode_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,2),_H3cDomainSchemeMode_Type())
h3cDomainSchemeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainSchemeMode.setStatus(_A)
class _H3cDomainAuthSchemeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDomainAuthSchemeName_Type.__name__=_D
_H3cDomainAuthSchemeName_Object=MibTableColumn
h3cDomainAuthSchemeName=_H3cDomainAuthSchemeName_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,3),_H3cDomainAuthSchemeName_Type())
h3cDomainAuthSchemeName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainAuthSchemeName.setStatus(_A)
class _H3cDomainAcctSchemeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDomainAcctSchemeName_Type.__name__=_D
_H3cDomainAcctSchemeName_Object=MibTableColumn
h3cDomainAcctSchemeName=_H3cDomainAcctSchemeName_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,4),_H3cDomainAcctSchemeName_Type())
h3cDomainAcctSchemeName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainAcctSchemeName.setStatus(_A)
_H3cDomainSchemeRowStatus_Type=RowStatus
_H3cDomainSchemeRowStatus_Object=MibTableColumn
h3cDomainSchemeRowStatus=_H3cDomainSchemeRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,5),_H3cDomainSchemeRowStatus_Type())
h3cDomainSchemeRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainSchemeRowStatus.setStatus(_A)
_H3cDomainSchemeAAAType_Type=H3cAAATypeDomainScheme
_H3cDomainSchemeAAAType_Object=MibTableColumn
h3cDomainSchemeAAAType=_H3cDomainSchemeAAAType_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,6),_H3cDomainSchemeAAAType_Type())
h3cDomainSchemeAAAType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainSchemeAAAType.setStatus(_A)
class _H3cDomainSchemeAAAName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDomainSchemeAAAName_Type.__name__=_D
_H3cDomainSchemeAAAName_Object=MibTableColumn
h3cDomainSchemeAAAName=_H3cDomainSchemeAAAName_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,7),_H3cDomainSchemeAAAName_Type())
h3cDomainSchemeAAAName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainSchemeAAAName.setStatus(_A)
_H3cDomainSchemeAccessMode_Type=H3cAccessModeofDomainScheme
_H3cDomainSchemeAccessMode_Object=MibTableColumn
h3cDomainSchemeAccessMode=_H3cDomainSchemeAccessMode_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,2,1,8),_H3cDomainSchemeAccessMode_Type())
h3cDomainSchemeAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainSchemeAccessMode.setStatus(_A)
_H3cDomainIpPoolTable_Object=MibTable
h3cDomainIpPoolTable=_H3cDomainIpPoolTable_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,3))
if mibBuilder.loadTexts:h3cDomainIpPoolTable.setStatus(_A)
_H3cDomainIpPoolEntry_Object=MibTableRow
h3cDomainIpPoolEntry=_H3cDomainIpPoolEntry_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,3,1))
h3cDomainIpPoolEntry.setIndexNames((0,_E,_F),(0,_E,_I))
if mibBuilder.loadTexts:h3cDomainIpPoolEntry.setStatus(_A)
class _H3cDomainIpPoolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_H3cDomainIpPoolNum_Type.__name__=_C
_H3cDomainIpPoolNum_Object=MibTableColumn
h3cDomainIpPoolNum=_H3cDomainIpPoolNum_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,3,1,1),_H3cDomainIpPoolNum_Type())
h3cDomainIpPoolNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDomainIpPoolNum.setStatus(_A)
_H3cDomainIpPoolLowIpAddrType_Type=InetAddressType
_H3cDomainIpPoolLowIpAddrType_Object=MibTableColumn
h3cDomainIpPoolLowIpAddrType=_H3cDomainIpPoolLowIpAddrType_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,3,1,2),_H3cDomainIpPoolLowIpAddrType_Type())
h3cDomainIpPoolLowIpAddrType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIpPoolLowIpAddrType.setStatus(_A)
_H3cDomainIpPoolLowIpAddr_Type=InetAddress
_H3cDomainIpPoolLowIpAddr_Object=MibTableColumn
h3cDomainIpPoolLowIpAddr=_H3cDomainIpPoolLowIpAddr_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,3,1,3),_H3cDomainIpPoolLowIpAddr_Type())
h3cDomainIpPoolLowIpAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIpPoolLowIpAddr.setStatus(_A)
_H3cDomainIpPoolLen_Type=Integer32
_H3cDomainIpPoolLen_Object=MibTableColumn
h3cDomainIpPoolLen=_H3cDomainIpPoolLen_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,3,1,4),_H3cDomainIpPoolLen_Type())
h3cDomainIpPoolLen.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIpPoolLen.setStatus(_A)
_H3cDomainIpPoolRowStatus_Type=RowStatus
_H3cDomainIpPoolRowStatus_Object=MibTableColumn
h3cDomainIpPoolRowStatus=_H3cDomainIpPoolRowStatus_Object((1,3,6,1,4,1,43,45,1,10,2,46,2,3,1,5),_H3cDomainIpPoolRowStatus_Type())
h3cDomainIpPoolRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIpPoolRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'H3cModeOfDomainScheme':H3cModeOfDomainScheme,'H3cAAATypeDomainScheme':H3cAAATypeDomainScheme,'H3cAccessModeofDomainScheme':H3cAccessModeofDomainScheme,'h3cDomain':h3cDomain,'h3cDomainControl':h3cDomainControl,'h3cDomainDefault':h3cDomainDefault,'h3cDomainTables':h3cDomainTables,'h3cDomainInfoTable':h3cDomainInfoTable,'h3cDomainInfoEntry':h3cDomainInfoEntry,_F:h3cDomainName,'h3cDomainState':h3cDomainState,'h3cDomainMaxAccessNum':h3cDomainMaxAccessNum,'h3cDomainVlanAssignMode':h3cDomainVlanAssignMode,'h3cDomainIdleCutEnable':h3cDomainIdleCutEnable,'h3cDomainIdleCutMaxTime':h3cDomainIdleCutMaxTime,'h3cDomainIdleCutMinFlow':h3cDomainIdleCutMinFlow,'h3cDomainMessengerEnable':h3cDomainMessengerEnable,'h3cDomainMessengerLimitTime':h3cDomainMessengerLimitTime,'h3cDomainMessengerSpanTime':h3cDomainMessengerSpanTime,'h3cDomainSelfServiceEnable':h3cDomainSelfServiceEnable,'h3cDomainSelfServiceURL':h3cDomainSelfServiceURL,'h3cDomainAccFailureAction':h3cDomainAccFailureAction,'h3cDomainRowStatus':h3cDomainRowStatus,'h3cDomainCurrentAccessNum':h3cDomainCurrentAccessNum,'h3cDomainSchemeTable':h3cDomainSchemeTable,'h3cDomainSchemeEntry':h3cDomainSchemeEntry,_H:h3cDomainSchemeIndex,'h3cDomainSchemeMode':h3cDomainSchemeMode,'h3cDomainAuthSchemeName':h3cDomainAuthSchemeName,'h3cDomainAcctSchemeName':h3cDomainAcctSchemeName,'h3cDomainSchemeRowStatus':h3cDomainSchemeRowStatus,'h3cDomainSchemeAAAType':h3cDomainSchemeAAAType,'h3cDomainSchemeAAAName':h3cDomainSchemeAAAName,'h3cDomainSchemeAccessMode':h3cDomainSchemeAccessMode,'h3cDomainIpPoolTable':h3cDomainIpPoolTable,'h3cDomainIpPoolEntry':h3cDomainIpPoolEntry,_I:h3cDomainIpPoolNum,'h3cDomainIpPoolLowIpAddrType':h3cDomainIpPoolLowIpAddrType,'h3cDomainIpPoolLowIpAddr':h3cDomainIpPoolLowIpAddr,'h3cDomainIpPoolLen':h3cDomainIpPoolLen,'h3cDomainIpPoolRowStatus':h3cDomainIpPoolRowStatus})