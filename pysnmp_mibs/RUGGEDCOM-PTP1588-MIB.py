_AD='rcPTP1588BClkPriority'
_AC='rcPTP1588BClkVlanId'
_AB='rcPTP1588BClkGMIdentity'
_AA='rcPTP1588BClkBackUpIP'
_A9='rcPTP1588BClkMasterIP'
_A8='rcPTP1588BClkAutoReg'
_A7='rcPTP1588BClkAnnounceRcTout'
_A6='rcPTP1588BClkAnnounceInt'
_A5='rcPTP1588BClkSyncInt'
_A4='rcPTP1588BClkPTPPortType'
_A3='rcPTP1588BClkPathDelayMech'
_A2='rcPTP1588BClkDomainNumber'
_A1='rcPTP1588BClkProfileId'
_A0='rcPTP1588BClkGroupName'
_z='rcPTP1588ClkAccuracy'
_y='rcPTP1588ClkPriority'
_x='rcPTP1588ClkVlanId'
_w='rcPTP1588ClkNetProtocol'
_v='rcPTP1588ClkDomainNumber'
_u='rcPTP1588ClkProfileId'
_t='rcPTP1588ClkDelayMech'
_s='rcPTP1588ClkSyncInt'
_r='rcPTP1588ClkAnnounceRcTout'
_q='rcPTP1588ClkAnnounceInt'
_p='rcPTP1588Global1Step'
_o='rcPTP1588GlobalE2ERequestInterval'
_n='rcPTP1588GlobalP2PRequestInterval'
_m='rcPTP1588GlobalEnable'
_l='rcPTP1588E2EDelay'
_k='rcPTP1588SlaveFeqAdj'
_j='rcPTP1588ServoStatus'
_i='rcPTP1588SlaveBackUpIP'
_h='rcPTP1588SlaveMasteIP'
_g='rcPTP1588SlaveAutoReg'
_f='rcPTP1588SlaveDomain'
_e='rcPTP1588SlaveEthPort'
_d='rcPTP1588NetClass'
_c='rcPTP1588StartUpWait'
_b='rcPTP1588EthPorts'
_a='rcPTP1588ClkType'
_Z='powerProfileV2'
_Y='customProfile'
_X='defaultE2EProfile'
_W='utilityProfile'
_V='telecom'
_U='ieee8021as'
_T='powerProfile'
_S='defaultP2PProfile'
_R='disabled'
_Q='value500millSec'
_P='value250millSec'
_O='value125millSec'
_N='rcPTP1588BClkPorts'
_M='read-only'
_L='TruthValue'
_K='value32Sec'
_J='value16Sec'
_I='value8Sec'
_H='value4Sec'
_G='Unsigned32'
_F='value2Sec'
_E='value1Sec'
_D='Integer32'
_C='read-write'
_B='RUGGEDCOM-PTP1588-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ruggedcomMgmt,=mibBuilder.importSymbols('RUGGEDCOM-MIB','ruggedcomMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_L)
rcPTP1588=ModuleIdentity((1,3,6,1,4,1,15004,4,12))
if mibBuilder.loadTexts:rcPTP1588.setRevisions(('2015-09-23 13:00','2022-06-17 13:00','2022-07-20 12:15','2022-07-25 10:00','2023-05-01 17:00','2023-07-07 16:00'))
_RcPTP1588Base_ObjectIdentity=ObjectIdentity
rcPTP1588Base=_RcPTP1588Base_ObjectIdentity((1,3,6,1,4,1,15004,4,12,1))
class _RcPTP1588ClkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('ordinaryClock',2),('p2ptc',3),('boundaryClock',4),('e2etc',5),('ocp2ptc',6),('oce2etc',7),('transparentClock',8),('ocAndTc',9)))
_RcPTP1588ClkType_Type.__name__=_D
_RcPTP1588ClkType_Object=MibScalar
rcPTP1588ClkType=_RcPTP1588ClkType_Object((1,3,6,1,4,1,15004,4,12,1,1),_RcPTP1588ClkType_Type())
rcPTP1588ClkType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkType.setStatus(_A)
_RcPTP1588EthPorts_Type=PortList
_RcPTP1588EthPorts_Object=MibScalar
rcPTP1588EthPorts=_RcPTP1588EthPorts_Object((1,3,6,1,4,1,15004,4,12,1,2),_RcPTP1588EthPorts_Type())
rcPTP1588EthPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588EthPorts.setStatus(_A)
class _RcPTP1588StartUpWait_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3600))
_RcPTP1588StartUpWait_Type.__name__=_D
_RcPTP1588StartUpWait_Object=MibScalar
rcPTP1588StartUpWait=_RcPTP1588StartUpWait_Object((1,3,6,1,4,1,15004,4,12,1,3),_RcPTP1588StartUpWait_Type())
rcPTP1588StartUpWait.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588StartUpWait.setStatus(_A)
class _RcPTP1588NetClass_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('netclass1588',1),('nonnetclass1588',2)))
_RcPTP1588NetClass_Type.__name__=_D
_RcPTP1588NetClass_Object=MibScalar
rcPTP1588NetClass=_RcPTP1588NetClass_Object((1,3,6,1,4,1,15004,4,12,1,4),_RcPTP1588NetClass_Type())
rcPTP1588NetClass.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588NetClass.setStatus(_A)
_RcPTP1588SlaveEthPort_Type=PortList
_RcPTP1588SlaveEthPort_Object=MibScalar
rcPTP1588SlaveEthPort=_RcPTP1588SlaveEthPort_Object((1,3,6,1,4,1,15004,4,12,1,5),_RcPTP1588SlaveEthPort_Type())
rcPTP1588SlaveEthPort.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588SlaveEthPort.setStatus(_A)
class _RcPTP1588SlaveDomain_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,127))
_RcPTP1588SlaveDomain_Type.__name__=_D
_RcPTP1588SlaveDomain_Object=MibScalar
rcPTP1588SlaveDomain=_RcPTP1588SlaveDomain_Object((1,3,6,1,4,1,15004,4,12,1,6),_RcPTP1588SlaveDomain_Type())
rcPTP1588SlaveDomain.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588SlaveDomain.setStatus(_A)
_RcPTP1588SlaveAutoReg_Type=TruthValue
_RcPTP1588SlaveAutoReg_Object=MibScalar
rcPTP1588SlaveAutoReg=_RcPTP1588SlaveAutoReg_Object((1,3,6,1,4,1,15004,4,12,1,7),_RcPTP1588SlaveAutoReg_Type())
rcPTP1588SlaveAutoReg.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588SlaveAutoReg.setStatus(_A)
_RcPTP1588SlaveMasteIP_Type=IpAddress
_RcPTP1588SlaveMasteIP_Object=MibScalar
rcPTP1588SlaveMasteIP=_RcPTP1588SlaveMasteIP_Object((1,3,6,1,4,1,15004,4,12,1,8),_RcPTP1588SlaveMasteIP_Type())
rcPTP1588SlaveMasteIP.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588SlaveMasteIP.setStatus(_A)
_RcPTP1588SlaveBackUpIP_Type=IpAddress
_RcPTP1588SlaveBackUpIP_Object=MibScalar
rcPTP1588SlaveBackUpIP=_RcPTP1588SlaveBackUpIP_Object((1,3,6,1,4,1,15004,4,12,1,9),_RcPTP1588SlaveBackUpIP_Type())
rcPTP1588SlaveBackUpIP.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588SlaveBackUpIP.setStatus(_A)
_RcPTP1588ServoStatus_Type=DisplayString
_RcPTP1588ServoStatus_Object=MibScalar
rcPTP1588ServoStatus=_RcPTP1588ServoStatus_Object((1,3,6,1,4,1,15004,4,12,1,10),_RcPTP1588ServoStatus_Type())
rcPTP1588ServoStatus.setMaxAccess(_M)
if mibBuilder.loadTexts:rcPTP1588ServoStatus.setStatus(_A)
_RcPTP1588SlaveFeqAdj_Type=Integer32
_RcPTP1588SlaveFeqAdj_Object=MibScalar
rcPTP1588SlaveFeqAdj=_RcPTP1588SlaveFeqAdj_Object((1,3,6,1,4,1,15004,4,12,1,11),_RcPTP1588SlaveFeqAdj_Type())
rcPTP1588SlaveFeqAdj.setMaxAccess(_M)
if mibBuilder.loadTexts:rcPTP1588SlaveFeqAdj.setStatus(_A)
_RcPTP1588E2EDelay_Type=Integer32
_RcPTP1588E2EDelay_Object=MibScalar
rcPTP1588E2EDelay=_RcPTP1588E2EDelay_Object((1,3,6,1,4,1,15004,4,12,1,12),_RcPTP1588E2EDelay_Type())
rcPTP1588E2EDelay.setMaxAccess(_M)
if mibBuilder.loadTexts:rcPTP1588E2EDelay.setStatus(_A)
class _RcPTP1588GlobalEnable_Type(TruthValue):defaultValue=2
_RcPTP1588GlobalEnable_Type.__name__=_L
_RcPTP1588GlobalEnable_Object=MibScalar
rcPTP1588GlobalEnable=_RcPTP1588GlobalEnable_Object((1,3,6,1,4,1,15004,4,12,1,13),_RcPTP1588GlobalEnable_Type())
rcPTP1588GlobalEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588GlobalEnable.setStatus(_A)
class _RcPTP1588GlobalP2PRequestInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_RcPTP1588GlobalP2PRequestInterval_Type.__name__=_D
_RcPTP1588GlobalP2PRequestInterval_Object=MibScalar
rcPTP1588GlobalP2PRequestInterval=_RcPTP1588GlobalP2PRequestInterval_Object((1,3,6,1,4,1,15004,4,12,1,14),_RcPTP1588GlobalP2PRequestInterval_Type())
rcPTP1588GlobalP2PRequestInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588GlobalP2PRequestInterval.setStatus(_A)
class _RcPTP1588GlobalE2ERequestInterval_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_RcPTP1588GlobalE2ERequestInterval_Type.__name__=_D
_RcPTP1588GlobalE2ERequestInterval_Object=MibScalar
rcPTP1588GlobalE2ERequestInterval=_RcPTP1588GlobalE2ERequestInterval_Object((1,3,6,1,4,1,15004,4,12,1,15),_RcPTP1588GlobalE2ERequestInterval_Type())
rcPTP1588GlobalE2ERequestInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588GlobalE2ERequestInterval.setStatus(_A)
class _RcPTP1588Global1Step_Type(TruthValue):defaultValue=2
_RcPTP1588Global1Step_Type.__name__=_L
_RcPTP1588Global1Step_Object=MibScalar
rcPTP1588Global1Step=_RcPTP1588Global1Step_Object((1,3,6,1,4,1,15004,4,12,1,16),_RcPTP1588Global1Step_Type())
rcPTP1588Global1Step.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588Global1Step.setStatus(_A)
class _RcPTP1588ClkAnnounceInt_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_RcPTP1588ClkAnnounceInt_Type.__name__=_D
_RcPTP1588ClkAnnounceInt_Object=MibScalar
rcPTP1588ClkAnnounceInt=_RcPTP1588ClkAnnounceInt_Object((1,3,6,1,4,1,15004,4,12,1,17),_RcPTP1588ClkAnnounceInt_Type())
rcPTP1588ClkAnnounceInt.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkAnnounceInt.setStatus(_A)
class _RcPTP1588ClkAnnounceRcTout_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_RcPTP1588ClkAnnounceRcTout_Type.__name__=_D
_RcPTP1588ClkAnnounceRcTout_Object=MibScalar
rcPTP1588ClkAnnounceRcTout=_RcPTP1588ClkAnnounceRcTout_Object((1,3,6,1,4,1,15004,4,12,1,18),_RcPTP1588ClkAnnounceRcTout_Type())
rcPTP1588ClkAnnounceRcTout.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkAnnounceRcTout.setStatus(_A)
class _RcPTP1588ClkSyncInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_E,4),(_F,5)))
_RcPTP1588ClkSyncInt_Type.__name__=_D
_RcPTP1588ClkSyncInt_Object=MibScalar
rcPTP1588ClkSyncInt=_RcPTP1588ClkSyncInt_Object((1,3,6,1,4,1,15004,4,12,1,19),_RcPTP1588ClkSyncInt_Type())
rcPTP1588ClkSyncInt.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkSyncInt.setStatus(_A)
class _RcPTP1588ClkDelayMech_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,254)));namedValues=NamedValues(*(('e2e',1),('p2p',2),(_R,254)))
_RcPTP1588ClkDelayMech_Type.__name__=_D
_RcPTP1588ClkDelayMech_Object=MibScalar
rcPTP1588ClkDelayMech=_RcPTP1588ClkDelayMech_Object((1,3,6,1,4,1,15004,4,12,1,20),_RcPTP1588ClkDelayMech_Type())
rcPTP1588ClkDelayMech.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkDelayMech.setStatus(_A)
class _RcPTP1588ClkProfileId_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),('lxi',3),(_V,4),(_W,5),(_X,6),(_Y,7),(_Z,8)))
_RcPTP1588ClkProfileId_Type.__name__=_D
_RcPTP1588ClkProfileId_Object=MibScalar
rcPTP1588ClkProfileId=_RcPTP1588ClkProfileId_Object((1,3,6,1,4,1,15004,4,12,1,21),_RcPTP1588ClkProfileId_Type())
rcPTP1588ClkProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkProfileId.setStatus(_A)
class _RcPTP1588ClkDomainNumber_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_RcPTP1588ClkDomainNumber_Type.__name__=_G
_RcPTP1588ClkDomainNumber_Object=MibScalar
rcPTP1588ClkDomainNumber=_RcPTP1588ClkDomainNumber_Object((1,3,6,1,4,1,15004,4,12,1,22),_RcPTP1588ClkDomainNumber_Type())
rcPTP1588ClkDomainNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkDomainNumber.setStatus(_A)
class _RcPTP1588ClkNetProtocol_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ieee8023',1),('udpIpv4',2)))
_RcPTP1588ClkNetProtocol_Type.__name__=_D
_RcPTP1588ClkNetProtocol_Object=MibScalar
rcPTP1588ClkNetProtocol=_RcPTP1588ClkNetProtocol_Object((1,3,6,1,4,1,15004,4,12,1,23),_RcPTP1588ClkNetProtocol_Type())
rcPTP1588ClkNetProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkNetProtocol.setStatus(_A)
class _RcPTP1588ClkVlanId_Type(Integer32):defaultValue=-2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,4094))
_RcPTP1588ClkVlanId_Type.__name__=_D
_RcPTP1588ClkVlanId_Object=MibScalar
rcPTP1588ClkVlanId=_RcPTP1588ClkVlanId_Object((1,3,6,1,4,1,15004,4,12,1,24),_RcPTP1588ClkVlanId_Type())
rcPTP1588ClkVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkVlanId.setStatus(_A)
class _RcPTP1588ClkPriority_Type(Unsigned32):defaultValue=4;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcPTP1588ClkPriority_Type.__name__=_G
_RcPTP1588ClkPriority_Object=MibScalar
rcPTP1588ClkPriority=_RcPTP1588ClkPriority_Object((1,3,6,1,4,1,15004,4,12,1,25),_RcPTP1588ClkPriority_Type())
rcPTP1588ClkPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkPriority.setStatus(_A)
class _RcPTP1588ClkAccuracy_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14)));namedValues=NamedValues(*(('timeAccurateTo50ns',0),('timeAccurateTo100ns',1),('timeAccurateTo250ns',2),('timeAccurateTo1us',3),('timeAccurateTo2to5us',4),('timeAccurateTo10us',5),('timeAccurateTo25us',6),('timeAccurateTo100us',7),('timeAccurateTo250us',8),('timeAccurateTo1ms',9),('timeAccurateTo2to5ms',10),('timeAccurateTo10ms',11),('timeAccurateTo25ms',12),('timeAccurateTo100ms',13),('timeAccurateTo250ms',14)))
_RcPTP1588ClkAccuracy_Type.__name__=_D
_RcPTP1588ClkAccuracy_Object=MibScalar
rcPTP1588ClkAccuracy=_RcPTP1588ClkAccuracy_Object((1,3,6,1,4,1,15004,4,12,1,26),_RcPTP1588ClkAccuracy_Type())
rcPTP1588ClkAccuracy.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588ClkAccuracy.setStatus(_A)
_RcPTP1588Conformance_ObjectIdentity=ObjectIdentity
rcPTP1588Conformance=_RcPTP1588Conformance_ObjectIdentity((1,3,6,1,4,1,15004,4,12,3))
_RcPTP1588Groups_ObjectIdentity=ObjectIdentity
rcPTP1588Groups=_RcPTP1588Groups_ObjectIdentity((1,3,6,1,4,1,15004,4,12,3,2))
_RcPTP1588BCTables_ObjectIdentity=ObjectIdentity
rcPTP1588BCTables=_RcPTP1588BCTables_ObjectIdentity((1,3,6,1,4,1,15004,4,12,4))
_RcPTP1588BClkTable_Object=MibTable
rcPTP1588BClkTable=_RcPTP1588BClkTable_Object((1,3,6,1,4,1,15004,4,12,4,1))
if mibBuilder.loadTexts:rcPTP1588BClkTable.setStatus(_A)
_RcPTP1588BClkEntry_Object=MibTableRow
rcPTP1588BClkEntry=_RcPTP1588BClkEntry_Object((1,3,6,1,4,1,15004,4,12,4,1,1))
rcPTP1588BClkEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:rcPTP1588BClkEntry.setStatus(_A)
_RcPTP1588BClkPorts_Type=PortList
_RcPTP1588BClkPorts_Object=MibTableColumn
rcPTP1588BClkPorts=_RcPTP1588BClkPorts_Object((1,3,6,1,4,1,15004,4,12,4,1,1,1),_RcPTP1588BClkPorts_Type())
rcPTP1588BClkPorts.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkPorts.setStatus(_A)
_RcPTP1588BClkGroupName_Type=DisplayString
_RcPTP1588BClkGroupName_Object=MibTableColumn
rcPTP1588BClkGroupName=_RcPTP1588BClkGroupName_Object((1,3,6,1,4,1,15004,4,12,4,1,1,2),_RcPTP1588BClkGroupName_Type())
rcPTP1588BClkGroupName.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkGroupName.setStatus(_A)
class _RcPTP1588BClkProfileId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_S,0),(_T,1),(_U,2),('lxi',3),(_V,4),(_W,5),(_X,6),(_Y,7),(_Z,8)))
_RcPTP1588BClkProfileId_Type.__name__=_D
_RcPTP1588BClkProfileId_Object=MibTableColumn
rcPTP1588BClkProfileId=_RcPTP1588BClkProfileId_Object((1,3,6,1,4,1,15004,4,12,4,1,1,3),_RcPTP1588BClkProfileId_Type())
rcPTP1588BClkProfileId.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkProfileId.setStatus(_A)
class _RcPTP1588BClkDomainNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,254))
_RcPTP1588BClkDomainNumber_Type.__name__=_G
_RcPTP1588BClkDomainNumber_Object=MibTableColumn
rcPTP1588BClkDomainNumber=_RcPTP1588BClkDomainNumber_Object((1,3,6,1,4,1,15004,4,12,4,1,1,4),_RcPTP1588BClkDomainNumber_Type())
rcPTP1588BClkDomainNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkDomainNumber.setStatus(_A)
class _RcPTP1588BClkTransportProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('layer2multicast',1),('layer3multicast',2),('layer3unicast',3)))
_RcPTP1588BClkTransportProtocol_Type.__name__=_D
_RcPTP1588BClkTransportProtocol_Object=MibTableColumn
rcPTP1588BClkTransportProtocol=_RcPTP1588BClkTransportProtocol_Object((1,3,6,1,4,1,15004,4,12,4,1,1,5),_RcPTP1588BClkTransportProtocol_Type())
rcPTP1588BClkTransportProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkTransportProtocol.setStatus(_A)
class _RcPTP1588BClkPathDelayMech_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('end2end',1),('peer2peer',2),(_R,3)))
_RcPTP1588BClkPathDelayMech_Type.__name__=_D
_RcPTP1588BClkPathDelayMech_Object=MibTableColumn
rcPTP1588BClkPathDelayMech=_RcPTP1588BClkPathDelayMech_Object((1,3,6,1,4,1,15004,4,12,4,1,1,6),_RcPTP1588BClkPathDelayMech_Type())
rcPTP1588BClkPathDelayMech.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkPathDelayMech.setStatus(_A)
class _RcPTP1588BClkPTPPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('slaveonly',2),('masteronly',3)))
_RcPTP1588BClkPTPPortType_Type.__name__=_D
_RcPTP1588BClkPTPPortType_Object=MibTableColumn
rcPTP1588BClkPTPPortType=_RcPTP1588BClkPTPPortType_Object((1,3,6,1,4,1,15004,4,12,4,1,1,7),_RcPTP1588BClkPTPPortType_Type())
rcPTP1588BClkPTPPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkPTPPortType.setStatus(_A)
class _RcPTP1588BClkSyncInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*((_O,1),(_P,2),(_Q,3),(_E,4),(_F,5)))
_RcPTP1588BClkSyncInt_Type.__name__=_D
_RcPTP1588BClkSyncInt_Object=MibTableColumn
rcPTP1588BClkSyncInt=_RcPTP1588BClkSyncInt_Object((1,3,6,1,4,1,15004,4,12,4,1,1,8),_RcPTP1588BClkSyncInt_Type())
rcPTP1588BClkSyncInt.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkSyncInt.setStatus(_A)
class _RcPTP1588BClkAnnounceInt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*((_E,1),(_F,2),(_H,3),(_I,4),(_J,5),(_K,6)))
_RcPTP1588BClkAnnounceInt_Type.__name__=_D
_RcPTP1588BClkAnnounceInt_Object=MibTableColumn
rcPTP1588BClkAnnounceInt=_RcPTP1588BClkAnnounceInt_Object((1,3,6,1,4,1,15004,4,12,4,1,1,9),_RcPTP1588BClkAnnounceInt_Type())
rcPTP1588BClkAnnounceInt.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkAnnounceInt.setStatus(_A)
class _RcPTP1588BClkAnnounceRcTout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(2,4))
_RcPTP1588BClkAnnounceRcTout_Type.__name__=_D
_RcPTP1588BClkAnnounceRcTout_Object=MibTableColumn
rcPTP1588BClkAnnounceRcTout=_RcPTP1588BClkAnnounceRcTout_Object((1,3,6,1,4,1,15004,4,12,4,1,1,10),_RcPTP1588BClkAnnounceRcTout_Type())
rcPTP1588BClkAnnounceRcTout.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkAnnounceRcTout.setStatus(_A)
_RcPTP1588BClkAutoReg_Type=TruthValue
_RcPTP1588BClkAutoReg_Object=MibTableColumn
rcPTP1588BClkAutoReg=_RcPTP1588BClkAutoReg_Object((1,3,6,1,4,1,15004,4,12,4,1,1,11),_RcPTP1588BClkAutoReg_Type())
rcPTP1588BClkAutoReg.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkAutoReg.setStatus(_A)
_RcPTP1588BClkMasterIP_Type=IpAddress
_RcPTP1588BClkMasterIP_Object=MibTableColumn
rcPTP1588BClkMasterIP=_RcPTP1588BClkMasterIP_Object((1,3,6,1,4,1,15004,4,12,4,1,1,12),_RcPTP1588BClkMasterIP_Type())
rcPTP1588BClkMasterIP.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkMasterIP.setStatus(_A)
_RcPTP1588BClkBackUpIP_Type=IpAddress
_RcPTP1588BClkBackUpIP_Object=MibTableColumn
rcPTP1588BClkBackUpIP=_RcPTP1588BClkBackUpIP_Object((1,3,6,1,4,1,15004,4,12,4,1,1,13),_RcPTP1588BClkBackUpIP_Type())
rcPTP1588BClkBackUpIP.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkBackUpIP.setStatus(_A)
_RcPTP1588BClkGMIdentity_Type=Integer32
_RcPTP1588BClkGMIdentity_Object=MibTableColumn
rcPTP1588BClkGMIdentity=_RcPTP1588BClkGMIdentity_Object((1,3,6,1,4,1,15004,4,12,4,1,1,14),_RcPTP1588BClkGMIdentity_Type())
rcPTP1588BClkGMIdentity.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkGMIdentity.setStatus(_A)
class _RcPTP1588BClkVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-2,4094))
_RcPTP1588BClkVlanId_Type.__name__=_D
_RcPTP1588BClkVlanId_Object=MibTableColumn
rcPTP1588BClkVlanId=_RcPTP1588BClkVlanId_Object((1,3,6,1,4,1,15004,4,12,4,1,1,15),_RcPTP1588BClkVlanId_Type())
rcPTP1588BClkVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkVlanId.setStatus(_A)
class _RcPTP1588BClkPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_RcPTP1588BClkPriority_Type.__name__=_G
_RcPTP1588BClkPriority_Object=MibTableColumn
rcPTP1588BClkPriority=_RcPTP1588BClkPriority_Object((1,3,6,1,4,1,15004,4,12,4,1,1,16),_RcPTP1588BClkPriority_Type())
rcPTP1588BClkPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rcPTP1588BClkPriority.setStatus(_A)
rcPTP1588BaseGroup=ObjectGroup((1,3,6,1,4,1,15004,4,12,3,2,1))
rcPTP1588BaseGroup.setObjects(*((_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z)))
if mibBuilder.loadTexts:rcPTP1588BaseGroup.setStatus(_A)
rcPTP1588BCTablesGroup=ObjectGroup((1,3,6,1,4,1,15004,4,12,3,2,2))
rcPTP1588BCTablesGroup.setObjects(*((_B,_N),(_B,_A0),(_B,_A1),(_B,_A2),(_B,'rcPTP1588BClkNetProtocol'),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD)))
if mibBuilder.loadTexts:rcPTP1588BCTablesGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rcPTP1588':rcPTP1588,'rcPTP1588Base':rcPTP1588Base,_a:rcPTP1588ClkType,_b:rcPTP1588EthPorts,_c:rcPTP1588StartUpWait,_d:rcPTP1588NetClass,_e:rcPTP1588SlaveEthPort,_f:rcPTP1588SlaveDomain,_g:rcPTP1588SlaveAutoReg,_h:rcPTP1588SlaveMasteIP,_i:rcPTP1588SlaveBackUpIP,_j:rcPTP1588ServoStatus,_k:rcPTP1588SlaveFeqAdj,_l:rcPTP1588E2EDelay,_m:rcPTP1588GlobalEnable,_n:rcPTP1588GlobalP2PRequestInterval,_o:rcPTP1588GlobalE2ERequestInterval,_p:rcPTP1588Global1Step,_q:rcPTP1588ClkAnnounceInt,_r:rcPTP1588ClkAnnounceRcTout,_s:rcPTP1588ClkSyncInt,_t:rcPTP1588ClkDelayMech,_u:rcPTP1588ClkProfileId,_v:rcPTP1588ClkDomainNumber,_w:rcPTP1588ClkNetProtocol,_x:rcPTP1588ClkVlanId,_y:rcPTP1588ClkPriority,_z:rcPTP1588ClkAccuracy,'rcPTP1588Conformance':rcPTP1588Conformance,'rcPTP1588Groups':rcPTP1588Groups,'rcPTP1588BaseGroup':rcPTP1588BaseGroup,'rcPTP1588BCTablesGroup':rcPTP1588BCTablesGroup,'rcPTP1588BCTables':rcPTP1588BCTables,'rcPTP1588BClkTable':rcPTP1588BClkTable,'rcPTP1588BClkEntry':rcPTP1588BClkEntry,_N:rcPTP1588BClkPorts,_A0:rcPTP1588BClkGroupName,_A1:rcPTP1588BClkProfileId,_A2:rcPTP1588BClkDomainNumber,'rcPTP1588BClkTransportProtocol':rcPTP1588BClkTransportProtocol,_A3:rcPTP1588BClkPathDelayMech,_A4:rcPTP1588BClkPTPPortType,_A5:rcPTP1588BClkSyncInt,_A6:rcPTP1588BClkAnnounceInt,_A7:rcPTP1588BClkAnnounceRcTout,_A8:rcPTP1588BClkAutoReg,_A9:rcPTP1588BClkMasterIP,_AA:rcPTP1588BClkBackUpIP,_AB:rcPTP1588BClkGMIdentity,_AC:rcPTP1588BClkVlanId,_AD:rcPTP1588BClkPriority})