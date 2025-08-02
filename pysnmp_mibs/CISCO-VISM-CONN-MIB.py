_AN='ciscoVismConnGroupRev1'
_AM='ciscoVismConnGroup'
_AL='vismChanUserPcrNumber'
_AK='vismChanUserMinPCRBandwidth'
_AJ='vismChanUserMaxMbsIngress'
_AI='vismChanUserMaxScrIngress'
_AH='vismChanUserMaxPCRBandwidth'
_AG='vismChanAisDelayTime'
_AF='vismChanAisSuppression'
_AE='vismChanDirectRoute'
_AD='vismChanPrefRouteId'
_AC='vismChanStatusBitMap'
_AB='vismChanRcvATMState'
_AA='vismChanXmtATMState'
_A9='vismChanState'
_A8='deprecated'
_A7='percentage'
_A6='ciscoVismConnStateGroup'
_A5='vismConnAdminStatus'
_A4='vismVCCI'
_A3='vismFarEndNSAPAddress'
_A2='vismFarEndGWIDAddress'
_A1='vismFarEndE164Address'
_A0='vismFarEndAddressType'
_z='vismChanReroute'
_y='vismChanFallbackLcn'
_x='vismChanApplication'
_w='vismChanClrEgress'
_v='vismChanMbsEgress'
_u='vismChanScrEgress'
_t='vismConnPCREgress'
_s='vismChanClrIngress'
_r='vismChanCdvt'
_q='vismChanMbsIngress'
_p='vismChanScrIngress'
_o='vismChanLockingState'
_n='vismChanActivityState'
_m='vismChanPreference'
_l='vismChanProtection'
_k='vismConnRemotePercentUtil'
_j='vismConnRemotePCR'
_i='vismConnPercentUtil'
_h='vismConnPCR'
_g='vismRestrictTrunkType'
_f='vismMaxCost'
_e='vismRoutingPriority'
_d='vismConnServiceType'
_c='vismVpcFlag'
_b='vismMastership'
_a='vismRemoteNSAP'
_Z='vismRemoteVci'
_Y='vismRemoteVpi'
_X='vismLocalNSAP'
_W='vismLocalVci'
_V='vismLocalVpi'
_U='vismChanConnType'
_T='vismChanPvcType'
_S='vismChanRTDResult'
_R='vismChanTestState'
_Q='vismChanTestType'
_P='vismChanLocRmtLpbkState'
_O='vismChanPortNum'
_N='vismChanRowStatus'
_M='vismChanNumNextAvailable'
_L='vismStateChanNum'
_K='DisplayString'
_J='vismCnfChanNum'
_I='TruthValue'
_H='OctetString'
_G='Unsigned32'
_F='cells-per-second'
_E='read-only'
_D='Integer32'
_C='read-write'
_B='current'
_A='CISCO-VISM-CONN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
vismChanCnfGrp,vismChanGrp=mibBuilder.importSymbols('BASIS-MIB','vismChanCnfGrp','vismChanGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_G,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_K,'PhysAddress','TextualConvention',_I)
ciscoVismConnMIB=ModuleIdentity((1,3,6,1,4,1,351,150,86))
if mibBuilder.loadTexts:ciscoVismConnMIB.setRevisions(('2004-05-03 00:00','2004-03-09 00:00','2004-02-18 00:00'))
_VismChanCnfGrpTable_Object=MibTable
vismChanCnfGrpTable=_VismChanCnfGrpTable_Object((1,3,6,1,4,1,351,110,5,5,3,1,1))
if mibBuilder.loadTexts:vismChanCnfGrpTable.setStatus(_B)
_VismChanCnfGrpEntry_Object=MibTableRow
vismChanCnfGrpEntry=_VismChanCnfGrpEntry_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1))
vismChanCnfGrpEntry.setIndexNames((0,_A,_J))
if mibBuilder.loadTexts:vismChanCnfGrpEntry.setStatus(_B)
class _VismCnfChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismCnfChanNum_Type.__name__=_D
_VismCnfChanNum_Object=MibTableColumn
vismCnfChanNum=_VismCnfChanNum_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,1),_VismCnfChanNum_Type())
vismCnfChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismCnfChanNum.setStatus(_B)
class _VismChanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3),('outOfService',4)))
_VismChanRowStatus_Type.__name__=_D
_VismChanRowStatus_Object=MibTableColumn
vismChanRowStatus=_VismChanRowStatus_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,2),_VismChanRowStatus_Type())
vismChanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanRowStatus.setStatus(_B)
class _VismChanPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_VismChanPortNum_Type.__name__=_D
_VismChanPortNum_Object=MibTableColumn
vismChanPortNum=_VismChanPortNum_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,3),_VismChanPortNum_Type())
vismChanPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanPortNum.setStatus(_B)
class _VismChanLocRmtLpbkState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_VismChanLocRmtLpbkState_Type.__name__=_D
_VismChanLocRmtLpbkState_Object=MibTableColumn
vismChanLocRmtLpbkState=_VismChanLocRmtLpbkState_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,4),_VismChanLocRmtLpbkState_Type())
vismChanLocRmtLpbkState.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanLocRmtLpbkState.setStatus(_B)
class _VismChanTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('testcon',1),('testdelay',2),('notest',3)))
_VismChanTestType_Type.__name__=_D
_VismChanTestType_Object=MibTableColumn
vismChanTestType=_VismChanTestType_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,5),_VismChanTestType_Type())
vismChanTestType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanTestType.setStatus(_B)
class _VismChanTestState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('passed',1),('failed',2),('inprogress',3),('notinprogress',4)))
_VismChanTestState_Type.__name__=_D
_VismChanTestState_Object=MibTableColumn
vismChanTestState=_VismChanTestState_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,6),_VismChanTestState_Type())
vismChanTestState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanTestState.setStatus(_B)
class _VismChanRTDResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_VismChanRTDResult_Type.__name__=_D
_VismChanRTDResult_Object=MibTableColumn
vismChanRTDResult=_VismChanRTDResult_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,7),_VismChanRTDResult_Type())
vismChanRTDResult.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanRTDResult.setStatus(_B)
if mibBuilder.loadTexts:vismChanRTDResult.setUnits('microseconds')
class _VismChanPvcType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('aal-5',1),('aal-2',2),('aal-1',3)))
_VismChanPvcType_Type.__name__=_D
_VismChanPvcType_Object=MibTableColumn
vismChanPvcType=_VismChanPvcType_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,8),_VismChanPvcType_Type())
vismChanPvcType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanPvcType.setStatus(_B)
class _VismChanConnType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('pvc',1))
_VismChanConnType_Type.__name__=_D
_VismChanConnType_Object=MibTableColumn
vismChanConnType=_VismChanConnType_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,9),_VismChanConnType_Type())
vismChanConnType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanConnType.setStatus(_B)
class _VismLocalVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismLocalVpi_Type.__name__=_D
_VismLocalVpi_Object=MibTableColumn
vismLocalVpi=_VismLocalVpi_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,10),_VismLocalVpi_Type())
vismLocalVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLocalVpi.setStatus(_B)
class _VismLocalVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismLocalVci_Type.__name__=_D
_VismLocalVci_Object=MibTableColumn
vismLocalVci=_VismLocalVci_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,11),_VismLocalVci_Type())
vismLocalVci.setMaxAccess(_E)
if mibBuilder.loadTexts:vismLocalVci.setStatus(_B)
class _VismLocalNSAP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_VismLocalNSAP_Type.__name__=_H
_VismLocalNSAP_Object=MibTableColumn
vismLocalNSAP=_VismLocalNSAP_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,12),_VismLocalNSAP_Type())
vismLocalNSAP.setMaxAccess(_C)
if mibBuilder.loadTexts:vismLocalNSAP.setStatus(_B)
class _VismRemoteVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismRemoteVpi_Type.__name__=_D
_VismRemoteVpi_Object=MibTableColumn
vismRemoteVpi=_VismRemoteVpi_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,13),_VismRemoteVpi_Type())
vismRemoteVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRemoteVpi.setStatus(_B)
class _VismRemoteVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismRemoteVci_Type.__name__=_D
_VismRemoteVci_Object=MibTableColumn
vismRemoteVci=_VismRemoteVci_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,14),_VismRemoteVci_Type())
vismRemoteVci.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRemoteVci.setStatus(_B)
class _VismRemoteNSAP_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_VismRemoteNSAP_Type.__name__=_H
_VismRemoteNSAP_Object=MibTableColumn
vismRemoteNSAP=_VismRemoteNSAP_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,15),_VismRemoteNSAP_Type())
vismRemoteNSAP.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRemoteNSAP.setStatus(_B)
class _VismMastership_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),('unknown',3)))
_VismMastership_Type.__name__=_D
_VismMastership_Object=MibTableColumn
vismMastership=_VismMastership_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,16),_VismMastership_Type())
vismMastership.setMaxAccess(_C)
if mibBuilder.loadTexts:vismMastership.setStatus(_B)
class _VismVpcFlag_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(2));namedValues=NamedValues(('vcc',2))
_VismVpcFlag_Type.__name__=_D
_VismVpcFlag_Object=MibTableColumn
vismVpcFlag=_VismVpcFlag_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,17),_VismVpcFlag_Type())
vismVpcFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVpcFlag.setStatus(_B)
class _VismConnServiceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cbr',1),('vbr-rt',2),('vbr-nrt',3),('vbr3-rt',4),('vbr2-rt',5),('vbr2-nrt',6),('vbr3-nrt',7)))
_VismConnServiceType_Type.__name__=_D
_VismConnServiceType_Object=MibTableColumn
vismConnServiceType=_VismConnServiceType_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,18),_VismConnServiceType_Type())
vismConnServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismConnServiceType.setStatus(_B)
class _VismRoutingPriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_VismRoutingPriority_Type.__name__=_D
_VismRoutingPriority_Object=MibTableColumn
vismRoutingPriority=_VismRoutingPriority_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,19),_VismRoutingPriority_Type())
vismRoutingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRoutingPriority.setStatus(_B)
class _VismMaxCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VismMaxCost_Type.__name__=_D
_VismMaxCost_Object=MibTableColumn
vismMaxCost=_VismMaxCost_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,20),_VismMaxCost_Type())
vismMaxCost.setMaxAccess(_C)
if mibBuilder.loadTexts:vismMaxCost.setStatus(_B)
class _VismRestrictTrunkType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noresriction',1),('terrestrialTrunk',2),('sateliteTrunk',3)))
_VismRestrictTrunkType_Type.__name__=_D
_VismRestrictTrunkType_Object=MibTableColumn
vismRestrictTrunkType=_VismRestrictTrunkType_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,21),_VismRestrictTrunkType_Type())
vismRestrictTrunkType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismRestrictTrunkType.setStatus(_B)
class _VismConnPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismConnPCR_Type.__name__=_D
_VismConnPCR_Object=MibTableColumn
vismConnPCR=_VismConnPCR_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,22),_VismConnPCR_Type())
vismConnPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:vismConnPCR.setStatus(_B)
if mibBuilder.loadTexts:vismConnPCR.setUnits(_F)
class _VismConnPercentUtil_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismConnPercentUtil_Type.__name__=_D
_VismConnPercentUtil_Object=MibTableColumn
vismConnPercentUtil=_VismConnPercentUtil_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,23),_VismConnPercentUtil_Type())
vismConnPercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:vismConnPercentUtil.setStatus(_B)
if mibBuilder.loadTexts:vismConnPercentUtil.setUnits(_A7)
class _VismConnRemotePCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismConnRemotePCR_Type.__name__=_D
_VismConnRemotePCR_Object=MibTableColumn
vismConnRemotePCR=_VismConnRemotePCR_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,24),_VismConnRemotePCR_Type())
vismConnRemotePCR.setMaxAccess(_C)
if mibBuilder.loadTexts:vismConnRemotePCR.setStatus(_B)
if mibBuilder.loadTexts:vismConnRemotePCR.setUnits(_F)
class _VismConnRemotePercentUtil_Type(Integer32):defaultValue=100;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_VismConnRemotePercentUtil_Type.__name__=_D
_VismConnRemotePercentUtil_Object=MibTableColumn
vismConnRemotePercentUtil=_VismConnRemotePercentUtil_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,25),_VismConnRemotePercentUtil_Type())
vismConnRemotePercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:vismConnRemotePercentUtil.setStatus(_B)
if mibBuilder.loadTexts:vismConnRemotePercentUtil.setUnits(_A7)
class _VismChanProtection_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('protected',1),('unprotected',2)))
_VismChanProtection_Type.__name__=_D
_VismChanProtection_Object=MibTableColumn
vismChanProtection=_VismChanProtection_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,26),_VismChanProtection_Type())
vismChanProtection.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanProtection.setStatus(_B)
class _VismChanPreference_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('primary',1),('secondary',2)))
_VismChanPreference_Type.__name__=_D
_VismChanPreference_Object=MibTableColumn
vismChanPreference=_VismChanPreference_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,27),_VismChanPreference_Type())
vismChanPreference.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanPreference.setStatus(_B)
class _VismChanActivityState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('active',1),('standby',2),('failed',3),('unknown',4)))
_VismChanActivityState_Type.__name__=_D
_VismChanActivityState_Object=MibTableColumn
vismChanActivityState=_VismChanActivityState_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,28),_VismChanActivityState_Type())
vismChanActivityState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanActivityState.setStatus(_B)
class _VismChanLockingState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unlock',1),('lock',2)))
_VismChanLockingState_Type.__name__=_D
_VismChanLockingState_Object=MibTableColumn
vismChanLockingState=_VismChanLockingState_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,29),_VismChanLockingState_Type())
vismChanLockingState.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanLockingState.setStatus(_B)
class _VismChanScrIngress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismChanScrIngress_Type.__name__=_D
_VismChanScrIngress_Object=MibTableColumn
vismChanScrIngress=_VismChanScrIngress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,30),_VismChanScrIngress_Type())
vismChanScrIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanScrIngress.setStatus(_B)
if mibBuilder.loadTexts:vismChanScrIngress.setUnits(_F)
class _VismChanMbsIngress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VismChanMbsIngress_Type.__name__=_D
_VismChanMbsIngress_Object=MibTableColumn
vismChanMbsIngress=_VismChanMbsIngress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,31),_VismChanMbsIngress_Type())
vismChanMbsIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanMbsIngress.setStatus(_B)
if mibBuilder.loadTexts:vismChanMbsIngress.setUnits(_F)
class _VismChanClrIngress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VismChanClrIngress_Type.__name__=_D
_VismChanClrIngress_Object=MibTableColumn
vismChanClrIngress=_VismChanClrIngress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,32),_VismChanClrIngress_Type())
vismChanClrIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanClrIngress.setStatus(_B)
class _VismChanCdvt_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_VismChanCdvt_Type.__name__=_D
_VismChanCdvt_Object=MibTableColumn
vismChanCdvt=_VismChanCdvt_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,33),_VismChanCdvt_Type())
vismChanCdvt.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanCdvt.setStatus(_B)
class _VismConnPCREgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismConnPCREgress_Type.__name__=_D
_VismConnPCREgress_Object=MibTableColumn
vismConnPCREgress=_VismConnPCREgress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,34),_VismConnPCREgress_Type())
vismConnPCREgress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismConnPCREgress.setStatus(_B)
if mibBuilder.loadTexts:vismConnPCREgress.setUnits(_F)
class _VismChanScrEgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismChanScrEgress_Type.__name__=_D
_VismChanScrEgress_Object=MibTableColumn
vismChanScrEgress=_VismChanScrEgress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,35),_VismChanScrEgress_Type())
vismChanScrEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanScrEgress.setStatus(_B)
if mibBuilder.loadTexts:vismChanScrEgress.setUnits(_F)
class _VismChanMbsEgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VismChanMbsEgress_Type.__name__=_D
_VismChanMbsEgress_Object=MibTableColumn
vismChanMbsEgress=_VismChanMbsEgress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,36),_VismChanMbsEgress_Type())
vismChanMbsEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanMbsEgress.setStatus(_B)
if mibBuilder.loadTexts:vismChanMbsEgress.setUnits(_F)
class _VismChanClrEgress_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VismChanClrEgress_Type.__name__=_D
_VismChanClrEgress_Object=MibTableColumn
vismChanClrEgress=_VismChanClrEgress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,37),_VismChanClrEgress_Type())
vismChanClrEgress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanClrEgress.setStatus(_B)
class _VismChanApplication_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('control',1),('bearer',2),('signaling',3)))
_VismChanApplication_Type.__name__=_D
_VismChanApplication_Object=MibTableColumn
vismChanApplication=_VismChanApplication_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,38),_VismChanApplication_Type())
vismChanApplication.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanApplication.setStatus(_B)
class _VismChanFallbackLcn_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismChanFallbackLcn_Type.__name__=_D
_VismChanFallbackLcn_Object=MibTableColumn
vismChanFallbackLcn=_VismChanFallbackLcn_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,39),_VismChanFallbackLcn_Type())
vismChanFallbackLcn.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanFallbackLcn.setStatus(_B)
class _VismChanReroute_Type(TruthValue):defaultValue=2
_VismChanReroute_Type.__name__=_I
_VismChanReroute_Object=MibTableColumn
vismChanReroute=_VismChanReroute_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,40),_VismChanReroute_Type())
vismChanReroute.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanReroute.setStatus(_B)
class _VismFarEndAddressType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('notapplicable',1),('nsap',2),('e164',3),('gwid',4),('unspecified',5)))
_VismFarEndAddressType_Type.__name__=_D
_VismFarEndAddressType_Object=MibTableColumn
vismFarEndAddressType=_VismFarEndAddressType_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,41),_VismFarEndAddressType_Type())
vismFarEndAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFarEndAddressType.setStatus(_B)
class _VismFarEndE164Address_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,15))
_VismFarEndE164Address_Type.__name__=_K
_VismFarEndE164Address_Object=MibTableColumn
vismFarEndE164Address=_VismFarEndE164Address_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,42),_VismFarEndE164Address_Type())
vismFarEndE164Address.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFarEndE164Address.setStatus(_B)
class _VismFarEndGWIDAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_VismFarEndGWIDAddress_Type.__name__=_K
_VismFarEndGWIDAddress_Object=MibTableColumn
vismFarEndGWIDAddress=_VismFarEndGWIDAddress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,43),_VismFarEndGWIDAddress_Type())
vismFarEndGWIDAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFarEndGWIDAddress.setStatus(_B)
class _VismFarEndNSAPAddress_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_VismFarEndNSAPAddress_Type.__name__=_H
_VismFarEndNSAPAddress_Object=MibTableColumn
vismFarEndNSAPAddress=_VismFarEndNSAPAddress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,44),_VismFarEndNSAPAddress_Type())
vismFarEndNSAPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismFarEndNSAPAddress.setStatus(_B)
class _VismVCCI_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismVCCI_Type.__name__=_D
_VismVCCI_Object=MibTableColumn
vismVCCI=_VismVCCI_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,45),_VismVCCI_Type())
vismVCCI.setMaxAccess(_C)
if mibBuilder.loadTexts:vismVCCI.setStatus(_B)
class _VismConnAdminStatus_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_VismConnAdminStatus_Type.__name__=_D
_VismConnAdminStatus_Object=MibTableColumn
vismConnAdminStatus=_VismConnAdminStatus_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,46),_VismConnAdminStatus_Type())
vismConnAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:vismConnAdminStatus.setStatus(_B)
class _VismChanPrefRouteId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VismChanPrefRouteId_Type.__name__=_G
_VismChanPrefRouteId_Object=MibTableColumn
vismChanPrefRouteId=_VismChanPrefRouteId_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,47),_VismChanPrefRouteId_Type())
vismChanPrefRouteId.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanPrefRouteId.setStatus(_B)
class _VismChanDirectRoute_Type(TruthValue):defaultValue=2
_VismChanDirectRoute_Type.__name__=_I
_VismChanDirectRoute_Object=MibTableColumn
vismChanDirectRoute=_VismChanDirectRoute_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,48),_VismChanDirectRoute_Type())
vismChanDirectRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanDirectRoute.setStatus(_B)
class _VismChanAisSuppression_Type(TruthValue):defaultValue=2
_VismChanAisSuppression_Type.__name__=_I
_VismChanAisSuppression_Object=MibTableColumn
vismChanAisSuppression=_VismChanAisSuppression_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,49),_VismChanAisSuppression_Type())
vismChanAisSuppression.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanAisSuppression.setStatus(_B)
class _VismChanAisDelayTime_Type(Unsigned32):defaultValue=30;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_VismChanAisDelayTime_Type.__name__=_G
_VismChanAisDelayTime_Object=MibTableColumn
vismChanAisDelayTime=_VismChanAisDelayTime_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,50),_VismChanAisDelayTime_Type())
vismChanAisDelayTime.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanAisDelayTime.setStatus(_B)
class _VismChanUserMaxPCRBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismChanUserMaxPCRBandwidth_Type.__name__=_G
_VismChanUserMaxPCRBandwidth_Object=MibTableColumn
vismChanUserMaxPCRBandwidth=_VismChanUserMaxPCRBandwidth_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,51),_VismChanUserMaxPCRBandwidth_Type())
vismChanUserMaxPCRBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanUserMaxPCRBandwidth.setStatus(_B)
if mibBuilder.loadTexts:vismChanUserMaxPCRBandwidth.setUnits(_F)
class _VismChanUserMaxScrIngress_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismChanUserMaxScrIngress_Type.__name__=_G
_VismChanUserMaxScrIngress_Object=MibTableColumn
vismChanUserMaxScrIngress=_VismChanUserMaxScrIngress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,52),_VismChanUserMaxScrIngress_Type())
vismChanUserMaxScrIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanUserMaxScrIngress.setStatus(_B)
if mibBuilder.loadTexts:vismChanUserMaxScrIngress.setUnits(_F)
class _VismChanUserMaxMbsIngress_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VismChanUserMaxMbsIngress_Type.__name__=_G
_VismChanUserMaxMbsIngress_Object=MibTableColumn
vismChanUserMaxMbsIngress=_VismChanUserMaxMbsIngress_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,53),_VismChanUserMaxMbsIngress_Type())
vismChanUserMaxMbsIngress.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanUserMaxMbsIngress.setStatus(_B)
if mibBuilder.loadTexts:vismChanUserMaxMbsIngress.setUnits(_F)
class _VismChanUserMinPCRBandwidth_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000))
_VismChanUserMinPCRBandwidth_Type.__name__=_G
_VismChanUserMinPCRBandwidth_Object=MibTableColumn
vismChanUserMinPCRBandwidth=_VismChanUserMinPCRBandwidth_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,54),_VismChanUserMinPCRBandwidth_Type())
vismChanUserMinPCRBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanUserMinPCRBandwidth.setStatus(_B)
if mibBuilder.loadTexts:vismChanUserMinPCRBandwidth.setUnits(_F)
class _VismChanUserPcrNumber_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('userConfiguredMaxBandwidth',1),('userConfiguredMinBandwidth',2)))
_VismChanUserPcrNumber_Type.__name__=_D
_VismChanUserPcrNumber_Object=MibTableColumn
vismChanUserPcrNumber=_VismChanUserPcrNumber_Object((1,3,6,1,4,1,351,110,5,5,3,1,1,1,55),_VismChanUserPcrNumber_Type())
vismChanUserPcrNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:vismChanUserPcrNumber.setStatus(_B)
class _VismChanNumNextAvailable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,510))
_VismChanNumNextAvailable_Type.__name__=_D
_VismChanNumNextAvailable_Object=MibScalar
vismChanNumNextAvailable=_VismChanNumNextAvailable_Object((1,3,6,1,4,1,351,110,5,5,3,1,2),_VismChanNumNextAvailable_Type())
vismChanNumNextAvailable.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanNumNextAvailable.setStatus(_B)
_VismChanStateGrp_ObjectIdentity=ObjectIdentity
vismChanStateGrp=_VismChanStateGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,3,2))
_VismChanStateGrpTable_Object=MibTable
vismChanStateGrpTable=_VismChanStateGrpTable_Object((1,3,6,1,4,1,351,110,5,5,3,2,1))
if mibBuilder.loadTexts:vismChanStateGrpTable.setStatus(_B)
_VismChanStateGrpEntry_Object=MibTableRow
vismChanStateGrpEntry=_VismChanStateGrpEntry_Object((1,3,6,1,4,1,351,110,5,5,3,2,1,1))
vismChanStateGrpEntry.setIndexNames((0,_A,_L))
if mibBuilder.loadTexts:vismChanStateGrpEntry.setStatus(_B)
class _VismStateChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismStateChanNum_Type.__name__=_D
_VismStateChanNum_Object=MibTableColumn
vismStateChanNum=_VismStateChanNum_Object((1,3,6,1,4,1,351,110,5,5,3,2,1,1,1),_VismStateChanNum_Type())
vismStateChanNum.setMaxAccess(_E)
if mibBuilder.loadTexts:vismStateChanNum.setStatus(_B)
class _VismChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notConfigured',1),('okay',2),('alarm',3)))
_VismChanState_Type.__name__=_D
_VismChanState_Object=MibTableColumn
vismChanState=_VismChanState_Object((1,3,6,1,4,1,351,110,5,5,3,2,1,1,2),_VismChanState_Type())
vismChanState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanState.setStatus(_B)
class _VismChanXmtATMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('normal',2),('sendingAIS',3),('sendingFERF',4)))
_VismChanXmtATMState_Type.__name__=_D
_VismChanXmtATMState_Object=MibTableColumn
vismChanXmtATMState=_VismChanXmtATMState_Object((1,3,6,1,4,1,351,110,5,5,3,2,1,1,3),_VismChanXmtATMState_Type())
vismChanXmtATMState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanXmtATMState.setStatus(_B)
class _VismChanRcvATMState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('other',1),('normal',2),('receivingAIS',3),('receivingFERF',4),('oamFailure',5)))
_VismChanRcvATMState_Type.__name__=_D
_VismChanRcvATMState_Object=MibTableColumn
vismChanRcvATMState=_VismChanRcvATMState_Object((1,3,6,1,4,1,351,110,5,5,3,2,1,1,4),_VismChanRcvATMState_Type())
vismChanRcvATMState.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanRcvATMState.setStatus(_B)
class _VismChanStatusBitMap_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VismChanStatusBitMap_Type.__name__=_D
_VismChanStatusBitMap_Object=MibTableColumn
vismChanStatusBitMap=_VismChanStatusBitMap_Object((1,3,6,1,4,1,351,110,5,5,3,2,1,1,5),_VismChanStatusBitMap_Type())
vismChanStatusBitMap.setMaxAccess(_E)
if mibBuilder.loadTexts:vismChanStatusBitMap.setStatus(_B)
_CiscoVismConnMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismConnMIBConformance=_CiscoVismConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,86,2))
_CiscoVismConnMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismConnMIBGroups=_CiscoVismConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,86,2,1))
_CiscoVismConnMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismConnMIBCompliances=_CiscoVismConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,86,2,2))
ciscoVismConnGroup=ObjectGroup((1,3,6,1,4,1,351,150,86,2,1,1))
ciscoVismConnGroup.setObjects(*((_A,_M),(_A,_J),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5)))
if mibBuilder.loadTexts:ciscoVismConnGroup.setStatus(_A8)
ciscoVismConnStateGroup=ObjectGroup((1,3,6,1,4,1,351,150,86,2,1,2))
ciscoVismConnStateGroup.setObjects(*((_A,_L),(_A,_A9),(_A,_AA),(_A,_AB),(_A,_AC)))
if mibBuilder.loadTexts:ciscoVismConnStateGroup.setStatus(_B)
ciscoVismConnGroupRev1=ObjectGroup((1,3,6,1,4,1,351,150,86,2,1,3))
ciscoVismConnGroupRev1.setObjects(*((_A,_M),(_A,_J),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_AD),(_A,_AE),(_A,_AF),(_A,_AG),(_A,_AH),(_A,_AI),(_A,_AJ),(_A,_AK),(_A,_AL)))
if mibBuilder.loadTexts:ciscoVismConnGroupRev1.setStatus(_B)
ciscoVismConnCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,86,2,2,1))
ciscoVismConnCompliance.setObjects(*((_A,_AM),(_A,_A6)))
if mibBuilder.loadTexts:ciscoVismConnCompliance.setStatus(_A8)
ciscoVismConnComplianceRev1=ModuleCompliance((1,3,6,1,4,1,351,150,86,2,2,2))
ciscoVismConnComplianceRev1.setObjects(*((_A,_AN),(_A,_A6)))
if mibBuilder.loadTexts:ciscoVismConnComplianceRev1.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vismChanCnfGrpTable':vismChanCnfGrpTable,'vismChanCnfGrpEntry':vismChanCnfGrpEntry,_J:vismCnfChanNum,_N:vismChanRowStatus,_O:vismChanPortNum,_P:vismChanLocRmtLpbkState,_Q:vismChanTestType,_R:vismChanTestState,_S:vismChanRTDResult,_T:vismChanPvcType,_U:vismChanConnType,_V:vismLocalVpi,_W:vismLocalVci,_X:vismLocalNSAP,_Y:vismRemoteVpi,_Z:vismRemoteVci,_a:vismRemoteNSAP,_b:vismMastership,_c:vismVpcFlag,_d:vismConnServiceType,_e:vismRoutingPriority,_f:vismMaxCost,_g:vismRestrictTrunkType,_h:vismConnPCR,_i:vismConnPercentUtil,_j:vismConnRemotePCR,_k:vismConnRemotePercentUtil,_l:vismChanProtection,_m:vismChanPreference,_n:vismChanActivityState,_o:vismChanLockingState,_p:vismChanScrIngress,_q:vismChanMbsIngress,_s:vismChanClrIngress,_r:vismChanCdvt,_t:vismConnPCREgress,_u:vismChanScrEgress,_v:vismChanMbsEgress,_w:vismChanClrEgress,_x:vismChanApplication,_y:vismChanFallbackLcn,_z:vismChanReroute,_A0:vismFarEndAddressType,_A1:vismFarEndE164Address,_A2:vismFarEndGWIDAddress,_A3:vismFarEndNSAPAddress,_A4:vismVCCI,_A5:vismConnAdminStatus,_AD:vismChanPrefRouteId,_AE:vismChanDirectRoute,_AF:vismChanAisSuppression,_AG:vismChanAisDelayTime,_AH:vismChanUserMaxPCRBandwidth,_AI:vismChanUserMaxScrIngress,_AJ:vismChanUserMaxMbsIngress,_AK:vismChanUserMinPCRBandwidth,_AL:vismChanUserPcrNumber,_M:vismChanNumNextAvailable,'vismChanStateGrp':vismChanStateGrp,'vismChanStateGrpTable':vismChanStateGrpTable,'vismChanStateGrpEntry':vismChanStateGrpEntry,_L:vismStateChanNum,_A9:vismChanState,_AA:vismChanXmtATMState,_AB:vismChanRcvATMState,_AC:vismChanStatusBitMap,'ciscoVismConnMIB':ciscoVismConnMIB,'ciscoVismConnMIBConformance':ciscoVismConnMIBConformance,'ciscoVismConnMIBGroups':ciscoVismConnMIBGroups,_AM:ciscoVismConnGroup,_A6:ciscoVismConnStateGroup,_AN:ciscoVismConnGroupRev1,'ciscoVismConnMIBCompliances':ciscoVismConnMIBCompliances,'ciscoVismConnCompliance':ciscoVismConnCompliance,'ciscoVismConnComplianceRev1':ciscoVismConnComplianceRev1})