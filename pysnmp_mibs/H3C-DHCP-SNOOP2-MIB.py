_T='h3cDhcpSnoop2IfVlanRIDVlanIndex'
_S='h3cDhcpSnoop2IfVlanCIDVlanIndex'
_R='normal'
_Q='h3cDhcpSnoop2BindSecVlanId'
_P='h3cDhcpSnoop2BindVlanId'
_O='h3cDhcpSnoop2BindIpAddr'
_N='sysname'
_M='userDefine'
_L='ifIndex'
_K='IF-MIB'
_J='not-accessible'
_I='read-create'
_H='H3C-DHCP-SNOOP2-MIB'
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
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_K,'InterfaceIndexOrZero',_L)
InetAddressIPv4,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention',_F)
h3cDhcpSnoop2=ModuleIdentity((1,3,6,1,4,1,2011,10,2,124))
if mibBuilder.loadTexts:h3cDhcpSnoop2.setRevisions(('2017-01-13 00:00','2013-04-15 00:00'))
_H3cDhcpSnoop2ScalarObjects_ObjectIdentity=ObjectIdentity
h3cDhcpSnoop2ScalarObjects=_H3cDhcpSnoop2ScalarObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,124,1))
_H3cDhcpSnoop2ConfigGroup_ObjectIdentity=ObjectIdentity
h3cDhcpSnoop2ConfigGroup=_H3cDhcpSnoop2ConfigGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,124,1,1))
class _H3cDhcpSnoop2Enabled_Type(TruthValue):defaultValue=2
_H3cDhcpSnoop2Enabled_Type.__name__=_F
_H3cDhcpSnoop2Enabled_Object=MibScalar
h3cDhcpSnoop2Enabled=_H3cDhcpSnoop2Enabled_Object((1,3,6,1,4,1,2011,10,2,124,1,1,1),_H3cDhcpSnoop2Enabled_Type())
h3cDhcpSnoop2Enabled.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2Enabled.setStatus(_A)
class _H3cDhcpSnoop2BindDbName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_H3cDhcpSnoop2BindDbName_Type.__name__=_E
_H3cDhcpSnoop2BindDbName_Object=MibScalar
h3cDhcpSnoop2BindDbName=_H3cDhcpSnoop2BindDbName_Object((1,3,6,1,4,1,2011,10,2,124,1,1,2),_H3cDhcpSnoop2BindDbName_Type())
h3cDhcpSnoop2BindDbName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindDbName.setStatus(_A)
class _H3cDhcpSnoop2BindRefreshIntvl_Type(Unsigned32):defaultValue=300;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,864000))
_H3cDhcpSnoop2BindRefreshIntvl_Type.__name__=_D
_H3cDhcpSnoop2BindRefreshIntvl_Object=MibScalar
h3cDhcpSnoop2BindRefreshIntvl=_H3cDhcpSnoop2BindRefreshIntvl_Object((1,3,6,1,4,1,2011,10,2,124,1,1,3),_H3cDhcpSnoop2BindRefreshIntvl_Type())
h3cDhcpSnoop2BindRefreshIntvl.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindRefreshIntvl.setStatus(_A)
class _H3cDhcpSnoop2BindRefresh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('on',1))
_H3cDhcpSnoop2BindRefresh_Type.__name__=_C
_H3cDhcpSnoop2BindRefresh_Object=MibScalar
h3cDhcpSnoop2BindRefresh=_H3cDhcpSnoop2BindRefresh_Object((1,3,6,1,4,1,2011,10,2,124,1,1,4),_H3cDhcpSnoop2BindRefresh_Type())
h3cDhcpSnoop2BindRefresh.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindRefresh.setStatus(_A)
_H3cDhcpSnoop2StatisticsGroup_ObjectIdentity=ObjectIdentity
h3cDhcpSnoop2StatisticsGroup=_H3cDhcpSnoop2StatisticsGroup_ObjectIdentity((1,3,6,1,4,1,2011,10,2,124,1,2))
_H3cDhcpSnoop2PktSentNum_Type=Counter64
_H3cDhcpSnoop2PktSentNum_Object=MibScalar
h3cDhcpSnoop2PktSentNum=_H3cDhcpSnoop2PktSentNum_Object((1,3,6,1,4,1,2011,10,2,124,1,2,1),_H3cDhcpSnoop2PktSentNum_Type())
h3cDhcpSnoop2PktSentNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoop2PktSentNum.setStatus(_A)
_H3cDhcpSnoop2PktRcvNum_Type=Counter64
_H3cDhcpSnoop2PktRcvNum_Object=MibScalar
h3cDhcpSnoop2PktRcvNum=_H3cDhcpSnoop2PktRcvNum_Object((1,3,6,1,4,1,2011,10,2,124,1,2,2),_H3cDhcpSnoop2PktRcvNum_Type())
h3cDhcpSnoop2PktRcvNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoop2PktRcvNum.setStatus(_A)
_H3cDhcpSnoop2PktDropNum_Type=Counter64
_H3cDhcpSnoop2PktDropNum_Object=MibScalar
h3cDhcpSnoop2PktDropNum=_H3cDhcpSnoop2PktDropNum_Object((1,3,6,1,4,1,2011,10,2,124,1,2,3),_H3cDhcpSnoop2PktDropNum_Type())
h3cDhcpSnoop2PktDropNum.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoop2PktDropNum.setStatus(_A)
_H3cDhcpSnoop2Tables_ObjectIdentity=ObjectIdentity
h3cDhcpSnoop2Tables=_H3cDhcpSnoop2Tables_ObjectIdentity((1,3,6,1,4,1,2011,10,2,124,2))
_H3cDhcpSnoop2BindTable_Object=MibTable
h3cDhcpSnoop2BindTable=_H3cDhcpSnoop2BindTable_Object((1,3,6,1,4,1,2011,10,2,124,2,1))
if mibBuilder.loadTexts:h3cDhcpSnoop2BindTable.setStatus(_A)
_H3cDhcpSnoop2BindEntry_Object=MibTableRow
h3cDhcpSnoop2BindEntry=_H3cDhcpSnoop2BindEntry_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1))
h3cDhcpSnoop2BindEntry.setIndexNames((0,_H,_O),(0,_H,_P),(0,_H,_Q))
if mibBuilder.loadTexts:h3cDhcpSnoop2BindEntry.setStatus(_A)
_H3cDhcpSnoop2BindIpAddr_Type=InetAddressIPv4
_H3cDhcpSnoop2BindIpAddr_Object=MibTableColumn
h3cDhcpSnoop2BindIpAddr=_H3cDhcpSnoop2BindIpAddr_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1,1),_H3cDhcpSnoop2BindIpAddr_Type())
h3cDhcpSnoop2BindIpAddr.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindIpAddr.setStatus(_A)
class _H3cDhcpSnoop2BindVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cDhcpSnoop2BindVlanId_Type.__name__=_D
_H3cDhcpSnoop2BindVlanId_Object=MibTableColumn
h3cDhcpSnoop2BindVlanId=_H3cDhcpSnoop2BindVlanId_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1,2),_H3cDhcpSnoop2BindVlanId_Type())
h3cDhcpSnoop2BindVlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindVlanId.setStatus(_A)
class _H3cDhcpSnoop2BindSecVlanId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094),ValueRangeConstraint(65535,65535))
_H3cDhcpSnoop2BindSecVlanId_Type.__name__=_D
_H3cDhcpSnoop2BindSecVlanId_Object=MibTableColumn
h3cDhcpSnoop2BindSecVlanId=_H3cDhcpSnoop2BindSecVlanId_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1,3),_H3cDhcpSnoop2BindSecVlanId_Type())
h3cDhcpSnoop2BindSecVlanId.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindSecVlanId.setStatus(_A)
_H3cDhcpSnoop2BindMacAddr_Type=MacAddress
_H3cDhcpSnoop2BindMacAddr_Object=MibTableColumn
h3cDhcpSnoop2BindMacAddr=_H3cDhcpSnoop2BindMacAddr_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1,4),_H3cDhcpSnoop2BindMacAddr_Type())
h3cDhcpSnoop2BindMacAddr.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindMacAddr.setStatus(_A)
_H3cDhcpSnoop2BindLease_Type=Unsigned32
_H3cDhcpSnoop2BindLease_Object=MibTableColumn
h3cDhcpSnoop2BindLease=_H3cDhcpSnoop2BindLease_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1,5),_H3cDhcpSnoop2BindLease_Type())
h3cDhcpSnoop2BindLease.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindLease.setStatus(_A)
_H3cDhcpSnoop2BindPortIndex_Type=InterfaceIndexOrZero
_H3cDhcpSnoop2BindPortIndex_Object=MibTableColumn
h3cDhcpSnoop2BindPortIndex=_H3cDhcpSnoop2BindPortIndex_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1,6),_H3cDhcpSnoop2BindPortIndex_Type())
h3cDhcpSnoop2BindPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindPortIndex.setStatus(_A)
_H3cDhcpSnoop2BindRowStatus_Type=RowStatus
_H3cDhcpSnoop2BindRowStatus_Object=MibTableColumn
h3cDhcpSnoop2BindRowStatus=_H3cDhcpSnoop2BindRowStatus_Object((1,3,6,1,4,1,2011,10,2,124,2,1,1,7),_H3cDhcpSnoop2BindRowStatus_Type())
h3cDhcpSnoop2BindRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoop2BindRowStatus.setStatus(_A)
_H3cDhcpSnoop2IfConfigTable_Object=MibTable
h3cDhcpSnoop2IfConfigTable=_H3cDhcpSnoop2IfConfigTable_Object((1,3,6,1,4,1,2011,10,2,124,2,2))
if mibBuilder.loadTexts:h3cDhcpSnoop2IfConfigTable.setStatus(_A)
_H3cDhcpSnoop2IfConfigEntry_Object=MibTableRow
h3cDhcpSnoop2IfConfigEntry=_H3cDhcpSnoop2IfConfigEntry_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1))
h3cDhcpSnoop2IfConfigEntry.setIndexNames((0,_K,_L))
if mibBuilder.loadTexts:h3cDhcpSnoop2IfConfigEntry.setStatus(_A)
class _H3cDhcpSnoop2IfTrustStatus_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('untrusted',0),('trusted',1)))
_H3cDhcpSnoop2IfTrustStatus_Type.__name__=_C
_H3cDhcpSnoop2IfTrustStatus_Object=MibTableColumn
h3cDhcpSnoop2IfTrustStatus=_H3cDhcpSnoop2IfTrustStatus_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,1),_H3cDhcpSnoop2IfTrustStatus_Type())
h3cDhcpSnoop2IfTrustStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfTrustStatus.setStatus(_A)
class _H3cDhcpSnoop2IfCheckMac_Type(TruthValue):defaultValue=2
_H3cDhcpSnoop2IfCheckMac_Type.__name__=_F
_H3cDhcpSnoop2IfCheckMac_Object=MibTableColumn
h3cDhcpSnoop2IfCheckMac=_H3cDhcpSnoop2IfCheckMac_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,2),_H3cDhcpSnoop2IfCheckMac_Type())
h3cDhcpSnoop2IfCheckMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfCheckMac.setStatus(_A)
class _H3cDhcpSnoop2IfCheckRequest_Type(TruthValue):defaultValue=2
_H3cDhcpSnoop2IfCheckRequest_Type.__name__=_F
_H3cDhcpSnoop2IfCheckRequest_Object=MibTableColumn
h3cDhcpSnoop2IfCheckRequest=_H3cDhcpSnoop2IfCheckRequest_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,3),_H3cDhcpSnoop2IfCheckRequest_Type())
h3cDhcpSnoop2IfCheckRequest.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfCheckRequest.setStatus(_A)
class _H3cDhcpSnoop2IfRateLimit_Type(Unsigned32):defaultValue=0
_H3cDhcpSnoop2IfRateLimit_Type.__name__=_D
_H3cDhcpSnoop2IfRateLimit_Object=MibTableColumn
h3cDhcpSnoop2IfRateLimit=_H3cDhcpSnoop2IfRateLimit_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,4),_H3cDhcpSnoop2IfRateLimit_Type())
h3cDhcpSnoop2IfRateLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfRateLimit.setStatus(_A)
class _H3cDhcpSnoop2IfRecordBind_Type(TruthValue):defaultValue=2
_H3cDhcpSnoop2IfRecordBind_Type.__name__=_F
_H3cDhcpSnoop2IfRecordBind_Object=MibTableColumn
h3cDhcpSnoop2IfRecordBind=_H3cDhcpSnoop2IfRecordBind_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,5),_H3cDhcpSnoop2IfRecordBind_Type())
h3cDhcpSnoop2IfRecordBind.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfRecordBind.setStatus(_A)
class _H3cDhcpSnoop2IfMaxLearnNum_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_H3cDhcpSnoop2IfMaxLearnNum_Type.__name__=_D
_H3cDhcpSnoop2IfMaxLearnNum_Object=MibTableColumn
h3cDhcpSnoop2IfMaxLearnNum=_H3cDhcpSnoop2IfMaxLearnNum_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,6),_H3cDhcpSnoop2IfMaxLearnNum_Type())
h3cDhcpSnoop2IfMaxLearnNum.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfMaxLearnNum.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82Enable_Type(TruthValue):defaultValue=2
_H3cDhcpSnoop2IfOpt82Enable_Type.__name__=_F
_H3cDhcpSnoop2IfOpt82Enable_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82Enable=_H3cDhcpSnoop2IfOpt82Enable_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,7),_H3cDhcpSnoop2IfOpt82Enable_Type())
h3cDhcpSnoop2IfOpt82Enable.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82Enable.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82Strategy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('drop',1),('keep',2),('replace',3)))
_H3cDhcpSnoop2IfOpt82Strategy_Type.__name__=_C
_H3cDhcpSnoop2IfOpt82Strategy_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82Strategy=_H3cDhcpSnoop2IfOpt82Strategy_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,8),_H3cDhcpSnoop2IfOpt82Strategy_Type())
h3cDhcpSnoop2IfOpt82Strategy.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82Strategy.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82CIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_R,1),('verbose',2),(_M,3),('bas',4)))
_H3cDhcpSnoop2IfOpt82CIDMode_Type.__name__=_C
_H3cDhcpSnoop2IfOpt82CIDMode_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82CIDMode=_H3cDhcpSnoop2IfOpt82CIDMode_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,9),_H3cDhcpSnoop2IfOpt82CIDMode_Type())
h3cDhcpSnoop2IfOpt82CIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82CIDMode.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82CIDNodeType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('invalid',1),('mac',2),(_N,3),(_M,4)))
_H3cDhcpSnoop2IfOpt82CIDNodeType_Type.__name__=_C
_H3cDhcpSnoop2IfOpt82CIDNodeType_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82CIDNodeType=_H3cDhcpSnoop2IfOpt82CIDNodeType_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,10),_H3cDhcpSnoop2IfOpt82CIDNodeType_Type())
h3cDhcpSnoop2IfOpt82CIDNodeType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82CIDNodeType.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82CIDNodeStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,50))
_H3cDhcpSnoop2IfOpt82CIDNodeStr_Type.__name__=_E
_H3cDhcpSnoop2IfOpt82CIDNodeStr_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82CIDNodeStr=_H3cDhcpSnoop2IfOpt82CIDNodeStr_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,11),_H3cDhcpSnoop2IfOpt82CIDNodeStr_Type())
h3cDhcpSnoop2IfOpt82CIDNodeStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82CIDNodeStr.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82CIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(3,63))
_H3cDhcpSnoop2IfOpt82CIDStr_Type.__name__=_E
_H3cDhcpSnoop2IfOpt82CIDStr_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82CIDStr=_H3cDhcpSnoop2IfOpt82CIDStr_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,12),_H3cDhcpSnoop2IfOpt82CIDStr_Type())
h3cDhcpSnoop2IfOpt82CIDStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82CIDStr.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82CIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('hex',1),('ascii',2),('undefine',3)))
_H3cDhcpSnoop2IfOpt82CIDFormat_Type.__name__=_C
_H3cDhcpSnoop2IfOpt82CIDFormat_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82CIDFormat=_H3cDhcpSnoop2IfOpt82CIDFormat_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,13),_H3cDhcpSnoop2IfOpt82CIDFormat_Type())
h3cDhcpSnoop2IfOpt82CIDFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82CIDFormat.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82RIDMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_R,1),(_N,2),(_M,3)))
_H3cDhcpSnoop2IfOpt82RIDMode_Type.__name__=_C
_H3cDhcpSnoop2IfOpt82RIDMode_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82RIDMode=_H3cDhcpSnoop2IfOpt82RIDMode_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,14),_H3cDhcpSnoop2IfOpt82RIDMode_Type())
h3cDhcpSnoop2IfOpt82RIDMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82RIDMode.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82RIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDhcpSnoop2IfOpt82RIDStr_Type.__name__=_E
_H3cDhcpSnoop2IfOpt82RIDStr_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82RIDStr=_H3cDhcpSnoop2IfOpt82RIDStr_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,15),_H3cDhcpSnoop2IfOpt82RIDStr_Type())
h3cDhcpSnoop2IfOpt82RIDStr.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82RIDStr.setStatus(_A)
class _H3cDhcpSnoop2IfOpt82RIDFormat_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('hex',1),('ascii',2)))
_H3cDhcpSnoop2IfOpt82RIDFormat_Type.__name__=_C
_H3cDhcpSnoop2IfOpt82RIDFormat_Object=MibTableColumn
h3cDhcpSnoop2IfOpt82RIDFormat=_H3cDhcpSnoop2IfOpt82RIDFormat_Object((1,3,6,1,4,1,2011,10,2,124,2,2,1,16),_H3cDhcpSnoop2IfOpt82RIDFormat_Type())
h3cDhcpSnoop2IfOpt82RIDFormat.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfOpt82RIDFormat.setStatus(_A)
_H3cDhcpSnoop2IfVlanCIDTable_Object=MibTable
h3cDhcpSnoop2IfVlanCIDTable=_H3cDhcpSnoop2IfVlanCIDTable_Object((1,3,6,1,4,1,2011,10,2,124,2,3))
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanCIDTable.setStatus(_A)
_H3cDhcpSnoop2IfVlanCIDEntry_Object=MibTableRow
h3cDhcpSnoop2IfVlanCIDEntry=_H3cDhcpSnoop2IfVlanCIDEntry_Object((1,3,6,1,4,1,2011,10,2,124,2,3,1))
h3cDhcpSnoop2IfVlanCIDEntry.setIndexNames((0,_K,_L),(0,_H,_S))
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanCIDEntry.setStatus(_A)
class _H3cDhcpSnoop2IfVlanCIDVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cDhcpSnoop2IfVlanCIDVlanIndex_Type.__name__=_D
_H3cDhcpSnoop2IfVlanCIDVlanIndex_Object=MibTableColumn
h3cDhcpSnoop2IfVlanCIDVlanIndex=_H3cDhcpSnoop2IfVlanCIDVlanIndex_Object((1,3,6,1,4,1,2011,10,2,124,2,3,1,1),_H3cDhcpSnoop2IfVlanCIDVlanIndex_Type())
h3cDhcpSnoop2IfVlanCIDVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanCIDVlanIndex.setStatus(_A)
class _H3cDhcpSnoop2IfVlanCIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,63))
_H3cDhcpSnoop2IfVlanCIDStr_Type.__name__=_E
_H3cDhcpSnoop2IfVlanCIDStr_Object=MibTableColumn
h3cDhcpSnoop2IfVlanCIDStr=_H3cDhcpSnoop2IfVlanCIDStr_Object((1,3,6,1,4,1,2011,10,2,124,2,3,1,2),_H3cDhcpSnoop2IfVlanCIDStr_Type())
h3cDhcpSnoop2IfVlanCIDStr.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanCIDStr.setStatus(_A)
_H3cDhcpSnoop2IfVlanCIDRowStatus_Type=RowStatus
_H3cDhcpSnoop2IfVlanCIDRowStatus_Object=MibTableColumn
h3cDhcpSnoop2IfVlanCIDRowStatus=_H3cDhcpSnoop2IfVlanCIDRowStatus_Object((1,3,6,1,4,1,2011,10,2,124,2,3,1,3),_H3cDhcpSnoop2IfVlanCIDRowStatus_Type())
h3cDhcpSnoop2IfVlanCIDRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanCIDRowStatus.setStatus(_A)
_H3cDhcpSnoop2IfVlanRIDTable_Object=MibTable
h3cDhcpSnoop2IfVlanRIDTable=_H3cDhcpSnoop2IfVlanRIDTable_Object((1,3,6,1,4,1,2011,10,2,124,2,4))
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanRIDTable.setStatus(_A)
_H3cDhcpSnoop2IfVlanRIDEntry_Object=MibTableRow
h3cDhcpSnoop2IfVlanRIDEntry=_H3cDhcpSnoop2IfVlanRIDEntry_Object((1,3,6,1,4,1,2011,10,2,124,2,4,1))
h3cDhcpSnoop2IfVlanRIDEntry.setIndexNames((0,_K,_L),(0,_H,_T))
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanRIDEntry.setStatus(_A)
class _H3cDhcpSnoop2IfVlanRIDVlanIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_H3cDhcpSnoop2IfVlanRIDVlanIndex_Type.__name__=_D
_H3cDhcpSnoop2IfVlanRIDVlanIndex_Object=MibTableColumn
h3cDhcpSnoop2IfVlanRIDVlanIndex=_H3cDhcpSnoop2IfVlanRIDVlanIndex_Object((1,3,6,1,4,1,2011,10,2,124,2,4,1,1),_H3cDhcpSnoop2IfVlanRIDVlanIndex_Type())
h3cDhcpSnoop2IfVlanRIDVlanIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanRIDVlanIndex.setStatus(_A)
class _H3cDhcpSnoop2IfVlanRIDMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_N,1),(_M,2)))
_H3cDhcpSnoop2IfVlanRIDMode_Type.__name__=_C
_H3cDhcpSnoop2IfVlanRIDMode_Object=MibTableColumn
h3cDhcpSnoop2IfVlanRIDMode=_H3cDhcpSnoop2IfVlanRIDMode_Object((1,3,6,1,4,1,2011,10,2,124,2,4,1,2),_H3cDhcpSnoop2IfVlanRIDMode_Type())
h3cDhcpSnoop2IfVlanRIDMode.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanRIDMode.setStatus(_A)
class _H3cDhcpSnoop2IfVlanRIDStr_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H3cDhcpSnoop2IfVlanRIDStr_Type.__name__=_E
_H3cDhcpSnoop2IfVlanRIDStr_Object=MibTableColumn
h3cDhcpSnoop2IfVlanRIDStr=_H3cDhcpSnoop2IfVlanRIDStr_Object((1,3,6,1,4,1,2011,10,2,124,2,4,1,3),_H3cDhcpSnoop2IfVlanRIDStr_Type())
h3cDhcpSnoop2IfVlanRIDStr.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanRIDStr.setStatus(_A)
_H3cDhcpSnoop2IfVlanRIDRowStatus_Type=RowStatus
_H3cDhcpSnoop2IfVlanRIDRowStatus_Object=MibTableColumn
h3cDhcpSnoop2IfVlanRIDRowStatus=_H3cDhcpSnoop2IfVlanRIDRowStatus_Object((1,3,6,1,4,1,2011,10,2,124,2,4,1,4),_H3cDhcpSnoop2IfVlanRIDRowStatus_Type())
h3cDhcpSnoop2IfVlanRIDRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:h3cDhcpSnoop2IfVlanRIDRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_H,**{'h3cDhcpSnoop2':h3cDhcpSnoop2,'h3cDhcpSnoop2ScalarObjects':h3cDhcpSnoop2ScalarObjects,'h3cDhcpSnoop2ConfigGroup':h3cDhcpSnoop2ConfigGroup,'h3cDhcpSnoop2Enabled':h3cDhcpSnoop2Enabled,'h3cDhcpSnoop2BindDbName':h3cDhcpSnoop2BindDbName,'h3cDhcpSnoop2BindRefreshIntvl':h3cDhcpSnoop2BindRefreshIntvl,'h3cDhcpSnoop2BindRefresh':h3cDhcpSnoop2BindRefresh,'h3cDhcpSnoop2StatisticsGroup':h3cDhcpSnoop2StatisticsGroup,'h3cDhcpSnoop2PktSentNum':h3cDhcpSnoop2PktSentNum,'h3cDhcpSnoop2PktRcvNum':h3cDhcpSnoop2PktRcvNum,'h3cDhcpSnoop2PktDropNum':h3cDhcpSnoop2PktDropNum,'h3cDhcpSnoop2Tables':h3cDhcpSnoop2Tables,'h3cDhcpSnoop2BindTable':h3cDhcpSnoop2BindTable,'h3cDhcpSnoop2BindEntry':h3cDhcpSnoop2BindEntry,_O:h3cDhcpSnoop2BindIpAddr,_P:h3cDhcpSnoop2BindVlanId,_Q:h3cDhcpSnoop2BindSecVlanId,'h3cDhcpSnoop2BindMacAddr':h3cDhcpSnoop2BindMacAddr,'h3cDhcpSnoop2BindLease':h3cDhcpSnoop2BindLease,'h3cDhcpSnoop2BindPortIndex':h3cDhcpSnoop2BindPortIndex,'h3cDhcpSnoop2BindRowStatus':h3cDhcpSnoop2BindRowStatus,'h3cDhcpSnoop2IfConfigTable':h3cDhcpSnoop2IfConfigTable,'h3cDhcpSnoop2IfConfigEntry':h3cDhcpSnoop2IfConfigEntry,'h3cDhcpSnoop2IfTrustStatus':h3cDhcpSnoop2IfTrustStatus,'h3cDhcpSnoop2IfCheckMac':h3cDhcpSnoop2IfCheckMac,'h3cDhcpSnoop2IfCheckRequest':h3cDhcpSnoop2IfCheckRequest,'h3cDhcpSnoop2IfRateLimit':h3cDhcpSnoop2IfRateLimit,'h3cDhcpSnoop2IfRecordBind':h3cDhcpSnoop2IfRecordBind,'h3cDhcpSnoop2IfMaxLearnNum':h3cDhcpSnoop2IfMaxLearnNum,'h3cDhcpSnoop2IfOpt82Enable':h3cDhcpSnoop2IfOpt82Enable,'h3cDhcpSnoop2IfOpt82Strategy':h3cDhcpSnoop2IfOpt82Strategy,'h3cDhcpSnoop2IfOpt82CIDMode':h3cDhcpSnoop2IfOpt82CIDMode,'h3cDhcpSnoop2IfOpt82CIDNodeType':h3cDhcpSnoop2IfOpt82CIDNodeType,'h3cDhcpSnoop2IfOpt82CIDNodeStr':h3cDhcpSnoop2IfOpt82CIDNodeStr,'h3cDhcpSnoop2IfOpt82CIDStr':h3cDhcpSnoop2IfOpt82CIDStr,'h3cDhcpSnoop2IfOpt82CIDFormat':h3cDhcpSnoop2IfOpt82CIDFormat,'h3cDhcpSnoop2IfOpt82RIDMode':h3cDhcpSnoop2IfOpt82RIDMode,'h3cDhcpSnoop2IfOpt82RIDStr':h3cDhcpSnoop2IfOpt82RIDStr,'h3cDhcpSnoop2IfOpt82RIDFormat':h3cDhcpSnoop2IfOpt82RIDFormat,'h3cDhcpSnoop2IfVlanCIDTable':h3cDhcpSnoop2IfVlanCIDTable,'h3cDhcpSnoop2IfVlanCIDEntry':h3cDhcpSnoop2IfVlanCIDEntry,_S:h3cDhcpSnoop2IfVlanCIDVlanIndex,'h3cDhcpSnoop2IfVlanCIDStr':h3cDhcpSnoop2IfVlanCIDStr,'h3cDhcpSnoop2IfVlanCIDRowStatus':h3cDhcpSnoop2IfVlanCIDRowStatus,'h3cDhcpSnoop2IfVlanRIDTable':h3cDhcpSnoop2IfVlanRIDTable,'h3cDhcpSnoop2IfVlanRIDEntry':h3cDhcpSnoop2IfVlanRIDEntry,_T:h3cDhcpSnoop2IfVlanRIDVlanIndex,'h3cDhcpSnoop2IfVlanRIDMode':h3cDhcpSnoop2IfVlanRIDMode,'h3cDhcpSnoop2IfVlanRIDStr':h3cDhcpSnoop2IfVlanRIDStr,'h3cDhcpSnoop2IfVlanRIDRowStatus':h3cDhcpSnoop2IfVlanRIDRowStatus})