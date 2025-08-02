_J='h3cDomainIpPoolNum'
_I='h3cDomainSchemeIndex'
_H='not-accessible'
_G='h3cDomainName'
_F='H3C-DOMAIN-MIB'
_E='Integer32'
_D='OctetString'
_C='read-create'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
h3cDomain=ModuleIdentity((1,3,6,1,4,1,2011,10,2,46))
if mibBuilder.loadTexts:h3cDomain.setRevisions(('2017-10-13 00:00','2017-06-03 00:00','2013-11-25 00:00','2013-04-25 00:00','2013-02-28 00:00','2012-10-15 00:00','2012-05-20 00:00','2009-08-05 00:00','2008-12-30 00:00','2008-11-25 00:00','2007-03-07 00:00','2006-03-27 00:00','2005-06-30 00:00','2005-03-23 00:00'))
class H3cModeOfDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('none',1),('local',2),('radius',3),('tacacs',4),('ldap',5)))
class H3cAAATypeDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('accounting',1),('authentication',2),('authorization',3),('none',4)))
class H3cAccessModeofDomainScheme(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('default',1),('login',2),('lanAccess',3),('portal',4),('ppp',5),('gcm',6),('dvpn',7),('dhcp',8),('voice',9),('superauthen',10),('command',11),('reserved',12)))
_H3cDomainControl_ObjectIdentity=ObjectIdentity
h3cDomainControl=_H3cDomainControl_ObjectIdentity((1,3,6,1,4,1,2011,10,2,46,1))
class _H3cDomainDefault_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_H3cDomainDefault_Type.__name__=_D
_H3cDomainDefault_Object=MibScalar
h3cDomainDefault=_H3cDomainDefault_Object((1,3,6,1,4,1,2011,10,2,46,1,1),_H3cDomainDefault_Type())
h3cDomainDefault.setMaxAccess('read-write')
if mibBuilder.loadTexts:h3cDomainDefault.setStatus(_A)
_H3cDomainTables_ObjectIdentity=ObjectIdentity
h3cDomainTables=_H3cDomainTables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,46,2))
_H3cDomainInfoTable_Object=MibTable
h3cDomainInfoTable=_H3cDomainInfoTable_Object((1,3,6,1,4,1,2011,10,2,46,2,1))
if mibBuilder.loadTexts:h3cDomainInfoTable.setStatus(_A)
_H3cDomainInfoEntry_Object=MibTableRow
h3cDomainInfoEntry=_H3cDomainInfoEntry_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1))
h3cDomainInfoEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDomainInfoEntry.setStatus(_A)
class _H3cDomainName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_H3cDomainName_Type.__name__=_D
_H3cDomainName_Object=MibTableColumn
h3cDomainName=_H3cDomainName_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,1),_H3cDomainName_Type())
h3cDomainName.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDomainName.setStatus(_A)
class _H3cDomainState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('active',1),('block',2)))
_H3cDomainState_Type.__name__=_E
_H3cDomainState_Object=MibTableColumn
h3cDomainState=_H3cDomainState_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,2),_H3cDomainState_Type())
h3cDomainState.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainState.setStatus(_A)
_H3cDomainMaxAccessNum_Type=Integer32
_H3cDomainMaxAccessNum_Object=MibTableColumn
h3cDomainMaxAccessNum=_H3cDomainMaxAccessNum_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,3),_H3cDomainMaxAccessNum_Type())
h3cDomainMaxAccessNum.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainMaxAccessNum.setStatus(_A)
class _H3cDomainVlanAssignMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('integer',1),('string',2),('vlanlist',3)))
_H3cDomainVlanAssignMode_Type.__name__=_E
_H3cDomainVlanAssignMode_Object=MibTableColumn
h3cDomainVlanAssignMode=_H3cDomainVlanAssignMode_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,4),_H3cDomainVlanAssignMode_Type())
h3cDomainVlanAssignMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainVlanAssignMode.setStatus(_A)
_H3cDomainIdleCutEnable_Type=TruthValue
_H3cDomainIdleCutEnable_Object=MibTableColumn
h3cDomainIdleCutEnable=_H3cDomainIdleCutEnable_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,5),_H3cDomainIdleCutEnable_Type())
h3cDomainIdleCutEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIdleCutEnable.setStatus(_A)
_H3cDomainIdleCutMaxTime_Type=Integer32
_H3cDomainIdleCutMaxTime_Object=MibTableColumn
h3cDomainIdleCutMaxTime=_H3cDomainIdleCutMaxTime_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,6),_H3cDomainIdleCutMaxTime_Type())
h3cDomainIdleCutMaxTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIdleCutMaxTime.setStatus(_A)
class _H3cDomainIdleCutMinFlow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10240000))
_H3cDomainIdleCutMinFlow_Type.__name__=_E
_H3cDomainIdleCutMinFlow_Object=MibTableColumn
h3cDomainIdleCutMinFlow=_H3cDomainIdleCutMinFlow_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,7),_H3cDomainIdleCutMinFlow_Type())
h3cDomainIdleCutMinFlow.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIdleCutMinFlow.setStatus(_A)
_H3cDomainMessengerEnable_Type=TruthValue
_H3cDomainMessengerEnable_Object=MibTableColumn
h3cDomainMessengerEnable=_H3cDomainMessengerEnable_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,8),_H3cDomainMessengerEnable_Type())
h3cDomainMessengerEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainMessengerEnable.setStatus(_A)
class _H3cDomainMessengerLimitTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_H3cDomainMessengerLimitTime_Type.__name__=_E
_H3cDomainMessengerLimitTime_Object=MibTableColumn
h3cDomainMessengerLimitTime=_H3cDomainMessengerLimitTime_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,9),_H3cDomainMessengerLimitTime_Type())
h3cDomainMessengerLimitTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainMessengerLimitTime.setStatus(_A)
class _H3cDomainMessengerSpanTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,60))
_H3cDomainMessengerSpanTime_Type.__name__=_E
_H3cDomainMessengerSpanTime_Object=MibTableColumn
h3cDomainMessengerSpanTime=_H3cDomainMessengerSpanTime_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,10),_H3cDomainMessengerSpanTime_Type())
h3cDomainMessengerSpanTime.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainMessengerSpanTime.setStatus(_A)
_H3cDomainSelfServiceEnable_Type=TruthValue
_H3cDomainSelfServiceEnable_Object=MibTableColumn
h3cDomainSelfServiceEnable=_H3cDomainSelfServiceEnable_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,11),_H3cDomainSelfServiceEnable_Type())
h3cDomainSelfServiceEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainSelfServiceEnable.setStatus(_A)
class _H3cDomainSelfServiceURL_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_H3cDomainSelfServiceURL_Type.__name__=_D
_H3cDomainSelfServiceURL_Object=MibTableColumn
h3cDomainSelfServiceURL=_H3cDomainSelfServiceURL_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,12),_H3cDomainSelfServiceURL_Type())
h3cDomainSelfServiceURL.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainSelfServiceURL.setStatus(_A)
class _H3cDomainAccFailureAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ignore',1),('reject',2)))
_H3cDomainAccFailureAction_Type.__name__=_E
_H3cDomainAccFailureAction_Object=MibTableColumn
h3cDomainAccFailureAction=_H3cDomainAccFailureAction_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,13),_H3cDomainAccFailureAction_Type())
h3cDomainAccFailureAction.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainAccFailureAction.setStatus(_A)
_H3cDomainRowStatus_Type=RowStatus
_H3cDomainRowStatus_Object=MibTableColumn
h3cDomainRowStatus=_H3cDomainRowStatus_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,14),_H3cDomainRowStatus_Type())
h3cDomainRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainRowStatus.setStatus(_A)
_H3cDomainCurrentAccessNum_Type=Integer32
_H3cDomainCurrentAccessNum_Object=MibTableColumn
h3cDomainCurrentAccessNum=_H3cDomainCurrentAccessNum_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,15),_H3cDomainCurrentAccessNum_Type())
h3cDomainCurrentAccessNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainCurrentAccessNum.setStatus(_A)
_H3cDomainIdleCutTime_Type=TimeTicks
_H3cDomainIdleCutTime_Object=MibTableColumn
h3cDomainIdleCutTime=_H3cDomainIdleCutTime_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,16),_H3cDomainIdleCutTime_Type())
h3cDomainIdleCutTime.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIdleCutTime.setStatus(_A)
class _H3cDomainServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hsi',1),('stb',2),('voip',3)))
_H3cDomainServiceType_Type.__name__=_E
_H3cDomainServiceType_Object=MibTableColumn
h3cDomainServiceType=_H3cDomainServiceType_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,17),_H3cDomainServiceType_Type())
h3cDomainServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainServiceType.setStatus(_A)
class _H3cDomainIpPoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDomainIpPoolName_Type.__name__=_D
_H3cDomainIpPoolName_Object=MibTableColumn
h3cDomainIpPoolName=_H3cDomainIpPoolName_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,18),_H3cDomainIpPoolName_Type())
h3cDomainIpPoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIpPoolName.setStatus(_A)
class _H3cDomainIpv6PoolName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDomainIpv6PoolName_Type.__name__=_D
_H3cDomainIpv6PoolName_Object=MibTableColumn
h3cDomainIpv6PoolName=_H3cDomainIpv6PoolName_Object((1,3,6,1,4,1,2011,10,2,46,2,1,1,19),_H3cDomainIpv6PoolName_Type())
h3cDomainIpv6PoolName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIpv6PoolName.setStatus(_A)
_H3cDomainSchemeTable_Object=MibTable
h3cDomainSchemeTable=_H3cDomainSchemeTable_Object((1,3,6,1,4,1,2011,10,2,46,2,2))
if mibBuilder.loadTexts:h3cDomainSchemeTable.setStatus(_A)
_H3cDomainSchemeEntry_Object=MibTableRow
h3cDomainSchemeEntry=_H3cDomainSchemeEntry_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1))
h3cDomainSchemeEntry.setIndexNames((0,_F,_G),(0,_F,_I))
if mibBuilder.loadTexts:h3cDomainSchemeEntry.setStatus(_A)
_H3cDomainSchemeIndex_Type=Integer32
_H3cDomainSchemeIndex_Object=MibTableColumn
h3cDomainSchemeIndex=_H3cDomainSchemeIndex_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,1),_H3cDomainSchemeIndex_Type())
h3cDomainSchemeIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDomainSchemeIndex.setStatus(_A)
_H3cDomainSchemeMode_Type=H3cModeOfDomainScheme
_H3cDomainSchemeMode_Object=MibTableColumn
h3cDomainSchemeMode=_H3cDomainSchemeMode_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,2),_H3cDomainSchemeMode_Type())
h3cDomainSchemeMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainSchemeMode.setStatus(_A)
class _H3cDomainAuthSchemeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDomainAuthSchemeName_Type.__name__=_D
_H3cDomainAuthSchemeName_Object=MibTableColumn
h3cDomainAuthSchemeName=_H3cDomainAuthSchemeName_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,3),_H3cDomainAuthSchemeName_Type())
h3cDomainAuthSchemeName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainAuthSchemeName.setStatus(_A)
class _H3cDomainAcctSchemeName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDomainAcctSchemeName_Type.__name__=_D
_H3cDomainAcctSchemeName_Object=MibTableColumn
h3cDomainAcctSchemeName=_H3cDomainAcctSchemeName_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,4),_H3cDomainAcctSchemeName_Type())
h3cDomainAcctSchemeName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainAcctSchemeName.setStatus(_A)
_H3cDomainSchemeRowStatus_Type=RowStatus
_H3cDomainSchemeRowStatus_Object=MibTableColumn
h3cDomainSchemeRowStatus=_H3cDomainSchemeRowStatus_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,5),_H3cDomainSchemeRowStatus_Type())
h3cDomainSchemeRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainSchemeRowStatus.setStatus(_A)
_H3cDomainSchemeAAAType_Type=H3cAAATypeDomainScheme
_H3cDomainSchemeAAAType_Object=MibTableColumn
h3cDomainSchemeAAAType=_H3cDomainSchemeAAAType_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,6),_H3cDomainSchemeAAAType_Type())
h3cDomainSchemeAAAType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainSchemeAAAType.setStatus(_A)
class _H3cDomainSchemeAAAName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDomainSchemeAAAName_Type.__name__=_D
_H3cDomainSchemeAAAName_Object=MibTableColumn
h3cDomainSchemeAAAName=_H3cDomainSchemeAAAName_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,7),_H3cDomainSchemeAAAName_Type())
h3cDomainSchemeAAAName.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainSchemeAAAName.setStatus(_A)
_H3cDomainSchemeAccessMode_Type=H3cAccessModeofDomainScheme
_H3cDomainSchemeAccessMode_Object=MibTableColumn
h3cDomainSchemeAccessMode=_H3cDomainSchemeAccessMode_Object((1,3,6,1,4,1,2011,10,2,46,2,2,1,8),_H3cDomainSchemeAccessMode_Type())
h3cDomainSchemeAccessMode.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainSchemeAccessMode.setStatus(_A)
_H3cDomainIpPoolTable_Object=MibTable
h3cDomainIpPoolTable=_H3cDomainIpPoolTable_Object((1,3,6,1,4,1,2011,10,2,46,2,3))
if mibBuilder.loadTexts:h3cDomainIpPoolTable.setStatus(_A)
_H3cDomainIpPoolEntry_Object=MibTableRow
h3cDomainIpPoolEntry=_H3cDomainIpPoolEntry_Object((1,3,6,1,4,1,2011,10,2,46,2,3,1))
h3cDomainIpPoolEntry.setIndexNames((0,_F,_G),(0,_F,_J))
if mibBuilder.loadTexts:h3cDomainIpPoolEntry.setStatus(_A)
class _H3cDomainIpPoolNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_H3cDomainIpPoolNum_Type.__name__=_E
_H3cDomainIpPoolNum_Object=MibTableColumn
h3cDomainIpPoolNum=_H3cDomainIpPoolNum_Object((1,3,6,1,4,1,2011,10,2,46,2,3,1,1),_H3cDomainIpPoolNum_Type())
h3cDomainIpPoolNum.setMaxAccess(_H)
if mibBuilder.loadTexts:h3cDomainIpPoolNum.setStatus(_A)
_H3cDomainIpPoolLowIpAddrType_Type=InetAddressType
_H3cDomainIpPoolLowIpAddrType_Object=MibTableColumn
h3cDomainIpPoolLowIpAddrType=_H3cDomainIpPoolLowIpAddrType_Object((1,3,6,1,4,1,2011,10,2,46,2,3,1,2),_H3cDomainIpPoolLowIpAddrType_Type())
h3cDomainIpPoolLowIpAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIpPoolLowIpAddrType.setStatus(_A)
_H3cDomainIpPoolLowIpAddr_Type=InetAddress
_H3cDomainIpPoolLowIpAddr_Object=MibTableColumn
h3cDomainIpPoolLowIpAddr=_H3cDomainIpPoolLowIpAddr_Object((1,3,6,1,4,1,2011,10,2,46,2,3,1,3),_H3cDomainIpPoolLowIpAddr_Type())
h3cDomainIpPoolLowIpAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIpPoolLowIpAddr.setStatus(_A)
_H3cDomainIpPoolLen_Type=Integer32
_H3cDomainIpPoolLen_Object=MibTableColumn
h3cDomainIpPoolLen=_H3cDomainIpPoolLen_Object((1,3,6,1,4,1,2011,10,2,46,2,3,1,4),_H3cDomainIpPoolLen_Type())
h3cDomainIpPoolLen.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIpPoolLen.setStatus(_A)
_H3cDomainIpPoolRowStatus_Type=RowStatus
_H3cDomainIpPoolRowStatus_Object=MibTableColumn
h3cDomainIpPoolRowStatus=_H3cDomainIpPoolRowStatus_Object((1,3,6,1,4,1,2011,10,2,46,2,3,1,5),_H3cDomainIpPoolRowStatus_Type())
h3cDomainIpPoolRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:h3cDomainIpPoolRowStatus.setStatus(_A)
_H3cDomainStatTable_Object=MibTable
h3cDomainStatTable=_H3cDomainStatTable_Object((1,3,6,1,4,1,2011,10,2,46,2,4))
if mibBuilder.loadTexts:h3cDomainStatTable.setStatus(_A)
_H3cDomainStatEntry_Object=MibTableRow
h3cDomainStatEntry=_H3cDomainStatEntry_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1))
h3cDomainStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDomainStatEntry.setStatus(_A)
_H3cDomainAccessedNum_Type=Unsigned32
_H3cDomainAccessedNum_Object=MibTableColumn
h3cDomainAccessedNum=_H3cDomainAccessedNum_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,1),_H3cDomainAccessedNum_Type())
h3cDomainAccessedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainAccessedNum.setStatus(_A)
_H3cDomainOnlineNum_Type=Unsigned32
_H3cDomainOnlineNum_Object=MibTableColumn
h3cDomainOnlineNum=_H3cDomainOnlineNum_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,2),_H3cDomainOnlineNum_Type())
h3cDomainOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlineNum.setStatus(_A)
_H3cDomainOnlinePPPUser_Type=Unsigned32
_H3cDomainOnlinePPPUser_Object=MibTableColumn
h3cDomainOnlinePPPUser=_H3cDomainOnlinePPPUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,3),_H3cDomainOnlinePPPUser_Type())
h3cDomainOnlinePPPUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlinePPPUser.setStatus(_A)
_H3cDomainOnlineIPoEUser_Type=Unsigned32
_H3cDomainOnlineIPoEUser_Object=MibTableColumn
h3cDomainOnlineIPoEUser=_H3cDomainOnlineIPoEUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,4),_H3cDomainOnlineIPoEUser_Type())
h3cDomainOnlineIPoEUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlineIPoEUser.setStatus(_A)
_H3cDomainOnlinePPPoEUser_Type=Unsigned32
_H3cDomainOnlinePPPoEUser_Object=MibTableColumn
h3cDomainOnlinePPPoEUser=_H3cDomainOnlinePPPoEUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,5),_H3cDomainOnlinePPPoEUser_Type())
h3cDomainOnlinePPPoEUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlinePPPoEUser.setStatus(_A)
_H3cDomainOnlinePPPoAUser_Type=Unsigned32
_H3cDomainOnlinePPPoAUser_Object=MibTableColumn
h3cDomainOnlinePPPoAUser=_H3cDomainOnlinePPPoAUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,6),_H3cDomainOnlinePPPoAUser_Type())
h3cDomainOnlinePPPoAUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlinePPPoAUser.setStatus(_A)
_H3cDomainOnlinePPPoFRUser_Type=Unsigned32
_H3cDomainOnlinePPPoFRUser_Object=MibTableColumn
h3cDomainOnlinePPPoFRUser=_H3cDomainOnlinePPPoFRUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,7),_H3cDomainOnlinePPPoFRUser_Type())
h3cDomainOnlinePPPoFRUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlinePPPoFRUser.setStatus(_A)
_H3cDomainOnlineLacUser_Type=Unsigned32
_H3cDomainOnlineLacUser_Object=MibTableColumn
h3cDomainOnlineLacUser=_H3cDomainOnlineLacUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,8),_H3cDomainOnlineLacUser_Type())
h3cDomainOnlineLacUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlineLacUser.setStatus(_A)
_H3cDomainOnlineLnsUser_Type=Unsigned32
_H3cDomainOnlineLnsUser_Object=MibTableColumn
h3cDomainOnlineLnsUser=_H3cDomainOnlineLnsUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,9),_H3cDomainOnlineLnsUser_Type())
h3cDomainOnlineLnsUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlineLnsUser.setStatus(_A)
_H3cDomainOnlineIPoEBindAuthUser_Type=Unsigned32
_H3cDomainOnlineIPoEBindAuthUser_Object=MibTableColumn
h3cDomainOnlineIPoEBindAuthUser=_H3cDomainOnlineIPoEBindAuthUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,10),_H3cDomainOnlineIPoEBindAuthUser_Type())
h3cDomainOnlineIPoEBindAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlineIPoEBindAuthUser.setStatus(_A)
_H3cDomainOnlineIPoEWebAuthUser_Type=Unsigned32
_H3cDomainOnlineIPoEWebAuthUser_Object=MibTableColumn
h3cDomainOnlineIPoEWebAuthUser=_H3cDomainOnlineIPoEWebAuthUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,11),_H3cDomainOnlineIPoEWebAuthUser_Type())
h3cDomainOnlineIPoEWebAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlineIPoEWebAuthUser.setStatus(_A)
_H3cDomainOnlineLeasedUser_Type=Unsigned32
_H3cDomainOnlineLeasedUser_Object=MibTableColumn
h3cDomainOnlineLeasedUser=_H3cDomainOnlineLeasedUser_Object((1,3,6,1,4,1,2011,10,2,46,2,4,1,12),_H3cDomainOnlineLeasedUser_Type())
h3cDomainOnlineLeasedUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainOnlineLeasedUser.setStatus(_A)
_H3cDomainIPPoolStatTable_Object=MibTable
h3cDomainIPPoolStatTable=_H3cDomainIPPoolStatTable_Object((1,3,6,1,4,1,2011,10,2,46,2,5))
if mibBuilder.loadTexts:h3cDomainIPPoolStatTable.setStatus(_A)
_H3cDomainIPPoolStatEntry_Object=MibTableRow
h3cDomainIPPoolStatEntry=_H3cDomainIPPoolStatEntry_Object((1,3,6,1,4,1,2011,10,2,46,2,5,1))
h3cDomainIPPoolStatEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:h3cDomainIPPoolStatEntry.setStatus(_A)
_H3cDomainIPTotalNum_Type=Unsigned32
_H3cDomainIPTotalNum_Object=MibTableColumn
h3cDomainIPTotalNum=_H3cDomainIPTotalNum_Object((1,3,6,1,4,1,2011,10,2,46,2,5,1,1),_H3cDomainIPTotalNum_Type())
h3cDomainIPTotalNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIPTotalNum.setStatus(_A)
_H3cDomainIPUsedNum_Type=Unsigned32
_H3cDomainIPUsedNum_Object=MibTableColumn
h3cDomainIPUsedNum=_H3cDomainIPUsedNum_Object((1,3,6,1,4,1,2011,10,2,46,2,5,1,2),_H3cDomainIPUsedNum_Type())
h3cDomainIPUsedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIPUsedNum.setStatus(_A)
_H3cDomainIPConflictNum_Type=Unsigned32
_H3cDomainIPConflictNum_Object=MibTableColumn
h3cDomainIPConflictNum=_H3cDomainIPConflictNum_Object((1,3,6,1,4,1,2011,10,2,46,2,5,1,3),_H3cDomainIPConflictNum_Type())
h3cDomainIPConflictNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIPConflictNum.setStatus(_A)
_H3cDomainIPExcludeNum_Type=Unsigned32
_H3cDomainIPExcludeNum_Object=MibTableColumn
h3cDomainIPExcludeNum=_H3cDomainIPExcludeNum_Object((1,3,6,1,4,1,2011,10,2,46,2,5,1,4),_H3cDomainIPExcludeNum_Type())
h3cDomainIPExcludeNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIPExcludeNum.setStatus(_A)
_H3cDomainIPIdleNum_Type=Unsigned32
_H3cDomainIPIdleNum_Object=MibTableColumn
h3cDomainIPIdleNum=_H3cDomainIPIdleNum_Object((1,3,6,1,4,1,2011,10,2,46,2,5,1,5),_H3cDomainIPIdleNum_Type())
h3cDomainIPIdleNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIPIdleNum.setStatus(_A)
class _H3cDomainIPUsedPercent_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_H3cDomainIPUsedPercent_Type.__name__=_D
_H3cDomainIPUsedPercent_Object=MibTableColumn
h3cDomainIPUsedPercent=_H3cDomainIPUsedPercent_Object((1,3,6,1,4,1,2011,10,2,46,2,5,1,6),_H3cDomainIPUsedPercent_Type())
h3cDomainIPUsedPercent.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainIPUsedPercent.setStatus(_A)
_H3cDomainGlobalStat_ObjectIdentity=ObjectIdentity
h3cDomainGlobalStat=_H3cDomainGlobalStat_ObjectIdentity((1,3,6,1,4,1,2011,10,2,46,3))
_H3cDomainGlobalAccessedNum_Type=Unsigned32
_H3cDomainGlobalAccessedNum_Object=MibScalar
h3cDomainGlobalAccessedNum=_H3cDomainGlobalAccessedNum_Object((1,3,6,1,4,1,2011,10,2,46,3,1),_H3cDomainGlobalAccessedNum_Type())
h3cDomainGlobalAccessedNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalAccessedNum.setStatus(_A)
_H3cDomainGlobalOnlineNum_Type=Unsigned32
_H3cDomainGlobalOnlineNum_Object=MibScalar
h3cDomainGlobalOnlineNum=_H3cDomainGlobalOnlineNum_Object((1,3,6,1,4,1,2011,10,2,46,3,2),_H3cDomainGlobalOnlineNum_Type())
h3cDomainGlobalOnlineNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlineNum.setStatus(_A)
_H3cDomainGlobalOnlinePPPUser_Type=Unsigned32
_H3cDomainGlobalOnlinePPPUser_Object=MibScalar
h3cDomainGlobalOnlinePPPUser=_H3cDomainGlobalOnlinePPPUser_Object((1,3,6,1,4,1,2011,10,2,46,3,3),_H3cDomainGlobalOnlinePPPUser_Type())
h3cDomainGlobalOnlinePPPUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlinePPPUser.setStatus(_A)
_H3cDomainGlobalOnlineIPoEUser_Type=Unsigned32
_H3cDomainGlobalOnlineIPoEUser_Object=MibScalar
h3cDomainGlobalOnlineIPoEUser=_H3cDomainGlobalOnlineIPoEUser_Object((1,3,6,1,4,1,2011,10,2,46,3,4),_H3cDomainGlobalOnlineIPoEUser_Type())
h3cDomainGlobalOnlineIPoEUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlineIPoEUser.setStatus(_A)
_H3cDomainGlobalOnlinePPPoEUser_Type=Unsigned32
_H3cDomainGlobalOnlinePPPoEUser_Object=MibScalar
h3cDomainGlobalOnlinePPPoEUser=_H3cDomainGlobalOnlinePPPoEUser_Object((1,3,6,1,4,1,2011,10,2,46,3,5),_H3cDomainGlobalOnlinePPPoEUser_Type())
h3cDomainGlobalOnlinePPPoEUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlinePPPoEUser.setStatus(_A)
_H3cDomainGlobalOnlinePPPoAUser_Type=Unsigned32
_H3cDomainGlobalOnlinePPPoAUser_Object=MibScalar
h3cDomainGlobalOnlinePPPoAUser=_H3cDomainGlobalOnlinePPPoAUser_Object((1,3,6,1,4,1,2011,10,2,46,3,6),_H3cDomainGlobalOnlinePPPoAUser_Type())
h3cDomainGlobalOnlinePPPoAUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlinePPPoAUser.setStatus(_A)
_H3cDomainGlobalOnlinePPPoFRUser_Type=Unsigned32
_H3cDomainGlobalOnlinePPPoFRUser_Object=MibScalar
h3cDomainGlobalOnlinePPPoFRUser=_H3cDomainGlobalOnlinePPPoFRUser_Object((1,3,6,1,4,1,2011,10,2,46,3,7),_H3cDomainGlobalOnlinePPPoFRUser_Type())
h3cDomainGlobalOnlinePPPoFRUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlinePPPoFRUser.setStatus(_A)
_H3cDomainGlobalOnlineLacUser_Type=Unsigned32
_H3cDomainGlobalOnlineLacUser_Object=MibScalar
h3cDomainGlobalOnlineLacUser=_H3cDomainGlobalOnlineLacUser_Object((1,3,6,1,4,1,2011,10,2,46,3,8),_H3cDomainGlobalOnlineLacUser_Type())
h3cDomainGlobalOnlineLacUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlineLacUser.setStatus(_A)
_H3cDomainGlobalOnlineLnsUser_Type=Unsigned32
_H3cDomainGlobalOnlineLnsUser_Object=MibScalar
h3cDomainGlobalOnlineLnsUser=_H3cDomainGlobalOnlineLnsUser_Object((1,3,6,1,4,1,2011,10,2,46,3,9),_H3cDomainGlobalOnlineLnsUser_Type())
h3cDomainGlobalOnlineLnsUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlineLnsUser.setStatus(_A)
_H3cDomainGlobalOnlineIPoEBindAuthUser_Type=Unsigned32
_H3cDomainGlobalOnlineIPoEBindAuthUser_Object=MibScalar
h3cDomainGlobalOnlineIPoEBindAuthUser=_H3cDomainGlobalOnlineIPoEBindAuthUser_Object((1,3,6,1,4,1,2011,10,2,46,3,10),_H3cDomainGlobalOnlineIPoEBindAuthUser_Type())
h3cDomainGlobalOnlineIPoEBindAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlineIPoEBindAuthUser.setStatus(_A)
_H3cDomainGlobalOnlineIPoEWebAuthUser_Type=Unsigned32
_H3cDomainGlobalOnlineIPoEWebAuthUser_Object=MibScalar
h3cDomainGlobalOnlineIPoEWebAuthUser=_H3cDomainGlobalOnlineIPoEWebAuthUser_Object((1,3,6,1,4,1,2011,10,2,46,3,11),_H3cDomainGlobalOnlineIPoEWebAuthUser_Type())
h3cDomainGlobalOnlineIPoEWebAuthUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlineIPoEWebAuthUser.setStatus(_A)
_H3cDomainGlobalOnlineLeasedUser_Type=Unsigned32
_H3cDomainGlobalOnlineLeasedUser_Object=MibScalar
h3cDomainGlobalOnlineLeasedUser=_H3cDomainGlobalOnlineLeasedUser_Object((1,3,6,1,4,1,2011,10,2,46,3,12),_H3cDomainGlobalOnlineLeasedUser_Type())
h3cDomainGlobalOnlineLeasedUser.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDomainGlobalOnlineLeasedUser.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'H3cModeOfDomainScheme':H3cModeOfDomainScheme,'H3cAAATypeDomainScheme':H3cAAATypeDomainScheme,'H3cAccessModeofDomainScheme':H3cAccessModeofDomainScheme,'h3cDomain':h3cDomain,'h3cDomainControl':h3cDomainControl,'h3cDomainDefault':h3cDomainDefault,'h3cDomainTables':h3cDomainTables,'h3cDomainInfoTable':h3cDomainInfoTable,'h3cDomainInfoEntry':h3cDomainInfoEntry,_G:h3cDomainName,'h3cDomainState':h3cDomainState,'h3cDomainMaxAccessNum':h3cDomainMaxAccessNum,'h3cDomainVlanAssignMode':h3cDomainVlanAssignMode,'h3cDomainIdleCutEnable':h3cDomainIdleCutEnable,'h3cDomainIdleCutMaxTime':h3cDomainIdleCutMaxTime,'h3cDomainIdleCutMinFlow':h3cDomainIdleCutMinFlow,'h3cDomainMessengerEnable':h3cDomainMessengerEnable,'h3cDomainMessengerLimitTime':h3cDomainMessengerLimitTime,'h3cDomainMessengerSpanTime':h3cDomainMessengerSpanTime,'h3cDomainSelfServiceEnable':h3cDomainSelfServiceEnable,'h3cDomainSelfServiceURL':h3cDomainSelfServiceURL,'h3cDomainAccFailureAction':h3cDomainAccFailureAction,'h3cDomainRowStatus':h3cDomainRowStatus,'h3cDomainCurrentAccessNum':h3cDomainCurrentAccessNum,'h3cDomainIdleCutTime':h3cDomainIdleCutTime,'h3cDomainServiceType':h3cDomainServiceType,'h3cDomainIpPoolName':h3cDomainIpPoolName,'h3cDomainIpv6PoolName':h3cDomainIpv6PoolName,'h3cDomainSchemeTable':h3cDomainSchemeTable,'h3cDomainSchemeEntry':h3cDomainSchemeEntry,_I:h3cDomainSchemeIndex,'h3cDomainSchemeMode':h3cDomainSchemeMode,'h3cDomainAuthSchemeName':h3cDomainAuthSchemeName,'h3cDomainAcctSchemeName':h3cDomainAcctSchemeName,'h3cDomainSchemeRowStatus':h3cDomainSchemeRowStatus,'h3cDomainSchemeAAAType':h3cDomainSchemeAAAType,'h3cDomainSchemeAAAName':h3cDomainSchemeAAAName,'h3cDomainSchemeAccessMode':h3cDomainSchemeAccessMode,'h3cDomainIpPoolTable':h3cDomainIpPoolTable,'h3cDomainIpPoolEntry':h3cDomainIpPoolEntry,_J:h3cDomainIpPoolNum,'h3cDomainIpPoolLowIpAddrType':h3cDomainIpPoolLowIpAddrType,'h3cDomainIpPoolLowIpAddr':h3cDomainIpPoolLowIpAddr,'h3cDomainIpPoolLen':h3cDomainIpPoolLen,'h3cDomainIpPoolRowStatus':h3cDomainIpPoolRowStatus,'h3cDomainStatTable':h3cDomainStatTable,'h3cDomainStatEntry':h3cDomainStatEntry,'h3cDomainAccessedNum':h3cDomainAccessedNum,'h3cDomainOnlineNum':h3cDomainOnlineNum,'h3cDomainOnlinePPPUser':h3cDomainOnlinePPPUser,'h3cDomainOnlineIPoEUser':h3cDomainOnlineIPoEUser,'h3cDomainOnlinePPPoEUser':h3cDomainOnlinePPPoEUser,'h3cDomainOnlinePPPoAUser':h3cDomainOnlinePPPoAUser,'h3cDomainOnlinePPPoFRUser':h3cDomainOnlinePPPoFRUser,'h3cDomainOnlineLacUser':h3cDomainOnlineLacUser,'h3cDomainOnlineLnsUser':h3cDomainOnlineLnsUser,'h3cDomainOnlineIPoEBindAuthUser':h3cDomainOnlineIPoEBindAuthUser,'h3cDomainOnlineIPoEWebAuthUser':h3cDomainOnlineIPoEWebAuthUser,'h3cDomainOnlineLeasedUser':h3cDomainOnlineLeasedUser,'h3cDomainIPPoolStatTable':h3cDomainIPPoolStatTable,'h3cDomainIPPoolStatEntry':h3cDomainIPPoolStatEntry,'h3cDomainIPTotalNum':h3cDomainIPTotalNum,'h3cDomainIPUsedNum':h3cDomainIPUsedNum,'h3cDomainIPConflictNum':h3cDomainIPConflictNum,'h3cDomainIPExcludeNum':h3cDomainIPExcludeNum,'h3cDomainIPIdleNum':h3cDomainIPIdleNum,'h3cDomainIPUsedPercent':h3cDomainIPUsedPercent,'h3cDomainGlobalStat':h3cDomainGlobalStat,'h3cDomainGlobalAccessedNum':h3cDomainGlobalAccessedNum,'h3cDomainGlobalOnlineNum':h3cDomainGlobalOnlineNum,'h3cDomainGlobalOnlinePPPUser':h3cDomainGlobalOnlinePPPUser,'h3cDomainGlobalOnlineIPoEUser':h3cDomainGlobalOnlineIPoEUser,'h3cDomainGlobalOnlinePPPoEUser':h3cDomainGlobalOnlinePPPoEUser,'h3cDomainGlobalOnlinePPPoAUser':h3cDomainGlobalOnlinePPPoAUser,'h3cDomainGlobalOnlinePPPoFRUser':h3cDomainGlobalOnlinePPPoFRUser,'h3cDomainGlobalOnlineLacUser':h3cDomainGlobalOnlineLacUser,'h3cDomainGlobalOnlineLnsUser':h3cDomainGlobalOnlineLnsUser,'h3cDomainGlobalOnlineIPoEBindAuthUser':h3cDomainGlobalOnlineIPoEBindAuthUser,'h3cDomainGlobalOnlineIPoEWebAuthUser':h3cDomainGlobalOnlineIPoEWebAuthUser,'h3cDomainGlobalOnlineLeasedUser':h3cDomainGlobalOnlineLeasedUser})