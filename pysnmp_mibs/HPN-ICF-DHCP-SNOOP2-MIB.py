_T='hpnicfDhcpSnoop2IfVlanRIDVlanIndex'
_S='hpnicfDhcpSnoop2IfVlanCIDVlanIndex'
_R='normal'
_Q='hpnicfDhcpSnoop2BindSecVlanId'
_P='hpnicfDhcpSnoop2BindVlanId'
_O='hpnicfDhcpSnoop2BindIpAddr'
_N='sysname'
_M='userDefine'
_L='ifIndex'
_K='IF-MIB'
_J='not-accessible'
_I='read-create'
_H='HPN-ICF-DHCP-SNOOP2-MIB'
_G='read-only'
_F='TruthValue'
_E='OctetString'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_K,'InterfaceIndexOrZero',_L)
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
hpnicfDhcpSnoop2=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,124))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2.setRevisions(('2013-04-15 00:00',))
_HpnicfDhcpSnoop2ScalarObjects_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoop2ScalarObjects=_HpnicfDhcpSnoop2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,124,1))
_HpnicfDhcpSnoop2ConfigGroup_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoop2ConfigGroup=_HpnicfDhcpSnoop2ConfigGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,124,1,1))
class _HpnicfDhcpSnoop2Enabled_Type(TruthValue):defaultValue=2
_HpnicfDhcpSnoop2Enabled_Type.__name__=_F
_HpnicfDhcpSnoop2Enabled_Object=MibScalar
hpnicfDhcpSnoop2Enabled=_HpnicfDhcpSnoop2Enabled_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,1,1,1),_HpnicfDhcpSnoop2Enabled_Type())
hpnicfDhcpSnoop2Enabled.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2Enabled.setStatus(_A)
class _HpnicfDhcpSnoop2BindDbName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_HpnicfDhcpSnoop2BindDbName_Type.__name__=_E
_HpnicfDhcpSnoop2BindDbName_Object=MibScalar
hpnicfDhcpSnoop2BindDbName=_HpnicfDhcpSnoop2BindDbName_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,1,1,2),_HpnicfDhcpSnoop2BindDbName_Type())
hpnicfDhcpSnoop2BindDbName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindDbName.setStatus(_A)
class _HpnicfDhcpSnoop2BindRefreshIntvl_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,864000))
_HpnicfDhcpSnoop2BindRefreshIntvl_Type.__name__=_D
_HpnicfDhcpSnoop2BindRefreshIntvl_Object=MibScalar
hpnicfDhcpSnoop2BindRefreshIntvl=_HpnicfDhcpSnoop2BindRefreshIntvl_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,1,1,3),_HpnicfDhcpSnoop2BindRefreshIntvl_Type())
hpnicfDhcpSnoop2BindRefreshIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindRefreshIntvl.setStatus(_A)
class _HpnicfDhcpSnoop2BindRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('on',1))
_HpnicfDhcpSnoop2BindRefresh_Type.__name__=_C
_HpnicfDhcpSnoop2BindRefresh_Object=MibScalar
hpnicfDhcpSnoop2BindRefresh=_HpnicfDhcpSnoop2BindRefresh_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,1,1,4),_HpnicfDhcpSnoop2BindRefresh_Type())
hpnicfDhcpSnoop2BindRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindRefresh.setStatus(_A)
_HpnicfDhcpSnoop2StatisticsGroup_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoop2StatisticsGroup=_HpnicfDhcpSnoop2StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,124,1,2))
_HpnicfDhcpSnoop2PktSentNum_Type=Counter64
_HpnicfDhcpSnoop2PktSentNum_Object=MibScalar
hpnicfDhcpSnoop2PktSentNum=_HpnicfDhcpSnoop2PktSentNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,1,2,1),_HpnicfDhcpSnoop2PktSentNum_Type())
hpnicfDhcpSnoop2PktSentNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2PktSentNum.setStatus(_A)
_HpnicfDhcpSnoop2PktRcvNum_Type=Counter64
_HpnicfDhcpSnoop2PktRcvNum_Object=MibScalar
hpnicfDhcpSnoop2PktRcvNum=_HpnicfDhcpSnoop2PktRcvNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,1,2,2),_HpnicfDhcpSnoop2PktRcvNum_Type())
hpnicfDhcpSnoop2PktRcvNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2PktRcvNum.setStatus(_A)
_HpnicfDhcpSnoop2PktDropNum_Type=Counter64
_HpnicfDhcpSnoop2PktDropNum_Object=MibScalar
hpnicfDhcpSnoop2PktDropNum=_HpnicfDhcpSnoop2PktDropNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,1,2,3),_HpnicfDhcpSnoop2PktDropNum_Type())
hpnicfDhcpSnoop2PktDropNum.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2PktDropNum.setStatus(_A)
_HpnicfDhcpSnoop2Tables_ObjectIdentity=ObjectIdentity
hpnicfDhcpSnoop2Tables=_HpnicfDhcpSnoop2Tables_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,124,2))
_HpnicfDhcpSnoop2BindTable_Object=MibTable
hpnicfDhcpSnoop2BindTable=_HpnicfDhcpSnoop2BindTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindTable.setStatus(_A)
_HpnicfDhcpSnoop2BindEntry_Object=MibTableRow
hpnicfDhcpSnoop2BindEntry=_HpnicfDhcpSnoop2BindEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1))
hpnicfDhcpSnoop2BindEntry.setIndexNames((0,_H,_O),(0,_H,_P),(0,_H,_Q))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindEntry.setStatus(_A)
_HpnicfDhcpSnoop2BindIpAddr_Type=InetAddressIPv4
_HpnicfDhcpSnoop2BindIpAddr_Object=MibTableColumn
hpnicfDhcpSnoop2BindIpAddr=_HpnicfDhcpSnoop2BindIpAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1,1),_HpnicfDhcpSnoop2BindIpAddr_Type())
hpnicfDhcpSnoop2BindIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindIpAddr.setStatus(_A)
class _HpnicfDhcpSnoop2BindVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfDhcpSnoop2BindVlanId_Type.__name__=_D
_HpnicfDhcpSnoop2BindVlanId_Object=MibTableColumn
hpnicfDhcpSnoop2BindVlanId=_HpnicfDhcpSnoop2BindVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1,2),_HpnicfDhcpSnoop2BindVlanId_Type())
hpnicfDhcpSnoop2BindVlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindVlanId.setStatus(_A)
class _HpnicfDhcpSnoop2BindSecVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_HpnicfDhcpSnoop2BindSecVlanId_Type.__name__=_D
_HpnicfDhcpSnoop2BindSecVlanId_Object=MibTableColumn
hpnicfDhcpSnoop2BindSecVlanId=_HpnicfDhcpSnoop2BindSecVlanId_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1,3),_HpnicfDhcpSnoop2BindSecVlanId_Type())
hpnicfDhcpSnoop2BindSecVlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindSecVlanId.setStatus(_A)
_HpnicfDhcpSnoop2BindMacAddr_Type=MacAddress
_HpnicfDhcpSnoop2BindMacAddr_Object=MibTableColumn
hpnicfDhcpSnoop2BindMacAddr=_HpnicfDhcpSnoop2BindMacAddr_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1,4),_HpnicfDhcpSnoop2BindMacAddr_Type())
hpnicfDhcpSnoop2BindMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindMacAddr.setStatus(_A)
_HpnicfDhcpSnoop2BindLease_Type=Unsigned32
_HpnicfDhcpSnoop2BindLease_Object=MibTableColumn
hpnicfDhcpSnoop2BindLease=_HpnicfDhcpSnoop2BindLease_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1,5),_HpnicfDhcpSnoop2BindLease_Type())
hpnicfDhcpSnoop2BindLease.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindLease.setStatus(_A)
_HpnicfDhcpSnoop2BindPortIndex_Type=InterfaceIndexOrZero
_HpnicfDhcpSnoop2BindPortIndex_Object=MibTableColumn
hpnicfDhcpSnoop2BindPortIndex=_HpnicfDhcpSnoop2BindPortIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1,6),_HpnicfDhcpSnoop2BindPortIndex_Type())
hpnicfDhcpSnoop2BindPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindPortIndex.setStatus(_A)
_HpnicfDhcpSnoop2BindRowStatus_Type=RowStatus
_HpnicfDhcpSnoop2BindRowStatus_Object=MibTableColumn
hpnicfDhcpSnoop2BindRowStatus=_HpnicfDhcpSnoop2BindRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,1,1,7),_HpnicfDhcpSnoop2BindRowStatus_Type())
hpnicfDhcpSnoop2BindRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2BindRowStatus.setStatus(_A)
_HpnicfDhcpSnoop2IfConfigTable_Object=MibTable
hpnicfDhcpSnoop2IfConfigTable=_HpnicfDhcpSnoop2IfConfigTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfConfigTable.setStatus(_A)
_HpnicfDhcpSnoop2IfConfigEntry_Object=MibTableRow
hpnicfDhcpSnoop2IfConfigEntry=_HpnicfDhcpSnoop2IfConfigEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1))
hpnicfDhcpSnoop2IfConfigEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfConfigEntry.setStatus(_A)
class _HpnicfDhcpSnoop2IfTrustStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
_HpnicfDhcpSnoop2IfTrustStatus_Type.__name__=_C
_HpnicfDhcpSnoop2IfTrustStatus_Object=MibTableColumn
hpnicfDhcpSnoop2IfTrustStatus=_HpnicfDhcpSnoop2IfTrustStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,1),_HpnicfDhcpSnoop2IfTrustStatus_Type())
hpnicfDhcpSnoop2IfTrustStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfTrustStatus.setStatus(_A)
class _HpnicfDhcpSnoop2IfCheckMac_Type(TruthValue):defaultValue=2
_HpnicfDhcpSnoop2IfCheckMac_Type.__name__=_F
_HpnicfDhcpSnoop2IfCheckMac_Object=MibTableColumn
hpnicfDhcpSnoop2IfCheckMac=_HpnicfDhcpSnoop2IfCheckMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,2),_HpnicfDhcpSnoop2IfCheckMac_Type())
hpnicfDhcpSnoop2IfCheckMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfCheckMac.setStatus(_A)
class _HpnicfDhcpSnoop2IfCheckRequest_Type(TruthValue):defaultValue=2
_HpnicfDhcpSnoop2IfCheckRequest_Type.__name__=_F
_HpnicfDhcpSnoop2IfCheckRequest_Object=MibTableColumn
hpnicfDhcpSnoop2IfCheckRequest=_HpnicfDhcpSnoop2IfCheckRequest_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,3),_HpnicfDhcpSnoop2IfCheckRequest_Type())
hpnicfDhcpSnoop2IfCheckRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfCheckRequest.setStatus(_A)
class _HpnicfDhcpSnoop2IfRateLimit_Type(Unsigned32):defaultValue=0
_HpnicfDhcpSnoop2IfRateLimit_Type.__name__=_D
_HpnicfDhcpSnoop2IfRateLimit_Object=MibTableColumn
hpnicfDhcpSnoop2IfRateLimit=_HpnicfDhcpSnoop2IfRateLimit_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,4),_HpnicfDhcpSnoop2IfRateLimit_Type())
hpnicfDhcpSnoop2IfRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfRateLimit.setStatus(_A)
class _HpnicfDhcpSnoop2IfRecordBind_Type(TruthValue):defaultValue=2
_HpnicfDhcpSnoop2IfRecordBind_Type.__name__=_F
_HpnicfDhcpSnoop2IfRecordBind_Object=MibTableColumn
hpnicfDhcpSnoop2IfRecordBind=_HpnicfDhcpSnoop2IfRecordBind_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,5),_HpnicfDhcpSnoop2IfRecordBind_Type())
hpnicfDhcpSnoop2IfRecordBind.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfRecordBind.setStatus(_A)
class _HpnicfDhcpSnoop2IfMaxLearnNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_HpnicfDhcpSnoop2IfMaxLearnNum_Type.__name__=_D
_HpnicfDhcpSnoop2IfMaxLearnNum_Object=MibTableColumn
hpnicfDhcpSnoop2IfMaxLearnNum=_HpnicfDhcpSnoop2IfMaxLearnNum_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,6),_HpnicfDhcpSnoop2IfMaxLearnNum_Type())
hpnicfDhcpSnoop2IfMaxLearnNum.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfMaxLearnNum.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82Enable_Type(TruthValue):defaultValue=2
_HpnicfDhcpSnoop2IfOpt82Enable_Type.__name__=_F
_HpnicfDhcpSnoop2IfOpt82Enable_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82Enable=_HpnicfDhcpSnoop2IfOpt82Enable_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,7),_HpnicfDhcpSnoop2IfOpt82Enable_Type())
hpnicfDhcpSnoop2IfOpt82Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82Enable.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82Strategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),('replace',3)))
_HpnicfDhcpSnoop2IfOpt82Strategy_Type.__name__=_C
_HpnicfDhcpSnoop2IfOpt82Strategy_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82Strategy=_HpnicfDhcpSnoop2IfOpt82Strategy_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,8),_HpnicfDhcpSnoop2IfOpt82Strategy_Type())
hpnicfDhcpSnoop2IfOpt82Strategy.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82Strategy.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82CIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),('verbose',2),(_M,3)))
_HpnicfDhcpSnoop2IfOpt82CIDMode_Type.__name__=_C
_HpnicfDhcpSnoop2IfOpt82CIDMode_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDMode=_HpnicfDhcpSnoop2IfOpt82CIDMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,9),_HpnicfDhcpSnoop2IfOpt82CIDMode_Type())
hpnicfDhcpSnoop2IfOpt82CIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82CIDMode.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82CIDNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalid',1),('mac',2),(_N,3),(_M,4)))
_HpnicfDhcpSnoop2IfOpt82CIDNodeType_Type.__name__=_C
_HpnicfDhcpSnoop2IfOpt82CIDNodeType_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDNodeType=_HpnicfDhcpSnoop2IfOpt82CIDNodeType_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,10),_HpnicfDhcpSnoop2IfOpt82CIDNodeType_Type())
hpnicfDhcpSnoop2IfOpt82CIDNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82CIDNodeType.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Type.__name__=_E
_HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDNodeStr=_HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,11),_HpnicfDhcpSnoop2IfOpt82CIDNodeStr_Type())
hpnicfDhcpSnoop2IfOpt82CIDNodeStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82CIDNodeStr.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82CIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(3,63))
_HpnicfDhcpSnoop2IfOpt82CIDStr_Type.__name__=_E
_HpnicfDhcpSnoop2IfOpt82CIDStr_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDStr=_HpnicfDhcpSnoop2IfOpt82CIDStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,12),_HpnicfDhcpSnoop2IfOpt82CIDStr_Type())
hpnicfDhcpSnoop2IfOpt82CIDStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82CIDStr.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82CIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hex',1),('ascii',2),('undefine',3)))
_HpnicfDhcpSnoop2IfOpt82CIDFormat_Type.__name__=_C
_HpnicfDhcpSnoop2IfOpt82CIDFormat_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82CIDFormat=_HpnicfDhcpSnoop2IfOpt82CIDFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,13),_HpnicfDhcpSnoop2IfOpt82CIDFormat_Type())
hpnicfDhcpSnoop2IfOpt82CIDFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82CIDFormat.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82RIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_N,2),(_M,3)))
_HpnicfDhcpSnoop2IfOpt82RIDMode_Type.__name__=_C
_HpnicfDhcpSnoop2IfOpt82RIDMode_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82RIDMode=_HpnicfDhcpSnoop2IfOpt82RIDMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,14),_HpnicfDhcpSnoop2IfOpt82RIDMode_Type())
hpnicfDhcpSnoop2IfOpt82RIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82RIDMode.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82RIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfDhcpSnoop2IfOpt82RIDStr_Type.__name__=_E
_HpnicfDhcpSnoop2IfOpt82RIDStr_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82RIDStr=_HpnicfDhcpSnoop2IfOpt82RIDStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,15),_HpnicfDhcpSnoop2IfOpt82RIDStr_Type())
hpnicfDhcpSnoop2IfOpt82RIDStr.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82RIDStr.setStatus(_A)
class _HpnicfDhcpSnoop2IfOpt82RIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hex',1),('ascii',2)))
_HpnicfDhcpSnoop2IfOpt82RIDFormat_Type.__name__=_C
_HpnicfDhcpSnoop2IfOpt82RIDFormat_Object=MibTableColumn
hpnicfDhcpSnoop2IfOpt82RIDFormat=_HpnicfDhcpSnoop2IfOpt82RIDFormat_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,2,1,16),_HpnicfDhcpSnoop2IfOpt82RIDFormat_Type())
hpnicfDhcpSnoop2IfOpt82RIDFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfOpt82RIDFormat.setStatus(_A)
_HpnicfDhcpSnoop2IfVlanCIDTable_Object=MibTable
hpnicfDhcpSnoop2IfVlanCIDTable=_HpnicfDhcpSnoop2IfVlanCIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,3))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanCIDTable.setStatus(_A)
_HpnicfDhcpSnoop2IfVlanCIDEntry_Object=MibTableRow
hpnicfDhcpSnoop2IfVlanCIDEntry=_HpnicfDhcpSnoop2IfVlanCIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,3,1))
hpnicfDhcpSnoop2IfVlanCIDEntry.setIndexNames((0,_K,_L),(0,_H,_S))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanCIDEntry.setStatus(_A)
class _HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Type.__name__=_D
_HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Object=MibTableColumn
hpnicfDhcpSnoop2IfVlanCIDVlanIndex=_HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,3,1,1),_HpnicfDhcpSnoop2IfVlanCIDVlanIndex_Type())
hpnicfDhcpSnoop2IfVlanCIDVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanCIDVlanIndex.setStatus(_A)
class _HpnicfDhcpSnoop2IfVlanCIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,63))
_HpnicfDhcpSnoop2IfVlanCIDStr_Type.__name__=_E
_HpnicfDhcpSnoop2IfVlanCIDStr_Object=MibTableColumn
hpnicfDhcpSnoop2IfVlanCIDStr=_HpnicfDhcpSnoop2IfVlanCIDStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,3,1,2),_HpnicfDhcpSnoop2IfVlanCIDStr_Type())
hpnicfDhcpSnoop2IfVlanCIDStr.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanCIDStr.setStatus(_A)
_HpnicfDhcpSnoop2IfVlanCIDRowStatus_Type=RowStatus
_HpnicfDhcpSnoop2IfVlanCIDRowStatus_Object=MibTableColumn
hpnicfDhcpSnoop2IfVlanCIDRowStatus=_HpnicfDhcpSnoop2IfVlanCIDRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,3,1,3),_HpnicfDhcpSnoop2IfVlanCIDRowStatus_Type())
hpnicfDhcpSnoop2IfVlanCIDRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanCIDRowStatus.setStatus(_A)
_HpnicfDhcpSnoop2IfVlanRIDTable_Object=MibTable
hpnicfDhcpSnoop2IfVlanRIDTable=_HpnicfDhcpSnoop2IfVlanRIDTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,4))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanRIDTable.setStatus(_A)
_HpnicfDhcpSnoop2IfVlanRIDEntry_Object=MibTableRow
hpnicfDhcpSnoop2IfVlanRIDEntry=_HpnicfDhcpSnoop2IfVlanRIDEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,4,1))
hpnicfDhcpSnoop2IfVlanRIDEntry.setIndexNames((0,_K,_L),(0,_H,_T))
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanRIDEntry.setStatus(_A)
class _HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Type.__name__=_D
_HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Object=MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDVlanIndex=_HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,4,1,1),_HpnicfDhcpSnoop2IfVlanRIDVlanIndex_Type())
hpnicfDhcpSnoop2IfVlanRIDVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanRIDVlanIndex.setStatus(_A)
class _HpnicfDhcpSnoop2IfVlanRIDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_HpnicfDhcpSnoop2IfVlanRIDMode_Type.__name__=_C
_HpnicfDhcpSnoop2IfVlanRIDMode_Object=MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDMode=_HpnicfDhcpSnoop2IfVlanRIDMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,4,1,2),_HpnicfDhcpSnoop2IfVlanRIDMode_Type())
hpnicfDhcpSnoop2IfVlanRIDMode.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanRIDMode.setStatus(_A)
class _HpnicfDhcpSnoop2IfVlanRIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_HpnicfDhcpSnoop2IfVlanRIDStr_Type.__name__=_E
_HpnicfDhcpSnoop2IfVlanRIDStr_Object=MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDStr=_HpnicfDhcpSnoop2IfVlanRIDStr_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,4,1,3),_HpnicfDhcpSnoop2IfVlanRIDStr_Type())
hpnicfDhcpSnoop2IfVlanRIDStr.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanRIDStr.setStatus(_A)
_HpnicfDhcpSnoop2IfVlanRIDRowStatus_Type=RowStatus
_HpnicfDhcpSnoop2IfVlanRIDRowStatus_Object=MibTableColumn
hpnicfDhcpSnoop2IfVlanRIDRowStatus=_HpnicfDhcpSnoop2IfVlanRIDRowStatus_Object((1,3,6,1,4,1,11,2,14,11,15,2,124,2,4,1,4),_HpnicfDhcpSnoop2IfVlanRIDRowStatus_Type())
hpnicfDhcpSnoop2IfVlanRIDRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:hpnicfDhcpSnoop2IfVlanRIDRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'hpnicfDhcpSnoop2':hpnicfDhcpSnoop2,'hpnicfDhcpSnoop2ScalarObjects':hpnicfDhcpSnoop2ScalarObjects,'hpnicfDhcpSnoop2ConfigGroup':hpnicfDhcpSnoop2ConfigGroup,'hpnicfDhcpSnoop2Enabled':hpnicfDhcpSnoop2Enabled,'hpnicfDhcpSnoop2BindDbName':hpnicfDhcpSnoop2BindDbName,'hpnicfDhcpSnoop2BindRefreshIntvl':hpnicfDhcpSnoop2BindRefreshIntvl,'hpnicfDhcpSnoop2BindRefresh':hpnicfDhcpSnoop2BindRefresh,'hpnicfDhcpSnoop2StatisticsGroup':hpnicfDhcpSnoop2StatisticsGroup,'hpnicfDhcpSnoop2PktSentNum':hpnicfDhcpSnoop2PktSentNum,'hpnicfDhcpSnoop2PktRcvNum':hpnicfDhcpSnoop2PktRcvNum,'hpnicfDhcpSnoop2PktDropNum':hpnicfDhcpSnoop2PktDropNum,'hpnicfDhcpSnoop2Tables':hpnicfDhcpSnoop2Tables,'hpnicfDhcpSnoop2BindTable':hpnicfDhcpSnoop2BindTable,'hpnicfDhcpSnoop2BindEntry':hpnicfDhcpSnoop2BindEntry,_O:hpnicfDhcpSnoop2BindIpAddr,_P:hpnicfDhcpSnoop2BindVlanId,_Q:hpnicfDhcpSnoop2BindSecVlanId,'hpnicfDhcpSnoop2BindMacAddr':hpnicfDhcpSnoop2BindMacAddr,'hpnicfDhcpSnoop2BindLease':hpnicfDhcpSnoop2BindLease,'hpnicfDhcpSnoop2BindPortIndex':hpnicfDhcpSnoop2BindPortIndex,'hpnicfDhcpSnoop2BindRowStatus':hpnicfDhcpSnoop2BindRowStatus,'hpnicfDhcpSnoop2IfConfigTable':hpnicfDhcpSnoop2IfConfigTable,'hpnicfDhcpSnoop2IfConfigEntry':hpnicfDhcpSnoop2IfConfigEntry,'hpnicfDhcpSnoop2IfTrustStatus':hpnicfDhcpSnoop2IfTrustStatus,'hpnicfDhcpSnoop2IfCheckMac':hpnicfDhcpSnoop2IfCheckMac,'hpnicfDhcpSnoop2IfCheckRequest':hpnicfDhcpSnoop2IfCheckRequest,'hpnicfDhcpSnoop2IfRateLimit':hpnicfDhcpSnoop2IfRateLimit,'hpnicfDhcpSnoop2IfRecordBind':hpnicfDhcpSnoop2IfRecordBind,'hpnicfDhcpSnoop2IfMaxLearnNum':hpnicfDhcpSnoop2IfMaxLearnNum,'hpnicfDhcpSnoop2IfOpt82Enable':hpnicfDhcpSnoop2IfOpt82Enable,'hpnicfDhcpSnoop2IfOpt82Strategy':hpnicfDhcpSnoop2IfOpt82Strategy,'hpnicfDhcpSnoop2IfOpt82CIDMode':hpnicfDhcpSnoop2IfOpt82CIDMode,'hpnicfDhcpSnoop2IfOpt82CIDNodeType':hpnicfDhcpSnoop2IfOpt82CIDNodeType,'hpnicfDhcpSnoop2IfOpt82CIDNodeStr':hpnicfDhcpSnoop2IfOpt82CIDNodeStr,'hpnicfDhcpSnoop2IfOpt82CIDStr':hpnicfDhcpSnoop2IfOpt82CIDStr,'hpnicfDhcpSnoop2IfOpt82CIDFormat':hpnicfDhcpSnoop2IfOpt82CIDFormat,'hpnicfDhcpSnoop2IfOpt82RIDMode':hpnicfDhcpSnoop2IfOpt82RIDMode,'hpnicfDhcpSnoop2IfOpt82RIDStr':hpnicfDhcpSnoop2IfOpt82RIDStr,'hpnicfDhcpSnoop2IfOpt82RIDFormat':hpnicfDhcpSnoop2IfOpt82RIDFormat,'hpnicfDhcpSnoop2IfVlanCIDTable':hpnicfDhcpSnoop2IfVlanCIDTable,'hpnicfDhcpSnoop2IfVlanCIDEntry':hpnicfDhcpSnoop2IfVlanCIDEntry,_S:hpnicfDhcpSnoop2IfVlanCIDVlanIndex,'hpnicfDhcpSnoop2IfVlanCIDStr':hpnicfDhcpSnoop2IfVlanCIDStr,'hpnicfDhcpSnoop2IfVlanCIDRowStatus':hpnicfDhcpSnoop2IfVlanCIDRowStatus,'hpnicfDhcpSnoop2IfVlanRIDTable':hpnicfDhcpSnoop2IfVlanRIDTable,'hpnicfDhcpSnoop2IfVlanRIDEntry':hpnicfDhcpSnoop2IfVlanRIDEntry,_T:hpnicfDhcpSnoop2IfVlanRIDVlanIndex,'hpnicfDhcpSnoop2IfVlanRIDMode':hpnicfDhcpSnoop2IfVlanRIDMode,'hpnicfDhcpSnoop2IfVlanRIDStr':hpnicfDhcpSnoop2IfVlanRIDStr,'hpnicfDhcpSnoop2IfVlanRIDRowStatus':hpnicfDhcpSnoop2IfVlanRIDRowStatus})