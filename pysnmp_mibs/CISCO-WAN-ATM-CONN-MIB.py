_Al='ciscoWanAtmConnChan4MIBGroup'
_Ak='ciscoWanAtmConnChan3MIBGroup'
_Aj='ciscoWanAtmConnChan2MIBGroup'
_Ai='ciscoWanAtmConnChanMIBGroup'
_Ah='cwChanGlobalTransactionId'
_Ag='cwaChanDirectRoute'
_Af='cwaChanPrefRouteId'
_Ae='cwaChanP2MP'
_Ad='cwaChanNumVCCsInAlarm'
_Ac='cwaChanNumVPCsInAlarm'
_Ab='cwaChanIngressRcvState'
_Aa='cwaChanIngressXmtState'
_AZ='cwaChanEgressRcvState'
_AY='cwaChanEgressXmtState'
_AX='cwaChanAlarmState'
_AW='cwaChanRemoteCDVT'
_AV='cwSlotIndex'
_AU='CiscoWanTestStatus'
_AT='CiscoWanLpbkTypes'
_AS='CiscoWanAisIW'
_AR='CiscoWanERSConfg'
_AQ='milliseconds'
_AP='ciscoWanAtmInformationGroup'
_AO='cwaChanRoutingPriority'
_AN='cwaChanSlaveType'
_AM='cwaChanAisIWCapability'
_AL='cwaChanAbrERS'
_AK='read-write'
_AJ='CiscoWanVSVDConfg'
_AI='cells'
_AH='not-accessible'
_AG='cwaChanOamSegEpEnable'
_AF='cwaChanVci'
_AE='cwaChanVpi'
_AD='ifIndex'
_AC='IF-MIB'
_AB='ciscoWanAtmConnStateGroup'
_AA='cwaChanTestRoundTripDelay'
_A9='cwaChanTestState'
_A8='cwaChanTestIterations'
_A7='cwaChanTestDir'
_A6='cwaChanTestType'
_A5='cwaChanRemoteCLR'
_A4='cwaChanCLR'
_A3='cwaChanExtAbrVSVD'
_A2='cwaChanIntAbrVSVD'
_A1='cwaChanRowStatus'
_A0='cwaChanAbrVSVDEnable'
_z='cwaChanAbrTBE'
_y='cwaChanAbrFRTT'
_x='cwaChanAbrCDF'
_w='cwaChanAbrTRM'
_v='cwaChanAbrNRM'
_u='cwaChanAbrRIF'
_t='cwaChanAbrRDF'
_s='cwaChanAbrADTF'
_r='cwaChanAbrICR'
_q='cwaChanRemotePercentUtil'
_p='cwaChanRemoteMBS'
_o='cwaChanRemoteCTD'
_n='cwaChanRemoteCDV'
_m='cwaChanRemoteSCR'
_l='cwaChanRemoteMCR'
_k='cwaChanRemotePCR'
_j='cwaChanPercentUtil'
_i='cwaChanCDVT'
_h='cwaChanMBS'
_g='cwaChanCTD'
_f='cwaChanCDV'
_e='cwaChanSCR'
_d='cwaChanMCR'
_c='cwaChanPCR'
_b='cwaChanOperStatus'
_a='cwaChanFrameDiscard'
_Z='cwaChanReroute'
_Y='cwaChanMaxCost'
_X='cwaChanRoutingMastership'
_W='cwaChanControllerId'
_V='cwaChanRemoteNSAPAddr'
_U='cwaChanRemoteVci'
_T='cwaChanRemoteVpi'
_S='cwaChanLocalNSAPAddr'
_R='cwaChanLocalVci'
_Q='cwaChanLocalVpi'
_P='cwaChanIdentifier'
_O='cwaChanUploadCounter'
_N='cwaChanCCEnable'
_M='cwaChanStatsEnable'
_L='cwaChanVpcFlag'
_K='cwaChanServiceCategory'
_J='microseconds'
_I='cells per second'
_H='Integer32'
_G='deprecated'
_F='TruthValue'
_E='read-only'
_D='Unsigned32'
_C='read-create'
_B='current'
_A='CISCO-WAN-ATM-CONN-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ifIndex,=mibBuilder.importSymbols(_AC,_AD)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_F)
ciscoWanAtmConnMIB=ModuleIdentity((1,3,6,1,4,1,351,150,1))
if mibBuilder.loadTexts:ciscoWanAtmConnMIB.setRevisions(('2003-03-30 00:00','2002-09-18 00:00','2002-03-24 00:00','2001-02-09 00:00','2001-01-03 00:00','2000-11-15 00:00','2000-07-17 00:00','2000-06-19 00:00'))
class CiscoAtmServiceCategory(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('cbr1',1),('vbr1RT',2),('vbr2RT',3),('vbr3RT',4),('vbr1nRT',5),('vbr2nRT',6),('vbr3nRT',7),('ubr1',8),('ubr2',9),('abr',10),('cbr2',11),('cbr3',12)))
class CiscoWanLpbkTypes(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noLpbk',1),('destructive',2),('nonDestructive',3)))
class CiscoWanLpbkDir(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('external',1),('internal',2),('forward',3),('reverse',4)))
class CiscoWanTestStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('noStatus',1),('lpbkInProgress',2),('lpbkSuccess',3),('lpbkAbort',4),('lpbkTimeOut',5),('lpbkInEffect',6)))
class CiscoWanOperStatus(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('operOk',1),('operFail',2),('adminDown',3)))
class CiscoWanNsapAtmAddress(TextualConvention,OctetString):status=_B;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
class CiscoWanAlarmState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,8,16,32,64)));namedValues=NamedValues(*(('ingAisRdi',1),('egrAisRdi',2),('conditioned',4),('interfaceFail',8),('ccFail',16),('mismatch',32),('ingAbitFail',64)))
class CiscoWanXmtState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('sendingAIS',2),('sendingRDI',3)))
class CiscoWanRcvState(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('normal',1),('receivingRDI',2),('receivingAIS',3),('ccFailure',4)))
class CiscoWanERSConfg(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('none',1),('enableIngress',2),('enableEgress',3),('enableBoth',4)))
class CiscoWanVSVDConfg(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('vsvdOff',1),('vsvdOn',2),('switchDefault',3)))
class CiscoWanAisIW(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('e2eAisCapable',1),('segAisCapable',2)))
class AbrRateFactors(TextualConvention,Integer32):status=_B;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16)));namedValues=NamedValues(*(('oneOver32768',1),('oneOver16384',2),('oneOver8192',3),('oneOver4096',4),('oneOver2048',5),('oneOver1024',6),('oneOver512',7),('oneOver256',8),('oneOver128',9),('oneOver64',10),('oneOver32',11),('oneOver16',12),('oneOver8',13),('oneOver4',14),('oneOver2',15),('one',16)))
_CwConnMibObjects_ObjectIdentity=ObjectIdentity
cwConnMibObjects=_CwConnMibObjects_ObjectIdentity((1,3,6,1,4,1,351,150,1,1))
_CwAtmChanCnfg_ObjectIdentity=ObjectIdentity
cwAtmChanCnfg=_CwAtmChanCnfg_ObjectIdentity((1,3,6,1,4,1,351,150,1,1,1))
_CwAtmChanCnfgTable_Object=MibTable
cwAtmChanCnfgTable=_CwAtmChanCnfgTable_Object((1,3,6,1,4,1,351,150,1,1,1,1))
if mibBuilder.loadTexts:cwAtmChanCnfgTable.setStatus(_B)
_CwAtmChanCnfgEntry_Object=MibTableRow
cwAtmChanCnfgEntry=_CwAtmChanCnfgEntry_Object((1,3,6,1,4,1,351,150,1,1,1,1,1))
cwAtmChanCnfgEntry.setIndexNames((0,_AC,_AD),(0,_A,_AE),(0,_A,_AF))
if mibBuilder.loadTexts:cwAtmChanCnfgEntry.setStatus(_B)
class _CwaChanVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwaChanVpi_Type.__name__=_D
_CwaChanVpi_Object=MibTableColumn
cwaChanVpi=_CwaChanVpi_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,1),_CwaChanVpi_Type())
cwaChanVpi.setMaxAccess(_AH)
if mibBuilder.loadTexts:cwaChanVpi.setStatus(_B)
class _CwaChanVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwaChanVci_Type.__name__=_D
_CwaChanVci_Object=MibTableColumn
cwaChanVci=_CwaChanVci_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,2),_CwaChanVci_Type())
cwaChanVci.setMaxAccess(_AH)
if mibBuilder.loadTexts:cwaChanVci.setStatus(_B)
_CwaChanServiceCategory_Type=CiscoAtmServiceCategory
_CwaChanServiceCategory_Object=MibTableColumn
cwaChanServiceCategory=_CwaChanServiceCategory_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,3),_CwaChanServiceCategory_Type())
cwaChanServiceCategory.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanServiceCategory.setStatus(_B)
_CwaChanVpcFlag_Type=TruthValue
_CwaChanVpcFlag_Object=MibTableColumn
cwaChanVpcFlag=_CwaChanVpcFlag_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,4),_CwaChanVpcFlag_Type())
cwaChanVpcFlag.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanVpcFlag.setStatus(_B)
class _CwaChanIdentifier_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanIdentifier_Type.__name__=_D
_CwaChanIdentifier_Object=MibTableColumn
cwaChanIdentifier=_CwaChanIdentifier_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,5),_CwaChanIdentifier_Type())
cwaChanIdentifier.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanIdentifier.setStatus(_B)
class _CwaChanUploadCounter_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanUploadCounter_Type.__name__=_D
_CwaChanUploadCounter_Object=MibTableColumn
cwaChanUploadCounter=_CwaChanUploadCounter_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,6),_CwaChanUploadCounter_Type())
cwaChanUploadCounter.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanUploadCounter.setStatus(_B)
class _CwaChanStatsEnable_Type(TruthValue):defaultValue=2
_CwaChanStatsEnable_Type.__name__=_F
_CwaChanStatsEnable_Object=MibTableColumn
cwaChanStatsEnable=_CwaChanStatsEnable_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,7),_CwaChanStatsEnable_Type())
cwaChanStatsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanStatsEnable.setStatus(_B)
class _CwaChanCCEnable_Type(TruthValue):defaultValue=2
_CwaChanCCEnable_Type.__name__=_F
_CwaChanCCEnable_Object=MibTableColumn
cwaChanCCEnable=_CwaChanCCEnable_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,8),_CwaChanCCEnable_Type())
cwaChanCCEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanCCEnable.setStatus(_B)
class _CwaChanLocalVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwaChanLocalVpi_Type.__name__=_D
_CwaChanLocalVpi_Object=MibTableColumn
cwaChanLocalVpi=_CwaChanLocalVpi_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,9),_CwaChanLocalVpi_Type())
cwaChanLocalVpi.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanLocalVpi.setStatus(_B)
class _CwaChanLocalVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwaChanLocalVci_Type.__name__=_D
_CwaChanLocalVci_Object=MibTableColumn
cwaChanLocalVci=_CwaChanLocalVci_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,10),_CwaChanLocalVci_Type())
cwaChanLocalVci.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanLocalVci.setStatus(_B)
_CwaChanLocalNSAPAddr_Type=CiscoWanNsapAtmAddress
_CwaChanLocalNSAPAddr_Object=MibTableColumn
cwaChanLocalNSAPAddr=_CwaChanLocalNSAPAddr_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,11),_CwaChanLocalNSAPAddr_Type())
cwaChanLocalNSAPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanLocalNSAPAddr.setStatus(_B)
class _CwaChanRemoteVpi_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_CwaChanRemoteVpi_Type.__name__=_D
_CwaChanRemoteVpi_Object=MibTableColumn
cwaChanRemoteVpi=_CwaChanRemoteVpi_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,12),_CwaChanRemoteVpi_Type())
cwaChanRemoteVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteVpi.setStatus(_B)
class _CwaChanRemoteVci_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwaChanRemoteVci_Type.__name__=_D
_CwaChanRemoteVci_Object=MibTableColumn
cwaChanRemoteVci=_CwaChanRemoteVci_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,13),_CwaChanRemoteVci_Type())
cwaChanRemoteVci.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteVci.setStatus(_B)
_CwaChanRemoteNSAPAddr_Type=CiscoWanNsapAtmAddress
_CwaChanRemoteNSAPAddr_Object=MibTableColumn
cwaChanRemoteNSAPAddr=_CwaChanRemoteNSAPAddr_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,14),_CwaChanRemoteNSAPAddr_Type())
cwaChanRemoteNSAPAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteNSAPAddr.setStatus(_B)
class _CwaChanControllerId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CwaChanControllerId_Type.__name__=_D
_CwaChanControllerId_Object=MibTableColumn
cwaChanControllerId=_CwaChanControllerId_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,15),_CwaChanControllerId_Type())
cwaChanControllerId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanControllerId.setStatus(_B)
class _CwaChanRoutingMastership_Type(TruthValue):defaultValue=2
_CwaChanRoutingMastership_Type.__name__=_F
_CwaChanRoutingMastership_Object=MibTableColumn
cwaChanRoutingMastership=_CwaChanRoutingMastership_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,16),_CwaChanRoutingMastership_Type())
cwaChanRoutingMastership.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRoutingMastership.setStatus(_B)
class _CwaChanMaxCost_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanMaxCost_Type.__name__=_D
_CwaChanMaxCost_Object=MibTableColumn
cwaChanMaxCost=_CwaChanMaxCost_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,17),_CwaChanMaxCost_Type())
cwaChanMaxCost.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanMaxCost.setStatus(_B)
class _CwaChanReroute_Type(TruthValue):defaultValue=2
_CwaChanReroute_Type.__name__=_F
_CwaChanReroute_Object=MibTableColumn
cwaChanReroute=_CwaChanReroute_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,18),_CwaChanReroute_Type())
cwaChanReroute.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanReroute.setStatus(_B)
class _CwaChanFrameDiscard_Type(TruthValue):defaultValue=2
_CwaChanFrameDiscard_Type.__name__=_F
_CwaChanFrameDiscard_Object=MibTableColumn
cwaChanFrameDiscard=_CwaChanFrameDiscard_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,19),_CwaChanFrameDiscard_Type())
cwaChanFrameDiscard.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanFrameDiscard.setStatus(_B)
_CwaChanOperStatus_Type=CiscoWanOperStatus
_CwaChanOperStatus_Object=MibTableColumn
cwaChanOperStatus=_CwaChanOperStatus_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,20),_CwaChanOperStatus_Type())
cwaChanOperStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanOperStatus.setStatus(_B)
class _CwaChanPCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanPCR_Type.__name__=_D
_CwaChanPCR_Object=MibTableColumn
cwaChanPCR=_CwaChanPCR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,21),_CwaChanPCR_Type())
cwaChanPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanPCR.setStatus(_B)
if mibBuilder.loadTexts:cwaChanPCR.setUnits(_I)
class _CwaChanMCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanMCR_Type.__name__=_D
_CwaChanMCR_Object=MibTableColumn
cwaChanMCR=_CwaChanMCR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,22),_CwaChanMCR_Type())
cwaChanMCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanMCR.setStatus(_B)
if mibBuilder.loadTexts:cwaChanMCR.setUnits(_I)
class _CwaChanSCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanSCR_Type.__name__=_D
_CwaChanSCR_Object=MibTableColumn
cwaChanSCR=_CwaChanSCR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,23),_CwaChanSCR_Type())
cwaChanSCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanSCR.setStatus(_B)
if mibBuilder.loadTexts:cwaChanSCR.setUnits(_I)
class _CwaChanCDV_Type(Unsigned32):defaultValue=16777215;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CwaChanCDV_Type.__name__=_D
_CwaChanCDV_Object=MibTableColumn
cwaChanCDV=_CwaChanCDV_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,24),_CwaChanCDV_Type())
cwaChanCDV.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanCDV.setStatus(_B)
if mibBuilder.loadTexts:cwaChanCDV.setUnits(_J)
class _CwaChanCTD_Type(Unsigned32):defaultValue=65535;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwaChanCTD_Type.__name__=_D
_CwaChanCTD_Object=MibTableColumn
cwaChanCTD=_CwaChanCTD_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,25),_CwaChanCTD_Type())
cwaChanCTD.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanCTD.setStatus(_B)
if mibBuilder.loadTexts:cwaChanCTD.setUnits(_AQ)
class _CwaChanMBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000000))
_CwaChanMBS_Type.__name__=_D
_CwaChanMBS_Object=MibTableColumn
cwaChanMBS=_CwaChanMBS_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,26),_CwaChanMBS_Type())
cwaChanMBS.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanMBS.setStatus(_B)
if mibBuilder.loadTexts:cwaChanMBS.setUnits(_AI)
class _CwaChanCDVT_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanCDVT_Type.__name__=_D
_CwaChanCDVT_Object=MibTableColumn
cwaChanCDVT=_CwaChanCDVT_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,27),_CwaChanCDVT_Type())
cwaChanCDVT.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanCDVT.setStatus(_B)
if mibBuilder.loadTexts:cwaChanCDVT.setUnits(_J)
class _CwaChanPercentUtil_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CwaChanPercentUtil_Type.__name__=_D
_CwaChanPercentUtil_Object=MibTableColumn
cwaChanPercentUtil=_CwaChanPercentUtil_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,28),_CwaChanPercentUtil_Type())
cwaChanPercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanPercentUtil.setStatus(_B)
class _CwaChanRemotePCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanRemotePCR_Type.__name__=_D
_CwaChanRemotePCR_Object=MibTableColumn
cwaChanRemotePCR=_CwaChanRemotePCR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,29),_CwaChanRemotePCR_Type())
cwaChanRemotePCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemotePCR.setStatus(_B)
if mibBuilder.loadTexts:cwaChanRemotePCR.setUnits(_I)
class _CwaChanRemoteMCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanRemoteMCR_Type.__name__=_D
_CwaChanRemoteMCR_Object=MibTableColumn
cwaChanRemoteMCR=_CwaChanRemoteMCR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,30),_CwaChanRemoteMCR_Type())
cwaChanRemoteMCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteMCR.setStatus(_B)
if mibBuilder.loadTexts:cwaChanRemoteMCR.setUnits(_I)
class _CwaChanRemoteSCR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanRemoteSCR_Type.__name__=_D
_CwaChanRemoteSCR_Object=MibTableColumn
cwaChanRemoteSCR=_CwaChanRemoteSCR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,31),_CwaChanRemoteSCR_Type())
cwaChanRemoteSCR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteSCR.setStatus(_B)
if mibBuilder.loadTexts:cwaChanRemoteSCR.setUnits(_I)
class _CwaChanRemoteCDV_Type(Unsigned32):defaultValue=16777215;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CwaChanRemoteCDV_Type.__name__=_D
_CwaChanRemoteCDV_Object=MibTableColumn
cwaChanRemoteCDV=_CwaChanRemoteCDV_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,32),_CwaChanRemoteCDV_Type())
cwaChanRemoteCDV.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteCDV.setStatus(_B)
if mibBuilder.loadTexts:cwaChanRemoteCDV.setUnits(_J)
class _CwaChanRemoteCTD_Type(Unsigned32):defaultValue=65535;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwaChanRemoteCTD_Type.__name__=_D
_CwaChanRemoteCTD_Object=MibTableColumn
cwaChanRemoteCTD=_CwaChanRemoteCTD_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,33),_CwaChanRemoteCTD_Type())
cwaChanRemoteCTD.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteCTD.setStatus(_B)
if mibBuilder.loadTexts:cwaChanRemoteCTD.setUnits(_AQ)
class _CwaChanRemoteMBS_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5000000))
_CwaChanRemoteMBS_Type.__name__=_D
_CwaChanRemoteMBS_Object=MibTableColumn
cwaChanRemoteMBS=_CwaChanRemoteMBS_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,34),_CwaChanRemoteMBS_Type())
cwaChanRemoteMBS.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteMBS.setStatus(_B)
if mibBuilder.loadTexts:cwaChanRemoteMBS.setUnits(_AI)
class _CwaChanRemoteCDVT_Type(Unsigned32):defaultValue=4294967295;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanRemoteCDVT_Type.__name__=_D
_CwaChanRemoteCDVT_Object=MibTableColumn
cwaChanRemoteCDVT=_CwaChanRemoteCDVT_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,35),_CwaChanRemoteCDVT_Type())
cwaChanRemoteCDVT.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteCDVT.setStatus(_G)
if mibBuilder.loadTexts:cwaChanRemoteCDVT.setUnits(_AI)
class _CwaChanRemotePercentUtil_Type(Unsigned32):defaultValue=100;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100))
_CwaChanRemotePercentUtil_Type.__name__=_D
_CwaChanRemotePercentUtil_Object=MibTableColumn
cwaChanRemotePercentUtil=_CwaChanRemotePercentUtil_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,36),_CwaChanRemotePercentUtil_Type())
cwaChanRemotePercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemotePercentUtil.setStatus(_B)
class _CwaChanAbrICR_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwaChanAbrICR_Type.__name__=_D
_CwaChanAbrICR_Object=MibTableColumn
cwaChanAbrICR=_CwaChanAbrICR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,37),_CwaChanAbrICR_Type())
cwaChanAbrICR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrICR.setStatus(_B)
if mibBuilder.loadTexts:cwaChanAbrICR.setUnits('cells/sec')
class _CwaChanAbrADTF_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1023))
_CwaChanAbrADTF_Type.__name__=_D
_CwaChanAbrADTF_Object=MibTableColumn
cwaChanAbrADTF=_CwaChanAbrADTF_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,38),_CwaChanAbrADTF_Type())
cwaChanAbrADTF.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrADTF.setStatus(_B)
if mibBuilder.loadTexts:cwaChanAbrADTF.setUnits('10 milliseconds')
_CwaChanAbrRDF_Type=AbrRateFactors
_CwaChanAbrRDF_Object=MibTableColumn
cwaChanAbrRDF=_CwaChanAbrRDF_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,39),_CwaChanAbrRDF_Type())
cwaChanAbrRDF.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrRDF.setStatus(_B)
_CwaChanAbrRIF_Type=AbrRateFactors
_CwaChanAbrRIF_Object=MibTableColumn
cwaChanAbrRIF=_CwaChanAbrRIF_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,40),_CwaChanAbrRIF_Type())
cwaChanAbrRIF.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrRIF.setStatus(_B)
class _CwaChanAbrNRM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('nrm2',1),('nrm4',2),('nrm8',3),('nrm16',4),('nrm32',5),('nrm64',6),('nrm128',7),('nrm256',8)))
_CwaChanAbrNRM_Type.__name__=_H
_CwaChanAbrNRM_Object=MibTableColumn
cwaChanAbrNRM=_CwaChanAbrNRM_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,41),_CwaChanAbrNRM_Type())
cwaChanAbrNRM.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrNRM.setStatus(_B)
class _CwaChanAbrTRM_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('trm0point78125',1),('trm1point5625',2),('trm3point125',3),('trm6point25',4),('trm12point5',5),('trm25',6),('trm50',7),('trm100',8)))
_CwaChanAbrTRM_Type.__name__=_H
_CwaChanAbrTRM_Object=MibTableColumn
cwaChanAbrTRM=_CwaChanAbrTRM_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,42),_CwaChanAbrTRM_Type())
cwaChanAbrTRM.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrTRM.setStatus(_B)
class _CwaChanAbrCDF_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('cdf0',1),('cdfOneOver64',2),('cdfOneOver32',3),('cdfOneOver16',4),('cdfOneOver8',5),('cdfOneOver4',6),('cdfOneOver2',7),('cdfOne',8)))
_CwaChanAbrCDF_Type.__name__=_H
_CwaChanAbrCDF_Object=MibTableColumn
cwaChanAbrCDF=_CwaChanAbrCDF_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,43),_CwaChanAbrCDF_Type())
cwaChanAbrCDF.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrCDF.setStatus(_B)
class _CwaChanAbrFRTT_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16700000))
_CwaChanAbrFRTT_Type.__name__=_D
_CwaChanAbrFRTT_Object=MibTableColumn
cwaChanAbrFRTT=_CwaChanAbrFRTT_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,44),_CwaChanAbrFRTT_Type())
cwaChanAbrFRTT.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrFRTT.setStatus(_B)
if mibBuilder.loadTexts:cwaChanAbrFRTT.setUnits(_J)
class _CwaChanAbrTBE_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,16777215))
_CwaChanAbrTBE_Type.__name__=_D
_CwaChanAbrTBE_Object=MibTableColumn
cwaChanAbrTBE=_CwaChanAbrTBE_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,45),_CwaChanAbrTBE_Type())
cwaChanAbrTBE.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrTBE.setStatus(_B)
class _CwaChanAbrERS_Type(CiscoWanERSConfg):defaultValue=1
_CwaChanAbrERS_Type.__name__=_AR
_CwaChanAbrERS_Object=MibTableColumn
cwaChanAbrERS=_CwaChanAbrERS_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,46),_CwaChanAbrERS_Type())
cwaChanAbrERS.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrERS.setStatus(_G)
class _CwaChanAbrVSVDEnable_Type(TruthValue):defaultValue=2
_CwaChanAbrVSVDEnable_Type.__name__=_F
_CwaChanAbrVSVDEnable_Object=MibTableColumn
cwaChanAbrVSVDEnable=_CwaChanAbrVSVDEnable_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,47),_CwaChanAbrVSVDEnable_Type())
cwaChanAbrVSVDEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAbrVSVDEnable.setStatus(_B)
_CwaChanRowStatus_Type=RowStatus
_CwaChanRowStatus_Object=MibTableColumn
cwaChanRowStatus=_CwaChanRowStatus_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,48),_CwaChanRowStatus_Type())
cwaChanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRowStatus.setStatus(_B)
class _CwaChanIntAbrVSVD_Type(CiscoWanVSVDConfg):defaultValue=3
_CwaChanIntAbrVSVD_Type.__name__=_AJ
_CwaChanIntAbrVSVD_Object=MibTableColumn
cwaChanIntAbrVSVD=_CwaChanIntAbrVSVD_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,49),_CwaChanIntAbrVSVD_Type())
cwaChanIntAbrVSVD.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanIntAbrVSVD.setStatus(_B)
class _CwaChanExtAbrVSVD_Type(CiscoWanVSVDConfg):defaultValue=3
_CwaChanExtAbrVSVD_Type.__name__=_AJ
_CwaChanExtAbrVSVD_Object=MibTableColumn
cwaChanExtAbrVSVD=_CwaChanExtAbrVSVD_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,50),_CwaChanExtAbrVSVD_Type())
cwaChanExtAbrVSVD.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanExtAbrVSVD.setStatus(_B)
class _CwaChanAisIWCapability_Type(CiscoWanAisIW):defaultValue=1
_CwaChanAisIWCapability_Type.__name__=_AS
_CwaChanAisIWCapability_Object=MibTableColumn
cwaChanAisIWCapability=_CwaChanAisIWCapability_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,51),_CwaChanAisIWCapability_Type())
cwaChanAisIWCapability.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanAisIWCapability.setStatus(_G)
class _CwaChanCLR_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CwaChanCLR_Type.__name__=_D
_CwaChanCLR_Object=MibTableColumn
cwaChanCLR=_CwaChanCLR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,52),_CwaChanCLR_Type())
cwaChanCLR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanCLR.setStatus(_B)
class _CwaChanRemoteCLR_Type(Unsigned32):defaultValue=6;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CwaChanRemoteCLR_Type.__name__=_D
_CwaChanRemoteCLR_Object=MibTableColumn
cwaChanRemoteCLR=_CwaChanRemoteCLR_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,53),_CwaChanRemoteCLR_Type())
cwaChanRemoteCLR.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRemoteCLR.setStatus(_B)
class _CwaChanOamSegEpEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('oamSegEp',1),('nonOamSegEp',2)))
_CwaChanOamSegEpEnable_Type.__name__=_H
_CwaChanOamSegEpEnable_Object=MibTableColumn
cwaChanOamSegEpEnable=_CwaChanOamSegEpEnable_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,54),_CwaChanOamSegEpEnable_Type())
cwaChanOamSegEpEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanOamSegEpEnable.setStatus(_B)
class _CwaChanSlaveType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('persistentSlave',1),('nonPersistentSlave',2)))
_CwaChanSlaveType_Type.__name__=_H
_CwaChanSlaveType_Object=MibTableColumn
cwaChanSlaveType=_CwaChanSlaveType_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,55),_CwaChanSlaveType_Type())
cwaChanSlaveType.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanSlaveType.setStatus(_B)
class _CwaChanRoutingPriority_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_CwaChanRoutingPriority_Type.__name__=_H
_CwaChanRoutingPriority_Object=MibTableColumn
cwaChanRoutingPriority=_CwaChanRoutingPriority_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,56),_CwaChanRoutingPriority_Type())
cwaChanRoutingPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanRoutingPriority.setStatus(_B)
class _CwaChanP2MP_Type(TruthValue):defaultValue=2
_CwaChanP2MP_Type.__name__=_F
_CwaChanP2MP_Object=MibTableColumn
cwaChanP2MP=_CwaChanP2MP_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,57),_CwaChanP2MP_Type())
cwaChanP2MP.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanP2MP.setStatus(_B)
class _CwaChanPrefRouteId_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CwaChanPrefRouteId_Type.__name__=_H
_CwaChanPrefRouteId_Object=MibTableColumn
cwaChanPrefRouteId=_CwaChanPrefRouteId_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,58),_CwaChanPrefRouteId_Type())
cwaChanPrefRouteId.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanPrefRouteId.setStatus(_B)
class _CwaChanDirectRoute_Type(TruthValue):defaultValue=2
_CwaChanDirectRoute_Type.__name__=_F
_CwaChanDirectRoute_Object=MibTableColumn
cwaChanDirectRoute=_CwaChanDirectRoute_Object((1,3,6,1,4,1,351,150,1,1,1,1,1,59),_CwaChanDirectRoute_Type())
cwaChanDirectRoute.setMaxAccess(_C)
if mibBuilder.loadTexts:cwaChanDirectRoute.setStatus(_B)
_CwAtmChanState_ObjectIdentity=ObjectIdentity
cwAtmChanState=_CwAtmChanState_ObjectIdentity((1,3,6,1,4,1,351,150,1,1,2))
_CwAtmChanStateTable_Object=MibTable
cwAtmChanStateTable=_CwAtmChanStateTable_Object((1,3,6,1,4,1,351,150,1,1,2,1))
if mibBuilder.loadTexts:cwAtmChanStateTable.setStatus(_B)
_CwAtmChanStateEntry_Object=MibTableRow
cwAtmChanStateEntry=_CwAtmChanStateEntry_Object((1,3,6,1,4,1,351,150,1,1,2,1,1))
cwAtmChanStateEntry.setIndexNames((0,_AC,_AD),(0,_A,_AE),(0,_A,_AF))
if mibBuilder.loadTexts:cwAtmChanStateEntry.setStatus(_B)
_CwaChanAlarmState_Type=CiscoWanAlarmState
_CwaChanAlarmState_Object=MibTableColumn
cwaChanAlarmState=_CwaChanAlarmState_Object((1,3,6,1,4,1,351,150,1,1,2,1,1,1),_CwaChanAlarmState_Type())
cwaChanAlarmState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanAlarmState.setStatus(_B)
_CwaChanEgressXmtState_Type=CiscoWanXmtState
_CwaChanEgressXmtState_Object=MibTableColumn
cwaChanEgressXmtState=_CwaChanEgressXmtState_Object((1,3,6,1,4,1,351,150,1,1,2,1,1,2),_CwaChanEgressXmtState_Type())
cwaChanEgressXmtState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanEgressXmtState.setStatus(_B)
_CwaChanEgressRcvState_Type=CiscoWanRcvState
_CwaChanEgressRcvState_Object=MibTableColumn
cwaChanEgressRcvState=_CwaChanEgressRcvState_Object((1,3,6,1,4,1,351,150,1,1,2,1,1,3),_CwaChanEgressRcvState_Type())
cwaChanEgressRcvState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanEgressRcvState.setStatus(_B)
_CwaChanIngressXmtState_Type=CiscoWanXmtState
_CwaChanIngressXmtState_Object=MibTableColumn
cwaChanIngressXmtState=_CwaChanIngressXmtState_Object((1,3,6,1,4,1,351,150,1,1,2,1,1,4),_CwaChanIngressXmtState_Type())
cwaChanIngressXmtState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanIngressXmtState.setStatus(_B)
_CwaChanIngressRcvState_Type=CiscoWanRcvState
_CwaChanIngressRcvState_Object=MibTableColumn
cwaChanIngressRcvState=_CwaChanIngressRcvState_Object((1,3,6,1,4,1,351,150,1,1,2,1,1,5),_CwaChanIngressRcvState_Type())
cwaChanIngressRcvState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanIngressRcvState.setStatus(_B)
_CwAtmChanTest_ObjectIdentity=ObjectIdentity
cwAtmChanTest=_CwAtmChanTest_ObjectIdentity((1,3,6,1,4,1,351,150,1,1,3))
_CwAtmChanTestTable_Object=MibTable
cwAtmChanTestTable=_CwAtmChanTestTable_Object((1,3,6,1,4,1,351,150,1,1,3,1))
if mibBuilder.loadTexts:cwAtmChanTestTable.setStatus(_B)
_CwAtmChanTestEntry_Object=MibTableRow
cwAtmChanTestEntry=_CwAtmChanTestEntry_Object((1,3,6,1,4,1,351,150,1,1,3,1,1))
cwAtmChanTestEntry.setIndexNames((0,_AC,_AD),(0,_A,_AE),(0,_A,_AF))
if mibBuilder.loadTexts:cwAtmChanTestEntry.setStatus(_B)
class _CwaChanTestType_Type(CiscoWanLpbkTypes):defaultValue=1
_CwaChanTestType_Type.__name__=_AT
_CwaChanTestType_Object=MibTableColumn
cwaChanTestType=_CwaChanTestType_Object((1,3,6,1,4,1,351,150,1,1,3,1,1,1),_CwaChanTestType_Type())
cwaChanTestType.setMaxAccess(_AK)
if mibBuilder.loadTexts:cwaChanTestType.setStatus(_B)
_CwaChanTestDir_Type=CiscoWanLpbkDir
_CwaChanTestDir_Object=MibTableColumn
cwaChanTestDir=_CwaChanTestDir_Object((1,3,6,1,4,1,351,150,1,1,3,1,1,2),_CwaChanTestDir_Type())
cwaChanTestDir.setMaxAccess(_AK)
if mibBuilder.loadTexts:cwaChanTestDir.setStatus(_B)
class _CwaChanTestIterations_Type(Unsigned32):defaultValue=1;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CwaChanTestIterations_Type.__name__=_D
_CwaChanTestIterations_Object=MibTableColumn
cwaChanTestIterations=_CwaChanTestIterations_Object((1,3,6,1,4,1,351,150,1,1,3,1,1,3),_CwaChanTestIterations_Type())
cwaChanTestIterations.setMaxAccess(_AK)
if mibBuilder.loadTexts:cwaChanTestIterations.setStatus(_B)
class _CwaChanTestState_Type(CiscoWanTestStatus):defaultValue=1
_CwaChanTestState_Type.__name__=_AU
_CwaChanTestState_Object=MibTableColumn
cwaChanTestState=_CwaChanTestState_Object((1,3,6,1,4,1,351,150,1,1,3,1,1,4),_CwaChanTestState_Type())
cwaChanTestState.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanTestState.setStatus(_B)
class _CwaChanTestRoundTripDelay_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,100000000))
_CwaChanTestRoundTripDelay_Type.__name__=_D
_CwaChanTestRoundTripDelay_Object=MibTableColumn
cwaChanTestRoundTripDelay=_CwaChanTestRoundTripDelay_Object((1,3,6,1,4,1,351,150,1,1,3,1,1,5),_CwaChanTestRoundTripDelay_Type())
cwaChanTestRoundTripDelay.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanTestRoundTripDelay.setStatus(_B)
if mibBuilder.loadTexts:cwaChanTestRoundTripDelay.setUnits(_J)
_CwAtmChanInformation_ObjectIdentity=ObjectIdentity
cwAtmChanInformation=_CwAtmChanInformation_ObjectIdentity((1,3,6,1,4,1,351,150,1,1,4))
_CwaChanNumVPCsInAlarm_Type=Unsigned32
_CwaChanNumVPCsInAlarm_Object=MibScalar
cwaChanNumVPCsInAlarm=_CwaChanNumVPCsInAlarm_Object((1,3,6,1,4,1,351,150,1,1,4,1),_CwaChanNumVPCsInAlarm_Type())
cwaChanNumVPCsInAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanNumVPCsInAlarm.setStatus(_B)
_CwaChanNumVCCsInAlarm_Type=Unsigned32
_CwaChanNumVCCsInAlarm_Object=MibScalar
cwaChanNumVCCsInAlarm=_CwaChanNumVCCsInAlarm_Object((1,3,6,1,4,1,351,150,1,1,4,2),_CwaChanNumVCCsInAlarm_Type())
cwaChanNumVCCsInAlarm.setMaxAccess(_E)
if mibBuilder.loadTexts:cwaChanNumVCCsInAlarm.setStatus(_B)
_CwGlobalChanDataGroup_ObjectIdentity=ObjectIdentity
cwGlobalChanDataGroup=_CwGlobalChanDataGroup_ObjectIdentity((1,3,6,1,4,1,351,150,1,1,5))
_CwGlobalChanDataTable_Object=MibTable
cwGlobalChanDataTable=_CwGlobalChanDataTable_Object((1,3,6,1,4,1,351,150,1,1,5,1))
if mibBuilder.loadTexts:cwGlobalChanDataTable.setStatus(_B)
_CwGlobalChanDataEntry_Object=MibTableRow
cwGlobalChanDataEntry=_CwGlobalChanDataEntry_Object((1,3,6,1,4,1,351,150,1,1,5,1,1))
cwGlobalChanDataEntry.setIndexNames((0,_A,_AV))
if mibBuilder.loadTexts:cwGlobalChanDataEntry.setStatus(_B)
class _CwSlotIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,429496729))
_CwSlotIndex_Type.__name__=_D
_CwSlotIndex_Object=MibTableColumn
cwSlotIndex=_CwSlotIndex_Object((1,3,6,1,4,1,351,150,1,1,5,1,1,1),_CwSlotIndex_Type())
cwSlotIndex.setMaxAccess(_AH)
if mibBuilder.loadTexts:cwSlotIndex.setStatus(_B)
class _CwChanGlobalTransactionId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_CwChanGlobalTransactionId_Type.__name__=_D
_CwChanGlobalTransactionId_Object=MibTableColumn
cwChanGlobalTransactionId=_CwChanGlobalTransactionId_Object((1,3,6,1,4,1,351,150,1,1,5,1,1,2),_CwChanGlobalTransactionId_Type())
cwChanGlobalTransactionId.setMaxAccess(_E)
if mibBuilder.loadTexts:cwChanGlobalTransactionId.setStatus(_B)
_CiscoWanAtmConnMIBConformance_ObjectIdentity=ObjectIdentity
ciscoWanAtmConnMIBConformance=_CiscoWanAtmConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,1,2))
_CiscoWanAtmConnMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoWanAtmConnMIBCompliances=_CiscoWanAtmConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,1,2,1))
_CiscoWanAtmConnMIBGroups_ObjectIdentity=ObjectIdentity
ciscoWanAtmConnMIBGroups=_CiscoWanAtmConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,1,2,2))
ciscoWanAtmConnChanMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,1,2,2,1))
ciscoWanAtmConnChanMIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_AW),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_AL),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_AM),(_A,_A4),(_A,_A5),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoWanAtmConnChanMIBGroup.setStatus(_G)
ciscoWanAtmConnStateGroup=ObjectGroup((1,3,6,1,4,1,351,150,1,2,2,2))
ciscoWanAtmConnStateGroup.setObjects(*((_A,_AX),(_A,_AY),(_A,_AZ),(_A,_Aa),(_A,_Ab)))
if mibBuilder.loadTexts:ciscoWanAtmConnStateGroup.setStatus(_B)
ciscoWanAtmConnChan2MIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,1,2,2,3))
ciscoWanAtmConnChan2MIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_AL),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_AM),(_A,_A4),(_A,_A5),(_A,_AG),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoWanAtmConnChan2MIBGroup.setStatus(_G)
ciscoWanAtmConnChan3MIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,1,2,2,4))
ciscoWanAtmConnChan3MIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_AG),(_A,_AN),(_A,_AO),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoWanAtmConnChan3MIBGroup.setStatus(_G)
ciscoWanAtmInformationGroup=ObjectGroup((1,3,6,1,4,1,351,150,1,2,2,5))
ciscoWanAtmInformationGroup.setObjects(*((_A,_Ac),(_A,_Ad)))
if mibBuilder.loadTexts:ciscoWanAtmInformationGroup.setStatus(_B)
ciscoWanAtmConnChan4MIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,1,2,2,6))
ciscoWanAtmConnChan4MIBGroup.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_U),(_A,_V),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0),(_A,_A1),(_A,_A2),(_A,_A3),(_A,_A4),(_A,_A5),(_A,_AG),(_A,_AN),(_A,_AO),(_A,_Ae),(_A,_Af),(_A,_Ag),(_A,_A6),(_A,_A7),(_A,_A8),(_A,_A9),(_A,_AA)))
if mibBuilder.loadTexts:ciscoWanAtmConnChan4MIBGroup.setStatus(_B)
ciscoWanConMIBGroup=ObjectGroup((1,3,6,1,4,1,351,150,1,2,2,7))
ciscoWanConMIBGroup.setObjects((_A,_Ah))
if mibBuilder.loadTexts:ciscoWanConMIBGroup.setStatus(_B)
ciscoWanAtmConnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,1,2,1,1))
ciscoWanAtmConnMIBCompliance.setObjects(*((_A,_Ai),(_A,_AB)))
if mibBuilder.loadTexts:ciscoWanAtmConnMIBCompliance.setStatus(_G)
ciscoWanAtmConnMIBCompliance2=ModuleCompliance((1,3,6,1,4,1,351,150,1,2,1,2))
ciscoWanAtmConnMIBCompliance2.setObjects(*((_A,_Aj),(_A,_AB)))
if mibBuilder.loadTexts:ciscoWanAtmConnMIBCompliance2.setStatus(_G)
ciscoWanAtmConnMIBCompliance3=ModuleCompliance((1,3,6,1,4,1,351,150,1,2,1,3))
ciscoWanAtmConnMIBCompliance3.setObjects(*((_A,_Ak),(_A,_AB),(_A,_AP)))
if mibBuilder.loadTexts:ciscoWanAtmConnMIBCompliance3.setStatus(_G)
ciscoWanAtmConnMIBCompliance4=ModuleCompliance((1,3,6,1,4,1,351,150,1,2,1,4))
ciscoWanAtmConnMIBCompliance4.setObjects(*((_A,_Al),(_A,_AB),(_A,_AP)))
if mibBuilder.loadTexts:ciscoWanAtmConnMIBCompliance4.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'CiscoAtmServiceCategory':CiscoAtmServiceCategory,_AT:CiscoWanLpbkTypes,'CiscoWanLpbkDir':CiscoWanLpbkDir,_AU:CiscoWanTestStatus,'CiscoWanOperStatus':CiscoWanOperStatus,'CiscoWanNsapAtmAddress':CiscoWanNsapAtmAddress,'CiscoWanAlarmState':CiscoWanAlarmState,'CiscoWanXmtState':CiscoWanXmtState,'CiscoWanRcvState':CiscoWanRcvState,_AR:CiscoWanERSConfg,_AJ:CiscoWanVSVDConfg,_AS:CiscoWanAisIW,'AbrRateFactors':AbrRateFactors,'ciscoWanAtmConnMIB':ciscoWanAtmConnMIB,'cwConnMibObjects':cwConnMibObjects,'cwAtmChanCnfg':cwAtmChanCnfg,'cwAtmChanCnfgTable':cwAtmChanCnfgTable,'cwAtmChanCnfgEntry':cwAtmChanCnfgEntry,_AE:cwaChanVpi,_AF:cwaChanVci,_K:cwaChanServiceCategory,_L:cwaChanVpcFlag,_P:cwaChanIdentifier,_O:cwaChanUploadCounter,_M:cwaChanStatsEnable,_N:cwaChanCCEnable,_Q:cwaChanLocalVpi,_R:cwaChanLocalVci,_S:cwaChanLocalNSAPAddr,_T:cwaChanRemoteVpi,_U:cwaChanRemoteVci,_V:cwaChanRemoteNSAPAddr,_W:cwaChanControllerId,_X:cwaChanRoutingMastership,_Y:cwaChanMaxCost,_Z:cwaChanReroute,_a:cwaChanFrameDiscard,_b:cwaChanOperStatus,_c:cwaChanPCR,_d:cwaChanMCR,_e:cwaChanSCR,_f:cwaChanCDV,_g:cwaChanCTD,_h:cwaChanMBS,_i:cwaChanCDVT,_j:cwaChanPercentUtil,_k:cwaChanRemotePCR,_l:cwaChanRemoteMCR,_m:cwaChanRemoteSCR,_n:cwaChanRemoteCDV,_o:cwaChanRemoteCTD,_p:cwaChanRemoteMBS,_AW:cwaChanRemoteCDVT,_q:cwaChanRemotePercentUtil,_r:cwaChanAbrICR,_s:cwaChanAbrADTF,_t:cwaChanAbrRDF,_u:cwaChanAbrRIF,_v:cwaChanAbrNRM,_w:cwaChanAbrTRM,_x:cwaChanAbrCDF,_y:cwaChanAbrFRTT,_z:cwaChanAbrTBE,_AL:cwaChanAbrERS,_A0:cwaChanAbrVSVDEnable,_A1:cwaChanRowStatus,_A2:cwaChanIntAbrVSVD,_A3:cwaChanExtAbrVSVD,_AM:cwaChanAisIWCapability,_A4:cwaChanCLR,_A5:cwaChanRemoteCLR,_AG:cwaChanOamSegEpEnable,_AN:cwaChanSlaveType,_AO:cwaChanRoutingPriority,_Ae:cwaChanP2MP,_Af:cwaChanPrefRouteId,_Ag:cwaChanDirectRoute,'cwAtmChanState':cwAtmChanState,'cwAtmChanStateTable':cwAtmChanStateTable,'cwAtmChanStateEntry':cwAtmChanStateEntry,_AX:cwaChanAlarmState,_AY:cwaChanEgressXmtState,_AZ:cwaChanEgressRcvState,_Aa:cwaChanIngressXmtState,_Ab:cwaChanIngressRcvState,'cwAtmChanTest':cwAtmChanTest,'cwAtmChanTestTable':cwAtmChanTestTable,'cwAtmChanTestEntry':cwAtmChanTestEntry,_A6:cwaChanTestType,_A7:cwaChanTestDir,_A8:cwaChanTestIterations,_A9:cwaChanTestState,_AA:cwaChanTestRoundTripDelay,'cwAtmChanInformation':cwAtmChanInformation,_Ac:cwaChanNumVPCsInAlarm,_Ad:cwaChanNumVCCsInAlarm,'cwGlobalChanDataGroup':cwGlobalChanDataGroup,'cwGlobalChanDataTable':cwGlobalChanDataTable,'cwGlobalChanDataEntry':cwGlobalChanDataEntry,_AV:cwSlotIndex,_Ah:cwChanGlobalTransactionId,'ciscoWanAtmConnMIBConformance':ciscoWanAtmConnMIBConformance,'ciscoWanAtmConnMIBCompliances':ciscoWanAtmConnMIBCompliances,'ciscoWanAtmConnMIBCompliance':ciscoWanAtmConnMIBCompliance,'ciscoWanAtmConnMIBCompliance2':ciscoWanAtmConnMIBCompliance2,'ciscoWanAtmConnMIBCompliance3':ciscoWanAtmConnMIBCompliance3,'ciscoWanAtmConnMIBCompliance4':ciscoWanAtmConnMIBCompliance4,'ciscoWanAtmConnMIBGroups':ciscoWanAtmConnMIBGroups,_Ai:ciscoWanAtmConnChanMIBGroup,_AB:ciscoWanAtmConnStateGroup,_Aj:ciscoWanAtmConnChan2MIBGroup,_Ak:ciscoWanAtmConnChan3MIBGroup,_AP:ciscoWanAtmInformationGroup,_Al:ciscoWanAtmConnChan4MIBGroup,'ciscoWanConMIBGroup':ciscoWanConMIBGroup})