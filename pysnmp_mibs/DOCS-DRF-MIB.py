_l='docsDrfCmtsGroup'
_k='docsDrfDownstreamPhyDependencies'
_j='docsDrfChannelBlockTestIfIndex'
_i='docsDrfChannelBlockTestType'
_h='docsDrfChannelBlockMute'
_g='docsDrfChannelBlockCfgNumberChannels'
_f='docsDrfChannelBlockNumberChannels'
_e='docsDrfGroupDependencyType'
_d='docsDrfGroupDependencyGroupID'
_c='docsDrfDownstreamCapabMuting'
_b='docsDrfDownstreamCapabServicesTransport'
_a='docsDrfDownstreamCapabConcurrentServices'
_Z='docsDrfDownstreamCapabJ83Annex'
_Y='docsDrfDownstreamCapabInterleaver'
_X='docsDrfDownstreamCapabModulation'
_W='docsDrfDownstreamCapabPower'
_V='docsDrfDownstreamCapabBandwidth'
_U='docsDrfDownstreamCapabFrequency'
_T='docsDrfDownstreamEntry'
_S='docsDrfChannelBlockPhysicalIndex'
_R='docsDrfGroupDependencyPhysicalIndex'
_Q='docsDrfGroupDependencyPhyParam'
_P='symbolRate'
_O='modulation'
_N='bandwidth'
_M='frequency'
_L='Unsigned32'
_K='ifIndex'
_J='IF-MIB'
_I='docsDrfGroup'
_H='read-write'
_G='not-accessible'
_F='Integer32'
_E='qamDependency'
_D='Bits'
_C='read-only'
_B='DOCS-DRF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
clabProjDocsis,=mibBuilder.importSymbols('CLAB-DEF-MIB','clabProjDocsis')
docsIfDownstreamChannelEntry,=mibBuilder.importSymbols('DOCS-IF-MIB','docsIfDownstreamChannelEntry')
PhysicalIndex,PhysicalIndexOrZero=mibBuilder.importSymbols('ENTITY-MIB','PhysicalIndex','PhysicalIndexOrZero')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols(_J,'InterfaceIndexOrZero',_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_L,'iso')
AutonomousType,DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','AutonomousType','DisplayString','PhysAddress','TextualConvention','TruthValue')
docsDrfMib=ModuleIdentity((1,3,6,1,4,1,4491,2,1,23))
if mibBuilder.loadTexts:docsDrfMib.setRevisions(('2007-12-06 00:00',))
_DocsDrfNotifications_ObjectIdentity=ObjectIdentity
docsDrfNotifications=_DocsDrfNotifications_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,0))
_DocsDrfObjects_ObjectIdentity=ObjectIdentity
docsDrfObjects=_DocsDrfObjects_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,1))
_DocsDrfRegistry_ObjectIdentity=ObjectIdentity
docsDrfRegistry=_DocsDrfRegistry_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,1,1))
if mibBuilder.loadTexts:docsDrfRegistry.setStatus(_A)
_DocsDrfPhyParamFixValue_ObjectIdentity=ObjectIdentity
docsDrfPhyParamFixValue=_DocsDrfPhyParamFixValue_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,1,1,1))
if mibBuilder.loadTexts:docsDrfPhyParamFixValue.setStatus(_A)
_DocsDrfPhyParamSameValue_ObjectIdentity=ObjectIdentity
docsDrfPhyParamSameValue=_DocsDrfPhyParamSameValue_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,1,1,2))
if mibBuilder.loadTexts:docsDrfPhyParamSameValue.setStatus(_A)
_DocsDrfPhyParamAdjacentValues_ObjectIdentity=ObjectIdentity
docsDrfPhyParamAdjacentValues=_DocsDrfPhyParamAdjacentValues_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,1,1,3))
if mibBuilder.loadTexts:docsDrfPhyParamAdjacentValues.setStatus(_A)
_DocsDrfPhyParamFrequencyRange_ObjectIdentity=ObjectIdentity
docsDrfPhyParamFrequencyRange=_DocsDrfPhyParamFrequencyRange_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,1,1,4))
if mibBuilder.loadTexts:docsDrfPhyParamFrequencyRange.setStatus(_A)
_DocsDrfDownstreamTable_Object=MibTable
docsDrfDownstreamTable=_DocsDrfDownstreamTable_Object((1,3,6,1,4,1,4491,2,1,23,1,2))
if mibBuilder.loadTexts:docsDrfDownstreamTable.setStatus(_A)
_DocsDrfDownstreamEntry_Object=MibTableRow
docsDrfDownstreamEntry=_DocsDrfDownstreamEntry_Object((1,3,6,1,4,1,4491,2,1,23,1,2,1))
if mibBuilder.loadTexts:docsDrfDownstreamEntry.setStatus(_A)
class _DocsDrfDownstreamPhyDependencies_Type(Bits):namedValues=NamedValues(*((_M,0),(_N,1),('power',2),(_O,3),('interleaver',4),('j83Annex',5),(_P,6),('mute',7)))
_DocsDrfDownstreamPhyDependencies_Type.__name__=_D
_DocsDrfDownstreamPhyDependencies_Object=MibTableColumn
docsDrfDownstreamPhyDependencies=_DocsDrfDownstreamPhyDependencies_Object((1,3,6,1,4,1,4491,2,1,23,1,2,1,1),_DocsDrfDownstreamPhyDependencies_Type())
docsDrfDownstreamPhyDependencies.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamPhyDependencies.setStatus(_A)
_DocsDrfDownstreamCapabilitiesTable_Object=MibTable
docsDrfDownstreamCapabilitiesTable=_DocsDrfDownstreamCapabilitiesTable_Object((1,3,6,1,4,1,4491,2,1,23,1,3))
if mibBuilder.loadTexts:docsDrfDownstreamCapabilitiesTable.setStatus(_A)
_DocsDrfDownstreamCapabilitiesEntry_Object=MibTableRow
docsDrfDownstreamCapabilitiesEntry=_DocsDrfDownstreamCapabilitiesEntry_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1))
docsDrfDownstreamCapabilitiesEntry.setIndexNames((0,_J,_K))
if mibBuilder.loadTexts:docsDrfDownstreamCapabilitiesEntry.setStatus(_A)
class _DocsDrfDownstreamCapabFrequency_Type(Bits):namedValues=NamedValues(*((_E,0),('adjacentChannel',1),('adjacentChannelOrder',2)))
_DocsDrfDownstreamCapabFrequency_Type.__name__=_D
_DocsDrfDownstreamCapabFrequency_Object=MibTableColumn
docsDrfDownstreamCapabFrequency=_DocsDrfDownstreamCapabFrequency_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,1),_DocsDrfDownstreamCapabFrequency_Type())
docsDrfDownstreamCapabFrequency.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabFrequency.setStatus(_A)
class _DocsDrfDownstreamCapabBandwidth_Type(Bits):namedValues=NamedValues(*((_E,0),('chan6Mhz',1),('chan8Mhz',2)))
_DocsDrfDownstreamCapabBandwidth_Type.__name__=_D
_DocsDrfDownstreamCapabBandwidth_Object=MibTableColumn
docsDrfDownstreamCapabBandwidth=_DocsDrfDownstreamCapabBandwidth_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,2),_DocsDrfDownstreamCapabBandwidth_Type())
docsDrfDownstreamCapabBandwidth.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabBandwidth.setStatus(_A)
class _DocsDrfDownstreamCapabPower_Type(Bits):namedValues=NamedValues((_E,0))
_DocsDrfDownstreamCapabPower_Type.__name__=_D
_DocsDrfDownstreamCapabPower_Object=MibTableColumn
docsDrfDownstreamCapabPower=_DocsDrfDownstreamCapabPower_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,3),_DocsDrfDownstreamCapabPower_Type())
docsDrfDownstreamCapabPower.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabPower.setStatus(_A)
class _DocsDrfDownstreamCapabModulation_Type(Bits):namedValues=NamedValues(*((_E,0),('qam64',1),('qam256',2)))
_DocsDrfDownstreamCapabModulation_Type.__name__=_D
_DocsDrfDownstreamCapabModulation_Object=MibTableColumn
docsDrfDownstreamCapabModulation=_DocsDrfDownstreamCapabModulation_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,4),_DocsDrfDownstreamCapabModulation_Type())
docsDrfDownstreamCapabModulation.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabModulation.setStatus(_A)
class _DocsDrfDownstreamCapabInterleaver_Type(Bits):namedValues=NamedValues(*((_E,0),('taps8Increment16',1),('taps16Increment8',2),('taps32Increment4',3),('taps64Increment2',4),('taps128Increment1',5),('taps12increment17',6),('taps128increment2',7),('taps128increment3',8),('taps128increment4',9),('taps128increment5',10),('taps128increment6',11),('taps128increment7',12),('taps128increment8',13)))
_DocsDrfDownstreamCapabInterleaver_Type.__name__=_D
_DocsDrfDownstreamCapabInterleaver_Object=MibTableColumn
docsDrfDownstreamCapabInterleaver=_DocsDrfDownstreamCapabInterleaver_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,5),_DocsDrfDownstreamCapabInterleaver_Type())
docsDrfDownstreamCapabInterleaver.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabInterleaver.setStatus(_A)
class _DocsDrfDownstreamCapabJ83Annex_Type(Bits):namedValues=NamedValues(*((_E,0),('annexA',1),('annexB',2),('annexC',3)))
_DocsDrfDownstreamCapabJ83Annex_Type.__name__=_D
_DocsDrfDownstreamCapabJ83Annex_Object=MibTableColumn
docsDrfDownstreamCapabJ83Annex=_DocsDrfDownstreamCapabJ83Annex_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,6),_DocsDrfDownstreamCapabJ83Annex_Type())
docsDrfDownstreamCapabJ83Annex.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabJ83Annex.setStatus(_A)
class _DocsDrfDownstreamCapabConcurrentServices_Type(Bits):namedValues=NamedValues(*((_E,0),('videoAndDocsis',1)))
_DocsDrfDownstreamCapabConcurrentServices_Type.__name__=_D
_DocsDrfDownstreamCapabConcurrentServices_Object=MibTableColumn
docsDrfDownstreamCapabConcurrentServices=_DocsDrfDownstreamCapabConcurrentServices_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,7),_DocsDrfDownstreamCapabConcurrentServices_Type())
docsDrfDownstreamCapabConcurrentServices.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabConcurrentServices.setStatus(_A)
class _DocsDrfDownstreamCapabServicesTransport_Type(Bits):namedValues=NamedValues(*((_E,0),('mpeg2OverIP',1),('dmpt',2),('psp',3)))
_DocsDrfDownstreamCapabServicesTransport_Type.__name__=_D
_DocsDrfDownstreamCapabServicesTransport_Object=MibTableColumn
docsDrfDownstreamCapabServicesTransport=_DocsDrfDownstreamCapabServicesTransport_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,8),_DocsDrfDownstreamCapabServicesTransport_Type())
docsDrfDownstreamCapabServicesTransport.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabServicesTransport.setStatus(_A)
class _DocsDrfDownstreamCapabMuting_Type(Bits):namedValues=NamedValues((_E,0))
_DocsDrfDownstreamCapabMuting_Type.__name__=_D
_DocsDrfDownstreamCapabMuting_Object=MibTableColumn
docsDrfDownstreamCapabMuting=_DocsDrfDownstreamCapabMuting_Object((1,3,6,1,4,1,4491,2,1,23,1,3,1,9),_DocsDrfDownstreamCapabMuting_Type())
docsDrfDownstreamCapabMuting.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfDownstreamCapabMuting.setStatus(_A)
_DocsDrfGroupDependencyTable_Object=MibTable
docsDrfGroupDependencyTable=_DocsDrfGroupDependencyTable_Object((1,3,6,1,4,1,4491,2,1,23,1,4))
if mibBuilder.loadTexts:docsDrfGroupDependencyTable.setStatus(_A)
_DocsDrfGroupDependencyEntry_Object=MibTableRow
docsDrfGroupDependencyEntry=_DocsDrfGroupDependencyEntry_Object((1,3,6,1,4,1,4491,2,1,23,1,4,1))
docsDrfGroupDependencyEntry.setIndexNames((0,_B,_Q),(0,_B,_R))
if mibBuilder.loadTexts:docsDrfGroupDependencyEntry.setStatus(_A)
class _DocsDrfGroupDependencyPhyParam_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noDependencies',0),('all',1),(_M,2),(_N,3),('power',4),(_O,5),('interleave',6),('annex',7),(_P,8),('mute',9)))
_DocsDrfGroupDependencyPhyParam_Type.__name__=_F
_DocsDrfGroupDependencyPhyParam_Object=MibTableColumn
docsDrfGroupDependencyPhyParam=_DocsDrfGroupDependencyPhyParam_Object((1,3,6,1,4,1,4491,2,1,23,1,4,1,1),_DocsDrfGroupDependencyPhyParam_Type())
docsDrfGroupDependencyPhyParam.setMaxAccess(_G)
if mibBuilder.loadTexts:docsDrfGroupDependencyPhyParam.setStatus(_A)
_DocsDrfGroupDependencyPhysicalIndex_Type=PhysicalIndexOrZero
_DocsDrfGroupDependencyPhysicalIndex_Object=MibTableColumn
docsDrfGroupDependencyPhysicalIndex=_DocsDrfGroupDependencyPhysicalIndex_Object((1,3,6,1,4,1,4491,2,1,23,1,4,1,2),_DocsDrfGroupDependencyPhysicalIndex_Type())
docsDrfGroupDependencyPhysicalIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:docsDrfGroupDependencyPhysicalIndex.setStatus(_A)
class _DocsDrfGroupDependencyGroupID_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,127))
_DocsDrfGroupDependencyGroupID_Type.__name__=_L
_DocsDrfGroupDependencyGroupID_Object=MibTableColumn
docsDrfGroupDependencyGroupID=_DocsDrfGroupDependencyGroupID_Object((1,3,6,1,4,1,4491,2,1,23,1,4,1,3),_DocsDrfGroupDependencyGroupID_Type())
docsDrfGroupDependencyGroupID.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfGroupDependencyGroupID.setStatus(_A)
_DocsDrfGroupDependencyType_Type=AutonomousType
_DocsDrfGroupDependencyType_Object=MibTableColumn
docsDrfGroupDependencyType=_DocsDrfGroupDependencyType_Object((1,3,6,1,4,1,4491,2,1,23,1,4,1,4),_DocsDrfGroupDependencyType_Type())
docsDrfGroupDependencyType.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfGroupDependencyType.setStatus(_A)
_DocsDrfChannelBlockTable_Object=MibTable
docsDrfChannelBlockTable=_DocsDrfChannelBlockTable_Object((1,3,6,1,4,1,4491,2,1,23,1,5))
if mibBuilder.loadTexts:docsDrfChannelBlockTable.setStatus(_A)
_DocsDrfChannelBlockEntry_Object=MibTableRow
docsDrfChannelBlockEntry=_DocsDrfChannelBlockEntry_Object((1,3,6,1,4,1,4491,2,1,23,1,5,1))
docsDrfChannelBlockEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:docsDrfChannelBlockEntry.setStatus(_A)
_DocsDrfChannelBlockPhysicalIndex_Type=PhysicalIndex
_DocsDrfChannelBlockPhysicalIndex_Object=MibTableColumn
docsDrfChannelBlockPhysicalIndex=_DocsDrfChannelBlockPhysicalIndex_Object((1,3,6,1,4,1,4491,2,1,23,1,5,1,1),_DocsDrfChannelBlockPhysicalIndex_Type())
docsDrfChannelBlockPhysicalIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:docsDrfChannelBlockPhysicalIndex.setStatus(_A)
_DocsDrfChannelBlockNumberChannels_Type=Unsigned32
_DocsDrfChannelBlockNumberChannels_Object=MibTableColumn
docsDrfChannelBlockNumberChannels=_DocsDrfChannelBlockNumberChannels_Object((1,3,6,1,4,1,4491,2,1,23,1,5,1,2),_DocsDrfChannelBlockNumberChannels_Type())
docsDrfChannelBlockNumberChannels.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfChannelBlockNumberChannels.setStatus(_A)
_DocsDrfChannelBlockCfgNumberChannels_Type=Unsigned32
_DocsDrfChannelBlockCfgNumberChannels_Object=MibTableColumn
docsDrfChannelBlockCfgNumberChannels=_DocsDrfChannelBlockCfgNumberChannels_Object((1,3,6,1,4,1,4491,2,1,23,1,5,1,3),_DocsDrfChannelBlockCfgNumberChannels_Type())
docsDrfChannelBlockCfgNumberChannels.setMaxAccess(_H)
if mibBuilder.loadTexts:docsDrfChannelBlockCfgNumberChannels.setStatus(_A)
_DocsDrfChannelBlockMute_Type=TruthValue
_DocsDrfChannelBlockMute_Object=MibTableColumn
docsDrfChannelBlockMute=_DocsDrfChannelBlockMute_Object((1,3,6,1,4,1,4491,2,1,23,1,5,1,4),_DocsDrfChannelBlockMute_Type())
docsDrfChannelBlockMute.setMaxAccess(_H)
if mibBuilder.loadTexts:docsDrfChannelBlockMute.setStatus(_A)
class _DocsDrfChannelBlockTestType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('noTest',1),('offOthersNormal',2),('allOff',3),('onOthersOff',4),('cwOnOthersOff',5),('cwOnOthersNormal',6),('clockTest',7)))
_DocsDrfChannelBlockTestType_Type.__name__=_F
_DocsDrfChannelBlockTestType_Object=MibTableColumn
docsDrfChannelBlockTestType=_DocsDrfChannelBlockTestType_Object((1,3,6,1,4,1,4491,2,1,23,1,5,1,5),_DocsDrfChannelBlockTestType_Type())
docsDrfChannelBlockTestType.setMaxAccess(_C)
if mibBuilder.loadTexts:docsDrfChannelBlockTestType.setStatus(_A)
_DocsDrfChannelBlockTestIfIndex_Type=InterfaceIndexOrZero
_DocsDrfChannelBlockTestIfIndex_Object=MibTableColumn
docsDrfChannelBlockTestIfIndex=_DocsDrfChannelBlockTestIfIndex_Object((1,3,6,1,4,1,4491,2,1,23,1,5,1,6),_DocsDrfChannelBlockTestIfIndex_Type())
docsDrfChannelBlockTestIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:docsDrfChannelBlockTestIfIndex.setStatus(_A)
_DocsDrfConformance_ObjectIdentity=ObjectIdentity
docsDrfConformance=_DocsDrfConformance_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,2))
_DocsDrfCompliances_ObjectIdentity=ObjectIdentity
docsDrfCompliances=_DocsDrfCompliances_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,2,1))
_DocsDrfGroups_ObjectIdentity=ObjectIdentity
docsDrfGroups=_DocsDrfGroups_ObjectIdentity((1,3,6,1,4,1,4491,2,1,23,2,2))
docsIfDownstreamChannelEntry.registerAugmentions((_B,_T))
docsDrfDownstreamEntry.setIndexNames(*docsIfDownstreamChannelEntry.getIndexNames())
docsDrfGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,23,2,2,1))
docsDrfGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j)))
if mibBuilder.loadTexts:docsDrfGroup.setStatus(_A)
docsDrfCmtsGroup=ObjectGroup((1,3,6,1,4,1,4491,2,1,23,2,2,2))
docsDrfCmtsGroup.setObjects((_B,_k))
if mibBuilder.loadTexts:docsDrfCmtsGroup.setStatus(_A)
docsDrfDeviceCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,1,23,2,1,1))
docsDrfDeviceCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:docsDrfDeviceCompliance.setStatus(_A)
docsDrfCmtsCompliance=ModuleCompliance((1,3,6,1,4,1,4491,2,1,23,2,1,2))
docsDrfCmtsCompliance.setObjects(*((_B,_I),(_B,_l)))
if mibBuilder.loadTexts:docsDrfCmtsCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'docsDrfMib':docsDrfMib,'docsDrfNotifications':docsDrfNotifications,'docsDrfObjects':docsDrfObjects,'docsDrfRegistry':docsDrfRegistry,'docsDrfPhyParamFixValue':docsDrfPhyParamFixValue,'docsDrfPhyParamSameValue':docsDrfPhyParamSameValue,'docsDrfPhyParamAdjacentValues':docsDrfPhyParamAdjacentValues,'docsDrfPhyParamFrequencyRange':docsDrfPhyParamFrequencyRange,'docsDrfDownstreamTable':docsDrfDownstreamTable,_T:docsDrfDownstreamEntry,_k:docsDrfDownstreamPhyDependencies,'docsDrfDownstreamCapabilitiesTable':docsDrfDownstreamCapabilitiesTable,'docsDrfDownstreamCapabilitiesEntry':docsDrfDownstreamCapabilitiesEntry,_U:docsDrfDownstreamCapabFrequency,_V:docsDrfDownstreamCapabBandwidth,_W:docsDrfDownstreamCapabPower,_X:docsDrfDownstreamCapabModulation,_Y:docsDrfDownstreamCapabInterleaver,_Z:docsDrfDownstreamCapabJ83Annex,_a:docsDrfDownstreamCapabConcurrentServices,_b:docsDrfDownstreamCapabServicesTransport,_c:docsDrfDownstreamCapabMuting,'docsDrfGroupDependencyTable':docsDrfGroupDependencyTable,'docsDrfGroupDependencyEntry':docsDrfGroupDependencyEntry,_Q:docsDrfGroupDependencyPhyParam,_R:docsDrfGroupDependencyPhysicalIndex,_d:docsDrfGroupDependencyGroupID,_e:docsDrfGroupDependencyType,'docsDrfChannelBlockTable':docsDrfChannelBlockTable,'docsDrfChannelBlockEntry':docsDrfChannelBlockEntry,_S:docsDrfChannelBlockPhysicalIndex,_f:docsDrfChannelBlockNumberChannels,_g:docsDrfChannelBlockCfgNumberChannels,_h:docsDrfChannelBlockMute,_i:docsDrfChannelBlockTestType,_j:docsDrfChannelBlockTestIfIndex,'docsDrfConformance':docsDrfConformance,'docsDrfCompliances':docsDrfCompliances,'docsDrfDeviceCompliance':docsDrfDeviceCompliance,'docsDrfCmtsCompliance':docsDrfCmtsCompliance,'docsDrfGroups':docsDrfGroups,_I:docsDrfGroup,_l:docsDrfCmtsGroup})