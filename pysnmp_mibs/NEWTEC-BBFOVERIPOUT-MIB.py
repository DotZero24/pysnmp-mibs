_h='ntcBbfOIpOutConfGrpV1Standard'
_g='ntcBbfOIpOutMonInvalPadd'
_f='ntcBbfOIpOutMonInvalCrc8'
_e='ntcBbfOIpOutMonDestBbfDropCount'
_d='ntcBbfOIpOutMonDestBbfOutCount'
_c='ntcBbfOIpOutMonDestBbfInCount'
_b='ntcBbfOIpOutMonDestBitRate'
_a='ntcBbfOIpOutMonBbfDropCount'
_Z='ntcBbfOIpOutMonBbfOutCount'
_Y='ntcBbfOIpOutMonBbfInCount'
_X='ntcBbfOIpOutMonOutputBbfBitRate'
_W='ntcBbfOIpOutMonReset'
_V='ntcBbfOIpOutEncapProt'
_U='ntcBbfOIpOutPassInvalidFrames'
_T='ntcBbfOIpOutDestinationUdpPort'
_S='ntcBbfOIpOutDestinationIpAddress'
_R='ntcBbfOIpOutBbfOutEnable'
_Q='ntcBbfOIpOutOutputSelection'
_P='ntcBbfOIpOutEnable'
_O='ntcBbfOIpOutMonInvalFramDemodId'
_N='ntcBbfOIpOutMonDestDemodId'
_M='ntcBbfOIpOutDestinationsDemodId'
_L='Unsigned32'
_K='not-accessible'
_J='demod3'
_I='demod2'
_H='demod1'
_G='NtcEnable'
_F='Integer32'
_E='frames'
_D='read-write'
_C='read-only'
_B='NEWTEC-BBFOVERIPOUT-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ntcFunction,=mibBuilder.importSymbols('NEWTEC-MAIN-MIB','ntcFunction')
NtcEnable,=mibBuilder.importSymbols('NEWTEC-TC-MIB',_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ntcBbfOverIpOut=ModuleIdentity((1,3,6,1,4,1,5835,5,2,1300))
if mibBuilder.loadTexts:ntcBbfOverIpOut.setRevisions(('2018-02-02 09:00','2017-10-16 12:00','2015-04-13 07:00','2013-05-22 06:00','2013-01-08 12:00'))
_NtcBbfOIpOutObjects_ObjectIdentity=ObjectIdentity
ntcBbfOIpOutObjects=_NtcBbfOIpOutObjects_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1300,1))
if mibBuilder.loadTexts:ntcBbfOIpOutObjects.setStatus(_A)
class _NtcBbfOIpOutEnable_Type(NtcEnable):defaultValue=0
_NtcBbfOIpOutEnable_Type.__name__=_G
_NtcBbfOIpOutEnable_Object=MibScalar
ntcBbfOIpOutEnable=_NtcBbfOIpOutEnable_Object((1,3,6,1,4,1,5835,5,2,1300,1,1),_NtcBbfOIpOutEnable_Type())
ntcBbfOIpOutEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutEnable.setStatus(_A)
class _NtcBbfOIpOutOutputSelection_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('data1',1),('data2',2),('data',3),('sat1',4),('sat2',5),('sat',6)))
_NtcBbfOIpOutOutputSelection_Type.__name__=_F
_NtcBbfOIpOutOutputSelection_Object=MibScalar
ntcBbfOIpOutOutputSelection=_NtcBbfOIpOutOutputSelection_Object((1,3,6,1,4,1,5835,5,2,1300,1,2),_NtcBbfOIpOutOutputSelection_Type())
ntcBbfOIpOutOutputSelection.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutOutputSelection.setStatus(_A)
_NtcBbfOIpOutDestinationsTable_Object=MibTable
ntcBbfOIpOutDestinationsTable=_NtcBbfOIpOutDestinationsTable_Object((1,3,6,1,4,1,5835,5,2,1300,1,3))
if mibBuilder.loadTexts:ntcBbfOIpOutDestinationsTable.setStatus(_A)
_NtcBbfOIpOutDestinationsEntry_Object=MibTableRow
ntcBbfOIpOutDestinationsEntry=_NtcBbfOIpOutDestinationsEntry_Object((1,3,6,1,4,1,5835,5,2,1300,1,3,1))
ntcBbfOIpOutDestinationsEntry.setIndexNames((0,_B,_M))
if mibBuilder.loadTexts:ntcBbfOIpOutDestinationsEntry.setStatus(_A)
class _NtcBbfOIpOutDestinationsDemodId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_NtcBbfOIpOutDestinationsDemodId_Type.__name__=_F
_NtcBbfOIpOutDestinationsDemodId_Object=MibTableColumn
ntcBbfOIpOutDestinationsDemodId=_NtcBbfOIpOutDestinationsDemodId_Object((1,3,6,1,4,1,5835,5,2,1300,1,3,1,1),_NtcBbfOIpOutDestinationsDemodId_Type())
ntcBbfOIpOutDestinationsDemodId.setMaxAccess(_K)
if mibBuilder.loadTexts:ntcBbfOIpOutDestinationsDemodId.setStatus(_A)
class _NtcBbfOIpOutBbfOutEnable_Type(NtcEnable):defaultValue=0
_NtcBbfOIpOutBbfOutEnable_Type.__name__=_G
_NtcBbfOIpOutBbfOutEnable_Object=MibTableColumn
ntcBbfOIpOutBbfOutEnable=_NtcBbfOIpOutBbfOutEnable_Object((1,3,6,1,4,1,5835,5,2,1300,1,3,1,2),_NtcBbfOIpOutBbfOutEnable_Type())
ntcBbfOIpOutBbfOutEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutBbfOutEnable.setStatus(_A)
_NtcBbfOIpOutDestinationIpAddress_Type=IpAddress
_NtcBbfOIpOutDestinationIpAddress_Object=MibTableColumn
ntcBbfOIpOutDestinationIpAddress=_NtcBbfOIpOutDestinationIpAddress_Object((1,3,6,1,4,1,5835,5,2,1300,1,3,1,3),_NtcBbfOIpOutDestinationIpAddress_Type())
ntcBbfOIpOutDestinationIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutDestinationIpAddress.setStatus(_A)
class _NtcBbfOIpOutDestinationUdpPort_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_NtcBbfOIpOutDestinationUdpPort_Type.__name__=_L
_NtcBbfOIpOutDestinationUdpPort_Object=MibTableColumn
ntcBbfOIpOutDestinationUdpPort=_NtcBbfOIpOutDestinationUdpPort_Object((1,3,6,1,4,1,5835,5,2,1300,1,3,1,4),_NtcBbfOIpOutDestinationUdpPort_Type())
ntcBbfOIpOutDestinationUdpPort.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutDestinationUdpPort.setStatus(_A)
class _NtcBbfOIpOutPassInvalidFrames_Type(NtcEnable):defaultValue=0
_NtcBbfOIpOutPassInvalidFrames_Type.__name__=_G
_NtcBbfOIpOutPassInvalidFrames_Object=MibTableColumn
ntcBbfOIpOutPassInvalidFrames=_NtcBbfOIpOutPassInvalidFrames_Object((1,3,6,1,4,1,5835,5,2,1300,1,3,1,5),_NtcBbfOIpOutPassInvalidFrames_Type())
ntcBbfOIpOutPassInvalidFrames.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutPassInvalidFrames.setStatus(_A)
class _NtcBbfOIpOutEncapProt_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('udp',0),('rtp',1)))
_NtcBbfOIpOutEncapProt_Type.__name__=_F
_NtcBbfOIpOutEncapProt_Object=MibTableColumn
ntcBbfOIpOutEncapProt=_NtcBbfOIpOutEncapProt_Object((1,3,6,1,4,1,5835,5,2,1300,1,3,1,6),_NtcBbfOIpOutEncapProt_Type())
ntcBbfOIpOutEncapProt.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutEncapProt.setStatus(_A)
_NtcBbfOIpOutMonitor_ObjectIdentity=ObjectIdentity
ntcBbfOIpOutMonitor=_NtcBbfOIpOutMonitor_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1300,1,4))
if mibBuilder.loadTexts:ntcBbfOIpOutMonitor.setStatus(_A)
class _NtcBbfOIpOutMonReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('counting',0),('reset',1)))
_NtcBbfOIpOutMonReset_Type.__name__=_F
_NtcBbfOIpOutMonReset_Object=MibScalar
ntcBbfOIpOutMonReset=_NtcBbfOIpOutMonReset_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,1),_NtcBbfOIpOutMonReset_Type())
ntcBbfOIpOutMonReset.setMaxAccess(_D)
if mibBuilder.loadTexts:ntcBbfOIpOutMonReset.setStatus(_A)
_NtcBbfOIpOutMonOutputBbfBitRate_Type=Unsigned32
_NtcBbfOIpOutMonOutputBbfBitRate_Object=MibScalar
ntcBbfOIpOutMonOutputBbfBitRate=_NtcBbfOIpOutMonOutputBbfBitRate_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,2),_NtcBbfOIpOutMonOutputBbfBitRate_Type())
ntcBbfOIpOutMonOutputBbfBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonOutputBbfBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonOutputBbfBitRate.setUnits('bps')
_NtcBbfOIpOutMonBbfInCount_Type=Counter32
_NtcBbfOIpOutMonBbfInCount_Object=MibScalar
ntcBbfOIpOutMonBbfInCount=_NtcBbfOIpOutMonBbfInCount_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,3),_NtcBbfOIpOutMonBbfInCount_Type())
ntcBbfOIpOutMonBbfInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonBbfInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonBbfInCount.setUnits(_E)
_NtcBbfOIpOutMonBbfOutCount_Type=Counter32
_NtcBbfOIpOutMonBbfOutCount_Object=MibScalar
ntcBbfOIpOutMonBbfOutCount=_NtcBbfOIpOutMonBbfOutCount_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,4),_NtcBbfOIpOutMonBbfOutCount_Type())
ntcBbfOIpOutMonBbfOutCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonBbfOutCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonBbfOutCount.setUnits(_E)
_NtcBbfOIpOutMonBbfDropCount_Type=Counter32
_NtcBbfOIpOutMonBbfDropCount_Object=MibScalar
ntcBbfOIpOutMonBbfDropCount=_NtcBbfOIpOutMonBbfDropCount_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,5),_NtcBbfOIpOutMonBbfDropCount_Type())
ntcBbfOIpOutMonBbfDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonBbfDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonBbfDropCount.setUnits(_E)
_NtcBbfOIpOutMonDestTable_Object=MibTable
ntcBbfOIpOutMonDestTable=_NtcBbfOIpOutMonDestTable_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,6))
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestTable.setStatus(_A)
_NtcBbfOIpOutMonDestEntry_Object=MibTableRow
ntcBbfOIpOutMonDestEntry=_NtcBbfOIpOutMonDestEntry_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,6,1))
ntcBbfOIpOutMonDestEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestEntry.setStatus(_A)
class _NtcBbfOIpOutMonDestDemodId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_NtcBbfOIpOutMonDestDemodId_Type.__name__=_F
_NtcBbfOIpOutMonDestDemodId_Object=MibTableColumn
ntcBbfOIpOutMonDestDemodId=_NtcBbfOIpOutMonDestDemodId_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,6,1,1),_NtcBbfOIpOutMonDestDemodId_Type())
ntcBbfOIpOutMonDestDemodId.setMaxAccess(_K)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestDemodId.setStatus(_A)
_NtcBbfOIpOutMonDestBitRate_Type=Unsigned32
_NtcBbfOIpOutMonDestBitRate_Object=MibTableColumn
ntcBbfOIpOutMonDestBitRate=_NtcBbfOIpOutMonDestBitRate_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,6,1,2),_NtcBbfOIpOutMonDestBitRate_Type())
ntcBbfOIpOutMonDestBitRate.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBitRate.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBitRate.setUnits('bps')
_NtcBbfOIpOutMonDestBbfInCount_Type=Counter32
_NtcBbfOIpOutMonDestBbfInCount_Object=MibTableColumn
ntcBbfOIpOutMonDestBbfInCount=_NtcBbfOIpOutMonDestBbfInCount_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,6,1,3),_NtcBbfOIpOutMonDestBbfInCount_Type())
ntcBbfOIpOutMonDestBbfInCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBbfInCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBbfInCount.setUnits(_E)
_NtcBbfOIpOutMonDestBbfOutCount_Type=Counter32
_NtcBbfOIpOutMonDestBbfOutCount_Object=MibTableColumn
ntcBbfOIpOutMonDestBbfOutCount=_NtcBbfOIpOutMonDestBbfOutCount_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,6,1,4),_NtcBbfOIpOutMonDestBbfOutCount_Type())
ntcBbfOIpOutMonDestBbfOutCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBbfOutCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBbfOutCount.setUnits(_E)
_NtcBbfOIpOutMonDestBbfDropCount_Type=Counter32
_NtcBbfOIpOutMonDestBbfDropCount_Object=MibTableColumn
ntcBbfOIpOutMonDestBbfDropCount=_NtcBbfOIpOutMonDestBbfDropCount_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,6,1,5),_NtcBbfOIpOutMonDestBbfDropCount_Type())
ntcBbfOIpOutMonDestBbfDropCount.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBbfDropCount.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonDestBbfDropCount.setUnits(_E)
_NtcBbfOIpOutMonInvalFramTable_Object=MibTable
ntcBbfOIpOutMonInvalFramTable=_NtcBbfOIpOutMonInvalFramTable_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,7))
if mibBuilder.loadTexts:ntcBbfOIpOutMonInvalFramTable.setStatus(_A)
_NtcBbfOIpOutMonInvalFramEntry_Object=MibTableRow
ntcBbfOIpOutMonInvalFramEntry=_NtcBbfOIpOutMonInvalFramEntry_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,7,1))
ntcBbfOIpOutMonInvalFramEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:ntcBbfOIpOutMonInvalFramEntry.setStatus(_A)
class _NtcBbfOIpOutMonInvalFramDemodId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),(_I,2),(_J,3)))
_NtcBbfOIpOutMonInvalFramDemodId_Type.__name__=_F
_NtcBbfOIpOutMonInvalFramDemodId_Object=MibTableColumn
ntcBbfOIpOutMonInvalFramDemodId=_NtcBbfOIpOutMonInvalFramDemodId_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,7,1,1),_NtcBbfOIpOutMonInvalFramDemodId_Type())
ntcBbfOIpOutMonInvalFramDemodId.setMaxAccess(_K)
if mibBuilder.loadTexts:ntcBbfOIpOutMonInvalFramDemodId.setStatus(_A)
_NtcBbfOIpOutMonInvalCrc8_Type=Counter32
_NtcBbfOIpOutMonInvalCrc8_Object=MibTableColumn
ntcBbfOIpOutMonInvalCrc8=_NtcBbfOIpOutMonInvalCrc8_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,7,1,2),_NtcBbfOIpOutMonInvalCrc8_Type())
ntcBbfOIpOutMonInvalCrc8.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonInvalCrc8.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonInvalCrc8.setUnits(_E)
_NtcBbfOIpOutMonInvalPadd_Type=Counter32
_NtcBbfOIpOutMonInvalPadd_Object=MibTableColumn
ntcBbfOIpOutMonInvalPadd=_NtcBbfOIpOutMonInvalPadd_Object((1,3,6,1,4,1,5835,5,2,1300,1,4,7,1,3),_NtcBbfOIpOutMonInvalPadd_Type())
ntcBbfOIpOutMonInvalPadd.setMaxAccess(_C)
if mibBuilder.loadTexts:ntcBbfOIpOutMonInvalPadd.setStatus(_A)
if mibBuilder.loadTexts:ntcBbfOIpOutMonInvalPadd.setUnits(_E)
_NtcBbfOIpOutConformance_ObjectIdentity=ObjectIdentity
ntcBbfOIpOutConformance=_NtcBbfOIpOutConformance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1300,2))
if mibBuilder.loadTexts:ntcBbfOIpOutConformance.setStatus(_A)
_NtcBbfOIpOutConfCompliance_ObjectIdentity=ObjectIdentity
ntcBbfOIpOutConfCompliance=_NtcBbfOIpOutConfCompliance_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1300,2,1))
if mibBuilder.loadTexts:ntcBbfOIpOutConfCompliance.setStatus(_A)
_NtcBbfOIpOutConfGroup_ObjectIdentity=ObjectIdentity
ntcBbfOIpOutConfGroup=_NtcBbfOIpOutConfGroup_ObjectIdentity((1,3,6,1,4,1,5835,5,2,1300,2,2))
if mibBuilder.loadTexts:ntcBbfOIpOutConfGroup.setStatus(_A)
ntcBbfOIpOutConfGrpV1Standard=ObjectGroup((1,3,6,1,4,1,5835,5,2,1300,2,2,1))
ntcBbfOIpOutConfGrpV1Standard.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g)))
if mibBuilder.loadTexts:ntcBbfOIpOutConfGrpV1Standard.setStatus(_A)
ntcBbfOIpOutConfCompV1Standard=ModuleCompliance((1,3,6,1,4,1,5835,5,2,1300,2,1,1))
ntcBbfOIpOutConfCompV1Standard.setObjects((_B,_h))
if mibBuilder.loadTexts:ntcBbfOIpOutConfCompV1Standard.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ntcBbfOverIpOut':ntcBbfOverIpOut,'ntcBbfOIpOutObjects':ntcBbfOIpOutObjects,_P:ntcBbfOIpOutEnable,_Q:ntcBbfOIpOutOutputSelection,'ntcBbfOIpOutDestinationsTable':ntcBbfOIpOutDestinationsTable,'ntcBbfOIpOutDestinationsEntry':ntcBbfOIpOutDestinationsEntry,_M:ntcBbfOIpOutDestinationsDemodId,_R:ntcBbfOIpOutBbfOutEnable,_S:ntcBbfOIpOutDestinationIpAddress,_T:ntcBbfOIpOutDestinationUdpPort,_U:ntcBbfOIpOutPassInvalidFrames,_V:ntcBbfOIpOutEncapProt,'ntcBbfOIpOutMonitor':ntcBbfOIpOutMonitor,_W:ntcBbfOIpOutMonReset,_X:ntcBbfOIpOutMonOutputBbfBitRate,_Y:ntcBbfOIpOutMonBbfInCount,_Z:ntcBbfOIpOutMonBbfOutCount,_a:ntcBbfOIpOutMonBbfDropCount,'ntcBbfOIpOutMonDestTable':ntcBbfOIpOutMonDestTable,'ntcBbfOIpOutMonDestEntry':ntcBbfOIpOutMonDestEntry,_N:ntcBbfOIpOutMonDestDemodId,_b:ntcBbfOIpOutMonDestBitRate,_c:ntcBbfOIpOutMonDestBbfInCount,_d:ntcBbfOIpOutMonDestBbfOutCount,_e:ntcBbfOIpOutMonDestBbfDropCount,'ntcBbfOIpOutMonInvalFramTable':ntcBbfOIpOutMonInvalFramTable,'ntcBbfOIpOutMonInvalFramEntry':ntcBbfOIpOutMonInvalFramEntry,_O:ntcBbfOIpOutMonInvalFramDemodId,_f:ntcBbfOIpOutMonInvalCrc8,_g:ntcBbfOIpOutMonInvalPadd,'ntcBbfOIpOutConformance':ntcBbfOIpOutConformance,'ntcBbfOIpOutConfCompliance':ntcBbfOIpOutConfCompliance,'ntcBbfOIpOutConfCompV1Standard':ntcBbfOIpOutConfCompV1Standard,'ntcBbfOIpOutConfGroup':ntcBbfOIpOutConfGroup,_h:ntcBbfOIpOutConfGrpV1Standard})