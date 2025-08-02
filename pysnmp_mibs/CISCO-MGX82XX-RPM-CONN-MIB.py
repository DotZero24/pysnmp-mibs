_r='cmrConnConfGroup'
_q='rpmChanAbrRIF'
_p='rpmChanAbrRDF'
_o='rpmChanVirtualTemplate'
_n='rpmChanState'
_m='rpmChanOAMloopback'
_l='rpmChanInArpFreq'
_k='rpmChanEncapType'
_j='rpmChanBurstSize'
_i='rpmChanMidHigh'
_h='rpmChanMidLow'
_g='rpmChanRemotePercentUtil'
_f='rpmChanPercentUtil'
_e='rpmChanRemoteMCR'
_d='rpmChanMCR'
_c='rpmChanRemotePCR'
_b='rpmChanPCR'
_a='rpmChanRestrictTrkType'
_Z='rpmChanMaxCost'
_Y='rpmChanRtePriority'
_X='rpmChanMastership'
_W='rpmChanServiceType'
_V='rpmChanConnType'
_U='rpmChanType'
_T='rpmChanRemoteNsap'
_S='rpmChanRemoteVci'
_R='rpmChanRemoteVpi'
_Q='rpmChanLocalNsap'
_P='rpmChanLocalVci'
_O='rpmChanLocalVpi'
_N='rpmChanSubInterface'
_M='rpmChanVci'
_L='rpmChanVpi'
_K='rpmChanVcd'
_J='rpmChanRowStatus'
_I='rpmChanInterface'
_H='cells-per-second'
_G='unknown'
_F='rpmChanNum'
_E='rpmChanSlotNum'
_D='Integer32'
_C='read-only'
_B='CISCO-MGX82XX-RPM-CONN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rpmChanGrp,=mibBuilder.importSymbols('BASIS-MIB','rpmChanGrp')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxRpmConnMIB=ModuleIdentity((1,3,6,1,4,1,351,150,62))
if mibBuilder.loadTexts:ciscoMgx82xxRpmConnMIB.setRevisions(('2002-09-08 00:00',))
class RpmNsapAddress(TextualConvention,OctetString):status=_A;subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(20,20));fixedLength=20
_RpmChanGrpTable_Object=MibTable
rpmChanGrpTable=_RpmChanGrpTable_Object((1,3,6,1,4,1,351,110,5,2,10,1,1))
if mibBuilder.loadTexts:rpmChanGrpTable.setStatus(_A)
_RpmChanGrpEntry_Object=MibTableRow
rpmChanGrpEntry=_RpmChanGrpEntry_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1))
rpmChanGrpEntry.setIndexNames((0,_B,_E),(0,_B,_F))
if mibBuilder.loadTexts:rpmChanGrpEntry.setStatus(_A)
class _RpmChanSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,30))
_RpmChanSlotNum_Type.__name__=_D
_RpmChanSlotNum_Object=MibTableColumn
rpmChanSlotNum=_RpmChanSlotNum_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,1),_RpmChanSlotNum_Type())
rpmChanSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanSlotNum.setStatus(_A)
_RpmChanInterface_Type=Integer32
_RpmChanInterface_Object=MibTableColumn
rpmChanInterface=_RpmChanInterface_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,2),_RpmChanInterface_Type())
rpmChanInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanInterface.setStatus(_A)
class _RpmChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(16,4095))
_RpmChanNum_Type.__name__=_D
_RpmChanNum_Object=MibTableColumn
rpmChanNum=_RpmChanNum_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,3),_RpmChanNum_Type())
rpmChanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanNum.setStatus(_A)
class _RpmChanRowStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('add',1),('del',2),('mod',3)))
_RpmChanRowStatus_Type.__name__=_D
_RpmChanRowStatus_Object=MibTableColumn
rpmChanRowStatus=_RpmChanRowStatus_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,4),_RpmChanRowStatus_Type())
rpmChanRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRowStatus.setStatus(_A)
class _RpmChanVcd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_RpmChanVcd_Type.__name__=_D
_RpmChanVcd_Object=MibTableColumn
rpmChanVcd=_RpmChanVcd_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,5),_RpmChanVcd_Type())
rpmChanVcd.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanVcd.setStatus(_A)
class _RpmChanVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RpmChanVpi_Type.__name__=_D
_RpmChanVpi_Object=MibTableColumn
rpmChanVpi=_RpmChanVpi_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,6),_RpmChanVpi_Type())
rpmChanVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanVpi.setStatus(_A)
class _RpmChanVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpmChanVci_Type.__name__=_D
_RpmChanVci_Object=MibTableColumn
rpmChanVci=_RpmChanVci_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,7),_RpmChanVci_Type())
rpmChanVci.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanVci.setStatus(_A)
class _RpmChanSubInterface_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_RpmChanSubInterface_Type.__name__=_D
_RpmChanSubInterface_Object=MibTableColumn
rpmChanSubInterface=_RpmChanSubInterface_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,8),_RpmChanSubInterface_Type())
rpmChanSubInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanSubInterface.setStatus(_A)
class _RpmChanLocalVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RpmChanLocalVpi_Type.__name__=_D
_RpmChanLocalVpi_Object=MibTableColumn
rpmChanLocalVpi=_RpmChanLocalVpi_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,9),_RpmChanLocalVpi_Type())
rpmChanLocalVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanLocalVpi.setStatus(_A)
class _RpmChanLocalVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpmChanLocalVci_Type.__name__=_D
_RpmChanLocalVci_Object=MibTableColumn
rpmChanLocalVci=_RpmChanLocalVci_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,10),_RpmChanLocalVci_Type())
rpmChanLocalVci.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanLocalVci.setStatus(_A)
_RpmChanLocalNsap_Type=RpmNsapAddress
_RpmChanLocalNsap_Object=MibTableColumn
rpmChanLocalNsap=_RpmChanLocalNsap_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,11),_RpmChanLocalNsap_Type())
rpmChanLocalNsap.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanLocalNsap.setStatus(_A)
class _RpmChanRemoteVpi_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_RpmChanRemoteVpi_Type.__name__=_D
_RpmChanRemoteVpi_Object=MibTableColumn
rpmChanRemoteVpi=_RpmChanRemoteVpi_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,12),_RpmChanRemoteVpi_Type())
rpmChanRemoteVpi.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRemoteVpi.setStatus(_A)
class _RpmChanRemoteVci_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpmChanRemoteVci_Type.__name__=_D
_RpmChanRemoteVci_Object=MibTableColumn
rpmChanRemoteVci=_RpmChanRemoteVci_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,13),_RpmChanRemoteVci_Type())
rpmChanRemoteVci.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRemoteVci.setStatus(_A)
_RpmChanRemoteNsap_Type=RpmNsapAddress
_RpmChanRemoteNsap_Object=MibTableColumn
rpmChanRemoteNsap=_RpmChanRemoteNsap_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,14),_RpmChanRemoteNsap_Type())
rpmChanRemoteNsap.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRemoteNsap.setStatus(_A)
class _RpmChanType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('svc',1),('pvc',2),('spvc',3)))
_RpmChanType_Type.__name__=_D
_RpmChanType_Object=MibTableColumn
rpmChanType=_RpmChanType_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,15),_RpmChanType_Type())
rpmChanType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanType.setStatus(_A)
class _RpmChanConnType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('vpc',1),('vcc',2)))
_RpmChanConnType_Type.__name__=_D
_RpmChanConnType_Object=MibTableColumn
rpmChanConnType=_RpmChanConnType_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,16),_RpmChanConnType_Type())
rpmChanConnType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanConnType.setStatus(_A)
class _RpmChanServiceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4,5,6,7)));namedValues=NamedValues(*(('cbr',1),('vbr',2),('ubr',4),('atfr',5),('abrstd',6),('abrfst',7)))
_RpmChanServiceType_Type.__name__=_D
_RpmChanServiceType_Object=MibTableColumn
rpmChanServiceType=_RpmChanServiceType_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,17),_RpmChanServiceType_Type())
rpmChanServiceType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanServiceType.setStatus(_A)
class _RpmChanMastership_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('master',1),('slave',2),(_G,3)))
_RpmChanMastership_Type.__name__=_D
_RpmChanMastership_Object=MibTableColumn
rpmChanMastership=_RpmChanMastership_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,18),_RpmChanMastership_Type())
rpmChanMastership.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanMastership.setStatus(_A)
class _RpmChanRtePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,15))
_RpmChanRtePriority_Type.__name__=_D
_RpmChanRtePriority_Object=MibTableColumn
rpmChanRtePriority=_RpmChanRtePriority_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,19),_RpmChanRtePriority_Type())
rpmChanRtePriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRtePriority.setStatus(_A)
class _RpmChanMaxCost_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_RpmChanMaxCost_Type.__name__=_D
_RpmChanMaxCost_Object=MibTableColumn
rpmChanMaxCost=_RpmChanMaxCost_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,20),_RpmChanMaxCost_Type())
rpmChanMaxCost.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanMaxCost.setStatus(_A)
class _RpmChanRestrictTrkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('noRestriction',1),('terrestrialTrunk',2),('satelliteTrunk',3)))
_RpmChanRestrictTrkType_Type.__name__=_D
_RpmChanRestrictTrkType_Object=MibTableColumn
rpmChanRestrictTrkType=_RpmChanRestrictTrkType_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,21),_RpmChanRestrictTrkType_Type())
rpmChanRestrictTrkType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRestrictTrkType.setStatus(_A)
class _RpmChanPCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,353208))
_RpmChanPCR_Type.__name__=_D
_RpmChanPCR_Object=MibTableColumn
rpmChanPCR=_RpmChanPCR_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,22),_RpmChanPCR_Type())
rpmChanPCR.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanPCR.setStatus(_A)
if mibBuilder.loadTexts:rpmChanPCR.setUnits(_H)
class _RpmChanRemotePCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,353208))
_RpmChanRemotePCR_Type.__name__=_D
_RpmChanRemotePCR_Object=MibTableColumn
rpmChanRemotePCR=_RpmChanRemotePCR_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,23),_RpmChanRemotePCR_Type())
rpmChanRemotePCR.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRemotePCR.setStatus(_A)
class _RpmChanMCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,353208))
_RpmChanMCR_Type.__name__=_D
_RpmChanMCR_Object=MibTableColumn
rpmChanMCR=_RpmChanMCR_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,24),_RpmChanMCR_Type())
rpmChanMCR.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanMCR.setStatus(_A)
if mibBuilder.loadTexts:rpmChanMCR.setUnits(_H)
class _RpmChanRemoteMCR_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,353208))
_RpmChanRemoteMCR_Type.__name__=_D
_RpmChanRemoteMCR_Object=MibTableColumn
rpmChanRemoteMCR=_RpmChanRemoteMCR_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,25),_RpmChanRemoteMCR_Type())
rpmChanRemoteMCR.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRemoteMCR.setStatus(_A)
class _RpmChanPercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RpmChanPercentUtil_Type.__name__=_D
_RpmChanPercentUtil_Object=MibTableColumn
rpmChanPercentUtil=_RpmChanPercentUtil_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,26),_RpmChanPercentUtil_Type())
rpmChanPercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanPercentUtil.setStatus(_A)
class _RpmChanRemotePercentUtil_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,100))
_RpmChanRemotePercentUtil_Type.__name__=_D
_RpmChanRemotePercentUtil_Object=MibTableColumn
rpmChanRemotePercentUtil=_RpmChanRemotePercentUtil_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,27),_RpmChanRemotePercentUtil_Type())
rpmChanRemotePercentUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanRemotePercentUtil.setStatus(_A)
class _RpmChanEncapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12)));namedValues=NamedValues(*(('aal5snap',1),('aal34smds',2),('aal5nlpid',3),('qsaal',4),('ilmi',5),('aal5muxXNS',6),('aal5muxIP',7),('aal5muxVINES',8),('aal5muxDECNET',9),('aal5muxNOVELL1',10),('ppp',11),(_G,12)))
_RpmChanEncapType_Type.__name__=_D
_RpmChanEncapType_Object=MibTableColumn
rpmChanEncapType=_RpmChanEncapType_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,28),_RpmChanEncapType_Type())
rpmChanEncapType.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanEncapType.setStatus(_A)
class _RpmChanMidLow_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_RpmChanMidLow_Type.__name__=_D
_RpmChanMidLow_Object=MibTableColumn
rpmChanMidLow=_RpmChanMidLow_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,29),_RpmChanMidLow_Type())
rpmChanMidLow.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanMidLow.setStatus(_A)
class _RpmChanMidHigh_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_RpmChanMidHigh_Type.__name__=_D
_RpmChanMidHigh_Object=MibTableColumn
rpmChanMidHigh=_RpmChanMidHigh_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,30),_RpmChanMidHigh_Type())
rpmChanMidHigh.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanMidHigh.setStatus(_A)
class _RpmChanBurstSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RpmChanBurstSize_Type.__name__=_D
_RpmChanBurstSize_Object=MibTableColumn
rpmChanBurstSize=_RpmChanBurstSize_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,31),_RpmChanBurstSize_Type())
rpmChanBurstSize.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanBurstSize.setStatus(_A)
class _RpmChanInArpFreq_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_RpmChanInArpFreq_Type.__name__=_D
_RpmChanInArpFreq_Object=MibTableColumn
rpmChanInArpFreq=_RpmChanInArpFreq_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,32),_RpmChanInArpFreq_Type())
rpmChanInArpFreq.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanInArpFreq.setStatus(_A)
if mibBuilder.loadTexts:rpmChanInArpFreq.setUnits('minutes')
class _RpmChanOAMloopback_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_RpmChanOAMloopback_Type.__name__=_D
_RpmChanOAMloopback_Object=MibTableColumn
rpmChanOAMloopback=_RpmChanOAMloopback_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,33),_RpmChanOAMloopback_Type())
rpmChanOAMloopback.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanOAMloopback.setStatus(_A)
if mibBuilder.loadTexts:rpmChanOAMloopback.setUnits('seconds')
class _RpmChanState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('notConfigured',1),('active',2),('failed',3)))
_RpmChanState_Type.__name__=_D
_RpmChanState_Object=MibTableColumn
rpmChanState=_RpmChanState_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,34),_RpmChanState_Type())
rpmChanState.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanState.setStatus(_A)
_RpmChanVirtualTemplate_Type=Integer32
_RpmChanVirtualTemplate_Object=MibTableColumn
rpmChanVirtualTemplate=_RpmChanVirtualTemplate_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,35),_RpmChanVirtualTemplate_Type())
rpmChanVirtualTemplate.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanVirtualTemplate.setStatus(_A)
_RpmChanAbrRDF_Type=Integer32
_RpmChanAbrRDF_Object=MibTableColumn
rpmChanAbrRDF=_RpmChanAbrRDF_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,36),_RpmChanAbrRDF_Type())
rpmChanAbrRDF.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanAbrRDF.setStatus(_A)
_RpmChanAbrRIF_Type=Integer32
_RpmChanAbrRIF_Object=MibTableColumn
rpmChanAbrRIF=_RpmChanAbrRIF_Object((1,3,6,1,4,1,351,110,5,2,10,1,1,1,37),_RpmChanAbrRIF_Type())
rpmChanAbrRIF.setMaxAccess(_C)
if mibBuilder.loadTexts:rpmChanAbrRIF.setStatus(_A)
_CmrConnMIBConformance_ObjectIdentity=ObjectIdentity
cmrConnMIBConformance=_CmrConnMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,62,2))
_CmrConnMIBCompliances_ObjectIdentity=ObjectIdentity
cmrConnMIBCompliances=_CmrConnMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,62,2,1))
_CmrConnMIBGroups_ObjectIdentity=ObjectIdentity
cmrConnMIBGroups=_CmrConnMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,62,2,2))
cmrConnConfGroup=ObjectGroup((1,3,6,1,4,1,351,150,62,2,2,1))
cmrConnConfGroup.setObjects(*((_B,_E),(_B,_I),(_B,_F),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p),(_B,_q)))
if mibBuilder.loadTexts:cmrConnConfGroup.setStatus(_A)
cmrConnMIBCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,62,2,1,1))
cmrConnMIBCompliance.setObjects((_B,_r))
if mibBuilder.loadTexts:cmrConnMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'RpmNsapAddress':RpmNsapAddress,'rpmChanGrpTable':rpmChanGrpTable,'rpmChanGrpEntry':rpmChanGrpEntry,_E:rpmChanSlotNum,_I:rpmChanInterface,_F:rpmChanNum,_J:rpmChanRowStatus,_K:rpmChanVcd,_L:rpmChanVpi,_M:rpmChanVci,_N:rpmChanSubInterface,_O:rpmChanLocalVpi,_P:rpmChanLocalVci,_Q:rpmChanLocalNsap,_R:rpmChanRemoteVpi,_S:rpmChanRemoteVci,_T:rpmChanRemoteNsap,_U:rpmChanType,_V:rpmChanConnType,_W:rpmChanServiceType,_X:rpmChanMastership,_Y:rpmChanRtePriority,_Z:rpmChanMaxCost,_a:rpmChanRestrictTrkType,_b:rpmChanPCR,_c:rpmChanRemotePCR,_d:rpmChanMCR,_e:rpmChanRemoteMCR,_f:rpmChanPercentUtil,_g:rpmChanRemotePercentUtil,_k:rpmChanEncapType,_h:rpmChanMidLow,_i:rpmChanMidHigh,_j:rpmChanBurstSize,_l:rpmChanInArpFreq,_m:rpmChanOAMloopback,_n:rpmChanState,_o:rpmChanVirtualTemplate,_p:rpmChanAbrRDF,_q:rpmChanAbrRIF,'ciscoMgx82xxRpmConnMIB':ciscoMgx82xxRpmConnMIB,'cmrConnMIBConformance':cmrConnMIBConformance,'cmrConnMIBCompliances':cmrConnMIBCompliances,'cmrConnMIBCompliance':cmrConnMIBCompliance,'cmrConnMIBGroups':cmrConnMIBGroups,_r:cmrConnConfGroup})