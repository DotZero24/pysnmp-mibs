_AO='ciscoIpSlaTcpConnTmplGroup'
_AN='ciscoIpSlaUdpEchoTmplGroup'
_AM='ciscoIpSlaIcmpEchoTmplGroup'
_AL='cipslaTcpConnTmplRowStatus'
_AK='cipslaTcpConnTmplStorageType'
_AJ='cipslaTcpConnTmplDistInterval'
_AI='cipslaTcpConnTmplDistBuckets'
_AH='cipslaTcpConnTmplStatsHours'
_AG='cipslaTcpConnTmplHistFilter'
_AF='cipslaTcpConnTmplHistBuckets'
_AE='cipslaTcpConnTmplHistLives'
_AD='cipslaTcpConnTmplThreshold'
_AC='cipslaTcpConnTmplTOS'
_AB='cipslaTcpConnTmplVerifyData'
_AA='cipslaTcpConnTmplTimeOut'
_A9='cipslaTcpConnTmplSrcPort'
_A8='cipslaTcpConnTmplSrcAddr'
_A7='cipslaTcpConnTmplSrcAddrType'
_A6='cipslaTcpConnTmplControlEnable'
_A5='cipslaTcpConnTmplDescription'
_A4='cipslaUdpEchoTmplRowStatus'
_A3='cipslaUdpEchoTmplStorageType'
_A2='cipslaUdpEchoTmplDistInterval'
_A1='cipslaUdpEchoTmplDistBuckets'
_A0='cipslaUdpEchoTmplStatsHours'
_z='cipslaUdpEchoTmplHistFilter'
_y='cipslaUdpEchoTmplHistBuckets'
_x='cipslaUdpEchoTmplHistLives'
_w='cipslaUdpEchoTmplThreshold'
_v='cipslaUdpEchoTmplVrfName'
_u='cipslaUdpEchoTmplTOS'
_t='cipslaUdpEchoTmplReqDataSize'
_s='cipslaUdpEchoTmplVerifyData'
_r='cipslaUdpEchoTmplTimeOut'
_q='cipslaUdpEchoTmplSrcPort'
_p='cipslaUdpEchoTmplSrcAddr'
_o='cipslaUdpEchoTmplSrcAddrType'
_n='cipslaUdpEchoTmplControlEnable'
_m='cipslaUdpEchoTmplDescription'
_l='cipslaIcmpEchoTmplRowStatus'
_k='cipslaIcmpEchoTmplStorageType'
_j='cipslaIcmpEchoTmplDistInterval'
_i='cipslaIcmpEchoTmplDistBuckets'
_h='cipslaIcmpEchoTmplStatsHours'
_g='cipslaIcmpEchoTmplHistFilter'
_f='cipslaIcmpEchoTmplHistBuckets'
_e='cipslaIcmpEchoTmplHistLives'
_d='cipslaIcmpEchoTmplThreshold'
_c='cipslaIcmpEchoTmplVrfName'
_b='cipslaIcmpEchoTmplTOS'
_a='cipslaIcmpEchoTmplReqDataSize'
_Z='cipslaIcmpEchoTmplVerifyData'
_Y='cipslaIcmpEchoTmplTimeOut'
_X='cipslaIcmpEchoTmplSrcAddr'
_W='cipslaIcmpEchoTmplSrcAddrType'
_V='cipslaIcmpEchoTmplDescription'
_U='cipslaTcpConnTmplName'
_T='cipslaUdpEchoTmplName'
_S='octets'
_R='cipslaIcmpEchoTmplName'
_Q='hours'
_P='failures'
_O='overThreshold'
_N='all'
_M='none'
_L='not-accessible'
_K='InetPortNumber'
_J='StorageType'
_I='Integer32'
_H='InetAddressType'
_G='TruthValue'
_F='milliseconds'
_E='SnmpAdminString'
_D='Unsigned32'
_C='read-create'
_B='CISCO-IPSLA-ECHO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_H,_K)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_J,'TextualConvention',_G)
ciscoIpSlaEchoMIB=ModuleIdentity((1,3,6,1,4,1,9,9,636))
if mibBuilder.loadTexts:ciscoIpSlaEchoMIB.setRevisions(('2007-08-16 00:00',))
_CiscoIpSlaEchoMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpSlaEchoMIBNotifs=_CiscoIpSlaEchoMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,636,0))
_CiscoIpSlaEchoMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpSlaEchoMIBObjects=_CiscoIpSlaEchoMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,636,1))
_CipslaIcmpEchoTmplTable_Object=MibTable
cipslaIcmpEchoTmplTable=_CipslaIcmpEchoTmplTable_Object((1,3,6,1,4,1,9,9,636,1,1))
if mibBuilder.loadTexts:cipslaIcmpEchoTmplTable.setStatus(_A)
_CipslaIcmpEchoTmplEntry_Object=MibTableRow
cipslaIcmpEchoTmplEntry=_CipslaIcmpEchoTmplEntry_Object((1,3,6,1,4,1,9,9,636,1,1,1))
cipslaIcmpEchoTmplEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:cipslaIcmpEchoTmplEntry.setStatus(_A)
class _CipslaIcmpEchoTmplName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaIcmpEchoTmplName_Type.__name__=_E
_CipslaIcmpEchoTmplName_Object=MibTableColumn
cipslaIcmpEchoTmplName=_CipslaIcmpEchoTmplName_Object((1,3,6,1,4,1,9,9,636,1,1,1,1),_CipslaIcmpEchoTmplName_Type())
cipslaIcmpEchoTmplName.setMaxAccess(_L)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplName.setStatus(_A)
class _CipslaIcmpEchoTmplDescription_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CipslaIcmpEchoTmplDescription_Type.__name__=_E
_CipslaIcmpEchoTmplDescription_Object=MibTableColumn
cipslaIcmpEchoTmplDescription=_CipslaIcmpEchoTmplDescription_Object((1,3,6,1,4,1,9,9,636,1,1,1,2),_CipslaIcmpEchoTmplDescription_Type())
cipslaIcmpEchoTmplDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplDescription.setStatus(_A)
class _CipslaIcmpEchoTmplSrcAddrType_Type(InetAddressType):defaultValue=1
_CipslaIcmpEchoTmplSrcAddrType_Type.__name__=_H
_CipslaIcmpEchoTmplSrcAddrType_Object=MibTableColumn
cipslaIcmpEchoTmplSrcAddrType=_CipslaIcmpEchoTmplSrcAddrType_Object((1,3,6,1,4,1,9,9,636,1,1,1,3),_CipslaIcmpEchoTmplSrcAddrType_Type())
cipslaIcmpEchoTmplSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplSrcAddrType.setStatus(_A)
_CipslaIcmpEchoTmplSrcAddr_Type=InetAddress
_CipslaIcmpEchoTmplSrcAddr_Object=MibTableColumn
cipslaIcmpEchoTmplSrcAddr=_CipslaIcmpEchoTmplSrcAddr_Object((1,3,6,1,4,1,9,9,636,1,1,1,4),_CipslaIcmpEchoTmplSrcAddr_Type())
cipslaIcmpEchoTmplSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplSrcAddr.setStatus(_A)
class _CipslaIcmpEchoTmplTimeOut_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800000))
_CipslaIcmpEchoTmplTimeOut_Type.__name__=_D
_CipslaIcmpEchoTmplTimeOut_Object=MibTableColumn
cipslaIcmpEchoTmplTimeOut=_CipslaIcmpEchoTmplTimeOut_Object((1,3,6,1,4,1,9,9,636,1,1,1,5),_CipslaIcmpEchoTmplTimeOut_Type())
cipslaIcmpEchoTmplTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplTimeOut.setUnits(_F)
class _CipslaIcmpEchoTmplVerifyData_Type(TruthValue):defaultValue=2
_CipslaIcmpEchoTmplVerifyData_Type.__name__=_G
_CipslaIcmpEchoTmplVerifyData_Object=MibTableColumn
cipslaIcmpEchoTmplVerifyData=_CipslaIcmpEchoTmplVerifyData_Object((1,3,6,1,4,1,9,9,636,1,1,1,6),_CipslaIcmpEchoTmplVerifyData_Type())
cipslaIcmpEchoTmplVerifyData.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplVerifyData.setStatus(_A)
class _CipslaIcmpEchoTmplReqDataSize_Type(Unsigned32):defaultValue=28;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_CipslaIcmpEchoTmplReqDataSize_Type.__name__=_D
_CipslaIcmpEchoTmplReqDataSize_Object=MibTableColumn
cipslaIcmpEchoTmplReqDataSize=_CipslaIcmpEchoTmplReqDataSize_Object((1,3,6,1,4,1,9,9,636,1,1,1,7),_CipslaIcmpEchoTmplReqDataSize_Type())
cipslaIcmpEchoTmplReqDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplReqDataSize.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplReqDataSize.setUnits(_S)
class _CipslaIcmpEchoTmplTOS_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CipslaIcmpEchoTmplTOS_Type.__name__=_D
_CipslaIcmpEchoTmplTOS_Object=MibTableColumn
cipslaIcmpEchoTmplTOS=_CipslaIcmpEchoTmplTOS_Object((1,3,6,1,4,1,9,9,636,1,1,1,8),_CipslaIcmpEchoTmplTOS_Type())
cipslaIcmpEchoTmplTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplTOS.setStatus(_A)
class _CipslaIcmpEchoTmplVrfName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CipslaIcmpEchoTmplVrfName_Type.__name__=_E
_CipslaIcmpEchoTmplVrfName_Object=MibTableColumn
cipslaIcmpEchoTmplVrfName=_CipslaIcmpEchoTmplVrfName_Object((1,3,6,1,4,1,9,9,636,1,1,1,9),_CipslaIcmpEchoTmplVrfName_Type())
cipslaIcmpEchoTmplVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplVrfName.setStatus(_A)
class _CipslaIcmpEchoTmplThreshold_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CipslaIcmpEchoTmplThreshold_Type.__name__=_D
_CipslaIcmpEchoTmplThreshold_Object=MibTableColumn
cipslaIcmpEchoTmplThreshold=_CipslaIcmpEchoTmplThreshold_Object((1,3,6,1,4,1,9,9,636,1,1,1,10),_CipslaIcmpEchoTmplThreshold_Type())
cipslaIcmpEchoTmplThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplThreshold.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplThreshold.setUnits(_F)
class _CipslaIcmpEchoTmplHistLives_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CipslaIcmpEchoTmplHistLives_Type.__name__=_D
_CipslaIcmpEchoTmplHistLives_Object=MibTableColumn
cipslaIcmpEchoTmplHistLives=_CipslaIcmpEchoTmplHistLives_Object((1,3,6,1,4,1,9,9,636,1,1,1,11),_CipslaIcmpEchoTmplHistLives_Type())
cipslaIcmpEchoTmplHistLives.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplHistLives.setStatus(_A)
class _CipslaIcmpEchoTmplHistBuckets_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CipslaIcmpEchoTmplHistBuckets_Type.__name__=_D
_CipslaIcmpEchoTmplHistBuckets_Object=MibTableColumn
cipslaIcmpEchoTmplHistBuckets=_CipslaIcmpEchoTmplHistBuckets_Object((1,3,6,1,4,1,9,9,636,1,1,1,12),_CipslaIcmpEchoTmplHistBuckets_Type())
cipslaIcmpEchoTmplHistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplHistBuckets.setStatus(_A)
class _CipslaIcmpEchoTmplHistFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_CipslaIcmpEchoTmplHistFilter_Type.__name__=_I
_CipslaIcmpEchoTmplHistFilter_Object=MibTableColumn
cipslaIcmpEchoTmplHistFilter=_CipslaIcmpEchoTmplHistFilter_Object((1,3,6,1,4,1,9,9,636,1,1,1,13),_CipslaIcmpEchoTmplHistFilter_Type())
cipslaIcmpEchoTmplHistFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplHistFilter.setStatus(_A)
class _CipslaIcmpEchoTmplStatsHours_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_CipslaIcmpEchoTmplStatsHours_Type.__name__=_D
_CipslaIcmpEchoTmplStatsHours_Object=MibTableColumn
cipslaIcmpEchoTmplStatsHours=_CipslaIcmpEchoTmplStatsHours_Object((1,3,6,1,4,1,9,9,636,1,1,1,14),_CipslaIcmpEchoTmplStatsHours_Type())
cipslaIcmpEchoTmplStatsHours.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplStatsHours.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplStatsHours.setUnits(_Q)
class _CipslaIcmpEchoTmplDistBuckets_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CipslaIcmpEchoTmplDistBuckets_Type.__name__=_D
_CipslaIcmpEchoTmplDistBuckets_Object=MibTableColumn
cipslaIcmpEchoTmplDistBuckets=_CipslaIcmpEchoTmplDistBuckets_Object((1,3,6,1,4,1,9,9,636,1,1,1,15),_CipslaIcmpEchoTmplDistBuckets_Type())
cipslaIcmpEchoTmplDistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplDistBuckets.setStatus(_A)
class _CipslaIcmpEchoTmplDistInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CipslaIcmpEchoTmplDistInterval_Type.__name__=_D
_CipslaIcmpEchoTmplDistInterval_Object=MibTableColumn
cipslaIcmpEchoTmplDistInterval=_CipslaIcmpEchoTmplDistInterval_Object((1,3,6,1,4,1,9,9,636,1,1,1,16),_CipslaIcmpEchoTmplDistInterval_Type())
cipslaIcmpEchoTmplDistInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplDistInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplDistInterval.setUnits(_F)
class _CipslaIcmpEchoTmplStorageType_Type(StorageType):defaultValue=3
_CipslaIcmpEchoTmplStorageType_Type.__name__=_J
_CipslaIcmpEchoTmplStorageType_Object=MibTableColumn
cipslaIcmpEchoTmplStorageType=_CipslaIcmpEchoTmplStorageType_Object((1,3,6,1,4,1,9,9,636,1,1,1,17),_CipslaIcmpEchoTmplStorageType_Type())
cipslaIcmpEchoTmplStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplStorageType.setStatus(_A)
_CipslaIcmpEchoTmplRowStatus_Type=RowStatus
_CipslaIcmpEchoTmplRowStatus_Object=MibTableColumn
cipslaIcmpEchoTmplRowStatus=_CipslaIcmpEchoTmplRowStatus_Object((1,3,6,1,4,1,9,9,636,1,1,1,18),_CipslaIcmpEchoTmplRowStatus_Type())
cipslaIcmpEchoTmplRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpEchoTmplRowStatus.setStatus(_A)
_CipslaUdpEchoTmplTable_Object=MibTable
cipslaUdpEchoTmplTable=_CipslaUdpEchoTmplTable_Object((1,3,6,1,4,1,9,9,636,1,2))
if mibBuilder.loadTexts:cipslaUdpEchoTmplTable.setStatus(_A)
_CipslaUdpEchoTmplEntry_Object=MibTableRow
cipslaUdpEchoTmplEntry=_CipslaUdpEchoTmplEntry_Object((1,3,6,1,4,1,9,9,636,1,2,1))
cipslaUdpEchoTmplEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:cipslaUdpEchoTmplEntry.setStatus(_A)
class _CipslaUdpEchoTmplName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaUdpEchoTmplName_Type.__name__=_E
_CipslaUdpEchoTmplName_Object=MibTableColumn
cipslaUdpEchoTmplName=_CipslaUdpEchoTmplName_Object((1,3,6,1,4,1,9,9,636,1,2,1,1),_CipslaUdpEchoTmplName_Type())
cipslaUdpEchoTmplName.setMaxAccess(_L)
if mibBuilder.loadTexts:cipslaUdpEchoTmplName.setStatus(_A)
class _CipslaUdpEchoTmplDescription_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CipslaUdpEchoTmplDescription_Type.__name__=_E
_CipslaUdpEchoTmplDescription_Object=MibTableColumn
cipslaUdpEchoTmplDescription=_CipslaUdpEchoTmplDescription_Object((1,3,6,1,4,1,9,9,636,1,2,1,2),_CipslaUdpEchoTmplDescription_Type())
cipslaUdpEchoTmplDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplDescription.setStatus(_A)
class _CipslaUdpEchoTmplControlEnable_Type(TruthValue):defaultValue=1
_CipslaUdpEchoTmplControlEnable_Type.__name__=_G
_CipslaUdpEchoTmplControlEnable_Object=MibTableColumn
cipslaUdpEchoTmplControlEnable=_CipslaUdpEchoTmplControlEnable_Object((1,3,6,1,4,1,9,9,636,1,2,1,3),_CipslaUdpEchoTmplControlEnable_Type())
cipslaUdpEchoTmplControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplControlEnable.setStatus(_A)
class _CipslaUdpEchoTmplSrcAddrType_Type(InetAddressType):defaultValue=1
_CipslaUdpEchoTmplSrcAddrType_Type.__name__=_H
_CipslaUdpEchoTmplSrcAddrType_Object=MibTableColumn
cipslaUdpEchoTmplSrcAddrType=_CipslaUdpEchoTmplSrcAddrType_Object((1,3,6,1,4,1,9,9,636,1,2,1,4),_CipslaUdpEchoTmplSrcAddrType_Type())
cipslaUdpEchoTmplSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplSrcAddrType.setStatus(_A)
_CipslaUdpEchoTmplSrcAddr_Type=InetAddress
_CipslaUdpEchoTmplSrcAddr_Object=MibTableColumn
cipslaUdpEchoTmplSrcAddr=_CipslaUdpEchoTmplSrcAddr_Object((1,3,6,1,4,1,9,9,636,1,2,1,5),_CipslaUdpEchoTmplSrcAddr_Type())
cipslaUdpEchoTmplSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplSrcAddr.setStatus(_A)
class _CipslaUdpEchoTmplSrcPort_Type(InetPortNumber):defaultValue=0
_CipslaUdpEchoTmplSrcPort_Type.__name__=_K
_CipslaUdpEchoTmplSrcPort_Object=MibTableColumn
cipslaUdpEchoTmplSrcPort=_CipslaUdpEchoTmplSrcPort_Object((1,3,6,1,4,1,9,9,636,1,2,1,6),_CipslaUdpEchoTmplSrcPort_Type())
cipslaUdpEchoTmplSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplSrcPort.setStatus(_A)
class _CipslaUdpEchoTmplTimeOut_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800000))
_CipslaUdpEchoTmplTimeOut_Type.__name__=_D
_CipslaUdpEchoTmplTimeOut_Object=MibTableColumn
cipslaUdpEchoTmplTimeOut=_CipslaUdpEchoTmplTimeOut_Object((1,3,6,1,4,1,9,9,636,1,2,1,7),_CipslaUdpEchoTmplTimeOut_Type())
cipslaUdpEchoTmplTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpEchoTmplTimeOut.setUnits(_F)
class _CipslaUdpEchoTmplVerifyData_Type(TruthValue):defaultValue=2
_CipslaUdpEchoTmplVerifyData_Type.__name__=_G
_CipslaUdpEchoTmplVerifyData_Object=MibTableColumn
cipslaUdpEchoTmplVerifyData=_CipslaUdpEchoTmplVerifyData_Object((1,3,6,1,4,1,9,9,636,1,2,1,8),_CipslaUdpEchoTmplVerifyData_Type())
cipslaUdpEchoTmplVerifyData.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplVerifyData.setStatus(_A)
class _CipslaUdpEchoTmplReqDataSize_Type(Unsigned32):defaultValue=16;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,1500))
_CipslaUdpEchoTmplReqDataSize_Type.__name__=_D
_CipslaUdpEchoTmplReqDataSize_Object=MibTableColumn
cipslaUdpEchoTmplReqDataSize=_CipslaUdpEchoTmplReqDataSize_Object((1,3,6,1,4,1,9,9,636,1,2,1,9),_CipslaUdpEchoTmplReqDataSize_Type())
cipslaUdpEchoTmplReqDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplReqDataSize.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpEchoTmplReqDataSize.setUnits(_S)
class _CipslaUdpEchoTmplTOS_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CipslaUdpEchoTmplTOS_Type.__name__=_D
_CipslaUdpEchoTmplTOS_Object=MibTableColumn
cipslaUdpEchoTmplTOS=_CipslaUdpEchoTmplTOS_Object((1,3,6,1,4,1,9,9,636,1,2,1,10),_CipslaUdpEchoTmplTOS_Type())
cipslaUdpEchoTmplTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplTOS.setStatus(_A)
class _CipslaUdpEchoTmplVrfName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CipslaUdpEchoTmplVrfName_Type.__name__=_E
_CipslaUdpEchoTmplVrfName_Object=MibTableColumn
cipslaUdpEchoTmplVrfName=_CipslaUdpEchoTmplVrfName_Object((1,3,6,1,4,1,9,9,636,1,2,1,11),_CipslaUdpEchoTmplVrfName_Type())
cipslaUdpEchoTmplVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplVrfName.setStatus(_A)
class _CipslaUdpEchoTmplThreshold_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CipslaUdpEchoTmplThreshold_Type.__name__=_D
_CipslaUdpEchoTmplThreshold_Object=MibTableColumn
cipslaUdpEchoTmplThreshold=_CipslaUdpEchoTmplThreshold_Object((1,3,6,1,4,1,9,9,636,1,2,1,12),_CipslaUdpEchoTmplThreshold_Type())
cipslaUdpEchoTmplThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplThreshold.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpEchoTmplThreshold.setUnits(_F)
class _CipslaUdpEchoTmplHistLives_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CipslaUdpEchoTmplHistLives_Type.__name__=_D
_CipslaUdpEchoTmplHistLives_Object=MibTableColumn
cipslaUdpEchoTmplHistLives=_CipslaUdpEchoTmplHistLives_Object((1,3,6,1,4,1,9,9,636,1,2,1,13),_CipslaUdpEchoTmplHistLives_Type())
cipslaUdpEchoTmplHistLives.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplHistLives.setStatus(_A)
class _CipslaUdpEchoTmplHistBuckets_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CipslaUdpEchoTmplHistBuckets_Type.__name__=_D
_CipslaUdpEchoTmplHistBuckets_Object=MibTableColumn
cipslaUdpEchoTmplHistBuckets=_CipslaUdpEchoTmplHistBuckets_Object((1,3,6,1,4,1,9,9,636,1,2,1,14),_CipslaUdpEchoTmplHistBuckets_Type())
cipslaUdpEchoTmplHistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplHistBuckets.setStatus(_A)
class _CipslaUdpEchoTmplHistFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_CipslaUdpEchoTmplHistFilter_Type.__name__=_I
_CipslaUdpEchoTmplHistFilter_Object=MibTableColumn
cipslaUdpEchoTmplHistFilter=_CipslaUdpEchoTmplHistFilter_Object((1,3,6,1,4,1,9,9,636,1,2,1,15),_CipslaUdpEchoTmplHistFilter_Type())
cipslaUdpEchoTmplHistFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplHistFilter.setStatus(_A)
class _CipslaUdpEchoTmplStatsHours_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_CipslaUdpEchoTmplStatsHours_Type.__name__=_D
_CipslaUdpEchoTmplStatsHours_Object=MibTableColumn
cipslaUdpEchoTmplStatsHours=_CipslaUdpEchoTmplStatsHours_Object((1,3,6,1,4,1,9,9,636,1,2,1,16),_CipslaUdpEchoTmplStatsHours_Type())
cipslaUdpEchoTmplStatsHours.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplStatsHours.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpEchoTmplStatsHours.setUnits(_Q)
class _CipslaUdpEchoTmplDistBuckets_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CipslaUdpEchoTmplDistBuckets_Type.__name__=_D
_CipslaUdpEchoTmplDistBuckets_Object=MibTableColumn
cipslaUdpEchoTmplDistBuckets=_CipslaUdpEchoTmplDistBuckets_Object((1,3,6,1,4,1,9,9,636,1,2,1,17),_CipslaUdpEchoTmplDistBuckets_Type())
cipslaUdpEchoTmplDistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplDistBuckets.setStatus(_A)
class _CipslaUdpEchoTmplDistInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CipslaUdpEchoTmplDistInterval_Type.__name__=_D
_CipslaUdpEchoTmplDistInterval_Object=MibTableColumn
cipslaUdpEchoTmplDistInterval=_CipslaUdpEchoTmplDistInterval_Object((1,3,6,1,4,1,9,9,636,1,2,1,18),_CipslaUdpEchoTmplDistInterval_Type())
cipslaUdpEchoTmplDistInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplDistInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpEchoTmplDistInterval.setUnits(_F)
class _CipslaUdpEchoTmplStorageType_Type(StorageType):defaultValue=3
_CipslaUdpEchoTmplStorageType_Type.__name__=_J
_CipslaUdpEchoTmplStorageType_Object=MibTableColumn
cipslaUdpEchoTmplStorageType=_CipslaUdpEchoTmplStorageType_Object((1,3,6,1,4,1,9,9,636,1,2,1,19),_CipslaUdpEchoTmplStorageType_Type())
cipslaUdpEchoTmplStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplStorageType.setStatus(_A)
_CipslaUdpEchoTmplRowStatus_Type=RowStatus
_CipslaUdpEchoTmplRowStatus_Object=MibTableColumn
cipslaUdpEchoTmplRowStatus=_CipslaUdpEchoTmplRowStatus_Object((1,3,6,1,4,1,9,9,636,1,2,1,20),_CipslaUdpEchoTmplRowStatus_Type())
cipslaUdpEchoTmplRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpEchoTmplRowStatus.setStatus(_A)
_CipslaTcpConnTmplTable_Object=MibTable
cipslaTcpConnTmplTable=_CipslaTcpConnTmplTable_Object((1,3,6,1,4,1,9,9,636,1,3))
if mibBuilder.loadTexts:cipslaTcpConnTmplTable.setStatus(_A)
_CipslaTcpConnTmplEntry_Object=MibTableRow
cipslaTcpConnTmplEntry=_CipslaTcpConnTmplEntry_Object((1,3,6,1,4,1,9,9,636,1,3,1))
cipslaTcpConnTmplEntry.setIndexNames((0,_B,_U))
if mibBuilder.loadTexts:cipslaTcpConnTmplEntry.setStatus(_A)
class _CipslaTcpConnTmplName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaTcpConnTmplName_Type.__name__=_E
_CipslaTcpConnTmplName_Object=MibTableColumn
cipslaTcpConnTmplName=_CipslaTcpConnTmplName_Object((1,3,6,1,4,1,9,9,636,1,3,1,1),_CipslaTcpConnTmplName_Type())
cipslaTcpConnTmplName.setMaxAccess(_L)
if mibBuilder.loadTexts:cipslaTcpConnTmplName.setStatus(_A)
class _CipslaTcpConnTmplDescription_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CipslaTcpConnTmplDescription_Type.__name__=_E
_CipslaTcpConnTmplDescription_Object=MibTableColumn
cipslaTcpConnTmplDescription=_CipslaTcpConnTmplDescription_Object((1,3,6,1,4,1,9,9,636,1,3,1,2),_CipslaTcpConnTmplDescription_Type())
cipslaTcpConnTmplDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplDescription.setStatus(_A)
class _CipslaTcpConnTmplControlEnable_Type(TruthValue):defaultValue=1
_CipslaTcpConnTmplControlEnable_Type.__name__=_G
_CipslaTcpConnTmplControlEnable_Object=MibTableColumn
cipslaTcpConnTmplControlEnable=_CipslaTcpConnTmplControlEnable_Object((1,3,6,1,4,1,9,9,636,1,3,1,3),_CipslaTcpConnTmplControlEnable_Type())
cipslaTcpConnTmplControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplControlEnable.setStatus(_A)
class _CipslaTcpConnTmplSrcAddrType_Type(InetAddressType):defaultValue=1
_CipslaTcpConnTmplSrcAddrType_Type.__name__=_H
_CipslaTcpConnTmplSrcAddrType_Object=MibTableColumn
cipslaTcpConnTmplSrcAddrType=_CipslaTcpConnTmplSrcAddrType_Object((1,3,6,1,4,1,9,9,636,1,3,1,4),_CipslaTcpConnTmplSrcAddrType_Type())
cipslaTcpConnTmplSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplSrcAddrType.setStatus(_A)
_CipslaTcpConnTmplSrcAddr_Type=InetAddress
_CipslaTcpConnTmplSrcAddr_Object=MibTableColumn
cipslaTcpConnTmplSrcAddr=_CipslaTcpConnTmplSrcAddr_Object((1,3,6,1,4,1,9,9,636,1,3,1,5),_CipslaTcpConnTmplSrcAddr_Type())
cipslaTcpConnTmplSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplSrcAddr.setStatus(_A)
class _CipslaTcpConnTmplSrcPort_Type(InetPortNumber):defaultValue=0
_CipslaTcpConnTmplSrcPort_Type.__name__=_K
_CipslaTcpConnTmplSrcPort_Object=MibTableColumn
cipslaTcpConnTmplSrcPort=_CipslaTcpConnTmplSrcPort_Object((1,3,6,1,4,1,9,9,636,1,3,1,6),_CipslaTcpConnTmplSrcPort_Type())
cipslaTcpConnTmplSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplSrcPort.setStatus(_A)
class _CipslaTcpConnTmplTimeOut_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800000))
_CipslaTcpConnTmplTimeOut_Type.__name__=_D
_CipslaTcpConnTmplTimeOut_Object=MibTableColumn
cipslaTcpConnTmplTimeOut=_CipslaTcpConnTmplTimeOut_Object((1,3,6,1,4,1,9,9,636,1,3,1,7),_CipslaTcpConnTmplTimeOut_Type())
cipslaTcpConnTmplTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cipslaTcpConnTmplTimeOut.setUnits(_F)
class _CipslaTcpConnTmplVerifyData_Type(TruthValue):defaultValue=2
_CipslaTcpConnTmplVerifyData_Type.__name__=_G
_CipslaTcpConnTmplVerifyData_Object=MibTableColumn
cipslaTcpConnTmplVerifyData=_CipslaTcpConnTmplVerifyData_Object((1,3,6,1,4,1,9,9,636,1,3,1,8),_CipslaTcpConnTmplVerifyData_Type())
cipslaTcpConnTmplVerifyData.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplVerifyData.setStatus(_A)
class _CipslaTcpConnTmplTOS_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CipslaTcpConnTmplTOS_Type.__name__=_D
_CipslaTcpConnTmplTOS_Object=MibTableColumn
cipslaTcpConnTmplTOS=_CipslaTcpConnTmplTOS_Object((1,3,6,1,4,1,9,9,636,1,3,1,9),_CipslaTcpConnTmplTOS_Type())
cipslaTcpConnTmplTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplTOS.setStatus(_A)
class _CipslaTcpConnTmplThreshold_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CipslaTcpConnTmplThreshold_Type.__name__=_D
_CipslaTcpConnTmplThreshold_Object=MibTableColumn
cipslaTcpConnTmplThreshold=_CipslaTcpConnTmplThreshold_Object((1,3,6,1,4,1,9,9,636,1,3,1,10),_CipslaTcpConnTmplThreshold_Type())
cipslaTcpConnTmplThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplThreshold.setStatus(_A)
if mibBuilder.loadTexts:cipslaTcpConnTmplThreshold.setUnits(_F)
class _CipslaTcpConnTmplHistLives_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CipslaTcpConnTmplHistLives_Type.__name__=_D
_CipslaTcpConnTmplHistLives_Object=MibTableColumn
cipslaTcpConnTmplHistLives=_CipslaTcpConnTmplHistLives_Object((1,3,6,1,4,1,9,9,636,1,3,1,11),_CipslaTcpConnTmplHistLives_Type())
cipslaTcpConnTmplHistLives.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplHistLives.setStatus(_A)
class _CipslaTcpConnTmplHistBuckets_Type(Unsigned32):defaultValue=15;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_CipslaTcpConnTmplHistBuckets_Type.__name__=_D
_CipslaTcpConnTmplHistBuckets_Object=MibTableColumn
cipslaTcpConnTmplHistBuckets=_CipslaTcpConnTmplHistBuckets_Object((1,3,6,1,4,1,9,9,636,1,3,1,12),_CipslaTcpConnTmplHistBuckets_Type())
cipslaTcpConnTmplHistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplHistBuckets.setStatus(_A)
class _CipslaTcpConnTmplHistFilter_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_M,1),(_N,2),(_O,3),(_P,4)))
_CipslaTcpConnTmplHistFilter_Type.__name__=_I
_CipslaTcpConnTmplHistFilter_Object=MibTableColumn
cipslaTcpConnTmplHistFilter=_CipslaTcpConnTmplHistFilter_Object((1,3,6,1,4,1,9,9,636,1,3,1,13),_CipslaTcpConnTmplHistFilter_Type())
cipslaTcpConnTmplHistFilter.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplHistFilter.setStatus(_A)
class _CipslaTcpConnTmplStatsHours_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_CipslaTcpConnTmplStatsHours_Type.__name__=_D
_CipslaTcpConnTmplStatsHours_Object=MibTableColumn
cipslaTcpConnTmplStatsHours=_CipslaTcpConnTmplStatsHours_Object((1,3,6,1,4,1,9,9,636,1,3,1,14),_CipslaTcpConnTmplStatsHours_Type())
cipslaTcpConnTmplStatsHours.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplStatsHours.setStatus(_A)
if mibBuilder.loadTexts:cipslaTcpConnTmplStatsHours.setUnits(_Q)
class _CipslaTcpConnTmplDistBuckets_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CipslaTcpConnTmplDistBuckets_Type.__name__=_D
_CipslaTcpConnTmplDistBuckets_Object=MibTableColumn
cipslaTcpConnTmplDistBuckets=_CipslaTcpConnTmplDistBuckets_Object((1,3,6,1,4,1,9,9,636,1,3,1,15),_CipslaTcpConnTmplDistBuckets_Type())
cipslaTcpConnTmplDistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplDistBuckets.setStatus(_A)
class _CipslaTcpConnTmplDistInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CipslaTcpConnTmplDistInterval_Type.__name__=_D
_CipslaTcpConnTmplDistInterval_Object=MibTableColumn
cipslaTcpConnTmplDistInterval=_CipslaTcpConnTmplDistInterval_Object((1,3,6,1,4,1,9,9,636,1,3,1,16),_CipslaTcpConnTmplDistInterval_Type())
cipslaTcpConnTmplDistInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplDistInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaTcpConnTmplDistInterval.setUnits(_F)
class _CipslaTcpConnTmplStorageType_Type(StorageType):defaultValue=3
_CipslaTcpConnTmplStorageType_Type.__name__=_J
_CipslaTcpConnTmplStorageType_Object=MibTableColumn
cipslaTcpConnTmplStorageType=_CipslaTcpConnTmplStorageType_Object((1,3,6,1,4,1,9,9,636,1,3,1,17),_CipslaTcpConnTmplStorageType_Type())
cipslaTcpConnTmplStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplStorageType.setStatus(_A)
_CipslaTcpConnTmplRowStatus_Type=RowStatus
_CipslaTcpConnTmplRowStatus_Object=MibTableColumn
cipslaTcpConnTmplRowStatus=_CipslaTcpConnTmplRowStatus_Object((1,3,6,1,4,1,9,9,636,1,3,1,18),_CipslaTcpConnTmplRowStatus_Type())
cipslaTcpConnTmplRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaTcpConnTmplRowStatus.setStatus(_A)
_CiscoIpSlaEchoMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpSlaEchoMIBConform=_CiscoIpSlaEchoMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,636,2))
_CiscoIpSlaEchoMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpSlaEchoMIBCompliances=_CiscoIpSlaEchoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,636,2,1))
_CiscoIpSlaEchoMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpSlaEchoMIBGroups=_CiscoIpSlaEchoMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,636,2,2))
ciscoIpSlaIcmpEchoTmplGroup=ObjectGroup((1,3,6,1,4,1,9,9,636,2,2,1))
ciscoIpSlaIcmpEchoTmplGroup.setObjects(*((_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l)))
if mibBuilder.loadTexts:ciscoIpSlaIcmpEchoTmplGroup.setStatus(_A)
ciscoIpSlaUdpEchoTmplGroup=ObjectGroup((1,3,6,1,4,1,9,9,636,2,2,2))
ciscoIpSlaUdpEchoTmplGroup.setObjects(*((_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4)))
if mibBuilder.loadTexts:ciscoIpSlaUdpEchoTmplGroup.setStatus(_A)
ciscoIpSlaTcpConnTmplGroup=ObjectGroup((1,3,6,1,4,1,9,9,636,2,2,3))
ciscoIpSlaTcpConnTmplGroup.setObjects(*((_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ),(_B,_AK),(_B,_AL)))
if mibBuilder.loadTexts:ciscoIpSlaTcpConnTmplGroup.setStatus(_A)
ciscoIpSlaEchoMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,636,2,1,1))
ciscoIpSlaEchoMIBCompliance.setObjects(*((_B,_AM),(_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:ciscoIpSlaEchoMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpSlaEchoMIB':ciscoIpSlaEchoMIB,'ciscoIpSlaEchoMIBNotifs':ciscoIpSlaEchoMIBNotifs,'ciscoIpSlaEchoMIBObjects':ciscoIpSlaEchoMIBObjects,'cipslaIcmpEchoTmplTable':cipslaIcmpEchoTmplTable,'cipslaIcmpEchoTmplEntry':cipslaIcmpEchoTmplEntry,_R:cipslaIcmpEchoTmplName,_V:cipslaIcmpEchoTmplDescription,_W:cipslaIcmpEchoTmplSrcAddrType,_X:cipslaIcmpEchoTmplSrcAddr,_Y:cipslaIcmpEchoTmplTimeOut,_Z:cipslaIcmpEchoTmplVerifyData,_a:cipslaIcmpEchoTmplReqDataSize,_b:cipslaIcmpEchoTmplTOS,_c:cipslaIcmpEchoTmplVrfName,_d:cipslaIcmpEchoTmplThreshold,_e:cipslaIcmpEchoTmplHistLives,_f:cipslaIcmpEchoTmplHistBuckets,_g:cipslaIcmpEchoTmplHistFilter,_h:cipslaIcmpEchoTmplStatsHours,_i:cipslaIcmpEchoTmplDistBuckets,_j:cipslaIcmpEchoTmplDistInterval,_k:cipslaIcmpEchoTmplStorageType,_l:cipslaIcmpEchoTmplRowStatus,'cipslaUdpEchoTmplTable':cipslaUdpEchoTmplTable,'cipslaUdpEchoTmplEntry':cipslaUdpEchoTmplEntry,_T:cipslaUdpEchoTmplName,_m:cipslaUdpEchoTmplDescription,_n:cipslaUdpEchoTmplControlEnable,_o:cipslaUdpEchoTmplSrcAddrType,_p:cipslaUdpEchoTmplSrcAddr,_q:cipslaUdpEchoTmplSrcPort,_r:cipslaUdpEchoTmplTimeOut,_s:cipslaUdpEchoTmplVerifyData,_t:cipslaUdpEchoTmplReqDataSize,_u:cipslaUdpEchoTmplTOS,_v:cipslaUdpEchoTmplVrfName,_w:cipslaUdpEchoTmplThreshold,_x:cipslaUdpEchoTmplHistLives,_y:cipslaUdpEchoTmplHistBuckets,_z:cipslaUdpEchoTmplHistFilter,_A0:cipslaUdpEchoTmplStatsHours,_A1:cipslaUdpEchoTmplDistBuckets,_A2:cipslaUdpEchoTmplDistInterval,_A3:cipslaUdpEchoTmplStorageType,_A4:cipslaUdpEchoTmplRowStatus,'cipslaTcpConnTmplTable':cipslaTcpConnTmplTable,'cipslaTcpConnTmplEntry':cipslaTcpConnTmplEntry,_U:cipslaTcpConnTmplName,_A5:cipslaTcpConnTmplDescription,_A6:cipslaTcpConnTmplControlEnable,_A7:cipslaTcpConnTmplSrcAddrType,_A8:cipslaTcpConnTmplSrcAddr,_A9:cipslaTcpConnTmplSrcPort,_AA:cipslaTcpConnTmplTimeOut,_AB:cipslaTcpConnTmplVerifyData,_AC:cipslaTcpConnTmplTOS,_AD:cipslaTcpConnTmplThreshold,_AE:cipslaTcpConnTmplHistLives,_AF:cipslaTcpConnTmplHistBuckets,_AG:cipslaTcpConnTmplHistFilter,_AH:cipslaTcpConnTmplStatsHours,_AI:cipslaTcpConnTmplDistBuckets,_AJ:cipslaTcpConnTmplDistInterval,_AK:cipslaTcpConnTmplStorageType,_AL:cipslaTcpConnTmplRowStatus,'ciscoIpSlaEchoMIBConform':ciscoIpSlaEchoMIBConform,'ciscoIpSlaEchoMIBCompliances':ciscoIpSlaEchoMIBCompliances,'ciscoIpSlaEchoMIBCompliance':ciscoIpSlaEchoMIBCompliance,'ciscoIpSlaEchoMIBGroups':ciscoIpSlaEchoMIBGroups,_AM:ciscoIpSlaIcmpEchoTmplGroup,_AN:ciscoIpSlaUdpEchoTmplGroup,_AO:ciscoIpSlaTcpConnTmplGroup})