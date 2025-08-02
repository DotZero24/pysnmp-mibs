_G='ifStaPortPortIndex'
_F='ifStaPortSlotIndex'
_E='ifStaSlotIndex'
_D='NTNTECH-INTERFACE-MODULE-STATUS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
NtnCounter32,NtnDisplayString,NtnGauge32,NtnMacAddress,NtnTimeTicks,ntntechInterfaceModule=mibBuilder.importSymbols('NTNTECH-ROOT-MIB','NtnCounter32','NtnDisplayString','NtnGauge32','NtnMacAddress','NtnTimeTicks','ntntechInterfaceModule')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntntechInterfaceModuleStatusMIB=ModuleIdentity((1,3,6,1,4,1,8059,1,2,2))
if mibBuilder.loadTexts:ntntechInterfaceModuleStatusMIB.setRevisions(('1902-06-17 03:05','1902-08-13 11:03','1902-08-28 10:48','1902-09-27 08:11','1902-10-22 02:00','1903-09-30 10:43','1904-03-15 10:00','1904-04-27 10:48','1904-10-11 09:39','1904-11-17 10:04'))
_IfModStaMIBObjects_ObjectIdentity=ObjectIdentity
ifModStaMIBObjects=_IfModStaMIBObjects_ObjectIdentity((1,3,6,1,4,1,8059,1,2,2,1))
_IfModStaValues_ObjectIdentity=ObjectIdentity
ifModStaValues=_IfModStaValues_ObjectIdentity((1,3,6,1,4,1,8059,1,2,2,1,1))
_ValInterface_ObjectIdentity=ObjectIdentity
valInterface=_ValInterface_ObjectIdentity((1,3,6,1,4,1,8059,1,2,2,1,1,1))
class _IfStaCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,12))
_IfStaCount_Type.__name__=_C
_IfStaCount_Object=MibScalar
ifStaCount=_IfStaCount_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,1),_IfStaCount_Type())
ifStaCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaCount.setStatus(_A)
_IfStaTable_Object=MibTable
ifStaTable=_IfStaTable_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,2))
if mibBuilder.loadTexts:ifStaTable.setStatus(_A)
_IfStaEntry_Object=MibTableRow
ifStaEntry=_IfStaEntry_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,2,1))
ifStaEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ifStaEntry.setStatus(_A)
class _IfStaSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfStaSlotIndex_Type.__name__=_C
_IfStaSlotIndex_Object=MibTableColumn
ifStaSlotIndex=_IfStaSlotIndex_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,2,1,1),_IfStaSlotIndex_Type())
ifStaSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaSlotIndex.setStatus(_A)
class _IfStaType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,130,131,135)));namedValues=NamedValues(*(('iam144p12',1),('sam1000p12',2),('tam1500p12',3),('sam2000p12',4),('eam2000p12',5),('sim2000p24',6),('smD2000p12',7),('smD2000Qp12',8),('sam2000Qp12',9),('aam8000p12',10),('amD8000p12',11),('sam2000Dp12',12),('sam2000DQp12',13),('sam2000Gp12',14),('sne2040',14),('sam2000Vp12',15),('sam2000QVp12',16),('sam2000GVp12',17),('sim2000p12',18),('smD2000Gp12',19),('sim2000Vp24',20),('sim2000Vp12',21),('suD2011p12T',22),('suD2011p12E',23),('suD2003p12T',24),('suD2003p12E',25),('suD2011p6T',26),('suD2011p6E',27),('suD2002p6T',28),('suD2002p6E',29),('aam8000p24',30),('tim1500p12',31),('eim2000p12',32),('tim1500p24',33),('eim2000p24',34),('aim24000p48',35),('smD2000p24',130),('auD8000p12',131),('ane8420',135)))
_IfStaType_Type.__name__=_C
_IfStaType_Object=MibTableColumn
ifStaType=_IfStaType_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,2,1,2),_IfStaType_Type())
ifStaType.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaType.setStatus(_A)
_IfStaFirmwareRev_Type=NtnDisplayString
_IfStaFirmwareRev_Object=MibTableColumn
ifStaFirmwareRev=_IfStaFirmwareRev_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,2,1,3),_IfStaFirmwareRev_Type())
ifStaFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaFirmwareRev.setStatus(_A)
_IfStaPortTable_Object=MibTable
ifStaPortTable=_IfStaPortTable_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3))
if mibBuilder.loadTexts:ifStaPortTable.setStatus(_A)
_IfStaPortEntry_Object=MibTableRow
ifStaPortEntry=_IfStaPortEntry_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1))
ifStaPortEntry.setIndexNames((0,_D,_F),(0,_D,_G))
if mibBuilder.loadTexts:ifStaPortEntry.setStatus(_A)
class _IfStaPortSlotIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,12))
_IfStaPortSlotIndex_Type.__name__=_C
_IfStaPortSlotIndex_Object=MibTableColumn
ifStaPortSlotIndex=_IfStaPortSlotIndex_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,1),_IfStaPortSlotIndex_Type())
ifStaPortSlotIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortSlotIndex.setStatus(_A)
class _IfStaPortPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,48))
_IfStaPortPortIndex_Type.__name__=_C
_IfStaPortPortIndex_Object=MibTableColumn
ifStaPortPortIndex=_IfStaPortPortIndex_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,2),_IfStaPortPortIndex_Type())
ifStaPortPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortPortIndex.setStatus(_A)
_IfStaPortFirmwareRev_Type=NtnDisplayString
_IfStaPortFirmwareRev_Object=MibTableColumn
ifStaPortFirmwareRev=_IfStaPortFirmwareRev_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,3),_IfStaPortFirmwareRev_Type())
ifStaPortFirmwareRev.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortFirmwareRev.setStatus(_A)
class _IfStaPortLinkState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('linkup',1),('linkdown',2),('linkloopback',3),('linkdefect',4),('linkdisabled',5)))
_IfStaPortLinkState_Type.__name__=_C
_IfStaPortLinkState_Object=MibTableColumn
ifStaPortLinkState=_IfStaPortLinkState_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,4),_IfStaPortLinkState_Type())
ifStaPortLinkState.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortLinkState.setStatus(_A)
_IfStaPortRxWanNUCastUtil_Type=NtnCounter32
_IfStaPortRxWanNUCastUtil_Object=MibTableColumn
ifStaPortRxWanNUCastUtil=_IfStaPortRxWanNUCastUtil_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,5),_IfStaPortRxWanNUCastUtil_Type())
ifStaPortRxWanNUCastUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanNUCastUtil.setStatus(_A)
_IfStaPortRxWanNUCastRate_Type=NtnGauge32
_IfStaPortRxWanNUCastRate_Object=MibTableColumn
ifStaPortRxWanNUCastRate=_IfStaPortRxWanNUCastRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,6),_IfStaPortRxWanNUCastRate_Type())
ifStaPortRxWanNUCastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanNUCastRate.setStatus(_A)
_IfStaPortRxWanNUCastMaxRate_Type=NtnGauge32
_IfStaPortRxWanNUCastMaxRate_Object=MibTableColumn
ifStaPortRxWanNUCastMaxRate=_IfStaPortRxWanNUCastMaxRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,7),_IfStaPortRxWanNUCastMaxRate_Type())
ifStaPortRxWanNUCastMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanNUCastMaxRate.setStatus(_A)
_IfStaPortRxWanNUCastAveRate_Type=NtnGauge32
_IfStaPortRxWanNUCastAveRate_Object=MibTableColumn
ifStaPortRxWanNUCastAveRate=_IfStaPortRxWanNUCastAveRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,8),_IfStaPortRxWanNUCastAveRate_Type())
ifStaPortRxWanNUCastAveRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanNUCastAveRate.setStatus(_A)
_IfStaPortTxWanNUCastUtil_Type=NtnCounter32
_IfStaPortTxWanNUCastUtil_Object=MibTableColumn
ifStaPortTxWanNUCastUtil=_IfStaPortTxWanNUCastUtil_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,9),_IfStaPortTxWanNUCastUtil_Type())
ifStaPortTxWanNUCastUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanNUCastUtil.setStatus(_A)
_IfStaPortTxWanNUCastRate_Type=NtnGauge32
_IfStaPortTxWanNUCastRate_Object=MibTableColumn
ifStaPortTxWanNUCastRate=_IfStaPortTxWanNUCastRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,10),_IfStaPortTxWanNUCastRate_Type())
ifStaPortTxWanNUCastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanNUCastRate.setStatus(_A)
_IfStaPortTxWanNUCastMaxRate_Type=NtnGauge32
_IfStaPortTxWanNUCastMaxRate_Object=MibTableColumn
ifStaPortTxWanNUCastMaxRate=_IfStaPortTxWanNUCastMaxRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,11),_IfStaPortTxWanNUCastMaxRate_Type())
ifStaPortTxWanNUCastMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanNUCastMaxRate.setStatus(_A)
_IfStaPortTxWanNUCastAveRate_Type=NtnGauge32
_IfStaPortTxWanNUCastAveRate_Object=MibTableColumn
ifStaPortTxWanNUCastAveRate=_IfStaPortTxWanNUCastAveRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,12),_IfStaPortTxWanNUCastAveRate_Type())
ifStaPortTxWanNUCastAveRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanNUCastAveRate.setStatus(_A)
_IfStaPortRxWanUCastUtil_Type=NtnCounter32
_IfStaPortRxWanUCastUtil_Object=MibTableColumn
ifStaPortRxWanUCastUtil=_IfStaPortRxWanUCastUtil_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,13),_IfStaPortRxWanUCastUtil_Type())
ifStaPortRxWanUCastUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanUCastUtil.setStatus(_A)
_IfStaPortRxWanUCastRate_Type=NtnGauge32
_IfStaPortRxWanUCastRate_Object=MibTableColumn
ifStaPortRxWanUCastRate=_IfStaPortRxWanUCastRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,14),_IfStaPortRxWanUCastRate_Type())
ifStaPortRxWanUCastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanUCastRate.setStatus(_A)
_IfStaPortRxWanUCastMaxRate_Type=NtnGauge32
_IfStaPortRxWanUCastMaxRate_Object=MibTableColumn
ifStaPortRxWanUCastMaxRate=_IfStaPortRxWanUCastMaxRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,15),_IfStaPortRxWanUCastMaxRate_Type())
ifStaPortRxWanUCastMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanUCastMaxRate.setStatus(_A)
_IfStaPortRxWanUCastAveRate_Type=NtnGauge32
_IfStaPortRxWanUCastAveRate_Object=MibTableColumn
ifStaPortRxWanUCastAveRate=_IfStaPortRxWanUCastAveRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,16),_IfStaPortRxWanUCastAveRate_Type())
ifStaPortRxWanUCastAveRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortRxWanUCastAveRate.setStatus(_A)
_IfStaPortTxWanUCastUtil_Type=NtnCounter32
_IfStaPortTxWanUCastUtil_Object=MibTableColumn
ifStaPortTxWanUCastUtil=_IfStaPortTxWanUCastUtil_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,17),_IfStaPortTxWanUCastUtil_Type())
ifStaPortTxWanUCastUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanUCastUtil.setStatus(_A)
_IfStaPortTxWanUCastRate_Type=NtnGauge32
_IfStaPortTxWanUCastRate_Object=MibTableColumn
ifStaPortTxWanUCastRate=_IfStaPortTxWanUCastRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,18),_IfStaPortTxWanUCastRate_Type())
ifStaPortTxWanUCastRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanUCastRate.setStatus(_A)
_IfStaPortTxWanUCastMaxRate_Type=NtnGauge32
_IfStaPortTxWanUCastMaxRate_Object=MibTableColumn
ifStaPortTxWanUCastMaxRate=_IfStaPortTxWanUCastMaxRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,19),_IfStaPortTxWanUCastMaxRate_Type())
ifStaPortTxWanUCastMaxRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanUCastMaxRate.setStatus(_A)
_IfStaPortTxWanUCastAveRate_Type=NtnGauge32
_IfStaPortTxWanUCastAveRate_Object=MibTableColumn
ifStaPortTxWanUCastAveRate=_IfStaPortTxWanUCastAveRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,20),_IfStaPortTxWanUCastAveRate_Type())
ifStaPortTxWanUCastAveRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTxWanUCastAveRate.setStatus(_A)
_IfStaPortTotRxWanPercentUtil_Type=NtnCounter32
_IfStaPortTotRxWanPercentUtil_Object=MibTableColumn
ifStaPortTotRxWanPercentUtil=_IfStaPortTotRxWanPercentUtil_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,21),_IfStaPortTotRxWanPercentUtil_Type())
ifStaPortTotRxWanPercentUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTotRxWanPercentUtil.setStatus(_A)
_IfStaPortTotRxWanRate_Type=NtnGauge32
_IfStaPortTotRxWanRate_Object=MibTableColumn
ifStaPortTotRxWanRate=_IfStaPortTotRxWanRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,22),_IfStaPortTotRxWanRate_Type())
ifStaPortTotRxWanRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTotRxWanRate.setStatus(_A)
_IfStaPortTotTxWanPercentUtil_Type=NtnCounter32
_IfStaPortTotTxWanPercentUtil_Object=MibTableColumn
ifStaPortTotTxWanPercentUtil=_IfStaPortTotTxWanPercentUtil_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,23),_IfStaPortTotTxWanPercentUtil_Type())
ifStaPortTotTxWanPercentUtil.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTotTxWanPercentUtil.setStatus(_A)
_IfStaPortTotTxWanRate_Type=NtnGauge32
_IfStaPortTotTxWanRate_Object=MibTableColumn
ifStaPortTotTxWanRate=_IfStaPortTotTxWanRate_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,24),_IfStaPortTotTxWanRate_Type())
ifStaPortTotTxWanRate.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTotTxWanRate.setStatus(_A)
_IfStaPortTotUpTime_Type=NtnTimeTicks
_IfStaPortTotUpTime_Object=MibTableColumn
ifStaPortTotUpTime=_IfStaPortTotUpTime_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,25),_IfStaPortTotUpTime_Type())
ifStaPortTotUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTotUpTime.setStatus(_A)
_IfStaPortTotDwnTime_Type=NtnTimeTicks
_IfStaPortTotDwnTime_Object=MibTableColumn
ifStaPortTotDwnTime=_IfStaPortTotDwnTime_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,26),_IfStaPortTotDwnTime_Type())
ifStaPortTotDwnTime.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaPortTotDwnTime.setStatus(_A)
_IfStaUCastTxPkt_Type=NtnCounter32
_IfStaUCastTxPkt_Object=MibTableColumn
ifStaUCastTxPkt=_IfStaUCastTxPkt_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,27),_IfStaUCastTxPkt_Type())
ifStaUCastTxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaUCastTxPkt.setStatus(_A)
_IfStaUCastRxPkt_Type=NtnCounter32
_IfStaUCastRxPkt_Object=MibTableColumn
ifStaUCastRxPkt=_IfStaUCastRxPkt_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,28),_IfStaUCastRxPkt_Type())
ifStaUCastRxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaUCastRxPkt.setStatus(_A)
_IfStaNUCastTxPkt_Type=NtnCounter32
_IfStaNUCastTxPkt_Object=MibTableColumn
ifStaNUCastTxPkt=_IfStaNUCastTxPkt_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,29),_IfStaNUCastTxPkt_Type())
ifStaNUCastTxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaNUCastTxPkt.setStatus(_A)
_IfStaNUCastRxPkt_Type=NtnCounter32
_IfStaNUCastRxPkt_Object=MibTableColumn
ifStaNUCastRxPkt=_IfStaNUCastRxPkt_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,30),_IfStaNUCastRxPkt_Type())
ifStaNUCastRxPkt.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaNUCastRxPkt.setStatus(_A)
class _IfStaNetworkLoopCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IfStaNetworkLoopCount_Type.__name__=_C
_IfStaNetworkLoopCount_Object=MibTableColumn
ifStaNetworkLoopCount=_IfStaNetworkLoopCount_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,31),_IfStaNetworkLoopCount_Type())
ifStaNetworkLoopCount.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaNetworkLoopCount.setStatus(_A)
_IfStaLastMacCausingLoop_Type=NtnMacAddress
_IfStaLastMacCausingLoop_Object=MibTableColumn
ifStaLastMacCausingLoop=_IfStaLastMacCausingLoop_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,32),_IfStaLastMacCausingLoop_Type())
ifStaLastMacCausingLoop.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaLastMacCausingLoop.setStatus(_A)
class _IfStaLastMacSrcPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IfStaLastMacSrcPort_Type.__name__=_C
_IfStaLastMacSrcPort_Object=MibTableColumn
ifStaLastMacSrcPort=_IfStaLastMacSrcPort_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,33),_IfStaLastMacSrcPort_Type())
ifStaLastMacSrcPort.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaLastMacSrcPort.setStatus(_A)
class _IfStaLoopBondedGroupPortList_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IfStaLoopBondedGroupPortList_Type.__name__=_C
_IfStaLoopBondedGroupPortList_Object=MibTableColumn
ifStaLoopBondedGroupPortList=_IfStaLoopBondedGroupPortList_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,34),_IfStaLoopBondedGroupPortList_Type())
ifStaLoopBondedGroupPortList.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaLoopBondedGroupPortList.setStatus(_A)
class _IfStaLoopBondedGroupID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_IfStaLoopBondedGroupID_Type.__name__=_C
_IfStaLoopBondedGroupID_Object=MibTableColumn
ifStaLoopBondedGroupID=_IfStaLoopBondedGroupID_Object((1,3,6,1,4,1,8059,1,2,2,1,1,1,3,1,35),_IfStaLoopBondedGroupID_Type())
ifStaLoopBondedGroupID.setMaxAccess(_B)
if mibBuilder.loadTexts:ifStaLoopBondedGroupID.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'ntntechInterfaceModuleStatusMIB':ntntechInterfaceModuleStatusMIB,'ifModStaMIBObjects':ifModStaMIBObjects,'ifModStaValues':ifModStaValues,'valInterface':valInterface,'ifStaCount':ifStaCount,'ifStaTable':ifStaTable,'ifStaEntry':ifStaEntry,_E:ifStaSlotIndex,'ifStaType':ifStaType,'ifStaFirmwareRev':ifStaFirmwareRev,'ifStaPortTable':ifStaPortTable,'ifStaPortEntry':ifStaPortEntry,_F:ifStaPortSlotIndex,_G:ifStaPortPortIndex,'ifStaPortFirmwareRev':ifStaPortFirmwareRev,'ifStaPortLinkState':ifStaPortLinkState,'ifStaPortRxWanNUCastUtil':ifStaPortRxWanNUCastUtil,'ifStaPortRxWanNUCastRate':ifStaPortRxWanNUCastRate,'ifStaPortRxWanNUCastMaxRate':ifStaPortRxWanNUCastMaxRate,'ifStaPortRxWanNUCastAveRate':ifStaPortRxWanNUCastAveRate,'ifStaPortTxWanNUCastUtil':ifStaPortTxWanNUCastUtil,'ifStaPortTxWanNUCastRate':ifStaPortTxWanNUCastRate,'ifStaPortTxWanNUCastMaxRate':ifStaPortTxWanNUCastMaxRate,'ifStaPortTxWanNUCastAveRate':ifStaPortTxWanNUCastAveRate,'ifStaPortRxWanUCastUtil':ifStaPortRxWanUCastUtil,'ifStaPortRxWanUCastRate':ifStaPortRxWanUCastRate,'ifStaPortRxWanUCastMaxRate':ifStaPortRxWanUCastMaxRate,'ifStaPortRxWanUCastAveRate':ifStaPortRxWanUCastAveRate,'ifStaPortTxWanUCastUtil':ifStaPortTxWanUCastUtil,'ifStaPortTxWanUCastRate':ifStaPortTxWanUCastRate,'ifStaPortTxWanUCastMaxRate':ifStaPortTxWanUCastMaxRate,'ifStaPortTxWanUCastAveRate':ifStaPortTxWanUCastAveRate,'ifStaPortTotRxWanPercentUtil':ifStaPortTotRxWanPercentUtil,'ifStaPortTotRxWanRate':ifStaPortTotRxWanRate,'ifStaPortTotTxWanPercentUtil':ifStaPortTotTxWanPercentUtil,'ifStaPortTotTxWanRate':ifStaPortTotTxWanRate,'ifStaPortTotUpTime':ifStaPortTotUpTime,'ifStaPortTotDwnTime':ifStaPortTotDwnTime,'ifStaUCastTxPkt':ifStaUCastTxPkt,'ifStaUCastRxPkt':ifStaUCastRxPkt,'ifStaNUCastTxPkt':ifStaNUCastTxPkt,'ifStaNUCastRxPkt':ifStaNUCastRxPkt,'ifStaNetworkLoopCount':ifStaNetworkLoopCount,'ifStaLastMacCausingLoop':ifStaLastMacCausingLoop,'ifStaLastMacSrcPort':ifStaLastMacSrcPort,'ifStaLoopBondedGroupPortList':ifStaLoopBondedGroupPortList,'ifStaLoopBondedGroupID':ifStaLoopBondedGroupID})