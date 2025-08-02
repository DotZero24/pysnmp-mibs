_AJ='cAAASvrExtGenericConfGroup2'
_AI='cAAASvrExtSvrMonitorConfGroup'
_AH='cAAASvrExtSvrGroupLDAPConfGroup'
_AG='cAAASvrExtSvrTableLDAPConfGroup'
_AF='cAAASvrExtSvrGroupConfGroup2'
_AE='cAAASvrExtProtoParamConfigGroup1'
_AD='cAAASvrExtGenericConfGroup'
_AC='cAAAServerTestPassword'
_AB='cAAAServerTestUser'
_AA='cAAAServerIdleTime'
_A9='cAAASvrGrpLDAPUserProfile'
_A8='cAAASvrGrpLDAPFilterUser'
_A7='cAAASvrGrpLDAPBaseDN'
_A6='cAAAServerRootDN'
_A5='cAAAServerProtoDirectedReq'
_A4='cAAASvrGrpConfigDeadTime'
_A3='cAAALoginAuthTypeMSCHAP'
_A2='cAAASvrExtClearAccLog'
_A1='cAAASvrExtAppToSvrGrpMaxEnt'
_A0='cAAASvrGrpList'
_z='cAAASvrGrpTrivial'
_y='cAAASvrGrpLocal'
_x='cAAAServerRetransmits'
_w='cAAAServerTimeOut'
_v='cAAAServerDeadTime'
_u='cAAAServerKeyEncrType'
_t='cAAAServerAddr'
_s='cAAAServerAddrType'
_r='cAAASvrExtConfigEntry'
_q='cAAAFunction'
_p='cAAAApplicationSubType'
_o='cAAAApplicationType'
_n='cAAAServerProtocol'
_m='retransmits'
_l='seconds'
_k='DisplayString'
_j='InetAddressType'
_i='CiscoAAAProtocol'
_h='cAAASvrExtGenericConfGroup1'
_g='cAAASvrExtSvrGroupConfGroup'
_f='cAAASvrExtProtoParamConfigGroup'
_e='cAAASvrExtSvrGrpSvrListMaxEnt'
_d='cAAASvrGrpConfigRowStatus'
_c='cAAAServerList'
_b='cAAASvrGrpProtocol'
_a='cAAASvrGrpName'
_Z='cAAAServerProtoSvrTableMaxEnt'
_Y='cAAAServerProtoRetransmits'
_X='cAAAServerProtoTimeOut'
_W='cAAAServerProtoDeadTime'
_V='cAAAServerProtoKeyEncrType'
_U='cAAAServerProtoAuthKey'
_T='cAAASvrExtLocalAccLogMaxSize'
_S='cAAASvrGrpIndex'
_R='CiscoAAAServerKeyEncrType'
_Q='read-only'
_P='TruthValue'
_O='TimeIntervalSec'
_N='OctetString'
_M='cAAASvrExtAppSvrGroupConfGroup'
_L='cAAASvrExtSvrTableConfGroup'
_K='minutes'
_J='deprecated'
_I='not-accessible'
_H='Integer32'
_G='TimeIntervalMin'
_F='Unsigned32'
_E='SnmpAdminString'
_D='read-write'
_C='read-create'
_B='current'
_A='CISCO-AAA-SERVER-EXT-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_N,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
CiscoAAAProtocol,casConfigEntry=mibBuilder.importSymbols('CISCO-AAA-SERVER-MIB',_i,'casConfigEntry')
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
TimeIntervalMin,TimeIntervalSec=mibBuilder.importSymbols('CISCO-TC',_G,_O)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress',_j)
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB',_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_k,'PhysAddress','RowStatus','TextualConvention',_P)
ciscoAAAServerExtMIB=ModuleIdentity((1,3,6,1,4,1,9,9,367))
if mibBuilder.loadTexts:ciscoAAAServerExtMIB.setRevisions(('2005-05-23 00:00','2005-05-09 00:00','2003-11-14 00:00'))
class CiscoAAAServerKeyEncrType(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('plain',1),('encrypted',2),('notConfigured',3)))
_CiscoAAASvrExtMIBObjects_ObjectIdentity=ObjectIdentity
ciscoAAASvrExtMIBObjects=_CiscoAAASvrExtMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,367,1))
_CAAASvrExtGenericConfig_ObjectIdentity=ObjectIdentity
cAAASvrExtGenericConfig=_CAAASvrExtGenericConfig_ObjectIdentity((1,3,6,1,4,1,9,9,367,1,1))
class _CAAASvrExtLocalAccLogMaxSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100000000))
_CAAASvrExtLocalAccLogMaxSize_Type.__name__=_F
_CAAASvrExtLocalAccLogMaxSize_Object=MibScalar
cAAASvrExtLocalAccLogMaxSize=_CAAASvrExtLocalAccLogMaxSize_Object((1,3,6,1,4,1,9,9,367,1,1,1),_CAAASvrExtLocalAccLogMaxSize_Type())
cAAASvrExtLocalAccLogMaxSize.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAASvrExtLocalAccLogMaxSize.setStatus(_B)
if mibBuilder.loadTexts:cAAASvrExtLocalAccLogMaxSize.setUnits('bytes')
class _CAAASvrExtSvrGrpSvrListMaxEnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CAAASvrExtSvrGrpSvrListMaxEnt_Type.__name__=_F
_CAAASvrExtSvrGrpSvrListMaxEnt_Object=MibScalar
cAAASvrExtSvrGrpSvrListMaxEnt=_CAAASvrExtSvrGrpSvrListMaxEnt_Object((1,3,6,1,4,1,9,9,367,1,1,2),_CAAASvrExtSvrGrpSvrListMaxEnt_Type())
cAAASvrExtSvrGrpSvrListMaxEnt.setMaxAccess(_Q)
if mibBuilder.loadTexts:cAAASvrExtSvrGrpSvrListMaxEnt.setStatus(_B)
class _CAAASvrExtAppToSvrGrpMaxEnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,64))
_CAAASvrExtAppToSvrGrpMaxEnt_Type.__name__=_F
_CAAASvrExtAppToSvrGrpMaxEnt_Object=MibScalar
cAAASvrExtAppToSvrGrpMaxEnt=_CAAASvrExtAppToSvrGrpMaxEnt_Object((1,3,6,1,4,1,9,9,367,1,1,3),_CAAASvrExtAppToSvrGrpMaxEnt_Type())
cAAASvrExtAppToSvrGrpMaxEnt.setMaxAccess(_Q)
if mibBuilder.loadTexts:cAAASvrExtAppToSvrGrpMaxEnt.setStatus(_B)
class _CAAASvrExtClearAccLog_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clear',1),('noOp',2)))
_CAAASvrExtClearAccLog_Type.__name__=_H
_CAAASvrExtClearAccLog_Object=MibScalar
cAAASvrExtClearAccLog=_CAAASvrExtClearAccLog_Object((1,3,6,1,4,1,9,9,367,1,1,4),_CAAASvrExtClearAccLog_Type())
cAAASvrExtClearAccLog.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAASvrExtClearAccLog.setStatus(_B)
class _CAAALoginAuthTypeMSCHAP_Type(TruthValue):defaultValue=2
_CAAALoginAuthTypeMSCHAP_Type.__name__=_P
_CAAALoginAuthTypeMSCHAP_Object=MibScalar
cAAALoginAuthTypeMSCHAP=_CAAALoginAuthTypeMSCHAP_Object((1,3,6,1,4,1,9,9,367,1,1,5),_CAAALoginAuthTypeMSCHAP_Type())
cAAALoginAuthTypeMSCHAP.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAALoginAuthTypeMSCHAP.setStatus(_B)
_CAAASvrExtSvrTableConfig_ObjectIdentity=ObjectIdentity
cAAASvrExtSvrTableConfig=_CAAASvrExtSvrTableConfig_ObjectIdentity((1,3,6,1,4,1,9,9,367,1,2))
_CAAASvrExtConfigTable_Object=MibTable
cAAASvrExtConfigTable=_CAAASvrExtConfigTable_Object((1,3,6,1,4,1,9,9,367,1,2,1))
if mibBuilder.loadTexts:cAAASvrExtConfigTable.setStatus(_B)
_CAAASvrExtConfigEntry_Object=MibTableRow
cAAASvrExtConfigEntry=_CAAASvrExtConfigEntry_Object((1,3,6,1,4,1,9,9,367,1,2,1,1))
if mibBuilder.loadTexts:cAAASvrExtConfigEntry.setStatus(_B)
class _CAAAServerAddrType_Type(InetAddressType):defaultValue=1
_CAAAServerAddrType_Type.__name__=_j
_CAAAServerAddrType_Object=MibTableColumn
cAAAServerAddrType=_CAAAServerAddrType_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,1),_CAAAServerAddrType_Type())
cAAAServerAddrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerAddrType.setStatus(_B)
_CAAAServerAddr_Type=InetAddress
_CAAAServerAddr_Object=MibTableColumn
cAAAServerAddr=_CAAAServerAddr_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,2),_CAAAServerAddr_Type())
cAAAServerAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerAddr.setStatus(_B)
class _CAAAServerKeyEncrType_Type(CiscoAAAServerKeyEncrType):defaultValue=1
_CAAAServerKeyEncrType_Type.__name__=_R
_CAAAServerKeyEncrType_Object=MibTableColumn
cAAAServerKeyEncrType=_CAAAServerKeyEncrType_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,3),_CAAAServerKeyEncrType_Type())
cAAAServerKeyEncrType.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerKeyEncrType.setStatus(_B)
class _CAAAServerDeadTime_Type(TimeIntervalMin):defaultValue=0;subtypeSpec=TimeIntervalMin.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CAAAServerDeadTime_Type.__name__=_G
_CAAAServerDeadTime_Object=MibTableColumn
cAAAServerDeadTime=_CAAAServerDeadTime_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,4),_CAAAServerDeadTime_Type())
cAAAServerDeadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerDeadTime.setStatus(_B)
if mibBuilder.loadTexts:cAAAServerDeadTime.setUnits(_K)
class _CAAAServerTimeOut_Type(TimeIntervalSec):defaultValue=0;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_CAAAServerTimeOut_Type.__name__=_O
_CAAAServerTimeOut_Object=MibTableColumn
cAAAServerTimeOut=_CAAAServerTimeOut_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,5),_CAAAServerTimeOut_Type())
cAAAServerTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerTimeOut.setStatus(_B)
if mibBuilder.loadTexts:cAAAServerTimeOut.setUnits(_l)
class _CAAAServerRetransmits_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CAAAServerRetransmits_Type.__name__=_F
_CAAAServerRetransmits_Object=MibTableColumn
cAAAServerRetransmits=_CAAAServerRetransmits_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,6),_CAAAServerRetransmits_Type())
cAAAServerRetransmits.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerRetransmits.setStatus(_B)
if mibBuilder.loadTexts:cAAAServerRetransmits.setUnits(_m)
class _CAAAServerRootDN_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CAAAServerRootDN_Type.__name__=_E
_CAAAServerRootDN_Object=MibTableColumn
cAAAServerRootDN=_CAAAServerRootDN_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,7),_CAAAServerRootDN_Type())
cAAAServerRootDN.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerRootDN.setStatus(_B)
class _CAAAServerIdleTime_Type(TimeIntervalMin):defaultValue=0;subtypeSpec=TimeIntervalMin.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CAAAServerIdleTime_Type.__name__=_G
_CAAAServerIdleTime_Object=MibTableColumn
cAAAServerIdleTime=_CAAAServerIdleTime_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,8),_CAAAServerIdleTime_Type())
cAAAServerIdleTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerIdleTime.setStatus(_B)
if mibBuilder.loadTexts:cAAAServerIdleTime.setUnits(_K)
class _CAAAServerTestUser_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CAAAServerTestUser_Type.__name__=_E
_CAAAServerTestUser_Object=MibTableColumn
cAAAServerTestUser=_CAAAServerTestUser_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,9),_CAAAServerTestUser_Type())
cAAAServerTestUser.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerTestUser.setStatus(_B)
class _CAAAServerTestPassword_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CAAAServerTestPassword_Type.__name__=_E
_CAAAServerTestPassword_Object=MibTableColumn
cAAAServerTestPassword=_CAAAServerTestPassword_Object((1,3,6,1,4,1,9,9,367,1,2,1,1,10),_CAAAServerTestPassword_Type())
cAAAServerTestPassword.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerTestPassword.setStatus(_B)
_CAAASvrExtProtoParamConfig_ObjectIdentity=ObjectIdentity
cAAASvrExtProtoParamConfig=_CAAASvrExtProtoParamConfig_ObjectIdentity((1,3,6,1,4,1,9,9,367,1,3))
_CAAASvrExtProtocolParamTable_Object=MibTable
cAAASvrExtProtocolParamTable=_CAAASvrExtProtocolParamTable_Object((1,3,6,1,4,1,9,9,367,1,3,1))
if mibBuilder.loadTexts:cAAASvrExtProtocolParamTable.setStatus(_B)
_CAAASvrExtProtocolParamEntry_Object=MibTableRow
cAAASvrExtProtocolParamEntry=_CAAASvrExtProtocolParamEntry_Object((1,3,6,1,4,1,9,9,367,1,3,1,1))
cAAASvrExtProtocolParamEntry.setIndexNames((0,_A,_n))
if mibBuilder.loadTexts:cAAASvrExtProtocolParamEntry.setStatus(_B)
_CAAAServerProtocol_Type=CiscoAAAProtocol
_CAAAServerProtocol_Object=MibTableColumn
cAAAServerProtocol=_CAAAServerProtocol_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,1),_CAAAServerProtocol_Type())
cAAAServerProtocol.setMaxAccess(_I)
if mibBuilder.loadTexts:cAAAServerProtocol.setStatus(_B)
class _CAAAServerProtoAuthKey_Type(DisplayString):defaultValue=OctetString('')
_CAAAServerProtoAuthKey_Type.__name__=_k
_CAAAServerProtoAuthKey_Object=MibTableColumn
cAAAServerProtoAuthKey=_CAAAServerProtoAuthKey_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,2),_CAAAServerProtoAuthKey_Type())
cAAAServerProtoAuthKey.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAAServerProtoAuthKey.setStatus(_B)
class _CAAAServerProtoKeyEncrType_Type(CiscoAAAServerKeyEncrType):defaultValue=1
_CAAAServerProtoKeyEncrType_Type.__name__=_R
_CAAAServerProtoKeyEncrType_Object=MibTableColumn
cAAAServerProtoKeyEncrType=_CAAAServerProtoKeyEncrType_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,3),_CAAAServerProtoKeyEncrType_Type())
cAAAServerProtoKeyEncrType.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAAServerProtoKeyEncrType.setStatus(_B)
class _CAAAServerProtoDeadTime_Type(TimeIntervalMin):defaultValue=0;subtypeSpec=TimeIntervalMin.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CAAAServerProtoDeadTime_Type.__name__=_G
_CAAAServerProtoDeadTime_Object=MibTableColumn
cAAAServerProtoDeadTime=_CAAAServerProtoDeadTime_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,4),_CAAAServerProtoDeadTime_Type())
cAAAServerProtoDeadTime.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAAServerProtoDeadTime.setStatus(_B)
if mibBuilder.loadTexts:cAAAServerProtoDeadTime.setUnits(_K)
class _CAAAServerProtoTimeOut_Type(TimeIntervalSec):defaultValue=1;subtypeSpec=TimeIntervalSec.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_CAAAServerProtoTimeOut_Type.__name__=_O
_CAAAServerProtoTimeOut_Object=MibTableColumn
cAAAServerProtoTimeOut=_CAAAServerProtoTimeOut_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,5),_CAAAServerProtoTimeOut_Type())
cAAAServerProtoTimeOut.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAAServerProtoTimeOut.setStatus(_B)
if mibBuilder.loadTexts:cAAAServerProtoTimeOut.setUnits(_l)
class _CAAAServerProtoRetransmits_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_CAAAServerProtoRetransmits_Type.__name__=_F
_CAAAServerProtoRetransmits_Object=MibTableColumn
cAAAServerProtoRetransmits=_CAAAServerProtoRetransmits_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,6),_CAAAServerProtoRetransmits_Type())
cAAAServerProtoRetransmits.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAAServerProtoRetransmits.setStatus(_B)
if mibBuilder.loadTexts:cAAAServerProtoRetransmits.setUnits(_m)
class _CAAAServerProtoSvrTableMaxEnt_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65536))
_CAAAServerProtoSvrTableMaxEnt_Type.__name__=_F
_CAAAServerProtoSvrTableMaxEnt_Object=MibTableColumn
cAAAServerProtoSvrTableMaxEnt=_CAAAServerProtoSvrTableMaxEnt_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,7),_CAAAServerProtoSvrTableMaxEnt_Type())
cAAAServerProtoSvrTableMaxEnt.setMaxAccess(_Q)
if mibBuilder.loadTexts:cAAAServerProtoSvrTableMaxEnt.setStatus(_B)
class _CAAAServerProtoDirectedReq_Type(TruthValue):defaultValue=2
_CAAAServerProtoDirectedReq_Type.__name__=_P
_CAAAServerProtoDirectedReq_Object=MibTableColumn
cAAAServerProtoDirectedReq=_CAAAServerProtoDirectedReq_Object((1,3,6,1,4,1,9,9,367,1,3,1,1,8),_CAAAServerProtoDirectedReq_Type())
cAAAServerProtoDirectedReq.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAAServerProtoDirectedReq.setStatus(_B)
_CAAASvrExtSvrGrpConfig_ObjectIdentity=ObjectIdentity
cAAASvrExtSvrGrpConfig=_CAAASvrExtSvrGrpConfig_ObjectIdentity((1,3,6,1,4,1,9,9,367,1,4))
_CAAASvrExtSvrGrpConfigTable_Object=MibTable
cAAASvrExtSvrGrpConfigTable=_CAAASvrExtSvrGrpConfigTable_Object((1,3,6,1,4,1,9,9,367,1,4,1))
if mibBuilder.loadTexts:cAAASvrExtSvrGrpConfigTable.setStatus(_B)
_CAAASvrExtSvrGrpConfigEntry_Object=MibTableRow
cAAASvrExtSvrGrpConfigEntry=_CAAASvrExtSvrGrpConfigEntry_Object((1,3,6,1,4,1,9,9,367,1,4,1,1))
cAAASvrExtSvrGrpConfigEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:cAAASvrExtSvrGrpConfigEntry.setStatus(_B)
class _CAAASvrGrpIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CAAASvrGrpIndex_Type.__name__=_F
_CAAASvrGrpIndex_Object=MibTableColumn
cAAASvrGrpIndex=_CAAASvrGrpIndex_Object((1,3,6,1,4,1,9,9,367,1,4,1,1,1),_CAAASvrGrpIndex_Type())
cAAASvrGrpIndex.setMaxAccess(_I)
if mibBuilder.loadTexts:cAAASvrGrpIndex.setStatus(_B)
class _CAAASvrGrpName_Type(SnmpAdminString):subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_CAAASvrGrpName_Type.__name__=_E
_CAAASvrGrpName_Object=MibTableColumn
cAAASvrGrpName=_CAAASvrGrpName_Object((1,3,6,1,4,1,9,9,367,1,4,1,1,2),_CAAASvrGrpName_Type())
cAAASvrGrpName.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAASvrGrpName.setStatus(_B)
class _CAAASvrGrpProtocol_Type(CiscoAAAProtocol):defaultValue=1
_CAAASvrGrpProtocol_Type.__name__=_i
_CAAASvrGrpProtocol_Object=MibTableColumn
cAAASvrGrpProtocol=_CAAASvrGrpProtocol_Object((1,3,6,1,4,1,9,9,367,1,4,1,1,3),_CAAASvrGrpProtocol_Type())
cAAASvrGrpProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAASvrGrpProtocol.setStatus(_B)
class _CAAAServerList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,256))
_CAAAServerList_Type.__name__=_N
_CAAAServerList_Object=MibTableColumn
cAAAServerList=_CAAAServerList_Object((1,3,6,1,4,1,9,9,367,1,4,1,1,4),_CAAAServerList_Type())
cAAAServerList.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAAServerList.setStatus(_B)
_CAAASvrGrpConfigRowStatus_Type=RowStatus
_CAAASvrGrpConfigRowStatus_Object=MibTableColumn
cAAASvrGrpConfigRowStatus=_CAAASvrGrpConfigRowStatus_Object((1,3,6,1,4,1,9,9,367,1,4,1,1,5),_CAAASvrGrpConfigRowStatus_Type())
cAAASvrGrpConfigRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAASvrGrpConfigRowStatus.setStatus(_B)
class _CAAASvrGrpConfigDeadTime_Type(TimeIntervalMin):defaultValue=0;subtypeSpec=TimeIntervalMin.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1440))
_CAAASvrGrpConfigDeadTime_Type.__name__=_G
_CAAASvrGrpConfigDeadTime_Object=MibTableColumn
cAAASvrGrpConfigDeadTime=_CAAASvrGrpConfigDeadTime_Object((1,3,6,1,4,1,9,9,367,1,4,1,1,6),_CAAASvrGrpConfigDeadTime_Type())
cAAASvrGrpConfigDeadTime.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAASvrGrpConfigDeadTime.setStatus(_B)
if mibBuilder.loadTexts:cAAASvrGrpConfigDeadTime.setUnits(_K)
_CAAASvrExtSvrGrpLDAPConfigTable_Object=MibTable
cAAASvrExtSvrGrpLDAPConfigTable=_CAAASvrExtSvrGrpLDAPConfigTable_Object((1,3,6,1,4,1,9,9,367,1,4,2))
if mibBuilder.loadTexts:cAAASvrExtSvrGrpLDAPConfigTable.setStatus(_B)
_CAAASvrExtSvrGrpLDAPConfigEntry_Object=MibTableRow
cAAASvrExtSvrGrpLDAPConfigEntry=_CAAASvrExtSvrGrpLDAPConfigEntry_Object((1,3,6,1,4,1,9,9,367,1,4,2,1))
cAAASvrExtSvrGrpLDAPConfigEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:cAAASvrExtSvrGrpLDAPConfigEntry.setStatus(_B)
class _CAAASvrGrpLDAPBaseDN_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CAAASvrGrpLDAPBaseDN_Type.__name__=_E
_CAAASvrGrpLDAPBaseDN_Object=MibTableColumn
cAAASvrGrpLDAPBaseDN=_CAAASvrGrpLDAPBaseDN_Object((1,3,6,1,4,1,9,9,367,1,4,2,1,1),_CAAASvrGrpLDAPBaseDN_Type())
cAAASvrGrpLDAPBaseDN.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAASvrGrpLDAPBaseDN.setStatus(_B)
class _CAAASvrGrpLDAPFilterUser_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_CAAASvrGrpLDAPFilterUser_Type.__name__=_E
_CAAASvrGrpLDAPFilterUser_Object=MibTableColumn
cAAASvrGrpLDAPFilterUser=_CAAASvrGrpLDAPFilterUser_Object((1,3,6,1,4,1,9,9,367,1,4,2,1,2),_CAAASvrGrpLDAPFilterUser_Type())
cAAASvrGrpLDAPFilterUser.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAASvrGrpLDAPFilterUser.setStatus(_B)
class _CAAASvrGrpLDAPUserProfile_Type(SnmpAdminString):defaultValue=OctetString('');subtypeSpec=SnmpAdminString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_CAAASvrGrpLDAPUserProfile_Type.__name__=_E
_CAAASvrGrpLDAPUserProfile_Object=MibTableColumn
cAAASvrGrpLDAPUserProfile=_CAAASvrGrpLDAPUserProfile_Object((1,3,6,1,4,1,9,9,367,1,4,2,1,3),_CAAASvrGrpLDAPUserProfile_Type())
cAAASvrGrpLDAPUserProfile.setMaxAccess(_C)
if mibBuilder.loadTexts:cAAASvrGrpLDAPUserProfile.setStatus(_B)
_CAAASvrExtAppSvrGrpMapConfig_ObjectIdentity=ObjectIdentity
cAAASvrExtAppSvrGrpMapConfig=_CAAASvrExtAppSvrGrpMapConfig_ObjectIdentity((1,3,6,1,4,1,9,9,367,1,5))
_CAAASvrExtAppSvrGrpConfigTable_Object=MibTable
cAAASvrExtAppSvrGrpConfigTable=_CAAASvrExtAppSvrGrpConfigTable_Object((1,3,6,1,4,1,9,9,367,1,5,1))
if mibBuilder.loadTexts:cAAASvrExtAppSvrGrpConfigTable.setStatus(_B)
_CAAASvrExtAppSvrGrpConfigEntry_Object=MibTableRow
cAAASvrExtAppSvrGrpConfigEntry=_CAAASvrExtAppSvrGrpConfigEntry_Object((1,3,6,1,4,1,9,9,367,1,5,1,1))
cAAASvrExtAppSvrGrpConfigEntry.setIndexNames((0,_A,_o),(0,_A,_p),(0,_A,_q))
if mibBuilder.loadTexts:cAAASvrExtAppSvrGrpConfigEntry.setStatus(_B)
class _CAAAApplicationType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('default',1),('login',2),('dhchap',3),('iSCSI',4)))
_CAAAApplicationType_Type.__name__=_H
_CAAAApplicationType_Object=MibTableColumn
cAAAApplicationType=_CAAAApplicationType_Object((1,3,6,1,4,1,9,9,367,1,5,1,1,1),_CAAAApplicationType_Type())
cAAAApplicationType.setMaxAccess(_I)
if mibBuilder.loadTexts:cAAAApplicationType.setStatus(_B)
class _CAAAApplicationSubType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('all',1),('console',2)))
_CAAAApplicationSubType_Type.__name__=_H
_CAAAApplicationSubType_Object=MibTableColumn
cAAAApplicationSubType=_CAAAApplicationSubType_Object((1,3,6,1,4,1,9,9,367,1,5,1,1,2),_CAAAApplicationSubType_Type())
cAAAApplicationSubType.setMaxAccess(_I)
if mibBuilder.loadTexts:cAAAApplicationSubType.setStatus(_B)
class _CAAAFunction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('authentication',1),('authorization',2),('accounting',3)))
_CAAAFunction_Type.__name__=_H
_CAAAFunction_Object=MibTableColumn
cAAAFunction=_CAAAFunction_Object((1,3,6,1,4,1,9,9,367,1,5,1,1,3),_CAAAFunction_Type())
cAAAFunction.setMaxAccess(_I)
if mibBuilder.loadTexts:cAAAFunction.setStatus(_B)
_CAAASvrGrpLocal_Type=TruthValue
_CAAASvrGrpLocal_Object=MibTableColumn
cAAASvrGrpLocal=_CAAASvrGrpLocal_Object((1,3,6,1,4,1,9,9,367,1,5,1,1,4),_CAAASvrGrpLocal_Type())
cAAASvrGrpLocal.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAASvrGrpLocal.setStatus(_B)
_CAAASvrGrpTrivial_Type=TruthValue
_CAAASvrGrpTrivial_Object=MibTableColumn
cAAASvrGrpTrivial=_CAAASvrGrpTrivial_Object((1,3,6,1,4,1,9,9,367,1,5,1,1,5),_CAAASvrGrpTrivial_Type())
cAAASvrGrpTrivial.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAASvrGrpTrivial.setStatus(_B)
class _CAAASvrGrpList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,256))
_CAAASvrGrpList_Type.__name__=_N
_CAAASvrGrpList_Object=MibTableColumn
cAAASvrGrpList=_CAAASvrGrpList_Object((1,3,6,1,4,1,9,9,367,1,5,1,1,6),_CAAASvrGrpList_Type())
cAAASvrGrpList.setMaxAccess(_D)
if mibBuilder.loadTexts:cAAASvrGrpList.setStatus(_B)
_CiscoAAASvrExtMIBConformance_ObjectIdentity=ObjectIdentity
ciscoAAASvrExtMIBConformance=_CiscoAAASvrExtMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,367,2))
_CiscoAAASvrExtMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoAAASvrExtMIBCompliances=_CiscoAAASvrExtMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,367,2,1))
_CiscoAAASvrExtMIBGroups_ObjectIdentity=ObjectIdentity
ciscoAAASvrExtMIBGroups=_CiscoAAASvrExtMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,367,2,2))
casConfigEntry.registerAugmentions((_A,_r))
cAAASvrExtConfigEntry.setIndexNames(*casConfigEntry.getIndexNames())
cAAASvrExtGenericConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,1))
cAAASvrExtGenericConfGroup.setObjects((_A,_T))
if mibBuilder.loadTexts:cAAASvrExtGenericConfGroup.setStatus(_J)
cAAASvrExtSvrTableConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,2))
cAAASvrExtSvrTableConfGroup.setObjects(*((_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x)))
if mibBuilder.loadTexts:cAAASvrExtSvrTableConfGroup.setStatus(_B)
cAAASvrExtProtoParamConfigGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,3))
cAAASvrExtProtoParamConfigGroup.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z)))
if mibBuilder.loadTexts:cAAASvrExtProtoParamConfigGroup.setStatus(_J)
cAAASvrExtSvrGroupConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,4))
cAAASvrExtSvrGroupConfGroup.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e)))
if mibBuilder.loadTexts:cAAASvrExtSvrGroupConfGroup.setStatus(_J)
cAAASvrExtAppSvrGroupConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,5))
cAAASvrExtAppSvrGroupConfGroup.setObjects(*((_A,_y),(_A,_z),(_A,_A0),(_A,_A1)))
if mibBuilder.loadTexts:cAAASvrExtAppSvrGroupConfGroup.setStatus(_B)
cAAASvrExtGenericConfGroup1=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,6))
cAAASvrExtGenericConfGroup1.setObjects(*((_A,_T),(_A,_A2)))
if mibBuilder.loadTexts:cAAASvrExtGenericConfGroup1.setStatus(_B)
cAAASvrExtGenericConfGroup2=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,7))
cAAASvrExtGenericConfGroup2.setObjects((_A,_A3))
if mibBuilder.loadTexts:cAAASvrExtGenericConfGroup2.setStatus(_B)
cAAASvrExtSvrGroupConfGroup2=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,8))
cAAASvrExtSvrGroupConfGroup2.setObjects(*((_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_A4)))
if mibBuilder.loadTexts:cAAASvrExtSvrGroupConfGroup2.setStatus(_B)
cAAASvrExtProtoParamConfigGroup1=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,9))
cAAASvrExtProtoParamConfigGroup1.setObjects(*((_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_A5)))
if mibBuilder.loadTexts:cAAASvrExtProtoParamConfigGroup1.setStatus(_B)
cAAASvrExtSvrTableLDAPConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,10))
cAAASvrExtSvrTableLDAPConfGroup.setObjects((_A,_A6))
if mibBuilder.loadTexts:cAAASvrExtSvrTableLDAPConfGroup.setStatus(_B)
cAAASvrExtSvrGroupLDAPConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,11))
cAAASvrExtSvrGroupLDAPConfGroup.setObjects(*((_A,_A7),(_A,_A8),(_A,_A9)))
if mibBuilder.loadTexts:cAAASvrExtSvrGroupLDAPConfGroup.setStatus(_B)
cAAASvrExtSvrMonitorConfGroup=ObjectGroup((1,3,6,1,4,1,9,9,367,2,2,12))
cAAASvrExtSvrMonitorConfGroup.setObjects(*((_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:cAAASvrExtSvrMonitorConfGroup.setStatus(_B)
ciscoAAAServerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,367,2,1,1))
ciscoAAAServerMIBCompliance.setObjects(*((_A,_AD),(_A,_L),(_A,_f),(_A,_g),(_A,_M)))
if mibBuilder.loadTexts:ciscoAAAServerMIBCompliance.setStatus(_J)
ciscoAAAServerMIBCompliance1=ModuleCompliance((1,3,6,1,4,1,9,9,367,2,1,2))
ciscoAAAServerMIBCompliance1.setObjects(*((_A,_h),(_A,_L),(_A,_f),(_A,_g),(_A,_M)))
if mibBuilder.loadTexts:ciscoAAAServerMIBCompliance1.setStatus(_J)
ciscoAAAServerMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,9,9,367,2,1,3))
ciscoAAAServerMIBCompliance2.setObjects(*((_A,_h),(_A,_L),(_A,_AE),(_A,_AF),(_A,_M),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ)))
if mibBuilder.loadTexts:ciscoAAAServerMIBCompliance2.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_R:CiscoAAAServerKeyEncrType,'ciscoAAAServerExtMIB':ciscoAAAServerExtMIB,'ciscoAAASvrExtMIBObjects':ciscoAAASvrExtMIBObjects,'cAAASvrExtGenericConfig':cAAASvrExtGenericConfig,_T:cAAASvrExtLocalAccLogMaxSize,_e:cAAASvrExtSvrGrpSvrListMaxEnt,_A1:cAAASvrExtAppToSvrGrpMaxEnt,_A2:cAAASvrExtClearAccLog,_A3:cAAALoginAuthTypeMSCHAP,'cAAASvrExtSvrTableConfig':cAAASvrExtSvrTableConfig,'cAAASvrExtConfigTable':cAAASvrExtConfigTable,_r:cAAASvrExtConfigEntry,_s:cAAAServerAddrType,_t:cAAAServerAddr,_u:cAAAServerKeyEncrType,_v:cAAAServerDeadTime,_w:cAAAServerTimeOut,_x:cAAAServerRetransmits,_A6:cAAAServerRootDN,_AA:cAAAServerIdleTime,_AB:cAAAServerTestUser,_AC:cAAAServerTestPassword,'cAAASvrExtProtoParamConfig':cAAASvrExtProtoParamConfig,'cAAASvrExtProtocolParamTable':cAAASvrExtProtocolParamTable,'cAAASvrExtProtocolParamEntry':cAAASvrExtProtocolParamEntry,_n:cAAAServerProtocol,_U:cAAAServerProtoAuthKey,_V:cAAAServerProtoKeyEncrType,_W:cAAAServerProtoDeadTime,_X:cAAAServerProtoTimeOut,_Y:cAAAServerProtoRetransmits,_Z:cAAAServerProtoSvrTableMaxEnt,_A5:cAAAServerProtoDirectedReq,'cAAASvrExtSvrGrpConfig':cAAASvrExtSvrGrpConfig,'cAAASvrExtSvrGrpConfigTable':cAAASvrExtSvrGrpConfigTable,'cAAASvrExtSvrGrpConfigEntry':cAAASvrExtSvrGrpConfigEntry,_S:cAAASvrGrpIndex,_a:cAAASvrGrpName,_b:cAAASvrGrpProtocol,_c:cAAAServerList,_d:cAAASvrGrpConfigRowStatus,_A4:cAAASvrGrpConfigDeadTime,'cAAASvrExtSvrGrpLDAPConfigTable':cAAASvrExtSvrGrpLDAPConfigTable,'cAAASvrExtSvrGrpLDAPConfigEntry':cAAASvrExtSvrGrpLDAPConfigEntry,_A7:cAAASvrGrpLDAPBaseDN,_A8:cAAASvrGrpLDAPFilterUser,_A9:cAAASvrGrpLDAPUserProfile,'cAAASvrExtAppSvrGrpMapConfig':cAAASvrExtAppSvrGrpMapConfig,'cAAASvrExtAppSvrGrpConfigTable':cAAASvrExtAppSvrGrpConfigTable,'cAAASvrExtAppSvrGrpConfigEntry':cAAASvrExtAppSvrGrpConfigEntry,_o:cAAAApplicationType,_p:cAAAApplicationSubType,_q:cAAAFunction,_y:cAAASvrGrpLocal,_z:cAAASvrGrpTrivial,_A0:cAAASvrGrpList,'ciscoAAASvrExtMIBConformance':ciscoAAASvrExtMIBConformance,'ciscoAAASvrExtMIBCompliances':ciscoAAASvrExtMIBCompliances,'ciscoAAAServerMIBCompliance':ciscoAAAServerMIBCompliance,'ciscoAAAServerMIBCompliance1':ciscoAAAServerMIBCompliance1,'ciscoAAAServerMIBCompliance2':ciscoAAAServerMIBCompliance2,'ciscoAAASvrExtMIBGroups':ciscoAAASvrExtMIBGroups,_AD:cAAASvrExtGenericConfGroup,_L:cAAASvrExtSvrTableConfGroup,_f:cAAASvrExtProtoParamConfigGroup,_g:cAAASvrExtSvrGroupConfGroup,_M:cAAASvrExtAppSvrGroupConfGroup,_h:cAAASvrExtGenericConfGroup1,_AJ:cAAASvrExtGenericConfGroup2,_AF:cAAASvrExtSvrGroupConfGroup2,_AE:cAAASvrExtProtoParamConfigGroup1,_AG:cAAASvrExtSvrTableLDAPConfGroup,_AH:cAAASvrExtSvrGroupLDAPConfGroup,_AI:cAAASvrExtSvrMonitorConfGroup})