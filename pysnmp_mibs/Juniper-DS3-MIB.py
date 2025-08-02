_y='juniDs3FarEndGroup2'
_x='juniDs3FarEndGroup'
_w='juniDs3Group4'
_v='juniDs3Group3'
_u='juniDs3Group2'
_t='juniDs3Group'
_s='juniDsx3FarEndCarrier'
_r='juniDsx3FarEndGeneratorNumber'
_q='juniDsx3FarEndPortNumber'
_p='juniDsx3MdlGenerator'
_o='juniDsx3MdlPort'
_n='juniDsx3MdlPfi'
_m='juniDsx3MdlUnit'
_l='juniDsx3MdlFic'
_k='juniDsx3MdlLic'
_j='juniDsx3MdlEic'
_i='juniDsx3MdlTransmit'
_h='juniDsx3MdlCarrier'
_g='juniDsx3FarEndConfigEntry'
_f='juniDsx3FarEndTotalEntry'
_e='juniDsx3FarEndIntervalEntry'
_d='juniDsx3FarEndCurrentEntry'
_c='enabled'
_b='disabled'
_a='ifIndex'
_Z='IF-MIB'
_Y='juniDs3Group5'
_X='juniDsx3FarEndTotalInvalidSeconds'
_W='juniDsx3FarEndIntervalInvalidSeconds'
_V='juniDsx3FarEndCurrentInvalidSeconds'
_U='juniDs3NextIfIndex'
_T='juniDsx3RowStatus'
_S='juniDsx3LowerIfIndex'
_R='juniDsx3Ds3Channel'
_Q='juniDsx3Application'
_P='juniDsx3InterfaceType'
_O='juniDsx3Channelization'
_N='read-write'
_M='juniDsx3Ds3DsuScrambleMode'
_L='juniDsx3Ds3BandwidthLimit'
_K='juniDsx3Ds3DsuMode'
_J='read-only'
_I='juniDsx3CellScramblerConfig'
_H='juniDsx3LineType'
_G='juniDsx3LineLength'
_F='obsolete'
_E='DisplayString'
_D='Integer32'
_C='read-create'
_B='current'
_A='Juniper-DS3-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dsx3FarEndConfigEntry,dsx3FarEndCurrentEntry,dsx3FarEndIntervalEntry,dsx3FarEndTotalEntry=mibBuilder.importSymbols('DS3-MIB','dsx3FarEndConfigEntry','dsx3FarEndCurrentEntry','dsx3FarEndIntervalEntry','dsx3FarEndTotalEntry')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_Z,'InterfaceIndexOrZero',_a)
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniNextIfIndex,=mibBuilder.importSymbols('Juniper-TC','JuniNextIfIndex')
PerfCurrentCount,PerfIntervalCount,PerfTotalCount=mibBuilder.importSymbols('PerfHist-TC-MIB','PerfCurrentCount','PerfIntervalCount','PerfTotalCount')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention','TruthValue')
juniDs3MIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,4))
if mibBuilder.loadTexts:juniDs3MIB.setRevisions(('2004-10-12 06:51','2003-09-30 12:11','2002-09-16 21:44','2002-09-12 16:59','2002-04-04 14:07','2002-02-22 21:21','2001-04-27 19:49','2001-02-05 00:00','1999-07-27 00:00','1998-11-13 00:00'))
_JuniDs3Objects_ObjectIdentity=ObjectIdentity
juniDs3Objects=_JuniDs3Objects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,4,1))
_JuniDsx3ConfigTable_Object=MibTable
juniDsx3ConfigTable=_JuniDsx3ConfigTable_Object((1,3,6,1,4,1,4874,2,2,4,1,1))
if mibBuilder.loadTexts:juniDsx3ConfigTable.setStatus(_B)
_JuniDsx3ConfigEntry_Object=MibTableRow
juniDsx3ConfigEntry=_JuniDsx3ConfigEntry_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1))
juniDsx3ConfigEntry.setIndexNames((0,_Z,_a))
if mibBuilder.loadTexts:juniDsx3ConfigEntry.setStatus(_B)
class _JuniDsx3LineLength_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,137))
_JuniDsx3LineLength_Type.__name__=_D
_JuniDsx3LineLength_Object=MibTableColumn
juniDsx3LineLength=_JuniDsx3LineLength_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,1),_JuniDsx3LineLength_Type())
juniDsx3LineLength.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3LineLength.setStatus(_B)
if mibBuilder.loadTexts:juniDsx3LineLength.setUnits('meters')
class _JuniDsx3LineType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,18,20)));namedValues=NamedValues(*(('juniDsx3other',1),('juniDsx3M23',2),('juniDsx3SYNTRAN',3),('juniDsx3CbitParity',4),('juniDsx3ClearChannel',5),('juniE3G832',6),('juniE3Framed',7),('juniE3Plcp',8),('juniDsx3M23Plcp',18),('juniDsx3CbitParityPlcp',20)))
_JuniDsx3LineType_Type.__name__=_D
_JuniDsx3LineType_Object=MibTableColumn
juniDsx3LineType=_JuniDsx3LineType_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,2),_JuniDsx3LineType_Type())
juniDsx3LineType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3LineType.setStatus(_B)
class _JuniDsx3CellScramblerConfig_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('scramblerOn',1),('scramblerOff',2),('notSupported',3)))
_JuniDsx3CellScramblerConfig_Type.__name__=_D
_JuniDsx3CellScramblerConfig_Object=MibTableColumn
juniDsx3CellScramblerConfig=_JuniDsx3CellScramblerConfig_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,3),_JuniDsx3CellScramblerConfig_Type())
juniDsx3CellScramblerConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3CellScramblerConfig.setStatus(_B)
_JuniDsx3Channelization_Type=TruthValue
_JuniDsx3Channelization_Object=MibTableColumn
juniDsx3Channelization=_JuniDsx3Channelization_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,4),_JuniDsx3Channelization_Type())
juniDsx3Channelization.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3Channelization.setStatus(_B)
class _JuniDsx3InterfaceType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ds3T3',0),('ds3E3',1)))
_JuniDsx3InterfaceType_Type.__name__=_D
_JuniDsx3InterfaceType_Object=MibTableColumn
juniDsx3InterfaceType=_JuniDsx3InterfaceType_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,5),_JuniDsx3InterfaceType_Type())
juniDsx3InterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3InterfaceType.setStatus(_B)
class _JuniDsx3Application_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ds3FrameOverDs3',0),('ds3AtmOverDs3',1)))
_JuniDsx3Application_Type.__name__=_D
_JuniDsx3Application_Object=MibTableColumn
juniDsx3Application=_JuniDsx3Application_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,6),_JuniDsx3Application_Type())
juniDsx3Application.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3Application.setStatus(_B)
class _JuniDsx3Ds3Channel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,28))
_JuniDsx3Ds3Channel_Type.__name__=_D
_JuniDsx3Ds3Channel_Object=MibTableColumn
juniDsx3Ds3Channel=_JuniDsx3Ds3Channel_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,7),_JuniDsx3Ds3Channel_Type())
juniDsx3Ds3Channel.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3Ds3Channel.setStatus(_B)
_JuniDsx3LowerIfIndex_Type=InterfaceIndexOrZero
_JuniDsx3LowerIfIndex_Object=MibTableColumn
juniDsx3LowerIfIndex=_JuniDsx3LowerIfIndex_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,8),_JuniDsx3LowerIfIndex_Type())
juniDsx3LowerIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3LowerIfIndex.setStatus(_B)
_JuniDsx3RowStatus_Type=RowStatus
_JuniDsx3RowStatus_Object=MibTableColumn
juniDsx3RowStatus=_JuniDsx3RowStatus_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,9),_JuniDsx3RowStatus_Type())
juniDsx3RowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3RowStatus.setStatus(_B)
class _JuniDsx3Ds3DsuMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,2,4)));namedValues=NamedValues(*(('ds3DsuModeNone',0),('ds3DsuLarsCom',2),('ds3DsuDigitalLink',4)))
_JuniDsx3Ds3DsuMode_Type.__name__=_D
_JuniDsx3Ds3DsuMode_Object=MibTableColumn
juniDsx3Ds3DsuMode=_JuniDsx3Ds3DsuMode_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,10),_JuniDsx3Ds3DsuMode_Type())
juniDsx3Ds3DsuMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3Ds3DsuMode.setStatus(_B)
class _JuniDsx3Ds3BandwidthLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,44210))
_JuniDsx3Ds3BandwidthLimit_Type.__name__=_D
_JuniDsx3Ds3BandwidthLimit_Object=MibTableColumn
juniDsx3Ds3BandwidthLimit=_JuniDsx3Ds3BandwidthLimit_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,11),_JuniDsx3Ds3BandwidthLimit_Type())
juniDsx3Ds3BandwidthLimit.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3Ds3BandwidthLimit.setStatus(_B)
class _JuniDsx3Ds3DsuScrambleMode_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('ds3DsuScrambleDisabled',0),('ds3DsuScrambleEnable',1)))
_JuniDsx3Ds3DsuScrambleMode_Type.__name__=_D
_JuniDsx3Ds3DsuScrambleMode_Object=MibTableColumn
juniDsx3Ds3DsuScrambleMode=_JuniDsx3Ds3DsuScrambleMode_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,12),_JuniDsx3Ds3DsuScrambleMode_Type())
juniDsx3Ds3DsuScrambleMode.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3Ds3DsuScrambleMode.setStatus(_B)
class _JuniDsx3MdlCarrier_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_JuniDsx3MdlCarrier_Type.__name__=_D
_JuniDsx3MdlCarrier_Object=MibTableColumn
juniDsx3MdlCarrier=_JuniDsx3MdlCarrier_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,13),_JuniDsx3MdlCarrier_Type())
juniDsx3MdlCarrier.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlCarrier.setStatus(_B)
class _JuniDsx3MdlTransmit_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*(('path',1),('idlesignal',2),('pathIdlesignal',3),('testsignal',4),('pathTestsignal',5),('idlesignalTestsignal',6),('pathIdlesignalTestsignal',7),('none',8)))
_JuniDsx3MdlTransmit_Type.__name__=_D
_JuniDsx3MdlTransmit_Object=MibTableColumn
juniDsx3MdlTransmit=_JuniDsx3MdlTransmit_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,14),_JuniDsx3MdlTransmit_Type())
juniDsx3MdlTransmit.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlTransmit.setStatus(_B)
class _JuniDsx3MdlEic_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniDsx3MdlEic_Type.__name__=_E
_JuniDsx3MdlEic_Object=MibTableColumn
juniDsx3MdlEic=_JuniDsx3MdlEic_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,15),_JuniDsx3MdlEic_Type())
juniDsx3MdlEic.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlEic.setStatus(_B)
class _JuniDsx3MdlLic_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,11))
_JuniDsx3MdlLic_Type.__name__=_E
_JuniDsx3MdlLic_Object=MibTableColumn
juniDsx3MdlLic=_JuniDsx3MdlLic_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,16),_JuniDsx3MdlLic_Type())
juniDsx3MdlLic.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlLic.setStatus(_B)
class _JuniDsx3MdlFic_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_JuniDsx3MdlFic_Type.__name__=_E
_JuniDsx3MdlFic_Object=MibTableColumn
juniDsx3MdlFic=_JuniDsx3MdlFic_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,17),_JuniDsx3MdlFic_Type())
juniDsx3MdlFic.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlFic.setStatus(_B)
class _JuniDsx3MdlUnit_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,6))
_JuniDsx3MdlUnit_Type.__name__=_E
_JuniDsx3MdlUnit_Object=MibTableColumn
juniDsx3MdlUnit=_JuniDsx3MdlUnit_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,18),_JuniDsx3MdlUnit_Type())
juniDsx3MdlUnit.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlUnit.setStatus(_B)
class _JuniDsx3MdlPfi_Type(DisplayString):defaultValue=OctetString('');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx3MdlPfi_Type.__name__=_E
_JuniDsx3MdlPfi_Object=MibTableColumn
juniDsx3MdlPfi=_JuniDsx3MdlPfi_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,19),_JuniDsx3MdlPfi_Type())
juniDsx3MdlPfi.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlPfi.setStatus(_B)
class _JuniDsx3MdlPort_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx3MdlPort_Type.__name__=_E
_JuniDsx3MdlPort_Object=MibTableColumn
juniDsx3MdlPort=_JuniDsx3MdlPort_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,20),_JuniDsx3MdlPort_Type())
juniDsx3MdlPort.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlPort.setStatus(_B)
class _JuniDsx3MdlGenerator_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx3MdlGenerator_Type.__name__=_E
_JuniDsx3MdlGenerator_Object=MibTableColumn
juniDsx3MdlGenerator=_JuniDsx3MdlGenerator_Object((1,3,6,1,4,1,4874,2,2,4,1,1,1,21),_JuniDsx3MdlGenerator_Type())
juniDsx3MdlGenerator.setMaxAccess(_C)
if mibBuilder.loadTexts:juniDsx3MdlGenerator.setStatus(_B)
_JuniDs3NextIfIndex_Type=JuniNextIfIndex
_JuniDs3NextIfIndex_Object=MibScalar
juniDs3NextIfIndex=_JuniDs3NextIfIndex_Object((1,3,6,1,4,1,4874,2,2,4,1,2),_JuniDs3NextIfIndex_Type())
juniDs3NextIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:juniDs3NextIfIndex.setStatus(_B)
_JuniDsx3FarEndCurrentTable_Object=MibTable
juniDsx3FarEndCurrentTable=_JuniDsx3FarEndCurrentTable_Object((1,3,6,1,4,1,4874,2,2,4,1,3))
if mibBuilder.loadTexts:juniDsx3FarEndCurrentTable.setStatus(_B)
_JuniDsx3FarEndCurrentEntry_Object=MibTableRow
juniDsx3FarEndCurrentEntry=_JuniDsx3FarEndCurrentEntry_Object((1,3,6,1,4,1,4874,2,2,4,1,3,1))
if mibBuilder.loadTexts:juniDsx3FarEndCurrentEntry.setStatus(_B)
_JuniDsx3FarEndCurrentInvalidSeconds_Type=PerfCurrentCount
_JuniDsx3FarEndCurrentInvalidSeconds_Object=MibTableColumn
juniDsx3FarEndCurrentInvalidSeconds=_JuniDsx3FarEndCurrentInvalidSeconds_Object((1,3,6,1,4,1,4874,2,2,4,1,3,1,1),_JuniDsx3FarEndCurrentInvalidSeconds_Type())
juniDsx3FarEndCurrentInvalidSeconds.setMaxAccess(_J)
if mibBuilder.loadTexts:juniDsx3FarEndCurrentInvalidSeconds.setStatus(_B)
_JuniDsx3FarEndIntervalTable_Object=MibTable
juniDsx3FarEndIntervalTable=_JuniDsx3FarEndIntervalTable_Object((1,3,6,1,4,1,4874,2,2,4,1,4))
if mibBuilder.loadTexts:juniDsx3FarEndIntervalTable.setStatus(_B)
_JuniDsx3FarEndIntervalEntry_Object=MibTableRow
juniDsx3FarEndIntervalEntry=_JuniDsx3FarEndIntervalEntry_Object((1,3,6,1,4,1,4874,2,2,4,1,4,1))
if mibBuilder.loadTexts:juniDsx3FarEndIntervalEntry.setStatus(_B)
_JuniDsx3FarEndIntervalInvalidSeconds_Type=PerfIntervalCount
_JuniDsx3FarEndIntervalInvalidSeconds_Object=MibTableColumn
juniDsx3FarEndIntervalInvalidSeconds=_JuniDsx3FarEndIntervalInvalidSeconds_Object((1,3,6,1,4,1,4874,2,2,4,1,4,1,1),_JuniDsx3FarEndIntervalInvalidSeconds_Type())
juniDsx3FarEndIntervalInvalidSeconds.setMaxAccess(_J)
if mibBuilder.loadTexts:juniDsx3FarEndIntervalInvalidSeconds.setStatus(_B)
_JuniDsx3FarEndTotalTable_Object=MibTable
juniDsx3FarEndTotalTable=_JuniDsx3FarEndTotalTable_Object((1,3,6,1,4,1,4874,2,2,4,1,5))
if mibBuilder.loadTexts:juniDsx3FarEndTotalTable.setStatus(_B)
_JuniDsx3FarEndTotalEntry_Object=MibTableRow
juniDsx3FarEndTotalEntry=_JuniDsx3FarEndTotalEntry_Object((1,3,6,1,4,1,4874,2,2,4,1,5,1))
if mibBuilder.loadTexts:juniDsx3FarEndTotalEntry.setStatus(_B)
_JuniDsx3FarEndTotalInvalidSeconds_Type=PerfTotalCount
_JuniDsx3FarEndTotalInvalidSeconds_Object=MibTableColumn
juniDsx3FarEndTotalInvalidSeconds=_JuniDsx3FarEndTotalInvalidSeconds_Object((1,3,6,1,4,1,4874,2,2,4,1,5,1,1),_JuniDsx3FarEndTotalInvalidSeconds_Type())
juniDsx3FarEndTotalInvalidSeconds.setMaxAccess(_J)
if mibBuilder.loadTexts:juniDsx3FarEndTotalInvalidSeconds.setStatus(_B)
_JuniDsx3FarEndConfigTable_Object=MibTable
juniDsx3FarEndConfigTable=_JuniDsx3FarEndConfigTable_Object((1,3,6,1,4,1,4874,2,2,4,1,6))
if mibBuilder.loadTexts:juniDsx3FarEndConfigTable.setStatus(_B)
_JuniDsx3FarEndConfigEntry_Object=MibTableRow
juniDsx3FarEndConfigEntry=_JuniDsx3FarEndConfigEntry_Object((1,3,6,1,4,1,4874,2,2,4,1,6,1))
if mibBuilder.loadTexts:juniDsx3FarEndConfigEntry.setStatus(_B)
class _JuniDsx3FarEndPortNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx3FarEndPortNumber_Type.__name__=_E
_JuniDsx3FarEndPortNumber_Object=MibTableColumn
juniDsx3FarEndPortNumber=_JuniDsx3FarEndPortNumber_Object((1,3,6,1,4,1,4874,2,2,4,1,6,1,1),_JuniDsx3FarEndPortNumber_Type())
juniDsx3FarEndPortNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:juniDsx3FarEndPortNumber.setStatus(_B)
class _JuniDsx3FarEndGeneratorNumber_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,38))
_JuniDsx3FarEndGeneratorNumber_Type.__name__=_E
_JuniDsx3FarEndGeneratorNumber_Object=MibTableColumn
juniDsx3FarEndGeneratorNumber=_JuniDsx3FarEndGeneratorNumber_Object((1,3,6,1,4,1,4874,2,2,4,1,6,1,2),_JuniDsx3FarEndGeneratorNumber_Type())
juniDsx3FarEndGeneratorNumber.setMaxAccess(_N)
if mibBuilder.loadTexts:juniDsx3FarEndGeneratorNumber.setStatus(_B)
class _JuniDsx3FarEndCarrier_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*((_b,0),(_c,1)))
_JuniDsx3FarEndCarrier_Type.__name__=_D
_JuniDsx3FarEndCarrier_Object=MibTableColumn
juniDsx3FarEndCarrier=_JuniDsx3FarEndCarrier_Object((1,3,6,1,4,1,4874,2,2,4,1,6,1,3),_JuniDsx3FarEndCarrier_Type())
juniDsx3FarEndCarrier.setMaxAccess(_N)
if mibBuilder.loadTexts:juniDsx3FarEndCarrier.setStatus(_B)
_JuniDs3Conformance_ObjectIdentity=ObjectIdentity
juniDs3Conformance=_JuniDs3Conformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,4,4))
_JuniDs3Compliances_ObjectIdentity=ObjectIdentity
juniDs3Compliances=_JuniDs3Compliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,4,4,1))
_JuniDs3Groups_ObjectIdentity=ObjectIdentity
juniDs3Groups=_JuniDs3Groups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,4,4,2))
dsx3FarEndCurrentEntry.registerAugmentions((_A,_d))
juniDsx3FarEndCurrentEntry.setIndexNames(*dsx3FarEndCurrentEntry.getIndexNames())
dsx3FarEndIntervalEntry.registerAugmentions((_A,_e))
juniDsx3FarEndIntervalEntry.setIndexNames(*dsx3FarEndIntervalEntry.getIndexNames())
dsx3FarEndTotalEntry.registerAugmentions((_A,_f))
juniDsx3FarEndTotalEntry.setIndexNames(*dsx3FarEndTotalEntry.getIndexNames())
dsx3FarEndConfigEntry.registerAugmentions((_A,_g))
juniDsx3FarEndConfigEntry.setIndexNames(*dsx3FarEndConfigEntry.getIndexNames())
juniDs3Group=ObjectGroup((1,3,6,1,4,1,4874,2,2,4,4,2,1))
juniDs3Group.setObjects((_A,_G))
if mibBuilder.loadTexts:juniDs3Group.setStatus(_F)
juniDs3Group2=ObjectGroup((1,3,6,1,4,1,4874,2,2,4,4,2,2))
juniDs3Group2.setObjects(*((_A,_G),(_A,_H),(_A,_I)))
if mibBuilder.loadTexts:juniDs3Group2.setStatus(_F)
juniDs3Group3=ObjectGroup((1,3,6,1,4,1,4874,2,2,4,4,2,3))
juniDs3Group3.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_K),(_A,_L),(_A,_M)))
if mibBuilder.loadTexts:juniDs3Group3.setStatus(_F)
juniDs3Group4=ObjectGroup((1,3,6,1,4,1,4874,2,2,4,4,2,4))
juniDs3Group4.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_K),(_A,_L),(_A,_M),(_A,_U)))
if mibBuilder.loadTexts:juniDs3Group4.setStatus(_F)
juniDs3Group5=ObjectGroup((1,3,6,1,4,1,4874,2,2,4,4,2,5))
juniDs3Group5.setObjects(*((_A,_G),(_A,_H),(_A,_I),(_A,_O),(_A,_P),(_A,_Q),(_A,_R),(_A,_S),(_A,_T),(_A,_K),(_A,_L),(_A,_M),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_U)))
if mibBuilder.loadTexts:juniDs3Group5.setStatus(_B)
juniDs3FarEndGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,4,4,2,6))
juniDs3FarEndGroup.setObjects(*((_A,_V),(_A,_W),(_A,_X)))
if mibBuilder.loadTexts:juniDs3FarEndGroup.setStatus(_F)
juniDs3FarEndGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,4,4,2,7))
juniDs3FarEndGroup2.setObjects(*((_A,_V),(_A,_W),(_A,_X),(_A,_q),(_A,_r),(_A,_s)))
if mibBuilder.loadTexts:juniDs3FarEndGroup2.setStatus(_B)
juniDs3Compliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,4,4,1,1))
juniDs3Compliance.setObjects((_A,_t))
if mibBuilder.loadTexts:juniDs3Compliance.setStatus(_F)
juniDs3Compliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,4,4,1,2))
juniDs3Compliance2.setObjects((_A,_u))
if mibBuilder.loadTexts:juniDs3Compliance2.setStatus(_F)
juniDs3Compliance3=ModuleCompliance((1,3,6,1,4,1,4874,2,2,4,4,1,3))
juniDs3Compliance3.setObjects((_A,_v))
if mibBuilder.loadTexts:juniDs3Compliance3.setStatus(_F)
juniDs3Compliance4=ModuleCompliance((1,3,6,1,4,1,4874,2,2,4,4,1,4))
juniDs3Compliance4.setObjects((_A,_w))
if mibBuilder.loadTexts:juniDs3Compliance4.setStatus(_F)
juniDs3Compliance5=ModuleCompliance((1,3,6,1,4,1,4874,2,2,4,4,1,5))
juniDs3Compliance5.setObjects(*((_A,_Y),(_A,_x)))
if mibBuilder.loadTexts:juniDs3Compliance5.setStatus(_F)
juniDs3Compliance6=ModuleCompliance((1,3,6,1,4,1,4874,2,2,4,4,1,6))
juniDs3Compliance6.setObjects(*((_A,_Y),(_A,_y)))
if mibBuilder.loadTexts:juniDs3Compliance6.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'juniDs3MIB':juniDs3MIB,'juniDs3Objects':juniDs3Objects,'juniDsx3ConfigTable':juniDsx3ConfigTable,'juniDsx3ConfigEntry':juniDsx3ConfigEntry,_G:juniDsx3LineLength,_H:juniDsx3LineType,_I:juniDsx3CellScramblerConfig,_O:juniDsx3Channelization,_P:juniDsx3InterfaceType,_Q:juniDsx3Application,_R:juniDsx3Ds3Channel,_S:juniDsx3LowerIfIndex,_T:juniDsx3RowStatus,_K:juniDsx3Ds3DsuMode,_L:juniDsx3Ds3BandwidthLimit,_M:juniDsx3Ds3DsuScrambleMode,_h:juniDsx3MdlCarrier,_i:juniDsx3MdlTransmit,_j:juniDsx3MdlEic,_k:juniDsx3MdlLic,_l:juniDsx3MdlFic,_m:juniDsx3MdlUnit,_n:juniDsx3MdlPfi,_o:juniDsx3MdlPort,_p:juniDsx3MdlGenerator,_U:juniDs3NextIfIndex,'juniDsx3FarEndCurrentTable':juniDsx3FarEndCurrentTable,_d:juniDsx3FarEndCurrentEntry,_V:juniDsx3FarEndCurrentInvalidSeconds,'juniDsx3FarEndIntervalTable':juniDsx3FarEndIntervalTable,_e:juniDsx3FarEndIntervalEntry,_W:juniDsx3FarEndIntervalInvalidSeconds,'juniDsx3FarEndTotalTable':juniDsx3FarEndTotalTable,_f:juniDsx3FarEndTotalEntry,_X:juniDsx3FarEndTotalInvalidSeconds,'juniDsx3FarEndConfigTable':juniDsx3FarEndConfigTable,_g:juniDsx3FarEndConfigEntry,_q:juniDsx3FarEndPortNumber,_r:juniDsx3FarEndGeneratorNumber,_s:juniDsx3FarEndCarrier,'juniDs3Conformance':juniDs3Conformance,'juniDs3Compliances':juniDs3Compliances,'juniDs3Compliance':juniDs3Compliance,'juniDs3Compliance2':juniDs3Compliance2,'juniDs3Compliance3':juniDs3Compliance3,'juniDs3Compliance4':juniDs3Compliance4,'juniDs3Compliance5':juniDs3Compliance5,'juniDs3Compliance6':juniDs3Compliance6,'juniDs3Groups':juniDs3Groups,_t:juniDs3Group,_u:juniDs3Group2,_v:juniDs3Group3,_w:juniDs3Group4,_Y:juniDs3Group5,_x:juniDs3FarEndGroup,_y:juniDs3FarEndGroup2})