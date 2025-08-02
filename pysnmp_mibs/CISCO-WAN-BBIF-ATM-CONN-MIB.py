_AR='cwbAtmConnGeneralGroup'
_AQ='cwbAtmConnStateGroup'
_AP='cwbAtmConnGroup'
_AO='bbChanVpIdNextAvailable'
_AN='bbChanNumNextAvailable'
_AM='bbChanIngrRcvState'
_AL='bbChanEgrXmtState'
_AK='bbChanState'
_AJ='bbChanUpcMCR'
_AI='bbRemoteConnPercentUtil'
_AH='bbRemoteConnSCR'
_AG='bbRemoteConnPCR'
_AF='bbConnPercentUtil'
_AE='bbConnSCR'
_AD='bbConnPCR'
_AC='bbConnServiceType'
_AB='bbConnVpcFlag'
_AA='bbChanTestStateCPESide'
_A9='bbChanTestTypeCPESide'
_A8='bbChanTestResult'
_A7='bbChanTestState'
_A6='bbChanTestType'
_A5='bbChanRestrictTrkType'
_A4='bbChanMaxCost'
_A3='bbChanRtePriority'
_A2='bbChanMaster'
_A1='bbChanRemoteNsapAddr'
_A0='bbChanRemoteVci'
_z='bbChanRemoteVpi'
_y='bbChanLocalNsapAddr'
_x='bbChanLocalVci'
_w='bbChanLocalVpi'
_v='bbChanOvrSubOvrRide'
_u='bbChanEgrSrvRate'
_t='bbChanEgrPercentUtil'
_s='bbChanIngrPercentUtil'
_r='bbChanMaxCellMemThreshold'
_q='bbChanCongstUpdateCode'
_p='bbChanClpLoThreshold'
_o='bbChanClpHiThreshold'
_n='bbChanFrmDiscardThreshold'
_m='bbChanDiscardOption'
_l='bbChanEfciThreshold'
_k='bbChanUpcSCRPolicing'
_j='bbChanGcra2Action'
_i='bbChanGcra1Action'
_h='bbChanUpcMBS'
_g='bbChanUpcSCR'
_f='bbChanUpcCDVT'
_e='bbChanUpcPCR'
_d='bbChanUpcEnable'
_c='bbChanVci'
_b='bbChanVpi'
_a='bbChanIfNum'
_Z='bbChanSvcConnId'
_Y='bbChanSvcFlag'
_X='bbChanConnDesc'
_W='bbChanServiceType'
_V='bbChanConnType'
_U='bbChanRowStatus'
_T='notinprogress'
_S='inprogress'
_R='failed'
_Q='passed'
_P='notest'
_O='discardAllNonComformCells'
_N='tagAndDiscard'
_M='tagCells'
_L='noAction'
_K='enable'
_J='disable'
_I='DisplayString'
_H='normal'
_G='bbChanStateNum'
_F='bbChanCnfNum'
_E='read-only'
_D='read-write'
_C='Integer32'
_B='CISCO-WAN-BBIF-ATM-CONN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bbChanCnfGrp,bbChanStateGrp=mibBuilder.importSymbols('BASIS-MIB','bbChanCnfGrp','bbChanStateGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_I,'PhysAddress','TextualConvention')
ciscoWanBbifAtmConnMIB=ModuleIdentity((1,3,6,1,4,1,351,150,35))
if mibBuilder.loadTexts:ciscoWanBbifAtmConnMIB.setRevisions(('2002-09-09 00:00',))
class IfNsapAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_BbChanCnfGrpTable_Object=MibTable
bbChanCnfGrpTable=_BbChanCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,2,7,1,1))
if mibBuilder.loadTexts:bbChanCnfGrpTable.setStatus(_A)
_BbChanCnfGrpEntry_Object=MibTableRow
bbChanCnfGrpEntry=_BbChanCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1))
bbChanCnfGrpEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:bbChanCnfGrpEntry.setStatus(_A)
class _BbChanCnfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4111))
_BbChanCnfNum_Type.__name__=_C
_BbChanCnfNum_Object=MibTableColumn
bbChanCnfNum=_BbChanCnfNum_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,1),_BbChanCnfNum_Type())
bbChanCnfNum.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanCnfNum.setStatus(_A)
class _BbChanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('delete',2),('modify',3)))
_BbChanRowStatus_Type.__name__=_C
_BbChanRowStatus_Object=MibTableColumn
bbChanRowStatus=_BbChanRowStatus_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,2),_BbChanRowStatus_Type())
bbChanRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanRowStatus.setStatus(_A)
class _BbChanConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vpc',1),('vcc',2)))
_BbChanConnType_Type.__name__=_C
_BbChanConnType_Object=MibTableColumn
bbChanConnType=_BbChanConnType_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,3),_BbChanConnType_Type())
bbChanConnType.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanConnType.setStatus(_A)
class _BbChanServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('cbr',1),('vbr',2),('abr',3),('ubr',4),('vbr-rt',5)))
_BbChanServiceType_Type.__name__=_C
_BbChanServiceType_Object=MibTableColumn
bbChanServiceType=_BbChanServiceType_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,4),_BbChanServiceType_Type())
bbChanServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanServiceType.setStatus(_A)
class _BbChanConnDesc_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_BbChanConnDesc_Type.__name__=_I
_BbChanConnDesc_Object=MibTableColumn
bbChanConnDesc=_BbChanConnDesc_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,5),_BbChanConnDesc_Type())
bbChanConnDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanConnDesc.setStatus(_A)
class _BbChanSvcFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('svc',1),('pvc',2),('spvc',3)))
_BbChanSvcFlag_Type.__name__=_C
_BbChanSvcFlag_Object=MibTableColumn
bbChanSvcFlag=_BbChanSvcFlag_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,6),_BbChanSvcFlag_Type())
bbChanSvcFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanSvcFlag.setStatus(_A)
_BbChanSvcConnId_Type=Integer32
_BbChanSvcConnId_Object=MibTableColumn
bbChanSvcConnId=_BbChanSvcConnId_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,7),_BbChanSvcConnId_Type())
bbChanSvcConnId.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanSvcConnId.setStatus(_A)
class _BbChanIfNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_BbChanIfNum_Type.__name__=_C
_BbChanIfNum_Object=MibTableColumn
bbChanIfNum=_BbChanIfNum_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,8),_BbChanIfNum_Type())
bbChanIfNum.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanIfNum.setStatus(_A)
class _BbChanVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BbChanVpi_Type.__name__=_C
_BbChanVpi_Object=MibTableColumn
bbChanVpi=_BbChanVpi_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,9),_BbChanVpi_Type())
bbChanVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanVpi.setStatus(_A)
class _BbChanVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BbChanVci_Type.__name__=_C
_BbChanVci_Object=MibTableColumn
bbChanVci=_BbChanVci_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,10),_BbChanVci_Type())
bbChanVci.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanVci.setStatus(_A)
class _BbChanUpcEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BbChanUpcEnable_Type.__name__=_C
_BbChanUpcEnable_Object=MibTableColumn
bbChanUpcEnable=_BbChanUpcEnable_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,11),_BbChanUpcEnable_Type())
bbChanUpcEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanUpcEnable.setStatus(_A)
class _BbChanUpcPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(50,1412832))
_BbChanUpcPCR_Type.__name__=_C
_BbChanUpcPCR_Object=MibTableColumn
bbChanUpcPCR=_BbChanUpcPCR_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,12),_BbChanUpcPCR_Type())
bbChanUpcPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanUpcPCR.setStatus(_A)
class _BbChanUpcCDVT_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5000000))
_BbChanUpcCDVT_Type.__name__=_C
_BbChanUpcCDVT_Object=MibTableColumn
bbChanUpcCDVT=_BbChanUpcCDVT_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,13),_BbChanUpcCDVT_Type())
bbChanUpcCDVT.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanUpcCDVT.setStatus(_A)
class _BbChanUpcSCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1412832))
_BbChanUpcSCR_Type.__name__=_C
_BbChanUpcSCR_Object=MibTableColumn
bbChanUpcSCR=_BbChanUpcSCR_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,14),_BbChanUpcSCR_Type())
bbChanUpcSCR.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanUpcSCR.setStatus(_A)
class _BbChanUpcMBS_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,5000000))
_BbChanUpcMBS_Type.__name__=_C
_BbChanUpcMBS_Object=MibTableColumn
bbChanUpcMBS=_BbChanUpcMBS_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,15),_BbChanUpcMBS_Type())
bbChanUpcMBS.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanUpcMBS.setStatus(_A)
class _BbChanGcra1Action_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_BbChanGcra1Action_Type.__name__=_C
_BbChanGcra1Action_Object=MibTableColumn
bbChanGcra1Action=_BbChanGcra1Action_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,16),_BbChanGcra1Action_Type())
bbChanGcra1Action.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanGcra1Action.setStatus(_A)
class _BbChanGcra2Action_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_L,1),(_M,2),(_N,3),(_O,4)))
_BbChanGcra2Action_Type.__name__=_C
_BbChanGcra2Action_Object=MibTableColumn
bbChanGcra2Action=_BbChanGcra2Action_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,17),_BbChanGcra2Action_Type())
bbChanGcra2Action.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanGcra2Action.setStatus(_A)
class _BbChanUpcSCRPolicing_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('clp0',1),('clp0and1',2),('off',3)))
_BbChanUpcSCRPolicing_Type.__name__=_C
_BbChanUpcSCRPolicing_Object=MibTableColumn
bbChanUpcSCRPolicing=_BbChanUpcSCRPolicing_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,18),_BbChanUpcSCRPolicing_Type())
bbChanUpcSCRPolicing.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanUpcSCRPolicing.setStatus(_A)
class _BbChanEfciThreshold_Type(Integer32):defaultValue=196608;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,491520))
_BbChanEfciThreshold_Type.__name__=_C
_BbChanEfciThreshold_Object=MibTableColumn
bbChanEfciThreshold=_BbChanEfciThreshold_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,19),_BbChanEfciThreshold_Type())
bbChanEfciThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanEfciThreshold.setStatus(_A)
class _BbChanDiscardOption_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clpHysteresis',1),('frameDiscard',2)))
_BbChanDiscardOption_Type.__name__=_C
_BbChanDiscardOption_Object=MibTableColumn
bbChanDiscardOption=_BbChanDiscardOption_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,20),_BbChanDiscardOption_Type())
bbChanDiscardOption.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanDiscardOption.setStatus(_A)
class _BbChanFrmDiscardThreshold_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,491520))
_BbChanFrmDiscardThreshold_Type.__name__=_C
_BbChanFrmDiscardThreshold_Object=MibTableColumn
bbChanFrmDiscardThreshold=_BbChanFrmDiscardThreshold_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,21),_BbChanFrmDiscardThreshold_Type())
bbChanFrmDiscardThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanFrmDiscardThreshold.setStatus(_A)
class _BbChanClpHiThreshold_Type(Integer32):defaultValue=196608;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,491520))
_BbChanClpHiThreshold_Type.__name__=_C
_BbChanClpHiThreshold_Object=MibTableColumn
bbChanClpHiThreshold=_BbChanClpHiThreshold_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,22),_BbChanClpHiThreshold_Type())
bbChanClpHiThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanClpHiThreshold.setStatus(_A)
class _BbChanClpLoThreshold_Type(Integer32):defaultValue=131072;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,491520))
_BbChanClpLoThreshold_Type.__name__=_C
_BbChanClpLoThreshold_Object=MibTableColumn
bbChanClpLoThreshold=_BbChanClpLoThreshold_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,23),_BbChanClpLoThreshold_Type())
bbChanClpLoThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanClpLoThreshold.setStatus(_A)
class _BbChanCongstUpdateCode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('dontUpdate',1),('setCiBit',2),('setEfciBit',3),('clearEfciBit',4)))
_BbChanCongstUpdateCode_Type.__name__=_C
_BbChanCongstUpdateCode_Object=MibTableColumn
bbChanCongstUpdateCode=_BbChanCongstUpdateCode_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,24),_BbChanCongstUpdateCode_Type())
bbChanCongstUpdateCode.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanCongstUpdateCode.setStatus(_A)
class _BbChanMaxCellMemThreshold_Type(Integer32):defaultValue=262144;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,512000))
_BbChanMaxCellMemThreshold_Type.__name__=_C
_BbChanMaxCellMemThreshold_Object=MibTableColumn
bbChanMaxCellMemThreshold=_BbChanMaxCellMemThreshold_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,25),_BbChanMaxCellMemThreshold_Type())
bbChanMaxCellMemThreshold.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanMaxCellMemThreshold.setStatus(_A)
class _BbChanIngrPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BbChanIngrPercentUtil_Type.__name__=_C
_BbChanIngrPercentUtil_Object=MibTableColumn
bbChanIngrPercentUtil=_BbChanIngrPercentUtil_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,26),_BbChanIngrPercentUtil_Type())
bbChanIngrPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanIngrPercentUtil.setStatus(_A)
class _BbChanEgrPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BbChanEgrPercentUtil_Type.__name__=_C
_BbChanEgrPercentUtil_Object=MibTableColumn
bbChanEgrPercentUtil=_BbChanEgrPercentUtil_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,27),_BbChanEgrPercentUtil_Type())
bbChanEgrPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanEgrPercentUtil.setStatus(_A)
class _BbChanEgrSrvRate_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1412832))
_BbChanEgrSrvRate_Type.__name__=_C
_BbChanEgrSrvRate_Object=MibTableColumn
bbChanEgrSrvRate=_BbChanEgrSrvRate_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,28),_BbChanEgrSrvRate_Type())
bbChanEgrSrvRate.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanEgrSrvRate.setStatus(_A)
class _BbChanOvrSubOvrRide_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_BbChanOvrSubOvrRide_Type.__name__=_C
_BbChanOvrSubOvrRide_Object=MibTableColumn
bbChanOvrSubOvrRide=_BbChanOvrSubOvrRide_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,29),_BbChanOvrSubOvrRide_Type())
bbChanOvrSubOvrRide.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanOvrSubOvrRide.setStatus(_A)
class _BbChanLocalVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BbChanLocalVpi_Type.__name__=_C
_BbChanLocalVpi_Object=MibTableColumn
bbChanLocalVpi=_BbChanLocalVpi_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,30),_BbChanLocalVpi_Type())
bbChanLocalVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanLocalVpi.setStatus(_A)
class _BbChanLocalVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BbChanLocalVci_Type.__name__=_C
_BbChanLocalVci_Object=MibTableColumn
bbChanLocalVci=_BbChanLocalVci_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,31),_BbChanLocalVci_Type())
bbChanLocalVci.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanLocalVci.setStatus(_A)
_BbChanLocalNsapAddr_Type=IfNsapAddress
_BbChanLocalNsapAddr_Object=MibTableColumn
bbChanLocalNsapAddr=_BbChanLocalNsapAddr_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,32),_BbChanLocalNsapAddr_Type())
bbChanLocalNsapAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanLocalNsapAddr.setStatus(_A)
class _BbChanRemoteVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_BbChanRemoteVpi_Type.__name__=_C
_BbChanRemoteVpi_Object=MibTableColumn
bbChanRemoteVpi=_BbChanRemoteVpi_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,33),_BbChanRemoteVpi_Type())
bbChanRemoteVpi.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanRemoteVpi.setStatus(_A)
class _BbChanRemoteVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_BbChanRemoteVci_Type.__name__=_C
_BbChanRemoteVci_Object=MibTableColumn
bbChanRemoteVci=_BbChanRemoteVci_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,34),_BbChanRemoteVci_Type())
bbChanRemoteVci.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanRemoteVci.setStatus(_A)
_BbChanRemoteNsapAddr_Type=IfNsapAddress
_BbChanRemoteNsapAddr_Object=MibTableColumn
bbChanRemoteNsapAddr=_BbChanRemoteNsapAddr_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,35),_BbChanRemoteNsapAddr_Type())
bbChanRemoteNsapAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanRemoteNsapAddr.setStatus(_A)
class _BbChanMaster_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('unknown',3)))
_BbChanMaster_Type.__name__=_C
_BbChanMaster_Object=MibTableColumn
bbChanMaster=_BbChanMaster_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,36),_BbChanMaster_Type())
bbChanMaster.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanMaster.setStatus(_A)
class _BbChanRtePriority_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_BbChanRtePriority_Type.__name__=_C
_BbChanRtePriority_Object=MibTableColumn
bbChanRtePriority=_BbChanRtePriority_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,37),_BbChanRtePriority_Type())
bbChanRtePriority.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanRtePriority.setStatus(_A)
class _BbChanMaxCost_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BbChanMaxCost_Type.__name__=_C
_BbChanMaxCost_Object=MibTableColumn
bbChanMaxCost=_BbChanMaxCost_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,38),_BbChanMaxCost_Type())
bbChanMaxCost.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanMaxCost.setStatus(_A)
class _BbChanRestrictTrkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noRestriction',1),('terrestrialTrunk',2),('satelliteTrunk',3)))
_BbChanRestrictTrkType_Type.__name__=_C
_BbChanRestrictTrkType_Object=MibTableColumn
bbChanRestrictTrkType=_BbChanRestrictTrkType_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,39),_BbChanRestrictTrkType_Type())
bbChanRestrictTrkType.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanRestrictTrkType.setStatus(_A)
class _BbChanTestType_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('testcon',1),('testdelay',2),(_P,3)))
_BbChanTestType_Type.__name__=_C
_BbChanTestType_Object=MibTableColumn
bbChanTestType=_BbChanTestType_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,40),_BbChanTestType_Type())
bbChanTestType.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanTestType.setStatus(_A)
class _BbChanTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4)))
_BbChanTestState_Type.__name__=_C
_BbChanTestState_Object=MibTableColumn
bbChanTestState=_BbChanTestState_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,41),_BbChanTestState_Type())
bbChanTestState.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanTestState.setStatus(_A)
class _BbChanTestResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_BbChanTestResult_Type.__name__=_C
_BbChanTestResult_Object=MibTableColumn
bbChanTestResult=_BbChanTestResult_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,42),_BbChanTestResult_Type())
bbChanTestResult.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanTestResult.setStatus(_A)
if mibBuilder.loadTexts:bbChanTestResult.setUnits('milliseconds')
class _BbChanTestTypeCPESide_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('testconseg',1),(_P,2)))
_BbChanTestTypeCPESide_Type.__name__=_C
_BbChanTestTypeCPESide_Object=MibTableColumn
bbChanTestTypeCPESide=_BbChanTestTypeCPESide_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,43),_BbChanTestTypeCPESide_Type())
bbChanTestTypeCPESide.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanTestTypeCPESide.setStatus(_A)
class _BbChanTestStateCPESide_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_Q,1),(_R,2),(_S,3),(_T,4)))
_BbChanTestStateCPESide_Type.__name__=_C
_BbChanTestStateCPESide_Object=MibTableColumn
bbChanTestStateCPESide=_BbChanTestStateCPESide_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,44),_BbChanTestStateCPESide_Type())
bbChanTestStateCPESide.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanTestStateCPESide.setStatus(_A)
class _BbConnVpcFlag_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vpc',1),('vcc',2)))
_BbConnVpcFlag_Type.__name__=_C
_BbConnVpcFlag_Object=MibTableColumn
bbConnVpcFlag=_BbConnVpcFlag_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,45),_BbConnVpcFlag_Type())
bbConnVpcFlag.setMaxAccess(_D)
if mibBuilder.loadTexts:bbConnVpcFlag.setStatus(_A)
class _BbConnServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,6,8)));namedValues=NamedValues(*(('cbr',1),('vbr',2),('ubr',4),('abrstd',6),('vbrrt',8)))
_BbConnServiceType_Type.__name__=_C
_BbConnServiceType_Object=MibTableColumn
bbConnServiceType=_BbConnServiceType_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,46),_BbConnServiceType_Type())
bbConnServiceType.setMaxAccess(_D)
if mibBuilder.loadTexts:bbConnServiceType.setStatus(_A)
_BbConnPCR_Type=Integer32
_BbConnPCR_Object=MibTableColumn
bbConnPCR=_BbConnPCR_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,47),_BbConnPCR_Type())
bbConnPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:bbConnPCR.setStatus(_A)
_BbConnSCR_Type=Integer32
_BbConnSCR_Object=MibTableColumn
bbConnSCR=_BbConnSCR_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,48),_BbConnSCR_Type())
bbConnSCR.setMaxAccess(_D)
if mibBuilder.loadTexts:bbConnSCR.setStatus(_A)
class _BbConnPercentUtil_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BbConnPercentUtil_Type.__name__=_C
_BbConnPercentUtil_Object=MibTableColumn
bbConnPercentUtil=_BbConnPercentUtil_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,49),_BbConnPercentUtil_Type())
bbConnPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:bbConnPercentUtil.setStatus(_A)
_BbRemoteConnPCR_Type=Integer32
_BbRemoteConnPCR_Object=MibTableColumn
bbRemoteConnPCR=_BbRemoteConnPCR_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,50),_BbRemoteConnPCR_Type())
bbRemoteConnPCR.setMaxAccess(_D)
if mibBuilder.loadTexts:bbRemoteConnPCR.setStatus(_A)
_BbRemoteConnSCR_Type=Integer32
_BbRemoteConnSCR_Object=MibTableColumn
bbRemoteConnSCR=_BbRemoteConnSCR_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,51),_BbRemoteConnSCR_Type())
bbRemoteConnSCR.setMaxAccess(_D)
if mibBuilder.loadTexts:bbRemoteConnSCR.setStatus(_A)
class _BbRemoteConnPercentUtil_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_BbRemoteConnPercentUtil_Type.__name__=_C
_BbRemoteConnPercentUtil_Object=MibTableColumn
bbRemoteConnPercentUtil=_BbRemoteConnPercentUtil_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,52),_BbRemoteConnPercentUtil_Type())
bbRemoteConnPercentUtil.setMaxAccess(_D)
if mibBuilder.loadTexts:bbRemoteConnPercentUtil.setStatus(_A)
class _BbChanUpcMCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1412832))
_BbChanUpcMCR_Type.__name__=_C
_BbChanUpcMCR_Object=MibTableColumn
bbChanUpcMCR=_BbChanUpcMCR_Object((1,3,6,1,4,1,351,110,5,2,7,1,1,1,53),_BbChanUpcMCR_Type())
bbChanUpcMCR.setMaxAccess(_D)
if mibBuilder.loadTexts:bbChanUpcMCR.setStatus(_A)
class _BbChanNumNextAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4111))
_BbChanNumNextAvailable_Type.__name__=_C
_BbChanNumNextAvailable_Object=MibScalar
bbChanNumNextAvailable=_BbChanNumNextAvailable_Object((1,3,6,1,4,1,351,110,5,2,7,1,2),_BbChanNumNextAvailable_Type())
bbChanNumNextAvailable.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanNumNextAvailable.setStatus(_A)
class _BbChanVpIdNextAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4095))
_BbChanVpIdNextAvailable_Type.__name__=_C
_BbChanVpIdNextAvailable_Object=MibScalar
bbChanVpIdNextAvailable=_BbChanVpIdNextAvailable_Object((1,3,6,1,4,1,351,110,5,2,7,1,3),_BbChanVpIdNextAvailable_Type())
bbChanVpIdNextAvailable.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanVpIdNextAvailable.setStatus(_A)
_BbChanStateGrpTable_Object=MibTable
bbChanStateGrpTable=_BbChanStateGrpTable_Object((1,3,6,1,4,1,351,110,5,2,7,2,1))
if mibBuilder.loadTexts:bbChanStateGrpTable.setStatus(_A)
_BbChanStateGrpEntry_Object=MibTableRow
bbChanStateGrpEntry=_BbChanStateGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,7,2,1,1))
bbChanStateGrpEntry.setIndexNames((0,_B,_G))
if mibBuilder.loadTexts:bbChanStateGrpEntry.setStatus(_A)
class _BbChanStateNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4111))
_BbChanStateNum_Type.__name__=_C
_BbChanStateNum_Object=MibTableColumn
bbChanStateNum=_BbChanStateNum_Object((1,3,6,1,4,1,351,110,5,2,7,2,1,1,1),_BbChanStateNum_Type())
bbChanStateNum.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanStateNum.setStatus(_A)
class _BbChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notconfigured',1),(_H,2),('alarm',3)))
_BbChanState_Type.__name__=_C
_BbChanState_Object=MibTableColumn
bbChanState=_BbChanState_Object((1,3,6,1,4,1,351,110,5,2,7,2,1,1,2),_BbChanState_Type())
bbChanState.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanState.setStatus(_A)
class _BbChanEgrXmtState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),(_H,2),('sendingAis',3),('sendingFerf',4)))
_BbChanEgrXmtState_Type.__name__=_C
_BbChanEgrXmtState_Object=MibTableColumn
bbChanEgrXmtState=_BbChanEgrXmtState_Object((1,3,6,1,4,1,351,110,5,2,7,2,1,1,3),_BbChanEgrXmtState_Type())
bbChanEgrXmtState.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanEgrXmtState.setStatus(_A)
class _BbChanIngrRcvState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),(_H,2),('receivingAis',3),('receivingFerf',4),('alarm',5)))
_BbChanIngrRcvState_Type.__name__=_C
_BbChanIngrRcvState_Object=MibTableColumn
bbChanIngrRcvState=_BbChanIngrRcvState_Object((1,3,6,1,4,1,351,110,5,2,7,2,1,1,4),_BbChanIngrRcvState_Type())
bbChanIngrRcvState.setMaxAccess(_E)
if mibBuilder.loadTexts:bbChanIngrRcvState.setStatus(_A)
_CwbAtmConnMIBConformance_ObjectIdentity=ObjectIdentity
cwbAtmConnMIBConformance=_CwbAtmConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,35,2))
_CwbAtmConnMIBGroups_ObjectIdentity=ObjectIdentity
cwbAtmConnMIBGroups=_CwbAtmConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,35,2,1))
_CwbAtmConnMIBCompliances_ObjectIdentity=ObjectIdentity
cwbAtmConnMIBCompliances=_CwbAtmConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,35,2,2))
cwbAtmConnGroup=ObjectGroup((1,3,6,1,4,1,351,150,35,2,1,1))
cwbAtmConnGroup.setObjects(*((_B,_F),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q),(_B,_r),(_B,_s),(_B,_t),(_B,_u),(_B,_v),(_B,_w),(_B,_x),(_B,_y),(_B,_z),(_B,_A0),(_B,_A1),(_B,_A2),(_B,_A3),(_B,_A4),(_B,_A5),(_B,_A6),(_B,_A7),(_B,_A8),(_B,_A9),(_B,_AA),(_B,_AB),(_B,_AC),(_B,_AD),(_B,_AE),(_B,_AF),(_B,_AG),(_B,_AH),(_B,_AI),(_B,_AJ)))
if mibBuilder.loadTexts:cwbAtmConnGroup.setStatus(_A)
cwbAtmConnStateGroup=ObjectGroup((1,3,6,1,4,1,351,150,35,2,1,2))
cwbAtmConnStateGroup.setObjects(*((_B,_G),(_B,_AK),(_B,_AL),(_B,_AM)))
if mibBuilder.loadTexts:cwbAtmConnStateGroup.setStatus(_A)
cwbAtmConnGeneralGroup=ObjectGroup((1,3,6,1,4,1,351,150,35,2,1,3))
cwbAtmConnGeneralGroup.setObjects(*((_B,_AN),(_B,_AO)))
if mibBuilder.loadTexts:cwbAtmConnGeneralGroup.setStatus(_A)
cwbAtmConnCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,35,2,2,1))
cwbAtmConnCompliance.setObjects(*((_B,_AP),(_B,_AQ),(_B,_AR)))
if mibBuilder.loadTexts:cwbAtmConnCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'IfNsapAddress':IfNsapAddress,'bbChanCnfGrpTable':bbChanCnfGrpTable,'bbChanCnfGrpEntry':bbChanCnfGrpEntry,_F:bbChanCnfNum,_U:bbChanRowStatus,_V:bbChanConnType,_W:bbChanServiceType,_X:bbChanConnDesc,_Y:bbChanSvcFlag,_Z:bbChanSvcConnId,_a:bbChanIfNum,_b:bbChanVpi,_c:bbChanVci,_d:bbChanUpcEnable,_e:bbChanUpcPCR,_f:bbChanUpcCDVT,_g:bbChanUpcSCR,_h:bbChanUpcMBS,_i:bbChanGcra1Action,_j:bbChanGcra2Action,_k:bbChanUpcSCRPolicing,_l:bbChanEfciThreshold,_m:bbChanDiscardOption,_n:bbChanFrmDiscardThreshold,_o:bbChanClpHiThreshold,_p:bbChanClpLoThreshold,_q:bbChanCongstUpdateCode,_r:bbChanMaxCellMemThreshold,_s:bbChanIngrPercentUtil,_t:bbChanEgrPercentUtil,_u:bbChanEgrSrvRate,_v:bbChanOvrSubOvrRide,_w:bbChanLocalVpi,_x:bbChanLocalVci,_y:bbChanLocalNsapAddr,_z:bbChanRemoteVpi,_A0:bbChanRemoteVci,_A1:bbChanRemoteNsapAddr,_A2:bbChanMaster,_A3:bbChanRtePriority,_A4:bbChanMaxCost,_A5:bbChanRestrictTrkType,_A6:bbChanTestType,_A7:bbChanTestState,_A8:bbChanTestResult,_A9:bbChanTestTypeCPESide,_AA:bbChanTestStateCPESide,_AB:bbConnVpcFlag,_AC:bbConnServiceType,_AD:bbConnPCR,_AE:bbConnSCR,_AF:bbConnPercentUtil,_AG:bbRemoteConnPCR,_AH:bbRemoteConnSCR,_AI:bbRemoteConnPercentUtil,_AJ:bbChanUpcMCR,_AN:bbChanNumNextAvailable,_AO:bbChanVpIdNextAvailable,'bbChanStateGrpTable':bbChanStateGrpTable,'bbChanStateGrpEntry':bbChanStateGrpEntry,_G:bbChanStateNum,_AK:bbChanState,_AL:bbChanEgrXmtState,_AM:bbChanIngrRcvState,'ciscoWanBbifAtmConnMIB':ciscoWanBbifAtmConnMIB,'cwbAtmConnMIBConformance':cwbAtmConnMIBConformance,'cwbAtmConnMIBGroups':cwbAtmConnMIBGroups,_AP:cwbAtmConnGroup,_AQ:cwbAtmConnStateGroup,_AR:cwbAtmConnGeneralGroup,'cwbAtmConnMIBCompliances':cwbAtmConnMIBCompliances,'cwbAtmConnCompliance':cwbAtmConnCompliance})