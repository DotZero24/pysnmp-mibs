_A9='ciscoIpSlaIcmpJitterTmplGroup'
_A8='ciscoIpSlaUdpJitterTmplGroup'
_A7='cipslaIcmpJitterTmplRowStatus'
_A6='cipslaIcmpJitterTmplStorageType'
_A5='cipslaIcmpJitterTmplDistInterval'
_A4='cipslaIcmpJitterTmplDistBuckets'
_A3='cipslaIcmpJitterTmplStatsHours'
_A2='cipslaIcmpJitterTmplThreshold'
_A1='cipslaIcmpJitterTmplVrfName'
_A0='cipslaIcmpJitterTmplTOS'
_z='cipslaIcmpJitterTmplSrcAddr'
_y='cipslaIcmpJitterTmplSrcAddrType'
_x='cipslaIcmpJitterTmplInterval'
_w='cipslaIcmpJitterTmplNumPkts'
_v='cipslaIcmpJitterTmplVerifyData'
_u='cipslaIcmpJitterTmplTimeOut'
_t='cipslaIcmpJitterTmplDescription'
_s='cipslaUdpJitterTmplRowStatus'
_r='cipslaUdpJitterTmplStorageType'
_q='cipslaUdpJitterTmplDistInterval'
_p='cipslaUdpJitterTmplDistBuckets'
_o='cipslaUdpJitterTmplStatsHours'
_n='cipslaUdpJitterTmplIcpifFactor'
_m='cipslaUdpJitterTmplNTPTolType'
_l='cipslaUdpJitterTmplNTPTolPct'
_k='cipslaUdpJitterTmplNTPTolAbs'
_j='cipslaUdpJitterTmplThreshold'
_i='cipslaUdpJitterTmplVrfName'
_h='cipslaUdpJitterTmplTOS'
_g='cipslaUdpJitterTmplPktPriority'
_f='cipslaUdpJitterTmplReqDataSize'
_e='cipslaUdpJitterTmplPrecision'
_d='cipslaUdpJitterTmplSrcPort'
_c='cipslaUdpJitterTmplSrcAddr'
_b='cipslaUdpJitterTmplSrcAddrType'
_a='cipslaUdpJitterTmplNumPkts'
_Z='cipslaUdpJitterTmplInterval'
_Y='cipslaUdpJitterTmplCodecNumPkts'
_X='cipslaUdpJitterTmplCodecPayload'
_W='cipslaUdpJitterTmplCodecInterval'
_V='cipslaUdpJitterTmplCodecType'
_U='cipslaUdpJitterTmplVerifyData'
_T='cipslaUdpJitterTmplTimeOut'
_S='cipslaUdpJitterTmplControlEnable'
_R='cipslaUdpJitterTmplDescription'
_Q='cipslaIcmpJitterTmplName'
_P='microseconds'
_O='octets'
_N='not-accessible'
_M='cipslaUdpJitterTmplName'
_L='InetPortNumber'
_K='packets'
_J='StorageType'
_I='InetAddressType'
_H='TruthValue'
_G='Integer32'
_F='SnmpAdminString'
_E='milliseconds'
_D='Unsigned32'
_C='read-create'
_B='CISCO-IPSLA-JITTER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
IpSlaCodecType,=mibBuilder.importSymbols('CISCO-IPSLA-TC-MIB','IpSlaCodecType')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InetAddress,InetAddressType,InetPortNumber=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_I,_L)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,StorageType,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus',_J,'TextualConvention',_H)
ciscoIpSlaJitterMIB=ModuleIdentity((1,3,6,1,4,1,9,9,635))
if mibBuilder.loadTexts:ciscoIpSlaJitterMIB.setRevisions(('2007-07-24 00:00',))
_CiscoIpSlaJitterMIBNotifs_ObjectIdentity=ObjectIdentity
ciscoIpSlaJitterMIBNotifs=_CiscoIpSlaJitterMIBNotifs_ObjectIdentity((1,3,6,1,4,1,9,9,635,0))
_CiscoIpSlaJitterMIBObjects_ObjectIdentity=ObjectIdentity
ciscoIpSlaJitterMIBObjects=_CiscoIpSlaJitterMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,635,1))
_CipslaUdpJitterTmplTable_Object=MibTable
cipslaUdpJitterTmplTable=_CipslaUdpJitterTmplTable_Object((1,3,6,1,4,1,9,9,635,1,1))
if mibBuilder.loadTexts:cipslaUdpJitterTmplTable.setStatus(_A)
_CipslaUdpJitterTmplEntry_Object=MibTableRow
cipslaUdpJitterTmplEntry=_CipslaUdpJitterTmplEntry_Object((1,3,6,1,4,1,9,9,635,1,1,1))
cipslaUdpJitterTmplEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:cipslaUdpJitterTmplEntry.setStatus(_A)
class _CipslaUdpJitterTmplName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaUdpJitterTmplName_Type.__name__=_F
_CipslaUdpJitterTmplName_Object=MibTableColumn
cipslaUdpJitterTmplName=_CipslaUdpJitterTmplName_Object((1,3,6,1,4,1,9,9,635,1,1,1,1),_CipslaUdpJitterTmplName_Type())
cipslaUdpJitterTmplName.setMaxAccess(_N)
if mibBuilder.loadTexts:cipslaUdpJitterTmplName.setStatus(_A)
class _CipslaUdpJitterTmplDescription_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CipslaUdpJitterTmplDescription_Type.__name__=_F
_CipslaUdpJitterTmplDescription_Object=MibTableColumn
cipslaUdpJitterTmplDescription=_CipslaUdpJitterTmplDescription_Object((1,3,6,1,4,1,9,9,635,1,1,1,2),_CipslaUdpJitterTmplDescription_Type())
cipslaUdpJitterTmplDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplDescription.setStatus(_A)
class _CipslaUdpJitterTmplControlEnable_Type(TruthValue):defaultValue=1
_CipslaUdpJitterTmplControlEnable_Type.__name__=_H
_CipslaUdpJitterTmplControlEnable_Object=MibTableColumn
cipslaUdpJitterTmplControlEnable=_CipslaUdpJitterTmplControlEnable_Object((1,3,6,1,4,1,9,9,635,1,1,1,3),_CipslaUdpJitterTmplControlEnable_Type())
cipslaUdpJitterTmplControlEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplControlEnable.setStatus(_A)
class _CipslaUdpJitterTmplTimeOut_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800000))
_CipslaUdpJitterTmplTimeOut_Type.__name__=_D
_CipslaUdpJitterTmplTimeOut_Object=MibTableColumn
cipslaUdpJitterTmplTimeOut=_CipslaUdpJitterTmplTimeOut_Object((1,3,6,1,4,1,9,9,635,1,1,1,4),_CipslaUdpJitterTmplTimeOut_Type())
cipslaUdpJitterTmplTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplTimeOut.setUnits(_E)
class _CipslaUdpJitterTmplVerifyData_Type(TruthValue):defaultValue=2
_CipslaUdpJitterTmplVerifyData_Type.__name__=_H
_CipslaUdpJitterTmplVerifyData_Object=MibTableColumn
cipslaUdpJitterTmplVerifyData=_CipslaUdpJitterTmplVerifyData_Object((1,3,6,1,4,1,9,9,635,1,1,1,5),_CipslaUdpJitterTmplVerifyData_Type())
cipslaUdpJitterTmplVerifyData.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplVerifyData.setStatus(_A)
_CipslaUdpJitterTmplCodecType_Type=IpSlaCodecType
_CipslaUdpJitterTmplCodecType_Object=MibTableColumn
cipslaUdpJitterTmplCodecType=_CipslaUdpJitterTmplCodecType_Object((1,3,6,1,4,1,9,9,635,1,1,1,6),_CipslaUdpJitterTmplCodecType_Type())
cipslaUdpJitterTmplCodecType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplCodecType.setStatus(_A)
class _CipslaUdpJitterTmplCodecInterval_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60000))
_CipslaUdpJitterTmplCodecInterval_Type.__name__=_D
_CipslaUdpJitterTmplCodecInterval_Object=MibTableColumn
cipslaUdpJitterTmplCodecInterval=_CipslaUdpJitterTmplCodecInterval_Object((1,3,6,1,4,1,9,9,635,1,1,1,7),_CipslaUdpJitterTmplCodecInterval_Type())
cipslaUdpJitterTmplCodecInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplCodecInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplCodecInterval.setUnits(_E)
class _CipslaUdpJitterTmplCodecPayload_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16384))
_CipslaUdpJitterTmplCodecPayload_Type.__name__=_D
_CipslaUdpJitterTmplCodecPayload_Object=MibTableColumn
cipslaUdpJitterTmplCodecPayload=_CipslaUdpJitterTmplCodecPayload_Object((1,3,6,1,4,1,9,9,635,1,1,1,8),_CipslaUdpJitterTmplCodecPayload_Type())
cipslaUdpJitterTmplCodecPayload.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplCodecPayload.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplCodecPayload.setUnits(_O)
class _CipslaUdpJitterTmplCodecNumPkts_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_CipslaUdpJitterTmplCodecNumPkts_Type.__name__=_D
_CipslaUdpJitterTmplCodecNumPkts_Object=MibTableColumn
cipslaUdpJitterTmplCodecNumPkts=_CipslaUdpJitterTmplCodecNumPkts_Object((1,3,6,1,4,1,9,9,635,1,1,1,9),_CipslaUdpJitterTmplCodecNumPkts_Type())
cipslaUdpJitterTmplCodecNumPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplCodecNumPkts.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplCodecNumPkts.setUnits(_K)
class _CipslaUdpJitterTmplInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60000))
_CipslaUdpJitterTmplInterval_Type.__name__=_D
_CipslaUdpJitterTmplInterval_Object=MibTableColumn
cipslaUdpJitterTmplInterval=_CipslaUdpJitterTmplInterval_Object((1,3,6,1,4,1,9,9,635,1,1,1,10),_CipslaUdpJitterTmplInterval_Type())
cipslaUdpJitterTmplInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplInterval.setUnits(_E)
class _CipslaUdpJitterTmplNumPkts_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_CipslaUdpJitterTmplNumPkts_Type.__name__=_D
_CipslaUdpJitterTmplNumPkts_Object=MibTableColumn
cipslaUdpJitterTmplNumPkts=_CipslaUdpJitterTmplNumPkts_Object((1,3,6,1,4,1,9,9,635,1,1,1,11),_CipslaUdpJitterTmplNumPkts_Type())
cipslaUdpJitterTmplNumPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplNumPkts.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplNumPkts.setUnits(_K)
class _CipslaUdpJitterTmplSrcAddrType_Type(InetAddressType):defaultValue=1
_CipslaUdpJitterTmplSrcAddrType_Type.__name__=_I
_CipslaUdpJitterTmplSrcAddrType_Object=MibTableColumn
cipslaUdpJitterTmplSrcAddrType=_CipslaUdpJitterTmplSrcAddrType_Object((1,3,6,1,4,1,9,9,635,1,1,1,12),_CipslaUdpJitterTmplSrcAddrType_Type())
cipslaUdpJitterTmplSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplSrcAddrType.setStatus(_A)
_CipslaUdpJitterTmplSrcAddr_Type=InetAddress
_CipslaUdpJitterTmplSrcAddr_Object=MibTableColumn
cipslaUdpJitterTmplSrcAddr=_CipslaUdpJitterTmplSrcAddr_Object((1,3,6,1,4,1,9,9,635,1,1,1,13),_CipslaUdpJitterTmplSrcAddr_Type())
cipslaUdpJitterTmplSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplSrcAddr.setStatus(_A)
class _CipslaUdpJitterTmplSrcPort_Type(InetPortNumber):defaultValue=0
_CipslaUdpJitterTmplSrcPort_Type.__name__=_L
_CipslaUdpJitterTmplSrcPort_Object=MibTableColumn
cipslaUdpJitterTmplSrcPort=_CipslaUdpJitterTmplSrcPort_Object((1,3,6,1,4,1,9,9,635,1,1,1,14),_CipslaUdpJitterTmplSrcPort_Type())
cipslaUdpJitterTmplSrcPort.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplSrcPort.setStatus(_A)
class _CipslaUdpJitterTmplPrecision_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_P,2)))
_CipslaUdpJitterTmplPrecision_Type.__name__=_G
_CipslaUdpJitterTmplPrecision_Object=MibTableColumn
cipslaUdpJitterTmplPrecision=_CipslaUdpJitterTmplPrecision_Object((1,3,6,1,4,1,9,9,635,1,1,1,15),_CipslaUdpJitterTmplPrecision_Type())
cipslaUdpJitterTmplPrecision.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplPrecision.setStatus(_A)
class _CipslaUdpJitterTmplReqDataSize_Type(Unsigned32):defaultValue=32;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,65024))
_CipslaUdpJitterTmplReqDataSize_Type.__name__=_D
_CipslaUdpJitterTmplReqDataSize_Object=MibTableColumn
cipslaUdpJitterTmplReqDataSize=_CipslaUdpJitterTmplReqDataSize_Object((1,3,6,1,4,1,9,9,635,1,1,1,16),_CipslaUdpJitterTmplReqDataSize_Type())
cipslaUdpJitterTmplReqDataSize.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplReqDataSize.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplReqDataSize.setUnits(_O)
class _CipslaUdpJitterTmplPktPriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('normal',1),('high',2)))
_CipslaUdpJitterTmplPktPriority_Type.__name__=_G
_CipslaUdpJitterTmplPktPriority_Object=MibTableColumn
cipslaUdpJitterTmplPktPriority=_CipslaUdpJitterTmplPktPriority_Object((1,3,6,1,4,1,9,9,635,1,1,1,17),_CipslaUdpJitterTmplPktPriority_Type())
cipslaUdpJitterTmplPktPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplPktPriority.setStatus(_A)
class _CipslaUdpJitterTmplTOS_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CipslaUdpJitterTmplTOS_Type.__name__=_D
_CipslaUdpJitterTmplTOS_Object=MibTableColumn
cipslaUdpJitterTmplTOS=_CipslaUdpJitterTmplTOS_Object((1,3,6,1,4,1,9,9,635,1,1,1,18),_CipslaUdpJitterTmplTOS_Type())
cipslaUdpJitterTmplTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplTOS.setStatus(_A)
class _CipslaUdpJitterTmplVrfName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CipslaUdpJitterTmplVrfName_Type.__name__=_F
_CipslaUdpJitterTmplVrfName_Object=MibTableColumn
cipslaUdpJitterTmplVrfName=_CipslaUdpJitterTmplVrfName_Object((1,3,6,1,4,1,9,9,635,1,1,1,19),_CipslaUdpJitterTmplVrfName_Type())
cipslaUdpJitterTmplVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplVrfName.setStatus(_A)
class _CipslaUdpJitterTmplThreshold_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CipslaUdpJitterTmplThreshold_Type.__name__=_D
_CipslaUdpJitterTmplThreshold_Object=MibTableColumn
cipslaUdpJitterTmplThreshold=_CipslaUdpJitterTmplThreshold_Object((1,3,6,1,4,1,9,9,635,1,1,1,20),_CipslaUdpJitterTmplThreshold_Type())
cipslaUdpJitterTmplThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplThreshold.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplThreshold.setUnits(_E)
class _CipslaUdpJitterTmplNTPTolAbs_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000))
_CipslaUdpJitterTmplNTPTolAbs_Type.__name__=_D
_CipslaUdpJitterTmplNTPTolAbs_Object=MibTableColumn
cipslaUdpJitterTmplNTPTolAbs=_CipslaUdpJitterTmplNTPTolAbs_Object((1,3,6,1,4,1,9,9,635,1,1,1,21),_CipslaUdpJitterTmplNTPTolAbs_Type())
cipslaUdpJitterTmplNTPTolAbs.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplNTPTolAbs.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplNTPTolAbs.setUnits(_P)
class _CipslaUdpJitterTmplNTPTolPct_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CipslaUdpJitterTmplNTPTolPct_Type.__name__=_D
_CipslaUdpJitterTmplNTPTolPct_Object=MibTableColumn
cipslaUdpJitterTmplNTPTolPct=_CipslaUdpJitterTmplNTPTolPct_Object((1,3,6,1,4,1,9,9,635,1,1,1,22),_CipslaUdpJitterTmplNTPTolPct_Type())
cipslaUdpJitterTmplNTPTolPct.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplNTPTolPct.setStatus(_A)
class _CipslaUdpJitterTmplNTPTolType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('percent',1),('absolute',2)))
_CipslaUdpJitterTmplNTPTolType_Type.__name__=_G
_CipslaUdpJitterTmplNTPTolType_Object=MibTableColumn
cipslaUdpJitterTmplNTPTolType=_CipslaUdpJitterTmplNTPTolType_Object((1,3,6,1,4,1,9,9,635,1,1,1,23),_CipslaUdpJitterTmplNTPTolType_Type())
cipslaUdpJitterTmplNTPTolType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplNTPTolType.setStatus(_A)
class _CipslaUdpJitterTmplIcpifFactor_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20))
_CipslaUdpJitterTmplIcpifFactor_Type.__name__=_D
_CipslaUdpJitterTmplIcpifFactor_Object=MibTableColumn
cipslaUdpJitterTmplIcpifFactor=_CipslaUdpJitterTmplIcpifFactor_Object((1,3,6,1,4,1,9,9,635,1,1,1,24),_CipslaUdpJitterTmplIcpifFactor_Type())
cipslaUdpJitterTmplIcpifFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplIcpifFactor.setStatus(_A)
class _CipslaUdpJitterTmplStatsHours_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_CipslaUdpJitterTmplStatsHours_Type.__name__=_D
_CipslaUdpJitterTmplStatsHours_Object=MibTableColumn
cipslaUdpJitterTmplStatsHours=_CipslaUdpJitterTmplStatsHours_Object((1,3,6,1,4,1,9,9,635,1,1,1,25),_CipslaUdpJitterTmplStatsHours_Type())
cipslaUdpJitterTmplStatsHours.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplStatsHours.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplStatsHours.setUnits('hours')
class _CipslaUdpJitterTmplDistBuckets_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CipslaUdpJitterTmplDistBuckets_Type.__name__=_D
_CipslaUdpJitterTmplDistBuckets_Object=MibTableColumn
cipslaUdpJitterTmplDistBuckets=_CipslaUdpJitterTmplDistBuckets_Object((1,3,6,1,4,1,9,9,635,1,1,1,26),_CipslaUdpJitterTmplDistBuckets_Type())
cipslaUdpJitterTmplDistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplDistBuckets.setStatus(_A)
class _CipslaUdpJitterTmplDistInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CipslaUdpJitterTmplDistInterval_Type.__name__=_D
_CipslaUdpJitterTmplDistInterval_Object=MibTableColumn
cipslaUdpJitterTmplDistInterval=_CipslaUdpJitterTmplDistInterval_Object((1,3,6,1,4,1,9,9,635,1,1,1,27),_CipslaUdpJitterTmplDistInterval_Type())
cipslaUdpJitterTmplDistInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplDistInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaUdpJitterTmplDistInterval.setUnits(_E)
class _CipslaUdpJitterTmplStorageType_Type(StorageType):defaultValue=3
_CipslaUdpJitterTmplStorageType_Type.__name__=_J
_CipslaUdpJitterTmplStorageType_Object=MibTableColumn
cipslaUdpJitterTmplStorageType=_CipslaUdpJitterTmplStorageType_Object((1,3,6,1,4,1,9,9,635,1,1,1,28),_CipslaUdpJitterTmplStorageType_Type())
cipslaUdpJitterTmplStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplStorageType.setStatus(_A)
_CipslaUdpJitterTmplRowStatus_Type=RowStatus
_CipslaUdpJitterTmplRowStatus_Object=MibTableColumn
cipslaUdpJitterTmplRowStatus=_CipslaUdpJitterTmplRowStatus_Object((1,3,6,1,4,1,9,9,635,1,1,1,30),_CipslaUdpJitterTmplRowStatus_Type())
cipslaUdpJitterTmplRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaUdpJitterTmplRowStatus.setStatus(_A)
_CipslaIcmpJitterTmplTable_Object=MibTable
cipslaIcmpJitterTmplTable=_CipslaIcmpJitterTmplTable_Object((1,3,6,1,4,1,9,9,635,1,2))
if mibBuilder.loadTexts:cipslaIcmpJitterTmplTable.setStatus(_A)
_CipslaIcmpJitterTmplEntry_Object=MibTableRow
cipslaIcmpJitterTmplEntry=_CipslaIcmpJitterTmplEntry_Object((1,3,6,1,4,1,9,9,635,1,2,1))
cipslaIcmpJitterTmplEntry.setIndexNames((0,_B,_Q))
if mibBuilder.loadTexts:cipslaIcmpJitterTmplEntry.setStatus(_A)
class _CipslaIcmpJitterTmplName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CipslaIcmpJitterTmplName_Type.__name__=_F
_CipslaIcmpJitterTmplName_Object=MibTableColumn
cipslaIcmpJitterTmplName=_CipslaIcmpJitterTmplName_Object((1,3,6,1,4,1,9,9,635,1,2,1,1),_CipslaIcmpJitterTmplName_Type())
cipslaIcmpJitterTmplName.setMaxAccess(_N)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplName.setStatus(_A)
class _CipslaIcmpJitterTmplDescription_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CipslaIcmpJitterTmplDescription_Type.__name__=_F
_CipslaIcmpJitterTmplDescription_Object=MibTableColumn
cipslaIcmpJitterTmplDescription=_CipslaIcmpJitterTmplDescription_Object((1,3,6,1,4,1,9,9,635,1,2,1,2),_CipslaIcmpJitterTmplDescription_Type())
cipslaIcmpJitterTmplDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplDescription.setStatus(_A)
class _CipslaIcmpJitterTmplTimeOut_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,604800000))
_CipslaIcmpJitterTmplTimeOut_Type.__name__=_D
_CipslaIcmpJitterTmplTimeOut_Object=MibTableColumn
cipslaIcmpJitterTmplTimeOut=_CipslaIcmpJitterTmplTimeOut_Object((1,3,6,1,4,1,9,9,635,1,2,1,3),_CipslaIcmpJitterTmplTimeOut_Type())
cipslaIcmpJitterTmplTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplTimeOut.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplTimeOut.setUnits(_E)
class _CipslaIcmpJitterTmplVerifyData_Type(TruthValue):defaultValue=2
_CipslaIcmpJitterTmplVerifyData_Type.__name__=_H
_CipslaIcmpJitterTmplVerifyData_Object=MibTableColumn
cipslaIcmpJitterTmplVerifyData=_CipslaIcmpJitterTmplVerifyData_Object((1,3,6,1,4,1,9,9,635,1,2,1,4),_CipslaIcmpJitterTmplVerifyData_Type())
cipslaIcmpJitterTmplVerifyData.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplVerifyData.setStatus(_A)
class _CipslaIcmpJitterTmplNumPkts_Type(Unsigned32):defaultValue=10;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60000))
_CipslaIcmpJitterTmplNumPkts_Type.__name__=_D
_CipslaIcmpJitterTmplNumPkts_Object=MibTableColumn
cipslaIcmpJitterTmplNumPkts=_CipslaIcmpJitterTmplNumPkts_Object((1,3,6,1,4,1,9,9,635,1,2,1,5),_CipslaIcmpJitterTmplNumPkts_Type())
cipslaIcmpJitterTmplNumPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplNumPkts.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplNumPkts.setUnits(_K)
class _CipslaIcmpJitterTmplInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(4,60000))
_CipslaIcmpJitterTmplInterval_Type.__name__=_D
_CipslaIcmpJitterTmplInterval_Object=MibTableColumn
cipslaIcmpJitterTmplInterval=_CipslaIcmpJitterTmplInterval_Object((1,3,6,1,4,1,9,9,635,1,2,1,6),_CipslaIcmpJitterTmplInterval_Type())
cipslaIcmpJitterTmplInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplInterval.setUnits(_E)
class _CipslaIcmpJitterTmplSrcAddrType_Type(InetAddressType):defaultValue=1
_CipslaIcmpJitterTmplSrcAddrType_Type.__name__=_I
_CipslaIcmpJitterTmplSrcAddrType_Object=MibTableColumn
cipslaIcmpJitterTmplSrcAddrType=_CipslaIcmpJitterTmplSrcAddrType_Object((1,3,6,1,4,1,9,9,635,1,2,1,7),_CipslaIcmpJitterTmplSrcAddrType_Type())
cipslaIcmpJitterTmplSrcAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplSrcAddrType.setStatus(_A)
_CipslaIcmpJitterTmplSrcAddr_Type=InetAddress
_CipslaIcmpJitterTmplSrcAddr_Object=MibTableColumn
cipslaIcmpJitterTmplSrcAddr=_CipslaIcmpJitterTmplSrcAddr_Object((1,3,6,1,4,1,9,9,635,1,2,1,8),_CipslaIcmpJitterTmplSrcAddr_Type())
cipslaIcmpJitterTmplSrcAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplSrcAddr.setStatus(_A)
class _CipslaIcmpJitterTmplTOS_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CipslaIcmpJitterTmplTOS_Type.__name__=_D
_CipslaIcmpJitterTmplTOS_Object=MibTableColumn
cipslaIcmpJitterTmplTOS=_CipslaIcmpJitterTmplTOS_Object((1,3,6,1,4,1,9,9,635,1,2,1,9),_CipslaIcmpJitterTmplTOS_Type())
cipslaIcmpJitterTmplTOS.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplTOS.setStatus(_A)
class _CipslaIcmpJitterTmplVrfName_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CipslaIcmpJitterTmplVrfName_Type.__name__=_F
_CipslaIcmpJitterTmplVrfName_Object=MibTableColumn
cipslaIcmpJitterTmplVrfName=_CipslaIcmpJitterTmplVrfName_Object((1,3,6,1,4,1,9,9,635,1,2,1,10),_CipslaIcmpJitterTmplVrfName_Type())
cipslaIcmpJitterTmplVrfName.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplVrfName.setStatus(_A)
class _CipslaIcmpJitterTmplThreshold_Type(Unsigned32):defaultValue=5000;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_CipslaIcmpJitterTmplThreshold_Type.__name__=_D
_CipslaIcmpJitterTmplThreshold_Object=MibTableColumn
cipslaIcmpJitterTmplThreshold=_CipslaIcmpJitterTmplThreshold_Object((1,3,6,1,4,1,9,9,635,1,2,1,11),_CipslaIcmpJitterTmplThreshold_Type())
cipslaIcmpJitterTmplThreshold.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplThreshold.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplThreshold.setUnits(_E)
class _CipslaIcmpJitterTmplStatsHours_Type(Unsigned32):defaultValue=2;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,25))
_CipslaIcmpJitterTmplStatsHours_Type.__name__=_D
_CipslaIcmpJitterTmplStatsHours_Object=MibTableColumn
cipslaIcmpJitterTmplStatsHours=_CipslaIcmpJitterTmplStatsHours_Object((1,3,6,1,4,1,9,9,635,1,2,1,12),_CipslaIcmpJitterTmplStatsHours_Type())
cipslaIcmpJitterTmplStatsHours.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplStatsHours.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplStatsHours.setUnits('hours')
class _CipslaIcmpJitterTmplDistBuckets_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,20))
_CipslaIcmpJitterTmplDistBuckets_Type.__name__=_D
_CipslaIcmpJitterTmplDistBuckets_Object=MibTableColumn
cipslaIcmpJitterTmplDistBuckets=_CipslaIcmpJitterTmplDistBuckets_Object((1,3,6,1,4,1,9,9,635,1,2,1,13),_CipslaIcmpJitterTmplDistBuckets_Type())
cipslaIcmpJitterTmplDistBuckets.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplDistBuckets.setStatus(_A)
class _CipslaIcmpJitterTmplDistInterval_Type(Unsigned32):defaultValue=20;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CipslaIcmpJitterTmplDistInterval_Type.__name__=_D
_CipslaIcmpJitterTmplDistInterval_Object=MibTableColumn
cipslaIcmpJitterTmplDistInterval=_CipslaIcmpJitterTmplDistInterval_Object((1,3,6,1,4,1,9,9,635,1,2,1,14),_CipslaIcmpJitterTmplDistInterval_Type())
cipslaIcmpJitterTmplDistInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplDistInterval.setStatus(_A)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplDistInterval.setUnits(_E)
class _CipslaIcmpJitterTmplStorageType_Type(StorageType):defaultValue=3
_CipslaIcmpJitterTmplStorageType_Type.__name__=_J
_CipslaIcmpJitterTmplStorageType_Object=MibTableColumn
cipslaIcmpJitterTmplStorageType=_CipslaIcmpJitterTmplStorageType_Object((1,3,6,1,4,1,9,9,635,1,2,1,15),_CipslaIcmpJitterTmplStorageType_Type())
cipslaIcmpJitterTmplStorageType.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplStorageType.setStatus(_A)
_CipslaIcmpJitterTmplRowStatus_Type=RowStatus
_CipslaIcmpJitterTmplRowStatus_Object=MibTableColumn
cipslaIcmpJitterTmplRowStatus=_CipslaIcmpJitterTmplRowStatus_Object((1,3,6,1,4,1,9,9,635,1,2,1,16),_CipslaIcmpJitterTmplRowStatus_Type())
cipslaIcmpJitterTmplRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cipslaIcmpJitterTmplRowStatus.setStatus(_A)
_CiscoIpSlaJitterMIBConform_ObjectIdentity=ObjectIdentity
ciscoIpSlaJitterMIBConform=_CiscoIpSlaJitterMIBConform_ObjectIdentity((1,3,6,1,4,1,9,9,635,2))
_CiscoIpSlaJitterMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoIpSlaJitterMIBCompliances=_CiscoIpSlaJitterMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,635,2,1))
_CiscoIpSlaJitterMIBGroups_ObjectIdentity=ObjectIdentity
ciscoIpSlaJitterMIBGroups=_CiscoIpSlaJitterMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,635,2,2))
ciscoIpSlaUdpJitterTmplGroup=ObjectGroup((1,3,6,1,4,1,9,9,635,2,2,1))
ciscoIpSlaUdpJitterTmplGroup.setObjects(*((_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s)))
if mibBuilder.loadTexts:ciscoIpSlaUdpJitterTmplGroup.setStatus(_A)
ciscoIpSlaIcmpJitterTmplGroup=ObjectGroup((1,3,6,1,4,1,9,9,635,2,2,2))
ciscoIpSlaIcmpJitterTmplGroup.setObjects(*((_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7)))
if mibBuilder.loadTexts:ciscoIpSlaIcmpJitterTmplGroup.setStatus(_A)
ciscoIpSlaJitterMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,635,2,1,1))
ciscoIpSlaJitterMIBCompliance.setObjects(*((_B,_A8),(_B,_A9)))
if mibBuilder.loadTexts:ciscoIpSlaJitterMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoIpSlaJitterMIB':ciscoIpSlaJitterMIB,'ciscoIpSlaJitterMIBNotifs':ciscoIpSlaJitterMIBNotifs,'ciscoIpSlaJitterMIBObjects':ciscoIpSlaJitterMIBObjects,'cipslaUdpJitterTmplTable':cipslaUdpJitterTmplTable,'cipslaUdpJitterTmplEntry':cipslaUdpJitterTmplEntry,_M:cipslaUdpJitterTmplName,_R:cipslaUdpJitterTmplDescription,_S:cipslaUdpJitterTmplControlEnable,_T:cipslaUdpJitterTmplTimeOut,_U:cipslaUdpJitterTmplVerifyData,_V:cipslaUdpJitterTmplCodecType,_W:cipslaUdpJitterTmplCodecInterval,_X:cipslaUdpJitterTmplCodecPayload,_Y:cipslaUdpJitterTmplCodecNumPkts,_Z:cipslaUdpJitterTmplInterval,_a:cipslaUdpJitterTmplNumPkts,_b:cipslaUdpJitterTmplSrcAddrType,_c:cipslaUdpJitterTmplSrcAddr,_d:cipslaUdpJitterTmplSrcPort,_e:cipslaUdpJitterTmplPrecision,_f:cipslaUdpJitterTmplReqDataSize,_g:cipslaUdpJitterTmplPktPriority,_h:cipslaUdpJitterTmplTOS,_i:cipslaUdpJitterTmplVrfName,_j:cipslaUdpJitterTmplThreshold,_k:cipslaUdpJitterTmplNTPTolAbs,_l:cipslaUdpJitterTmplNTPTolPct,_m:cipslaUdpJitterTmplNTPTolType,_n:cipslaUdpJitterTmplIcpifFactor,_o:cipslaUdpJitterTmplStatsHours,_p:cipslaUdpJitterTmplDistBuckets,_q:cipslaUdpJitterTmplDistInterval,_r:cipslaUdpJitterTmplStorageType,_s:cipslaUdpJitterTmplRowStatus,'cipslaIcmpJitterTmplTable':cipslaIcmpJitterTmplTable,'cipslaIcmpJitterTmplEntry':cipslaIcmpJitterTmplEntry,_Q:cipslaIcmpJitterTmplName,_t:cipslaIcmpJitterTmplDescription,_u:cipslaIcmpJitterTmplTimeOut,_v:cipslaIcmpJitterTmplVerifyData,_w:cipslaIcmpJitterTmplNumPkts,_x:cipslaIcmpJitterTmplInterval,_y:cipslaIcmpJitterTmplSrcAddrType,_z:cipslaIcmpJitterTmplSrcAddr,_A0:cipslaIcmpJitterTmplTOS,_A1:cipslaIcmpJitterTmplVrfName,_A2:cipslaIcmpJitterTmplThreshold,_A3:cipslaIcmpJitterTmplStatsHours,_A4:cipslaIcmpJitterTmplDistBuckets,_A5:cipslaIcmpJitterTmplDistInterval,_A6:cipslaIcmpJitterTmplStorageType,_A7:cipslaIcmpJitterTmplRowStatus,'ciscoIpSlaJitterMIBConform':ciscoIpSlaJitterMIBConform,'ciscoIpSlaJitterMIBCompliances':ciscoIpSlaJitterMIBCompliances,'ciscoIpSlaJitterMIBCompliance':ciscoIpSlaJitterMIBCompliance,'ciscoIpSlaJitterMIBGroups':ciscoIpSlaJitterMIBGroups,_A8:ciscoIpSlaUdpJitterTmplGroup,_A9:ciscoIpSlaIcmpJitterTmplGroup})